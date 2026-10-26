import os
import requests


FRED_API_KEY = os.getenv(
    "FRED_API_KEY"
)

BASE_URL = (
    "https://api.stlouisfed.org/fred/series/observations"
)


def get_fred_series(series_id):

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

    return data["observations"]


def get_latest_value(series_id):

    observations = get_fred_series(
        series_id
    )

    latest = observations[-1]

    return float(
        latest["value"]
    )


def get_cpi_yoy():

    observations = get_fred_series(
        "CPIAUCSL"
    )

    current = float(
        observations[-1]["value"]
    )

    one_year_ago = float(
        observations[-13]["value"]
    )

    yoy = (
        (current - one_year_ago)
        / one_year_ago
        * 100
    )

    return round(
        yoy,
        2
    )


def get_core_cpi_yoy():

    observations = get_fred_series(
        "CPILFESL"
    )

    current = float(
        observations[-1]["value"]
    )

    one_year_ago = float(
        observations[-13]["value"]
    )

    yoy = (
        (current - one_year_ago)
        / one_year_ago
        * 100
    )

    return round(
        yoy,
        2
    )


def get_fed_rate():

    return get_latest_value(
        "FEDFUNDS"
    )


def get_unemployment():

    return get_latest_value(
        "UNRATE"
    )


def get_10y_treasury():

    return get_latest_value(
        "GS10"
    )


def get_2y_treasury():

    return get_latest_value(
        "GS2"
    )


def calculate_inflation_score():

    inflation = get_cpi_yoy()

    if inflation < 2:
        return 100

    elif inflation < 3:
        return 85

    elif inflation < 4:
        return 70

    elif inflation < 6:
        return 50

    return 25


def calculate_liquidity_score():

    fed = get_fed_rate()

    if fed < 2:
        return 100

    elif fed < 3:
        return 85

    elif fed < 4:
        return 70

    elif fed < 5:
        return 55

    return 35


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
        return 100

    elif spread > 0:
        return 75

    elif spread > -0.5:
        return 50

    return 25


def calculate_dollar_score():

    # v0.6 geçici skor
    # Bir sonraki aşamada DXY API bağlanacak

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
