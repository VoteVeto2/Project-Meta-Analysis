"""
Plotting functions: forest, funnel, Baujat, subgroup forest, bubble.
"""

from pathlib import Path

import matplotlib
if matplotlib.get_backend() == "agg" or "inline" not in matplotlib.get_backend().lower():
    try:
        matplotlib.use("Agg")
    except Exception:
        pass
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#000000"]
ASSETS = Path(__file__).resolve().parent.parent / "report" / "assets"


def _ensure_assets():
    ASSETS.mkdir(parents=True, exist_ok=True)


def forest_plot(df: pd.DataFrame, pooled: dict, save: bool = True):
    """
    Static forest plot (matplotlib).
    """
    _ensure_assets()
    k = len(df)
    fig, ax = plt.subplots(figsize=(10, max(6, k * 0.35)))
    y = np.arange(k)
    ax.errorbar(df["yi"], y, xerr=1.96 * df["sei"], fmt="o",
                color=OKABE_ITO[4], ecolor=OKABE_ITO[4], capsize=3, ms=5)
    ax.axvline(0, color="grey", ls="--", lw=0.8)
    ax.axvline(pooled["pooled-lor"], color=OKABE_ITO[5], ls="-", lw=1.5)
    ax.fill_betweenx([-1, k], pooled["ci-lo"], pooled["ci-hi"],
                     alpha=0.15, color=OKABE_ITO[5])
    ax.set_yticks(y)
    ax.set_yticklabels(df["citation-key"], fontsize=8)
    ax.set_xlabel("Log Odds Ratio (MA vs SA)")
    ax.set_title(f"Forest Plot (k={pooled['k']}, "
                 f"pooled LOR={pooled['pooled-lor']:.2f} "
                 f"[{pooled['ci-lo']:.2f}, {pooled['ci-hi']:.2f}], "
                 f"I²={pooled['i2']:.0f}%)")
    ax.invert_yaxis()
    plt.tight_layout()
    if save:
        fig.savefig(ASSETS / "forest-plot.png", dpi=150)
    return fig


def forest_plot_interactive(df: pd.DataFrame, pooled: dict, save: bool = True):
    """
    Interactive forest plot (plotly).
    """
    _ensure_assets()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["yi"], y=df["citation-key"],
        error_x=dict(type="data", array=1.96 * df["sei"], visible=True),
        mode="markers", marker=dict(color=OKABE_ITO[4], size=8),
        name="Studies",
        hovertemplate="%{y}<br>LOR=%{x:.3f}<extra></extra>",
    ))
    fig.add_vline(x=0, line_dash="dash", line_color="grey")
    fig.add_vline(x=pooled["pooled-lor"], line_color=OKABE_ITO[5])
    fig.add_vrect(x0=pooled["ci-lo"], x1=pooled["ci-hi"],
                  fillcolor=OKABE_ITO[5], opacity=0.1)
    fig.update_layout(
        title=f"Forest Plot (k={pooled['k']}, pooled LOR={pooled['pooled-lor']:.2f}, I²={pooled['i2']:.0f}%)",
        xaxis_title="Log Odds Ratio", height=max(400, len(df) * 25),
        yaxis=dict(autorange="reversed"),
    )
    if save:
        fig.write_html(str(ASSETS / "forest-plot.html"))
    return fig


def funnel_plot(df: pd.DataFrame, pooled: dict, save: bool = True):
    """Funnel plot."""
    _ensure_assets()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df["yi"], df["sei"], c=OKABE_ITO[4], s=30, alpha=0.7)
    ax.axvline(pooled["pooled-lor"], color=OKABE_ITO[5], ls="-")
    se_range = np.linspace(0, df["sei"].max() * 1.1, 100)
    ax.plot(pooled["pooled-lor"] - 1.96 * se_range, se_range,
            "k--", lw=0.8)
    ax.plot(pooled["pooled-lor"] + 1.96 * se_range, se_range,
            "k--", lw=0.8)
    ax.set_xlabel("Log Odds Ratio")
    ax.set_ylabel("Standard Error")
    ax.set_title("Funnel Plot")
    ax.invert_yaxis()
    plt.tight_layout()
    if save:
        fig.savefig(ASSETS / "funnel-plot.png", dpi=150)
    return fig


