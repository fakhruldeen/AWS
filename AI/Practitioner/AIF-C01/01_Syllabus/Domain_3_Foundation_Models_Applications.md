# Domain 3: Applications of Foundation Models (`28%` of Scored Content — Highest Weight)

> **Official Blueprint:** AWS Certified AI Practitioner (`AIF-C01`) Exam Guide v1.2 (Oct 29, 2026)  
> **Scored Questions (~50 scored total):** ~14 scored questions (~18 in a 65-question full mock)

---

## Task Statement 3.1: Describe design considerations for applications that use foundation models (FMs)
- **FM Selection Criteria (v1.2):** Cost, modality (text/image/audio/video), latency, multi-lingual support, model size, model complexity, customization options, input/output token length, and **`Prompt Caching`**.
- **Inference Parameters:** `Temperature` (randomness/creativity), `Top-P` (nucleus probability threshold), `Top-K` (top K candidate tokens), max input/output length, stop sequences.
- **Retrieval-Augmented Generation (`RAG`):** Grounding FM outputs in up-to-date proprietary enterprise data (`Amazon Bedrock Knowledge Bases`) without retraining weights.
- **AWS Vector Databases:** `Amazon OpenSearch Service` (`Serverless`), `Amazon Aurora` (`pgvector`), `Amazon Neptune` (`GraphRAG`), `Amazon RDS for PostgreSQL` (`pgvector`), `Amazon DocumentDB`.
- **FM Customization Cost Tradeoffs (v1.2):** In-context learning (Prompting) < `RAG` < **`Model Distillation`** (large Teacher → small fast Student) < Instruction Fine-Tuning / PEFT (`LoRA`) < Continued Pre-Training < Pre-Training from scratch.
- **AI Agents:** Role of autonomous agents (reasoning, planning, invoking tools/APIs, maintaining memory) and business applications (order fulfillment, IT automation, multi-step research).

## Task Statement 3.2: Choose effective prompt engineering techniques
- **Prompt Constructs:** System instructions, context, input data, output indicators, `negative prompts`.
- **Techniques:** `Zero-shot`, `Single-shot` (`One-shot`), `Few-shot`, `Chain-of-Thought (CoT)`, and reusable `Prompt Templates`.
- **Best Practices:** Specificity and concision, iterative experimentation, guardrails, structured delimiters, multiple comments/examples.
- **Risks & Limitations:** Prompt `exposure` (leakage), `poisoning`, `hijacking` / `prompt injection`, and `jailbreaking`.
- **Prompt Versioning & Management (v1.2):** Using **`Amazon Bedrock Prompt Management`** to version, test, compare, and deploy prompts safely across environments.

## Task Statement 3.3: Describe the training and fine-tuning process for FMs
- **Key Training Elements:** `Pre-training`, `Instruction Fine-Tuning`, `Continuous Pre-Training`, and **`Model Distillation`**.
- **Fine-Tuning Methods:** Instruction tuning, domain adaptation, transfer learning, parameter-efficient fine-tuning (`PEFT` / `LoRA`), continuous pre-training.
- **Data Preparation for Fine-Tuning:** Data curation, governance, dataset size, high-quality labeling, demographic/domain representativeness, and **`RLHF`** (Reinforcement Learning from Human Feedback).

## Task Statement 3.4: Describe methods to evaluate FM performance
- **Evaluation Approaches:** Human-in-the-loop (`HITL`) evaluation, standardized benchmark datasets, and **`Amazon Bedrock Model Evaluation`**.
- **Automated FM Metrics (v1.2):** `ROUGE` (summarization recall), `BLEU` (translation precision), **`BERTScore`** (contextual embedding semantic similarity), `Perplexity` (lower is better), and **`LLM-as-a-judge`** (evaluator FM scoring open-ended quality at scale).
- **Application-Level Evaluation (v1.2):** Evaluating complete FM applications including **RAG** (retrieval precision/recall, faithfulness), **Agents** (tool selection accuracy, trajectory efficiency), and **Workflows**.
- **Business Objective Alignment Metrics:** Productivity gains, user engagement, **task completion rate**, **user satisfaction**, and **cost per interaction**.
