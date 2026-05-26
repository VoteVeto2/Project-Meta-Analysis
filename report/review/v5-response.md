# Response to review-v5.md

## Summary

The v5 review identified 10 major issues. v6 addresses all of them, with varying degrees of scope.

### Fully addressed

| # | Issue | Fix in v6 |
|---|-------|-----------|
| 1 | Report claims reproducibility but submitted artifact has no code/data | Appendix A now explicitly states this is an HTML export; reproducibility claim reworded to point readers to the GitHub repo rather than claiming the HTML is self-contained |
| 2 | Missing 41-row extraction table | New Appendix Table A1 with all 41 rows: study-id, benchmark, task, architecture, n-items, MA/SA accuracy, RD, log-OR, n-items-source, compute-parity, audit-status, RoB |
| 3 | Subgroup tables don't sum to k=41 | Singleton categories merged: factuality (k=1) → other; moa + planner-executor → other/rare. Task table now sums to 41 (6 groups). Architecture table sums to 41 (6 groups). Pipeline validation enforces this. |
| 4 | Sprague citation misused for multi-agent compute parity | Sprague removed from the multi-agent compute-parity argument. Zhang 2025 is now the sole skeptical source. Sprague retained only as a general inference-cost reference in Discussion 4.3. |
| 5 | MetaGPT and ChatDev citation errors | MetaGPT author list corrected to end with "& Schmidhuber, J." per arXiv metadata. ChatDev final author corrected to "& Sun, M." per ACL Anthology. |
| 7 | Effect-size model too clean for data | Section 2.3 now explicitly states: "Because item-level paired correctness was unavailable, MA and SA proportions were treated as independent binomial counts. This likely underestimates uncertainty." |
| 8 | Subgroup p-values not worth the space | Subgroup Q_between values retained but explicitly labeled as exploratory/descriptive. New sentence: "These subgroup patterns are exploratory and should not be interpreted causally." |
| 9 | P-curve should be removed | P-curve removed from pipeline (main.py), results-summary.json, Table 6, and all report text. Egger/Begg/trim-and-fill retained as exploratory diagnostics with caveat about unreliability under extreme heterogeneity. |
| 10 | GRADE/ROB language too formal | Renamed throughout: "Informal risk-of-bias assessment adapted from ROB 2 concepts"; "Informal certainty assessment (GRADE-like)"; "PRISMA-style flow diagram" |

### Partially addressed

| # | Issue | Status |
|---|-------|--------|
| 6 | Report overuses advanced meta-analysis language for a convenience sample | Title updated to include "Exploratory Convenience-Sample." Abstract simplified. Subtitle and framing throughout now use "exploratory convenience-sample meta-analysis." However, the statistical machinery (REML, HKSJ, meta-regression) is retained because it is part of the course requirements — the framing simply no longer oversells the design. |

### Additional changes in v6

| Change | Description |
|--------|-------------|
| Risk difference foregrounded | RD (percentage-point difference) now appears first in the pooled results section and abstract; log-OR presented as the formal effect size afterward |
| Meta-regression demoted | Moved to appendix-level prominence. Main text reduced to one sentence: "Exploratory meta-regression did not identify reliable moderators (Appendix)." |
| Verified subset promoted | k=10 verified subset now appears as a key result in the main sensitivity discussion, not buried |
| Extraction table added to pipeline | `reporting.py` now exports `extraction-table.csv` with 18 columns including MA/SA percentages and risk differences |
| Subgroup validation | `main.py` validation now checks both task and architecture subgroup k sums equal 41 |
| Abstract simplified | Subgroup Q statistics removed from abstract per reviewer suggestion |
| Revised title | English: "More Agents, Better Results? An Exploratory Convenience-Sample Meta-Analysis…" / Chinese: "更多智能体，更好结果？…探索性便利样本元分析" |
| Revised conclusion | Final paragraph uses reviewer-suggested language: "This project does not establish that multi-agent LLM systems generally outperform single-agent baselines." |
| Introduction citation fix | Sprague paragraph rewritten to use Zhang 2025 as the multi-agent skeptical source |
| PICOS criterion added | Section 2.2: "Only studies reporting comparable MA and SA outcomes on the same benchmark, using the same or clearly comparable backbone model, were eligible." |
