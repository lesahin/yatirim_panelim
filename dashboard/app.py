import streamlit as st
import json

st.set_page_config(
    page_title="Alpha Terminal",
    layout="wide"
)

with open(
    "data/scores/latest_score.json"
) as f:

    score = json.load(f)

st.title("🏠 Alpha Terminal")

# -----------------
# ÜST SATIR
# -----------------

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

# -----------------
# MAKRO SKORLAR
# -----------------

st.subheader("📈 Makro Skorlar")

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

# -----------------
# GERÇEK MAKRO VERİLER
# -----------------

st.subheader("📊 Gerçek Makro Veriler")

c9, c10, c11 = st.columns(3)

with c9:
    st.metric(
        "CPI YoY %",
        score["cpi_yoy"]
    )

with c10:
    st.metric(
        "Core CPI %",
        score["core_cpi_yoy"]
    )

with c11:
    st.metric(
        "FED Funds %",
        score["fed_rate"]
    )

c12, c13, c14, c15 = st.columns(4)

with c12:
    st.metric(
        "İşsizlik %",
        score["unemployment"]
    )

with c13:
    st.metric(
        "10Y Treasury %",
        score["ten_year"]
    )

with c14:
    st.metric(
        "2Y Treasury %",
        score["two_year"]
    )

with c15:
    st.metric(
        "Yield Curve",
        score["yield_curve"]
    )

st.divider()

# -----------------
# TEKNİK ANALİZ
# -----------------

st.subheader("📉 Teknik Analiz")

c16, c17, c18, c19 = st.columns(4)

with c16:
    st.metric(
        "Momentum",
        score["nasdaq_momentum"]
    )

with c17:
    st.metric(
        "RSI",
        score["nasdaq_rsi"]
    )

with c18:
    st.metric(
        "Trend",
        score["nasdaq_trend"]
    )

with c19:
    st.metric(
        "Relative Strength",
        score["nasdaq_relative_strength"]
    )

st.divider()

# -----------------
# RİSK GÖSTERGELERİ
# -----------------

st.subheader("⚠️ Risk Göstergeleri")

c20, c21, c22, c23 = st.columns(4)

with c20:
    st.metric(
        "Volatilite",
        score["nasdaq_volatility"]
    )

with c21:
    st.metric(
        "Sharpe",
        score["nasdaq_sharpe"]
    )

with c22:
    st.metric(
        "Sortino",
        score["nasdaq_sortino"]
    )

with c23:
    st.metric(
        "Calmar",
        score["nasdaq_calmar"]
    )

st.metric(
    "Max Drawdown",
    score["nasdaq_max_drawdown"]
)

st.divider()

# -----------------
# PORTFÖY
# -----------------

st.subheader("💼 Önerilen Portföy Dağılımı")

c24, c25, c26, c27 = st.columns(4)

with c24:
    st.metric(
        "Hisse %",
        score["recommended_equity"]
    )

with c25:
    st.metric(
        "Fon %",
        score["recommended_fund"]
    )

with c26:
    st.metric(
        "Altın %",
        score["recommended_gold"]
    )

with c27:
    st.metric(
        "Nakit %",
        score["recommended_cash"]
    )

st.divider()

# -----------------
# ÖZET
# -----------------

st.subheader("🧠 Sistem Özeti")

st.info(
    f"""
Makro Skor: {score['macro_score']}

Rejim: {score['regime']}

Alpha Skoru: {score['alpha_score']}

CPI YoY: %{score['cpi_yoy']}

FED Funds: %{score['fed_rate']}

İşsizlik: %{score['unemployment']}

Yield Curve: {score['yield_curve']}

RSI: {score['nasdaq_rsi']}

Momentum: {score['nasdaq_momentum']}
"""
)
