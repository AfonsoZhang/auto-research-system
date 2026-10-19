---
name: limitation-and-risk-writer
description: >-
  Draft or revise a paper's Limitations section from the author's perspective,
  admitting only grounded, non-obvious limitations not already explained in
  the body. Use for limitations writing, semantic deduplication, generic caveats
  or excessive self-criticism. Works from manuscript evidence and known
  constraints; not a reviewer, rebuttal, or topic-rejection workflow.
license: MIT
metadata:
  upstream-author: AIPOCH
  upstream-repo: https://github.com/aipoch/medical-research-skills
  upstream-commit: 686e09dfdb45d9fa1a08664f06bb93769b3c9d91
  local-adaptation: author-perspective-evidence-bound
---

# Author-perspective Limitations writing

For substantive claim creation or revision, follow the [cross-revision claim-preservation policy](../shared-references/claim-preservation.md).

Write the boundary of what this paper establishes. Preserve contributions that the
evidence supports and state material constraints accurately. Do not turn the section
into a rejection argument, an experiment wishlist, or generic reassurance.

## Inputs and scope

Use the available manuscript, methods, results, tables, experiment records, and the
author's known constraints. Reuse material already supplied. Establish the main
contribution and its actual claimed scope before deciding which limitations matter.
If a consequential detail is missing, finish only the portion whose evidence and
body comparison can be checked, and identify the missing detail. Do not fill gaps
with plausible weaknesses or mitigation measures.

Before content drafting or substantive revision, read the current Introduction,
Methods, Results, Discussion and Conclusion, plus relevant captions/appendices.
Locate existing scope statements, assumptions, failure analyses and caveats by
meaning, not keyword matches. Reuse an existing coverage map only after checking
that it matches the current body. A supplied Limitations paragraph alone cannot
establish that a candidate is new to the paper. If the body is unavailable, report
that missing input instead of producing a supposedly deduplicated final section.
A narrowly requested language edit may preserve the supplied content, but must
not claim that body-level redundancy was checked.

For a planning-stage paper without results, keep design boundaries and open factual
questions in planning notes. Only a grounded additional consequence can become a
provisional limitations bullet; a scope inventory cannot. Do not describe imagined
failures or planned experiments as observed results.

## Decide what each candidate actually means

| Kind | Evidence needed | Writing decision |
|---|---|---|
| Observed limitation | A result, error analysis, assumption, or documented constraint with a specific consequence | Admit only through the gate below; an already explained failure is not new Limitations content. |
| Untested range | The evaluation scope establishes that a relevant setting was not tested | An untested setting alone is ineligible. Require an additional grounded consequence for an actual claim or use; do not infer poor performance. |
| Deliberate scope | The stated research question and design genuinely bound the work | Keep an adequate scope statement in its existing location. Do not recast the exclusion as a weakness merely to fill this section. |

An untested range becomes important if the paper claims results beyond the tested
range. Identify the unsupported part and the smallest justified body-text correction
under the claim-preservation policy; retain the supported finding and its useful
implication. Do not repeatedly narrow a claim that already accounts for this boundary. Do not relabel a missing
control, invalid comparison, or contradictory result as a deliberate scope choice
when it is necessary to establish the paper's own central claim.

## Admission gate: all four conditions required

For each candidate, keep a compact eligibility record in working context or
existing notes: source locator, affected claim/use, closest body passage, added
consequence and decision. This is a source comparison, not a reviewer score or a
new required artifact. Only `KEEP_NEW` candidates may become new limitations prose.

1. **Grounded:** identify an actual result, design choice, assumption or documented
   dependency and its source location. A reasoned consequence of the design may
   qualify without another experiment; label an unobserved consequence as a risk.
   Unsupported plausibility gets `NEEDS_SOURCE`, not a hedged invented limitation.
   A small sample count alone does not establish low statistical power, and a
   narrow test set alone does not establish poor generalization.
2. **Consequential:** name the particular claim, inference or intended use affected
   and what changes about its interpretation. Restating a setup fact, declaring
   uncertainty or asking for more experiments does not pass this condition.
3. **Non-obvious:** write only non-obvious limitations. Otherwise use `DROP_GENERIC`.
4. **Additional to the body:** compare constraint AND consequence against the
   current manuscript. If already explained, use `DROP_REPEAT`, even when true
   or important. Synonyms, a longer paraphrase, a mitigation/future-work sentence
   or a more cautionary tone do not count as added information. If only the setup
   fact appears in the body, admit only a grounded additional consequence that
   passes the other conditions; its obvious negative restatement is insufficient.

Failing any condition excludes the candidate from new section prose. Do not
rewrite a rejected point repeatedly until it looks specific. Merge accepted
points with the same underlying constraint and consequence; do not split them
into differently named categories. Recheck the actual composed sentences against
the body, since drafting can reintroduce excluded material.

If a candidate exposes an unsupported central claim, use `AUTHOR_FIX`: identify
the needed body correction to the author. A limitations paragraph must not serve
as a disclaimer that leaves the stronger body claim intact. This does not authorize
unrequested edits to other sections or a new experiment.

## Empty result and required sections

Zero admitted points is allowed. Omit an optional section or return a short author
note that no additional qualifying limitation was found in the supplied material.
Do not assert that the research has no limitations. Do not fill a word target or
invent an exotic weakness to avoid an empty result.

Preserve material disclosures where they are already adequately explained in the
body. Materiality requires accurate disclosure, not duplicate paragraphs. If a
separate section is explicitly required by the user or verified venue instructions,
use the shortest permitted cross-reference to existing discussion. Only an explicit
self-contained disclosure requirement justifies the minimum necessary restatement;
"readers expect it," genre conventions and a desire for balance are not exceptions.
Do not silently remove a required section.

