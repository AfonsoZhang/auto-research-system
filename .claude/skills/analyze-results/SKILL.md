---
name: analyze-results
description: >-
  Analyze research results against the experiment plan, preserving failed/missing
  runs and separating implementation problems, inconclusive evidence and evidence
  against a claim. Use for result analysis, ablation interpretation, negative-result diagnosis or deciding what a
  completed experiment supports.
license: MIT
metadata:
  upstream-repo: wanshuiyin/Auto-claude-code-research-in-sleep
  upstream-commit: c4535ea8ae1e013399a2525dc7d285859f672b62
  local-adaptation: author-led-experiment-workflow
---

# Interpret results at the strength the evidence supports

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

For structure or evidence requirements, use [paper-type-routing.md](../shared-references/paper-type-routing.md). Reuse the contribution type, stage and venue from existing materials; select only claim-relevant checks. This selects guidance within the current task and does not start another phase.

For substantive claim creation or revision, follow the [cross-revision claim-preservation policy](../shared-references/claim-preservation.md).

Read the research question, experiment plan, expected runs, raw results and known
implementation checks. Reuse existing analysis code after inspecting its grouping
and exclusions. Apply [experiment records](../experiment-bridge/references/experiment-records.md)
before using aggregates. The local installation does not bundle RPW's three
reported run-generation/validation/aggregation helpers.

## Validate the comparison

Reconcile planned versus observed runs, including missing seeds, failures and
exclusions. Inspect whether methods share the intended split, preprocessing,
metric, evaluation budget and sampling unit. Retain original per-run values.
Identify suspect outputs, leakage, failed baseline reproduction or incorrect
metrics before interpreting a difference as a scientific finding.

Apply [benchmark comparability and validity](../benchmark-research-skill/references/selection-and-validity.md)
to the recorded conditions. Keep official-protocol, adapted, pilot-subset and
author-created diagnostic results identifiable. A subset score is not a full-suite
score; published baseline numbers are directly comparable only under compatible
conditions. State the concrete measurement gap when one remains, while preserving
conclusions already supported by valid comparisons.

Unavailable resources or unresolved access leave the affected comparison untested;
they are not negative scientific results. Analyze valid completed comparisons at
their actual scope, but do not treat a convenient substitute as completing the
selected design. Preserve the open question and present any resource-driven change
of scope to the user under the
[resource-selection rule](../experiment-plan/SKILL.md#select-the-best-suited-design-before-checking-availability).

Aggregate only compatible experimental conditions. Report sample counts and an
appropriate uncertainty estimate; a single observation cannot estimate between-run
variability. Distinguish seed variation from task/subject variation and use paired
comparisons where the same cases are evaluated. State metric direction and report
absolute changes; use relative changes only when meaningful and defined.

## Classify what was learned

| Finding | Interpretation and next action |
|---|---|
| Invalid or incomplete measurement | Repair the implementation, measurement or missing run. This does not test the scientific claim yet. |
| Inconclusive evidence | Explain the uncertainty or unresolved confound. Consider a targeted discriminating test; do not equate non-significance with no effect. |
| Evidence against a claim | Identify the contradicted claim and conditions. Evaluate any proposed narrowing under the claim-preservation policy, including the retained contribution and whether it still answers the question. A changed mechanism is an explicit scope option. |
| Evidence supporting a claim | State the effect and supported scope. Do not generalize beyond the design or promote an association into an identified mechanism. |

Mixed outcomes may support some claims or conditions and weaken others. Keep those
findings separate. Positive and negative results face the same evidence standard;
preserve valid negative findings and do not invent a defense for a contradicted claim.

## Explain and propose the next test

For each material finding distinguish observation, plausible explanation and what
would discriminate that explanation from alternatives. A removed component hurting
performance is not automatically proof of the claimed causal mechanism.

For a pilot, apply the [plan's outcome distinctions](../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot)
and assess the remaining budget separately. Recommend scientific stopping only
when credible negative evidence meets the predeclared stopping rule under the
tested conditions. A below-threshold estimate or non-significance alone is
insufficient. Inconclusive evidence calls for an authorized, bounded discriminating
follow-up or an unresolved finding; invalid measurement leaves the claim unevaluated.
Budget exhaustion pauses affected spending without turning either outcome into
refutation. Retain the specific evidence and any resumption condition; none of
these outcomes automatically rejects the whole direction or permits unlimited runs.

Recommend only follow-ups that resolve a specific uncertainty, with a priority and
cost rationale. If the existing evidence already answers the question, say so.
Apply the agreed early-stop rule without asking again. Changing the research
direction remains the author's decision; no unplanned topic rejection, pivot or
external model jury is part of this skill. A reviewer can be consulted separately
when requested, but its score is not empirical evidence.

## Deliver and hand off

Return the essential comparison, coverage/exclusions, supported interpretations,
uncertainty and useful next action. Link findings to result artifacts. Use the
project's experiment report/tracker rather than automatically editing paper prose.
When the task continues into paper planning or writing, hand analyzed findings to
[good-story](../good-story/SKILL.md) using the shared
[results-to-writing handoff](../experiment-bridge/references/experiment-records.md#results-to-writing-handoff).
Reuse the current report or Evidence Map. Pass supported, opposing, and unresolved
findings with their scope and source links. `good-story` proposes argument and
figure order, then passes that to `ts-paper-plan` / `paper-writer` within the
requested scope. If only analysis was requested, finish with the analysis report.

For a follow-up that is needed and requested, return the specific open question
and comparison to [experiment-plan](../experiment-plan/SKILL.md). Do not start a
repeat-until-positive experiment or writing loop.

For a requested Limitations draft use
[limitation-and-risk-writer](../limitation-and-risk-writer/SKILL.md); for plots use
[nature-figure](../nature-figure/SKILL.md). Retain their respective output boundaries.

Adapted from ARIS `skills/analyze-results/SKILL.md` at the revision above;
see [LICENSE](LICENSE). Local interpretation categories are an explicit adaptation.
