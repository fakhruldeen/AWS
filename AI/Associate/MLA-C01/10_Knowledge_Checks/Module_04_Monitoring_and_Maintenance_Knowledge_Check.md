# Module 04: ML Solution Monitoring & Maintenance — Knowledge Check

> **Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Module 4: Data Drift, Concept Drift, SageMaker Model Monitor, Clarify & Model Cards  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 4 materials and completing Labs 03 & 05. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
A real-time fraud detection model begins experiencing a statistical shift where the distribution of incoming transaction amounts changes dramatically, but the relationship between transaction amount and fraud probability remains constant. What type of drift is this, and which AWS tool detects it?

- **A.** **Data Drift (Covariate Shift)**; detected by **Amazon SageMaker Model Monitor (Data Quality)**.
- **B.** Concept Drift; detected by AWS CloudTrail.
- **C.** Hardware degradation; detected by CloudWatch Synthetics.
- **D.** Network latency drift; detected by AWS Global Accelerator.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Data Drift (Covariate Shift)** occurs when the distribution of input features $P(X)$ changes over time while the conditional probability $P(y|X)$ remains unchanged. SageMaker Model Monitor Data Quality continuously captures live endpoint payloads and compares them against baseline `statistics.json` and `constraints.json` without requiring ground truth labels.
</details>

---

### Question 2
What is the fundamental operational difference between SageMaker Model Monitor **Data Quality** monitoring and **Model Quality** monitoring?

- **A.** Data Quality monitors input feature distributions and schema rules without needing ground truth; Model Quality measures predictive accuracy (Accuracy, F1, RMSE) and strictly requires uploading ground-truth labels to S3 post-inference.
- **B.** Data Quality only runs on GPUs while Model Quality runs on CPUs.
- **C.** Data Quality works only for computer vision while Model Quality is for tabular data.
- **D.** There is no difference; they are aliases for the same CloudWatch metric.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
You cannot evaluate true model performance (Precision, Recall, F1, MSE) without knowing the real-world outcome! Therefore, **Model Quality monitoring requires ground-truth labels** to be uploaded to Amazon S3, which SageMaker matches against captured prediction IDs.
</details>

---

### Question 3
An ML engineer wants to explain why a specific customer was denied a mortgage application. Which mathematical game-theoretic methodology used by **Amazon SageMaker Clarify** calculates the exact marginal contribution of each input feature to the individual decision?

- **A.** SHAP (Shapley Additive Explanations)
- **B.** Gini Impurity
- **C.** Pearson Correlation Coefficient
- **D.** Mean Squared Logarithmic Error

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**SHAP (Shapley Additive Explanations)** is based on cooperative game theory. It treats features as players in a coalition, computing the fair marginal contribution (Shapley value) of each feature to the difference between the actual prediction and the average baseline prediction.
</details>

---

### Question 4
In Amazon SageMaker Clarify pre-training bias metrics, what does a **Difference in Positive Proportions in Labels (DPPL)** value significantly greater than zero indicate?

- **A.** Historical training labels have a higher positive outcome rate (e.g., loan approval rate) for the favored facet group compared to the disfavored group.
- **B.** The training job crashed due to out-of-memory errors.
- **C.** The model is 100% free of demographic bias.
- **D.** The dataset has zero missing values.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
$$\text{DPPL} = q_a - q_d$$
where $q_a$ is the proportion of positive labels in the favored facet (e.g., Male) and $q_d$ is the proportion in the disfavored facet (e.g., Female). When DPPL > 0, the historical dataset reflects a historical disparity favoring group $a$.
</details>

---

### Question 5
What is the primary function of **Amazon SageMaker Model Cards**?

- **A.** Providing standardized, auditable documentation acting as a "fact sheet" or "nutrition label" for ML models, capturing intended use, training parameters, evaluation metrics, and governance sign-offs.
- **B.** Graphically rendering 3D neural network layers in the browser.
- **C.** Providing credit card processing APIs.
- **D.** Compressing model weights to 4-bit precision.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**SageMaker Model Cards** centralize and standardize model documentation throughout the lifecycle. They document intended use cases, risk assessments, evaluation results from Clarify, and approval signatures, and can be exported as official PDF compliance reports for external regulators.
</details>

---

### Question 6
An enterprise deploys a foundation model on Amazon Bedrock. To comply with strict corporate safety rules, the application must block hate speech, prevent investment advice, and automatically redact customer Social Security numbers and phone numbers from both user prompts and model completions. Which native feature should be configured?

- **A.** Amazon Bedrock Guardrails (Content Filters, Denied Topics, and Sensitive Information Filters)
- **B.** Writing custom regex logic in client mobile apps.
- **C.** Fine-tuning the base model using RLHF.
- **D.** Creating an AWS WAF IP rate limit rule.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Amazon Bedrock Guardrails** provides an independent, centralized policy engine that enforces content filters, denied topics, word filters, and PII masking across multiple foundation models on both input prompts and generated responses.
</details>

---

### Question 7
What is **Contextual Grounding** in Amazon Bedrock Guardrails, and what specific Generative AI issue does it detect and mitigate?

- **A.** Evaluates whether a generated response is factually grounded in the retrieved source context to detect and block **Hallucinations**.
- **B.** Evaluates whether an EC2 instance is connected to physical ground wiring.
- **C.** Measures GPU memory bandwidth utilization.
- **D.** Checks whether the user is located in a supported geographic region.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
Contextual Grounding Checks in Bedrock Guardrails analyze whether the model's response is factually supported by reference context (detecting hallucinations) and whether the response directly addresses the user's inquiry (relevance filter).
</details>

---

### Question 8
What type of attack occurs when an attacker embeds malicious instructions inside an external PDF document or web page that an LLM retrieves and processes, causing the model to disobey its original system prompt?

- **A.** Indirect Prompt Injection
- **B.** Direct Prompt Injection (Jailbreaking)
- **C.** SQL Injection
- **D.** SYN Flood Attack

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Indirect Prompt Injection** occurs when adversarial instructions enter the model through untrusted external data (such as emails, uploaded resumes, web search results) rather than the primary user interface prompt.
</details>

---

### Question 9
How does Amazon Bedrock ensure **customer data privacy** when an organization invokes foundation models from third-party providers (such as Anthropic Claude or Meta Llama)?

- **A.** Customer prompts and completions are **never used to train base models** and are **never shared with third-party model providers**.
- **B.** Data is transmitted to third-party public cloud endpoints in plaintext.
- **C.** Models are retrained on customer prompts every 24 hours.
- **D.** Data is stored in public S3 buckets for open-source researchers.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
AWS guarantees that customer data (prompts, completions, custom fine-tuning data) is strictly private, remains within the customer's selected AWS region, is never used to train or improve base foundation models, and is never shared with third-party model providers.
</details>

---

### Question 10
Which international standard published in 2023 specifies the requirements for establishing, implementing, maintaining, and continually improving an **Artificial Intelligence Management System (AIMS)**?

- **A.** ISO/IEC 42001:2023
- **B.** ISO 9001
- **C.** PCI-DSS v4.0
- **D.** SOC 2 Type II

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**ISO/IEC 42001** is the world's first certifiable standard for Artificial Intelligence Management Systems (AIMS). It provides an overarching framework for organizations to develop, deploy, and govern AI systems responsibly, ethically, and in compliance with global regulations like the EU AI Act.
</details>
