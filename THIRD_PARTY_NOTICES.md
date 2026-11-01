# Third-party notices

This distribution as a whole is released under CC BY-NC-SA 4.0 (see `LICENSE`).
Several components are adapted from the projects below. Their original
copyright notices and license texts are retained, either next to the component
or under `licenses/`, as those licenses require. Material originally under MIT,
Apache-2.0 or CC BY 4.0 remains available from its upstream under that license;
the modifications made here are distributed under CC BY-NC-SA 4.0.

| Upstream (revision) | Original license | Components here | License text |
|---|---|---|---|
| HKUSTDial/Supervisor-Skills (207bc6f), © 2026 Yuyu Luo and contributors | CC BY-NC-SA 4.0 | paper-writer, paper-polish, intro-drafter, deep-research, idea-evaluator, vibe-research-workflow, tech-paper-template, benchmark-paper-template, pre-submission-reviewer, figure-designer, drawio-reconstruction, rebuttal-guidance | `licenses/LICENSE-supervisor-skills`; drawio-reconstruction also ships its own MIT `LICENSE` (© 2026 VCG-Bench Authors) |
| wanshuiyin/Auto-claude-code-research-in-sleep (ARIS; 341f914, c4535ea), © 2026 wanshuiyin | MIT | research-review, paper-claim-audit, research-lit, novelty-check, experiment-plan, experiment-bridge, run-experiment, analyze-results, part of shared-references, `.agents/aris/tools`, `.agents/mcp-servers/codex-exec` | `licenses/LICENSE-aris`; per-skill `LICENSE` |
| Yuan1z0825/nature-skills (2375e0a) | Apache-2.0 | nature-figure, nature-reader, nature-ref-verifier, nature-response, nature-shared (including example figures under `nature-figure/assets`) | `licenses/LICENSE-nature-skills` |
| andrehuang/research-companion (733e9e8), © 2026 Andre Huang | MIT | research-companion, brainstormer, idea-critic, research-strategist agents | `licenses/LICENSE-research-companion` |
| Orchestra-Research/AI-Research-SKILLs (773a529), © 2025 Claude AI Research Skills Contributors | MIT | brainstorming-research-ideas, creative-thinking-for-research | `licenses/LICENSE-ai-research-skills` |
| Spark-To-Paper-Skills/spark-to-paper-skills (c17149d), © 2025 Albus White | MIT | ts-paper-plan, ts-paper-cite, ts-paper/templates | `licenses/LICENSE-spark-to-paper` |
| acl-org/acl-style-files (d5adc82) | no license file upstream; official ACL author style files | ts-paper/templates/acl_long, acl_short (`acl.sty`, `acl_natbib.bst`) | — |
| ShaishavMaisuria/research-paper-lifecycle-skills (f9a0ed8), © 2026 Shaishav Maisuria | Apache-2.0 | select-venue | `select-venue/LICENSE`, `select-venue/NOTICE` |
| Rimagination/good-story (978c44d), © 2026 Rimagination | MIT | good-story | `good-story/LICENSE` |
| EternalWavee/benchmark-research-skill (b620e27), © 2026 Hengtao Wu | MIT | benchmark-research-skill | `benchmark-research-skill/LICENSE` |
| UKGovernmentBEIS/inspect_evals (cef701f), © 2024 UK AI Security Institute | MIT | benchmark-research-skill/references/selection-and-validity.md | `benchmark-research-skill/LICENSE-inspect-evals` |
| aipoch/medical-research-skills (686e09d), © 2026 AIpoch | MIT | limitation-and-risk-writer | `limitation-and-risk-writer/LICENSE` |
| Airjiannan05/research-paper-workflow-skill (f47d131) | MIT | experiment-bridge/references/experiment-records.md | `experiment-bridge/references/LICENSE-rpw` |
| panbibliotekar/gaidet-declaration (9fac8c0) | MIT | ai-use-drafter terms | `ai-use-drafter/references/LICENSE-gaidet` |
| blader/humanizer (225a6f3), © 2025 Siqi Chen; AIScientists-Dev/academic-humanizer (v0.3.3), © 2026 AIScientists-Dev | MIT | prose checks in paper-polish and paper-writer | `references/LICENSE-humanizer`, `references/LICENSE-academic-humanizer` in both skills |

Ideas without copied text: `shared-references/problem-selection-strategy.md`
synthesizes methods discussed in anthropics/knowledge-work-plugins
(scientific-problem-selection, Apache-2.0) and Fischbach, Cell 2024
(doi:10.1016/j.cell.2024.03.012). `shared-references/target-exemplars.md` adapts
the idea of an exemplar knowledge base from joshzyj/open-scholar-skill; no text
from that project is included.

Not bundled: Python/Node dependencies (installed from their registries under
their own licenses, e.g. the MCP SDK), model weights, and
journal or conference templates other than those listed above. Check the license
of any image model you configure.

wanshuiyin/Anti-Autoresearch (45135aa), © 2026 Anti-Autoresearch contributors, MIT:
`paper-claim-audit/scripts/integrity/` (build_claim_ledger, check_numeric_consistency,
check_stat_consistency, check_presentation; the number extractor was modified to
match decimals without a leading zero) and the eval fixture and corruption list
under `paper-claim-audit/tests/integrity_fixtures/`. License text:
`paper-claim-audit/scripts/integrity/LICENSE-anti-autoresearch`. `precheck.py` and
the test are original. The defect families in `shared-references/integrity-patterns.md`
follow its taxonomy, in original wording. The README layout follows Anti-Autoresearch
and wanshuiyin/HERO-Anti-OverDefense (MIT).
