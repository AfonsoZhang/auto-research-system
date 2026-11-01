#!/usr/bin/env python3
"""Add only missing ARIS MCP tables; preserve user configuration verbatim."""
import json
from pathlib import Path
import re


def configure(root):
    path = root / '.codex/config.toml'
    path.parent.mkdir(exist_ok=True)
    text = path.read_text() if path.exists() else ''
    servers = {
        'claude_reviewer': root / '.agents/mcp-servers/claude-reviewer/server.py',
    }
    for name, script in servers.items():
        # Leave existing tables (including quoted keys) entirely user-owned.
        if re.search(r'^\s*\[mcp_servers\.(?:' + name + '|"' + name + '"|\'' + name + '\')\]', text, re.M):
            print(f'Preserved existing MCP configuration: {name}')
            continue
        text += (f'\n[mcp_servers.{name}]\ncommand = '
                 + json.dumps(str(root / '.venvs/claude-reviewer/bin/python'))
                 + '\nargs = [' + json.dumps(str(script)) + ']\n'
                 + 'startup_timeout_sec = 30\ntool_timeout_sec = 660\n')
    path.write_text(text)
    print(f'Configured {path}')


if __name__ == '__main__':
    configure(Path(__file__).resolve().parents[1])
