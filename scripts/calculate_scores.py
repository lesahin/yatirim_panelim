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

print("Macro Score:", macro_score)
print("Regime:", regime)
print("Alpha Score:", alpha_score)
