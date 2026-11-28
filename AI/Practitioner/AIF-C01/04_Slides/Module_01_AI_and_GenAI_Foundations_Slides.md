---
marp: true
theme: default
paginate: true
header: "AWS Certified AI Practitioner (AIF-C01) | Module 1: AI & GenAI Foundations"
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
## Module 1: Foundations of Artificial Intelligence & Generative AI

**Instructor:** Mohamed Fakhruldeen  
**Track:** AI Foundation  
**Repository:** `fakhruldeen/AWS`

---

## What is Artificial Intelligence?

* **Artificial Intelligence (AI):** The overarching science of building systems capable of simulating human cognitive processes (vision, language, reasoning).
* **Machine Learning (ML):** A subset of AI where mathematical models learn patterns directly from statistical data without hand-coded rules.
* **Deep Learning (DL):** A subset of ML utilizing multi-layered artificial neural networks (Transformers, CNNs) to model non-linear abstractions.
* **Generative AI (GenAI):** The frontier of Deep Learning focused on **creating novel, coherent content** (text, code, images, audio) conditioned on input prompts.

---

## The Machine Learning Taxonomy

```
+-----------------------------------------------------------+
|                   Machine Learning                        |
+--------------------+---------------------+----------------+
| Supervised         | Unsupervised        | Reinforcement  |
+--------------------+---------------------+----------------+
| Labeled data (X,Y) | Unlabeled data (X)  | Agent & Env    |
| • Classification   | • Clustering        | • State/Action |
| • Regression       | • Dim. Reduction    | • Reward/Loss  |
| Ex: Fraud, Churn   | Ex: Customer Groups | Ex: DeepRacer  |
+--------------------+---------------------+----------------+
```

* **Supervised:** We teach the model with input/output pairs.
* **Unsupervised:** The model discovers underlying patterns on its own.
* **Reinforcement:** Learning optimal policies via reward maximization.

---

## What Makes Generative AI Different?

| Traditional / Discriminative AI | Generative AI |
|---|---|
| Estimates P(Y \| X) (Conditional probability) | Estimates $P(X)$ or generates $Y$ conditioned on prompt |
| Answers: *"Is this transaction fraudulent?"* | Answers: *"Draft an executive summary of this audit"* |
| Fixed tabular or categorical outputs | Open-ended, creative, synthesized outputs |
| Examples: Random Forest, XGBoost | Examples: Anthropic Claude, Amazon Titan |

---

## Foundation Models (FMs)

* **Definition:** Massive neural networks pre-trained on broad, internet-scale datasets (billions or trillions of tokens).
* **The Paradigm Shift:**
  * **Past:** Train a distinct machine learning model for every specific downstream task (one for sentiment, one for grammar, one for summarization).
  * **Present:** One general Foundation Model adapted to hundreds of downstream tasks via prompting or fine-tuning!
* **Key Modalities:**
  * **Text-to-Text:** Large Language Models (LLMs).
  * **Text-to-Image:** Diffusion Models (e.g., Stable Diffusion, Titan Image Generator).
  * **Multimodal:** Models accepting text + image inputs to output text.

---

## Understanding Tokens & Tokenization

* Language models do not read characters or words—they read **Tokens**.
* Tokens are sub-word numerical chunks (e.g., Byte-Pair Encoding).
* **Rule of Thumb (English):**
  * 1 token ≈ 0.75 words (or ≈ 4 characters).
  * 1,000 tokens ≈ 750 words.
* **Why Tokens Matter:**
  1. **Context Window Limits:** Models have strict token capacities per call.
  2. **Billing:** In Amazon Bedrock, you pay per $1,000$ (or 1M) input and output tokens. Output tokens cost more due to auto-regressive generation.

---

## The Context Window

* **Analogy:** The model's *active working memory* or short-term RAM.
* Everything needed to generate an answer must fit within the context window (system instructions + conversation history + retrieved docs + question).
* **Evolution of Context Windows:**
  * Early LLMs: $2,048 - 4,096$ tokens.
  * Modern FMs: Claude 3.5 Sonnet supports **200,000 tokens** (≈ 150,000 words).
* **Watch Out:** *"Lost in the Middle"* effect—information placed in the exact middle of very long contexts can sometimes be overlooked.

---

## Embeddings & Vector Space

* **Embeddings:** High-dimensional numerical arrays (vectors) representing the semantic meaning of text or images.
* Words and sentences with similar meanings map close together in vector space:

  $$
  \text{Vector}(\text{"Physician"}) \approx \text{Vector}(\text{"Doctor"})
  $$

* **AWS Services for Embeddings:**
  * **Amazon Titan Text Embeddings V2:** Generates high-accuracy vectors.
  * **Vector Databases:** Amazon OpenSearch Serverless, Aurora PostgreSQL with `pgvector`, Neptune Analytics.

---

## Controlling Inference: Temperature

