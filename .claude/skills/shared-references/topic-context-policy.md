# Context boundaries for topic selection

Read before generating or reopening research directions. Use with the
[topic-selection policy](topic-selection-policy.md); contribution and evidence
standards remain unchanged. Apply to the requested work without activating a
team, another phase or additional model calls.

During generation, apply the policy's
[question value and hypothesis relationships](topic-selection-policy.md#question-value-and-hypothesis-relationships)
to how candidates are framed, before ranking them. This does not turn an ideation
request into a selection decision or require additional experiments.

## Identify what is being continued

- **Fresh exploration:** a new topic search without a requested continuation.
  Establish the field from the current task and explicitly applicable user
  requirements. A workspace name, historical interest, installed skill example,
  available dataset or old recommendation does not set the field by itself.
- **Continuation:** the user asks to continue, evaluate or modify a named idea or
  project. Reuse its valid evidence and decisions within their original scope.
  Ordinary revisions do not trigger fresh brainstorming or discard project history.
- **Reselection:** the question or core candidate is being replaced. Retain the
  user's applicable requirements and verified facts; reassess attached choices
  such as the dataset, location, method and venue instead of carrying them forward
  merely because they appeared in the previous plan.

Infer the mode from the request. Use existing clarification/delegation rules only
for consequential ambiguity; identifying the mode needs no separate approval.
After proposing a new or replacement topic, apply the mandatory
[human checkpoint](topic-selection-policy.md#human-approval-after-topic-selection).
If the task leaves
the field open, keep it open or record a choice made within existing delegated
authority. Do not silently fill it from a historical profile.

## Prepare the selection brief

In existing task notes, keep the objective and the origin of each consequential
constraint or preference: its source, applicable project/scope and current status.
Distinguish explicit user requirements, verified facts, user preferences,
unconfirmed suggestions and agent decisions made under delegated authority.
Include the necessary resource facts and uncertainty, not unrelated project history.

An agent decision can guide authorized execution without becoming a user mandate
or a scientific fact. Preserve that distinction in handoffs, summaries and memory.
Repetition, a saved plan, elapsed time or lack of user reply does not change its
origin. Check original statements when a summary's attribution is ambiguous.
Retrieve a necessary preference narrowly from its known source; do not search all
project memories for a seed. Historical exclusions require applicable current
authority, and unverified access limitations remain unknown rather than hard limits.

## Generate before recalling old judgments

For fresh exploration or reselection, generate from the scoped brief and relevant
scientific sources. Keep old candidate lists, rankings, verdicts, the main agent's
preferred answer and unrelated project summaries out of the generation input.
Do not list excluded old topics in the brief either. A user-requested seed or
comparison is an explicit input, not something to hide.

Preserve the initial candidates in the existing work notes before consulting past
evaluations. Then retrieve relevant history to reuse verified evidence, identify
previously explored work and assess what changed. Old verdicts are historical
judgments to reassess, not automatic rejection or selection rules. Current
literature searches and relevant verified scientific facts remain usable during
generation; this ordering does not require brainstorming without evidence.

When delegation in automatic mode is authorized and the runtime supports it, use an
existing brainstorming/analysis role in a new context with the scoped brief.
Do not fork or resume the full parent conversation for this pass. In Claude Code,
call the Agent tool with a named `subagent_type` such as `brainstormer` or
`research-analyst`; never `fork`, and do not SendMessage an agent that already saw
earlier judgments. A fresh subagent can still inherit `CLAUDE.md`/`AGENTS.md`
routing, auto-memory and hook-injected session summaries, which may contain past
topic verdicts. Check the actual assignment and available runtime evidence of
inherited instructions, automatically injected memory, opened files and tool access. Supply the needed standards and
source access; keep unrelated histories out of the task inputs and retrieval scope.
A new agent name or an instruction to ignore history does not establish isolation.

If inherited inputs cannot be inspected or restricted, record that limitation;
do not claim a clean context. Continue authorized work with source-based checks
when useful, without silently adding a subprocess, paid call or new permission.
Standalone inline calls remain available and make no independence claim.

## Accept the choice and preserve its origin

Before ranking or issuing a decision card, check that material restrictions trace
to the brief or identified evidence. Compare alternatives against the current
objective; time already spent and available assets inform remaining cost, not
scientific value. If the old framing alone explains a restriction, reopen that
choice within existing authorization. Completing a full workflow does not require
selecting an inadequately supported topic merely to advance a stage.

When independent comparison is already authorized, provide the brief, candidates
and evidence without the main agent's preferred ranking. A card-selection model
cannot repair alternatives omitted by the card author. Check the options' scope
and premises before passing them to that model, and retain the actual decision
source: user, model or main agent.

Record the mode, brief/source references, initial candidate snapshot and actual
input-boundary checks in the existing evaluation or tracker, proportionate to the
task. No parallel ledger, new role, fixed candidate quota or global memory deletion
is introduced. After the topic checkpoint is approved, reuse relevant valid work
and continue the authorized workflow; do not restart completed stages on every invocation.
