# peer-review comments on your meta-analysis report

- Author: GPT5.5-pro

**Decision: Major revisions.**
Not “reject,” because this is an intro meta-analysis course project and you are already unusually honest about limitations. But right now the report is over-engineered, under-audited, and too confident in places where the data pipeline cannot support the statistical polish.

The brutal summary: **your statistics look more sophisticated than your data deserve.** The project can still be saved, but only by simplifying the claims, auditing the extraction table, fixing source/citation errors, and making the report less performative.

---

## What I could and could not verify

I reviewed the uploaded file `report-v5-cn.html`. The upload contains only the rendered HTML. It does **not** contain the claimed reproducibility materials: no `main.py`, no `src/`, no `data/`, no `pyproject.toml`, no `uv.lock`, and no `report/assets/` image files. Therefore I could not run the actual meta-analysis code.

I did run basic internal consistency checks from the HTML tables. The reported percentages such as 25/41 = 61%, 31/41 = 76%, and 6/12 = 50% are internally consistent. The reported Egger p-value is also consistent with `t(39)=2.34`, giving about p = .0245. But the actual pooled effects, subgroup effects, and sensitivity analyses cannot be reproduced without the study-level dataset.

I also checked the reference-list sources online. Most method references exist and are real. Several LLM paper citations are real, but at least two are cited sloppily, and one source is misused in the argument.

---

# Major problems

## 1. The report claims reproducibility, but the submitted artifact is not reproducible

Appendix A says the full workflow can be run with:

```bash
uv sync && uv run python main.py
```

But the uploaded artifact contains no code or data. That makes the reproducibility section look like window dressing. Worse, the HTML references figures such as `assets/prisma-flow.png`, `assets/forest-plot.png`, and `assets/funnel-plot.png`, but those assets are not present in the upload. So the rendered report is not self-contained.

**Reviewer comment:** Do not claim “完整的分析流程” unless the reader can actually run it. For a course project, this is easy to fix: submit a ZIP or GitHub repo with `data/`, `src/`, `main.py`, `pyproject.toml`, `uv.lock`, and `report/assets/`. If that is not possible, delete the strong reproducibility claim and say: “Code and data are maintained separately and were not included in this HTML export.”

---

## 2. The most important data are missing: the 41 included studies are not shown

This is the biggest weakness. You say you included **41 study-level comparisons**, but the report does not give a proper extraction table with:

| study ID | paper | benchmark | MA accuracy | SA accuracy | denominator | exact/estimated denominator | metric type | compute-equivalent? | risk of bias | verified? | source page/table |
| -------- | ----- | --------: | ----------: | ----------: | ----------: | --------------------------- | ----------- | ------------------- | ------------ | --------- | ----------------- |

Without that table, the reader cannot audit your actual meta-analysis. This is especially damaging because the report admits that only 10/41 rows were verified and that 6/12 audited rows required correction. That is not a footnote; that is the main threat to the whole project.

**Reviewer comment:** You cannot bury a 50% extraction correction rate and then present a polished REML-HKSJ model as if the input data are stable. The model is not the problem. The spreadsheet is the problem.

**Practical fix:** Add a compact Appendix Table A1 with all 41 rows. Even if ugly, it will save the project.

---

## 3. Your subgroup tables do not add up to k = 41

This is an embarrassing but very fixable error.

In Section 3.2, task categories are reported as:

* code generation k = 11
* other/mixed k = 10
* medical reasoning k = 7
* math k = 6
* evaluation k = 3
* general knowledge k = 3
* factuality verification k = 1

These sum to **41**.

But Table 3 omits factuality verification and sums to **40**.

Architecture categories in Section 3.2 are:

* debate k = 20
* cooperation k = 9
* hierarchy k = 6
* verification-critique k = 2
* role-playing k = 2
* hybrid k = 1
* planning-execution k = 1

These sum to **41**.

But Table 4 omits hybrid and planning-execution, summing to **39**.

**Reviewer comment:** This makes the subgroup analysis look untrustworthy. If you omit singleton categories, say so explicitly and do not pretend the subgroup analysis covers all studies.

