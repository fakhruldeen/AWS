# Domain 5: Security, Compliance, and Governance for AI Solutions

> **Weight:** 14% of Scored Exam Content  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Exam Guide Baseline:** v1.2 (October 2026 - incorporating the Generative AI Security Scoping Matrix)  
> **Index:** `AI/Practitioner/AIF-C01/explanations/05_Domain_5_Security_Compliance_and_Governance.md`

---

## 🧭 Domain Overview

Domain 5 addresses the enterprise security, compliance, data protection, and audit controls essential for deploying AI solutions on AWS. Key subjects include the **Generative AI Security Scoping Matrix**, data privacy guarantees in Amazon Bedrock, network isolation via VPC Endpoints and PrivateLink, identity governance with AWS IAM and AgentCore, automated PII discovery with **Amazon Macie**, cryptographic controls with **AWS KMS**, and comprehensive audit logging with **AWS CloudTrail**.

---

## 🎯 Task Statement 5.1: Apply the Generative AI Security Scoping Matrix

AWS defines four architectural scopes of Generative AI deployment. As an organization moves from consumer SaaS tools toward custom pre-training, security responsibilities shift from the cloud provider to the customer:

```mermaid
flowchart LR
    Scope1["Scope 1\nConsumer / Public SaaS\n(Third-party consumer apps)"] --> Scope2["Scope 2\nEnterprise Managed\n(Amazon Q, Bedrock Base FMs)"]
    Scope2 --> Scope3["Scope 3\nCustom Fine-Tuning & RAG\n(Bedrock Custom Models, SageMaker)"]
    Scope3 --> Scope4["Scope 4\nFull Custom Pre-Training\n(Building FMs from scratch)"]
```

### Generative AI Shared Responsibility Matrix
| Architectural Scope | AWS Responsibility | Customer Responsibility | Example Service |
|---|---|---|---|
| **Scope 1: Third-Party Consumer Applications** | Provider controls underlying infrastructure and model training data. | Data sharing settings, policy adherence, avoiding entering confidential data. | Public consumer chatbots, third-party browser extensions. |
| **Scope 2: Enterprise Managed AI Services** | Model weights, physical infrastructure, API availability, base safety alignment. AWS **never** trains base models on customer data. | Prompt engineering, IAM identity access, input/output data classification, Bedrock Guardrails configuration. | **Amazon Bedrock (On-Demand FMs)**, **Amazon Q Business / Developer**. |
| **Scope 3: Custom Models, Fine-Tuning & RAG** | Base model execution runtime, hyperparameter execution environment, isolated compute. | Curation and sanitization of fine-tuning datasets in S3, vector database access control, RAG document permissions, evaluation. | **Bedrock Knowledge Bases**, **Bedrock Custom Models**, **SageMaker JumpStart**. |
| **Scope 4: Custom Foundation Models Built from Scratch** | Cloud hardware availability (Trainium, GPU instances), low-level network fabric. | Full data collection, ethics filtering, tokenization, architecture design, distributed training, bias auditing, ongoing maintenance. | **Amazon EC2 UltraClusters**, **AWS Trainium / Inferentia**. |

---

## 🎯 Task Statement 5.2: Safeguard data privacy, isolation, and residency

### 1. Amazon Bedrock Data Privacy Guarantees
* **Zero Model Training on Customer Data:** By default, AWS does **not** use any customer inputs (prompts) or outputs (completions) to train base foundation models, nor are they shared with third-party model providers (Anthropic, Meta, Mistral).
* **Cryptographic Isolation:** Customer data remains encrypted at rest and in transit within the customer's selected AWS Region.
* **Custom Models Isolation:** When fine-tuning a model in Amazon Bedrock, the resulting custom model weights are encrypted using customer KMS keys and stored in a private tenant partition dedicated solely to the customer's account.

### 2. Network Isolation with AWS PrivateLink & VPC Endpoints
To prevent generative AI traffic from traversing the public internet:

```mermaid
flowchart LR
    VPC["Customer Virtual Private Cloud (VPC)"]
    App["Internal EC2 / EKS Application"] --> VPCE["VPC Interface Endpoint\n(AWS PrivateLink)"]
    VPCE -->|"AWS Private Network Fabric\n(No Public Internet)"| BedrockAPI["Amazon Bedrock Service Endpoint"]
    VPCE --> S3["Amazon S3\n(Document Lake)"]
```

