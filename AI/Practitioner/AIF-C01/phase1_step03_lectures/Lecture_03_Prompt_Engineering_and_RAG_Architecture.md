# Lecture 03: Prompt Engineering, RAG Architecture & Autonomous Agents

> **Course Track:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Target Exam Domain:** Domain 3: Applications of Foundation Models (28% of Exam Blueprint - *Highest Weight Domain*)  
> **Estimated Delivery Duration:** 120 Minutes  
> **Associated Slide Deck:** `slides/Module_02_Amazon_Bedrock_and_RAG_Slides.md` (Part 2)  
> **Target Hands-On Labs:** `labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md` & `labs/Lab_04_Autonomous_AI_Agents_with_Amazon_Bedrock.md`  
> **Student Explanations:** `explanations/03_Domain_3_Applications_of_Foundation_Models.md`

---

## 📚 Prescribed Textbook Reading & Literature Grounding

Before delivering or attending this lecture, review the assigned chapters:
* **Vikram Elango, Vivek Gangasani, Shreyas Subramanian (*Wiley / Sybex 2025*):**
  * Chapter 5: *Prompt Engineering Techniques* (pp. 161–210)
    * Anatomy of a prompt: instructions, contextual grounding, few-shot exemplars, delimiters, output format schemas.
    * Prompt techniques: Zero-shot, Few-shot (in-context learning), Chain-of-Thought (CoT), Step-Back prompting, ReAct.
  * Chapter 6: *Retrieval-Augmented Generation (RAG) & Vector Databases* (pp. 211–268)
    * The RAG Triad: Ingestion, Retrieval, and Generation.
    * Chunking strategies: Fixed-size, hierarchical, semantic, overlapping windows.
    * Vector embeddings and distance metrics: Cosine similarity, Euclidean (L2) distance, Dot product.
    * Vector store landscape: Amazon OpenSearch Serverless, Amazon Aurora PostgreSQL (`pgvector`), Amazon Neptune Analytics.
  * Chapter 7: *Bedrock Knowledge Bases & Agents* (pp. 269–318)
    * Managed Knowledge Bases synchronization with Amazon S3.
    * Multi-step autonomous planning: ReAct loop, OpenAPI 3.0 schemas, and AWS Lambda Action Groups.
  * Chapter 11: *Generative AI Model Evaluation* (pp. 439–460)
    * ROUGE (1, 2, L), BLEU, Perplexity, BERTScore, and LLM-as-a-Judge evaluation pipelines.
