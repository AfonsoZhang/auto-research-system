# Concern classification

Classify each Weakness / Question before selecting a response strategy.

## Categories

| Type | Signals in the review | Priority strategy | Template |
|---|---|---|---|
| **misunderstanding** | "seems", "unclear whether", contradiction with the manuscript | clarification_quality + paper_grounding | A |
| **evidence_gap** | "more experiments", "ablation", "only one dataset" | new_experiment_strength + specific_evidence | B |
| **novelty** | "incremental", "similar to X", "limited contribution" | specific_evidence + explicit differentiation; controlled_concession when needed | A or C |
| **baseline_fairness** | "unfair comparison", "weak baseline", "missing SOTA" | Additional comparison + protocol explanation | B |
| **scope_claim** | "overclaim", "overstated", "not supported by evidence" | controlled_concession with justified claim scope | C |
| **writing_clarity** | "hard to follow", "notation", "organization" | Revision + example + manuscript pointer | A |
| **theory** | "proof", "assumption", "bound", "convergence" | Equation/proof pointer or acknowledgment of a limitation | A or C |
| **efficiency** | "complexity", "scalability", "overhead" | Complexity analysis + measured latency | B |
| **other** | No clear match | Restate, then classify again | Depends on content |

## Weaknesses and Questions

| | Weakness | Question |
|---|---|---|
| Reviewer intent | Identifies a flaw | Requests understanding or confirmation |
| Response focus | Evidence and revision when needed | Concise answer and Section/Table pointer |
| Common mistake | Explanation without action | Excessive apology |

## Keyword cues

```text
novelty:     novel, contribution, incremental, original, marginal
experiments: experiment, baseline, ablation, dataset, evaluation
writing:     clarity, unclear, confusing, notation, presentation
theory:      proof, theorem, assumption, bound, convergence
efficiency:  scalable, complexity, computation, overhead, efficient
scope:       limitation, generalize, broader, overclaim, overstated
```

## Compound concerns

Split a Weakness combining novelty and evidence_gap into sub-concerns and give each
its own strategy. Prioritize the reviewer's central concern, often stated first.
