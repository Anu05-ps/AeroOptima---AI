import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PREMIUM CONSOLE ARCHITECTURE & CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AeroOptima AI | Revenue At Risk",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced Glassmorphic & Dusk Gradient UI Architecture
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* Core Application Framework with Depth Gradient */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background: radial-gradient(circle at top right, #E0E7FF 0%, #F1F5F9 60%, #E2E8F0 100%) !important;
        color: #1E293B !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Elegant Title Architecture */
    .control-tower-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.8rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #0F172A 0%, #2563EB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin-bottom: 2px;
    }
    
    .radar-sub-ticker {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem !important;
        color: #1E293B;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        display: inline-block;
        padding: 6px 14px;
        border-radius: 8px;
        letter-spacing: 0.05em;
        margin-bottom: 30px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
    }
    
    .module-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: #0F172A;
        letter-spacing: -0.01em;
        margin-top: 15px;
        margin-bottom: 22px;
    }

    /* High-End Glassmorphic Silk Containers with Dynamic Hover Effects */
    .hud-card {
        background: rgba(255, 255, 255, 0.65) !important;
        backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(255, 255, 255, 0.7) !important;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.04), 0 1px 3px rgba(15, 23, 42, 0.02);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        margin-bottom: 20px;
    }
    .hud-card:hover {
        transform: translateY(-2px);
        background: rgba(255, 255, 255, 0.8) !important;
        box-shadow: 0 20px 40px -15px rgba(37, 99, 235, 0.08), 0 1px 4px rgba(15, 23, 42, 0.02);
        border-color: rgba(37, 99, 235, 0.2) !important;
    }
    
    .hud-alert-card {
        background: rgba(254, 243, 199, 0.4) !important;
        backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(251, 191, 36, 0.4) !important;
        border-radius: 16px;
        padding: 24px;
        border-left: 5px solid #D97706 !important;
        box-shadow: 0 10px 30px -10px rgba(217, 119, 6, 0.05);
        margin-bottom: 20px;
    }

    /* Status Micro-Indicators */
    .status-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    .badge-red { background-color: #FCE8E6; color: #A61C1C; border: 1px solid #FAD2CF; }
    
    /* Native Metric Overrides */
    div[data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 600 !important;
        color: #0F172A !important;
        font-size: 2.1rem !important;
        letter-spacing: -0.03em;
    }
    div[data-testid="stMetricLabel"] {
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        color: #475569 !important;
    }
    
    /* Premium Table Styling */
    .premium-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem;
    }
    .premium-table tr { border-bottom: 1px solid rgba(15, 23, 42, 0.05); }
    .premium-table tr:last-child { border-bottom: none; }
    .premium-table th { padding: 12px 8px; text-align: left; color: #475569; font-weight: 600; background: rgba(15,23,42,0.02); }
    .premium-table td { padding: 14px 8px; }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN LAYOUT HEADERS
# --------------------------------------------------
st.markdown('<h1 class="control-tower-title">Revenue At Risk Engine™</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-sub-ticker">FINANCIAL FORECAST NODE V3.0 // EXPOSURE REVENUE RISK TRACING</p>', unsafe_allow_html=True)

# App Briefing Banner in Premium Silk UI Style
st.markdown("""
    <div class="hud-card" style="margin-bottom: 25px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
            <strong style="color: #0F172A; font-size: 1rem;">Financial Portfolio Integrity Scan</strong>
            <span class="status-badge badge-red">LEAKAGE PROFILE DETECTED</span>
        </div>
        <p style="color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.5;">
            Isolate and trace financial exposure trends across cabin tier configurations and specific churn vectors. Proactively map structural capital deficiencies triggered directly by negative passenger experience parameters.
        </p>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# EXECUTIVE FINANCING KPI CARDS LAYER
# --------------------------------------------------
TOTAL_REVENUE_AT_RISK = 31250630
HIGHEST_RISK_PERSONA = "Frustrated Short-Haul Traveler"
HIGHEST_RISK_CLASS = "Business"
BUSINESS_REVENUE_RISK = 23198920

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Net Revenue At Risk", "$31.25M")
with col2:
    st.metric("📊 Max Exposure Index", "48K")
    st.caption(f"Cohort Vector: {HIGHEST_RISK_PERSONA}")
with col3:
    st.metric("🛫 Highest Risk Class", HIGHEST_RISK_CLASS)
with col4:
    st.metric("💎 Premium Capital Risk", f"${BUSINESS_REVENUE_RISK/1000000:.2f}M")

st.markdown("<br>", unsafe_allow_html=True)

# Global UI configuration properties for Plotly charts matching layout aesthetics
plotly_layout_args = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_family="Inter",
    font_color="#1E293B",
    title_font=dict(
        size=15,
        color="#0F172A"
    )
)

# --------------------------------------------------
# VISUAL RISK INTERFACES (Two Column Workspace)
# --------------------------------------------------
workspace_left, workspace_right = st.columns(2, gap="large")

with workspace_left:
    st.markdown('<p class="module-header">📈 Volatility Burden by Segment Profile</p>', unsafe_allow_html=True)
    persona_risk = pd.DataFrame({
        "Persona": [
            "Frustrated Short-Haul Traveler",
            "Premium Long-Haul Traveler",
            "Express Comfort Traveler",
            "At-Risk Long-Haul Traveler"
        ],
        "Revenue_At_Risk": [9920616, 7475620, 7040665, 6813730]
    })
    
    fig_bar = px.bar(
        persona_risk,
        x="Revenue_At_Risk",
        y="Persona",
        orientation="h",
        color="Revenue_At_Risk",
        title="Revenue At Risk Scale Matrix ($)",
        color_continuous_scale=["#C7D2FE", "#3B82F6", "#1E3A8A"] # Custom Premium Corporate Indigo Scale
    )
    fig_bar.update_layout(**plotly_layout_args, coloraxis_showscale=False)
    fig_bar.update_xaxes(showgrid=True, gridcolor="rgba(15, 23, 42, 0.05)", title_text="Exposed Value Portfolio")
    fig_bar.update_yaxes(showgrid=False, title=None)
    st.plotly_chart(fig_bar, use_container_width=True)

with workspace_right:
    st.markdown('<p class="module-header">🍩 Cabin Tier Exposure Proportions</p>', unsafe_allow_html=True)
    class_risk = pd.DataFrame({
        "Class": ["Business", "Eco", "Eco Plus"],
        "Revenue_At_Risk": [23198920, 6081578, 1970133]
    })
    
    fig_pie = px.pie(
        class_risk,
        names="Class",
        values="Revenue_At_Risk",
        hole=0.55,
        title="Revenue Leakage Ratios by Fare Classification",
        color_discrete_sequence=["#1E3A8A", "#2563EB", "#60A5FA"] # High-Contrast Luxury Blues
    )
    fig_pie.update_layout(**plotly_layout_args)
    fig_pie.update_traces(textposition='outside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

# --------------------------------------------------
# REVENUE RISK BREAKDOWN MATRIX TABLE
# --------------------------------------------------


st.markdown(
    '<p class="module-header">📡 Parametric Revenue Risk Breakdown</p>',
    unsafe_allow_html=True
)

risk_table = persona_risk.copy()

risk_table.columns = [
    "Target Strategic Behavioral Persona",
    "Calculated Capital Exposure ($)",
]

risk_table["Mitigation Feasibility Vector"] = "ACTIVE TARGET LAYER"

st.dataframe(
    risk_table,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# STRATEGIC INTERVENTION ACTION CENTRE
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📌 Executive Financial Insights Desk</p>', unsafe_allow_html=True)

info_col1, info_col2 = st.columns(2, gap="medium")

with info_col1:
    st.markdown("""
        <div class="hud-alert-card" style="height: 100%;">
            <h4 style="margin-top:0; color:#D97706; font-weight:600; font-size:1.05rem; margin-bottom:8px;">
                ⚠️ Critical Portfolio Risk Notification
            </h4>
            <p style="color:#92400E; font-size:0.9rem; margin:0; line-height:1.6; font-weight: 500;">
                <b>Business Class configurations</b> account for over <b>74%</b> of overall system revenue leakage risk metrics.<br><br>
                Executing targeted optimizations across cabin Wi-Fi connectivity arrays, ergonomic configuration enhancements, and gate queue handling mechanisms generates immediate high-yield capital preservation variables.
            </p>
        </div>
    """, unsafe_allow_html=True)

with info_col2:
    st.markdown("""
        <div class="hud-card" style="height: 100%; border-top: 4px solid #2563EB !important;">
            <h4 style="margin-top:0; color:#0F172A; font-weight:600; font-size:1.05rem; margin-bottom:12px;">
                Strategic ROI Yield Parameters
            </h4>
            <ul style="color:#475569; font-size:0.85rem; margin:0; padding-left:18px; line-height:1.7;">
                <li>Net Financial Risk Exposure exceeds a critical baseline threshold of <b>$31M+</b>.</li>
                <li>Frustrated Short-Haul clusters maintain maximum volumetric capital vulnerability counts.</li>
                <li>Prioritizing resolution paths for premium traveler profiles generates high return-on-investment parameters.</li>
                <li>System-wide client friction suppression directly compresses margins lost to passive churn.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# SYSTEM CONSOLE FOOTER TERMINAL
# --------------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(15, 23, 42, 0.08);'/>", unsafe_allow_html=True)
f_col1, f_col2 = st.columns(2)
with f_col1:
    st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.7rem; color:#94A3B8;'>AEROOPTIMA OPERATIONAL INTERFACE PLATFORM v3.0 // SECURITY LOG LINK ENCRYPTED</p>", unsafe_allow_html=True)

# --------------------------------------------------
# VISUAL RISK INTERFACES (Two Column Workspace)
# --------------------------------------------------
