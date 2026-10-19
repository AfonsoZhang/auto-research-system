import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / 'scripts' / 'check_retrieval.py'

REPORT = """# Survey

Tool retrieval degrades on multi-tool requests [1], [2]-[3].

## 11. References

[1] A. Author, B. Author, "Retrieval for Agents," ACL, 2025.
[2] C. Author, et al., "Tool Graphs: A Study," arXiv:2501.00001, 2025.
[3] D. Author, "Benchmarking Tool Use," NeurIPS, 2024.
"""


def run(report, records):
    with tempfile.TemporaryDirectory() as tmp:
        r, l = Path(tmp) / 'r.md', Path(tmp) / 'log.jsonl'
        r.write_text(report, encoding='utf-8')
        l.write_text('\n'.join(json.dumps(x) for x in records), encoding='utf-8')
        p = subprocess.run([sys.executable, str(SCRIPT), '--report', str(r), '--log', str(l)],
                           capture_output=True, text=True)
        return p.returncode, p.stdout


GOOD = [{'title': 'Retrieval for agents', 'grade': 'VERIFIED'},
        {'title': 'Tool Graphs: a study', 'grade': 'MINOR'},
        {'title': 'Benchmarking Tool Use', 'grade': 'PAYWALL'}]


class CheckRetrieval(unittest.TestCase):
    def test_all_retrieved(self):
        code, out = run(REPORT, GOOD)
        self.assertEqual(code, 0, out)

    def test_reference_not_retrieved(self):
        code, out = run(REPORT, GOOD[:2])
        self.assertEqual(code, 1)
        self.assertIn('[3] not in the retrieval log', out)

    def test_unusable_grade(self):
        code, out = run(REPORT, GOOD[:2] + [{'title': 'Benchmarking Tool Use', 'grade': 'UNVERIFIABLE'}])
        self.assertEqual(code, 1)
        self.assertIn('not usable', out)

    def test_citation_without_reference(self):
        code, out = run(REPORT.replace('[1], [2]-[3]', '[1], [2]-[4]'), GOOD)
        self.assertEqual(code, 1)
        self.assertIn('[4] cited in the text but missing', out)

    def test_uncited_reference_is_warning(self):
        code, out = run(REPORT.replace('[1], [2]-[3]', '[1], [2]'), GOOD)
        self.assertEqual(code, 0, out)
        self.assertIn('WARN  [3]', out)


if __name__ == '__main__':
    unittest.main()
