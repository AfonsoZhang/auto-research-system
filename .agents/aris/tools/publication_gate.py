#!/usr/bin/env python3
"""Offline consistency check for publication records; NOT external fact verification."""
import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


def url_ok(value):
    return isinstance(value, str) and urlparse(value).scheme in {"http", "https"} and bool(urlparse(value).netloc)


def identity(value):
    value = value.strip().lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    value = re.sub(r"^doi:", "", value)
    value = re.sub(r"^https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/", "arxiv:", value)
    if value.startswith("10.48550/arxiv."):
        value = "arxiv:" + value[len("10.48550/arxiv."):]
    if value.startswith("arxiv:"):
        value = re.sub(r"(?:v\d+)?(?:\.pdf)?$", "", value)
    return value


def validate(records, claims=None):
    issues, counts, by_id, seen = [], Counter(), {}, {}

    def fail(pid, rule):
        issues.append({"paper_id": pid, "rule": rule})

    if not isinstance(records, dict) or records.get("schema_version") != 1 or not isinstance(records.get("papers"), list):
        return {"ok": False, "issues": [{"rule": "invalid_record_schema"}]}
    enums = {
        "existence_status": {"verified", "unverified", "verify_pending", "error"},
        "publication_status": {"published", "accepted", "preprint", "unknown"},
        "peer_review_status": {"confirmed", "not_peer_reviewed", "unknown"},
        "selected_version": {"publishedVersion", "acceptedVersion", "submittedVersion", "unknown"},
        "tier": {"core", "supplement", "pending", "excluded"},
    }
    official = {"publisher", "proceedings", "official_acceptance", "official_review"}
    for p in records["papers"]:
        if not isinstance(p, dict):
            fail(None, "invalid_paper_record")
            continue
        pid = p.get("id")
        if not isinstance(pid, str) or not pid.strip():
            fail(None, "missing_paper_id")
            continue
        if pid in by_id:
            fail(pid, "duplicate_paper_id")
        by_id[pid] = p
        if not isinstance(p.get("title"), str) or not p["title"].strip():
            fail(pid, "missing_title")
        valid_enums = True
        for field, allowed in enums.items():
            if not isinstance(p.get(field), str) or p[field] not in allowed:
                fail(pid, "invalid_" + field)
                valid_enums = False
        if not valid_enums:
            continue
        tier = p.get("tier")
        if isinstance(tier, str):
            counts[tier] += 1
        aliases = p.get("aliases", [])
        if not isinstance(aliases, list):
            fail(pid, "invalid_aliases")
            aliases = []
        identifiers = [p.get("doi")] + aliases
        if p.get("arxiv_id"):
            arxiv = str(p["arxiv_id"])
            identifiers.append(arxiv if ":" in arxiv else "arxiv:" + arxiv)
        for raw in identifiers:
            if raw is None:
                continue
            if not isinstance(raw, str) or not raw.strip():
                fail(pid, "invalid_identifier")
                continue
            key = identity(raw)
            if key in seen and seen[key] != pid:
                fail(pid, "duplicate_work_identifier:" + seen[key])
            seen[key] = pid
        supported = set()
        evidence = p.get("evidence", [])
        if not isinstance(evidence, list):
            fail(pid, "invalid_evidence")
            evidence = []
        for e in evidence:
            if not isinstance(e, dict):
                fail(pid, "invalid_evidence_entry")
                continue
            supports = e.get("supports")
            valid_supports = isinstance(supports, list) and all(isinstance(s, str) and s in {"publication", "peer_review", "version_link"} for s in supports)
            try:
                checked = date.fromisoformat(e.get("checked_at", ""))
                valid_date = checked <= date.today()
            except (ValueError, TypeError):
                valid_date = False
            kind = e.get("kind")
            if not (url_ok(e.get("url")) and valid_supports and valid_date and isinstance(e.get("note"), str) and e["note"].strip() and isinstance(kind, str) and kind in official | {"index"}):
                fail(pid, "incomplete_evidence_entry")
                continue
            if kind in official:
                supported.update(supports)
        if p.get("publication_status") in {"published", "accepted"} and "publication" not in supported:
            fail(pid, "publication_without_official_evidence")
        if p.get("peer_review_status") == "confirmed" and "peer_review" not in supported:
            fail(pid, "peer_review_without_official_evidence")
        if tier in {"core", "supplement"} and p.get("existence_status") != "verified":
            fail(pid, "unverified_work_selected")
        if tier in {"core", "supplement"} and not url_ok(p.get("selected_source_url")):
            fail(pid, "selected_source_missing")
        if tier == "core":
            if p.get("publication_status") not in {"published", "accepted"} or p.get("peer_review_status") != "confirmed" or p.get("selected_version") not in {"publishedVersion", "acceptedVersion"}:
                fail(pid, "ineligible_core_record")
            if not p.get("venue"):
                fail(pid, "core_missing_venue")
        if tier in {"supplement", "excluded"} and not p.get("selection_reason"):
            fail(pid, "missing_selection_reason")
    if claims is not None:
        if not isinstance(claims, dict):
            fail(None, "invalid_claims_map")
        else:
            for bibkey, claim in claims.items():
                if not isinstance(claim, dict) or not isinstance(claim.get("paper_id"), str):
                    fail(bibkey, "claim_missing_paper_id")
                    continue
                p = by_id.get(claim["paper_id"])
                if p is None or p.get("tier") not in ("core", "supplement"):
                    fail(bibkey, "claim_paper_not_selected")
                    continue
                read = p.get("read_source")
                if not isinstance(read, dict) or not url_ok(read.get("url")) or read.get("url") != p.get("selected_source_url") or read.get("version") != p.get("selected_version") or read.get("version") == "unknown":
                    fail(bibkey, "selected_version_not_read")
                    continue
                if claim.get("read_version") != read["version"] or claim.get("evidence_url") != read["url"]:
                    fail(bibkey, "claim_version_or_source_mismatch")
                if not isinstance(claim.get("evidence_locator"), str) or not claim["evidence_locator"].strip():
                    fail(bibkey, "claim_missing_evidence_locator")
    return {"ok": not issues, "counts": dict(counts), "issues": issues,
            "warnings": (["no_core_papers"] if not counts["core"] else []) + (["pending_records_retained"] if counts["pending"] else []),
            "scope": "record_consistency_only_not_external_verification"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", type=Path)
    parser.add_argument("--claims-map", type=Path)
    args = parser.parse_args()
    try:
        records = json.loads(args.records.read_text())
        claims = json.loads(args.claims_map.read_text()) if args.claims_map else None
        report = validate(records, claims)
    except (OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
