import streamlit as st
import pandas as pd
import plotly.express as px

from utils.style import load_css

st.set_page_config(page_title="Recommendations", layout="wide")

load_css()

# ==========================
# Page-level CSS refinements
# ==========================

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 0.9rem !important;
        padding-bottom: 0.9rem !important;
        padding-left: 1.8rem !important;
        padding-right: 1.8rem !important;
    }

    h1 {
        font-size: 1.7rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.15rem !important;
        padding-bottom: 0 !important;
    }

    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        gap: 0.65rem !important;
    }

    /* Equal-height, aligned bordered cards within any row */
    [data-testid="stHorizontalBlock"] [data-testid="stVerticalBlockBorderWrapper"]{
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border-radius: 14px !important;
        transition: box-shadow .2s ease, transform .2s ease, border-color .2s ease;
    }

    [data-testid="stHorizontalBlock"] [data-testid="stVerticalBlockBorderWrapper"]:hover{
        box-shadow: 0 10px 24px rgba(15,23,42,0.12);
        transform: translateY(-2px);
        border-color: var(--brand-primary, #2563EB);
    }

    /* Dark-theme fix: metric card now uses theme-aware background
       instead of a hardcoded light-gray fill that made text
       unreadable in Dark Mode */
    [data-testid="stMetric"] {
        background-color: var(--secondary-background-color);
        border: 1px solid var(--border-soft, rgba(120,130,150,0.18));
        border-radius: 12px;
        padding: 1rem !important;
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.9rem !important;
        font-weight: 800 !important;
        color: var(--brand-primary, #2563EB) !important;
    }

    hr {
        margin: 0.5rem 0 !important;
        height: 1px !important;
        border-top: 1px solid var(--border-softer, rgba(120,130,150,0.15)) !important;
    }

    .rec-panel-title{
        font-size: 1rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.6rem;
    }

    [data-testid="stDownloadButton"] button {
        background-color: var(--brand-primary, #2563EB);
        color: white;
        font-weight: 600;
        padding: 0.5rem 1.3rem;
        border-radius: 8px;
        border: none;
        transition: all 0.2s ease;
        width: 100%;
    }

    [data-testid="stDownloadButton"] button:hover {
        background-color: var(--brand-primary-dark, #1d4ed8);
        transform: translateY(-1px);
        box-shadow: 0 4px 14px rgba(37,99,235,0.35);
    }
    </style>
    """,
    unsafe_allow_html=True
)

PLOTLY_TEMPLATE = "plotly_white"

# ==========================
# Load Data
# ==========================

df = pd.read_csv("../data/processed/cloud_recommendations.csv")

# ==========================
# Header
# ==========================

with st.container(border=True):
    st.title("💡 AI Recommendations")
    st.caption("Final AI-driven optimization decisions and executive-ready action items")

st.divider()

recommendations = df[df["recommendation"] != "No Action Required"]

# ==========================
# KPI + Chart Row
# ==========================

top_left, top_right = st.columns([1, 2], gap="medium")

with top_left:
    with st.container(border=True):
        st.metric(
            "Resources Requiring Action",
            len(recommendations),
            label_visibility="visible"
        )
        st.caption(f"Out of {len(df):,} total tracked resources")

with top_right:
    with st.container(border=True):
        chart = (
            recommendations["recommendation"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["Recommendation", "Count"]

        fig = px.bar(
            chart,
            x="Recommendation",
            y="Count",
            color="Recommendation",
            title="Recommendation Distribution",
            template=PLOTLY_TEMPLATE
        )

        fig.update_layout(
            height=270,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            font=dict(size=11)
        )

        fig.update_traces(
            marker_line_width=1,
            marker_line_color="white",
            opacity=0.9
        )

        st.plotly_chart(fig, width="stretch")

# ==========================
# Detailed Recommendations Table + Download
# ==========================

with st.container(border=True):
    header_left, header_right = st.columns([4, 1], gap="medium")

    with header_left:
        st.markdown("<div class='rec-panel-title'>📋 Detailed Recommendations</div>", unsafe_allow_html=True)

    with header_right:
        csv = recommendations.to_csv(index=False)

        st.download_button(
            "⬇ Download CSV",
            csv,
            "recommendations.csv",
            "text/csv",
            key="download_recommendations"
        )

    st.dataframe(
        recommendations,
        width="stretch",
        height=280,
        hide_index=True
    )