# Topic selection policy

When identifying the contribution and its evidence obligations, use [paper-type-routing.md](paper-type-routing.md). Contribution type, research stage and venue are separate; type does not itself determine novelty, value or the continuation decision.

Local decision policy. This is the shared
source for topic-selection judgments in this research installation. Read it
before ranking, rejecting or recommending a research direction. It supersedes
conflicting local score cutoffs, head-start tests and automatic rejection
heuristics in the installed skills; explicit user constraints take precedence.

## Scope and contribution size

Establish the research area from the current task and explicitly applicable user
requirements. This shared policy has no default method exclusion.

**User-set research direction.** The user's
core research direction is **agent infrastructure**: management mechanisms outside
the model itself, such as resource/context/memory management, scheduling,
evaluation and supervision, human handoff, and external knowledge and
skill/tool management. The user prefers contributions that **explain why a
design is right**: mechanisms, failure boundaries and principled comparisons,
rather than building a system for adoption. For fresh exploration with no field
given by the task, use this as the field. A field or scope set by the current
task or project takes precedence. This setting does not narrow the field to a specific
question, and it does not reopen existing projects.
Before generating or reopening directions, apply the
[topic context boundaries](topic-context-policy.md) to distinguish fresh exploration,
continuation and reselection, and to trace inherited constraints to their sources.
Calibrate to the actual field, contribution types and any specified venue's current
official requirements; examples below do not supply a topic or scope constraint.

Default target: one meaningful, focused research question with a distinguishable,
testable contribution and evidence sufficient for its claims. Valid contribution
types include a local mechanism improvement, a justified combination, a useful
new setting, an evaluation/metric/resource, a systematic empirical finding,
failure boundary, negative result or informative replication. A contribution may
matter to a specialized community; it need not introduce a full agent framework,
new foundation model or paradigm shift.

Separate **novelty**, **research value**, **evidence strength** and **feasibility**.
Disruptive potential and competitive advantage are optional strategic benefits,
not default admission requirements. Do not impose numerical novelty cutoffs,
required score counts, fixed improvement percentages, universal model/benchmark
counts, or a months/years competitive head start. An ordinary incremental change
still needs a meaningful contribution; changing a label, model or dataset alone
does not establish one. Identify what the change teaches or enables.

When comparing candidates, prioritizing uncertain assumptions or revisiting a
stuck project, use the [problem-selection strategy](problem-selection-strategy.md)
as needed. It supplies assumption, constraint and decision-branch methods; this
policy continues to govern contribution criteria and final decisions.

## Question value and hypothesis relationships

During generation and selection, state what answering the question would teach,
enable or change in a scientific or design decision. An easy ablation or an
unassigned component contribution is not sufficient reason to make it the main
research question. Attribution can be a primary contribution when its answer has
independent scientific value; otherwise keep it as supporting evidence for the
substantive question. Explaining why a design works can concern an entire process,
joint behavior or operating conditions, as well as individual components.

Before framing a question as "A or B", identify the proposed relationship: competing
explanations, upstream/downstream steps, mediation, complementary mechanisms or
interaction. Allow mechanisms to coexist. Record uncertain relationships as
hypotheses; do not invent exclusivity, a fixed number of rivals, or a dominant
component to complete a template. For causal questions, a short causal chain or
plain-language account is enough when it makes the proposed interventions clear.

For example, under a hypothesized X -> M -> Y pathway, X acting through M is part
of X's effect. Holding M fixed asks a different question from measuring X's total
effect. An absent effect at fixed M alone does not negate the mediated benefit.
Whether effects can be separated depends on well-defined interventions, feasible
comparisons and identification assumptions; neither separability nor inseparability
is automatic. Preserve interactions and essential dependencies when proposing a
comparison. An unresolved relationship calls for clarification or a better design,
not automatic rejection of the direction.

For open exploration, vary the substantive questions and expected contributions:
capability bottlenecks, design principles, empirical patterns, useful capabilities,
boundary conditions or mechanism explanations, as appropriate to the user's scope.
Changing component names within the same attribution question is not substantive
diversity. Use relevant lenses without fixed quotas or a requirement to broaden
an explicitly focused task. Do not demand surprising findings or a new method.

Keep the question's value, relevant relationship and role of any attribution test
in the existing candidate notes. Reuse this judgment in experiment planning;
no extra reviewer, subagent, causal package or separate report is required.

## Prior work and uncertainty

Use [publication-policy.md](publication-policy.md) for literature/version handling.
Reuse relevant verified publication records and search notes; do not create a
parallel bibliography. For fresh exploration, follow the context policy's ordering
for historical candidate evaluations; this does not delay relevant literature search.
Verified formally published/accepted work anchors synthesis
and publication calibration. Label Main, Findings, dataset tracks and workshops
accurately. Search relevant recent preprints as well: they can invalidate a
priority claim even though their review status differs.

Compare the **question, mechanism, setting/assumptions, evidence and conclusion**
against the closest relevant works. Read the actual passages needed for the
comparison. Topic/title similarity, a crowded field, famous competitors or a
simple method do not establish duplication. Conversely, a superficial difference
does not establish a substantive contribution.

A negative novelty judgment must name a verified work, locate the overlapping
claim, and explain what remaining contribution was considered. Retrieval failure,
unverified metadata and an unread method remain **unverified**. They cannot prove
absence of novelty or novelty itself. Do not downgrade merely to appear cautious,
and do not automatically pass an unresolved central comparison.

## Evidence and resources

- Match evidence to the actual claim. Select relevant strong baselines and simple
  controls; use mechanism ablations where the claim needs them. Assess uncertainty, repeatability and coverage
  where they affect the conclusion. No automatic newest-model or SOTA requirement.
