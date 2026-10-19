# Ideation evidence

Empirical findings on LLM-assisted ideation and the rules this skill derives from
them. They refine, not replace, the shared topic-selection policy.

| Finding | Source | Rule |
|---|---|---|
| In blind review, LLM ideas were rated more novel than expert ideas, slightly less feasible; at scale LLM ideas duplicate heavily and LLMs rank their own ideas unreliably | Si, Yang, Hashimoto, ICLR 2025 (arXiv 2409.04109) | Deduplicate generated candidates by core mechanism; the generating model does not rank its own ideas |
| After 100+ hours of execution per idea, LLM ideas lost much more score than human ideas and the ranking flipped; most of the drop came from weaknesses reviewers only saw after execution | Si, Hashimoto, Yang, ICLR 2026 (arXiv 2506.20803) | Paper-stage novelty is not a result; probe weaknesses that only execution exposes and run the smallest execution before scaling |
| LLM novelty judges cluster on middle scores and diverge from expert gold labels; they rate model-generated research questions as highly novel ("novelty mirage") | RINoBench, Schopf & Färber, LREC 2026 (2026.lrec-1.370); On the Limits of LLM-as-Judge for Scientific Novelty Assessment (arXiv 2606.12071) | An LLM saying an idea is novel is not evidence; novelty rests on retrieved, read papers |
| AI Scientist's novelty check used Semantic Scholar keyword matching and marked established techniques and plain domain transfer as novel | Beel, Kan, Baumgart, arXiv 2502.14297 | Keyword search is insufficient; "nobody applied A in B" alone does not establish a contribution (see novelty-check Phase A) |
| Decomposing papers into purpose / mechanism / evaluation facets and recombining them supported exploration better than plain prompting; facet-based retrieval surfaced more relevant prior work | Scideator, Radensky et al., CAIS 2026 (arXiv 2409.14634) | Diverge by facet recombination; search prior work per facet |
| Organizing literature as a progression chain produced better-developed ideas than an unordered pile | Chain of Ideas Agent (DAMO-NLP-SG) | Give the brainstormer a chronologically ordered chain of core papers |
| Hypotheses are validated by a sequence of falsification experiments with Type-I error control | POPPER, Huang et al., ICML 2025 (arXiv 2502.09858) | The first step tries to refute the idea, not to collect support |

## Pre-registration before the first step

Before spending compute on a CONTINUE / VALIDATE_FIRST first step, write in the
topic's plan artifact:

- The expected result as a number against a named baseline ("top 10% versus a
  random-timing baseline", "≥3 points over baseline X"), not "should improve".
- A meaningful null: for timing or selection effects, compare against randomized
  controls under the same conditions, not against zero.
- The result that refutes the idea and what happens then. Do not switch metrics or
  baselines afterward to rescue it.
- Test data and labels come from a source independent of the system under test.

## Open-source systems (borrow parts, not pipelines)

- SakanaAI/AI-Scientist, AI-Scientist-v2: end-to-end pipeline; its novelty step is the keyword matching criticized above
- JinheonBaek/ResearchAgent: literature-grounded idea generation with iterative reviewing agents
- DAMO-NLP-SG/CoI-Agent: progression-chain literature organization
- Agent Laboratory: execution side, from a given idea to experiments and report
- jerry609/AI4S: paper list for AI-for-science ideation and evaluation
