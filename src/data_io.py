"""Data I/O utilities for the meta-analysis pipeline."""

import json
import os
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_EXTRACTED = PROJECT_ROOT / "data" / "extracted"
DATA_VERIFIED = PROJECT_ROOT / "data" / "verified"
REPORT_ASSETS = PROJECT_ROOT / "report" / "assets"

RAW_COLUMNS = [
    "citation-key", "title", "authors", "venue", "year", "url",
    "abstract-summary", "reported-metric", "reported-value-ma",
    "reported-value-sa", "benchmark", "backbone-model", "architecture",
    "sa-baseline-reported", "compute-parity", "notes",
]

EXTRACTED_COLUMNS = [
    "study-id", "citation-key", "year", "backbone-model", "architecture",
    "n-agents", "task-category", "benchmark-name", "n-items",
    "n-correct-ma", "n-correct-sa", "compute-parity-flag",
    "compute-ratio-ma-to-sa", "source-table-or-figure",
]

ARCHITECTURE_VALUES = [
    "debate", "cooperation", "hierarchy", "role-play",
    "verifier-critic", "moa", "planner-executor", "other",
]

TASK_CATEGORIES = [
    "reasoning", "code", "medical", "math", "factuality",
    "general-knowledge", "evaluation", "planning", "other",
]


def load_raw_csvs() -> pd.DataFrame:
    frames = []
    for f in sorted(DATA_RAW.glob("agent-*-*.csv")):
        df = pd.read_csv(f)
        df["source-agent"] = f.name
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def dedupe_by_title(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df["title-norm"] = (
        df["title"].str.lower().str.strip()
        .str.replace(r"[^a-z0-9 ]", "", regex=True)
    )
    has_ma = df["reported-value-ma"].apply(_is_numeric)
    has_sa = df["reported-value-sa"].apply(_is_numeric)
    df["data-richness"] = has_ma.astype(int) + has_sa.astype(int)
    df = df.sort_values("data-richness", ascending=False)
    kept = df.drop_duplicates(subset="title-norm", keep="first")
    removed = df[~df.index.isin(kept.index)]
    return kept.drop(columns=["title-norm", "data-richness"]), removed


def _is_numeric(val) -> bool:
    try:
        float(str(val))
        return True
    except (ValueError, TypeError):
        return False


def screen_picos(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Screen against PICOS: need SA baseline, empirical results, 2023+."""
    mask_sa = df["sa-baseline-reported"].str.lower() == "yes"
    mask_year = df["year"].astype(int) >= 2023
    mask_not_frontier_only = df["architecture"] != "single-agent-frontier"
    included = df[mask_sa & mask_year & mask_not_frontier_only].copy()
    excluded = df[~(mask_sa & mask_year & mask_not_frontier_only)].copy()
    excluded["exclusion-reason"] = ""
    excluded.loc[~mask_sa, "exclusion-reason"] += "no-sa-baseline;"
    excluded.loc[~mask_year, "exclusion-reason"] += "pre-2023;"
    excluded.loc[~mask_not_frontier_only, "exclusion-reason"] += "single-agent-only;"
    return included, excluded


def save_prisma_counts(counts: dict, path: Path | None = None):
    path = path or DATA_EXTRACTED / "prisma-counts.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(counts, f, indent=2)


def save_extracted(df: pd.DataFrame, path: Path | None = None):
    path = path or DATA_EXTRACTED / "effect-size-table.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def load_extracted(path: Path | None = None) -> pd.DataFrame:
    path = path or DATA_EXTRACTED / "effect-size-table.csv"
    return pd.read_csv(path)


def load_verified(path: Path | None = None) -> pd.DataFrame:
    path = path or DATA_VERIFIED / "effect-size-table.csv"
    return pd.read_csv(path)
