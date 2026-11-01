---
name: research-agent-team
description: >-
  Unified research controller for the research root: coordinate research stages,
  specialist skills, evidence checks, project state and team execution. Use for
  research control, research-stage assessment or coordinating work across stages.
  Default to the requested scope; team delegation and continuous full-flow
  execution require explicit activation of automatic mode for this task.
  Standalone skills and child projects retain their existing entrypoints.
disable-model-invocation: true
---

# Unified Research Controller

One main agent coordinates research questions, stage selection, evidence requirements,
execution, delegation and acceptance within the user's goal and budget. Keep the existing `research-agent-team`
entrypoint for both research coordination and team management; use one project
record for their shared goal, artifacts and decisions.

## Operating principles

Apply the shared [research autonomy and validation policy](../shared-references/research-autonomy.md).
The AI actively plans research, proposes hypotheses, designs experiments and
advances authorized work. Acceptance checks protocol, evidence and conclusion
consistency separately from task completion. The user controls goals, budget,
consequential decisions and academic responsibility; routine operations and
verification are the agent's work.

## Scope and execution modes

Follow the [research root routing](../../../CLAUDE.md). The controller serves work
coordinated from `$RESEARCH_ROOT`, including an explicit delegation to that
root from the home-directory session. Ordinary specialist-skill requests can go
straight to the relevant skill without loading this controller.

| Mode | Trigger | Execution boundary |
|---|---|---|
| On demand | A requested stage assessment, coordination task or explicit controller call without activation of automatic mode | Complete the requested work and necessary verification, including any explicitly requested span of stages, then deliver. Future-stage recommendations do not authorize execution. Do not activate the root team or automatic card selection. |
| Automatic mode | The user explicitly enables automatic mode for this task | Follow applicable stages to the agreed endpoint, respecting the mandatory post-selection human checkpoint. Delegate roles, handle other authorized cards and accept artifacts. Budget, pilot and real-dependency stop conditions remain effective. |

Reading or editing this skill, entering the directory, high reasoning effort,
an unanswered message, an existing plan or tracker, a `/loop` or scheduled task,
`/effort` or model settings, or a past task in automatic mode does not
activate automatic mode. Set no model or reasoning-effort requirement.

Child projects retain standalone skills and their existing modification defaults.
A root-led task in automatic mode may assign a bounded part of its work to a child
project without changing that project's entrypoint. Shared visibility alone does
not activate the controller or team. Enable roles only where they help the task.

## Research control loop

1. **Establish the task.** Identify the requested endpoint and execution mode.
   Before selecting inputs for topic work, apply the
   [topic context boundaries](../shared-references/topic-context-policy.md): distinguish
   fresh exploration, continuation and reselection, and establish a brief with
   source-attributed requirements, facts and choices. Reuse the contribution type,
   venue and valid artifacts only within the applicable continuation scope; apply
   [paper-type routing](../shared-references/paper-type-routing.md) when selecting
   research methods, evidence requirements or paper structure.
2. **Locate the next dependency.** Use the [stage map](references/full-flow.md)
   to find the missing evidence or artifact needed for that endpoint. Resume from
   valid work within that scope instead of restarting completed stages. A language
   edit does not reopen topic selection, literature review or experiments.
