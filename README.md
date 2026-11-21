# AWS Certification, Training & Delivery Repository

> **GitHub Repository:** `fakhruldeen/AWS`  
> **Author & Trainer:** Mohamed Fakhruldeen  
> **Knowledge Base Sync:** Mirrored 1-to-1 with Obsidian Second Brain (`Documents/Obsidian Vault/Brain/AWS`)  
> **Active Certification Tracks:** 
> 1. **Cloud Foundation:** AWS Certified Cloud Practitioner (CLF-C02)
> 2. **AI Foundation:** AWS Certified AI Practitioner (AIF-C01)

---

## 🎯 Dual-Track Mission

This repository is built for two strategic purposes:
1. **Personal Certification Mastery:** Concise, high-yield study notes, architectural comparison matrices ("X vs Y"), and verified question banks mapped against official exam domains.
2. **Professional Student Delivery & Training:** Pedagogically paced lecture decks, Marp presentation slides, visual architecture diagrams, and step-by-step hands-on lab manuals for training students.

---

## 📁 Repository Structure

```text
/home/mohamed/Desktop/Work/aws/
├── README.md                                  <-- Master Repository Index
│
├── .vscode/mcp.json                           <-- AWS MCP Server Configuration (Agent Toolkit)
├── mcp.json                                   <-- Workspace MCP Descriptor
├── .agents/                                   <-- Official AWS Agent Toolkit Integration
│   ├── rules/aws-agent-rules.md               (AWS operational & architectural rules for agents)
│   └── skills/                                (26 official AWS core skills: Bedrock, IAM, VPC, etc.)
│
├── Cloud/                                     <-- Domain 1: Cloud Architecture & Operations
│   ├── README.md                              (Domain roadmap and certification tiers)
│   └── Foundation/                            <-- Foundational Tier
│       ├── README.md                          (Foundation track syllabus & exam index)
│       └── CLF-C02/                           <-- AWS Certified Cloud Practitioner (ACTIVE)
│           ├── README.md                      (CLF-C02 Master Course Portal)
│           ├── syllabus/                      (Exam Blueprint & Domain Breakdowns)
│           ├── explanations/                  (Comprehensive guides across Domains 1-4)
│           ├── tutorials/                     (7 End-to-end architectural tutorials)
│           ├── diagrams/                      (10 Production Mermaid blueprints)
│           ├── labs/                          (14 Visual student labs + assets + fast-track)
│           ├── notes/                         (Atomic study notes & cheat sheets)
│           ├── slides/                        (Student lecture presentation decks)
│           ├── sources/                       (Reference literature - GitIgnored)
│           └── questions_bank/                (4,954 Practice questions - GitIgnored)
│
└── AI/                                        <-- Domain 2: Artificial Intelligence & Machine Learning
    ├── README.md                              (AI domain roadmap and certification tiers)
    └── Foundation/                            <-- Foundational Tier
        ├── README.md                          (AI Foundation track syllabus & index)
        └── AIF-C01/                           <-- AWS Certified AI Practitioner (ACTIVE)
            ├── README.md                      (AIF-C01 Master Course Portal)
            ├── syllabus/                      (Course syllabus & exam guide)
            ├── notes/                         (Atomic study notes & cheat sheets)
            ├── slides/                        (Student lecture presentation decks)
            └── labs/                          (Bedrock playgrounds, RAG, and Guardrails labs)
```

---

## 🧭 Track 1: Cloud Practitioner (CLF-C02) Blueprint

All 4,954 questions in this repository are audited and mapped against the official **CLF-C02** domains:

| Domain | Domain Title | Official Weighting | Question Pool Count | Primary Student Lab |
|:---:|:---|:---:|:---:|:---|
| **Domain 1** | Cloud Concepts | **24%** | ~580 Qs | [Lab 3: Multi-AZ Web Tier](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_03_ec2_compute_bootstrap.md) |
| **Domain 2** | Security and Compliance | **30%** | ~735 Qs | [Lab 1: IAM Least Privilege & MFA](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/fast_track/Lab_01_AWS_IAM_Least_Privilege_and_MFA.md) |
| **Domain 3** | Cloud Technology and Services | **34%** | ~1,140 Qs | [Lab 7: S3 Storage Lifecycle](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_07_s3_storage_lifecycle.md) |
| **Domain 4** | Billing, Pricing, and Support | **12%** | ~469 Qs | [Lab 14: FinOps Cost Governance](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_14_billing_cost_management.md) |
| **TOTAL** | | **100%** | **4,954 Questions** | |

---

## 🤖 Track 2: AI Practitioner (AIF-C01) Blueprint

The AI Foundation curriculum maps 1-to-1 to the 5 domains of the official **AIF-C01** exam:

