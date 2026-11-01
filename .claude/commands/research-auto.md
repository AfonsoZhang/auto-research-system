---
description: 开启研究自动模式——按 research-agent-team 控制器连续推进本任务，给了终点就停在终点、没给就一直推进（选题后仍停下等人工批准）
argument-hint: [可选：本次任务与终点，如「只把 pilot 跑完并验收」；留空则不设终点、一直推进]
disable-model-invocation: true
---

The user typed `/research-auto`. This invocation **is** the explicit activation of
automatic mode required by `$RESEARCH_ROOT/CLAUDE.md`, scoped to **this task only**.
It does not carry over to later tasks or sessions.

Task and endpoint from the user: $ARGUMENTS

# Steps

1. **Load the controller.** Read `$RESEARCH_ROOT/.claude/skills/research-agent-team/SKILL.md`
   and its `references/full-flow.md`, and follow them in automatic mode. Everything
   below only pins down what activation means; the controller is the source of truth.
2. **Fix the task and endpoint.**
   - `$ARGUMENTS` names a task: use it. A narrower endpoint stated there (single stage,
     single revision, pilot only) stays narrow; do not expand it.
   - `$ARGUMENTS` is empty: **no endpoint — keep going.** Take the task from the current
     conversation or the project's existing plan/tracker and do not ask the user for a task
     or endpoint. Advance through every applicable stage; when one deliverable is accepted,
     continue to the next useful stage of the same project instead of stopping. Stop only
     at a hard stop condition (below), the topic-approval checkpoint, or the user saying stop.
3. **Announce, in Chinese, one short block:** `自动模式已开启` + task + endpoint (`不设终点，持续推进` when empty) + the
   stop conditions that still apply (budget/resource caps, pilot stop rules, real external
   dependencies, the post-selection topic approval). Then start working without asking
   for confirmation.
4. **Run.** Delegate to the `research-*` roles only where they help; select and execute
   authorized card options directly under the
   [decision-card policy](../skills/research-agent-team/references/decision-cards.md),
   recording evidence and rationale; advance between accepted stages without
   asking at each transition; reuse the existing plan/tracker for state.

# Limits that activation does not lift

- **Topic approval:** after fresh selection or reselection, deliver the Chinese topic
  report, record `AWAITING_TOPIC_APPROVAL` and end the turn. No timeout, default
  or main-agent recommendation can approve it.
- New authority (spending beyond the agreed budget, paid services not yet authorized,
  external submission or publication, destructive operations) still needs the user.
- Child projects keep their own workflow and freeze/data constraints; delegate only
  bounded work into them.
- Automatic mode ends at the endpoint (if one was given), at a hard stop condition, or
  when the user says to stop. Report actual results and unfinished items; do not claim completion that the
  acceptance checks did not establish.
