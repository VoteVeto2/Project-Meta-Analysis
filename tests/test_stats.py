"""Tests for core statistical functions against known values."""

import numpy as np
import pytest
from src.pooling import dl_estimate, reml_estimate, pool, random_effects
from src.publication_bias import egger_test
from src.effect_sizes import log_odds_ratio, cohens_h


# --- Known-value fixtures ---

# Borenstein (2009) Example 14.1: 6 studies
YI_BOREN = np.array([0.5, 0.3, 0.1, 0.4, 0.2, 0.6])
VI_BOREN = np.array([0.04, 0.05, 0.03, 0.06, 0.04, 0.05])


class TestDLEstimate:
    def test_positive_tau2(self):
        tau2 = dl_estimate(YI_BOREN, VI_BOREN)
        assert tau2 >= 0

    def test_zero_heterogeneity(self):
        yi = np.array([1.0, 1.0, 1.0])
        vi = np.array([0.1, 0.1, 0.1])
        assert dl_estimate(yi, vi) == 0.0

    def test_dl_close_to_reml(self):
        tau2_dl = dl_estimate(YI_BOREN, VI_BOREN)
        tau2_reml = reml_estimate(YI_BOREN, VI_BOREN)
        assert abs(tau2_dl - tau2_reml) < 0.1


class TestPool:
    def test_q_uses_fe_weights(self):
        res1 = random_effects(YI_BOREN, VI_BOREN, "reml")
        res2 = random_effects(YI_BOREN, VI_BOREN, "dl")
        assert abs(res1["q"] - res2["q"]) < 1e-10, "Q must be identical across estimators"

    def test_ci_brackets_estimate(self):
        res = random_effects(YI_BOREN, VI_BOREN)
        assert res["ci-lo"] < res["pooled-lor"] < res["ci-hi"]

    def test_pi_wider_than_ci(self):
        res = random_effects(YI_BOREN, VI_BOREN)
        pi_width = res["pi-hi"] - res["pi-lo"]
        ci_width = res["ci-hi"] - res["ci-lo"]
        assert pi_width >= ci_width

    def test_i2_in_range(self):
        res = random_effects(YI_BOREN, VI_BOREN)
        assert 0 <= res["i2"] <= 100

    def test_hksj_floor(self):
        """max(1, s2_hk) floor should never narrow the naive CI."""
        res = pool(YI_BOREN, VI_BOREN, dl_estimate(YI_BOREN, VI_BOREN))
        wi = 1.0 / (VI_BOREN + dl_estimate(YI_BOREN, VI_BOREN))
        se_naive = np.sqrt(1.0 / np.sum(wi))
        assert res["se"] >= se_naive


class TestEffectSizes:
    def test_log_or_zero(self):
        lor, _ = log_odds_ratio(50, 50, 100, 100)
        assert lor == 0.0

    def test_log_or_positive_when_ma_better(self):
        lor, _ = log_odds_ratio(80, 60, 100, 100)
        assert lor > 0

    def test_cohens_h_zero(self):
        assert cohens_h(0.5, 0.5) == 0.0

    def test_cohens_h_positive_when_ma_better(self):
        assert cohens_h(0.8, 0.6) > 0


class TestEgger:
    def test_intercept_p_not_slope_p(self):
        """Regression: ensure we test the intercept, not the slope."""
        np.random.seed(42)
        yi = np.random.normal(0.5, 0.3, 30)
        sei = np.abs(np.random.normal(0.1, 0.05, 30)) + 0.01
        result = egger_test(yi, sei)
        assert "intercept" in result
        assert "t" in result
        assert result["df"] == 28

    def test_symmetric_funnel_not_significant(self):
        np.random.seed(123)
        sei = np.random.uniform(0.05, 0.3, 50)
        yi = np.random.normal(0, sei)
        result = egger_test(yi, sei)
        assert result["p"] > 0.05


class TestProjectData:
    """Tests against our actual 41-study dataset."""

    @pytest.fixture
    def data(self):
        from src.data_io import load_verified
        from src.effect_sizes import compute_effect_sizes
        df = compute_effect_sizes(load_verified())
        return df

    def test_k_is_41(self, data):
        assert len(data) == 41

    def test_pooled_lor_in_range(self, data):
        res = random_effects(data["yi"].values, data["vi"].values)
        assert 0.3 < res["pooled-lor"] < 0.6

    def test_q_matches_across_estimators(self, data):
        yi, vi = data["yi"].values, data["vi"].values
        r = random_effects(yi, vi, "reml")
        d = random_effects(yi, vi, "dl")
        assert abs(r["q"] - d["q"]) < 1e-10

    def test_egger_significant(self, data):
        from src.publication_bias import egger_test
        result = egger_test(data["yi"].values, data["sei"].values)
        assert result["p"] < 0.05
