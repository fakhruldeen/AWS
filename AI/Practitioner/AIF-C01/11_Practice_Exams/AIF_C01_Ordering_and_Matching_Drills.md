# 🧩 AWS Certified AI Practitioner (`AIF-C01`) — Official Ordering & Matching Question Drills

> **Why This Drill Matters:** Unlike `CLF-C02`, the official `AIF-C01` Exam Guide v1.2 explicitly tests **four** question types: Multiple Choice, Multiple Response, **Ordering (3–5 steps)**, and **Matching (3–7 prompts)**. You must order or match **all items correctly** to receive credit (no partial credit).

---

## Part 1: Ordering Drills (10 Questions — 3 to 5 Steps Each)

### Order 01 — End-to-End Machine Learning Lifecycle (Domain 1)
Place the following 5 stages of a traditional ML development lifecycle in the correct chronological order:
- `[A]` Deploy the model to a production SageMaker endpoint and monitor for drift
- `[B]` Define the business problem and confirm ML is the right approach
- `[C]` Train candidate algorithms and tune hyperparameters on training data
- `[D]` Collect, clean, label, and engineer features from raw datasets
- `[E]` Evaluate model performance on a held-out test set using Precision/Recall or RMSE

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → C → E → A`  
**Rationale:** Always start by framing the business problem (`B`), prepare and clean data (`D`), train the model (`C`), evaluate on unseen test data (`E`), and finally deploy and monitor (`A`).
</details>

---

### Order 02 — Enterprise RAG Ingestion & Query Pipeline (Domain 3)
Order the 5 steps of an `Amazon Bedrock Knowledge Bases` RAG pipeline from document upload to grounded answer:
- `[A]` Convert document chunks into dense vector embeddings using an embedding model
- `[B]` Retrieve the top-K most semantically similar chunks for the user's query
- `[C]` Split source PDFs stored in Amazon S3 into manageable overlapping chunks
- `[D]` Store embeddings and metadata inside Amazon OpenSearch Serverless
- `[E]` Augment the user prompt with retrieved chunks and generate a cited response with an FM

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `C → A → D → B → E`  
**Rationale:** Ingestion chunks documents (`C`), embeds chunks (`A`), and indexes vectors (`D`). At query time, the system retrieves relevant chunks (`B`) and augments the FM prompt to generate a grounded response (`E`).
</details>

---

### Order 03 — FM Customization Escalation Ladder (Lowest to Highest Cost & Effort) (Domain 3)
Order the 5 Foundation Model adaptation approaches from **lowest** upfront cost/effort to **highest**:
- `[A]` Continued Pre-Training on massive unlabeled domain corpora
- `[B]` Prompt Engineering / In-Context Learning (Zero-Shot / Few-Shot)
- `[C]` Pre-Training a new Foundation Model from scratch
- `[D]` Retrieval-Augmented Generation (`RAG`) with a vector database
- `[E]` Instruction Fine-Tuning (`PEFT` / `LoRA`) on labeled prompt-response pairs

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → E → A → C`  
**Rationale:** Always escalate from zero-training Prompting (`B`) → dynamic knowledge via RAG (`D`) → task/style adaptation via Fine-Tuning (`E`) → domain corpus absorption via Continued Pre-Training (`A`) → Pre-Training from scratch (`C`).
</details>

---

### Order 04 — Amazon Bedrock Model Distillation Workflow (Domain 3 — v1.2)
Order the 4 steps of distilling a large Foundation Model into a faster, lower-cost production model:
- `[A]` Deploy the distilled Student model to serve high-volume production traffic at lower latency
- `[B]` Supply representative production prompts from your specific use case
- `[C]` Fine-tune a smaller Student model (e.g., `Nova Micro`) on the Teacher's generated outputs
- `[D]` Generate high-accuracy synthetic responses using a large Teacher model (e.g., `Nova Pro`)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → C → A`  
**Rationale:** Distillation starts with domain prompts (`B`), uses the Teacher FM to generate high-quality outputs (`D`), trains the compact Student FM (`C`), and deploys the Student for low-latency, low-cost inference (`A`).
</details>

---

### Order 05 — Secure Agentic AI Execution Flow with AgentCore & MCP (Domain 2 & 5 — v1.2)
Order the 4 steps when an enterprise user asks an `Amazon Bedrock AgentCore` agent to look up an order and issue a refund:
- `[A]` `Policy in AgentCore` deterministically evaluates whether the tool invocation is allowed
- `[B]` The FM reasons over the prompt + `AgentCore Memory` and selects an `MCP` tool call
- `[C]` The tool executes via `AgentCore Gateway` using scoped credentials from `AgentCore Identity`
- `[D]` The agent incorporates the tool result into context and returns the verified response to the user

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → A → C → D`  
**Rationale:** First the FM plans the tool call (`B`), `Policy in AgentCore` enforces deterministic allow/forbid rules before execution (`A`), `AgentCore Gateway` + `Identity` execute the authorized action (`C`), and the agent synthesizes the final reply (`D`).
</details>

