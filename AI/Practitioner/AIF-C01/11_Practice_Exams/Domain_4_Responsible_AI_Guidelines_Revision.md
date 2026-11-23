# Domain 4 Revision Questions: Guidelines for Responsible AI

> **Domain:** Domain 4: Guidelines for Responsible AI (14% Exam Weight)  
> **Question Count:** 15 Comprehensive Scenario-Based Questions  
> **Format:** Multiple Choice & Multiple Response with Detailed Explanations

---

### Question 1
A loan origination chatbot must be prevented from offering binding legal advice or drafting mortgage agreements. Which capability within Amazon Bedrock Guardrails should the administrator configure?
- [ ] A) Word Filters
- [ ] B) Denied Topics Policy
- [ ] C) Sensitive Information Policy
- [ ] D) Content Filters
> **Correct Answer:** B  
> **Rationale:** Denied Topics allows architects to define off-limits conversational subjects using natural language descriptions and example phrases to prevent the model from engaging in forbidden topics.

---

### Question 2
Before training a predictive hiring model, a data scientist uses Amazon SageMaker Clarify to evaluate the training dataset. The report indicates a Difference in Positive Proportions in Labels (DPL) of $+0.38$ favoring male candidates over female candidates. What does this metric indicate?
- [ ] A) Male candidates have 38% higher accuracy scores on test exams.
- [ ] B) Historical hiring data awarded positive outcomes (hires) to male applicants at a significantly higher rate than female applicants.
- [ ] C) The model weights are corrupted and must be re-initialized.
- [ ] D) Female applicants submitted 38% more resumes.
> **Correct Answer:** B  
> **Rationale:** DPL ($q_a - q_d$) measures label disparity in raw historical data. A positive DPL indicates that the favored group historically received more positive outcomes, signaling pre-training bias.

---

### Question 3
An applicant whose mortgage pre-approval was denied requests an explanation under consumer financial protection regulations. Which explainability technique provided by SageMaker Clarify explains the specific reasons for this individual decision?
- [ ] A) Global Feature Importance ranking
- [ ] B) Local SHAP (Shapley Additive exPlanations) feature attribution
- [ ] C) ROUGE-L sequence alignment
- [ ] D) Confusion Matrix accuracy score
> **Correct Answer:** B  
> **Rationale:** Local SHAP values quantify the exact marginal contribution (positive or negative) of each feature toward an individual applicant's specific prediction score.

---

### Question 4
An enterprise chatbot deployed across multiple models (Amazon Nova Pro and Claude 3.5 Sonnet) must automatically redact customer email addresses and phone numbers in chat transcripts. Which service provides a centralized PII masking layer across all models?
- [ ] A) SageMaker Canvas Quick Build
- [ ] B) Amazon Bedrock Guardrails Sensitive Information Filters (Anonymize)
- [ ] C) Amazon CloudWatch Alarms
- [ ] D) AWS IAM Permission Boundaries
> **Correct Answer:** B  
> **Rationale:** Bedrock Guardrails sits as an independent perimeter that intercepts prompts and completions, replacing detected PII entities with tags like `[EMAIL]` across any foundation model.

---

### Question 5
A predictive recidivism model is evaluated using SageMaker Clarify. The post-training analysis reveals a Disparate Impact (DI) score of $0.62$ for minority demographic groups. What does this score indicate?
- [ ] A) The model meets legal lending thresholds under the 80% rule.
- [ ] B) The model exhibits adverse disparate impact, predicting positive outcomes for the minority group at only 62% of the rate of the majority group.
- [ ] C) The model is 62% accurate on unseen test data.
- [ ] D) The dataset is completely balanced with zero bias.
> **Correct Answer:** B  
> **Rationale:** Disparate Impact is the ratio of positive prediction rates: $P(\hat{Y}=1 | \text{Disfavored}) / P(\hat{Y}=1 | \text{Favored})$. Scores below $0.80$ indicate adverse impact and potential algorithmic bias.

---

### Question 6
Which Amazon Bedrock Guardrail capability specifically detects whether a generated response hallucinated claims that are unsupported by the reference documents retrieved during RAG?
- [ ] A) Word Filter Blocklist
- [ ] B) Contextual Grounding Check
- [ ] C) Content Policy High Threshold
- [ ] D) Denied Topics Evaluation
> **Correct Answer:** B  
> **Rationale:** The Contextual Grounding filter evaluates both Grounding (factual adherence to retrieved reference chunks) and Relevance (direct alignment with user intent) to block hallucinations.

---

### Question 7
What is the primary purpose of an Amazon SageMaker Model Card in an enterprise AI governance framework?
- [ ] A) To provide a standardized digital artifact documenting model intended use, limitations, Clarify bias metrics, and compliance sign-offs for audits
- [ ] B) To store encrypted GPU passwords
- [ ] C) To act as a billing invoice sent to the accounting department
- [ ] D) To compile Python code into C++ binaries
> **Correct Answer:** A  
> **Rationale:** SageMaker Model Cards act as standardized governance records, centralizing intended purpose, training data profiles, evaluation benchmarks, and risk ratings for regulatory auditing.

