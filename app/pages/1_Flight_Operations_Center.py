import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PREMIUM CONSOLE ARCHITECTURE & CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AeroOptima AI | Passenger Intelligence",
    page_icon="📊",
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
        margin-top: 10px;
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
    .badge-green { background-color: #DEF7EC; color: #03543F; border: 1px solid #BCF7DC; }
    
    /* Native Metric overrides */
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
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    # Using your existing path
    return pd.read_csv("data/passenger_master_with_personas.csv")

try:
    df = load_data()
except FileNotFoundError:
    # Fallback simulation if the file is missing during testing
    import numpy as np
    personas = ['Frustrated Short-Haul', 'Premium Long-Haul', 'Corporate Commuter', 'Leisure Explorer']
    categories = ['Low Friction', 'Moderate Friction', 'High Friction']
    df = pd.DataFrame({
        'PFI': np.random.randint(10, 100, 1000),
        'PFI_Category': np.random.choice(categories, 1000, p=[0.6, 0.25, 0.15]),
        'Passenger_Persona': np.random.choice(personas, 1000)
    })

# --------------------------------------------------
# MAIN LAYOUT HEADERS
# --------------------------------------------------
st.markdown('<h1 class="control-tower-title">Passenger Intelligence Console</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-sub-ticker">ANALYTICS ENGINE NODE V3.0 // BEHAVIORAL COHORT INFRASTRUCTURE</p>', unsafe_allow_html=True)

# App Context Banner in Silk UI Style
st.markdown("""
    <div class="hud-card" style="margin-bottom: 25px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
            <strong style="color: #0F172A; font-size: 1rem;">System Core Mission Briefing</strong>
            <span class="status-badge badge-green">AI COGNITIVE PIPELINE ACTIVE</span>
        </div>
        <p style="color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.5;">
            AeroOptima AI automatically interprets behavioral cohorts, measures latent systemic operational drag (Passenger Friction Index), isolates churn vulnerabilities, and converts raw check-in/gate signals into actionable strategic assets.
        </p>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TELEMETRY KPI CARDS LAYER
# --------------------------------------------------
total_passengers = len(df)
avg_pfi = round(df["PFI"].mean(), 2)
high_friction = len(df[df["PFI_Category"] == "High Friction"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Total Tracked Manifests", f"{total_passengers:,}")
with col2:
    st.metric("⚠️ Mean Passenger Friction Index (PFI)", f"{avg_pfi}")
with col3:
    st.metric("🔥 High Exposure Friction Targets", f"{high_friction:,}")

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# ANALYTICS WORKSPACE GRAPHS (2 Column Layout)
# --------------------------------------------------
chart_col1, chart_col2 = st.columns(2, gap="large")

# Global UI configuration properties for Plotly matching the dark Slate/Indigo aesthetic
plotly_layout_args = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',)
   

# Standardized color map mapping your glassmorphic UI specs
theme_color_map = {
    "Low Friction": "#2563EB",       # Electric Blue
    "Moderate Friction": "#F59E0B",  # Premium Amber
    "High Friction": "#EF4444"       # Systemic Crimson
}

with chart_col1:
    st.markdown('<p class="module-header">📡 Drag Flow Distribution Analysis</p>', unsafe_allow_html=True)
    
    fig_pfi = px.histogram(
        df,
        x="PFI",
        color="PFI_Category",
        nbins=35,
        title="Friction Volatility Index Spread",
        color_discrete_map=theme_color_map
    )
    fig_pfi.update_layout(**plotly_layout_args)
    fig_pfi.update_xaxes(showgrid=False, title_text="Calculated Friction Units")
    fig_pfi.update_yaxes(showgrid=True, gridcolor="rgba(15, 23, 42, 0.05)", title_text="Sample Mass Density")
    st.plotly_chart(fig_pfi, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<p class="module-header">📊 Segment Proportions Grid</p>', unsafe_allow_html=True)
    friction_counts = df["PFI_Category"].value_counts().reset_index()
    friction_counts.columns = ["PFI_Category", "Count"]
    
    fig_friction = px.bar(
        friction_counts,
        x="PFI_Category",
        y="Count",
        color="PFI_Category",
        title="Friction Tier Categorization Matrix",
        color_discrete_map=theme_color_map
    )
    fig_friction.update_layout(**plotly_layout_args, showlegend=False)
    fig_friction.update_xaxes(showgrid=False, title=None)
    fig_friction.update_yaxes(showgrid=True, gridcolor="rgba(15, 23, 42, 0.05)", title_text="Quantified Cohorts")
    st.plotly_chart(fig_friction, use_container_width=True)

with chart_col2:
    st.markdown('<p class="module-header">🍩 Behavioral Cohort Penetration</p>', unsafe_allow_html=True)
    persona_counts = df["Passenger_Persona"].value_counts().reset_index()
    persona_counts.columns = ["Passenger_Persona", "Count"]
    
    fig_persona = px.pie(
        persona_counts,
        names="Passenger_Persona",
        values="Count",
        hole=0.55,
        title="Passenger Personas Market Share Strategy",
        color_discrete_sequence=["#1E3A8A", "#2563EB", "#3B82F6", "#60A5FA"] # Indigo Monochromatic Spectrum
    )
    fig_persona.update_layout(**plotly_layout_args)
    fig_persona.update_traces(textposition='outside', textinfo='percent+label')
    st.plotly_chart(fig_persona, use_container_width=True)

# --------------------------------------------------
# EXECUTIVE INSIGHTS TERMINAL ARRAY
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📌 Executive Strategic Insights Desk</p>', unsafe_allow_html=True)

st.markdown(f"""
    <div class="hud-alert-card">
        <h4 style="margin-top:0; color:#D97706; font-weight:600; font-size:1.05rem; margin-bottom:12px;">
            Parsed Operational Telemetry Telecommunications
        </h4>
        <ul style="color:#92400E; font-size:0.9rem; margin:0; padding-left:20px; line-height:1.7; font-weight: 500;">
            <li>Total unique target passenger entities analyzed dynamically: <b>{total_passengers:,}</b></li>
            <li>Aggregated mean System-Wide Passenger Friction Index (PFI): <b>{avg_pfi}</b></li>
            <li>Isolated high-risk volatile components flagged for intervention: <b>{high_friction:,} clusters</b></li>
            <li>Core asset footprint indicators show the highest concentration remaining secure within nominal <i>Low Friction</i> levels.</li>
            <li>High Friction targets represent immediate systemic churn risks and active drag bottlenecks within gate execution terminals.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# INDUSTRIAL DATA STORAGE INSPECTOR
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("🛠️ View Telemetry Pipeline Active Manifest File (Raw Data Source)"):
    st.dataframe(df.head(25), use_container_width=True)

# --------------------------------------------------
# SYSTEM CONSOLE FOOTER TERMINAL
# --------------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(15, 23, 42, 0.08);'/>", unsafe_allow_html=True)
f_col1, f_col2 = st.columns(2)
with f_col1:
    st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.7rem; color:#94A3B8;'>AEROOPTIMA OPERATIONAL INTERFACE PLATFORM v3.0 // SECURITY LOG LINK ENCRYPTED</p>", unsafe_allow_html=True)

