import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Yatırım Panelim",
    layout="wide"
)

def get_last_value(file_name):

    df = pd.read_csv(f"data/{file_name}")

    close_col = "Close"

    last = float(df[close_col].iloc[-1])
    prev = float(df[close_col].iloc[-2])

    change = round(
        ((last - prev) / prev) * 100,
        2
    )

    return round(last, 2), change


nasdaq, nasdaq_change = get_last_value("nasdaq.csv")
gold, gold_change = get_last_value("gold.csv")
brent, brent_change = get_last_value("brent.csv")
usdtry, usdtry_change = get_last_value("usdtry.csv")

st.title("📈 Yatırım Panelim")

st.subheader("Günlük Piyasa Özeti")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "NASDAQ",
        f"{nasdaq:,.2f}",
        f"{nasdaq_change}%"
    )

with c2:
    st.metric(
        "ALTIN",
        f"{gold:,.2f}",
        f"{gold_change}%"
    )

with c3:
    st.metric(
        "BRENT",
        f"{brent:,.2f}",
        f"{brent_change}%"
    )

with c4:
    st.metric(
        "USD/TRY",
        f"{usdtry:,.2f}",
        f"{usdtry_change}%"
    )
st.divider()

st.subheader("NASDAQ Son 1 Yıl")

nasdaq_df = pd.read_csv("data/nasdaq.csv")

st.write(nasdaq_df.columns)
