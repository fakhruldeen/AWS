# Lecture 05: Security, Compliance, and Governance for AI Solutions

> **Course Track:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Target Exam Domain:** Domain 5: Security, Compliance, and Governance (14% of Exam Blueprint)  
> **Estimated Delivery Duration:** 90 Minutes  
> **Associated Slide Deck:** `slides/Module_05_Security_Compliance_and_Governance_Slides.md`  
> **Target Hands-On Labs:** `labs/Lab_05_Securing_Bedrock_with_PrivateLink_and_IAM.md`, `labs/Lab_10_Data_Privacy_Auditing_with_Amazon_Macie.md` & `labs/Lab_12_AI_Security_Auditing_with_AWS_CloudTrail.md`  
> **Student Explanations:** `explanations/05_Domain_5_Security_Compliance_and_Governance.md`

---

## 📚 Prescribed Textbook Reading & Literature Grounding

Before delivering or attending this lecture, review the assigned chapters:
* **Vikram Elango, Vivek Gangasani, Shreyas Subramanian (*Wiley / Sybex 2025*):**
  * Chapter 10: *Security, Compliance, and Governance for AI Systems* (pp. 415–462)
    * The Generative AI Security Scoping Matrix: Shared responsibility across Scopes 1, 2, 3, and 4.
    * Amazon Bedrock data privacy, residency, and tenancy guarantees (zero training on customer prompts).
    * Identity and access management (IAM) least privilege, Bedrock model access permissions, and Agent execution roles.
    * Network perimeter protection: AWS PrivateLink (VPC Interface Endpoints), VPC Endpoint Policies, security groups.
    * Data security and cryptographic controls: AWS KMS Customer Managed Keys (CMK), envelope encryption, Amazon Macie sensitive data discovery.
    * Auditing, monitoring, and compliance logging: AWS CloudTrail (management vs data events), Bedrock Model Invocation Logging, AWS Artifact.
