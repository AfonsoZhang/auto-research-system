#!/usr/bin/env python3
"""Check a deep-research report's references against its retrieval log.

Every entry in the report's References section must match (by normalized title)
a work recorded in the retrieval log with a usable verification grade, every
in-text citation [n] must have a reference entry, and every reference should be
cited. Standard library only.

Log format, one JSON object per line (retrieval_log.jsonl):
  {"title": "...", "grade": "VERIFIED", "round": 1, "source": "semantic-scholar",
   "id": "doi:... | arXiv:... | url"}
grade is one of VERIFIED, MINOR, MAJOR, UNVERIFIABLE, PAYWALL
(references/citation-protocol.md); MAJOR and UNVERIFIABLE are not usable.

Usage: check_retrieval.py --report survey.md --log retrieval_log.jsonl
Exit 0 when no errors; 1 otherwise. Uncited references are warnings.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

USABLE = {'VERIFIED', 'MINOR', 'PAYWALL'}
GRADES = USABLE | {'MAJOR', 'UNVERIFIABLE'}
REF_LINE = re.compile(r'^\s*\[(\d+)\]\s+(.*)$')
TITLE = re.compile(r'["“]([^"”]+?)[,.]?["”]')
CITE = re.compile(r'\[(\d+(?:\s*[,–-]\s*\d+)*)\]')


def norm(title):
    t = unicodedata.normalize('NFKC', title).lower()
    return re.sub(r'[^0-9a-z一-鿿]+', '', t)


def split_report(text):
    m = re.search(r'^#{1,3}\s*(?:\d+\.\s*)?(References|参考文献)\s*$', text, re.M)
    if not m:
        raise SystemExit('no "References" heading found in the report')
    return text[:m.start()], text[m.end():]


def cited_numbers(body):
    nums = set()
    for m in CITE.finditer(body):
        for part in re.split(r'\s*,\s*', m.group(1)):
            bounds = re.split(r'\s*[–-]\s*', part)
            if len(bounds) == 2:
                lo, hi = int(bounds[0]), int(bounds[1])
                nums.update(range(lo, hi + 1) if 0 < hi - lo < 200 else (lo, hi))
            else:
                nums.add(int(bounds[0]))
    return nums


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--report', required=True, type=Path)
    ap.add_argument('--log', required=True, type=Path)
    args = ap.parse_args(argv)

    log = {}
    for i, line in enumerate(args.log.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        rec = json.loads(line)
        grade = str(rec.get('grade', '')).upper()
        if grade not in GRADES or not rec.get('title'):
            raise SystemExit(f'{args.log}:{i}: needs "title" and a grade in {sorted(GRADES)}')
        key = norm(rec['title'])
        # keep the best grade if a work was logged more than once
        if key not in log or (grade in USABLE and log[key]['grade'] not in USABLE):
            log[key] = {**rec, 'grade': grade}

    body, refs = split_report(args.report.read_text(encoding='utf-8'))
    errors, warnings, entries = [], [], {}
    for line in refs.splitlines():
        m = REF_LINE.match(line)
        if not m:
            continue
        n, rest = int(m.group(1)), m.group(2)
        t = TITLE.search(rest)
        if not t:
            errors.append(f'[{n}] no quoted title to match: {rest[:80]}')
            continue
        entries[n] = t.group(1)
        rec = log.get(norm(t.group(1)))
        if rec is None:
            errors.append(f'[{n}] not in the retrieval log: "{t.group(1)}"')
        elif rec['grade'] not in USABLE:
            errors.append(f'[{n}] logged as {rec["grade"]}, not usable: "{t.group(1)}"')

    cited = cited_numbers(body)
    for n in sorted(cited - entries.keys()):
        errors.append(f'[{n}] cited in the text but missing from References')
    for n in sorted(entries.keys() - cited):
        warnings.append(f'[{n}] listed in References but never cited')

    for e in errors:
        print('ERROR', e)
    for w in warnings:
        print('WARN ', w)
    print(f'{len(entries)} references, {len(cited)} cited numbers, '
          f'{len(log)} logged works: {len(errors)} error(s), {len(warnings)} warning(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
