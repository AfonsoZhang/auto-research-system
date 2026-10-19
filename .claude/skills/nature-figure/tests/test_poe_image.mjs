import test from 'node:test';
import assert from 'node:assert/strict';
// Isolate from the user's local provider config: fall back to the built-in model list.
process.env.IMAGE_PROVIDER_CONFIG = '/nonexistent/image-provider.json';
const {validateJob,budget,runBatch,client,imageSources} = await import('../scripts/poe_image.mjs');

function job(calls=1) {return {model:'nano-banana-2',calls,prompt_file:'prompt.txt',quote:{points_per_call_upper:100,source:'test fixture, not a live quote',assumptions:'one image',checked_at:new Date().toISOString()}};}

test('insufficient balance prevents every paid request',async()=>{
  let charged=0;
  await assert.rejects(runBatch(job(),{}, {balance:async()=>99,generate:async()=>{charged++;}}, {report:()=>{},result:()=>{}}),/充值/);
  assert.equal(charged,0);
});
test('balance is checked again before the next batch request',async()=>{
  let charged=0,reads=0;
  const j=job(2);
  await assert.rejects(runBatch(j,{}, {balance:async()=>++reads===1?200:0,generate:async()=>{charged++;return {};}}, {report:()=>{},result:()=>{}}),/充值/);
  assert.equal(charged,1);assert.equal(reads,2);
});
test('unknown balance is not reported as insufficient',()=>{
  assert.throws(()=>budget(undefined,100,1),/cannot assess/);
});
test('missing, zero and stale estimates cannot generate',async()=>{
  for(const quote of [undefined,{...job().quote,points_per_call_upper:0},{...job().quote,checked_at:'2000-01-01T00:00:00Z'}]){
    let requests=0;
    await assert.rejects(runBatch({...job(),quote},{},{balance:async()=>{requests++;return 1000;},generate:async()=>{requests++;}},{report:()=>{},result:()=>{}}));
    assert.equal(requests,0);
  }
});
test('text models and reserved HTTP fields cannot bypass image-only routing',()=>{
  assert.throws(()=>validateJob({...job(),model:'Claude-Sonnet-4.6'}));
  for(const parameters of [{model:'other'},{messages:[]},{web_search:true}])assert.throws(()=>validateJob({...job(),parameters,parameters_source:'test'}));
  assert.doesNotThrow(()=>validateJob({...job(),model:'gpt-image-2',parameters:{size:'1536x1024',quality:'medium'},parameters_source:'verified bot controls'}));
  assert.throws(()=>validateJob({...job(),model:'gpt-image-2',parameters:{aspect_ratio:'3:2'},parameters_source:'wrong field'}));
  assert.throws(()=>validateJob({...job(),model:'gpt-image-2',parameters:{use_mask:true},parameters_source:'test'}));
});
test('connection failure never retries paid POST and does not expose key',async()=>{
  let calls=0;
  const api=client('TEST-SECRET',async()=>{calls++;throw Error('TEST-SECRET');});
  await assert.rejects(api.generate({}),e=>/unknown/.test(e.message)&&!e.message.includes('TEST-SECRET'));
  assert.equal(calls,1);
});
test('HTTP errors never retry paid POST',async()=>{
  for(const status of [402,429,500]){
    let calls=0;
    await assert.rejects(client('TEST',async()=>{calls++;return {ok:false,status};}).generate({}));
    assert.equal(calls,1);
  }
});
test('saved response handling failure does not trigger regeneration',async()=>{
  let calls=0;
  await assert.rejects(runBatch(job(2),{}, {balance:async()=>1000,generate:async()=>{calls++;return {};}},{report:()=>{},result:()=>{throw Error('download failed');}}));
  assert.equal(calls,1);
});
test('Poe markdown and multimodal image outputs are extracted, prose is not',()=>{
  const url='https://pfst.cf2.poecdn.net/image.png';
  assert.deepEqual(imageSources({choices:[{message:{content:`![image](${url})`}}]}),[url]);
  assert.deepEqual(imageSources({choices:[{message:{content:[{type:'image_url',image_url:{url}}]}}]}),[url]);
  assert.deepEqual(imageSources({choices:[{message:{content:'Unable to generate an image.'}}]}),[]);
});
