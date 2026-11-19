---
marp: true
theme: default
paginate: true
header: "AWS Certified AI Practitioner (AIF-C01) | Module 3: Applications of Foundation Models"
footer: "© Mohamed Fakhruldeen — fakhruldeen/AWS"
style: |
  section {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    background-color: #f8fafc;
  }
  h1 { color: #0f172a; }
  h2 { color: #2563eb; }
  footer { font-size: 0.75rem; color: #64748b; }
---

# AWS Certified AI Practitioner (AIF-C01)
## Module 3: Applications of Foundation Models, RAG & Agents

**Instructor:** Mohamed Fakhruldeen  
**Track:** AI Practitioner (`AIF-C01`)  
**Exam Weight:** 28% (Highest Weighted Domain)  
**Repository:** `fakhruldeen/AWS`

---

# Domain 3 Blueprint Alignment

1. **FM Selection Criteria:** Latency, modality, token cost, context window.
2. **Prompt Engineering:** Zero-shot, few-shot, chain-of-thought, prompt caching.
3. **Retrieval-Augmented Generation (RAG):** Ingestion, chunking, Titan Embeddings v2, OpenSearch Serverless.
4. **Agentic AI & MCP:** Autonomous ReAct loops, Action Groups, Lambda, Model Context Protocol.
5. **Model Customization:** PEFT, LoRA, RLHF, DPO, Continued Pre-training.
6. **Model Evaluation:** ROUGE, BLEU, BERTScore, Perplexity, LLM-as-a-judge.

---

# Foundation Model Selection Criteria

| Dimension | Consideration | Exam Rule of Thumb |
|---|---|---|
| **Modality** | Text vs Image vs Multimodal | Use Nova Lite/Pro for charts/docs, Titan for images |
| **Latency** | Time to First Token (TTFT) | Nova Micro for sub-second classification |
| **Throughput** | Invocations per minute | On-demand vs Provisioned Throughput (Model Units) |
| **Cost** | Input / Output token price | Input caching saves up to 50% |
| **Context** | Window size (tokens) | Long context (200K+) for legal/contracts |

---

# Advanced Prompt Engineering

* **Zero-Shot:** No examples provided; relies on pre-trained parametric knowledge.
* **Few-Shot (In-Context Learning):** 2–5 structured input/output examples establish format and tone.
* **Chain-of-Thought (CoT):** *"Think step-by-step"* enables multi-hop reasoning and prevents arithmetic errors.
* **Prompt Caching:**
  * Freezes large static preambles (system instructions, documents) in GPU memory.
  * Reduces latency up to 80%, cuts token costs up to 50%.

---

# Retrieval-Augmented Generation (RAG) Architecture

* **The Core Problem:** Foundation models lack private enterprise data and have fixed knowledge cutoffs.
* **The Solution:** RAG retrieves authoritative context dynamically and appends it to the prompt.
* **AWS Bedrock Knowledge Bases Workflow:**
  1. Ingest raw PDFs/Word docs from **Amazon S3**.
  2. Parse & chunk (fixed, semantic, or hierarchical).
  3. Generate dense vectors with **Titan Text Embeddings v2**.
  4. Store in **Amazon OpenSearch Serverless** vector index.
  5. Search via k-NN and synthesize answer with source citations.

---

# Autonomous Agents & Model Context Protocol (MCP)

* **Bedrock AgentCore:**
  * Uses ReAct framework (*Reason + Act + Observe*).
  * Decomposes user goal into sequential tool invocations.
* **Action Groups:**
  * Connects agent reasoning to execution via **AWS Lambda**.
  * Parameter contracts validated via **OpenAPI 3.0 schemas**.
* **Model Context Protocol (MCP):**
  * Universal open standard for connecting agents to external databases and dev tools over JSON-RPC 2.0.

---

# The Customization Spectrum

```
[Prompt Engineering]  -->  [RAG Knowledge Base]  -->  [PEFT / LoRA]  -->  [Pre-Training]
- Zero training data       - Private S3 data          - Custom style/tone       - Billions of tokens
- $0 training cost         - Dynamic lookup           - Updates <1% weights    - Millions $ compute
- Minutes                  - Hours                    - Days                    - Months
```

* **Catastrophic Forgetting:** Risk when fine-tuning a model alters its base weights, erasing prior reasoning.
* **LoRA (Low-Rank Adaptation):** Freezes base weights and trains lightweight adapter matrices.

---

# Foundation Model Evaluation Metrics

1. **BLEU (Bilingual Evaluation Understudy):**
   * Measures $n$-gram precision against reference text (standard for Translation).
2. **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):**
   * Measures $n$-gram recall (ROUGE-1, ROUGE-2, ROUGE-L) (standard for Summarization).
3. **BERTScore:**
   * Contextual embedding semantic similarity (captures synonyms).
4. **LLM-as-a-Judge (v1.2 Addition):**
   * Frontier model (Nova Pro / Claude 3.5) evaluates smaller models on a scoring rubric.

---

# Key Takeaways & Exam Traps

* ⚡ **Private Data without Retraining?** $\rightarrow$ Always **RAG (Bedrock Knowledge Bases)**.
* ⚡ **Tone & Style Customization?** $\rightarrow$ **Fine-Tuning / PEFT (LoRA)**.
* ⚡ **Evaluating Summarization Recall?** $\rightarrow$ **ROUGE**.
* ⚡ **Predictable Sub-Second Peak Throughput?** $\rightarrow$ **Provisioned Throughput (Model Units)**.

---

# Module 3 Student Review Quiz

1. **An enterprise wants to customize an open-source Large Language Model for a customer support domain with minimal GPU memory overhead and without retraining all billions of parameters. Which technique should they select?**
   * A) Full Pre-training from scratch
   * B) Low-Rank Adaptation (LoRA / PEFT) *(Correct — freezes base model weights and trains small adapter matrices)*
   * C) Zero-Shot Prompting
   * D) Retrieval-Augmented Generation only

2. **Which prompt engineering technique explicitly instructs a Large Language Model to break down complex multi-step arithmetic or logic problems into sequential reasoning steps before generating the final answer?**
   * A) Few-Shot In-Context Prompting
   * B) Chain-of-Thought (CoT) Prompting *(Correct — "Think step-by-step")*
   * C) Directional Stimulus Prompting
   * D) System Persona Prompting

3. **An insurance company needs an AI assistant that can autonomously look up policy details, check weather records via an API, and file claims in a PostgreSQL database. Which Amazon Bedrock feature coordinates this multi-step execution?**
   * A) Amazon Bedrock Guardrails
   * B) Amazon Bedrock Agents with Action Groups *(Correct — breaks tasks into steps and invokes AWS Lambda APIs)*
   * C) Amazon Bedrock Model Evaluation
   * D) Amazon Bedrock Watermarking

