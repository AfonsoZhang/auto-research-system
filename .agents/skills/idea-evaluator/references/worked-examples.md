# Selection calibration examples

Use the [shared topic-selection policy](../../shared-references/topic-selection-policy.md)
for the governing rules and verified publication links. Historical reviewer scores
and retrospective best-paper heuristics are not acceptance thresholds.

## Published examples of contribution scope

- LLMCompiler (ICML 2024) targets function-call planning and parallel execution,
  with latency/cost/accuracy comparisons. A concrete scheduling mechanism can be
  the paper's focus; this does not make any parallelization patch publishable.
- Agent Workflow Memory (ICML 2025) and A-Mem (NeurIPS 2025 Main) both concern
  external memory, with different workflow and memory-organization contributions.
  Their broad overlap is compatible with distinct research contributions.
- ToolRet (Findings of ACL 2025) systematically evaluates tool retrieval;
  AgentBoard (NeurIPS 2024 Datasets and Benchmarks) studies process-level agent
  evaluation. Evaluation work is not required to introduce a new agent method.

These selected accepted examples establish possibilities, not acceptance rates,
minimum experimental counts or the current novelty of a new proposed idea.

## Hypothetical decision cases (not empirical publication claims)

| Case | Appropriate reasoning and decision |
|---|---|
| A crowded memory area, but a verified meaningful delta and appropriate next step | CONTINUE; document the nearest work and remaining evidence needs |
| Combining two known techniques with an unresolved interaction benefit | VALIDATE_FIRST; isolate the interaction against constituent methods and a simple control |
| An unread preprint appears to contain the same mechanism | VALIDATE_FIRST for that comparison; verify its contents/status and priority implications before judging remaining value |
| Reliable experiments contradict a claimed accuracy benefit but establish a useful cost/reliability tradeoff | Withdraw the accuracy claim; assess the distinct finding and any authorized scope revision rather than automatically stopping |
| A single noisy pilot loses to baseline | Check validity/uncertainty and use a bounded decisive check; no automatic rejection or unbounded scaling |
| An essential resource is unavailable but obtainable with approval | Present the preferred resource and cost choice; PARK dependent work if blocked, without declaring the idea scientifically invalid |
| Verified prior work establishes the same claims and no worthwhile delta remains in scope | STOP_CURRENT_VERSION with exact work/claim locators and what was considered |

A clear pitch alone does not establish novelty. A high optional score cannot
override contrary evidence. A low score or lack of disruptive potential cannot
override a substantive, properly scoped contribution.