**Practical fix:** Merge rare groups into “Other/rare architecture” and “Other/rare task” so the subgroup tables sum to 41. Or write: “Subgroup tests exclude singleton categories; therefore k = 40 / k = 39.” But the cleaner course-project fix is to merge rare categories.

---

## 4. The source use is uneven; one key skeptical citation is misused

Your report uses Sprague et al. as if it supports the claim that multi-agent advantages fade when compute is equalized. But the verified paper is **“To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning.”** Its abstract says it is about chain-of-thought prompting across many papers and datasets, not a multi-agent debate compute-parity study. It may be relevant to inference-time computation generally, but it does **not** directly support the multi-agent claim as written. ([arXiv][1])

Zhang et al. 2025 is the better skeptical source. Its abstract says multi-agent debate often fails to outperform simple single-agent baselines such as CoT and self-consistency, even while consuming more inference-time computation. That supports your skeptical paragraph, but not necessarily the exact stronger wording “under equal token budget” unless you can point to a specific table/result in the paper. ([arXiv][2])

**Reviewer comment:** Replace the Sprague-based claim. Use Sprague only for a general statement about inference-time reasoning costs, or remove it. Use Zhang 2025 for the multi-agent debate critique.

---

## 5. Some citations have author-list errors

The paper entries exist, but your reference formatting is sloppy in ways that make the literature review look AI-generated.

For **MetaGPT**, the current arXiv page lists the authors as Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. Your reference ends with “& Wu, Y.”, which does not match the current arXiv metadata. ([arXiv][3])

For **ChatDev**, the official ACL/arXiv metadata show the final author as Maosong Sun; your truncated reference ending with “& Liu, Z.” is misleading if you are using an APA-style ellipsis. ([arXiv][4])

**Reviewer comment:** These are small mistakes, but they damage credibility because the report is already defending itself against AI-assisted extraction errors. Fix the bibliography.

---

## 6. The report overuses advanced meta-analysis language for a convenience sample

You repeatedly use formal language: PRISMA, GRADE, ROB 2.0, HKSJ, REML, Q partitioning, p-curve, Egger, trim-and-fill, prediction intervals, meta-regression. Some of that is fine. But the study is openly a convenience sample, not a registered systematic review.

**Reviewer comment:** The report is trying to sound like a journal article while admitting that the data were found by six AI agents, only partly audited, and not independently screened. That combination is awkward.

For a course project, this should be framed as:

> “Exploratory rapid meta-analysis / course project using a convenience sample.”

Do not let the statistical machinery outrun the sampling design.

---

## 7. The effect-size model is probably too clean for the actual data

You treat benchmark outcomes as binomial counts and compute log odds ratios. That is defensible as a simplification, but it is not innocent.

Many included results are likely based on the **same benchmark items** evaluated under two conditions. That creates paired/dependent data. A standard two-independent-binomial log-OR assumes the MA and SA counts are independent, which is probably false. Without item-level joint counts, you cannot properly model paired correctness.

You also combine accuracy, pass@1, win rate, execution score, and solving rate. These are not the same measurement model. A win rate from pairwise evaluation is not the same as item-level accuracy.

**Reviewer comment:** You acknowledge metric heterogeneity, but then proceed as if acknowledging it solves it. It does not.

**Practical fix:** Make **raw percentage-point difference** the main effect for interpretability, and keep log-OR as a secondary analysis. For an intro course, this is simpler and more honest.

---

## 8. The subgroup p-values are not worth the space

The task subgroup test is reported as `Q_between(5)=197.56, p<.001`, and the architecture subgroup test as `Q_between(4)=32.75, p<.001`. But the subgroups are confounded by task, architecture, model family, year, compute budget, and data quality. Also, some groups have k = 2 or k = 3.

**Reviewer comment:** A significant subgroup Q here mostly says “the dataset is a mess,” not “task category causally moderates the effect.”

**Practical fix:** Keep the subgroup tables as descriptive. Remove or downplay the p-values. Write: “These subgroup patterns are exploratory and should not be interpreted causally.”

---

## 9. P-curve should probably be removed

P-curve assumes a set of interpretable, independent, comparable significance tests. Your inputs are heterogeneous, partly dependent, partly estimated, and not from a registered literature search.

**Reviewer comment:** P-curve is not adding credibility here. It looks like statistical ornamentation.

