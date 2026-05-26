# Point-by-Point Response to Peer Review (v1)

**Manuscript:** "More Agents, Better Results? A Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems"
**Author:** Xinyu Yang, KU Leuven
**Reviewer:** Prof. Dr. habil. Dietrich Schmidt-Hoffmann, LMU Munich
**Date of response:** 22 May 2026

---

We thank the reviewer for the thorough and constructive evaluation. The review identified genuine computational errors, methodological gaps, and data-quality concerns that have materially improved the analysis. Below we address each issue in turn.

---

## Critical Issues

### C1. Cochran's Q statistic computed incorrectly

**Accepted.**

The reviewer is correct that `pool()` computed Q using fixed-effect weights but the random-effects pooled mean, violating Borenstein et al. (2009, Eq. 16.3). We fixed `pool()` in `pooling.py` to compute Q using both fixed-effect weights and the fixed-effect mean:

```
Q = sum(w_FE * (yi - mu_FE)^2),  where w_FE = 1/vi, mu_FE = sum(w_FE * yi) / sum(w_FE)
```

The corrected Q = 1016.6 (previously 1624.7), and I^2 drops from 97.5% to 96.1%. Q is now identical across the REML and DL rows, as it must be. All downstream statistics (I^2, H^2, heterogeneity tests) have been updated accordingly.

### C2. CI/PI use z instead of t

**Accepted.**

Both the confidence interval and prediction interval now use t(k-2) via `scipy.stats.t.ppf` instead of z = 1.96. At k = 41, t(39, 0.975) = 2.023. The CI widens modestly and the PI shifts from [-0.68, 1.57] to approximately [-0.71, 1.60]. The qualitative conclusions are unchanged, but the intervals are now methodologically correct per IntHout et al. (2014, 2016) and consistent with `metafor` default behavior under `test="knha"`.

### C3. Unconditional continuity correction

**Accepted.**

The reviewer correctly identifies that the 0.5 Haldane-Anscombe correction was applied to all 41 studies regardless of whether any cell was zero. `effect_sizes.py` now applies cc = 0.5 only when a zero cell exists. Since no study in our dataset has zero cells, no correction is applied, eliminating the systematic bias toward zero noted by Sweeting et al. (2004). All effect sizes and variances have been recomputed without the correction.

### C4. Suspicious n-items values

**Partial.**

We accept the specific data-entry error and address flagging, but cannot fully verify all n-items from abstracts alone.

*Accepted components:*
- S018 (MedARC2025): n-items corrected from 1273 to 1000 (the standard PubMedQA test set size). The value 1273 was indeed a copy error from MedQA.
- A new `n-items-estimated` flag column has been added to the dataset, marking the four studies (S032, S034, S036, S038) whose n-items = 5000 are rounded estimates from aggregated benchmarks.
- A sensitivity analysis excluding estimated-n-items studies is now reported. Results remain consistent with the full sample.

*Not fully resolved:*
- For multi-benchmark studies, exact item counts per benchmark are not always recoverable from the published papers. We acknowledge this limitation explicitly in the revised manuscript and report the provenance of each n-items value in the data appendix.

### C5. Meta-regression unconditional tau-squared

**Accepted.**

The reviewer is correct that the meta-regression used unconditional tau^2, making R^2 = 0 by construction. `moderators.py` now estimates tau^2 conditional on the design matrix X via `reml_estimate(yi, vi, X=X)`, using iterative REML estimation as described in Viechtbauer (2005, 2010). R^2 is now computed as:

```
R^2 = 1 - tau^2_conditional / tau^2_unconditional
```

This yields a meaningful (non-tautological) estimate of variance explained by the moderators.

### C6. No Knapp-Hartung adjustment for meta-regression

**Accepted.**

Meta-regression inference now uses the Knapp-Hartung adjustment: z-tests are replaced with t-tests using df = k - p, and the variance estimate is inflated by the Knapp-Hartung scaling factor s^2_KH. The omnibus test of moderators (QM) is now reported alongside individual coefficient tests. While all moderators remain non-significant under the corrected inference, the methodology is now consistent with current best practice per Hartung and Knapp (2001) and Viechtbauer et al. (2015).

### C7. Dependency among effect sizes

**Partial.**

We accept that dependency is a genuine concern and have added a targeted sensitivity analysis. Robust variance estimation (RVE) was not implemented due to scope constraints.

*Accepted components:*
- A sensitivity analysis excluding studies with aggregated benchmarks (S015, S032, S034, S036, S038) is now reported. The reduced sample (k = 36) yields LOR = 0.48 [0.24, 0.72], consistent with the full-sample estimate.

*Not implemented:*
- Full RVE via `robumeta` or `clubSandwich` is beyond the scope of this project given the Python stack and course timeline. We acknowledge this as a limitation and note that shared benchmarks (e.g., six studies using HumanEval) introduce correlated sampling error that the current independence assumption does not capture.

### C8. Frontier-paradox moderator

**Accepted.**

The reviewer's critique is well-taken: year is a fundamentally invalid proxy for model capability. We replaced year with single-agent accuracy (sa-accuracy = n-correct-sa / n-items) as the direct moderator for RQ3 in the meta-regression, as the reviewer suggested. This variable directly measures what the frontier-paradox hypothesis predicts. The result: beta = -0.77, t = -1.38, p = .176 -- the direction is consistent with the paradox (higher SA accuracy associated with smaller multi-agent advantage), but the effect is not significant at alpha = .05. This is now reported as suggestive but inconclusive evidence, consistent with the limited power at k = 41.

