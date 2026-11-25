# Module 04 Knowledge Check: Guidelines for Responsible AI

> **Domain:** Domain 4: Guidelines for Responsible AI (14% Weight)  
> **Questions:** 10 Diagnostic Questions with Answers & Rationales

---

### Questions

1. **Which Amazon Bedrock Guardrail policy allows administrators to block conversations discussing forbidden business domains, such as medical advice or investment suggestions?**
   - A) Content Policy
   - B) Denied Topics Policy
   - C) Sensitive Information Policy
   - D) Contextual Grounding Policy

2. **In SageMaker Clarify, which pre-training metric measures whether historical labels in a training dataset favored one demographic group over another?**
   - A) Class Imbalance (CI)
   - B) Difference in Positive Proportions in Labels (DPL)
   - C) Root Mean Squared Error (RMSE)
   - D) Disparate Impact (DI)

3. **What is the primary function of SHAP (Shapley Additive exPlanations) values in machine learning explainability?**
   - A) To encrypt model training weights using KMS
   - B) To quantify the exact marginal contribution of each input feature toward a specific prediction
   - C) To compress neural network layers for mobile deployment
   - D) To eliminate overfitting automatically

4. **A customer care chatbot must ensure that credit card numbers and Social Security numbers entered by users are completely redacted before reaching the foundation model. Which feature accomplishes this?**
   - A) SageMaker Canvas Quick Build
   - B) Amazon Bedrock Guardrails Sensitive Information Filters (Anonymize / Mask)
   - C) Amazon Comprehend Custom Classification
   - D) AWS CloudTrail Insights

5. **Which post-training metric evaluated by SageMaker Clarify computes the ratio of favorable predictions between disfavored and favored demographic groups?**
   - A) Disparate Impact (DI)
   - B) Cosine Similarity
   - C) Confusion Accuracy
   - D) Mean Absolute Error (MAE)

6. **What is an Amazon SageMaker Model Card?**
   - A) A physical hardware GPU acceleration board
   - B) A standardized digital governance document recording intended use, evaluation benchmarks, limitations, and risk ratings
   - C) A credit card for purchasing SageMaker compute credits
   - D) A visualization tool for plotting real-time inference latency

7. **Which Amazon Bedrock Guardrail capability specifically detects hallucinations in RAG applications by validating that generated responses adhere to retrieved documents?**
   - A) Word Filter
   - B) Contextual Grounding Check
   - C) PII Regex Policy
   - D) Model Evaluation Job

8. **What protection does AWS provide to enterprise customers against third-party copyright infringement claims arising from the use of Amazon Titan foundation models?**
   - A) Free Tier credit rebates
   - B) Intellectual Property (IP) Indemnification
   - C) Automatic source code generation
   - D) CloudFront edge caching

9. **In the SageMaker Model Registry, what is the default status assigned to newly registered model packages before they are approved for production deployment?**
   - A) `Approved`
   - B) `PendingManualApproval`
   - C) `Archived`
   - D) `Active`

10. **Which pillar of Responsible AI addresses ensuring that automated AI systems do not disproportionately disadvantage protected demographic groups?**
    - A) Veracity
    - B) Fairness
    - C) Robustness
    - D) Controllability

---

### Answer Key & Explanations

| Q# | Answer | Key Concept Reference | Detailed Explanation |
|:---:|:---:|:--- |:--- |
| **1** | **B** | Denied Topics | Denied Topics define high-level conversational boundaries using natural language instructions and sample phrases. |
| **2** | **B** | DPL (Pre-Training Bias) | DPL measures $q_a - q_d$ (the difference in favorable outcome rates between demographic facets in historical training data). |
| **3** | **B** | SHAP Values | Grounded in cooperative game theory, SHAP values explain individual and global feature importance. |
| **4** | **B** | Sensitive Information Filters | Bedrock Guardrails can either `ANONYMIZE` (mask with placeholders) or `BLOCK` predefined PII entities and regexes. |
| **5** | **A** | Disparate Impact | Disparate Impact ($DI$) calculates the ratio of positive prediction rates. Values <0.80 indicate adverse disparate impact. |
| **6** | **B** | SageMaker Model Cards | Model Cards provide an auditable source of truth detailing model intended uses, risk ratings, and evaluation benchmarks. |
| **7** | **B** | Contextual Grounding Check | Contextual Grounding filters score responses for Grounding (factual adherence to RAG docs) and Relevance to the user query. |
| **8** | **B** | IP Indemnification | AWS offers intellectual property indemnification for customers using Amazon Titan foundation models. |
| **9** | **B** | Model Registry Status | Model versions enter as `PendingManualApproval` to ensure compliance and technical review before production rollout. |
| **10** | **B** | Fairness | Fairness ensures unbiased, equitable treatment across sensitive facets (race, gender, age). |
