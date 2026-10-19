# Choosing and revising research problems

Use these methods when comparing candidate directions, prioritizing an unresolved
assumption or revisiting a stuck project. Apply the parts that can change the
current decision. The [topic-selection policy](topic-selection-policy.md) owns
contribution criteria and the four continuation decisions.

## Separate scientific value from uncertainty

Explain what would be learned or enabled if the proposed work succeeds, then
assess what must hold for that result to be established. A useful question can
have an uncertain technical route. Compare ways to resolve that uncertainty;
neither ease of execution nor high ambition alone determines priority. When a
negative result could be informative, identify the knowledge it would add.

Use [question value and hypothesis relationships](topic-selection-policy.md#question-value-and-hypothesis-relationships)
when proposing candidate questions or interpreting an unresolved mechanism.
Choose a valuable question before optimizing its supporting experimental package.

## Identify the assumptions that can change the decision

Distinguish assumptions about the phenomenon or proposed mechanism from
assumptions about measurement, implementation and access. For each consequential
unknown, identify its current evidence, what depends on it, the consequence if it
fails, and the earliest credible check with its resource prerequisites. Reuse
existing claim and experiment identifiers. A short list in the current evaluation
is sufficient; do not inventory every conceivable assumption.

Prioritize checks by the decision they can change, unresolved evidence, dependency
order and time/cost to learn. Look for a pivotal uncertainty hidden behind a long
chain of implementation work. Bring its test forward when a valid measurement is
possible; retain necessary readiness checks. Do not replace missing evidence with
invented success probabilities, fixed risk-score cutoffs or assumption counts.
Use [experiment-plan](../experiment-plan/SKILL.md) for the actual protocol.

## Distinguish essential constraints from revisable choices

For a choice that blocks progress, identify why it is fixed: an explicit user
requirement, a condition essential to the scientific question, or a provisional
design choice. Consider whether changing the method, system, measurement or
resource plan could still answer the question. Respect existing authorization
when recommending or making changes.

If the question itself is replaced, apply
[reselection context boundaries](topic-context-policy.md#identify-what-is-being-continued)
to its attached choices. Preserve each choice's source; an earlier agent proposal
or saved plan does not by itself make that choice binding on the replacement.

There is no required number of fixed or flexible parameters. A user budget or
scientifically necessary condition stays binding. Changing an agent-selected
implementation choice can be routine; changing the research question, supported
claim or agreed resource tradeoff follows the existing decision process. A cheaper
or smaller experiment is useful only if its interpretation remains valid.

For example, a study of whether memory reuse transfers across tasks could compare
retrieval strategies while keeping the transfer question fixed. Replacing transfer
evaluation with repeated instances of the same task would change the question.
This is an illustrative comparison, not a recommended research direction.

## Plan branches and revisit them when evidence changes

For the next consequential check, state what different credible outcomes would
change: the claim, technical route, next comparison or investment decision. Reuse
the support, refutation, inconclusive and technical-failure handling in
[experiment-plan](../experiment-plan/SKILL.md#order-and-stopping-decisions).
These branches are conditional proposals, not authorization to run them.

Revisit the relevant branch after informative results, a verified nearby finding,
a changed prerequisite or a persistent implementation obstacle. Ask what has
changed and which options it opens or closes. Use these evidence-triggered reviews
within the existing workflow rather than adding a calendar-driven review cycle.

When a route fails, consider an alternative route to the same question before
proposing a narrower question. If the original objective is no longer justified,
assess any meaningful finding the evidence actually supports and compare the
value of a proposed alternative. A pivot is a candidate change, not an obligation
to rescue every project. Apply [claim preservation](claim-preservation.md).

Unexpected data can motivate a new question. Preserve the original protocol and
identify that question as exploratory; specify any fresh evidence needed before
making confirmatory claims. Do not retroactively rewrite the original hypothesis
or success criterion around the observed result.

## Fit the existing workflow

Keep the selected assumption, revisable choice, conditional next action and reason
in the current evaluation or experiment plan. Use clarification cards only for
consequential choices requiring the user's input under
[research autonomy](research-autonomy.md#human-participation-at-consequential-decisions).
No additional report, subagent, fixed pilot duration or automatic next phase is
introduced. A focused amendment updates only the affected judgments.

## Method sources

Written locally on 2026-10-14, borrowing selected concepts from Anthropic's
[scientific-problem-selection](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection)
in its Apache-2.0 repository: assumption analysis, revisable parameters, decision
trees and problem inversion. Upstream implementation and templates are not copied;
the methods are adapted to this workspace's existing evidence and scope rules.

The underlying published methodological commentary is Michael A. Fischbach,
"Problem choice and decision trees in science and engineering," *Cell* 187,
1828-1833 (2024), [doi:10.1016/j.cell.2024.03.012](https://doi.org/10.1016/j.cell.2024.03.012).
It is a framework for research judgment, not experimental validation of this skill.

Question-framing refinement (2026-10-23): the shared policy adapts value-before-method
reasoning from Anthropic's
[optimization-function guidance](https://github.com/anthropics/knowledge-work-plugins/blob/main/bio-research/skills/scientific-problem-selection/references/03-optimization-function.md),
assumption/value questions from Rimagination's MIT-licensed
[good-question method cards](https://github.com/Rimagination/good-question/tree/main/references),
and hypothesis/claim distinctions from K-Dense's MIT-licensed
[hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/hypothesis-generation).
The latter explicitly allows mixed mechanisms and avoids forced symmetry;
its causal reference distinguishes mediators from effect modifiers. See also
[DoWhy's mediation example](https://www.pywhy.org/dowhy/main/example_notebooks/dowhy_mediation_analysis.html)
for total, direct and indirect effects and identification assumptions.
These are methodological references, not evidence that a skill eliminates ideation
bias. No upstream code or templates are installed; fixed rival counts, reviewer
vetoes, pilot durations and automatic narrowing are not adopted.
