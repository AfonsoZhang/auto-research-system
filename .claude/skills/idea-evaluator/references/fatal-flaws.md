# Contribution risks and blocking claims

Apply the [shared topic-selection policy](../../shared-references/topic-selection-policy.md).
The historical filename is retained for compatibility. These are diagnostic
questions, not ten automatic rejection rules or predictions of reviewer behavior.

## Checks

| ID | Potential issue | Evidence needed | Appropriate response |
|---|---|---|---|
| F1 | No substantive delta | A verified closest work and relevant passages already establish the proposed claim, with no meaningful remaining contribution | Revise the contribution or STOP_CURRENT_VERSION when the shared stop condition holds |
| F2 | Venue/track mismatch | Current official scope and contribution-type requirements, not a few sampled titles | Reconsider the venue/track; separate venue fit from scientific value |
| F3 | Uninformative comparison | The baseline/control cannot test the stated improvement or causal claim | Add the relevant comparator or narrow the claim; recency alone is not the criterion |
| F4 | Value unclear | No identifiable scientific/practical use has been articulated | Clarify the beneficiary or changed understanding; a specialized research audience counts |
| F5 | Resource/expertise gap | Concrete unmet requirements of the appropriate study | Check acquisition, collaboration, scope and budget; PARK if a prerequisite is unavailable |
| F6 | Claim cannot be tested by the design | A specific mismatch between claimed generality/mechanism and planned observations | Design the decisive comparison or revise the claim |
| F7 | Access/ethics prerequisite | Applicable, verified data/access or human-subject requirements | Secure the prerequisite before dependent work; do not equate pending access with poor novelty |
| F8 | Scope exceeds feasible evidence | Specific claims lack necessary tests within the agreed budget/time | Prioritize coherent claims; no contribution-bullet count or forced paper splitting |
| F9 | Technique without demonstrated purpose | No defined question that the technique can usefully answer | Establish a meaningful question/use; solution-first exploration itself is legitimate |
| F10 | Overclaim or unexamined limits | A claim exceeds the observed conditions, or a plausible failure changes its interpretation | Bound the claim and test the relevant concern; do not invent a quota of failure cases |

For F1, compare question, mechanism, setting/assumptions, evidence and conclusion.
A combination of known components or a small method change can be valuable;
neither a familiar template nor a cosmetic difference settles its contribution.
Unverified metadata, title similarity and failed retrieval cannot establish F1.

## Severity and decisions

Assess severity by the effect on the **specific claim**, rather than the number
of issues, weeks of work, baseline age or student profile:

- **Claim-invalidating:** reliable evidence contradicts/covers the proposed claim.
  Withdraw or revise it. Assess the remaining contribution before recommending
  STOP_CURRENT_VERSION.
- **Needs validation:** a central comparison, attribution or uncertainty is
  unresolved. Recommend VALIDATE_FIRST and the decisive check.
- **Execution prerequisite:** access, budget, data or expertise is missing. State
  the acquisition choice; PARK when it prevents justified work now.
- **Non-blocking improvement:** useful clarification or extra coverage that does
  not determine the current claim. Do not escalate it into a rejection reason.

Two major issues do not become a critical one by counting. Strong performance
cannot compensate for an invalid claim, but an invalid claim does not automatically
erase a distinct contribution. Use the shared four decisions in the final output.

## Data contradicting the mechanism

Before calling a mechanism refuted, check implementation and measurement validity,
comparable budgets/settings, uncertainty and whether the tested metric is the one
the claim concerns. Distinguish a real refutation from a single noisy loss,
missing data or a comparison that does not isolate the mechanism.

If adequately informative valid controls contradict the claim, do not headline
it as supported, invent a passing threshold or promise that more runs will rescue
it. Withdraw that claim. A systematic negative result, failure boundary or corrected
attribution may itself have research value; assess that explicitly and request any
needed scope change. Retain the negative evidence. For inconclusive results, state
VALIDATE_FIRST with a bounded next check rather than continuing spending indefinitely.
