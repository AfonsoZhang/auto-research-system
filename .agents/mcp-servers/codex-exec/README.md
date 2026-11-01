# codex-exec — the `codex` MCP server for this repository

Adapted from ARIS (`mcp-servers/codex-exec`, MIT; see `THIRD_PARTY_NOTICES.md`).

On the Claude Code host, skills reach Codex through the MCP tools
`mcp__codex__codex` and `mcp__codex__codex-reply`: external review
(`shared-references/reviewer-routing.md`) and the built-in image handoff in
`nature-figure`. This bridge provides both tools by running each call as a
`codex exec` subprocess and returns `{threadId, content}`. It is optional; without
it, external review and built-in image generation are reported as unavailable.

## Register

Requirements: `codex` on PATH and logged in (a version with `codex exec resume`);
Python 3.9+; no packages.

`install.sh` does not register this server. From the repository root, register it
for this project only:

```bash
claude mcp add codex -s project -- python3 "$PWD/.agents/mcp-servers/codex-exec/server.py"
```

or add the equivalent entry to `.mcp.json`:

```json
"codex": {
  "type": "stdio",
  "command": "python3",
  "args": ["/absolute/path/to/this/repo/.agents/mcp-servers/codex-exec/server.py"]
}
```

Restart Claude Code; `claude mcp list` should show `codex … ✓ Connected`. The
server key must be `codex`, because skills call `mcp__codex__*`. The Codex host
(`install.sh --host codex`) does not use this bridge; it uses
`.agents/mcp-servers/claude-reviewer/` in the opposite direction.

## What a call becomes

| MCP argument | `codex exec` |
|---|---|
| `prompt` | stdin (no argv limit) |
| `model` | `-m MODEL` |
| `config` `{"model_reasoning_effort": "high"}` | `-c model_reasoning_effort="high"` (nested objects become dotted keys) |
| `sandbox` | `--sandbox MODE` |
| `cwd` | `--cd DIR` |
| `codex-reply` `threadId` | `codex exec resume THREAD` **plus the model, config, sandbox and cwd the thread was created with**; `resume` alone would fall back to `config.toml` defaults, and reviewer routing relies on a continued thread keeping its reviewer model and effort |

The reviewer model and efforts come from `.tools/reviewer.json` (see
`config/reviewer.example.json`). Per-thread settings live in
`~/.codex/state/codex-exec/threads/<threadId>.json`, one file each
(`CODEX_EXEC_STATE_DIR` overrides the directory), so a continued thread survives a
bridge restart. Thread IDs that are not plain identifiers are rejected.

A failed turn (unknown model, auth, API error) comes back as `isError: true` with
Codex's own error text; reviewer routing treats it as review unavailable, never as
a verdict.

While a call runs, the bridge streams `codex/event` notifications and, when the
host passes a `progressToken`, a `notifications/progress` heartbeat every 15 s
(`CODEX_EXEC_PROGRESS_INTERVAL_SEC`), answers `ping`, and honours
`notifications/cancelled`. Notifications cannot override a host's hard tool
timeout; deep reviews at high effort can run 30+ minutes.

Not offered, because `codex exec` cannot honour them: `approval-policy`,
`base-instructions`, `developer-instructions`, `compact-prompt`.

Debugging: `CODEX_EXEC_DEBUG_LOG=/path/to/log` records every request and the exact
`codex exec` command line; `CODEX_BIN` points at a specific codex binary. Tests:
`python3 -m unittest discover -s tests -p test_claude_host.py` from the repository root.
