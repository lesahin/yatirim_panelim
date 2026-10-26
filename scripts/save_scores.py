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
    calculate_inflation_score,
    calculate_liquidity_score,
    calculate_growth_score,
    calculate_bond_score,
    calculate_dollar_score,
    calculate_macro_score
)

from engines.regime_engine import (
    detect_regime
)

# -----------------
# MARKET ANALYSIS
# -----------------

nasdaq_momentum = calculate_momentum(
    "data/nasdaq.csv"
)

gold_momentum = calculate_momentum(
    "data/gold.csv"
)

brent_momentum = calculate_momentum(
    "data/brent.csv"
)

nasdaq_rsi = calculate_rsi(
    "data/nasdaq.csv"
)

nasdaq_volatility = calculate_volatility(
    "data/nasdaq.csv"
)

nasdaq_sharpe = calculate_sharpe(
    "data/nasdaq.csv"
)

nasdaq_sortino = calculate_sortino(
    "data/nasdaq.csv"
)

nasdaq_calmar = calculate_calmar(
    "data/nasdaq.csv"
)

nasdaq_max_drawdown = calculate_max_drawdown(
    "data/nasdaq.csv"
)

nasdaq_relative_strength = (
    calculate_relative_strength(
        "data/nasdaq.csv",
        "data/gold.csv"
    )
)

nasdaq_trend = calculate_trend_score(
    "data/nasdaq.csv"
)

# -----------------
# MACRO ANALYSIS
# -----------------

inflation_score = (
    calculate_inflation_score()
)

liquidity_score = (
    calculate_liquidity_score()
)

growth_score = (
    calculate_growth_score()
)

bond_score = (
    calculate_bond_score()
)

dollar_score = (
    calculate_dollar_score()
)

macro_score = (
    calculate_macro_score(
        inflation_score,
        liquidity_score,
        growth_score,
        bond_score,
        dollar_score
    )
)

# ----------------
