import json

from engines.alpha_engine import calculate_alpha_score
from engines.macro_engine import calculate_macro_score
from engines.regime_engine import detect_regime


macro_score = calculate_macro_score(
    inflation=70,
    fed=75,
    bonds=60,
    dxy=65,
    gold=80,
    oil=55,
    nasdaq=85
)

regime = detect_regime(
    macro_score
)

alpha_score = calculate_alpha_score(
    momentum=80,
    macro=macro_score,
    risk=75,
    relative_strength=85,
    volatility=70,
    liquidity=80
)

result = {
    "macro_score": macro_score,
    "regime": regime,
    "alpha_score": alpha_score
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
