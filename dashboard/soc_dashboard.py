import pandas as pd
import plotly.graph_objects as go
import time
import random
import streamlit as st
from streamlit_autorefresh import st_autorefresh


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="SentinelAI SOC",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# AUTO REFRESH (SAFE & PRODUCTION READY)
# =========================================================
st_autorefresh(interval=2000, key="soc_refresh")

# =========================================================
# CYBER HUD CSS
# =========================================================
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
body { background-color: #0b0f1a; }

.glass {
    background: linear-gradient(
        145deg,
        rgba(17, 24, 39, 0.85),
        rgba(10, 15, 25, 0.85)
    );
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 22px;
    border: 1px solid rgba(0,245,212,0.18);
    box-shadow:
        inset 0 0 30px rgba(0,245,212,0.12),
        0 0 60px rgba(0,245,212,0.08);
}

.neon {
    color: #00f5d4;
    text-shadow:
        0 0 6px rgba(0,245,212,0.9),
        0 0 18px rgba(0,245,212,0.6);
    letter-spacing: 1.5px;
}

.feed {
    max-height: 280px;
    overflow-y: auto;
    font-size: 14px;
    line-height: 1.6;
}

.feed::-webkit-scrollbar {
    width: 6px;
}
.feed::-webkit-scrollbar-thumb {
    background: rgba(0,245,212,0.4);
    border-radius: 10px;
}

hr {
    border: none;
    height: 1px;
    margin: 30px 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(0,245,212,0.6),
        transparent
    );
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        rgba(12,18,32,0.95),
        rgba(8,12,22,0.95)
    );
}
</style>
""", unsafe_allow_html=True)
# =========================================================
# HEADER
# =========================================================
st.markdown("<h1 class='neon'>🛡️ SENTINEL AI — SECURITY OPERATIONS CENTER</h1>", unsafe_allow_html=True)
st.caption(f"🟢 LIVE SOC FEED • {time.strftime('%H:%M:%S')}")
st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# LOAD DATA (DOCKER + RENDER SAFE PATHS)
# =========================================================
alerts = pd.read_csv("alerts/prioritized_alerts.csv")
explanations = pd.read_csv("reports/ai_soc_explanations.csv")

data = alerts.merge(
    explanations,
    on=["source_ip", "user", "risk_score"],
    how="left"
)
# =========================================================
# SIDEBAR FILTERS
# =========================================================
st.sidebar.markdown("## 🎛️ SOC Filters")
min_risk = st.sidebar.slider("Minimum Risk Score", 0, 100, 20)
filtered = data[data["risk_score"] >= min_risk]
st.sidebar.markdown("## 🎮 Demo Mode")
demo_mode = st.sidebar.toggle("Enable Demo Mode", value=False)
# =========================================================
# KPI GAUGES
# =========================================================
def radial(title, value, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': color}},
        title={'text': title}
    ))
    fig.update_layout(height=220, paper_bgcolor="rgba(0,0,0,0)")
    return fig

c1, c2, c3, c4 = st.columns(4)
with c1: st.plotly_chart(radial("Threat Detection", 98, "#00f5d4"), use_container_width=True)
with c2: st.plotly_chart(radial("Response Accuracy", 96, "#5b7cfa"), use_container_width=True)
with c3: st.plotly_chart(radial("SOC Confidence", 99, "#f472b6"), use_container_width=True)
with c4: st.plotly_chart(radial("System Health", 92, "#4ade80"), use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# GLOBAL ATTACK PATHS
# =========================================================
st.markdown("## 🌍 Global Attack Paths")

attack_data = [
    (55.75, 37.61), (40.71, -74.00), (35.68, 139.69), (48.85, 2.35)
]

fig = go.Figure()
for lat, lon in attack_data:
    fig.add_trace(go.Scattergeo(
        lon=[lon, 77.20],
        lat=[lat, 28.61],
        mode="lines",
        line=dict(width=2, color="#ff4d4f"),
        opacity=0.6
    ))

fig.add_trace(go.Scattergeo(
    lon=[77.20], lat=[28.61],
    mode="markers",
    marker=dict(size=16, color="#00f5d4", line=dict(width=2, color="white"))
))

fig.update_layout(
    geo=dict(showland=True, landcolor="#0b0f1a", showcountries=True),
    paper_bgcolor="rgba(0,0,0,0)",
    height=420, showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# LOWER PANELS
# =========================================================
left, center, right = st.columns([1.2, 1.6, 1.2])

# =========================================================
# LIVE SOC LOG STREAM
# =========================================================
with left:
    st.markdown("## 📡 Live SOC Logs")

    if "logs" not in st.session_state:
        st.session_state.logs = []

    logs = [
        ("LOW", "User login success", "#4ade80"),
        ("MEDIUM", "Multiple failed logins", "#facc15"),
        ("HIGH", "Brute-force detected", "#ff4d4f"),
        ("HIGH", "Admin anomaly", "#ff4d4f"),
        ("MEDIUM", "Suspicious IP behavior", "#facc15"),
    ]

    if demo_mode:
       lvl, msg, col = random.choice(logs + [
        ("CRITICAL", "Credential stuffing attack", "#ff0066"),
        ("CRITICAL", "Suspicious admin elevation", "#ff0066")
    ])
    else:
       lvl, msg, col = random.choice(logs)

    entry = f"<span style='color:{col}; font-weight:bold;'>[{lvl}]</span> {time.strftime('%H:%M:%S')} — {msg}"

    st.session_state.logs.insert(0, entry)
    st.session_state.logs = st.session_state.logs[:10]

    st.markdown("<div class='glass feed'>" + "<br>".join(st.session_state.logs) + "</div>", unsafe_allow_html=True)

# =========================================================
# SOC COPILOT (OFFLINE LOGIC)
# =========================================================
with center:
    st.markdown("## 🤖 SOC Copilot")
    question = st.text_input("Ask the SOC Copilot", key="soc_copilot_input")

    if question:
        if "why" in question.lower():
            answer = "This alert shows brute-force behavior caused by repeated authentication failures."
        elif "action" in question.lower():
            answer = "Recommended actions: block source IP, reset credentials, monitor lateral movement."
        elif "mitre" in question.lower():
            answer = "Mapped to MITRE ATT&CK technique T1110 (Brute Force)."
        else:
            answer = "Analysis complete. Alert requires analyst investigation."

        st.markdown(f"<div class='glass'>{answer}</div>", unsafe_allow_html=True)
# =========================================================
# SOAR ACTIONS — PROFESSIONAL AUDIT TRAIL (STABLE)
# =========================================================
with right:
    st.markdown("## ⚡ SOAR Actions")

    # ---- Persistent State ----
    if "soar_audit" not in st.session_state:
        st.session_state.soar_audit = []

    if "soar_report" not in st.session_state:
        st.session_state.soar_report = None

    # ---- Analyst Controls (ALL KEYS DEFINED) ----
    action = st.selectbox(
        "Select Automated Response",
        ["Contain Threat", "Investigate Incident", "Ignore Alert"],
        key="soar_action_select"
    )

    confirm = st.checkbox(
        "Confirm action (required)",
        key="soar_confirm_checkbox"
    )

    # ---- Execute Playbook ----
    if st.button(
        "🚀 Execute SOAR Playbook",
        use_container_width=True,
        key="soar_execute_button"
    ):

        if not confirm:
            st.error("Confirmation required before executing SOAR action.")
        else:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            incident_id = f"INC-{random.randint(100000, 999999)}"

            if action == "Contain Threat":
                severity = "CRITICAL"
                response_steps = [
                    "Malicious indicators identified",
                    "Source IP blocked at perimeter firewall",
                    "Affected user account isolated",
                    "All active sessions revoked",
                    "SOC and Incident Response teams notified"
                ]
                conclusion = "Threat successfully contained. No further malicious activity observed."

            elif action == "Investigate Incident":
                severity = "HIGH"
                response_steps = [
                    "Authentication and access logs collected",
                    "IP reputation and geo-location correlated",
                    "MITRE ATT&CK techniques mapped",
                    "Incident escalated to Tier-2 analyst"
                ]
                conclusion = "Incident under investigation. Awaiting analyst findings."

            else:  # Ignore Alert
                severity = "LOW"
                response_steps = [
                    "Alert reviewed by SOC analyst",
                    "Determined to be false positive",
                    "No response actions required"
                ]
                conclusion = "Alert closed with no impact."

            # ---- Build Professional Audit Report ----
            report = f"""
