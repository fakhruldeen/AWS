# 🖥️ AWS Certified AI Practitioner (AIF-C01) Marp Lecture Slide Decks

> **Module:** Classroom Presentation Slide Decks  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Format:** Marp (Markdown Presentation Ecosystem)  
> **Exam Version Alignment:** Official v1.2 (October 2026)

---

## 🗺️ Master Slide Decks Index

| Deck File | Domain Alignment | Exam Weight | Key Covered Topics |
|:--- |:--- |:---:|---|
| **[Module 01 Slides](./Module_01_AI_and_GenAI_Foundations_Slides.md)** | **Domain 1:** Fundamentals of AI & ML | 20% | AI vs ML vs DL, supervised/unsupervised/RL, ML lifecycle, evaluation metrics, SageMaker Canvas & AI Services. |
| **[Module 02 Slides](./Module_02_Amazon_Bedrock_and_RAG_Slides.md)** | **Domain 2:** Fundamentals of Generative AI | 24% | Transformers, Self-Attention, tokens, embeddings, context windows, Amazon Nova family, Agentic AI & MCP. |
| **[Module 03 Slides](./Module_03_Applications_of_FMs_RAG_and_Agents_Slides.md)** | **Domain 3:** Applications of Foundation Models | 28% | FM selection, Prompt Engineering, Prompt Caching, Enterprise RAG, Vector Search, LoRA, LLM-as-a-judge. |
| **[Module 04 Slides](./Module_04_Responsible_Transparent_and_Explainable_AI_Slides.md)** | **Domain 4:** Guidelines for Responsible AI | 14% | Responsible AI pillars, pre/post-training bias (CI, DPL, DI), SHAP explainability, Bedrock Guardrails, Model Cards. |
| **[Module 05 Slides](./Module_05_Security_Compliance_and_Governance_Slides.md)** | **Domain 5:** Security, Compliance & Governance | 14% | Generative AI Security Scoping Matrix, zero data retention, PrivateLink, IAM, Macie, CloudTrail, KMS CMKs. |

---

## 🚀 How to Render & Present with Marp

### 1. Visual Studio Code / Antigravity IDE:
* Install the **Marp for VS Code** extension (`marp-team.marp-vscode`).
* Open any slide deck markdown file and click the **Marp preview** icon in the top right.
* Press `F1` and select **Marp: Export Slide Deck...** to export to PDF, HTML, or PowerPoint (PPTX).

### 2. Command Line Interface (CLI):
```bash
npx @marp-team/marp-cli@latest Module_03_Applications_of_FMs_RAG_and_Agents_Slides.md --pdf -o Module_03_Slides.pdf
```
