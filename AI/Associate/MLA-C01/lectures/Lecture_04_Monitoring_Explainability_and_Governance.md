# Lecture 04: Model Monitoring, Explainability & Governance

> **Course Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Domain 4: ML Solution Monitoring and Maintenance (24%)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Differentiate between Data Drift, Concept Drift, Prior Probability Shift, and Feature Attribution Drift.
2. Configure Amazon SageMaker Model Monitor to continuously detect data quality and model quality violations.
3. Detect pre-training and post-training bias and generate local/global feature attributions using SageMaker Clarify and SHAP values.
4. Document models using SageMaker Model Cards and enforce guardrails via Amazon Bedrock Guardrails.

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:15] 1. The Drift Taxonomy: Data Drift vs. Concept Drift vs. Prior Probability Shift
[01:15 - 02:45] 2. Amazon SageMaker Model Monitor Architecture & CloudWatch Alarms
[02:45 - 04:15] 3. Bias Detection & SHAP Explainability with Amazon SageMaker Clarify
[04:15 - 05:15] 4. Model Governance: Model Cards, Bedrock Guardrails & Data Privacy
[05:15 - 06:00] 5. Exam Preparation Recap & Mock Exam Strategy
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. The Drift Taxonomy (Whiteboard Diagram)
- **Data Drift (Covariate Shift):**
  - $P(X)$ changes, $P(y|X)$ stays the same.
  - Example: User age distribution changes from 20s to 50s.
  - *Can be detected immediately on raw input payloads without ground truth!*
- **Concept Drift:**
  - $P(y|X)$ changes, $P(X)$ stays the same.
  - Example: Macroeconomic inflation causes higher credit default for the same income level.
  - *Requires ground-truth labels uploaded to S3 post-inference!*

### 2. SageMaker Clarify: Bias & Explainability
- **Pre-Training Bias:** Checked on raw training data before training.
  - Class Imbalance (CI)
  - Difference in Positive Proportions in Labels (DPPL)
  - Disparate Impact (DI)
- **Explainability (SHAP - Shapley Additive Explanations):**
  - Based on cooperative game theory.
  - Quantifies how much each feature pushed the prediction away from the baseline average.
  - Local Explainability: Explaining Jane Doe's individual loan denial.
  - Global Explainability: Ranking feature importance across the entire enterprise dataset.

### 3. Bedrock Guardrails & Data Privacy
- Bedrock Zero-Retention Guarantee: Customer prompts and completions are NEVER used to train base foundation models and NEVER shared with model providers.
- Guardrails: Denied topics, content filters (hate, violence), PII masking (SSNs, credit cards), and **Contextual Grounding** to detect and block hallucinations.

---

## 💻 Classroom Live Demo Walkthrough (5 Minutes)

1. Show a `constraint_violations.json` output file from Model Monitor in CloudShell.
2. Inspect a SageMaker Model Card in the AWS Console, showing pre-attached Clarify SHAP plots and export-to-PDF functionality.

---

## 🎯 High-Yield Exam Traps for this Lecture

1. **Trap:** Expecting Model Quality monitoring to work without uploading ground truth.  
   *Correction:* Model Quality monitoring strictly requires ground-truth labels in S3 to match against inference prediction IDs.
2. **Trap:** Removing the sensitive feature column (e.g., 'Gender') to prevent bias.  
   *Correction:* Removing the column is ineffective because proxy variables (e.g., shopping habits, clubs) reproduce the bias. Use SageMaker Clarify to measure disparate impact across proxy correlations.
