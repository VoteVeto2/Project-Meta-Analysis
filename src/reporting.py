"""Report generation utilities."""

import numpy as np
import pandas as pd


def format_pooled(res: dict) -> str:
    """Format pooled result for inline reporting."""
    return (f"LOR = {res['pooled-lor']:.2f}, 95% CI [{res['ci-lo']:.2f}, {res['ci-hi']:.2f}], "
            f"95% PI [{res['pi-lo']:.2f}, {res['pi-hi']:.2f}], "
            f"τ² = {res['tau2']:.3f}, I² = {res['i2']:.0f}%, "
            f"Q({res['df']}) = {res['q']:.1f}, p = {res['p-q']:.4f}")


def descriptives_table(df: pd.DataFrame) -> pd.DataFrame:
    """Cross-tabulation of year × architecture × task-category."""
    return pd.crosstab(
        [df["year"], df["architecture"]], df["task-category"],
        margins=True, margins_name="Total"
    )


def extraction_table(df: pd.DataFrame, rob: pd.DataFrame) -> pd.DataFrame:
    """Full 41-row extraction table for auditability (Appendix A1)."""
    merged = df.merge(rob[["study-id", "rob-overall"]], on="study-id", how="left")
    cols = [
        "study-id", "citation-key", "benchmark-name", "task-category",
        "architecture", "n-items", "n-correct-ma", "n-correct-sa",
        "n-items-source", "compute-parity-flag", "audit-status",
        "rob-overall", "yi", "vi", "h",
    ]
    out = merged[cols].copy()
    out["ma-pct"] = np.round(out["n-correct-ma"] / out["n-items"] * 100, 1)
    out["sa-pct"] = np.round(out["n-correct-sa"] / out["n-items"] * 100, 1)
    out["rd-pct"] = np.round(out["ma-pct"] - out["sa-pct"], 1)
    out["yi"] = np.round(out["yi"], 3)
    out["vi"] = np.round(out["vi"], 4)
    out["h"] = np.round(out["h"], 3)
    return out


def sensitivity_table(results: pd.DataFrame) -> str:
    """Format sensitivity results as markdown table."""
    cols = ["label", "k", "pooled-lor", "ci-lo", "ci-hi", "i2"]
    available = [c for c in cols if c in results.columns]
    sub = results[available].copy()
    for c in ["pooled-lor", "ci-lo", "ci-hi"]:
        if c in sub.columns:
            sub[c] = sub[c].apply(lambda x: f"{x:.2f}" if pd.notna(x) else "—")
    if "i2" in sub.columns:
        sub["i2"] = sub["i2"].apply(lambda x: f"{x:.0f}%" if pd.notna(x) else "—")
    return sub.to_markdown(index=False)
