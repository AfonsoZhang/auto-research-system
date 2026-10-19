#!/usr/bin/env python3
"""Resolve a venue name/acronym to DBLP venue records (and optionally count
papers in one year's proceedings as a venue-size signal).

DBLP is the canonical, CC0, key-free registry of CS venues — the right place
to resolve "what is this venue's identity" when it has no profile under
venues/conferences/ yet. The returned `key` (e.g. conf/gis) is what the
venue-profile schema stores as `aliases.dblp_key`.

Subcommands:
  search <query>            venue search, e.g.  search "SIGSPATIAL"
  toc-count <key> <year>    count papers in one year's table of contents,
                            e.g.  toc-count conf/gis 2025
                            (single toc fetch — a polite venue-size proxy)

Politeness (required by this repo's rules):
  * <=1 request/second per host, exponential backoff on HTTP 429
  * User-Agent "research-paper-skills (mailto:$CONTACT_EMAIL)" — set the
    CONTACT_EMAIL env var (prompted for interactively if unset)
  * responses cached under .cache/ at the repo root (gitignored)
  * fetches single items only, never bulk crawls

Examples:
  CONTACT_EMAIL=you@example.org python3 scripts/dblp_venue_lookup.py search "SIGSPATIAL"
  python3 scripts/dblp_venue_lookup.py toc-count conf/gis 2025
  python3 scripts/dblp_venue_lookup.py toc-count conf/nips 2024 --bht db/conf/nips/neurips2024.bht
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Local adaptation 2026-10-01: official SPARQL fallback and exact TOC resolution.
SPARQL_URL = "https://sparql.dblp.org/sparql"


class DblpError(RuntimeError):
    """A remote failure, never an empty search result."""


DBLP_BASE = "https://dblp.org/search"
USER_AGENT_TMPL = "research-paper-skills (mailto:%s)"
MIN_INTERVAL_S = 1.0          # <=1 req/s per host
MAX_RETRIES = 4               # backoff: 2s, 4s, 8s, 16s on HTTP 429
CACHE_TTL_S = 24 * 3600       # search results: 1 day
CACHE_TTL_TOC_S = 7 * 24 * 3600  # historical tocs barely change: 7 days

_last_request_at = {}


def get_contact_email():
    email = next((os.environ.get(k, "").strip() for k in
                  ("CONTACT_EMAIL", "ARIS_VERIFY_EMAIL", "OPENALEX_EMAIL")
                  if os.environ.get(k, "").strip()), "")
    if email:
        return email
    if sys.stdin.isatty():
        try:
            email = input(
                "CONTACT_EMAIL is not set. Enter a contact email to identify "
                "polite API traffic (stored nowhere, sent in User-Agent): "
            ).strip()
        except EOFError:
            email = ""
        if email:
            return email
    sys.exit(
        "error: CONTACT_EMAIL is not set. Set it so API operators can contact "
        "you instead of blocking you, e.g.\n"
        "  CONTACT_EMAIL=you@example.org python3 scripts/dblp_venue_lookup.py ..."
    )


def find_cache_dir():
    if os.environ.get("DBLP_CACHE_DIR"):
        d = Path(os.environ["DBLP_CACHE_DIR"]).expanduser()
        d.mkdir(parents=True, exist_ok=True)
        return d
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for anc in [start] + list(start.parents):
            if (anc / "venues").is_dir() or (anc / ".git").is_dir():
                d = anc / ".cache" / "select-venue"
                d.mkdir(parents=True, exist_ok=True)
                return d
    d = Path.cwd() / ".cache" / "select-venue"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _rate_limit(host):
    last = _last_request_at.get(host)
    if last is not None:
        wait = MIN_INTERVAL_S - (time.monotonic() - last)
        if wait > 0:
            time.sleep(wait)
    _last_request_at[host] = time.monotonic()


def valid_body(body, sparql):
    if not isinstance(body, dict):
        return False
    if sparql:
        return isinstance(body.get("results"), dict) and isinstance(body["results"].get("bindings"), list)
    hits = (body.get("result") or {}).get("hits")
    return isinstance(hits, dict) and "@total" in hits


def fetch_json(url, email, ttl, refresh=False):
    sparql = url.startswith(SPARQL_URL + "?")
    cache_dir = find_cache_dir()
    cache_file = cache_dir / (hashlib.sha256(url.encode()).hexdigest() + ".json")
    if not refresh and cache_file.exists():
        try:
            entry = json.loads(cache_file.read_text(encoding="utf-8"))
            if (time.time() - entry["fetched_at"] < ttl
                    and valid_body(entry.get("body"), sparql)):
                return entry["body"], True
        except (ValueError, KeyError, TypeError, AttributeError):
            pass  # corrupt cache entry — refetch

    host = urllib.parse.urlparse(url).netloc
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT_TMPL % email,
        "Accept": "application/sparql-results+json" if sparql else "application/json"})
    delay = 2.0
    for attempt in range(MAX_RETRIES + 1):
        _rate_limit(host)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                if "text/html" in resp.headers.get("Content-Type", "").lower() or raw.lstrip().startswith("<"):
                    raise DblpError("HTML response from %s (possible bot challenge)" % host)
                body = json.loads(raw)
                if not valid_body(body, sparql):
                    raise DblpError("unexpected JSON schema from %s" % host)
            cache_file.write_text(
                json.dumps({"fetched_at": time.time(), "url": url, "body": body}),
                encoding="utf-8",
            )
            return body, False
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < MAX_RETRIES:
                print("HTTP 429 from %s — backing off %.0fs (attempt %d/%d)"
                      % (host, delay, attempt + 1, MAX_RETRIES), file=sys.stderr)
                time.sleep(delay)
                delay *= 2
                continue
            raise DblpError("HTTP %s from %s — %s" % (e.code, host, e.reason)) from e
        except urllib.error.URLError as e:
            raise DblpError("could not reach %s — %s" % (host, e.reason)) from e
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            raise DblpError("non-JSON response from %s" % host) from e
        except TimeoutError as e:
            raise DblpError("timeout from %s" % host) from e
    raise DblpError("still rate-limited by %s after %d retries" % (host, MAX_RETRIES))


def sparql_query(query, email, ttl, refresh):
    url = SPARQL_URL + "?" + urllib.parse.urlencode({"query": query})
    body, cached = fetch_json(url, email, ttl, refresh)
    return body["results"]["bindings"], cached


def value(row, key, default=""):
    return row.get(key, {}).get("value", default)


def choose_backend(args, rest, sparql):
    if args.backend == "sparql":
        return sparql()
    try:
        return rest()
    except DblpError as e:
        if args.backend == "rest":
            raise
        print("DBLP search API unavailable: %s; using official SPARQL." % e, file=sys.stderr)
        return sparql()


def cmd_search(args, email):
    def rest():
        url = DBLP_BASE + "/venue/api?" + urllib.parse.urlencode(
            {"q": args.query, "format": "json", "h": args.max})
        body, cached = fetch_json(url, email, CACHE_TTL_S, args.refresh)
        results = []
        for hit in body["result"]["hits"].get("hit", []) or []:
            info = hit.get("info", {})
            match = re.search(r"/db/((?:conf|journals|series)/[^/]+)", info.get("url", ""))
            results.append({"venue": info.get("venue"), "acronym": info.get("acronym"),
                            "type": info.get("type"), "dblp_key": match.group(1) if match else None,
                            "url": info.get("url")})
        return {"query": args.query, "from_cache": cached, "backend": "rest", "results": results}

    def sparql():
        terms = args.query.lower().split()
        if not terms:
            raise DblpError("search query must not be empty")
        filters = " && ".join("CONTAINS(LCASE(STR(?match)), %s)" % json.dumps(t) for t in terms)
        query = '''PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT DISTINCT ?stream ?title ?page WHERE {
 ?stream dblp:primaryStreamTitle ?title ; ?predicate ?match .
 VALUES ?predicate { dblp:primaryStreamTitle dblp:streamTitle dblp:acronym dblp:iso4 }
 FILTER(%s)
 OPTIONAL { ?stream dblp:indexPage ?page }
} ORDER BY ?title LIMIT %d''' % (filters, args.max)
        rows, cached = sparql_query(query, email, CACHE_TTL_S, args.refresh)
        results = []
        for row in rows:
            stream = value(row, "stream")
            key = stream.removeprefix("https://dblp.org/streams/")
            if key == stream:
                continue
            results.append({"venue": value(row, "title"), "acronym": None,
                            "type": key.split("/")[0], "dblp_key": key,
                            "url": value(row, "page") or "https://dblp.org/db/" + key + "/index"})
        return {"query": args.query, "from_cache": cached, "backend": "sparql",
                "endpoint": SPARQL_URL, "search_mode": "all terms as substrings of a venue title or alias",
                "results": results}

    out = choose_backend(args, rest, sparql)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print("DBLP venue search %r: %d hit(s), %s%s" %
              (args.query, len(out["results"]), out["backend"], " [cached]" if out["from_cache"] else ""))
        for row in out["results"]:
            print("  %s  %s\n  %s" % (row["dblp_key"], row["venue"], row["url"]))
    return 0


def cmd_toc_count(args, email):
    if not re.fullmatch(r"(?:conf|journals|series)/[A-Za-z0-9_-]+", args.key):
        raise DblpError("invalid DBLP venue key; use a key returned by search")
    bht = args.bht or "db/%s/%s%d.bht" % (args.key, args.key.split("/")[-1], args.year)
    if not re.fullmatch(r"db/(?:conf|journals|series)/[A-Za-z0-9_./-]+\.bht", bht) or ".." in bht:
        raise DblpError("invalid TOC path")

    def rest():
        url = DBLP_BASE + "/publ/api?" + urllib.parse.urlencode(
            {"q": "toc:%s:" % bht, "format": "json", "h": 1})
        body, cached = fetch_json(url, email, CACHE_TTL_TOC_S, args.refresh)
        total = int(body["result"]["hits"]["@total"])
        if total == 0 and not args.bht and args.backend == "auto":
            raise DblpError("inferred TOC filename returned zero; resolving the actual TOC")
        return {"dblp_key": args.key, "year": args.year, "bht": bht, "paper_count": total,
                "from_cache": cached, "backend": "rest", "count_scope": "distinct DBLP records on this TOC"}

    def sparql():
        cached_resolution = True
        if args.bht:
            toc = "https://dblp.org/" + bht[:-4]
        else:
            query = '''PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT DISTINCT ?toc WHERE {
 ?paper dblp:publishedInStream <https://dblp.org/streams/%s> ;
        dblp:yearOfPublication ?year ; dblp:listedOnTocPage ?toc .
 FILTER(STR(?year) = %s)
} ORDER BY ?toc LIMIT 21''' % (args.key, json.dumps(str(args.year)))
            rows, cached_resolution = sparql_query(query, email, CACHE_TTL_TOC_S, args.refresh)
            pages = [value(r, "toc") for r in rows]
            if not pages:
                raise DblpError("no TOC found for this venue/year; verify key and indexing (not a zero paper count)")
            if len(pages) != 1:
                raise DblpError("multiple TOCs found; choose one with --bht: " + ", ".join(pages))
            toc = pages[0]
        query = '''PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT (COUNT(DISTINCT ?paper) AS ?count) WHERE {
 ?paper dblp:listedOnTocPage ?toc . FILTER(STR(?toc) = %s)
}''' % json.dumps(toc)
        rows, cached = sparql_query(query, email, CACHE_TTL_TOC_S, args.refresh)
        if len(rows) != 1 or not value(rows[0], "count").isdigit():
            raise DblpError("invalid count response from SPARQL")
        count = int(value(rows[0], "count"))
        if count == 0:
            raise DblpError("no records on this TOC; verify the path and indexing")
        return {"dblp_key": args.key, "year": args.year,
                "bht": toc.removeprefix("https://dblp.org/") + ".bht", "toc_url": toc,
                "paper_count": count, "from_cache": cached and cached_resolution,
                "backend": "sparql", "endpoint": SPARQL_URL,
                "count_scope": "distinct DBLP records on this TOC; not full-paper acceptances"}

    out = choose_backend(args, rest, sparql)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print("%s %d: %d DBLP TOC records (%s; %s)%s" %
              (args.key, args.year, out["paper_count"], out["bht"], out["backend"],
               " [cached]" if out["from_cache"] else ""))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Polite DBLP venue lookup (stdlib only, cached, rate-limited).",
        epilog="DBLP metadata is CC0. Requires CONTACT_EMAIL for the User-Agent.",
    )
    ap.add_argument("--backend", choices=("auto", "rest", "sparql"), default="auto",
                    help="auto falls back to the official SPARQL endpoint")
    ap.add_argument("--json", action="store_true", help="machine-readable JSON output")
    ap.add_argument("--refresh", action="store_true", help="bypass the .cache/ entry")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("search", help="search DBLP venues by name/acronym")
    sp.add_argument("query", help='venue name or acronym, e.g. "SIGSPATIAL"')
    sp.add_argument("--max", type=int, default=10, help="max hits (default 10)")

    tp = sub.add_parser("toc-count", help="count papers in one year's proceedings toc")
    tp.add_argument("key", help="DBLP venue key, e.g. conf/gis")
    tp.add_argument("year", type=int, help="proceedings year, e.g. 2025")
    tp.add_argument("--bht", help="explicit toc path when it differs from "
                                  "db/<key>/<basename><year>.bht")

    args = ap.parse_args(argv)
    if args.cmd == "search" and not 1 <= args.max <= 100:
        ap.error("--max must be between 1 and 100")
    email = get_contact_email()
    if args.cmd == "search":
        return cmd_search(args, email)
    return cmd_toc_count(args, email)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except DblpError as exc:
        sys.exit("error: %s" % exc)
