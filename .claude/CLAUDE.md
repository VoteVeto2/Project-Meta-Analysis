# Project conventions

## Naming
- Use **kebab-case** (`-`) for all files, folders, notebooks, reports, CSV/JSON keys.
- **Exception:** Python module files in `src/` keep `snake_case` (Python import requirement). Prefer single-word module names when possible to
minimize the exception.

## Writing
- Be concise. Focus on insights, not throat-clearing.
- Cap top-level sections at **5 max**; use subsections inside them.
- No restating the obvious. No verbose preambles.

## Code
- **Stack:** `uv` + `python`. No `pip install`, no `conda`. Always `uv add`, `uv run`.
- Notebooks run on the project `uv` kernel; all reusable logic lives in `src/`.