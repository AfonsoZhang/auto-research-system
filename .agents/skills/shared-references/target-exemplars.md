# Target exemplar notes

Local procedure, added 2026-10-19, for steps 2–3 of
[target calibration](paper-type-routing.md#calibrate-to-the-selected-target).
The idea of a per-paper exemplar knowledge base follows open-scholar-skill's
`scholar-write` asset library; the content here is rewritten for local rules
(moves and measurements, no verbatim text store, no pass/fail norms).

## Select the papers

- **Target set:** 3–6 accepted papers from the target venue and track, normally
  the last one or two cycles, closest in topic and contribution type.
- **Bar set:** 2–4 same-topic, same-type papers from venues one or two tiers higher.
- If fewer suitable papers exist, use what exists and say so. Do not pad with
  off-type papers; a survey or position paper does not calibrate a method paper.
- Each paper must already be (or be added) in `literature/publication_records.json`
  under [publication-policy.md](publication-policy.md); reference it by that record
  key, not a second bibliography. Track/year are confirmed as in step 2.
- Read the selected full text (local library, Zotero, open-access version or
  `nature-reader`). An abstract-only entry is labeled `abstract-only` and is not
  used for structure or evidence measurements.

## Record each paper

Write `literature/target_exemplars.md` in the current topic directory; reuse and
update an existing file. One entry per paper:

- **Identity:** record key, venue/track/year, role (`target` / `bar` + tier source),
  contribution type, why selected.
- **Structure:** section order, rough share of Introduction / Method / Experiments /
  Discussion, figure and table counts, what Figure 1 does.
- **Moves** (own words + section/page locator): opening hook type, how the gap is
  established, how contributions are stated, how results are led in, where
  limitations sit.
- **Evidence depth:** datasets/benchmarks, number and kind of baselines, ablations
  or controls, statistics (seeds, std, CI, tests), error/failure analysis, released
  artifacts.
- **Prose:** register, paragraph length, Introduction citation density, how claims
  are qualified.

Mark counted values separately from estimates.

## Synthesize

Put a short synthesis at the top of the file:

- **Target norms:** ranges and spread across target entries. A common practice is
  a reference point, not a requirement.
- **Bar delta:** what bar papers do that target papers typically do not (framing,
  evidence completeness, figures, prose).
- **Gaps for this paper:** compare with the current outline or draft. Label each
  gap `writing` (fixable within the requested scope), `evidence` (route to
  [experiment-plan](../experiment-plan/SKILL.md)) or `claim` (route to
  [claim-preservation.md](claim-preservation.md)).

Only verified venue rules from step 1 are hard requirements. Exemplar-derived
norms yield suggestions or warnings, never pass/fail verdicts; conformity to a
majority layout is not scientific quality. Apply contribution-type routing first.

## Text boundary

Store no verbatim sentences, full abstracts or full-text extracts in the project.
Describe each move in your own words with a locator so it can be reread at the
source; established technical terms are fine. Keep PDFs in the existing library,
not in the project. When drafting, adopt the move, never the wording.

Record the check date; refresh when the target cycle or contribution type changes.
