import yfinance as yf
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

assets = {
    "nasdaq": "^IXIC",
    "gold": "GC=F",
    "brent": "BZ=F",
    "usdtry": "USDTRY=X"
}

for name, symbol in assets.items():

    df = yf.download(
        symbol,
        period="1y",
        interval="1d",
        progress=False,
        auto_adjust=True
    )

    df = df.reset_index()

    df.columns = [
        str(col[0]) if isinstance(col, tuple)
        else str(col)
        for col in df.columns
    ]

    df.to_csv(
        f"data/{name}.csv",
        index=False
    )

print("Tamamlandı")