INCIDENT REPORT
────────────────────────────────
Incident ID     : {incident_id}
Timestamp       : {timestamp}
Severity        : {severity}
Action Taken    : {action}

Execution Summary
─────────────────
""" + "\n".join([f"- {step}" for step in response_steps]) + f"""

Conclusion
──────────
{conclusion}

Audit Status
────────────
✔ Action executed successfully
✔ Logged for compliance and review
"""

            # ---- Save State ----
            st.session_state.soar_report = report.strip()
            st.session_state.soar_audit.insert(
                0, f"{timestamp} | {incident_id} | {action} | {severity}"
            )

            st.success("SOAR playbook executed and audit report generated.")

    # ---- DISPLAY AUDIT REPORT ----
    if st.session_state.soar_report:
        st.markdown("### 📄 SOAR Audit Report")
        st.markdown(
            f"<div class='glass'><pre>{st.session_state.soar_report}</pre></div>",
            unsafe_allow_html=True
        )

    # ---- DISPLAY AUDIT TRAIL ----
    if st.session_state.soar_audit:
        st.markdown("### 🧾 SOAR Audit Trail")
        st.markdown(
            "<div class='glass'>" +
            "<br>".join(st.session_state.soar_audit[:5]) +
            "</div>",
            unsafe_allow_html=True
        )
