# Reviewer Routing

## Local configuration (overrides the upstream defaults below)

The reviewer backend and model are configured, not built in. Read them from the
environment (`REVIEWER_BACKEND`, `REVIEWER_MODEL`, `REVIEWER_EFFORT_DEEP`,
`REVIEWER_EFFORT_REGULAR`) or `$RESEARCH_ROOT/.tools/reviewer.json`
(`backend`, `model`, `effort_deep`, `effort_regular`). `$REVIEWER_MODEL` below
means that configured model; the deep-audit and regular tiers map to the two
configured effort values. The Codex MCP bridge works with whatever provider the
user's Codex CLI is configured for (an official API, Azure, a local or other
OpenAI-compatible endpoint). If nothing is configured, use the `manual` backend
or report that external review is unavailable; never present self-review as an
external review.

**Making Codex use a named skill.** Codex does not load skills from `.claude/skills/`.
Pass `cwd: $RESEARCH_ROOT`, give the absolute `SKILL.md` path in the prompt, and ask
Codex to begin its reply with `SKILL LOADED: <name>`; without that line, treat the
review as not run under the skill.

## Backends

| Backend | Selected by | Calls |
|---|---|---|
| `codex` (default) | configuration, or `— reviewer: codex` | `mcp__codex__codex` for a new thread, `mcp__codex__codex-reply` for follow-up rounds |
| `manual` | configuration, or `— reviewer: manual` | The main agent writes the review brief to a file; the user runs it in a model of their choice and pastes the reply back |

The reviewer should come from a different model family than the executor
(OpenAI, Anthropic, Google, DeepSeek, Moonshot/Kimi, Qwen, …). If the families
cannot be shown to differ, report the review as same-family or unverified rather
than as independent cross-model review.

## Codex backend

- Pin both `model: $REVIEWER_MODEL` and `config: {"model_reasoning_effort": <tier effort>}`
  in the first call of every thread. Verdict-bearing audits (`research-review`,
  `paper-claim-audit` and similar one-shot judgments) use the deep effort; other
  reviewer calls, including every round of a multi-round thread, use the regular
  effort. Do not rely on `~/.codex/config.toml` defaults.
- `codex-reply` continues a thread with the model, effort, sandbox and cwd it was
  created with; pass only the saved `threadId` and the message.
- If the first call fails because the configured model or effort is explicitly
  rejected as unsupported, report that and ask the user to correct the
  configuration. Do not substitute a model on your own.
- Never retry blindly on a timeout, rate limit, authentication, transport, server
  or parse error: the review may already have run. Report `REVIEW_UNAVAILABLE`
  (or `ERROR` for an audit artifact) instead of a verdict.
- After upgrading Codex CLI, restart the Claude Code session so the `codex` MCP
  server (`.agents/mcp-servers/codex-exec/server.py`) picks up the new binary.

## Manual backend

1. Write the same substantive brief Codex would receive to
   `review-stage/<skill>-<YYYYMMDD>-<NN>.prompt.md` in the project, with the
   primary artifacts attached or pasted inline (a remote web UI cannot read local
   paths). Add one response-format line: the reply must begin with
   `Reviewer-Model: <exact-model-id>`.
2. Ask the user to run it in a model from a different family and paste the full
   reply back, or save it beside the prompt as `.response.md`. Wait for it; do not
   draft the reviewer's answer yourself.
3. For a follow-up round, write the next prompt in the same way and ask the user to
   continue in the same model conversation.
4. A reply without a classifiable `Reviewer-Model` line, or from the executor's
   family, cannot acquit an acceptance check; record it as `REVIEW_UNAVAILABLE`
   for that purpose and keep its content as advisory feedback.

## Invariants

- Reviewer independence ([reviewer-independence.md](reviewer-independence.md))
  applies to both backends: pass primary artifacts, not executor summaries.
- Trace every reviewer call ([review-tracing.md](review-tracing.md)).
- An unavailable or failed review is reported as unavailable, never replaced by
  self-review or a silent backend switch.
