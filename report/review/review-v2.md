# Peer Review of `report/report-v2.html`

**Manuscript:** "More Agents, Better Results? A Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems"  
**Review date:** 22 May 2026  
**Reviewer stance:** adversarial statistical and source audit  
**Recommendation:** **Reject in present form / resubmit only after a full data and citation audit**

## Summary Verdict

Revision 2 fixes some defects from the first review, but it is not yet a trustworthy meta-analysis. The paper now looks more polished than the underlying evidence deserves. Several headline claims rest on a bibliography that contains outright wrong arXiv IDs, unsupported narrative citations, uncited references, unverifiable included studies, and statistics that do not agree with the repository code. The most damaging problems are not stylistic. They are validity problems: source provenance is weak, publication-bias inference is miscoded, subgroup tests in the report disagree with the current implementation, the claimed reproduction command does not run the analysis, and only 12 of 41 extracted studies have been audited despite a 50% correction rate among audited rows.

The manuscript should stop presenting itself as an improved quantitative synthesis and instead admit that it is still a preliminary, error-prone convenience audit.

## Source Verification Audit

I checked every reference listed in the HTML bibliography against its DOI landing page, arXiv page, or official documentation page. The DOI-method references mostly resolve correctly. The LLM-agent references are much weaker: several entries are uncited, and several narrative claims are not supported by the cited source.

| Report reference | Verification result | Problem |
|---|---:|---|
| Anthropic (2025), Claude Code docs: https://docs.anthropic.com/en/docs/claude-code | Partly verified | The page documents Claude Code as an agentic coding tool, but it does not support the surrounding claim about Claude Opus 4.5, GPT-4o, Gemini 2.5, Cursor, or Devin. |
| Begg & Mazumdar (1994): https://doi.org/10.2307/2533446 | Verified | DOI/title match. |
| Borenstein et al. (2009): https://doi.org/10.1002/9780470743386 | Verified | DOI/title match. |
| Bradburn et al. (2007): https://doi.org/10.1002/sim.2528 | Verified but uncited | Present in bibliography but not cited in the report body. |
| Chan et al. (2024), ChatEval: https://arxiv.org/abs/2308.07201 | Verified but uncited | Source exists; not cited in body. |
| Chen et al. (2025), "Stop overvaluing...": https://arxiv.org/abs/2502.15234 | **Failed** | The linked arXiv paper is a numerical-analysis paper on Cahn-Hilliard-Navier-Stokes equations, not multi-agent debate. The actual "Stop Overvaluing Multi-Agent Debate" paper is by Hangfan Zhang et al. at https://arxiv.org/abs/2502.08788. |
| Du et al. (2023): https://arxiv.org/abs/2305.14325 | Verified | Source exists and matches multi-agent debate. |
| Duval & Tweedie (2000): https://doi.org/10.1111/j.0006-341X.2000.00455.x | Verified | DOI/title match. |
| Egger et al. (1997): https://doi.org/10.1136/bmj.315.7109.629 | Verified | DOI/title match. |
| Fleiss et al. (2003): https://doi.org/10.1002/0471445428 | Verified but uncited | Present in bibliography but not cited in body. |
| Guyatt et al. (2011): https://doi.org/10.1016/j.jclinepi.2010.09.011 | Verified but uncited | Present in bibliography but not cited in body. |
| Hartung & Knapp (2001): https://doi.org/10.1002/sim.791 | Verified | DOI/title match. |
| Hedges et al. (2010): https://doi.org/10.1002/jrsm.5 | Verified | DOI/title match. |
| Higgins et al. (2003): https://doi.org/10.1136/bmj.327.7414.557 | Verified but uncited | Present in bibliography but not cited in body. |
| Hong et al. (2023), MetaGPT: https://arxiv.org/abs/2308.00352 | Mostly verified | Source exists; author list in report is imprecise and truncates/misinitializes names. |
| IntHout et al. (2014): https://doi.org/10.1186/1471-2288-14-25 | Verified | DOI/title match. |
| IntHout et al. (2016): https://doi.org/10.1136/bmjopen-2015-010247 | Verified | DOI/title match. |
| Li et al. (2024), CAMEL: https://arxiv.org/abs/2303.17760 | Verified but uncited | Source exists; bibliography year/venue treatment is sloppy, and it is not cited in body. |
| Liang et al. (2024): https://arxiv.org/abs/2305.19118 | Verified | Source exists and matches title. |
| Lu et al. (2024), BlendFilter: https://arxiv.org/abs/2402.11129 | **Failed / unsupported** | The linked paper is "BlendFilter" by Haoyu Wang et al., not Lu et al. It is a RAG paper and does not demonstrate that single-agent sampling budgets match or exceed multi-agent debate. |
| Pustejovsky & Tipton (2022): https://doi.org/10.1007/s11121-021-01246-3 | Verified | DOI/title match. |
| Qian et al. (2024), ChatDev: https://arxiv.org/abs/2307.07924 | Mostly verified | Source exists; author listing in report is incomplete/sloppy. |
| Simonsohn et al. (2014): https://doi.org/10.1037/a0033242 | Verified | DOI/title match. |
| Sprague et al. (2024): https://arxiv.org/abs/2409.12183 | Verified but weakly used | Source is about chain-of-thought effects, not a direct multi-agent debate compute-parity paper. The citation is overextended. |
| Sterne et al. (2019): https://doi.org/10.1136/bmj.l4898 | Verified | DOI/title match. |
| Sweeting et al. (2004): https://doi.org/10.1002/sim.1761 | Verified | DOI/title match. |
| Tang et al. (2024), MedAgents: https://arxiv.org/abs/2311.10537 | Verified | Source exists and matches title. |
| Van den Noortgate et al. (2013): https://doi.org/10.3758/s13428-012-0261-6 | Verified | DOI/title match. |
| Viechtbauer (2005): https://doi.org/10.3102/10769986030003261 | Verified | DOI/title match. |
| Viechtbauer (2010): https://doi.org/10.18637/jss.v036.i03 | Verified | DOI/title match. |
| Wu et al. (2023), AutoGen: https://arxiv.org/abs/2308.08155 | Verified | Source exists and supports AutoGen as a multi-agent conversation framework. |
| Xiong et al. (2024): https://arxiv.org/abs/2311.08207 | **Failed** | The linked arXiv paper is "Data-driven Control Against False Data Injection Attacks," not a medical LLM paper. |
| Zhang et al. (2024), CodeAgent: https://arxiv.org/abs/2401.07339 | Verified | Source exists and matches title. |

