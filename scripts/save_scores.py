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

# -----------------
# REGIME
# -----------------

regime = detect_regime(
    macro_score
)

# -----------------
# PORTFOLIO
# -----------------

if regime == "RISK_ON":

    recommended_equity = 50
    recommended_fund = 25
    recommended_gold = 15
    recommended_cash = 10

elif regime == "GROWTH":

    recommended_equity = 35
    recommended_fund = 35
    recommended_gold = 20
    recommended_cash = 10

elif regime == "CAUTION":

    recommended_equity = 25
    recommended_fund = 35
    recommended_gold = 30
    recommended_cash = 10

else:

    recommended_equity = 10
    recommended_fund = 30
    recommended_gold = 40
    recommended_cash = 20

# -----------------
# ALPHA
# -----------------

alpha_score = calculate_alpha_score(
    momentum=nasdaq_momentum,

    macro=macro_score,

    risk=max(
        0,
        100 - abs(
            nasdaq_max_drawdown
        )
    ),

    relative_strength=max(
        0,
        nasdaq_relative_strength + 50
    ),

    volatility=max(
        0,
        100 - nasdaq_volatility
    ),

    liquidity=liquidity_score
)

# -----------------
# OUTPUT
# -----------------

result = {

    "macro_score": round(
        macro_score,
        2
    ),

    "inflation_score": round(
        inflation_score,
        2
    ),

    "liquidity_score": round(
        liquidity_score,
        2
    ),

    "growth_score": round(
        growth_score,
        2
    ),

    "bond_score": round(
        bond_score,
        2
    ),

    "dollar_score": round(
        dollar_score,
        2
    ),

    "regime": regime,

    "recommended_equity":
        recommended_equity,

    "recommended_fund":
        recommended_fund,

    "recommended_gold":
        recommended_gold,

    "recommended_cash":
        recommended_cash,

    "alpha_score": round(
        alpha_score,
        2
    ),

    "nasdaq_momentum": round(
        nasdaq_momentum,
        2
    ),

    "gold_momentum": round(
        gold_momentum,
        2
    ),

    "brent_momentum": round(
        brent_momentum,
        2
    ),

    "nasdaq_rsi": round(
        nasdaq_rsi,
        2
    ),

    "nasdaq_volatility": round(
        nasdaq_volatility,
        2
    ),

    "nasdaq_sharpe": round(
        nasdaq_sharpe,
        2
    ),

    "nasdaq_sortino": round(
        nasdaq_sortino,
        2
    ),

    "nasdaq_calmar": round(
        nasdaq_calmar,
        2
    ),

    "nasdaq_max_drawdown": round(
        nasdaq_max_drawdown,
        2
    ),

    "nasdaq_relative_strength": round(
        nasdaq_relative_strength,
        2
    ),

    "nasdaq_trend": round(
        nasdaq_trend,
        2
    )
}

with open(
    "data/scores/latest_score.json",
    "w"
) as file:

    json.dump(
        result,
        file,
        indent=4
    )

print(
    json.dumps(
        result,
        indent=4
    )
)
