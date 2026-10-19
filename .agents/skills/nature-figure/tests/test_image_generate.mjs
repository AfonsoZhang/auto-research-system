import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {loadConfig, validateJob, budget, generate} from '../scripts/image_generate.mjs';

const cfg = {base_url: 'https://x.example/v1', models: ['m1'], download_hosts: []};
const job = (o = {}) => ({model: 'm1', calls: 2, prompt_file: 'p.txt', budget_cap: 1,
  quote: {cost_per_call_upper: 0.3, source: 'pricing page', assumptions: 'one image', checked_at: new Date().toISOString()}, ...o});

test('config requires an approved model list', () => {
  const d = fs.mkdtempSync(path.join(os.tmpdir(), 'img-'));
  fs.writeFileSync(path.join(d, 'c.json'), JSON.stringify({base_url: 'https://x/v1', models: []}));
  assert.throws(() => loadConfig({IMAGE_PROVIDER_CONFIG: path.join(d, 'c.json')}), /models/);
});

test('rejects unapproved model, stale quote and missing cap', () => {
  assert.throws(() => validateJob(job({model: 'other'}), cfg), /user-approved/);
  assert.throws(() => validateJob(job({quote: {...job().quote, checked_at: '2000-01-01T00:00:00Z'}}), cfg), /Refresh/);
  assert.throws(() => validateJob(job({budget_cap: undefined}), cfg), /budget_cap/);
});

test('budget compares the whole batch with the cap', () => {
  assert.equal(budget(job()).within_cap, true);
  assert.equal(budget(job({budget_cap: 0.5})).within_cap, false);
});

test('charged POST is never retried', async () => {
  let calls = 0;
  const flaky = async () => { calls++; return {ok: false, status: 503}; };
  await assert.rejects(generate(cfg, {}, flaky), /no automatic retry/);
  assert.equal(calls, 1);
});
