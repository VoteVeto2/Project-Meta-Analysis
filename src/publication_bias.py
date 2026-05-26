"""Publication bias tests: funnel, Egger, Begg, trim-and-fill, p-curve."""

import numpy as np
from scipy import stats


def egger_test(yi: np.ndarray, sei: np.ndarray):
    """Egger's regression test for funnel plot asymmetry (Egger 1997).
    Regresses standardized effect (yi/sei) on precision (1/sei).
    The intercept tests for asymmetry."""
    k = len(yi)
    zi = yi / sei
    prec = 1.0 / sei
    X = np.column_stack([np.ones(k), prec])
    beta = np.linalg.lstsq(X, zi, rcond=None)[0]
    resid = zi - X @ beta
    mse = np.sum(resid ** 2) / (k - 2)
    var_beta = mse * np.linalg.inv(X.T @ X)
    se_intercept = np.sqrt(var_beta[0, 0])
    t_intercept = beta[0] / se_intercept
    p_intercept = 2 * (1 - stats.t.cdf(abs(t_intercept), k - 2))
    return {"intercept": beta[0], "slope": beta[1], "se": se_intercept,
            "t": t_intercept, "p": p_intercept, "df": k - 2}


def begg_test(yi: np.ndarray, vi: np.ndarray):
    """Begg and Mazumdar rank correlation test."""
    sei = np.sqrt(vi)
    k = len(yi)
    wi = 1.0 / vi
    mu = np.sum(wi * yi) / np.sum(wi)
    standardized = (yi - mu) / sei
    tau, p = stats.kendalltau(standardized, vi)
    return {"tau": tau, "p": p}


def trim_and_fill(yi: np.ndarray, vi: np.ndarray, side: str = "right"):
    """Trim-and-fill estimator (Duval & Tweedie). Returns adjusted pooled estimate."""
    from src.pooling import random_effects
    k = len(yi)
    wi = 1.0 / vi
    mu = np.sum(wi * yi) / np.sum(wi)

    if side == "right":
        deviations = yi - mu
        candidates = np.argsort(-deviations)
    else:
        deviations = mu - yi
        candidates = np.argsort(-deviations)

    r0_est = 0
    for n_trim in range(k // 2):
        trimmed = np.delete(np.arange(k), candidates[:n_trim])
        wi_t = 1.0 / vi[trimmed]
        mu_t = np.sum(wi_t * yi[trimmed]) / np.sum(wi_t)
        ranks = stats.rankdata(np.abs(yi - mu_t))
        sign_rank = np.sum(ranks[yi > mu_t])
        expected = k * (k + 1) / 4
        if abs(sign_rank - expected) < 1.96 * np.sqrt(k * (k + 1) * (2 * k + 1) / 24):
            r0_est = n_trim
            break

    if r0_est == 0:
        orig = random_effects(yi, vi)
        return {"k0": 0, "k-filled": k, "pooled-lor-adj": orig["pooled-lor"],
                "ci-lo-adj": orig["ci-lo"], "ci-hi-adj": orig["ci-hi"],
                "pooled-lor-orig": orig["pooled-lor"]}

    fill_yi = 2 * mu - yi[candidates[:r0_est]]
    fill_vi = vi[candidates[:r0_est]]
    yi_adj = np.concatenate([yi, fill_yi])
    vi_adj = np.concatenate([vi, fill_vi])
    adj = random_effects(yi_adj, vi_adj)
    orig = random_effects(yi, vi)
    return {"k0": r0_est, "k-filled": len(yi_adj),
            "pooled-lor-adj": adj["pooled-lor"],
            "ci-lo-adj": adj["ci-lo"], "ci-hi-adj": adj["ci-hi"],
            "pooled-lor-orig": orig["pooled-lor"]}


def p_curve(yi: np.ndarray, sei: np.ndarray, alpha: float = 0.05):
    """P-curve analysis: test for evidential value."""
    zi = yi / sei
    p_vals = 2 * (1 - stats.norm.cdf(np.abs(zi)))
    sig = p_vals[p_vals < alpha]
    if len(sig) < 3:
        return {"n-sig": len(sig), "sufficient": False, "note": "too few significant results"}

    pp = sig / alpha
    n_right = np.sum(pp < 0.5)
    n_total = len(pp)
    binom_p = stats.binom_test(n_right, n_total, 0.5) if hasattr(stats, 'binom_test') else stats.binomtest(n_right, n_total, 0.5).pvalue
    return {"n-sig": len(sig), "n-right-skewed": int(n_right),
            "n-total": int(n_total), "prop-right": n_right / n_total,
            "binom-p": binom_p, "evidential-value": binom_p < 0.05}
