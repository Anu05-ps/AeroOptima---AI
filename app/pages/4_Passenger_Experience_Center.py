import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PREMIUM CONSOLE ARCHITECTURE & CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AeroOptima AI | Voice of Passenger",
    page_icon="🎙️",
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
    .badge-indigo { background-color: #E0E7FF; color: #1E3A8A; border: 1px solid #C7D2FE; }
    
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
st.markdown('<h1 class="control-tower-title">Voice of Passenger™</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-sub-ticker">NLP SENTIMENT LAYER V3.0 // UNSTRUCTURED LINGUISTIC PIPELINE</p>', unsafe_allow_html=True)

# App Briefing Banner in Premium Silk UI Style
st.markdown("""
    <div class="hud-card" style="margin-bottom: 25px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
            <strong style="color: #0F172A; font-size: 1rem;">Semantic Experience Pipeline</strong>
            <span class="status-badge badge-indigo">REAL-TIME NLP PROCESSING ON</span>
        </div>
        <p style="color: #475569; font-size: 0.9rem; margin: 0; line-height: 1.5;">
            Extract semantic context trends from multi-channel user reviews. Track systemic sentiment distributions, isolate qualitative fault areas, and visualize severity parameters on a normalized index footprint.
        </p>
    </div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TELEMETRY KPI CARDS LAYER
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎙️ Positive Mentions Clustered", "58,956")
with col2:
    st.metric("😐 Neutral Signal Manifests", "50,144")
with col3:
    st.metric("⚠️ Negative Core Grievances", "20,355")

st.markdown("<br>", unsafe_allow_html=True)

# Global UI configuration properties for Plotly charts matching layout aesthetics
plotly_layout_args = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_family="Inter",
    font_color="#1E293B",
    title_font_size=14,
    title_font_color="#0F172A",
    
)

# --------------------------------------------------
# VISUAL INSIGHT INTERFACES (Two Column Workspace)
# --------------------------------------------------
workspace_left, workspace_right = st.columns(2, gap="large")

with workspace_left:
    st.markdown('<p class="module-header">🍩 Aggregated Sentiment Ratios</p>', unsafe_allow_html=True)
    sentiment_df = pd.DataFrame({
        "Sentiment": ["Positive", "Neutral", "Negative"],
        "Count": [58956, 50144, 20355]
    })
    
    fig_pie = px.pie(
        sentiment_df,
        names="Sentiment",
        values="Count",
        hole=0.55,
        title="Qualitative Feedback Vector Spread",
        color_discrete_sequence=["#2563EB", "#94A3B8", "#EF4444"] # Blue (Pos), Slate (Neu), Crimson (Neg)
    )
    fig_pie.update_layout(**plotly_layout_args)
    fig_pie.update_traces(textposition='outside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with workspace_right:
    st.markdown('<p class="module-header">📊 Primary Incident Volume Drivers</p>', unsafe_allow_html=True)
    complaints = pd.DataFrame({
        "Topic": ["Food", "Seat Comfort", "Delay", "Service", "Wifi", "Baggage", "Entertainment"],
        "Count": [47100, 27587, 20690, 16363, 4225, 3120, 2301]
    })
    
    fig_bar = px.bar(
        complaints,
        x="Count",
        y="Topic",
        orientation="h",
        color="Count",
        title="NLP Extracted Topic Frequency Thresholds",
        color_continuous_scale=["#C7D2FE", "#3B82F6", "#1E3A8A"] # Custom Premium Corporate Indigo Scale
    )
    fig_bar.update_layout(**plotly_layout_args, coloraxis_showscale=False)
    fig_bar.update_xaxes(showgrid=True, gridcolor="rgba(15, 23, 42, 0.05)", title_text="Total Document Hits")
    fig_bar.update_yaxes(showgrid=False, title=None)
    st.plotly_chart(fig_bar, use_container_width=True)

# --------------------------------------------------
# ADVANCED SEVERITY CORRELATION LAYER
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📈 Passenger Pain Index™ (Friction Matrix vs Severity Scores)</p>', unsafe_allow_html=True)

pain_df = pd.DataFrame({
    "Topic": ["Baggage", "Delay", "Service", "Seat Comfort", "Entertainment", "Wifi", "Food"],
    "Avg_Score": [2.38, 2.40, 4.23, 4.50, 4.53, 5.76, 5.95]
})

fig_pain = px.bar(
    pain_df,
    x="Topic",
    y="Avg_Score",
    color="Avg_Score",
    title="Normalized Complaint Gravity Curve (Lower Scores = Higher Friction/Severe Impact)",
    color_continuous_scale=["#EF4444", "#F59E0B", "#10B981"] # Modern Crimson -> Amber -> Emerald scale
)
fig_pain.update_layout(**plotly_layout_args, coloraxis_showscale=False)
fig_pain.update_xaxes(showgrid=False, title=None)
fig_pain.update_yaxes(showgrid=True, gridcolor="rgba(15, 23, 42, 0.05)", title_text="Normalized Score Baseline")
st.plotly_chart(fig_pain, use_container_width=True)

# --------------------------------------------------
# STRATEGIC INTERVENTION ACTION CENTRE
# --------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="module-header">📌 Executive Sentiment Insights Desk</p>', unsafe_allow_html=True)

info_col1, info_col2 = st.columns(2, gap="medium")

with info_col1:
    st.markdown("""
        <div class="hud-alert-card" style="height: 100%;">
            <h4 style="margin-top:0; color:#D97706; font-weight:600; font-size:1.05rem; margin-bottom:8px;">
                ⚠️ Volume vs Severity Disconnect Flagged
            </h4>
            <p style="color:#92400E; font-size:0.9rem; margin:0; line-height:1.6; font-weight: 500;">
                <b>Food & Beverage</b> components trigger maximum overall mention density counts.<br><br>
                However, <b>Baggage Tracking</b> and <b>Terminal Delays</b> generate disproportionately harsher sentiment impacts, dragging down individual core CSAT performance rankings. Remediation focus should shift to backend tracking infrastructure.
            </p>
        </div>
    """, unsafe_allow_html=True)

with info_col2:
    st.markdown("""
        <div class="hud-card" style="height: 100%; border-top: 4px solid #2563EB !important;">
            <h4 style="margin-top:0; color:#0F172A; font-weight:600; font-size:1.05rem; margin-bottom:12px;">
                Strategic Operational Directives
            </h4>
            <ul style="color:#475569; font-size:0.85rem; margin:0; padding-left:18px; line-height:1.7;">
                <li>Food remains a primary qualitative talking point across customer touchpoint clusters.</li>
                <li>Baggage-handling logistics failures cause immediate customer retention drops.</li>
                <li>Delay mitigation steps provide the fastest path to recovering neutral-to-negative pipelines.</li>
                <li>Strategic resource deployment provides the highest structural ROI by targeting baggage and delay infrastructure.</li>
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
