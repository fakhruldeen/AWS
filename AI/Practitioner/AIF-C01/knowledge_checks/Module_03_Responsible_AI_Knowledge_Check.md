# Module 03 Knowledge Check: Responsible AI & Safety

### Questions
1. **Which Amazon Bedrock feature allows organizations to block specific undesirable topics, filter toxic content, and mask sensitive PII like credit card numbers?**
   - A) Amazon Bedrock Agents
   - B) Amazon Bedrock Guardrails
   - C) Amazon Bedrock Knowledge Bases
   - D) Amazon Bedrock Custom Models
2. **Which AWS tool provides explainability for machine learning models using SHAP (Shapley Additive exPlanations) values to determine feature importance?**
   - A) Amazon SageMaker Clarify
   - B) Amazon SageMaker Canvas
   - C) AWS Artifact
   - D) Amazon Inspector
3. **What is a "Hallucination" in the context of Large Language Models?**
   - A) An EC2 instance running out of memory
   - B) When a model generates incorrect, fabricated, or nonsensical information presented as fact
   - C) A DDoS attack targeting an Application Load Balancer
   - D) A network packet drop between Availability Zones
4. **Which AWS service standardizes model documentation, governance, intended use cases, and ethical evaluation results into structured metadata cards?**
   - A) Amazon SageMaker Model Cards
   - B) AWS CloudTrail
   - C) AWS Config
   - D) AWS Systems Manager
5. **How does Amazon Bedrock handle customer data privacy?**
   - A) Prompts are retained to improve public AI models
   - B) Customer prompts and outputs are NEVER used to train base foundation models and are encrypted
   - C) Data is shared with model creators without customer knowledge
   - D) Encryption requires purchasing an Enterprise Support plan

---

### Answer Key & Explanations
| Q# | Answer | Key Concept Reference |
| :---: | :---: | :--- |
| **1** | **B** | Bedrock Guardrails applies configurable safety filters, topic bans, and PII masking. |
| **2** | **A** | SageMaker Clarify computes SHAP values to explain how each feature influences predictions. |
| **3** | **B** | Hallucinations are confident generations of factually untrue or fabricated statements. |
| **4** | **A** | SageMaker Model Cards record factual model documentation, training lineage, and evaluation metrics. |
| **5** | **B** | Amazon Bedrock guarantees customer inputs/outputs are never used to train base foundation models. |