---

### Order 06 — Bedrock Guardrails Runtime Inspection Flow (Domain 4)
Order the 4 stages of how `Amazon Bedrock Guardrails` protects a RAG application at runtime:
- `[A]` Inspect the FM's draft output for toxicity, PII leakage, and Contextual Grounding against RAG sources
- `[B]` Inspect the incoming user prompt for Denied Topics, Prompt Attacks, and PII
- `[C]` Deliver the validated/masked response to the end user (or return a blocked message)
- `[D]` Forward the clean prompt + retrieved RAG context to the Foundation Model

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → A → C`  
**Rationale:** Guardrails evaluate inputs first (`B`), pass clean inputs to the FM (`D`), evaluate generated outputs + contextual grounding (`A`), and deliver only safe, grounded outputs (`C`).
</details>

---

### Order 07 — Securing S3 Data Before ML Training (Domain 5)
Order the 4 steps to prepare and govern a sensitive S3 dataset before training a custom model:
- `[A]` Enable `SSE-KMS` encryption and least-privilege `IAM` / `Lake Formation` access controls
- `[B]` Scan raw S3 buckets with `Amazon Macie` to discover unmasked PII
- `[C]` Document data origins, lineage, and intended use inside `Amazon SageMaker Model Cards`
- `[D]` Clean, anonymize, and redact detected PII using `AWS Glue DataBrew` or `SageMaker Data Wrangler`

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → A → C`  
**Rationale:** Discover PII (`B`), redact/clean it (`D`), lock down encryption and access controls (`A`), and document provenance/governance in Model Cards (`C`).
</details>

---

### Order 08 — Foundation Model Lifecycle (Task Statement 2.1)
Order the 5 major phases of the Foundation Model lifecycle:
- `[A]` Evaluation against benchmarks, `LLM-as-a-judge`, and human-in-the-loop reviews
- `[B]` Data selection and curation of massive multi-source corpora
- `[C]` Deployment to production and continuous feedback monitoring
- `[D]` Pre-training the base model via self-supervised learning
- `[E]` Fine-tuning and alignment (`RLHF`) for instruction following and safety

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → E → A → C`  
**Rationale:** Data selection (`B`) → Pre-training (`D`) → Fine-tuning/RLHF (`E`) → Evaluation (`A`) → Deployment & feedback (`C`).
</details>

---

### Order 09 — Detecting and Mitigating Bias with SageMaker Clarify (Domain 4)
Order the 4 steps to audit and remediate bias in a tabular credit-scoring model:
- `[A]` Run post-training bias analysis (`Disparate Impact`) and `SHAP` explainability on the trained model
- `[B]` Run pre-training bias detection (`Class Imbalance`) on the raw training dataset
- `[C]` Rebalance/curate the dataset and retrain the model to reduce demographic disparity
- `[D]` Record fairness metrics, limitations, and risk ratings in `SageMaker Model Cards`

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → A → C → D`  
**Rationale:** Check dataset bias first (`B`), measure trained model bias & SHAP attribution (`A`), remediate/retrain (`C`), and document governance evidence in Model Cards (`D`).
</details>

---

### Order 10 — Spec-Driven Agentic Development with Kiro (Domain 1 & 2 — v1.2)
Order the 4 stages of a spec-driven software workflow in `Kiro`:
- `[A]` Execute modular implementation tasks with agent assistance
- `[B]` Capture natural-language product requirements and user stories
- `[C]` Run automated tests and verify code against acceptance criteria
- `[D]` Generate structured technical architecture and design specifications

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Order:** `B → D → A → C`  
**Rationale:** `Kiro` structures agentic engineering from requirements (`B`) → design specs (`D`) → task-by-task implementation (`A`) → verification (`C`).
</details>

