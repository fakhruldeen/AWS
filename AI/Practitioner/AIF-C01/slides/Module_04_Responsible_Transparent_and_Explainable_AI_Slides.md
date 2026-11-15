---
marp: true
theme: default
paginate: true
header: "AWS Certified AI Practitioner (AIF-C01) | Module 4: Responsible AI"
footer: "© Mohamed Fakhruldeen — fakhruldeen/AWS"
style: |
  section {
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    background-color: #f8fafc;
  }
  h1 { color: #0f172a; }
  h2 { color: #2563eb; }
  footer { font-size: 0.75rem; color: #64748b; }
---

# AWS Certified AI Practitioner (AIF-C01)
## Module 4: Guidelines for Responsible, Transparent & Explainable AI

**Instructor:** Mohamed Fakhruldeen  
**Track:** AI Practitioner (`AIF-C01`)  
**Exam Weight:** 14%  
**Repository:** `fakhruldeen/AWS`

---

# Domain 4 Blueprint Alignment

1. **Responsible AI Pillars:** Fairness, Explainability, Transparency, Privacy, Safety, Veracity, Governance.
2. **Bias Detection with SageMaker Clarify:** Pre-training (CI, DPL) and Post-training (Disparate Impact).
3. **Model Explainability:** SHAP (Shapley Additive exPlanations) local and global feature attribution.
4. **Safety & Guardrails:** Amazon Bedrock Guardrails (Denied Topics, Content Filters, PII Masking, Grounding).
5. **Model Governance & Auditing:** SageMaker Model Cards and Model Registry approval gates.

---

# The 7 Core Pillars of Responsible AI

1. **Fairness:** Equitable outcomes across sensitive demographic facets (gender, race, age).
2. **Explainability:** Providing transparent rationales for automated model predictions.
3. **Privacy & Security:** Safeguarding PII and preventing training data leakage.
4. **Transparency:** Documenting model provenance, intended use, and limitations.
5. **Veracity (Truthfulness):** Mitigating hallucinations and fact fabrication.
6. **Robustness & Safety:** Resisting adversarial prompt injection and jailbreaks.
7. **Accountability:** Establishing clear human ownership and governance approval gates.

---

# Bias Metrics with Amazon SageMaker Clarify

* **Pre-Training Bias (In the Training Dataset):**
  * **Class Imbalance (CI):** Measures proportional under-representation of a demographic facet.
  * **Difference in Positive Proportions (DPL):** Disparity in favorable labels assigned in historical data.
* **Post-Training Bias (In Model Inferences):**
  * **Disparate Impact (DI):** Ratio of positive prediction rates for disfavored vs favored groups.
  $$\text{DI} = \frac{P(\hat{Y}=1 | \text{Disfavored})}{P(\hat{Y}=1 | \text{Favored})}$$
  * A DI below $0.80$ triggers regulatory scrutiny under anti-discrimination guidelines.

---

# Model Explainability with SHAP Values

* **SHAP (Shapley Additive exPlanations):**
  * Grounded in cooperative game theory.
  * Measures the exact marginal contribution of each feature toward a prediction.
* **Global Explainability:**
  * Which features drive the model's overall predictions across the entire population?
  * Example: *Credit Score* and *Debt-to-Income* are top global drivers.
* **Local Explainability:**
  * Why was *Applicant #1042* rejected?
  * Example: High debt ratio contributed $+0.42$ risk score, low tenure $+0.18$.

---

# Amazon Bedrock Guardrails: Multi-Layered Perimeter

1. **Denied Topics:** Blocks forbidden conversational domains (e.g., tax advice, medical diagnosis).
2. **Content Filters:** 4 categories (Hate, Insults, Sexual, Violence) with Low/Med/High thresholds.
3. **Sensitive Information (PII):** Predefined entities (SSN, credit card, phone) + Custom Regex.
   * Actions: **Block** (halts generation) or **Anonymize / Mask** (replaces with `[EMAIL]`).
4. **Contextual Grounding Check (v1.2 Feature):**
   * Verifies response is factually grounded in retrieved RAG documents.
   * Mitigates hallucinations before output reaches end users.

---

# Model Governance: Model Cards & Registry

* **Amazon SageMaker Model Cards:**
  * Standardized digital documentation artifact.
  * Captures: Intended purpose, out-of-scope uses, bias evaluation scores, risk tiers.
  * Serves as compliance audit evidence for regulators.
* **Amazon SageMaker Model Registry:**
  * Catalogs versioned model packages.
  * Manages approval workflow: `PendingManualApproval` $\rightarrow$ `Approved`.
  * Integrates with CI/CD deployment pipelines.

---

# Domain 4 Exam Highlights

* ⚡ **Detecting Bias in Unprocessed Training Data?** $\rightarrow$ SageMaker Clarify (Class Imbalance, DPL).
* ⚡ **Explaining Single-Applicant Loan Rejections?** $\rightarrow$ Local SHAP Feature Attribution.
* ⚡ **Masking PII across Multiple LLMs?** $\rightarrow$ Amazon Bedrock Guardrails Sensitive Info Policy.
* ⚡ **Standardized Compliance Documentation?** $\rightarrow$ SageMaker Model Cards.
