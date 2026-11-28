# ⚡ AWS Certified AI Practitioner (`AIF-C01`) — Full-Course Quick Revision (Bullet Points Only)

> **Exam Specs (v1.2 — Oct 2026):** 65 Questions (50 scored + 15 unscored) • 90 mins (+30 mins free `ESL +30`) • Pass: `700 / 1000`  
> **Question Types:** Multiple Choice • Multiple Response • **Ordering** (3–5 steps) • **Matching** (3–7 pairs)

---

## 1️⃣ Domain 1: Fundamentals of AI and ML (`20%`)

### Core AI Hierarchy & Learning Paradigms
- **AI > ML > Deep Learning > GenAI / Agentic AI:**
  - **AI:** Broad field of machines mimicking human intelligence (includes rule-based systems).
  - **ML:** Algorithms that learn statistical patterns from data without explicit programming.
  - **Deep Learning (`DL`):** Multi-layer neural networks (`CNN` for vision, `RNN`/`Transformer` for sequences).
  - **Generative AI (`GenAI`):** Deep learning models (`FMs`/`LLMs`/`Diffusion`) that *create* new text, code, images, audio, or video.
  - **Agentic AI:** Autonomous FM-powered systems that reason, maintain memory, invoke external tools (`MCP`), and execute multi-step workflows.
- **Learning Paradigms:**
  - **Supervised Learning:** Labeled data → **Classification** (discrete labels: fraud/not fraud, spam) & **Regression** (continuous numbers: house price, revenue).
  - **Unsupervised Learning:** Unlabeled data → **Clustering** (`k-means`, customer segments), **Dimensionality Reduction** (`PCA`), **Anomaly Detection**.
  - **Reinforcement Learning (`RL`):** Agent interacts with environment, learns policy via **rewards & penalties** (robotics, games, `RLHF`).
  - **Self-Supervised Learning:** Creates labels from raw unlabeled text (next-token prediction) — used to pre-train `LLMs`.
- **Fit & Generalization:**
  - **Overfitting** (*High Variance, Low Bias*): Memorizes training noise, fails on test data → Fix: more data, simpler model, regularization, dropout, early stopping.
  - **Underfitting** (*High Bias, Low Variance*): Too simple to capture patterns → Fix: more features, deeper model, train longer.
- **When NOT to Use AI/ML:** Deterministic rules exist (100% exact outcome needed, e.g., tax formula), insufficient/poor-quality data, or cost exceeds business ROI.

### Inference Types & ML Lifecycle (`MLOps`)
- **4 SageMaker Inference Modes:**
  - **Real-Time:** Low-latency (`ms`), persistent HTTPS endpoint, steady traffic, payloads ≤ 25 MB, timeout ≤ 60s.
  - **Serverless:** Intermittent/unpredictable traffic, scales to zero (cold starts possible), payloads ≤ 4 MB.
  - **Asynchronous:** Large payloads (up to 1 GB) & long processing (up to 1 hour), internal queue, near-real-time.
  - **Batch Transform:** Offline bulk predictions on huge S3 datasets, no persistent endpoint.
- **ML Pipeline Stages:** Business Problem → Data Collection & Preparation (`AWS Glue`, `Glue DataBrew`, `SageMaker Data Wrangler`, `Ground Truth`) → Training (`SageMaker AI`) → Evaluation (`Confusion Matrix`, `F1`, `RMSE`) → Deployment → Monitoring & Retraining (`SageMaker Model Monitor`, `SageMaker Pipelines`).
- **Classification Metrics:**
  - **Precision** ($\frac{TP}{TP+FP}$): Minimize **False Positives** (spam filter, legal flags).
  - **Recall** ($\frac{TP}{TP+FN}$): Minimize **False Negatives** (cancer screening, fraud detection).
  - **F1 Score:** Harmonic mean of Precision & Recall (best for **imbalanced datasets**).
  - **ROC-AUC:** Measures classifier discrimination across all thresholds.
- **Regression Metrics:** `MAE` (robust to outliers), `RMSE` (penalizes large errors heavily), `R²` (variance explained).

