# Critical/Null-Result Papers Search Notes

## Search Strategy

### Queries Used (16 distinct query formulations)
1. `"single agent outperforms multi-agent" LLM 2024 2025`
2. `multi-agent LLM "no improvement" OR "not necessary" OR "does not help" single agent baseline`
3. `"echo chamber" OR sycophancy multi-agent LLM debate failure`
4. `"diminishing returns" multi-agent LLM scaling agents`
5. `"multi-agent overhead" OR "coordination cost" LLM agents performance degradation`
6. `arxiv "multi-agent debate" LLM "does not improve" OR "fails to" OR "no significant"`
7. `"more agents is less" OR "more agents worse" OR "agent redundancy" LLM`
8. `multi-agent LLM "equal compute" OR "compute-matched" OR "token budget" single agent`
9. `multi-agent debate "correct to incorrect" answer shift conformity LLM`
10. `multi-agent LLM "mixture of agents" MoA limitation underperform single stronger model`
11. `multi-agent collaboration LLM "negative results" OR "null results" OR "no benefit"`
12. `multi-agent LLM hallucination amplification error propagation cascading failure`
13. `multi-agent LLM code generation "single agent" comparison limitation`
14. `multi-agent LLM "role-playing" failure OR limitation OR "does not scale"`
15. `multi-agent LLM "self-consistency" outperforms debate OR collaboration reasoning`
16. `"Reasoning Trap" information-theoretic bound multi-agent debate failure`

### Sources Covered
- arXiv preprints (primary source)
- OpenReview submissions (ICLR, NeurIPS)
- ACL Anthology
- ICML proceedings
- Semantic Scholar
- ResearchGate

## Key Findings on Publication Bias

### Evidence of Publication Bias
1. **Difficulty of finding null results**: Critical/null-result papers exist but are significantly harder to find than positive-result papers. Most searches for "multi-agent improvement" return dozens of positive claims, while searches for failures require very specific query terms.

2. **Framing bias**: Many papers that find null or negative results frame them as "motivation for improvement" rather than as standalone negative findings. For example:
   - Papers finding MAD underperforms CoT still propose a "fix" (e.g., diversity-aware initialization)
   - Papers documenting failure modes (MAST taxonomy) position themselves as constructive rather than critical
   - Papers showing single-agent sufficiency (OneFlow) still frame multi-agent as the default

3. **Compute-parity gap**: The most damning finding is from Tran & Kiela (2025) and corroborated by the ICLR 2025 blogpost: most published MA vs SA comparisons do NOT control for compute. When compute is equalized, advantages largely disappear. This means a large fraction of the positive-result literature may be confounded.

4. **Recency of critical work**: Nearly all critical papers are from 2025-2026. Before 2025, the literature was almost entirely positive about multi-agent approaches. This suggests the field went through a hype cycle before critical examination began.

### Taxonomy of Failure Modes Found

#### Category 1: Compute-Fairness Failures
- MA advantages disappear under equal token budgets (Tran & Kiela 2025)
- Single agent matches homogeneous MA workflows (Xu et al. 2025)
- MAD fails to outperform self-consistency which is cheaper (Zhang et al. 2025)
- Debate component adds no expected improvement (martingale proof, Choi et al. 2025)

#### Category 2: Communication/Coordination Failures
- Problem drift over debate rounds (Becker et al. 2025)
- Error cascading through agent chains (Xie et al. 2026)
- Communication-Reasoning Gap: agents coordinate but fail to integrate information (Silo-Bench 2026)
- Information loss through communication compression (Ao et al. 2026)

#### Category 3: Social/Conformity Failures
- Sycophancy causing premature consensus (Liu et al. 2025)
- Conformity to incorrect majorities (Zhu et al. 2025, ACL)
- Identity bias (self-bias and peer-sycophancy) in debate (Choi et al. 2025)
- Correct-to-incorrect answer shifts under peer pressure (Wynn et al. 2025)

#### Category 4: Scaling Failures
- Diminishing returns with homogeneous agents (Yang et al. 2026)
- Capability-saturation effect (Li et al. 2024)
- Hidden profile failures worsening at scale (Zhou et al. 2025)
- Selection bottleneck in MoA pipelines (Maryanskyy 2026)

#### Category 5: Theoretical Impossibility Results
- Data Processing Inequality bounds on closed-system reasoning (Tran & Kiela 2025; Shin 2026)
- Delegated networks dominated by centralized Bayes decision makers (Ao et al. 2026)
- Martingale property of debate (Choi et al. 2025)

## Coverage Gaps

1. **Software engineering benchmarks**: Limited critical evaluation specific to SWE-Bench or coding tasks. Most SE papers report positive results; null results may exist but are harder to find.

2. **Tool-use and planning domains**: While Silo-Bench covers coordination, specific tool-use failure comparisons are scarce.

3. **Heterogeneous multi-agent failures**: Most criticism targets homogeneous MA systems. Fewer papers critically examine heterogeneous MA systems, which may reflect a genuine advantage or simply less scrutiny.

4. **Industry/deployment failure reports**: Academic papers dominate. Real-world deployment failure data from industry is essentially absent from the public literature.

5. **Cost-adjusted comparisons**: While compute-parity papers exist, systematic dollar-cost-adjusted comparisons (accounting for API pricing, latency, etc.) are rare.

## Implications for Meta-Analysis

- The meta-analysis MUST control for compute parity. Studies without compute-matched baselines likely overestimate MA benefits.
- Publication bias is strong: the ratio of positive to critical papers is heavily skewed positive, especially pre-2025.
- Funnel plot analysis should show asymmetry if including both positive and critical papers.
- Architecture matters: debate architectures have the most critical examination; cooperation/hierarchy architectures have less scrutiny.
- The 27 papers collected here represent a significant fraction of the total critical literature, suggesting the field's critical mass is still small relative to the positive-result literature.

## Paper Count Summary
- Total critical/null-result papers collected: 27
- Year distribution: 2024 (2), 2025 (17), 2026 (8)
- Venue distribution: arXiv preprint (21), NeurIPS (2), ACL (1), ICML (2), ICLR blogpost (1, not in CSV)
- Architecture focus: debate (15), cooperation (5), hierarchy (1), moa (1), other (5)
