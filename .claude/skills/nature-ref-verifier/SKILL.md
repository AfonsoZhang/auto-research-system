---
name: nature-ref-verifier
description: >-
  Cross-check academic references against multiple sources, comparing authors,
  titles, years, volumes, issues and pages. Flag year conflicts, author-order
  errors, page discrepancies and DOI mismatches in a structured report.
  Verify individual entries or complete bibliographies and prepare Zotero corrections.
---

# nature-ref-verifier: Multi-source reference verification

For literature-review or citation work, first read the
[publication/version policy](../shared-references/publication-policy.md) and reuse
`literature/publication_records.json` or the supplied record path. Report publication
status, peer-review status, selected version and official evidence separately from
field consistency. `Verified` means the checked fields agree; it does not establish
peer review. Investigate new or conflicting records and reuse stable ones. After
replacing a preprint with a published version, check associated claims rather than
only changing the DOI. A single-reference formatting check retains its requested scope.

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language):
English verification records and internal reports; a Chinese final user report.
Preserve original reference titles, author names and other source metadata.

Read `references/common-patterns.md` for batch discrepancies, recurring field errors,
DOI/title conflicts, author order, page drift or report wording. Do not preload it for
unrelated work. `manifest.yaml` records the same conditional routing; document the
loading condition here whenever adding a resource.

## Triggers

`verify references`, `check references`, `bibliography verification`, `ref check`.

## Use cases

- Final bibliography checks before a proposal or paper submission.
- Locating citation errors raised in review.
- Validating references transferred from an older project.
- Periodic Zotero library checks.

## Workflow

### Step 1: Parse the input

**A. Complete paper or proposal:** extract the numbered `[N]` bibliography and
identify each DOI where available.

**B. Individual reference:** accept pasted citation text or a Zotero item key.

**C. BibTeX file:** parse `.bib` and check entries individually.

### Step 2: Query sources in parallel

**Step 2.0: Check the DOI record first.** Request
`https://api.crossref.org/works/<DOI>`. A 404 means Crossref has no record; continue
with DOI resolution, another registration agency and the publisher rather than
calling the DOI invalid. For a 200 response, compare title, authors and publication
fields. A different title/author record indicates a mismatched DOI. An inherited
35-reference audit found that 7/9 errors were of this kind.

Query available sources for each entry:

| Source | Suitable references | Recorded coverage or role |
|---|---|---|
| Crossref | DOI-bearing international journal articles | Approximately 70% in the prior workflow; older IEEE and Chinese records may be absent |
| IEEE Xplore | IEEE journals and conferences | Fallback for an IEEE DOI with no Crossref record |
| WebSearch (Bing/Google) | Missing DOI or source coverage | General fallback |
| CNKI / Wanfang through kimi-datasource or webbridge | Chinese journals and theses | Check these sources for Chinese literature |
| Local Zotero library through zotero-mcp | Imported references | Quick comparison with stored metadata |

Prefer DOI lookup in Crossref, then search the web by title and author when needed.
For more than 20 entries, when delegation is authorized, the existing batching
convention uses groups of 10–15 for parallel agents and merges their independently
checked results. The prior 35-entry trial reported completion with 3 parallel agents
in one round trip and serial execution roughly an order of magnitude slower. This
is a historical observation, not a new benchmark or a general timing guarantee.

### Step 3: Compare fields

#### Critical: correction required

| Check | Description | Recorded example |
|---|---|---|
| Author names or order | Different first author, reversed order or fabricated names | Smogavec → Leckebusch; Vainikainen → Mikhnev |
| Missing authors | Fewer authors than the publisher record, often 3–4 recorded for papers with 5+ | Fifth author Ge omitted from a TGRS 2019 PCA paper; fifth author Kim omitted from a TAES 2021 UAV paper |
| Page discrepancy ≥5 | Substantially different page range | Noon: 1309-1319 → 1444-1449 |
| Article-number character confusion | Letters mistaken for digits, such as T/7, l/1 or O/0 | SPIE 101880T entered as 1018807 |
| Core title-word mismatch | More than capitalization or punctuation | Inherited examples: Iwasaki T → Wu K H; Zhang W → Zhu M H |
| DOI points to another paper | Existing DOI with a different title or author record | Abidi 1995: 10.1109/4.482157 → 10.1109/4.482187 |
| Resolvable but mismatched DOI | Title/author comparison identifies a different work | A JAG 2017 SVD citation resolved to an ERT article in the same volume; an AST 2022 rotor citation resolved to a turbine-noise article |

