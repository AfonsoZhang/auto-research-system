#!/usr/bin/env node
// Provider-neutral image generation through any OpenAI-compatible chat endpoint
// (an official API, a local server or a relay). Node >=18, no SDK dependencies.
// Never retry a charged POST. Poe users may prefer poe_image.mjs for its live balance check.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {imageSources} from './poe_image.mjs';

const json = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const save = (p, v) => fs.writeFileSync(p, JSON.stringify(v, null, 2) + '\n', {flag: 'wx', mode: 0o600});
const emit = v => console.log(JSON.stringify(v));
function fail(message) { throw new Error(message); }

// Config: IMAGE_PROVIDER_CONFIG, else $RESEARCH_ROOT/.tools/image-provider.json.
// {"base_url": "https://host/v1", "api_key_env": "NAME_OF_ENV_VAR", "models": ["..."],
//  "download_hosts": ["cdn.example.com"], "currency": "USD"}
export function loadConfig(env = process.env) {
  const root = env.RESEARCH_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../..');
  const p = env.IMAGE_PROVIDER_CONFIG || path.join(root, '.tools/image-provider.json');
  if (!fs.existsSync(p)) fail(`No image provider configured (${p}). Copy image-provider.example.json and fill it in.`);
  const c = json(p);
  if (!/^https?:\/\//.test(c.base_url || '')) fail('base_url must be an http(s) URL.');
  if (!Array.isArray(c.models) || !c.models.length || c.models.some(m => typeof m !== 'string' || !m.trim())) fail('models must list the image models the user approved.');
  return {...c, base_url: c.base_url.replace(/\/$/, ''), download_hosts: c.download_hosts || []};
}

export function validateJob(job, cfg, now = Date.now()) {
  if (!cfg.models.includes(job.model)) fail('Model is not in the configured, user-approved list.');
  if (!Number.isSafeInteger(job.calls) || job.calls < 1 || job.calls > 20) fail('calls must be 1..20.');
  if (typeof job.prompt_file !== 'string' || !job.prompt_file) fail('prompt_file is required.');
  if (job.references !== undefined && (!Array.isArray(job.references) || job.references.some(x => typeof x !== 'string'))) fail('references must be local image paths.');
  const q = job.quote;
  if (!q || typeof q.cost_per_call_upper !== 'number' || !(q.cost_per_call_upper > 0) || !q.source?.trim() || !q.assumptions?.trim()) fail('A sourced per-call cost estimate with assumptions is required; pricing is unverified.');
  const age = now - Date.parse(q.checked_at);
  if (!Number.isFinite(age) || age < -300000 || age > 86400000) fail('Refresh the quote: checked_at must be within the last 24 hours.');
  if (typeof job.budget_cap !== 'number' || !(job.budget_cap > 0)) fail('budget_cap (the user-authorized spend for this batch) is required.');
  const p = job.parameters || {};
  if (typeof p !== 'object' || Array.isArray(p)) fail('parameters must be an object.');
  if (Object.keys(p).length && !job.parameters_source?.trim()) fail('parameters_source is required for model-specific parameters.');
  return job;
}

export function budget(job) {
  const estimated = job.quote.cost_per_call_upper * job.calls;
  return {estimated_cost_upper: estimated, budget_cap: job.budget_cap,
    within_cap: estimated <= job.budget_cap, estimated_excess: Math.max(0, estimated - job.budget_cap)};
}

function payload(job, dir) {
  const prompt = fs.readFileSync(path.resolve(dir, job.prompt_file), 'utf8').trim();
  if (!prompt) fail('Empty prompt.');
  const content = [{type: 'text', text: prompt + '\nGenerate exactly one image.'}];
  for (const name of job.references || []) {
    const p = path.resolve(dir, name), ext = path.extname(p).toLowerCase();
    const mime = {'.png':'image/png', '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.webp':'image/webp'}[ext];
    if (!mime || fs.statSync(p).size > 20 * 1024 * 1024) fail('Reference must be PNG/JPEG/WebP, at most 20 MiB.');
    content.push({type:'image_url', image_url:{url:`data:${mime};base64,${fs.readFileSync(p).toString('base64')}`}});
  }
  return {model:job.model, messages:[{role:'user',content}], stream:false, n:1, ...(job.parameters || {})};
}

export async function generate(cfg, body, fetchImpl = fetch) {
  const key = cfg.api_key_env ? process.env[cfg.api_key_env]?.trim() : '';
  if (cfg.api_key_env && !key) fail(`Set ${cfg.api_key_env} with the provider key.`);
  let r;
  try {
    r = await fetchImpl(cfg.base_url + '/chat/completions', {method: 'POST',
      headers: {...(key ? {Authorization: `Bearer ${key}`} : {}), 'Content-Type': 'application/json'},
      body: JSON.stringify(body), redirect: 'error', signal: AbortSignal.timeout(300000)});
  } catch { fail('Generation connection failed: charge/outcome unknown. Do not retry automatically; check provider usage first.'); }
  if (r.status === 402) fail('Provider reports insufficient credits.');
  if (!r.ok) fail(`Generation HTTP ${r.status}; no automatic retry. Check provider usage before resubmitting.`);
  return r.json();
}

async function download(source, hosts) {
  const data = source.match(/^data:image\/(png|jpeg|webp);base64,([A-Za-z0-9+/=\r\n]+)$/);
  if (data) return Buffer.from(data[2], 'base64');
  let u = new URL(source);
  for (let i = 0; i < 4; i++) {
    if (u.protocol !== 'https:' || u.username || u.password || (u.port && u.port !== '443') || !hosts.some(h => u.hostname === h || u.hostname.endsWith('.' + h))) fail('Image host is not in download_hosts; inspect the saved response before downloading.');
    // Never forward the provider Authorization header to an image CDN.
    const r = await fetch(u, {redirect:'manual', signal:AbortSignal.timeout(60000)});
    if (r.status >= 300 && r.status < 400 && r.headers.get('location')) {u = new URL(r.headers.get('location'), u); continue;}
    if (!r.ok) fail(`Image download HTTP ${r.status}; use recover, do not regenerate.`);
    const chunks = []; let size = 0;
    for await (const chunk of r.body) {size += chunk.length; if (size > 50*1024*1024) fail('Image exceeds 50 MiB.'); chunks.push(chunk);}
    return Buffer.concat(chunks);
  }
  fail('Too many image redirects.');
}

function extension(b) {
  if (b.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]))) return 'png';
  if (b[0]===255 && b[1]===216 && b[2]===255) return 'jpg';
  if (b.toString('ascii',0,4)==='RIFF' && b.toString('ascii',8,12)==='WEBP') return 'webp';
  fail('Response is not a supported image; do not claim generation success.');
}