### AWS Managed AI Services (Zero-ML-Expertise APIs)
- **[Amazon Rekognition](./AWS_AI_SERVICES_GLOSSARY.md#amazon-rekognition):** Computer vision — image/video object detection, facial analysis, content moderation.
- **[Amazon Textract](./AWS_AI_SERVICES_GLOSSARY.md#amazon-textract):** Smart OCR — extracts text, handwriting, **forms (key-value pairs), and tables** from scanned PDFs/images.
- **[Amazon Comprehend](./AWS_AI_SERVICES_GLOSSARY.md#amazon-comprehend):** NLP — sentiment analysis, entities, key phrases, language detection, PII redaction.
- **[Amazon Transcribe](./AWS_AI_SERVICES_GLOSSARY.md#amazon-transcribe):** Speech-to-Text (`STT`) with speaker diarization & call analytics.
- **[Amazon Polly](./AWS_AI_SERVICES_GLOSSARY.md#amazon-polly):** Text-to-Speech (`TTS`) with lifelike neural/generative voices.
- **[Amazon Translate](./AWS_AI_SERVICES_GLOSSARY.md#amazon-translate):** Neural machine translation across languages.
- **[Amazon Lex](./AWS_AI_SERVICES_GLOSSARY.md#amazon-lex):** Conversational voice/text chatbots (powers Alexa).
- **[Amazon Personalize](./AWS_AI_SERVICES_GLOSSARY.md#amazon-personalize):** Real-time product/content recommendations (same tech as Amazon.com).

---

## 2️⃣ Domain 2: Fundamentals of Generative AI (`24%`)

### Core GenAI Mechanics & Context Engineering
- **Tokens:** Sub-word text units (~¾ of an English word); billing and **context window** limits are measured in tokens.
- **Chunking:** Splitting large documents into overlapping passages for vector indexing and RAG retrieval.
- **Embeddings & Vectors:** Dense numerical arrays capturing semantic meaning; similar concepts have close vector distances (cosine similarity).
- **Transformers & Self-Attention:** Architecture weighing relationships between all tokens in parallel (enables long-range context and massive scaling).
- **Diffusion Models:** Generate images/video by iteratively denoising random Gaussian noise (e.g., `Amazon Nova Canvas`, Stability AI).
- **Context Engineering:** Systematically curating the **entire runtime context window** (system instructions + RAG chunks + short/long-term memory + tool outputs) within token budgets.
- **Agentic AI & `MCP`:**
  - **Model Context Protocol (`MCP`):** Open standard connecting AI agents/FMs to external tools, APIs, and enterprise data sources.
  - **Multi-Agent Patterns:** Supervisor/router, sequential handoffs, parallel swarms, shared memory, tool orchestration.

### GenAI Capabilities, Limitations & AWS Stack (v1.2)
- **Disadvantages / Risks:** **Hallucinations** (confident fabrication), **Nondeterminism** (varying outputs for identical inputs), **Interpretability** (black-box reasoning), stale training cutoff.
- **Core AWS GenAI Services:**
  - **[Amazon Bedrock](./AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock):** Serverless API for FMs (`Amazon Nova`, `Claude`, `Llama`, `Mistral`, `Titan`), `Knowledge Bases`, `Guardrails`, `Prompt Management`, `Model Evaluation`.
  - **[Amazon Nova](./AWS_AI_SERVICES_GLOSSARY.md#amazon-nova):** AWS-native FM family (`Nova Micro` text, `Nova Lite`/`Pro` multimodal, `Nova Canvas` image, `Nova Reel` video).
  - **[Amazon Bedrock AgentCore](./AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock-agentcore):** Serverless enterprise runtime for deploying, scaling, and securing AI agents (`Runtime`, `Memory`, `Gateway` for MCP, `Identity`, `Policy`, `Observability`).
  - **[Strands Agents](./AWS_AI_SERVICES_GLOSSARY.md#strands-agents):** Open-source AWS model-driven Python SDK for building single- and multi-agent apps with MCP tools.
  - **[Kiro](./AWS_AI_SERVICES_GLOSSARY.md#kiro):** AWS agentic AI IDE for **spec-driven development** (requirements → design specs → tasks → code).
  - **[Amazon Quick](./AWS_AI_SERVICES_GLOSSARY.md#amazon-quick):** Unified AI-powered BI, natural-language analytics, research, and enterprise workflow assistant.
  - **[AWS Transform](./AWS_AI_SERVICES_GLOSSARY.md#aws-transform):** Agentic AI service automating enterprise modernization of legacy `.NET`, `Java`, `VMware`, and `Mainframe` workloads.
  - **[Amazon SageMaker JumpStart](./AWS_AI_SERVICES_GLOSSARY.md#amazon-sagemaker-jumpstart):** Hub to deploy/fine-tune open-source FMs on dedicated SageMaker infrastructure when you need full infra control.
- **Bedrock Pricing Tradeoffs:**
  - **On-Demand:** Pay per input/output token — best for unpredictable/spiky workloads.
  - **Batch Inference:** Discounted offline processing for huge prompt datasets.
  - **Provisioned Throughput:** Hourly Model Unit (`MU`) commitment — required for **guaranteed high throughput** or **custom fine-tuned models**.

---

## 3️⃣ Domain 3: Applications of Foundation Models (`28%` — Highest Weight!)

### Inference Parameters & Design Considerations
- **Temperature (`0.0` → `1.0+`):** Controls randomness. **Low (`0.0–0.2`)** = deterministic, factual, code/SQL. **High (`0.7–1.0`)** = creative brainstorming.
- **Top-P (Nucleus Sampling):** Samples from smallest set of tokens whose cumulative probability ≥ $P$.
- **Top-K:** Limits sampling strictly to the top $K$ highest-probability tokens.
- **Max Tokens / Stop Sequences:** Caps output length and controls cost/latency.
- **Prompt Caching:** Caches static prompt prefixes (long system instructions/docs) across calls → **lower input token cost & lower latency**.

### RAG, Vector Databases & Customization Tradeoffs
- **RAG (`Amazon Bedrock Knowledge Bases`):** Retrieves up-to-date proprietary facts from a vector DB at query time and injects them into the prompt → **reduces hallucinations, provides source citations, no retraining needed**.
- **In-Scope AWS Vector Stores:** **[Amazon OpenSearch Service](./AWS_AI_SERVICES_GLOSSARY.md#amazon-opensearch-service)** (Serverless default for Bedrock KB), **[Amazon Aurora](./AWS_AI_SERVICES_GLOSSARY.md#amazon-aurora)** (`pgvector`), **[Amazon RDS for PostgreSQL](./AWS_AI_SERVICES_GLOSSARY.md#amazon-rds)** (`pgvector`), **[Amazon Neptune](./AWS_AI_SERVICES_GLOSSARY.md#amazon-neptune)** (GraphRAG).
- **Customization Escalation Ladder (Cheapest → Most Expensive):**
  1. **Prompt Engineering / In-Context Learning** (zero training cost)
  2. **RAG** (dynamic enterprise facts + citations)
  3. **Model Distillation** (transfers large **Teacher** FM quality into a small, fast, cheap **Student** model for narrow high-volume tasks)
  4. **Instruction Fine-Tuning / PEFT (`LoRA`)** (labeled prompt-completion pairs → teaches style, tone, format)
  5. **Continued Pre-Training** (massive unlabeled domain text → deep domain vocabulary)
  6. **Pre-Training from Scratch** (most expensive; custom architecture/weights)

### Prompt Engineering, Risks & FM Evaluation
- **Techniques:** `Zero-Shot` (no examples) • `One/Single-Shot` (1 example) • `Few-Shot` (2–5 examples) • `Chain-of-Thought (CoT)` ("think step by step" for reasoning/math) • `Negative Prompts` (exclude unwanted elements in image/text gen) • `Prompt Templates` (`Amazon Bedrock Prompt Management` for versioning & testing).
- **Prompt Risks:** **Prompt Injection / Hijacking** (untrusted input overrides system rules) • **Jailbreaking** (bypassing safety filters) • **Exposure** (leaking system prompts/PII) • **Poisoning** (malicious training/RAG data).
- **Automated FM Evaluation Metrics:**
  - **ROUGE:** Recall-oriented n-gram overlap → **Text Summarization**.
  - **BLEU:** Precision-oriented n-gram overlap → **Machine Translation**.
  - **BERTScore:** Contextual embedding **semantic similarity** (captures paraphrases).
  - **Perplexity:** How well a language model predicts next tokens (**lower is better**).
  - **LLM-as-a-Judge:** Strong evaluator FM scores open-ended responses on correctness, faithfulness, and helpfulness at scale (`Amazon Bedrock Model Evaluation`).
  - **Human-in-the-Loop (`HITL`):** Gold standard for nuance, tone, and safety audits.
  - **App/Business Metrics:** Task completion rate, user satisfaction, cost per interaction.

---

## 4️⃣ Domain 4: Guidelines for Responsible AI (`14%`)

### Core Pillars & Tools
- **Responsible AI Dimensions:** **Fairness** (no demographic discrimination), **Explainability** (interpretable decisions), **Privacy & Security**, **Safety** (prevent harmful content), **Controllability**, **Veracity & Robustness** (accuracy, anti-hallucination), **Governance**, **Transparency**.
- **Amazon Bedrock Guardrails:**
  - **Content Filters** (hate, insults, sexual, violence, misconduct, prompt attack).
  - **Denied Topics** (block off-limits subjects like investment/medical advice).
  - **Sensitive Information / PII Filters** (block or mask SSNs, emails, credit cards).
  - **Word Filters** (profanity & custom blocked terms).
  - **Contextual Grounding Check** (detects hallucinations not supported by RAG source).
- **Amazon SageMaker Clarify:** Detects **pre-training data bias** (`Class Imbalance`), **post-training model bias** (`Disparate Impact`), and computes **SHAP** feature attribution explainability.
- **Transparency Tools:**
  - **Amazon SageMaker Model Cards:** Standardized documentation of intended use, training data, risk rating, evaluation metrics, and limitations.
  - **Amazon SageMaker Model Dashboard:** Centralized visibility across deployed models' bias, drift, and quality.
- **Sustainability:** Choose smaller/distilled models (`Nova Micro`), `AWS Trainium`/`Inferentia`, `Prompt Caching`, and right-sized inference to minimize energy/carbon footprint.
- **Legal Risks:** Intellectual property / copyright infringement claims, biased outputs, hallucinations, loss of customer trust.

---

## 5️⃣ Domain 5: Security, Compliance & Governance for AI (`14%`)

### Securing AI Systems (v1.2)
- **AWS Shared Responsibility for AI:** AWS secures physical infra, Bedrock managed service, and base model isolation (**customer prompts/data in Bedrock are NEVER used to train base FMs**). Customer secures `IAM` policies, data encryption (`KMS`), VPC connectivity (`PrivateLink`), Guardrails, and input/output validation.
- **Agentic Security (v1.2):**
  - **Amazon Bedrock AgentCore Identity:** Manages OAuth/IAM delegation and scoped least-privilege credentials for AI agents.
  - **Policy in AgentCore:** Enforces deterministic allow/forbid policies on agent tool invocations before execution.
- **Core Security Controls:**
  - **[AWS IAM](./AWS_AI_SERVICES_GLOSSARY.md#aws-iam):** Least-privilege roles/policies for Bedrock, SageMaker, and S3.
  - **[AWS KMS](./AWS_AI_SERVICES_GLOSSARY.md#aws-kms):** Encrypts training data, vector stores, custom models, and invocation logs at rest; TLS encrypts in transit.
  - **[AWS PrivateLink](./AWS_AI_SERVICES_GLOSSARY.md#amazon-vpc):** Interface VPC Endpoints keep Bedrock/SageMaker traffic off the public internet.
  - **[Amazon Macie](./AWS_AI_SERVICES_GLOSSARY.md#amazon-macie):** ML-powered discovery of **PII / sensitive data in S3** before training/RAG ingestion.
  - **Bedrock Model Invocation Logging:** Captures prompts & completions to `S3` / `CloudWatch Logs` for audit trails.

### Governance, Compliance & Scoping Matrix
- **Generative AI Security Scoping Matrix (5 Scopes):**
  - **Scope 1:** Consumer apps (e.g., public chatbots) → Acceptable Use Policy only.
  - **Scope 2:** Enterprise apps (e.g., `Amazon Quick`, `Kiro`) → SSO, IAM, data permissions.
  - **Scope 3:** Pre-trained FMs via API (`Amazon Bedrock`, RAG) → Guardrails, PrivateLink, KMS, invocation logs.
  - **Scope 4:** Fine-tuned / customized FMs → Data curation, poisoning prevention, model access control.
  - **Scope 5:** Self-trained FMs from scratch → Full ML infrastructure, supply-chain, and training-cluster security.
- **Governance & Compliance Services:**
  - **[AWS Artifact](./AWS_AI_SERVICES_GLOSSARY.md#aws-artifact):** Download `SOC`, `ISO`, `PCI`, `HIPAA BAA` compliance reports.
  - **[AWS CloudTrail](./AWS_AI_SERVICES_GLOSSARY.md#aws-cloudtrail):** Audit log of all AWS API calls (who called what, when).
  - **[AWS Config](./AWS_AI_SERVICES_GLOSSARY.md#aws-config):** Tracks resource configuration history & continuous compliance rules.
  - **[Amazon Inspector](./AWS_AI_SERVICES_GLOSSARY.md#amazon-inspector):** Automated vulnerability scanning for `EC2`, `ECR` containers, and `Lambda`.
  - **[AWS Trusted Advisor](./AWS_AI_SERVICES_GLOSSARY.md#aws-trusted-advisor):** Best-practice checks across security, cost, performance, fault tolerance, and quotas.
