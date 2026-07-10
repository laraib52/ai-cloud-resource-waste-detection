import streamlit as st
import pandas as pd
import plotly.express as px
from utils.style import load_css
from utils.loader import load_data

st.set_page_config(page_title="AI Anomaly Detection", layout="wide")

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
        padding-left: 1.6rem !important;
        padding-right: 1.6rem !important;
    }

    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        gap: 0.5rem !important;
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
        box-shadow: 0 10px 22px rgba(15,23,42,0.12);
        transform: translateY(-2px);
        border-color: var(--brand-primary, #2563EB);
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.5rem;
        font-weight: 700;
    }

    h1, h2, h3 {
        margin-top: 0rem;
        margin-bottom: 0.3rem;
    }

    .section-label{
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        color: var(--text-color);
    }
    </style>
    """,
    unsafe_allow_html=True
)

PLOTLY_TEMPLATE = "plotly_dark"

# ==========================
# ==========================
# Load Data
# ==========================

df, _, _ = load_data()
# ==========================
# Header
# ==========================

with st.container(border=True):
    st.markdown("### 🤖 AI Anomaly Detection")
    st.caption("Machine Learning Based Resource Classification")

# ==========================
# Sidebar Filters
# ==========================

region = st.sidebar.multiselect(
    "Select Region",
    sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

environment = st.sidebar.multiselect(
    "Select Environment",
    sorted(df["environment"].unique()),
    default=sorted(df["environment"].unique())
)

service = st.sidebar.multiselect(
    "Select Service",
    sorted(df["service"].unique()),
    default=sorted(df["service"].unique())
)

filtered = df[
    (df["region"].isin(region)) &
    (df["environment"].isin(environment)) &
    (df["service"].isin(service))
]

# ==========================
# Search + Records + Download
# ==========================

with st.container(border=True):
    c1, c2, c3 = st.columns([2, 1, 1], gap="medium")

    with c1:
        resource = st.text_input("🔍 Search Resource ID")

    if resource:
        filtered = filtered[
            filtered["resource_id"].str.contains(resource, case=False)
        ]

    with c2:
        st.metric("Records", len(filtered))

    with c3:
        csv = filtered.to_csv(index=False)

        st.download_button(
            "⬇ Download",
            csv,
            "filtered_anomalies.csv",
            "text/csv"
        )

# ==========================
# Charts Row (Side by Side)
# ==========================

left, right = st.columns(2, gap="medium")

with left:
    chart = (
        filtered["prediction"]
        .value_counts()
        .reset_index()
    )
    chart.columns = ["Prediction", "Count"]

    fig = px.bar(
        chart,
        x="Prediction",
        y="Count",
        color="Prediction",
        title="Prediction Distribution",
        template=PLOTLY_TEMPLATE
    )

    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            width="stretch"
        )

with right:
    scatter = px.scatter(
        filtered,
        x="cpu_pct",
        y="ram_pct",
        color="prediction",
        hover_data=["resource_id"],
        title="CPU vs RAM Utilization",
        template=PLOTLY_TEMPLATE
    )

    scatter.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    with st.container(border=True):
        st.plotly_chart(
            scatter,
            width="stretch"
        )

# ==========================
# Detected Resources Table
# ==========================

with st.container(border=True):
    st.markdown("<div class='section-label'>Detected Resources</div>", unsafe_allow_html=True)
    st.dataframe(
        filtered.head(8),
        width="stretch",
        height=210
    )

# ==========================
# Footer
# ==========================

st.caption(
    "Cloud Waste Optimization Platform • AI Anomaly Detection Module"
)