| Domain | Domain Title | Exam Weight | Core AWS Tooling Covered | Primary Student Lab |
|:---:|:---|:---:|:---|:---|
| **Domain 1** | Fundamentals of AI and ML | **20%** | SageMaker Studio, Canvas, Data Wrangler, Ground Truth, 4 Deployment Modes | [Lab 1: Bedrock Playgrounds](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) |
| **Domain 2** | Fundamentals of Generative AI | **24%** | Foundation Models, Tokens, Context Window, Embeddings, Inference Tuning | [Lab 1: Prompt Engineering](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) |
| **Domain 3** | Applications of Foundation Models | **28%** | Amazon Bedrock, Knowledge Bases (RAG), Agents, Prompt Flows, Amazon Q | [Lab 2: Bedrock RAG KB](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md) |
| **Domain 4** | Guidelines for Responsible AI | **14%** | SageMaker Clarify (Bias & SHAP), Bedrock Guardrails, Model Cards | [Lab 3: Bedrock Guardrails](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) |
| **Domain 5** | Security, Compliance, and Governance | **14%** | Bedrock Data Privacy, KMS encryption, PrivateLink, CloudTrail, Invocation Logs | [Lab 3: PII Masking](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) |
| **TOTAL** | | **100%** | | |

---

## 🚀 Student Hands-On Learning Paths & Full Curriculum

The repository is completely self-contained and structured into four interconnected learning layers under each exam code:

### 1. 🔬 14 Visual Student Labs (`Cloud/Practitioner/CLF-C02/phase2_step07_labs/`)
*Master Index:* **[Cloud/Practitioner/CLF-C02/phase2_step07_labs/README.md](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/README.md)**  
Every lab features: (1) Prerequisite Concept Refresher, (2) Step-by-Step Console Walkthrough with real screenshots, (3) AWS CLI v2 production commands (`eu-north-1`), and (4) Cost-Free Cleanup Safeguards.
* **[Lab 00: AWS Account Creation & Security Baseline Walkthrough](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/00_Account_Creation_Walkthrough.md)**
* **[Lab 01: Multi-AZ VPC Networking Infrastructure](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_01_vpc_networking.md)**
* **[Lab 02: Network Security Controls: Security Groups vs NACLs & Flow Logs](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_02_vpc_security_controls.md)**
* **[Lab 03: EC2 Compute, User Data Automation & Elastic IPs](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_03_ec2_compute_bootstrap.md)**
* **[Lab 04: High-Availability Web Tier: ALB & Auto Scaling Groups](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_04_alb_autoscaling_ha.md)**
* **[Lab 05: Serverless Backend: AWS Lambda & REST API Gateway](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_05_serverless_lambda_apigateway.md)**
* **[Lab 06: Serverless Containers: Amazon ECR & ECS Fargate](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_06_containers_ecr_ecs_fargate.md)**
* **[Lab 07: S3 Storage Lifecycle Tiering, Versioning & Security](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_07_s3_storage_lifecycle.md)**
* **[Lab 08: Persistent Block & Shared File Storage: Amazon EBS vs EFS](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_08_ebs_efs_storage.md)**
* **[Lab 09: Relational Database High Availability: Amazon RDS Multi-AZ](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_09_rds_database_ha.md)**
* **[Lab 10: NoSQL Scalability & In-Memory Caching: DynamoDB & DAX](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_10_dynamodb_nosql_dax.md)**
* **[Lab 11: Global Edge Acceleration & Defense: Route 53, CloudFront & WAF](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_11_route53_cloudfront_edge.md)**
* **[Lab 12: Decoupled Enterprise Messaging: SNS, SQS & EventBridge](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_12_sqs_sns_eventbridge_messaging.md)**
* **[Lab 13: Enterprise Observability: CloudWatch, CloudTrail & AWS Config](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_13_observability_cloudwatch_cloudtrail_config.md)**
* **[Lab 14: FinOps & Cost Governance: Budgets, Cost Explorer & Calculator](./Cloud/Practitioner/CLF-C02/phase2_step07_labs/lab_14_billing_cost_management.md)**

### 2. 🏛️ Architectural Multi-Service Tutorials (`Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/`)
*Master Index:* **[Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/README.md](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/README.md)**  
End-to-end multi-service architectures showing how individual AWS components interconnect into enterprise systems:
* **[Tutorial 00: AWS Account Creation, Root Securing & Security Baseline](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_00_AWS_Account_Creation_and_Security_Baseline.md)**
* **[Tutorial 01: Multi-Tier VPC and Bastion Host Infrastructure](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_01_Multi_Tier_VPC_and_Bastion_Host.md)**
* **[Tutorial 02: Highly Available Auto-Scaling Web Tier](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_02_Highly_Available_AutoScaling_Web_Tier.md)**
* **[Tutorial 03: Secure Multi-AZ RDS PostgreSQL with Secrets Manager](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_03_Secure_Multi_AZ_RDS_with_Secrets_Manager.md)**
* **[Tutorial 04: Serverless Event-Driven Pipeline](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_04_Serverless_Event_Driven_Pipeline.md)**
* **[Tutorial 05: Automating Infrastructure with CloudFormation](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_05_Automating_Infrastructure_with_CloudFormation.md)**
* **[Tutorial 06: Multi-Account Governance with Organizations & SCPs](./Cloud/Practitioner/CLF-C02/phase2_step08_tutorials/Tutorial_06_Enterprise_Governance_Organizations_and_SCPs.md)**

