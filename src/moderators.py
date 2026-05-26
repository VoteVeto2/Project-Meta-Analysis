"""Subgroup analysis and meta-regression.
C5 fix: conditional REML for meta-regression.
C6 fix: Knapp-Hartung adjustment for meta-regression inference.
C9 fix: between-group Q via partition-of-Q (Borenstein 2009 Ch 19).
C10 fix: proper between-group Q computation."""

import numpy as np
import pandas as pd
from scipy.stats import chi2
from src.pooling import random_effects, reml_estimate


def merge_rare_groups(df: pd.DataFrame, group_col: str,
                      min_k: int = 2) -> pd.DataFrame:
    """Merge groups with fewer than min_k studies into an existing 'other' group
    or create 'other/rare' if no 'other' group exists."""
    df = df.copy()
    counts = df[group_col].value_counts()
    rare = counts[counts < min_k].index.tolist()
    if not rare:
        return df
    has_other = "other" in counts.index
    target = "other" if has_other else "other/rare"
    df[group_col] = df[group_col].replace({g: target for g in rare})
    return df


def subgroup_analysis(df: pd.DataFrame, group_col: str,
                      method: str = "reml",
                      merge_rare: bool = True) -> pd.DataFrame:
    """Run random-effects within each subgroup; between-group Q via partition.
    When merge_rare=True, singleton categories are merged into 'other/rare'
    so all k studies appear in the subgroup table."""
    if merge_rare:
        df = merge_rare_groups(df, group_col)
    results = []
    q_within_total = 0.0
    df_within_total = 0
    for grp, sub in df.groupby(group_col):
        if len(sub) < 2:
            continue
        res = random_effects(sub["yi"].values, sub["vi"].values, method)
        res["group"] = grp
        q_within_total += res["q"]
        df_within_total += res["df"]
        results.append(res)

    out = pd.DataFrame(results)

    if len(out) >= 2:
        yi_all = df["yi"].values
        vi_all = df["vi"].values
        wi_fe = 1.0 / vi_all
        mu_fe = np.sum(wi_fe * yi_all) / np.sum(wi_fe)
        q_total = np.sum(wi_fe * (yi_all - mu_fe) ** 2)
        q_between = q_total - q_within_total
        df_between = len(out) - 1
        p_between = 1 - chi2.cdf(max(0, q_between), df_between)
        out.attrs["q-between"] = q_between
        out.attrs["df-between"] = df_between
        out.attrs["p-between"] = p_between
        out.attrs["q-total"] = q_total
        out.attrs["q-within"] = q_within_total

    return out


def meta_regression(df: pd.DataFrame, formula_cols: list[str]):
    """Mixed-effects meta-regression with conditional REML and Knapp-Hartung."""
    yi = df["yi"].values
    vi = df["vi"].values

    X_cols = []
    X_data = []
    for col in formula_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            dummies = pd.get_dummies(df[col], prefix=col, drop_first=True,
                                     dtype=float)
            X_cols.extend(dummies.columns.tolist())
            X_data.append(dummies.values)
        else:
            X_cols.append(col)
            X_data.append(df[col].values.reshape(-1, 1).astype(float))

    X = np.hstack([np.ones((len(df), 1))] + X_data)
    col_names = ["intercept"] + X_cols
    p = X.shape[1]

    tau2_unconditional = reml_estimate(yi, vi)
    tau2_conditional = reml_estimate(yi, vi, X=X)

    W = np.diag(1.0 / (vi + tau2_conditional))
    XtWX = X.T @ W @ X
    try:
        XtWX_inv = np.linalg.inv(XtWX)
        beta = XtWX_inv @ X.T @ W @ yi
    except np.linalg.LinAlgError:
        beta = np.full(p, np.nan)
        XtWX_inv = np.full((p, p), np.nan)

    resid = yi - X @ beta
    from scipy.stats import t as t_dist
    s2_kh = np.sum(resid ** 2 * np.diag(W)) / (len(yi) - p)
    var_beta_kh = s2_kh * XtWX_inv
    se_beta = np.sqrt(np.diag(var_beta_kh))

    df_residual = len(yi) - p
    t_vals = beta / se_beta
    p_vals = 2 * (1 - t_dist.cdf(np.abs(t_vals), df_residual))

    q_model = beta[1:] @ np.linalg.solve(
        XtWX_inv[1:, 1:], beta[1:]
    ) / s2_kh if not np.any(np.isnan(beta)) else np.nan
    p_qm = 1 - chi2.cdf(q_model, p - 1) if not np.isnan(q_model) else np.nan

    r2 = max(0, 1 - tau2_conditional / tau2_unconditional) if tau2_unconditional > 0 else 0

    results = pd.DataFrame({
        "coef": col_names,
        "estimate": beta,
        "se": se_beta,
        "t": t_vals,
        "p": p_vals,
        "df": df_residual,
    })
    results.attrs["tau2-unconditional"] = tau2_unconditional
    results.attrs["tau2-conditional"] = tau2_conditional
    results.attrs["r2"] = r2
    results.attrs["q-model"] = q_model
    results.attrs["p-qm"] = p_qm
    results.attrs["s2-kh"] = s2_kh

    return results
