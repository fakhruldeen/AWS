# AWS Certified AI Practitioner (AIF-C01) Exam Guide & Blueprint (v1.2)

> **Document:** AWS Certified AI Practitioner Exam Guide (`AIF-C01`)  
> **Official Version:** 1.2 (October 29, 2026)  
> **Target Certification:** AWS Certified AI Practitioner  
> **Course Track:** `AI/Practitioner/AIF-C01/`  
> **Passing Score:** 700 / 1000 (Scaled score across 50 scored + 15 unscored questions)  
> **Question Types:** Multiple choice, Multiple response, Ordering (3-5 steps), Matching (3-7 items)

---

## 📊 Exam Content Domains & Weightings

| Domain | Domain Title | Official Weighting | Question Pool Share |
|:---:|:---|:---:|:---|
| **Domain 1** | Fundamentals of AI and ML | **20%** | ~13 Questions |
| **Domain 2** | Fundamentals of Generative AI (GenAI) | **24%** | ~16 Questions |
| **Domain 3** | Applications of Foundation Models (FMs) | **28%** | ~18 Questions |
| **Domain 4** | Guidelines for Responsible AI | **14%** | ~9 Questions |
| **Domain 5** | Security, Compliance, and Governance for AI Solutions | **14%** | ~9 Questions |
| **TOTAL** | | **100%** | **65 Questions** |

---

## 🗺️ Domain & Task Breakdown

### Domain 1: Fundamentals of AI and ML (20%)
* **Task 1.1:** Explain basic AI concepts and terminologies (AI, ML, Deep Learning, Neural Networks, Computer Vision, NLP, Model, Algorithm, Training vs Inferencing, Bias, Fairness, Fit, LLM, GenAI, Agentic AI; Inferencing types: batch, real-time, async, serverless; Data types: labeled/unlabeled, tabular, time-series, image, text, structured/unstructured; Supervised, Unsupervised, Reinforcement Learning).
* **Task 1.2:** Identify practical use cases for AI (Decision assist, scalability, automation; when NOT appropriate: deterministic outcome needed vs prediction, cost-benefit; regression, classification, clustering; real-world applications; AWS AI services: SageMaker AI, Transcribe, Translate, Comprehend, Lex, Polly; traditional ML vs FMs: explainability, operational constraints).
* **Task 1.3:** Describe the AI/ML development lifecycle (Pipeline components, FM sources: open source pre-trained vs custom training; production methods: managed API vs self-hosted; AWS tools: Bedrock, Quick, Kiro, SageMaker AI; MLOps fundamentals: experimentation, technical debt, production readiness, monitoring, re-training; Model metrics: accuracy, precision, recall, F1; Business metrics: cost per user, ROI).

### Domain 2: Fundamentals of Generative AI (24%)
* **Task 2.1:** Explain basic concepts of GenAI (Tokens, chunking, embeddings, vectors, prompt engineering, transformer LLMs, FMs, multi-modal, diffusion models; use cases: image/video/audio generation, summarization, assistants, code generation; FM lifecycle; token-based pricing; context engineering; Agentic AI: multi-agent system patterns, Model Context Protocol [MCP], multi-agent communication patterns, memory management, tool usage, workflow orchestration).
* **Task 2.2:** Capabilities and limitations of GenAI for business problems (Advantages: adaptability, responsiveness, conversational, content generation; Disadvantages: hallucinations, interpretability, inaccuracy, nondeterminism; model selection factors: compliance, cost, latency, complexity; business metrics: cross-domain performance, ROI, ARPU, CLV).
* **Task 2.3:** AWS infrastructure and technologies for building GenAI applications (AWS services: Amazon Bedrock, SageMaker AI, SageMaker JumpStart, Amazon Quick, Kiro, Strands Agents, Bedrock AgentCore; AWS infrastructure benefits: security, compliance, responsibility, safety; cost trade-offs: responsiveness, availability, redundancy, token-based pricing, provisioned throughput, custom models).

