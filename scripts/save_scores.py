import json

from engines.market_engine import (
    calculate_momentum,
    calculate_rsi,
    calculate_volatility,
    calculate_sharpe,
    calculate_trend_score,
    calculate_sortino,
    calculate_max_drawdown,
    calculate_calmar,
    calculate_relative_strength
)

from engines.alpha_engine import (
    calculate_alpha_score
)

from engines.macro_engine import (
    calculate_macro_score
)

from engines.regime_engine import (
    detect_regime
)

# MOMENTUM

nasdaq_momentum = calculate_momentum(
    "data/nasdaq.csv"
)

gold_momentum = calculate_momentum(
    "data/gold.csv"
)

brent_momentum = calculate_momentum(
    "data/brent.csv"
)

# RSI

nasdaq_rsi = calculate_rsi(
    "data/nasdaq.csv"
)

# VOLATILITY

nasdaq_volatility = calculate_volatility(
    "data/nasdaq.csv"
)

# SHARPE

nasdaq_sharpe = calculate_sharpe(
    "data/nasdaq.csv"
)

# SORTINO

nasdaq_sortino = calculate_sortino(
    "data/nasdaq.csv"
)

# MAX DRAWDOWN

nasdaq_max_drawdown = (
    calculate_max_drawdown(
        "data/nasdaq.csv"
    )
)

# CALMAR

nasdaq_calmar = calculate_calmar(
    "data/nasdaq.csv"
)

# TREND

nasdaq_trend = calculate_trend_score(
    "data/nasdaq.csv"
)

# RELATIVE STRENGTH

nas
