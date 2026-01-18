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

## 👨‍💻 Author
**Jose Lugo** *Senior Systems Administrator | ISSO | CISSP | Security+*

A 12-year **U.S. Army Veteran** (HUMINT & Civil Affairs) and current **Senior Windows Systems Administrator** with a career dedicated to safeguarding mission-critical information systems. 

I specialize in **Hardened Infrastructure**, leveraging deep expertise in:
* **Compliance:** Implementing STIGs, RMF, and NIST frameworks within Lockheed Martin and V2X environments.
* **Identity & Access:** Managing Active Directory, GPOs, and Certificate Authorities (CAs) for high-security networks.
* **Automation:** Using PowerShell to bridge the gap between legacy systems and modern cloud architecture.

**The Mission:** This project represents my transition into **AI Security**, applying a "Zero-Trust" mindset to Generative AI. I build RAG solutions that respect the same strict security protocols (STIGs/VNet isolation) required by the US Department of Defense and global enterprise leaders.

[![LinkedIn](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)
