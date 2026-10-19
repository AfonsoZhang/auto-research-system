---
name: human-annotation-page
description: >-
  Build a local, single-file HTML page for the user to label or check research items
  by hand (gold labels, human checks of LLM labels, browser checks), with autosave and
  a JSON download. Use whenever the user is asked to annotate, label, verify or check
  a sample by clicking. Output stays a local file, never an Artifact.
---

# Human annotation page

## Hard rules

- **Local file only.** Write the page to the project (next to its sample, e.g.
  `data/<...>/audit/<check>/<name>.html`) and give the user the Windows path from
  `wslpath -w <file>`. Do not publish it with the Artifact tool or any hosting, even
  though it is HTML; research items and answers stay on disk.
- **Freeze the design before the page.** Write a `design.json` beside the page first:
  purpose, frame, sample size and stratification, seed, what is shown, answer scheme,
  metrics, and how the result is used whatever it shows. Do not change items, answer
  options or scoring after the user starts; if a scoring rule is only fixed after
  reading answers, record that in the project's deviations log.
- **Blind.** Never show automatic, model or reviewed labels, stratum or cell. Shuffle
  item order with a fixed seed so strata cannot be inferred from position.
- **Show what the label is about.** Use the same inputs as the labels under check
  (same text cut-offs, same reference material), and say on the page which part is the
  object being judged and which is reference only.
- **Generate with a script**, kept in the project (e.g. `study/<name>_page.py`), so the
  page can be rebuilt; the script reads the frozen item list from `design.json`.

## Page contract

Start from `references/example_k1_check_page.py` (two-level answers: type, then a
follow-up only for one type) or the project's earlier page if it has one; reuse its
style so the user sees a familiar layout.

- One card per item: number, link (opens in a new tab), the judged content, the
  reference (thumbnail screenshot, downscaled into `thumbs/` beside the page, ~400 px wide).
- Short intro with a legend for every answer code, the exact question, `?` for unsure,
  and an optional note box per item.
- Keyboard shortcuts on the focused card; progress bar with "n / N"; filter "Not answered".
- Autosave each click to `localStorage` under a page-specific key, wrapped in try/catch
  with a visible banner when storage is blocked.
- "Download answers" saves `<name>_answers.json` (one row per item, unanswered rows
  included with nulls) to the user's Downloads. Tell the user to click it and tell you.
- An item counts as done only when every required sub-answer is present.
- Inline all data and script; no external scripts. Escape `</` inside embedded JSON.

## Verify before handing over

`file:` URLs are blocked in the Playwright browser: serve the directory with
`python3 -m http.server <port> --bind 127.0.0.1` in the background, then check with
Playwright: no console errors other than favicon, all thumbnails load, a click saves,
follow-up questions show/hide correctly, the done count is right. Clear the test answers
from `localStorage` and stop the server afterwards.

## After the user returns answers

Read the downloaded JSON from the browser's download folder (newest file of that name),
copy it into the project beside `design.json`, and score it exactly as `design.json`
says. Report every disagreement with the user's note; do not silently drop `?` items,
report their count.

**Ask the user to re-check a disagreement** with a concrete comparison method: which
panel to look at (re-read the page's actual layout before naming left or right),
which text to search for, and what each label would require. Describe the judged
content fully (its length and what it consists of), not its first line. When the
user checks the live site, remind them it is the rendered page; a static-fetch label
is judged on the fetched text shown on the page, so locate quoted text in that file.

**Adjudication.** Discussing disagreements after the blind pass is normal
adjudication, not contamination. Keep the blind answers unchanged (dated copy) and
write the final labels with one cause per item to a separate `adjudication.json`;
the reviewed labels file stays as it was unless a label is shown wrong. Attribute a
disagreement to unclear instructions only after checking the page text said
otherwise; otherwise list causes neutrally.

**Reporting.** Report the blind pass as the independent comparison (agreement,
kappa, reweighted to the frame when strata were sampled unequally), then the
adjudication outcome, and say the reviewer took part in the discussion. Do not
derive an error-rate bound from the adjudicated result: it is not independent.
Credibility comes from the concrete details (fixed plan, imperfect kappa, named
causes), not from a bound.
