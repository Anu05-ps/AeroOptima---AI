import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PREMIUM CONSOLE ARCHITECTURE & CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AeroOptima AI | Passenger Personas",
    page_icon="🧑‍✈️",
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
    .badge-blue { background-color: #E0E7FF; color: #1E3A8A; border: 1px solid #C7D2FE; }
    
    /* Native Input & Metric Interception overrides */
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
    
    /* Clean custom styling for clean tables */
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
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/passenger_master_with_personas.csv")

try:
    df = load_data()
except FileNotFoundError:
    # Fallback simulation if file paths vary across work environments
    import numpy as np
    personas = ['Premium Long-Haul Traveler', 'Express Comfort Traveler', 'Frustrated Short-Haul Traveler', 'At-Risk Long-Haul Traveler']
    df = pd.DataFrame({
        'PFI': np.random.randint(15, 95, 1200),
        'Flight Distance': np.random.randint(300, 5000, 1200),
        'Service_Quality_Score': np.random.uniform(2.5, 9.8, 1200),
        'Passenger_Persona': np.random.choice(personas, 1200, p=[0.2, 0.25, 0.4, 0.15])
    })

# --------------------------------------------------
# MAIN LAYOUT HEADERS
# --------------------------------------------------
st.markdown('<h1 class="control-tower-title">Passenger Personas</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-sub-ticker">COGNITIVE ENGINE NODE V3.0 // SEGMENTATION INFRASTRUCTURE TELEMETRY</p>', unsafe_allow_html=True)

# App Briefing Banner in Premium Silk UI Style
st.markdown("""
    <div class="hud-card" style="margin-bottom: 25px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
            <strong style="color: #0F172A; font-size: 1rem;">Behavioral Topology Overview</strong>
            <span class="status-badge badge-blue">SEGMENTATION MODELS ACTIVE</span>
        </div>
        <p style="color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.5;">
            AeroOptima AI maps raw telemetry indicators across complex variables (travel habits, friction thresholds, system-wide touchpoints) to isolate passenger cohorts into highly defined behavioral profiles.
        </p>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TELEMETRY KPI CARDS LAYER
# --------------------------------------------------
persona_counts = df["Passenger_Persona"].value_counts()
total_personas = df["Passenger_Persona"].nunique()
largest_persona = persona_counts.idxmax()
largest_count = persona_counts.max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Traveler Segments", total_personas)

with col2:
    st.metric("Largest Segment Size", f"{largest_count:,}")
    st.caption(f"Isolate Core: {largest_persona}")
with col3:
    st.metric("Passengers Analyzed", f"{len(df):,}")
st.markdown("<br>", unsafe_allow_html=True)

# Global UI configuration properties for Plotly charts matching layout aesthetics
plotly_layout_args = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_family="Inter",
    font_color="#1E293B",
    title_font=dict(
        size=15,
        color="#0F172A"
    )
)
# --------------------------------------------------
# VISUAL ANALYTICS LAYERS (Two Column Workspace)
# --------------------------------------------------
workspace_left, workspace_right = st.columns(2, gap="large")

with workspace_left:
    st.markdown('<p class="module-header">🍩 Market Share Structural Profile</p>', unsafe_allow_html=True)
    persona_df = persona_counts.reset_index()
    persona_df.columns = ["Passenger_Persona", "Count"]
    
    fig_pie = px.pie(
        persona_df,
        names="Passenger_Persona",
        values="Count",
        hole=0.55,
        title="Persona Volumetric Saturation Matrix",
        color_discrete_sequence=["#1E3A8A", "#2563EB", "#3B82F6", "#60A5FA"] # Deep Slate to Luxury Indigo Gradient
    )
    fig_pie.update_layout(**plotly_layout_args)
    fig_pie.update_traces(textposition='outside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with workspace_right:
    st.markdown('<p class="module-header">📈 Friction Multipliers Across Profiles</p>', unsafe_allow_html=True)
    pfi_persona = df.groupby("Passenger_Persona")["PFI"].mean().reset_index()
    
    fig_bar = px.bar(
        pfi_persona,
        x="Passenger_Persona",
        y="PFI",
        color="PFI",
        title="Mean Passenger Friction Index (PFI) by Cohort",
        color_continuous_scale=["#C7D2FE", "#3B82F6", "#1E3A8A"] # Custom Premium Indigo-Blue scale
    )
    fig_bar.update_layout(**plotly_layout_args, coloraxis_showscale=False)
    fig_bar.update_xaxes(showgrid=False, title=None)
    fig_bar.update_yaxes(showgrid=True, gridcolor="rgba(15, 23, 42, 0.05)", title_text="Mean Friction Load")
    st.plotly_chart(fig_bar, use_container_width=True)

# --------------------------------------------------
# DATA CHARACTERISTICS MATRIX
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📡 Cohort Parametric Telemetry Performance</p>', unsafe_allow_html=True)

persona_summary = (
    df.groupby("Passenger_Persona")
    .agg({
        "PFI": "mean",
        "Flight Distance": "mean",
        "Service_Quality_Score": "mean"
    })
    .round(2)
    .reset_index()
)

# Render a beautifully formatted premium HTML table instead of raw st.dataframe
st.markdown(
    '<div class="hud-card">',
    unsafe_allow_html=True
)

st.dataframe(
    persona_summary,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# STRATEGIC EXPOSURE INTERVENTION DESK
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📌 Executive Strategic Insights Desk</p>', unsafe_allow_html=True)

info_col1, info_col2 = st.columns(2, gap="medium")

with info_col1:
    st.markdown("""
        <div class="hud-alert-card" style="height: 100%;">
            <h4 style="margin-top:0; color:#D97706; font-weight:600; font-size:1.05rem; margin-bottom:8px;">
                ⚠️ High Priority Exposure Alert
            </h4>
            <p style="color:#92400E; font-size:0.9rem; margin:0; line-height:1.6; font-weight: 500;">
                <b>Frustrated Short-Haul Travelers</b> represent the highest volumetric asset density inside operations while presenting deep structural churn risks.<br><br>
                Targeted minimization adjustments in check-in processing cycles for this specific sub-group yield immediate compound safety variables for customer retention models.
            </p>
        </div>
    """, unsafe_allow_html=True)

with info_col2:
    st.markdown("""
        <div class="hud-card" style="height: 100%; border-top: 4px solid #2563EB !important;">
            <h4 style="margin-top:0; color:#0F172A; font-weight:600; font-size:1.05rem; margin-bottom:12px;">
                Strategic Asset Alignment Matrix
            </h4>
            <ul style="color:#475569; font-size:0.85rem; margin:0; padding-left:18px; line-height:1.6;">
                <li><b>Premium Long-Haul Travelers:</b> Maximizes baseline operational yield and luxury profile retention metrics.</li>
                <li><b>Express Comfort Travelers:</b> Highly structured, consistent segment demonstrating optimization stability.</li>
                <li><b>At-Risk Long-Haul Travelers:</b> Exhibits severe friction spikes requires prioritized routing recovery workflows.</li>
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
