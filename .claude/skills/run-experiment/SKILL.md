---
name: run-experiment
description: >-
  Execute an authorized research pilot or experiment batch on the specified local
  or existing remote environment, recording commands, failures and outputs.
  Use for running experiments, pilots, experiment batches or collecting results from approved runs.
license: MIT
metadata:
  upstream-repo: wanshuiyin/Auto-claude-code-research-in-sleep
  upstream-commit: c4535ea8ae1e013399a2525dc7d285859f672b62
  local-adaptation: author-led-experiment-workflow
---

# Execute and track research runs

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

Read the plan, run list, project environment instructions and existing status.
Resolve the command, working directory, data, environment, compute/API budget,
concurrency and expected outputs. Use the specified environment when it supports
the selected design: CPU, local GPU, existing remote host or an already authorized
service. Do not assume every experiment is GPU training. If the environment or
access cannot support the design, apply the
[resource-selection rule](../experiment-plan/SKILL.md#select-the-best-suited-design-before-checking-availability):
recommend what is needed and ask the user before substituting a smaller model,
convenient dataset, proxy evaluator or reduced scope. Reuse approved fallback
choices; independent preparation can continue while dependent runs remain pending.

## Execution boundaries

Run only the requested pilot or batch. Reuse prior authorization and continue
within its limits. If a missing budget, destination or dataset makes the requested
run materially ambiguous, resolve that detail before launching dependent work.

Do not infer permission to rent cloud resources, modify account settings, push git
commits, send notifications, destroy instances or invoke external reviewer models.
For a specified cloud or queue service, use its existing project workflow within
the authorized scope; this skill does not install or provision a scheduler.

## Preflight and launch

- Check that code, configs and required data exist and that the environment can
  execute the planned operation. Use the smallest meaningful smoke check before
  an expensive new batch. Apply [experiment records](../experiment-bridge/references/experiment-records.md).
- For benchmark runs, confirm actual task IDs/subset, split, scorer, tools and
  budgets match the selected protocol. Record deviations and keep pilot subsets
  and modified conditions distinct under [benchmark reuse](../benchmark-research-skill/references/selection-and-validity.md).
- Respect allocated resources. Low GPU memory usage alone does not establish that
  a shared GPU is yours to use. Match concurrency to the actual allocation.
- For remote work, sync the required source AND configs/dependency specifications
  into the intended location. Avoid blanket git add/commit/push or overwriting
  unrelated remote files. Record which source revision/configuration ran.
- Capture stdout/stderr and the program's actual exit status. When using a shell
  pipeline with `tee`, preserve the experiment's failure status using `pipefail`
  or an equivalent subprocess wrapper; `tee` success is not experiment success.
- For long jobs, use the available background-process mechanism and record its
  process/session/job ID. Do not block communication while a batch runs.

### Local memory guard

On a local machine, the experiment shares memory with the agent session, MCP
servers and other processes. A job that exhausts memory can be OOM-killed (exit
137), and a machine- or VM-wide OOM can take the agent session down with it.

- **Know available memory first.** Before planning workers or caps, check total
  and available RAM and swap (`free -h`; inside a VM or container, the VM or
  cgroup limit, not the host's) and what other processes already use. Record the
  figures; every later limit is derived from them.
- **Estimate before launch.** Run the smoke check under `/usr/bin/time -v` and
  read "Maximum resident set size"; scale by data size and worker count, and
  compare the estimate with the available memory recorded above.
- **Cap every heavy local job and detach it from the session.** On Linux with a
  systemd user session, launch it as a transient user unit, so it dies alone on
  overflow and keeps running if the agent session ends (survival after logout
  needs `loginctl enable-linger`):
  `systemd-run --user --unit=<project>-<step> -p MemoryMax=<cap> -p MemorySwapMax=<swap-cap> --collect <cmd>`
  Set the cap below available memory, leaving headroom for the agent session and other processes. Status:
  `systemctl --user status <unit>`; logs: `journalctl --user -u <unit>`; stop by
  unit name. Use `--scope` only for short foreground checks. Without systemd,
  use `prlimit --as=<bytes>` or `ulimit -v` with the platform's background
  mechanism, and record which limit applied.
- **Make jobs durable (state outside the process, idempotent tasks, bounded retries).**
  - Required: write each item's result to its own file (or append one JSONL
    line) as soon as it finishes; write to a temp name and rename, so a kill
    never leaves a half-written result. On restart, skip items whose result
    exists. Log failed items with the error. Judge progress by counting result
    files.
  - Optional ledger, only for large batches with many failures: item key →
    failed/attempts/error, so known failures are not rerun blindly and retries
    stay bounded.
  - Item keys are deterministic (arm, dataset, query ID, seed). Cache paid LLM/API
    responses by key so a rerun after a crash does not bill twice.
  - Per-item timeout and a bounded retry with backoff for transient errors (API
    429/5xx, network); a deterministic error fails the item once and is recorded,
    not retried forever.
  - Concurrency cap per resource (API calls, CPU workers) set in config, not
    derived from core count.
  - On SIGTERM/SIGINT flush finished results before exiting.
  - Liveness is progress, not a live PID: check that the result-file count
    grows; a running job with a flat count is stalled.
  - Cache expensive encodings to disk keyed by model and input hash.
- **Bound worker memory.** Fix the worker count from the measured per-worker peak,
  not the core count; recycle workers (`maxtasksperchild` / `max_tasks_per_child`)
  when per-task memory accumulates; stream or batch instead of holding all outputs
  in RAM.
- **Exit 137 or "Killed".** Confirm OOM with `journalctl --user -n 50` or
  `dmesg | grep -i oom` (if permitted); record it as an implementation failure,
  not a result. Apply the fixes above, then rerun only the missing items.
- **When it still does not fit** (training, large-model eval): stop and propose a
  remote GPU with a cost estimate; renting needs the user's approval. Changing
  host or VM memory settings also needs the user.

## Monitor, retry and collect

Record status as planned/running/completed/failed/cancelled as appropriate.
Completion requires the actual process/job outcome plus readable outputs for this
run, with matching IDs, configuration and expected metrics. An old result file or
an empty output is not sufficient. Unobservable completion remains unverified.

Keep per-attempt logs. Diagnose failures before retrying; respect the authorized
retry/time/spend budget. Do not repeatedly consume resources on an unchanged
deterministic failure. A scientific result below expectations is not a job failure.
Distinguish rerunning an identical attempt from changing the experimental condition.

Classify a nonpassing result before deciding what it blocks: technical readiness,
valid scientific evidence, inconclusive scientific evidence, or a resource/access
limit. Missing labels, invalid output schemas and broken measurement do not evaluate
the scientific claim. Diagnose and make bounded development repairs under the
[plan's repair allowance](../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot),
preserving failed attempts. Freeze repaired prompts/adapters before held-out use;
require a new readiness check when the relevant configuration changes. Never fill
missing predictions from reference labels or relabel an old failed run as passed.

Evaluate the planned [pilot gate](../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot)
before launching main runs. Process success and readable outputs alone do not meet
the scientific continuation criterion. Use the plan's distinct scientific outcomes:
credible negative evidence stops the dependent campaign; inconclusive evidence
keeps main runs pending and permits only authorized, bounded discriminating
follow-ups; technical failure leaves the claim unevaluated and calls for bounded
repair. Merely not meeting the continuation criterion is not scientific refutation.
Reaching the cumulative resource cap pauses affected spending regardless of the
scientific outcome; record the resumption condition without relabeling the finding.
Hold or cancel queued dependent runs as appropriate to that reason and name the
affected jobs. Do not automatically extend the budget or repeat until positive.
Technical readiness alone neither passes nor refutes the scientific gate.
Independent authorized work can continue.

For an active full-workflow task, before ending the turn reconcile this branch stop
with unfinished work: continue useful work that does not depend on the stopped or
paused branch, and record any remaining dependency, resource pause or scoped
scientific stopping reason. A standalone run request still ends at its requested
reporting boundary.

Start dependent jobs only when their required upstream artifacts were successfully
produced and checked. A failed parent becoming terminal does not satisfy a data or
checkpoint dependency. Preserve failed jobs in the final coverage report.

After collection, reconcile planned and observed runs. Report completed, failed,
missing and excluded counts, actual artifact locations, and recorded time/cost
(label estimates as estimates), including runs intentionally not launched after
an early stop. Analyze valid results with
[analyze-results](../analyze-results/SKILL.md) when analysis is in scope.

Adapted from ARIS `skills/run-experiment/SKILL.md` at the revision above;
see [LICENSE](LICENSE). This local variant has no mandatory cloud, queue or MCP dependency.
