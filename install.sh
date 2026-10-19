#!/usr/bin/env bash
# Set up the research system in place. Safe to re-run; never overwrites local config.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export RESEARCH_ROOT="$ROOT"
PY="${PYTHON:-python3}"

# Create a venv and install requirements; prefer uv when present (no ensurepip needed).
make_venv() {
  local dir="$1" req="$2"
  [ -x "$dir/bin/python" ] && "$dir/bin/python" -c "import sys" 2>/dev/null && [ -e "$dir/.installed" ] && return 0
  rm -rf "$dir"
  if command -v uv >/dev/null 2>&1; then
    uv venv -q --python "$PY" "$dir" && uv pip install -q --python "$dir/bin/python" -r "$req"
  else
    "$PY" -m venv "$dir" && "$dir/bin/pip" install -q -r "$req"
  fi || { rm -rf "$dir"; echo "venv setup failed for $dir (install uv, or python3-venv)"; return 1; }
  touch "$dir/.installed"
}

echo "RESEARCH_ROOT=$ROOT"
mkdir -p "$ROOT/.tools/clarification-decider" "$ROOT/.venvs"

# Local config: copied once from the examples, then owned by the user.
copy_once() { [ -e "$2" ] || { cp "$1" "$2"; echo "created $2 (edit it)"; }; }
copy_once "$ROOT/config/decider.example.json" "$ROOT/.tools/clarification-decider/config.json"
copy_once "$ROOT/config/image-provider.example.json" "$ROOT/.tools/image-provider.json"
copy_once "$ROOT/config/reviewer.example.json" "$ROOT/.tools/reviewer.json"

render() { [ -e "$2" ] || { sed "s#\${RESEARCH_ROOT}#$ROOT#g" "$1" > "$2"; echo "created $2"; }; }
render "$ROOT/.mcp.json.example" "$ROOT/.mcp.json"
render "$ROOT/.codex/config.toml.example" "$ROOT/.codex/config.toml"

# Decision-card MCP server (model-agnostic client; no weights are downloaded here).
make_venv "$ROOT/.venvs/clarification-decider" \
  "$ROOT/.agents/skills/research-agent-team/scripts/requirements-decider.txt"

# Optional: diagram rendering for nature-figure.
if [ "${WITH_DIAGRAMS:-0}" = 1 ]; then
  make_venv "$ROOT/.venvs/nature-diagrams" "$ROOT/.agents/skills/nature-figure/requirements-diagrams.txt"
fi

cat <<MSG

Done. Next:
  1. Edit .tools/clarification-decider/config.json (decision model), .tools/image-provider.json
     and .tools/reviewer.json, or leave them; unconfigured parts fall back to the main agent
     or report that the external step is unavailable.
  2. Optional literature keys as environment variables: EXA_API_KEY,
     SEMANTIC_SCHOLAR_API_KEY, OPENALEX_EMAIL (see .agents/skills/research-lit/SKILL.md).
  3. Start Claude Code or Codex in $ROOT. Add 'export RESEARCH_ROOT=$ROOT' to your shell profile
     if you run the helper scripts by hand.
MSG
