import pandas as pd


def calculate_momentum(csv_file):

    df = pd.read_csv(csv_file)

    close_col = [c for c in df.columns if "Close" in str(c)][0]

    last_price = float(df[close_col].iloc[-1])

    old_price = float(df[close_col].iloc[-22])

    momentum = (
        (last_price - old_price)
        / old_price
        * 100
    )

    return round(momentum, 2)
