# Experiment records and aggregation

Use a lightweight local CSV/JSONL log unless the project already has a suitable
tracker. Define the records before expensive runs. Keep raw outputs intact and
write processed results separately.

## Plan and identity

Each executable run needs a unique run ID, condition, seed/repetition where
applicable, resolved config, exact command, expected outputs and status. Assign
distinct output paths. A physical run may inform multiple claims: represent the
claim links explicitly instead of duplicating run rows with the same ID.

Retries retain the logical run identity but receive separate attempt IDs and logs.
Changing an experimental condition creates a new condition/run, not a silent retry.
Record which attempt supplies the analysis value and why; do not keep the best
outcome selectively from repeated attempts.

For unresolved resource choices, retain the recommended condition and mark its
runs pending with the missing prerequisite. Record the user's decision and any
accepted alternative in the existing plan/tracker; access failure does not turn
the recommendation into a completed or scientifically failed experiment. Link a
substitute condition to the decision rather than overwriting the original plan.

Keep the pilot's predeclared continuation and scientific stopping criteria,
cumulative resource cap and observed outcome in the same plan/tracker. Use the
[plan's scientific outcome distinctions](../../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot)
and record resource status separately. Distinguish downstream runs skipped after
a credible scientific stop from runs pending evidence, technical repair or budget
resumption; retain the reason, supporting records and resumption condition where
applicable. None is an unexplained missing run or automatically a failed experiment.

## Per-run provenance

Record applicable fields:

- Run/attempt ID and linked claims; experiment family and method/baseline/ablation.
- Dataset/workload version, split, sampling/subset and preprocessing.
- Benchmark/source and selected task IDs or sampling rule; protocol/scorer version,
  evidence role (primary, complementary, pilot or fixture), and deviations from
  the official protocol. Link the existing selection note and publication records
  where applicable; do not duplicate them in a separate ledger.
- Code revision or snapshot, resolved configuration, model/provider version,
  prompts and evaluator version where relevant; mark unavailable versions unknown.
- Seed/repetition, hardware/environment, command and start/end times.
- Metric names, units, direction and values; raw output/prediction locations.
- Status, failure/exclusion reason, duration and measured or estimated resource use.

Keep evaluation shared across methods, match tuning budgets where necessary and
record baseline deviations. Separate exploratory tuning from final evaluation.
Synthetic test fixtures, simulated outcomes and measured benchmark results must
remain distinguishable.

## Coverage and validity

Compare observed results against the expected run list. Checking existing rows
alone cannot discover runs that never produced a log. Report expected/completed/
failed/missing/excluded counts, and assess coverage per condition and claim.
A header-only file does not establish completion of a nonempty plan.

Check duplicate IDs, missing metadata, failure reasons, metric types and non-finite
values. A field named `completed` is not proof: corroborate with process/job outcome
and expected outputs. Keep failures visible without forcing a missing metric to
look like an ordinary zero or silently discarding it.

For tabular run records, the bundled read-only helper checks planned-run coverage,
duplicate run/attempt identities, status/reason fields and explicitly named numeric
metrics. It accepts CSV, a JSON array or JSONL; use a temporary projection if the
project's existing tracker has different field names, rather than replacing it.

```bash
python3 <experiment-bridge>/scripts/check_run_records.py \
  --planned planned.csv --observed results.jsonl --metric accuracy
```

Replace `<experiment-bridge>` with this skill's actual directory. Planned rows use
`run_id`; observed rows use `run_id`, `status`, optional `attempt_id`, `reason`,
and metric columns. Statuses are `planned`, `pending`, `running`, `completed`,
`failed`, `cancelled`, `excluded` or `skipped`; the last four require a reason.
Multiple attempts need distinct attempt IDs. Failed attempts may lack metrics;
completed attempts need finite values for each requested metric. The helper emits
JSON and exits nonzero on inconsistent records. Pending/running/failed statuses
remain visible even when records are consistent: passing is not a claim of run
completion, artifact validity or scientific acceptance. The helper does not choose
attempts, aggregate results or verify source files.

## Aggregation

Group by the actual experimental condition: dataset version, split/subset, method,
baseline/ablation, relevant hyperparameters/budget, evaluator and metric/unit.
Combine across the intended replication axis only. Do not merge different splits
or count two measurements from the same replicate as independent seeds.

Configuration identifiers may include seed/attempt-specific fields: compare the
scientific condition excluding those replication fields rather than grouping by
the entire config hash and preventing aggregation. Never drop a changed setting.

Record included run IDs and exclusions for every summary. Report n alongside the
estimate and uncertainty. With one replicate, between-replicate variance is
unavailable, not measured as zero. Use `not run`, `missing` or an explicit planning
placeholder where appropriate. Every published table value must trace to raw data.

## Results-to-writing handoff

Reuse the project's analysis report or Evidence Map; no new tracker or copy of raw
data is required. For each claim/question, retain:

- The planned comparison and whether the analysis was specified before seeing
  its outcomes or introduced afterward; unknown timing stays unknown.
- What the comparison supports, contradicts, or leaves unresolved, with actual
  conditions, sample counts and uncertainty where available.
- Links to included run IDs, raw results, analysis/configuration and table or
  figure outputs; keep coverage gaps and exclusions visible in the source report.
- Which explanations are interpretations and which proposed follow-ups have not run.
- For substantive claim changes, the reference/current/proposed wording or scope,
  evidence/concern locator, justification, resolved/open concern and remaining
  scientific/practical value under [claim-preservation.md](../../shared-references/claim-preservation.md).
  Reuse this report or Evidence Map; no new required schema, ledger or directory.
  Carry already-accounted-for boundaries forward to avoid repeated narrowing.

`analyze-results` establishes these findings. `good-story` organizes their
presentation without recalculating metrics, changing included runs, or selecting
only favorable findings. A changed aggregation returns to analysis; a new
comparison returns to experiment planning within the user's task scope. Preserve
findings that already answer their questions while resolving a separate gap.

Keep timestamps, attempts and engineering changes in the records. Paper prose
follows the argument and includes temporal facts when they affect interpretation.
Reordering sections must not turn exploration into pre-specified tests or planned
experiments into completed evidence.

## Attribution and known helper gaps

Adapted from [Research Paper Workflow](https://github.com/Airjiannan05/research-paper-workflow-skill/tree/f47d13154a97d471517b44f1cdacd2d7c34327af/references)
(`experiment-implementation.md`, `result-logging.md`, `experiment-design.md`),
with local clarification of run identity, coverage and aggregation.
See [LICENSE-rpw](LICENSE-rpw).

The upstream helper scripts are not installed: reported issues
[#1](https://github.com/Airjiannan05/research-paper-workflow-skill/issues/1),
[#2](https://github.com/Airjiannan05/research-paper-workflow-skill/issues/2) and
[#3](https://github.com/Airjiannan05/research-paper-workflow-skill/issues/3)
cover duplicate run IDs, split mixing and missing planned-run coverage checks.
