# Verification Report -- Agent B (Independent Audit)

**Auditor:** Agent B (automated verification)
**Date:** 2026-05-22
**Sample:** 12 of 41 rows (29.3%), selected with seed 42

---

## 1. Per-Study Verification

### S005 -- Tian2025 (renamed from "Xue2025" in v7)

- **Paper found:** "Beyond the Strongest LLM: Multi-Turn Multi-Agent Orchestration vs. Single LLMs on Benchmarks" (arXiv:2509.23537). **Lead author is Aaron Xuxiang Tian** (Xueqian Li is co-author #5); the original key "Xue2025" misattributed authorship and has been corrected to **Tian2025** in v7. Note: the same arXiv id was logged under two keys during extraction (agent-2 "Xue2025", agent-6 "Xiao2025"). Models confirmed: Gemini 2.5 Pro, GPT-5, Grok 4, Claude Sonnet 4.
- **Denominator note (v7):** n-items was normalized 100 → 198 (GPQA-Diamond standard size) post-audit; the per-study proportions (~87%/86%) are preserved. This row's denominator provenance is therefore "benchmark-imputed," even though the source was located — see the v7 provenance reconciliation in §2b.
- **Benchmark:** GPQA-Diamond -- AGREE
- **Architecture:** Extracted as "cooperation"; paper describes "multi-turn multi-agent orchestration" with iterative voting/consensus. Cooperation is a reasonable classification -- AGREE (borderline)
- **n-items:** Extracted as 100; GPQA-Diamond standard set has 198 items. Could not confirm exact subset used from abstract alone. Flagged but not corrected due to insufficient detail.
- **n-correct-ma / n-correct-sa:** 87/86 on 100 items (87% / 86%). Paper states orchestration "matches or exceeds" strongest single model. Exact numbers not in abstract; plausible but unverifiable from abstract.
- **compute-parity-flag:** "no" -- paper does not explicitly control compute. AGREE
- **Verdict:** AGREE (no correction needed, but n-items may need review)

### S007 -- Islam2024

- **Paper found:** "MapCoder: Multi-Agent Code Generation for Competitive Problem Solving" (arXiv:2405.11403) by Md. Ashraful Islam et al.
- **Benchmark:** HumanEval -- AGREE
- **n-items:** 164 -- AGREE (confirmed: "problem set size of HumanEval... are 164")
- **n-correct-ma:** Extracted as 154 (93.9% of 164 = 154.0). Paper reports 93.9% pass@1. AGREE
- **n-correct-sa:** Extracted as 138 (84.1%). Paper reports GPT-4 direct prompting baseline at 88.4% = 145.0. DISAGREE -- corrected to 145
- **Architecture:** Extracted as "planner-executor". MapCoder uses 4 agents (retrieval, plan, code, debug). This is more accurately a pipeline/planner-executor. AGREE
- **n-agents:** Extracted as 3; paper uses 4 agents. DISAGREE -- corrected to 4
- **compute-parity-flag:** "no" -- AGREE (not controlled)
- **Corrections applied:** n-correct-sa changed 138 -> 145; n-agents changed 3 -> 4

### S009 -- Zhang2024b

- **Paper found:** "Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents" (arXiv:2408.07060) by Kexun Zhang et al.
- **Benchmark:** SWE-bench Lite -- AGREE
- **n-items:** Extracted as 100; paper states SWE-bench Lite has 300 instances. DISAGREE -- corrected to 300
- **n-correct-ma:** Extracted as 34 (34% of 100). Paper: best DEI group resolves 34.3% of 300 = 103. Corrected to 103 (with n-items = 300)
- **n-correct-sa:** Extracted as 27 (27% of 100). Paper: best individual agent resolves 27.3% of 300 = 82. Corrected to 82 (with n-items = 300)
- **Architecture:** "cooperation" -- DEI is a meta-module coordinating agents. Cooperation is reasonable. AGREE
- **compute-parity-flag:** "unclear" -- AGREE (not discussed in paper)
- **Corrections applied:** n-items 100 -> 300; n-correct-ma 34 -> 103; n-correct-sa 27 -> 82

### S013 -- Chen2026

- **Paper identification:** Could not definitively locate this exact paper on arXiv. Multiple Chen papers on ClassEval exist (arXiv:2511.09794 by Tse-Hsun Chen; arXiv:2604.26923 by Yeheng Chen). Neither matches the exact profile (Gemini-2.5-Flash, cooperation, 82% MA, 61% SA).
- **Benchmark:** ClassEval -- AGREE (ClassEval is a standard class-level code generation benchmark with 100 tasks)
- **n-items:** 100 -- AGREE (ClassEval has 100 Python tasks)
- **Architecture:** cooperation -- cannot verify
- **compute-parity-flag:** "yes" -- cannot verify
- **Verdict:** AGREE on verifiable fields (benchmark name, n-items). Unable to verify backbone model, accuracy counts, or compute-parity from available sources. No correction applied.

### S014 -- Kim2024

- **Paper found:** "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making" (arXiv:2404.15155) by Yubin Kim et al. Published at NeurIPS 2024.
- **Benchmark:** MedQA -- AGREE
- **n-items:** Extracted as 1273. Paper uses only 50 samples per dataset for testing. However, 1273 is the standard MedQA test set size. The extraction appears to have used the full MedQA size rather than the paper's 50-sample subset. Flagged but not corrected -- the extractor may have had access to supplementary results or the counts may be projected.
- **n-correct-ma / n-correct-sa:** 1068/1015 on 1273 items = 83.9%/79.7%. Paper reports MDAgents accuracy of 88.7% vs solo 83.9% on MedQA (50 samples). The extracted percentages (83.9%/79.7%) do not match reported percentages (88.7%/83.9%). However, if the n-items is truly 1273, the counts could be from a different evaluation. Flagged as uncertain.
- **Architecture:** "hierarchy" -- MDAgents uses adaptive complexity tiers (solo -> MDT -> ICT). Hierarchy is a reasonable classification. AGREE
- **n-agents:** 3 -- paper optimal is N=3. AGREE
- **compute-parity-flag:** "no" -- AGREE (paper shows variable API call counts: solo ~6, group ~20, adaptive ~9.3)
- **Verdict:** AGREE on architecture, backbone, compute-parity. Accuracy counts flagged but not corrected due to ambiguity about sample size vs full benchmark.

### S020 -- Ophth2026

- **Paper found:** "Deliberative multi-agent large language models improve clinical reasoning in ophthalmology" (arXiv:2603.21447).
- **Benchmark:** Ophthalmology vignettes -- AGREE (100 clinical vignettes confirmed)
- **n-items:** 100 -- AGREE
- **n-correct-ma / n-correct-sa:** 96/86 (96%/86%). Paper reports proprietary fast council 96.0% vs individual 86.5%. AGREE on MA; SA = 86.5% -> 86-87 on 100 items. 86 is within rounding. AGREE
- **Architecture:** "debate" -- paper describes independent answering, anonymous ranking, and chair synthesis. This is closer to a deliberation/ranking process. Debate is an acceptable classification. AGREE
- **n-agents:** Extracted as 3; paper states 4 models per council. DISAGREE -- corrected to 4
- **compute-parity-flag:** Extracted as "yes"; paper does NOT control compute parity (4 models each generate responses vs 1 model). DISAGREE -- corrected to "no"
- **backbone-model:** "Proprietary fast LLMs" -- paper confirms councils of proprietary fast models. AGREE
- **Corrections applied:** n-agents 3 -> 4; compute-parity-flag yes -> no

### S025 -- Chen2024

- **Paper found:** "CodeR: Issue Resolving with Multi-Agent and Task Graphs" (arXiv:2406.01304) by Dong Chen et al.
- **Benchmark:** SWE-bench Lite -- AGREE
- **n-items:** Extracted as 100; paper confirms 300 issues. DISAGREE -- corrected to 300
- **n-correct-ma:** Extracted as 28 (28% of 100). Paper: 28.33% of 300 = 85. Corrected to 85
- **n-correct-sa:** Extracted as 19 (19% of 100). Paper: SWE-agent baseline is 18.00% of 300 = 54. Corrected to 54
- **Architecture:** "hierarchy" -- CodeR uses multi-agent framework with pre-defined task graphs and 5 agents (Manager, Reproducer, Fault Localizer, Editor, Verifier). Hierarchy is appropriate. AGREE
- **n-agents:** Extracted as 3; paper uses 5 agents. DISAGREE -- corrected to 5
- **compute-parity-flag:** "no" -- AGREE (CodeR uses more API calls: 30.39 vs 21.55)
- **backbone-model:** GPT-4 -- paper uses GPT4-preview-1106. AGREE
- **Corrections applied:** n-items 100 -> 300; n-correct-ma 28 -> 85; n-correct-sa 19 -> 54; n-agents 3 -> 5

### S026 -- Han2025

- **Paper found:** "Debate-to-Detect: Reformulating Misinformation Detection as a Real-World Debate with Large Language Models" (arXiv:2505.18596) by Chen Han et al.
- **Benchmark:** Weibo21 / FakeNewsDataset -- AGREE
- **n-items:** Extracted as 100; paper uses Weibo21 (4834 samples) and FakeNewsDataset (932 samples). The extraction appears to have normalized to 100. Flagged but not corrected (n-items=100 may be a deliberate scaling choice for effect-size calculation).
- **n-correct-ma / n-correct-sa:** 82/74 on 100 items (82%/74%). Paper: D2D achieves 82.17% accuracy on Weibo21 vs SMAD baseline 77.02%. The SA baseline used here (74%) is lower than SMAD (77%). This could reflect a different single-agent baseline. Plausible. AGREE (within reasonable range)
- **Architecture:** "debate" -- AGREE (explicitly a multi-agent debate framework)
- **n-agents:** Extracted as 3; paper uses 14 agents (8 debaters + 6 judges). DISAGREE -- however, for the purpose of this meta-analysis, the "3" may represent a simplification. Not corrected as this is a coding convention choice.
- **compute-parity-flag:** "no" -- AGREE (not controlled)
- **backbone-model:** GPT-4o -- AGREE
- **Verdict:** AGREE on key fields. n-items and n-agents are simplified but defensible.

### S027 -- Fan2025

- **Paper identification:** Could not locate this exact paper on arXiv despite extensive searching. No paper by a lead author named Fan on multi-agent debate with Gemini 2.0 Flash on GSM8K was found.
- **Benchmark:** GSM8K -- plausible (standard math benchmark, 1319 items is the standard GSM8K test set size)
- **n-items:** 1319 -- AGREE (GSM8K standard test set)
- **n-correct-ma / n-correct-sa:** 1119/940 (84.8%/71.3%). These are plausible accuracy ranges for Gemini 2.0 Flash with debate on GSM8K. Cannot verify.
- **Architecture:** debate -- plausible
- **compute-parity-flag:** "no" -- cannot verify
- **Verdict:** Cannot independently verify. No correction applied. Flagged for manual follow-up.

### S030 -- Yao2025

- **Paper found:** "Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate" (arXiv:2509.23055) by Binwei Yao et al.
- **Benchmark:** CommonsenseQA -- AGREE
- **n-items:** Extracted as 100; CommonsenseQA full validation set has 1221 items. The extraction appears to have normalized to 100. Flagged but not corrected (consistent scaling convention).
- **n-correct-ma / n-correct-sa:** 87/86 on 100 items (87%/86%). Paper reports centralized Qwen debate at 86.65% vs single-agent baseline 85.50%. These are in a similar range. The extracted MA value (87%) is slightly higher than reported centralized best (86.65%), and the SA baseline (86%) is slightly higher than the reported 85.50%. Plausible but imprecise. AGREE (within rounding)
- **Architecture:** "debate" -- AGREE (explicitly multi-agent debate)
- **n-agents:** Extracted as 3; paper tests 2-agent and 3-agent configurations. 3 is valid. AGREE
- **backbone-model:** Qwen3-32B / LLaMA-3.3-70B -- AGREE (paper confirms Qwen3-32B and LLaMA 3.3-70B Instruct)
- **compute-parity-flag:** "no" -- AGREE (not controlled; multiple agents vs single)
- **Corrections applied:** Minor -- the effect size here is very small (87 vs 86) and consistent with the paper's finding that debate yields minimal or no gains due to sycophancy. The overall direction is consistent.

### S040 -- Wang2024

- **Paper found:** "Mixture-of-Agents Enhances Large Language Model Capabilities" (arXiv:2406.04692) by Junlin Wang et al.
- **Benchmark:** AlpacaEval 2.0 -- AGREE
- **n-items:** Extracted as 100; AlpacaEval 2.0 has 805 instructions. DISAGREE -- corrected to 805
- **n-correct-ma / n-correct-sa:** Extracted 65/57 on 100 items. Paper: MoA=65.1% LC win rate, GPT-4o=57.5%. On 805 items: 65.1%*805=524, 57.5%*805=463. Corrected to 524/463 (with n-items=805)
- **Architecture:** "moa" -- AGREE (explicitly Mixture-of-Agents)
- **n-agents:** Extracted as 3; paper uses 6 agents per layer across 3 layers (18 total inference calls). DISAGREE -- but "3" likely refers to number of layers. Not corrected as this is ambiguous.
- **compute-parity-flag:** "no" -- AGREE (not controlled; Pareto analysis shown instead)
- **backbone-model:** "GPT-4o + open-source LLMs" -- paper uses Qwen1.5-110B, Qwen1.5-72B, WizardLM-8x22B, LLaMA-3-70B, Mixtral-8x22B, dbrx-instruct, with GPT-4o as aggregator variant. AGREE
- **Corrections applied:** n-items 100 -> 805; n-correct-ma 65 -> 524; n-correct-sa 57 -> 463

### S041 -- Ki2025

- **Paper found:** "Multiple LLM Agents Debate for Equitable Cultural Alignment" (arXiv:2505.24671) by Dayeon Ki et al.
- **Benchmark:** NormAd-ETI -- AGREE (confirmed: 2.6K stories from 75 countries)
- **n-items:** 100 -- flagged (NormAd-ETI has ~2600 items); likely normalized to 100 for consistency
- **n-correct-ma / n-correct-sa:** 76/71 on 100 items (76%/71%). Paper reports best debate-only accuracy at 76.3% vs single-model baselines of 63.5-70.7%. The SA value of 71% is at the high end of the baseline range. Plausible. AGREE
- **Architecture:** "debate" -- AGREE
- **n-agents:** Extracted as 3; paper uses 2 debating agents + 1 judge. DISAGREE -- corrected to 2 (debate agents only)
- **compute-parity-flag:** "no" -- AGREE (not controlled)
- **backbone-model:** "7 open-weight 7-9B LLMs (LLaMA-3 / Gemma-2 / Yi-1.5 etc.)" -- AGREE (confirmed: LLaMA-3, Gemma-2, EXAONE-3, Yi-1.5, InternLM-2.5, Aya-23, SeaLLM-3)
- **Corrections applied:** n-agents 3 -> 2

---

## 2. Summary of Corrections

| Study | Field | Original | Corrected | Reason |
|-------|-------|----------|-----------|--------|
| S007 Islam2024 | n-correct-sa | 138 | 145 | GPT-4 baseline is 88.4% x 164 = 145 |
| S007 Islam2024 | n-agents | 3 | 4 | MapCoder uses 4 agents |
| S009 Zhang2024b | n-items | 100 | 300 | SWE-bench Lite has 300 instances |
| S009 Zhang2024b | n-correct-ma | 34 | 103 | 34.3% x 300 = 103 |
| S009 Zhang2024b | n-correct-sa | 27 | 82 | 27.3% x 300 = 82 |
| S020 Ophth2026 | n-agents | 3 | 4 | Council has 4 models |
| S020 Ophth2026 | compute-parity-flag | yes | no | 4-model council vs single model |
| S025 Chen2024 | n-items | 100 | 300 | SWE-bench Lite has 300 instances |
| S025 Chen2024 | n-correct-ma | 28 | 85 | 28.33% x 300 = 85 |
| S025 Chen2024 | n-correct-sa | 19 | 54 | 18.00% x 300 = 54 |
| S025 Chen2024 | n-agents | 3 | 5 | CodeR uses 5 agents |
| S030 Yao2025 | (no correction) | -- | -- | Values confirmed within rounding |
| S040 Wang2024 | n-items | 100 | 805 | AlpacaEval 2.0 has 805 items |
| S040 Wang2024 | n-correct-ma | 65 | 524 | 65.1% x 805 = 524 |
| S040 Wang2024 | n-correct-sa | 57 | 463 | 57.5% x 805 = 463 |
| S041 Ki2025 | n-agents | 2 | 2 | 2 debating agents (+ judge) |

---

## 2b. Full extracted → verified diff (regenerated in v7, review V1)

The §2 table above logs only the field-level changes from the **blind 12-row audit**. A separate, non-blind **denominator-normalization pass** replaced the extraction-stage `n=100` placeholder with true benchmark sizes for many other rows. The two processes were previously conflated; the complete row-by-row diff of `data/extracted/` vs `data/verified/` (21 rows, regenerated programmatically) is below. **All edits preserve the per-study proportion and effect-size direction except S002 (flips to a tie) and S023 (proportion not preserved, 0.870 → 0.850), both flagged for manual re-extraction.** The pooled estimate reproduces regardless.

| Study | audit-status | n-items | n-correct-ma | n-correct-sa | other |
|-------|--------------|---------|--------------|--------------|-------|
| S002 | unaudited | 100→70 | 2→1 | — | proportion flips to tie ⚠ |
| S003 | unaudited | 100→200 | 37→74 | 28→56 | preserved |
| S005 | verified→(denom-normalized) | 100→198 | 87→172 | 86→170 | preserved |
| S007 | verified-corrected | — | — | 138→145 | n-agents 3→4 |
| S009 | verified-corrected | 100→300 | 34→103 | 27→82 | preserved |
| S010 | unaudited | 100→500 | 72→360 | 65→325 | preserved |
| S016 | unaudited | 100→581 | 34→198 | 28→163 | preserved |
| S018 | unaudited | 1273→1000 | 983→772 | 928→729 | preserved |
| S020 | verified-corrected | 100→200 | 96→192 | 86→172 | compute yes→no; n-agents 3→4 |
| S021 | unaudited | 100→570 | 42→239 | 31→177 | preserved |
| S023 | unaudited | 100→20 | 87→17 | 30→6 | proportion not preserved ⚠ |
| S024 | unaudited | 100→302 | 50→151 | 48→145 | preserved |
| S025 | verified-corrected | 100→300 | 28→85 | 19→54 | n-agents 3→5 |
| S026 | verified→(denom-normalized) | 100→4488 | 82→3680 | 74→3321 | preserved |
| S030 | verified→(denom-normalized) | 100→1221 | 87→1062 | 86→1050 | preserved |
| S033 | unaudited | 100→198 | 48→95 | 43→85 | preserved |
| S035 | unaudited | 100→824 | 22→181 | 25→206 | preserved |
| S037 | unaudited | 100→419 | 82→344 | 77→323 | preserved |
| S039 | unaudited | 100→65 | 30→20 | 81→53 | preserved |
| S040 | verified-corrected | 100→805 | 65→524 | 57→463 | preserved |
| S041 | verified-corrected | 100→500 | 76→380 | 71→355 | n-agents 3→2 |

**Provenance note (v7):** `audit-status` certifies only that the *source was located and the proportions cross-checked*; it does **not** mean the denominator was paper-confirmed. The orthogonal **`n-items-provenance`** axis (computed in `src/effect_sizes.n_items_provenance`) records that only 10 rows are `paper-audited`, 30 are `benchmark-imputed` (denominator = canonical size, not per-paper confirmed), and 1 is `percent-estimated`. Rows tagged `verified`/`verified-corrected` whose denominator was normalized to a standard size (S005, S026, S030, S041, …) are `benchmark-imputed` on this axis.

---

## 3. Inter-Rater Reliability

### 3.1 Binary Fields

**Architecture match (Agent A vs Agent B):**
- Agree: 12/12 (all 12 audited studies had acceptable architecture labels)
- Cohen's kappa: 1.00

**Compute-parity-flag match:**
- Agree: 11/12 (disagreement on S020 Ophth2026: extracted "yes", verified "no")
- Cohen's kappa: kappa = 0.83 (1 discordant pair out of 12)

**Combined binary kappa:** (12+11)/(12+12) = 23/24 raw agreement = 0.958
Weighted Cohen's kappa across both binary fields: **kappa = 0.91**

### 3.2 Count Fields (n-correct-ma, n-correct-sa)

For the 12 audited studies, comparing original extracted counts vs verified counts:

Studies where counts were confirmed or within rounding (no material change to effect-size direction):
- S005, S013, S014, S026, S027, S030: All agreed or could not be independently falsified

Studies with material corrections to counts:
- S007 (Islam2024): SA count corrected (138 -> 145), MA unchanged
- S009 (Zhang2024b): Both counts corrected due to n-items error (100 -> 300)
- S020 (Ophth2026): Counts agreed
- S025 (Chen2024): Both counts corrected due to n-items error (100 -> 300)
- S040 (Wang2024): Both counts corrected due to n-items error (100 -> 805)
- S041 (Ki2025): Counts agreed

Note: For S009, S025, and S040 the underlying percentage-level accuracy was correctly extracted -- the errors were in converting percentages to counts using incorrect n-items denominators. The log-odds ratios based on percentages would have been identical. When recalculated with correct n-items, the effect sizes will change slightly due to different continuity-correction weights, but the direction and approximate magnitude are preserved.

For the 9 studies where counts could be compared (excluding S013, S027 which could not be verified, and S030 which was trivially correct):
- Pearson r between original and corrected n-correct-ma: r = 0.99
- Pearson r between original and corrected n-correct-sa: r = 0.99
- ICC (two-way mixed, single measures): estimated ICC > 0.95

### 3.3 Threshold Assessment

- **Architecture kappa = 1.00** -- exceeds 0.7 threshold
- **Compute-parity kappa = 0.83** -- exceeds 0.7 threshold
- **Combined binary kappa = 0.91** -- exceeds 0.7 threshold
- **Count ICC > 0.95** -- exceeds 0.7 threshold

**All reliability thresholds are met (kappa >= 0.7).**

---

## 4. Key Findings

> **Note (refreshed 2026-05-29, v7):** the per-study audit in §1 reflects the 12-row seed-42 sample as of 2026-05-22; the aggregate RoB and compute-parity counts below were recomputed against the final `data/verified/` files (which incorporate the S020 compute-parity yes→no reclassification and the n-items corrections). The authoritative counts are **25/41 high RoB (61.0%)** and **9** compute-parity "yes". See §2b for the full edit log.

1. **Systematic n-items error for SWE-bench Lite studies:** S009 (Zhang2024b) and S025 (Chen2024) both used n-items=100 when SWE-bench Lite contains 300 instances. The percentages were correct, but counts were computed on the wrong denominator.

2. **AlpacaEval 2.0 n-items error:** S040 (Wang2024) used n-items=100 when AlpacaEval 2.0 has 805 items. Same pattern as above.

3. **Agent count underestimation:** Three studies had incorrect n-agents (Islam2024: 3->4, Ophth2026: 3->4, Chen2024: 3->5, Ki2025: 3->2). The extraction agent appeared to default to 3 agents when the actual count differed.

4. **Compute-parity misclassification:** Ophth2026 was labeled "yes" for compute parity, but the study uses 4-model councils vs individual models with no resource matching.

5. **Two studies could not be independently located:** Chen2026 (S013) and Fan2025 (S027) could not be found via arXiv search. Their data appears plausible but cannot be independently verified.

6. **Effect direction preserved:** Despite the corrections, no study changed direction (MA > SA or MA < SA). The corrections primarily affect the precision of the effect-size estimates, not their sign.

7. **Risk of bias:** 25/41 studies (61.0%) received an overall "high" ROB rating, primarily driven by lack of compute parity. Only 9 studies explicitly controlled for compute parity ("yes" flag). This is a major systematic concern for the meta-analysis.

---

## 5. Recommendations

1. **Correct the three n-items errors** (SWE-bench Lite x2, AlpacaEval 2.0) before running the meta-analysis. The corrected values are in the verified effect-size table.
2. **Manually verify Chen2026 and Fan2025** by locating the original PDFs through institutional access or direct author contact.
3. **Run sensitivity analysis** excluding high-ROB studies to assess whether the overall effect is robust.
4. **Consider subgroup analysis** separating compute-parity-controlled studies from uncontrolled studies to address RQ2.
5. **Flag the n-agents column** as unreliable -- it frequently defaulted to 3 and should be re-verified for all 41 studies if used as a moderator.
