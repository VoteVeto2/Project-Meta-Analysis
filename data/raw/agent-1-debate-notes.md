# Agent 1 -- Multi-Agent Debate: Search Notes

## Search strategy

Executed 15+ WebSearch queries across the following axes:

1. **Seed papers**: Du 2023, Smit 2023 ("Should we be going MAD"), ChatEval (Chan 2023)
2. **Named frameworks**: iMAD, ConfMAD, A-HMAD, Free-MAD, MARS, DReaMAD, DOWN, MAD-M2, SDRL, M-MAD, Tool-MAD, D2D, MAD-Fact, Debate4MATH, M3MAD-Bench
3. **Critical/negative results**: "Stop Overvaluing Multi-Agent Debate" (Zhang 2025), "Cost of Consensus" (Bertalanic 2026), "Talk Isn't Always Cheap" (Wynn 2025), Tran & Kiela 2026 (compute parity)
4. **Application domains**: medical, cultural alignment, misinformation detection, translation evaluation, safety evaluation, LLM-as-judge
5. **Mechanisms**: sycophancy/conformity bias, voting vs consensus, memory masking, confidence calibration, belief entrenchment

Queries targeted arXiv, ACL Anthology, NeurIPS/ICML/ICLR proceedings, and Springer. WebFetch was used on 12+ paper pages to extract numerical results from tables.

## Coverage

- **Total papers**: 25
- **Year range**: 2023--2026 (2 from 2023, 2 from 2024, 16 from 2025, 5 from 2026)
- **Papers with numerical MA vs SA comparison**: 18 of 25
- **Papers with "NR" values**: 7 (typically position/analysis papers or papers where full tables required PDF access)

## Venues represented

ICML 2024, ICML 2025, ICLR 2024, ICLR 2026, NeurIPS 2025, ACL 2024, ACL 2025, AAAI 2026, TACL, arXiv preprints

## Key patterns

1. **Foundational MAD (Du 2023)** shows clear gains (GSM8K: 85 vs 77) but uses 3+ agents without compute control.
2. **Compute-parity studies** (Tran 2026, Zhang 2025a, Bertalanic 2026) consistently find SA matches or beats MA when tokens are equalized.
3. **Efficiency-focused MAD** (iMAD, DOWN, MARS) reduce tokens 50--92% while preserving gains, suggesting selective debate is key.
4. **Failure-mode papers** (Wynn 2025, Yao 2025, Bertalanic 2026) identify sycophancy, conformity, and consensus collapse as core risks.
5. **Heterogeneity** is widely identified as the primary driver of debate gains (Zhang 2025a, A-HMAD, ConfMAD).

## Borderline inclusions

| Paper | Decision | Reason |
|-------|----------|--------|
| Debate4MATH (Zhang 2025b) | Included | Uses debate for reward-model training, not pure inference-time MAD, but reports MA vs SA accuracy |
| SDRL (Liu 2026) | Included | Training-time debate preparation, but evaluates debate vs standalone at inference |
| ChatEval (Chan 2023) | Included | Evaluation-focused rather than task-solving, but reports MA vs SA judge accuracy |
| M-MAD (ACL 2025) | Excluded | Translation evaluation; no direct MA vs SA accuracy comparison found in accessible content |
| MAD-Fact (2025) | Excluded | Long-form factuality evaluation; no standard accuracy comparison available |
| Tool-MAD (2026) | Excluded | Fact verification with tool augmentation; insufficient numerical comparison found |
| Epistemic Gain / Aleatoric Cost (2026) | Excluded | Theoretical uncertainty framework; limited empirical MA vs SA comparison |
| Efficient LLM Safety Eval (2025) | Excluded | Safety-specific; no standard accuracy comparison with SA baseline |

## Coverage gaps

- **Non-English venues**: Limited coverage of papers published primarily in Chinese or other languages (e.g., some AAAI/IJCAI workshop papers)
- **Domain-specific MAD**: Medical (e.g., MDAgents), legal, and code-generation MAD papers may exist but were not fully captured
- **Very recent 2026 papers**: May exist on arXiv but not yet indexed in all search engines
- **Negative/null results**: Likely underrepresented due to publication bias; the 3 critical papers found (Zhang 2025a, Tran 2026, Bertalanic 2026) may not capture all null-result studies
- **Compute parity**: Only 10 of 25 papers report compute-controlled comparisons; most MA vs SA comparisons are not token-matched
