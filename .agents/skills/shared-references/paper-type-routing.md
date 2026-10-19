# Route by contribution, stage and venue

Local routing policy, added 2026-10-06. Use when choosing a paper structure,
evidence plan or substantive review criteria. It selects applicable checks;
it does not launch another skill, a team, a reviewer/model call or a new phase.
For language-only edits, retain the existing type and meaning without a new audit.

## Establish the route from existing material

Keep three independent dimensions:

- **Contribution type:** what the paper claims readers learn, measure, build or
  reason about. Use the actual question and claims, not its title, presence of
  code, the author's discipline, or availability of favorable results.
- **Stage/task:** proposal, pilot, analyzed results, draft or submission check;
  also distinguish a requested paragraph edit from whole-paper review. A proposal
  needs a credible evidence plan, not fabricated completed experiments.
- **Venue/track/format:** a named conference is not a contribution type. Reuse
  verified current requirements for the selected track and cycle; a local LaTeX
  template's default figures, tables or contribution count are not scientific
  admission criteria. Unknown venue rules remain unverified.

Reuse an existing agreed route. If none exists and the material is sufficient,
infer a provisional route and state it briefly in the existing outline/review
note. Ask only when competing interpretations materially change direction,
scope or cost; use the workspace's existing decision-card rules. Continue any
independent work while a required choice is pending. No new routing file/schema
or approval is required for an ordinary edit.

Mixed papers use a primary type plus only the secondary checks warranted by
specific claims. A benchmark using an off-the-shelf agent does not inherit a
method-novelty requirement. A benchmark claiming a new controller's improvement
also needs appropriate evidence for that improvement. Do not stack every profile.
If none fits, describe the contribution/evidence contract directly rather than
forcing a label. A changed scientific question or contribution is a substantive
revision under [claim-preservation.md](claim-preservation.md), not a cosmetic
reclassification to evade a failed test.

## Calibrate to the selected target

Local author rule, added 2026-10-18. Apply once the author has selected a target
venue/track (not while shortlisting); reuse an existing calibration for that cycle.

1. **Check the target's requirements.** Read the current official CFP/author
   guidelines: scope, track, page limit and exclusions, anonymity, template,
   required statements/artifacts, deadlines with timezone. Record verified facts
   and the check date in the existing outline or plan; unverified items stay pending.
2. **Read what the target has published.** Read recent accepted papers from the
   same venue and track (normally the last one or two cycles) closest to this
   paper's topic and contribution type. Note framing, contribution scale, evidence
   depth (baselines, data, ablations, analysis), structure and figure/table use.
   Confirm venue, year and track against the DBLP TOC (`select-venue` lookup helper)
   or official proceedings; S2/OpenAlex venue fields can mix main, Findings,
   workshop and short papers.
3. **Model on papers one or two tiers above the target.** Choose a few same-topic,
   same-type papers from venues one or two tiers higher (e.g. CCF-A or a leading
   journal for a CCF-B target). Use them as the bar for problem framing, argument,
   evidence completeness, figures and prose. Name the chosen reference venues; tier
   labels follow `select-venue/references/ranking-sources.md`.

For steps 2–3, record and synthesize the papers per
[target-exemplars.md](target-exemplars.md); writing skills reuse an existing
`literature/target_exemplars.md` instead of rereading the papers.

Keep the target's format, page budget and scope. Exemplars set a quality bar; they
do not authorize unplanned experiments or claims beyond the evidence. Route an
evidence gap they expose to [experiment-plan](../experiment-plan/SKILL.md) and a
claim change to [claim-preservation.md](claim-preservation.md). Use `research-lit`
/ `nature-reader` records under [publication-policy.md](publication-policy.md);
do not copy exemplar text or full abstracts into the project.

## Contribution profiles

These are local working categories, not official submission tracks or an
acceptance rubric. Choose checks by the asserted contribution within each row.
Universal integrity and clear claims apply to every profile.

