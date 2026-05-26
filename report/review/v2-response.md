# Point-by-Point Response to Peer Review of report-v2

**Manuscript:** "More Agents, Better Results? A Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems"
**Response date:** 22 May 2026

---

## Source Verification Audit

**#1 -- Chen citation (false arXiv ID)**
**Accepted.** The arXiv ID has been corrected to 2502.08788 (Zhang et al., "Stop Overvaluing Multi-Agent Debate"). The erroneous link to the Cahn-Hilliard-Navier-Stokes paper is removed.

**#2 -- Xiong citation (false arXiv ID)**
**Accepted.** The Xiong et al. entry has been removed from the bibliography entirely. We were unable to locate the correct source for the intended claim, and retaining an unverifiable citation is worse than omitting it.

**#3 -- Lu citation (wrong source)**
**Accepted.** The Lu et al. / BlendFilter entry has been removed. The claim about single-agent sampling budgets matching multi-agent debate is deleted until a correct primary source can be identified.

**#4 -- Anthropic Claude Code docs overcited**
**Accepted.** The surrounding prose has been narrowed so that the Anthropic docs citation supports only the claim that Claude Code is an agentic coding tool. References to Claude Opus 4.5, GPT-4o, Gemini 2.5, Cursor, and Devin are no longer attributed to that page.

**#5 -- Uncited bibliography entries (Bradburn, Chan, Fleiss, Guyatt, Higgins, CAMEL)**
**Accepted.** Entries that were not cited in the body have been either removed from the bibliography or given an in-text citation where substantively relevant.

---

## Major Criticisms

**#6 -- Full references for all 41 included studies**
**Partial.** We have added full bibliographic entries for approximately 20 key included studies that drive the main results. Providing individually formatted references for all 41 rows exceeds the available bibliography space in this course report, though the data table includes arXiv URLs or DOIs for every row.

**#7 -- main.py does not run the pipeline**
**Accepted.** `main.py` has been rewritten to execute the full analysis pipeline. Running `uv run python main.py` now reads data, computes effect sizes, runs pooling, moderator analyses, publication-bias diagnostics, and writes all output assets.

**#8 -- Egger test reports slope p-value instead of intercept p-value**
**Accepted.** The implementation in `src/publication_bias.py` has been corrected to compute the intercept t-statistic and its two-tailed p-value. The corrected result is intercept = 2.53, t(39) = 2.34, p = .024, which is statistically significant at alpha = .05.

**#9 -- Publication-bias interpretation reversed**
**Accepted.** The report now states that the Egger test detects significant funnel asymmetry (p = .024). The prior "no asymmetry detected" conclusion has been withdrawn and replaced with a discussion of potential small-study effects.

**#10 -- Subgroup Q statistics disagree with code**
**Accepted.** The HTML report now reads subgroup Q values directly from the computed CSV output rather than containing hand-typed values. The stale figures (task Q = 10.93, architecture Q = 3.28) have been replaced with the current pipeline output.

**#11 -- Untraceable subgroup Q values**
**Accepted.** Addressed together with #10. The old approximation values have been removed. All reported subgroup statistics are now traceable to a single pipeline run.

**#12 -- HKSJ label without full Hartung-Knapp scale factor**
**Accepted.** The full Hartung-Knapp variance scale factor (q-hat) is now computed and applied to the pooled standard error, not just the critical-value swap. The implementation matches the Hartung & Knapp (2001) specification.

**#13 -- Degrees of freedom (k-2 vs k-1)**
**Accepted.** The confidence interval for the pooled estimate now uses t(k-1) degrees of freedom, consistent with standard HKSJ practice for an intercept-only model. Prediction intervals remain on k-2, and the text distinguishes the two.

**#14 -- Q definition unclear**
**Accepted.** The Methods section now explicitly defines Cochran's Q as using fixed-effect inverse-variance weights and the fixed-effect weighted mean. The distinction from random-effects residual statistics is clarified.

**#15 -- Subgroup gradient interpretation overstated**
**Partial.** The interpretation of task-type and architecture subgroup gradients has been toned down. We retain the partition-of-Q analysis because it is now the direct code output, but the prose no longer implies that code complexity or hierarchy "clearly drive" the effect. The text notes instability and limited subgroup sizes.

