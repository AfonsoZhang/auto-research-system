# Vibe Figure: design, render and verify

Apply the shared [research autonomy and validation policy](../../shared-references/research-autonomy.md).
AI may design and produce final figures using suitable tools. Judge the actual
artifact and its evidence; human redrawing is not a default acceptance condition.

## 1. Establish the figure's purpose

Read the relevant claim, analyzed data and intended placement. Determine what the
reader should learn and whether the artifact is a data plot, schematic or mixed
figure. Distinguish measured data from illustrative examples. Consult
`figure-designer` for design alternatives where needed.

## 2. Select the design and tool

Choose a design within the requested scope and existing preferences. Present
options when the choice changes the scientific message, requires new data or has
a material cost. Routine layout decisions do not each need user approval.

Use `nature-figure` for the actual production and its backend, layout and export
checks. Reuse its plotting or diagram pipeline rather than imposing a separate
manual-only workflow. Use the verified venue requirements for final dimensions
and typography.

## 3. Render from traceable inputs

Data charts use identified analyzed results and reproducible plotting code.
Keep source data, aggregation and uncertainty consistent with the experiment
report. An image generator or illustrative sketch does not supply experimental
measurements. Preserve native editable sources where the requested artifact
requires them.

## 4. Verify and deliver

Check data-to-plot values, axes, units, uncertainty, labels and caption claims.
Visually inspect the rendered figure and run the applicable `nature-figure`
audits. A successful render does not establish that the figure represents the
scientific result correctly.

Fix layout problems within the task. A discrepancy in analysis returns to the
relevant analysis work within authorization; it is not repaired by changing the
figure's numbers. Deliver the requested exports and their editable or reproducible
sources, with unresolved issues stated plainly. The user retains decisions over
material scientific messages and final publication commitments.
