import os
import requests


FRED_API_KEY = os.getenv(
    "FRED_API_KEY"
)

BASE_URL = (
    "https://api.stlouisfed.org/fred/series/observations"
)


def get_fred_value(series_id):

    response = requests.get(
        BASE_URL,
        params={
            "series_id": series_id,
            "api_key": FRED_API_KEY,
            "file_type": "json"
        },
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    observations = data[
        "observations"
    ]

    latest = observations[-1]

    return float(
        latest["value"]
    )


def get_cpi():

    return get_fred_value(
        "CPIAUCSL"
    )


def get_core_cpi():

    return get_fred_value(
        "CPILFESL"
    )


def get_fed_rate():

    return get_fred_value(
        "FEDFUNDS"
    )


def get_unemployment():

    return get_fred_value(
        "UNRATE"
    )


def get_10y_treasury():

    return get_fred_value(
        "GS10"
    )


def get_2y_treasury():

    return get_fred_value(
        "GS2"
    )


def calculate_inflation_score():

    cpi = get_cpi()

    if cpi < 250:
        return 90

    elif cpi < 300:
        return 75

    elif cpi < 350:
        return 60

    return 40


def calculate_liquidity_score():

    fed = get_fed_rate()

    if fed < 2:
        return 100

    elif fed < 4:
        return 80

    elif fed < 5:
        return 60

    return 40


def calculate_growth_score():

    unemployment = get_unemployment()

    if unemployment < 4:
        return 90

    elif unemployment < 5:
        return 75

    elif unemployment < 6:
        return 60

    return 40


def calculate_bond_score():

    ten_year = get_10y_treasury()

    two_year = get_2y_treasury()

    spread = (
        ten_year
        - two_year
    )

    if spread > 1:
        return 90

    elif spread > 0:
        return 70

    elif spread > -1:
        return 50

    return 25


def calculate_dollar_score():

    return 60


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
