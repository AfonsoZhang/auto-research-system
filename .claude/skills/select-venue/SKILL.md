---
name: select-venue
description: Builds a ranked venue shortlist for a research paper. Use when the user asks where to submit, which conference or journal to target, venue selection, track selection, or mentions CORE rank, h5-index, acceptance rate, CCF class, or submission deadlines. Maps the paper's topic and contribution type (method, system, dataset, demo, vision, industrial, survey) to venue-track pairs scored on topic fit, track fit, prestige signals, and deadline proximity computed from the machine-readable venues/ profiles — with mandatory re-verification of deadlines and page limits against each live CFP before the user relies on them.
---

# Select Venue

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

<!-- Locally adapted 2026-10-01: missing profile data, installed-skill routing,
     command paths, and unknown-policy handling. Original saved in installation backup. -->

When this task includes assessing a candidate contribution, use the [shared topic-selection policy](../shared-references/topic-selection-policy.md). Literature coverage or venue fit alone does not settle research value. Do not restart topic selection for an ordinary literature/venue update.

## Local installation

This pinned upstream version does not ship `venues/` or `venues/schema.yml`.
Default to live venue discovery and official CFP / author-guideline checks; the
profile lister is optional and requires author-supplied or separately verified
profiles. See [optional profile format](references/venue-profiles.md). Never
invent profiles or dates just to make a helper run. Scripts use Python 3 standard
libraries only. DBLP lookup needs an actual `CONTACT_EMAIL` in the environment;
reuse an already configured contact email if available without printing it. If
absent, use browser/web discovery instead of sending the example address.

Reuse topic, contribution, and constraints already supplied; ask only for missing
information that materially changes the shortlist. Scores express comparative
fit, not acceptance probabilities. Unknown requirements remain pending, not a
reason to infer poor fit or rule the venue out. A verified, applicable conflict
can exclude a candidate. Apply current official policy to preprints, article
types, and tracks; historical examples below are not universal restrictions.

