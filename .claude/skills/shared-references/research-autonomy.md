# Research autonomy, validation and human decisions

Local operating principles. Apply within the
current task and its authorization. This policy does not activate automatic
mode, extend a standalone skill call, or change child-project entrypoints.

## Working language

Use English for maintained skill instructions, shared rules, agent briefs, internal
templates, progress updates, agent exchanges, clarification cards, plans, analysis
notes and newly authored research records. This applies to standalone work and
automatic mode; include the rule in delegated tasks. Keep the final conversational
report and the mandatory topic-approval report to the user in Chinese.

Preserve original quotations, bibliographic metadata, proper names, identifiers,
raw data and historical source records. Chinese examples used as translation data
or user-facing report samples may remain in their original language; their surrounding
instructions are English. An explicit request for a Chinese or bilingual deliverable
controls that deliverable's language. Do not infer such a request merely from the
language of the user's message or turn internal research notes into bilingual readers.

Apply this policy when maintaining shared copies. Language edits preserve scientific
criteria, authorization boundaries, runtime identifiers and source provenance.

## High autonomy within the agreed objective

The AI may actively plan research, generate candidate hypotheses and alternatives,
design discriminating experiments, choose methods, implement, analyze and propose
the next useful step. In a task authorized in automatic mode it executes that work
within the agreed scope and budget, without seeking approval for each operation.
A candidate hypothesis is a proposal until evidence supports it.

When generating or reopening topics, apply the
[topic context boundaries](topic-context-policy.md): establish the current scope
and preserve the origin of requirements, evidence and delegated agent decisions.

The user controls the goal, resource ceiling, material direction choices and
academic responsibility. Those responsibilities do not require the user to
originate every hypothesis, write every passage or personally inspect every line
of code. Preserve how ideas, decisions and results were produced. Use those
records for an accurate AI-use disclosure when requested; disclosure remains an
independent draft under [ai-use-drafter](../ai-use-drafter/SKILL.md).

## Scientific acceptance is separate from execution completion

Record both in the existing project tracker: whether the work ran and produced
the expected artifacts, and what the evidence actually establishes. A successful
process exit, completed task, plausible plot or reviewer/model score does not
establish a scientifically valid conclusion.

For empirical claims, check the full chain before accepting a result for a
dependent research decision or manuscript claim:

1. **Protocol:** before observing final outcomes, record the hypothesis or
   exploratory question, comparison, data/splits, metrics, analysis and stopping
   rules, relevant budget and protocol version. Use
   [experiment-plan](../experiment-plan/SKILL.md). Preserve amendments with their
   reasons and timing; label analyses introduced after seeing outcomes and use
   fresh evaluation when needed. Do not retrofit hypotheses or lower a success
   threshold to fit a favorable result.
2. **Execution and evidence:** reconcile the planned and actual runs, including
   failures, exclusions and deviations. Verify data separation, scoring and
   comparable baseline conditions. Trace configurations and raw outputs through
   [experiment records](../experiment-bridge/references/experiment-records.md);
   keep fixtures, pilots and main results distinguishable.
3. **Analysis:** check inclusion rules, aggregation, sampling units and relevant
   uncertainty. Reproduce the key summaries from identified raw records. Use the
   [analysis categories](../analyze-results/SKILL.md#classify-what-was-learned)
   to separate invalid measurements, inconclusive evidence, opposing evidence
   and supporting evidence.
4. **Conclusion:** trace each material empirical claim to that comparison and
   analysis, preserving its scope and inference strength. Keep observations,
   explanations and untested proposals distinct. Apply
   [claim preservation](claim-preservation.md) to both overstatement and
   unjustified weakening.

Inspect the chain for each pivotal claim; use independent QA when available and
appropriate. An independent check examines original protocols and raw artifacts,
not just the executor's summary. If independent verification is unavailable,
state the actual verification used. Human approval and agent consensus do not
replace evidence. Valid negative results can satisfy the research objective;
invalid measurements cannot be accepted as confirmation or refutation.

For theory, surveys and other non-empirical work, apply the relevant proof or source-evidence
obligations in [paper-type routing](paper-type-routing.md), rather than imposing
an experimental campaign.

## Local changes

The same standards apply to standalone skills and local edits. Load the policy
sections and specialist checks relevant to the change, reuse valid prior checks
and inspect only affected dependencies.

- **Wording or layout:** verify that meaning, numbers, applicable conditions and
  inference strength are preserved; unchanged substance does not reopen experiments.
- **Result figures or passages:** verify the affected source data, calculations,
  visual mappings, captions and linked conclusions.
- **Metrics or protocols:** identify affected analyses and conclusions; recompute
  or rerun the necessary parts within the task's scope and resource authorization.

A wording edit that changes a claim or its conditions is substantive and requires
the corresponding evidence checks. Report any evidence gap that cannot be resolved
within the current task; a local check does not authorize a wider research workflow.

## Human participation at consequential decisions

Reuse the user's existing decisions and delegated authority. Reserve clarification
cards for real choices affecting the objective, scope, resources or final academic
commitment:

- Establish or materially change the research goal, primary question or
  contribution type.
- Exceed the agreed budget, obtain missing access, or accept a resource/design
  tradeoff that changes what the study can establish.
- Decide a material change to the central claim or paper direction, or make
  final author, disclosure, submission or publication commitments requiring the
  user's decision. Such a choice cannot replace the evidence needed for a claim.

Present concrete options, a recommendation and their effects. Previously
authorized card choices may use the established default/decision-model
path in automatic mode, except the mandatory
[post-selection human checkpoint](topic-selection-policy.md#human-approval-after-topic-selection).
A new or replacement topic must be reported and explicitly approved before
downstream work, including in automatic mode; the main agent and decision model
cannot approve it. A decision needing new authorization stays with the user; elapsed time
cannot supply that authorization.

Routine planning, hypothesis generation, protocol implementation, debugging,
scheduled comparisons and already-budgeted follow-ups proceed within the current
task. Apply agreed pilot stops without asking again. The main agent owns routine
verification and provides inspectable evidence and remaining uncertainties for
human judgment, rather than transferring every operation back to the user.

Outward-facing actions stay with the user; existing rules for each: arXiv posting
time and the venue's anonymity policy for papers under review (verify on the
live CFP),
code/data release and submission (decided per paper, recorded in project memory),
sending unpublished text to an external model for polish. Collect
any pending ones in one list when reporting rather than deciding them in passing.

Retrieval in the loop (RITP) complements this: evaluative and design judgments
are calibrated against the closest published comparators before they are made,
and an unchecked judgment is labelled uncalibrated. It is applied where each
decision is made (search "RITP"): experiment-plan (metrics, extra blocks),
abstract-and-findings (Conclusion), limitation-and-risk-writer (borrowed
evidence), citation-discipline (claim validation), section-guidance (baseline
adaptations, weak arms), arxiv-packaging (title).
