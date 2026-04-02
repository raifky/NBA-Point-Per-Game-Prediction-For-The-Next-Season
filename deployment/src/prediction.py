import os
import json
import joblib
import pandas as pd
import streamlit as st

def run():
    st.title("NBA Player PTS Prediction")

    @st.cache_resource
    def load_model():
        BASE_DIR = os.path.dirname(__file__)
        model = joblib.load(os.path.join(BASE_DIR, "ridge_pipeline.pkl"))

        with open(os.path.join(BASE_DIR, "model_metadata.json"), "r") as f:
            metadata = json.load(f)

        return model, metadata

    model, metadata = load_model()

    num_features = metadata["numerical_features"]
    cat_features = metadata["categorical_features"]
    required_cols = num_features + cat_features

    st.subheader("Masukkan Statistik Pemain")

    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Age", min_value=18, max_value=45, value=30)
        MP = st.number_input("Minutes Played (MP)", value=32.0)
        FGA = st.number_input("Field Goal Attempts (FGA)", value=18.0)
        PA3 = st.number_input("3 Point Attempts (3PA)", value=8.0)
        FTA = st.number_input("Free Throw Attempts (FTA)", value=4.0)

    with col2:
        AST = st.number_input("Assists (AST)", value=5.0)
        TRB = st.number_input("Total Rebounds (TRB)", value=4.0)
        TOV = st.number_input("Turnovers (TOV)", value=2.5)
        Pos = st.selectbox("Position", ["PG", "SG", "SF", "PF", "C"])


    if st.button("🔮 Predict PTS"):
        X_new = pd.DataFrame([{
            "Age": Age,
            "MP": MP,
            "FGA": FGA,
            "3PA": PA3,
            "FTA": FTA,
            "AST": AST,
            "TRB": TRB,
            "TOV": TOV,
            "Pos": Pos
        }])

        # validasi kolom
        missing = set(required_cols) - set(X_new.columns)
        if missing:
            st.error(f"Kolom hilang: {missing}")
        else:
            pred = model.predict(X_new)[0]
            st.success(f" Prediksi Points Per Game (PTS): **{pred:.2f}**")