---

## Part 2: Matching Drills (10 Questions — 4 to 6 Pairs Each)

### Match 01 — AWS Managed AI Services to Use Cases (Domain 1)
Match each AWS service (`1–6`) to its primary capability (`A–F`):
1. `Amazon Textract`
2. `Amazon Comprehend`
3. `Amazon Rekognition`
4. `Amazon Transcribe`
5. `Amazon Polly`
6. `Amazon Personalize`

- **A.** Convert customer support call recordings into searchable text transcripts
- **B.** Extract structured key-value form fields and tables from scanned PDF invoices
- **C.** Detect customer sentiment, named entities, and key phrases in product reviews
- **D.** Generate lifelike spoken audio narration from written text
- **E.** Deliver real-time individualized product recommendations on an e-commerce site
- **F.** Moderate unsafe images and detect objects/faces in uploaded videos

<details><summary><b>View Answer</b></summary>

`1 → B`, `2 → C`, `3 → F`, `4 → A`, `5 → D`, `6 → E`
</details>

---

### Match 02 — SageMaker Inference Modes to Workload Patterns (Domain 1)
Match each deployment option (`1–4`) to the ideal scenario (`A–D`):
1. `Real-Time Inference`
2. `Serverless Inference`
3. `Asynchronous Inference`
4. `Batch Transform`

- **A.** Overnight scoring of 10 million customer records stored in Amazon S3
- **B.** Processing 500 MB medical imaging payloads taking 15 minutes each
- **C.** Fraud-scoring API requiring sub-100ms latency under steady 24/7 traffic
- **D.** Internal HR tool with sporadic traffic that should scale to zero when idle

<details><summary><b>View Answer</b></summary>

`1 → C`, `2 → D`, `3 → B`, `4 → A`
</details>

---

### Match 03 — GenAI Evaluation Metrics to Best Use Cases (Domain 3 — v1.2)
Match each metric (`1–5`) to its primary evaluation strength (`A–E`):
1. `ROUGE`
2. `BLEU`
3. `BERTScore`
4. `Perplexity`
5. `LLM-as-a-Judge`

- **A.** Measures precision-oriented n-gram overlap for machine translation
- **B.** Evaluates open-ended helpfulness, tone, and faithfulness at scale using an evaluator FM
- **C.** Measures recall-oriented n-gram overlap for text summarization
- **D.** Measures how well a language model predicts next tokens (lower is better)
- **E.** Uses contextual embeddings to measure semantic similarity across paraphrases

<details><summary><b>View Answer</b></summary>

`1 → C`, `2 → A`, `3 → E`, `4 → D`, `5 → B`
</details>

---

### Match 04 — AWS v1.2 GenAI & Agentic Services to Roles (Domain 2 — v1.2)
Match each AWS offering (`1–5`) to its exact role (`A–E`):
1. `Strands Agents`
2. `Amazon Bedrock AgentCore`
3. `Kiro`
4. `Amazon Quick`
5. `AWS Transform`

- **A.** Agentic AI service automating enterprise modernization of legacy `.NET`, `Java`, and `Mainframe` apps
- **B.** Open-source AWS model-driven Python SDK for building multi-agent apps with `MCP`
- **C.** Unified AI-powered BI, natural-language analytics, and enterprise workflow workspace
- **D.** Serverless enterprise runtime, memory, identity, policy, and gateway platform for production agents
- **E.** Agentic AI IDE for spec-driven software development

<details><summary><b>View Answer</b></summary>

`1 → B`, `2 → D`, `3 → E`, `4 → C`, `5 → A`
</details>

---

### Match 05 — AWS Vector Databases to Architectural Requirements (Domain 3)
Match each AWS database (`1–4`) to the best RAG vector storage scenario (`A–D`):
1. `Amazon OpenSearch Serverless`
2. `Amazon Aurora PostgreSQL (pgvector)`
3. `Amazon Neptune`
4. `Amazon DocumentDB`

- **A.** GraphRAG combining vector search with complex multi-hop entity relationship traversal
- **B.** Default fully managed, auto-scaling serverless vector engine for Bedrock Knowledge Bases
- **C.** Storing embeddings alongside existing high-availability relational PostgreSQL data
- **D.** Storing JSON documents and vector embeddings for MongoDB-compatible applications

<details><summary><b>View Answer</b></summary>

`1 → B`, `2 → C`, `3 → A`, `4 → D`
</details>

