import pandas as pd
import numpy as np


def get_close_column(df):

    for col in df.columns:

        if "Close" in str(col):
            return col

    raise ValueError(
        "Close column bulunamadı"
    )


def load_close_series(csv_file):

    df = pd.read_csv(csv_file)

    close_col = get_close_column(df)

    return pd.to_numeric(
        df[close_col],
        errors="coerce"
    )


def calculate_momentum(csv_file):

    close = load_close_series(csv_file)

    current = close.iloc[-1]

    previous = close.iloc[-22]

    momentum = (
        (current - previous)
        / previous
        * 100
    )

    return round(
        momentum,
        2
    )


def calculate_daily_change(csv_file):

    close = load_close_series(csv_file)

    current = close.iloc[-1]

    previous = close.iloc[-2]

    change = (
        (current - previous)
        / previous
        * 100
    )

    return round(
        change,
        2
    )


def calculate_volatility(csv_file):

    close = load_close_series(csv_file)

    returns = close.pct_change().dropna()

    volatility = (
        returns.std()
        * np.sqrt(252)
        * 100
    )

    return round(
        volatility,
        2
    )


def calculate_rsi(
    csv_file,
    period=14
):

    close = load_close_series(csv_file)

    delta = close.diff()

    gain = delta.where(
        delta > 0,
        0
    )

    loss = -delta.where(
        delta < 0,
        0
    )

    avg_gain = (
        gain.rolling(period)
        .mean()
    )

    avg_loss = (
        loss.rolling(period)
        .mean()
    )

    rs = avg_gain / avg_loss

    rsi = (
        100
        - (
            100
            / (1 + rs)
        )
    )

    return round(
        float(rsi.iloc[-1]),
        2
    )


def calculate_trend_score(csv_file):

    close = load_close_series(csv_file)

    current = close.iloc[-1]

    ema20 = close.ewm(
        span=20
    ).mean().iloc[-1]

    ema50 = close.ewm(
        span=50
    ).mean().iloc[-1]

    ema200 = close.ewm(
        span=200
    ).mean().iloc[-1]

    score = 0

    if current > ema20:
        score += 30

    if current > ema50:
        score += 30

    if current > ema200:
        score += 40

    return score


def calculate_sharpe(
    csv_file,
    risk_free_rate=0.03
):

    close = load_close_series(csv_file)

    returns = (
        close
        .pct_change()
        .dropna()
    )

    annual_return = (
        returns.mean()
        * 252
    )

    annual_volatility = (
        returns.std()
        * np.sqrt(252)
    )

    sharpe = (
        annual_return
        - risk_free_rate
    ) / annual_volatility

    return round(
        float(sharpe),
        2
    )