#### Warning: check suggested

| Check | Description | Recorded example |
|---|---|---|
| Volume year differs from the year embedded in the DOI | Different publication and identifier dates | Dadrass: volume 2025 / online 2024; Ni: volume 2022 / DOI includes 2020 |
| Early Access metadata drift | Volume, issue, pages and year may change on final publication; compare the current Crossref record | TGRS autoencoder: 59(12):10437-10449, 2021 → 60:1-13, 2022 |
| Missing or extra middle initial | Name-form discrepancy | Rabiner L vs Rabiner L R; usually still searchable |
| Missing issue | Volume present without issue | Smogavec 2025: 17 → 17(10) |
| Page discrepancy ≤4 | Small range difference | Leckebusch: 15-24 → 15-25 |
| Publisher-name variant | Possible historical name change | IET vs IEE |

#### Info: formatting differences

| Check | Description |
|---|---|
| Title capitalization | Title case vs sentence case |
| Abbreviated vs full journal name | IEEE Trans. AES vs IEEE Transactions on Aerospace and Electronic Systems |
| Punctuation or conjunctions | For example, and vs & |

### Step 4: Assess verification status

| Status | Meaning |
|---|---|
| ✅ Verified | Multiple sources agree; no correction identified |
| ⚠️ Check suggested | Warning-level discrepancy requiring judgment |
| ❌ Needs fix | Critical discrepancy requiring correction |
| ❓ Unverifiable | No checked source supplied a record, as with some internal reports or old theses |

### Step 5: Produce the report

**Internal Markdown report template:**

```markdown
## Verification results: 56 references

- ✅ Verified: 42
- ⚠️ Check suggested: 8
- ❌ Needs fix: 4
- ❓ Unverifiable: 2

### ❌ Corrections required
| # | Issue | Current value | Correct value | Source |
|---|---|---|---|---|
| [6] | Incorrect author | Smogavec P | Leckebusch J | Wiley |
| [42] | Reversed author order | Vainikainen P… | Mikhnev V A… | IEEE |

### ⚠️ Checks suggested
| # | Issue | Details |
|---|---|---|
| [18] | Volume/DOI-year mismatch | Volume year 2025; DOI includes 2024 |
```

**BibTeX patch:** generate the corrected `.bib` content.

**Zotero update instructions:** prepare a correction list for the library. Preserve
these integration observations recorded in 2026:

- Zotero 7's local HTTP API at localhost:23119 was read-only; writes returned 501.
  Wrapper instability or a busy Zotero instance can be checked directly with curl
  and `--max-time`.
- The preferred batch-write path is pyzotero Web mode with userID and API key,
  CRUD support and 429 backoff.
- Without a key, local `/connector/saveItems` can add items, not edit existing ones.
- Direct `zotero.sqlite` changes require Zotero to be closed and manual maintenance
  of related tables and versions; retain this only as a last resort.
- Confirm the item is actually in Zotero before correcting it. An empty title search
  may mean the bibliography came from another source, such as a literature CSV.

## Multi-source verification sequence

```text
User input: DOI/title
  -> Parse author/title/year/volume/pages
  -> Query Crossref (DOI), IEEE Xplore and WebSearch in parallel
  -> Compare author/title/year/volume/issue/pages/DOI/journal
  -> Rate discrepancies and assign verification status
```

## Known coverage gaps

| Gap | Response |
|---|---|
| Chinese DOI absent from Crossref | Check CNKI/Wanfang through webbridge or WebSearch |
| Older IEEE DOI returns 404 | Search IEEE Xplore directly; a missing Crossref record alone is not an error |
| Thesis without DOI | Verify title, author and year through CNKI, Wanfang or ProQuest |
| Product manual or patent | Confirm the source is accessible; the existing workflow does not verify all metadata |
| Missing Google Scholar result | Try Bing, Baidu Scholar or Semantic Scholar |

## Optional dependencies

Use available tools and fall back when they are absent:

- `pyzotero[cli]`: preferred Zotero channel, with local read-only and Web read/write
  modes; its CLI can be called from Bash without a persistent process.
- `zotero-cli` / `zotero-mcp`: local Zotero wrappers; prior tests found lower stability.
- `kimi-datasource` (scholar): academic search.
- `kimi-webbridge`: authenticated CNKI access.
- WebSearch / FetchURL: general fallback.
