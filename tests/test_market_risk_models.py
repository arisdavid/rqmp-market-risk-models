from unittest import mock

import numpy as np
import pytest
from market_risk_models.market_risk_models import geometric_brownian_motion


@pytest.mark.parametrize(
    "starting_value, mu, sigma, num_trading_days, forecast_period,  expected",
    [
        (
            100,
            0.18,
            0.12,
            250,
            5,
            np.array([100, 100.06912, 100.13824, 100.20736, 100.27648, 100.3456]),
        )
    ],
)
def test_geometric_brownian_motion(
    starting_value, mu, sigma, num_trading_days, forecast_period, expected
):
    """ Test Geometric Brownian Motion """
    with mock.patch(
        "market_risk_models.market_risk_models.np.random.normal",
        return_value=np.array([[0, 0, 0, 0, 0]]),
    ):

        result = geometric_brownian_motion(
            starting_value=starting_value,
            mu=mu,
            sigma=sigma,
            num_trading_days=num_trading_days,
            forecast_period=forecast_period,
        )

        assert np.alltrue(result == expected)
