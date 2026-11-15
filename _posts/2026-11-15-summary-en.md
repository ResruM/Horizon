---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 146 items, 3 important content pieces were selected

---

**Technology News**
1. [Persona prompts shift clinical action thresholds in 20 open-weight LLMs](#item-tech-news-1) ⭐️ 8.0/10
2. [Ash study finds five engagement patterns among 102,684 AI mental health users](#item-tech-news-2) ⭐️ 7.0/10
3. [Source transparency and accuracy warnings cut wrong-answer acceptance](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Persona prompts shift clinical action thresholds in 20 open-weight LLMs](https://www.nature.com/articles/s44401-026-00121-z) ⭐️ 8.0/10

A large-scale evaluation found that decision-style system prompts reliably shift clinical action thresholds in large language models even when the clinical facts are held fixed. The study crossed three ethical orientations with three cognitive styles to define nine physician personas and tested 20 open-weight LLMs on 2,500 simulated emergency-department vignettes and 2,500 MIMIC-IV-Note discharge summaries, asking five binary decision questions ten times per condition for 5,000,000 total decisions. Under baseline prompting, models answered “Yes” to 42.8% of decisions; persona prompts shifted affirmative rates from 36.9% to 46.4%, a 9.5-percentage-point swing. Effects were largest for autonomy and treatment, showed 85.7% directional agreement across corpora, and varied by model from 4.9 to 16.1 points, with no consistent protection from medical fine-tuning or model size.

rss · Nature Psychology · Nov 14, 00:00

**「Background」** Clinical LLM guidance has largely framed deployment risk as a control problem—access limits, monitoring, and human review—while evidence has shown that model outputs can shift systematically with context and framing. The study builds on that by treating decision-style system prompts as an experimental variable rather than a mere communication layer, holding the clinical facts constant.

**「Impact」** For clinical LLM deployments, the results imply that persona or system-prompt choices must be treated as a governed configuration with measured effects: the same clinical evidence produced affirmative rates spanning 9.5 percentage points, and model susceptibility ranged from 4.9 to 16.1 points, so teams should test and document prompt-specific thresholds rather than assume medical fine-tuning or larger models reduce the shift.

**Tags**: `#clinical LLMs`, `#AI safety`, `#prompt engineering`, `#model evaluation`, `#healthcare AI`

---

<a id="item-tech-news-2"></a>
### [Ash study finds five engagement patterns among 102,684 AI mental health users](https://www.nature.com/articles/s41598-026-78802-w) ⭐️ 7.0/10

An observational study of 102,684 users of Ash, a purpose-built AI mental health chatbot, applied k-means clustering to eight behavioral features and identified five engagement phenotypes: Early Dropouts \(52.2%\), Weekly Users \(25.3%\), Concentrated Users \(16.8%\), Intensive Users \(4.1%\), and Power Users \(1.6%\); 66.9% had at least one session between 9pm and 5am. In subsamples assessed at baseline and three weeks, the study reported pre-post improvements in depression \(PHQ-9, n=298; d=-0.51\), anxiety \(GAD-7, n=298; d=-0.57\), and social support \(MSPSS, n=194; d=0.22\), while 11,437 users completed a baseline Working Alliance Inventory. A depression dose-response gradient—largest for Power \(d=-0.57\) and Intensive \(d=-0.50\) users and smallest for Early Dropouts \(d=-0.22\)—was replicated in a model-predicted PHQ-9 sample of 23,813. The authors describe the evidence as naturalistic and correlational and caution against using session counts as a primary engagement metric, pending controlled designs.

rss · Nature Psychology · Nov 15, 00:00

**「Background」** Ash is the flagship mental health chatbot from Slingshot AI, which describes itself as a mental health research lab building a foundation model for psychology and markets Ash as an AI designed for mental health support. The study evaluates that purpose-built product rather than a general-purpose chatbot, and the paper discloses that four authors are employees of the company building the model.

**「Impact」** For developers and researchers evaluating AI mental health tools, the results indicate that a single session-count metric would obscure distinct use patterns and outcome-specific associations; engagement should be measured across behavioral dimensions, and claims of clinical benefit should be framed as awaiting controlled confirmation.

<details><summary>References</summary>
<ul>
<li><a href="https://slingshotai.com/">Slingshot AI</a></li>
<li><a href="https://www.talktoash.com/">Ash - AI for Mental Health</a></li>

</ul>
</details>

**Tags**: `#AI mental health`, `#chatbot engagement`, `#clinical outcomes`, `#digital health`, `#clustering`

---

<a id="item-tech-news-3"></a>
### [Source transparency and accuracy warnings cut wrong-answer acceptance](https://www.nature.com/articles/s41598-026-80733-5) ⭐️ 7.0/10

In a randomized online experiment, 800 adults evaluating 24 AI-style answers each \(19,200 trials\) accepted incorrect answers less often when the interface showed source information, an accuracy warning, or both. Acceptance of incorrect answers fell from 45% in the control condition to 36% with source information only, 28% with a warning only, and 21% with both; verification behavior was highest with both cues \(52%\). Participants accepted correct answers more often than incorrect ones, and that correct-versus-incorrect gap was largest in the source-plus-warning condition. The authors characterize the setting as low-risk factual information evaluation and flag the distinction between response bias and sensitivity as a boundary condition.

rss · Nature Psychology · Nov 14, 00:00

**「Background」** The experiment addresses trust calibration in human–AI interaction: ideally, users accept correct AI answers and reject incorrect ones rather than uniformly trusting or distrusting the system. It also separates overall acceptance, or response bias, from sensitivity to whether an answer is actually correct—a distinction the authors identify as an important boundary condition.

**「Impact」** For AI interface designers, the evidence supports testing source transparency and accuracy warnings together, since the combined condition produced the lowest incorrect-answer acceptance and highest verification rate. The study does not establish that users became better at discriminating correct from incorrect answers—the authors note the response-bias versus sensitivity issue—and its low-risk tasks limit generalization to higher-stakes use.

**Tags**: `#generative AI`, `#human-AI interaction`, `#trust calibration`, `#source transparency`, `#randomized experiment`

---