#!/usr/bin/env python3
"""Read-only checks of a planned run list against observed experiment records."""
import argparse
from collections import Counter
import csv
import json
import math
from pathlib import Path


def load_rows(path):
    path = Path(path)
    with path.open(encoding='utf-8-sig', newline='') as stream:
        if path.suffix.lower() == '.csv':
            rows = list(csv.DictReader(stream))
        elif path.suffix.lower() == '.jsonl':
            rows = [json.loads(line) for line in stream if line.strip()]
        else:
            rows = json.load(stream)
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise ValueError(f'{path}: expected an array of records')
    return rows


def check(planned, observed, metrics=()):
    """Compare run/attempt identities without selecting or aggregating attempts."""
    errors = []
    plan_ids = []
    for index, row in enumerate(planned, 1):
        run_id = row.get('run_id')
        if not isinstance(run_id, str) or not run_id.strip():
            errors.append(f'Plan row {index}: missing string run_id')
        else:
            plan_ids.append(run_id)
    for run_id, count in Counter(plan_ids).items():
        if count > 1:
            errors.append(f'Duplicate planned run_id: {run_id}')
    if not planned:
        errors.append('Expected run list is empty; coverage cannot be established')

    expected = set(plan_ids)
    seen = set()
    identities = set()
    statuses = Counter()
    reasons_required = {'failed', 'cancelled', 'excluded', 'skipped'}
    allowed = reasons_required | {'planned', 'pending', 'running', 'completed'}
    for index, row in enumerate(observed, 1):
        run_id = row.get('run_id')
        attempt = row.get('attempt_id') or ''
        label = f'Result row {index}'
        if not isinstance(run_id, str) or not run_id.strip():
            errors.append(f'{label}: missing string run_id')
            continue
        if not isinstance(attempt, str):
            errors.append(f'{label}: attempt_id must be a string')
            continue
        identity = (run_id, attempt)
        if identity in identities:
            errors.append(f'Duplicate run/attempt: {run_id}/{attempt or "<unspecified>"}')
        identities.add(identity)
        seen.add(run_id)
        if run_id not in expected:
            errors.append(f'{label}: unplanned run_id {run_id}')
        status = row.get('status')
        if not isinstance(status, str) or status not in allowed:
            errors.append(f'{label}: unknown status {status!r}')
            continue
        statuses[status] += 1
        if status in reasons_required and not str(row.get('reason') or '').strip():
            errors.append(f'{label}: {status} requires a reason')
        for metric in metrics:
            value = row.get(metric)
            if value is None or value == '':
                if status == 'completed':
                    errors.append(f'{label}: completed run lacks metric {metric}')
                continue
            try:
                valid = not isinstance(value, bool) and math.isfinite(float(value))
            except (ValueError, TypeError, OverflowError):
                valid = False
            if not valid:
                errors.append(f'{label}: metric {metric} is not a finite number')
    missing = sorted(expected - seen)
    errors.extend(f'Missing planned run: {run_id}' for run_id in missing)
    return {
        'passed': not errors,
        'expected_runs': len(expected),
        'observed_runs': len(seen),
        'observed_attempts': len(observed),
        'attempt_status_counts': dict(statuses),
        'missing_run_ids': missing,
        'errors': errors,
        'scope': 'Record consistency only; does not verify execution, artifacts or scientific validity.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--planned', required=True, help='CSV, JSON array or JSONL with run_id')
    parser.add_argument('--observed', required=True, help='Records with run_id, status and optional attempt_id')
    parser.add_argument('--metric', action='append', default=[], help='Numeric metric column; repeat as needed')
    args = parser.parse_args()
    try:
        report = check(load_rows(args.planned), load_rows(args.observed), args.metric)
    except (OSError, ValueError, csv.Error) as error:
        report = {'passed': False, 'errors': [str(error)]}
    print(json.dumps(report, indent=2, allow_nan=False))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
