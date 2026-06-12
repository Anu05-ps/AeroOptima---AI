import streamlit as st

# --------------------------------------------------
# PREMIUM CONSOLE ARCHITECTURE & CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AeroOptima AI | What-If Simulator",
    page_icon="🚀",
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
    .badge-green { background-color: #DEF7EC; color: #03543F; border: 1px solid #BCF7DC; }
    
    /* Native Input & Metric Interception Overrides */
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
    div[data-testid="stMetricDelta"] {
        font-weight: 600 !important;
    }
    
    /* Premium Grid List Custom Layout */
    .telemetry-item {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #334155;
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid rgba(15, 23, 42, 0.04);
    }
    .telemetry-item:last-child { border-bottom: none; }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN LAYOUT HEADERS
# --------------------------------------------------
st.markdown('<h1 class="control-tower-title">What-If Simulator™</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-sub-ticker">PREDICTIVE INTERFACES V3.0 // EXPERIMENTAL RESOURCE WEIGHT BALANCER</p>', unsafe_allow_html=True)

# App Briefing Banner in Premium Silk UI Style
st.markdown("""
    <div class="hud-card" style="margin-bottom: 25px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
            <strong style="color: #0F172A; font-size: 1rem;">Experience Optimization Sandbox</strong>
            <span class="status-badge badge-green">HYPOTHETICAL ENGINE STANDBY</span>
        </div>
        <p style="color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.5;">
            Adjust hypothetical performance parameter inputs below. Real-time optimization algorithms calculate the dynamic shift variables across total passenger satisfaction metrics and potential capital protection reserves.
        </p>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BASELINE STATIC DEFINITIONS
# --------------------------------------------------
BASE_SATISFACTION = 58.4
BASE_REVENUE_RISK = 31.25

# --------------------------------------------------
# INPUT VARIABLES SLIDERS LAYER
# --------------------------------------------------
st.markdown('<p class="module-header">🛠️ Tune Hypothetical Asset Allocation Variables</p>', unsafe_allow_html=True)

sim_col1, sim_col2 = st.columns(2, gap="large")

with sim_col1:
    st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.75rem; color:#2563EB; font-weight:600; margin-bottom:12px;'>[ IN-CABIN SERVICE TUNING PARAMETERS ]</p>", unsafe_allow_html=True)
    wifi = st.slider("📶 Inflight Wifi Improvement Vector", min_value=0, max_value=5, value=0, step=1)
    seat = st.slider("💺 Seat Comfort Ergonomic Allocation", min_value=0, max_value=5, value=0, step=1)

with sim_col2:
    st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.75rem; color:#D97706; font-weight:600; margin-bottom:12px;'>[ TERMINAL & LOGISTICS OPERATION CORES ]</p>", unsafe_allow_html=True)
    boarding = st.slider("🛫 Online Boarding Infrastructure Flow", min_value=0, max_value=5, value=0, step=1)
    delay = st.slider("⏱️ Operational Delay Reduction Programs", min_value=0, max_value=5, value=0, step=1)

# --------------------------------------------------
# IMPACT ALCULATION MATRICES
# --------------------------------------------------
impact_score = (wifi * 2.5) + (boarding * 4.0) + (seat * 3.0) + (delay * 5.0)
predicted_satisfaction = min(BASE_SATISFACTION + impact_score, 100.0)
satisfaction_gain = predicted_satisfaction - BASE_SATISFACTION

revenue_saved = impact_score * 0.75
remaining_risk = max(BASE_REVENUE_RISK - revenue_saved, 0.0)

# --------------------------------------------------
# TELEMETRY YIELD MATRIX CARDS
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">🔮 Projected Satisfaction Metric Array</p>', unsafe_allow_html=True)

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
with kpi_col1:
    st.metric("Baseline Satisfaction Score", f"{BASE_SATISFACTION:.1f}%")
with kpi_col2:
    st.metric("Simulated Satisfaction Score", f"{predicted_satisfaction:.1f}%")
with kpi_col3:
    st.metric("Net Satisfaction Shift", f"+{satisfaction_gain:.1f}%", delta="Positive Shift Variance")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📈 Projected Financial Performance Matrix</p>', unsafe_allow_html=True)

kpi_col4, kpi_col5 = st.columns(2)
with kpi_col4:
    st.metric("Current Unmanaged Value Portfolio", f"${BASE_REVENUE_RISK:.2f}M")
with kpi_col5:
    st.metric("Residual Value Leakage After Actions", f"${remaining_risk:.2f}M", delta=f"-${revenue_saved:.2f}M Volatility Deflection", delta_color="inverse")

# --------------------------------------------------
# CONFIGURATION SUMMARY & RECOMMENDATIONS WORKSPACE
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
workspace_left, workspace_right = st.columns(2, gap="large")

with workspace_left:
    st.markdown('<p class="module-header">📋 Current Telemetry Allocation Summary</p>', unsafe_allow_html=True)
    
    summary_html = f"""
    <div class="hud-card" style="padding: 28px 24px;">
        <div class="telemetry-item"><span>Wifi Configuration Level:</span><b style="color:#2563EB;">+{wifi}</b></div>
        <div class="telemetry-item"><span>Boarding Configuration Level:</span><b style="color:#2563EB;">+{boarding}</b></div>
        <div class="telemetry-item"><span>Seat Ergonomics Level:</span><b style="color:#2563EB;">+{seat}</b></div>
        <div class="telemetry-item"><span>Delay Mitigation Target Force:</span><b style="color:#2563EB;">+{delay}</b></div>
    </div>
    """
    st.markdown(summary_html, unsafe_allow_html=True)

with workspace_right:
    st.markdown('<p class="module-header">🎯 Recommended Strategic Directives</p>', unsafe_allow_html=True)
    
    recommendations = []
    if boarding >= 3:
        recommendations.append("Prioritize digital boarding automation optimization routines.")
    if wifi >= 3:
        recommendations.append("Upgrade physical in-flight wireless connectivity network nodes.")
    if seat >= 3:
        recommendations.append("Improve premium-tier and economy seating design standards.")
    if delay >= 3:
        recommendations.append("Deploy root delay reduction and turnaround enforcement models.")
        
    if not recommendations:
        st.markdown("""
            <div class="hud-card" style="text-align: center; color: #64748B; font-style: italic; font-size:0.9rem;">
                Increase slider level targets to update and output strategic solution vectors.
            </div>
        """, unsafe_allow_html=True)
    else:
        rec_list_html = "".join([f"<li style='margin-bottom:8px;'>{rec}</li>" for rec in recommendations])
        st.markdown(f"""
            <div class="hud-card" style="border-top: 4px solid #2563EB !important; padding: 22px 24px;">
                <ul style="margin: 0; padding-left: 20px; font-size: 0.9rem; color: #1E293B; line-height:1.6; font-weight:500;">
                    {rec_list_html}
                </ul>
            </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# STRATEGIC EXPOSURE INTERVENTION DESK
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📌 Simulation Architecture Forecast Briefing</p>', unsafe_allow_html=True)

st.markdown(f"""
    <div class="hud-alert-card">
        <h4 style="margin-top:0; color:#D97706; font-weight:600; font-size:1.05rem; margin-bottom:12px;">
            Estimated Strategic Impact Summary
        </h4>
        <ul style="color:#92400E; font-size:0.9rem; margin:0; padding-left:20px; line-height:1.7; font-weight: 500;">
            <li>Overall Passenger Satisfaction scores shift from baseline <b>{BASE_SATISFACTION:.1f}%</b> to a projected <b>{predicted_satisfaction:.1f}%</b> ranking footprint.</li>
            <li>Net structural revenue leakage risk maps a downward vector from <b>${BASE_REVENUE_RISK:.2f}M</b> to a safe residual target of <b>${remaining_risk:.2f}M</b>.</li>
            <li>Calculated total preserved revenue value protected via execution pathways: <b>${revenue_saved:.2f}M</b></li>
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