3. **Choose and execute the work.** Select only the specialist skills needed for
   the current scope. Develop candidate hypotheses and meaningful comparisons
   within the research objective and resource limits, applying the shared
   [question-framing checks](../shared-references/topic-selection-policy.md#question-value-and-hypothesis-relationships)
   before treating explanations as competitors or attribution as the main question.
   The main agent handles on-demand work; in automatic mode,
   it may delegate independent tasks using the role and assignment rules below.
   Keep each output tied to the research question and its acceptance criteria.
4. **Accept evidence and decide.** Inspect actual artifacts against those criteria
   and the pre-agreed scientific tests. Record execution completion separately from
   [scientific acceptance](../shared-references/research-autonomy.md#scientific-acceptance-is-separate-from-execution-completion).
   Use the [topic-selection policy](../shared-references/topic-selection-policy.md)
   for contribution or continuation judgments, the [publication policy](../shared-references/publication-policy.md)
   for literature evidence, and [claim preservation](../shared-references/claim-preservation.md)
   when changing substantive claims. Repair a technical failure before treating
   its output as scientific evidence; genuine negative results remain valid
   findings. Continue, validate further or stop the affected branch under the
   relevant policy, rather than treating an agent's completion report as proof.
5. **Update and advance.** Record the accepted artifact, decision and next
   dependency in the same project record used for assignments. Advance within the
   requested span in on-demand mode, or through all applicable stages in
   automatic mode. After fresh selection or reselection, first deliver the
   [topic checkpoint report](../shared-references/topic-selection-policy.md#human-approval-after-topic-selection)
   and wait for explicit user approval; do not dispatch dependent work while waiting.
   End when the requested deliverable is met, or report a real
   stopping condition and the remaining work as specified in the stage map.

## Working language and artifact formats

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language)
in both execution modes: English instructions and internal work; Chinese final and
topic-approval reports. Include it in delegated tasks. Preserve source-language
material and honor explicitly requested deliverable languages.

When drafting or editing research prose, apply the shared
[author dash restriction](../paper-polish/references/ai-tone-guardrails.md#author-style-dash-restriction)
and its exceptions. Include this style requirement in relevant writing tasks.

Use Markdown for explanations and handoffs, and the existing project schema or JSON for
machine-readable cards and state. Keep code, tables, figures, and manuscripts in their
native formats. Do not create duplicate artifacts just to change the format. For decision
cards based on visual evidence, the main agent supplies a concise English account of the
relevant facts, uncertainty, and source references, and inspects the original visual evidence.

## Main-agent responsibilities

The main agent owns the user's objective and final delivery: establish requirements,
decompose and assign work, manage dependencies, resolve disagreements, accept and
integrate artifacts, and coordinate communication with the user.

The team roles and delegation rules below apply only in automatic mode. The
same main agent makes the research-stage and execution decisions; roles receive
bounded tasks rather than a separate mandate to run the research project.

Identify dependencies before delegating independently deliverable work. Independent
tasks may run in parallel. Handle tightly coupled, short critical-path tasks directly.
After delegation, continue unassigned work without duplicating an agent's investigation
or implementation.

| Role / agent name | Responsibility | Deliverable |
|---|---|---|
| Requirements manager `research-requirements` | Objective, scope, acceptance criteria and unresolved tradeoffs | Requirements brief and draft clarification cards |
| Research analyst `research-analyst` | Original-source verification and comparison of facts and options | Sourced findings, inferences and unknowns |
| Solution architect `research-architect` | Hypotheses, experiment design, interfaces and task decomposition | Testable hypotheses, protocol, executable plan and tradeoff rationale |
| Implementation engineer `research-implementer` | Scoped implementation, repair and self-checks | Actual artifacts, check results and remaining issues |
| Quality engineer `research-qa` | Independent verification against original requirements | Passed checks, specific defects and reproduction or verification evidence |
| Delivery editor `research-editor` | Explanation, consistent wording and packaging | Usable delivery package and unresolved content questions |

Assignments involving topic generation, selection, novelty or continuation must carry
the [shared topic-selection policy](../shared-references/topic-selection-policy.md).
The main agent uses the same standard for acceptance.
This policy also applies to the main agent's on-demand research judgments; it
does not activate delegation or extend the requested scope.

For fresh exploration or reselection, pass the scoped brief and necessary sources
under the [context policy](../shared-references/topic-context-policy.md#generate-before-recalling-old-judgments),
not the full parent conversation or prior rankings. Use an existing role when
authorized and verify the actual input boundary. Record inherited-context limits
when isolation is unavailable; do not treat delegation alone as independence.

Use existing specialists such as brainstormer when needed, with assignments from the
main agent. Supply the skills relevant to each role. The controller coordinates stages
and execution; specialist skills provide methods. Use actual runtime delegation
capabilities. A role label can describe an assignment, but renaming the same agent
does not create independent verification. If delegation is unavailable, report that
and complete the work that remains possible.

In Claude Code, delegate with the Agent tool and set `subagent_type` to the role
name in the table (definitions in `$RESEARCH_ROOT/.claude/agents/`), or to an
existing specialist such as `brainstormer` or `idea-critic`. These start in a
fresh context, so the assignment must carry the brief, sources, writable scope and
acceptance criteria. `subagent_type: "fork"` inherits the whole conversation and
does not count as an independent check or an isolated topic pass. Agents run in
the background: never predict a result before its notification arrives, and relay
what matters because the user does not see agent reports. Continue an agent with
SendMessage; a new Agent call starts fresh. Give parallel writers disjoint files,
or `isolation: "worktree"` inside a git repository. Every role here is Claude, so
role QA is same-family; cross-family review uses the reviewer skills' Codex route.

## Responsibility for full-workflow completion

On-demand coordination ends after the requested scope. The full-paper default
and continuous-progression responsibility below apply only in automatic mode.

In automatic mode, follow the [full-workflow delivery rules](references/full-flow.md)
from valid existing artifacts to final delivery. Establish the endpoint and stage
acceptance criteria at the start. For a paper-research task without a narrower endpoint,
deliver an inspectable complete draft, applicable reproduction materials and verification
report. Advance between accepted stages without treating a topic, plan, pilot or agent
report as full completion or asking for permission at every transition.

The post-selection human checkpoint is a required exception to automatic stage
handoff: report the proposed topic, record `AWAITING_TOPIC_APPROVAL` and wait.
After the user's explicit approval, resume the remaining authorized stages.

Reuse the existing plan or tracker for artifact locations, actual status, next actions
and unresolved dependencies so work can resume after interruption. Accept artifacts
before advancing dependent stages. Pilot stopping rules, resource caps and real external
dependencies remain effective. Complete independent work and report actual results and
unfinished items when they apply; do not claim full completion. Distinguish preflight
failures, scientific outcomes and project completion under full-flow's ending conditions.
A format or execution failure does not reject the whole study. Finish at the requested
endpoint without expanding the objective. Standalone revision entrypoints retain their scope.

## Assignment and management

Each assignment specifies its objective, necessary context, inputs, owner, writable
files or objects, dependencies, deliverables, acceptance criteria, budget and stopping
conditions. Simple tasks do not require a table.

Give each deliverable one owner. Parallel writers receive disjoint scopes; one owner
integrates shared files without overwriting other sessions' or contributors' changes.
Reuse the project's plan or tracker. Add a compact record only when sustained
collaboration needs one; do not create competing ledgers.

Agents report questions to the main agent, which supplies context, coordinates or
reassigns work. Repeated attempts without progress require a new diagnosis within
the budget and stopping rules. Only the main agent arranges further delegation.

## Clarification cards and default decisions

In on-demand mode, clarify only material missing information and continue work
that does not depend on it. Direct execution of delegated decisions below applies
only in explicitly activated automatic mode.

The main agent makes routine technical choices. Send clarification cards for real
tradeoffs affecting direction, scope or cost. Investigate enough to make the options
reviewable before issuing a card, and keep unknowns explicit.
Use the shared [human decision points](../shared-references/research-autonomy.md#human-participation-at-consequential-decisions).
Planning, hypothesis generation, protocol implementation and validation within the
agreed scope do not require operation-by-operation approval. Previously authorized
defaults remain usable; new authority and final academic commitments stay with the user.

Topic approval follows the
[mandatory human checkpoint](../shared-references/topic-selection-policy.md#human-approval-after-topic-selection),
not the ordinary card template below. It has no timeout, automatic default
or main-agent substitute for approval. Mark it `decision_kind: "topic_approval"`
and `delegated: false`; only an actual user reply can release dependent work.

Use one decision per card, normally with 2–3 executable options and the recommendation
first. Include:

> **D1 | Decision needed**  
> Context: why this decision matters now.  
> A (recommended): action, benefits, and costs.  
> B: an alternative and its tradeoffs. Add C only for a distinct viable option.  
> Rationale: why the recommendation fits the current goal.  
> Default: A. Response: wait for the user's answer, unless the card is authorized for automatic selection.  
> Next action: the concrete step following this decision.

The user may select an option or correct its premise. In Claude Code, ask a card
that needs the user's answer with AskUserQuestion: one question per card, the
options as choices with the recommendation first and labelled `(Recommended)`,
benefits and costs in each description; "Other" lets the user correct the premise.
Finish unaffected work before asking, because AskUserQuestion blocks until answered.
Claude Code has no card timer, so it cannot run a timed response window. In
automatic mode, cards authorized for immediate or timed selection do not block:
state the card and the adopted option in the progress message, record its source
and continue. Check any user message that has arrived before dependent work; a
later reply steers work not yet executed. Topic approval always waits for an
explicit reply: deliver the Chinese topic report and end the turn, or ask with
AskUserQuestion after the report. Silence or a dismissed question is not approval.

In automatic mode, the main agent directly selects and executes the recommended
option within existing delegated authority. Follow the
[decision-card policy](references/decision-cards.md): record the options, choice,
evidence, rationale, authority and downstream effects in the existing task record.
There is no separate decision model, MCP call, probability output or confidence
threshold. When evidence is insufficient, prefer an authorized, bounded, reversible
check that reduces uncertainty. A recommendation is not scientific evidence or
independent acceptance. Explicit user replies take precedence; neither a default
nor a recommendation supplies missing authority.

Defaults cannot exceed explicit user limits or replace approval required by a tool.
If a default needs unavailable access, resources or budget, finish independent
preparation and report that dependency. Do not claim timers, automatic resumption
or background execution without actual runtime support. In Claude Code, a Bash
command with `run_in_background` or a Monitor re-invokes the agent when it finishes,
but only while this session stays open; ScheduleWakeup works only inside `/loop`.
Nothing resumes after the session ends unless the user starts it again. Later user
replies steer unfinished work; report decisions already executed and their outcomes
accurately.

## Lightweight acceptance and delivery

In on-demand mode, follow the selected skill's verification requirements and
main-agent checks. The root quality role is used only in automatic mode; any
independent checks required by a standalone skill retain that skill's own scope.

Implementers check their own work first. An independent quality agent checks important
tasks against original requirements, actual artifacts and source evidence; the main
agent may spot-check small tasks. Return concrete defects to their owner. List optional
improvements separately without expanding scope or blocking an adequate deliverable.

The main agent checks goal coverage, evidence and integration, investigating pivotal
points or anomalies. Reuse valid checks when their inputs are unchanged and verify
new effects introduced by integration. An agent's completion report requests acceptance;
it does not replace inspectable results or the main agent's responsibility.
For pivotal empirical claims, QA checks the original protocol, actual conditions,
raw evidence, analysis and claim wording. A mismatch blocks the affected scientific
conclusion until repaired or appropriately qualified, without discarding valid
independent findings. Human signoff or model agreement cannot waive evidence checks.

For topic decisions, check consequential constraints against their original sources
and the scoped brief, including automatic memory/context inputs where observable.
Preserve agent-selected assumptions and delegated decisions as such in the accepted
record; summaries must not relabel them as user requirements.

Report concisely what was completed, verified and remains unresolved, including
default decisions and their effects where relevant. Preserve valid artifacts, failures
and genuine unknowns. Agreement among agents does not replace evidence.

Local provenance: research-specific roles, with
reference to [gstack stage handoffs](https://github.com/garrytan/gstack/blob/main/docs/skills.md)
and [decision classification](https://github.com/garrytan/gstack/blob/main/autoplan/SKILL.md).
