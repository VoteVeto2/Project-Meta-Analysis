# Research Plan v1 — Meta-Analysis of Multi-Agent vs Single-Agent LLM Systems

**Author:** Xinyu Yang (r1020926), KU Leuven, Meta-Analysis (G0B75a)
**Deadline:** 2026-05-31 23:59 (Toledo upload `MA2026_Yang_Xinyu`)
**Target:** 2000–3000-word HTML report + reproducible notebook, NeurIPS-spotlight quality
**Status:** Executable prompt. No literature search or code has run yet.

---

## 1. Question

**RQ1 (primary).** Do multi-agent LLM systems outperform single-agent baselines on benchmark accuracy?
**RQ2 (compute parity).** Under matched compute, does the multi-agent advantage survive?
**RQ3 (frontier-model paradox).** As baselines strengthen (Claude Opus 4.5 → 4.6, Claude Code), does orchestration gain shrink?
**RQ4 (moderators).** Which task properties (decomposability, sequentiality, tool diversity) predict effect direction?

**PICOS.** P = empirical 2023–2026 LLM studies. I = any multi-agent orchestration (debate, cooperation, hierarchy, role-play, verifier-critic, MoA, planner-executor). C = single-agent same backbone. O = accuracy / success-rate proportion. S = within-study head-to-head.

**Exclude.** Classical MARL, position papers, no SA comparator, simulation-only.

**Effect size.** Log odds ratio (primary) + Cohen's *h* (secondary), 0.5 continuity correction for zero cells.

---

## 2. Setup

### 2.1 Folder layout

```
proj-meta/
├── plan/RESEARCH-PLAN-v1.md          # this file
├── pyproject.toml  uv.lock           # uv-managed
├── data/{raw,extracted,verified}/
├── src/                              # Python modules (snake_case files)
│   ├── data_io.py  effect_sizes.py  pooling.py  heterogeneity.py
│   ├── moderators.py  publication_bias.py  sensitivity.py  plots.py  reporting.py
├── notebook/meta-analysis-v1.ipynb   # v2 added in Phase 5
└── report/
    ├── report-v1.html  report-v2.html  report-v2-cn.html
    ├── assets/                       # figures (png + interactive html)
    └── review/review-v1.md  v1-response.md
```

**Naming.** Kebab-case everywhere except Python module files in `src/` (Python import rules). CSV columns and JSON keys: kebab-case.

### 2.2 Toolchain

```
uv init --python 3.12 --no-readme
uv add numpy pandas scipy statsmodels matplotlib seaborn plotly \
       jupyter ipykernel nbformat pymare beautifulsoup4 markdown jinja2 openpyxl
uv run python -m ipykernel install --user --name proj-meta --display-name "Proj-Meta (uv)"
```

Fallback: hand-roll REML in `src/pooling.py` (Borenstein 2009, Ch. 12) if `pymare` install fails. All notebook stats logic must come from `src/` — no inline functions.

---

## 3. Pipeline

### 3.1 Phase 1 — Literature search (6 parallel agents)

Spawn 6 agents in a single message. Each returns ≥20 papers (prefer 2025–2026; seminal 2023–2024 allowed). Primary sources: arXiv, ACL Anthology, NeurIPS/ICML/ICLR proceedings, npj Digital Medicine. Each writes `data/raw/agent-{N}-{topic}.csv` + a notes `.md`.

| # | Topic | Seed terms |
|---|---|---|
| 1 | Multi-agent debate | MAD, Du 2023, A-HMAD, iMAD, ConfMAD, MACA, DTE, "stop overvaluing multi-agent debate" |
| 2 | Cooperative/hierarchical architectures | AutoGen, MetaGPT, ChatDev, CAMEL, AgentVerse, MoA, planner-executor |
| 3 | SWE & code generation | SWE-bench multi-agent, SWE-Search, AutoCodeRover, CodeR, Agentless |
| 4 | Medical/scientific reasoning | MDAgents, ArgMed-Agents, Catfish agent, multi-agent clinical decision |
| 5 | **Critical/null/failure modes** | "single-agent outperforms", equal-compute, echo chamber, sycophancy, diminishing returns — *hunts publication bias* |
| 6 | **Claude Code / Opus 4.5–4.6 / frontier-model paradox** | Claude Code agentic, Opus 4.5 / 4.6 benchmarks, terminal-bench, SWE-bench Verified, "as models improve coordination diminishes" |

