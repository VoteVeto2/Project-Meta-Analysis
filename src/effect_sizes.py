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
