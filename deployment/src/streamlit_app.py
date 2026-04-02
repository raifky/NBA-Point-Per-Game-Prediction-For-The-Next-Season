# streamlit_app.py
import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title="NBA Analytics App",
    layout="wide"
)

page = st.sidebar.selectbox(
    "Choose page",
    ("EDA", "Prediction")
)

if page == "EDA":
    eda.run()
else:
    prediction.run()
