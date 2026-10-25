import yfinance as yf
import pandas as pd
import os

symbols = {
    "BIST100": "XU100.IS",
    "NASDAQ": "^IXIC",
    "ALTIN": "GC=F",
    "BRENT": "BZ=F"
}

os.makedirs("data", exist_ok=True)

for name, symbol in symbols.items():

    df = yf.download(
        symbol,
        period="1y",
        interval="1d",
        auto_adjust=True
    )

    df.to_csv(f"data/{name}.csv")

print("Veriler güncellendi.")
