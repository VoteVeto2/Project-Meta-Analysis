# Search notes: agent-4-medical

## Search strategy

Searched via WebSearch across arXiv, ACL Anthology, NeurIPS/AAAI proceedings, npj Digital Medicine, Nature Cancer, PLOS Digital Health, and general academic search.

### Queries used (25+ total)
- MDAgents multi-agent LLM medical reasoning benchmark
- ArgMed-Agents argumentation medical reasoning
- "multi-agent" LLM "clinical decision" MedQA benchmark
- "agent hospital" LLM multi-agent medical simulation
- LLM debate medical reasoning MedQA PubMedQA
- "multi-agent" scientific reasoning LLM benchmark discovery chemistry biology
- "collaborative diagnosis" LLM multi-agent system
- multi-agent drug discovery LLM benchmark
- MedAgents Tang 2024 ACL accuracy
- "mixture of agents" medical LLM MoA healthcare
- multi-agent LLM ophthalmology radiology pathology diagnosis
- "Catfish agent" LLM multi-agent medical
- MedARC adaptive refinement collaboration medical
- MediHive decentralized multi-agent medical
- ClinicalAgents multi-agent orchestration dual-memory
- "multi-agent" neurological clinical reasoning
- orchestrated multi-agent clinical workloads
- MoMA mixture multimodal agents clinical prediction
- rare disease diagnosis multi-agent LLM
- AgentClinic multimodal agent benchmark
- RareAgents autonomous multi-disciplinary rare disease
- Prompt-to-Pill multi-agent drug discovery
- MedAgentsBench thinking models agent medical reasoning
- "multi-agent" verifier/critic medical LLM
- expertise-aware multi-LLM recruitment medical
- enhancing diagnostic capability multi-agents conversational LLM
- counterfactual multi-agent reasoning clinical diagnosis
- SciAgent unified multi-agent scientific reasoning
- multi-agent LLM oncology cancer decision support
- mixed-vendor multi-agent LLM clinical diagnosis
- evaluating multi-agent LLM architectures rare disease
- KG4Diagnosis hierarchical multi-agent knowledge graph

## Yield

26 papers collected, spanning 2024-2026.

### Year distribution
- 2024: 5 papers (MDAgents, MedAgents, ArgMed-Agents, AgentClinic, DrugAgent)
- 2025: 12 papers (Catfish Agent, MedARC, Gibbons Council, Chen MAC, MAM, Bao EMRC, Ferber oncology, RareAgents, SciAgents, SciAgent, MoMA, Neuro)
- 2026: 9 papers (MediHive, Charney orchestrated, Ophthalmology council, MedLA, MixedVendor, ClinicalAgents, You counterfactual, MedCollab, Topologies)

### Architecture distribution
- Debate/discussion: 11
- Hierarchy/orchestration: 7
- Cooperation: 4
- Role-play: 3
- Verifier-critic: 1
- MoA: 1

### Benchmarks covered
- MedQA: 6 papers
- PubMedQA: 3 papers
- USMLE: 1 paper
- Rare disease: 4 papers
- Clinical prediction/diagnosis: 5 papers
- Oncology: 1 paper
- Scientific olympiads: 1 paper
- Drug discovery: 1 paper
- Ophthalmology: 1 paper
- Neurology: 1 paper
- Multimodal medical: 2 papers

## Papers with direct single-agent vs multi-agent numerical comparisons
- Kim2024 (MDAgents): 83.9 vs 79.7 on MedQA
- Tang2024 (MedAgents): 86.7 vs 80.6 avg across 9 datasets
- MediHive2026: 84.3 vs 77.0 on MedQA
- MedARC2025: 77.2 vs 72.9 on PubMedQA
- Charney2026: 90.6 vs 73.1 at 5 tasks
- Ophth2026: 96.0 vs 86.5 (proprietary fast)
- MedLA2025: 41.7 vs 30.6 on MedDDx-Expert (8B)
- Bao2025 (EMRC): 74.45 vs 71.76 on MMLU-Pro-Health
- Ferber2025: 87.2 vs 30.3 completeness on oncology
- Topologies2026: 50.0 vs 48.5 on rare disease

## Coverage gaps

1. **Chinese-language medical benchmarks**: Several papers test on Chinese medical exams but were excluded due to language-specific scope.
2. **Radiology-specific multi-agent**: Found reviews but few papers with direct SA vs MA numerical comparisons.
3. **Mental health / psychiatry**: Benchmarks exist (PsychiatryBench, LingxiDiagBench) but multi-agent comparison data is sparse.
4. **Genomics / proteomics**: BixBench exists for computational biology agents but lacks direct MA vs SA comparisons.
5. **Prompt-to-Pill**: Excluded because it is a pipeline framework paper rather than a benchmark comparison.
6. **Some papers lack specific numerical results**: ArgMed-Agents, Chen2025 MAC, ClinicalAgents, MAM, MoMA, You2026 do not report easily extractable accuracy numbers in search results.

## Borderline papers (not included)

- **MedAgentsBench** (Tang 2025): Primarily a benchmarking paper for thinking models, not a multi-agent system itself.
- **AI Hospital** (Fan 2024): Multi-agent simulation benchmark but primarily evaluates doctor agents in interactive format rather than comparing MA vs SA.
- **CoMMa** (2026): Game-theoretic multi-agent for oncology; found late, could be added.
- **KG4Diagnosis** (2024): Promising but benchmark still under development at time of search.
- **Prompt-to-Pill** (2025): Pipeline architecture paper, not a benchmark comparison.
- **LLM-MedQA** (2025): Uses case studies, borderline multi-agent.
