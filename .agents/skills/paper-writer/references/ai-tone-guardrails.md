<!-- Copy. Canonical: paper-polish/references/ai-tone-guardrails.md;
     synchronize the body, LICENSE-humanizer and LICENSE-academic-humanizer
     from there. -->

# Academic prose: clarity and AI-tone checks

Use these patterns to find unhelpful prose, not to diagnose who wrote it. Except
for the explicit author style rule below, a word, punctuation mark, or sentence
shape alone does not justify an edit. Read the paragraph's purpose and the
author's sample, when supplied, before changing it. Keep clear, precise prose
unchanged when it already follows the author's style requirements.

## What to improve

- **Empty lead-ins and importance claims:** start with the finding or argument
  instead of announcing its importance. Replace grand framing with facts already
  present; never invent a concrete detail to make a sentence livelier.
- **Repeated endings:** remove a closing line that only repeats the paragraph.
  Retain an interpretation or consequence that adds meaning. Abstracts and
  conclusions legitimately summarize; do not treat all repetition as filler.
- **Mechanical rhythm:** vary repeated openings when this improves readability.
  Keep a list of three when there are three distinct items; do not merge away
  information or rename the same technical object merely to vary the language.
- **Decorative phrasing:** shorten inflated adjectives, empty participial tails,
  and needlessly elaborate verbs when they add no meaning. A familiar word such
  as "significant", "robust", "represents", or "attention" may have a precise
  technical use and must not be removed through keyword matching.
- **Vague attribution:** use an existing specific source when available. Flag
  missing support separately; do not invent a citation or silently delete a
  substantive argument because its reference needs checking.
- **Formatting and chat residue:** remove assistant greetings, drafting offers,
  explanations of the drafting process, and accidental formatting clutter. Keep
  material methods, evidence provenance, reproducibility details, usage disclosures,
  the venue's headings, proper names, quotations, citation commands, equations,
  labels, and meaningful typography.

Do not impose blanket bans on curly quotes, passive voice, or hedging.
Do not add personal opinions, anecdotes, invented experience, or deliberate
errors to make academic writing appear more human.

## Complex-sentence checks

Inspect English sentences longer than about 30 words or with three or more
subordinate clauses for buried main clauses, unclear attachments and competing
ideas. These counts are inspection cues, not pass/fail limits. Keep a long
sentence when its meaning and relationships are already clear.

When readability needs repair, bring the main clause forward, remove empty
clauses or split separable ideas. Carry each condition, qualifier and comparison
with its original claim; keep references clear and preserve inference strength.
Protect definitions, equations and technical terms. Re-read the neighboring
sentences to check flow after splitting.

## Locate before rewriting

Before editing an existing passage, identify its location (section/paragraph and
a short text span), the concrete wording or readability problem, and the proposed
change. Keep brief notes in working context or existing edit notes; group
repeated mechanical corrections. The current writing agent performs this check
within the editing task, without a separate audit file or review round.

