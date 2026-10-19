---
name: research-review
description: Get a deep critical review of research from an external reviewer backend (Codex or manual). Use when user says "review my research", "help me review", "get external review", or wants critical feedback on research ideas, papers, or experimental results.
argument-hint: "[topic-or-scope]"
allowed-tools: Bash(*), Read, Grep, Glob, Write, Edit, mcp__codex__codex, mcp__codex__codex-reply, mcp__manual_review__review, mcp__manual_review__review_reply
---

# Research Review via External Reviewer Backend (deep reasoning)

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

For structure or evidence requirements, use [paper-type-routing.md](../shared-references/paper-type-routing.md). Reuse the contribution type, stage and venue from existing materials; select only claim-relevant checks. This selects guidance within the current task and does not start another phase.

Include the [claim-preservation policy](../shared-references/claim-preservation.md) in substantive review briefs (readable path or text). For requested revision rounds, retain the reference/current claim, evidence-linked corrections and resolved/open concerns in the existing brief. Review remains optional and user-requested; this integration does not start a model call or an automatic revision loop.

> 🔒 **Do not wrap this skill in `/loop`, `/schedule`, or `CronCreate`.** It is
> verdict-bearing — it produces a cross-model review verdict, multi-round with
> reviewer thread continuity. An external timer re-fires the verdict on
> wall-clock time and breaks the reviewer's round-to-round memory: zero new
> signal, full token cost. Schedule the *external wait that precedes it* (work
> ready → then review once), not the verdict. See
> [`shared-references/external-cadence.md`](../shared-references/external-cadence.md).

Get a multi-round critical review of research work from the selected external reviewer backend with maximum reasoning depth.

## Constants

