---
name: ts-paper-plan
description: >
  Plan or revise a paper outline as blueprint.json using the selected venue
  template, including TS, ACL or NeurIPS templates. Use existing analyzed results
  when supplied; otherwise plan with explicit proposal-stage evidence gaps.
  Adapt the scientific structure to the contribution type. Use for a structured
  manuscript plan before drafting or a requested update to an existing outline.

---

# ts-paper-plan — proposal → blueprint.json

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

For structure or evidence requirements, use [paper-type-routing.md](../shared-references/paper-type-routing.md). Reuse the contribution type, stage and venue from existing materials; select only claim-relevant checks. This selects guidance within the current task and does not start another phase.

For substantive claim creation or revision, follow the [cross-revision claim-preservation policy](../shared-references/claim-preservation.md).

Produce the **entire blueprint in ONE reasoning pass** (the original split this into 3 calls; you
don't need to). Write it to `blueprint.json` in the working dir. For a **proposal**,
plan experiments with placeholder results only. When actual analyzed results are
supplied, use the **data_aware** branch below; never invent measurements.

When planning or revising a Limitations section, use the installed
[limitation-and-risk-writer](../limitation-and-risk-writer/SKILL.md) for author-perspective
scope and wording. Supply the actual contribution, research scope, and known constraints.
Include existing passages already covering those constraints. Apply its
[admission gate](../limitation-and-risk-writer/SKILL.md#admission-gate-all-four-conditions-required)
before creating limitations bullets. At proposal stage, keep only grounded design
consequences provisional and recheck against the written body later; do not invent
observed failures. If no candidate qualifies, omit an optional section rather than
fill it with scope recaps; follow the skill's exception for explicitly required sections.
The template and user determine whether a separate section is needed. Publication and
peer-review preferences apply to literature selection, not to choosing writing skills.

Use the writer's [length budget](../limitation-and-risk-writer/SKILL.md#length-budget-hard-acceptance-limits)
for Limitations: no minimum, at most the permitted distinct points. Set its
`target_words` and the working template's `words` to `[0, resolved_word_cap]`,
unless an explicit override requires otherwise. Template examples are not venue
word-count requirements; do not extend this cap to an entire mixed Discussion.

Apply [abstract and findings guidance](../shared-references/abstract-and-findings.md)
when assigning abstract, central-result, conclusion and limitations content.
Keep the abstract focused on the contribution; no automatic limitations slot.

When the author requests an AI-use declaration, hand off to
[ai-use-drafter](../ai-use-drafter/SKILL.md). It returns a standalone draft for the
author to edit. Keep it outside the manuscript blueprint and automatic assembly;
do not insert it into the body, acknowledgments, appendices, or LaTeX includes.

When materials or an existing draft read like a project timeline, or the author
asks to clarify the paper's main argument, use [good-story](../good-story/SKILL.md)
to map claims to evidence and propose section/figure order before finalizing the
blueprint. Preserve scientifically relevant chronology and the distinction between
pre-specified and exploratory analyses. Reuse an already agreed argument.
Use [experiment-plan](../experiment-plan/SKILL.md) for experimental design rather
than treating the paper outline as a run protocol. After experiments, reuse the
[analyze-results](../analyze-results/SKILL.md) report and `good-story` argument:
plan real condition/metric keys and trace figures/tables to existing findings.
Keep completed findings distinct from planned follow-ups; planning the paper
does not launch those follow-ups.

## Step 0 — load the template (the suite is template-agnostic)
Before planning, reuse the established venue/template or the user's `template=<name>`;
use `ts_iieta` only if no template is established. Templates
live in `../ts-paper/templates/<name>/`. Validate and copy it into the workdir:
```
python scripts/template_lint.py ../ts-paper/templates/<name>/      # must be ok:true
cp ../ts-paper/templates/<name>/*  <workdir>/                       # template.json + .sty/.cls + main.tex.tmpl + assets
```
**Set `results_mode` after copying the template.** The bundled template may reset
`<workdir>/template.json` to `"results_mode": "proposal"`. If `analyze-results` has
provided actual validated findings (or the task established equivalent analysis),
set it to `"data_aware"`; otherwise retain `"proposal"`. Do not infer completed
results from logs alone. `template.json` is the source of truth for downstream
stages; record the chosen mode in `logs/1_plan.io.md`.

Then **read `<workdir>/template.json`** and let it drive the blueprint: the **section list + ids +
titles**, the **per-section word bands** (`sections[].words`), the **contributions count**
(`contributions.count` — may be 0 = not enforced, e.g. NeurIPS), the **result-table set**
(`experiments.recipe.result_tables`), the **title/keyword limits**, and the **citation types/floor**
all come from the spec. Confirm that its scientific recipe fits the paper type.
For Limitations, apply the local length-budget exception above after loading the
spec; keep any required section while removing unsupported drafting minimums.
If it requires irrelevant method/ablation slots, adapt the optional recipe within
the requested planning scope or use an ordinary outline; do not invent contributions
to clear the linter. Preserve mandatory venue formatting. The TS values below are the *default template's* values; for another template,
use that template's sections/recipes instead. Everything downstream (`draft_lint`, `assemble`,
`citations_lint`) reads the same `template.json`.

## blueprint.json schema
```json
{
  "paper_title": "8–14 word technical title, no filler, ≤1 colon",
  "keywords": "4–6 lowercase comma-separated index terms (proper nouns/acronyms keep case)",
  "contributions": ["C1: ...", "C2: ...", "C3: ..."],
  "terminology": {"method_name":"X","component_1":"...","dataset_1":"...","baseline_1":"..."},
  "notation": {"x_s":"input skeleton sequence","T":"number of frames"},
  "experiment_design": {
    "datasets":[{"name":"","description":""}],
    "baselines":[{"name":"","description":""}],
    "metrics":[{"name":"","description":""}],
    "main_table":{"columns":["Method","..."],"rows":["Baseline A","...","<Method> (Ours)"]},
    "ablation_table":{"columns":["Variant","..."],"rows":["Full","w/o <component>"]}
  },
  "section_order": ["introduction","related_work","method","experiments","analysis","conclusion"],
  "sections": {
    "<id>": {"title":"","target_words":[min,max],"key_arguments":[".."],
             "citation_types":["CORE","CONTEXT"],
             "paragraph_outline":[{"para":1,"topic":"","key_points":[".."],"citations":"2-3","sentences":4}],
             "figures":[{"id":"system_overview","type":"architecture","caption":"","label":"fig:.."}],
             "tables":[]}
  }
}
```

## Canonical sections, default word targets (min,max), dependencies — `ts_iieta` default
(For another template, use **its** `sections`/`words` from `template.json` instead of this table.)
| id | title | target_words | depends_on |
|---|---|---|---|
| method | Methodology | (2000,3000) | — |
| related_work | Related Works (3 themes) | (800,1200) | method |
| introduction | Introduction | (800,1200) | method, related_work |
| experiments | Experimental Results | (1000,1500) | method |
| analysis | Discussion and Analysis | (900,1400) | experiments |
| conclusion | Conclusion | (200,280) | intro, method, experiments |
| abstract | (front matter, not numbered) | (150,220) | all |

(These ts_iieta bands target a substantial **~10–12 page** two-column journal article. Copy them into
`blueprint.json` `target_words` as-is unless the template differs; the band is reached by real
substance, never padding.)

(Optional `limitations` only when requested or required, with `[0, resolved_word_cap]`
from the length-budget policy above.) Other sections may shift `target_words` to
match source content, retaining `[min,max]` pairs. Zero means no drafting minimum,
not permission to omit a required section.

## Rules
- **Title**: technical, specific, 8–14 words; avoid filler ("comprehensive/framework/study/toward/universal"); key terms should overlap the method/problem terms.
- **Keywords**: 4–6, lowercase, comma-separated; specific topical terms (task, method, signal/data type, key technique); no connectors ("and/of/based").
- **Contributions**: exactly `template.contributions.count` (TS=3; `C1:/C2:/C3:`), each a concrete technical statement from the proposal's innovation claims; the last may describe the *planned* evaluation (never a result number). If the count is 0 (e.g. NeurIPS), contributions are optional/free-form.
- **Terminology glossary**: fix the exact canonical names (method, components, datasets, baselines) that EVERY section must reuse — prevents drift.
- **Tables live ONLY in experiments**, exactly the set in `template.experiments.recipe.result_tables` (TS: `main_results`, `secondary_results`, `ablation_results`; NeurIPS: `main_results`, `ablation_results`). Every other section has `"tables":[]`. **In proposal mode, keep quantitative result placeholders in tables. In data_aware mode, figures may show actual analyzed results, as described below.**
- **Figures: plan at least `template.figures.min` (TS = 5)**, distributed across **method / experiments / analysis** (the architect's rule). These are **schematic / conceptual / qualitative** diagrams that depict the *method or an idea*, each standing on its own merit (not padding): e.g. (1) the **architecture/pipeline overview** (method); (2) a **component-detail** diagram (e.g. how the trajectory descriptors are computed) (method); (3) a **concept** diagram (e.g. formation-graph construction + its Laplacian-spectrum signal) (method/analysis); (4) a **qualitative scenario** (e.g. a crossing event where appearance fails but the formation prior disambiguates — illustrative, NO numbers) (experiments/analysis); (5) a **protocol/diagnostic concept** (e.g. how the stratification by occlusion/density is defined) (experiments). Each gets `{id, type, caption, label}` with `type` in the drawable set `{architecture, pipeline, framework, concept, schematic, overview, qualitative, diagram, flow}`.
  - **Results figures depend on `template.results_mode`:** in **`proposal`** mode (no real data) **do NOT plan any results figure** — there is nothing to plot; numbers live only in the (blank `--`) tables. Do not invent a stand-in figure for the missing results. In **`data_aware`** mode (the proposal ships real, validated results) **DO plan results figures** (metric curves/bars/comparison plots) drawn from that data, in addition to the schematic ones.
- **citation_types**: only `CORE, CONTEXT, BASELINE, METRIC, DEFINITION`; don't request more CORE cites than real papers will exist. Abstract & conclusion carry no citations.
- **paragraph_outline**: 3–6 paragraphs/section (2–4 for abstract/conclusion), each specific to THIS paper, never a generic template. Limitations is exempt from these paragraph floors; prefer one compact paragraph under its length budget, or the permitted empty result.
- **Writing order** is Method-First (`method → related_work → introduction → experiments → analysis → conclusion → abstract`); `section_order` above is the *reading* order for the PDF.
- **Honesty**: proposal-mode results remain placeholders and use proposal language. In data_aware mode, report supported findings from analysis and distinguish them from unrun follow-ups.

## DATA-AWARE branch (only when `template.results_mode == "data_aware"`)
When `results_mode == "data_aware"`, use the installed **analyze-results** handoff
and its source artifacts to plan against the **real analyzed data**:
- **Plan the result tables with the REAL keys** Claude read from the data: each table's rows = the actual
  method/variant names, columns = the actual metric names (not invented placeholders). Plan the table
  *ids* (`main_results`, `secondary_results`, `ablation_results`) and honor the `tables.min` floor; the
  write stage fills the cells itself with the real numbers (no markers, no auto-filler).
- **Force `experiment_complexity="full"`** (real data warrants the full experimental treatment).
- **Enable the `analysis` section** and **plan results figures** (metric bar/curve/comparison plots) drawn
  from the data, in addition to the schematic figures — these are rendered later via matplotlib
  the installed [nature-figure](../nature-figure/SKILL.md) workflow or existing project plotting code.
- Everything else (title, keywords, contributions, notation, terminology, per-section outlines) is
  planned exactly as in proposal mode. `blueprint_lint` accepts the exact-key data-aware table plan and
  only enforces `tables.min` (it does not force the proposal table count).

## Validate (enforced) + log
Run `python scripts/blueprint_lint.py <workdir> --fix`, then re-run without `--fix` until `ok=true`. It is now **template-driven** (reads `template.json` from the workdir): `citation_types` must be a subset of the template's `citations.types` (remaps aliases — `DATASET→METRIC`, `METHOD→CORE`, …), all of the template's sections present (self-heal with the template's titles/word-targets), every `target_words` a 2-tuple, the template's result-table count in experiments (mode-dependent: in **proposal** mode the experiments section plans either **0 or exactly** `template.experiments.recipe.result_tables` result tables — 0 is allowed because a proposal has no measured results to tabulate; in **data_aware** mode it must plan at least `tables.min` filled tables), title within the template's `title` limits, contributions == the template's `contributions.count` (skipped when 0). Do not proceed on a failing blueprint.

Then write **`logs/1_plan.io.md`** — three blocks: INPUT (the proposal text/path), DECISIONS (why this title / these word targets / these keywords), OUTPUT (blueprint.json one-line summary). The optional next requested stage is **ts-paper-cite**; a standalone plan stops here.