* **Temperature ($0.0 - 1.0$):** Controls the randomness and shape of the candidate word probability distribution.
* **Low Temperature ($0.0 - 0.2$):**
  * Greedy, deterministic, strict.
  * Best for: **Data extraction, SQL/code generation, math, and factual Q&A**.
* **High Temperature ($0.7 - 1.0$):**
  * Diverse, creative, imaginative.
  * Best for: **Marketing copy, brainstorming, fiction, dialogue**.
* **Exam Rule:** If you need consistent JSON output, set Temperature to `0.0`!

---

## Controlling Inference: Top-P & Top-K

* **Top-P (Nucleus Sampling):**
  * The model pools only the top candidate tokens whose cumulative probability reaches threshold $P$ (e.g., $0.90$).
  * Dynamic pool: Grows when many plausible words exist, shrinks when one word is obvious.
* **Top-K:**
  * Restricts candidate tokens to a fixed number $K$ (e.g., Top 50 words).
* **Best Practice:** Adjust **either** Temperature **or** Top-P. Avoid tweaking both aggressively at once!

---

## Stop Sequences & Max Tokens

* **Max Generation Length (Max Tokens):**
  * Caps the maximum number of tokens generated in the response.
  * Prevents runaway generation and controls API costs.
* **Stop Sequences:**
  * Specific characters or strings that trigger the model to immediately stop generating.
  * Example in chat: Stop sequence `\nUser:` prevents the model from generating both sides of the conversation.

---

## Prompt Engineering: The Art of Direction

* **Core Definition:** Designing and refining inputs to guide foundation models toward desired, reliable outputs.
* **Key Techniques:**
  1. **Zero-Shot:** Give the task instruction directly without examples.
  2. **Few-Shot (In-Context Learning):** Provide 2-5 demonstration pairs.
  3. **Chain-of-Thought (CoT):** Add *"Think step by step"* to force explicit reasoning before the final answer.
  4. **System Prompts:** Enforce role, tone, and safety constraints.

---

## Prompt Injection & Security

* **Prompt Injection:** An adversary crafts malicious user inputs designed to override developer system instructions.
* **Jailbreaking:** Using creative roleplay or hypothetical framing to bypass built-in safety filters.
* **AWS Mitigation Strategy:**
  1. Wrap user inputs in XML boundaries (`<user_input>`).
  2. Implement **Amazon Bedrock Guardrails** to filter toxicity, redact PII, and block denied topics.
  3. Contextual Grounding Check to eliminate hallucinations.

---

## Hands-On Lab Preview: Lab 01

* **Lab 01:** Prompt Engineering in the Amazon Bedrock Playground.
* **What You Will Do:**
  1. Access Amazon Bedrock console.
  2. Compare Anthropic Claude and Amazon Titan models.
  3. Observe the direct effect of shifting Temperature from `0.0` to `1.0`.
  4. Build Zero-Shot, Few-Shot, and Chain-of-Thought prompts.
  5. Test Stop Sequences and Max Tokens.

---

# Questions & Discussion

**Next Module:** Module 2: Applications of Foundation Models & Amazon Bedrock RAG

---

# Module 1 Student Review Quiz

1. **A hospital wants to build a machine learning model to detect malignant tumors from patient CT scans. Which evaluation metric should the data science team prioritize to MINIMIZE undetected cancer cases?**
   * A) Precision
   * B) Recall (Sensitivity) *(Correct — minimizes False Negatives)*
   * C) Mean Absolute Error (MAE)
   * D) R-squared (^2$)

2. **A retail company has a database of 2 million customer transaction records with no predefined labels. They want to group customers with similar buying habits into marketing segments. Which machine learning technique is required?**
   * A) Supervised Binary Classification
   * B) Linear Regression
   * C) Unsupervised Clustering *(Correct — discovers latent groupings without ground truth labels)*
   * D) Reinforcement Learning

3. **A machine learning model achieves 99.4% accuracy on training data, but drops to 62.1% accuracy on independent test data. What problem is the model experiencing, and what is the primary remedy?**
   * A) Underfitting (High Bias); increase model complexity
   * B) Overfitting (High Variance); apply regularization, dropout, or collect more data *(Correct)*
   * C) Data drift; retrain the model on the same training set
   * D) High precision; increase learning rate



---

# 🆕 Exam Guide v1.2 (2026) — AI/ML Pipeline & Architecture Quick Map

- **Neural Network Families:** `CNN` (Vision) • `RNN/LSTM` (Sequences) • `GAN` & `VAE` (Synthetic Gen) • `Transformer` (LLMs) • `Diffusion` (Images/Video)
- **Expanded AWS Pipeline Services (Task 1.3):**
  - **`Kiro`:** AWS spec-driven agentic AI IDE (requirements → design specs → verified code)
  - **`Amazon Quick`:** Unified AI-powered BI, natural-language analytics & enterprise workflows
  - **`Amazon SageMaker AI`** & **`Amazon Bedrock`**
- **When NOT to Use ML:** Deterministic rules needing 100% exact results → use rule-based code or `RPA`
