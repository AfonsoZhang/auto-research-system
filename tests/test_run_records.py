import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / '.claude/skills/experiment-bridge/scripts/check_run_records.py'
spec = importlib.util.spec_from_file_location('run_records', SCRIPT)
records = importlib.util.module_from_spec(spec)
spec.loader.exec_module(records)


class RunRecordTests(unittest.TestCase):
    def test_failed_attempt_and_valid_zero_are_preserved(self):
        observed = [
            {'run_id': 'a', 'attempt_id': '1', 'status': 'failed', 'reason': 'OOM'},
            {'run_id': 'a', 'attempt_id': '2', 'status': 'completed', 'score': 0},
        ]
        report = records.check([{'run_id': 'a'}], observed, ['score'])
        self.assertTrue(report['passed'])
        self.assertEqual(report['observed_runs'], 1)
        self.assertEqual(report['observed_attempts'], 2)
        self.assertEqual(report['attempt_status_counts'], {'failed': 1, 'completed': 1})

    def test_missing_plan_rows_and_duplicate_attempts_are_detected(self):
        report = records.check([{'run_id': 'a'}, {'run_id': 'b'}], [
            {'run_id': 'a', 'status': 'completed'},
            {'run_id': 'a', 'status': 'completed'},
        ])
        self.assertFalse(report['passed'])
        self.assertEqual(report['missing_run_ids'], ['b'])
        self.assertTrue(any('Duplicate run/attempt' in x for x in report['errors']))

    def test_invalid_metrics_and_unexplained_failures(self):
        for value in ('NaN', 'Infinity', '-inf', None, True, 'not measured'):
            with self.subTest(value=value):
                report = records.check([{'run_id': 'a'}], [
                    {'run_id': 'a', 'status': 'completed', 'score': value},
                ], ['score'])
                self.assertFalse(report['passed'])
        self.assertFalse(records.check([{'run_id': 'a'}], [
            {'run_id': 'a', 'status': 'failed'},
        ])['passed'])

    def test_empty_duplicate_and_unplanned_records(self):
        self.assertFalse(records.check([], [])['passed'])
        self.assertFalse(records.check([{'run_id': 'a'}] * 2, [])['passed'])
        self.assertFalse(records.check([{'run_id': 'a'}], [
            {'run_id': 'b', 'status': 'running'},
        ])['passed'])
        self.assertFalse(records.check([{'run_id': []}], [])['passed'])

    def test_cli_csv_jsonl_and_read_only_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            planned = Path(temp) / 'planned.csv'
            observed = Path(temp) / 'observed.jsonl'
            planned.write_text('run_id\na\nb\n')
            observed.write_text(json.dumps({'run_id': 'a', 'status': 'completed', 'score': 0}) + '\n')
            before = {p: p.read_bytes() for p in (planned, observed)}
            result = subprocess.run([
                sys.executable, str(SCRIPT), '--planned', str(planned),
                '--observed', str(observed), '--metric', 'score',
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)['missing_run_ids'], ['b'])
            self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_json_array_and_malformed_cli_input(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'records.json'
            path.write_text('[{"run_id":"a","status":"pending"}]')
            self.assertEqual(records.load_rows(path)[0]['status'], 'pending')
            path.write_text('{}')
            result = subprocess.run([
                sys.executable, str(SCRIPT), '--planned', str(path), '--observed', str(path),
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertFalse(json.loads(result.stdout)['passed'])
            self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
