# Unified figure workflow

## Choose a route

Start with the scientific message, figure type, output size, and supplied data.
Use the lightest route that expresses the requested content accurately.

| Content | Tool | Source to preserve |
|---|---|---|
| Observations, uncertainty, curves, statistics | Existing Python/R plotting route | Plotting source and data |
| Architecture, workflow, labelled dependencies | D2 by default; Graphviz for graph layouts; authored SVG for precise geometry | `.d2`, `.dot`, or `.svg` |
| Concept artwork, scenes, generated visual assets | Configured image provider with budget preflight ([image-generation.md](image-generation.md)) | Prompt, references, job/response/usage receipt, original image |
| Mixed panels | Combine the above, then assemble in selected Python/R or SVG layout | Component sources and assembly source |

An editable diagram with boxes and arrows normally uses the diagram route even
if called a mechanism schematic or graphical abstract. Use image generation when generated
visual assets are actually needed or requested. Retain existing task tool
choices unless the figure's requirements change.

Python/R exclusivity applies to quantitative panels. In SVG assembly, place
finished quantitative panels without changing their values, axes, uncertainty,
or aspect ratio; preserve their original exports. An SVG-only schematic does
not require choosing Python/R. Use the diagram environment only to convert
authored SVG and inspect final PDF, not to redraw an R data plot in Python.

## Shared render → inspect → revise loop

1. Establish one layout contract: physical dimensions, font sizes (5 pt minimum
   unless a stricter target applies), palette, panel labels, and output formats.
2. Render each selected route. Inspect actual output, not just source code or
   the model's response. For Poe, inspect pixel dimensions and small text;
   a requested resolution is not proof of the returned resolution.
3. Run applicable local checks on the final composition. Python/R uses its
   existing source, panel-alignment, PDF text, and collision gates. Diagrams use
   PDF text/collision audits plus main-agent visual review. For mixed comparable
   panels, record final panel rectangles for the alignment auditor.
4. The main agent checks scientific meaning, arrow direction, label spelling,
   clipping, line crossings, scale consistency, and legibility at intended size.
   Raster content and outlined text cannot pass a text-geometry check merely
   because the PDF auditor finds no glyphs. Record those checks as visual-only.
5. Modify the responsible source and render again. Use Poe only for necessary
   image edits, with a fresh point preflight. Do not regenerate an entire
   composite for a local label/layout fix that can be made in the assembly.
6. Deliver source, final export, preview, and relevant audit outputs. Record
   unresolved limitations honestly; do not call an unchecked result passed.

No default subagent: the main agent owns planning and final acceptance. The image
provider is only for generating/editing images, never for reviewing or reasoning
about the figure. Balance/pricing/usage queries support its generation budget check.
Use the existing journal-specific rules when a submission target is given.

Installation does not authorize an arbitrary paid demonstration. Validate
transport and budget gates with mocked responses; use live read-only balance
and catalog checks. For an actual requested figure, proceed after the required
estimate passes without asking for another routine confirmation.
