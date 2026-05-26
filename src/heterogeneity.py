"""Heterogeneity diagnostics: Baujat, Cook's distance, hat values.
C11 fix: leave-one-out re-estimates tau2 per iteration."""

import numpy as np
import pandas as pd


def baujat(yi: np.ndarray, vi: np.ndarray, tau2: float):
    """Baujat plot data: contribution to Q vs influence on pooled estimate."""
    k = len(yi)
    wi = 1.0 / (vi + tau2)
    mu = np.sum(wi * yi) / np.sum(wi)
    qi = wi * (yi - mu) ** 2

    influence = np.zeros(k)
    for i in range(k):
        mask = np.ones(k, bool)
        mask[i] = False
        wi_loo = wi[mask]
        yi_loo = yi[mask]
        mu_loo = np.sum(wi_loo * yi_loo) / np.sum(wi_loo)
        influence[i] = abs(mu - mu_loo)

    return qi, influence


def cooks_distance(yi: np.ndarray, vi: np.ndarray, tau2: float):
    """Cook's distance for each study."""
    k = len(yi)
    wi = 1.0 / (vi + tau2)
    mu = np.sum(wi * yi) / np.sum(wi)
    se_mu = np.sqrt(1.0 / np.sum(wi))
    cooks = np.zeros(k)
    for i in range(k):
        mask = np.ones(k, bool)
        mask[i] = False
        wi_loo = wi[mask]
        yi_loo = yi[mask]
        mu_loo = np.sum(wi_loo * yi_loo) / np.sum(wi_loo)
        cooks[i] = (mu - mu_loo) ** 2 / se_mu ** 2
    return cooks


def hat_values(vi: np.ndarray, tau2: float):
    """Hat values (leverage) for each study."""
    wi = 1.0 / (vi + tau2)
    return wi / np.sum(wi)


def leave_one_out(yi: np.ndarray, vi: np.ndarray):
    """Leave-one-out with re-estimated tau2 per iteration."""
    from src.pooling import reml_estimate, pool
    k = len(yi)
    results = []
    for i in range(k):
        mask = np.ones(k, bool)
        mask[i] = False
        yi_loo = yi[mask]
        vi_loo = vi[mask]
        tau2_loo = reml_estimate(yi_loo, vi_loo)
        res = pool(yi_loo, vi_loo, tau2_loo)
        results.append({
            "omitted": i,
            "mu": res["pooled-lor"],
            "se": res["se"],
            "ci-lo": res["ci-lo"],
            "ci-hi": res["ci-hi"],
            "tau2": tau2_loo,
            "i2": res["i2"],
        })
    return pd.DataFrame(results)
