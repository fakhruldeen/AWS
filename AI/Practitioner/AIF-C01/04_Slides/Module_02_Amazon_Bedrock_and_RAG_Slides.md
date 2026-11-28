---
marp: true
theme: default
paginate: true
header: "AWS Certified AI Practitioner (AIF-C01) | Module 2: Amazon Bedrock & RAG"
footer: "© Mohamed Fakhruldeen — fakhruldeen/AWS"
style: |
  section {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    background-color: #f8fafc;
  }
  h1 {
    color: #0f172a;
  }
  h2 {
    color: #2563eb;
  }
  footer {
    font-size: 0.75rem;
    color: #64748b;
  }
---

# AWS Certified AI Practitioner (AIF-C01)
## Module 2: Amazon Bedrock, RAG & Foundation Model Applications

**Instructor:** Mohamed Fakhruldeen  
**Track:** AI Foundation  
**Repository:** `fakhruldeen/AWS`

---

## What is Amazon Bedrock?

* A **fully managed, serverless service** offering high-performing Foundation Models (FMs) from Amazon and leading AI startups through a **single, unified API**.
* **Zero Infrastructure Overhead:** No EC2 instances, GPU drivers, or Kubernetes clusters to manage.
* **The Privacy Guarantee:**
  * **AWS never uses your prompts, completions, or data to train base models!**
  * Your data is cryptographically isolated and remains in your AWS account and chosen Region.

---

## The Bedrock Model Catalog

| Provider | Model Family | Ideal Use Case |
|---|---|---|
| **Anthropic** | Claude (3.5 Sonnet, 3 Haiku, Opus) | Coding, reasoning, multimodal vision, 200k context |
| **Amazon** | Titan (Text, Image, Embeddings) | High-speed, cost-effective embeddings and generation |
| **Amazon** | Nova (Micro, Lite, Pro, Premier) | Next-gen cost-optimized reasoning and multimodal |
| **Meta** | Llama 3.1 / 3.2 | Open-weights, efficient multilingual processing |
| **Mistral AI** | Mistral / Mixtral / Large | High-efficiency mixture-of-experts (MoE) |
| **Cohere** | Command / Embed | Enterprise text, multilingual search re-ranking |

---

## The Model Customization Spectrum

```
[Prompt Engineering] ---> [RAG] ---> [Fine-Tuning] ---> [Pre-Training]
  Lowest Cost / Zero       Dynamic Data      Custom Style/Jargon   Massive Scale
  Weights Frozen           Weights Frozen    Weights Updated       All Weights Init
```

* **When to Prompt:** Zero training budget, quick experimentation.
* **When to RAG:** Internal, rapidly changing company docs; strict citation needs.
* **When to Fine-Tune:** Specific brand voice, niche terminology, custom JSON syntax.
* **When to Pre-Train:** Building your own foundation model from scratch.

---

## Retrieval-Augmented Generation (RAG) Architecture

```
1. INGESTION (Offline):
   S3 Docs ---> Chunking ---> Titan Embeddings ---> Vector Store (OpenSearch)

2. QUERY (Runtime):
   User Prompt ---> Vector Search ---> Retrieve Top-K Chunks
   Augmented Prompt (Context + Question) ---> Claude/Titan ---> Answer + Citations
```

* **Why RAG Wins:**
  * Eliminates hallucinations by grounding the model in verified facts.
  * Instant knowledge updates (re-index docs without retraining).
  * Direct clickable source citations for regulatory trust.

---

## Amazon Bedrock Knowledge Bases

* The **fully managed RAG solution** built directly into Bedrock.
* **Supported Vector Stores:**
  * Amazon OpenSearch Serverless (Default & recommended)
  * Amazon Aurora PostgreSQL (`pgvector`)
  * Amazon Neptune Analytics
  * Pinecone
* **Chunking Options:**
  * *Fixed-size:* Default 300 tokens with 20% overlap.
  * *Hierarchical:* Child chunks for search, parent chunks for broad context.
  * *Semantic:* Splits on topic shifts.

---

## Amazon Bedrock Agents

* **What They Are:** Autonomous generative AI agents that orchestrate multi-step business workflows.
* **How They Work (ReAct Framework):**
  1. Break user goal into sequential sub-tasks.
  2. Call external APIs (**Action Groups**) via **AWS Lambda** using **OpenAPI schemas**.
  3. Query **Knowledge Bases** for enterprise context.
  4. Retain conversational memory across multi-turn dialogues.
* **Example:** *"Check customer balance, if positive book flight #45, send confirmation email."*

---

## Amazon Bedrock Guardrails

