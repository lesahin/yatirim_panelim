import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title="Yatırım Panelim",
    layout="wide"
)

def get_last_data(symbol):
    df = yf.download(
        symbol,
        period="5d",
        progress=False,
        auto_adjust=True
    )

    last_close = float(df["Close"].iloc[-1])
    prev_close = float(df["Close"].iloc[-2])

    change_pct = (
        (last_close - prev_close)
        / prev_close
        * 100
    )

    return round(last_close, 2), round(change_pct, 2)

st.title("📈 Yatırım Panelim")

st.subheader("Piyasa Özeti")

bist, bist_pct = get_last_data("XU100.IS")
nasdaq, nasdaq_pct = get_last_data("^IXIC")
gold, gold_pct = get_last_data("GC=F")
brent, brent_pct = get_last_data("BZ=F")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "BIST100",
        f"{bist:,.2f}",
        f"{bist_pct}%"
    )

with col2:
    st.metric(
        "NASDAQ",
        f"{nasdaq:,.2f}",
        f"{nasdaq_pct}%"
    )

with col3:
    st.metric(
        "ALTIN",
        f"{gold:,.2f}",
        f"{gold_pct}%"
    )

with col4:
    st.metric(
        "BRENT",
        f"{brent:,.2f}",
        f"{brent_pct}%"
    )
