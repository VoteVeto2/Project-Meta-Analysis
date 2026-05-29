# Peer-review comments on report-v6

- **Reviewer:** Claude (Opus 4.8), acting as adversarial peer reviewer
- **Artifact reviewed:** `report/report-v6.html` (Revision 6, 26 May 2026)
- **Materials cross-checked:** `notebook/meta-analysis-v6.ipynb`, `src/*.py`, `main.py`, `data/verified/effect-size-table.csv`, `data/verified/verification-report.md`, `data/verified/risk-of-bias.csv`, `data/extracted/effect-size-table.csv`, `report/assets/*.csv`. All citations re-verified against arXiv / publishers / ACL Anthology via web search.

**Decision: Minor-to-moderate revisions.** This is now a genuinely careful, unusually self-critical course project, and — importantly — **every formal statistic in the main pipeline reproduces *exactly* from the committed code** (I re-ran it; see §"What is solid"). The remaining problems are not in the random-effects machinery. They are in (a) the *plain-language* effect numbers the report foregrounds, which are not reproducible and in one place contradicted by the project's own notebook; (b) an incomplete reference apparatus for the 41 included studies; (c) four citation/claim defects; and (d) an internally inconsistent verification trail. None is fatal; all are fixable.

---

## What I verified by re-running the pipeline

I recomputed all headline numbers from `data/verified/effect-size-table.csv` using the committed `src/` functions. **They match the report to the decimal:** REML log-OR = 0.4499 → 0.45, CI [0.231, 0.668], PI [−0.741, 1.641], τ² = 0.335, I² = 96.07%, Q(40) = 1016.6; DL = 0.41 [0.22, 0.61]; Egger intercept = 2.526, t(39) = 2.343, p = .0243; Begg τ = 0.056, p = .605; trim-and-fill k₀ = 0; all nine Table-6 sensitivity rows; both subgroup tables (k sums = 41; Q_between = 180.82 and 31.92); meta-regression Q_M = 5.35, p = .72, R² = 0%; leave-one-out range [0.396, 0.476], most-influential Wu2025 → 0.40 (τ² = 0.23). The statistical core is sound and faithfully reported. My criticisms below are about everything *around* it.

---

## Major issues

### M1. The foregrounded "interpretable" metrics (Cohen's *h* and risk difference) are not reproducible — and the notebook contradicts the report on *h*

