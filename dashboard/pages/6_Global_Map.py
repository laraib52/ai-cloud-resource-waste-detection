import streamlit as st
import pandas as pd
import plotly.express as px

from utils.style import load_css
from utils.region_coordinates import REGION_COORDINATES

st.set_page_config(
    page_title="Global Infrastructure",
    page_icon="🌍",
    layout="wide"
)

load_css()

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

# ==========================
# Header
# ==========================

with st.container(border=True):
    st.markdown("### 🌍 Global Cloud Infrastructure")
    st.caption("Worldwide Distribution of Cloud Resources")

# ==========================
# Load Data
# ==========================

df = pd.read_csv("../data/processed/cloud_recommendations.csv")

# ==========================
# Region Summary
# ==========================

summary = (
    df.groupby("region")
    .agg(
        Monthly_Cost=("monthly_cost", "sum"),
        Resources=("resource_id", "nunique"),
        Anomalies=("prediction", lambda x: (x == "Anomaly").sum())
    )
    .reset_index()
)

summary["Latitude"] = summary["region"].apply(
    lambda x: REGION_COORDINATES[x]["lat"]
)

summary["Longitude"] = summary["region"].apply(
    lambda x: REGION_COORDINATES[x]["lon"]
)

summary["Country"] = summary["region"].apply(
    lambda x: REGION_COORDINATES[x]["country"]
)

# ==========================
# KPI Row
# ==========================

total_regions = summary["region"].nunique()
total_resources = summary["Resources"].sum()
total_cost = summary["Monthly_Cost"].sum()
total_anomalies = summary["Anomalies"].sum()

k1, k2, k3, k4 = st.columns(4)

with k1:
    with st.container(border=True):
        st.markdown("##### 🌐 Regions")
        st.metric("", total_regions)

with k2:
    with st.container(border=True):
        st.markdown("##### 🖥 Resources")
        st.metric("", f"{total_resources:,}")

with k3:
    with st.container(border=True):
        st.markdown("##### 💰 Total Cost")
        st.metric("", f"${total_cost:,.0f}")

with k4:
    with st.container(border=True):
        st.markdown("##### ⚠ Anomalies")
        st.metric("", total_anomalies)

# ==========================
# Interactive Map
# ==========================

fig = px.scatter_geo(
    summary,
    lat="Latitude",
    lon="Longitude",
    size="Monthly_Cost",
    color="Anomalies",
    hover_name="region",
    hover_data={
        "Country": True,
        "Monthly_Cost": ":,.0f",
        "Resources": True,
        "Anomalies": True,
        "Latitude": False,
        "Longitude": False
    },
    projection="natural earth",
    title="Global Cloud Infrastructure"
)

fig.update_geos(
    showcountries=True,
    countrycolor="gray",
    showcoastlines=True,
    coastlinecolor="white",
    showland=True,
    landcolor="#1f2937",
    showocean=True,
    oceancolor="#0b1120",
    bgcolor="#0b1120"
)

fig.update_layout(
    paper_bgcolor="#0b1120",
    plot_bgcolor="#0b1120",
    font=dict(color="white"),
    height=430,
    margin=dict(l=10, r=10, t=40, b=10)
)

with st.container(border=True):
    st.plotly_chart(
        fig,
        width="stretch"
    )

st.success("Interactive Global Infrastructure Loaded Successfully")