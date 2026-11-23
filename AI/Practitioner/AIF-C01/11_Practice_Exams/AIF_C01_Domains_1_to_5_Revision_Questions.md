# AIF-C01: Domains 1 to 5 Revision Questions

### Question 1 (Domain 1: Fundamentals of AI/ML)
A business analyst wants to build a predictive machine learning model to forecast customer churn using an existing CSV dataset without writing Python code or managing infrastructure. Which AWS tool is designed specifically for this persona?
- [ ] A) Amazon SageMaker Studio Code Editor
- [ ] B) Amazon SageMaker Canvas
- [ ] C) AWS Deep Learning AMIs (DLAMI)
- [ ] D) Amazon EMR
> **Correct Answer:** B  
> **Rationale:** SageMaker Canvas provides a visual, point-and-click interface that enables non-programmers and business analysts to generate accurate ML predictions with zero code.

---

### Question 2 (Domain 2: Fundamentals of Generative AI)
When generating technical customer support responses from a Foundation Model, an engineer notices the model is producing overly creative and varying answers. Which inference parameter should be decreased to make the model's responses more deterministic and focused?
- [ ] A) Context Window size
- [ ] B) Temperature
- [ ] C) Maximum Generation Length
- [ ] D) Embedding Dimensions
> **Correct Answer:** B  
> **Rationale:** Lowering the Temperature (e.g. from 0.8 to 0.1) reduces randomness, compelling the model to select higher-probability next tokens, resulting in factual, deterministic output.

---

### Question 3 (Domain 3: Applications of Foundation Models)
A financial firm wants to connect Amazon Bedrock foundation models to internal quarterly earnings reports stored in Amazon S3 so the model can cite exact sources without retraining. Which capability provides this managed workflow?
- [ ] A) Amazon Bedrock Agents
- [ ] B) Amazon Bedrock Knowledge Bases (RAG)
- [ ] C) Amazon SageMaker JumpStart Fine-Tuning
- [ ] D) Amazon Bedrock Model Evaluation
> **Correct Answer:** B  
> **Rationale:** Amazon Bedrock Knowledge Bases automates Retrieval-Augmented Generation (RAG) by converting S3 documents into vector embeddings and retrieving relevant chunks to augment user prompts.

---

### Question 4 (Domain 4: Responsible AI)
An enterprise chatbot must block users from asking about internal competitors and automatically mask Social Security Numbers (SSNs) in both user prompts and model completions. Which AWS service feature natively accomplishes this?
- [ ] A) Amazon SageMaker Clarify
- [ ] B) Amazon Bedrock Guardrails
- [ ] C) AWS WAF Rate Limiting
- [ ] D) AWS IAM Permission Boundaries
> **Correct Answer:** B  
> **Rationale:** Amazon Bedrock Guardrails enforces custom policies across applications, including Denied Topics (blocking competitor mentions) and Sensitive Information Filters (redacting or masking PII like SSNs).

---

### Question 5 (Domain 5: Security, Compliance & Governance)
A regulated healthcare organization requires assurance that their clinical prompts submitted to Amazon Bedrock are never used to train the base foundation models or shared with third-party model providers. What is Amazon Bedrock's data privacy policy?
- [ ] A) Customer prompts are retained for 90 days to retrain public models
- [ ] B) Customer prompts and completions are never used to train base models and remain within the customer's selected AWS Region and VPC
- [ ] C) Prompts are shared with model creators only if anonymized
- [ ] D) Training exemption requires purchasing an Enterprise Support Plan
> **Correct Answer:** B  
> **Rationale:** Amazon Bedrock provides enterprise-grade data privacy: customer data is never used to train base foundation models, is encrypted in transit and at rest, and remains under customer control.
