# Reviewer routing on Codex

The default external reviewer is Claude; the executor and language polisher are
Codex. This replaces the Claude-host Codex transport and effort examples, including
those embedded in individual skills. Scientific review tasks, independence,
primary-artifact inputs, split review, trace requirements and verdict criteria
remain unchanged. Explicit manual review remains available when configured.

Read `$RESEARCH_ROOT/.tools/reviewer-codex.json`. Environment overrides are
`CLAUDE_REVIEW_MODEL`, `CLAUDE_REVIEW_EFFORT_DEEP`, `CLAUDE_REVIEW_EFFORT_REGULAR`.
Do not reuse `.tools/reviewer.json`: that belongs to the Claude host.

Call `mcp__claude_reviewer__review` (discover its actual exposed name) with:
- `prompt`: the original review task, absolute skill path, raw artifact paths,
  venue and scope. Require `SKILL LOADED: <name>` when a named skill is required.
- `cwd`: absolute project directory.
- `executor_model`: actual known executor model ID; never infer it from the host
  name. Unknown identity cannot satisfy the cross-family acceptance gate.
- `tier`: `deep` for research-review, experiment-audit, paper-claim-audit,
  result-to-claim, proof-checker, kill-argument or meta-apply; otherwise `regular`.

Do not pass Codex `config`, `sandbox`, `approval-policy`, base instructions or
reasoning effort enums. The bridge pins the configured Claude model and effort,
exposes only Read/Grep/Glob, disables nested MCP and hooks, and resumes only its
own session IDs. The reviewer may read primary artifacts, but cannot execute
experiments or edit them. The main agent performs necessary executable checks.

Continue with `mcp__claude_reviewer__review_reply(threadId, prompt)` using the
returned ID; it retains model, cwd, tier and executor identity. Never substitute
`--continue` or the most recent unrelated session. A restarted bridge does not
recover session ownership automatically: start a new explicitly fresh review.
Record the returned actual model, identity sources, thread ID and raw review in
the existing trace schema. Caller-declared executor identity remains labelled
as such; do not describe it as independently attested. Check required skill
acknowledgement in the review text, not just the transport response.

Missing CLI/auth, unknown or same-family model, empty/error/malformed response,
timeout or missing session ID yields REVIEW_UNAVAILABLE, never a verdict. No
silent model downgrade, alternate paid dispatch or self-review fallback. An
ambiguous timeout may have consumed usage; inspect it before any explicit retry.
