# 🛡️ Secure-KB-Assistant: Enterprise RAG Architecture
**A Security-First Internal Knowledge Base powered by Azure OpenAI & LangChain.**

[![Status](https://img.shields.io/badge/Status-Demo--Ready-success.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](#)
[![Security](https://img.shields.io/badge/Architecture-Zero--Trust-red.svg)](#)

## 📖 Overview
The **Secure-KB-Assistant** is a Retrieval-Augmented Generation (RAG) solution designed for regulated industries (Finance, Healthcare, Government). It allows employees to query sensitive internal PDF documents (Security STIGs, HR Policies, Compliance Manuals) while ensuring data never leaves the private corporate perimeter.

### Key Highlights:
* **🔒 Data Privacy:** 100% hosted within Azure; zero training on public models.
* **📚 Deep Context:** Processes complex PDF structures using LangChain & Azure AI Search.
* **✅ Fact-Grounded:** Includes automatic source citations to prevent AI hallucinations.
* **🏗️ Infrastructure-Ready:** Built with a staged Virtual Network (VNet) for Private Link isolation.

---

## 📐 Architecture
![Enterprise RAG Diagram](./Hardened-Enterprise-RAG-Architecture.png) 

> **Architecture Note:** The diagram illustrates the "Hardened" production state (Private Endpoints + Disabled Public Access). This repository is configured for a rapid <10 minute cutover from public demo to fully isolated environment.

---

## ⚖️ Compliance & Governance Frameworks
This architecture is designed to meet the rigorous data protection standards required by global regulatory bodies. 

* **GDPR (EU):** Ensures data residency and sovereignty; no data is sent to public models for training.
* **EU AI Act:** Implements "Human-in-the-loop" transparency via source citations and verifiable grounding.
* **HIPAA / HITRUST (US):** Supports encryption-at-rest and in-transit for Protected Health Information (PHI).
* **SOC2 / ISO 27001:** Provides the logging, monitoring, and identity isolation (RBAC) required for enterprise security audits.
* **NIST AI 100-1:** Aligns with the AI Risk Management Framework (AI RMF) for trustworthy AI deployment.

---

## 🛡️ Security & Hardening (CISSP Mindset)
This project is built for **Enterprise Readiness**. While currently configured for a public demo, the following architecture is staged:

* **Virtual Network (VNet):** `secure-kb-vnet` is provisioned to isolate AI traffic.
* **Private DNS Zones:** Configured for `openai.azure.com` and `search.windows.net`.
* **Private Endpoints:** Staged for immediate cutover to disable public internet access.
* **Managed Identity:** Prepared for passwordless authentication using Azure RBAC.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Azure OpenAI & Azure AI Search Resources

### Installation & Usage
1. **Clone the repo:**
   git clone https://github.com/JoseLugo-AI/secure-kb-bot.git
   cd secure-kb-bot

2. **Install dependencies:**
   *(Includes LangChain, Azure SDKs, Streamlit, and PyPDF)*
   pip install -r requirements.txt

3. **Configure Environment:** Create a .env file (use .env.example as a template) and add your Azure credentials.

4. **Ingest Data:**
   Place PDFs in the data/ folder and run:
   python scripts/ingest_data.py

5. **Launch Chatbot:**
   streamlit run scripts/app.py

---

## 📜 License & Contributions
* **License:** MIT License – feel free to fork and adapt for your internal use.
* **Contributing:** Issues and Pull Requests are welcome for improvements to security features or prompt engineering.

---

## 👨‍💻 Author
**Jose Lugo** *Infrastructure Security Expert & AI Solutions Architect*

A 12-year **U.S. Army Veteran** and **Senior Systems Administrator** specializing in the intersection of **Cybersecurity (CISSP/Security+)** and Generative AI. Based in Germany, I bridge the gap between complex US-based security frameworks and European data sovereignty requirements.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)

---
