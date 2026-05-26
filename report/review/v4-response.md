# Response to review-v4.md

## Summary

Of the 20 remaining problems identified in the v4 review, v5 addresses the following:

### Fully addressed

| # | Issue | Fix in v5 |
|---|-------|-----------|
| 2 | Zhang citation wrong authors/title | Corrected to Zhang, H., Cui, Z., Chen, J. et al.; title updated to match arXiv |
| 3 | Uncited references (Du2023, Liang2024) | Both now cited in Introduction paragraph 1 |
| 6 | "12 audited, 29 unaudited" misleading | Replaced throughout with "10 verified/corrected, 2 unverifiable, 29 unaudited" (76% unverified) |
| 7 | n-items accounting inconsistent | Section 2.3 now reconciles the two definitions: 18 broadly estimated, 13 non-exact source; sensitivity uses the stricter k=28 |
| 8 | Subgroup k<3 vs k=3 labeling | Changed threshold to k < 5; table labels now consistent |
| 9 | Subgroup PIs missing from tables | PI columns added to Tables 3 and 4 |
| 10 | Table 7 mentions leave-one-out but shows none | Leave-one-out summary row added; range [0.40, 0.48], most influential = Wu2025 |
| 11 | Exclusion table only categorical | Appendix D now explicitly states directional consequence: analytic sample likely overrepresents positive findings |
| 15 | No output validation | main.py now includes 8 runtime sanity checks (k, df, Q, CI/PI brackets, Egger df) |
| 16 | Boolean reindexing warning | Fixed in sensitivity.py: use `.values` for the mask array |
| 17 | No tests | 18 unit tests in tests/test_stats.py covering DL, REML, HKSJ, Egger, effect sizes, and project-data constraints |
| 18 | "Full HKSJ" needs qualification | Section 2.4 now names the max(1, s²_HK) floor and cites Rover et al. (2015) |

### Partially addressed (scope constraints)

| # | Issue | Status |
|---|-------|--------|
| 1 | Full primary-study references | Du2023, Liang2024 now cited in body; remaining 39 studies are in the data table but not individually referenced in the bibliography. Adding all 41 references exceeds word count. |
| 4 | Extractable-count provenance | Data limitation: source column provides table/figure reference but not page-level detail. Acknowledged. |
| 5 | Unverifiable studies in primary model | New "unverifiable removed" sensitivity (k=39, log-OR=0.43) shows negligible impact; kept in primary model with explicit note. |
| 12 | Search strings representative | Appendix C already notes this is a convenience trawl. Full query logs not available. |
| 14 | Compute ratios NR | Data column remains NR for all 41 rows; discussed qualitatively in Section 4.3. |
| 19 | Primary-study bibliography sparse | Same as #1. |
| 20 | Convenience-sample limitation | Already extensively acknowledged. |

### Out of scope for this revision

| # | Issue | Reason |
|---|-------|--------|
| 13 | RVE / multilevel meta-analysis | Implementation complexity exceeds course scope; acknowledged in Section 2.4 and 4.4. |

### GRADE update

Imprecision upgraded from "Not serious" to "Some concerns" to reflect the borderline compute-parity CI.
