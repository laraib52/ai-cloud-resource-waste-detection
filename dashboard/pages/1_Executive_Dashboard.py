import streamlit as st
import pandas as pd
import plotly.express as px

from utils.style import load_css
from utils.loader import load_data

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="☁️",
    layout="wide"
)

load_css()

# ==========================
# Page-level CSS refinements
# (theme-aware, does not touch global style.css)
# ==========================

st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 0.9rem !important;
        padding-bottom: 0.9rem !important;
        padding-left: 1.6rem !important;
        padding-right: 1.6rem !important;
        max-width: 100% !important;
    }

    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        gap: 0.55rem !important;
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
        box-shadow: 0 10px 22px rgba(15,23,42,0.10);
        transform: translateY(-2px);
        border-color: var(--brand-primary, #2563EB);
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        margin-bottom: 0 !important;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
        margin-bottom: 0 !important;
    }

    div[data-testid="stMetricDelta"] {
        font-size: 0.8rem !important;
        margin-top: 0 !important;
    }

    .kpi-card-label{
        text-align: center;
        font-size: 0.92rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        color: var(--text-color);
        opacity: 0.85;
    }

    h1 {
        font-size: 1.7rem !important;
        font-weight: 700 !important;
        margin-top: 0 !important;
        margin-bottom: 0.2rem !important;
        padding-bottom: 0 !important;
    }

    h2, h3 {
        font-weight: 700 !important;
        margin-top: 0.2rem !important;
        margin-bottom: 0.35rem !important;
    }

    hr {
        margin: 0.55rem 0 !important;
        border-top: 1px solid var(--border-softer, rgba(120,130,150,0.15)) !important;
    }

    [data-testid="stInfo"],
    [data-testid="stSuccess"],
    [data-testid="stWarning"],
    [data-testid="stError"] {
        padding: 0.65rem 1rem !important;
        margin: 0.3rem 0 !important;
        font-size: 0.9rem !important;
        border-radius: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

PLOTLY_TEMPLATE = "plotly_white"

# ==========================
# Load Data
# ==========================

_, df, forecast = load_data()

# ==========================
# Header
# ==========================

with st.container(border=True):
    st.title("☁️ Executive Analytics Dashboard")
    st.caption(
        "Real-time Cloud Intelligence powered by Machine Learning"
    )

st.divider()

# ==========================
# KPI Calculations
# ==========================

total_resources = df["resource_id"].nunique()

total_records = len(df)

total_cost = df["monthly_cost"].sum()

total_anomalies = (df["prediction"] == "Anomaly").sum()

potential_saving = df.loc[
    df["prediction"] == "Anomaly",
    "monthly_cost"
].sum() * 0.30

# ==========================
# Additional KPI Metrics
# ==========================

waste_percent = (
    total_anomalies / total_records
) * 100

avg_cost = (
    total_cost / total_resources
)

health_score = 100 - waste_percent

# ==========================
# KPI Cards - Equal Height Row
# ==========================

c1, c2, c3, c4 = st.columns(4, gap="small")

with c1:
    with st.container(border=True):
        st.markdown("<div class='kpi-card-label'>🖥 Resources</div>", unsafe_allow_html=True)
        st.metric("", f"{total_resources:,}")
        st.caption("Cloud Resources")

with c2:
    with st.container(border=True):
        st.markdown("<div class='kpi-card-label'>💰 Cloud Cost</div>", unsafe_allow_html=True)
        st.metric("", f"${total_cost:,.0f}")
        st.caption("Current Spend")

with c3:
    with st.container(border=True):
        st.markdown("<div class='kpi-card-label'>⚠ AI Anomalies</div>", unsafe_allow_html=True)
        st.metric("", total_anomalies)
        st.caption("Detected by AI")

with c4:
    with st.container(border=True):
        st.markdown("<div class='kpi-card-label'>💵 Savings</div>", unsafe_allow_html=True)
        st.metric("", f"${potential_saving:,.0f}")
        st.caption("Estimated Monthly")

# Health Score - Inline
if health_score >= 90:
    st.success(f"🟢 AI Infrastructure Health Score : {health_score:.1f}/100")

elif health_score >= 75:
    st.warning(f"🟡 AI Infrastructure Health Score : {health_score:.1f}/100")

else:
    st.error(f"🔴 AI Infrastructure Health Score : {health_score:.1f}/100")

st.divider()

# ==========================
# AI Insights
# ==========================

st.subheader("🤖 AI Insights")

highest_region = (
    df.groupby("region")["monthly_cost"]
    .sum()
    .idxmax()
)

highest_service = (
    df.groupby("service")["monthly_cost"]
    .sum()
    .idxmax()
)

anomaly_rate = (
    total_anomalies /
    total_records
) * 100

st.info(
    f"""
**🤖 AI Executive Summary**

- Total Resources : **{total_resources:,}**
- AI detected **{total_anomalies}** anomalous workloads
- Estimated Monthly Saving : **${potential_saving:,.0f}**
- Highest Spending Region : **{highest_region}**
- Highest Spending Service : **{highest_service}**
- Infrastructure Health Score : **{health_score:.1f}/100**
- Waste Percentage : **{waste_percent:.2f}%**
"""
)

st.divider()

# ==========================
# Charts Row 1
# ==========================

left, right = st.columns(2, gap="medium")

with left:
    fig = px.pie(
        df,
        names="prediction",
        title="Prediction Distribution",
        hole=0.5,
        template=PLOTLY_TEMPLATE
    )
    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=35, b=10),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.05,
            xanchor="center",
            x=0.5,
            font=dict(size=9)
        ),
        font=dict(size=11)
    )
    with st.container(border=True):
        st.plotly_chart(
            fig,
            width="stretch"
        )

