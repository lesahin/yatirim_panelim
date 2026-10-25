import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title="Yatırım Panelim",
    layout="wide"
)

def get_last_data(symbol):
    try:
        df = yf.download(
            symbol,
            period="10d",
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            return "Veri yok", ""

        close = df["Close"]

        if len(close) < 2:
            return round(float(close.iloc[-1]), 2), ""

        last_price = round(float(close.iloc[-1]), 2)
        change = round(
            (
                float(close.iloc[-1])
                - float(close.iloc[-2])
            )
            / float(close.iloc[-2])
            * 100,
            2
        )

        return last_price, f"{change}%"

    except Exception:
        return "Hata", ""

st.title("📈 Yatırım Panelim")

st.subheader("Piyasa Özeti")

col1, col2, col3, col4 = st.columns(4)

bist, bist_change = get_last_data("^XU100")
nasdaq, nasdaq_change = get_last_data("^IXIC")
gold, gold_change = get_last_data("GC=F")
brent, brent_change = get_last_data("BZ=F")

with col1:
    st.metric("BIST100", bist, bist_change)

with col2:
    st.metric("NASDAQ", nasdaq, nasdaq_change)

with col3:
    st.metric("ALTIN", gold, gold_change)

with col4:
    st.metric("BRENT", brent, brent_change)
