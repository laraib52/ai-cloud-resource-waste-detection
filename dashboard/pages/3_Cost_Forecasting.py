import streamlit as st
import pandas as pd
import plotly.express as px
from utils.loader import load_data

st.set_page_config(page_title="Cost Forecasting", layout="wide")

# ==========================
# Compact Layout CSS
# ==========================

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.4rem;
        font-weight: 700;
    }
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 0.3rem;
    }
    h1, h2, h3 {
        margin-top: 0rem;
        margin-bottom: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

PLOTLY_TEMPLATE = "plotly_white"

# ==========================
# ==========================
# Load Data
# ==========================

_, _, forecast = load_data()
# ==========================
# Header
# ==========================

with st.container(border=True):
    st.markdown("### 📈 Cloud Cost Forecasting")
    st.caption("Predictive Cost Analytics powered by Machine Learning")

# ==========================
# KPI Row
# ==========================

avg_forecast = forecast["yhat"].mean()
max_forecast = forecast["yhat"].max()
min_forecast = forecast["yhat"].min()
next_30_total = forecast.tail(30)["yhat"].sum()

k1, k2, k3, k4 = st.columns(4)

with k1:
    with st.container(border=True):
        st.markdown("##### 💰 Avg Forecast")
        st.metric("", f"${avg_forecast:,.0f}")

with k2:
    with st.container(border=True):
        st.markdown("##### 📈 Peak Forecast")
        st.metric("", f"${max_forecast:,.0f}")

with k3:
    with st.container(border=True):
        st.markdown("##### 📉 Lowest Forecast")
        st.metric("", f"${min_forecast:,.0f}")

with k4:
    with st.container(border=True):
        st.markdown("##### 🗓 Next 30-Day Total")
        st.metric("", f"${next_30_total:,.0f}")

# ==========================
# Chart + Table Side by Side
# ==========================

left, right = st.columns([2, 1])

with left:
    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        title="Forecasted Cloud Cost",
        labels={"ds": "Date", "yhat": "Predicted Cost"},
        template=PLOTLY_TEMPLATE
    )

    fig.update_layout(
        height=270,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width="stretch"
        )

with right:
    with st.container(border=True):
        st.markdown("##### Forecast Data (Last 30 Days)")
        st.dataframe(
            forecast.tail(30),
            width="stretch",
            height=220
        )

        csv = forecast.to_csv(index=False)

        st.download_button(
            "⬇ Download Forecast",
            csv,
            "cost_forecast.csv",
            "text/csv"
        )