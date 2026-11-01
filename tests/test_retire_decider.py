"""Migration preserves other MCP servers and keeps the reviewer usable."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from retire_decider import retire
from configure_codex import configure


class MigrationTests(unittest.TestCase):
    def test_retirement_preserves_other_servers_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '.codex').mkdir()
            old = root / '.tools/clarification-decider/config.json'
            old.parent.mkdir(parents=True)
            old.write_text('{"custom": true}')
            script = str(root / '.claude/skills/research-agent-team/scripts/clarification_decider.py')
            other = {'command': 'user-tool', 'args': ['custom']}
            config = root / '.mcp.json'
            config.write_text(json.dumps({'mcpServers': {
                'research_clarification': {'args': [script]}, 'other': other}}))
            toml = root / '.codex/config.toml'
            tail = '[mcp_servers.other]\ncommand = "user-tool"\n'
            toml.write_text('model = "user-model"\n[mcp_servers."research_clarification"]\n'
                            f'args = [{json.dumps(script)}]\n'
                            '[mcp_servers.claude_reviewer]\n'
                            f'command = "{root}/.venvs/clarification-decider/bin/python"\n'
                            f'args = ["{root}/.agents/mcp-servers/claude-reviewer/server.py"]\n' + tail)
            retire(root)
            configure(root)
            first = toml.read_text()
            self.assertNotIn('research_clarification', first)
            self.assertIn('/.venvs/claude-reviewer/bin/python', first)
            self.assertTrue(first.endswith(tail))
            self.assertEqual(json.loads(config.read_text())['mcpServers'], {'other': other})
            self.assertEqual(old.with_name('config.retired.json').read_text(), '{"custom": true}')
            self.assertFalse(old.exists())
            retire(root)
            configure(root)
            self.assertEqual(toml.read_text(), first)

    def test_custom_named_registration_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / '.mcp.json'
            original = '{"mcpServers":{"research_clarification":{"args":["user-custom.py"]}}}'
            config.write_text(original)
            retire(root)
            self.assertEqual(config.read_text(), original)


if __name__ == '__main__':
    unittest.main()
