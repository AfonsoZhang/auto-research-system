# Integrity patterns: what a reviewer-side audit will look for

Reviewer-side forensic tools such as
[Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch) check
machine-assisted papers for self-contradiction and fabrication signs, grouped in
families A–H. This file maps each family to the step in this system that must
prevent it, so the author side finds the defect first.

**Fix the evidence, not the wording.** A finding is resolved by correcting the
number, adding the missing run or baseline, or narrowing the claim to what the
evidence supports ([claim-preservation](claim-preservation.md)). Rewording a
passage so a check no longer matches, while the defect remains, is not a fix
and must not be proposed.

| Family | Typical defect | Prevented by | Checked by |
|---|---|---|---|
| A · Numeric self-consistency | Abstract number absent from tables; wrong relative delta; best seed reported as mean; GRIM-impossible percentage; p value contradicting its statistic; points vs percent; appendix contradicting body | `analyze-results`, `paper-writer` (claims trace to supplied results) | `paper-claim-audit` deterministic pre-check (Step 1b) and failure modes 1–10 |
| B · Method and scope | Method says "no labels" but evaluation uses them; "comprehensive" over two datasets; credit to a component never ablated alone; causal claim without an intervention | `experiment-plan`, [claim-preservation](claim-preservation.md) | `paper-claim-audit` 7, `pre-submission-reviewer` §1 |
| C · Baseline integrity | Missing recent baseline behind a "SOTA" claim; baseline given less tuning or compute; win inside overlapping error bars | `experiment-plan` (credible baselines with matched preprocessing, evaluation and resources), `benchmark-research-skill` | `paper-claim-audit` 3, `pre-submission-reviewer` §1 |
| D · Experiment integrity (needs code and results) | Ground truth produced by the evaluated model; self-normalized scores; result file or metric key that does not exist; placeholder data feeding a figure; released code not reproducing the numbers | `experiment-bridge` (logged raw outputs), `run-experiment` (commands and failures recorded) | `paper-claim-audit` 11 |
| E · Citation integrity | Nonexistent reference; real paper cited for a claim it does not make; retracted paper used as support | [citation-discipline](citation-discipline.md), `paper-writer` verification ladder | `nature-ref-verifier`, `pre-submission-reviewer` §1 |
| F · Surface signals (never a verdict alone) | Duplicated tables; template strings left in the text; decorative generated image presented as a figure; page padding | `nature-figure` (evidence figures from data), `paper-polish` | `paper-claim-audit` pre-check, failure modes 10 and 12, `pre-submission-reviewer` §4 |
| G · Proof integrity | Skipped lemma; circular proof; invalid step; symbol changing meaning; unstated assumption | `paper-writer` | `pre-submission-reviewer` (proofs for formal claims) |
| H · Evaluation design | Train/test leakage or pretraining contamination; LLM judge from the evaluated model family or never checked against humans; declared dataset, seed or metric silently dropped | `experiment-plan` (conditions, splits and metrics fixed before results), `analyze-results` (failed and missing runs kept) | `pre-submission-reviewer` §1 |

Writing-style impressions (defensive hedging, stock phrases, bullet walls) carry
no integrity weight in such audits; `paper-polish` handles them as prose quality.

## Optional independent check

Before submission, an author may run the reviewer-side tool on their own paper
directory (installation and usage in its README). Treat its output like any
external review: verify each finding against the files, fix real defects at
their source, and record false positives with the reason. Its verdict does not
replace `paper-claim-audit` or the user's decision to submit.
