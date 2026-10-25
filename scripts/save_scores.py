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

# TREND

nasdaq_trend = calculate_trend_score(
    "data/nasdaq.csv"
)

# MACRO SCORE

macro_score = calculate_macro_score(
    inflation=70,
    fed=75,
    bonds=60,
    dxy=65,
    gold=gold_momentum,
    oil=brent_momentum,
    nasdaq=nasdaq_momentum
)

# REGIME

regime = detect_regime(
    macro_score
)

# ALPHA SCORE

alpha_score = calculate_alpha_score(
    momentum=nasdaq_momentum,
    macro=macro_score,
    risk=75,
    relative_strength=80,
    volatility=max(
        0,
        100 - nasdaq_volatility
    ),
    liquidity=80
)

# JSON OUTPUT

result = {
    "macro_score": round(macro_score, 2),
    "regime": regime,
    "alpha_score": round(alpha_score, 2),

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