**Per-paper fields:** citation-key, title, authors, venue, year, url, abstract-summary, reported-metric, reported-value-ma, reported-value-sa, benchmark, backbone-model, architecture, sa-baseline-reported, compute-parity, notes. Flag any paper missing a fair SA baseline or with cherry-picked benchmarks.

**Gate.** All 6 CSVs exist; combined unique-paper count ≥ 100.

### 3.2 Phase 2 — Extract → verify → analyze (3 sequential agents)

**Agent A (extract).** Merge raw CSVs, dedupe by DOI/arXiv ID + normalized title, screen against §1 PICOS. Produce `data/extracted/effect-size-table.csv` with study-id, citation-key, year, backbone-model, architecture (`debate|cooperation|hierarchy|role-play|verifier-critic|moa|planner-executor|other`), n-agents, task-category, benchmark-name, n-items, n-correct-ma, n-correct-sa, compute-parity-flag, compute-ratio-ma-to-sa, source-table-or-figure. Target: 20–40 rows. Also `data/extracted/prisma-counts.json` + `screening-log.md`.

**Agent B (verify).** Independent second-coder. Random-sample 30% (seed 42), re-extract from primary sources via WebFetch. Compute Cohen's κ on binary fields and ICC on counts. Escalate to full re-extraction if κ < 0.7 or any count disagrees > 5%. Output `data/verified/effect-size-table.csv` (with `audit-status` col), `data/verified/risk-of-bias.csv` (ROB 2.0 adapted: selection, performance/compute-parity, reporting, attrition), `verification-report.md`.

**Agent C (analyze).** Build `notebook/meta-analysis-v1.ipynb` on the `Proj-Meta (uv)` kernel. All logic imported from `src/`. Required sections:

| § | Output |
|---|---|
| Load | import `src`, sanity-print verified table |
| Effect sizes | log-OR + variance via `src.effect_sizes`, Cohen's *h* secondary |
| Descriptives | year × architecture × backbone × task-category table |
| Primary pool | REML random-effects + DerSimonian-Laird sensitivity; report pooled log-OR, 95% CI, 95% **prediction interval**, τ², I², Q, df, p(Q) |
| Forest plot | static PNG + interactive plotly HTML |
| Heterogeneity | Baujat plot, Cook's distance, hat values |
| Subgroup | by task-category and architecture, between-group Q |
| Meta-regression | `yi ~ compute-parity + year + backbone-family + n-agents`, mixed-effects |
| Publication bias | funnel, Egger, Begg, trim-and-fill, p-curve |
| Sensitivity | leave-one-out; compute-parity-only; 2025+ only; high-RoB removed |
| Frontier-paradox | meta-reg of yi on baseline-SA-accuracy; bubble plot |
| Export | all figures/tables to `report/assets/` with stable filenames |

**Gate.** `uv run jupyter nbconvert --execute --to notebook --inplace notebook/meta-analysis-v1.ipynb` exits clean; ≥1 figure per stats section.

---

## 4. Reports & Review

### 4.1 Phase 3 — Report v1 (NeurIPS-spotlight grade)

Output: `report/report-v1.html`, single-file, CSS inlined, assets either base64-embedded or referenced under `report/assets/`. Body 2000–3000 words; tables/figures/refs/appendices excluded from count.

Structure: title (≤15 words) → abstract (≤250 words) → introduction (frame the enthusiast-vs-skeptic controversy, state RQ1–4 verbatim) → methods (search, inclusion, effect size, statistical model, RoB, protocol deviations) → results (PRISMA flow, descriptives, pooled, heterogeneity *with prediction interval emphasized*, subgroup, meta-regression, frontier-paradox, publication bias, sensitivity) → discussion (main finding, architecture reconciliation, practitioner implications in the Claude-Code era, limitations, what a full systematic review would add) → conclusion (≤150 words) → references (APA, ≥20, hyperlinked) → Appendix A reproducibility → Appendix B AI-use declaration per KU Leuven Article 84.

Visual bar: ≥5 figures (PRISMA, forest, funnel, subgroup forest, meta-reg bubble), ≥3 tables, colorblind-safe palette (Okabe-Ito or viridis), self-contained captions.

**Gate.** Opens in Safari/Chrome; body 2000–3000 words; no broken assets; AI appendix present.

### 4.2 Phase 4 — Adversarial peer review

Output: `report/review/review-v1.md`. Spawn one agent under this persona:

