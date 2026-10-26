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

# ÜST SATIR

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Makro Skor",
        score["macro_score"]
    )

with c2:
    st.metric(
        "Piyasa Rejimi",
        score["regime"]
    )

with c3:
    st.metric(
        "Alpha Skoru",
        score["alpha_score"]
    )

st.divider()

# MAKRO SATIRI

c4, c5, c6, c7, c8 = st.columns(5)

with c4:
    st.metric(
        "Enflasyon",
        score["inflation_score"]
    )

with c5:
    st.metric(
        "Likidite",
        score["liquidity_score"]
    )

with c6:
    st.metric(
        "Büyüme",
        score["growth_score"]
    )

with c7:
    st.metric(
        "Tahvil",
        score["bond_score"]
    )

with c8:
    st.metric(
        "Dolar",
        score["dollar_score"]
    )

st.divider()

# TEKNİK ANALİZ

c9, c10, c11, c12 = st.columns(4)

with c9:
    st.metric(
        "Momentum",
        score["nasdaq_momentum"]
    )

with c10:
    st.metric(
        "RSI",
        score["nasdaq_rsi"]
    )

with c11:
    st.metric(
        "Trend",
        score["nasdaq_trend"]
    )

with c12:
    st.metric(
        "Relative Strength",
        score["nasdaq_relative_strength"]
    )

st.divider()

# RİSK ANALİZİ

c13, c14, c15, c16 = st.columns(4)

with c13:
    st.metric(
        "Volatilite",
        score["nasdaq_volatility"]
    )

with c14:
    st.metric(
        "Sharpe",
        score["nasdaq_sharpe"]
    )

with c15:
    st.metric(
        "Sortino",
        score["nasdaq_sortino"]
    )

with c16:
    st.metric(
        "Calmar",
        score["nasdaq_calmar"]
    )

st.divider()

# DRAWDOWN

st.metric(
    "Max Drawdown",
    score["nasdaq_max_drawdown"]
)

st.divider()

# PORTFÖY ÖNERİSİ

st.subheader("Önerilen Portföy Dağılımı")

c17, c18, c19, c20 = st.columns(4)

with c17:
    st.metric(
        "Hisse %",
        score["recommended_equity"]
    )

with c18:
    st.metric(
        "Fon %",
        score["recommended_fund"]
    )

with c19:
    st.metric(
        "Altın %",
        score["recommended_gold"]
    )

with c20:
    st.metric(
        "Nakit %",
        score["recommended_cash"]
    )

st.divider()

# ÖZET

st.subheader("Genel Durum")

st.info(
    f"""
Makro Skor: {score['macro_score']}

Rejim: {score['regime']}

Alpha Skoru: {score['alpha_score']}

RSI: {score['nasdaq_rsi']}

Trend: {score['nasdaq_trend']}

Sharpe: {score['nasdaq_sharpe']}
"""
)