The v5 review told the author to foreground absolute effects (risk difference, Cohen's *h*). v6 added those numbers to the prose but **never added them to the pipeline.** `main.py` and `src/` compute *per-study* `h` and the log-OR, but compute **no pooled Cohen's *h* and no pooled risk difference at all.** So the headline numbers were filled in by hand, and they do not survive checking:

- **Cohen's *h* = 0.08 "trivial, well below 0.20" is self-contradictory.** The v6 notebook itself computes `Cohen's h (overall) = df['h'].mean()` and prints **0.199** (cells 8 and 12) — yet the *same notebook's* summary table (cell 35) and the HTML report (abstract, §3.3, §4.1, danger box, Table E1) state **"0.08 (trivial)."** A mean *h* of 0.199 sits essentially *at* Cohen's 0.20 "small" threshold, the opposite of "well below." The reproducible candidates are: unweighted mean 0.199; random-effects-weighted 0.180; inverse-variance-weighted 0.069; pooled-from-summed-proportions 0.066. The reported 0.08 matches none cleanly (it is closest to the inverse-variance value, 0.069 → 0.07) and is *not* the number the notebook displays. **A central plank of the skeptical narrative — "the absolute effect is trivial" — rests on a figure that the project's own code refutes.**

- **Appendix Table E1's per-subgroup *h* (0.08 / 0.14 / 0.05 / 0.09 / 0.00) is not produced anywhere** and is internally inconsistent: the compute-parity row claims *h* ≈ 0.05, but the reproducible compute-parity *h* is 0.105 (pooled proportions) or 0.180 (mean of study *h*).

- **Appendix A1's Cohen's *h* column is stale.** The log-OR column in A1 matches the pipeline exactly, but the *h* column does not, for ≥6 studies: S011 (A1 0.866 vs pipeline 0.855), S012 (0.390 vs 0.423), S019 (0.478 vs 0.483), S020 (0.346 vs 0.364), S023 (1.218 vs 1.187), S028 (1.116 vs 1.111). The A1 *h* values were evidently not regenerated from `extraction-table.csv`.

- **"3–5 pp" full-sample RD** reconciles only with the *inverse-variance-weighted* RD (3.09 pp); the notebook prints the unweighted mean (8.21 pp) and median (6.13 pp), neither of which is 3–5 pp. The number is defensible under one (undisclosed) weighting but is not the quantity the displayed code reports.

- **"≈ 2 pp under compute parity" is not supported and understates the effect.** The reproducible compute-parity RD is **5.26 pp (inverse-variance weighted) / 5.15 pp (n-weighted) / 7.92 pp (unweighted)** — roughly 2–4× the claimed 2 pp — and pooled *h* ≈ 0.105, not 0.05. Ironically, on the absolute scale the compute-parity result is *less* trivial than the report says. The "most practically important finding" is dramatized beyond what the data show. (The log-OR attenuation 0.45 → 0.31 is real and reproducible; the *absolute*-scale gloss is the problem.)

**Fix:** Compute pooled RD and pooled Cohen's *h* *in the pipeline* under one stated convention (I recommend inverse-variance weighting, consistent with how the log-OR is pooled, or pooled-proportions), report whatever those values actually are, regenerate the A1 *h* column, and delete every hand-entered absolute-scale number. Also note explicitly that RD on the absolute scale is non-monotone across subsets (full inv-var RD 3.1 pp < compute-parity inv-var RD 5.3 pp because inverse-variance weighting up-weights the large MMLU/MATH studies), which is itself a reason to keep log-OR as the primary metric.

### M2. The 41 included studies are not fully referenced

Appendix A1 lists all 41 studies by citation key, but the References section provides full bibliographic entries for only ~10 of them (those that double as intro/discussion citations). There is **no way for a reader to locate** Benkovich2026, MediHive2026, Charney2026, Topologies2026, Hong2024, Doki2024, Xie2025, Wu2025, Fan2025, Wynn2025, Lin2025, Cui2025, Tian2026, Tran2026, Li2026, Liu2026, Hu2025, Zhou2025, Bao2025, Ferber2025, Li2025, MedARC2025, MedLA2025, and the rest. For a meta-analysis, a complete, resolvable list of included studies is a non-negotiable reporting item (it is what makes the synthesis auditable at all). This is the largest scholarly gap remaining after v5's table fix. **Fix:** add an "Included Studies" appendix giving, for each S0xx, the title + arXiv-id/DOI where known, and an explicit "could not be independently located" for S013 (Chen2026) and S027 (Fan2025).

### M3. Confirmed citation / claim defects (web-verified)

All method references and foundational LLM references check out, and the v5 MetaGPT/ChatDev author-list fixes held. But:

1. **Guo et al. (2024) is a conflated reference.** The report gives "Artificial Intelligence Review, 57, 367, DOI 10.1007/s44336-024-00009-2." That journal + article-number + DOI belong to a **different** paper (Li et al., "A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges," journal *Vicinagearth*). Guo et al.'s actual survey is arXiv:2402.01680, IJCAI 2024 (and the prefix 10.1007/s44336 is not *AI Review*, whose prefix is 10.1007/s10462). This is a fabricated-by-conflation citation and must be corrected. *(Flagged independently by two verification agents.)*

2. **Sprague et al. (2024) is still misused** (§4.3). The report says it shows "inference-time computation scaling can substitute for multi-step reasoning strategies." Sprague's actual thesis is that chain-of-thought helps *mainly on math/symbolic* tasks and that the field needs paradigms *beyond* prompt-based CoT — not that compute substitutes for reasoning. The v5 fix relocated the citation but did not cure the misrepresentation. Either restate accurately ("CoT's benefits are concentrated in math/symbolic domains") or drop it.

3. **MedAgents (Tang et al. 2024) is mischaracterized** (§4.2) as "adversarial verification, where a second agent challenges the first's diagnosis." MedAgents is *cooperative* multi-round discussion / consensus among expert personas, not adversarial verification. Reword.

4. **S005's citation key "Xue2025" is a misattribution.** arXiv:2509.23537 is led by Aaron Xuxiang **Tian**; there is no author named Xue. Rename the key (e.g., Tian2025) to avoid an incorrect author attribution.

5. Trivia: Pustejovsky & Tipton (2022) title is truncated ("...: Expanding the Range of Working Models").

### M4. The AlpacaEval 2.0 study (S040) is an invalid binomial

AlpacaEval 2.0's metric is the **length-controlled win rate** — a pairwise preference of the model's output over a **GPT-4 reference**, judged by an LLM annotator. It is a *relative, continuous* score, not per-item binary correctness. Back-computing "524/463 correct out of 805" and feeding them as independent binomial counts is not valid (the 805 denominator is right; the events are not item-level successes). The report acknowledges win-rate conflation in the abstract and §2.4, and the "accuracy-only (k=37)" sensitivity row does remove S040 (plus the three resolve-rate studies) — good — but the headline k=41 still includes it, and A1 still reports an RD/log-OR/*h* for it as if it were accuracy. **Fix:** either exclude win-rate/resolve-rate metrics from the primary analysis (make k=37 primary) or state plainly that S040 is retained only as a robustness inclusion.

---

## Moderate issues — verification-trail integrity

### V1. The "verified" data does not match the verification log, and ~21 "unaudited" rows were silently rescaled

Comparing `data/extracted/effect-size-table.csv` to `data/verified/effect-size-table.csv`, **27 rows changed** — far more than the 12 the report says were audited:

- **Three rows labeled `verified` (no correction) were in fact changed:** S005 (n 100→198, counts 87/86→172/170), S026 (100→4488, 82/74→3680/3321), S030 (100→1221, 87/86→1062/1050). The verification report explicitly says each was "flagged but **not** corrected" and is not in its corrections table — yet the analytic file rescaled them. So the audit log contradicts the audited data, and (for S005 at least) the row should be "verified-corrected," not "verified."
- **~18 rows labeled `unaudited` were also rescaled** from the n=100 placeholder to real benchmark sizes (e.g., S010 100→500, S016 100→581, S018 1273→1000, S021 100→570, S023 100→20, S024 100→302, S033 100→198, S035 100→824, S037 100→419, S039 100→65). "Unaudited" therefore does **not** mean "unchanged since extraction" — an undocumented denominator-correction pass touched most of the table.

The clean "12 audited, 6 corrected, 29 unaudited" framing materially understates how much the analytic table was edited after extraction. (Reassuringly, because these edits preserved the reported percentages, they do not change effect *directions* — but they do change precision/weights, and the provenance is opaque.) **Fix:** add a one-line note per changed row to the verification report (or a "denominator source" provenance column), and relabel S005/S026/S030 honestly.

### V2. The verification report disagrees with the final data on summary counts

`verification-report.md` §4 states "22/41 (53.7%) high RoB" and "only 8 studies controlled compute parity." The final files give **25/41 high (61%)** (`risk-of-bias.csv`) and **9** compute-parity "yes" (`effect-size-table.csv`). The *report's* numbers (25/61%, 9) match the data and are correct; the *audit artifact it cites* is stale. Refresh it, or the auditability claim is undercut by its own appendix.

### V3. `n-items-source = "exact"` conflicts with `audit-status = "unaudited"`

Several rows are tagged "exact" denominators yet "unaudited" *and* had their denominators changed from extraction (S010, S016, S018, S021, S023, S024, S033, S037, S039). If "exact" means "confirmed against the paper," that implies an audit; the combination is contradictory and inflates the apparent count of trustworthy denominators (28 "exact"). Clarify what "exact" certifies for an unaudited row.

---

## Minor issues

- **m1. Figure 6 is missing.** Figures run 1, 2, 3, 4, 5, **7**, F1 — the funnel plot is labeled "Figure 7" with no Figure 6. Renumber.
- **m2. "Treated as independent binomial counts … likely underestimates uncertainty" — direction is dubious.** For *paired* benchmark data (same items, positively correlated arms), analyzing as independent binomials typically *over*states the within-study variance (conservative). The genuine under-estimation comes from unmodeled dependency among multiple effect sizes per paper (already noted in §2.5). The blanket sentence conflates the two and likely has the within-study direction backwards. Reword to separate the two effects.
- **m3. `n-agents` is used as a meta-regression moderator despite being declared unreliable** (§2.3 calls it "known to be unreliable"; the verification report recommends not using it without re-verification). Harmless to the R² = 0% conclusion, but inconsistent — drop it from Table F1 or caveat it at the regression.
- **m4. The verifier-critic subgroup CI [−8.41, 10.43]** (Table 4, k=2; OR from 0.0002 to ~34000) is so uninformative it distracts even when labeled "descriptive only." Consider suppressing the interval and showing only k and the point estimate.
- **m5. Liang2024 / Tang2024 are dated by venue year** (EMNLP/ACL-Findings 2024) over a 2023 arXiv posting — defensible, but be consistent (Du2023 is dated by arXiv).
- **m6. Egger's second author** is conventionally "Davey Smith" (hyphenless surname "Davey Smith"); the current "Smith, G. D." is a common but technically wrong split. Cosmetic.

---

## What is solid (and should not be touched)

- The entire random-effects pipeline reproduces exactly (see §"What I verified"). HKSJ variance floor `max(1, s²_HK)`, fixed-effect Cochran's Q held constant across estimators, PI on t(k−2), conditional-REML + Knapp–Hartung meta-regression, partition-of-Q between-group test, merge-rare subgroups summing to k=41, leave-one-out re-estimating τ² — all implemented correctly and honestly caveated.
- All ~16 methodological citations verified correct; all foundational LLM citations correct; the v5 MetaGPT ("…Schmidhuber") and ChatDev ("…Sun") fixes held.
- All 10 "verified" included studies resolve to real arXiv papers matching their descriptions (Ophth2026 = arXiv:2603.21447 is real, dated 22 Mar 2026 — in the past relative to the 29 May 2026 submission).
- The "no prior quantitative meta-analysis" hedge is defensible; the Cohen's-*h* threshold usage (0.2/0.5/0.8) is standard and correctly attributed to Cohen (1988).
- The report's self-skepticism — danger boxes, GRADE "Very Low," compute-parity framing, the explicit "the spreadsheet is the problem, not the model" stance — is appropriate and, for a course project, exemplary.

---

## Prioritized fix list for v7

1. **(M1)** Add pooled RD and pooled Cohen's *h* to the pipeline under one stated convention; report the true values; fix the notebook summary (h ≠ 0.08 as displayed) and the A1 *h* column; correct or remove the "≈2 pp / h≈0.05" compute-parity gloss (true weighted RD ≈ 5 pp, *h* ≈ 0.10).
2. **(M2)** Add full references for all 41 included studies (Appendix); mark S013/S027 as unlocatable.
3. **(M3)** Fix the Guo (2024) reference; correct the Sprague and MedAgents claims; rename the Xue2025 key.
4. **(M4)** Make accuracy-only (k=37) the primary analysis, or clearly demote S040.
5. **(V1–V3)** Reconcile the verification report with the verified data; relabel S005/S026/S030; refresh the stale 22/8 counts; resolve the "exact" + "unaudited" contradiction.
6. **(m1–m6)** Renumber Figure 6; reword the independence/uncertainty sentence; handle `n-agents`; tidy the verifier-critic CI and minor citation polish.

**Bottom line:** The model is not the problem and never was — the math is clean and reproducible. The problem in v6 is the *connective tissue*: hand-typed absolute-effect numbers that the code does not produce (and in the *h* case actively contradicts), an incomplete bibliography for the included studies, four citation/claim slips, and a verification trail that no longer matches the data it certifies. Close those and v7 is a strong submission.
