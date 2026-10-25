import streamlit as st

st.set_page_config(
    page_title="Yatırım Panelim",
    layout="wide"
)

st.title("📈 Yatırım Panelim")

st.subheader("Piyasa Özeti")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("BIST100", "Yükleniyor...")

with col2:
    st.metric("NASDAQ", "Yükleniyor...")

with col3:
    st.metric("ALTIN", "Yükleniyor...")

with col4:
    st.metric("BRENT", "Yükleniyor...")
