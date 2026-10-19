---
name: novelty-check
description: Verify research idea novelty against recent literature. Use when user says "查新", "novelty check", "有没有人做过", "check novelty", or wants to verify a research idea is novel before implementing.
argument-hint: "[method-or-idea-description]"
allowed-tools: Bash(*), Write, WebSearch, WebFetch, Grep, Read, Glob, mcp__codex__codex
---

# Novelty Check Skill

Read the [shared topic-selection policy](../shared-references/topic-selection-policy.md)
before judging the idea. It defines the common contribution scale and four
decisions. For literature handling, also read the
[publication/version policy](../shared-references/publication-policy.md). Reuse
the topic's existing publication records (or supplied path), and verify/append
new candidates. Record publication status, review status, selected version and
official evidence. Include labeled preprints in the competitive scan.

Check the proposed idea: **$ARGUMENTS**. This is an early contribution check,
not a prediction of paper acceptance or permission to implement the idea.

## Constants

- REVIEWER_MODEL = `$REVIEWER_MODEL` — used only if a permitted Codex MCP review is requested.

## Phase A: Extract claims and possible contributions

Identify the central claims needed for the idea, without a fixed count:
the question, mechanism or evaluation design, setting/assumptions, proposed
finding, and its intended scientific/practical use. Distinguish a new method
from a new finding, combination, resource, failure boundary or replication.
An unclear claim needs refinement; a simple or incremental claim is eligible.

## Phase B: Search and compare

Use the available requested scholarly sources and local records. Search multiple
technical formulations for each central claim, starting with closest work and
following references. Use dates relative to the current search date and relevant
venues; include foundational work and the latest six months of preprints. Report
unavailable sources and coverage gaps, not exhaustive-search claims.

Verify bibliographic identity and publication/version status. Abstracts can screen
candidates, but a decisive overlap judgment requires reading the relevant method,
setting and result passages. Compare question, mechanism, assumptions, evidence
and conclusion. State the substantive delta and locate the overlapping passages.
Similar titles or shared components cannot settle the decision in either direction.

## Phase C: Optional cross-model verification

Honor user restrictions on external models and tools. If the user requests review
and a permitted bridge is available, call REVIEWER_MODEL through
`mcp__codex__codex`. Otherwise complete the check with available evidence; a model
call is not a novelty requirement and missing it is not a reason to reject.

For a substantial request, write a project-local dossier using existing artifact
paths, including the proposed claims, verified paper comparison, unresolved items
and the exact shared policy or a readable absolute path to it. Ask the reviewer to
use CONTINUE / VALIDATE_FIRST / PARK / STOP_CURRENT_VERSION, distinguish facts
from inference, and cite specific evidence for a negative judgment. Do not send
an older ABANDON rule or a numerical rejection cutoff alongside the shared policy.

Example bridge call (only within the authorized scope):

```text
mcp__codex__codex:
  model: $REVIEWER_MODEL
  config: {"model_reasoning_effort": "$REVIEWER_EFFORT_REGULAR"}
  prompt: Read <absolute dossier path>, including the shared topic-selection policy, and assess the claims and remaining delta.
```

Reviewer agreement does not replace verification of the cited papers. If the
reviewer returns a historical label/score, adjudicate its underlying evidence
under the shared policy before delivering the common decision.

## Phase D: Novelty report

Use the project's current artifact format where one exists. A compact report has:

```markdown
## Proposed contribution
[Question, contribution type and one-sentence candidate delta]

## Closest work
| Work / selected version | Publication / review status | Claim and evidence locator | Overlap | Substantive difference or unknown |
|---|---|---|---|---|

## Assessment
- Novelty: [established overlap, supported delta or specifically unverified]
- Research value: [what the finding enables or changes]
- Evidence and feasibility: [known results, unknowns, required resources]
- Decision: CONTINUE / VALIDATE_FIRST / PARK / STOP_CURRENT_VERSION
- Reason: [evidence; exact affected claim for STOP_CURRENT_VERSION]
- Next check/action: [smallest discriminating step, budget/stop or resumption condition if relevant]

## Positioning
[Honest difference from the closest work, without unsupported first/best claims]
```

Scores are optional comparison aids, never cutoffs. Uncertainty in a central
comparison means VALIDATE_FIRST; broad proximity alone is not such uncertainty.
An overlapping preprint can change priority wording without eliminating the value
of independent evidence, a distinct mechanism or another substantive contribution.

## Verification and tracing

Every candidate in the prior-work table uses `verify_papers.py` via the installed
[helper resolution chain](../shared-references/integration-contract.md) §2. If the
helper is unresolved or fails, retain entries as `[UNVERIFIED]` and describe the
gap. This helper checks existence, not novelty, publication or claim validity.
Never fabricate identifiers/titles. See the
[citation discipline](../shared-references/citation-discipline.md).

After any permitted `mcp__codex__codex` / `codex-reply` reviewer call, save the trace
under [review-tracing.md](../shared-references/review-tracing.md), using the existing
helper resolution chain or `.aris/traces/<skill>/<date>_run<NN>/`. Preserve the
`--- trace:` parameter (default `full`). Do not claim a model review was performed
when this optional phase was skipped. End after the requested check.
