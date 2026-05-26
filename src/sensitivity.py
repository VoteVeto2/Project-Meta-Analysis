"""Sensitivity analyses for the meta-analysis."""

import numpy as np
import pandas as pd
from src.pooling import random_effects


def sensitivity_subset(df: pd.DataFrame, mask: pd.Series,
                       label: str, method: str = "reml"):
    """Pool a subset and return results with label."""
    sub = df[mask]
    if len(sub) < 2:
        return {"label": label, "k": len(sub), "note": "too few studies"}
    res = random_effects(sub["yi"].values, sub["vi"].values, method)
    res["label"] = label
    return res


def run_all_sensitivity(df: pd.DataFrame, rob: pd.DataFrame | None = None):
    """Run standard sensitivity analyses per reviewer demands."""
    results = []
    full = random_effects(df["yi"].values, df["vi"].values, "reml")
    full["label"] = "Full sample"
    results.append(full)

    cp = df["compute-parity-flag"] == "yes"
    results.append(sensitivity_subset(df, cp, "Compute-parity only"))

    recent = df["year"] >= 2025
    results.append(sensitivity_subset(df, recent, "2025+ only"))

    if rob is not None:
        merged = df.merge(rob[["study-id", "rob-overall"]], on="study-id", how="left")
        low_rob = (merged["rob-overall"] != "high").values
        results.append(sensitivity_subset(df, low_rob, "High-RoB removed"))

    if "audit-status" in df.columns:
        verified = df["audit-status"].str.startswith("verified")
        results.append(sensitivity_subset(df, verified, "Verified studies only"))

    not_aggregated = ~df["benchmark-name"].str.contains(
        r"avg|dataset|benchmark|combined", case=False, na=False
    )
    results.append(sensitivity_subset(df, not_aggregated, "Non-aggregated benchmarks"))

    if "metric-type" in df.columns:
        accuracy_only = df["metric-type"] == "accuracy"
        results.append(sensitivity_subset(df, accuracy_only, "Accuracy metrics only"))

    if "n-items-source" in df.columns:
        exact_n = df["n-items-source"] == "exact"
        results.append(sensitivity_subset(df, exact_n, "Exact n-items only"))

    if "audit-status" in df.columns:
        not_unverifiable = df["audit-status"] != "unverifiable"
        results.append(sensitivity_subset(df, not_unverifiable,
                                          "Unverifiable removed"))

    return pd.DataFrame(results)
