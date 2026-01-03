# 🛡️ SentinelAI SOC  
### AI-Augmented Security Operations Center with SOAR & Audit Trail

SentinelAI SOC is a **portfolio-grade Security Operations Center (SOC) dashboard** that simulates how modern SOC teams **detect, investigate, and respond** to security incidents using **automation (SOAR)** and **analyst workflows**.

This project focuses on **stability, clarity, and realism** rather than gimmicks.

## 🚀 Key Features

### 🔍 Threat Monitoring
- Live SOC log simulation
- Risk-based alert filtering
- Global attack path visualization

### 🤖 SOC Copilot (Offline AI Logic)
- Human-readable alert explanations
- MITRE ATT&CK–style reasoning
- Analyst-friendly responses

### ⚡ SOAR Automation (Core Highlight)
- One-click SOAR playbook execution
- Analyst confirmation (real-world behavior)
- Severity classification (LOW / HIGH / CRITICAL)
- **Professional incident report generation**
- **Persistent SOC audit trail**

### 🧾 SOC Audit Trail
- Unique Incident ID generation
- Timestamped execution logs
- Compliance-style audit entries
- Session-persistent and refresh-safe
  
## 🧠 Example SOAR Audit Report
INCIDENT REPORT
────────────────────────────────
Incident ID : INC-483921
Timestamp : 2026-01-02 14:55:10
Severity : CRITICAL
Action Taken : Contain Threat

Execution Summary
─────────────────

Malicious indicators identified

Source IP blocked at perimeter firewall

Affected user account isolated

Active sessions revoked

SOC and IR teams notified

Conclusion
──────────
Threat successfully contained. No further malicious activity observed.

Audit Status
────────────
✔ Action executed successfully
✔ Logged for compliance and review

## 🧱 Tech Stack

- **Frontend / UI**: Streamlit  
- **Visualization**: Plotly  
- **Automation Logic**: Python  
- **State Management**: Streamlit Session State  
- **Containerization**: Docker  
- **Deployment**: Docker Hub / Render  

## 🖥️ Local Setup
pip install -r requirements.txt
streamlit run dashboard/soc_dashboard.py

## 🐳 Docker Deployment
Build Image
docker build -t safalc/sentinel-ai-soc:latest .

Push Image
docker push safalc/sentinel-ai-soc:latest

Image URL (Render / Cloud)
docker.io/safalc/sentinel-ai-soc:latest

## 📁 Project Structure
SentinelAI-SOC/
├── dashboard/
│   └── soc_dashboard.py
├── alerts/
│   └── prioritized_alerts.csv
├── reports/
│   └── ai_soc_explanations.csv
├── requirements.txt
├── Dockerfile
└── README.md

## 🎯 What This Project Demonstrates
Understanding of SOC workflows

Practical SOAR automation design

Incident response lifecycle knowledge

Stable audit trail implementation

Production-safe Streamlit architecture

Dockerized cloud deployment

## 📸 Screenshots & Demo

### 🖥️ SOC Dashboard Overview
Shows the main SOC interface with KPIs, global attack paths, and live log feed.

![SOC Dashboard](screenshots/dashboard_overview.png)

### ⚡ SOAR Playbook Execution
Demonstrates one-click SOAR automation with analyst confirmation and response execution.

![SOAR Execution](screenshots/soar_execution.png)

### 🧾 Professional SOAR Audit Report
Generated incident report with severity, execution summary, and compliance logging.

![SOAR Audit Report](screenshots/soar_audit_report.png)

### 📊 SOC Audit Trail
Persistent audit trail capturing all automated response actions.

![Audit Trail](screenshots/soar_audit_trail.png)

## ⚠️ Disclaimer
This project is a simulation intended for learning, demonstration, and portfolio purposes only.
It does not perform real security enforcement

## 👤 Author
Safal Chaturvedi
Cybersecurity | SOC | SOAR | AI-Assisted Security




