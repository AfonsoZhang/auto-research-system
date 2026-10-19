# D2, Graphviz, and SVG diagrams

Use for editable architecture/flow/module diagrams, bypassing the Python/R gate.
The local renderer creates SVG, physical-size PDF, PNG preview, and a render
record in a **new** directory. Keep the source; revise it after inspection.

## Relationship clarity

During the existing rendered review, compare the diagram with the source
material. Readers must be able to identify the participants, direction where
applicable, and meaning of each depicted relationship.

- Use labels, a legend or established notation where needed to distinguish
  relationships such as data flow, control/calls, feedback and association.
  Keep the meaning of any encoding consistent within the figure.
- Make line crossings distinguishable from junctions, and group membership
  clear. Placement, enclosure and arrowheads must not imply unsupported
  containment, sequence, control or causality.

Resolve ambiguity with the smallest necessary change. Labels on every edge
and any particular layout, layer order, spacing or palette are not required.
Use the existing review step without adding a separate audit or approval.

## Rendering and export

Installed tools:
- D2 v0.9.0: `$RESEARCH_ROOT/.tools/d2-v0.9.0/bin/d2` (Dagre layout).
- Graphviz: system `dot`.
- CairoSVG 2.8.2: isolated `$RESEARCH_ROOT/.venvs/nature-diagrams` environment.
- Existing PyMuPDF PDF auditors are shared with the plotting route.

Python dependency pins are in `requirements-diagrams.txt`. The isolated
environment can be repaired with `uv pip install --python
$RESEARCH_ROOT/.venvs/nature-diagrams/bin/python -r requirements-diagrams.txt`.

From the nature-figure directory:

```bash
$RESEARCH_ROOT/.venvs/nature-diagrams/bin/python scripts/render_schematic.py \
  diagram.d2 --out diagram-render-v1 --width-mm 180 --dpi 300
$RESEARCH_ROOT/.venvs/nature-diagrams/bin/python scripts/audit_schematic_text.py diagram-render-v1/figure.pdf
python3 scripts/audit_figure_collisions.py diagram-render-v1/figure.pdf \
  --json-out diagram-render-v1/collisions.json \
  --overlay-pdf diagram-render-v1/collisions.pdf
```

The same renderer accepts `.dot`, `.gv`, and authored `.svg`.
Use self-contained SVG with embedded images. Avoid external fonts/assets and
browser-only `foreignObject`; inspect font substitution in exported PDF.
The conversion uses the source aspect ratio and scales to the requested width.
Font-size audit is performed on the resulting physical size, not source pixels.
Use `audit_schematic_text.py` for these Cairo-generated PDFs: Cairo commonly
uses `1 Tf` with a scaling text matrix, so the plotting route's raw-Tf scanner
would falsely report 1 pt. The schematic auditor reads effective rendered
span sizes. Keep the existing plot auditor for the quantitative route.

The renderer moves D2 mask definitions into SVG `defs` before Cairo export;
otherwise their white rectangles can paint over the entire diagram despite
successful text extraction. Check visible pixels, not only extracted text.
Cairo's masking/font support differs from a browser: inspect connector labels,
embedded assets, and substituted fonts in every exported preview.

Minimal D2 source (scientific meaning must come from the task):

```d2
direction: right
input: Input
process: Method
output: Output
input -> process
process -> output
```

Use grouped nodes, short labels, restrained fills, and unambiguous connectors.
Do not treat D2's auto-layout as a scientific correctness check. Inspect both
the whole figure and small labels in the PNG/PDF. If text was converted to
outlines or rasterized, the text audit cannot certify it; inspect it manually.
Fix source and render into a new version directory rather than overwriting.

Official documentation: [D2](https://d2lang.com/tour/intro/),
[Graphviz outputs](https://graphviz.org/docs/outputs/),
[CairoSVG](https://cairosvg.org/documentation/).
