def detect_regime(macro_score):

    if macro_score >= 80:
        return "RISK_ON"

    elif macro_score >= 60:
        return "NEUTRAL"

    elif macro_score >= 40:
        return "CAUTION"

    return "RISK_OFF"