* **Tom Taulli (*O'Reilly 2025*):**
  * Chapter 4: *Prompt Engineering & Optimization* (pp. 67–92)
  * Chapter 5: *RAG and Enterprise Knowledge Integration* (pp. 93–122)
* **CloudExamPro AIF-C01 Master Cheat Sheet (2026 Edition):**
  * Section 3: *Prompt Engineering Taxonomy, RAG Architecture, and Agent Workflows* (pp. 11–16)
* **Notezio AIF-C01 Master Guide (2026):**
  * Chapters 9–14: *Prompting Techniques, Embeddings, Bedrock Knowledge Bases, Vector Databases, Agents for Bedrock, and Action Groups*.

---

## ⏱️ Detailed 120-Minute Delivery Schedule & Pacing

```
00:00 - 00:25 | Prompt Engineering Fundamentals: Anatomy, Delimiters, System Directives & Formatting
00:25 - 00:50 | Advanced Prompting: Zero-Shot, Few-Shot In-Context Learning, Chain-of-Thought (CoT) & ReAct
00:50 - 01:25 | Architecture of RAG: S3 Ingestion -> Chunking -> Vector Embeddings -> OpenSearch Serverless
01:25 - 01:45 | Autonomous Agents for Bedrock: Reasoning Engine, OpenAPI Schemas & Lambda Action Groups
01:45 - 01:55 | GenAI Evaluation Metrics: ROUGE (1, 2, L), BLEU, Perplexity, BERTScore & LLM-as-a-Judge
01:55 - 02:00 | Socratic Q&A & Transition to Lab 02 (Knowledge Bases) and Lab 04 (Bedrock Agents)
```

---

## 🗣️ Instructor Delivery Talking Points & Storytelling

### 1. The Art & Science of Prompt Engineering
* **Anatomy of an Enterprise Prompt:**
  1. **Role / System Prompt:** Assigns persona, authority, and boundaries (*"You are a Senior Cloud Compliance Auditor..."*).
  2. **Instruction / Task:** Explicit, unambiguous action verb (*"Extract all HIPAA violations and categorize them..."*).
  3. **Context / Grounding Data:** External text wrapped in clear delimiters (`"""`, `###`, `<context></context>`) to prevent prompt injection.
  4. **Output Constraints:** Exact desired structure (*"Return strictly valid JSON conforming to this schema..."*).

* **Prompt Engineering Taxonomy:**
  * **Zero-Shot Prompting:** Providing a prompt with zero example completions. Relies entirely on pre-trained parametric knowledge.
  * **Few-Shot Prompting (In-Context Learning):** Providing 2–5 high-quality input-output pairs inside the prompt before asking the target question. Guides formatting, tone, and reasoning style without updating model weights.
  * **Chain-of-Thought (CoT) Prompting:** Instructing the model to break down complex multi-step reasoning into intermediate steps (*"Think step by step before answering"*). Dramatically reduces arithmetic and logical errors.
  * **Step-Back Prompting:** Prompting the model to first identify high-level principles or governing laws before solving a specific edge case.
  * **ReAct Prompting (Reason + Act):** Interleaving reasoning traces (*Thought*) with concrete tool executions (*Action*) and sensory feedback (*Observation*). The foundational framework powering Bedrock Agents.

---

### 2. Retrieval-Augmented Generation (RAG): The Open-Book Exam
* **The Analogy:**
  * Base Foundation Model = A brilliant student taking a closed-book exam. They have great reasoning skills, but their knowledge cutoff was last year, and they know nothing about your company's private HR policies.
  * RAG = Giving that brilliant student an open-book library. Before answering any question, they search the library, find the exact relevant page, read it, and cite it in their answer.

```mermaid
flowchart TD
    subgraph Offline_Ingestion["Data Ingestion Pipeline (Offline Sync)"]
        S3["Amazon S3 Bucket<br/>(PDFs, DOCX, MD, HTML)"] --> Chunk["Chunking Engine<br/>(300 tokens, 20% overlap)"]
        Chunk --> EmbedModel["Amazon Titan Embeddings v2<br/>(1,536-dim vector)"]
        EmbedModel --> VectorDB[("Amazon OpenSearch Serverless<br/>Vector Search Collection")]
    end

    subgraph Online_Inference["Runtime Query & Generation Pipeline (Online)"]
        User["User Question"] --> QueryEmbed["Titan Embeddings<br/>(Vectorize Query)"]
        QueryEmbed --> VectorSearch["k-NN Vector Search<br/>(Cosine / Dot Product)"]
        VectorDB -.->|Top-K Chunks| VectorSearch
        VectorSearch --> ContextPack["Context Augmentation<br/>Prompt + Retrieved Passages"]
        ContextPack --> LLM["Foundation Model<br/>(Anthropic Claude / Titan)"]
        LLM --> Response["Grounded Answer + Citations"]
    end
```

* **Chunking Strategies:**
  * *Fixed-Size Chunking:* Splitting by token count (e.g., 300 tokens with 50-token overlap). Simple, fast, but can split sentences mid-thought.
  * *Hierarchical Chunking:* Small child chunks for high-precision retrieval linked to parent chunks for rich LLM context.
  * *Semantic Chunking:* Splitting based on semantic natural breaks (headers, paragraph themes).
* **Distance / Similarity Metrics:**
  * **Cosine Similarity:** Measures the cosine of the angle between two vectors. Normalized between -1 and 1 (1 = identical direction). Most common for text embeddings.
  * **Dot Product:** Considers both angle and vector magnitude.
  * **Euclidean Distance (L2):** Measures straight-line distance between vector coordinates (lower distance = higher similarity).
* **AWS Vector Store Options:**
  * *Amazon OpenSearch Serverless:* Fully serverless vector engine, native integration with Bedrock Knowledge Bases.
  * *Amazon Aurora PostgreSQL (`pgvector`):* Relational database with vector similarity extension; ideal if operational transactional data is already in Aurora.
  * *Amazon Neptune Analytics:* Graph vector database for knowledge graphs and connected entity search.

---

### 3. Autonomous AI Agents for Amazon Bedrock
* **What is an Agent?**
  * An autonomous system that uses an LLM as its reasoning brain to execute multi-step workflows, orchestrate tools, query knowledge bases, and make decisions dynamically.
* **Core Architecture Components:**
  1. **Foundation Model (The Brain):** Analyzes user intent, develops an execution plan, and decides which tools to invoke.
  2. **Knowledge Base (The Memory):** Access to private enterprise documentation for factual context retrieval.
  3. **Action Groups (The Hands):** The tools the agent can execute. Composed of:
     * *OpenAPI 3.0 Schema:* Defines available API endpoints, parameters, and return types in standard JSON/YAML.
     * *AWS Lambda Function:* The serverless compute that executes the actual business logic (e.g., querying DynamoDB, creating a Jira ticket, calling Stripe API).
* **The ReAct Execution Loop:**
  * User asks: *"Cancel flight FL-409 for customer C-902 and refund the ticket."*
  * Agent iterates:
    * **Thought 1:** I need to check the flight status and cancellation policy.
    * **Action 1:** Query Knowledge Base for flight cancellation guidelines.
    * **Observation 1:** Cancellations within 24 hours are eligible for 100% refund.
    * **Thought 2:** I need to call the flight cancellation API.
    * **Action 2:** Invoke Lambda function `CancelBooking(flightId="FL-409", customerId="C-902")`.
    * **Observation 2:** Booking successfully cancelled, refund ID `RF-881` generated.
    * **Thought 3:** I have fulfilled the user request.
    * **Final Answer:** Flight FL-409 cancelled and refund of \$450 issued (Ref: RF-881).

---

### 4. Generative AI Model Evaluation Metrics

| Metric | Measurement Focus | How It Works | Primary Use Case |
| :--- | :--- | :--- | :--- |
| **ROUGE-1** | Word / Unigram overlap | Measures overlap of individual words between generated text and reference text. | Text summarization baseline. |
| **ROUGE-2** | Bigram (2-word pair) overlap | Measures overlap of consecutive word pairs, assessing fluency and phrasal coherence. | Summary readability and cohesion. |
| **ROUGE-L** | Longest Common Subsequence | Measures the longest common string of words without requiring consecutive matches. | Sentence structure preservation in summarization. |
| **BLEU** | n-gram Precision | Precision-focused metric calculating how many candidate n-grams appear in reference translations. | Machine translation evaluation. |
| **Perplexity** | Uncertainty / Surprise | Exponential of negative log-likelihood. Lower perplexity = model is more confident in predicting the text. | Language model pre-training quality. |
| **BERTScore** | Semantic Similarity | Computes pairwise cosine similarity of contextual token embeddings (captures synonyms). | Abstractive rewriting where exact words differ. |
| **LLM-as-a-Judge** | Multi-dimensional scoring | Using a frontier model (Claude 3.5 Sonnet) with a structured rubric to score answers for Groundedness, Relevance, and Tone. | Bedrock Model Evaluation jobs and RAG pipelines. |

---

## 🏗️ Production Scenario: Global Telco Automated Customer Support Agent

* **Client:** *Apex Wireless*, servicing 20 million mobile subscribers.
* **Business Challenge:** Customers wait 45 minutes on hold to troubleshoot SIM card issues, check billing charges, or upgrade data plans.
* **Architecture Solution:**
  1. **Omnichannel Interface:** Amazon Lex conversational bot connected to customer mobile app and phone lines.
  2. **Bedrock Agent:** Orchestrates customer intent using Anthropic Claude 3.5 Sonnet.
  3. **Knowledge Base:** Bedrock Knowledge Base connected to Amazon S3 holding 5,000 PDF device troubleshooting manuals and plan terms indexed in OpenSearch Serverless.
  4. **Action Group 1 (Billing):** OpenAPI schema connected to AWS Lambda `FetchAccountBalance(phone_number)`.
  5. **Action Group 2 (SIM Reset):** OpenAPI schema connected to AWS Lambda `SendNetworkResetSignal(iccid)`.
  6. **Security & Guardrails:** Bedrock Guardrails masking all 16-digit credit card numbers and denying discussions about competitor pricing.

---

## ❓ Socratic Discussion Questions & Classroom Engagement

1. **Question:** *"If a model answers arithmetic word problems incorrectly despite knowing the formulas, what prompt engineering technique should you apply first?"*
   * *Answer:* **Chain-of-Thought (CoT) prompting** (e.g., adding *"Let's think step by step"*), which forces the model to generate intermediate reasoning tokens, vastly improving math accuracy.
2. **Question:** *"Why do we need vector embeddings for RAG instead of standard keyword search like SQL `LIKE '%query%'`?"*
   * *Answer:* Vector embeddings capture **semantic meaning and conceptual intent**. A user searching for *"How do I fix a flat tire?"* will match a document explaining *"Replacing a punctured wheel"*, even though they share zero identical keywords.
3. **Question:** *"In an Amazon Bedrock Agent, who writes the business logic that updates an order in DynamoDB?"*
   * *Answer:* The developer writes it inside an **AWS Lambda function**, which is referenced by the agent's **Action Group** via an OpenAPI 3.0 specification. The agent formulates the parameters; Lambda executes the action.

---

## ⚠️ Exam Traps & "Watch Out For..."

> [!WARNING]
> **Trap 1: ROUGE vs BLEU Selection**  
> Remember the mnemonic: **B**LEU = **B**ilingual / Translation (Precision-oriented). **R**OUGE = **R**ecall / Summarization (Overlap-oriented). If an exam question asks to evaluate automated summaries of financial earnings calls, choose **ROUGE**.

> [!IMPORTANT]
> **Trap 2: OpenSearch Serverless Cost Alert**  
> OpenSearch Serverless Vector Collections mandate a minimum of 2 OpenSearch Compute Units (OCUs) for search and 2 for indexing (or 1+1 minimum), costing ~$0.48/hr ($350/mo). For exam questions, it is the primary serverless vector store for Bedrock Knowledge Bases; for student labs, it must be deleted immediately after testing!

> [!TIP]
> **Trap 3: RAG vs Fine-Tuning Decision**  
> If proprietary data changes hourly/daily $\rightarrow$ **RAG**. Fine-tuning cannot keep up with rapidly changing data and requires costly recurring retraining runs.

---

## 📋 Post-Lecture Student Checklist & Lab Transition

- [ ] Complete **Lab 02:** `labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md`.
- [ ] Complete **Lab 04:** `labs/Lab_04_Autonomous_AI_Agents_with_Amazon_Bedrock.md`.
- [ ] Review `explanations/03_Domain_3_Applications_of_Foundation_Models.md`.
- [ ] Practice the ROUGE vs BLEU vs Perplexity distinction table.
- [ ] Run the Module 3 review quiz in `slides/Module_03_Prompt_Engineering_and_Applications_Slides.md`.


---

## 🎯 Authentic Exam Practice & Case Scenarios
> High-yield scenario questions from the authentic candidate practice pool reinforcing the core competencies of this lecture.

### Scenario Practice 1: AIF-C01-ET-Q122
**Question:**  
A company is using Retrieval Augmented Generation (RAG) with Amazon Bedrock and Stable Diffusion to generate product images based on text descriptions. The results are often random and lack specific details. The company wants to increase the specificity of the generated images.

Which solution meets these requirements?

**Options:**
- A) Increase the number of generation steps.
- B) Use the MASK_IMAGE_BLACK mask source option.
- C) Increase the classifier-free guidance (CFG) scale.
- D) Increase the prompt strength.

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `C`  
**Peer Consensus:** `57%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: C (57%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: D
Explicação:
A força do prompt (prompt strength) se refere ao grau de influência que o texto fornecido tem sobre a imagem gerada.

Quando a força do prompt é baixa, o modelo (como o Stable Diffusion) pode gerar imagens mais abstratas ou genéricas.

Ao aumentar a força do prompt, você orienta o modelo a seguir mais fielmente os detalhes fornecidos no texto, gerando imagens mais específicas e controladas — o que é justamente o que a empresa deseja.
---
Selected Answer: D
In Retrieval Augmented Generation (RAG) with Stable Diffusion, the prompt strength determines how closely the generated image aligns with the given text description. By increasing prompt strength, the model places more emphasis on the input prompt, making the output more specific and detailed, which directly addresses the company's concern about random and lacking specific details in generated images.
---
Selected Answer: C
Classifier-Free Guidance (CFG) is a technique used in generative models, especially in image generation tasks, that helps guide the generation process toward more specific or desired outputs. By increasing the CFG scale, the model's generated image becomes more closely aligned with the given text prompt, improving the specificity and control over the details in the generated image.

A higher CFG scale ensures that the model generates images that are more faithful to the prompt by reducing randomness and making the generation more deterministic. This technique allows for more control over the image generation process, making it suitable for use cases like generating product images from text descriptions, where specific details are important.

</details>

### Scenario Practice 2: AIF-C01-ET-Q033
**Question:**  
A company wants to use a large language model (LLM) on Amazon Bedrock for sentiment analysis. The company wants to classify the sentiment of text passages as positive or negative.

Which prompt engineering strategy meets these requirements?

**Options:**
- A) Provide examples of text passages with corresponding positive or negative labels in the prompt followed by the new text passage to be classified.
- B) Provide a detailed explanation of sentiment analysis and how LLMs work in the prompt.
- C) Provide the new text passage to be classified without any additional context or examples.
- D) Provide the new text passage with a few examples of unrelated tasks, such as text summarization or question answering.

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `A`  
**Peer Consensus:** `100%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
This approach is known as few-shot prompting, where you include a few labeled examples to guide the model on how to classify sentiment.
---
Selected Answer: A
Provide examples of text passages with corresponding positive or negative labels in the prompt followed by the new text passage to be classified: This approach uses few-shot learning, where you give the model clear examples of text passages labeled with sentiment (positive or negative). By providing these examples in the prompt, the model is better able to understand the task and generalize it to classify the new text passage correctly. This is a common and effective strategy for tasks like sentiment analysis.
---
Selected Answer: A
Set the proper label with a few examples to the prompts

