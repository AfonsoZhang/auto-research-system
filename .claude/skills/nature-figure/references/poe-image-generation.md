# Poe adapter: generation and point-budget check

Use this adapter when the configured image provider is Poe (see
[image-generation.md](image-generation.md)). It adds a live point-balance check
to the shared rules. Planning alone costs no generation points and can proceed
without account access.

## Scope: image generation only

Within this figure workflow, Poe is only for generating or editing images.
Do not call Poe text or vision-understanding models for planning, reviewing,
scientific judgment, or quality assurance. Balance, pricing, and usage queries
remain part of the required generation budget check.

Use nature-figure as the unified entry point, choose tools by figure type,
then inspect the rendered output and revise with the corresponding tool.
The main agent owns planning, tool selection, visual/scientific inspection,
and final acceptance; local tools handle measurable checks such as alignment,
font size, and collisions. Do not add a review-only subagent to this workflow.

## Figure language

Use English for generated figure labels and annotations by default. Do not
produce an additional Chinese or bilingual version unless explicitly requested.
State the label language when preparing generation/edit prompts, and preserve
canonical names and mathematical notation. Do not add a translation round or
budget for a Chinese duplicate. Keep progress and preflight notes in English;
use Chinese for the final user report under the shared
[working-language policy](../../shared-references/research-autonomy.md#working-language).

## Model selection

Choose from the configured `models` list. If the configuration records a default
or a task-based order, follow it; otherwise propose one model and state it in the
budget preflight. Honor an explicit task model choice first. Keep a satisfactory
model through subsequent iterations; do not run every model or escalate through
them on each figure. Recheck pricing and balance before any switch, and do not
switch to fit insufficient points instead of reporting the shortfall.

## Before every generation or edit batch

1. Identify the exact Poe bot, image count, resolution/quality, reference images,
   and requested edit rounds. Use an existing task choice or the approved defaults above; do not silently
   substitute a model. Bound the planned calls and retries.
2. Check the bot's current price for those parameters and the access method
   actually being used. Do not hardcode a universal points-per-image price or
   assume a web subscription gives unlimited API use. For variable pricing,
   report an estimated range and its assumptions, including relevant input and
   output costs. Estimate the entire requested batch, including planned edits.
3. Obtain a fresh balance through an available authenticated Poe interface.
   The official Usage API uses `Authorization: Bearer <Poe API key>`:
   - `GET https://api.poe.com/usage/current_balance`
   - Read `current_point_balance` (plan plus add-on points).
   An authenticated account page or a current user-provided balance/pricing
   can be used when API access is unavailable. Identify the source; never
   describe user-provided numbers as a live automated check. Never print keys.
4. Show a brief preflight: bot, planned calls/images, estimated points/range,
   current balance, and projected remaining points. Compare the balance with
   the estimated upper end when cost is variable. Any added contingency is a
   clearly labelled local estimate, not a Poe fee or guaranteed cost ceiling.
5. If sufficient, proceed within the user's authorized task without another
   permission question. If below the estimate, pause charged generation and
   say: `The current balance is X points; this batch is estimated to need Y points, leaving an estimated shortfall of Z points. Generation is paused pending sufficient balance.`
   Use estimated language for variable prices. Do not automatically purchase,
   top up, change provider, or reduce output quality to fit the balance.
6. If balance or pricing is unavailable, say that sufficiency cannot yet be
   assessed and identify the missing information. Authentication/network
   errors are not evidence of insufficient points. Pause charged generation
   until this preflight can be completed; independent preparation may continue.

Refresh the balance before each later charged batch, including revisions and
retries. When available, use the relevant `query_id` and `cost_points` from
`GET https://api.poe.com/usage/points_history` to compare actual consumption
with the estimate. Retrieve only what is needed; do not dump unrelated chat
history. If actual costs change the estimate, recalculate before continuing.
An estimate does not reserve points or guarantee the final charge.

## Access and integration boundary

Existing local credentials are available in
`~/.local/share/opencode/auth.json`: select the Poe provider entry
and read its nonempty `key` in memory. Reuse this source before asking the user
to configure `POE_API_KEY`. Never print, copy into artifacts, or pass the key as
a command-line argument. Do not modify the shared OpenCode account file.

The balance endpoint was successfully checked with this credential (HTTP 200).
Fetch a fresh balance for every preflight; do not reuse a recorded balance.
The Python HTTP client failed during that check while Node fetch succeeded;
a client/network failure alone does not establish invalid credentials.
The installed client is `scripts/poe_image.mjs` (Node 18+, no SDK dependency).
It uses Poe Chat Completions with `stream:false`, local reference-image data
URLs, and the three approved image-model IDs. Model defaults are defined above.
Live charged generation is not implied by successful balance or mock tests.
Do not point the OpenRouter image helper at Poe; its schema is different.

## Executable preflight and generation

From the nature-figure directory:

```bash
node scripts/poe_image.mjs balance
node scripts/poe_image.mjs models
node scripts/poe_image.mjs preflight --job /path/to/job.json
node scripts/poe_image.mjs generate --job /path/to/job.json --out /path/to/new-output-dir
```

Prepare a JSON job with `model`, `calls` (number of independent requests),
`prompt_file`, optional `references` (local image paths), and a `quote` object:

```json
{
  "model": "nano-banana-2",
  "calls": 1,
  "prompt_file": "prompt.txt",
  "references": [],
  "quote": {
    "points_per_call_upper": 0,
    "source": "REPLACE with current bot rate card or matched usage receipt",
    "checked_at": "REPLACE with ISO timestamp",
    "assumptions": "REPLACE with image count, size, quality, input and output assumptions"
  }
}
```

This example is deliberately **not executable** until its quote is filled:
zero, absent, or stale (>24 h) estimates fail closed. Relative file paths are
resolved beside the job file. Every request asks for one image. Independent
calls repeat the same prompt; a revision is a new job with the previous image
as a reference. Include planned revisions in the overall task budget.

Use current Poe point pricing or matched per-query usage for the same settings.
The model catalog's price fields do not by themselves specify complete image
costs in account points; `image` must not be assumed to mean a flat per-image
price. If pricing is incomplete, explain that it cannot yet be assessed; do
not make a paid exploratory call to discover cost without user authorization.

Optional `parameters` require `parameters_source` with a verified bot-specific
source. The client allows `aspect_ratio`, `image_size`, `image_only` for Nano
Banana, and `size`, `quality`, `use_mask` for GPT Image 2; verify exact
values against the current bot controls. Poe documentation differs about
custom-parameter support. The compatible-API guide says SDK `extra_body` fields
are supported best-effort; they are merged at the top level of a raw HTTP body.
Inspect actual returned size/content instead of assuming settings took effect.
For masks, attach the base image followed by the matching mask per bot guidance.

The client checks current balance before each request against the estimated
remaining batch. No automatic POST retries, purchases, or model substitution.
It saves the response before downloading images and matches usage by query ID
when available; missing/delayed usage is not a zero charge. Review actual cost
before planning a further job. Balance change alone may include other sessions.

If only download failed, use a new directory with:

```bash
node scripts/poe_image.mjs recover --response /path/to/call-1/response.json --out /path/to/recovered
```

This recovers images without a new generation request. Unknown output hosts or
formats need inspection; do not disable the check or blindly regenerate.

Continue to apply `ai-graphical-abstract-workflow.md` for scientific content,
human review, provenance, and the target journal's figure requirements.

## Official references (checked 2026-09-30)

- [Poe Usage API: balance and per-query usage](https://creator.poe.com/docs/resources/usage-api)
- [Poe FAQs: compute points and bot pricing](https://help.poe.com/hc/en-us/articles/19944206309524-Poe-FAQs)
- [Poe API keys](https://poe.com/api/keys)
- [Poe compatible API and custom parameters](https://creator.poe.com/docs/external-applications/openai-compatible-api)
- [Chat Completions endpoint](https://creator.poe.com/api-reference/createChatCompletion)

- [Nano-Banana-2](https://poe.com/Nano-Banana-2)
- [Nano-Banana-Pro](https://poe.com/Nano-Banana-Pro)
- [GPT-Image-2](https://poe.com/GPT-Image-2)
