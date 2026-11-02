# Research stages, shared state and delivery

This is the stage map and completion reference for the unified research controller.
In on-demand mode, use only the stages relevant to the requested scope; a suggested
next stage remains a recommendation. The full-paper default and continuous
execution rules apply only when automatic mode is explicitly activated for
this task. Automatic mode uses the same goal and evidence checks. Reading,
installing or editing these instructions does not launch research work.

Resolve a named specialist below to `../../<skill-name>/SKILL.md` relative to this
reference (`$RESEARCH_ROOT/.claude/skills/`) and read its instructions for the
current task. Select the needed
skills within a row; the list does not require calling every skill.

## Starting point, endpoint and progression

Start from the user's current objective and valid existing artifacts. Accept reusable
work, fill the gaps and continue. In automatic mode, a paper-research task without a
narrower endpoint covers all applicable stages below and delivers a complete draft
and reproduction package. An explicitly requested single revision remains a single
task. Topic selection, planning and pilot acceptance are intermediate milestones.
After selection, wait for the mandatory human checkpoint; after explicit approval,
continue the remaining authorized stages without asking at each transition.

| Stage | Existing skills to use as needed | Acceptance criteria and handoff |
|---|---|---|
| Problem discovery and topic selection | brainstorming-research-ideas, research-companion, idea-evaluator, novelty-check | Candidate comparison, central question, contribution type, selected scope and verifiable distinction; literature verification may revise candidate judgments |
| Topic approval | Main agent reports to the user | Apply the mandatory human checkpoint below; record explicit approval before dependent work |
| Literature review and evidence verification | research-lit, deep-research when a full review is requested, nature-reader, nature-ref-verifier | Traceable literature records, publication status, closest work and evidence gaps under publication-policy |
| Venue, benchmark selection and research design | select-venue, benchmark-research-skill, experiment-plan | Official requirements; reuse decision with source evidence and measurement fit; documented gap for any new benchmark; claim-linked design, suitable resources, decisive pilot and budget/stop conditions |
| Implementation and minimum pilot | experiment-bridge, run-experiment, analyze-results | Runnable implementation, measurement checks, actual raw results and grounds for continuation, follow-up or stopping |
| Main research and analysis | run-experiment, analyze-results | Authorized necessary comparisons and controls completed; failures and missing runs recorded; conclusions traceable to results |
| Argument and writing | good-story, ts-paper-plan, paper-writer, nature-figure, ts-paper-cite | Complete evidence-based draft, figures and authentic citations; argument structure rather than an experiment timeline; no unjustified iterative narrowing |
| Limitations and disclosure drafts | limitation-and-risk-writer, ai-use-drafter | Actual limitations from the author's perspective; AI-use remains an independent draft for user revision, never automatically inserted into the manuscript or submission form |
| Revision and verification | paper-polish, pre-submission-reviewer, nature-ref-verifier; paper-claim-audit when needed | Actual issues repaired; citations, claims, figures, numbers and applicable format checked; unresolved issues reported |
| Final delivery | Main agent; research-editor/qa as needed in automatic mode | Inspectable artifacts meeting the endpoint; for a full paper, a readable manuscript, applicable compiled output and reproduction materials, result sources, verification findings and remaining issues |

For topic work, use the [context policy](../../shared-references/topic-context-policy.md)
before loading historical evaluations. The selection handoff preserves the brief's
sources, fresh/continuation/reselection mode, initial candidates, later evidence
and actual input-boundary checks. A decision records its source and authority;
reuse of an artifact alone does not establish a constraint for a new topic.