def baujat_plot(qi: np.ndarray, influence: np.ndarray,
                labels: list, save: bool = True):
    """Baujat plot."""
    _ensure_assets()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(qi, influence, c=OKABE_ITO[4], s=30)
    for i, label in enumerate(labels):
        if qi[i] > np.percentile(qi, 75) or influence[i] > np.percentile(influence, 75):
            ax.annotate(label, (qi[i], influence[i]), fontsize=7,
                        xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel("Contribution to Q")
    ax.set_ylabel("Influence on Pooled Estimate")
    ax.set_title("Baujat Plot")
    plt.tight_layout()
    if save:
        fig.savefig(ASSETS / "baujat-plot.png", dpi=150)
    return fig


def subgroup_forest(subgroup_df: pd.DataFrame, group_col: str,
                    save: bool = True):
    """Forest plot for subgroup analysis."""
    _ensure_assets()
    k = len(subgroup_df)
    fig, ax = plt.subplots(figsize=(10, max(4, k * 0.6)))
    y = np.arange(k)
    colors = [OKABE_ITO[i % len(OKABE_ITO)] for i in range(k)]
    for i, (_, r) in enumerate(subgroup_df.iterrows()):
        ax.errorbar(r["pooled-lor"], i,
                    xerr=[[r["pooled-lor"] - r["ci-lo"]],
                          [r["ci-hi"] - r["pooled-lor"]]],
                    fmt="s", color=colors[i], capsize=5, ms=8)
        ax.annotate(f'k={r["k"]}', (r["ci-hi"] + 0.05, i), fontsize=8)
    ax.axvline(0, color="grey", ls="--")
    ax.set_yticks(y)
    ax.set_yticklabels(subgroup_df["group"])
    ax.set_xlabel("Pooled Log Odds Ratio")
    q_b = subgroup_df.attrs.get("q-between", "N/A")
    p_b = subgroup_df.attrs.get("p-between", "N/A")
    title = f"Subgroup Analysis by {group_col}"
    if isinstance(q_b, float):
        title += f"\nQ_between={q_b:.2f}, p={p_b:.3f}"
    ax.set_title(title)
    ax.invert_yaxis()
    plt.tight_layout()
    if save:
        fig.savefig(ASSETS / f"subgroup-{group_col}.png", dpi=150)
    return fig


def bubble_plot(df: pd.DataFrame, x_col: str, save: bool = True):
    """Bubble plot for meta-regression (frontier-paradox)."""
    _ensure_assets()
    fig, ax = plt.subplots(figsize=(8, 6))
    sizes = 100 / df["vi"]
    sizes = sizes / sizes.max() * 300
    ax.scatter(df[x_col], df["yi"], s=sizes, alpha=0.5,
               c=OKABE_ITO[0], edgecolors=OKABE_ITO[4])
    z = np.polyfit(df[x_col], df["yi"], 1, w=1/df["sei"])
    xr = np.linspace(df[x_col].min(), df[x_col].max(), 100)
    ax.plot(xr, np.polyval(z, xr), color=OKABE_ITO[5], lw=2)
    ax.axhline(0, color="grey", ls="--")
    ax.set_xlabel(x_col)
    ax.set_ylabel("Log Odds Ratio (MA vs SA)")
    ax.set_title(f"Meta-Regression: LOR ~ {x_col}")
    plt.tight_layout()
    if save:
        fig.savefig(ASSETS / "bubble-plot.png", dpi=150)
    return fig


def prisma_flow(counts: dict, save: bool = True):
    """PRISMA flow diagram as a figure."""
    _ensure_assets()
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    boxes = [
        (5, 9, f"Records identified\n(6 search agents)\nn = {counts['identification']['records-from-agents']}"),
        (5, 7, f"After deduplication\nn = {counts['screening']['after-dedup']}"),
        (5, 5, f"PICOS screened\nn = {counts['screening']['picos-included']}"),
        (5, 3, f"With extractable data\nn = {counts['screening']['with-extractable-data']}"),
        (5, 1, f"Included in meta-analysis\nk = {counts['included']['effect-size-rows']}"),
    ]

    excl = [
        (8.5, 8, f"Duplicates removed\nn = {counts['screening']['duplicates-removed']}"),
        (8.5, 6, f"PICOS excluded\nn = {counts['screening']['picos-excluded']}"),
        (8.5, 4, f"No extractable data\nn = {counts['screening']['without-extractable-data']}"),
    ]

    for x, y, text in boxes:
        ax.add_patch(plt.Rectangle((x-1.3, y-0.5), 2.6, 1, fill=True,
                     facecolor="#E8F4FD", edgecolor=OKABE_ITO[4], lw=1.5))
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    for x, y, text in excl:
        ax.add_patch(plt.Rectangle((x-1.2, y-0.4), 2.4, 0.8, fill=True,
                     facecolor="#FDE8E8", edgecolor=OKABE_ITO[5], lw=1))
        ax.text(x, y, text, ha="center", va="center", fontsize=8)

    for i in range(len(boxes) - 1):
        ax.annotate("", xy=(5, boxes[i+1][1] + 0.5),
                    xytext=(5, boxes[i][1] - 0.5),
                    arrowprops=dict(arrowstyle="->", color="grey"))

    arrows_excl = [(6.3, 8), (6.3, 6), (6.3, 4)]
    for x, y in arrows_excl:
        ax.annotate("", xy=(7.3, y), xytext=(x, y),
                    arrowprops=dict(arrowstyle="->", color="grey"))

    ax.set_title("PRISMA Flow Diagram", fontsize=14, fontweight="bold")
    plt.tight_layout()
    if save:
        fig.savefig(ASSETS / "prisma-flow.png", dpi=150)
    return fig