### C9. Small subgroups and multiplicity

**Partial.**

We accept the concern about small subgroups and have added interpretive caveats. We do not apply Bonferroni correction.

*Accepted components:*
- Subgroups with k < 5 (role-play k = 2, verifier-critic k = 2, evaluation k = 3, general-knowledge k = 3) are now explicitly labeled as "exploratory -- interpret with caution" in the text and tables. These subgroups are retained descriptively but their pooled estimates are not used to support any substantive claim.

*Rejected component (multiplicity correction):*
- We do not apply Bonferroni correction because the subgroup analyses are explicitly framed as exploratory throughout, following Borenstein et al. (2009, Ch. 19), who caution against mechanical multiplicity correction in meta-analysis when tests are pre-planned and the goal is hypothesis generation rather than confirmatory inference. We have added an explicit statement noting the inflated family-wise error rate under nominal alpha = .05 across 11 tests, so readers can calibrate accordingly.

### C10. Between-group Q-test

**Accepted.**

The between-group Q-test has been reimplemented using the partition-of-Q approach per Borenstein et al. (2009, Eq. 19.1-19.6):

```
Q_between = Q_total - sum(Q_within)
```

Results are now explicitly reported (statistic, df, p-value) for both task-category and architecture subgroup analyses, which were previously computed but not included in the manuscript.

### C11. Leave-one-out analysis uses fixed tau-squared

**Accepted.**

`leave_one_out()` in `heterogeneity.py` now re-estimates tau^2 via REML for each leave-one-out iteration. The output reports both the leave-one-out pooled estimate and the leave-one-out tau^2, enabling identification of studies that drive heterogeneity (tau^2 sensitivity) versus those that drive the point estimate (mean sensitivity). This is particularly informative for outliers such as S039 (LOR = -2.25), where removal substantially reduces tau^2.

### C12. Convenience-sample disclosure

**Accepted.**

The abstract and conclusion now explicitly state "exploratory convenience-sample meta-analysis" rather than making unqualified claims. Additionally, a sensitivity analysis restricted to the 12 verified/verified-corrected studies is now reported: k = 12 yields LOR = 0.45 [0.26, 0.64], which is reassuringly consistent with the full-sample estimate of LOR = 0.44. The direction and magnitude of corrections in the six verified-corrected studies are documented in the data appendix.

---

## Minor Issues

### M1. Inconsistent effect-size labeling

**Accepted.** Notation has been standardized to "log-OR" throughout the manuscript, with the abbreviation defined on first use in the abstract and Section 2.3. All tables, figures, and in-text references now use this consistent label.

### M2. REML vs. DL Q-values differ

**Accepted.** This discrepancy was a direct consequence of the error identified in C1. With the corrected Q computation (fixed-effect weights and fixed-effect mean), Q is now identical for both the REML and DL rows, as expected.

### M3. Incomplete reference entries

**Accepted.** All references have been verified and corrected. Placeholder URLs for Chen et al. (2025) and Xiong et al. (2024) have been replaced with correct arXiv identifiers. The Lu et al. (2024) citation has been corrected to point to the intended publication.

### M4. No GRADE assessment

**Partial.** A qualitative GRADE-style assessment has been added for the main conclusion (overall certainty rated as "low" given high risk of bias, serious inconsistency, and convenience sampling). A full formal GRADE assessment across all outcomes is not feasible within the scope of this course project, and we note this as a limitation.

### M5. Figure captions lack statistical detail

**Accepted.** Forest plot and subgroup plot captions now include tau, tau^2, and prediction intervals. The Baujat plot labels individual study identifiers for the most influential points.

### M6. p-curve denominator not reported

**Accepted.** The text now reports n-significant = 26 and n-total = 41 alongside the 93% right-skewed proportion, allowing readers to evaluate p-curve power.

### M7. Cohen's h computed but not reported

**Accepted.** Cohen's h is now reported as a secondary effect size in a supplementary table, providing a scale-free complement to the log-OR. This allows readers to gauge effect magnitude on the arcsine-difference scale.

---

## Summary of Changes

| Issue | Decision | Key change |
|---|---|---|
| C1 | Accepted | Q recomputed with FE weights and FE mean; Q = 1016.6, I^2 = 96.1% |
| C2 | Accepted | CI and PI use t(k-2) = 2.023 |
| C3 | Accepted | Continuity correction conditional on zero cells; none applied |
| C4 | Partial | S018 corrected; n-items-estimated flag added; sensitivity reported |
| C5 | Accepted | tau^2 estimated conditional on X; R^2 now meaningful |
| C6 | Accepted | Knapp-Hartung adjustment + QM omnibus test for meta-regression |
| C7 | Partial | Sensitivity excluding aggregated studies; RVE acknowledged as limitation |
| C8 | Accepted | sa-accuracy replaces year as frontier-paradox moderator |
| C9 | Partial | Small subgroups labeled exploratory; no Bonferroni (justified) |
| C10 | Accepted | Partition-of-Q approach; results reported |
| C11 | Accepted | tau^2 re-estimated per leave-one-out iteration |
| C12 | Accepted | Convenience sample stated in abstract/conclusion; verified-only sensitivity |
| M1-M7 | Accepted/Partial | See individual responses above |
