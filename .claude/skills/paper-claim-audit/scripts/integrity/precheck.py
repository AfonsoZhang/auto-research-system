#!/usr/bin/env python3
"""Deterministic integrity pre-check for paper-claim-audit.

Runs four arithmetic and surface checks adapted from Anti-Autoresearch (MIT, see
LICENSE-anti-autoresearch) on the paper's LaTeX source:

  HP-DELTA-ERROR, HP-NUM-INFLATE             check_numeric_consistency.py
  HP-GRANULARITY-IMPOSSIBLE (GRIM),
  HP-VARIANCE-IMPOSSIBLE, HP-STAT-INCONSISTENCY  check_stat_consistency.py
  HP-DUP-TABLE, HP-PIPELINE-ARTIFACT         check_presentation.py

Every finding is something for the author to verify, not a verdict. Standard
library only; t/F/chi2/r p-value checks additionally need scipy (z-tests always run).

Usage: precheck.py --latex main.tex [sections/*.tex] --out-dir DIR
Writes DIR/claims.json, DIR/<check>.findings.json and DIR/INTEGRITY_PRECHECK.md.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKS = ('check_numeric_consistency', 'check_stat_consistency', 'check_presentation')


def run(script, *args):
    r = subprocess.run([sys.executable, str(HERE / f'{script}.py'), *map(str, args)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f'{script} failed:\n{r.stdout}{r.stderr}')
    return r.stdout.strip()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--latex', nargs='+', required=True)
    ap.add_argument('--out-dir', required=True, type=Path)
    args = ap.parse_args(argv)
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    ledger = out / 'claims.json'
    log = [run('build_claim_ledger', '--paper-id', 'paper', '--latex', *args.latex, '--out', ledger)]
    findings = []
    for check in CHECKS:
        path = out / f'{check}.findings.json'
        log.append(run(check, '--ledger', ledger, '--out', path))
        findings += json.loads(path.read_text(encoding='utf-8'))

    lines = ['# Integrity pre-check', '', *[f'- {l}' for l in log], '']
    if not findings:
        lines.append('No deterministic findings. This does not establish that the paper is correct.')
    for f in findings:
        ev = f['evidence'][0]
        loc = ev.get('location', {})
        lines += [f"## {f['pattern_id']} ({f['severity']}, false-positive risk {f['false_positive_risk']})",
                  f"{loc.get('file')}:{loc.get('line')} [{loc.get('section')}]", '',
                  f['description'], '', f"> {ev.get('span', '')[:300]}", '']
    (out / 'INTEGRITY_PRECHECK.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{len(findings)} finding(s) -> {out / "INTEGRITY_PRECHECK.md"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
