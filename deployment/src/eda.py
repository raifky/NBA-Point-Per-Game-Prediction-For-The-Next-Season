import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr
import os

def run():
    st.title("📊 Exploratory Data Analysis – NBA Players")


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "sportsref_nba.csv")

    @st.cache_data
    def load_data():
        return pd.read_csv(DATA_PATH)

    nba = load_data()

    st.subheader("Dataset Preview")
    st.dataframe(nba.head())


    def correlation_section(feature, title, insight_text):
        corr, p = spearmanr(nba[feature], nba['PTS'])

        st.markdown(f"### {title}")
        st.write(f"**Spearman Correlation:** `{corr:.3f}`")
        st.write(f"**p-value:** `{p:.5f}`")

        # Scatter + trendline
        fig, ax = plt.subplots()
        ax.scatter(nba[feature], nba['PTS'], alpha=0.6)

        # trendline
        m, b = np.polyfit(nba[feature], nba['PTS'], 1)
        ax.plot(nba[feature], m*nba[feature] + b)

        ax.set_xlabel(feature)
        ax.set_ylabel("PTS")
        ax.set_title(f"Hubungan {feature} terhadap PTS")

        st.pyplot(fig)
        st.markdown(insight_text)
        st.divider()


    correlation_section(
        feature="MP",
        title="EDA Question 2 – Apakah Minutes Played (MP) berpengaruh terhadap PTS?",
        insight_text="""
**Insight:**
- Korelasi MP terhadap PTS sangat kuat (mendekati 1)
- Pemain dengan menit bermain tinggi cenderung mencetak poin lebih banyak
- Semakin lama pemain berada di lapangan, semakin besar peluang mencetak poin
"""
    )


    correlation_section(
        feature="FGA",
        title="Apakah Field Goal Attempted (FGA) berpengaruh terhadap PTS?",
        insight_text="""
**Insight:**
- FGA memiliki korelasi sangat kuat dengan PTS
- Semakin sering pemain melakukan percobaan tembakan, semakin besar peluang mencetak poin
- FGA merupakan indikator agresivitas ofensif pemain
"""
    )


    correlation_section(
        feature="3PA",
        title="EDA Question 4 – Apakah 3-Point Attempt (3PA) mempengaruhi PTS?",
        insight_text="""
**Insight:**
- Hubungan antara 3PA dan PTS tergolong cukup kuat
- Pemain yang sering melakukan tembakan 3 poin berpotensi mencetak poin lebih tinggi
- Namun, efektivitas tetap bergantung pada akurasi tembakan
"""
    )


    correlation_section(
        feature="AST",
        title="EDA Question 5 – Bagaimana hubungan Assist (AST) dengan PTS?",
        insight_text="""
**Insight:**
- AST memiliki korelasi kuat terhadap PTS
- Pemain dengan assist tinggi biasanya memiliki peran ofensif besar
- Assist tinggi sering berkaitan dengan usage rate yang tinggi
"""
    )


    correlation_section(
        feature="PF",
        title="EDA Question 6 – Apakah Personal Foul (PF) berkorelasi dengan PTS?",
        insight_text="""
**Insight:**
- PF memiliki korelasi sedang terhadap PTS
- Pemain dengan foul tinggi belum tentu mencetak poin tinggi
- PF lebih mencerminkan intensitas permainan dibanding kontribusi poin
"""
    )

  
    correlation_section(
        feature="TOV",
        title="EDA Question 7 – Apakah Turnover (TOV) mempengaruhi PTS?",
        insight_text="""
**Insight:**
- TOV memiliki korelasi kuat dengan PTS
- Pemain dengan usage rate tinggi cenderung memiliki turnover dan poin yang tinggi
- Turnover tinggi tidak selalu berarti performa buruk, bisa menunjukkan peran ofensif besar
"""
    )
