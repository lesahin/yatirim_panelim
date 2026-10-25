import streamlit as st
import json

with open(
    "data/scores/latest_score.json"
) as f:

    score = json.load(f)

st.set_page_config(
    page_title="Alpha Terminal",
    layout="wide"
)

st.title("🏠 Alpha Terminal")

# SATIR 1

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Makro Skor",
        score["macro_score"]
    )

with c2:
    st.metric(
        "Rejim",
        score["regime"]
    )

with c3:
    st.metric(
        "Alpha Skoru",
        score["alpha_score"]
    )

st.divider()

# SATIR 2

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "Momentum",
        score["nasdaq_momentum"]
    )

with c5:
    st.metric(
        "RSI",
        score["nasdaq_rsi"]
    )

with c6:
    st.metric(
        "Trend Skoru",
        score["nasdaq_trend"]
    )

st.divider()

# SATIR 3

c7, c8, c9 = st.columns(3)

with c7:
    st.metric(
        "Volatilite",
        score["nasdaq_volatility"]
    )

with c8:
    st.metric(
        "Sharpe",
        score["nasdaq_sharpe"]
    )

with c9:
    st.metric(
        "Sortino",
        score["nasdaq_sortino"]
    )

st.divider()

# SATIR 4

c10, c11, c12 = st.columns(3)

with c10:
    st.metric(
        "Max Drawdown",
        score["nasdaq_max_drawdown"]
    )

with c11:
    st.metric(
        "Calmar",
        score["nasdaq_calmar"]
    )

with c12:
    st.metric(
        "Relative Strength",
        score["nasdaq_relative_strength"]
    )

st.divider()

st.subheader("Analiz Özeti")

trend = score["nasdaq_trend"]
rsi = score["nasdaq_rsi"]

if trend >= 80:
    trend_text = "Güçlü Trend"
elif trend >= 50:
    trend_text = "Orta Trend"
else:
    trend_text = "Zayıf Trend"

if rsi >= 70:
    rsi_text = "Aşırı Alım"
elif rsi <= 30:
    rsi_text = "Aşırı Satım"
else:
    rsi_text = "Nötr"

st.info(
    f"""
Trend Durumu: {trend_text}

RSI Durumu: {rsi_text}

Sharpe: {score["nasdaq_sharpe"]}

Sortino: {score["nasdaq_sortino"]}

Alpha Skoru: {score["alpha_score"]}
"""
)