---

### Match 06 — Prompt Engineering Techniques to Scenarios (Domain 3)
Match each technique (`1–5`) to the matching prompt pattern (`A–E`):
1. `Zero-Shot Prompting`
2. `Few-Shot Prompting`
3. `Chain-of-Thought (CoT)`
4. `Negative Prompting`
5. `Prompt Caching`

- **A.** Instructing an image model: *"Avoid blurry edges, watermarks, or extra fingers"*
- **B.** Providing 3 labeled input→output examples to enforce a strict JSON classification format
- **C.** Adding *"Think step by step and show your calculations"* for multi-step math logic
- **D.** Asking the FM to summarize a paragraph with no examples provided
- **E.** Reusing a static 15,000-token reference manual prefix across repeated API calls to cut cost & latency

<details><summary><b>View Answer</b></summary>

`1 → D`, `2 → B`, `3 → C`, `4 → A`, `5 → E`
</details>

---

### Match 07 — Responsible AI & Governance Tools to Functions (Domain 4)
Match each AWS feature (`1–4`) to its primary responsibility (`A–D`):
1. `Amazon Bedrock Guardrails`
2. `Amazon SageMaker Clarify`
3. `Amazon SageMaker Model Cards`
4. `Amazon SageMaker Model Monitor`

- **A.** Standardized governance record documenting intended use, risk rating, and evaluation metrics
- **B.** Runtime filtering of Denied Topics, PII, prompt attacks, and ungrounded hallucinations
- **C.** Continuous production tracking of live data quality and prediction drift over time
- **D.** Pre/post-training bias detection (`Class Imbalance`, `Disparate Impact`) and `SHAP` explainability

<details><summary><b>View Answer</b></summary>

`1 → B`, `2 → D`, `3 → A`, `4 → C`
</details>

---

### Match 08 — Security & Compliance Services for AI Systems (Domain 5)
Match each service (`1–5`) to its AI security/governance function (`A–E`):
1. `Amazon Macie`
2. `AWS PrivateLink`
3. `AWS Artifact`
4. `AWS CloudTrail`
5. `AWS Config`

- **A.** Keep Bedrock and SageMaker API traffic off the public internet via Interface VPC Endpoints
- **B.** Download third-party `SOC`, `ISO`, and `HIPAA` compliance reports and agreements
- **C.** Automatically discover and classify PII stored in Amazon S3 training buckets
- **D.** Track continuous resource configuration history and evaluate compliance rules
- **E.** Record an immutable audit trail of all AWS API calls made by users and roles

<details><summary><b>View Answer</b></summary>

`1 → C`, `2 → A`, `3 → B`, `4 → E`, `5 → D`
</details>

---

### Match 09 — Generative AI Security Scoping Matrix (Domain 5)
Match each Scope (`1–5`) to the corresponding AI adoption pattern (`A–E`):
1. `Scope 1`
2. `Scope 2`
3. `Scope 3`
4. `Scope 4`
5. `Scope 5`

- **A.** Pre-training a proprietary Foundation Model from scratch on self-managed GPU clusters
- **B.** Employees using public third-party consumer GenAI websites (governed by Acceptable Use Policy)
- **C.** Building custom apps over pre-trained FMs via API (`Amazon Bedrock` + RAG)
- **D.** Enterprise SaaS AI assistants integrated with corporate SSO/IAM (`Amazon Quick`, `Kiro`)
- **E.** Fine-tuning or continued pre-training of FMs using proprietary enterprise datasets

<details><summary><b>View Answer</b></summary>

`1 → B`, `2 → D`, `3 → C`, `4 → E`, `5 → A`
</details>

---

### Match 10 — Classification Metrics to Business Priorities (Domain 1)
Match each metric (`1–4`) to the right real-world scenario (`A–D`):
1. `High Recall`
2. `High Precision`
3. `F1 Score`
4. `RMSE`

- **A.** Spam filter where blocking a legitimate executive email (False Positive) is unacceptable
- **B.** Cancer screening where missing a sick patient (False Negative) is life-threatening
- **C.** Evaluating a fraud classifier on a heavily imbalanced dataset (99.5% legitimate, 0.5% fraud)
- **D.** Predicting continuous house prices while heavily penalizing large prediction errors

<details><summary><b>View Answer</b></summary>

`1 → B`, `2 → A`, `3 → C`, `4 → D`
</details>
