import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_codex import build
from configure_codex import configure
spec = importlib.util.spec_from_file_location('reviewer', ROOT / '.agents/mcp-servers/claude-reviewer/server.py')
reviewer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reviewer)


class BridgeTests(unittest.TestCase):
    def setUp(self):
        reviewer.SESSIONS.clear()
        self.cfg = patch.object(reviewer, 'settings', return_value={'model': 'opus'})
        self.cfg.start()
        self.addCleanup(self.cfg.stop)

    def response(self, cmd, **kwargs):
        sid = cmd[-1]
        return subprocess.CompletedProcess(cmd, 0, json.dumps({
            'subtype': 'success', 'session_id': sid, 'result': 'Independent review',
            'modelUsage': {'claude-opus-test': {}}}), '')

    def test_session_continuity_and_restricted_tools(self):
        with patch.object(reviewer.subprocess, 'run', side_effect=self.response) as run:
            result = reviewer.review('Read paper $(touch /tmp/no)', str(ROOT), 'gpt-6')
            self.assertEqual(result['status'], 'ok')
            args, kw = run.call_args
            self.assertNotIn('shell', kw)
            self.assertEqual(kw['input'], 'Read paper $(touch /tmp/no)')
            self.assertIn('Read,Grep,Glob', args[0])
            self.assertIn('--strict-mcp-config', args[0])
            follow = reviewer.review_reply(result['threadId'], 'Read updated paper')
            self.assertEqual(follow['threadId'], result['threadId'])
            self.assertIn('--resume', run.call_args.args[0])
            self.assertEqual(run.call_count, 2)

    def test_bad_executor_and_foreign_thread_never_dispatch(self):
        with patch.object(reviewer.subprocess, 'run') as run:
            for model in ('unknown', 'claude-opus'):
                self.assertEqual(reviewer.review('Review', str(ROOT), model)['status'], 'REVIEW_UNAVAILABLE')
            self.assertEqual(reviewer.review_reply('foreign', 'Review')['status'], 'REVIEW_UNAVAILABLE')
            run.assert_not_called()

    def test_ambiguous_timeout_never_retries(self):
        with patch.object(reviewer.subprocess, 'run', side_effect=subprocess.TimeoutExpired('claude', 1)) as run:
            result = reviewer.review('Review', str(ROOT), 'gpt-6')
            self.assertEqual(result['status'], 'REVIEW_UNAVAILABLE')
            self.assertEqual(run.call_count, 1)
            self.assertFalse(reviewer.SESSIONS)

    def test_usage_limit_is_actionable_and_not_retried(self):
        response = subprocess.CompletedProcess([], 1, '{"api_error":"usage_limit_reached"}', '')
        with patch.object(reviewer.subprocess, 'run', return_value=response) as run:
            result = reviewer.review('Review', str(ROOT), 'gpt-6')
            self.assertEqual(result['status'], 'REVIEW_UNAVAILABLE')
            self.assertIn('usage limit', result['reason'])
            self.assertEqual(run.call_count, 1)

    def test_invalid_result_cannot_be_a_verdict(self):
        for response in ('bad JSON', '{}', '[]', '{"is_error":true}'):
            with self.subTest(response=response), patch.object(reviewer.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, response, '')):
                self.assertEqual(reviewer.review('Review', str(ROOT), 'gpt-6')['status'], 'REVIEW_UNAVAILABLE')
        with patch.object(reviewer.subprocess, 'run', side_effect=lambda cmd, **kw: subprocess.CompletedProcess(cmd, 0, json.dumps({'subtype':'success', 'session_id':cmd[-1], 'result':'PASS', 'modelUsage':{'gpt-6':{}}}), '')):
            self.assertEqual(reviewer.review('Review', str(ROOT), 'gpt-6')['status'], 'REVIEW_UNAVAILABLE')


class InstallTests(unittest.TestCase):
    def test_config_idempotent_and_preserves_user_settings(self):
        with tempfile.TemporaryDirectory(prefix='aris with spaces ') as temp:
            root = Path(temp)
            (root / '.codex').mkdir()
            path = root / '.codex/config.toml'
            custom = 'model = "custom"\n[mcp_servers."claude_reviewer"]\ncommand = "custom-review"\n'
            path.write_text(custom)
            configure(root)
            first = path.read_text()
            configure(root)
            self.assertEqual(path.read_text(), first)
            self.assertTrue(first.startswith(custom))
            self.assertNotIn('research_clarification', first)
            self.assertEqual(first.count('command = "custom-review"'), 1)

    def test_generated_view_preserves_sources_and_resource_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            src = root / '.claude/skills/demo'
            src.mkdir(parents=True)
            original = '---\nname: demo\ndescription: Test skill\ndisable-model-invocation: true\n---\nScientific rule.\n'
            (src / 'SKILL.md').write_text(original)
            (src / 'script.py').write_text('print("ok")\n')
            (root / 'config/codex').mkdir(parents=True)
            (root / 'config/codex/host.md').write_text('Host contract')
            build(root)
            build(root)
            self.assertEqual((src / 'SKILL.md').read_text(), original)
            skill = root / '.agents/skills/demo'
            self.assertIn('Scientific rule.', (skill / 'SKILL.md').read_text())
            self.assertEqual((skill / 'script.py').resolve(), src / 'script.py')
            self.assertIn('false', (skill / 'agents/openai.yaml').read_text())
            (root / '.claude/skills/new').mkdir()
            (root / '.claude/skills/new/file.md').write_text('new')
            (root / '.agents/skills/new').mkdir()
            (root / '.agents/skills/new/file.md').write_text('user-owned')
            with self.assertRaises(RuntimeError):
                build(root)
            self.assertEqual((root / '.agents/skills/new/file.md').read_text(), 'user-owned')


if __name__ == '__main__':
    unittest.main()