## Major Criticisms and Required Improvements

1. **Fix the false Chen citation immediately.** The report cites `arXiv:2502.15234` for "Stop overvaluing multi-agent debate"; that URL is a mathematics/numerical-analysis paper. This is not a small typo. It invalidates a central skeptical source in the introduction.

2. **Fix the false Xiong citation immediately.** The report cites `arXiv:2311.08207` for a medical LLM self-play/physician-feedback paper; that URL is a systems-control paper. This makes the medical-reasoning discussion look careless.

3. **Remove or replace the Lu citation.** The report claims Lu et al. showed that scaling single-agent sampling can match or exceed multi-agent debate, but the listed source is a RAG paper by different authors. The claim needs a real source or should be deleted.

4. **Stop citing Anthropic Claude Code docs as evidence for frontier-model coordination overhead.** The official Claude Code page supports only that Claude Code is an agentic coding tool. It does not substantiate the claims about Claude Opus 4.5, GPT-4o, Gemini 2.5, Cursor, Devin, or diminishing returns.

5. **Purge uncited bibliography entries.** Bradburn, Chan, Fleiss, Guyatt, Higgins, and CAMEL appear in the reference list but are not cited in the report body. A bibliography is not a dumping ground for sources that might have been useful.

6. **Add references for all 41 included studies.** The report synthesizes 41 comparisons but the bibliography does not provide full primary-source provenance for the included dataset. A reader cannot audit the forest plot from the paper.

7. **Do not claim all data are reproducible through `uv run python main.py`.** Appendix A says that command reproduces the pipeline, but `main.py` only prints `"Hello from proj-meta!"`. This is a direct reproducibility failure.

