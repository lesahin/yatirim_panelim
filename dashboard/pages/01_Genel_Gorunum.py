import streamlit as st
import json

with open(
    "data/scores/latest_score.json"
) as f:

    score = json.load(f)

st.title("🏠 Alpha Terminal")

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
        "Alpha Skor",
        score["alpha_score"]
    )

st.divider()

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "NASDAQ Momentum",
        score["nasdaq_momentum"]
    )

with c5:
    st.metric(
        "Altın Momentum",
        score["gold_momentum"]
    )

with c6:
    st.metric(
        "Brent Momentum",
        score["brent_momentum"]
    )
