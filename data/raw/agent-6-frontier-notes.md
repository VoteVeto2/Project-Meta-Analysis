# Agent 6: Frontier-Model Paradox -- Search Notes

## Search strategy

### Queries executed (WebSearch, May 2026)

1. `Claude Code SWE-bench Verified benchmark results 2025 2026`
2. `Anthropic "Opus 4.5" OR "Opus 4.6" model benchmarks agentic coding`
3. `"frontier model" multi-agent diminishing returns single-agent performance`
4. `multi-agent vs single-agent LLM comparison GPT-4o Claude stronger model 2025`
5. `Anthropic Claude Code terminal-bench benchmark 2025 2026 results`
6. `"scaling agents" vs "scaling model" LLM multi-agent performance paper 2024 2025`
7. `arxiv "multi-agent" "single agent" LLM benchmark comparison coordination overhead 2025`
8. `Anthropic system card Claude Opus 4.5 4.6 agentic benchmark results`
9. `"single-agent LLMs outperform multi-agent" reasoning token budget Tran Kiela 2025`
10. `"AgentArch" enterprise benchmark single-agent multi-agent comparison arxiv 2025`
11. `SWE-bench Claude Opus 4 single agent vs multi-agent software engineering 2025`
12. `"beyond the strongest LLM" multi-turn multi-agent orchestration arxiv 2025`
13. `MASEval multi-agent evaluation benchmark systems arxiv 2026`
14. `"single agent or multi-agent" "why not both" arxiv 2025 LLM frontier`
15. `Claude Code agentic coding agent engineering SWE-bench Anthropic blog 2025`
16. `"MultiAgentBench" evaluating collaboration competition LLM agents arxiv 2025`
17. `"Silo-Bench" distributed coordination multi-agent LLM systems arxiv 2026`
18. `GPT-4o GPT-4.5 multi-agent single-agent comparison benchmark 2025 paper`
19. `"APEX-SWE" agentic coding benchmark arxiv 2025 2026`
20. `SWE-Search Monte Carlo Tree Search software agents single agent arxiv 2024`
21. `"auto-scaling" multi-agent LLM dynamic integration agents 2025 paper`
22. `LLM debate multi-agent diminishing returns model capability improvement arxiv 2024 2025`
23. `Claude 3.5 Sonnet SWE-bench Verified Anthropic benchmark October 2024 raising the bar`
24. `"SWE-bench" original paper Jimenez 2024 arxiv benchmark`
25. `"debate only when necessary" adaptive multiagent collaboration efficient LLM reasoning arxiv 2025`
26. `Anthropic Claude 4 model card blog benchmark results May 2025`
27. `"should we be going MAD" multi-agent debate strategies LLMs arxiv 2024`
28. `OpenAI GPT-4o system card agentic benchmark results 2024`
29. `"featurebench" benchmarking agentic coding arxiv 2026`
30. `"SWE-ABS" adversarial benchmark inflated success rates test-based arxiv 2026`
31. `MAESTRO multi-agent evaluation suite testing arxiv 2026`
32. `"illusion of diminishing returns" measuring long horizon execution LLMs arxiv 2025`
33. `Claude Opus 4.5 system card November 2025 Anthropic benchmarks WebArena MCP-Atlas`
34. `"towards adaptive scalable robust coordination LLM agents" dynamic ad-hoc networking arxiv 2026`
35. `"SWE-Compass" unified evaluation agentic coding abilities LLM arxiv 2025`

### Source types covered

- Anthropic system cards and blog posts (4 items)
- Peer-reviewed papers at ICLR, ICML, ACL, ICML (6 items)
- arXiv preprints (14 items)
- Industry technical reports and blog posts (2 items)

## Coverage of the frontier-model paradox hypothesis

### Direct evidence FOR the paradox (stronger models -> less MAS benefit)

| Paper | Key finding |
|-------|-------------|
| Tran & Kiela 2026 | Under equal token budgets, single-agent LLMs outperform multi-agent on multi-hop reasoning; information-theoretic proof via Data Processing Inequality |
| Kim et al. 2025 | Coordination yields diminishing returns once single-agent baseline exceeds ~45% success rate |
| Chen et al. 2026 | Explicitly states MAS is a workaround for LLM limits that becomes less needed as models improve; frontier LLMs mitigate limitations that motivated MAS |
| Smit et al. 2024 | MAD does not reliably outperform self-consistency or ensembling; simpler single-agent methods match or beat debate |
| Eo et al. 2025 | Most queries don't need multi-agent debate; selective activation (DOWN) achieves 6x efficiency with same performance |
| Li et al. 2026 | Homogeneous agent scaling shows strong diminishing returns; marginal gain collapses toward zero |
| Qian et al. 2024 | Majority voting improves by only 0.9% and plateaus at ~8 agents |
| Sinha et al. 2025 | Small single-step accuracy gains compound exponentially for long-horizon tasks; larger models >> smaller models |
| SiloBench 2026 | Coordination overhead eliminates parallelization gains at scale; Communication-Reasoning Gap |
| MAESTRO 2026 | High run-to-run variance in MAS undermines reliability argument |

