# Research Plan v3 — Addressing GPT-5.5 Review (50 Issues)

**Predecessor:** `RESEARCH-PLAN-v1.md` → v2 code/report → `review-v2.md` (50 critical issues)
**Goal:** Fix every legitimate issue, re-run full pipeline, produce v3 analysis + v4 report + Chinese translation.

---

## 1. Code Bugs to Fix

### 1.1 Egger test miscoded (#8, #9)
`src/publication_bias.py` `egger_test()` reports `linregress` slope p-value as intercept p-value. Fix: compute intercept t-stat and p from intercept SE manually.

### 1.2 Subgroup Q mismatch (#10, #11, #14, #15)
The partition-of-Q in `moderators.py` produces different values than what was hardcoded in report-v2.html. Fix: ensure report reads from `results-summary.json` or `subgroup-*.csv`, not stale hand-typed numbers.

### 1.3 HKSJ incomplete (#12, #13)
Current `pooling.py` only swaps z→t but doesn't compute the Hartung-Knapp scale factor. Fix: implement full HKSJ with `s²_HK = (1/(k-1)) * Σ wi*(yi-μ)²` variance scaling. Use df=k-1 for intercept-only model.

### 1.4 Reproducibility entry point (#7, #47)
`main.py` just prints hello. Fix: make it a real pipeline that reads data → computes effects → exports assets → validates consistency.

### 1.5 Add unit tests (#45)
Add `tests/` with known-output checks against published examples (Borenstein 2009 Table 16.1).

---

## 2. Citation Fixes

### 2.1 Wrong arXiv IDs (#1, #2, #3)
- Chen et al. "Stop overvaluing..." → correct to `arXiv:2502.08788` (Zhang et al.)
- Xiong et al. medical → find correct URL or remove
- Lu et al. "BlendFilter" → remove; find real source for single-agent scaling claim or delete claim

### 2.2 Overcited Anthropic docs (#4)
Remove claims about GPT-4o, Gemini 2.5, Cursor, Devin from the Claude Code citation context.

### 2.3 Uncited bibliography entries (#5)
Remove Bradburn, Chan, Fleiss, Guyatt, Higgins, CAMEL from bibliography if not cited in body — OR add in-text citations where appropriate.

### 2.4 Add full references for all 41 studies (#6)
Include every included study in the bibliography with title, authors, venue, URL.

---

## 3. Data Quality Fixes

### 3.1 Full double-extraction (#21)
Agent B must verify ALL 41 studies, not just 30%. Re-extract counts from primary sources for every study.

### 3.2 Fix audit-status labels (#19)
S013 and S027 (unlocatable) → mark as "unverifiable" not "verified."

### 3.3 n-items provenance (#20, #23)
Add `n-items-source` column: "exact" (from paper) vs "estimated" (from benchmark size lookup) vs "imputed" (round number default). Run sensitivity excluding imputed.

### 3.4 Metric heterogeneity (#33, #34)
Flag studies using win-rate (AlpacaEval), resolve-rate (SWE-bench), vs item-level accuracy. Add `metric-type` column. Run sensitivity excluding non-accuracy metrics.

### 3.5 Exclusion table (#40)
Produce a table of all 65 excluded-for-no-data records with reasons.

---

## 4. Methodology Fixes

### 4.1 Subgroup handling (#16, #17, #9)
- Collapse k<3 subgroups into "other"
- Report prediction intervals for all subgroups
- Label all subgroup analyses as exploratory

### 4.2 Report absolute effects (#35, #36)
Compute and report risk difference (RD) alongside log-OR. Report Cohen's h prominently. Explicitly note that h=0.08 under compute parity is trivial.

### 4.3 Causal language (#38)
Audit all prose for causal hedging. Use "associated with" not "drives/confers."

### 4.4 Remove in-manuscript review response (#37)
Move response-to-review into `report/review/` only, not in the report body.

### 4.5 Search transparency (#42, #43)
Add appendix with full search strings used by each of the 6 agents. Note this is a convenience sample, not a registered protocol.

---

## 5. Execution Order

1. Fix all `src/` code (§1)
2. Fix citations in report template (§2)
3. Full re-verification of all 41 studies (§3.1)
4. Re-run notebook as v3
5. Write `report/report-v3.html`
6. Peer review → `report/review/review-v3.md`
7. Address review → v4 report + `report/review/v3-response.md`
8. Write `report/report-v4.html`
9. Translate → `report/report-v4-cn.html`

**Gate.** All 50 issues from review-v2.md addressable; notebooks execute clean; no stale numbers in HTML.
