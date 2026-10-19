# Optional local venue profiles

Local integration note, 2026-10-01. Upstream provides the lister but no profiles
or schema in this revision. Normal selection uses live official sources.

For an existing profile collection, pass its parent directory explicitly:
`python3 <skill-dir>/scripts/list_venues.py --venues-dir <profile-directory> --json`.
The directory must contain `conferences/*.yml`. Do not create an empty collection
and claim venue coverage. Discovery is not limited to the profile collection.

The lister reads these fields: `id`, `name`, `family`, `year`, `cfp_url`;
`deadlines` (abstract, paper, notification, camera_ready, timezone);
`tracks` (list of name, page_limit, page_limit_excludes, notes);
`review` (blind, submission_system, rebuttal_format); and
`verified` (date, confidence). Use YYYY-MM-DD for dates; leave unknowns null.
The bundled parser supports a limited YAML subset, not arbitrary YAML.

Its date arithmetic is calendar-day based. It does not resolve cutoff times,
AoE conversion, mandatory expired abstract-registration gates, or track-specific
deadlines stored in notes. Confirm the exact track's complete submission window
on the official site before describing a deadline as reachable. A venue-level
upcoming paper date alone does not establish that new submissions are allowed.

No real venue facts or user manuscript data are bundled here. Any profiles added
later need their own source and verification date. Avoid storing manuscript
content in the skill directory.
