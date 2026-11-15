# AIF-C01 Exam Distinction & Memory Cheat Sheet

> **Certification:** [[AIF-C01_Master_Blueprint|AWS Certified AI Practitioner (AIF-C01)]]  
> **Purpose:** High-yield side-by-side distinction tables to eliminate confusion on tricky exam questions.  
> **Tags:** `#aws/certification` `#aif-c01` `#cheatsheet` `#exam-prep`

---

## 1. Model Adaptation Spectrum: Prompting vs. RAG vs. Fine-Tuning

| Feature | Prompt Engineering | RAG (Bedrock Knowledge Bases) | Fine-Tuning (Custom Models) | Continued Pre-training |
|---|---|---|---|---|
| **Base Model Weights** | Unchanged (Frozen) | Unchanged (Frozen) | **Updated** (Adapters or weights) | **Updated** (Base weights) |
| **Knowledge Source** | Context provided in prompt | Dynamic retrieval from Vector DB | Baked into model weights | Baked into model weights |
| **Knowledge Freshness** | Frozen at model cutoff | **Real-time / Instant** | Frozen at training time | Frozen at training time |
| **Provides Citations?** | No (unless in prompt) | **Yes (Direct source links)** | No | No |
| **Hallucination Risk** | High | **Lowest (Grounded)** | Moderate | Moderate |
| **Typical Data Required** | $0 - 5$ prompt examples | Internal docs (PDF, HTML, TXT) | $100s - 10,000s$ labeled pairs | Millions of unlabeled tokens |
| **Cost & Compute** | Lowest ($\$$) | Low-Moderate ($\$\$$) | Moderate-High ($\$\$\$$) | Very High ($\$\$\$\$$) |

---

## 2. Generative AI Evaluation Metrics Comparison

| Metric | Full Name | Primary Task | Metric Focus | Direction | When to Choose |
|---|---|---|---|---|---|
| **ROUGE-1 / 2** | Recall-Oriented Understudy for Gisting Evaluation | **Text Summarization** | **Recall** ($n$-gram overlap) | Higher is better ($0 - 1$) | Evaluating whether a summary captured key points from source. |
| **ROUGE-L** | ROUGE Longest Common Subsequence | Summarization fluency | Sentence structure & order | Higher is better ($0 - 1$) | Evaluating sentence flow and structural order of summary. |
| **BLEU** | Bilingual Evaluation Understudy | **Machine Translation** | **Precision** + Brevity Penalty | Higher is better ($0 - 1$) | Checking translation accuracy against ground truth sentences. |
| **BERTScore** | BERT Semantic Score | Open-ended text, synonyms | **Semantic Cosine Similarity** | Higher is better ($0 - 1$) | Words differ in phrasing/synonyms but share exact meaning. |
| **Perplexity (PPL)** | Perplexity | Language model fluency | Uncertainty / entropy | **Lower is better** ($1 - \infty$) | Evaluating grammatical fluency and predictability of model output. |

---

## 3. SageMaker Model Deployment Modes

| Mode | Traffic Pattern | Scalability | Max Payload | Max Latency / Duration | Billing Model |
|---|---|---|---|---|---|
| **Real-Time** | Sustained, steady, high volume | Auto-scales instances based on CPU/Inv. | 6 MB | Sub-second (up to 60s) | Billed 24/7 per active instance-hour |
| **Serverless** | Sporadic, spiky, unpredictable | Scales down to **0** when idle | 4 MB | Up to 60s (has cold starts) | Billed per compute second used |
| **Batch Transform** | Bulk offline datasets (periodic) | Runs job and shuts down compute | Gigabytes (splits S3 files) | Hours to Days | Billed only for duration of transform job |
| **Asynchronous** | Large files, long-running processing | Queues requests in Amazon SQS | **1 GB** | **Up to 1 hour** (60 mins) | Scales to zero when SQS queue is empty |

---

## 4. Temperature vs. Top-P vs. Top-K

| Parameter | What it Does | Low Value Example | High Value Example | Best For |
|---|---|---|---|---|
| **Temperature** | Flattens or sharpens token probability curve | `0.0`: Greedy, deterministic | `1.0`: Broad, creative, varied | `0.0` for coding/JSON/facts; `0.8` for brainstorming |
| **Top-P (Nucleus)** | Restricts pool to cumulative probability $P$ | `0.1`: Only top 1-2 words | `0.95`: Includes long-tail words | Alternative to Temperature; tune one or the other |
| **Top-K** | Caps pool to top $K$ most probable tokens | `1`: Greedy decoding | `250`: Rich vocabulary | Restricting candidate tokens to fixed top count |

---

## 5. Amazon Bedrock vs. Amazon SageMaker AI

| Dimension | Amazon Bedrock | Amazon SageMaker AI |
|---|---|---|
| **Target User** | App developers building with GenAI via APIs | Data scientists, ML engineers building custom models |
| **Model Nature** | Ready-to-use Foundation Models (Claude, Titan, Llama) | Custom models (PyTorch, TensorFlow, XGBoost, Scikit) |
| **Infrastructure** | **Serverless** (No servers or GPUs to configure) | Managed compute (EC2 ML instances, clusters, containers) |
| **Customization** | RAG (Knowledge Bases), Fine-tuning (Serverless) | Full training scripts, custom hyperparameter tuning, containers |
| **ML Code** | **Zero ML code**; simple REST/SDK calls | Full Python/Jupyter scripting, MLOps pipelines |

---

## 6. Amazon Q Family Cheat Sheet

| Service | Primary User | Core Capability | Key Feature |
|---|---|---|---|
| **Amazon Q Developer** | Software developers, Cloud architects | AI pair programming in IDE/CLI, code modernization | Migrates **Java 8/11 to Java 17**; security vulnerability scanning |
| **Amazon Q Business** | Corporate business employees | Enterprise question answering across 40+ connectors | Strict Role-Based Access Control (**RBAC**); source citations |
| **Amazon Q in QuickSight** | Business intelligence analysts | Natural language to BI dashboards and reports | Generates executive summaries and charts from prompt |
| **Amazon Q in AWS Glue** | Data engineers | Natural language to ETL pipeline code | Generates PySpark transformations via conversation |

---

## 7. Responsible AI & Governance Tooling

| Capability | AWS Tool | Primary Function | Exam Trigger |
|---|---|---|---|
| **Pre-Training Bias** | SageMaker Clarify | Analyzes raw data for class imbalance | *"Detect demographic bias in training data before modeling"* |
| **Post-Training Bias** | SageMaker Clarify | Analyzes predictions for disparate impact | *"Measure fairness of loan approval predictions across groups"* |
| **Explainability (SHAP)** | SageMaker Clarify | Computes feature attribution scores | *"Explain which features caused a model to reject an application"* |
| **GenAI Safety & PII** | Bedrock Guardrails | Filters toxicity, masks PII, blocks topics | *"Redact customer SSNs and block investment advice in chatbot"* |
| **Hallucination Suppression** | Bedrock Guardrails | Contextual Grounding Check | *"Ensure chatbot answers only come from retrieved reference docs"* |
| **Model Documentation** | SageMaker Model Cards | Auditable PDF record of model lifecycle | *"Produce standardized compliance documentation for auditors"* |
| **Model Drift Monitoring** | SageMaker Model Monitor | Detects data and concept drift in production | *"Alert when production inference inputs deviate from training data"* |
