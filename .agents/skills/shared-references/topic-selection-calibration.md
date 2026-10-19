# Historical contribution calibration for AI agent research

Read only when this field's contribution scale is relevant to the current task.
These examples supported the local selection policy on 2026-10-05; they do not
define the user's current field, seed new topics or supply a current novelty scan.
Use [topic-selection-policy.md](topic-selection-policy.md) for current decisions.

## Calibration evidence (checked 2026-10-05)

Official criteria, rather than personal experience:

- [ICML 2026 reviewer instructions](https://icml.cc/Conferences/2026/ReviewerInstructions):
  originality can be new combinations or insights into existing methods; soundness
  is distinct from impact. Incremental/specialized contributions still need value
  that others can build on. This is not an automatic acceptance rule.
- [ACL ARR reviewer guidelines](https://aclrollingreview.org/reviewerguidelines),
  H3/H5–H9/H13: analysis, negative findings and simple/narrow contributions are
  legitimate; evidence should support the actual claim, without mandatory SOTA.
- [NeurIPS 2026 Evaluations and Datasets guidance](https://neurips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines):
  evaluation audits/stress tests can contribute new insights when systematic and
  controlled, including rigorously supported negative findings.

Verified formally published examples of focused contributions:

| Work | Venue/track | Focus and evidence |
|---|---|---|
| [LLMCompiler](https://proceedings.mlr.press/v235/kim24y.html) | ICML 2024 | Function-call planning/parallel execution, evaluated for latency, cost and accuracy |
| [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html) | ICML 2025 | Reusable workflows; Mind2Web/WebArena and transfer evaluations |
| [A-Mem](https://proceedings.neurips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html) | NeurIPS 2025 Main | Memory organization/linking/evolution; multiple backbones and component ablations |
| [ToolRet](https://aclanthology.org/2025.findings-acl.1258/) | Findings of ACL 2025 | Tool retrieval benchmark and analysis of retrieval/downstream behavior |
| [AgentBoard](https://proceedings.neurips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Process-progress evaluation, diverse environments and human metric validation |

These are selected existence examples, not an exhaustive sample, current novelty
frontier, universal minimum or acceptance-rate estimate. Their focused contribution
does not imply low experimental workload. The contribution scale in the shared
policy is our local application of this evidence; recheck current official
requirements for an actual submission rather than treating this dated calibration
as permanent venue policy.
