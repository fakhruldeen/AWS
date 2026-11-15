# Module 05 Knowledge Check: Security, Compliance & Governance

> **Domain:** Domain 5: Security, Compliance, and Governance for AI Solutions (14% Weight)  
> **Questions:** 10 Diagnostic Questions with Answers & Rationales

---

### Questions

1. **Under the Generative AI Security Scoping Matrix, who is responsible for managing data classification and prompt guardrails when using an enterprise-managed service like Amazon Bedrock?**
   - A) AWS exclusively
   - B) The Customer
   - C) The third-party foundation model provider (e.g., Anthropic)
   - D) Hardware GPU manufacturers

2. **Does AWS use customer prompts or generated completions in Amazon Bedrock to train or improve base foundation models?**
   - A) Yes, for all models in the catalog
   - B) Yes, but only for Amazon Titan models
   - C) No, AWS never uses customer inputs or outputs to train base foundation models
   - D) Yes, if customer spending is under \$1,000/month

3. **Which AWS networking service enables private, encrypted connectivity between an enterprise VPC and the Amazon Bedrock service without traversing the public internet?**
   - A) AWS Direct Connect Gateway
   - B) AWS PrivateLink (VPC Interface Endpoint)
   - C) Internet Gateway (IGW)
   - D) NAT Gateway

4. **A security team wants to continuously audit Amazon S3 buckets holding documents for a RAG knowledge base to discover unmasked credit cards or passport numbers. Which service is optimal?**
   - A) AWS Shield Advanced
   - B) Amazon Macie
   - C) Amazon Inspector
   - D) AWS WAF

5. **Which AWS service records individual data-plane API calls, such as `InvokeModel` or `RetrieveAndGenerate`, for regulatory auditing and compliance?**
   - A) AWS CloudTrail Data Events
   - B) AWS CloudTrail Management Events
   - C) Amazon CloudWatch Synthetics
   - D) AWS Config Managed Rules

6. **In Amazon Bedrock, how is access to third-party foundation models (such as Claude or Llama) governed upon initial account creation?**
   - A) All models are enabled automatically for all users
   - B) Models are disabled by default and require an administrator to explicitly request access
   - C) Models require purchasing a physical GPU license
   - D) Access can only be granted via AWS Support tickets

7. **Which key management approach provides customers with complete control over key rotation, policy definitions, and the ability to instantly revoke model decryption privileges?**
   - A) AWS Owned Keys
   - B) AWS Managed Keys
   - C) AWS KMS Customer Managed Keys (CMKs)
   - D) S3 Managed Keys (SSE-S3)

8. **When an autonomous agent built with Bedrock AgentCore invokes an AWS Lambda function to query a database, what identity principle must be enforced on its IAM execution role?**
   - A) Administrator Access
   - B) Principle of Least Privilege (scoped strictly to the target Lambda function ARN)
   - C) Root Account Credential Delegation
   - D) Anonymous Public Access

9. **In which Generative AI Security Scope does an organization assume 100% of the responsibility for data filtering, architecture design, ethics auditing, and training hardware management?**
   - A) Scope 1 (Third-Party Consumer SaaS)
   - B) Scope 2 (Enterprise Managed Services)
   - C) Scope 3 (Custom Fine-Tuning & RAG)
   - D) Scope 4 (Custom Pre-Training from Scratch)

10. **Where are Amazon Bedrock custom fine-tuned model weights stored?**
    - A) In a public S3 bucket accessible across all AWS accounts
    - B) In an isolated, private customer-dedicated partition encrypted with KMS keys
    - C) On third-party partner servers outside of AWS
    - D) In the local browser cache of the practitioner

---

### Answer Key & Explanations

| Q# | Answer | Key Concept Reference | Detailed Explanation |
|:---:|:---:|:--- |:--- |
| **1** | **B** | Shared Responsibility (Scope 2) | While AWS manages physical infrastructure and base model security, the customer owns data classification, IAM, and guardrails. |
| **2** | **C** | Bedrock Zero-Training Pledge | AWS guarantees that no customer prompts or responses are used to train base foundation models or shared with third parties. |
| **3** | **B** | AWS PrivateLink | VPC Interface Endpoints route traffic to `bedrock-runtime` over private AWS network fabric without internet exposure. |
| **4** | **B** | Amazon Macie | Macie uses pattern matching and ML to scan S3 buckets for sensitive PII before ingestion into RAG indexes. |
| **5** | **A** | CloudTrail Data Events | Management events track administrative actions; Data Events must be enabled to log runtime data operations like `InvokeModel`. |
| **6** | **B** | Bedrock Model Access | All foundation models are disabled by default; access must be explicitly granted per region and account. |
| **7** | **C** | KMS Customer Managed Keys | CMKs allow customers to define key policies, rotate keys on schedule, and immediately revoke access by disabling the key. |
| **8** | **B** | Principle of Least Privilege | Agents must operate under strict least privilege, assuming IAM roles with access limited strictly to the required resources. |
| **9** | **D** | Security Scope 4 | Building a foundation model from scratch shifts full responsibility for data curation, legal compliance, and training to the customer. |
| **10** | **B** | Custom Model Security | Fine-tuned weights reside in private customer-dedicated tenant partitions encrypted at rest with customer KMS keys. |