### Domain 3: Applications of Foundation Models (28%)
* **Task 3.1:** Design considerations for applications that use FMs (Selection criteria: cost, modality, latency, multi-lingual, size, complexity, customization, context length, prompt caching; inference parameters: temperature, output length; RAG: Amazon Bedrock Knowledge Bases; Vector databases: OpenSearch Service, Aurora, Neptune, RDS PostgreSQL; Cost trade-offs: pre-training, fine-tuning, in-context learning, RAG, distillation; Role of AI agents).
* **Task 3.2:** Choose effective prompt engineering techniques (Constructs: context, instruction, negative prompts; Techniques: chain-of-thought, zero-shot, single-shot, few-shot, templates; Best practices: quality, experimentation, guardrails, concision; Risks: exposure, poisoning, hijacking, jailbreaking; Versioning: Amazon Bedrock Prompt Management).
* **Task 3.3:** Training and fine-tuning process for FMs (Pre-training, fine-tuning, continuous pre-training, distillation; Instruction tuning, domain adaptation, transfer learning; Data prep: curation, governance, size, labeling, RLHF).
* **Task 3.4:** Describe methods to evaluate FM performance (Approaches: human-in-the-loop, benchmark datasets, Amazon Bedrock Model Evaluation; Metrics: ROUGE, BLEU, BERTScore, LLM-as-a-judge; Business alignment: task completion rate, user satisfaction, cost per interaction; App evaluation: RAG, agents, workflows).

### Domain 4: Guidelines for Responsible AI (14%)
* **Task 4.1:** Explain development of AI systems that are responsible (Features: bias, fairness, inclusivity, robustness, safety, veracity; Tools: Amazon Bedrock Guardrails; Responsible model selection: environmental considerations, sustainability; Legal risks: IP infringement, biased outputs, customer trust, hallucinations; Dataset characteristics: diversity, curated sources, balanced data; Bias/variance: demographic groups, overfitting, underfitting; Monitoring tools: label quality, human audits, subgroup analysis).
* **Task 4.2:** Recognize importance of transparent and explainable models (Transparent vs opaque; Tools: Amazon SageMaker Model Cards, Bedrock Model Evaluations, open-source models, data, licensing; Trade-offs: safety vs transparency, interpretability vs performance; Human-centered design for XAI: user feedback, AI decision transparency).

### Domain 5: Security, Compliance, and Governance for AI Solutions (14%)
* **Task 5.1:** Explain methods to secure AI systems (Services: IAM roles/policies, encryption, Amazon Macie, AWS PrivateLink, shared responsibility, Amazon Bedrock AgentCore Identity, Policy in AgentCore, Amazon Bedrock Guardrails; Source citation: data lineage, data cataloging, SageMaker Model Cards; Secure data engineering: PETs, access control, integrity; Security & privacy: prompt injection, encryption at rest/transit, data leakage prevention, output filtering, audit trail, toxicity; Hallucination detection & grounding: RAG grounding, output validation, confidence scoring).
* **Task 5.2:** Recognize governance and compliance regulations for AI systems (Services: AWS Config, Amazon Inspector, AWS Artifact, AWS CloudTrail, AWS Trusted Advisor; Data governance: data lifecycles, logging, residency, monitoring, retention; Governance protocols: review cadence, Generative AI Security Scoping Matrix, transparency standards, team training).

---

## 🎯 In-Scope Modern AWS Offerings
- **Foundation Models:** Amazon Bedrock, Amazon Nova (Nova Micro, Nova Lite, Nova Pro, Nova Premier).
- **Agentic AI & Tooling:** Amazon Bedrock AgentCore (Identity & Policy), Strands Agents, Kiro, Model Context Protocol (MCP).
- **RAG & Vector Stores:** Amazon Bedrock Knowledge Bases, Amazon OpenSearch Service, Amazon Aurora pgvector, Amazon Neptune, Amazon RDS PostgreSQL.
- **ML Lifecycle & Explainability:** Amazon SageMaker AI (Studio, Canvas, Data Wrangler, Clarify, Model Cards, JumpStart).
- **Applied AI Services:** Amazon Textract, Amazon Transcribe, Amazon Comprehend, Amazon Translate, Amazon Polly, Amazon Rekognition, Amazon Lex, Amazon Personalize, AWS Transform.
