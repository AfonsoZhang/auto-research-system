---
name: experiment-plan
description: >-
  Turn a research question or method proposal into an experiment plan:
  existing benchmark selection, competing explanations, baselines, metrics, controls, minimum pilot, run order,
  budget and interpretation of possible outcomes. Use for 实验设计、消融规划、
  evaluation protocols or claim-to-test planning.
license: MIT
metadata:
  upstream-repo: wanshuiyin/Auto-claude-code-research-in-sleep
  upstream-commit: c4535ea8ae1e013399a2525dc7d285859f672b62
  local-adaptation: author-led-experiment-workflow
---

# Plan experiments that answer the research question

For structure or evidence requirements, use [paper-type-routing.md](../shared-references/paper-type-routing.md). Reuse the contribution type, stage and venue from existing materials; select only claim-relevant checks. This selects guidance within the current task and does not start another phase.

Start from the author's question and the evidence needed to answer it. A plan should distinguish
plausible explanations, including outcomes that do not favor the proposed method.
The author's research objective, not a simulated reviewer score, determines scope.

Apply the shared [research autonomy and validation policy](../shared-references/research-autonomy.md).
The agent may formulate candidate hypotheses and design the protocol within the
requested research objective. Routine design choices use existing authorization;
material goal, scope or resource tradeoffs use the established decision process.
Record the protocol before evaluation; planning alone still does not launch jobs.

## Establish the question

Reuse the current proposal, research notes, code, literature records and explicit
user constraints. Inventory available resources separately from design requirements. If present, read `refine-logs/FINAL_PROPOSAL.md` and the existing
experiment plan. Clarify only missing details that change the design.

Identify the central claim, its intended scope, the closest alternative explanation,
and the comparison that would distinguish them. For exploratory work, state the
question without inventing a settled mechanism or claiming confirmed novelty.
Use the installed literature workflow when a baseline or external fact needs checking.

If [good-story](../good-story/SKILL.md) supplied a proposed main claim or evidence
order, treat it as a candidate argument to test. Reuse its claim/question labels;
state which comparisons could support, contradict, or leave each claim unresolved.
The proposed paper order does not determine run order or authorize experiments.
A later story change does not retroactively change the original hypotheses.

If the topic evaluation used [problem-selection strategy](../shared-references/problem-selection-strategy.md),
carry its consequential assumptions, essential constraints, revisable choices and
conditional next steps into this plan. Consult that reference when these remain
unresolved; reuse an adequate existing decision rather than restarting selection.

## Select the best-suited design before checking availability

Recommend datasets, baselines, models, evaluators and compute by how well they
answer the research question within the user's stated constraints. Compare credible
options and explain the preferred choice. Current access is a resource inventory,
not an implicit limit on the design. Best-suited does not mean largest, newest,
most expensive, or most likely to favor the method.

If the preferred design needs unavailable data, access, hardware, API capacity or
tools, present a concrete recommendation before asking the user: what is needed,
why it matters, how it could be obtained, and expected cost/time when known. Mark
unknown estimates explicitly. Offer a practical alternative with its effect on the
comparison and supported claims. Ask whether to obtain the preferred resources or
accept that tradeoff; do not silently select the currently runnable alternative.

Reuse decisions and budgets the user has already supplied. While a material
resource choice is pending, continue independent preparation but leave dependent
runs pending. A small local smoke test may check implementation; it does not replace
the selected pilot or main experiment. Resource-driven changes to data, baselines,
models or evaluation scope need the user's choice unless already authorized.

## Select existing benchmarks before proposing construction

For empirical evaluation, reuse an adequate existing benchmark decision or apply
[benchmark selection and validity](../benchmark-research-skill/references/selection-and-validity.md).
Use [benchmark-research-skill](../benchmark-research-skill/SKILL.md) for missing
comparison evidence within the planning task. Start from closely related papers'
actual evaluations and reuse the literature module's publication/version records.
Choose the primary comparison by measurement fit, independent use and reproducible
protocol. Identify any complementary diagnosis and preserve concrete resource choices.

Prefer a suitable established/public benchmark. Before recommending a new dataset,
task suite or scorer, document what existing protocols fail to measure and why
reuse or a labeled extension is insufficient. Author-created pilot/stress cases
do not alone establish broad capability claims. A demonstrated measurement gap
can justify a new benchmark; neither popularity nor a fixed dataset count settles
scientific validity. Record the decision in the existing plan, with versions,
splits, scoring, baselines and any intended deviations. Ordinary plan edits do not
restart selection.

## Design a compact evidence package