async function saveImages(response, out, hosts) {
  const sources = imageSources(response);
  if (!sources.length) fail('No image found. Response saved for inspection; do not auto-regenerate.');
  const files = [];
  for (let i = 0; i < sources.length; i++) {
    const b = await download(sources[i], hosts);
    const p = path.join(out, `image-${i+1}.${extension(b)}`);
    fs.writeFileSync(p, b, {flag:'wx', mode:0o600}); files.push(p);
  }
  return files;
}

async function main() {
  const [command, ...args] = process.argv.slice(2), opt = {};
  for (let i = 0; i < args.length; i += 2) {if (!args[i].startsWith('--') || !args[i+1]) fail('Expected --option value.'); opt[args[i].slice(2)] = args[i+1];}
  if (!command || command === 'help') {console.log('image_generate.mjs preflight --job job.json | generate --job job.json --out NEW_DIR | recover --response saved.json --out NEW_DIR'); return;}
  const cfg = loadConfig();
  if (command === 'recover') {if (!opt.response || !opt.out) fail('response and out required.'); fs.mkdirSync(opt.out, {recursive:false}); emit({files: await saveImages(json(opt.response), opt.out, cfg.download_hosts)}); return;}
  if (!['preflight','generate'].includes(command)) fail('Unknown command.');
  if (!opt.job) fail('--job required.');
  const job = validateJob(json(opt.job), cfg), request = payload(job, path.dirname(path.resolve(opt.job)));
  const check = budget(job);
  emit({model: job.model, calls: job.calls, currency: cfg.currency || 'unspecified', quote_source: job.quote.source, ...check});
  if (!check.within_cap) {console.error('Estimated cost exceeds the authorized budget_cap; ask the user before spending more.'); process.exitCode = 3; return;}
  if (command === 'preflight') return;
  if (!opt.out) fail('--out NEW_DIR required.');
  fs.mkdirSync(opt.out, {recursive:false});
  save(path.join(opt.out, 'job.json'), job);
  const summary = [];
  for (let i = 0; i < job.calls; i++) {
    const response = await generate(cfg, request);
    const d = path.join(opt.out, `call-${i+1}`); fs.mkdirSync(d);
    save(path.join(d, 'response.json'), response);
    const item = {call: i+1, response_id: response.id, status: 'response_saved', usage: response.usage};
    summary.push(item);
    item.files = await saveImages(response, d, cfg.download_hosts); item.status = 'images_saved';
    save(path.join(d, 'result.json'), item); emit(item);
  }
  save(path.join(opt.out, 'summary.json'), summary);
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(e => {console.error(e.message?.includes('Bearer') ? 'Request failed; inspect locally without exposing credentials.' : e.message); process.exitCode = 1;});
}
