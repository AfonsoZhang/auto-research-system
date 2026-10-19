# Split review: materials audit + reviewer-view paper review

When a full review of a research project with a paper
is requested (pre-submission, before a revision, or "全面审查"), run two
independent reviews in parallel with separate inputs, then merge.

## A. Research-materials audit (Claude sub-agent)

- One fresh `general-purpose` sub-agent, read-only: no edits, no runs, no external
  LLM calls, no reading of secrets.
- Inputs: code, configs, raw results, experiment plan, records, build scripts,
  existing audit files, and the paper source.
- Checks: data leakage and train/test separation; ground-truth construction;
  metric and statistics implementation; cost accounting; fairness of each
  baseline's adaptation and matched settings; reproducibility (seeds, versions,
  regenerability of every table, stale results); plan vs execution and
  disclosed/undisclosed deviations; paper-to-result consistency beyond issues
  already listed in existing audits.
- Every issue needs a file locator, the affected paper claim and the smallest fix.
  New experiments only when no other fix resolves the issue, with the reason.

## B. Reviewer-view paper review (Codex)

- `mcp__codex__codex`, new thread, `config: {"model_reasoning_effort": "max"}`,
  `sandbox: read-only`, cwd = paper directory. Sending unpublished
  material to an external reviewer needs the user's authorization.
- Input: the manuscript and its figures only. Tell it not to open code, results,
  plans, audits or author notes; do not send summaries or prior verdicts.
- Role: senior reviewer at the realistic target venue, judging by contribution
  type (analysis, method, benchmark ...).
- Required in the prompt: locator per weakness; before requesting an experiment,
  name the claim that cannot be read without it and whether comparable published
  papers report it (experiment-plan "Literature sets the bar"); flag overclaiming
  and defensive/hedged wording alike; separate required from optional.
- Output: summary, strengths, CRITICAL/MAJOR/MINOR weaknesses with fixes,
  questions, score and confidence.
- Save the trace per review-tracing.md.

## Merge (main agent)

- Wait for both; never report one side's findings as the other's or predict them.
- Deduplicate by locator. Where both flag the same point, note the agreement.
  Where the paper review asks for something the materials already contain, mark
  it as a presentation fix, not a missing experiment.
- Verify each MAJOR/CRITICAL item against the files before reporting it; drop
  or downgrade unverified items and say so.
- Report in Chinese: one table (finding, source A/B/both, locator, affected
  claim, severity, smallest fix), then optional suggestions. Do not edit the
  paper until the user picks which items to fix.
