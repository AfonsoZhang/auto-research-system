# Per-section drafting guidance

## Table of contents

1. Abstract
2. Related Work
3. Methods
4. Results
5. Discussion
6. Conclusion
7. Future Work

Content contracts for drafting each non-Introduction section. The evidence
discipline applies throughout; this file adds the per-section form.
(Introductions have their own skill: intro-drafter.)

## 1. Abstract

Follow the requested venue's length and format. Organize around the problem or
gap, key approach, decisive supported finding and significance; sentence counts
follow the content. State the finding's information beyond an obvious restatement
of the setup, using actual measurements where useful. Apply
[abstract and findings guidance](../../shared-references/abstract-and-findings.md):
detailed limitations belong elsewhere by default, with only necessary scope
qualifiers retained here. A central negative or boundary result is still a finding.

No citations in the abstract. No undefined acronyms. Any name introduced
(framework, dataset, model) must appear again in the paper. No superlatives.
Write it last.

## 2. Related Work

Organize as themes, not as a chronological list. Two to four themes is
typical. For each theme: state the line of work, name two to four
representative works with a brief note on their approach, and end with one
sentence naming the specific limitation this paper addresses. That closing
sentence ties the theme to the paper's argument.

Do not write "for a survey, see ...". Do not write "while many works have
explored ...". Each paragraph should leave the reader knowing exactly where
this paper sits.

## 3. Methods

Open with a one-paragraph overview: name the framework (one sentence), state
the pipeline (one to two), list the modules (one per module). This paragraph
mirrors the Introduction's solution overview.

For each module, a subsection that states its purpose (which challenge it
addresses), describes the technical mechanism, optionally walks the paper's
running example through it, and notes practical implementation
considerations.

Equations: include only those the user supplied, or where a formal statement
is genuinely necessary for the mechanism. Never invent an equation. If a
formal expression is needed but the user has not provided one, write the
mechanism in prose, omit the equation, and raise it in the delivery note as
something for the author to supply. Format: `$$...$$` display, `$...$`
inline.

## 4. Results

Open with a brief paragraph naming the evaluation setup (datasets, baselines,
metrics), using only values the user actually gave.

For each result, follow describe-then-interpret: first state what was
observed (the number, the comparison, the trend), then what it means (which
challenge it resolves, which hypothesis it supports, which baseline it beats
and why).

Never invent numbers. If a result calls for a value the user did not give,
write qualitatively ("outperforms prior baselines by a substantial margin,
with exact values in the results table") and name the actual table from the
user's materials; if no such table exists yet, say so in the delivery note
rather than inventing a reference.

Keep observation and inference distinct: "we observe X" versus "this suggests
Y". Never collapse the two.

## 5. Discussion

The Discussion is where the paper earns its venue tier. Three layers:

1. **Mechanism**: explain why the results are what they are, connected to the
   paper's key idea. If the user gave a mechanism hypothesis, develop it; if
   not, propose the most plausible mechanism consistent with the observed
   results and label it plainly as a working hypothesis.
2. **Connection to prior work**: relate the findings to the limitations of
   prior work. Cite specifically where the user supplied references;
   otherwise search with the session's literature capability, and if nothing
   suitable is found, keep the connection at citation level or drop it. Never
   patch the gap with a placeholder.
3. **Limits and future work**: select consequential boundaries, explaining what
   each changes about a particular inference or use. An untested setting alone
   is not an informative limitation. Apply the
   [Limitations admission gate](../../limitation-and-risk-writer/SKILL.md#admission-gate-all-four-conditions-required)
   before drafting. Do not repeat a constraint and consequence already treated
   elsewhere; zero new limitations is allowed. Apply the writer's
   [length budget](../../limitation-and-risk-writer/SKILL.md#length-budget-hard-acceptance-limits),
   including a measured final word count and the distinct-point cap. No minimum
   count or obligatory future-work list.

Voice discipline is critical here: "is consistent with" for agreement with
prior reports; "suggests that" for supported hypotheses; "we hypothesise
that" for proposed but untested mechanisms; "would require further
validation" for tentative claims. Avoid "proves", "demonstrates
conclusively", "establishes", unless the user stated the experiment provides
that level of proof.

## 6. Conclusion

Answer the research question with the decisive supported finding and its useful
implication. Explain what the evidence adds beyond the setup or a predictable
truism. Include a next question only when it follows meaningfully from the finding;
no compulsory future-work paragraph or limitations recap.

Do not summarise section by section. Do not introduce new material. Do not
repeat the Abstract.

## 7. Future Work (when separate from the Conclusion)

When requested or useful, state a specific remaining question, why it matters,
and a feasible next experiment or extension. Select what follows from the findings;
do not fill a fixed number of items or list every possible extension.
