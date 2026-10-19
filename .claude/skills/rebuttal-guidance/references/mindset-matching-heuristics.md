# Reviewer-mindset matching heuristics

Score signals in the review from 1 (low) to 5 (high), then compare their combination
with the cluster descriptions.

## Behavioral signals

| Signal | High (5) | Low (1) |
|---|---|---|
| **Openness** | "willing to raise", "if addressed", "open to" | "reject", "not convincing", "final decision" |
| **Severity** | "fundamental flaw", "fatal issue", "strong reject" | "minor concern", "small issue" |
| **Constructiveness** | "I suggest", "would strengthen if", "recommend adding" | Rejection without a repair path |
| **Specificity** | Table 2, Sec 3 or equation references | "overall not convincing" without a specific target |
| **Skepticism** | "not convinced", "insufficient evidence", "doubtful" | Neutral wording without expressed doubt |
| **Harshness** | "reject", "misleading", "wrong", "unacceptable" | Polite or indirect wording |
| **Actionability** | "add experiment", "compare to X", "ablation needed" | No executable suggestion |

## Six-pattern quick reference

| Pattern | Typical signal combination | Historical score-increase reference | Core strategy |
|---|---|---|---|
| **Precise Constructive** | High constructiveness, specificity and actionability | ~36% | Structured responses with specific manuscript references |
| **Mild Skeptic** | Low severity and actionability; vague wording | ~19% | Resolve confusion directly and confidently without overexplaining |
| **Experiment-oriented** | Repeated evidence_gap concerns and comparison requests | See mindset-library | Add experiments or explain why current evidence suffices |
| **Highly skeptical and severe** | High skepticism and severity; low score | ~7-15% | Prioritize evidence, calibrate claims and acknowledge limitations |
| **Forceful with multiple concerns** | High harshness, multiple concerns and long review | ~12% | New experiments, direct manuscript references and concrete commitments |
| **Other** | No clear match | - | Identify the strongest individual signal first |

For detailed score-increase rates and Cohen's d values, see
[mindset-library.md](mindset-library.md).

## Matching procedure

1. Score 5–7 signals and retain the exact phrases supporting each score.
2. Select the closest pattern from the combination of signals.
3. If two patterns are close, label primary and secondary.
4. Confidence: at least 3 aligned signals supports a high-confidence match;
   a very short or generic review supports only low confidence.

## Effect of matching confidence

| Confidence | Action |
|---|---|
| High | Use the matched success_patterns to guide the strategy |
| Medium | Give primary and secondary matches and explain the strategy differences |
| Low | Use general guidance and state that the mindset match is uncertain |
