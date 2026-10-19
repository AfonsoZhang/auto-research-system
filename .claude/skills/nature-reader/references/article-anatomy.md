# Article Anatomy — a reading aid (Nat Commun 2025 CS/AI corpus)

Use this file as a **reading aid** while building the bilingual reader, to label
the *argumentative function* of each block so the reader can locate the gap, the
contribution, the decisive result, and the self-contained figure legends. It is
distilled from a 2025 set of 20 open-access *Nature Communications* computer
science / AI papers across genres.

> This is an aid for **locating structure**, not a license to summarise. The
> `core/principles.md` contract still holds: translate every block for meaning,
> keep the bilingual side-by-side, and never degrade to a summary-only output.
> Use the function labels to help a reader navigate, e.g. in a short orientation
> note, not to replace the full translation.

## Where each function lives

- **Abstract = a funnel.** Read it as five moves: field value → gap (almost
  always after **However**) → hinge `Here we show/present X` → one quantified
  result → significance. The hinge sentence is the fastest way to state what the
  paper actually contributes.
- **Introduction = hook → gap → contribution.** Gap signal words to spot:
  **However / remains / Unfortunately / underexplored / the scarcity of … /
  Without X, Y cannot be …**. The contribution is the explicit `Here we… / In
  this work, we…` sentence, often with a `(Fig. 1)` pointer.
- **Results = conclusion-first.** Each paragraph opens with the judgement; the
  figure call (`Fig. Xa`, or `Figure X shows…`) and the numbers follow.
  Subheadings are often conclusions or method names, so the subheading list
  alone sketches the evidence ladder.
- **Figure/Table legends are self-contained.** `Fig. N | bold noun title`, then
  `a/b/c` panels, with `n=`, error type, and test written in. A legend's last
  sentence sometimes advances a claim (*"…indicating that the models are not
  predicting poses based on physics…"*) — flag it; it is interpretation, not
  description.
- **Discussion = restate contribution → why credible → wider meaning → limits
  (`Another limitation…` / `remains to be tested`) → future work.** The limits
  sentence is where the paper bounds its own claim.

## Genre tells (so the reader frames the paper correctly)

- **Research article**: own data, IMRaD, `we` + passive.
- **Review**: chapters by topic/modality synthesising others' citations, little
  own data, closes with `Conclusions and outlook`.
- **Perspective**: history/era hook, numbered argument, normative `X should…`,
  roadmap close.
- **Comment**: first-person `I`, rhetorical-question opening, analogy/history,
  no IMRaD, no figures.
- **Benchmark/framework**: the gap is "the field lacks an agreed standard";
  tables dominate; stresses community / reproducibility / versioning.

## Reading guidance for Chinese-language delivery

For an explicitly requested bilingual reader, navigation notes may label paragraphs
as background, gap, contribution, result or limitation. These labels do not replace
the requested paragraph-level aligned translation.

Gap cues include however, remains challenging, few studies, lacks, and cannot do Y
without X. Here we or an equivalent source-language phrase often introduces the
stated contribution. Captions are often self-contained, including sample size, error
measures and tests; distinguish an interpretive final sentence from visual description.
Identify the article type first: research article, review, perspective, commentary
or benchmark. Interpret its organization and tone accordingly.