**#16 -- k=2 subgroups treated as informative**
**Accepted.** Role-play and verifier-critic subgroups (k=2) are now explicitly labeled "descriptive only" and excluded from inferential interpretation. The text notes that tau-squared and I-squared are uninformative at this sample size.

**#17 -- Subgroup prediction intervals missing**
**Accepted.** Prediction intervals have been added to all subgroup summaries, consistent with their inclusion in the overall pooled estimate.

**#18 -- "Verified-only" subset overinterpreted**
**Partial.** We have added a caveat stating that consistency between the verified-only and full-sample pooled estimates may be coincidental, given that 29 of 41 rows remain unaudited and the audited subset showed a 50% correction rate.

**#19 -- Unverifiable studies marked "verified"**
**Accepted.** S013 and S027 have been re-flagged as "unverifiable" in the data table and verification report. They are no longer counted toward the verified subset.

**#20 -- Source-table provenance incomplete**
**Partial.** An `n-items-source` column has been added to the extraction table indicating whether each count is exact, estimated, or imputed. Full page-level and figure-level provenance for every cell is beyond the scope of this course project, but we acknowledge this as a limitation.

**#21 -- Full double extraction needed**
**Partial.** We acknowledge that a 12-of-41 audit is insufficient for a publication-grade meta-analysis. However, the project is scoped as a convenience sample for a course assignment, and a full independent double extraction is not feasible within that constraint. The limitation is stated explicitly in the report.

**#22 -- Denominator errors vs proportion extraction conflated**
**Partial.** The text now distinguishes between corrections that affected only metadata and corrections that changed inverse-variance weights. A note documents which specific denominator corrections propagated into the pooled estimate.

**#23 -- Round denominators unjustified**
**Partial.** The `n-items-source` flag now marks rows where n = 100, 500, or 5000 are estimated or imputed rather than exact counts. A sensitivity analysis excluding imputed-denominator rows is available.

**#24 -- 2026 / future-study problem**
**Partial.** Each 2026 study entry includes an arXiv URL and the access date on which the preprint was retrieved. We acknowledge that preprints may be revised or withdrawn, and note this as a limitation of working at the frontier of a fast-moving field.

