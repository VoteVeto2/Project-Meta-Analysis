# Peer Review: "More Agents, Better Results? A Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems"

**Reviewer:** Prof. Dr. habil. Dietrich Schmidt-Hoffmann, Ludwig-Maximilians-Universitat Munchen
**Manuscript:** Yang (2026), submitted for G0B75a Meta-Analysis, KU Leuven
**Date of review:** 22 May 2026

---

## 1. Summary

Yang (2026) presents a random-effects meta-analysis of 41 within-study comparisons examining whether multi-agent LLM orchestration (debate, hierarchy, cooperation, etc.) outperforms single-agent baselines on benchmark accuracy. Using log odds ratios as the effect metric and a REML estimator, the paper reports a pooled LOR of 0.44 (95% CI [0.26, 0.63]), with extreme heterogeneity (reported I^2 = 97.5%), a prediction interval crossing zero, and subgroup analyses suggesting that code-generation tasks and hierarchical architectures drive the effect. The paper claims the advantage attenuates by approximately 30% under compute parity (k = 9). The paper is ambitious in scope, covers a timely topic, and attempts many of the right analyses. However, as detailed below, there are serious computational errors in the Q statistic and I^2, methodological gaps in the treatment of sampling variances and confidence/prediction intervals, and the data extraction contains irregularities that undermine confidence in the reported numbers.

---

## 2. Recommendation

**Major revision.**

---

## 3. Strengths

**S1. Timely and well-motivated research question (Section 1).** The four research questions are clearly stated, the PICOS framework is properly specified (Section 2.2), and the introduction correctly identifies the tension between the multi-agent enthusiasm and the compute-confound critique. The paper addresses a genuine gap: no prior meta-analysis synthesizes these findings.

**S2. Prediction interval reported and foregrounded (Section 3.3, Table 2, highlight box).** The authors deserve credit for reporting and emphasizing the prediction interval, following IntHout et al. (2016). The highlight box in Section 3.3 correctly notes that the pooled mean is "nearly meaningless as a point prediction" given the heterogeneity. This is exactly the kind of honest interpretive framing that is too rare in student work.

**S3. Compute-parity sensitivity analysis (Section 3.9, Table 7).** The k = 9 compute-parity subset is the most substantively important analysis in the paper. The 30% attenuation from LOR = 0.44 to 0.30 is a genuine contribution. The paper correctly identifies uncontrolled compute as the field's dominant methodological weakness.

**S4. Multi-method publication bias assessment (Section 3.8, Table 6).** Deploying Egger's test, Begg's test, trim-and-fill, and p-curve in parallel is thorough and appropriate for k = 41.

**S5. Transparent AI-use declaration (Appendix B).** The declaration is unusually detailed and honest for student work, correctly identifying AI assistance at each stage.

---

## 4. Critical Issues

### C1. Cochran's Q statistic is computed incorrectly (Section 3.3, Table 2; `pooling.py` lines 47-48)

The `pool()` function computes Q as:

```
q = sum((1/vi) * (yi - mu)^2)
```

where `mu` is the **random-effects** pooled estimate (i.e., computed with weights `1/(vi + tau2)`). This is wrong. Cochran's Q must be computed using fixed-effect weights **and** the fixed-effect mean (Cochran, 1954; Borenstein et al., 2009, Ch. 16). Specifically:

```
Q = sum(wi_FE * (yi - mu_FE)^2), where wi_FE = 1/vi
```

Using the random-effects mean with fixed-effect weights inflates Q because the RE mean differs from the FE mean. My recomputation yields Q = 1013.93, not the reported 1624.69. While still highly significant, this is a 60% overestimate. I^2 correspondingly drops from the reported 97.5% to approximately 96.1%. The DerSimonian-Laird Q (reported as 1494.92) is similarly affected, since `pool()` is called for both estimators.

**Fix:** Compute Q using fixed-effect weights and fixed-effect mu exclusively, as in Equation 16.3 of Borenstein et al. (2009). The `dl_estimate()` function already does this correctly internally (line 33) but `pool()` recomputes Q incorrectly.

### C2. Confidence and prediction intervals use z = 1.96 instead of the Knapp-Hartung t-distribution adjustment (`pooling.py` lines 43-44, 51-52)

