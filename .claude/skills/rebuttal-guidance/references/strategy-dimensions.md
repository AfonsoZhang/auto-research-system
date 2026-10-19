# Rebuttal strategy dimensions (Y vector)

Ten dimensions derived from the historical successful/unsuccessful rebuttal data,
scored from 1–5. **overpromise_risk** and **vague_future_work** are risk dimensions:
higher values indicate greater risk.

## Ten dimensions

| Dimension | Meaning | Writing guidance |
|---|---|---|
| **direct_address** | Address the concern directly | Give each W/Q its own heading |
| **specific_evidence** | Use numbers, figures and comparison results | Support "significantly improve" with relevant numbers |
| **new_experiment_strength** | New experiments target the concern | Explain their relationship to the central claim |
| **clarification_quality** | Clear explanation tied to the manuscript | 2–4 sentences plus a Section/Table pointer |
| **controlled_concession** | Acknowledge valid limitations without excessive retreat | Follow with the corresponding improvement or justified scope |
| **structure_quality** | Traceable W/Q organization | Use headings and numbered lists |
| **tone_confidence** | Confident, respectful and nondefensive | Avoid "you misunderstood" |
| **paper_grounding** | Claims tied to precise main-text/appendix locations | Do not introduce claims absent from the paper |
| **overpromise_risk** ↓ | Commit only to deliverable actions | Avoid unrealistic claims such as "fully solve" |
| **vague_future_work** ↓ | Address what can be addressed now | Deferral to future work can signal evasion |

## Priorities conditional on mindset

Read the matched cluster in `mindset-library.md`:

1. **rule_diff Top 3:** the 3 largest differences between successful and unsuccessful
   groups; positive means higher in the successful group.
2. **Cohen's d:** the inherited rule treats d > 0.8 as substantial group separation.
3. **success_patterns / failure_patterns:** concrete strategy descriptions extracted
   by an LLM.

Emphasize positive differences and treat negative ones cautiously: higher values in
unsuccessful cases may indicate excessive remedial effort.

## Strategy combinations

The source analysis reports higher success when these dimensions co-occur:

- `direct_address` + `specific_evidence`: the core combination.
- `specific_evidence` + `paper_grounding`: data tied to manuscript locations.
- `new_experiment_strength` + `specific_evidence`: new experiments with actual numbers.
- `tone_confidence` + low `overpromise_risk`: confidence without exaggeration.

## Per-concern annotation

```text
R1.W2 → Prioritize: specific_evidence, paper_grounding, clarification_quality
         Avoid: high overpromise_risk, vague_future_work
```
