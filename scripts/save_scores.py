import json

from engines.market_engine import (
    calculate_momentum,
    calculate_rsi,
    calculate_volatility,
    calculate_sharpe,
    calculate_trend_score
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

# MARKET VERILERI

nasdaq_momentum = calculate_momentum(
    "data/nasdaq.csv"
)

gold_momentum = calculate_momentum(
    "data/gold.csv"
)

brent_momentum = calculate_momentum(
    "data/brent.csv"
)

# NASDAQ TEKNIK METRIKLERI

nasdaq_rsi = calculate_rsi(
    "data/nasdaq.csv"
)

nasdaq_volatility = calculate_volatility(
    "data/nasdaq.csv"
)

nasdaq_sharpe = calculate_sharpe(
    "data/nasdaq.csv"
)

nasdaq_trend = calculate_trend_score(
    "data/nasdaq.csv"
)

# MAKRO SKOR

macro_score = calculate_macro_score(
    inflation=70,
    fed=75,