**Practical fix:** Delete the p-curve row. Keep Egger/Begg/trim-and-fill as exploratory publication-bias checks, and add one sentence saying they are unreliable under extreme heterogeneity. Egger’s original paper is about detecting funnel-plot asymmetry, but it does not magically diagnose publication bias when heterogeneity and small-study effects are tangled. ([BMJ][5])

---

## 10. GRADE / ROB 2 language is too formal for this design

ROB 2 is a tool for randomized trials; your objects are computational benchmark papers. The BMJ article on RoB 2 describes it as a revised tool for assessing risk of bias in randomized trials. ([BMJ][6])

Your adaptation is reasonable for a class project, but do not present it as if it were a validated risk-of-bias instrument for LLM benchmark studies.

**Practical fix:** Rename it:

> “Informal risk-of-bias assessment adapted from ROB 2 concepts.”

Similarly, rename GRADE to:

> “Informal certainty assessment.”

That avoids sounding overconfident.

---

# Source audit

## Mostly verified and usable

The following core LLM papers exist and broadly support their basic descriptive use:

| Source                                        | Status   | Comment                                                                                                 |
| --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------- |
| Du et al. 2023, multiagent debate             | Verified | Supports claim that multi-agent debate improved factuality/reasoning in their experiments. ([arXiv][7]) |
| Liang et al. 2024, divergent thinking via MAD | Verified | Supports the divergent-thinking / debate framing. ([arXiv][8])                                          |
| AutoGen / Wu et al. 2023                      | Verified | Supports multi-agent conversation framework claim. ([arXiv][9])                                         |
| MetaGPT / Hong et al.                         | Verified | Supports multi-agent collaborative framework claim, but fix author list. ([arXiv][3])                   |
| ChatDev / Qian et al.                         | Verified | Supports communicative agents for software development; fix bibliography final author. ([arXiv][4])     |
| MedAgents / Tang et al.                       | Verified | Supports multi-agent medical reasoning claim. ([arXiv][10])                                             |
| CodeAgent / Zhang K. et al.                   | Verified | Supports code-generation/tool-agent claim. ([arXiv][11])                                                |
| Zhang H. et al. 2025                          | Verified | Strong skeptical source for multi-agent debate evaluation; use this more carefully. ([arXiv][2])        |

## Problematic or needs correction

| Source                        | Problem                                                                                                                   | Fix                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Sprague et al. 2024/2025      | Real paper, but about chain-of-thought, not directly multi-agent compute parity.                                          | Remove from multi-agent compute-parity argument or rewrite as a broader inference-cost citation. ([arXiv][1])                               |
| MetaGPT citation              | Author list appears wrong in your bibliography.                                                                           | Use current arXiv metadata or a stable conference citation. ([arXiv][3])                                                                    |
| ChatDev citation              | Truncated author list ends with wrong final author.                                                                       | End with Maosong Sun if using ellipsis style. ([ACL Anthology][12])                                                                         |
| “Currently no meta-analysis…” | Hard to prove. I found surveys and benchmarks, but not a directly comparable quantitative meta-analysis in a quick check. | Soften to “To our knowledge…” and describe the search as non-exhaustive. Multi-agent LLM surveys/benchmarks do exist. ([Springer Link][13]) |

## Methods references

The main method references are real and mostly appropriate: Begg rank correlation, Duval–Tweedie trim-and-fill, Egger funnel asymmetry, HKSJ/mKH, prediction intervals, robust variance estimation, three-level meta-analysis, and `metafor` are all traceable. For example, IntHout et al. support HKSJ over DL in many random-effects settings, Röver et al. discuss modified HKSJ for few studies, and Viechtbauer’s `metafor` paper is correctly cited. ([DOI][14])

---

# Section-by-section harsh comments

## Abstract

The abstract is too crowded. It tries to report every caveat, every statistic, and every subgroup result. For a course project, the reader needs the core message:

1. k = 41 convenience-sample comparisons.
2. Average log-OR positive.
3. Absolute gain tiny.
4. Heterogeneity extreme.
5. Compute-equivalent subset much weaker.
6. Data verification weak.

Cut the subgroup Q statistics from the abstract. They are not worth abstract space.

