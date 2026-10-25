import yfinance as yf
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

    df.to_csv(f"data/{name}.csv")

print("Tamamlandı")
