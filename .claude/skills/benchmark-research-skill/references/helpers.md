# Optional retrieval and report helpers

Resolve `BENCHMARK_SKILL_DIR` to this skill's real directory in the current
Claude/Codex installation. Use `python3`; dependencies are in
`$BENCHMARK_SKILL_DIR/requirements.txt`. Check the environment before installing
anything. The scripts do not call an external inference model.

## Outputs and configuration

Prefer explicit `--output`/`--output-dir` arguments under the current research
topic. Config is optional for those paths. When needed, copy `config.example.yaml`
to the research topic's existing configuration area, set `vault_path` to that
topic's absolute directory and pass `--config` explicitly. The field is named
`vault_path` upstream, but no Obsidian application is required.

Never put a live config, paper cache or generated report inside the installed
skill. Do not overwrite author notes with the report renderer: write a fresh
intermediate file, inspect it and incorporate the relevant content into the
existing note. Preserve source titles; working extraction and prose use English.

## Fetch the chosen paper

For a previously downloaded selected version:

```bash
python3 "$BENCHMARK_SKILL_DIR/scripts/fetch_context.py" \
  --pdf "$SELECTED_PDF" --output-dir "$BENCHMARK_EVIDENCE_DIR"
```

Read `context.json`, the identified sections and the source itself as necessary.
`status.usable_text` checks text availability, not extraction correctness. The
section detector may miss appendices or task details; verify the original source.
For a chosen arXiv version, `--paper-id` can fetch source/PDF context. Do not pass
`--paper-id` together with a selected official PDF to mean "prefer the PDF": the
upstream helper gives arXiv source text priority. Use only `--pdf` for that PDF.
Use existing source-reading tools for official HTML or other source types.

`--with-assets` optionally recovers figures/renders pages. Inspect source images
or pages only when required to resolve experiment/table details. Missing usable
text/assets leaves extraction pending; do not reconstruct facts from memory.

## Extract and optionally render

The agent writes evidence-backed extraction; scripts do not extract semantics.
Use the upstream structure only when a helper needs it:

```json
{
  "paper": {"id": "stable-paper-id", "title": "Exact source title", "links": {}},
  "benchmarks": [{
    "dataset": "Exact task or dataset name",
    "dataset_link": null,
    "task": "Capability actually evaluated",
    "metrics": [{"name": "Exact metric", "direction": "unknown", "meaning": "Definition"}],
    "protocol": "Version, split, tools, limits and evaluator",
    "compared_methods": [],
    "evidence": "Source URL/version and table, page or code locator",
    "assets": [],
    "notes": "Source-backed caveats or explicit unknowns"
  }],
  "eval_scripts": [],
  "related_work_edges": []
}
```

Keep the stable publication-record ID and selected-version provenance with this
extraction; the renderer's basic schema does not enforce them.

```bash
python3 "$BENCHMARK_SKILL_DIR/scripts/generate_report.py" \
  --mode single-paper --input "$BENCHMARK_EXTRACTION_JSON" \
  --output "$NEW_INTERMEDIATE_REPORT"
```

For multiple extraction files, supply a comma-separated `--input` list and
`--mode survey --topic "$BENCHMARK_TOPIC"`. Check inputs before running: the
upstream renderer can skip missing/malformed files and still exit successfully.
It does not render all protocol/publication/selection fields. Use its result only
as a basic extraction note, then include the protocol, source status, validity
findings and recommendation required by the selection reference in the final note.

## Discovery limitations

Use `research-lit`'s sources for the main search. `search_papers.py` is an optional
arXiv-only supplement with simple lexical ranking. It can return an empty paper
list after a network error; retain stderr and do not interpret this as no matches.
Its `published` field is an arXiv date, not a formal-publication decision. Run it
only with explicit topic/source intent and an output path or a project config.

`collect_links.py` only proposes candidate links and contains audio-specific query
heuristics. It is disabled in the example config; for Agent research prefer links
from source papers, official repos and the existing Exa/web workflow. If explicitly
used, verify every selected link and preserve search failures. Candidate URLs and
successful reports are not proof of ownership, validity or community adoption.