---

### Question 8
What legal protection does AWS provide to enterprise customers using Amazon Titan foundation models against third-party copyright claims?
- [ ] A) Free AWS support tier upgrades
- [ ] B) Intellectual Property (IP) Indemnification
- [ ] C) Exemption from GDPR compliance
- [ ] D) Automated patent filings
> **Correct Answer:** B  
> **Rationale:** AWS provides IP indemnification for Amazon Titan models, defending customers against copyright infringement allegations arising from generated outputs.

---

### Question 9
In the Amazon SageMaker Model Registry, why do newly registered models enter the registry with a status of `PendingManualApproval`?
- [ ] A) Because the EC2 instances are paused
- [ ] B) To enforce a human-in-the-loop governance gate requiring technical and compliance sign-off before production deployment
- [ ] C) Because the AWS account is out of credits
- [ ] D) To prevent Python from compiling
> **Correct Answer:** B  
> **Rationale:** Gated approvals in Model Registry ensure that models cannot be deployed into production without explicit verification of evaluation metrics and governance compliance.

---

### Question 10 (Multiple Response)
Which TWO filters within Amazon Bedrock Guardrails are specifically designed to address toxic language and adversarial abuse? (Select TWO.)
- [ ] A) Content Filters with configurable severity thresholds for Hate, Insults, Sexual, and Violence
- [ ] B) Word Filters with customizable blocklists for profanity and derogatory slurs
- [ ] C) Amazon CloudFront Origin Shield
- [ ] D) AWS Auto Scaling Group Target Tracking
- [ ] E) Amazon S3 Glacier Flexible Retrieval
> **Correct Answers:** A, B  
> **Rationale:** Content filters and custom word filter blocklists directly inspect text to filter hate speech, violence, insults, and profanity.

---

### Question 11
What is the distinction between Class Imbalance (CI) and Difference in Positive Proportions in Labels (DPL) in SageMaker Clarify?
- [ ] A) CI measures the proportion of samples between demographic groups; DPL measures the difference in positive outcome labels between those groups.
- [ ] B) CI is evaluated after training; DPL is evaluated before training.
- [ ] C) CI applies only to regression; DPL applies only to clustering.
- [ ] D) CI evaluates GPU memory; DPL evaluates disk storage.
> **Correct Answer:** A  
> **Rationale:** Class Imbalance checks if demographic representation is numerically skewed in the dataset. DPL checks if historical positive target labels were distributed unfairly.

---

### Question 12
A hospital trains an image classification model to detect skin lesions. The training dataset consists of 95% light-skinned patients and 5% dark-skinned patients. What type of bias does this dataset exhibit?
- [ ] A) Algorithmic Convergence Bias
- [ ] B) Sampling / Representation Bias (Class Imbalance)
- [ ] C) Confirmation Bias
- [ ] D) Deployment Drift
> **Correct Answer:** B  
> **Rationale:** Sampling bias occurs when the collected dataset does not accurately reflect the diversity of the real-world population that the model will serve.

---

### Question 13
How does Amazon Titan Image Generator assist in verifying the synthetic provenance of images to prevent misinformation and deepfakes?
- [ ] A) It adds a visible red border around every image
- [ ] B) It embeds an invisible, tamper-resistant digital watermark into the pixel data of all generated images
- [ ] C) It emails a copy of the image to AWS Support
- [ ] D) It limits resolution to 256x256 pixels
> **Correct Answer:** B  
> **Rationale:** Titan Image Generator automatically embeds invisible watermarks that survive compression and cropping, allowing automated detection of AI-generated images.

---

### Question 14
Which pillar of Responsible AI focuses on understanding the internal decision logic of an AI model rather than treating it as an opaque black box?
- [ ] A) Explainability & Interpretability
- [ ] B) Security
- [ ] C) Controllability
- [ ] D) Cost Efficiency
> **Correct Answer:** A  
> **Rationale:** Explainability ensures that models provide understandable rationales for their predictions to build trust and satisfy regulatory audits.

---

### Question 15
An architect wants to verify that Bedrock Guardrail interventions are logged and tracked over time. Where can the security team inspect metrics on how often guardrails blocked toxic inputs?
- [ ] A) Amazon CloudWatch Metrics (e.g., `InvocationsIntervened`)
- [ ] B) AWS Route 53 Health Checks
- [ ] C) AWS Trusted Advisor Cost Reports
- [ ] D) Amazon DynamoDB Streams
> **Correct Answer:** A  
> **Rationale:** Amazon Bedrock Guardrails emits detailed operational metrics into Amazon CloudWatch, allowing teams to monitor intervention counts and trigger security alarms.
