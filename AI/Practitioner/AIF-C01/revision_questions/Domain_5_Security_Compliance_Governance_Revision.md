# Domain 5 Revision Questions: Security, Compliance & Governance

> **Domain:** Domain 5: Security, Compliance, and Governance for AI Solutions (14% Exam Weight)  
> **Question Count:** 15 Comprehensive Scenario-Based Questions  
> **Format:** Multiple Choice & Multiple Response with Detailed Explanations

---

### Question 1
According to the Generative AI Security Scoping Matrix, what are the customer's responsibilities when using an Enterprise-Managed Foundation Model in Amazon Bedrock (Scope 2)?
- [ ] A) Managing physical server hardware and patching hypervisors
- [ ] B) Configuring IAM access policies, implementing Bedrock Guardrails, and classifying input data
- [ ] C) Pre-training base transformer models from raw web data
- [ ] D) Designing custom silicon ASIC accelerators
> **Correct Answer:** B  
> **Rationale:** In Scope 2, AWS manages the underlying foundation model and infrastructure, while the customer is responsible for data classification, IAM permissions, prompt governance, and guardrails.

---

### Question 2
A pharmaceutical company must ensure that its proprietary molecular research prompts sent to Amazon Bedrock never traverse the public internet. Which architecture should be deployed?
- [ ] A) An Internet Gateway (IGW) attached to the public subnet
- [ ] B) An AWS PrivateLink VPC Interface Endpoint for the Bedrock Runtime (`com.amazonaws.<region>.bedrock-runtime`)
- [ ] C) An open NAT Gateway with elastic IP
- [ ] D) Public Route 53 DNS records
> **Correct Answer:** B  
> **Rationale:** AWS PrivateLink provisions private VPC Interface Endpoints, routing API requests over AWS's internal network backbone without public internet exposure.

---

### Question 3
Does AWS use customer prompts, fine-tuning datasets, or generated completions in Amazon Bedrock to train public base models or share them with third-party model providers?
- [ ] A) Yes, all prompts are retained for 1 year to update model weights.
- [ ] B) No. Customer inputs and outputs are never used to train base foundation models and are never shared with model partners.
- [ ] C) Yes, but only for accounts using the free tier.
- [ ] D) Yes, if customer spending is below \$10,000/month.
> **Correct Answer:** B  
> **Rationale:** AWS guarantees cryptographic isolation: customer prompts and outputs are never used to train base models and remain within the customer's account and region.

---

### Question 4
A compliance officer wants to ensure that all data-plane API invocations of Amazon Bedrock (e.g., `InvokeModel`, `InvokeModelWithResponseStream`) are logged with the caller's IAM identity, timestamp, and source IP. Which service feature must be configured?
- [ ] A) AWS CloudTrail Data Events for Bedrock resources
- [ ] B) AWS CloudTrail Management Events only
- [ ] C) Amazon VPC Flow Logs
- [ ] D) AWS Artifact Compliance Reports
> **Correct Answer:** A  
> **Rationale:** Management events only record control-plane administrative changes. Data Events must be explicitly enabled to capture data-plane runtime invocations like `InvokeModel`.

---

### Question 5
Before ingesting thousands of PDF files into an Amazon Bedrock Knowledge Base vector index, a security architect wants to scan the S3 bucket to discover unmasked sensitive data such as credit card numbers or passport IDs. Which AWS service is purpose-built for this?
- [ ] A) AWS Shield Advanced
- [ ] B) Amazon Macie
- [ ] C) Amazon Inspector
- [ ] D) AWS WAF
> **Correct Answer:** B  
> **Rationale:** Amazon Macie uses pattern matching and machine learning to automatically discover, classify, and protect sensitive Personally Identifiable Information (PII) stored in Amazon S3.

---

### Question 6
An organization requires full control over the encryption keys used to protect its Amazon Bedrock custom model weights and OpenSearch Serverless vector indices, including the ability to immediately revoke access by disabling the key. Which key type is required?
- [ ] A) AWS Owned Keys
- [ ] B) AWS Managed Keys (e.g., `aws/bedrock`)
- [ ] C) AWS KMS Customer Managed Keys (CMKs)
- [ ] D) Plaintext local storage
> **Correct Answer:** C  
> **Rationale:** Customer Managed Keys (CMKs) grant the customer complete control over key policies, annual rotation, and immediate revocation privileges.

---

### Question 7
When deploying an autonomous Bedrock Agent with Action Groups that invoke AWS Lambda functions to access internal databases, which security best practice must be applied to the agent's IAM service role?
- [ ] A) Grant `AdministratorAccess` to prevent permission errors
- [ ] B) Enforce the Principle of Least Privilege by scoping permissions strictly to the specific Lambda function ARNs and S3 buckets required
- [ ] C) Use hardcoded AWS access keys in the agent prompt
- [ ] D) Disable IAM authentication on the Bedrock endpoint
> **Correct Answer:** B  
> **Rationale:** Agents should operate with least-privilege IAM service execution roles, granting access only to the exact resources and Lambda functions necessary for their designated tasks.

