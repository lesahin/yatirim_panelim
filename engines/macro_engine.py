def calculate_inflation_score():

    return 70


def calculate_liquidity_score():

    return 75


def calculate_growth_score():

    return 65


def calculate_bond_score():

    return 60


def calculate_dollar_score():

    return 55


def calculate_macro_score(
    inflation_score,
    liquidity_score,
    growth_score,
    bond_score,
    dollar_score
):

    score = (

        inflation_score * 0.25 +

        liquidity_score * 0.25 +

        growth_score * 0.20 +

        bond_score * 0.15 +

        dollar_score * 0.15

    )

    return round(
        score,
        2
    )
