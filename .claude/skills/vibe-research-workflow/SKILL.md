---
name: vibe-research-workflow
description: >-
  Plan an AI-assisted research work session across coding, figures and writing.
  AI may help plan research, form hypotheses and design experiments within the
  user's objective; evidence is verified and consequential choices stay with the
  user or their existing delegation. Use for AI-assisted workflow advice, tool
  selection or organizing a requested work block. This advisory skill does not
  activate execution in automatic mode or replace the research controller.
license: CC-BY-4.0
---

# Vibe Research Workflow

Apply the shared [research autonomy and validation policy](../shared-references/research-autonomy.md).
The AI can do substantive research work within the requested task. The user owns
the goal, budget, consequential decisions and academic responsibility; routine
operations do not each require their approval.

This skill helps plan a work session. The research root's `research-agent-team`
remains the single controller for research stages and team execution. A workflow
suggestion here does not activate that controller, a team or the next phase.

## Route the actual request

- Workflow advice or a coding/figure/writing work-block plan: use this skill.
- Hypothesis or direction exploration: `research-companion` or
  `brainstorming-research-ideas`; evaluation: `idea-evaluator`.
- Experiment design: `experiment-plan`; implementation and requested runs:
  `experiment-bridge` / `run-experiment`; interpretation: `analyze-results`.
- New prose from research materials: `paper-writer` or `intro-drafter`;
  revision of existing prose: `paper-polish`.
- Figure production: `nature-figure`; design advice: `figure-designer`.
- Root-level research coordination or explicitly requested automatic mode:
  use the unified controller under the workspace routing rules.

These routes select methods inside the user's scope; they do not authorize an
extra research phase, experiment batch or external action.

## Plan the work block

1. Read the goal and current artifacts. Identify the needed output and dependencies;
   reuse completed work and existing plans.
2. Select the relevant guidance:
   [coding](references/vibe-coding.md),
   [figures](references/vibe-figure.md), or
   [writing](references/vibe-writing.md).
   Use [tool selection](references/tool-selection.md) as a starting point and
   check actual capabilities when a recommendation depends on them.
3. Identify the next useful work and its verification. For research claims,
   distinguish execution checks from the protocol/evidence/conclusion checks in
   the shared policy.
4. Resolve ordinary implementation choices within authorization. Give options
   only for material goal, scope, cost or academic commitments; reuse decisions
   already supplied instead of asking again.
5. Deliver the requested plan or advisory answer. If execution was also requested,
   complete that authorized scope using the selected skills.

## Verification and responsibility

Use [behavior guidelines](references/behavior-guidelines.md) for the common rules.
Inspect actual sources and artifacts. Keep planned work, failed measurements and
valid negative results identifiable. Do not replace verification with a claim
that the user has checked everything.

Human review focuses on consequential choices, central scientific conclusions and
final commitments. Routine code tests, factual checks and semantic comparisons
are the agent's work. Maintain records that let the user inspect that work.
Verified venue or institutional requirements and explicit user restrictions still
apply; do not invent blanket bans on AI-originated ideas or drafts.

## Deliver

Give the current phase, concrete next work, relevant tool/skill, verification and
any unresolved decision. Keep the form proportional to the task; use a table only
when it helps compare options. Reuse the project's existing tracker. Do not add a
mandatory rules recital, line-by-line user signoff, second control ledger or
automatic continuation.
