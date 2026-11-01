# Review Tracing Protocol

## Purpose

Save the full prompt and response of every cross-model reviewer call, so that:
- **Reviewer independence can be checked:** the trace shows whether the executor
  passed primary files or its own summaries.
- **Reviews can be resumed and reproduced:** the `threadId` and the model and effort
  that actually ran are recorded.
- **Surprising verdicts can be explained** from the transcript instead of by
  re-running the reviewer.

## When to trace

After every reviewer call that serves a review, audit or critique function:
`mcp__codex__codex`, `mcp__codex__codex-reply`, and each manual-review round
(see [reviewer-routing.md](reviewer-routing.md)). Failed attempts are traced too,
with `--status error`. Purely informational calls are not traced.

## Where

```
.aris/traces/<skill-name>/<YYYY-MM-DD>_run<NN>/
  ├── run.meta.json                 # run-level metadata
  ├── 001-<purpose>.request.json    # request snapshot
  ├── 001-<purpose>.response.md     # full response text
  ├── 001-<purpose>.meta.json       # response metadata
  └── 002-...                       # follow-up rounds
```

`<purpose>` is a short kebab-case label such as `round-1-review` or `audit`.
`.aris/` is project-local and ignored by git; traces may contain unpublished work.

## How

Use the bundled helper when it resolves (`install.sh` registers
`.agents/aris/tools/` for the resolver below):

```bash
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
if [ -z "${ARIS_REPO:-}" ] && [ -f .aris/installed-skills.txt ]; then
    ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null) || true
fi
TRACE_HELPER=".aris/tools/save_trace.sh"
[ -f "$TRACE_HELPER" ] || { [ -n "${ARIS_REPO:-}" ] && TRACE_HELPER="$ARIS_REPO/tools/save_trace.sh"; }
[ -f "$TRACE_HELPER" ] || TRACE_HELPER=""

if [ -n "$TRACE_HELPER" ]; then
  bash "$TRACE_HELPER" \
    --skill "<skill-name>" --purpose "<purpose>" \
    --backend "<codex | manual>" --tool "<mcp__codex__codex | mcp__codex__codex-reply | manual>" \
    --model "<model that actually ran>" --effort "<effort that actually ran>" \
    --status "<ok | error>" --fallback-reason "<empty unless an attempt failed>" \
    --thread-id "<threadId, empty for manual>" \
    --executor-model "<model this session runs as, if known>" \
    --reported-reviewer-model "<model the reviewer reports, e.g. the Reviewer-Model line>" \
    --prompt-file "<file with the full prompt>" --response-file "<file with the full response>"
else
  echo "WARN: save_trace.sh not resolved; writing trace files directly." >&2
fi
```

If the helper is unavailable, write the four files above directly. A missing
helper never means skipping the trace.

## Recorded identity

- Families (`openai`, `anthropic`, `google`, …) are derived from model strings:
  the reviewer-reported model if present, otherwise the requested model.
- `--executor-model` is caller-declared. A different family pair is recorded as
  `family_relation: "different"` with `independence_verified: "unverified"`; do not
  describe caller-declared identity as verified.
- Known same-family identities record `independence_verified: false`.

## Modes

Set inline with `--- trace: off | meta | full`:
- **`full`** (default): metadata plus full prompt and response.
- **`meta`**: metadata only, for sensitive projects.
- **`off`**: no tracing.

## Reading traces

When a verdict is surprising (a score drops after a fix, two reviewers disagree, a
reviewer forgets an earlier concern, a verdict contradicts a deterministic
check), read the transcripts before re-running the reviewer: diff the relevant
`.response.md` files and check which files each request actually pointed to. The
point where the assessment changed is the explanation; cite it.