Both the 95% CI and 95% PI are constructed using z = 1.96. For the confidence interval, the Hartung-Knapp-Sidik-Jonkman (HKSJ) adjustment (Hartung & Knapp, 2001; IntHout et al., 2014) is now standard practice and recommended by Cochrane. It replaces z with t(k-2) and uses a corrected variance estimator. At k = 41, t(39, 0.975) = 2.023, which modestly widens the CI. For the prediction interval, IntHout et al. (2016) explicitly specify t(k-2), not z. The correct PI formula is:

```
mu +/- t(k-2, 0.975) * sqrt(tau2 + se_mu^2)
```

With t = 2.023 instead of z = 1.96, the PI widens slightly (roughly [-0.71, 1.60] versus the reported [-0.68, 1.57]). This does not change the qualitative conclusion but is a methodological error.

**Fix:** Implement the HKSJ adjustment for CIs and use t(k-2) for PIs throughout, as recommended by IntHout et al. (2014) and Viechtbauer (2010, `metafor` default behavior with `test="knha"`).

### C3. Unconditional continuity correction applied to all 41 studies (Section 2.3; `effect_sizes.py` lines 9-12)

The 0.5 Haldane-Anscombe continuity correction is applied to every study unconditionally (`a = n_ma + cc` for all rows). Inspection of the data confirms that **no study has a zero cell** -- all n-correct-ma, n-correct-sa, n-items-minus-n-correct values are positive. Applying the correction when it is unnecessary introduces systematic bias toward zero (Sweeting et al., 2004; Bradburn et al., 2007). With n-items values as low as 20 (S023, Ferber2025) and 65 (S039, Zhou2025), the distortion from adding 0.5 to cells with small counts is non-trivial.

**Fix:** Apply the continuity correction only to studies with zero cells (i.e., conditionally). Since no study here has zero cells, remove the correction entirely. If the authors wish to maintain a uniform approach, they should use the treatment-arm continuity correction of Sweeting et al. (2004) rather than the constant 0.5.

### C4. Fabricated or estimated n-items values undermine effect-size validity (data: S032, S034, S036, S038)

Four studies (S032 Cui2025, S034 Tian2026, S036 Li2026, S038 Liu2026) all have n-items = 5000, despite covering different combinations of benchmarks ("8 benchmarks," "MATH," "13 datasets," "MATH500/AMC23/AIME24/AIME25 avg"). The value 5000 is suspiciously round and appears to be an estimate or imputation rather than an exact count. The paper acknowledges in Section 4.5 that "n-items counts were sometimes estimated from reported percentages and total benchmark sizes, introducing measurement error," but does not flag which studies are affected or quantify the impact.

Similarly, S018 (MedARC2025) reports n-items = 1273 for PubMedQA, but PubMedQA has 1000 items in its standard test set, not 1273. The value 1273 is the size of MedQA (used in S014, S015, S017), suggesting a data-entry error.

**Fix:** (a) Flag every study where n-items was estimated rather than directly extracted. (b) Conduct a sensitivity analysis excluding estimated-n-items studies. (c) Correct S018 if the n-items value is wrong. (d) Report the exact provenance of each n-items value in an appendix.

### C5. Meta-regression is unconditional and uses the wrong tau-squared (`moderators.py` lines 41, 82)

The meta-regression (Section 3.7, Table 5) computes tau2 using the unconditional REML estimator (line 41: `tau2 = reml_estimate(yi, vi)`, without the design matrix X). This means the regression weights `W = diag(1/(vi + tau2))` do not account for variance explained by the moderators. In a proper mixed-effects meta-regression, tau2_residual should be estimated iteratively conditional on X (Viechtbauer, 2010; Raudenbush, 2009). Furthermore, the R^2 computation at line 82 compares tau2 to `reml_estimate(yi, vi)`, which is the same unconditional tau2, yielding R^2 = 0 by construction.

The reported claim that "residual tau^2 remained at 0.32, essentially unchanged" (Section 3.7) is therefore tautological -- the code guarantees this result regardless of the data.

**Fix:** Implement iterative REML estimation of tau2 conditional on the moderator matrix X, as in Viechtbauer (2005, 2010). Compute R^2 as 1 - tau2_residual / tau2_unconditional. Alternatively, use `metafor::rma()` in R or `statsmodels` with proper mixed-effects specification.