with right:
    region = (
        df.groupby("region")["monthly_cost"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region,
        x="region",
        y="monthly_cost",
        color="monthly_cost",
        title="Region-wise Cost",
        template=PLOTLY_TEMPLATE
    )
    fig.update_layout(
        height=250,
        margin=dict(l=40, r=20, t=35, b=30),
        showlegend=False,
        font=dict(size=11),
        xaxis_tickfont_size=9,
        yaxis_tickfont_size=9
    )
    with st.container(border=True):
        st.plotly_chart(
            fig,
            width="stretch"
        )

# ==========================
# Charts Row 2
# ==========================

left, right = st.columns(2, gap="medium")

with left:
    env = (
        df.groupby("environment")["monthly_cost"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        env,
        x="environment",
        y="monthly_cost",
        color="environment",
        title="Environment Cost",
        template=PLOTLY_TEMPLATE
    )
    fig.update_layout(
        height=250,
        margin=dict(l=40, r=20, t=35, b=30),
        showlegend=False,
        font=dict(size=11),
        xaxis_tickfont_size=9,
        yaxis_tickfont_size=9
    )
    with st.container(border=True):
        st.plotly_chart(
            fig,
            width="stretch"
        )

with right:
    service = (
        df.groupby("service")["monthly_cost"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        service,
        x="service",
        y="monthly_cost",
        color="service",
        title="Service Cost",
        template=PLOTLY_TEMPLATE
    )
    fig.update_layout(
        height=250,
        margin=dict(l=40, r=20, t=35, b=30),
        showlegend=False,
        font=dict(size=11),
        xaxis_tickfont_size=9,
        yaxis_tickfont_size=9
    )
    with st.container(border=True):
        st.plotly_chart(
            fig,
            width="stretch"
        )

# ==========================
# Top Costly Resources
# ==========================

st.subheader("🔥 Top 10 Costliest Resources")

top = (
    df.groupby("resource_id")["monthly_cost"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top,
    x="resource_id",
    y="monthly_cost",
    color="monthly_cost",
    title="Top 10 Costliest Resources",
    template=PLOTLY_TEMPLATE
)
fig.update_layout(
    height=240,
    margin=dict(l=50, r=20, t=35, b=60),
    showlegend=False,
    font=dict(size=11),
    xaxis_tickfont_size=8,
    xaxis_tickangle=-45,
    yaxis_tickfont_size=9
)

with st.container(border=True):
    st.plotly_chart(
        fig,
        width="stretch"
    )

# ==========================
# Forecast
# ==========================

st.subheader("📈 Cost Forecast")

fig = px.line(
    forecast.tail(90),
    x="ds",
    y="yhat",
    markers=True,
    title="90-Day Cloud Cost Forecast",
    template=PLOTLY_TEMPLATE
)
fig.update_layout(
    height=240,
    margin=dict(l=50, r=20, t=35, b=30),
    showlegend=False,
    font=dict(size=11),
    xaxis_tickfont_size=8,
    yaxis_tickfont_size=9
)
fig.update_traces(marker=dict(size=3))

with st.container(border=True):
    st.plotly_chart(
        fig,
        width="stretch"
    )

st.success("✔ Dashboard Updated Successfully")