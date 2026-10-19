# Common reference-verification patterns

Inherited metadata patterns and examples for reference checking. Preserve source
records and verify the applicable publication version rather than treating identifier
formats or historical coverage observations as proof for a new entry.

## 1. Volume year and DOI year differ

A year embedded in a DOI can reflect receipt or manuscript numbering rather than
publication. Use the official journal volume year, or the online year when no volume
is assigned.

| Pattern | Explanation | Example |
|---|---|---|
| DOI year precedes volume year | Manuscript numbering predates publication | DOI includes 2024; volume is 2025 → cite 2025 |
| Manuscript processing crosses years | Identifier and final publication dates differ | DOI includes 2025; publication is 2026 → cite 2026 |
| Online year differs from volume year | Online at year end, assigned to next year's volume | Online 2024-12-31; volume 2025 → cite 2025 |

## 2. Author-name problems

### 2.1 Fabricated first author

An invented first author differing from the DOI record is a critical error. Query
Crossref or IEEE by DOI and compare the first author's surname.

### 2.2 Reversed author order

Exports or manual edits can move a later author into first position. Use the order
on the official journal page.

### 2.3 Similar Chinese characters

Source-name examples include `廷` / `延`, `健` / `建`, and `浩` / `皓`. Preserve
these characters and check the official CNKI/Wanfang record.

### 2.4 Spanish or Portuguese double surnames

Paternal and maternal surnames may have several abbreviated forms. The inherited
example lists `Álvarez López Y`, `López Y Á`, and `Alvarez Lopez Y` as equivalent.

### 2.5 Abbreviated and complete author lists

Chinese citations may use `等` as an et-al marker. When listing all authors, commonly
for 3-5 authors, preserve the source order.

## 3. Page-number errors

Common contexts include preprint/final-version differences, preliminary/final
conference versions, journal/proceedings versions, and copying an adjacent entry's
pages. Check the official journal or conference record rather than trusting an export.

## 4. DOI problems

### 4.1 DOI resolves to another paper

A syntactically valid DOI can resolve to a different work after a one-digit typo,
such as 482157 → 482187. Compare the title returned by Crossref with the citation.

### 4.2 Missing older IEEE record

The inherited notes report missing Crossref records for some pre-2000 IEEE papers
that remain available in IEEE Xplore. A Crossref 404 alone must not mark them incorrect.

### 4.3 Missing Chinese DOI record

A DOI registered outside Crossref may require CNKI/Wanfang verification.

### 4.4 Multiple DOIs for one work

Preprint, published and OA records may differ. Prefer the selected published
version's DOI under the shared publication policy.

## 5. Conference-paper years

- Proceedings and journal-special-issue versions can have different pages and years.
- Use the official conference name rather than an unverified alias.
- The inherited convention uses the conference event year rather than the proceedings
  publication year; check it against the applicable citation and version requirements.

## 6. Theses

- Many theses predating the 2000s were not digitized.
- The Chinese master's-thesis format is `Author. Title[D]. University, Year.`
- Page numbers may be omitted.
- The inherited notes report broader thesis coverage in Wanfang than CNKI.

## 7. Product manuals and technical reports

- Use `[Z]` where the citation style uses that marker for other material.
- Confirm the product/institution exists and its official source is accessible.
- Use the release year of the referenced version.

## 8. Historical publisher names

Preserve the publisher name used for the cited edition. The inherited example
contrasts IEE (Institution of Electrical Engineers) on pre-2006 publications with
IET (Institution of Engineering and Technology) on later records. Check the actual
edition and official history when a name change affects verification.
