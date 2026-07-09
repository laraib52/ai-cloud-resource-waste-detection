import streamlit as st

from utils.style import load_css

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

load_css()

# ==========================
# Page-level CSS refinements
# (matches styling pattern used across other dashboard pages)
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

    .panel-title{
        font-size: 1rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.7rem;
        display: flex;
        align-items: center;
        gap: 0.45rem;
    }

    .about-label{
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: .05em;
        color: var(--text-color);
        opacity: 0.55;
        font-weight: 600;
        margin-bottom: 0.1rem;
    }

    .about-value{
        font-size: 0.92rem;
        font-weight: 600;
        color: var(--text-color);
        margin-bottom: 0.7rem;
    }

    .chip-row{
        display: flex;
        flex-wrap: wrap;
        gap: 0.45rem;
    }

    .chip{
        font-size: 0.8rem;
        font-weight: 500;
        color: var(--text-color);
        background: var(--background-color);
        border: 1px solid var(--border-soft, rgba(120,130,150,0.18));
        padding: 0.3rem 0.75rem;
        border-radius: 999px;
    }

    /* System Workflow */
    .workflow-row{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.6rem;
        padding: 0.4rem 0;
    }

    .workflow-step{
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--text-color);
        background: var(--secondary-background-color);
        border: 1px solid var(--border-soft, rgba(120,130,150,0.18));
        padding: 0.55rem 1.1rem;
        border-radius: 10px;
        white-space: nowrap;
    }

    .workflow-arrow{
        font-size: 1.1rem;
        color: var(--brand-primary, #2563EB);
        opacity: 0.75;
    }

    /* Dataset Summary mini stats */
    .stat-box{
        text-align: center;
        padding: 0.4rem 0;
    }

    .stat-value{
        font-size: 1.3rem;
        font-weight: 800;
        color: var(--brand-primary, #2563EB);
    }

    .stat-label{
        font-size: 0.78rem;
        color: var(--text-color);
        opacity: 0.6;
        font-weight: 600;
        margin-top: 0.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# Header
# ==========================

with st.container(border=True):
    st.title("📘 About This Platform")
    st.caption("Project information, architecture, and platform overview")

st.divider()

# ==========================
# Project Information + Project Team
# ==========================

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>📘 Project Information</div>", unsafe_allow_html=True)

        st.markdown("<div class='about-label'>Project Name</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='about-value'>AI-Powered Cloud Resource Waste Detection & Cost Optimization System</div>",
            unsafe_allow_html=True
        )

        st.markdown("<div class='about-label'>Version</div>", unsafe_allow_html=True)
        st.markdown("<div class='about-value'>v1.0.0 (MSc Final Year Project Build)</div>", unsafe_allow_html=True)

        st.markdown("<div class='about-label'>University</div>", unsafe_allow_html=True)
        st.markdown("<div class='about-value'>University of the West of Scotland</div>", unsafe_allow_html=True)

        st.markdown("<div class='about-label'>Supervisor</div>", unsafe_allow_html=True)
        st.markdown("<div class='about-value' style='margin-bottom:0;'>Dr. Rejwan Bin Sulaiman</div>", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>👥 Project Team</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="chip-row">
                <span class="chip">Pravallika Seemala</span>
                <span class="chip">Prince Hiteshkumar Jaiswal</span>
                <span class="chip">Luqman Fida</span>
                <span class="chip">Mann Hiteshkumar Tandel</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================
# Technology Stack + AI Models Used
# ==========================

col3, col4 = st.columns(2, gap="medium")

with col3:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>🛠️ Technology Stack</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="chip-row">
                <span class="chip">Python</span>
                <span class="chip">Streamlit</span>
                <span class="chip">Pandas</span>
                <span class="chip">Plotly</span>
                <span class="chip">Scikit-Learn</span>
                <span class="chip">Prophet</span>
                <span class="chip">Jupyter Notebook</span>
            </div>
            """,
            unsafe_allow_html=True
        )

with col4:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>🧠 AI Models Used</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="chip-row">
                <span class="chip">Isolation Forest</span>
                <span class="chip">Prophet</span>
                <span class="chip">Rule-Based Recommendation Engine</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================
# System Workflow
# ==========================

with st.container(border=True):
    st.markdown("<div class='panel-title'>🔄 System Workflow</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="workflow-row">
            <span class="workflow-step">Synthetic Data</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Cleaning</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Feature Engineering</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">AI Models</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Recommendations</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Dashboard</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================
# Dashboard Modules + Dataset Summary
# ==========================

col5, col6 = st.columns(2, gap="medium")

with col5:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>🗂️ Dashboard Modules</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="chip-row">
                <span class="chip">Executive Dashboard</span>
                <span class="chip">AI Anomaly Detection</span>
                <span class="chip">Cost Forecasting</span>
                <span class="chip">Recommendations</span>
                <span class="chip">Resource Explorer</span>
                <span class="chip">Global Map</span>
            </div>
            """,
            unsafe_allow_html=True
        )

with col6:
    with st.container(border=True):
        st.markdown("<div class='panel-title'>📊 Dataset Summary</div>", unsafe_allow_html=True)

        d1, d2, d3, d4 = st.columns(4)

        with d1:
            st.markdown(
                "<div class='stat-box'><div class='stat-value'>Synthetic</div>"
                "<div class='stat-label'>AWS Dataset</div></div>",
                unsafe_allow_html=True
            )
        with d2:
            st.markdown(
                "<div class='stat-box'><div class='stat-value'>100+</div>"
                "<div class='stat-label'>Resources</div></div>",
                unsafe_allow_html=True
            )
        with d3:
            st.markdown(
                "<div class='stat-box'><div class='stat-value'>18,000+</div>"
                "<div class='stat-label'>Records</div></div>",
                unsafe_allow_html=True
            )
        with d4:
            st.markdown(
                "<div class='stat-box'><div class='stat-value'>Multi</div>"
                "<div class='stat-label'>Cloud Regions</div></div>",
                unsafe_allow_html=True
            )

st.divider()

# ==========================
# User Guide
# (new section only — no existing styles/sections modified)
# ==========================

st.markdown(
    """
    <style>
    .guide-text{
        font-size: 0.9rem;
        line-height: 1.65;
        color: var(--text-color);
        opacity: 0.85;
        margin-bottom: 0.5rem;
    }

    .guide-list{
        margin: 0;
        padding-left: 1.1rem;
    }

    .guide-list li{
        font-size: 0.9rem;
        line-height: 1.7;
        color: var(--text-color);
        opacity: 0.85;
        margin-bottom: 0.25rem;
    }

    .step-row{
        display: flex;
        align-items: flex-start;
        gap: 0.7rem;
        margin-bottom: 0.65rem;
    }

    .step-number{
        flex-shrink: 0;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        border: 1px solid var(--border-soft, rgba(120,130,150,0.25));
        color: var(--text-color);
        font-size: 0.72rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 0.1rem;
    }

    .step-text{
        font-size: 0.9rem;
        line-height: 1.6;
        color: var(--text-color);
        opacity: 0.85;
    }

    .guide-table{
        width: 100%;
        border-collapse: collapse;
        font-size: 0.88rem;
    }

    .guide-table th{
        text-align: left;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: .04em;
        color: var(--text-color);
        opacity: 0.55;
        font-weight: 700;
        padding: 0.4rem 0.6rem;
        border-bottom: 1px solid var(--border-soft, rgba(120,130,150,0.2));
    }

    .guide-table td{
        color: var(--text-color);
        opacity: 0.85;
        padding: 0.55rem 0.6rem;
        border-bottom: 1px solid var(--border-softer, rgba(120,130,150,0.12));
        vertical-align: top;
    }

    .guide-table td:first-child{
        font-weight: 600;
        opacity: 1;
        white-space: nowrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='panel-title' style='font-size:1.15rem;'>📖 User Guide</div>", unsafe_allow_html=True)
st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

# ---- What does this dashboard do? ----
with st.container(border=True):
    st.markdown("<div class='panel-title'>What does this dashboard do?</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class="guide-text">
        This dashboard helps you understand how your cloud resources (the online computing
        services a business rents, such as storage or servers) are being used. It highlights
        resources that may be wasting money, predicts what your cloud costs are likely to be
        in the future, and suggests simple actions you can take to reduce unnecessary spending.
        </p>
        """,
        unsafe_allow_html=True
    )

# ---- Who can use this dashboard? ----
with st.container(border=True):
    st.markdown("<div class='panel-title'>Who can use this dashboard?</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="guide-list">
            <li>Students learning about cloud computing and data analytics</li>
            <li>Researchers studying cost optimization or machine learning</li>
            <li>Cloud administrators managing day-to-day resources</li>
            <li>Business managers who want to understand cloud spending</li>
            <li>Anyone curious about how cloud resources and costs work</li>
        </ul>
        <p class="guide-text" style="margin-top:0.6rem; margin-bottom:0;">
        No technical background is required. The dashboard is designed to be understood by
        anyone, regardless of their profession.
        </p>
        """,
        unsafe_allow_html=True
    )

# ---- How to use this dashboard ----
with st.container(border=True):
    st.markdown("<div class='panel-title'>How to use this dashboard</div>", unsafe_allow_html=True)

    steps = [
        "Start with the Executive Dashboard to see an overall summary of your cloud resources and spending.",
        "Open Resource Explorer to look closely at any individual resource.",
        "Visit AI Anomaly Detection to see resources that are behaving unusually and may need attention.",
        "Open Cost Forecasting to view what your cloud costs are expected to look like in the coming months.",
        "Review Recommendations for simple, suggested actions that may help reduce unnecessary spending.",
        "Use the Global Map to see where your cloud resources are located around the world.",
    ]

    for i, step in enumerate(steps, start=1):
        st.markdown(
            f"""
            <div class="step-row">
                <div class="step-number">{i}</div>
                <div class="step-text">{step}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---- Dashboard Features ----
with st.container(border=True):
    st.markdown("<div class='panel-title'>Dashboard Features</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <table class="guide-table">
            <tr>
                <th>Feature</th>
                <th>Purpose</th>
            </tr>
            <tr>
                <td>Executive Dashboard</td>
                <td>Gives a quick, high-level summary of resources, costs, and overall system health.</td>
            </tr>
            <tr>
                <td>Resource Explorer</td>
                <td>Lets you look up and inspect the details of any single resource.</td>
            </tr>
            <tr>
                <td>AI Anomaly Detection</td>
                <td>Highlights resources that are behaving differently than expected, which may indicate waste.</td>
            </tr>
            <tr>
                <td>Cost Forecasting</td>
                <td>Shows an estimate of what your cloud costs are likely to be in the future.</td>
            </tr>
            <tr>
                <td>Recommendations</td>
                <td>Suggests practical actions that may help reduce unnecessary cloud spending.</td>
            </tr>
            <tr>
                <td>Global Map</td>
                <td>Displays where your cloud resources are physically located around the world.</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

# ---- Simple Workflow ----
with st.container(border=True):
    st.markdown("<div class='panel-title'>Simple Workflow</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="workflow-row">
            <span class="workflow-step">Collect Resource Data</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Analyze Resource Usage</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Detect Unusual Patterns</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Predict Future Costs</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Generate Recommendations</span>
            <span class="workflow-arrow">➜</span>
            <span class="workflow-step">Support Better Cost Decisions</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---- Important Note ----
st.markdown(
    """
    <div class="about-card">
        <p class="about-text" style="margin-bottom:0;">
        <strong>Note.</strong> This dashboard is intended for educational and research purposes.
        The recommendations are generated using machine learning models and predefined
        optimization rules to demonstrate how AI can support cloud cost management.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Cloud Waste Optimization Platform • About Module")