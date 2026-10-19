---
name: benchmark-research-skill
description: >-
  Survey and select existing benchmarks for a research question, or extract a
  paper's datasets, metrics, protocols and baselines with source evidence. Use
  for benchmark selection, evaluation reuse, benchmark surveys or checking
  measurement fit before experiment design. A survey does not launch experiments.
license: MIT
metadata:
  upstream-repo: EternalWavee/benchmark-research-skill
  upstream-commit: b620e27108a43f33c0a0554a55b9381a58344720
  local-adaptation: published-literature-benchmark-reuse
---

# Find and reuse benchmarks that answer the research question

Use [selection and validity](references/selection-and-validity.md) for decisions.
Use the existing [publication policy](../shared-references/publication-policy.md)
and literature records for paper identity, publication status and version choice.
Reuse current research questions, approved benchmark choices and existing notes.
A request to modify one protocol or analyze one paper stays within that scope.

## Direction survey

1. Identify the claim, capability, task setting and intended comparison. For Agent
   research, distinguish model answers from behavior involving tools, memory,
   context, scheduling or environment state when that distinction affects the claim.
2. Reuse the closest relevant papers and `literature/publication_records.json`.
   Use [research-lit](../research-lit/SKILL.md) for missing discovery or verification
   through the existing Semantic Scholar, Exa, OpenAlex and web sources. Read the
   selected published/accepted version when available; preserve labeled supplements
   and unresolved statuses. Respect explicit local-only or source restrictions.
3. Read experiment sections, result tables, appendices and official evaluation
   implementations. Follow the benchmarks and baselines those papers actually use.
   Search method/system papers as well as papers titled benchmark or dataset.
   Expand through shared tasks and comparisons only as far as needed to resolve
   credible alternatives; avoid an unbounded citation crawl.
4. Compare reusable candidates using the linked selection reference. Explain the
   recommended primary evaluation, any complementary diagnosis and remaining gaps.
   A known benchmark is useful only if its tasks and measurement fit the claim.
5. Save the compact comparison in the project's existing research notes or
   experiment plan. When a standalone survey is requested and no destination
   exists, use `literature/benchmark-survey.md` in the current research topic.
   Link supporting extraction and the shared publication records; avoid a second
   bibliography or tracker. Pass the choice to experiment planning when in scope.

## Single-paper analysis

Resolve the requested version and read its evaluation evidence. Extract the exact
dataset/task names, split and protocol, metrics, compared methods, evaluator/code
links and source locators. Distinguish training data from evaluation data and
ablations from competitive baselines. Conflicting table, prose or code details
remain explicit discrepancies until resolved; do not silently favor one source.
Do not infer benchmark facts from the title, an abstract or remembered results.

Report only what was verified. An inaccessible paper or failed API leaves a
coverage gap; it does not establish that no reusable benchmark exists. Preserve
the source/version and intermediate evidence needed to check the extraction.

## Optional helpers

The five Python files in `scripts/` are retrieval/report helpers, not semantic
extractors or validity certifiers. Read [helper usage](references/helpers.md)
before using them. Use absolute paths resolved from this skill directory and
explicit output paths in the current research project. Keep generated artifacts
out of the skill installation and unrelated projects. Obsidian is optional.

Default to English for working notes, extraction and saved reports; give the user
the final conversational report in Chinese. Preserve exact source titles and
technical identifiers. Use existing source-reading tools for official HTML/PDFs;
the optional arXiv fetcher does not determine publication status or selected version.

## Handoff and boundaries

[experiment-plan](../experiment-plan/SKILL.md) owns the final scientific design,
resource recommendation and decisive pilot. Hand off benchmark choice, protocol,
source evidence, known measurement limits and resource tradeoffs. Planning and
surveying do not start experiments, subagent teams or another research phase.
Within an explicitly authorized full workflow, continue its requested stages.

Adapted from [benchmark-research-skill](https://github.com/EternalWavee/benchmark-research-skill/tree/b620e27108a43f33c0a0554a55b9381a58344720)
under [MIT](LICENSE). The validity reference separately attributes Inspect Evals.
