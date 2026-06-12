import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# SESSION STATE ARCHITECTURE (CROSS-CONSOLE MEMORY)
# --------------------------------------------------
if 'boarding_efficiency' not in st.session_state:
    st.session_state.boarding_efficiency = 75
if 'delay_mitigation' not in st.session_state:
    st.session_state.delay_mitigation = 60
if 'wifi_reliability' not in st.session_state:
    st.session_state.wifi_reliability = 85
if 'seat_upgrade_factor' not in st.session_state:
    st.session_state.seat_upgrade_factor = 6

# Dynamic Calculation Matrix
simulated_csat_delta = (st.session_state.boarding_efficiency * 0.12) + (st.session_state.delay_mitigation * 0.18)
base_csat = 52400
dynamic_csat_score = min(100.0, 64.5 + simulated_csat_delta)
dynamic_csat_volume = int(base_csat * (1 + (simulated_csat_delta / 100)))

revenue_saved_value = (st.session_state.boarding_efficiency * 0.14) + (st.session_state.wifi_reliability * 0.11) + (st.session_state.seat_upgrade_factor * 0.4)
dynamic_risk_managed = f"${31.25 + revenue_saved_value:.2f}M"

# --------------------------------------------------
# PREMIUM CONSOLE ARCHITECTURE & CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AeroOptima AI | Mission Control",
    page_icon="✈️",
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
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        color: #0F172A;
        letter-spacing: -0.01em;
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
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }
    .hud-alert-card:hover {
        background: rgba(254, 243, 199, 0.55) !important;
        box-shadow: 0 15px 35px -10px rgba(217, 119, 6, 0.08);
    }

    /* Refined Progress Micro-Animations */
    .progress-track {
        background-color: rgba(15, 23, 42, 0.06);
        border-radius: 10px;
        width: 100%;
        margin-top: 8px;
        margin-bottom: 12px;
    }
    .progress-fill-orange { background: #D97706; height: 6px; border-radius: 10px; }
    .progress-fill-blue { background: linear-gradient(90deg, #2563EB, #3B82F6); height: 6px; border-radius: 10px; }

    /* Polished Status Micro-Indicators */
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
    .badge-orange { background-color: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }
    
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
    div[data-testid="stMetricDelta"] {
        font-weight: 500 !important;
    }
    
    /* Clean custom styling for clean tables */
    .premium-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem;
    }
    .premium-table tr { border-bottom: 1px solid rgba(15, 23, 42, 0.05); }
    .premium-table tr:last-child { border-bottom: none; }
    .premium-table td { padding: 14px 0; }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN LAYOUT HEADERS
# --------------------------------------------------
st.markdown('<h1 class="control-tower-title">AeroOptima Platform</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-sub-ticker">SYSTEM ENGINE NODE V3.0 // LUXURY GATE INFRASTRUCTURE TELEMETRY</p>', unsafe_allow_html=True)

left_workspace, right_control_deck = st.columns([3, 1], gap="large")

# --- RIGHT HAND SIDE: EXECUTIVE CONTROL PANEL ---
with right_control_deck:
    st.markdown("<div style='padding-bottom: 12px; display: flex; justify-content: space-between; align-items: center;'><h3 style='color: #0F172A; font-weight:600; font-size:0.95rem; margin:0; letter-spacing:-0.01em;'>CONSOLE LAYER</h3><span class='status-badge badge-green'>SYS OPERATIONAL</span></div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        selected_module = st.radio(
            "Select Node Console",
            [
                "📊 Executive Dashboard",
                "🛫 Flight Operations Center",
                "🧑‍✈️ Traveler Intelligence Hub",
                "💰 Revenue Control Tower",
                "🎙️ Passenger Experience Center",
                "🚀 Experience Simulator"
            ],
            label_visibility="collapsed"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.7rem; color:#64748B; font-weight:600; margin-bottom:8px;'>NETWORK TELEMETRY Matrix</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: #03543F; font-size:0.85rem; font-weight:500; margin: 0 0 4px 0; display:flex; align-items:center;'>● FEED VERIFIED SECURE</p>", unsafe_allow_html=True)
        st.caption("Active Pipeline Streams: 1,400+\n\nLive Pipeline Latency: 12ms")


# --- LEFT HAND SIDE: ACTIVE MODULE WORKSPACE ---
with left_workspace:
    
    # NODE 1: EXECUTIVE DASHBOARD
    if selected_module == "📊 Executive Dashboard":
        st.markdown('<p class="module-header">Global Network Overview Portfolio</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Aggregated Passenger Journeys", value="129,880", delta="+12.4% vs LY")
        with col2:
            st.metric(label="Predictive System Core Optimization", value=f"{dynamic_csat_score:.2f}%", delta="Live Simulator Variant")
        with col3:
            st.metric(label="Risk Loss Mitigation Capacity", value=dynamic_risk_managed, delta="Optimized Allocation", delta_color="inverse")
        with col4:
            st.metric(label="Global CSAT Metric Base", value=f"{dynamic_csat_volume:,}", delta="+4.2% MoM")
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Interactive Graphical Area Inside Enhanced UI Frame
        st.markdown('<p style="font-size:0.95rem; font-weight:600; color:#0F172A; margin-bottom:12px;">📡 24-Hour Pipeline Telemetry Flow Density</p>', unsafe_allow_html=True)
        chart_data = pd.DataFrame(
            np.random.randn(24, 2) / [11, 6] + [14.8, 11.9],
            columns=['Terminal Check-In Streams', 'Gate Deployment Loops']
        )
        st.area_chart(chart_data, height=230, use_container_width=True)

    # NODE 2: FLIGHT OPERATIONS CENTER
    elif selected_module == "🛫 Flight Operations Center":
        st.markdown('<p class="module-header">Terminal Pipeline Interface Layers</p>', unsafe_allow_html=True)
        
        flow_cols = st.columns(5)
        stages = [
            {"icon": "🛒", "name": "1. Booking & Offer", "stat": "0.4s Base Load"},
            {"icon": "📱", "name": "2. Terminal Check-In", "stat": "4.2m Queue Baseline"},
            {"icon": "🛫", "name": "3. Gate Logistics", "stat": "-12m Clean Turn"},
            {"icon": "✈️", "name": "4. Cabin Environment", "stat": f"{st.session_state.wifi_reliability}% Air Connected"},
            {"icon": "🛄", "name": "5. Baggage Return", "stat": "99.2% Sync Lock"}
        ]
        
        for i, col in enumerate(flow_cols):
            with col:
                st.markdown(f"""
                    <div class="hud-card" style="padding: 24px 14px; border-top: 4px solid #2563EB !important; text-align: center; margin-bottom:10px;">
                        <div style="font-size: 1.6rem; margin-bottom:8px;">{stages[i]['icon']}</div>
                        <div style="font-weight: 600; font-size:0.85rem; color:#0F172A; margin-bottom:4px;">{stages[i]['name']}</div>
                        <div style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#2563EB; font-weight:500;">{stages[i]['stat']}</div>
                    </div>
                """, unsafe_allow_html=True)

    # NODE 3: TRAVELER INTELLIGENCE HUB
    elif selected_module == "🧑‍✈️ Traveler Intelligence Hub":
        st.markdown('<p class="module-header">Traveler Segment Cohort Analytics</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:#475569; font-size:0.9rem; margin-bottom:24px;">Clustering engines parsing operational trends to isolate critical churn vulnerabilities:</p>', unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="hud-card">', unsafe_allow_html=True)
            st.markdown(
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:18px;">'
                '<h3 style="margin:0; color:#0F172A; font-size:1.05rem; font-weight:600;">AI-Driven Segment Classifications</h3>'
                '<span class="status-badge badge-green">4 Clusters Synchronized</span>'
                '</div>',
                unsafe_allow_html=True
            )
            alert_col, protection_col = st.columns(2)
            with alert_col:
                st.markdown("**⚠️ Churn Alert: Frustrated Short-Haul Cohorts**  \n*High Attrition Vector*")
                st.progress(st.session_state.boarding_efficiency / 100)
            with protection_col:
                st.markdown("**⭐ Asset Protection: Premium Long-Haul Cohorts**  \n*Max Yield Target*")
                st.progress(0.92)
            st.markdown('</div>', unsafe_allow_html=True)

    # NODE 4: REVENUE CONTROL TOWER
    elif selected_module == "💰 Revenue Control Tower":
        st.markdown('<p class="module-header">Revenue Optimization Intelligence Matrix</p>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="hud-card">
                <p style="color:#475569; font-size:0.9rem; margin-bottom:15px;">Dynamic margin protection loops calculated against system delays across current active manifests:</p>
                <div style="margin-bottom:5px;">
                    <div style="display:flex; justify-content:space-between; font-size:0.85rem;">
                        <span style="color:#2563EB; font-weight:600;">Target Protected Revenue Portfolio (Friction Reduction)</span>
                        <span style="color:#2563EB; font-family:'JetBrains Mono'; font-weight:600;">Optimal Feasibility Range</span>
                    </div>
                    <div class="progress-track"><div class="progress-fill-blue" style="width: 85%;"></div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p style="font-size:0.95rem; font-weight:600; color:#0F172A; margin-bottom:12px;">📈 Volatility Asset Drift Analysis (By Terminal Node Sector)</p>', unsafe_allow_html=True)
        revenue_data = pd.DataFrame(np.random.randint(12, 48, size=(15, 3)), columns=['APAC Corridors', 'EMEA Operations', 'AMER Sectors'])
        st.line_chart(revenue_data, height=190, use_container_width=True)

    # NODE 5: PASSENGER EXPERIENCE CENTER
    elif selected_module == "🎙️ Passenger Experience Center":
        st.markdown('<p class="module-header">Voice of Passenger (VoP) Priority Array Matrix</p>', unsafe_allow_html=True)
        
        matrix_col1, matrix_col2 = st.columns(2)
        with matrix_col1:
            st.markdown("""
                <div class="hud-card" style="border-top: 4px solid #2563EB !important; height: 100%;">
                    <h4 style="margin-top:0; color:#0F172A; font-weight:600; font-size:1rem;">🗣️ High Volume NLP Mentions</h4>
                    <p style="color:#64748B; font-size:0.8rem; margin-top:-6px;">Clustered semantic text trend volumes</p>
                    <table class="premium-table">
                        <tr><td style="color:#334155; font-weight:500;">1. In-Flight Catering Logistics Flow</td><td style="text-align:right; color:#64748B; font-family:'JetBrains Mono';">42k index</td></tr>
                        <tr><td style="color:#334155; font-weight:500;">2. Seat Cushion Space Optimization</td><td style="text-align:right; color:#64748B; font-family:'JetBrains Mono';">38k index</td></tr>
                        <tr><td style="color:#334155; font-weight:500;">3. Network Flight Schedule Variance</td><td style="text-align:right; color:#64748B; font-family:'JetBrains Mono';">31k index</td></tr>
                    </table>
                </div>
            """, unsafe_allow_html=True)
                
        with matrix_col2:
            st.markdown("""
                <div class="hud-alert-card" style="height: 100%;">
                    <h4 style="margin-top:0; color:#92400E; font-weight:600; font-size:1rem;">📉 High Impact Churn Drivers</h4>
                    <p style="color:#92400E; font-size:0.8rem; margin-top:-6px;">Negative correlation weights relative to CSAT scores</p>
                    <table class="premium-table">
                        <tr><td style="color:#334155; font-weight:500;">1. Terminal Baggage Mishandling Claims</td><td style="text-align:right; color:#92400E; font-weight:600; font-size:0.8rem;">CRITICAL MATCH</td></tr>
                        <tr><td style="color:#334155; font-weight:500;">2. Unmitigated Terminal Gate Delays</td><td style="text-align:right; color:#92400E; font-weight:600; font-size:0.8rem;">HIGH EXPOSURE</td></tr>
                        <tr><td style="color:#334155; font-weight:500;">3. In-Seat Wi-Fi Hardware Failures</td><td style="text-align:right; color:#92400E; font-weight:600; font-size:0.8rem;">SYSTEMIC FAULT</td></tr>
                    </table>
                </div>
            """, unsafe_allow_html=True)

    # NODE 6: EXPERIENCE SIMULATOR
    elif selected_module == "🚀 Experience Simulator":
        st.markdown('<p class="module-header">Real-Time Experience Tuning Deck Sandbox</p>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="hud-card" style="margin-bottom:24px;">
                <p style="margin:0; color:#475569; font-size:0.9rem; line-height:1.5;">
                    Predictive simulation sandbox allowing airport team leads to redistribute resource weights. 
                    Adjust variables below; changes dynamically recalculate system indicators across all active workspace terminals.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        sim_col1, sim_col2 = st.columns(2)
        with sim_col1:
            st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.75rem; color:#2563EB; font-weight:600; margin-bottom:12px;'>[ GROUND APPRON DISPATCH VARIABLES ]</p>", unsafe_allow_html=True)
            st.session_state.boarding_efficiency = st.slider("Boarding Optimization Factor (%)", 0, 100, st.session_state.boarding_efficiency)
            st.session_state.delay_mitigation = st.slider("Proactive Delay Management Rigor (%)", 0, 100, st.session_state.delay_mitigation)
        with sim_col2:
            st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.75rem; color:#D97706; font-weight:600; margin-bottom:12px;'>[ CABIN IN-FLIGHT FLEET PARAMETERS ]</p>", unsafe_allow_html=True)
            st.session_state.wifi_reliability = st.slider("Wi-Fi Array Fleet Coverage (%)", 0, 100, st.session_state.wifi_reliability)
            st.session_state.seat_upgrade_factor = st.slider("Seat Ergonomic Architecture Allocation Index", 1, 10, st.session_state.seat_upgrade_factor)
            
        st.markdown("<br><hr style='border-color: rgba(15, 23, 42, 0.08);'/>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='font-family:\"Inter\"; font-weight:600; font-size:1.1rem; color:#0F172A; margin-top:10px; margin-bottom:15px;'>Projected Simulation Array Yield Matrix</h3>", unsafe_allow_html=True)
        out1, out2 = st.columns(2)
        with out1:
            st.metric(label="Simulated Network CSAT Score target", value=f"{dynamic_csat_score:.2f}%", delta=f"+{dynamic_csat_score-72.4:.1f}% vs Control Base")
        with out2:
            st.metric(label="Calculated Gross Revenue Protection Yield Portfolio", value=f"${revenue_saved_value:.2f}M", delta="Risk Reduced Asset Vector")

# --------------------------------------------------
# SYSTEM CONSOLE FOOTER TERMINAL
# --------------------------------------------------
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(15, 23, 42, 0.08);'/>", unsafe_allow_html=True)
f_col1, f_col2 = st.columns(2)
with f_col1:
    st.markdown("<p style='font-family:\"JetBrains Mono\"; font-size:0.7rem; color:#94A3B8;'>AEROOPTIMA OPERATIONAL INTERFACE PLATFORM v3.0 // SECURITY LOG LINK ENCRYPTED</p>", unsafe_allow_html=True)