* Built-in responsible AI and content safety layer.
* **Key Mechanisms:**
  * **Denied Topics:** Block off-limit subjects using natural language descriptions.
  * **Content Filters:** Calibrate thresholds for Hate, Insults, Sexual, Violence, Misconduct.
  * **Sensitive Information (PII):** Auto-mask or block SSNs, credit cards, emails.
  * **Contextual Grounding Check:** Evaluates whether generated responses are factually grounded in retrieved RAG context.

---

## Bedrock Prompt Management & Prompt Flows

* **Prompt Management:**
  * Centralized catalog for creating, testing, versioning, and deploying prompt templates.
  * Supports runtime variables via `{{variable}}`.
* **Prompt Flows (Bedrock Flows):**
  * Visual, drag-and-drop canvas for generative AI pipelines.
  * Chaining *Prompt Nodes, Model Nodes, Knowledge Base Nodes, Lambda Nodes, and Router Nodes* without orchestration code.

---

## Automated Model Evaluation Metrics

* **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):**
  * Measures $n$-gram overlap; heavily **Recall-focused**.
  * Gold standard for **Text Summarization**.
* **BLEU (Bilingual Evaluation Understudy):**
  * Measures $n$-gram match; **Precision-focused** with Brevity Penalty.
  * Gold standard for **Machine Translation**.
* **BERTScore:**
  * Computes cosine similarity of contextual embeddings.
  * Evaluates **semantic meaning** when synonyms/paraphrasing are used.
* **Perplexity (PPL):**
  * Measures model uncertainty/fluency. **Lower is better!**

---

## The Amazon Q Enterprise Suite

* **Amazon Q Developer:**
  * Coding assistant in IDE/CLI; scans for vulnerabilities; automates **Java 8/11 to 17 migrations**.
* **Amazon Q Business:**
  * Enterprise assistant connecting to 40+ data stores (SharePoint, S3, Salesforce) with **Role-Based Access Control (RBAC)**.
* **Amazon Q in QuickSight:**
  * Conversational BI queries generating immediate charts and executive narratives.
* **Amazon Q in AWS Glue:**
  * Natural language generation of PySpark data integration pipelines.

---

## Hands-On Lab Preview: Lab 02 & Lab 03

* **Lab 02: Building a RAG Knowledge Base:**
  * Upload company policies to Amazon S3.
  * Create a Bedrock Knowledge Base using Titan Embeddings and OpenSearch Serverless.
  * Test semantic query retrieval and answer generation with Claude.
* **Lab 03: Responsible AI & Guardrails:**
  * Configure PII masking and denied topics.
  * Test prompt injection and observe real-time redaction.

---

# Questions & Discussion

**Next Module:** Module 3: Amazon SageMaker AI Ecosystem & Custom Machine Learning

---

# Module 2 Student Review Quiz

1. **A developer is building a legal document question-answering assistant with Amazon Bedrock. The model must produce strictly factual, deterministic answers with zero creative deviation. Which inference parameter setting is MOST appropriate?**
   * A) Temperature = 1.0, Top-P = 1.0
   * B) Temperature = 0.0, Top-P low *(Correct — minimizes randomness; greedy decoding)*
   * C) Temperature = 0.9, Top-K = 500
   * D) Max Generation Length = 10 tokens

2. **A bank wants to build an AI assistant that answers questions about internal private credit policies without updating the neural network weights of the underlying foundation model. Which architecture solves this?**
   * A) Full Model Pre-training
   * B) Instruction Fine-Tuning
   * C) Retrieval-Augmented Generation (RAG) using Bedrock Knowledge Bases *(Correct — grounds responses in external vector store)*
   * D) Prompt Injection

3. **Which family of AWS foundation models natively supports multimodal input processing across text, images, and video with state-of-the-art price-performance?**
   * A) Amazon Titan Text Express
   * B) Amazon Nova (Micro, Lite, Pro) *(Correct — next-generation multimodal foundation models)*
   * C) AWS DeepRacer
   * D) Amazon Kendra



---

# 🆕 Exam Guide v1.2 (2026) — Context Engineering & AWS Agentic Stack

- **Context Engineering:** Curating the *entire runtime context window* (system prompt + RAG + memory + tool outputs) within token limits
- **Model Context Protocol (`MCP`):** Open standard connecting AI agents to external tools, APIs, and data sources
- **AWS v1.2 GenAI & Agentic Offerings:**
  - **`Strands Agents`:** Open-source model-driven Python SDK for multi-agent apps with `MCP`
  - **`Amazon Bedrock AgentCore`:** Serverless enterprise runtime (`Runtime`, `Memory`, `Gateway`, `Identity`, `Policy`, `Observability`)
  - **`Kiro`** (spec-driven IDE) • **`Amazon Quick`** (AI BI) • **`AWS Transform`** (agentic legacy modernization)