| Type | Evidence and writing focus | Do not impose by default |
|---|---|---|
| Method / algorithm | Define the mechanism and target property; choose relevant comparisons. Use controls or ablations when attributing an effect to a component; use a proof when the claim is formal. | SOTA, a new foundation model, a fixed module/contribution count or a full agent framework. |
| System / engineering | State design constraints and trade-offs; match evaluation to claimed latency, cost, reliability, capability or other outcomes under relevant workloads and resource accounting. | Novelty of every component, a production deployment, or an adversarial threat model not asserted by the work. |
| Evaluation / benchmark / resource | Establish what is measured and why it matters. Check construct validity, relevant coverage, protocols, metric reliability and reuse; data provenance, annotation, leakage and access where the artifact involves them. | A companion method, beating the tested systems, creation of a new dataset for a metric-only paper, or all dataset checks for an audit using existing data. |
| Empirical analysis / failure boundary / negative result | State the question, sampling and controls; separate observation from causal attribution; assess uncertainty and informative alternatives. A negative conclusion needs adequate design sensitivity and implementation checks. | A new method, a positive gain, a surprise result, or mechanism-level causality for a descriptive finding. |
| Replication / reproducibility | Identify the original claim and protocol, departures, faithful implementation and uncertainty; explain what confirmation or disagreement teaches. | A new algorithm, outperforming the original, or treating a non-significant difference as proof of equality. |
| Theory / formal analysis | Make definitions and assumptions explicit; check theorem scope, proof or counterexample validity and consequences. Empirical claims, if present, need their own evidence. | Benchmark gains, real-world deployment, or experiments as a substitute for a missing proof. |
| Survey / synthesis | State scope, search/selection approach appropriate to the claimed coverage, source/version quality and a useful synthesis, taxonomy or unresolved question. Systematic/exhaustive claims require the corresponding transparent method. | A novel algorithm, new experiments, or calling a selective narrative overview an exhaustive systematic review. |
| Position / conceptual argument | State the thesis, reasoning, supporting literature, alternatives and implications. Separate normative proposals from empirical assertions. | Measured gains or a new system merely to look empirical; unsupported factual claims remain unsupported. |

Negative results are also an outcome attribute: a method or replication paper
may contain them without changing type. Preserve the original tested hypothesis,
failed results and post hoc status. An inconclusive/underpowered pilot is not a
demonstrated negative result. A scientifically useful negative contribution may
continue under [topic-selection-policy.md](topic-selection-policy.md); neither a
new label nor a disappointed prediction determines the decision by itself.

## Use existing skills within the requested task

- `tech-paper-template` supplies a method/system or new-problem-with-solution
  scaffold. `benchmark-paper-template` supplies evaluation/resource structure;
  adapt it for metrics or audits without inventing a construction pipeline.
- `good-story` organizes the actual argument for any type. `ts-paper-plan`
  represents it in the selected template when that template fits; adapt optional
  scientific recipes or use an ordinary outline when it does not. Do not reshape
  a contribution merely to satisfy a blueprint linter.
- `intro-drafter` and `paper-writer` draft the chosen argument; `paper-polish`
  preserves its meaning. The six-paragraph method introduction is an optional
  scaffold. `limitation-and-risk-writer` addresses actual claim/design boundaries.
- `experiment-plan` and `analyze-results` handle experimental evidence when
  needed. Theory and survey work need their relevant evidence procedures, not an
  automatic experiment phase. Empirical claims within either still need support.
- `pre-submission-reviewer` and requested `research-review` use the same route.
  A zero-context `paper-claim-audit` infers applicable evidence obligations from
  the paper itself; do not supply author history or prior verdicts to it.

Reuse existing claim/evidence identifiers across these handoffs. An already
adequately addressed concern is not a new reason to shrink the contribution.
These are choices of guidance, not a sequential workflow or mandatory skill list.

## Applicability and conflict handling

This policy governs the applicability of installed scientific checklists and
overrides conflicting generic module, dataset-count, running-example or
contribution-count defaults. Respect explicit user scope, project constraints and
verified venue requirements; keep research integrity intact. A real conflict
between the requested format and a verified venue rule should be surfaced, not
silently resolved by inventing content. Apply selection and claim-preservation
policies to their own decisions; type routing is not a new rejection gate.

For each substantive criticism, identify the affected claim or verified venue
rule, the evidence/missing evidence and its consequence. Mark an inapplicable
check N/A only when explaining its omission is useful; do not print a checklist
of irrelevant requirements. Optional enrichment and style preferences stay
separate from scientific defects. Severity follows the consequence for the claim,
not a count of missing template cells, punctuation marks or fashionable words.
Use the shared [academic prose guidance](../paper-polish/references/ai-tone-guardrails.md)
for wording; no profile mandates automatic keyword weakening.

## Calibration sources

Checked 2026-10-06; recheck the target cycle when making a submission decision.
The profiles above are a local implementation of contribution-sensitive guidance,
not an assertion that every venue accepts every listed type.

- [ARR reviewer guidelines](https://aclrollingreview.org/reviewerguidelines),
  “Adjust your expectations” and H3/H5/H6/H8: assess the actual contribution;
  analysis, replication, negative findings and non-method contributions should
  not inherit a requirement to introduce a new SOTA method.
- [ICML 2026 reviewer instructions](https://icml.cc/Conferences/2026/ReviewerInstructions),
  reading and soundness criteria: inspect proofs, experiments and empirical
  inferences as relevant to the stated claims, and judge issue severity by impact.
- [NeurIPS 2026 E&D reviewer guidelines](https://neurips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines),
  contribution-specific guidance separates benchmarks, metrics, infrastructure,
  audits and data resources while retaining common quality criteria.
