---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 46 items, 3 important content pieces were selected

---

**Technology News**
1. [Persona prompts shift LLM clinical thresholds 9.5 points in simulation](#item-tech-news-1) ⭐️ 8.0/10
2. [Deep learning and multitask models fail to beat tree ensembles for student early warning](#item-tech-news-2) ⭐️ 7.0/10
3. [Study clusters 102,684 Ash chatbot users into five engagement phenotypes](#item-tech-news-3) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Persona prompts shift LLM clinical thresholds 9.5 points in simulation](https://www.nature.com/articles/s44401-026-00121-z) ⭐️ 8.0/10

A peer-reviewed study in Nature Psychology reports that decision-style system prompts shifted large language models’ clinical action thresholds in a large simulation where the clinical facts were held constant. Researchers defined nine physician personas by crossing duty-based, care-based, and utilitarian ethical orientations with intuitive, integrative, and analytic cognitive styles, then tested 20 open-weight LLMs on 2,500 emergency-department vignettes and 2,500 MIMIC-IV-Note discharge summaries across five binary decision areas: safety, autonomy, treatment, resource use, and follow-up. Baseline affirmative responses were 42.8%; persona prompts moved them from 36.9% to 46.4%, a 9.5-percentage-point swing across 5,000,000 decisions with ten repeats per condition. The largest shifts appeared in autonomy and treatment; effects showed 85.7% directional agreement across corpora \(r = 0.82 for effect sizes\), while model susceptibility ranged from 4.9 to 16.1 points, with no consistent protection from medical fine-tuning or model size.

rss · Nature Psychology · Nov 14, 00:00

**「Background」** Existing clinical AI guidance has treated model behavior mainly as a control problem—managed through access limits, monitoring, documentation, and human oversight—even as evidence showed that instructions and framing can systematically change LLM outputs. The study isolates that effect at the action-threshold level by holding clinical facts fixed and varying only the decision-style prompt. The authors describe the personas as observable output patterns, not as intentions, beliefs, or psychological dispositions.

**「Impact」** Teams deploying clinical LLMs should treat persona and system-prompt selection as a governed deployment setting rather than a communication layer, because fixed clinical evidence can yield different action recommendations. Selecting a medically fine-tuned or larger model was not a consistent safeguard in this evaluation. The study measured simulated decisions only; it did not establish patient outcomes or a clinical harm rate.

**Tags**: `#large language models`, `#clinical AI`, `#AI safety`, `#prompt engineering`, `#healthcare`

---

<a id="item-tech-news-2"></a>
### [Deep learning and multitask models fail to beat tree ensembles for student early warning](https://www.nature.com/articles/s41598-026-80425-0) ⭐️ 7.0/10

A peer-reviewed study in Scientific Reports finds that temporal deep learning and multi-task learning give no accuracy advantage over well-tuned gradient-boosted trees for early-warning prediction of pass/fail and withdrawal. Using 14-day virtual learning environment \(VLE\) interaction sequences from the first weeks of enrollment for 22,848 Open University students, the authors compared single-task and multi-task BiLSTM architectures, a GRU variant, and four tabular baselines across 10 runs, evaluating differences with equivalence testing; all eight models fell within a narrow F1 band of 0.574–0.583. Multi-task sharing conferred no benefit despite moderate task correlation \(r = 0.589\), and the null result held under student-level bootstrap resampling and after excluding withdrawn students. The authors present this as a boundary condition: when the predictive signal in early click logs is limited, added model capacity and task correlation do not translate into accuracy, and predictive information was governed chiefly by cumulative and rolling engagement features.

rss · Nature Psychology · Nov 14, 00:00

**「Why tree ensembles are the benchmark to beat」** Gradient-boosted trees and random forests are established strong baselines for tabular prediction: a 2022 NeurIPS Datasets and Benchmarks benchmark of standard and novel deep learning methods against XGBoost and Random Forest across many tabular tasks found tree-based models consistently ahead, even after extensive hyperparameter tuning \(arXiv:2207.08815\). That finding frames the comparison in this study, where recurrent sequence models fed 14-day VLE click logs are tested against tuned gradient-boosted trees on the same student-level data.

**「Impact」** For learning-analytics teams building early-warning systems, the result supports starting with well-tuned gradient-boosted trees on interpretable engagement features rather than investing in recurrent or multi-task architectures, since the authors attribute the predictive signal mainly to cumulative and rolling engagement measures. The scope is 14-day early click-log data from a single institution, so the study does not establish that deep sequence models fail when richer or longer interaction signals are available.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2207.08815">[2207.08815] Why do tree -based models still outperform deep ...</a></li>
<li><a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/0378c7692da36807bdec87ab043cdadc-Abstract-Datasets_and_Benchmarks.html">Why do tree -based models still outperform deep learning on typical...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#deep learning`, `#gradient-boosted trees`, `#multi-task learning`, `#learning analytics`

---

<a id="item-tech-news-3"></a>
### [Study clusters 102,684 Ash chatbot users into five engagement phenotypes](https://www.nature.com/articles/s41598-026-78802-w) ⭐️ 6.0/10

A study in Scientific Reports used k-means clustering over eight behavioral features to sort 102,684 users of Ash, a purpose-built AI mental health chatbot, into five engagement phenotypes: Early Dropouts \(52.2%\), Weekly Users \(25.3%\), Concentrated Users \(16.8%\), Intensive Users \(4.1%\), and Power Users \(1.6%\). In small baseline-to-three-week subsamples, the study reported pre-post improvements in depression \(PHQ-9, n = 298; d = -0.51\), anxiety \(GAD-7, n = 298; d = -0.57\), and social support \(MSPSS, n = 194; d = 0.22\). A dose-response gradient in depression improvement was replicated using model-predicted PHQ-9 scores in a larger sample \(n = 23,813\), with the largest improvements among Power Users \(d = -0.57\) and Intensive Users \(d = -0.50\) and the smallest among Early Dropouts \(d = -0.22\). The authors caution that the uncontrolled pre-post design cannot establish causality, and that the findings require confirmation in controlled studies.

rss · Nature Psychology · Nov 15, 00:00

**「Background」** Ash is a purpose-built mental health chatbot from Slingshot AI, a research lab developing a foundation model for psychology; the company markets Ash as a private, therapist-like space for stress, anxiety, and relationships rather than a general-purpose assistant. The study analyzes naturalistic usage patterns among Ash users, not a generic chatbot or a controlled trial.

**「Impact」** For developers and researchers building conversational mental health tools, the results caution against treating raw session counts as a primary engagement or benefit metric: frequency, intensity, and the concentrated-use pattern were distinct, and different clinical outcomes were associated with different dimensions of use. The uncontrolled design means the reported effect sizes should not be read as evidence that the chatbot caused clinical improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://www.talktoash.com/">Ash - AI for Mental Health</a></li>
<li><a href="https://slingshotai.com/">Slingshot AI</a></li>
<li><a href="https://www.techbrew.com/stories/2025/07/31/slingshot-ai-therapy-chatbot-a16z">Slingshot AI &#x27;s Ash wants to be your therapist</a></li>

</ul>
</details>

**Tags**: `#AI mental health`, `#conversational agents`, `#user engagement`, `#clinical outcomes`, `#observational study`

---