After rewriting, apply the [final comparison](#final-comparison) against the
original. Use the existing delivery notes for meaningful changes and unresolved
meaning risks; keep the working notes out of manuscript prose.

## State supported claims directly

State the supported finding or argument directly, with necessary qualifications
beside the relevant claim. Report negative and null findings just as directly.
Apply these acceptance rules during drafting, polishing and requested review:

- **Purposeful qualifications:** retain a concession, disclaimer or negative
  preamble only when it contributes a concrete factual, inferential or scope
  distinction. Delete imagined objections and ornamental contrasts that add none.
- **Evidence-based strength:** preserve the warranted strength of an observation
  or argument. Changes to claim strength follow the
  [claim-preservation policy](../../shared-references/claim-preservation.md).
  Remove labels added solely to sound modest; correct actual overstatement.
- **One expression per uncertainty:** express each source of uncertainty once
  within a proposition. Combine redundant hedges while retaining distinct sources
  of uncertainty and the difference between an observation and its explanation.
- **One full treatment per boundary:** explain a boundary once and retain only
  necessary short scope qualifiers elsewhere. Follow explicit user or verified
  venue requirements for a self-contained restatement.
- **Contribution established by evidence:** let the results and argument carry
  the contribution. Omit automatic "despite these limitations" defenses and
  assurances that the work remains valuable or robust. Any substantive robustness
  claim needs its own relevant evidence.

During the final edit, temporarily remove a suspected defensive sentence. If the
facts, inference strength and applicable scope stay intact, delete it; otherwise
retain the shortest sufficient wording. Keep this comparison in working context.
Preserve real competing explanations, meaningful comparisons, explicit negations,
negative findings, actual uncertainty and necessary disclosures. These rules
evaluate the sentence's function, not whether it contains a particular word.

## Author style: dash restriction

The author requires no em dashes or en dashes as sentence connectors or
parenthetical breaks in research prose. This includes double/triple-hyphen
substitutes and LaTeX commands that render a prose dash. Rewrite the sentence
with commas, parentheses, a colon, a semicolon, or a full stop as appropriate,
preserving the claim, scope, and uncertainty. Do not substitute another dash.

Preserve numerical ranges, mathematical minus signs, compound-term hyphens,
code and command syntax, identifiers, proper names, exact quotations, and
source-faithful bibliographic titles. Inspect each occurrence in context;
do not run a global character replacement.

Apply this required style rule during drafting, polishing, and review. Record
violations as presentation corrections, normally MINOR, rather than scientific
defects or evidence of AI authorship. Occurrence counts do not make them MAJOR.

## Preserve the contribution and its boundaries

Words such as "first", "best", "superior", "proves", "首次", and "最优" call
for checking the supporting claim and scope, not automatic weakening. Formal
proofs and measured comparisons can justify strong wording. If support cannot
be checked from the supplied material, flag the uncertainty to the author.
Do not replace "best" with "competitive" or "demonstrates" with "suggests"
as a cosmetic edit: those changes can alter the scientific claim.

Likewise, repeated "might", "potentially", and "to some extent" do not make
an established result more accurate. Remove duplication without turning an
uncertain explanation into a fact. Keep real negative results and limitations;
style editing must neither hide them nor expand them into rejection arguments.

## Examples (wording demonstrations, not facts about a paper)

| Before | After or decision |
|---|---|
| "It is important to note that the controller logs each intervention." | "The controller logs each intervention." |
| "These results might potentially suggest that caching reduces latency on this benchmark." | If the hedges express the same uncertainty: "These results suggest that caching reduces latency on this benchmark." Preserve any distinct uncertainty and the benchmark boundary. |
| "We compare accuracy, latency, and memory use." | Keep all three metrics; this is an informative list. |
| "Unlike the fixed-budget baseline, our method reallocates unused calls." | Keep the comparison when the source supports it. |
| "Our method achieves the lowest measured latency among the evaluated systems." | Keep the strength and scope if supported; do not replace it with a vague competitive-performance claim. |

## Final comparison

Check the revised passage against the original: numbers, names, citations,
negations, conditions, uncertainty, rankings, and distinctions must retain their
meaning. Protect research content and the author's requested degree of rewriting.
Apply the direct-claim acceptance rules above before marking the prose complete.
Deliver the polished text with brief notes only where useful; an internal style
checklist does not belong in the manuscript. Evaluate readability and fidelity,
not a detector score or a promised classification as human-written.

## Source and local adaptation

Selected editing patterns adapted from [blader/humanizer](https://github.com/blader/humanizer)
at `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8` (MIT; copyright 2025 Siqi Chen).
The upstream [license](LICENSE-humanizer) is retained. This academic adaptation
uses contextual judgment for AI-tone checks, applies the author's scoped dash
restriction, preserves supported claims, and follows the existing
paper-polish delivery rules. Humanizer is not installed as a separate skill.

Complex-sentence cues and the locate-before-rewrite procedure are selectively
adapted from [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer/blob/main/SKILL.md),
version 0.3.3 (accessed 2026-10-10), Process and Layer 2.11. Its
[license](LICENSE-academic-humanizer) is retained. The local adaptation treats
length as an inspection cue and keeps edit notes within the current task.
