import json

from engines.market_engine import calculate_momentum

from engines.alpha_engine import (
    calculate_alpha_score
)

from engines.macro_engine import (
    calculate_macro_score
)

from engines.regime_engine import (
    detect_regime
)

nasdaq_momentum = calculate_momentum(
    "data/nasdaq.csv"
)

gold_momentum = calculate_momentum(
    "data/gold.csv"
)

brent_momentum = calculate_momentum(
    "data/brent.csv"
)

macro_score = calculate_macro_score(
    inflation=70,
    fed=75,
    bonds=60,
    dxy=65,
    gold=gold_momentum,
    oil=brent_momentum,
    nasdaq=nasdaq_momentum
)

regime = detect_regime(
    macro_score
)

alpha_score = calculate_alpha_score(
    momentum=nasdaq_momentum,
    macro=macro_score,
    risk=75,
    relative_strength=80,
    volatility=70,
    liquidity=80
)

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
    )
}

with open(
    "data/scores/latest_score.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=4
    )

print(result)
