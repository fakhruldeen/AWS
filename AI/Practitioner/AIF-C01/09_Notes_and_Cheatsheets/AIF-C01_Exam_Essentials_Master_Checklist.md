# ✅ AWS Certified AI Practitioner (`AIF-C01`) — Exam Essentials Master Checklist (`v1.2`)

> **Purpose:** High-yield, domain-by-domain readiness checklist synthesizing all core concepts from the **Official AIF-C01 Exam Guide v1.2 (October 29, 2026)** and foundational AI/ML engineering principles. Review every checkbox before sitting the real exam.

---

## Domain 1: Fundamentals of AI and ML (`20%`)
- [ ] **Distinguish the AI Hierarchy:** `AI` (includes rule-based systems) ⊃ `ML` (learns from data) ⊃ `Deep Learning` (multi-layer neural networks) ⊃ `GenAI` (creates new content) & `Agentic AI` (plans + uses memory & `MCP` tools).
- [ ] **Know Neural Network Specializations:** `CNN` (computer vision/images), `RNN`/`LSTM` (sequential/time-series), `GAN` (generator vs. discriminator synthetic generation), `VAE` (latent-space generation), `Transformer` (self-attention parallel sequence modeling), `Diffusion` (iterative denoising for images/video).
- [ ] **Parameters vs. Hyperparameters & Backpropagation:** Parameters (weights) are learned during training via backpropagation; Hyperparameters (learning rate, epochs, batch size) are set before training.
- [ ] **Match Learning Paradigms:** `Supervised` (labeled → Classification / Regression), `Unsupervised` (unlabeled → Clustering `k-means`, Dimensionality Reduction `PCA`, Anomaly Detection), `Reinforcement Learning` (agent + environment + rewards/penalties, `RLHF`), `Self-Supervised` (next-token pre-training of LLMs).
- [ ] **Know When NOT to Use ML:** Deterministic rules requiring 100% exact outcomes (e.g., tax/regulatory formulas) or poor ROI → use traditional rule-based code or `RPA`.
- [ ] **Diagnose Fit & Drift:** `Overfitting` (high variance → add data, regularize, simplify) vs. `Underfitting` (high bias → more features, train longer); `Data Drift` vs. `Concept Drift` (monitored by `SageMaker Model Monitor`).
- [ ] **Select the Right SageMaker Inference Mode:** `Real-Time` (low latency, ≤ 25 MB), `Serverless` (intermittent, scales to zero, ≤ 4 MB), `Asynchronous` (large payloads ≤ 1 GB, up to 1 hr), `Batch Transform` (offline bulk S3 scoring).
- [ ] **Master Managed AWS AI APIs:** `Rekognition` (vision), `Textract` (OCR + forms/tables), `Comprehend` (NLP sentiment/entities/PII), `Transcribe` (STT), `Polly` (TTS), `Translate` (translation), `Lex` (chatbots), `Personalize` (recommendations).
- [ ] **Distinguish Technical vs. Business Metrics:** Classification (`Precision`, `Recall`, `F1`, `ROC-AUC`), Regression (`MAE`, `MSE`, `RMSE`, `R²`), Business (`ROI`, cost per user, development cost, customer satisfaction).

---

## Domain 2: Fundamentals of Generative AI (`24%`)
- [ ] **Explain Core GenAI Mechanics:** `Tokens` (~¾ word, drive context limits & billing), `Chunking`, `Embeddings` (dense semantic vectors), `Self-Attention`, `Context Window`, and `Multimodal` models.
- [ ] **Differentiate Prompt Engineering vs. Context Engineering (`v1.2`):** Context engineering manages the *entire runtime context window* (system prompt + RAG passages + short/long-term memory + tool definitions/outputs) within token budgets.
- [ ] **Master Agentic AI & `MCP` (`v1.2`):** `Model Context Protocol (MCP)` standardizes connecting agents to external tools/APIs; know multi-agent orchestration (supervisor, handoffs, memory management).
- [ ] **Know AWS GenAI & Agentic Stack (`v1.2`):** `Amazon Bedrock` (serverless FM API), `Amazon Nova` (`Micro`/`Lite`/`Pro`/`Canvas`/`Reel`), `Amazon Bedrock AgentCore` (`Runtime`, `Memory`, `Gateway`, `Identity`, `Policy`, `Observability`), `Strands Agents` (open-source model-driven agent SDK), `Kiro` (spec-driven agentic IDE), `Amazon Quick` (AI BI & enterprise workflows), `AWS Transform` (agentic legacy modernization), `SageMaker JumpStart` (dedicated-infra open-weight FM hosting).
- [ ] **Understand GenAI Limitations & Pricing:** `Hallucinations`, `Nondeterminism`, black-box `Interpretability`, stale cutoffs; `On-Demand` (per-token) vs. `Batch Inference` (offline discount) vs. `Provisioned Throughput` (hourly Model Units — required for custom fine-tuned models & guaranteed throughput).

---