- REVIEWER_MODEL — the configured reviewer model (see [reviewer configuration](../shared-references/reviewer-routing.md#local-configuration-overrides-the-upstream-defaults-below)), at the configured deep-audit effort. Any model the selected backend can serve; it should come from a different family than the executor (OpenAI, Anthropic, Google, DeepSeek, Moonshot/Kimi, Qwen, …).
- **REVIEWER_BACKEND** — the configured backend; upstream default is Codex MCP. Override with `— reviewer: oracle-pro` for Oracle MCP, or `— reviewer: manual` for Manual Review MCP. If manual-review MCP is unavailable, stop and print the install command; do not fall back to Codex. See `shared-references/reviewer-routing.md`.

## Reviewer Calling Convention

When calling the reviewer, branch on REVIEWER_BACKEND:

**If REVIEWER_BACKEND = `codex`:**
  Use `mcp__codex__codex` for new review threads.
  Use `mcp__codex__codex-reply` for follow-up rounds (reuse threadId).

**If REVIEWER_BACKEND = `manual`:**
  Use `mcp__manual_review__review` for new review threads with:
    prompt: [exact same prompt that would go to Codex]
    config: {"model_reasoning_effort": "xhigh", "executor_model": "<actual executor model>", "require_reviewer_model": true}
  Save the returned `threadId`.
  Use `mcp__manual_review__review_reply` for follow-up rounds with:
    threadId: [saved manual-review threadId]
    prompt: [follow-up prompt]
    config: {"model_reasoning_effort": "xhigh", "executor_model": "<actual executor model>", "require_reviewer_model": true}

Content fidelity: the manual reviewer should see the same substantive review
brief Codex would read. If the manual UI supports file upload / attachment,
reuse the same brief file; otherwise paste the brief contents inline because
remote web UIs cannot read your local filesystem paths. Review tracing applies
equally to both backends.

## Context: $ARGUMENTS

## Prerequisites

- **Codex MCP Server** configured in Claude Code:
  ```bash
  claude mcp add codex -s user -- python3 "$HOME/aris_repo/mcp-servers/codex-exec/server.py"   # your ARIS clone's path
  ```
- This gives Claude Code access to `mcp__codex__codex` and `mcp__codex__codex-reply` tools

## Full project review

For a full review of a project with a paper, use
[split-review.md](../shared-references/split-review.md): a Claude sub-agent audits
the research materials while Codex reviews only the paper as a venue reviewer.

## Workflow

### Step 1: Gather Research Context
Before calling the external reviewer, compile a comprehensive briefing:
1. Read project narrative documents (e.g., STORY.md, README.md, paper drafts)
2. Read any memory/notes files for key findings and experiment history
3. Identify: contribution type(s), current stage, target venue/track if any, core
   claims, evidence, key results and known weaknesses. Carry the selected
   paper-type profile and its claim-specific obligations into the brief, as a
   readable path or text; do not classify every project with code as tooling.

### Step 2: Initial Review (Round 1)
Send a detailed prompt at the configured deep-audit effort, using the selected backend. For
the `codex` backend, keep the MCP payload short: write the full briefing to
`RESEARCH_REVIEW_REQUEST.md`, then point Codex at that file.

*For codex backend:*

```
mcp__codex__codex:
  model: $REVIEWER_MODEL
  config: {"model_reasoning_effort": "$REVIEWER_EFFORT_DEEP"}
  prompt: |
    Read the review brief at <absolute path to RESEARCH_REVIEW_REQUEST.md>.
    Executor notes are not evidence beyond the files they cite, so verify the
    referenced artifacts before judging.
    Evaluate the stated question and contribution using the requested venue/track
    when one is specified. Verify both supported claims and alleged weaknesses
    against the artifacts. Apply the paper-type route and claim-preservation
    policy in the brief. Use only checks justified by a claim or verified venue rule. Identify:
    1. Specific logical gaps or unsupported assertions, with evidence locators
    2. Experiments necessary for the current claim, separated from optional extensions
    3. Narrative problems, including unnecessary weakening of supported contributions
    4. Whether the remaining contribution answers a useful question; explain any
       venue-specific concern rather than imposing an unspecified top-venue standard

    === SCOPE AND APPLICABILITY ===
    For a paper, idea or result: assess its actual contribution and evidence.
    Do not assume it is a research-workflow tool, impose a method-paper template,
    invent a threat model, or exclude security/formal mechanisms by default.
    For an explicitly requested local workflow-tool/code audit: use the project's
    documented operating assumptions and engineering constraints. Do not propose
    infrastructure or speculative hardening without a demonstrated defect,
    invariant or authorized requirement. Scope limits do not hide real defects.
    In either case, identify the claim/rule affected by each finding and separate
    necessary corrections from optional extensions. Do not manufacture issues.

    Say plainly when something is correct.
    Be brutally honest. If, after genuinely trying to break it, the work
    holds up and is ready, say so clearly.
```

The review brief should contain the full research context, the specific
questions, and the primary artifact / raw-result paths the reviewer should
inspect.

*For manual backend:* use `mcp__manual_review__review` with the same brief
contents. If the manual-review UI supports attachments, attach
`RESEARCH_REVIEW_REQUEST.md`; otherwise paste the brief inline. Save the
returned `threadId`.

### Step 3: Iterative Dialogue (Rounds 2-N)
For `codex` backend: use `mcp__codex__codex-reply` with the returned `threadId`.
For `manual` backend: use `mcp__manual_review__review_reply` with the same `threadId`.
Use the appropriate tool to continue the conversation. For Codex follow-up
rounds, write an updated brief such as `RESEARCH_REVIEW_ROUND_2.md` and send
only the path:

```text
mcp__codex__codex-reply:
  threadId: [saved reviewer threadId from Step 2]
  # replies inherit the thread's model/effort ($REVIEWER_MODEL, deep-audit effort)
  prompt: |
    Read the updated review brief at <absolute path to
    RESEARCH_REVIEW_ROUND_2.md>.
    Check unresolved issues against their evidence and whether corrections
    address them. Do not reopen resolved scope concerns without identifying a
    remaining unsupported assertion or a new basis. Compare any further narrowing
    with the justified reference claim and assess the remaining contribution.
```

For manual follow-up rounds, attach that same updated brief if possible;
otherwise paste it inline.

For each round:
1. **Respond** to criticisms with evidence/counterarguments
2. **Ask targeted follow-ups** on the most actionable points
3. **Request specific deliverables** within the authorized scope: evidence-linked corrections, justified claim changes and remaining contribution; experimental designs or new outlines only when requested. Retain resolved concerns so the same limitation does not cause repeated weakening.

Key follow-up patterns:
- "If we reframe X as Y, does that change your assessment?"
- "What's the minimum experiment to satisfy concern Z?"
- "Please design the minimal additional experiment package (highest acceptance lift per GPU week)"
- "Please write a mock NeurIPS/ICML review with scores"
- "Give me a results-to-claims matrix for possible experimental outcomes"

### Step 4: Convergence
Stop iterating when:
- Both sides agree on the core claims and their evidence requirements
- A concrete experiment plan is established
- The narrative structure is settled

Agreement alone does not establish value or correctness. Before treating a materially
narrowed story as settled, verify that the remaining contribution still answers a
useful question. If not, state the unresolved contribution and applicable options
under the shared policy; do not keep shrinking merely to obtain reviewer agreement.

### Step 5: Document Everything
Save the full interaction and conclusions to a review document in the project root:
- Round-by-round summary of criticisms and responses
- Evidence-supported claims, narrative, remaining value, and any authorized experiments; distinguish consensus from evidence and preserve reasons for substantive claim changes
- Claims matrix (what claims are allowed under each possible outcome)
- Prioritized TODO list with estimated compute costs
- Paper outline if discussed

Update project memory/notes with key review conclusions.

> **Composed mode** — if invoked with `— composed: <canonical-report-path>` (an
> orchestrator like `/idea-discovery` passes this), do **not** write a standalone review
> `.md` in the project root. The raw conversation is already persisted to `.aris/traces/…`
> (see *Review Tracing* below — that audit copy is kept in every mode); fold the review
> *conclusions* (consensus, claims matrix, prioritized TODOs) into the orchestrator's
> canonical report and cite the trace path there. **Default (no `— composed:` directive):
> behave exactly as above — write the standalone review document.** Never infer composed
> mode from a report file merely existing. Full rules:
> [`shared-references/output-composition.md`](../shared-references/output-composition.md).

## Key Rules

- ALWAYS pin `model: $REVIEWER_MODEL` + `config: {"model_reasoning_effort": "$REVIEWER_EFFORT_DEEP"}` for reviews (deep-audit tier; capability fallback per `reviewer-routing.md`, never below the configured regular effort)
- That pin is the **Codex** backend's. For `manual`, use the identity-bearing config from the Reviewer Calling Convention above; `model`, `sandbox` and `cwd` are Codex-only
- Put comprehensive context in the review brief. Codex can read local files
  when you pass an absolute path; manual reviewers usually cannot, so attach or
  paste the same brief there.
- Be honest about weaknesses — hiding them leads to worse feedback
- Push back on criticisms you disagree with, but accept valid ones
- Focus on ACTIONABLE feedback — "what experiment would fix this?"
- Document the threadId for potential future resumption
- The review document should be self-contained (readable without the conversation)

## Prompt Templates

### For initial review:
"Review the stated research question and contribution against the supplied evidence and requested venue/track. Apply the claim-preservation policy: justify necessary corrections, retain supported significance and separate optional extensions."

### For experiment design:
"Please design the minimal additional experiment package that gives the highest acceptance lift per GPU week. Our compute: [describe]. Be very specific about configurations."

### For paper structure:
"Please turn this into a concrete paper outline with section-by-section claims and figure plan."

### For claims matrix:
"Please give me a results-to-claims matrix: what claim is allowed under each possible outcome of experiments X and Y?"

### For mock review:
"Please write a mock NeurIPS review with: Summary, Strengths, Weaknesses, Questions for Authors, Score, Confidence, and What Would Move Toward Accept."

## Review Tracing

After each reviewer call (`mcp__codex__codex`, `mcp__codex__codex-reply`, `mcp__manual_review__review`, or `mcp__manual_review__review_reply`), save the trace following `shared-references/review-tracing.md` (Policy C — forensic; never silently skip). Use `save_trace.sh` (resolved per the chain in `shared-references/integration-contract.md` §2) or write files directly to `.aris/traces/<skill>/<date>_run<NN>/`. Respect the `--- trace:` parameter (default: `full`).
  A verdict-bearing manual response MUST begin with
  `Reviewer-Model: <exact-model-id>` — pass the model THIS session is actually
  running as in `executor_model`. Missing, unknown, or same-family identity
  cannot acquit; emit `REVIEW_UNAVAILABLE` rather than guessing. If the executor
  model cannot be named, manual review's cross-family claim is unprovable — say
  so in the report instead of asserting it.