Suggested replacement:

> “This exploratory convenience-sample meta-analysis found a positive average association favoring multi-agent systems, but the absolute gain was small and the evidence was fragile. The main result was log-OR = 0.45, but Cohen’s h was only 0.08, heterogeneity was extreme, and the compute-equivalent subset showed only a negligible effect. Because most rows were not independently verified and most studies did not control compute, the findings should be treated as hypothesis-generating.”

That is cleaner and more defensible.

---

## Introduction

The introduction is mostly fine, but the skeptical paragraph has a citation problem. Replace the Sprague claim with Zhang 2025. Do not imply Sprague is a multi-agent paper.

Also, the phrase “目前尚无元分析” should become:

> “据我们有限检索所知，目前尚未发现直接比较多智能体与单智能体LLM系统的定量元分析。”

That is safer.

---

## Methods

The methods section is honest, but it still overstates the rigor.

The six-agent search strategy is interesting, but it is not equivalent to a systematic database search. The reader needs exact search dates, exact databases, exact strings, deduplication rules, and the final included-study list.

The PICOS criteria are good, but you should add one missing criterion:

> “Only studies reporting comparable MA and SA outcomes on the same benchmark, using the same or clearly comparable backbone model, were eligible.”

The effect-size section should explicitly say:

> “Because item-level paired correctness was unavailable, MA and SA proportions were treated as independent binomial counts. This likely underestimates uncertainty.”

That one sentence will prevent a reviewer from attacking you too hard.

---

## Results

The pooled result is okay as a descriptive average. But the interpretation should center absolute gains, not odds ratios. OR = 1.57 sounds much more impressive than “3–5 percentage points” or `h = 0.08`.

Your best result is actually the skeptical one:

> Under compute equivalence, the effect shrinks and is practically negligible.

That is the most interesting and honest finding. Put it earlier and make it central.

The subgroup results should be demoted. They are descriptive patterns, not reliable moderator evidence.

---

## Discussion

The discussion is one of the stronger parts because it is appropriately skeptical. But it still tries to preserve too much. You do not need to defend every analysis. Say plainly:

> “The main limitation is not the random-effects model; it is the quality and auditability of the extraction table.”

That is the truth.

---

## Conclusion

The conclusion is too long but directionally right. It should end with a modest course-project conclusion:

> “This project does not establish that multi-agent LLM systems generally outperform single-agent baselines. It suggests a small positive average effect in the current convenience sample, but the evidence is highly uncertain. The most practical takeaway is that multi-agent systems should be compared against compute-matched single-agent baselines before claiming synergy.”

That is defensible.

---

# Practical changes to save the project

## Minimum viable rescue

Do these simple things. Do not add more fancy statistics.

### 1. Add the 41-row extraction table

This is the single most important fix. Include columns for:

* study ID
* citation
* benchmark
* task category
* architecture category
* MA accuracy / correct count
* SA accuracy / correct count
* denominator
* whether denominator is exact or estimated
* whether compute-equivalent
* whether verified
* source location

Even if the table is ugly, it makes the project auditable.

### 2. Make the verified subset the credibility anchor

Right now “only verified studies k = 10” is buried in sensitivity analysis. Make it a key result:

> “The verified subset gave log-OR = 0.35, lower than the full sample.”

That is important and honest.

### 3. Fix subgroup counts

Either include all categories or merge rare categories:

Task categories:

* Code
* Medical
* Math
* General/evaluation
* Other/mixed/rare

Architecture categories:

* Debate
* Cooperation
* Hierarchical
* Other/rare

Make each table sum to 41.

### 4. Remove p-curve

It is not helping you. Keep Egger/Begg/trim-and-fill as exploratory diagnostics only.

### 5. Move meta-regression to appendix

The meta-regression has R² = 0% and no significant moderators. It is not central. In the main text, one sentence is enough:

> “Exploratory meta-regression did not identify reliable moderators.”

### 6. Put risk difference first

For an intro meta-analysis course, this is clearer:

> “Multi-agent systems improved performance by approximately 3–5 percentage points in the full sample and around 2 percentage points under compute equivalence.”

Then give log-OR as the formal effect size.

### 7. Fix the references

At minimum:

* Correct MetaGPT author list.
* Correct ChatDev final author.
* Remove or reframe Sprague.
* Add stable ACL Anthology citations for ChatDev and CodeAgent if you cite them as ACL 2024 papers. ([ACL Anthology][15])

### 8. Tone down PRISMA/GRADE/ROB language

Use:

* “PRISMA-style flow”
* “informal risk-of-bias assessment”
* “informal certainty assessment”
* “exploratory convenience-sample meta-analysis”

This is still respectable and much less vulnerable.

---

# Suggested revised title

Your current title is good rhetorically, but I would make the subtitle more honest:

> **更多智能体，更好结果？多智能体与单智能体LLM系统的探索性便利样本元分析**

Or in English:

> **More Agents, Better Results? An Exploratory Convenience-Sample Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems**

The phrase “便利样本” protects you.

---

# Suggested revised core conclusion

You can paste something like this into the final section:

> 本探索性便利样本元分析发现，多智能体LLM系统相对于单智能体基准线存在一个正向但很小的平均效应。全样本合并效应为 log-OR = 0.45，但绝对效应约为3–5个百分点，Cohen’s h = 0.08，异质性极高，且预测区间跨越零点。更重要的是，在计算资源相对公平的研究中，效应进一步缩小至实践意义很弱的水平。由于多数研究未控制推理计算量，多数提取行尚未独立核实，并且存在发表偏倚/小研究效应信号，本项目不能证明多智能体系统普遍优于单智能体系统。较稳妥的结论是：多智能体协同可能在可分解、可验证、且计算预算充足的任务中有价值，但任何实际部署前都应与计算匹配的单智能体基准线进行比较。

This is honest, simple, and hard to attack.

---

# Final harsh verdict

The project is **salvageable**, but only if you stop trying to impress with advanced meta-analysis machinery and instead make the data extraction transparent. The current version’s biggest flaw is not HKSJ, REML, Egger, or GRADE. The biggest flaw is that the reader cannot see or audit the 41 rows that generate every result.

For an intro course, the safest winning strategy is:

**show the 41-row table, fix the citations, simplify the analyses, foreground absolute effects, and call the whole thing exploratory.**

[1]: https://arxiv.org/abs/2409.12183 "[2409.12183] To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning"
[2]: https://arxiv.org/abs/2502.08788 "[2502.08788] Stop Overvaluing Multi-Agent Debate -- We Must Rethink Evaluation and Embrace Model Heterogeneity"
[3]: https://arxiv.org/abs/2308.00352 "[2308.00352] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"
[4]: https://arxiv.org/abs/2307.07924 "[2307.07924] ChatDev: Communicative Agents for Software Development"
[5]: https://www.bmj.com/content/315/7109/629?utm_source=chatgpt.com "Bias in meta-analysis detected by a simple, graphical test - The BMJ"
[6]: https://www.bmj.com/content/366/bmj.l4898?utm_source=chatgpt.com "RoB 2: a revised tool for assessing risk of bias in randomised trials"
[7]: https://arxiv.org/abs/2305.14325 "[2305.14325] Improving Factuality and Reasoning in Language Models through Multiagent Debate"
[8]: https://arxiv.org/abs/2305.19118 "[2305.19118] Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate"
[9]: https://arxiv.org/abs/2308.08155 "[2308.08155] AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
[10]: https://arxiv.org/abs/2311.10537 "[2311.10537] MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning"
[11]: https://arxiv.org/abs/2401.07339 "[2401.07339] CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges"
[12]: https://aclanthology.org/2024.acl-long.810.bib?utm_source=chatgpt.com "ACL Anthology"
[13]: https://link.springer.com/article/10.1007/s44336-024-00009-2?utm_source=chatgpt.com "A survey on LLM-based multi-agent systems: workflow ... - Springer"
[14]: https://doi.org/10.1186/1471-2288-14-25 "The Hartung-Knapp-Sidik-Jonkman method for random effects meta-analysis is straightforward and considerably outperforms the standard DerSimonian-Laird method | BMC Medical Research Methodology | Springer Nature Link"
[15]: https://aclanthology.org/2024.acl-long.737/?utm_source=chatgpt.com "CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems ..."