Output the shortlist for the author to choose. Do not change a manuscript or
choose a final target on the author's behalf. After selection, apply
[target calibration](../shared-references/paper-type-routing.md#calibrate-to-the-selected-target)
(requirements, target's published papers, exemplars one or two tiers higher); use the installed
[ts-paper-plan](../ts-paper-plan/SKILL.md); use [research-lit](../research-lit/SKILL.md)
for recent published exemplars and [nature-ref-verifier](../nature-ref-verifier/SKILL.md)
for citation verification. Other upstream skills named below are not installed
by this package and are not prerequisites.

Turn "where should I submit this paper?" into a ranked shortlist of
venue-track pairs with scores, deadlines, page budgets, and an explicit
verification status, grounded in official sources and any available verified profiles.

## DBLP access in this installation

The helper defaults to `--backend auto`: when the original search API returns
HTML or fails, it uses DBLP's [official SPARQL API](https://blog.dblp.org/2024/09/09/introducing-our-public-sparql-query-service/).
Use `--backend sparql` before the subcommand to go directly to that endpoint.
Both paths keep rate limits, validate JSON, and cache successful responses only.
Contact email also falls back to `ARIS_VERIFY_EMAIL` or `OPENALEX_EMAIL`.
`DBLP_CACHE_DIR` optionally chooses an isolated cache directory.

SPARQL venue search matches all query words as substrings of titles or aliases;
it does not implement the original search API's operator syntax. Use returned
`dblp_key` values, never derive them from acronyms (AAMAS is `conf/ifaamas`).
TOC counting resolves the actual volume for the venue/year; if several exist,
choose a specific `--bht` instead of combining volumes. Counts are distinct DBLP
TOC records and can include short papers or other entry types; they are not
full-paper acceptance statistics. JSON identifies the backend and count scope.

## When to use

- The user asks where to submit a paper, for target-venue recommendations,
  or to compare candidate venues/tracks.
- The user asks "does my paper fit venue X?" or "research track or industry
  track?"
- The user mentions CORE rank, h5-index, CCF class, acceptance rates, or
  upcoming CS conference deadlines in a submission-planning context.

Not for: parsing one specific CFP into a profile (`parse-cfp`), adapting a
draft to an already-chosen venue (`tailor-to-venue`), or pre-submission
compliance checks (`preflight-check`).

## Inputs

- **Topic** — one or two sentences on what the paper is about.
- **Contribution type** — classify using `references/track-fit.md`; ask the
  user if ambiguous.
- **Constraints** — earliest realistic submission date, prestige goals
  (and whether CCF class matters), page-budget reality of the current
  draft, blind-level conflicts (e.g. an already-public preprint),
  travel/registration constraints.
- **Venue data** — official CFPs / author guidelines and recent published examples.
  Optional local profiles use [this format](references/venue-profiles.md).

## Process

1. **Elicit the inputs.** Confirm topic, contribution type, and constraints
   in one round of questions. The contribution type changes the shortlist
   more than the topic — pin it down first (`references/track-fit.md`,
   "Contribution taxonomy").

2. **Discover venues.** Search official venue pages and relevant published papers.
   Only if a populated local profile directory is available, run:

   ```
   python3 $RESEARCH_ROOT/.claude/skills/select-venue/scripts/list_venues.py --venues-dir <profile-directory>
   ```

   This lists every profile with deadline proximity, blind level,
   submission system, and per-track page budgets, sorted by next upcoming
   submission deadline. Useful flags: `--upcoming-only`, `--family <name>`,
   `--track <name>`, `--json` (full data incl. track notes), `--today
   YYYY-MM-DD` (reproducible runs). Never compute date arithmetic by hand.
   Caveat: some venues (e.g. SIGSPATIAL) have per-track deadlines that
   differ from the top-level ones — they live in each track's `notes`
   field; read them in the `--json` output.

3. **Build the candidate set.** Combine (a) profiled venues that plausibly
   match the topic, and (b) venues you know fit the topic but have no
   profile yet. For unprofiled candidates, resolve identity via DBLP:

   ```
   python3 $RESEARCH_ROOT/.claude/skills/select-venue/scripts/dblp_venue_lookup.py search "<venue name>"
   ```

   Optionally gauge venue size with
   `dblp_venue_lookup.py toc-count <dblp_key> <year>`. Mark every
   unprofiled candidate clearly and record the current official CFP facts when useful.
   Aim for 5-10 candidate venue-track pairs before scoring.

4. **Gather prestige signals.** For each candidate, look up CORE rank,
   h5-index, CCF class (if the user cares), and acceptance rate following
   `references/ranking-sources.md`. Hard rule: every number carries a
   source + edition/year, or is labeled "unverified — indicative" /
   "unknown". Never state a rank or acceptance rate from memory as fact,
   and never invent one.

5. **Score and rank.** Apply the 0-10 rubric in `references/track-fit.md`
   (topic fit 0-3, track fit 0-3, prestige fit 0-2, deadline feasibility
   0-2), then apply its tie-breakers and red-flag vetoes (embargoes,
   dual-submission bans, attendance mandates).

6. **Re-verify the top picks against live CFPs — mandatory.** For the top
   3 venues, fetch each profile's `cfp_url` and confirm the facts the user
   will act on: deadlines (and their timezone — AoE vs PT matters), page
   limits and what they exclude, blind level, submission system. Profiles
   are a starting point, never ground truth; a stale page limit causes a
   desk reject. Record what was verified and when in the output. If a CFP
   cannot be reached, mark that venue "NOT re-verified" — do not silently
   present profile data as confirmed.

7. **Deliver the shortlist** (format below). Once the author selects a target,
   hand verified requirements to the installed `ts-paper-plan` when requested.

## Output

A ranked shortlist in chat (offer to save as `venue-shortlist.md`):

| # | Venue / track | Score | Deadline (tz) | Pages | Blind | Rank signals | Verified |
|---|---|---|---|---|---|---|---|
| 1 | SIGSPATIAL 2026 / Research | 9/10 | abstract 2026-05-29, paper 2026-06-05 (PT) | 10p excl refs +2p appendix | single | CORE2023 A (verify) | live CFP 2026-06-11 |

Below the table, per venue: 2-4 lines of rationale (the four rubric scores
with one-line justifications), the red flags checked, and — for any venue
whose deadline has passed — the next expected cycle. Close with the
explicit disclaimer that the user must confirm all critical facts on the
venue's own CFP page before planning around them.

## Bundled resources

- `references/ranking-sources.md` — CORE, h5-index, acceptance rates, CCF,
  deadline aggregators: where each lives, how to interpret, how to cite.
- `references/track-fit.md` — contribution taxonomy, track archetypes,
  the scoring rubric, tie-breakers, red flags.
- `scripts/list_venues.py` — stdlib-only profile lister + deadline math.
- `scripts/dblp_venue_lookup.py` — polite DBLP venue resolver (rate-limited
  ≤1 req/s, cached under `.cache/`, needs `CONTACT_EMAIL`).

## Guardrails

- Profiles and this skill's tables are **never ground truth** — re-verify
  deadlines, page limits, and policies against the live `cfp_url` (step 6)
  and say so in the output.
- Never fabricate ranks, h5-indexes, acceptance rates, or citations; route
  any bibliographic citation through the installed `nature-ref-verifier`.
- Never submit to, register with, or create accounts on any submission
  system on the user's behalf.
- Fetch venue/CFP pages on demand and process them transiently; do not
  copy paper abstracts or full text into the repo (metadata is fine).
- Prestige caps at 2 of 10 points by design — do not let "it's A*"
  override fit, and do not present prestige as publication advice ("aim
  lower/higher") unless the user asked for that judgment.