* **VPC Interface Endpoints (`com.amazonaws.<region>.bedrock-runtime`):** Enables private IP connectivity from private subnets directly to Amazon Bedrock without requiring an Internet Gateway (IGW), NAT Gateway, or public IP addresses.
* **VPC Endpoint Policies:** Enforces IAM restrictions directly on the network endpoint, allowing only specific IAM principals or specific model IDs to be invoked.

---

## 🎯 Task Statement 5.3: Implement Identity & Access Management (IAM) for AI

```mermaid
flowchart TD
    User["Developer / Application"] --> IAM["AWS IAM Policy Evaluation"]
    
    subgraph Controls["Access Governance Checks"]
        C1["1. Model Access Control\n(bedrock:InvokeModel on specific Model ARN)"]
        C2["2. Region Restrictions\n(e.g., Condition: StringEquals aws:RequestedRegion)"]
        C3["3. Guardrail Enforcement\n(bedrock:ApplyGuardrail mandatory header)"]
    end
    
    IAM --> Controls
    Controls --> Allowed["Authorized Model Invocation"]
    Controls --> Denied["Explicit Deny / AccessDeniedException"]
```

### Key IAM Actions for Generative AI
* `bedrock:InvokeModel`: Allows runtime inference requests.
* `bedrock:InvokeModelWithResponseStream`: Allows streaming real-time token responses.
* `bedrock:ApplyGuardrail`: Enforces passing inputs/outputs through Bedrock Guardrails.
* `sagemaker:CreateTrainingJob`: Permits launching ML training instances.

### AgentCore Identity & Least Privilege
When deploying autonomous agents using **Amazon Bedrock AgentCore**, the agent requires an IAM Service Role (`bedrock.amazonaws.com`). The role must follow strict least privilege:
* Read access to specific S3 knowledge base buckets.
* Permission to invoke specific AWS Lambda Action Group functions (`lambda:InvokeFunction`).
* Read-only query rights against the vector database (Amazon OpenSearch Serverless).

---

## 🎯 Task Statement 5.4: Compliance, Auditing, and Data Classification

```mermaid
flowchart LR
    S3Data["S3 Training & RAG Data"] --> Macie["Amazon Macie\n(Automated PII Discovery)"]
    Inference["Bedrock Invocations"] --> CloudTrail["AWS CloudTrail\n(Management & Data Events)"]
    Inference --> CloudWatch["Amazon CloudWatch\n(Model Latency & Error Metrics)"]
    CloudTrail --> Audit["Security & Compliance Auditing"]
```

### 1. Amazon Macie (Automated Sensitive Data Discovery)
* **Role in AI:** Scans Amazon S3 buckets holding documents for RAG Knowledge Bases or fine-tuning datasets to locate unmasked Personally Identifiable Information (SSNs, passport numbers, credit cards).
* **Remediation:** Flags high-risk buckets before documents are ingested into vector indexes or exposed to LLMs.

### 2. AWS CloudTrail (Audit Logging)
* **Management Events:** Tracks administrative actions (e.g., `CreateModelCustomizationJob`, `CreateGuardrail`, `DeleteKnowledgeBase`).
* **Data Events:** Tracks data-plane API calls (`InvokeModel`, `InvokeModelWithResponseStream`, `RetrieveAndGenerate`). Must be explicitly enabled in CloudTrail to record detailed model invocation request metadata.

### 3. Cryptographic Protection with AWS KMS
* **Encryption at Rest:**
  * S3 buckets hosting training data and knowledge base documents.
  * Amazon Bedrock custom model weights.
  * Amazon OpenSearch Serverless vector collections.
  * Amazon SageMaker Studio EBS storage volumes.
* **Customer Managed Keys (CMKs):** Allows organizations to control key rotation, enforce dual-custody access policies, and instantly revoke model decryption privileges by disabling the KMS key.

---

## 🔗 Related Resources
* Next: [AIF-C01 Master Cheat Sheet](../notes/06_AIF-C01_Exam_CheatSheet.md)
* Blueprint: [Diagram 09: Generative AI Security Scoping Matrix](../diagrams/Diagram_09_Generative_AI_Security_Scoping_Matrix.md)
* Blueprint: [Diagram 10: Enterprise AI Security, KMS, and Audit Loop](../diagrams/Diagram_10_Enterprise_AI_Security_KMS_and_Audit_Loop.md)
* Tutorial: [Tutorial 04: Enterprise Responsible AI & PII Governance Pipeline](../tutorials/Tutorial_04_Enterprise_Responsible_AI_and_PII_Governance_Pipeline.md)
