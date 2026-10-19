# Reviewer Mindset Library (Skill Snapshot)

## Table of Contents

- [Cluster 3: Precise Constructive](#cluster-3)
- [Cluster 4: Mild Skeptic](#cluster-4)
- [Cluster 0: Authoritative Negativist](#cluster-0)
- [Cluster 5: Harsh Dismissive](#cluster-5)
- [Cluster 1: Gentle Constructive](#cluster-1)
- [Cluster 2: Concise Affirmative](#cluster-2)

> Auto-generated from `data/behavior/mindset_library.json`.

Model method: `behavior_space_kmeans_llm`; 6 mindset clusters.

---

<a id="cluster-3"></a>

## Cluster 3: Precise Constructive

**Profile:** These reviewers emphasize actionable details and cite specific literature or methods. Criticism is moderate and highly constructive; the source profile describes openness to persuasion and an aim to improve the paper.

| Metric | Value |
|------|-----|
| Sample share | 9.5% (95 reviews) |
| Historical score-increase rate | 36.1% |
| Acceptance rate | 43.2% |
| Successful rebuttal samples | 44 |

### Recognition signals

- Missing parameter sizes, equation forms or implementation steps.
- Specific references or methods exposing conflicts or gaps.
- Concrete requests for clarification or an explicit formulation.

### Rule-statistic differences (Top 3)

- **Explicit revision commitment**: Successful 65.9% vs Unsuccessful 81.8% (Δ -15.9)
- **Direct quotation / point-by-point alignment**: Successful 77.3% vs Unsuccessful 66.7% (Δ +10.6)
- **New experiments/results**: Successful 61.4% vs Unsuccessful 51.5% (Δ +9.9)

### Strategy-vector effects (Cohen's d)

**Higher in the successful group (Cohen's d):**
- `structure_quality`: Successful mean 4.614 / Unsuccessful mean 3.157 (d=1.107)
- `paper_grounding`: Successful mean 4.386 / Unsuccessful mean 2.98 (d=1.074)
- `clarification_quality`: Successful mean 4.636 / Unsuccessful mean 3.235 (d=1.07)

**Higher in the unsuccessful group (risk dimensions):**
- `vague_future_work`: Successful mean 1.386 / Unsuccessful mean 2.333 (d=-0.727)
- `overpromise_risk`: Successful mean 1.295 / Unsuccessful mean 1.745 (d=-0.432)

### Success patterns (LLM-derived)

- Structured, direct responses: number concerns, quote the relevant review and provide specific explanations or evidence.
- Concrete evidence and manuscript grounding: use experiments, figures or quantitative results with precise manuscript locations.
- Confident, restrained tone: stay constructive without defensiveness or overpromising, and identify actual improvements when acknowledging limitations.
- Controlled concessions and commitments: distinguish completed improvements and concrete future directions from vague promises.

### Failure patterns (LLM-derived)

- Vague future-work promises without current action or evidence leave concerns unresolved.
- Overpromising or generalities without concrete plans or support undermine credibility.
- Unstructured long explanations without direct review references make information hard to find.
- Lengthy theory without new evidence or acknowledgment of an actual limitation can evade the central concern.

### Key strategy

Structured direct responses, concrete evidence and a confident, restrained tone.

---

<a id="cluster-4"></a>

## Cluster 4: Mild Skeptic

**Profile:** These reviewers express moderate, vague doubts with limited constructive guidance. They often indicate confusion or surface omissions rather than detailed analysis. The source profile describes a neutral or mildly negative stance, intermediate scores and nonspecific questions.

| Metric | Value |
|------|-----|
| Sample share | 20.5% (205 reviews) |
| Historical score-increase rate | 18.7% |
| Acceptance rate | 47.3% |
| Successful rebuttal samples | 99 |

### Recognition signals

- Openings such as "I am confused" or "If I am understanding correctly".
- Problems identified without concrete revisions or alternatives.
- Short comments with little technical analysis of methods or results.

### Rule-statistic differences (Top 3)

- **Moderate acknowledgment**: Successful 54.5% vs Unsuccessful 66.2% (Δ -11.7)
- **Clarification**: Successful 53.5% vs Unsuccessful 64.6% (Δ -11.1)
- **Explicit revision commitment**: Successful 59.6% vs Unsuccessful 49.2% (Δ +10.4)

### Strategy-vector effects (Cohen's d)

**Higher in the successful group (Cohen's d):**
- `tone_confidence`: Successful mean 4.535 / Unsuccessful mean 3.0 (d=1.246)
- `direct_address`: Successful mean 4.515 / Unsuccessful mean 3.048 (d=1.116)
- `clarification_quality`: Successful mean 4.404 / Unsuccessful mean 2.943 (d=1.148)

**Higher in the unsuccessful group (risk dimensions):**
- `vague_future_work`: Successful mean 1.616 / Unsuccessful mean 2.543 (d=-0.687)
- `overpromise_risk`: Successful mean 1.404 / Unsuccessful mean 2.219 (d=-0.685)

### Success patterns (LLM-derived)

- Confident, direct responses: resolve the doubt without vague language or excessive apologies.
- Clear clarification and manuscript grounding: use specific explanations supported by text, figures, appendices or experiments.
- Controlled concessions and concrete evidence: pair valid limitations with data, analysis or feasible improvements without empty promises.

### Failure patterns (LLM-derived)

- Excessive concessions and vague future work without concrete action weaken the response.
- Lengthy background or clarification can displace the answer and obscure the main concern.
- Clarification without table, appendix or manuscript references remains difficult to verify.

### Key strategy

Answer directly and confidently, anchor the response in manuscript evidence, and keep concessions specific.

---

<a id="cluster-0"></a>

## Cluster 0: Authoritative Negativist

**Profile:** These reviewers are confident and exacting, citing literature or technical details to support negative judgments. Their style is direct, concise and often list-based. They focus on flaws and limitations and the source profile describes low receptiveness to unsupported defenses.

| Metric | Value |
|------|-----|
| Sample share | 20.4% (204 reviews) |
| Historical score-increase rate | 14.7% |
| Acceptance rate | 27.9% |
| Successful rebuttal samples | 62 |

### Recognition signals

- Short criticisms or lists, such as "Unclear text encoder".
- Specific literature or details challenging the contribution, such as "has been studied in [1]".
- Direct challenges to claim strength, such as "claims are too strong".

### Rule-statistic differences (Top 3)

- **Explicit revision commitment**: Successful 51.6% vs Unsuccessful 66.2% (Δ -14.6)
- **Direct quotation / point-by-point alignment**: Successful 72.6% vs Unsuccessful 58.8% (Δ +13.8)
- **New experiments/results**: Successful 46.8% vs Unsuccessful 40.0% (Δ +6.8)

### Strategy-vector effects (Cohen's d)

**Higher in the successful group (Cohen's d):**
- `clarification_quality`: Successful mean 4.419 / Unsuccessful mean 2.794 (d=1.198)
- `direct_address`: Successful mean 4.613 / Unsuccessful mean 3.0 (d=1.112)
- `tone_confidence`: Successful mean 4.452 / Unsuccessful mean 2.858 (d=1.177)

**Higher in the unsuccessful group (risk dimensions):**
- `vague_future_work`: Successful mean 1.419 / Unsuccessful mean 2.603 (d=-0.801)
- `overpromise_risk`: Successful mean 1.323 / Unsuccessful mean 2.333 (d=-0.767)

### Success patterns (LLM-derived)

- Confident, direct responses: address the exact criticism without evasive wording.
- Substantive clarification and manuscript grounding: connect explanations to original text, theory or additional experiments.
- Controlled concessions and concrete evidence: acknowledge justified points while supporting the contribution with experiments, theory or new evidence.

### Failure patterns (LLM-derived)

- Vague future work or exaggerated commitments without current evidence or a concrete plan evade the problem.
- Dismissive or defensive replies such as "the bug does not affect results" or "we do not target SOTA" need serious explanation and evidence.
- Weak novelty defenses that merely assert difference without comparisons fail to establish the contribution.

### Key strategy

Answer directly and confidently with manuscript support and concrete evidence; avoid vague promises.

---

<a id="cluster-5"></a>

## Cluster 5: Harsh Dismissive

**Profile:** These reviewers give severe negative judgments with few actionable suggestions. The source profile describes low receptiveness to persuasion. They emphasize perceived writing, motivation or method flaws with relatively few concrete references, in a concise and negative style.

| Metric | Value |
|------|-----|
| Sample share | 9.8% (98 reviews) |
| Historical score-increase rate | 13.8% |
| Acceptance rate | 27.6% |
| Successful rebuttal samples | 30 |

### Recognition signals

- Strong negative terms such as "not well-written", "misleading" or "limited".
- Criticism without a concrete improvement path.
- Concise, direct statements or lists.

### Rule-statistic differences (Top 3)

- **New experiments/results**: Successful 60.0% vs Unsuccessful 34.3% (Δ +25.7)
- **Explicit revision commitment**: Successful 43.3% vs Unsuccessful 60.0% (Δ -16.7)
- **Clarification**: Successful 63.3% vs Unsuccessful 77.1% (Δ -13.8)

### Strategy-vector effects (Cohen's d)

**Higher in the successful group (Cohen's d):**
- `direct_address`: Successful mean 4.5 / Unsuccessful mean 2.691 (d=1.241)
- `tone_confidence`: Successful mean 4.4 / Unsuccessful mean 2.603 (d=1.307)
- `clarification_quality`: Successful mean 4.333 / Unsuccessful mean 2.588 (d=1.212)

**Higher in the unsuccessful group (risk dimensions):**
- `vague_future_work`: Successful mean 1.433 / Unsuccessful mean 2.574 (d=-0.721)
- `overpromise_risk`: Successful mean 1.533 / Unsuccessful mean 2.309 (d=-0.551)

### Success patterns (LLM-derived)

- Confident, direct responses: confront the central criticism and demonstrate understanding.
- Concrete evidence: provide experiments, quantitative results or specific data rather than explanation or promises alone.
- Clear structure: use headings or lists and precise clarification for every criticism.
- Controlled concessions: acknowledge valid weaknesses while explaining retained contributions or actual improvements.

### Failure patterns (LLM-derived)

- Vague future-work promises do not provide the requested present evidence.
- Overpromising capabilities or unrealistic outcomes increases distrust.
- Excessive concessions and unjustified changes to terminology or positioning weaken the contribution.

### Key strategy

Answer directly and confidently, replacing vague promises with concrete evidence.

---

<a id="cluster-1"></a>

## Cluster 1: Gentle Constructive

**Profile:** These reviewers aim to help improve the paper with mild, specific questions and actionable suggestions. The source profile describes low severity and openness to persuasion, attention to contributions and baselines, and constructive questions about details.

| Metric | Value |
|------|-----|
| Sample share | 34.5% (345 reviews) |
| Historical score-increase rate | 13.4% |
| Acceptance rate | 50.4% |
| Successful rebuttal samples | 177 |

### Recognition signals

- Mild questions such as "It would be helpful if..." or "Is this still true...".
- Clear Strengths and Questions sections with a positive opening.
- Specific requests for tasks or analyses rather than generic criticism.

### Rule-statistic differences (Top 3)

- **New experiments/results**: Successful 56.5% vs Unsuccessful 46.6% (Δ +9.9)
- **Clarification**: Successful 60.5% vs Unsuccessful 68.6% (Δ -8.1)
- **Moderate acknowledgment**: Successful 54.2% vs Unsuccessful 61.0% (Δ -6.8)

### Strategy-vector effects (Cohen's d)

**Higher in the successful group (Cohen's d):**
- `tone_confidence`: Successful mean 4.593 / Unsuccessful mean 3.398 (d=1.036)
- `direct_address`: Successful mean 4.689 / Unsuccessful mean 3.512 (d=0.985)
- `clarification_quality`: Successful mean 4.492 / Unsuccessful mean 3.349 (d=0.963)

**Higher in the unsuccessful group (risk dimensions):**
- `overpromise_risk`: Successful mean 1.35 / Unsuccessful mean 2.018 (d=-0.637)
- `vague_future_work`: Successful mean 1.542 / Unsuccessful mean 2.157 (d=-0.51)

### Success patterns (LLM-derived)

- Confident, direct responses: answer each specific question without ambiguity, evasion or excessive apology.
- Concrete evidence: use experiments, quantitative results, data or precise manuscript references.
- Controlled concessions: acknowledge justified points while explaining the position, contribution or existing support.
- Clear, structured clarification: organize replies with headings, numbering or paragraphs and refer to relevant tables or sections.

### Failure patterns (LLM-derived)

- Overpromising future work or unverified improvements without a concrete action plan creates doubt.
- Vague plans such as "will be explored" do not address the central concern.
- Hesitant or apologetic defenses without direct explanations obscure the answer and can weaken confidence.

### Key strategy

Answer directly and confidently with concrete evidence; avoid empty promises.

---

<a id="cluster-2"></a>

## Cluster 2: Concise Affirmative

**Profile:** These reviewers offer brief, general positive feedback with few details or actionable suggestions. The source profile suggests they may consider the paper adequate or have invested little in review, producing broad comments rather than detailed criticism.

| Metric | Value |
|------|-----|
| Sample share | 5.3% (53 reviews) |
| Historical score-increase rate | None% |
| Acceptance rate | 52.8% |
| Successful rebuttal samples | 27 |

### Recognition signals

- Very short comments, often one or two sentences.
- General positive words such as "rigorous", "strong" or "good" without concrete support.
- Few specific issues or improvement suggestions.

### Rule-statistic differences (Top 3)

- **New experiments/results**: Successful 48.1% vs Unsuccessful 65.0% (Δ -16.9)
- **Clarification**: Successful 59.3% vs Unsuccessful 75.0% (Δ -15.7)
- **Explicit revision commitment**: Successful 74.1% vs Unsuccessful 60.0% (Δ +14.1)

### Strategy-vector effects (Cohen's d)

**Higher in the successful group (Cohen's d):**
- `tone_confidence`: Successful mean 4.731 / Unsuccessful mean 3.44 (d=1.136)
- `clarification_quality`: Successful mean 4.654 / Unsuccessful mean 3.48 (d=1.043)
- `direct_address`: Successful mean 4.808 / Unsuccessful mean 3.64 (d=1.008)

**Higher in the unsuccessful group (risk dimensions):**
- `overpromise_risk`: Successful mean 1.154 / Unsuccessful mean 1.6 (d=-0.646)
- `vague_future_work`: Successful mean 1.423 / Unsuccessful mean 1.64 (d=-0.24)

### Success patterns (LLM-derived)

- Confident, direct responses: answer each question clearly without defensive language.
- High-quality clarification: support explanations with manuscript content or literature, not only additional experiments.
- Controlled concessions: identify actual improvements or concrete plans while retaining the core contribution.
- Manuscript grounding: refer to precise sections, figures or revision locations.
- Structured replies: use numbering or paragraphs so each response is traceable.

### Failure patterns (LLM-derived)

- Overpromising future code or extensive experiments without current evidence distracts from the concern.
- Vague future work defers the key question instead of addressing it.
- Untargeted new experiments add volume without resolving the central issue.
- Defensive argument over terminology or definitions can displace substantive answers.

### Key strategy

Answer directly and confidently with clear explanation and controlled concessions; avoid overpromising.

---
