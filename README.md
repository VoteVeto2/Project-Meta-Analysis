# Proj-Meta — Multi-agent vs. single-agent LLM systems: a meta-analysis

An exploratory, **hypothesis-generating** meta-analysis of within-study comparisons (2023–2026) pitting
multi-agent LLM orchestration (debate, cooperation, hierarchy, verifier-critic, MoA, …) against
single-agent prompting on benchmark accuracy. Course project for KU Leuven *Meta-Analysis* (G0B75a).

Everything downstream of the dataset is fully reproducible from `main.py` and the notebook; the dataset
itself is an acknowledged AI-extracted convenience sample (see [Data & provenance](#data--provenance)).

## Headline result

| Specification | k | log-OR [95% CI] | Read as |
|---|---|---|---|
| **Primary** (item-level binomial, accuracy metric only) | 37 | **0.46 [0.22, 0.71]** | small-to-moderate relative edge |
| Full convenience sample (+ 4 win-/resolve-rate studies) | 41 | 0.45 [0.23, 0.67] | robustness |
| Compute parity only | 9 | 0.31 | relative effect attenuates… |
| Source-located / verified subset | 10 | 0.35 | …and heterogeneity drops sharply |

On the **absolute** scale the gain is small and weighting-dependent: aggregate (precision-weighted) risk
difference **≈3 pp** (≈8 pp as an unweighted study mean); Cohen's *h* = 0.07 aggregate / 0.20 unweighted.
The estimate is **fragile**: heterogeneity is extreme (I² = 96.1%), the prediction interval crosses zero
([−0.74, 1.64]), and Egger's test flags funnel asymmetry (*p* = .024). Under compute parity the relative
effect shrinks but the absolute gain does **not** (aggregate RD ≈5 pp) — the parity subset omits the large
near-null general-knowledge benchmarks. **Provisional: 76% of rows are unverified and most studies did not
control compute.**

## Repository layout

```
main.py                     orchestration: load → effect sizes → pool → diagnostics → export assets
src/                        all reusable statistical logic (snake_case for Python imports)
notebook/                   meta-analysis-v{1..7}.ipynb — narrative run on the project uv kernel
data/                       raw/ → extracted/ → verified/ (see Data & provenance)
report/                     report-v{1..7}.html (+ -cn.html), review/, assets/ (figures, CSVs, JSON)
plan/                       research plans (v1, v3)
tests/                      test_stats.py — 18 known-value checks of the statistical core
guidelines.txt              course assignment brief
```

| `src/` module | Responsibility |
|---|---|
| `data_io.py` | Load raw/extracted/verified tables; path + column constants |
| `effect_sizes.py` | log odds ratio (independent-binomial variance), Cohen's *h*, risk difference, in-pipeline pooled absolute effects |
| `pooling.py` | Random-effects pooling — REML τ² (Fisher scoring), DerSimonian-Laird, modified HKSJ with `max(1, s²)` floor, prediction intervals |
| `heterogeneity.py` | Baujat, Cook's distance, hat values, leave-one-out (τ² re-estimated each iteration) |
| `moderators.py` | Subgroup analysis (partition-of-Q, merge-rare) + mixed-effects meta-regression (conditional REML + Knapp-Hartung) |
| `publication_bias.py` | Egger regression, Begg rank correlation, Duval-Tweedie trim-and-fill |
| `sensitivity.py` | Leave-one-out, risk-of-bias, and subset sensitivity sweeps |
| `plots.py` | Forest (static + interactive), funnel, Baujat, subgroup forest, bubble, PRISMA flow (Okabe-Ito palette) |
| `reporting.py` | Inline result formatting, descriptives cross-tab, 41-row auditable extraction table |

## Reproducing the analysis

Stack is **`uv` + Python 3.12** — no `pip`, no `conda`.

```bash
uv sync                     # install locked dependencies from uv.lock
uv run python main.py       # regenerate every figure + CSV + JSON in report/assets/
uv run pytest               # 18 known-value tests of the statistical core
```

`main.py` self-validates its outputs (k = 41, df = 40, CI brackets the pooled estimate, subgroup k sums to
41, …) and aborts on any mismatch. The notebook (`notebook/meta-analysis-v7.ipynb`) is the narrative
companion — same `src/` functions, run on the project uv kernel — and carries 14 in-notebook validation
checks. Reusable logic lives only in `src/`; notebooks and `main.py` import it rather than redefining it.

## Data & provenance

The dataset flows through three stages under `data/`:

- **`raw/`** — six topic-scoped search agents (debate, cooperative, SWE, medical, critical, frontier) returning 153 candidate records.
- **`extracted/`** — after dedup (127) and PICOS screening (106 eligible, 41 with extractable MA+SA counts). `screening-log.md` records every exclusion; `prisma-counts.json` drives the PRISMA figure.
- **`verified/`** — the analysed 41-row `effect-size-table.csv`, a `risk-of-bias.csv` (ROB-2-adapted; 25/41 = 61% high), and `verification-report.md` documenting the two-pass source audit.

**Treat results as exploratory.** The 41 rows are an AI-extracted convenience sample: **76% are unverified**,
and among independently audited rows the **error rate was ~50%** (hence the two-pass re-verification). Only
~14 studies have an independently located primary source; **S013 and S027 could not be located at all**.
Most studies did not control compute between conditions. Denominators flagged `exact` are often
benchmark-imputed rather than paper-reported — tracked per row via the `n-items-provenance` axis
(10 paper-audited / 30 benchmark-imputed / 1 percent-estimated).

## Reports & review cycle

Each version N is hardened through a fixed adversarial loop:
`review/review-vN.md` (peer review + source verification) → `review/vN-response.md` (point-by-point
rebuttal) → accepted fixes land in `src/`, the notebook, and a fresh `report-vN+1.html` → Simplified-Chinese
translation `report-vN+1-cn.html`.

**Current version: v7** (29 May 2026). The v6→v7 step made the previously hand-entered absolute metrics
(Cohen's *h*, risk difference) reproducible in-pipeline, foregrounded the k = 37 accuracy-only binomial spec,
dropped the unreliable `n-agents` moderator, and added Appendix G (per-study verification status).

- English report: [`report/report-v7.html`](report/report-v7.html)
- 中文报告: [`report/report-v7-cn.html`](report/report-v7-cn.html)
