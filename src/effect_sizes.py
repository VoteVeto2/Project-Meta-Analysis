"""Effect size computation: log odds ratio + Cohen's h.
C3 fix: continuity correction only applied when zero cells exist."""

import numpy as np
import pandas as pd


def log_odds_ratio(n_ma: int, n_sa: int, n_items_ma: int, n_items_sa: int,
                   cc: float = 0.5) -> tuple[float, float]:
    a = n_ma
    b = n_items_ma - n_ma
    c = n_sa
    d = n_items_sa - n_sa
    needs_cc = (a == 0) or (b == 0) or (c == 0) or (d == 0)
    if needs_cc:
        a, b, c, d = a + cc, b + cc, c + cc, d + cc
    lor = np.log(a * d / (b * c))
    var = 1/a + 1/b + 1/c + 1/d
    return lor, var


def cohens_h(p1: float, p2: float) -> float:
    return 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))


def pooled_absolute_effect(n_ma, n_sa, n_items) -> dict:
    """Reproducible absolute-scale summary (v7).

    Primary numbers come from *aggregate* (total-events) proportions:
      p_ma = Σ n-correct-ma / Σ n-items,  p_sa = Σ n-correct-sa / Σ n-items.
    This is the directly interpretable, fully reproducible pooled proportion;
    the aggregate RD equals the n-weighted mean RD. We also return the
    unweighted mean/median RD and mean per-study Cohen's h so the report can
    be transparent that the absolute gain is weighting-dependent (the v6 report
    hand-entered a single "trivial" number that the notebook contradicted).
    """
    n_ma = np.asarray(n_ma, float)
    n_sa = np.asarray(n_sa, float)
    n = np.asarray(n_items, float)
    p_ma = n_ma.sum() / n.sum()
    p_sa = n_sa.sum() / n.sum()
    rd_each = (n_ma / n - n_sa / n) * 100.0
    h_each = np.array([cohens_h(a / m, b / m) for a, b, m in zip(n_ma, n_sa, n)])
    return {
        "k": len(n),
        "p-ma": p_ma,
        "p-sa": p_sa,
        "rd-agg-pp": (p_ma - p_sa) * 100.0,   # = n-weighted RD
        "h-agg": cohens_h(p_ma, p_sa),         # Cohen's h from aggregate proportions
        "rd-mean-pp": rd_each.mean(),
        "rd-median-pp": float(np.median(rd_each)),
        "h-mean": h_each.mean(),
    }


def n_items_provenance(audit_status: str, n_items_source: str) -> str:
    """Honest denominator-provenance axis (v7), superseding the overloaded
    'exact/imputed/estimated' n-items-source field (review V3).

    - paper-audited:    source independently located and counts cross-checked
                        (audit-status starts with 'verified').
    - percent-estimated: count back-derived from a reported percentage.
    - benchmark-imputed: denominator set to the canonical benchmark size
                        without per-paper confirmation.
    """
    if str(audit_status).startswith("verified"):
        return "paper-audited"
    if n_items_source == "estimated":
        return "percent-estimated"
    return "benchmark-imputed"


def compute_effect_sizes(df: pd.DataFrame) -> pd.DataFrame:
    """Add yi, vi (log-OR) and h (Cohen's h) columns."""
    df = df.copy()
    yi_list, vi_list, h_list = [], [], []
    for _, r in df.iterrows():
        n_ma = int(r["n-correct-ma"])
        n_sa = int(r["n-correct-sa"])
        n_items = int(r["n-items"])
        lor, var = log_odds_ratio(n_ma, n_sa, n_items, n_items)
        p_ma = n_ma / n_items
        p_sa = n_sa / n_items
        h = cohens_h(p_ma, p_sa)
        yi_list.append(lor)
        vi_list.append(var)
        h_list.append(h)
    df["yi"] = yi_list
    df["vi"] = vi_list
    df["sei"] = np.sqrt(df["vi"])
    df["h"] = h_list
    return df