Apply the [post-selection human checkpoint](../../shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
after preparing a reviewable topic proposal. Preliminary literature/novelty checks
may inform selection; the full downstream stages wait for the user's explicit
decision. Keep the approval bound to the reported topic/version and scope when
recovering a session. An absent reply cannot supply approval in automatic mode.

The table checks coverage; it does not require repeating accepted stages with unchanged
inputs. Adapt methods to the contribution type under paper-type-routing. Surveys,
theory, position and replication papers do not require inapplicable experiments or
new methods. Record why a stage does not apply. Writing may reveal an evidence gap
that returns to the relevant stage without restarting all checks. Ordinary paper tasks
end with material delivery; submission, messages and publication require applicable
explicit authorization.

Before accepting a research result for a dependent stage, apply the shared
[scientific acceptance checks](../../shared-references/research-autonomy.md#scientific-acceptance-is-separate-from-execution-completion).
Record execution completion and evidential status separately in the existing
record, with the protocol version, actual result sources and supported claim scope.
Use the [human decision points](../../shared-references/research-autonomy.md#human-participation-at-consequential-decisions)
for consequential choices; do not add approval stops at every stage transition.

## Subagents and intermediate artifacts

Research-stage decisions and team assignments share one record in the project's
existing plan or tracker. Keep the execution mode, requested endpoint, current
stage, dependencies, responsible agent, artifact path/version, acceptance result,
decisions and remaining work together. Use an existing schema when available;
for a small on-demand task, working context and the deliverable are sufficient.
Do not create separate research-control and team-control ledgers.

Carry constraint origins and decision sources through compaction and recovery.
Consult the referenced originals when a summary cannot distinguish a user
requirement from an agent suggestion or delegated choice. Resume accepted work
within its scope; do not promote a provisional choice into a lasting user preference.

The main agent records the endpoint, stage status, owners, artifact locations,
acceptance findings and next steps in the existing plan/tracker. Preserve child-project
layouts rather than adding a parallel mandatory template. Assignments specify input
versions, writable scope, output location and acceptance criteria. A subagent submits
artifacts; only verification by the main agent establishes acceptance. A scientific
negative result can be an acceptable deliverable.

For delegated work and work that will cross a context/session boundary, save the
following in the existing tracker and native artifact locations. Link existing
records rather than copying them into another mandatory document:

- **Assignment:** goal, scope, owner, dependencies, input paths and identifiable
  versions (commit, run/config ID or a snapshot/hash for mutable inputs), output
  paths, acceptance criteria, budget and stopping conditions. Record before dispatch.
- **Intermediate evidence:** code and configuration changes, raw results, logs,
  source references and reproduction commands as applicable. Save at meaningful
  milestones and before handoff or a planned interruption; do not wait until final
  delivery. Retain failed attempts and incomplete outputs with their actual status.
- **Decision record:** consequential choices, supporting evidence, alternatives
  rejected and why, assumptions and unresolved questions. Record concise reasons
  and provenance sufficient to resume the work; no internal reasoning transcript
  is required.
- **Handoff:** actual artifact paths and versions, checks performed and their
  outcomes, verification gaps, remaining work and the next dependency. Distinguish
  worker-reported completion from main-agent acceptance and scientific acceptance.

Before continuing a handed-off task, read the assignment, handoff and relevant
primary artifacts, and check that their versions agree. A summary locates evidence;
it does not replace it. Independent reviewers receive the required primary inputs
without executor-selected conclusions or inherited rankings, under the existing
reviewer-independence and topic-context policies.

The main agent releases dependent work only after the relevant acceptance checks.
When an upstream input or protocol changes, mark affected downstream artifacts as
needing revalidation and record the replacement version. Preserve prior results
and valid independent work; do not mix results from incompatible versions or rerun
unaffected tasks. Parallel writers retain disjoint ownership, and one designated
owner integrates shared artifacts.

After compaction or recovery, read recorded artifacts and unfinished stages before
resuming. Do not reselect a topic from an abbreviated summary or mark unfinished
stages complete. Changed upstream inputs require only affected downstream checks.
Reuse the existing plan/tracker and its budget. This policy creates no goal and does
not claim background continuation, cross-process recovery or scheduling that the
runtime cannot provide: in Claude Code, background commands and Monitors notify only
the live session, and a later session resumes from the recorded artifacts and tracker.
An existing tracker, `/loop` or scheduled task neither activates automatic mode nor
expands scope. Switching to authorized automatic mode reuses the artifacts and record
without restarting research or creating a competing goal.

## Ending conditions

Apply these conditions to the authorized scope. Finishing a requested plan or
single-stage revision completes that on-demand task; it does not claim completion
of a full research project. In automatic mode, assess the full agreed endpoint.

Record scientific outcomes separately from resource status using the
[pilot outcome rules](../../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot).
Execution, output-format or measurement failure blocks only the dependent branch;
the scientific criterion remains unevaluated. Diagnose and make bounded development
repairs within the plan, authorization and remaining budget. Preserve failed attempts,
freeze repaired configurations and do not tune on held-out results or retry indefinitely.
Agent-selected operating settings are not user limits. Record reasons and scope before
adjusting them, while respecting explicit budget and authority boundaries.

- **Complete:** accepted actual artifacts cover all applicable stages and meet the
  agreed endpoint; remaining issues do not prevent that endpoint.
- **Awaiting topic approval:** deliver the topic report and record `AWAITING_TOPIC_APPROVAL`.
  Wait for the user's explicit choice; do not start dependent stages or replace approval
  with a timeout, automatic-mode authority or model selection. This is not full completion.
- **Scientific stop:** valid, sufficiently informative evidence meets the predeclared
  scientific stopping rule. Stop only branches dependent on that claim. A single low
  score, non-significance or missing continuation evidence alone does not invalidate
  the direction. Preserve raw results, conditions, reusable findings, stopping grounds
  and unexecuted stages; do not label this full-workflow completion.
- **Inconclusive evidence:** keep main runs pending. Use an authorized, bounded follow-up
  that distinguishes explanations, or report the unresolved question and resumption
  conditions. Do not relabel uncertainty as negative evidence or run unlimited follow-ups.
- **Budget pause:** pause affected spending when its cap is reached. Record usage,
  limits and resumption conditions. Preserve the scientific classification; supporting
  evidence does not automatically authorize a larger budget.
- **Waiting for a real dependency:** permission, data, resources or external feedback
  remain unavailable. Finish independent work and record the recovery point and missing
  input. An unanswered ordinary clarification card alone does not establish this state.
  In post-topic autopilot, request the missing resource from the user when it arises
  and record `AWAITING_RESOURCE`; see the controller's
  [autopilot rules](../SKILL.md#post-topic-autopilot).

Before ending a full-workflow turn, identify each stopping reason's scope, blocked
stages and independent required work. Continue such work when possible. Otherwise
report actual state if only unauthorized dependencies, stopped branches or topic
approval remain. Do not expand the goal or invent progress to avoid stopping.
An existing draft does not waive this check.

The final report states what was completed, verified and remains unresolved, plus
any default decisions. A plan, readiness for another stage or an agent's completion
report does not end an authorized full workflow that can still make necessary progress.