8. **Correct the Egger test implementation.** `src/publication_bias.py` reports the slope p-value from `stats.linregress` as if it were the intercept p-value. Recomputing with the intercept standard error gives intercept = 2.53, t(39) = 2.34, p = .024, not p = .765. The report's "no asymmetry detected" conclusion is therefore unsupported.

9. **Withdraw the confident publication-bias interpretation.** Once the Egger test is computed against the intercept, the publication-bias section is no longer reassuring. The manuscript cannot say diagnostics are "clean" while one diagnostic is miscoded and significant.

10. **Fix the subgroup Q statistics.** The HTML reports task Q_between(5) = 10.93, p = .053 and architecture Q_between(4) = 3.28, p = .512. The current `src/moderators.py` produces task Q_between = 197.56 and architecture Q_between = 32.75. The report and code cannot both be right.

11. **Explain which analysis generated the reported subgroup Q values.** If the HTML values came from an old approximation, they should be removed. If the code is wrong, the code should be fixed. At present this is an untraceable result.

12. **Do not call the primary CI "HKSJ" unless the full Hartung-Knapp variance adjustment is implemented.** `src/pooling.py` swaps z for a t critical value but does not compute the Hartung-Knapp scale factor for the pooled estimate. This is t-widening, not full HKSJ.

13. **Use defensible degrees of freedom.** The report says CIs use t(k-2). For an intercept-only meta-analysis, Hartung-Knapp inference conventionally uses k-1 degrees of freedom; prediction intervals are a separate issue. The paper should not blur these.

14. **Clarify whether Q is fixed-effect Cochran's Q or a random-effects residual statistic.** The prose treats Q as a simple invariant data property, while subgroup and model diagnostics mix several concepts. Define each statistic and keep formulas consistent.

15. **Stop interpreting subgroup gradients when between-group tests are unstable or contradictory.** The task and architecture subgroup sections read as if code and hierarchy clearly drive the effect, but the reported Q tests are either wrong or inconsistent with the repository.

16. **Do not pool k = 2 subgroups as if they mean anything.** Role-play and verifier-critic rows are statistical theater. With k = 2, tau-squared and I^2 are essentially uninformative.

17. **Add subgroup prediction intervals.** The paper emphasizes the overall prediction interval but then switches to only CIs for subgroups. That hides exactly the instability the discussion claims to foreground.

18. **Audit the "verified-only" subset more honestly.** Only 12 of 41 rows are audited. Of those, 6 required correction. Calling the matching verified-only pooled estimate "reassuring" is too generous; it may simply mean the unaudited errors have not yet been found.

19. **Stop treating "unable to verify" as "verified."** The verification report says S013 and S027 could not be definitively located, yet they remain marked `verified`. That label is misleading.

20. **Require source-table provenance for every extracted count.** "Table/Fig from X" is not enough. Each row needs page, table/figure number, exact metric, denominator, and whether the value was read, transformed, rounded, or imputed.

21. **Do a full double extraction, not a 12-row sample.** A 29.3% audit is inadequate when the audited subset already shows many denominator and agent-count corrections.

22. **Separate denominator errors from proportion extraction.** The report sometimes implies corrected denominators do not matter because percentages were right. They still affect inverse-variance weights and therefore pooled inference.

23. **Stop normalizing benchmarks to arbitrary round denominators.** Rows with n = 100, n = 500, and n = 5000 need explicit justification. If these are effective sample sizes rather than actual item counts, the effect-size model changes.

24. **Resolve the 2026/future-study problem.** The dataset contains many 2026 studies in a report dated 22 May 2026. Each needs a stable public source and access date; otherwise this reads like generated literature rather than an auditable evidence base.

25. **Do not include unverifiable or non-locatable papers in the main meta-analysis.** If a source cannot be located independently, it belongs in a sensitivity appendix or excluded entirely.

26. **Fix the high-risk-of-bias framing.** With 25 of 41 studies high RoB and 29 of 41 unaudited, "low certainty" is not harsh enough. The main conclusion should be framed as provisional and fragile.

27. **Downweight or stratify by compute parity rather than only running a sensitivity subset.** Compute confounding is the dominant threat to validity. A single subset row does not adequately address it.

28. **Model dependency properly.** Multiple rows share benchmark families, model families, and sometimes aggregated benchmark averages. A simple independent-effects random-effects model is too naive for the dataset.