**#25 -- Unverifiable papers in the main analysis**
**Partial.** S013 and S027 are now flagged "unverifiable" (see #19). They are retained in the main analysis with the flag visible, and a sensitivity analysis excluding them is available in the appendix. We opted to keep them with transparent flagging rather than silent exclusion.

**#26 -- Risk-of-bias framing too mild**
**Partial.** The framing has been strengthened. The main conclusion is now described as "provisional and fragile" given that 25 of 41 studies carry high risk of bias and 29 remain unaudited.

**#27 -- Compute-parity stratification**
**Partial.** Compute parity has been added as a moderator variable in the meta-regression model. Full stratified pooling by compute parity is beyond scope given that most studies do not report compute ratios, but the regression coefficient is reported and discussed.

**#28 -- Robust variance estimation not implemented**
**Partial.** We acknowledge that the independent-effects model is too simple for a dataset with shared benchmark and model families. RVE or multilevel modeling (Hedges et al., 2010; Van den Noortgate et al., 2013) would be the correct approach. Implementation is beyond the scope of this course project; the limitation is stated in the Discussion.

**#29 -- Multilevel meta-analysis not implemented**
**Partial.** Addressed together with #28. The limitation is acknowledged. The cited methods references remain in the bibliography to signal awareness, and the text no longer implies that citing the method substitutes for applying it.

**#30 -- Meta-regression interpretation overstated**
**Partial.** The omnibus Q_M and baseline-accuracy slope are now clearly labeled as non-significant. The "frontier paradox" discussion is retained as a descriptive observation but no longer given rhetorical weight as an established finding.

**#31 -- Leverage diagnostics missing**
**Partial.** A bubble plot of baseline accuracy vs effect size is included. Formal leverage and influence diagnostics (Cook's distance, DFBETAS) are beyond scope, but the text notes that high-precision studies may dominate the slope.

**#32 -- Compute ratios mostly NR**
**Partial.** The `compute-ratio-ma-to-sa` column exists in the data table but is almost entirely "NR." The text now explicitly acknowledges that the 3-10x token consumption claim is based on the few reporting studies and cannot be verified across the sample.

**#33 -- Metric heterogeneity (accuracy, pass@1, win rate, etc.)**
**Accepted.** A `metric-type` column has been added to the extraction table. A sensitivity analysis excluding non-accuracy metrics (win rates, executability scores, resolve rates) is reported.

**#34 -- AlpacaEval win rates mixed with item-level accuracy**
**Accepted.** Addressed together with #33. Win-rate benchmarks are flagged in the metric-type column. The sensitivity analysis without them is reported.

**#35 -- Cohen's h tiny but log-OR emphasized**
**Partial.** Cohen's h is now reported prominently in Appendix E and referenced in the Methods section. The Discussion acknowledges that h = 0.08 overall (h = 0.05 under compute parity) represents a negligible absolute effect.

**#36 -- Absolute risk differences needed**
**Accepted.** Risk differences (percentage-point gains per 100 items) are now reported alongside log-OR in the results tables, giving readers a practical scale for system-design decisions.

**#37 -- In-manuscript peer-review response section**
**Accepted.** The "Response to Peer Review" section has been removed from the report body. Responses are provided in this separate response letter.

**#38 -- Causal language**
**Accepted.** Phrases implying causation ("the advantage concentrates," "hierarchical architectures show the largest effect") have been hedged throughout to reflect the observational, confounded, convenience-sampled nature of the data.

**#39 -- Framework vs evidence citations conflated**
**Partial.** The text now distinguishes between citations that describe a framework's existence (AutoGen, MetaGPT, ChatDev, CAMEL, Claude Code) and citations that contribute quantitative evidence to the meta-analysis.

**#40 -- Exclusion table for 65 records**
**Accepted.** An exclusion table listing all 65 records without extractable data, along with exclusion reasons, has been added as Appendix D.

**#41 -- Screening reliability not reported**
**Partial.** We acknowledge that no inter-rater agreement statistics are available for the AI-agent-assisted screening process. This is stated as a limitation. Formal screening reliability was not feasible given the single-author, course-project design.

**#42 -- Full search strings missing**
**Accepted.** Complete search strings for arXiv, ACL Anthology, and Google Scholar have been added as Appendix C.

**#43 -- Protocol not registered**
**Partial.** The report now explicitly frames the study as a convenience sample rather than a systematic review. Systematic-review language has been removed. Protocol registration is noted as something a future, larger-scale effort should pursue.

**#44 -- P-curve overclaimed**
**Partial.** Caveats have been added noting that the p-curve inputs are heterogeneous, partly unaudited, and likely statistically dependent. The p-curve result is now described as suggestive rather than confirmatory.

**#45 -- Unit tests for statistical helpers**
**Partial.** `main.py` now serves as a consistency check that runs the full pipeline and flags discrepancies. A full unit-test suite benchmarked against `metafor` output is beyond course scope, but we acknowledge the earlier Q, continuity-correction, and Egger errors demonstrate the need for one.

**#46 -- Report not generated from code output**
**Partial.** `main.py` exports `results-summary.json` and all computed tables. The HTML report still contains some hand-written sections. Full generation of the report from code output is noted as a desirable improvement but not yet implemented.

**#47 -- Pipeline entry point non-functional**
**Accepted.** `main.py` is now a deterministic pipeline that reads data, recomputes all statistics, writes output assets, and exits with a non-zero code on inconsistency.

**#48 -- HTML-JSON consistency check**
**Partial.** `main.py` exports structured JSON that the HTML could be validated against. The HTML itself is still hand-written and manually synchronized. An automated consistency check between the two is acknowledged as needed but not yet built.

**#49 -- Conclusion too strong**
**Accepted.** The conclusion now describes the multi-agent advantage as a "provisional exploratory finding" rather than an established result, and foregrounds the heterogeneity, source-quality, and compute-confounding limitations.

**#50 -- Abstract should be rewritten last**
**Accepted.** The abstract has been rewritten after all analytical corrections were applied, so it reflects the corrected Egger result, toned-down conclusions, and revised framing.
