st.divider()

st.subheader("📊 Gerçek Makro Veriler")

c21, c22, c23 = st.columns(3)

with c21:
    st.metric(
        "CPI YoY %",
        score["cpi_yoy"]
    )

with c22:
    st.metric(
        "Core CPI %",
        score["core_cpi_yoy"]
    )

with c23:
    st.metric(
        "FED Funds %",
        score["fed_rate"]
    )

c24, c25, c26, c27 = st.columns(4)

with c24:
    st.metric(
        "İşsizlik %",
        score["unemployment"]
    )

with c25:
    st.metric(
        "10Y Treasury %",
        score["ten_year"]
    )

with c26:
    st.metric(
        "2Y Treasury %",
        score["two_year"]
    )

with c27:
    st.metric(
        "Yield Curve",
        score["yield_curve"]
    )
