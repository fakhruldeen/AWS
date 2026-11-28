# Domain 5: Security, Compliance, and Governance for AI Solutions (`14%` of Scored Content)

> **Official Blueprint:** AWS Certified AI Practitioner (`AIF-C01`) Exam Guide v1.2 (Oct 29, 2026)  
> **Scored Questions (~50 scored total):** ~7 scored questions (~9 in a 65-question full mock)

---

## Task Statement 5.1: Explain methods to secure AI systems
- **AWS Security Services & Features (v1.2):**
  - `AWS IAM` (least-privilege roles, policies, temporary credentials)
  - Encryption at rest (`AWS KMS`) and in transit (`TLS`)
  - `Amazon Macie` (ML discovery of PII/sensitive data in S3)
  - `AWS PrivateLink` (Interface VPC Endpoints keeping AI traffic off the public internet)
  - `AWS Shared Responsibility Model` (customer prompts/data in Bedrock are never used to train base FMs)
  - **`Amazon Bedrock AgentCore Identity`** (OAuth/IAM delegation & scoped credentials for agents)
  - **`Policy in AgentCore`** (deterministic allow/forbid policies governing agent tool invocations)
  - `Amazon Bedrock Guardrails` (input/output filtering, prompt attack defense, PII redaction)
- **Source Citation & Data Origins:** Data lineage tracking, `AWS Glue Data Catalog`, and `Amazon SageMaker Model Cards`.
- **Secure Data Engineering:** Assessing data quality, privacy-enhancing technologies (anonymization, tokenization, differential privacy), fine-grained data access control (`AWS Lake Formation`), and data integrity.
- **AI Security & Privacy Considerations:** Application security, threat detection, vulnerability management (`Amazon Inspector`), infrastructure protection, **prompt injection**, encryption, data leakage prevention, output filtering/validation, audit trails (`Bedrock Model Invocation Logging` + `CloudTrail`), and toxicity mitigation.
- **Hallucination Detection & Grounding (v1.2):** `RAG` grounding, `Bedrock Guardrails` contextual grounding checks, output validation, and confidence scoring.

## Task Statement 5.2: Recognize governance and compliance regulations for AI systems
- **Governance & Compliance AWS Services:** `AWS Config` (continuous resource compliance), `Amazon Inspector` (CVE scanning), `AWS Artifact` (compliance reports & agreements), `AWS CloudTrail` (API audit trails), `AWS Trusted Advisor` (best-practice checks).
- **Data Governance Strategies:** Data lifecycles (`S3 Lifecycle` / `Glacier`), centralized logging, **data residency** (Region selection), continuous monitoring, observation, and retention policies.
- **Governance Protocols & Frameworks:** Organizational AI policies, review cadence, review strategies, **`Generative AI Security Scoping Matrix`** (Scopes 1–5), transparency standards, and team training requirements.