- Distinguish invalid measurement, insufficient evidence, credible refutation and
  supported results. A single lower score is not automatic refutation. If valid,
  adequately informative controls refute a causal or superiority claim, retract
  or revise that claim; do not rescue it with invented thresholds or post hoc
  favorable subsets. Assess negative findings or failure boundaries separately.
- Choose the scientifically appropriate experiment first, then check compute,
  data, expertise, access and budget. Identify the preferred resources and ask
  about real acquisition/cost choices. Current lack of access alone does not
  invalidate a direction. Obtain authorization before dependent paid/resource work.
- Use a minimum decisive pilot before scaling when a central uncertainty warrants
  it. State what would support, refute or leave the claim unresolved, along with a
  bounded time/cost budget. Apply the [pilot outcome distinctions](../experiment-plan/SKILL.md#gate-further-investment-with-a-minimum-decisive-pilot):
  credible negative evidence can stop the tested campaign; inconclusive evidence
  leaves the claim unresolved, and technical failure leaves it unevaluated. Budget
  exhaustion pauses spending independently of those findings. A negative or
  unresolved scientific gate does not authorize scaling; bounded repairs and
  discriminating follow-ups use the existing authorization. Reuse the existing
  experiment-plan/analysis artifacts and user-approved stop conditions.

## Unified decisions

| Decision | Use when | Required explanation |
|---|---|---|
| CONTINUE | A meaningful, distinguishable contribution and a justified next step are identified | The delta, value, current evidence and next action; this is not acceptance prediction |
| VALIDATE_FIRST | A central mechanism, overlap comparison or claimed value is unresolved | The specific uncertainty, smallest decisive check, budget and continuation/stop conditions |
| PARK | An identified prerequisite or user priority prevents justified execution now | The missing prerequisite and a concrete condition for resuming |
| STOP_CURRENT_VERSION | Reliable evidence covers or refutes the claimed core contribution, and no worthwhile contribution remains within the current scope | Exact evidence, affected claim, alternatives considered and any reusable findings |

Apply one decision to the current candidate/version, not an entire field. An
interesting negative result may continue as a revised contribution, but changing
direction or scope needs the user's applicable authorization. Optional scores
serve comparison only and never determine the decision. Do not infer a decision
from the number of weaknesses. When revisiting old PURSUE/REFINE/KILL or reviewer
scores, inspect their evidence under this policy; retain historical records intact.

For delivery, state the contribution/delta, beneficiary or scientific use,
evidence/unknowns, chosen decision and next discriminating action. Include resource
or resumption conditions when applicable. Use existing project artifacts and
paths; do not force a fixed report template for a small revision.

## Human approval after topic selection

After fresh selection or reselection produces a proposed topic, report it to the
user and wait for their explicit decision before advancing research on that topic.
This mandatory checkpoint applies in automatic mode too. A CONTINUE
or VALIDATE_FIRST assessment is a scientific recommendation, not human approval.
General full-flow authorization and earlier delegation of decisions in automatic mode do
not waive this checkpoint.

Complete the preliminary literature, novelty and feasibility checks needed for a
reviewable proposal. Deliver a concise Chinese checkpoint report covering the
question and intended contribution, why it is worth pursuing relative to the
alternatives, the closest verified work and remaining uncertainty, and the proposed
next step with its time/cost bounds. Identify material assumptions chosen by the
agent. Keep internal records and task artifacts in English.

Offer concrete choices: **Continue with this topic and stated scope**, **Revise the
topic and report again**, or **Pause**. Recommend an option with reasons, but set
no automatic default or response deadline. Record `AWAITING_TOPIC_APPROVAL` with
the proposal version and report location in the existing tracker. Save the
selection deliverable and wait; do not start, queue or delegate the dependent full
review, experiment design/execution or manuscript drafting. This is an approval
checkpoint, not completion of the full research objective.

Neither silence, elapsed time, a main-agent fallback, a prior model choice nor a
session restart supplies approval. A structured card uses
`decision_kind: "topic_approval"`, `delegated: false`, and no default choice;
do not send it for automatic selection. Record an actual user response as the
decision source and bind approval to this topic/version, scope and existing budget.
An explicit continuation reply resumes the already-authorized workflow; a request
to revise authorizes that revision and another report, not downstream execution.

Reuse existing explicit approval for the same topic and scope. Routine revisions
and continuation of an approved project do not need another topic checkpoint.
A material replacement of the question or contribution requires a new report and
approval. Standalone skill requests still end with their requested deliverable;
this rule does not activate a workflow or add approval stops at every stage.

## Writing and revision handoff

During analysis or writing, [claim-preservation.md](claim-preservation.md) carries
the justified contribution across revisions. A material narrowing needs both an
evidence-based reason and reassessment of the remaining answer/value. This does
not reopen topic selection for ordinary language edits or impose minimum breadth.

## Stage and execution boundary

Brainstorming generates candidates; preliminary selection decides what deserves
checking. Neither requires already completed publication-scale experiments.
Publication readiness is a separate assessment using the selected venue and
finished evidence. Finding a paper nearby is not a decision about publishability.

This policy does not start another skill, experiment, reviewer/model call, team or
next phase. A standalone call finishes the requested task. Use optional handoffs
only within a user-requested multi-stage workflow. Respect each subproject's
configuration layout, artifact paths, frozen versions and narrower instructions.

## Calibration evidence (checked 2026-10-05)

The dated official criteria and published AI-agent examples are preserved in
[topic-selection-calibration.md](topic-selection-calibration.md). Load them only
when that field's contribution scale needs calibration; they are not default
generation inputs. Recheck current official requirements for an actual submission.