---

### Question 8
In which Generative AI Security Scope does an organization build a custom foundation model from scratch using billions of tokens on AWS Trainium clusters, assuming 100% of the responsibility for data curation, copyright compliance, and model safety?
- [ ] A) Scope 1
- [ ] B) Scope 2
- [ ] C) Scope 3
- [ ] D) Scope 4
> **Correct Answer:** D  
> **Rationale:** Scope 4 represents full custom pre-training from scratch, shifting complete responsibility for data provenance, legal copyright, ethics, and architecture to the customer.

---

### Question 9
How is model access initially configured when a new AWS account attempts to invoke third-party foundation models in Amazon Bedrock?
- [ ] A) All models are enabled automatically.
- [ ] B) Models are disabled by default and require an administrator to explicitly request and obtain access in the Model Access console.
- [ ] C) Access is granted only via phone verification with AWS Support.
- [ ] D) Access is restricted to root account credentials only.
> **Correct Answer:** B  
> **Rationale:** By default, foundation models in Amazon Bedrock are locked. An administrator must explicitly submit a model access request per region.

---

### Question 10 (Multiple Response)
Which TWO IAM policies or conditions can be used to restrict which foundation models a developer role is allowed to invoke in Amazon Bedrock? (Select TWO.)
- [ ] A) Specify the exact Model ARN in the `Resource` block of the IAM policy (e.g., `arn:aws:bedrock:eu-north-1::foundation-model/amazon.nova-pro-v1:0`)
- [ ] B) Use `Condition` blocks to restrict access based on request region (`aws:RequestedRegion`) or resource tags
- [ ] C) Delete the VPC route table
- [ ] D) Disable AWS KMS globally
- [ ] E) Modify the public DNS records in Amazon Route 53
> **Correct Answers:** A, B  
> **Rationale:** Least-privilege IAM policies specify exact Model ARNs in the Resource block and enforce contextual conditions like region or tags.

---

### Question 11
Where are the weights of custom models created via Amazon Bedrock fine-tuning stored, and how are they protected?
- [ ] A) Stored in public Amazon S3 buckets without encryption
- [ ] B) Stored in an isolated private partition dedicated to the customer's account and encrypted at rest with customer-selected AWS KMS keys
- [ ] C) Exported to the developer's laptop hard drive
- [ ] D) Shared with third-party foundation model partners
> **Correct Answer:** B  
> **Rationale:** Bedrock custom model weights are isolated in private tenant partitions and encrypted using the customer's KMS Customer Managed Keys.

---

### Question 12
An organization needs to obtain official SOC, ISO, and PCI-DSS third-party compliance reports proving that AWS AI services meet regulatory security standards. Which AWS service provides these downloadable compliance reports?
- [ ] A) AWS Trusted Advisor
- [ ] B) AWS Artifact
- [ ] C) Amazon Inspector
- [ ] D) AWS CloudShell
> **Correct Answer:** B  
> **Rationale:** AWS Artifact is the central portal for on-demand access to AWS's security and compliance reports and certifications.

---

### Question 13
Which Bedrock IAM action must be granted to allow an application to invoke a model while enforcing that inputs and outputs pass through an Amazon Bedrock Guardrail?
- [ ] A) `bedrock:ApplyGuardrail`
- [ ] B) `s3:PutObject`
- [ ] C) `kms:ReEncrypt`
- [ ] D) `ec2:DescribeInstances`
> **Correct Answer:** A  
> **Rationale:** The `bedrock:ApplyGuardrail` permission allows applications to evaluate text inputs and completions against configured guardrail safety policies.

---

### Question 14
What is the primary security advantage of using VPC Endpoint Policies on an AWS PrivateLink endpoint for Amazon Bedrock?
- [ ] A) It reduces electricity consumption in the data center.
- [ ] B) It allows security teams to restrict which specific IAM principals or foundation model ARNs can be invoked across that network boundary.
- [ ] C) It automatically translates prompts into Spanish.
- [ ] D) It provides free GPU compute credits.
> **Correct Answer:** B  
> **Rationale:** VPC Endpoint Policies enforce network-level perimeter control, allowing administrators to dictate which IAM users and model ARNs can be accessed through that private interface.

---

### Question 15
An AI application logs conversational prompts and responses for compliance. Under GDPR and privacy regulations, which practice must be applied before persisting this data to long-term storage in Amazon S3?
- [ ] A) Anonymizing or masking Personally Identifiable Information (PII) using Bedrock Guardrails or Amazon Comprehend
- [ ] B) Making the S3 bucket publicly readable
- [ ] C) Increasing the temperature parameter to 1.0
- [ ] D) Disabling S3 versioning
> **Correct Answer:** A  
> **Rationale:** Regulatory compliance under GDPR and HIPAA requires redacting or masking sensitive PII before storing records in audit data lakes.