For each necessary experiment block, specify:

- Claim/question, competing explanation, and what the comparison can identify.
- Dataset/workload, version, split, sampling unit and train/tuning/test separation.
- Method and credible baselines, matched preprocessing, evaluation and resource or
  tuning budgets. Record unavoidable differences rather than concealing them.
- Primary metric and direction; secondary measures only where useful. Define the
  outcome that would support the claim, weaken it, or leave it unresolved.
- Controls or ablations that isolate the proposed mechanism. Component removal
  alone may change capacity, compute or other factors; state remaining confounds.
- Variability that matters: tasks, subjects, seeds or repeated model/API calls.
  Choose replication and uncertainty estimates for that sampling structure; three
  seeds is not a universal guarantee. Do not count repeated measures as independent.
- Cost, duration, priority and the decision informed by the result.

After selecting suitable resources, prefer the smallest comparison that can
resolve the highest-risk assumption; ease of access alone does not make it suitable.
Add robustness, efficiency and scaling tests where the claim requires them, not
as a fixed checklist. Do not demand a new experiment for every conceivable weakness.
For proxy/simulation/model-judged outcomes, label the measurement and establish
what it measures; do not present model agreement as independent ground truth.

## Gate further investment with a minimum decisive pilot

Use the smallest scientifically informative experiment to decide whether further
investment is worthwhile. Select resources appropriate to that pilot; recommending
a strong main experiment does not require acquiring its full resources up front.
A reduced pilot is valid when it still tests the critical assumption. Distinguish
it from a smoke test that checks only code execution.

Separate technical readiness (execution, output schema and measurement integrity)
from the scientific continuation criterion. Development examples may be used to
repair prompts, adapters or parsers within scope; freeze the resulting configuration
before held-out evaluation. A ban on tuning held-out cases does not ban development
repairs. Do not require perfect toy-task accuracy merely to check output readiness;
if a semantic check is essential to measurement validity, justify it separately.

Before running, specify the assumption tested, a meaningful success/feasibility
threshold, what would justify stopping, and a time/compute/API-spend cap including
any permitted follow-up. Make main runs conditional on the pilot meeting this gate.
An informative failure to meet the continuation criterion stops the downstream
campaign early; retain the results and report why further investment is unwarranted
under the tested conditions. Do not keep tuning or rerunning until it passes.

Normally reserve a bounded development/repair allowance separately from scientific
evaluation. Record explicit user limits separately from agent-selected operating
limits. An omitted repair allowance is not itself a user prohibition: routine
technical fixes may use remaining authorized resources after recording their scope
and cap. Revise agent-selected settings within that authorization when justified;
do not exceed an explicit or exhausted budget, tune on held-out outcomes, or lower
a scientific threshold after seeing results.

For an ambiguous scientific result, use a pre-authorized discriminating follow-up
if it fits the cap; otherwise stop that spending and report the unresolved question.
Technical failure leaves the scientific criterion unevaluated. Budget exhaustion
stops the affected campaign, not independent work already within the task. A passing
pilot permits only already-authorized next steps; additional resources or spending
outside existing authorization need the user's decision on a concrete proposal.

## Order and stopping decisions

Use an appropriate sequence: metric/data sanity check → baseline reproduction →
minimum decisive pilot → main comparison/necessary controls → replication or
targeted follow-up. Keep exploratory tuning distinct from final evaluation.

Before seeing final outcomes, state the main comparison, sampling/stopping rule,
budget and meaningful effect where applicable. Later changes remain possible:
record why they changed and whether a fresh evaluation is needed.

Explain failure branches. A crashed or invalid run requires implementation repair;
an imprecise estimate calls for an uncertainty assessment; valid opposing evidence
may narrow or challenge a specific claim. None automatically rejects the whole idea.
Negative results may still answer the research question.

## Deliver and hand off

Write the requested plan in the current research project, normally
`refine-logs/EXPERIMENT_PLAN.md`, and a compact run tracker if useful. Read existing
files first and preserve author edits. Include the recommended first pilot, its
resource prerequisites, expected cost, controls and interpretation of alternative
outcomes. Mark unresolved resource choices and dependent runs as pending; do not
rewrite the plan around availability. Never fabricate results.

Use [experiment-bridge](../experiment-bridge/SKILL.md) when implementation is requested.
Apply the shared [experiment records](../experiment-bridge/references/experiment-records.md)
when assigning run IDs or designing result files.

Adapted from ARIS `skills/experiment-plan/SKILL.md` at the revision above;
see [LICENSE](LICENSE). Local integration uses the same file for Claude and Codex.
