"""Claude-host adapter tests: the codex-exec reviewer bridge and the /research-auto entrypoint."""
import importlib.util
import os
from pathlib import Path
import queue
import stat
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

FAKE_CODEX = r'''#!/usr/bin/env python3
import json, os, sys
sys.stdin.read()
with open(os.environ["FAKE_ARGV_LOG"], "a") as fh:
    fh.write(json.dumps(sys.argv[1:]) + "\n")
print(json.dumps({"type": "thread.started", "thread_id": "thread-1"}), flush=True)
print(json.dumps({"type": "item.completed", "item": {"type": "agent_message", "text": "Independent review"}}), flush=True)
print(json.dumps({"type": "turn.completed"}), flush=True)
'''


def load_bridge(tmp):
    os.environ['CODEX_EXEC_STATE_DIR'] = str(Path(tmp) / 'state')
    spec = importlib.util.spec_from_file_location(
        'codex_exec', ROOT / '.agents/mcp-servers/codex-exec/server.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CodexExecBridge(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        fake = Path(self.tmp.name) / 'codex'
        fake.write_text(FAKE_CODEX)
        fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
        self.log = Path(self.tmp.name) / 'argv.log'
        env = patch.dict(os.environ, {'FAKE_ARGV_LOG': str(self.log)})
        env.start()
        self.addCleanup(env.stop)
        self.bridge = load_bridge(self.tmp.name)
        self.bridge.CODEX_BIN = str(fake)
        quiet = patch.object(self.bridge, 'send_message')
        quiet.start()
        self.addCleanup(quiet.stop)

    def call(self, name, **args):
        request = {'id': 1, 'params': {'name': name, 'arguments': args}}
        return self.bridge.handle_call(request, queue.Queue(), [])

    def argv_calls(self):
        import json
        return [json.loads(x) for x in self.log.read_text().splitlines()]

    def test_reply_keeps_model_config_and_sandbox(self):
        first = self.call('codex', prompt='Review', model='gpt-test', sandbox='read-only',
                          config={'model_reasoning_effort': 'high'}, cwd=self.tmp.name)
        self.assertEqual(first['result']['structuredContent'],
                         {'threadId': 'thread-1', 'content': 'Independent review'})
        self.call('codex-reply', prompt='Follow up', threadId='thread-1')
        resumed = self.argv_calls()[1]
        self.assertEqual(resumed[:3], ['exec', 'resume', 'thread-1'])
        for flag in ('gpt-test', 'sandbox_mode="read-only"', 'model_reasoning_effort="high"'):
            self.assertIn(flag, resumed)

    def test_invalid_thread_id_rejected(self):
        reply = self.call('codex-reply', prompt='x', threadId='../../etc/passwd')
        self.assertEqual(reply['error']['message'], 'invalid threadId')


class ResearchAutoEntrypoint(unittest.TestCase):
    def test_command_exists_and_uses_main_agent_decisions(self):
        text = (ROOT / '.claude/commands/research-auto.md').read_text()
        self.assertIn('disable-model-invocation: true', text)
        self.assertIn('references/decision-cards.md', text)
        self.assertNotIn('choose_card', text)
        self.assertIn('AWAITING_TOPIC_APPROVAL', text)
        target = ROOT / '.claude/commands' / '../skills/research-agent-team/references/decision-cards.md'
        self.assertTrue(target.resolve().exists())


class ResearchAutopilotEntrypoint(unittest.TestCase):
    def test_command_exists_and_links_resolve(self):
        cmd_dir = ROOT / '.claude/commands'
        text = (cmd_dir / 'research-autopilot.md').read_text()
        self.assertIn('disable-model-invocation: true', text)
        for marker in ('AWAITING_TOPIC_APPROVAL', 'AWAITING_RESOURCE', 'research-auto.md',
                       'references/decision-cards.md', 'SKILL.md#post-topic-autopilot'):
            self.assertIn(marker, text)
        for rel in ('research-auto.md', '../skills/research-agent-team/SKILL.md',
                    '../skills/research-agent-team/references/decision-cards.md'):
            self.assertTrue((cmd_dir / rel).resolve().exists(), rel)
        skill = (ROOT / '.claude/skills/research-agent-team/SKILL.md').read_text()
        self.assertIn('## Post-topic autopilot', skill)


if __name__ == '__main__':
    unittest.main()
