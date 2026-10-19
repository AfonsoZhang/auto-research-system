#!/usr/bin/env node
// Poe images only. Node >=18, no SDK dependencies. Never retry a charged POST.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';

// Approved models come from the image-provider config when present (see image-generation.md).
function configuredModels() {
  const root = process.env.RESEARCH_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../..');
  const p = process.env.IMAGE_PROVIDER_CONFIG || path.join(root, '.tools/image-provider.json');
  try { const m = JSON.parse(fs.readFileSync(p, 'utf8')).models; if (Array.isArray(m) && m.length) return m; } catch {}
  return ['nano-banana-2', 'nano-banana-pro', 'gpt-image-2'];
}
export const MODELS = configuredModels();
const API = 'https://api.poe.com';
const json = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const save = (p, v) => fs.writeFileSync(p, JSON.stringify(v, null, 2) + '\n', {flag: 'wx', mode: 0o600});
const emit = v => console.log(JSON.stringify(v));
function fail(message) { throw new Error(message); }

export function validateJob(job, now = Date.now()) {
  if (!MODELS.includes(job.model)) fail('Model is not in the configured, user-approved list.');
  if (!Number.isSafeInteger(job.calls) || job.calls < 1 || job.calls > 20) fail('calls must be 1..20.');
  if (typeof job.prompt_file !== 'string' || !job.prompt_file) fail('prompt_file is required.');
  if (job.references !== undefined && (!Array.isArray(job.references) || job.references.some(x => typeof x !== 'string'))) fail('references must be local image paths.');
  const q = job.quote;
  if (!q || !Number.isSafeInteger(q.points_per_call_upper) || q.points_per_call_upper <= 0 || !q.source?.trim() || !q.assumptions?.trim()) fail('A sourced point estimate with assumptions is required; pricing is unverified.');
  const age = now - Date.parse(q.checked_at);
  if (!Number.isFinite(age) || age < -300000 || age > 86400000) fail('Refresh the quote: checked_at must be within the last 24 hours.');
  if (!Number.isSafeInteger(q.points_per_call_upper * job.calls)) fail('Invalid total point estimate.');
  const p = job.parameters || {};
  if (typeof p !== 'object' || Array.isArray(p)) fail('parameters must be an object.');
  const allowed = job.model === 'gpt-image-2' ? ['size','quality','use_mask'] : ['aspect_ratio','image_size','image_only'];
  if (Object.keys(p).some(k => !allowed.includes(k))) fail('Unverified parameter or non-image capability requested.');
  if (Object.keys(p).length && !job.parameters_source?.trim()) fail('parameters_source is required for model-specific parameters.');
  if(job.model==='gpt-image-2') {
    if(p.size!==undefined && !['auto','1024x1024','1536x1024','1024x1536'].includes(p.size))fail('Unsupported GPT Image 2 size.');
    if(p.quality!==undefined && !['low','medium','high'].includes(p.quality))fail('Unsupported GPT Image 2 quality.');
    if(p.use_mask!==undefined && typeof p.use_mask!=='boolean')fail('use_mask must be boolean.');
    if(p.use_mask && (job.references||[]).length<2)fail('Mask editing requires a base image followed by a mask.');
  } else {
    if(p.image_size!==undefined && !['1K','2K','4K'].includes(p.image_size))fail('Unsupported Nano Banana resolution.');
    if(p.image_only!==undefined && typeof p.image_only!=='boolean')fail('image_only must be boolean.');
    if(p.aspect_ratio!==undefined && !['1:1','2:3','3:2','3:4','4:3','4:5','5:4','9:16','16:9','21:9'].includes(p.aspect_ratio))fail('Unsupported aspect ratio.');
  }
  return job;
}

export function budget(balance, unit, calls) {
  if (!Number.isSafeInteger(balance) || balance < 0) fail('Balance unavailable or invalid; cannot assess sufficiency.');
  const estimated = unit * calls;
  return {balance_points: balance, estimated_points_upper: estimated,
    sufficient: balance >= estimated, estimated_shortfall: Math.max(0, estimated - balance),
    projected_remaining: balance - estimated};
}