</details>

### Scenario Practice 3: AIF-C01-ET-Q037
**Question:**  
A company wants to use a large language model (LLM) to develop a conversational agent. The company needs to prevent the LLM from being manipulated with common prompt engineering techniques to perform undesirable actions or expose sensitive information.
Which action will reduce these risks?

**Options:**
- A) Create a prompt template that teaches the LLM to detect attack patterns.
- B) Increase the temperature parameter on invocation requests to the LLM.
- C) Avoid using LLMs that are not listed in Amazon SageMaker.
- D) Decrease the number of input tokens on invocations of the LLM.

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `A`  
**Peer Consensus:** `88%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: A (88%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Explicação: A criação de cuidadosamente projetados,ados com técnicas de segurança como validação de entrada,agem de conteúdo e detecção padrões de engenharia de prompt (prompt injection), é prática fundamental para reduzir os riscos de manipulação de LLM. Essa abordagem ensina modelo a reconhecer e resistir tentativas maliciosas, como comandos disfarçados exploração de brechas prompt.
---
Selected Answer: A
Create a prompt template that teaches the LLM to detect attack patterns: By creating a prompt template that is specifically designed to identify and mitigate common attack patterns (e.g., prompt injections or malicious requests), you can make the LLM more robust to manipulation. This can help the LLM recognize when it's being manipulated into performing undesirable actions or exposing sensitive data, and take preventive measures accordingly.
---
Selected Answer: A
Ask model to use Prompt template to avoid the various types of prompt injection attacks.

</details>
