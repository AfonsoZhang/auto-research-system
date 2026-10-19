---
name: intro-drafter
description: >-
  Draft, outline or restructure an Introduction from the author's materials.
  Match the argument to the contribution type, using a method-paper flowchart
  only where appropriate; preserve evidence and weave verified citations.
  Return flowing prose by default or an outline on request.

license: CC-BY-NC-SA-4.0
---

# Introduction Drafter

Apply the shared [working-language policy](../shared-references/research-autonomy.md#working-language) to internal work and user reports.

For structure or evidence requirements, use [paper-type-routing.md](../shared-references/paper-type-routing.md). Reuse the contribution type, stage and venue from existing materials; select only claim-relevant checks. This selects guidance within the current task and does not start another phase.

For substantive claim creation or revision, follow the [cross-revision claim-preservation policy](../shared-references/claim-preservation.md).

## Overview

The Introduction is the compressed version of the entire paper. In one and a
half to two pages it must state the research object, why the problem
matters, why existing work falls short, what the paper contributes, and how
the contributions map to sections. Reviewers decide whether to keep reading
by the end of the Introduction, so the logical throughline has to be
airtight.

This skill is a **prose generator**, not an outline generator. It takes a
small set of inputs (research area, limitations, key idea, challenges,
solution overview, optional references) and produces real Introduction prose. Select the argument from the shared
paper-type route. The six-part method flowchart is an optional internal
scaffold, not a mandatory paragraph count.

The delivered text must read as if a researcher wrote it: flowing
paragraphs, no inline tags, no "Paragraph 1: Background" headings, no
severity tables, no consistency reports. Just the Introduction.

An explicit outline is still available: see "Outline mode" below.

## Evidence rules (inherited)

This skill follows the shared evidence discipline: every factual claim
traces to the user's materials, this session's verified retrieval, or field
common knowledge; model memory is never a source; delivered prose carries
zero bracketed placeholder tags; details the user did not provide (specific
scenarios, mechanisms, magnitudes, procedures, identifiers) are omitted, not
invented.

See: references/evidence-discipline.md and references/prose-delivery.md
(shared with `paper-writer`).

## When to use this skill

- "Write the Introduction." "Draft the Intro from this idea."
- The user has a paragraph of research thinking and wants finished prose,
  not bullets.
- The user has Goal and Key Idea settled but no Introduction text yet.
- The user pastes references and asks for them woven into the Introduction.

## When NOT to use this skill

- Any non-Introduction section: `paper-writer`.
- Prose exists and needs polishing: `paper-polish`.
- The user wants a submission-readiness verdict: `pre-submission-reviewer`.

## Pre-check: contribution type

Use the existing paper-type route. Method/system and new-problem-with-solution
papers may use the flowchart below. Evaluation/resource introductions foreground
the measurement gap; analysis/negative-result/replication papers the question and
what was learned; theory the formal problem and result; surveys the scope and
synthesis; position papers the thesis and reasoning. Use the corresponding shared
profile and write the requested Introduction here, keeping the evidence rules.
Do not route back and forth to `paper-writer` merely because a type is non-method.

For non-method papers, skip method-specific Steps 1–4 below and organize the
actual argument from existing material. Use Steps 5–6 for prose and delivery,
with paragraph/citation count determined by content and the venue.

## Method/system scaffold (when applicable)

Internal thinking first, prose second. None of the intermediate thinking is
printed.

### Step 1: paper-type positioning (internal)

See: references/paper-types.md for the Technique versus New Problem/Setting
distinction and worked examples from Alpha-SQL, AFlow, and LEAD.

- **Technique paper**: the contribution is a new method for an existing
  problem; the narrative axis is the key idea; Paragraph 3 is a short
  bridge.
- **New Problem/Setting paper**: the contribution is the problem
  formulation itself; Paragraph 3 is load-bearing.

### Step 2: plan the applicable argument functions (internal)

See: references/flowchart.md for each paragraph's purpose, writing points,
and common failures.

For each paragraph, settle: its purpose; two to four concrete writing
points drawn from the user's inputs; and its gaps (what the inputs do not
yet cover). Gaps are reported to the user after the prose, never inside it.