function credential() {
  if (process.env.POE_API_KEY?.trim()) return process.env.POE_API_KEY.trim();
  const p = path.join(os.homedir(), '.local/share/opencode/auth.json');
  if (fs.existsSync(p)) {
    const entries = Object.entries(json(p)).filter(([k,v]) => /poe/i.test(k) && typeof v?.key === 'string' && v.key.trim());
    if (entries.length === 1) return entries[0][1].key.trim();
    if (entries.length > 1) fail('Multiple Poe credentials found; select one with POE_API_KEY.');
  }
  fail('Poe credential unavailable. Use existing OpenCode auth or POE_API_KEY.');
}

export function client(key, fetchImpl = fetch) {
  async function get(endpoint) {
    for(let attempt=0;attempt<3;attempt++) {
      let r;
      try {r = await fetchImpl(API + endpoint, {headers: {Authorization: `Bearer ${key}`}, redirect: 'error', signal: AbortSignal.timeout(15000)});}
      catch {if(attempt<2){await new Promise(resolve=>setTimeout(resolve,500));continue;}fail('Poe read-only connection failed; balance/usage unverified.');}
      if (!r.ok) {
        if ([429,500,502,503,504].includes(r.status) && attempt<2){await new Promise(resolve=>setTimeout(resolve,500));continue;}
        fail(`Poe read-only endpoint HTTP ${r.status}; balance/usage unverified.`);
      }
      return r.json();
    }
  }
  return {
    balance: async () => (await get('/usage/current_balance')).current_point_balance,
    history: () => get('/usage/points_history?limit=20'),
    generate: async payload => {
      let r;
      try {
        r = await fetchImpl(API + '/v1/chat/completions', {method: 'POST',
          headers: {Authorization: `Bearer ${key}`, 'Content-Type': 'application/json'},
          body: JSON.stringify(payload), redirect: 'error', signal: AbortSignal.timeout(300000)});
      } catch { fail('Generation connection failed: charge/outcome unknown. Do not retry automatically; check usage first.'); }
      if (r.status === 402) fail('Poe reports insufficient credits. 请充值后再继续。');
      if (!r.ok) fail(`Generation HTTP ${r.status}; no automatic retry. Check usage before resubmitting.`);
      return r.json();
    }
  };
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
  // OpenAI SDK extra_body is merged at the HTTP body top level, not nested.
  return {model:job.model, messages:[{role:'user',content}], stream:false, n:1, ...(job.parameters || {})};
}

export function imageSources(response) {
  const result = new Set();
  function scan(value) {
    if (typeof value === 'string') {
      if (/^data:image\/(png|jpeg|webp);base64,/.test(value) || /^https:\/\/\S+$/.test(value)) result.add(value);
      for (const m of value.matchAll(/!\[[^\]]*\]\(<?(https:\/\/[^\s)>]+)>?(?:\s+"[^"]*")?\)/g)) result.add(m[1]);
    } else if (Array.isArray(value)) value.forEach(scan);
    else if (value && typeof value === 'object') {
      for (const k of ['content','image_url','images','url']) if (k in value) scan(value[k]);
    }
  }
  for (const c of response.choices || []) scan(c.message);
  return [...result];
}

async function download(source) {
  const data = source.match(/^data:image\/(png|jpeg|webp);base64,([A-Za-z0-9+/=\r\n]+)$/);
  if (data) return Buffer.from(data[2], 'base64');
  let u = new URL(source);
  for (let i=0; i<4; i++) {
    const hosts = ['poecdn.net','quoracdn.net','storage.googleapis.com','fal.media','replicate.delivery','oaidalleapiprodscus.blob.core.windows.net','deep-inference-results.s3.amazonaws.com'];
    if (u.protocol !== 'https:' || u.username || u.password || (u.port && u.port !== '443') || !hosts.some(h=>u.hostname===h || u.hostname.endsWith('.'+h))) fail('Unrecognized image download host; inspect saved response before downloading.');
    // Never forward the Poe Authorization header to an image CDN.
    const r = await fetch(u, {redirect:'manual', signal:AbortSignal.timeout(60000)});
    if (r.status >= 300 && r.status < 400 && r.headers.get('location')) {u=new URL(r.headers.get('location'),u);continue;}
    if (!r.ok) fail(`Image download HTTP ${r.status}; use recover, do not regenerate.`);
    const chunks=[];let size=0;
    for await (const chunk of r.body) {size+=chunk.length;if(size>50*1024*1024) fail('Image exceeds 50 MiB.');chunks.push(chunk);}
    return Buffer.concat(chunks);
  }
  fail('Too many image redirects.');
}

function extension(b) {
  if(b.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])))return 'png';
  if(b[0]===255&&b[1]===216&&b[2]===255)return 'jpg';
  if(b.toString('ascii',0,4)==='RIFF'&&b.toString('ascii',8,12)==='WEBP')return 'webp';
  fail('Response is not a supported image; do not claim generation success.');
}

