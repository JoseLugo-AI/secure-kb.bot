# 🛡️ Secure-KB-Assistant: Enterprise RAG Architecture
**A Security-First Internal Knowledge Base powered by Azure OpenAI & LangChain.**

[![Status](https://img.shields.io/badge/Status-Hardening--Ready-success.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](#)
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

> **Note:** Ensure your image filename on GitHub is exactly `Hardened-Enterprise-RAG-Architecture.png`.

### High-Level Flow:
1. **Ingestion:** PDFs are chunked and converted into vector embeddings via AzureOpenAIEmbeddings.
2. **Storage:** Vectors are indexed in Azure AI Search with high-dimensional metadata.
3. **Retrieval:** Users query via a Streamlit UI; the system retrieves only relevant document sections.
4. **Generation:** GPT-4o synthesizes an answer using only the provided context and cites the source file.

---

## 🛡️ Security & Hardening (CISSP Mindset)
This project is built for **Enterprise Readiness**. While currently configured for a public demo, the following "Safe Room" architecture is staged:

* **Virtual Network (VNet):** `secure-kb-vnet` is provisioned to isolate AI traffic.
* **Private DNS Zones:** Configured for `openai.azure.com` and `search.windows.net`.
* **Private Endpoints:** Staged for a < 10-minute cutover to disable all public internet access.
* **Managed Identity:** Prepared for passwordless authentication using Azure RBAC.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.14+
- Azure OpenAI & Azure AI Search Resources

### Installation & Usage
1. **Clone the repo:**
   git clone https://github.com/JoseLugo-AI/secure-kb.bot.git
   cd secure-kb.bot

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Configure Environment:** Create a .env file in the root directory (use .env.example as a template) and add your Azure credentials.

4. **Ingest Data:**
   Place your PDFs in the data/ folder and run:
   python scripts/ingest_data.py

5. **Launch Chatbot:**
   streamlit run scripts/app.py

---

---

## ⚖️ Compliance & Governance Frameworks
This architecture is designed to meet the rigorous data protection standards required by global regulatory bodies. By utilizing **Azure Private Link** and **Isolated VNet** configurations, this project aligns with:

* **GDPR (EU):** Ensures data residency and sovereignty; no data is sent to public models for training.
* **EU AI Act:** Implements "Human-in-the-loop" transparency via source citations and verifiable grounding.
* **HIPAA / HITRUST (US):** Supports encryption-at-rest and in-transit for Protected Health Information (PHI).
* **SOC2 / ISO 27001:** Provides the logging, monitoring, and identity isolation (RBAC) required for enterprise security audits.
* **NIST AI 100-1:** Aligns with the AI Risk Management Framework (AI RMF) for trustworthy AI deployment.

---

## 👨‍💻 Author
**Jose Lugo** *Infrastructure Security Expert & AI Solutions Architect*

A 12-year **U.S. Army Veteran** and **Senior Systems Administrator** specializing in the intersection of **Cybersecurity (CISSP/Security+)** and Generative AI. Based in Germany, I bridge the gap between complex US-based security frameworks and European data sovereignty requirements.

**The Mission:** I build "Zero-Trust" AI solutions designed for high-consequence industries (Finance, Healthcare, and Legal). My work focuses on deploying RAG architectures that are not only high-performing but are built from the ground up to be **audit-ready** and compliant with global standards.

[![LinkedIn](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)
