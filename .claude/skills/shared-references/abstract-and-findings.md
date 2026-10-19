# Abstract focus and informative findings

Author writing preference for story, outline, drafting, polishing and requested
review. Use with the existing paper-type and claim-preservation policies. Apply
within the requested editing scope; this does not reopen topic selection or runs.

For manuscript wording, apply the shared
[direct-claim acceptance rules](../paper-polish/references/ai-tone-guardrails.md#state-supported-claims-directly)
during drafting, revision and requested review.

## Abstract: contribution, result and significance

Prioritize the question, approach, decisive finding and what that finding changes.
Keep detailed limitations in Discussion/Limitations by default. Do not append a
routine caveat, future-work list or apologetic closing just to make the abstract
look balanced. A brief prior-work gap can motivate the question; it is not a
requirement to enumerate either prior work's shortcomings or this paper's limits.

If omitting a condition would materially mislead readers about the main result,
include the shortest sufficient qualifier with that result. Follow explicit venue
requirements when applicable. A negative result or discovered failure boundary
that is the central contribution belongs in the abstract as a finding. Abstract
selectivity does not remove material constraints from the paper.

## Core findings: state what the evidence adds

Ask what a reader learns beyond the task definition, metric, method description
or an expectation that could be stated before examining the evidence. Prefer
the supported comparison, conditional effect, tradeoff, boundary or explanation
that resolves an uncertainty. Identify the relevant conditions and consequence;
use measured magnitudes when available and useful.

Statements such as "more tokens cost more" or "the method works when its
assumptions hold" do not by themselves establish an informative core finding.
Replace a truism with the evidence-backed answer to the actual question, if one
exists. Keep a needed setup fact as setup rather than promoting it to a discovery.

Informative does not require counterintuitive, unprecedented or dramatic. An
expected effect, replication, null result or modest improvement can add useful
knowledge through its measured size, reliability, scope or a resolved uncertainty.
Do not invent surprise, causality, thresholds or implications. If the supplied
evidence does not resolve the question, flag that specific gap to the author;
stronger wording cannot repair it and does not authorize a new research campaign.

**Unsupported preregistered hypothesis that is not the main contribution.** Demote
it, do not argue with it. In Results, report the effect, its interval and the
protocol margin in one sentence; disclose any post-data protocol change in the
appendix (what changed, why, after which data) without restating a verdict. In the
abstract and conclusion, state the comparison by what was measured (e.g. "perform
comparably; the best gains X at Y times the false-alarm rate"), not by negation.
Do not call it "borderline" because the interval's upper end reaches the margin,
and do not blame sample size when the point estimate is far below the margin.

**Group statements hold for every member.** "Content readers add five points" is
false if only the best one does; name the member or the best one. When summarizing
the paper for the author, keep the main thesis distinct from secondary findings.

## Conclusion: a decision the reader can act on

RITP: compare with the closest
published conclusions before finalizing.

- **Shape by contribution type.** A method paper can follow problem, key idea,
  strongest evidence, impact (Master-cai/Research-Paper-Writing-Skills,
  `references/conclusion.md`, MIT); an analysis/comparison paper concludes with
  the decision rule below. Keep detailed limitations in their own section.
- **The user chooses the direction:** offer 2-3 versions first (paper-writer
  Phase 4, Human in the loop).
- **Open with the finding and its numbers.** Do not lead with a defensive frame
  ("In our check, X is a bottleneck"); state what the evidence shows, with the
  counts that carry it, and keep the scope qualifier beside the number.
- **Generalize at the level the design covers.** When each compared method stands
  for a design family, state the rule by family and name the method as its
  representative ("trained set-level retrieval, as represented by COLT"). Do not
  extend to families that were not represented.
- **Turn a measured tradeoff into a choice rule.** If the study measures a cost
  axis, conclude with condition, then family, then cost, each branch backed by a
  measured comparison. A branch with no winner is stated as a measured ceiling
  ("none of the compared ... completes a tenth"), not omitted.
- **Failure analysis goes last and separately.** State how the leading options
  fail, then "which motivates" the repair each failure points to. An untested
  repair is motivated, never claimed; do not merge repairs into the choice rule.
- **Drop meta advice that is not the contribution** ("we suggest reporting X").
  Keep a recommendation only when the evidence directly supports it.

## Limitations

**Write only non-obvious limitations.**

Apply the mandatory [Limitations admission gate](../limitation-and-risk-writer/SKILL.md#admission-gate-all-four-conditions-required)
before adding or substantively revising limitations. Read the current body first.
Each point must be grounded, consequential for a specific claim/use, non-obvious,
and additional to what the body already explains.
Any failed condition excludes it from new section prose; hedging or paraphrasing
does not repair a failed candidate.

Enforce the writer's [length budget](../limitation-and-risk-writer/SKILL.md#length-budget-hard-acceptance-limits)
after admission: measure final prose, apply the word/point caps, and never pad to a
minimum. Its scope and explicit override rules also apply to planning and review.

"Only a few models were tested," "generalization is not guaranteed," and
"more experiments are needed" do not pass by themselves. An already explained
constraint and consequence are excluded even when important. Adding identifiers,
counts or future-work language does not create a new implication.

Keep material disclosures in their appropriate existing location. The gate's
empty-result and required-section rules govern omission or minimal cross-reference;
do not populate an optional section for balance. Never invent a less obvious
failure or mechanism. A genuine unsupported main claim requires an author-facing
body correction, not a disclaimer that preserves the overclaim.

## Editing and review

Check abstract emphasis, information added by the central finding, and the
consequence of each limitation. Preserve accurate scope qualifiers and material
evidence; do not manufacture a more surprising story or a less obvious weakness.
In a requested review, distinguish a wording problem from a missing comparison
or unresolved inference. Lack of surprise or of a limitations sentence in the
abstract is not itself a scientific defect or a topic-rejection criterion.
