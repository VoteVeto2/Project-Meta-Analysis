# Proj-Meta — Multi-agent vs. single-agent LLM systems: a meta-analysis

A random-effects meta-analysis of 41 within-study comparisons (2023–2026) asking whether
multi-agent LLM orchestration beats single-agent prompting on benchmark accuracy — and
whether any advantage survives a compute-matched comparison.

## Research questions

- **RQ1** Do multi-agent LLM systems outperform single-agent baselines on accuracy?
- **RQ2** Under matched compute budgets, does the advantage survive?


## Layout

```
src/        # reusable pipeline: effect sizes, pooling, heterogeneity, publication bias, plots
notebook/   # meta-analysis-v8.ipynb — current narrative analysis 
data/       # raw/ (6 search-agent extracts) → extracted/ (screening, PRISMA) → verified/ (audited)
report/assets     # generated figures & tables (PNG / CSV / JSON)
```

## Run

```bash
uv sync                                   # install (uv-only: no pip / conda)
uv run python main.py                     # reproduce all assets in report/assets/
uv run jupyter notebook                   # open notebook/meta-analysis-v8.ipynb
uv run pytest                             # run tests
```
