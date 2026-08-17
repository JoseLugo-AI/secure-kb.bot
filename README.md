# Secure-KB-Assistant: Enterprise RAG Architecture
**Portfolio demo — security-first internal knowledge base on Azure OpenAI & LangChain.**

[![Status](https://img.shields.io/badge/Status-Portfolio--Demo-lightgrey.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](#)
[![Security](https://img.shields.io/badge/Architecture-Zero--Trust-red.svg)](#)

> **This is a portfolio / demo artifact, not a production product and not a client deployment.** The public repo is the demo configuration. My core offer is Microsoft 365 Copilot GDPR consulting: **[joselugo.de](https://joselugo.de)**.

## Overview
**Secure-KB-Assistant** is a Retrieval-Augmented Generation (RAG) demo: query internal PDF documents (security STIGs, HR policies, compliance manuals) with answers grounded in retrieved sources. The design goal is that data stays in your Azure tenant rather than public-model training.

### Key Highlights
* **Data Privacy:** Hosted on Azure; no training on public models.
* **Deep Context:** PDF structure via LangChain & Azure AI Search.
* **Fact-Grounded:** Source citations to reduce hallucinations.
* **Infrastructure-Ready:** Staged Virtual Network (VNet) notes for Private Link isolation.

## Architecture
![Enterprise RAG Diagram](./Hardened%20Enterprise%20RAG%20Architecture.png)

> **Architecture note:** The diagram shows a *target* hardened state (private endpoints + disabled public access). This repository is the public demo; treat the VNet cutover as a documented direction, not a claim that this clone is already isolated.

## Compliance & Governance Frameworks
This architecture is aimed at the following standards (alignment of design, not a formal certification of this repo):

* **GDPR (EU):** Data residency / sovereignty; no sending data to public models for training.
* **EU AI Act:** Human-in-the-loop transparency via source citations and grounding.
* **HIPAA / HITRUST (US):** Encryption-at-rest and in-transit patterns for PHI-style content.
* **SOC2 / ISO 27001:** Logging, monitoring, and identity isolation (RBAC) as design themes.
* **NIST AI 100-1:** AI Risk Management Framework (AI RMF) for trustworthy AI deployment.

## Security & Hardening (CISSP Mindset)
Built with **enterprise readiness** in mind. Currently configured as a public demo; the following is **staged / documented**, not implied to be live on this GitHub copy:

* **Virtual Network (VNet):** `secure-kb-vnet` to isolate AI traffic.
* **Private DNS Zones:** `openai.azure.com` and `search.windows.net`.
* **Private Endpoints:** Direction of travel to disable public internet access.
* **Managed Identity:** Passwordless authentication using Azure RBAC.

## Getting Started

### Prerequisites
- Python 3.12+
- Azure OpenAI and Azure AI Search resources

### Installation & Usage
1. **Clone the repo** (GitHub name is `secure-kb.bot`):

   ```bash
   git clone https://github.com/JoseLugo-AI/secure-kb.bot.git
   cd secure-kb.bot
   ```

2. **Install dependencies** (this repo does not currently ship `requirements.txt` or `.env.example`):

   ```bash
   pip install streamlit python-dotenv langchain-community langchain-text-splitters langchain-openai pypdf azure-search-documents
   ```

3. **Configure environment:** Create a `.env` file with your Azure OpenAI and Azure AI Search credentials (endpoint, keys, deployment, index name).

4. **Ingest data:** Create a `data/` folder, place PDFs there, then from the repo root:

   ```bash
   python scripts/ingest_data.py
   ```

5. **Launch chatbot:**

   ```bash
   streamlit run scripts/app.py
   ```

## License & Contributions
* **License:** MIT License — fork and adapt for internal use.
* **Contributing:** Issues and pull requests welcome for security features or prompt engineering.

## Author
**Jose Lugo** — Infrastructure Security Expert & AI Solutions Architect

A 12-year **U.S. Army Veteran** and **Senior Systems Administrator** specializing in the intersection of **Cybersecurity (CISSP/Security+)** and Generative AI. Based in Germany. Core consulting offer: Microsoft 365 Copilot GDPR / DSGVO — [joselugo.de](https://joselugo.de).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jose-lugo-cissp-327045308/)