## Length budget: hard acceptance limits

Default to **at most 250 English words total and two distinct admitted points**.
These are local author preferences, not venue standards. There is **no minimum**
word or point count; do not aim to fill the allowance. Prefer one compact paragraph.
An explicit user instruction or a verified incompatible venue requirement can
override the relevant limit; record that basis in working notes. A required section
does not by itself waive the budget.

Apply the budget to the complete Limitations section or equivalent caveat passages
in a combined Discussion/Threats to Validity section, not to all of Discussion or
to boundary results that are the paper's scientific findings. Count separate
constraint/consequence pairs as separate points even inside one sentence. Do not
evade the budget by moving excess caveats to another heading, footnote or appendix.

Before delivery, the writing agent must measure the final visible prose, for
example with Python `len(plain_text.split())`, rather than estimate its length.
Exclude the section heading, citation markers and formatting commands; include
cross-reference prose, mitigation and future-work sentences. Hyphenated words and
contractions count as one whitespace-delimited word. Keep the count in working
context, outside the manuscript. Recount after edits and check the distinct points.
An over-budget draft is not complete.

First remove failed candidates and duplicate explanations, then retain the most
consequential distinct points and compress their wording. Do not replace removed
text with generic closing remarks or generate new weaknesses to fill spare words.
Preserve material disclosures already adequately explained in the body. If safe
compression cannot retain a necessary disclosure within the active budget, flag
the specific conflict to the author instead of silently exceeding the cap or
hiding it. This check belongs to the writing agent and requires no separate subagent.

## Compose the section

Apply [abstract and findings guidance](../shared-references/abstract-and-findings.md):
retain only candidates that passed this skill's admission gate. The shared rule
does not license repetition of familiar or material constraints. Detailed
limitations belong here or in Discussion, with a single substantive treatment;
only a qualifier necessary to interpret the main result belongs in the abstract.

- Lead with the most consequential interpretation boundary and combine overlapping
  points. Follow the length budget above and the paper's language. Do not impose
  a minimum number of limitations, sentences, paragraphs, or validity categories.
- Describe the constraint and its concrete consequence in natural prose. Add an
  actual mitigation only when the provided evidence establishes it. Add future work
  only when it clarifies a useful next question; it is not required for each point
  or as a closing sentence.
- Calibrate both positive and negative statements to evidence. Keep uncertain
  consequences uncertain; do not hedge established contributions merely to sound
  cautious. Do not add reassurance such as “the conclusions remain robust” unless
  there is evidence for that specific assertion.
- Avoid repeated apologies, blanket statements that undermine the whole study,
  obvious truisms, and formulaic “despite these limitations” endings. The section
  need not repeat strengths or claim novelty to offset a real constraint.
- Preserve material disclosure without duplicating its existing treatment. If a
  real problem undermines a main claim, explain the required correction or narrower
  interpretation to the author; do not conceal
  it, invent a defense, or merely move it into this section while leaving the
  stronger claim unchanged. Flag needed body edits instead of rewriting unrelated
  sections without authorization.

## Calibration examples (illustrative, not evidence for the current paper)

- **English-only tasks already scoped in Methods, no multilingual claim:** reject
  "transfer to other languages remains untested" as `DROP_GENERIC`; it only
  restates the scope and a standard uncertainty.
- **A measured failure and its effect are already explained in Results/Discussion:**
  use `DROP_REPEAT`. Importance and accuracy do not justify another paragraph.
- **Only the model count or budget is repeated, followed by a call for more tests:**
  use `DROP_GENERIC`. Adding an actual number does not add an interpretive consequence.
- **Documented cache identity omits tool-version changes, with no prior discussion
  of this consequence:** a risk that a cached result survives an incompatible tool
  update may qualify as `KEEP_NEW` if the paper's design supports the dependency
  and an intended use is affected. Do not invent an observed failure or rate.
- **A causal claim rests on a baseline that changes two variables together:** use
  `AUTHOR_FIX` for the attribution problem. Preserve independently supported findings;
  do not recast the missing control as a deliberate scope choice.

## Handoff within this installation

- `ts-paper-plan` can supply the contribution, actual research scope, and known
  design constraints, together with existing body passages covering them. At
  planning time, retain only eligible design consequences as provisional outline
  content; a list of untested settings is not a limitations outline. Final prose
  still requires checking the current body.
- When external literature is genuinely needed, reuse `research-lit` records and
  `nature-reader` passages under the [publication/version policy](../shared-references/publication-policy.md).
  A local rewrite does not require a new literature review.
- Existing `claims_map.json` and publication records remain the source for external
  citations; new citations use `ts-paper-cite` / `nature-ref-verifier`. Do not create
  a second bibliography or automatically invoke reviewer agents or another model.

## Delivery

Give admitted Limitations prose or the empty-result author note first. Add brief
notes only for material uncertainty, a needed body-claim correction, or a requested
explanation.
Keep internal evidence checks out of manuscript prose. Follow the user's destination;
independent research lives under `$RESEARCH_ROOT`, not an unrelated project directory.

Before delivery check that no sentence promotes “not evaluated” into “does not work,”
no material disclosure is hidden, and no mitigation, failure, or reassurance was
invented. Each retained point must still pass the admission gate after composition;
drop repetitions and generic filler rather than merely rephrasing them. Supported
contributions should retain their warranted strength. Verify the final word and
point counts against the active length budget before marking the section complete.

Adapted locally from AIPOCH's `awesome-med-research-skills/Academic Writing/limitation-and-risk-writer`
at the pinned revision above. See [LICENSE](LICENSE).
