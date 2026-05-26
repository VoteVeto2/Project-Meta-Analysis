# Search notes: cooperative and hierarchical multi-agent LLM architectures

## Search strategy

Searched WebSearch with 20+ queries covering:
- Named frameworks: AutoGen, MetaGPT, ChatDev, CAMEL, AgentVerse, MoA
- Architecture types: planner-executor, hierarchical agents, role-playing agents
- Task domains: code generation, reasoning/debate, software development
- Critique/benchmark papers: compute-parity comparisons, MAD evaluation studies
- Venues targeted: arXiv, ACL Anthology, ICLR/ICML/NeurIPS/EMNLP/COLM proceedings

## Coverage summary

- **24 papers** collected, spanning 2023--2026
- Year distribution: 2023 (1), 2024 (13), 2025 (7), 2026 (3)
- Architecture distribution: cooperation (16), hierarchy (4), role-play (3), moa (1)
- Papers with both MA and SA numerical values: 12
- Papers with SA baseline reported but only relative or NR values: 8
- Papers with no direct SA comparison: 4

## Key patterns

1. **Code generation** is the domain with the strongest MA gains (AgentCoder 96.3% vs 90.2% SOTA; MapCoder 93.9% on HumanEval; MetaGPT 85.9% vs 67% GPT-4 alone).
2. **Multi-agent debate** shows mixed results: Du2024 shows clear gains on GSM8K, but Zhang2025b and Tran2026 argue gains disappear under compute parity or strong single-agent baselines.
3. **Hierarchical architectures** (MetaGPT, TalkHier, SWE-Search, MLPO) show consistent improvements but use more compute.
4. **MoA** (Wang2024) is a distinctive architecture showing open-source LLMs can surpass GPT-4o via layered aggregation.

## Coverage gaps

- **AutoGen**: No standalone empirical paper found comparing multi-agent AutoGen vs single-agent on benchmarks with controlled conditions. AutoGen is primarily a framework; most evaluation papers use it as infrastructure rather than as the subject.
- **CrewAI / LangGraph**: Popular frameworks but lack peer-reviewed benchmark papers comparing MA vs SA.
- **Embodied / robotics tasks**: Limited coverage; EmCoop (2025) exists but was not included as it focuses on embodied cooperation rather than LLM reasoning/coding.
- **Production/enterprise settings**: AgentArch (ServiceNow) evaluates enterprise tasks but the search did not yield exact SA vs MA accuracy numbers from the paper.
- **Non-English benchmarks**: All papers use English-language benchmarks except Liang2024 which includes Chinese translation.

## Borderline papers not included

- **PEAR** (arXiv 2510.07505): Planner-executor robustness benchmark. Focuses on adversarial robustness rather than MA vs SA performance comparison. Included search notes but excluded from CSV.
- **HieraMAS** (arXiv 2602.20229): Optimizes LLM mixtures and topology in hierarchical MAS. Promising but very recent (Feb 2026) with limited detail retrievable from search.
- **Exchange-of-Thought** (arXiv 2312.01823): Cross-model communication framework. Could not retrieve specific accuracy numbers from search.
- **LLM Harmony** (arXiv 2401.01312): Two-agent expert-evaluator setup. Lacks clear single-agent baseline comparison.
- **Self-Organized Agents** (arXiv 2404.02183): 5% Pass@1 improvement over Reflexion on HumanEval. Borderline due to small gain; could be added if more papers are needed.

## Compute parity assessment

Only 4 papers explicitly control for compute parity (Tran2026, Zhang2025b, M3MAD-Bench, Abdelnabi2025). Most papers compare MA systems that use significantly more LLM calls/tokens than the SA baseline. This is a critical methodological limitation noted by Tran2026 and Zhang2025b.