### C6. No Knapp-Hartung adjustment for meta-regression inference (`moderators.py` lines 68-70)

The meta-regression uses z-tests (normal distribution) for moderator significance. Hartung and Knapp (2001) and Viechtbauer et al. (2015) have shown that z-tests in meta-regression are anti-conservative, particularly at small k. With k = 41 and 8 parameters (intercept + 8 moderator coefficients), the effective degrees of freedom are low. The Knapp-Hartung adjustment replaces z with t(k - p) and inflates the variance estimate, producing more honest p-values.

Although all moderators are non-significant (p > .30), the z-test issue is a methodological deficiency that would matter if any moderator were marginal. The omnibus test of moderators (QM) is also not reported.

**Fix:** Apply the Knapp-Hartung adjustment to all meta-regression inference. Report the omnibus QM test for the set of moderators. Reference Hartung and Knapp (2001) and IntHout et al. (2014).

### C7. Dependency among effect sizes is not modeled (Section 4.5)

The paper acknowledges this limitation ("we did not model dependency among multiple effect sizes extracted from the same paper") and states it was "partially addressed by including at most one comparison per study." However, the data contradicts this claim in spirit: several studies use the same benchmark (six studies use HumanEval with identical n-items = 164), the same backbone model (multiple GPT-4 studies), and some benchmark/model combinations are nearly identical across nominally different papers. While the studies are technically independent publications, they share common variance through the benchmark and model, violating the independence assumption.

More critically, studies that aggregate across multiple benchmarks (S015: "avg 9 datasets"; S032: "8 benchmarks"; S036: "13 datasets") introduce within-study correlation that the current model ignores. The correct approach for such studies is to extract separate effect sizes per benchmark and use robust variance estimation (RVE; Hedges et al., 2010) or multilevel meta-analysis (Van den Noortgate et al., 2013).

**Fix:** At minimum, conduct a sensitivity analysis removing studies with aggregated benchmarks. Ideally, implement RVE via `robumeta` or the `clubSandwich` package (Pustejovsky & Tipton, 2022) to account for correlated effect sizes.

### C8. The frontier-model paradox (RQ3) is not testable with the available data (Section 3.7, Section 4.1)

RQ3 asks whether the multi-agent advantage shrinks as baseline models strengthen. The meta-regression tests this with "year" as a proxy for model capability, yielding a null result (beta = -0.03, p = .881). The paper correctly notes this may reflect the narrow 2023-2026 window and confounding of year with model capability (Section 3.7). However, this goes further than underpowered: the proxy is fundamentally invalid. Year is a poor measure of model strength because (a) multiple model generations coexist in the same year, (b) the backbone models in the sample range from GPT-3.5-Turbo to GPT-5 and Gemini 2.5 Pro, spanning several capability generations within overlapping time periods, and (c) the bubble plot (Figure 6) uses baseline SA accuracy as the x-axis, which would be the correct predictor, yet this variable is not included in the meta-regression.

**Fix:** Replace "year" with baseline single-agent accuracy (SA proportion correct) as the moderator for RQ3. This directly measures what the frontier-paradox hypothesis predicts: as the SA baseline improves, the marginal gain from multi-agent should shrink. If baseline accuracy data are available (they are, from n-correct-sa/n-items), this is a straightforward addition.

### C9. Subgroup analyses lack multiplicity correction and some subgroups are too small (Tables 3-4)

Six task-category subgroups and five architecture subgroups are tested without any multiplicity correction (Bonferroni, FDR, or analogous). With 11 subgroup tests, the family-wise error rate under nominal alpha = .05 exceeds 0.43. Furthermore, several subgroups contain only k = 2 studies (role-play, verifier-critic) or k = 3 (evaluation, general knowledge). Random-effects estimates from k = 2 are essentially uninterpretable: tau2 cannot be meaningfully estimated, and the CI is determined almost entirely by the prior (Borenstein et al., 2009, Ch. 17). The verifier-critic subgroup (k = 2, LOR = 1.00, CI [-0.44, 2.44], I^2 = 97.6%) is a striking example: an I^2 of 97.6% from two studies has no meaningful interpretation.

