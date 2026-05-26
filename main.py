"""Reproducible pipeline: read verified data → compute effects → pool → export assets."""

import json
from pathlib import Path

import numpy as np
import pandas as pd

from src.data_io import load_verified, DATA_VERIFIED, REPORT_ASSETS
from src.effect_sizes import compute_effect_sizes
from src.pooling import random_effects
from src.heterogeneity import baujat, cooks_distance, hat_values, leave_one_out
from src.moderators import subgroup_analysis, meta_regression
from src.publication_bias import egger_test, begg_test, trim_and_fill
from src.sensitivity import run_all_sensitivity
from src.plots import (forest_plot, forest_plot_interactive, funnel_plot,
                       baujat_plot, subgroup_forest, bubble_plot, prisma_flow)
from src.reporting import format_pooled, descriptives_table, extraction_table


def main():
    REPORT_ASSETS.mkdir(parents=True, exist_ok=True)
    df = load_verified()
    rob = pd.read_csv(DATA_VERIFIED / "risk-of-bias.csv")
    with open(Path("data/extracted/prisma-counts.json")) as f:
        prisma_counts = json.load(f)

    df = compute_effect_sizes(df)
    yi, vi = df["yi"].values, df["vi"].values

    res_reml = random_effects(yi, vi, "reml")
    res_dl = random_effects(yi, vi, "dl")
    pooled = res_reml
    print(f"REML: {format_pooled(res_reml)}")
    print(f"DL:   {format_pooled(res_dl)}")

    df_sorted = df.sort_values("yi")
    forest_plot(df_sorted, pooled)
    forest_plot_interactive(df_sorted, pooled)
    funnel_plot(df, pooled)
    prisma_flow(prisma_counts)

    qi, influence = baujat(yi, vi, pooled["tau2"])
    baujat_plot(qi, influence, df["citation-key"].tolist())

    sg_task = subgroup_analysis(df, "task-category", merge_rare=True)
    sg_arch = subgroup_analysis(df, "architecture", merge_rare=True)
    subgroup_forest(sg_task, "task-category")
    subgroup_forest(sg_arch, "architecture")

    mr_df = df.copy()
    mr_df["sa-accuracy"] = mr_df["n-correct-sa"] / mr_df["n-items"]
    mr_df["backbone-family"] = mr_df["backbone-model"].str.extract(
        r"(GPT|Claude|Llama|Gemini|Qwen|DeepSeek)", expand=False
    ).fillna("other")
    mr_df["n-agents"] = pd.to_numeric(mr_df["n-agents"], errors="coerce").fillna(3)
    mr_results = meta_regression(mr_df, ["compute-parity-flag", "sa-accuracy", "backbone-family", "n-agents"])

    df["sa-accuracy"] = df["n-correct-sa"] / df["n-items"]
    bubble_plot(df, "sa-accuracy")

    egger = egger_test(yi, df["sei"].values)
    begg = begg_test(yi, vi)
    tf = trim_and_fill(yi, vi)

    sens = run_all_sensitivity(df, rob)

    results = {
        "reml": res_reml, "dl": res_dl,
        "egger": egger, "begg": begg,
        "trim-and-fill": tf,
    }
    with open(REPORT_ASSETS / "results-summary.json", "w") as f:
        json.dump(results, f, indent=2, default=float)

    descriptives_table(df).to_csv(REPORT_ASSETS / "descriptives.csv")
    sens.to_csv(REPORT_ASSETS / "sensitivity.csv", index=False)
    sg_task.to_csv(REPORT_ASSETS / "subgroup-task.csv", index=False)
    sg_arch.to_csv(REPORT_ASSETS / "subgroup-arch.csv", index=False)
    mr_results.to_csv(REPORT_ASSETS / "meta-regression.csv", index=False)

    ext_table = extraction_table(df, rob)
    ext_table.to_csv(REPORT_ASSETS / "extraction-table.csv", index=False)

    validate(res_reml, egger, sg_task, sg_arch)

    print(f"\nAll assets exported to {REPORT_ASSETS}")
    print(f"Figures: {sorted(f.name for f in REPORT_ASSETS.glob('*.png'))}")
    print("Pipeline complete.")


def validate(reml: dict, egger: dict, sg_task: pd.DataFrame, sg_arch: pd.DataFrame):
    """Sanity-check key outputs against known constraints."""
    sg_task_k = int(sg_task["k"].sum())
    sg_arch_k = int(sg_arch["k"].sum())
    checks = [
        (reml["k"] == 41, f"k should be 41, got {reml['k']}"),
        (reml["df"] == 40, f"df should be 40, got {reml['df']}"),
        (reml["q"] > 0, f"Q should be positive, got {reml['q']}"),
        (0 < reml["i2"] <= 100, f"I² out of range: {reml['i2']}"),
        (reml["tau2"] >= 0, f"tau² negative: {reml['tau2']}"),
        (reml["ci-lo"] < reml["pooled-lor"] < reml["ci-hi"], "CI doesn't bracket pooled"),
        (reml["pi-lo"] < reml["pooled-lor"] < reml["pi-hi"], "PI doesn't bracket pooled"),
        (egger["df"] == 39, f"Egger df should be 39, got {egger['df']}"),
        (sg_task_k == 41, f"Task subgroup k should sum to 41, got {sg_task_k}"),
        (sg_arch_k == 41, f"Architecture subgroup k should sum to 41, got {sg_arch_k}"),
    ]
    failed = [(msg,) for ok, msg in checks if not ok]
    if failed:
        raise ValueError(f"Validation failed: {failed}")
    print("Output validation: all checks passed.")


if __name__ == "__main__":
    main()