29. **Implement robust variance estimation or multilevel meta-analysis.** The report cites Hedges and Van den Noortgate but does not do the work. Citing the method is not a substitute for modeling dependency.

30. **Correct the meta-regression interpretation.** The omnibus Q_M is non-significant and the baseline-accuracy slope is non-significant. The paper should stop giving the frontier-paradox result rhetorical weight.

31. **Center baseline accuracy and inspect leverage.** A single high-precision or high-baseline study can dominate the slope. The bubble plot is not enough.

32. **Report actual compute ratios.** The `compute-ratio-ma-to-sa` column is almost entirely `NR`, yet the paper repeatedly argues about 3-10x token consumption. That claim needs extracted numbers.

33. **Stop mixing accuracy, pass@1, win rate, executability score, and resolve rate as if they are interchangeable Bernoulli outcomes.** Some rows are not simple item-level accuracy proportions. The log-OR model assumes more homogeneity than the metrics provide.

34. **Handle AlpacaEval-style win rates separately.** A win-rate benchmark is not the same kind of binomial question-answer accuracy as GSM8K or HumanEval.

35. **Explain why Cohen's h is tiny while log-OR is emphasized.** Appendix C shows h = 0.08 overall and h = 0.05 under compute parity. The discussion still sells a "real advantage" more strongly than these absolute-scale effects justify.

36. **Use absolute risk differences or percentage-point gains alongside log-OR.** Readers designing systems care about added solved tasks per 100 examples, not only odds ratios inflated in high-accuracy regimes.

37. **Remove the in-manuscript "Response to Peer Review" section.** That belongs in a response letter, not in the article. It bloats the report and distracts from methods/results.

38. **Stop using vague causal language.** Phrases like "the advantage concentrates" and "hierarchical architectures show the largest effect" read causally despite uncontrolled, confounded, convenience-sampled data.

39. **Separate framework citations from included-effect citations.** AutoGen, MetaGPT, ChatDev, CAMEL, and Claude Code serve different rhetorical roles. The report currently blurs "framework exists" with "framework contributes quantitative evidence."

40. **Add an exclusion table for the 65 records without extractable data.** Those exclusions are likely non-random. Without a table, the selection process is opaque.

41. **Report screening reliability.** Six AI search agents and manual screening are described, but no inter-rater screening agreement or conflict-resolution details are provided.

42. **Give the full search strings.** "Queried arXiv, ACL Anthology, proceedings, and Google Scholar" is not a reproducible search strategy.

43. **Register or at least freeze the protocol.** An exploratory convenience sample can be useful, but the report should not retrofit systematic-review language onto a post hoc search.

44. **Stop overclaiming p-curve evidential value.** P-curve assumes a coherent set of hypothesis tests and independent evidential results. Here the inputs are heterogeneous, partly unaudited, and likely dependent.

45. **Add tests for every statistical helper.** The earlier Q, continuity-correction, meta-regression, and Egger errors show that the project needs unit tests with known outputs from `metafor` or another trusted implementation.

46. **Make the report generated, not hand-synchronized.** The HTML contains numbers that can drift from code. Generate tables from `results-summary.json` or the analysis script so stale statistics cannot survive.

47. **Use a real pipeline entry point.** A project claiming deterministic reproduction needs a command that reads data, recomputes effects, writes assets, writes summary JSON, and fails on inconsistency.

48. **Add a consistency check between HTML and JSON.** The build should fail if reported table values differ from computed outputs.

49. **Tone down the conclusion.** "Multi-agent systems outperform single-agent baselines" is too strong for a convenience sample with extreme heterogeneity, miscited sources, compute confounding, and weak verification.

50. **Rewrite the abstract after fixing the analysis.** The abstract currently packages unstable and partly erroneous diagnostics as settled findings. It should be the last section revised, not the first.

## Bottom Line

This manuscript is not ready for grading as a credible meta-analysis. It has the appearance of statistical sophistication, but the source audit reveals unacceptable citation errors, and the code audit reveals that at least one major diagnostic is wrong. The author should treat Revision 2 as a failed audit pass: useful work has been done, but the quantitative claims remain too brittle to trust.

