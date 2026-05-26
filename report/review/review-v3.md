# Peer Review of `report/report-v3.html`

**Manuscript:** "More Agents, Better Results? A Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems"
**Author:** Xinyu Yang (r1020926), KU Leuven
**Review date:** 22 May 2026
**Reviewer:** Prof. Dr. habil. Dietrich Schmidt-Hoffmann, Ludwig-Maximilians-Universitat Munchen
**Recommendation:** **Minor revision**

---

## 1. Summary

Yang (2026, v3) presents a REML random-effects meta-analysis of 41 within-study comparisons examining multi-agent versus single-agent LLM performance on benchmark accuracy. The pooled log-OR is 0.45 (95% HKSJ CI [0.23, 0.67]; PI [-0.74, 1.64]; I^2 = 96.1%; Cohen's h = 0.08). Egger's test is now correctly computed against the intercept and is significant (p = .024), the Cochran's Q uses fixed-effect weights and fixed-effect mean as required, the HKSJ adjustment is fully implemented with the scale factor and t(k-1) degrees of freedom, and prediction intervals use t(k-2). The paper reports eight sensitivity analyses, a GRADE-like assessment yielding "Very Low" certainty, and explicitly discloses the convenience-sample design, the 71% unaudited data, and the 50% correction rate. This third revision addresses the 50 issues raised in the v2 audit and the 12 issues from v1, resolving every computational and citation-provenance error that previously threatened the paper's validity. The remaining issues are presentational.

---

## 2. Recommendation

**Minor revision.** The fundamental statistical and citation errors from v1 and v2 are corrected. The paper is now computationally sound and honestly framed. The items below are improvements in clarity, not threats to validity. The student may address them at their discretion before final submission.

---

## 3. Improvements from v2

- **Egger's test corrected and consequences absorbed.** The intercept-based test (t(39) = 2.34, p = .024) is now correctly reported. More importantly, the paper does not flinch: the danger box in Section 3.8 states plainly that the pooled estimate "may be inflated by selective reporting," and the GRADE table downgrades publication bias to "Serious." This is exactly the right response.

- **Full HKSJ implemented.** The pooled CI now applies the Hartung-Knapp scale factor with t(40) degrees of freedom for the pooled estimate, and the prediction interval uses t(39). The DerSimonian-Laird sensitivity check is reported alongside with its own (narrower) intervals, allowing readers to see the estimator sensitivity. The distinction is properly documented in Section 2.4.

- **Cochran's Q computed correctly.** Q = 1016.6 on df = 40 now uses fixed-effect weights and the fixed-effect pooled mean, matching Borenstein et al. (2009, Ch. 16). The value is identical across REML and DL rows in Table 2, as it must be. This was a serious error in v1 (Q inflated by ~60%) and is now resolved.

- **Citation provenance cleaned.** The false Chen arXiv ID (2502.15234, a Cahn-Hilliard-Navier-Stokes paper) is replaced with the correct Zhang et al. (2025) reference (2502.08788). The false Xiong ID is removed. The Lu/BlendFilter misattribution is gone. Uncited bibliography entries (Bradburn, Chan, Fleiss, Guyatt, Higgins, CAMEL) have been purged. Every remaining reference in the bibliography is cited in the body.

- **Cohen's h and risk-difference reporting.** The addition of h = 0.08 (full sample) and the approximate 3-5 percentage point risk difference gives the reader absolute-scale context that the log-OR alone cannot provide. The new Appendix E with per-subgroup h values is a useful addition. The disconnect between a seemingly impressive OR of 1.57 and a trivial h of 0.08 is explicitly discussed -- this is a pedagogically valuable insight for a course paper.

---

## 4. Remaining minor issues

**M1. Table 2 note says "PIs use t(39)" but Section 2.4 says "t(k-2)."** At k = 41, t(k-2) = t(39), so the numbers are correct. But the table note should say t(k-2) = t(39) to make the link explicit. A reader unfamiliar with the convention may wonder whether t(39) is t(k-1) or t(k-2).

**M2. Subgroup Q_between interpretation could be sharpened.** The text reports Q_between(5) = 197.56 (task) and Q_between(4) = 32.75 (architecture) as "significant," which is correct. However, the partition-of-Q method assumes a common tau^2 across subgroups. Given that within-subgroup I^2 ranges from 0% (evaluation) to 99.7% (general knowledge), this assumption is visibly violated. A one-sentence caveat about heterogeneous within-group variances would strengthen the interpretation. This is not a statistical error -- partition-of-Q is standard -- but the heterogeneity pattern invites the note.

**M3. The compute-parity CI lower bound is reported as "0.00" in Table 7.** The JSON does not include the compute-parity sensitivity result, so I cannot verify the exact value. If the lower bound is, say, 0.003, writing "0.00" implies it touches exactly zero, which overstates the borderline character. If it genuinely rounds to 0.00, state the unrounded value in the text (e.g., "the lower bound is 0.003, rounding to 0.00").

**M4. The abstract is 194 words.** This is fine for a course paper, but it packs substantial statistical detail. Consider whether the Egger intercept value (2.53) and the exact t-statistic (2.34) need to appear in the abstract, or whether "Egger p = .024" suffices. Abstracts benefit from parsimony.

**M5. Section 4.4 lists nine limitations in a single paragraph.** This is thorough but dense. Numbering them (as is already done with parenthetical ordinals) helps, but splitting into two paragraphs -- one for data-quality limitations (items 1-5), one for analytical limitations (items 6-9) -- would improve readability.

**M6. The GRADE box rates imprecision as "Not serious."** The justification is that the pooled CI excludes zero. This is defensible for the full-sample estimate, but the compute-parity subset (the most policy-relevant analysis) has a CI lower bound that barely escapes zero. A parenthetical acknowledgment that imprecision is more concerning for the key sensitivity analysis would be balanced.

**M7. Appendix D could note the direction of potential bias from the 65 excluded records.** The text correctly states that excluded records "may not be missing at random" and that null-result studies may report less detail. The logical consequence -- that the analytic sample likely overrepresents positive results -- could be stated more directly. This reinforces the Egger finding and the GRADE downgrade.

---

## 5. Statistical check

I verified the key statistics against the results-summary.json output. The REML pooled log-OR of 0.4499 rounds correctly to 0.45; the CI [0.2313, 0.6685] rounds to [0.23, 0.67]; the PI [-0.7413, 1.6410] rounds to [-0.74, 1.64]; tau^2 = 0.3351 rounds to 0.34; I^2 = 96.07% rounds to 96.1%. Cochran's Q = 1016.62 on df = 40 is correctly reported as 1016.6 and is identical across the REML and DL rows, confirming it is computed from fixed-effect quantities. The Egger intercept of 2.5258 (t(39) = 2.34, p = .024) is correctly reported and correctly interpreted as significant funnel asymmetry. The Begg tau = 0.056 (p = .605) and trim-and-fill (k0 = 0) are correctly reported as non-significant. The DL sensitivity (pooled log-OR = 0.4145, CI [0.2165, 0.6126]) is consistent with the narrower intervals expected from z-based DL inference. All statistics that I can verify from the JSON check out. The HKSJ implementation is now correct: REML uses t-distribution inference with the Hartung-Knapp scale factor, while DL uses the standard z-based approach, and both share the same Q. This is textbook-compliant.

---

## 6. Verdict

This paper has matured from a computationally flawed first draft through a citation-contaminated second draft into a statistically sound, honestly framed, and well-documented exploratory meta-analysis that exceeds the expectations of a 4-ECTS course paper -- accept after minor presentational revisions.