**Fix:** (a) Collapse subgroups with k < 5 into an "other" category or report them descriptively without pooling. (b) Apply a correction for multiple comparisons, or at minimum label the subgroup analyses as exploratory with an explicit caveat. (c) Report prediction intervals for each subgroup, not just CIs.

### C10. The between-group Q-test in subgroup analysis is non-standard (`moderators.py` lines 22-29)

The between-group Q-test is computed by treating each subgroup's pooled estimate as a single observation, weighting by the inverse of its squared standard error, and computing a chi-squared statistic. This is a simplification. The standard between-group Q-test (Borenstein et al., 2009, Ch. 19) partitions the total Q into Q-within and Q-between, where Q-between = Q-total - sum(Q-within). The simplified approach in the code yields an approximation but not the exact statistic, and its properties are less well understood. Furthermore, the between-group Q-test result is not reported anywhere in the paper -- it is computed but apparently discarded.

**Fix:** Report the between-group Q-test explicitly (statistic, df, p-value) for both task-category and architecture subgroups. Use the partition-of-Q approach per Borenstein et al. (2009, Eq. 19.1-19.6).

### C11. Leave-one-out analysis uses fixed tau-squared (`heterogeneity.py` lines 49-62; `sensitivity.py` lines 9-12)

The leave-one-out analysis (used in sensitivity, Section 3.9) holds tau2 constant at the full-sample estimate and only recomputes the weighted mean. This is incorrect: removing a study changes the data, so tau2 should be re-estimated for each leave-one-out iteration. With I^2 > 96%, the tau2 estimate is heavily influenced by outliers (e.g., S039 with LOR = -2.25), and holding it fixed masks the sensitivity of the variance component to individual studies.

**Fix:** Re-estimate tau2 (via REML) within each leave-one-out iteration. Report both the leave-one-out pooled estimate and the leave-one-out tau2 to assess which studies drive heterogeneity versus which drive the point estimate.

### C12. Convenience-sample limitations are disclosed but insufficiently weighted (Section 4.5)

The paper lists "convenience-sample meta-analysis, not a registered systematic review" as its first limitation. However, the limitation is then quickly set aside, and the conclusion (Section 5) makes unqualified claims such as "multi-agent LLM orchestration confers a real but unstable advantage." A convenience sample of 41 studies from an initial pool of 153 records, with 65 excluded for lacking extractable data, raises severe selection concerns. The 65 excluded studies are not randomly missing: studies reporting accuracy counts are likely those with cleaner experimental designs and larger effects. This is a form of availability bias distinct from publication bias (which the Egger test assesses).

Moreover, 29 of 41 studies (71%) have audit status "unaudited," meaning their extracted data have not been independently verified. Only 6 are "verified" and 6 are "verified-corrected" (the latter implying the initial extraction was wrong). If 50% of audited studies required correction (6/12), the expected error rate in the 29 unaudited studies is substantial.

**Fix:** (a) State explicitly in the abstract and conclusion that this is an exploratory convenience-sample analysis, not a systematic review. (b) Report a sensitivity analysis restricted to the 12 verified/verified-corrected studies. (c) Quantify the direction and magnitude of corrections in the verified-corrected studies to estimate potential bias in unaudited studies.

---

## 5. Minor Issues

### M1. Inconsistent effect-size labeling

The abstract and text refer to "LOR" throughout, but the standard abbreviation in meta-analytic literature is "logOR" or "ln(OR)." Some tables use "LOR" while the formulas use natural log without specifying the base. Standardize notation and define the abbreviation on first use.

### M2. Table 2 REML vs. DL Q-values differ when they should not

Cochran's Q is a property of the data, not the estimator. Q should be identical for REML and DL rows. The reported values (1624.7 vs. 1494.9) differ because both are computed incorrectly in `pool()` using different mu values. This discrepancy should have been a red flag during quality control.

### M3. Reference list has incomplete entries

Chen et al. (2025) and Xiong et al. (2024) have placeholder URLs ("https://arxiv.org/" with no paper ID). Lu et al. (2024) is cited as the "Chameleon" paper about compositional reasoning, but the citation in Section 1 discusses single-agent sampling scaling, which is a different paper. Verify all references point to the correct publications.

