# 📝 AWS Certified AI Practitioner (AIF-C01) High-Yield Study Notes & Cheat Sheets

> **Module:** Rapid Study Notes, Distinction Tables & Exam Cheat Sheets  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Exam Version Alignment:** Official v1.2 (October 2026)  
> **Target Audience:** Students and exam candidates in their final sprint review before taking the official exam.

---

## 🗺️ Master Notes & Distinction Index

| Note Guide | Core Subject Area | Exam Domain | Key Concepts & High-Yield Tables |
| :--- | :--- | :---: | :--- |
| **[01_GenAI_Fundamentals.md](./01_GenAI_Fundamentals.md)** | Generative AI Core Concepts | **Domain 2** | Transformer Self-Attention, Positional Encoding, Tokens, Context Windows, Temperature, Top-P, Top-K, Nova Models. |
| **[02_Prompt_Engineering_Guide.md](./02_Prompt_Engineering_Guide.md)** | Prompt Engineering Patterns | **Domain 3** | Zero-Shot, Few-Shot In-Context Learning, Chain-of-Thought (CoT), Step-Back, ReAct loops, Delimiters, System Directives. |
| **[03_Amazon_Bedrock_and_RAG.md](./03_Amazon_Bedrock_and_RAG.md)** | Bedrock, RAG & Agents | **Domain 3** | Serverless Bedrock API, Titan Embeddings v2, OpenSearch Serverless, Chunking, Bedrock Agents, OpenAPI, Lambda Actions. |
| **[04_Amazon_SageMaker_Suite.md](./04_Amazon_SageMaker_Suite.md)** | SageMaker Predictive & GenAI | **Domain 1 & 4** | Canvas (No-Code), Data Wrangler, Autopilot, 4 Deployment Modes (Real-Time, Serverless, Async, Batch), Clarify, Model Cards. |
| **[05_Responsible_AI_and_Governance.md](./05_Responsible_AI_and_Governance.md)** | Responsible AI & Security | **Domain 4 & 5** | 6 Pillars of Responsible AI, Pre/Post Bias Metrics (CI, DPL, DPPL, DI), SHAP explainability, Bedrock Guardrails, PrivateLink. |
| **[06_AIF-C01_Exam_CheatSheet.md](./06_AIF-C01_Exam_CheatSheet.md)** | **Master Distinction Cheat Sheet** | **Domains 1–5** | **The Ultimate Exam Cheatsheet:** Side-by-side distinction tables (RAG vs Fine-Tuning, ROUGE vs BLEU, 4 Deployment Modes, Traps). |

---

## ⚖️ Dedicated "X vs. Y" Pairwise Distinction Suite (`distinctions/`)

For resolving close "distractor" choices on the exam, consult our 10 focused pairwise comparison guides:

| Distinction Guide | Compared Services & Concepts | Exam Domain Focus |
|---|---|:---:|
| **[01_Model_Adaptation_Prompting_vs_RAG_vs_FineTuning_vs_Pretraining.md](./distinctions/01_Model_Adaptation_Prompting_vs_RAG_vs_FineTuning_vs_Pretraining.md)** | Prompting vs. RAG vs. Fine-Tuning vs. Pretraining | Domain 2 & 3 |
| **[02_Evaluation_Metrics_ROUGE_vs_BLEU_vs_Perplexity_vs_BERTScore.md](./distinctions/02_Evaluation_Metrics_ROUGE_vs_BLEU_vs_Perplexity_vs_BERTScore.md)** | ROUGE vs. BLEU vs. Perplexity vs. BERTScore | Domain 2 |
| **[03_SageMaker_Deployment_Modes_RealTime_vs_Serverless_vs_Async_vs_Batch.md](./distinctions/03_SageMaker_Deployment_Modes_RealTime_vs_Serverless_vs_Async_vs_Batch.md)** | Real-Time vs. Serverless vs. Async vs. Batch Transform | Domain 1 & 4 |
| **[04_Inference_Parameters_Temperature_vs_TopP_vs_TopK.md](./distinctions/04_Inference_Parameters_Temperature_vs_TopP_vs_TopK.md)** | Temperature vs. Top-P vs. Top-K vs. Stop Sequences | Domain 2 |
| **[05_Bedrock_Model_Families_Claude_vs_Titan_vs_Nova_vs_Llama_vs_Mistral.md](./distinctions/05_Bedrock_Model_Families_Claude_vs_Titan_vs_Nova_vs_Llama_vs_Mistral.md)** | Claude 3.5 vs. Amazon Nova vs. Titan vs. Llama 3.1 vs. Mistral | Domain 3 |
| **[06_Responsible_AI_Clarify_vs_Guardrails_vs_ModelCards_vs_ModelDashboard.md](./distinctions/06_Responsible_AI_Clarify_vs_Guardrails_vs_ModelCards_vs_ModelDashboard.md)** | SageMaker Clarify vs. Bedrock Guardrails vs. Model Cards vs. Model Dashboard | Domain 4 & 5 |
| **[07_Generative_AI_Security_Scopes_1_vs_2_vs_3_vs_4.md](./distinctions/07_Generative_AI_Security_Scopes_1_vs_2_vs_3_vs_4.md)** | GenAI Security Scopes 1, 2, 3, and 4 (Bedrock PrivateLink & KMS) | Domain 5 |
| **[08_Vector_Databases_OpenSearch_Serverless_vs_Aurora_pgvector_vs_Neptune.md](./distinctions/08_Vector_Databases_OpenSearch_Serverless_vs_Aurora_pgvector_vs_Neptune.md)** | OpenSearch Serverless vs. Aurora pgvector vs. Neptune Analytics | Domain 3 |
| **[09_Learning_Paradigms_Supervised_vs_Unsupervised_vs_Reinforcement_Learning.md](./distinctions/09_Learning_Paradigms_Supervised_vs_Unsupervised_vs_Reinforcement_Learning.md)** | Supervised vs. Unsupervised vs. RL vs. RLHF/RLAIF | Domain 1 |
| **[10_Auditing_Trio_CloudTrail_Data_Events_vs_Bedrock_Invocation_Logs_vs_Macie.md](./distinctions/10_Auditing_Trio_CloudTrail_Data_Events_vs_Bedrock_Invocation_Logs_vs_Macie.md)** | CloudTrail Data Events vs. Bedrock Model Invocation Logs vs. Amazon Macie | Domain 5 |


---

## 🎯 How to Use These Notes for Revision

1. **Phase 1: Deep Dive Review:** Read files `01` through `05` after watching the lectures or reviewing the slide decks.
2. **Phase 2: Distinction Mastery:** Use `06_AIF-C01_Exam_CheatSheet.md` to memorize subtle service boundaries (e.g., when to choose Asynchronous Inference vs. Batch Transform, or ROUGE vs. BLEU).
3. **Phase 3: Targeted Practice:** Drill with the [AIF-C01 Practice Exams & Revision Sets](../11_Practice_Exams/README.md) and take the [65-Question Full-Length Mock Exam](../11_Practice_Exams/AIF_C01_Full_Length_Mock_Exam.md).