> *Prof. Dr. habil. Dietrich Schmidt-Hoffmann, full professor of Statistics and Methodology; editorial board, Psychological Methods and Research Synthesis Methods (22 yrs). Scrupulous, unsentimental, allergic to overclaiming. Review the report as a NeurIPS spotlight + Psychological Methods submission. Brutally honest.*

Required: 1-paragraph summary; recommendation (`accept | minor | major | reject`); ≥3 strengths with section refs; **≥10 critical issues**, each citing a section/figure plus the relevant statistical literature (Borenstein, Higgins, Hedges, IntHout) and proposing a concrete fix; ≥5 minor issues; statistical-orthodoxy audit (REML used? prediction interval reported? funnel only if k ≥ 10? RoB graded study-by-study? statistical vs clinical heterogeneity distinguished?); reproducibility score 1–10 with justification; 1-sentence verdict.

**Gate.** ≥10 critical issues with citations; default verdict on v1 should be `major revision` unless the paper is genuinely flawless.

### 4.3 Phase 5 — v2 iteration

1. Read `review-v1.md`.
2. Write `report/review/v1-response.md` — point-by-point: `accepted | rejected (justify) | partial`, with the concrete action taken.
3. Re-run any Phase-1 agent the reviewer flagged for missing literature (v2-suffixed raw files; never overwrite v1 data).
4. Re-extract / re-verify / re-analyze in `notebook/meta-analysis-v2.ipynb`.
5. Write `report/report-v2.html` with a labelled "Response to Review" section + change-log table mapping every revision to the reviewer comment that drove it.
6. (Optional, budget-permitting) Re-run the reviewer agent on v2 → `review-v2.md`. **No v3 unless user asks.**

**Gate.** v2 report exists; every v1 critical issue addressed (accepted or rebutted) in `v1-response.md`.

### 4.4 Phase 6 — Chinese translation

Output: `report/report-v2-cn.html`. Set `<html lang="zh-CN">`. Translate text, figure captions, table headers into academic Simplified Chinese. **Do not translate** code snippets, formulas, citation keys, DOIs/URLs, English author names, or direct quotes (gloss in parentheses if helpful). Preserve HTML structure and assets. Terminology consistency required — use **元分析** for "meta-analysis" throughout.

**Gate.** Renders intact; no untranslated paragraphs; terminology consistent.

---

## 5. Gates, timeline, tie-breakers

### 5.1 Cross-phase gates

- `pyproject.toml` + `uv.lock` clean install
- 6 raw CSVs ≥ 20 papers each; combined ≥ 100 unique
- `effect-size-table.csv` (extracted + verified) 20–40 rows, κ ≥ 0.7
- Both notebooks execute clean via `nbconvert --execute`
- `report-v1.html`, `report-v2.html`, `report-v2-cn.html` all render
- `review-v1.md` ≥ 10 critical issues with citations
- Body 2000–3000 words; AI declaration present; every claim cited

### 5.2 Timeline (deadline 2026-05-31)

| Day | Date | Activity |
|---|---|---|
| 1 | 05-22 | Plan + env setup |
| 2 | 05-23 | Phase 1 (6 agents) |
| 3 | 05-24 | Phase 2 — A + B |
| 4 | 05-25 | Phase 2 — C (notebook v1) |
| 5 | 05-26 | Phase 3 — report v1 |
| 6 | 05-27 | Phase 4 — review |
| 7 | 05-28 | Phase 5 — v2 analysis |
| 8 | 05-29 | Phase 5 — v2 report |
| 9 | 05-30 | Phase 6 — translation + hand-in |
| 10 | 05-31 | Buffer for Toledo upload |

### 5.3 Non-goals

No model training, no primary experiments, no exhaustive systematic review (convenience sample of 20–40 is fine — disclose), no v3, no dashboards.

### 5.4 Open questions (Methods §4.6 must record resolution)

1. Effect-size choice: log-OR primary, Cohen's *h* secondary (default).
2. Backbone collapsing: collapse `gpt-4-*` for primary, split in sensitivity.
3. Multiple ES per study: RVE in `src.pooling.rve(...)` rather than averaging.
4. Preprints: include with `peer-reviewed` flag for sensitivity.

### 5.5 Tie-breakers

Course guidelines (`guidelines.txt`) > this plan. Methodology orthodoxy (Borenstein 2009; Cochrane Handbook v6.4) > this plan. Document every deviation in report Methods §4.6.

**Begin at §2.2, then §3.1.**
