import pandas as pd


def get_close_column(df):

    for col in df.columns:

        if "Close" in str(col):
            return col

    raise ValueError(
        "Close column bulunamadı"
    )


def calculate_momentum(csv_file):

    df = pd.read_csv(csv_file)

    close_col = get_close_column(df)

    current = float(
        df[close_col].iloc[-1]
    )

    previous = float(
        df[close_col].iloc[-22]
    )

    momentum = (
        (current - previous)
        / previous
        * 100
    )

    return round(momentum, 2)


def calculate_daily_change(csv_file):

    df = pd.read_csv(csv_file)

    close_col = get_close_column(df)

    current = float(
        df[close_col].iloc[-1]
    )

    previous = float(
        df[close_col].iloc[-2]
    )

    change = (
        (current - previous)
        / previous
        * 100
    )

    return round(change, 2)