* **Tom Taulli (*O'Reilly 2025*):**
  * Chapter 6: *Responsible AI, Ethics, and Governance* (pp. 123–148)
    * Regulatory frameworks: EU AI Act, NIST AI Risk Management Framework (AI RMF), HIPAA, and GDPR.
* **CloudExamPro AIF-C01 Master Cheat Sheet (2026 Edition):**
  * Section 5: *Security, Governance, Data Privacy, Compliance, and AWS Artifact* (pp. 21–25)
* **Notezio AIF-C01 Master Guide (2026):**
  * Chapters 21–23: *Bedrock Data Isolation, PrivateLink Security, IAM Policies, CloudTrail Logging, and KMS Encryption*.

---

## ⏱️ Detailed 90-Minute Delivery Schedule & Pacing

```
00:00 - 00:15 | Generative AI Security Scoping Matrix: Shared Responsibility across Scopes 1, 2, 3 & 4
00:15 - 00:35 | Data Privacy & Residency in Amazon Bedrock: Zero Retention Pledge, Tenant Isolation & PrivateLink
00:35 - 00:55 | Identity & Access Governance: IAM SigV4, Bedrock Model Access & Least-Privilege Agent Roles
00:55 - 01:15 | Auditing & Compliance Infrastructure: CloudTrail Data Events, Model Invocation Logging & Macie
01:15 - 01:25 | Cryptography & Artifact: AWS KMS CMK Envelope Encryption & AWS Artifact Compliance Reports
01:25 - 01:30 | Socratic Q&A & Transition to Lab 05, Lab 10 & Lab 12
```

---

## 🎯 Core Learning Objectives
By the end of this lecture, students will be able to:
1. Explain the **Generative AI Security Scoping Matrix** and assign security responsibilities accurately.
2. Articulate Amazon Bedrock's data privacy guarantees (zero model training on customer prompts).
3. Architect network isolation for Generative AI using **AWS PrivateLink** and VPC Endpoint Policies.
4. Enforce least-privilege access using **AWS IAM** and **Bedrock Agent Execution Roles**.
5. Implement end-to-end auditability using **AWS CloudTrail**, **Model Invocation Logging**, **Amazon Macie**, and **AWS KMS**.

---

## 🗣️ Instructor Delivery Guide & Key Talking Points

### 1. The Generative AI Security Scoping Matrix (00–15m)
* **The Paradigm:** Draw the 4 scopes on the whiteboard. Emphasize that security responsibility is not static in Generative AI—it slides based on architectural ownership:
  * *Scope 1 (Consumer SaaS):* Customer has zero control over underlying training data or architecture; highest risk of proprietary data leakage.
  * *Scope 2 (Enterprise Managed Services):* Amazon Bedrock and Amazon Q. AWS owns model weights, hypervisor, and physical safety; customer owns IAM policies, data sanitation, and Bedrock Guardrails.
  * *Scope 3 (Fine-Tuning & RAG):* Customer becomes responsible for curating, sanitizing, and access-controlling private documents in S3 and vector embeddings in OpenSearch Serverless.
  * *Scope 4 (Pre-training from scratch on EC2/SageMaker):* Complete customer ownership of ethics, bias, copyright compliance, and hardware infrastructure.
* **Exam Tip:** Whenever an exam scenario asks who is responsible for preventing prompt injection in an application built on Amazon Bedrock, the answer is the **Customer** (via Amazon Bedrock Guardrails).

---

### 2. Bedrock Data Privacy & Network Isolation (15–35m)
* **AWS Zero-Training Guarantee:** Reiterate forcefully that AWS does **not** use customer prompts or completions to train base foundation models, nor are they shared with third-party model providers (Anthropic, Meta, Mistral).
* **Multi-Tenant Isolation:** Bedrock runs FMs within AWS-managed virtual enclaves. Inferences from Customer A and Customer B are strictly isolated at the hypervisor level.
* **Network Isolation with AWS PrivateLink:**
  * Public internet traversal is prohibited for HIPAA/PCI-DSS workloads.
  * Deploy **AWS PrivateLink** interface endpoints (`com.amazonaws.<region>.bedrock-runtime`) into private subnets.
  * All inference calls travel over AWS's private global fiber network without traversing the public internet.
  * Attach **VPC Endpoint Policies** to restrict traffic so that only specific IAM roles or specific Bedrock model ARNs can be accessed from that VPC.

---

### 3. Identity & Access Governance: Least Privilege (35–55m)
* **Model Access Controls:** In Amazon Bedrock, all foundation models are disabled by default. Administrators must explicitly request model access in the AWS Management Console per account and region.
* **IAM Policy Granularity:**
  * Use condition keys to enforce specific model usage (e.g., `bedrock:modelId = "anthropic.claude-3-5-sonnet-20241022-v2:0"`).
  * Enforce guardrail attachment: require `bedrock:GuardrailIdentifier` in every `bedrock:InvokeModel` request.
* **Agent Least Privilege:** When an Amazon Bedrock Agent invokes AWS Lambda functions to execute action groups, it assumes an IAM Execution Role.
  * The role must grant permissions strictly to the target Lambda function ARN and target S3 buckets.
  * Never grant `AdministratorAccess` or wildcard `*` permissions to an autonomous agent.

---

### 4. Continuous Auditing with Macie, CloudTrail & KMS (55–75m)
* **Amazon Macie (Data Lake S3 Sanitization):**
  * Acts as the data lake bouncer. Before synchronizing enterprise documents into a Bedrock Knowledge Base vector index, Macie scans the source S3 bucket using machine learning and pattern matching to flag unmasked credit cards, SSNs, or passport numbers.
* **AWS CloudTrail (Management vs. Data Events):**
  * *Management Events:* Track who created, updated, or deleted a Bedrock Agent or Guardrail (enabled by default).
  * *Data Events:* Must be explicitly enabled to capture individual model invocation API calls (`InvokeModel`, `InvokeModelWithResponseStream`).
* **Bedrock Model Invocation Logging:**
  * Captures the full input prompt and output completion text for regulatory audits.
  * Directs logs securely to **Amazon S3** or **Amazon CloudWatch Logs**, encrypted with AWS KMS.
* **AWS KMS Customer Managed Keys (CMK):**
  * Envelope encryption protects custom fine-tuned model weights, Knowledge Base vector embeddings in OpenSearch Serverless, and cached prompt data.

---

## 🏗️ Production Scenario: MedSecure Healthcare Diagnostic Assistant

* **Client:** *CareFirst Health*, operating 40 regional hospitals.
* **Challenge:** Deploy an AI clinical documentation assistant using Amazon Bedrock while maintaining strict HIPAA compliance, preventing patient health information (PHI) exposure, and ensuring full auditability.
* **Architecture Solution:**
  1. **Network Security:** Clinician tablets communicate via internal VPC with an AWS PrivateLink VPC Interface Endpoint to `bedrock-runtime`. No public internet gateway required.
  2. **Data Sanitation:** Amazon Macie scans patient records in S3 before ingestion into the Bedrock Knowledge Base.
  3. **Runtime Protection:** Amazon Bedrock Guardrails mask medical record numbers and patient names using custom regex and predefined PII filters.
  4. **Encryption:** S3 data source, OpenSearch Serverless vector collection, and Bedrock cache encrypted using an AWS KMS Customer Managed Key (CMK) with automated key rotation.
  5. **Auditing & Compliance:** Bedrock Model Invocation Logging enabled to an encrypted S3 audit bucket; AWS Artifact utilized to retrieve the official AWS HIPAA Business Associate Addendum (BAA).

---

## ❓ Socratic Discussion Questions & Classroom Engagement

1. **Question:** *"An insurance company wants to ensure employees cannot send sensitive claims data across the public internet when querying Amazon Bedrock. What should the architect deploy?"*
   * *Answer:* An **AWS PrivateLink VPC Interface Endpoint** for the Bedrock Runtime (`com.amazonaws.<region>.bedrock-runtime`).
2. **Question:** *"A healthcare provider must audit whether any S3 buckets intended for a RAG knowledge base contain exposed patient health identifiers. Which service is optimal?"*
   * *Answer:* **Amazon Macie**.
3. **Question:** *"Does CloudTrail standard logging automatically record the complete prompt text and model output of every Bedrock query?"*
   * *Answer:* No. CloudTrail standard management events record only the API call metadata (who, when, source IP, model ARN). To record the complete prompt and response text, you must enable **Bedrock Model Invocation Logging** directed to an encrypted S3 bucket or CloudWatch Logs.
4. **Question:** *"Where can an enterprise compliance officer download the AWS SOC 2 Type II report and HIPAA Business Associate Addendum (BAA)?"*
   * *Answer:* **AWS Artifact** (the central portal for on-demand access to AWS compliance reports and agreements).

---

## ⚠️ Exam Traps & "Watch Out For..."

> [!WARNING]
> **Trap 1: Third-Party Foundation Models and Data Privacy**  
> An exam question might ask if using Anthropic Claude in Bedrock shares customer data with Anthropic. **It does NOT.** All models in Bedrock run natively on AWS infrastructure; third-party model providers never receive customer prompt data.

> [!IMPORTANT]
> **Trap 2: CloudTrail Management vs Data Events vs Invocation Logging**  
> - Modifying a Bedrock Guardrail = **CloudTrail Management Event**.  
> - Invoking a model (`InvokeModel` API call) = **CloudTrail Data Event**.  
> - Recording the actual input prompt & output text = **Bedrock Model Invocation Logging**.

> [!TIP]
> **Trap 3: AWS Artifact vs AWS Audit Manager**  
> - **AWS Artifact:** Download AWS's own compliance documents (SOC reports, ISO certifications, BAA).  
> - **AWS Audit Manager:** Continuously audits the customer's *own* AWS environment to prepare customer audit reports.

---

## 📋 Post-Lecture Student Checklist & Lab Transition

- [ ] Complete **Lab 05:** `labs/Lab_05_Securing_Bedrock_with_PrivateLink_and_IAM.md`.
- [ ] Complete **Lab 10:** `labs/Lab_10_Data_Privacy_Auditing_with_Amazon_Macie.md`.
- [ ] Complete **Lab 12:** `labs/Lab_12_AI_Security_Auditing_with_AWS_CloudTrail.md`.
- [ ] Review `explanations/05_Domain_5_Security_Compliance_and_Governance.md`.
- [ ] Complete the Module 5 review quiz in `slides/Module_05_Security_Compliance_and_Governance_Slides.md`.


---

## 🎯 Authentic Exam Practice & Case Scenarios
> High-yield scenario questions from the authentic candidate practice pool reinforcing the core competencies of this lecture.

### Scenario Practice 1: AIF-C01-ET-Q142
**Question:**  
A hospital is developing an AI system to assist doctors in diagnosing diseases based on patient records and medical images. To comply with regulations, the sensitive patient data must not leave the country the data is located in.

Which data governance strategy will ensure compliance and protect patient privacy?

**Options:**
- A) Data residency
- B) Data quality
- C) Data discoverability
- D) Data enrichment

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `A`  
**Peer Consensus:** `100%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Ensures that sensitive data remains within the geographic boundaries of a specific country or region, helping to comply with data sovereignty and privacy regulations (such as HIPAA or GDPR).
---
Selected Answer: A
Data residency (residencia de datos) es una estrategia de gobernanza de datos que:

✔ Asegura que los datos permanezcan en una ubicación geográfica específica, según las regulaciones del país.
✔ Cumple con normativas de privacidad y seguridad como GDPR en Europa o HIPAA en EE.UU.
✔ Restringe el almacenamiento y procesamiento de datos fuera del país, evitando transferencias no permitidas.

En este caso, un hospital que maneja datos sensibles de pacientes debe asegurarse de que la información médica no se almacene ni procese fuera del país, lo que hace que Data residency sea la mejor estrategia.
---
Selected Answer: A
Only A talking about the data how to store

</details>

### Scenario Practice 2: AIF-C01-ET-Q015
**Question:**  
A global financial company has developed an ML application to analyze stock market data and provide stock market trends. The company wants to continuously monitor the application development phases and to ensure that company policies and industry regulations are followed.

Which AWS services will help the company assess compliance requirements? (Choose two.)

**Options:**
- A) AWS Audit Manager
- B) AWS Config
- C) Amazon Inspector
- D) Amazon CloudWatch
- E) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `B`  
**Peer Consensus:** `100%` agreement.  
> [!WARNING] Answer Distinction  
> Initial contributor marked `UB`, but community verified `B` with 100% consensus.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: B (100%). Contributor Answer: UB.

Community Rationale & Discussion:
Selected Answer: UB
Os dois serviços da AWS que ajudarão a empresa a avaliar os requisitos de conformidade são:

A. Gerenciador de Auditoria da AWS: Ele auxilia no gerenciamento contínuo de auditorias ao automatizar a coleta de evidências relacionadas à conformidade com as políticas da empresa e regulamentos do setor.

B. Configuração da AWS: Este serviço permite monitorar e avaliar configurações de recursos continuamente para garantir que estejam em conformidade com as políticas e regulamentos definidos.

</details>

### Scenario Practice 3: AIF-C01-ET-Q036
**Question:**  
An AI company periodically evaluates its systems and processes with the help of independent software vendors (ISVs). The company needs to receive email message notifications when an ISV's compliance reports become available.
Which AWS service can the company use to meet this requirement?

**Options:**
- A) AWS Audit Manager
- B) AWS Artifact
- C) AWS Trusted Advisor
- D) AWS Data Exchange

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `B`  
**Peer Consensus:** `67%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: B (67%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Artifacts has email notifications that notify you when a report is available.

---
Selected Answer: B
Portal that provides customers with on-demand access to AWS
compliance documentation and AWS agreements
• Artifact Reports - Allows you to download AWS security and compliance
documents from third-party auditors, like AWS ISO certifications, Payment
Card Industry (PCI), and System and Organization Control (SOC) reports
• Artifact Agreements - Allows you to review, accept, and track the status of
AWS agreements such as the Business Associate Addendum (BAA) or the
Health Insurance Portability and Accountability Act (HIPAA) for an individual
account or in your organization
---
Selected Answer: D
However, AWS Artifact is not designed for receiving notifications about third-party compliance reports from ISVs (Independent Software Vendors). Instead, it focuses on AWS's own compliance documentation, which makes it different from services like AWS Data Exchange that facilitate access to third-party data products and notifications about new data availability.

</details>
