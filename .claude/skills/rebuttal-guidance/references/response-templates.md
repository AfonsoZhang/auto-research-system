# Response templates

Three base templates for different concern types. This skill produces a guidance
plan, not the final rebuttal text. Keep internal guidance in English under the shared
[language policy](../../shared-references/research-autonomy.md#working-language).

## Overall structure

```text
[Optional: 2-3 opening sentences with thanks and a revision summary]

**R1.W1** [Title]
...

**R1.W2** [Title]
...

**R1.Q1** [Title]
...
```

## Template A: Clarification (misunderstanding / writing_clarity)

```text
**R?.W?** [Restate the concern in one sentence]

Thank you for this comment. It may arise from [specific point requiring clarification].

**Clarification.** [2–4 sentences referring to Sec. X / Table Y / Appendix Z.]

**Evidence.** [One specific fact or number from the paper.]

[If actually revised] We added this explanation in Sec. X (shown in blue in the revised version).
```

**Relevant mindset:** highly constructive reviewers respond to clear clarification.
**Avoid:** explanations longer than 4 sentences or missing manuscript locations.

## Template B: Additional evidence (evidence_gap / baseline_fairness / efficiency)

```text
**R?.W?** [Restate the concern]

We agree that [specific missing evidence] would strengthen the paper.

**New results.** We added [experiment/analysis]:
- [Metric] on [dataset]: our method X vs baseline Y
- See Table N / Appendix M

**Conclusion.** [One sentence explaining how this addresses the concern.]
```

**Relevant mindset:** the source analysis associates experiment-oriented and forceful,
multi-concern reviewers with stronger responses to new experiments (Cohen's d).
**Avoid:** experiments that cannot be completed during rebuttal, or numbers without
actual results.

## Template C: Limitation and scoped claim (scope_claim / novelty / theory)

```text
**R?.W?** [Restate the concern]

We acknowledge [specific limitation]. The contribution applies to [justified scope].

**Retained contribution.** [1–2 sentences establishing its value within that scope.]

**Action.** [Completed or proposed revision/additional analysis, clearly distinguished.]
```

**Relevant mindset:** for highly skeptical, severe reviews raising scope_claim issues,
the inherited guidance favors justified scope calibration over defensive argument.
**Avoid:** concessions without explaining the contribution's remaining value.

## Guidance block produced by this skill

Provide a per-concern guidance plan rather than final response prose:

```markdown
### R1.W2: [Short concern title]
- **Concern type**: evidence_gap
- **Recommended template**: B
- **Acknowledgment**: ImageNet evaluation would strengthen the paper
- **Response angle**: additional high-resolution results, without invented numbers
- **Available evidence**: CIFAR results in Table 2; new table pending actual results
- **Tone**: neutral and confident; avoid defensive wording
- **Avoid**: lengthy clarification without new evidence
```
