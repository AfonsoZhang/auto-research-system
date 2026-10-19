"""Regression test for scripts/integrity: the clean fixture yields no finding and each
injected defect (from Anti-Autoresearch's eval set) yields exactly its pattern."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIX = HERE / 'integrity_fixtures'
PRECHECK = HERE.parent / 'scripts' / 'integrity' / 'precheck.py'
sys.path.insert(0, str(FIX))
import corrupt  # noqa: E402


def patterns(tex_text, tmp, name):
    tex = Path(tmp) / f'{name}.tex'
    tex.write_text(tex_text, encoding='utf-8')
    out = Path(tmp) / name
    subprocess.run([sys.executable, str(PRECHECK), '--latex', str(tex), '--out-dir', str(out)],
                   check=True, capture_output=True, text=True)
    found = []
    for f in out.glob('*.findings.json'):
        found += [x['pattern_id'] for x in json.loads(f.read_text(encoding='utf-8'))]
    return sorted(found)


class IntegrityPrecheck(unittest.TestCase):
    def test_fixtures(self):
        clean = (FIX / 'clean.tex').read_text(encoding='utf-8')
        cases = [('clean', clean)] + [(n, corrupt.apply_corruption(clean, n))
                                      for n in sorted(corrupt.CORRUPTIONS)]
        with tempfile.TemporaryDirectory() as tmp:
            for name, text in cases:
                expected = json.loads((FIX / 'expected' / f'{name}.json').read_text())
                with self.subTest(name):
                    self.assertEqual(patterns(text, tmp, name),
                                     sorted(expected.get('required_patterns', [])))

    def test_leading_dot_decimals(self):
        rows = '\\\\\n'.join(f'M{i} & .{600 + i} & .{500 + i}' for i in range(3))
        table = ('\\begin{table}\n\\begin{tabular}{lrr}\n' + rows + '\\\\\n'
                 '\\end{tabular}\n\\end{table}\n')
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(patterns(table + '\n' + table, tmp, 'dup'), ['HP-DUP-TABLE'])


if __name__ == '__main__':
    unittest.main()
