#!/usr/bin/env python3
"""Retire this repository's old decision MCP registration without touching other servers."""
import json
from pathlib import Path
import re


def retire(root):
    json_path = root / '.mcp.json'
    if json_path.exists():
        data = json.loads(json_path.read_text())
        entry = data.get('mcpServers', {}).get('research_clarification', {})
        if any(str(arg).endswith('/research-agent-team/scripts/clarification_decider.py')
               for arg in entry.get('args', [])):
            del data['mcpServers']['research_clarification']
            json_path.write_text(json.dumps(data, indent=2) + '\n')
    toml_path = root / '.codex/config.toml'
    if toml_path.exists():
        text = toml_path.read_text()
        # Match complete top-level MCP tables, preserving unrelated text verbatim.
        pattern = r'(?m)^\[mcp_servers\.(?:"([^"\n]+)"|\'([^\'\n]+)\'|([\w-]+))\][^\n]*\n(?:(?!\[).*(?:\n|$))*'
        def migrate(match):
            name = next(x for x in match.groups() if x is not None)
            block = match.group(0)
            if name == 'research_clarification' and '/research-agent-team/scripts/clarification_decider.py' in block:
                return ''
            if name == 'claude_reviewer' and '/mcp-servers/claude-reviewer/server.py' in block:
                return block.replace('/.venvs/clarification-decider/bin/python', '/.venvs/claude-reviewer/bin/python')
            return block
        updated = re.sub(pattern, migrate, text)
        if updated != text:
            toml_path.write_text(updated)
    # Preserve local settings/weights for recovery, outside active configuration.
    config = root / '.tools/clarification-decider/config.json'
    if config.exists():
        backup = config.with_name('config.retired.json')
        if not backup.exists():
            config.rename(backup)
    # Leave the old venv alone: another running session may still hold its interpreter.


if __name__ == '__main__':
    retire(Path(__file__).resolve().parents[1])
