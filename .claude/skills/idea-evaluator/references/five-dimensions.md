# Five contribution lenses

Read the [shared topic-selection policy](../../shared-references/topic-selection-policy.md).
These lenses help characterize method improvements. They do not exhaust research
contributions or define publication thresholds; analyses, audits, resources,
replications and negative results need not improve any of these metrics.

| Lens | Question | Useful evidence / mechanism examples |
|---|---|---|
| Higher | Does task effectiveness improve under comparable conditions? | Relevant baselines; error-specific feedback, useful extra information, recovery |
| Faster | Does execution require less time or compute for the stated quality? | End-to-end overhead and cost/quality tradeoffs; caching, parallelization, early exit |
| Stronger | Is behavior more reliable under the claimed perturbation or shift? | Relevant fault/shift controls; recovery, decoupling, calibrated fallback |
| Cheaper | Is the total data, annotation, training or deployment cost lower? | Account for setup/amortization; active selection, reuse, distillation |
| Broader | Does the method support the stated additional conditions or tasks? | Tests of that transfer; cross-field combination, representations shared across tasks |

Choose the relevant lens or state N/A; a focused contribution need not excel on
two axes or unify multiple task families. Tradeoffs may be the finding. A narrow
setting can be appropriate when the claim is correspondingly scoped.

## Assessment and optional scores

Prefer a statement of the effect, its use and the supporting evidence. If the user
wants scores for comparing candidates, provide them with a local explanation;
do not interpret a 1–10 scale as calibrated acceptance probability. No score,
aggregate, number of high dimensions, speedup ratio or percentage gates a decision.

Use **unknown** for a missing measurement and **N/A** for an unrelated axis.
Distinguish observed evidence from a mechanism-based expectation. A plausible
untested mechanism may justify a pilot; it does not justify invented performance
numbers. Likewise, lack of an experiment at brainstorming time is not evidence
that the mechanism is weak. Novelty/value/feasibility stay separate.

## Attribution

For an apparent gain, consider the alternative explanations relevant to the
claim: stronger backbone, larger budget/context, routing or post-processing,
easier samples, different tool access or an unsuitable baseline. Use controlled
comparisons/ablations to isolate the claimed cause where necessary. Report the
gain as unassigned until the evidence supports attribution; do not infer that an
unresolved attribution disproves all value in the system.

Choose comparisons and repeated measurements according to the claim and observed
variability. No universal number of models, datasets or seeds is prescribed. A
reliable tie/loss refutes a superiority claim only to the extent supported by its
design and uncertainty; assess meaningful efficiency or negative findings separately.
