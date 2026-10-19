import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page Configuration for a Professional Look
st.set_page_config(
    page_title="AIUE / OSIN Enterprise Implementation Simulator",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Executive Theme
st.markdown("""
    <style>
    .main-header {
        font-size: 28px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 16px;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2563EB;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Controls for Enterprise Assessment
st.sidebar.header("⚙️ Evaluation Parameters")
st.sidebar.markdown("Adjust the sliders to simulate organizational readiness across the four core dimensions.")

data_infra = st.sidebar.slider("1. Data Infrastructure & Pipelines", 1, 5, 3, help="Unification, real-time sync, and data cleanliness.")
gov_risk = st.sidebar.slider("2. Governance & Risk De-escalation", 1, 5, 4, help="Automated compliance and risk monitoring protocols.")
op_agility = st.sidebar.slider("3. Operational Agility", 1, 5, 3, help="Workflow adaptability to advanced algorithmic outputs.")
cult_readiness = st.sidebar.slider("4. Leadership & Cultural Alignment", 1, 5, 4, help="Executive sponsorship and cross-functional execution.")

# Calculations
dimensions = [
    'Data Infrastructure', 
    'Governance & Risk', 
    'Operational Agility', 
    'Cultural Readiness'
]
scores = [data_infra, gov_risk, op_agility, cult_readiness]
iss_score = sum(scores)
max_score = 20
percentage = (iss_score / max_score) * 100

# Main Dashboard Layout
st.markdown('<p class="main-header">AIUE / OSIN Enterprise Scalability Simulator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Diagnostic Engine for Implementation Readiness & Risk Mitigation</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1.8], gap="large")

with col1:
    st.markdown("### 📊 Executive Scorecard")
    
    # Dynamic Verdict Logic
    if iss_score >= 16:
        status_color = "#10B981"
        verdict = "STAGE 4 READY: Full-Stack AIUE Deployment Authorized"
        description = "The organization exhibits robust scalability across all pillars. Ready for immediate integration."
    elif iss_score >= 11:
        status_color = "#F59E0B"
        verdict = "PHASED ROLLOUT: Targeted De-Risking Required"
        description = "High potential, but specific bottlenecks must be addressed before full-scale deployment."
    else:
        status_color = "#EF4444"
        verdict = "HIGH EXECUTION RISK: Foundational Remediation Needed"
        description = "Core structural or data vulnerabilities present high risk of project friction."

    st.markdown(f"""
        <div class="metric-card" style="border-left-color: {status_color};">
            <h2 style="margin: 0; color: {status_color};">{iss_score} / 20 ({percentage:.0f}%)</h2>
            <p style="font-weight: bold; margin-top: 5px; color: #1F2937;">{verdict}</p>
            <p style="font-size: 13px; color: #4B5563; margin-bottom: 0;">{description}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Strategic Recommendations")
    if data_infra < 3:
        st.warning("• **Data Action:** Establish centralized data lakes and clean ingestion channels before live deployment.")
    if gov_risk < 3:
        st.warning("• **Governance Action:** Implement automated compliance checks and risk mitigation guardrails.")
    if op_agility < 3:
        st.warning("• **Operations Action:** Conduct specialized team training programs on algorithmic workflows.")
    if cult_readiness < 3:
        st.warning("• **Culture Action:** Secure active executive sponsorship to drive cross-functional adoption.")
    
    if iss_score >= 11 and data_infra >= 3 and gov_risk >= 3 and op_agility >= 3 and cult_readiness >= 3:
        st.success("• **All Systems Optimal:** Proceed with scheduled OMNI-SYNAPSE protocol integration.")

with col2:
    st.markdown("### 🎯 Dimensional Radar & Competency Profile")
    
    # Creating a professional Plotly Radar Chart
    fig_radar = go.Figure()

    fig_radar.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],  # Close the loop
        theta=dimensions + [dimensions[0]],
        fill='toself',
        name='Organization Score',
        line=dict(color='#2563EB', width=3),
        fillcolor='rgba(37, 99, 235, 0.2)'
    ))

    # Benchmark Trace (Target = 4)
    fig_radar.add_trace(go.Scatterpolar(
        r=[4, 4, 4, 4, 4],
        theta=dimensions + [dimensions[0]],
        mode='lines',
        name='Target Threshold',
        line=dict(color='#9CA3AF', width=2, dash='dash')
    ))

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickfont=dict(size=10),
                gridcolor='#E5E7EB'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='#1F2937'),
                gridcolor='#E5E7EB'
            ),
            bgcolor='white'
        ),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="right", x=1),
        margin=dict(t=40, b=20, l=40, r=40),
        height=400
    )

    st.plotly_chart(fig_radar, use_container_width=True)

# Footer Detail
st.markdown("---")
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 12px;'>AI Universal Engine (AIUE) & OSIN Intelligence Nexus — Confidential Strategic Analytics</p>", unsafe_allow_html=True)
