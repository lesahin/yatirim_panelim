import streamlit as st
import json

with open(
    "data/scores/latest_score.json"
) as f:

    score = json.load(f)

st.title("🏠 Genel Görünüm")

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
