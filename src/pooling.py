"""Random-effects meta-analysis pooling.
HKSJ variant: uses max(1, s²_HK) floor per Röver et al. (2015) recommendation."""

import numpy as np
from scipy import stats


def reml_estimate(yi: np.ndarray, vi: np.ndarray,
                  X: np.ndarray | None = None,
                  max_iter: int = 200, tol: float = 1e-8) -> float:
    """
    REML estimator of tau-squared via Fisher scoring (Viechtbauer 2005).
    If X is provided, estimates tau2 conditional on the moderator matrix.
    """
    k = len(yi)
    tau2 = dl_estimate(yi, vi)
    for _ in range(max_iter):
        wi = 1.0 / (vi + tau2)
        W = np.diag(wi)
        if X is not None:
            P = W - W @ X @ np.linalg.solve(X.T @ W @ X, X.T @ W)
        else:
            ones = np.ones((k, 1))
            P = W - W @ ones @ (ones.T @ W) / np.sum(wi)
        P_diag = np.diag(P)
        Py = P @ yi
        score = -0.5 * np.trace(P) + 0.5 * (Py @ Py)
        info = 0.5 * np.trace(P @ P)
        if info < 1e-15:
            break
        tau2_new = max(0, tau2 + score / info)
        if abs(tau2_new - tau2) < tol:
            tau2 = tau2_new
            break
        tau2 = tau2_new
    return tau2


def dl_estimate(yi: np.ndarray, vi: np.ndarray) -> float:
    """
    DerSimonian-Laird estimator of tau-squared.
    """
    k = len(yi)
    wi = 1.0 / vi
    mu_fe = np.sum(wi * yi) / np.sum(wi)
    q = np.sum(wi * (yi - mu_fe) ** 2)
    c = np.sum(wi) - np.sum(wi ** 2) / np.sum(wi)
    return max(0, (q - (k - 1)) / c)


def pool(yi: np.ndarray, vi: np.ndarray, tau2: float):
    """Pool with full Hartung-Knapp-Sidik-Jonkman adjustment.
    Q: FE weights + FE mean (Borenstein 2009 Eq 16.3).
    CI: HKSJ scale factor + t(k-1) (Hartung & Knapp 2001).
    PI: t(k-2) per IntHout 2016."""
    k = len(yi)
    wi_re = 1.0 / (vi + tau2)
    mu = np.sum(wi_re * yi) / np.sum(wi_re)

    s2_hk = np.sum(wi_re * (yi - mu) ** 2) / (k - 1) if k > 1 else 1.0
    se_mu_naive = np.sqrt(1.0 / np.sum(wi_re))
    se_mu_hk = se_mu_naive * np.sqrt(max(1.0, s2_hk))

    t_ci = stats.t.ppf(0.975, k - 1) if k > 1 else 1.96
    t_pi = stats.t.ppf(0.975, k - 2) if k > 2 else 1.96
    ci_lo = mu - t_ci * se_mu_hk
    ci_hi = mu + t_ci * se_mu_hk

    wi_fe = 1.0 / vi
    mu_fe = np.sum(wi_fe * yi) / np.sum(wi_fe)
    q = np.sum(wi_fe * (yi - mu_fe) ** 2)
    i2 = max(0, (q - (k - 1)) / q) * 100 if q > 0 else 0
    p_q = 1 - stats.chi2.cdf(q, k - 1)

    pi_lo = mu - t_pi * np.sqrt(tau2 + se_mu_hk ** 2)
    pi_hi = mu + t_pi * np.sqrt(tau2 + se_mu_hk ** 2)

    return {
        "k": k,
        "pooled-lor": mu,
        "se": se_mu_hk,
        "ci-lo": ci_lo,
        "ci-hi": ci_hi,
        "pi-lo": pi_lo,
        "pi-hi": pi_hi,
        "tau2": tau2,
        "tau": np.sqrt(tau2),
        "i2": i2,
        "q": q,
        "df": k - 1,
        "p-q": p_q,
    }


def random_effects(yi: np.ndarray, vi: np.ndarray, method: str = "reml"):
    """
    Full random-effects pooling.
    """
    yi, vi = np.asarray(yi, float), np.asarray(vi, float)
    if method == "reml":
        tau2 = reml_estimate(yi, vi)
    else:
        tau2 = dl_estimate(yi, vi)
    return pool(yi, vi, tau2)
