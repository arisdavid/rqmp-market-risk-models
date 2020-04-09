import argparse
import logging

from market_risk_models.market_risk_models import geometric_brownian_motion

logging.basicConfig(level=logging.INFO)


def monte_carlo_simulation(num_sims, model, **kwargs):
    """
    Monte Carlo Simulator
    :param num_sims: Number of iterations
    :param model: function to be iterated
    :param kwargs: keyword arguments
    :return: yield generator object
    """

    for n_sim in range(num_sims):
        yield model(**kwargs)


if __name__ == "__main__":

    model = {"gbm": geometric_brownian_motion}

    parser = argparse.ArgumentParser("Geometric Brownian Motion")
    parser.add_argument("model_name", help="model", type=str)
    parser.add_argument("num_simulations", help="Number of simulations", type=int)
    parser.add_argument("starting_value", help="Starting value", type=float)
    parser.add_argument("mu", help="Expected annual return", type=float)
    parser.add_argument("sigma", help="Expected annual volatility", type=float)
    parser.add_argument("forecast_period", help="Forecast period in days", type=int)
    parser.add_argument(
        "num_trading_days", help="Number of trading days in year", type=int
    )

    args = parser.parse_args()

    model = model.get(args.model_name)

    asset_paths = monte_carlo_simulation(
        args.num_simulations,
        model,
        starting_value=args.starting_value,
        mu=args.mu,
        sigma=args.sigma,
        forecast_period=args.forecast_period,
        num_trading_days=args.num_trading_days,
    )

    for asset_path in asset_paths:
        curve_agg = +asset_path

    logging.info(curve_agg)
