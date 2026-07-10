import streamlit as st
import pandas as pd

from utils.style import load_css
from utils.loader import load_data

st.set_page_config(page_title="Resource Explorer", layout="wide")

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

    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        gap: 0.6rem !important;
    }

    [data-testid="stHorizontalBlock"] [data-testid="stVerticalBlockBorderWrapper"]{
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        border-radius: 14px !important;
        transition: box-shadow .2s ease, transform .2s ease, border-color .2s ease;
    }

    [data-testid="stHorizontalBlock"] [data-testid="stVerticalBlockBorderWrapper"]:hover{
        box-shadow: 0 10px 22px rgba(15,23,42,0.10);
        transform: translateY(-2px);
        border-color: var(--brand-primary, #2563EB);
    }

    h1, h2, h3 {
        margin-top: 0rem;
        margin-bottom: 0.3rem;
    }

    .panel-title{
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: var(--text-color);
    }

    .summary-label{
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: .04em;
        color: var(--text-color);
        opacity: 0.55;
        font-weight: 600;
        margin-bottom: 0.1rem;
    }

    .summary-value{
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-color);
        margin-bottom: 0.65rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# Load Data
# ==========================

_, df, _ = load_data()

# ==========================
# Header
# ==========================

with st.container(border=True):
    st.markdown("### 🔍 Resource Explorer")
    st.caption("Inspect Individual Cloud Resource Details")

# ==========================
# Selector + Summary Row
# ==========================

left, right = st.columns([1, 2], gap="medium")

with left:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>Select Resource</div>", unsafe_allow_html=True)
        resource = st.selectbox(
            "Select Resource ID",
            sorted(df["resource_id"].unique()),
            label_visibility="collapsed"
        )

    result = df[df["resource_id"] == resource]

    with st.container(border=True):
        st.markdown("<div class='panel-title'>Resource Summary</div>", unsafe_allow_html=True)
        s1, s2 = st.columns(2, gap="small")
        with s1:
            st.markdown("<div class='summary-label'>Prediction</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='summary-value'>{result['prediction'].iloc[0]}</div>", unsafe_allow_html=True)

            st.markdown("<div class='summary-label'>Environment</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='summary-value'>{result['environment'].iloc[0]}</div>", unsafe_allow_html=True)

            st.markdown("<div class='summary-label'>Region</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='summary-value'>{result['region'].iloc[0]}</div>", unsafe_allow_html=True)
        with s2:
            st.markdown("<div class='summary-label'>Recommendation</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='summary-value'>{result['recommendation'].iloc[0]}</div>", unsafe_allow_html=True)

            st.markdown("<div class='summary-label'>Service</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='summary-value'>{result['service'].iloc[0]}</div>", unsafe_allow_html=True)

with right:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>Resource Details</div>", unsafe_allow_html=True)
        st.dataframe(
            result,
            width="stretch",
            height=280,
            hide_index=True
        )