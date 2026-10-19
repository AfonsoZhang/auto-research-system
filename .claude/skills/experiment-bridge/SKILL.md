---
name: experiment-bridge
description: >-
  Implement a research experiment plan as runnable code, configs, metrics and
  result logging, then perform the requested smoke or pilot runs. Use for
  experiment implementation, translating a plan into code or completing a plan-to-results workflow.
license: MIT
metadata:
  upstream-repo: wanshuiyin/Auto-claude-code-research-in-sleep
  upstream-commit: c4535ea8ae1e013399a2525dc7d285859f672b62
  local-adaptation: author-led-experiment-workflow
---

# Implement the experiment plan

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

Read the supplied plan or `refine-logs/EXPERIMENT_PLAN.md`, the method description,
existing implementation and current tracker. Reuse working project code. If the
question is not specified well enough to implement, use
[experiment-plan](../experiment-plan/SKILL.md) for the missing design decisions.

## Scope of execution

An implementation request includes writing code and inexpensive correctness checks.
It does not by itself launch the full experimental campaign, rent resources, push
code, or invoke an external model reviewer. If the user has already authorized a
pilot or campaign with an adequate resource budget, continue within that scope;
do not ask again at each milestone. Installing this skill launches nothing.

External model review is optional and used only when requested. Never substitute a
simulated score for testing the implementation. This local variant does not require
Codex MCP, ARIS queue helpers or cloud provisioning skills.

## Preserve the selected design

Apply the [resource-selection rule](../experiment-plan/SKILL.md#select-the-best-suited-design-before-checking-availability)
when implementation reveals missing data, models, evaluators or compute. Recommend
the needed resource and ask the user about access or a concrete alternative before
changing the scientific comparison. Continue independent implementation while the
choice is pending. Fixtures and smoke runs remain implementation checks, not a
substitute for the selected experiment.

Preserve the chosen benchmark's task/version, split, scorer and baseline protocol
under [benchmark selection and validity](../benchmark-research-skill/references/selection-and-validity.md).
Prefer adapting the method to the official evaluation interface. Instrumentation
and adapters must preserve task and score semantics; label any scientific change
as a modified condition. Check outcome-to-score behavior where relevant, and keep
synthetic fixtures separate from the selected benchmark data.

## Build the smallest working implementation

1. Translate the first decisive experiment into concrete data loading, method,
   baseline, evaluation and logging components. Implement the actual algorithm,
   not only interfaces or a command that calls a missing script.
2. Make experimental variables configurable. Keep evaluation code shared across
   methods. Record deviations from the plan and distinguish engineering fixes
   from changes to the scientific comparison.
3. Follow [experiment records](references/experiment-records.md) for run identity,
   resolved configuration, raw outputs, failure reporting and aggregation.
4. Check metric behavior on tiny cases with known answers; verify split isolation,
   sample counts and label alignment. If applicable, reproduce a baseline or
   overfit a tiny batch. An import check or successful process exit is insufficient.
5. Complete one config → execution → raw result → summary path before scaling.
   Mark synthetic smoke data as a fixture; never count it as scientific evidence.

For supervised tasks, use the actual reference labels and official evaluator where
appropriate. For human evaluation, model judges, proxies or simulations, record
the reference source, independence and limitations. Do not prohibit these research
designs categorically or quietly relabel predictions as ground truth.

## Repair and run

When a check fails, inspect the actual traceback, raw predictions and metric code
before changing the method. Fix the identified cause and rerun the smallest check
that tests it. Repeated identical failures call for a different diagnosis; report
environment/design blockers when further progress needs information or resources.

Preserve raw outputs and user-authored code. Record attempts separately. Changing
batch size, model size or learning rate to recover from OOM/divergence may change
the experiment: if recovery changes the scientific comparison beyond an already
approved fallback, present the resource/fallback choice to the user first. Record
the chosen configuration and comparison separately from the planned condition.

Implement the [planned pilot outcomes](../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot)
and resource cap before scaling. Keep main runs pending until the continuation
criterion is supported. Distinguish credible scientific stopping from inconclusive
evidence, unevaluated claims after technical failure, and budget pauses; preserve
the applicable repair/follow-up allowance. Successful smoke execution alone does
not establish that the pilot passed.

Use [run-experiment](../run-experiment/SKILL.md) for authorized runs. Collect actual
exit status and expected outputs before updating the tracker. Preserve failed and
missing runs; do not mark a milestone complete because its process launched.

## Deliver

Report the implemented entry points, exact commands, checks performed, artifacts,
remaining blockers and what has actually run. For results ready to interpret,
hand off to [analyze-results](../analyze-results/SKILL.md). Do not automatically
start reviewer loops, revise manuscript claims or change research direction.

Adapted from ARIS `skills/experiment-bridge/SKILL.md` at the revision above;
see [LICENSE](LICENSE). RPW-derived record guidance has its own attribution and
license in the linked reference.
