def calculate_macro_score(
    inflation,
    fed,
    bonds,
    dxy,
    gold,
    oil,
    nasdaq
):

    score = (
        inflation * 0.20 +
        fed * 0.15 +
        bonds * 0.15 +
        dxy * 0.10 +
        gold * 0.10 +
        oil * 0.10 +
        nasdaq * 0.20
    )

    return round(score, 2)
