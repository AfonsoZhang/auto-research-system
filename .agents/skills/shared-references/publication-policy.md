# Literature workflow: published versions first

Local shared policy for this research installation. Apply during literature discovery,
selection, synthesis and citation work; an explicit user scope overrides the defaults.
Do not turn a single-paper question or translation into a full literature review.

## Sources and order

1. `research-lit` discovers papers using Semantic Scholar, OpenAlex, Exa and web,
   plus available local libraries. The installed S2 and Exa helpers use existing
   environment credentials. Never print keys or embed them in notes or commands.
   If needed, load the existing `~/.secrets/aris.env` in a shell with tracing off;
   never display its contents. Report unavailable requested sources without
   treating their failure as evidence that a paper does not exist.
2. `verify_papers.py` checks **existence only**. Preserve its output and statuses.
   `verified` and a resolvable DOI do not certify publication, review or claim quality.
3. Before substantive extraction, resolve publication/version evidence as below.
4. `nature-reader` reads the selected version; `research-lit` synthesizes its evidence.
5. `novelty-check` compares concrete contributions using the same records, including
   separately labeled recent preprints. Topic overlap is not a rejection criterion.
6. `ts-paper-cite` builds citations from these records; `nature-ref-verifier` checks
   bibliographic identity, publication evidence and version consistency again.

## Resolve publication and versions

- Reuse `semantic_scholar_fetch.py paper <identifier>`, `openalex_fetch.py work
  <DOI-or-OpenAlex-ID> --json`, Crossref's `/works/<doi>`, and official venue pages.
  Resolve helpers through the existing ARIS helper chain; never change `~/.aris/repo`.
  If an index lookup returns 404, try a known alternate identifier or title/authors
  and cross-check identity. Record the lookup gap; do not infer that the paper is fake.
- S2 `externalIds`, OpenAlex `locations`, arXiv related DOI/journal reference and
  Crossref `is-preprint-of`/`has-preprint` relations are matching leads. Compare title,
  authors and contribution; title similarity alone must not silently merge papers.
  Keep a distinct journal extension separate if it adds substantive results.
- Use Exa for targeted title + author searches for proceedings, publisher pages,
  acceptance lists or changed titles. For official acceptance pages, use general
  web search too: a `research paper` category can miss a conference program.
  Open the actual page; search snippets and LLM summaries are not publication proof.
- Record publication and peer-review status separately. A publisher/proceedings
  entry supports `published`; an official acceptance record supports `accepted`.
  Confirm peer review from the applicable venue/track policy or official review
  record. An OpenReview submission alone is not an acceptance. Keep Main, Findings,
  Demo and Workshop labels exact. Early Access may already be formally published.
- Prefer verified `publishedVersion`, then `acceptedVersion` for core synthesis.
  A PDF hosted on arXiv may be an accepted manuscript: classify the actual version,
  not the host. OpenAlex version flags are discovery evidence, not a standalone
  guarantee of peer review. Missing relationships/metadata remain `unknown`.
- No citation-count threshold, journal-only restriction, or open-access-only
  restriction by default. Include relevant conference papers and recent work.
  Crossref 404 means that registry has no match, not that the DOI is necessarily fake;
  try DOI resolution, the registration agency or the official publication page.

## Shared record and selection

Use **`literature/publication_records.json`** relative to the current research topic
directory (or an explicitly supplied path). Keep independent research under
`$RESEARCH_ROOT`, not in an unrelated code repository. Reuse an existing record file;
do not create a parallel bibliography per skill. Back up before replacing records.

Top level: `{"schema_version": 1, "papers": [...]}`. Each paper has:

| Field | Meaning |
|---|---|
| `id`, `title` | Stable local ID and verified title; ID survives version upgrades |
| `doi`, `arxiv_id` | Known identifiers or null; DOI refers to the selected publication |
| `aliases` | Other known identifiers, such as a preprint DOI; one work per row |
| `existence_status` | `verified`, `unverified`, `verify_pending`, `error` from existence check |
| `publication_status` | `published`, `accepted`, `preprint`, `unknown` |
| `peer_review_status` | `confirmed`, `not_peer_reviewed`, `unknown` |
| `venue` | Exact venue, year and track when known; otherwise null |
| `selected_version` | `publishedVersion`, `acceptedVersion`, `submittedVersion`, `unknown` |
| `selected_source_url` | Exact chosen source URL (version-pinned where possible); null until selected |
| `tier` | `core`, `supplement`, `pending`, `excluded` |
| `selection_reason` | Inclusion/exclusion reasoning; required for supplements |
| `evidence` | Objects with `url`, `kind`, `supports`, `checked_at`, `note` |
| `read_source` | Null before reading; then `{url, version, sha256}` (hash optional for HTML) |

Evidence `kind`: `publisher`, `proceedings`, `official_acceptance`, `official_review`,
`index`. `supports` lists `publication`, `peer_review`, and/or `version_link`.
`checked_at` is an ISO date; `note` states the observed fact, not a model confidence
score. Store the page/passage used to support the decision; do not invent evidence.
`read_source.url` must match `selected_source_url`; for mutable URLs retain the PDF
hash or retrieval snapshot so changing content is not mistaken for the old reading.

- **Core:** existence verified, published or accepted, peer review confirmed with
  official evidence, selected accepted/published version. Core supports the main synthesis.
- **Supplement:** verified work outside that default, e.g. important preprints,
  published work with unknown review status, standards or software documentation.
  Record why it is needed and label its status. This is a preference, not a ban.
- **Pending:** matching or verification unresolved; retain for follow-up, do not use
  it to assert novelty absence or establish a factual conclusion.
- **Excluded:** irrelevant or excluded by the user's protocol; retain the reason.

If no core papers qualify, report the gap; do not silently substitute preprints or
claim a finished peer-reviewed evidence base. Do not discard preprints from novelty
search: they may still contain the same result. Publication preference is not a
license to claim novelty while ignoring accessible prior work.

## Handoff and checks

Run the installed structural checker (resolve it like other ARIS helpers):

```bash
python3 $RESEARCH_ROOT/.agents/aris/tools/publication_gate.py literature/publication_records.json
```

This checker validates recorded decisions, required evidence fields and identity
consistency. **It does not fetch pages or certify that the recorded evidence is true.**
The executor must do the actual official-source verification above.

For each citation in `claims_map.json`, retain existing fields and add `paper_id`,
`read_version`, `evidence_url`, `evidence_locator` (actual section/page/table or
`abstract` for an abstract-only claim). A citation cannot support a body-text claim
that was only checked against an abstract. Before citation delivery run:

```bash
python3 $RESEARCH_ROOT/.agents/aris/tools/publication_gate.py literature/publication_records.json --claims-map claims_map.json
```

Then run the existing citation linter; neither check replaces the other. Standalone
reference-format cleanup does not require a claims map or reading every full paper.

Recheck new, pending, conflicting or upgraded records, and confirm status before
final delivery. Reuse stable evidence and notes. On a version upgrade, keep history,
compare affected claims/tables and re-read changed evidence; updating a DOI alone
does not update the evidence. Until checked, keep the old `read_source` and do not
represent it as reading the new version. Update only affected claims, not the whole
review. Never invoke a separate model/reviewer merely to establish publication status.
