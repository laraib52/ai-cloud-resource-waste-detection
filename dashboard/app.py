import streamlit as st
import os

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Cloud Waste Optimization",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Load Custom CSS
# ==========================

def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "style.css"
    )

    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.warning(f"CSS file not found: {css_path}")

load_css()

# ==========================
# Project Metadata
# ==========================

PROJECT_TITLE = "AI-Powered Cloud Resource Waste Detection & Cost Optimization System"
PROJECT_SUBTITLE = "Enterprise Cloud Analytics & Machine Learning Platform"
UNIVERSITY = "University of the West of Scotland"
SUPERVISOR = "Dr. Rejwan Bin Sulaiman"
TEAM_MEMBERS = [
    "Pravallika Seemala",
    "Prince Hiteshkumar Jaiswal",
    "Luqman Fida",
    "Mann Hiteshkumar Tandel",
]

# ==========================
# Hero Section
# ==========================

with st.container():
    team_badges = "".join(
        f'<span class="team-badge">{member}</span>' for member in TEAM_MEMBERS
    )

    st.markdown(
        f"""
        <div class="hero-section">
            <span class="hero-kicker">MSc Final Year Project</span>
            <h1 class="hero-title">{PROJECT_TITLE}</h1>
            <p class="hero-subtitle">{PROJECT_SUBTITLE}</p>
            <p class="hero-description">
                Monitor cloud infrastructure, detect anomalies with Machine Learning,
                forecast future cloud spend, and act on intelligent optimization
                recommendations — all from a single unified platform.
            </p>
            <div class="hero-meta">
                <div class="hero-meta-item">
                    <span class="hero-meta-label">University</span>
                    <span class="hero-meta-value">{UNIVERSITY}</span>
                </div>
                <div class="hero-meta-divider"></div>
                <div class="hero-meta-item">
                    <span class="hero-meta-label">Supervisor</span>
                    <span class="hero-meta-value">{SUPERVISOR}</span>
                </div>
            </div>
            <div class="hero-team">
                <span class="hero-meta-label">Project Team</span>
                <div class="team-badges">{team_badges}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================
# Quick Navigation - Module Cards
# ==========================

st.markdown('<p class="section-header">Dashboard Modules</p>', unsafe_allow_html=True)
st.markdown('<p class="section-subheader">Navigate to any module from the sidebar</p>', unsafe_allow_html=True)

modules_row_1 = [
    ("bar-chart-2", "Executive Dashboard", "Real-time KPIs, health scores & comprehensive cloud analytics overview"),
    ("cpu", "AI Anomaly Detection", "ML-powered identification of anomalous workloads & resource waste"),
    ("zap", "Recommendation Engine", "Intelligent optimization suggestions & actionable insights"),
]

modules_row_2 = [
    ("trending-up", "Cost Forecasting", "90-day predictive analytics & future cost projections"),
    ("search", "Resource Explorer", "Deep-dive into individual resources & detailed metrics"),
    ("globe", "Global Infrastructure Map", "Geographic visualization of worldwide cloud distribution"),
]

ICONS = {
    "bar-chart-2": "📊",
    "cpu": "🧠",
    "zap": "⚡",
    "trending-up": "📈",
    "search": "🔎",
    "globe": "🌐",
}

def render_module_row(modules):
    cols = st.columns(3, gap="medium")
    for col, (icon_key, title, desc) in zip(cols, modules):
        with col:
            st.markdown(
                f"""
                <div class="module-card">
                    <div class="module-icon-wrap">{ICONS[icon_key]}</div>
                    <p class="module-title">{title}</p>
                    <p class="module-desc">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

render_module_row(modules_row_1)
render_module_row(modules_row_2)

st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

# ==========================
# Project Summary - KPI Cards
# ==========================

st.markdown('<p class="section-header">Platform Overview</p>', unsafe_allow_html=True)

kpi_data = [
    ("layers", "Total Resources", "100"),
    ("database", "Data Records", "18,000"),
    ("cpu", "Active ML Models", "2"),
    ("calendar", "Forecast Horizon", "90 Days"),
]

KPI_ICONS = {
    "layers": "🗂️",
    "database": "🗄️",
    "cpu": "🧠",
    "calendar": "📅",
}

kpi_cols = st.columns(4, gap="medium")

for col, (icon_key, label, value) in zip(kpi_cols, kpi_data):
    with col:
        st.markdown(
            f"""
            <div class="kpi-widget">
                <div class="kpi-icon">{KPI_ICONS[icon_key]}</div>
                <div class="kpi-content">
                    <p class="kpi-label">{label}</p>
                    <p class="kpi-value">{value}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

# ==========================
# About Section
# ==========================

st.markdown(
    """
    <div class="about-card">
        <p class="section-header" style="margin-bottom:0.6rem;">About This Platform</p>
        <p class="about-text">
            <strong>Platform Overview.</strong> This platform uses advanced Machine Learning
            algorithms to identify cloud resource waste patterns, predict future cloud costs
            with high accuracy, and provide intelligent optimization recommendations tailored
            to your infrastructure.
        </p>
        <p class="about-text">
            <strong>Technology Stack.</strong> The solution integrates Data Analytics,
            Artificial Intelligence, and Cloud Computing into a single enterprise-grade
            dashboard, designed for modern DevOps and FinOps teams.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

# Status Footer
st.success("✔ Dashboard Ready — All Systems Operational")