## Domain 3: Applications of Foundation Models (`28%` — Highest Weight)
- [ ] **Tune Inference Parameters:** Low `Temperature` (`0.0–0.2`) = factual/deterministic; High `Temperature` (`0.7–1.0`) = creative; `Top-P` (cumulative probability nucleus); `Top-K` (top K tokens); `Max Tokens` & `Stop Sequences`.
- [ ] **Architect Enterprise `RAG`:** `Amazon Bedrock Knowledge Bases` grounds FMs in fresh proprietary data with citations and zero retraining; AWS vector stores = `OpenSearch Serverless`, `Aurora` (`pgvector`), `RDS for PostgreSQL` (`pgvector`), `Neptune` (`GraphRAG`), `DocumentDB`.
- [ ] **Climb the FM Customization Ladder (Cost & Effort):** Prompting → `RAG` → **`Model Distillation`** (Teacher FM → small fast Student FM) → Instruction Fine-Tuning / `PEFT` (`LoRA`) (labeled pairs for style/format) → Continued Pre-Training (massive unlabeled domain text) → Pre-Training from scratch.
- [ ] **Apply `Prompt Caching` & `Prompt Management` (`v1.2`):** `Prompt Caching` caches static prompt prefixes to cut latency and input token cost; `Bedrock Prompt Management` versions, tests, and rolls out prompt templates across environments.
- [ ] **Master Prompt Techniques & Attacks:** `Zero-Shot`, `Single-Shot`, `Few-Shot`, `Chain-of-Thought (CoT)`, `Negative Prompts`; mitigate `Prompt Injection / Hijacking`, `Prompt Leaking / Exposure`, `Jailbreaking`, and `Data/Model Poisoning`.
- [ ] **Select FM Evaluation Metrics (`v1.2`):** `ROUGE` (summarization recall), `BLEU` (translation precision), `BERTScore` (semantic embedding similarity), `Perplexity` (lower is better), `LLM-as-a-Judge` (scalable open-ended scoring in `Bedrock Model Evaluation`), `Human-in-the-Loop (HITL)`, plus business metrics (`Task Completion Rate`, `User Satisfaction`, `Cost per Interaction`).

---

## Domain 4: Guidelines for Responsible AI (`14%`)
- [ ] **Know All Responsible AI Dimensions:** `Fairness`, `Explainability`, `Privacy & Security`, `Safety`, `Controllability`, `Veracity & Robustness`, `Governance`, `Transparency`.
- [ ] **Distinguish AWS Responsible AI Tools:**
  - `Amazon Bedrock Guardrails`: **Runtime** filtering (Content Filters, Denied Topics, PII Redaction, Word Filters, Contextual Grounding Check).
  - `Amazon SageMaker Clarify`: **Pre-training** (`Class Imbalance`) & **Post-training** (`Disparate Impact`) bias detection + **`SHAP`** feature attribution explainability.
  - `Amazon SageMaker Model Cards`: Standardized transparency & governance documentation.
  - `Amazon SageMaker Model Dashboard`: Centralized drift, bias, and quality visibility.
- [ ] **Address Sustainability, Legal Risks & Human-Centered Design:** Right-sized/distilled models (`Nova Micro`), `Prompt Caching`, `Trainium`/`Inferentia` reduce carbon footprint; watch for `IP/Copyright` risks and demographic subgroup bias; design transparent explanations with user-feedback loops.

---

## Domain 5: Security, Compliance & Governance for AI (`14%`)
- [ ] **Apply Shared Responsibility & Defense in Depth:** Customer prompts/data in `Amazon Bedrock` are **never** used to train base FMs; layer `IAM` least privilege, `KMS` encryption at rest, `TLS` in transit, `AWS PrivateLink` (no public internet), `Amazon Macie` (discover PII in S3), and `Bedrock Model Invocation Logging`.
- [ ] **Secure Autonomous Agents (`v1.2`):** Use **`Amazon Bedrock AgentCore Identity`** for scoped OAuth/IAM delegation and **`Policy in AgentCore`** for deterministic allow/forbid checks before tool execution.
- [ ] **Master the Generative AI Security Scoping Matrix:** `Scope 1` (consumer web apps — AUP) → `Scope 2` (enterprise apps like `Amazon Quick`/`Kiro` — SSO/IAM) → `Scope 3` (pre-trained FMs via API like `Bedrock` + RAG) → `Scope 4` (fine-tuned FMs) → `Scope 5` (self-trained FMs from scratch).
- [ ] **Map Compliance & Governance Services:** `AWS Artifact` (`SOC`/`ISO`/`HIPAA` reports), `AWS CloudTrail` (API audit logs), `AWS Config` (continuous configuration compliance), `Amazon Inspector` (CVE scanning for EC2/ECR/Lambda), `AWS Trusted Advisor` (best-practice & quota checks), `AWS Region` selection (**Data Residency**), and `Data Lineage` (`Glue Data Catalog` + `Model Cards`).
