---
name: ai-use-drafter
description: >-
  Draft a standalone AI-use disclosure for an academic paper from actual usage
  records and author input. Use for AI 使用声明、AI use declaration or disclosure
  drafting. Deliver an editable draft for the author; never automatically insert
  it into a manuscript or submission form.
---

# AI-use disclosure draft

Help the author describe how AI was actually used. The deliverable is a separate
draft for the user to revise, not a finalized declaration or manuscript edit.

## Output boundary

- Return a clearly labelled draft in chat, or save a separate
  `drafts/ai-use-disclosure.draft.md` within the relevant research work directory
  when a file deliverable is appropriate. Do not infer a paper from an unrelated
  project or write into the skill installation directory.
- Do not modify manuscript text, acknowledgments, appendices, bibliography,
  submission fields, or LaTeX includes/build configuration. Do not add the draft
  to an automatic assembly pipeline. Suggested placement belongs in notes only.
- Leave insertion to the user. A request to generate, revise, or accept a draft
  does not authorize insertion; a later explicit request to insert specific text
  is a separate task.
- Preserve author edits. Read any existing draft first; when producing a new
  version, use a new filename unless asked to revise that existing file.

## Establish the facts

Use the supplied account and relevant, accessible project records. For each actual
use, identify the tool/model (version when known), task, affected material, and
what the author actually reviewed, changed, tested, or retained. Capture dates or
periods when available and relevant. Distinguish AI used as part of the research
method from AI used to assist the research or writing workflow.

Map supported uses to the bundled [GAIDeT tasks](references/gaidet-terms.yml) when
helpful. These categories describe tasks; they do not establish authorship,
policy compliance, human supervision, or whether disclosure is required. Select
only relevant tasks, not an exhaustive checklist in the statement.

- Installed tools are not evidence that they were used for this paper.
- Missing logs do not prove non-use. Keep unknown facts as questions for the
  author; do not guess model versions, task scope, or review actions.
- Distinguish drafting from proofreading, and proposed actions from completed
  actions. Do not reduce substantive AI assistance to language polishing.
- Do not erase historical use merely because the output was subsequently
  rewritten or discarded. Describe its actual role and disposition where needed.
- Do not prefill claims of full human supervision, complete verification,
  exclusively human intellectual contributions, or absence of sensitive data.
  Include such assertions only to the extent the author or records substantiate them.

## Draft and hand back

Use the paper's language and requested length. Write a concise natural paragraph
from known facts, with additional detail only when necessary or requested. Do not
impose a fixed template or require both short and long versions.

Describe specific actions and the material affected. Avoid umbrella phrases such
as "manuscript preparation", "writing assistance", "research support", or
"improving quality" as descriptions of AI use. A tool name or task-category
label alone is not an adequate account of what it did.

For example, when supported by actual records, write "corrected grammar in the
Abstract and Discussion", "drafted the first version of the Related Work
section", or "generated Python code for parsing evaluation logs". These are
wording examples, not facts to prefill. State which tasks actually occurred;
distinguish text generation, language correction, translation, literature
retrieval, code generation, and data analysis where relevant. Specify the scope
without inventing section names, coverage, or author verification actions.

When the task or scope is unknown, leave a precise question or placeholder for
the author instead of concealing the gap with a broad phrase. Greater specificity
must not turn substantive AI contributions into a claim of proofreading only.

When a target venue is given, consult its current official instructions or the
provided policy text for required content. Record the source and date in notes,
not in the declaration. If the target or policy is unavailable, produce a generic
draft and mark venue-specific wording as unverified; do not invent requirements
or claim acceptance/compliance. Do not upload project records to a website.

Present the draft first, followed by a short list of material facts the author
still needs to confirm. Use explicit placeholders for missing facts that the
paragraph cannot omit without misleading the reader. Keep source paths, policy
checks, and drafting notes separate from the proposed declaration text.

Before delivery, check that every described use names a supported action and its
scope, verify every factual assertion against the supplied information, ensure
uncertainty remains visible, and confirm the output is still a standalone draft.
No reviewer agent, external model call, or publication action is required.

## Integration and sources

`ts-paper-plan` may hand off the paper context and available usage records. Return
a separate draft path or chat draft; never merge declaration prose into its
manuscript blueprint. Cite-specific work, if actually needed, remains with the
existing citation workflow; do not alter the bibliography automatically.

The task vocabulary is copied unchanged from
[GAIDeT Declaration](https://github.com/panbibliotekar/gaidet-declaration)
at `9fac8c0b184f512e439764e83b6c123e76c60919` (`_data/terms.yml`), with its
[MIT license](references/LICENSE-gaidet). The website generator and its preset
assurances are not installed. The local instructions implement the user's
draft-only workflow; they are not an official venue policy.
