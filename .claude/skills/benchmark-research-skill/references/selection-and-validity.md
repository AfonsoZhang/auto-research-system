# Reuse existing benchmarks before constructing new ones

Apply to empirical evaluation selection, implementation and interpretation.
Scale the work to the question and existing evidence. An ordinary edit does not
restart a survey, and theory, survey or position work need not invent an experiment.
Explicit user choices and the shared paper-type route determine the scope.

## Select by measurement fit and independent use

Start with closely related work's actual evaluations. Prefer verified published
or accepted papers under the [publication policy](../../shared-references/publication-policy.md).
Keep recent preprints and software documentation labeled where relevant. A paper's
publication, a benchmark's public availability, independent reuse and suitability
for this question are separate facts. Do not equate a famous name or citation count
with valid measurement, and do not require a software harness to have its own paper.

Record enough to distinguish plausible candidates, using existing notes or the plan:

| Decision field | What to retain |
|---|---|
| Measurement fit | Claim/capability, task and environment, what is measured and what is not |
| Evidence of use | Original source and relevant independent uses actually found; paper record IDs, selected versions and experiment/table/code locators |
| Reusable protocol | Dataset/task version, evaluation split, official scorer and metric, prompts/tools/interaction limits, compatible baselines |
| Validity | Data provenance, feasible task completion, outcome-to-score alignment and claim-relevant leakage or shortcut concerns |
| Resources | License/access, environment/dependencies, compute/API cost and run time when known; unknowns stay explicit |
| Decision | Primary comparison, complementary diagnosis, pilot-only use, unsuitable or unresolved, with a specific reason |

Compare credible alternatives without a fixed number of datasets, citations,
models or seeds. Reuse an adequate existing comparison. Missing access is a
resource decision, not a reason to recommend an easier but scientifically weaker
substitute. Apply [experiment-plan's resource rule](../../experiment-plan/SKILL.md#select-the-best-suited-design-before-checking-availability).

## When custom evaluation is warranted

Use matching established/public benchmarks for the primary comparison by default.
Author-created cases can isolate a mechanism or stress a boundary, but do not let
those cases alone carry a broad capability or generalization claim.

Before proposing new benchmark construction, state the specific capability or
measurement gap in the closest existing protocols. Consider reuse, an explicitly
labeled extension and a new resource, then explain which answers the question.
Failed searches or downloads do not establish that gap. Do not manufacture a gap
just to make a benchmark paper fit its template.

A real gap can justify new data, tasks or metrics, including as the primary
contribution of an evaluation/resource paper. State validation, baselines and
source/annotation plans proportionate to that contribution. Reuse-first is a
default, not a ban on new benchmarks or a reason to reject a research direction.

## Preserve comparability from plan to results

Reuse the official tasks, version, test split and scorer when they answer the
question. Record the task IDs or selection rule, preprocessing, prompts, tools,
model/environment versions, budgets and metric definitions needed to reproduce
the comparison. Check baseline implementation and scoring on meaningful cases
before an expensive batch; match conditions across methods where the claim needs it.

Label any subset, filtering, added annotation, simulator, task adaptation, changed
judge or changed protocol. Explain its purpose and effect on comparison. Keep
official-protocol results separate from modified conditions. Compare to published
scores only when the conditions support it; otherwise mark them as contextual or
rerun the baseline under the actual shared protocol. Do not silently give modified
tasks the authority of the original benchmark name.

Choose subsets and inclusion rules before inspecting the compared systems' test
outcomes. Keep tuning apart from held-out evaluation. A reduced decisive pilot can
gate further investment; its subset score is not the full benchmark score. Carry
forward the existing pilot threshold, budget and stop rules.

## Check that the evaluation measures the intended outcome

Borrow the useful measurement checks from Inspect Evals without requiring its
directory layout or launching an external reviewer:

- **Claims and provenance:** compare the stated data/task origin and tested
  capability against source records, actual loaders, samples and environment.
  Distinguish original data, derived tasks and synthetic fixtures.
- **Task feasibility:** verify that relevant information, tools and services are
  available for a capable system to complete the task; check that failure is also
  meaningfully observable. Answering a question about behavior does not establish
  that the system performed it.
- **Scoring alignment:** trace success from task outcome to scorer. Check for false
  success without completion and false failure despite completion. Use known-outcome
  cases or trajectory inspection where they resolve an actual concern.
- **Measurement limits:** label direct outcomes, proxies, simulations and model
  judgments. Establish the proxy's role and validation appropriate to the claim;
  neither an LLM judge nor a public benchmark supplies independent truth by itself.

Separate confirmed defects, plausible concerns and untested coverage. Correct or
bound a demonstrated mismatch without automatically rejecting the idea or repeatedly
narrowing supported contributions. Use [claim preservation](../../shared-references/claim-preservation.md)
for substantive scope changes. A successful script run does not validate science.

## Provenance and reuse

Keep the selection rationale in the existing survey/experiment plan and run
conditions in [experiment records](../../experiment-bridge/references/experiment-records.md).
No additional compulsory ledger is needed. Publication verification remains owned
by the literature module; later stages reuse its records rather than certify it again.

Validity checks adapted from [Inspect Evals `eval-validity-review`](https://github.com/UKGovernmentBEIS/inspect_evals/blob/cef701f5546256fa5c57554529a373a011738339/.claude/skills/eval-validity-review/SKILL.md),
MIT; see [LICENSE-inspect-evals](../LICENSE-inspect-evals). The local adaptation
uses evidence-based concerns, accepts justified proxies, and leaves research
direction and scope decisions with the author and existing workflow.
