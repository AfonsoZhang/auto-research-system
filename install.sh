#!/usr/bin/env bash
# Set up the research system in place. Safe to re-run; never overwrites local config.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export RESEARCH_ROOT="$ROOT"
HOST=claude
if [ "${1:-}" = "--host" ] && [ "$#" = 2 ]; then
  HOST="$2"
elif [ "$#" != 0 ]; then
  echo "Usage: bash install.sh [--host claude|codex]" >&2; exit 2
fi
case "$HOST" in claude|codex) ;; *) echo "Unknown host: $HOST" >&2; exit 2 ;; esac
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
mkdir -p "$ROOT/.tools" "$ROOT/.venvs"
"$PY" "$ROOT/scripts/retire_decider.py"

# Local config: copied once from the examples, then owned by the user.
copy_once() { [ -e "$2" ] || { cp "$1" "$2"; echo "created $2 (edit it)"; }; }
copy_once "$ROOT/config/image-provider.example.json" "$ROOT/.tools/image-provider.json"
if [ "$HOST" = codex ]; then
  copy_once "$ROOT/config/reviewer-codex.example.json" "$ROOT/.tools/reviewer-codex.json"
  "$PY" "$ROOT/scripts/build_codex.py"
else
  copy_once "$ROOT/config/reviewer.example.json" "$ROOT/.tools/reviewer.json"
fi

render() { [ -e "$2" ] || { sed "s#\${RESEARCH_ROOT}#$ROOT#g" "$1" > "$2"; echo "created $2"; }; }
if [ "$HOST" = claude ]; then
  render "$ROOT/.mcp.json.example" "$ROOT/.mcp.json"
else
  make_venv "$ROOT/.venvs/claude-reviewer" "$ROOT/.agents/mcp-servers/claude-reviewer/requirements.txt"
  "$PY" "$ROOT/scripts/configure_codex.py"
fi

# Optional: diagram rendering for nature-figure.
if [ "${WITH_DIAGRAMS:-0}" = 1 ]; then
  make_venv "$ROOT/.venvs/nature-diagrams" "$ROOT/.claude/skills/nature-figure/requirements-diagrams.txt"
fi

cat <<MSG

Done. Next:
  1. Edit .tools/image-provider.json and the host-specific .tools/reviewer*.json as needed.
     Unavailable external steps are reported honestly. Ordinary authorized decisions
     in automatic mode are made directly by the main agent.
  2. Optional literature keys as environment variables: EXA_API_KEY,
     SEMANTIC_SCHOLAR_API_KEY, OPENALEX_EMAIL (see .claude/skills/research-lit/SKILL.md).
  3. Start $HOST in $ROOT (Codex project MCP requires project trust). Add 'export RESEARCH_ROOT=$ROOT' to your shell profile
     if you run the helper scripts by hand.
MSG