### M4. No GRADE or equivalent quality-of-evidence assessment

While the RoB assessment is study-level (appropriate), the paper does not provide an overall quality-of-evidence assessment (e.g., GRADE framework; Guyatt et al., 2011) for its main conclusions. Given that 61% of studies are high-RoB and 71% are unaudited, the overall certainty of evidence should be rated explicitly.

### M5. Figure captions lack statistical detail

Forest plot (Figure 2) and subgroup plots (Figures 4-5) do not report the between-study heterogeneity metrics (tau, prediction intervals) within the figures themselves. The Baujat plot (Figure 3) does not label individual studies, making it impossible for the reader to identify the influential outliers without cross-referencing the data.

### M6. The p-curve analysis reports 93% right-skewed but the JSON shows 92.9%

The paper rounds 92.86% (26/28) to 93%, which is acceptable, but the denominator (28 significant results out of 41) is not reported in the text. The reader cannot evaluate whether the p-curve had adequate power. Report n-significant and n-total alongside the proportion.

### M7. Cohen's h is computed but never reported

The source code (`effect_sizes.py`) computes Cohen's h as an alternative effect size, but it appears nowhere in the paper. Either report it as a sensitivity check or remove it from the code to avoid confusion about which metric was primary.

---

## 6. Statistical Orthodoxy Audit

| Criterion | Status | Notes |
|---|---|---|
| **REML used?** | Yes | REML is the primary estimator with DL as sensitivity check. Correct. |
| **Prediction interval reported?** | Yes | Reported in Table 2 and prominently highlighted. However, the formula uses z = 1.96 instead of t(k-2) per IntHout et al. (2016). See C2. |
| **Funnel plot only if k >= 10?** | Yes | k = 41. Per Sterne et al. (2011), the threshold of k >= 10 is met. Acceptable. |
| **RoB graded study-by-study?** | Yes | Each study graded on four domains plus overall, per adapted ROB 2.0. However, no study achieves "low" overall risk. The RoB assessment does not drive any analytic decisions (e.g., no downweighting of high-RoB studies, no stratified analysis by RoB level beyond the sensitivity in Table 7). |
| **Statistical vs. clinical heterogeneity distinguished?** | Partially | The paper discusses task-category and architecture moderators (clinical heterogeneity) alongside I^2 and tau (statistical heterogeneity), but does not explicitly label or distinguish these two concepts. The text in Section 3.4 conflates "the distribution of true effects is wide and multi-modal" (a statistical claim) with implicit causal claims about task and architecture moderators. |
| **CI and PI clearly distinguished?** | Yes | Table 2 reports both, and the highlight box explains the distinction. This is done well. |
| **Continuity correction appropriate?** | No | Applied unconditionally to all studies despite no zero cells. See C3. |
| **Q-test correctly computed?** | No | Q is computed with FE weights but RE mean, inflating the statistic by ~60%. See C1. The Q values also differ between REML and DL rows, which is impossible for a correctly computed Q. |

---

## 7. Reproducibility Score

**Score: 6/10**

**Justification:** The project provides a full code pipeline (Python modules in `src/`, notebook, `pyproject.toml`, `uv.lock`), seeded random operations, and exported data files -- all positive. However: (a) 71% of extracted data are unaudited, and 50% of audited studies required correction, raising serious concerns about data fidelity; (b) the Q statistic is computed incorrectly, meaning the reported I^2 and heterogeneity tests cannot be reproduced from correct formulas; (c) the meta-regression tau2 is unconditional, so the R^2 = 0 result is an artifact; (d) n-items values for at least 4 studies appear to be round-number estimates rather than exact counts; (e) the notebook path is referenced (`notebook/meta-analysis-v1.ipynb`) but the notebook is not included in the files available for review. Reproducibility of the pipeline is plausible in principle but the underlying data quality is insufficient for confident replication.

---

## 8. Verdict

A promising first attempt at a genuinely needed meta-analysis, undermined by a computational error in the Q statistic that inflates the headline heterogeneity metric, an unconditional continuity correction that biases all 41 effect sizes, a meta-regression that cannot by construction detect moderator effects, and data-quality concerns (71% unaudited, suspicious n-items values) that together mandate major revision before any of the quantitative claims can be trusted.