1. Background and motivation; a supplied example when useful.
2. Relevant, substantiated limitations of existing work.
3. Problem essence and goal; hard constraints explicit.
4. Challenges that the proposed design actually addresses.
5. Solution overview, where this is the contribution.
6. Actual contributions and where their support appears.

Combine functions as needed; these are not six required paragraphs.

### Step 3: the running example (internal)

See: references/running-example.md for the design principles and patterns.

If a real example is supplied and useful, use it consistently. Otherwise write
from the supplied problem description without inventing an example. Request one
only if a specific explanatory gap makes it material; it is not a required slot.

### Step 4: alignment checks (internal, before writing)

See: references/contribution-patterns.md for strong versus weak
contribution patterns.

Verify silently that the actual contributions follow from the question and
evidence; method choices answer the claimed challenges and terminology stays
consistent. Keep a supplied example consistent where used. Do not manufacture
one-to-one modules or three/four contributions; counts follow the real argument.

A failed check is fixed in the plan before any prose is written. Never
write around a broken chain.

**Human in the loop: the user picks the direction.** Before
writing the full Introduction,
offer 2-3 short versions that differ in direction (framing, what is generalized,
what leads), each one or two sentences or a paragraph skeleton, with the
trade-off of each. Expand only the version the user picks. Wording-level polish
of an agreed direction needs no new choice.

### Step 5: write the prose

Write flowing paragraphs for the selected argument, under these disciplines:

- **No paragraph labels in the output.** Natural transitions carry the
  structure ("Despite this progress, ...", "In this work, we ...", "We
  summarise our contributions as follows.").
- **Each paragraph develops a coherent point**; length follows its content
  and venue space rather than a fixed word range.
- **Citations**: use the selected venue style and verified sources relevant to
  the actual argument, with no quota or forced numeric style. Give a References
  list matching the citations when writing standalone prose. At three or more
  citations, use the existing `paper-writer` verification ladder, with honest
  capability degradation and disclosure. Search only the needed unresolved
  sources; reuse already verified references and do not inflate the bibliography.

- **Numbers and claims**: no invented percentages, speedups, or benchmark
  numbers. A specific gain appears only if the user reported it; otherwise
  state the proposed mechanism or objective without asserting an unmeasured gain.
- **Tense**: past for prior work and observations; present or future for
  the paper's own unvalidated claims ("this paper proposes"). Without
  reported results, never "we achieved" or "we demonstrated".
- **Tone pass**: before finalising, strip AI-tone signals and unsupported
  superlatives, and match verbs to evidence strength (see the "Tone
  references" section below for where the shared wordlists live).

### Step 6: a short closing note (optional, three lines at most)

After the prose (and References), at most a short plain-language note:
gaps the user should fill, a paragraph written tentatively for lack of
input, or the running-example request from Step 3. No tables, no lists, no
severity labels. Nothing useful to say means no note at all.

## What the user receives

- Introduction prose separated by blank lines, with citations in the selected
  venue style and length suited to the argument.
- A References list right after the prose, when citations are present.
- Optionally, one one-to-three-line plain note.

Nothing else. The full prohibition list (headings, gate results, severity
summaries, placeholder tags, process preambles) lives in
references/prose-delivery.md and is binding.

## Outline mode (on explicit request)

When the user asks for an outline, give the selected argument's paragraph or
section purposes and material gaps. Use the method flowchart only when it fits;
do not emit its module/alignment checks for other types. Reuse existing evidence
and identifiers, and keep the requested outline proportional to the task.

## Tone references

The shared style references live with their canonical copies in
`paper-polish` (ai-tone-guardrails, academic-phrasebank,
section-conventions) and apply to this skill's prose pass; consult them
through that skill's references when finer wording support is needed.

## Cross-skill handoffs

- Introduction done, rest of the paper wanted: `paper-writer`.
- Prose in place but stiff: `paper-polish`.
- A substantive uncertainty about the contribution: identify the concrete
  unresolved claim briefly. Topic reevaluation is a separate requested task;
  do not impose an unspecified top-venue threshold during drafting.

## Output language

Follow an explicit language request first; a named Chinese journal or
Chinese thesis means Chinese prose; otherwise default to English. Never
infer the output language from the language of the user's message.
