# Agent-3 SWE: Literature Search Notes

## Search strategy

Ran 20+ web searches across multiple query formulations targeting:
- Named systems: SWE-Search, AutoCodeRover, CodeR, Agentless, ChatDev, MetaGPT, MapCoder, AgentCoder, MASAI, DEI, Agyn, CodeCoR, CodeSIM, CodeTree, RGD, InfCode, SWE-Debate, DebateCoder, AdaCoder, TraceCoder, Blueprint2Code, SoA, LessonL
- Generic queries: "multi-agent software engineering", "multi-agent code generation benchmark", "collaborative coding agents", "multi-agent programming LLM"
- Venue-targeted queries: arXiv, ACL Anthology, ICLR/NeurIPS/NAACL proceedings, ICSE/ISSTA/FSE

Search domains: arXiv, ACL Anthology, OpenReview, ResearchGate, IEEE Xplore, ACM DL, Frontiers, conference sites.

## Papers collected: 25

### By benchmark type
- SWE-bench (Lite/Verified/500): 10 papers (CodeR, MASAI, AutoCodeRover, Agentless, DEI, SWE-Search, Agyn, InfCode, CodeTree, SWE-Debate)
- HumanEval/MBPP: 13 papers (AgentCoder, MapCoder, MetaGPT, CodeCoR, SoA, CodeSIM, DebateCoder, RGD, Blueprint2Code, AdaCoder, Dong self-collab, Ashrafi eval, LessonL)
- ClassEval: 1 paper (TraceCoder)
- SoftwareDev: 1 paper (ChatDev)

### By architecture
- cooperation: 8
- planner-executor: 5
- verifier-critic: 5
- role-play: 3
- hierarchy: 2
- other: 2

### By year
- 2024: 12
- 2025: 9
- 2026: 4

## Coverage gaps

1. **Single-agent baselines**: Many multi-agent papers compare against prior SOTA multi-agent systems rather than a clean single-agent baseline. Only ~15 of 25 papers report an explicit single-agent number.
2. **Compute parity**: Rarely controlled. Multi-agent systems inherently use more API calls/tokens. Only a few papers (SWE-Search, Agyn, CodeTree, SoA, AdaCoder) make fair compute-matched comparisons.
3. **Benchmark fragmentation**: SWE-bench and HumanEval ecosystems are largely separate. Few papers report on both, making cross-paper comparison difficult.
4. **Numerical extraction**: Some papers report only relative improvements (e.g., "+23% relative") rather than absolute numbers. Some values marked NR in the CSV.

## Borderline papers (included but flagged)

- **AutoCodeRover (Zhang2024)**: Primarily a single-agent system, but included because it serves as the SA baseline for CodeR and uses iterative multi-step search.
- **Agentless (Xia2024)**: Explicitly not multi-agent -- included as the key single-agent baseline that many MA papers compare against.
- **LessonL (Liu2025)**: Multi-agent lesson-sharing framework, but specific code-generation numbers were not extractable from search results.
- **SWE-Debate (Yang2025)**: Accepted at ICSE 2026 but specific resolve-rate numbers not found in search results.
- **Ashrafi2025**: Systematic evaluation paper rather than a new system; compares MA collaboration strategies across 19 LLMs.

## Borderline papers (excluded)

- **MARS (Wang2025)**: Multi-agent review system for general reasoning (MMLU/GPQA/GSM8K), not code-specific.
- **CVCP (2025)**: Cross-verification for competitive programming. Included domain is code but Elo-based evaluation makes it hard to compare with pass@1/resolve-rate metrics.
- **Chun2025 MAD analysis**: Empirical study of multi-agent debate for code summarization/translation, not code generation. Uses BLEU/ROUGE, not pass@1.
- **MultiAgentBench**: General multi-agent evaluation benchmark, not code-focused.

## Recommendations for next steps

1. Read full PDFs for papers where only relative improvements were found to extract absolute numbers.
2. Check whether ChatDev reports function-level HumanEval/MBPP results (the original paper focuses on software project generation).
3. Look for additional 2025-2026 papers from ICSE 2026, FSE 2025, ASE 2025 proceedings.
4. Consider adding papers on multi-agent test generation (e.g., TestPilot multi-agent variants) if they report code correctness metrics.
