# Review of `report/report-v4.html`

**Date:** 22 May 2026  
**Question:** Does v4 address the concerns raised in `review-v2.md`, and is the report cohesive?  
**Verdict:** **Major improvement, but not a clean pass.**

## Credit Where It Is Due

Version 4 is a real improvement over v2. The report no longer hides behind a confident pooled estimate. It now foregrounds fragility, publication bias, trivial absolute effects, compute confounding, extreme heterogeneity, and weak data provenance. The abstract, results, discussion, and conclusion mostly tell the same story: there is a positive signal, but the evidence base is too contaminated for strong claims.

Specific improvements:

1. The false Chen `arXiv:2502.15234` citation is gone.
2. The false Xiong `arXiv:2311.08207` citation is gone.
3. The unsupported Lu/BlendFilter citation is gone.
4. Anthropic Claude Code is no longer misused as evidence for frontier-model overhead.
5. Egger's test is now computed and interpreted correctly as significant: intercept = 2.53, t(39) = 2.34, p = .024.
6. The report now treats publication bias as a serious concern rather than claiming clean diagnostics.
7. Q_between values now match the current code/assets: task Q_between = 197.56; architecture Q_between = 32.75.
8. `main.py` now runs a real pipeline and regenerates assets, instead of printing only a placeholder.
9. The in-manuscript response-to-review section has been removed.
10. The report now includes Cohen's h, approximate risk differences, exact-n sensitivity, accuracy-only sensitivity, search-string appendix, and an exclusion-summary appendix.
11. The tone is much more appropriately cautious: "Very Low" certainty is the right direction.

## Remaining Problems

1. **Not all v2 concerns are addressed.** The biggest unresolved issue is that the report still does not provide full references or source provenance for all 41 included studies. A reader still cannot audit the forest plot from the report alone.

2. **The corrected Zhang citation still has a bibliographic error.** The arXiv ID `2502.08788` is now the right paper, but the report lists the authors as "Zhang, H., Du, Y., Tang, H., Chen, Y., & Ma, T." The arXiv page lists Hangfan Zhang, Zhiyao Cui, Jianhao Chen, Xinrun Wang, Qiaosheng Zhang, Zhen Wang, Dinghao Wu, and Shuyue Hu. The title in the report also does not match the arXiv title exactly.

3. **There are still uncited references.** `ref-du2023` and `ref-liang2024` appear in the bibliography but are not cited in the body.

4. **The "all 41 studies" provenance problem remains.** The verified table still has source provenance like "Table/Fig from Chen2026" rather than page/table/figure/metric/denominator details. This fails the v2 request for extractable-count provenance.

5. **Unverifiable studies remain in the main model.** S013 Chen2026 and S027 Fan2025 are now marked `unverifiable`, which is better than pretending they are verified, but they still remain in the primary pooled estimate.

6. **Only 10 studies are actually verified/corrected.** The report says 29/41 are unaudited, but the data also include 2 `unverifiable` rows. The cleaner statement is that only 10/41 rows are verified or verified-corrected; 31/41 are not verified.

7. **The n-items accounting is internally confusing.** Section 2.3 says 18 of 41 studies are flagged as estimated, but the exact-n sensitivity says the exact-n subset is k = 28, excluding 13. The data contain both `n-items-estimated=True` for 18 rows and `n-items-source != exact` for 13 rows. The report needs to reconcile these two definitions.

8. **The subgroup descriptive-only rule is inconsistent.** The text says subgroups with k < 3 are descriptive only, but Table 3 labels k = 3 evaluation and general-knowledge groups as descriptive only. It should say k < 5 or change the table labels.

9. **Subgroup prediction intervals are still not in the report tables.** They are available in the generated CSVs, but the HTML still only shows CIs. This leaves one of the v2 requests only partially addressed.

10. **Table 7's caption mentions leave-one-out analyses, but no leave-one-out rows are shown.** Either add leave-one-out results or remove that caption language.

11. **The exclusion "table" is only categorical.** Appendix D claims the 65 excluded records are catalogued, but it does not list the actual records. This is better than v2, but still not the exclusion table requested.

12. **Search strings are representative, not complete.** Appendix C improves reproducibility, but it explicitly gives representative queries rather than the full search log.

13. **Dependency modeling is still not implemented.** The report acknowledges this honestly, but the problem remains. RVE or multilevel meta-analysis is still needed for rigorous inference.

14. **Compute ratios are still not extracted.** The data column `compute-ratio-ma-to-sa` remains `NR` for all 41 rows, so the compute-confound discussion remains more qualitative than quantitative.

15. **`main.py` runs, but there is no real output validation.** Appendix A says output validation exists, but the script does not check that report table values match JSON/CSV outputs. It regenerates outputs; it does not validate the HTML.

16. **The pipeline emits a warning.** Running `uv run python main.py` completes, but `src/sensitivity.py` warns that a Boolean Series is being reindexed. This should be fixed even if the current output happens to be correct.

17. **No tests are present.** The v2 request for tests against known outputs remains unaddressed. Given the previous Egger/Q/HKSJ mistakes, tests are not optional polish.

18. **"Full HKSJ" needs qualification.** The code uses a variance floor via `max(1.0, s2_hk)`, which is closer to a modified/ad hoc Hartung-Knapp variant than a plain full HKSJ implementation. The report should name the variant or cite the adjustment.

19. **Primary-study bibliography is still too sparse.** The reference list now has 25 entries, but the analysis uses 41 comparisons. Framework/method citations are not a substitute for included-study references.

20. **The report remains a convenience-sample audit, not a robust meta-analysis.** V4 now admits this, which deserves credit, but admitting the limitation does not remove it.

## Cohesion Check

Overall cohesion is much better than v2. The abstract, caveat box, sensitivity section, GRADE-like assessment, discussion, and conclusion now agree that the positive effect is fragile and likely inflated. That is the strongest thing about v4.

The remaining cohesion problems are mostly bookkeeping and traceability:

- the denominator-count story uses two different definitions;
- the verified/unaudited/unverifiable categories are not summarized cleanly;
- the appendices promise more provenance than they deliver;
- the reproducibility appendix overstates validation;
- the references still do not fully support the evidence table.

## Recommendation

Give v4 credit for substantially improving the statistical honesty and narrative cohesion. Do not treat it as fully fixed. The next revision should focus less on adding caveats and more on hard auditability: complete primary-study references, exact extraction provenance, removal or quarantine of unverifiable studies, a real validation script, and tests for the statistical functions.

