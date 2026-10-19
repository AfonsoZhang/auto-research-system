# Forbidden patterns

## Table of contents

1. Punctuation in context
2. Inflated or unclear wording
3. Chartjunk patterns
4. Overclaim patterns
5. Plagiarism red lines
6. Detection heuristics

## 1. Punctuation in context

Use the shared [author dash restriction](../../paper-polish/references/ai-tone-guardrails.md#author-style-dash-restriction).
The author requires rewriting prose dashes used as sentence connectors or
parenthetical breaks. Preserve the documented exceptions for ranges, technical
syntax, names, and exact source text. Flag an in-scope occurrence as a required
presentation correction, normally MINOR. A dash is not a scientific defect or
evidence of AI authorship; occurrence counts do not make the finding MAJOR.

## 2. Inflated or unclear wording

Inspect vague praise, redundant hedging and unsupported superlatives in context.
Words such as “superior”, “general-purpose”, “reveal” or “yet” are not prohibited.
For a comparative term, check its evidence and scope; retain a supported strong
claim. Count neither word occurrences nor punctuation as MAJOR findings. Suggest
an edit only for a real clarity, fidelity or claim-support problem.

## 3. Chartjunk patterns

Chart elements that add visual noise without information:

- 3D bar charts, 3D pie charts.
- Drop shadows on bars or points.
- Gradient fills except where a gradient encodes a continuous
  variable.
- Heavy grid lines.
- Cross-hatching for decoration.
- Chart titles duplicating the caption.
- Legend keys with more than six entries (try grouping instead).

Each chartjunk instance is a MINOR or MAJOR finding depending on
severity.

## 4. Overclaim patterns

Overclaims common in draft papers:

- "Our method is state-of-the-art" without qualification. State
  state-of-the-art on which benchmark, under which conditions.
- "Comprehensive experiments" as a contribution. Experiments are
  expected; what was specifically shown?
- "Extensive analysis". Name what the analysis found, not that
  analysis exists.
- "We solve the problem of X". Solving is a strong claim; usually
  the paper improves on X rather than solves.
- "We are the first to". Verify carefully; if the claim is wrong,
  reviewers will find and quote it.

Locate an actual evidence/scope mismatch before flagging an overclaim. Severity
follows its effect on the contribution; a supported strong statement is retained.
Apply claim-preservation when recommending a substantive correction.

## 5. Plagiarism red lines

Never copy sentences from other papers, including the author's
own prior papers without explicit reuse acknowledgement. This
applies to:

- Related Work summaries of prior methods.
- Introduction references to prior work.
- Method descriptions that resemble baseline papers' own
  descriptions.

Plagiarism detection is a CRITICAL finding that blocks submission.
When the paper's Related Work or Introduction paraphrases prior
work too closely, rewrite in the author's own words.

## 6. Detection heuristics

Searches can locate wording for inspection, but cannot assign severity or infer
authorship. Read each hit in context; retain correct terminology and supported
claims. For dashes, flag only uses covered by the author style rule and preserve
its exceptions. Do not flag every superlative or grade by occurrence counts.

Inspect actual rendered figures when available; a description alone cannot
establish a visual defect. Check overclaims against source evidence and scope,
not a list of forbidden phrases. A textual overlap needs source comparison and
context before a plagiarism conclusion; an optional external checker is not a
mandatory call or proof of absence. State inspection limits honestly.