### 3. 📖 Comprehensive Conceptual & Service Explanations (`Cloud/Practitioner/CLF-C02/phase1_step06_explanations/`)
*Master Index:* **[Cloud/Practitioner/CLF-C02/phase1_step06_explanations/README.md](./Cloud/Practitioner/CLF-C02/phase1_step06_explanations/README.md)**  
Exhaustive domain-by-domain knowledge base covering every single service, framework, and exam trap across all 4 CLF-C02 domains:
* **[Domain 1: Cloud Concepts](./Cloud/Practitioner/CLF-C02/phase1_step06_explanations/01_Cloud_Concepts/)** - Cloud Economics & TCO, AWS CAF, Well-Architected Framework, Global Infrastructure, Shared Responsibility, and Disaster Recovery.
* **[Domain 2: Security and Compliance](./Cloud/Practitioner/CLF-C02/phase1_step06_explanations/02_Security_and_Compliance/)** - IAM Identity, Shield & WAF, Threat Detection & Compliance (GuardDuty, Inspector, Macie), and KMS Encryption & Secrets Manager.
* **[Domain 3: Cloud Technology and Services](./Cloud/Practitioner/CLF-C02/phase1_step06_explanations/03_Technology_and_Services/)** - Compute (EC2, ECS, EKS, Lambda), Storage (S3, EBS, EFS), Databases (RDS, DynamoDB, Aurora), Networking (VPC, Route 53, CloudFront), Management & Observability, Application Integration, and Analytics & AI.
* **[Domain 4: Billing, Pricing, and Support](./Cloud/Practitioner/CLF-C02/phase1_step06_explanations/04_Billing_and_Pricing/)** - Pricing Models (Savings Plans, Spot, RI), Cost Allocation Tags, Budgets, Cost Explorer, Support Plans, and AWS Marketplace.

### 4. 📊 Production Architecture Mermaid Blueprints (`Cloud/Practitioner/CLF-C02/phase1_step05_diagrams/`)
*Master Index:* **[Cloud/Practitioner/CLF-C02/phase1_step05_diagrams/README.md](./Cloud/Practitioner/CLF-C02/phase1_step05_diagrams/README.md)**  
10 standalone production blueprints rendering clear data flows, security perimeters, and service topology.

### 5. 🤖 AI Foundation Labs (`AI/Practitioner/AIF-C01/phase2_step07_labs/`)
*Master Index:* **[AI/Practitioner/AIF-C01/README.md](./AI/Practitioner/AIF-C01/README.md)**  
1. **[Lab 1: Bedrock Playgrounds & Prompt Engineering](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md)** - Master Temperature, Top-P, Zero-shot, Few-shot, and Chain-of-Thought prompting.
2. **[Lab 2: Building a RAG Knowledge Base](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md)** - Ingest enterprise documents from S3 into OpenSearch Serverless via Titan Embeddings and query with Claude.
3. **[Lab 3: Responsible AI & PII Masking](./AI/Practitioner/AIF-C01/phase2_step07_labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md)** - Configure Denied Topics, content filters, and PII redaction using Amazon Bedrock Guardrails.

---

## 📚 Course Reference Books (Sources)

For comprehensive offline study and deeper explanations, the curriculum references two core textbooks stored locally in `Cloud/Practitioner/CLF-C02/phase5_step12_sources/` (excluded from git):

1. **AWS Certified Cloud Practitioner (CLF-C02) Certification Guide (2nd Edition, 2026)**
   * **Author:** Rajesh Daswani (*Packt Publishing*) — `ISBN: 978-1-83546-429-8`
   * *Best For:* Practical exam readiness, exam-trap walkthroughs, and end-of-chapter review questions.
2. **AWS Certified Cloud Practitioner (CLF-C02) Study Guide (1st Edition, 2026)**
   * **Author:** Tom Taulli (*O'Reilly Media*) — `ISBN: 978-8-34164-022-2`
   * *Best For:* Conceptual grounding, cloud economics, TCO modeling, and enterprise architecture perspectives.

---

## 🛠️ Agent Toolkit for AWS (AI Assistant Layer)

This repository includes official integration with the **[Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html)** to provide AI coding assistants with live AWS documentation, regional feature verification, and governed architectural runbooks:

* **AWS MCP Server (`.vscode/mcp.json` / `mcp.json`):** Connects to the AWS remote MCP server via `uvx mcp-proxy-for-aws-cli@latest` with `--skip-auth`. Enables live documentation search (`aws___search_documentation`) and Markdown retrieval (`aws___read_documentation`) without requiring AWS credentials.
* **Agent Rules (`.agents/rules/aws-agent-rules.md`):** Mandates evidence-based verification against current AWS documentation, Infrastructure as Code (CDK/CloudFormation), and Well-Architected Framework principles.
* **Agent Skills (`.agents/skills/`):** 26 modular AWS core runbooks (Amazon Bedrock, SageMaker AI, IAM, VPC networking, CloudFormation, cost optimization) dynamically referenced during course development and maintenance.