export async function saveImages(response, out) {
  const sources=imageSources(response);
  if (!sources.length) fail('No image found. Response saved for inspection; do not auto-regenerate.');
  const files=[];
  for (let i=0;i<sources.length;i++) {
    const b=await download(sources[i]);
    const p=path.join(out,`image-${i+1}.${extension(b)}`);
    fs.writeFileSync(p,b,{flag:'wx',mode:0o600});files.push(p);
  }
  return files;
}

export async function runBatch(job, request, api, hooks) {
  validateJob(job);
  for (let i=0;i<job.calls;i++) {
    const check=budget(await api.balance(),job.quote.points_per_call_upper,job.calls-i);
    hooks.report({call:i+1,model:job.model,...check});
    if (!check.sufficient) fail(`当前余额 ${check.balance_points} 点，剩余任务预计需要 ${check.estimated_points_upper} 点，预计缺口 ${check.estimated_shortfall} 点；请充值后再继续。`);
    const response=await api.generate(request);
    await hooks.result(i,response);
  }
}

async function main() {
  const [command,...args]=process.argv.slice(2), opt={};
  for(let i=0;i<args.length;i+=2){if(!args[i].startsWith('--')||!args[i+1])fail('Expected --option value.');opt[args[i].slice(2)]=args[i+1];}
  if(!command || command==='help') {console.log('poe_image.mjs balance | models | preflight --job job.json | generate --job job.json --out NEW_DIR | recover --response saved.json --out NEW_DIR');return;}
  if(command==='models') {
    const r=await fetch(API+'/v1/models',{signal:AbortSignal.timeout(30000)});if(!r.ok)fail(`Catalog HTTP ${r.status}`);
    emit((await r.json()).data.filter(m=>MODELS.includes(m.id.toLowerCase())).map(m=>({id:m.id,description:m.description,pricing:m.pricing})));
    return;
  }
  if(command==='recover') {if(!opt.response||!opt.out)fail('response and out required.');const d=json(opt.response);fs.mkdirSync(opt.out,{recursive:false});emit({files:await saveImages(d,opt.out)});return;}
  if(!['balance','preflight','generate'].includes(command))fail('Unknown command.');
  const api=client(credential());
  if(command==='balance'){emit({balance_points:await api.balance(),checked_at:new Date().toISOString()});return;}
  if(!opt.job)fail('--job required.');
  const job=validateJob(json(opt.job)), request=payload(job,path.dirname(path.resolve(opt.job)));
  if(command==='preflight') {
    const check=budget(await api.balance(),job.quote.points_per_call_upper,job.calls);
    emit({model:job.model,calls:job.calls,quote_source:job.quote.source,...check});
    if(!check.sufficient){console.error('余额不足，请充值后再继续。');process.exitCode=3;}return;
  }
  if(!opt.out)fail('--out NEW_DIR required.');
  fs.mkdirSync(opt.out,{recursive:false});
  save(path.join(opt.out,'job.json'),job);
  const summary=[];
  await runBatch(job,request,api,{
    report:emit,
    result:async(i,response)=>{
      const d=path.join(opt.out,`call-${i+1}`);fs.mkdirSync(d);
      save(path.join(d,'response.json'),response);
      const item={call:i+1,response_id:response.id,query_id:response.id?.replace(/^chatcmpl-/,''),status:'response_saved'};
      summary.push(item);save(path.join(d,'receipt.json'),item);
      item.files=await saveImages(response,d);item.status='images_saved';
      try{const h=await api.history();const matched=h.data?.find(x=>x.query_id===item.query_id);if(matched)item.actual_points=matched.cost_points;}catch{item.usage_status='unavailable';}
      save(path.join(d,'result.json'),item);emit(item);
    }
  });
  save(path.join(opt.out,'summary.json'),summary);
}
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  main().catch(e=>{console.error(e.message?.includes('Bearer')?'Request failed; inspect locally without exposing credentials.':e.message);process.exitCode=1;});
}