### Evidence AGAINST or NUANCING the paradox

| Paper | Key finding |
|-------|-------------|
| Xiao et al. 2025 | Orchestration still matches or slightly exceeds strongest single model on GPQA/IFEval/MuSR |
| FeatureBench 2026 | Even frontier Claude 4.5 Opus achieves only 11% on complex feature development; room for MAS help |
| APEX-SWE 2026 | Frontier models top out at 40.5% on cross-system integration tasks; hard tasks remain |
| MultiAgentBench 2025 | GPT-4o-mini outperforms larger models in MAS; model size alone doesn't determine MAS effectiveness |
| SWE-ABS 2026 | Inflated SWE-bench scores mean frontier single-agent progress may be overstated |
| AgentArch 2025 | Model-specific architectural preferences; no one-size-fits-all; some models benefit more from MAS |

### Frontier single-agent trajectory (SWE-bench Verified)

This progression illustrates how rapidly single-agent performance has improved:

| Model | Date | SWE-bench Verified |
|-------|------|--------------------|
| GPT-4 (initial) | Oct 2023 | 1.96% |
| Claude 3.5 Sonnet (upgraded) | Oct 2024 | 49.0% |
| Claude Opus 4 | May 2025 | 72.5% |
| Claude Opus 4.5 | Nov 2025 | 80.9% |
| Claude Opus 4.6 | Feb 2026 | 80.8% |
| Claude Opus 4.7 | ~Apr 2026 | 87.6% |
| Claude Mythos Preview | Apr 2026 | 93.9% |

This 1.96% -> 93.9% trajectory over ~30 months is the strongest empirical illustration of the frontier-model paradox: tasks that once demanded complex multi-agent scaffolding are now handled by a single model call.

## Gaps and limitations

1. **Compute-parity controls are rare.** Only Tran & Kiela 2026 and Smit et al. 2024 rigorously control for compute. Most comparisons are confounded by unequal token budgets.

2. **Task-type dependency.** The paradox holds strongly for reasoning, bug-fixing, and Q&A but may not hold for complex feature development (FeatureBench), cross-system integration (APEX-SWE), or distributed coordination (Silo-Bench).

3. **No longitudinal multi-agent study.** No paper tracks the same MAS architecture across multiple model generations (e.g., GPT-3.5 -> GPT-4 -> GPT-4o -> GPT-5) to directly measure the shrinking gap. This would be the ideal study design for the paradox.

4. **SWE-bench score inflation.** SWE-ABS 2026 shows ~20% of "solved" cases are semantically incorrect. This tempers claims about frontier single-agent capabilities.

5. **Missing OpenAI agentic benchmark data.** GPT-4o system card (2024) did not report SWE-bench or similar agentic coding benchmarks. GPT-5 data is mostly from third-party benchmarks.

6. **Limited coverage of Gemini models.** Google DeepMind model cards with agentic benchmarks were not found in the search.

7. **No formal "frontier-model paradox" term in literature.** The concept exists across multiple papers but no single paper coins or formalizes this term. The meta-analysis can contribute by naming and formalizing this pattern.

## Recommendations for the meta-analysis

1. **Define the paradox formally:** propose a threshold-based definition (e.g., "when single-agent baseline exceeds X%, multi-agent marginal gain drops below Y%") drawing on Kim et al. 2025's ~45% threshold finding.

2. **Compute-parity as moderator:** the paradox is strongest under compute parity (Tran & Kiela 2026). Without controlling for compute, MAS can still outperform by simply using more tokens.

3. **Task decomposability as moderator:** the paradox is strongest for monolithic reasoning tasks and weakest for naturally decomposable tasks (Kim et al. 2025: +80.8% on decomposable financial reasoning).

4. **Use the SWE-bench trajectory** (1.96% -> 93.9%) as a case study for how model improvement eliminates the multi-agent advantage over time.

5. **Acknowledge the ceiling:** FeatureBench (11%) and APEX-SWE (40.5%) show that even frontier models have significant room to grow on complex real-world tasks, leaving space for MAS to add value.
