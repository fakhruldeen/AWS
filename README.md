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
│
├── .agents/                                   <-- Official AWS Agent Toolkit Integration
│   ├── rules/aws-agent-rules.md               (AWS operational & architectural rules for agents)
│   └── skills/                                (26 official AWS core skills: Bedrock, IAM, VPC, etc.)
│
├── labs/                                      <-- 14 Visual Student Labs (CLF-C02 Hands-On)
│   ├── README.md                              (Complete 14-lab directory & concept syllabus)
│   ├── 00_Account_Creation_Walkthrough.md     (Safe account setup, root MFA, free-tier guardrails)
│   ├── lab_01_vpc_networking.md               (Multi-AZ VPC, subnets, route tables, IGW, NAT GW)
│   ├── lab_02_vpc_security_controls.md        (Security Groups vs NACLs, VPC Flow Logs)
│   ├── lab_03_ec2_compute_bootstrap.md        (EC2 launch, User Data, Elastic IPs, systemctl)
│   ├── lab_04_alb_autoscaling_ha.md           (Application Load Balancer, ASG dynamic scaling)
│   ├── lab_05_serverless_lambda_apigateway.md (AWS Lambda, REST API Gateway, CloudWatch Logs)
│   ├── lab_06_containers_ecr_ecs_fargate.md   (Amazon ECR, ECS Fargate serverless containers)
│   ├── lab_07_s3_storage_lifecycle.md         (S3 bucket versioning, lifecycle transitions, OAC)
│   ├── lab_08_ebs_efs_storage.md              (EBS block storage vs EFS POSIX multi-instance share)
│   ├── lab_09_rds_database_ha.md              (Amazon RDS PostgreSQL, DB subnet groups, Multi-AZ)
│   ├── lab_10_dynamodb_nosql_dax.md           (DynamoDB NoSQL tables, primary/sort keys, streams)
│   ├── lab_11_route53_cloudfront_edge.md      (Route 53 DNS routing, CloudFront CDN, AWS WAF)
│   ├── lab_12_sqs_sns_eventbridge_messaging.md(SNS pub/sub, SQS queues, EventBridge decouple)
│   ├── lab_13_observability_cloudwatch_cloudtrail_config.md (Metrics, alarms, trails, Config rules)
│   ├── lab_14_billing_cost_management.md      (Cost allocation tags, Budgets, Cost Explorer)
│   └── assets/                                (70+ real console screenshots & terminal outputs)
│
├── tutorials/                                 <-- Architectural Multi-Service Tutorials
│   ├── README.md                              (Curriculum roadmap & architectural learning paths)
│   ├── Tutorial_00_AWS_Account_Creation_and_Security_Baseline.md
│   ├── Tutorial_01_Enterprise_Multi_Tier_VPC_and_Networking.md
│   ├── Tutorial_02_Serverless_Microservices_API_and_Data_Processing.md
│   ├── Tutorial_03_Event_Driven_Integration_and_Decoupled_Messaging.md
│   ├── Tutorial_04_Global_Edge_Acceleration_and_Perimeter_Security.md
│   ├── Tutorial_05_Enterprise_Observability_Auditing_and_Compliance.md
│   └── Tutorial_06_Enterprise_Governance_Organizations_and_SCPs.md
│
├── explanations/                              <-- Comprehensive In-Depth Service & Conceptual Guides
│   ├── README.md                              (CLF-C02 4-domain reference portal)
│   ├── 01_Cloud_Concepts/                     (Economics, TCO, CAF, Well-Architected, Global Infra, DR)
│   ├── 02_Security_and_Compliance/            (IAM, WAF/Shield, Threat Detection, KMS & Secrets)
│   ├── 03_Technology_and_Services/            (Compute, Storage, Database, Networking, Ops, Integration)
│   └── 04_Billing_and_Pricing/                (Pricing Models, Billing Tools, Support Plans, Marketplace)
│
├── diagrams/                                  <-- 10 Standalone Production Mermaid Architecture Blueprints
│   ├── README.md                              (Master diagram index & visual architectural specs)
│   ├── Diagram_01_Global_Infrastructure_Map.md
│   ├── Diagram_02_Enterprise_Multi_Tier_VPC_Architecture.md
│   ├── Diagram_03_High_Availability_Multi_AZ_Web_Application.md
│   ├── Diagram_04_Serverless_Microservices_Event_Driven_Pipeline.md
│   ├── Diagram_05_Enterprise_Data_Storage_and_Lifecycle_Tiering.md
│   ├── Diagram_06_Relational_and_NoSQL_Database_Topologies.md
│   ├── Diagram_07_Global_Edge_Acceleration_and_DDoS_Perimeter_Defense.md
│   ├── Diagram_08_Enterprise_Observability_Auditing_and_Compliance_Loop.md
│   ├── Diagram_09_IAM_Policy_Evaluation_and_Multi_Account_Organizations_Hierarchy.md
│   └── Diagram_10_Enterprise_Billing_and_Governance_Hierarchy.md
│
├── cloud/
│   └── foundation/                            <-- Track 1: AWS Certified Cloud Practitioner (CLF-C02)
│       ├── README.md                          (Track roadmap, syllabus, and module index)
│       ├── syllabus/                          <-- Exam Blueprint & Domain Breakdowns
│       ├── slides/                            <-- Student Lecture Decks (Marp Format)
│       ├── diagrams/                          <-- Mirrored Production Mermaid Blueprints
│       ├── labs/                              <-- Fast-track Student Lab Manuals
│       ├── notes/                             <-- Mirrored Atomic Study Notes
│       ├── sources/                           <-- Reference Literature (Packt & O'Reilly - GitIgnored)
│       └── questions_bank/                    <-- 2,924 Offline Practice Questions (GitIgnored)
│
└── ai/
    └── foundation/                            <-- Track 2: AWS Certified AI Practitioner (AIF-C01)
        ├── syllabus/                          <-- Course Syllabus & Official Exam Guide
        ├── slides/                            <-- Student Lecture Decks (Marp Format)
        ├── labs/                              <-- Hands-On Student Lab Manuals
        └── notes/                             <-- Atomic Study Notes & Cheat Sheets
```

---

## 🧭 Track 1: Cloud Practitioner (CLF-C02) Blueprint

All 2,924 questions in this repository are audited and mapped against the official **CLF-C02** domains:

| Domain | Domain Title | Official Weighting | Question Pool Count | Primary Student Lab |
|:---:|:---|:---:|:---:|:---|
| **Domain 1** | Cloud Concepts | **24%** | ~580 Qs | [Lab 3: Multi-AZ Web Tier](./cloud/foundation/labs/Lab_03_Resilient_MultiAZ_Web_Tier_EC2.md) |
| **Domain 2** | Security and Compliance | **30%** | ~735 Qs | [Lab 1: IAM Least Privilege & MFA](./cloud/foundation/labs/Lab_01_AWS_IAM_Least_Privilege_and_MFA.md) |
| **Domain 3** | Cloud Technology and Services | **34%** | ~1,140 Qs | [Lab 2: Static S3 & CloudFront](./cloud/foundation/labs/Lab_02_Static_Website_S3_and_CloudFront.md) |
| **Domain 4** | Billing, Pricing, and Support | **12%** | ~469 Qs | [Lab 4: AWS Budgets Safety Alerts](./cloud/foundation/labs/Lab_04_Proactive_Budget_Alerts_AWS_Budgets.md) |
| **TOTAL** | | **100%** | **2,924 Questions** | |

---

## 🤖 Track 2: AI Practitioner (AIF-C01) Blueprint

The AI Foundation curriculum maps 1-to-1 to the 5 domains of the official **AIF-C01** exam:

| Domain | Domain Title | Exam Weight | Core AWS Tooling Covered | Primary Student Lab |
|:---:|:---|:---:|:---|:---|
| **Domain 1** | Fundamentals of AI and ML | **20%** | SageMaker Studio, Canvas, Data Wrangler, Ground Truth, 4 Deployment Modes | [Lab 1: Bedrock Playgrounds](./ai/foundation/labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) |
| **Domain 2** | Fundamentals of Generative AI | **24%** | Foundation Models, Tokens, Context Window, Embeddings, Inference Tuning | [Lab 1: Prompt Engineering](./ai/foundation/labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) |
| **Domain 3** | Applications of Foundation Models | **28%** | Amazon Bedrock, Knowledge Bases (RAG), Agents, Prompt Flows, Amazon Q | [Lab 2: Bedrock RAG KB](./ai/foundation/labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md) |
| **Domain 4** | Guidelines for Responsible AI | **14%** | SageMaker Clarify (Bias & SHAP), Bedrock Guardrails, Model Cards | [Lab 3: Bedrock Guardrails](./ai/foundation/labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) |
| **Domain 5** | Security, Compliance, and Governance | **14%** | Bedrock Data Privacy, KMS encryption, PrivateLink, CloudTrail, Invocation Logs | [Lab 3: PII Masking](./ai/foundation/labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) |
| **TOTAL** | | **100%** | | |

---

## 🚀 Student Hands-On Learning Paths & Full Curriculum

The repository is completely self-contained and structured into four interconnected learning layers:

### 1. 🔬 14 Visual Student Labs (`labs/`)
*Master Index:* **[labs/README.md](./labs/README.md)**  
Every lab features: (1) Prerequisite Concept Refresher, (2) Step-by-Step Console Walkthrough with real screenshots, (3) AWS CLI v2 production commands (`eu-north-1`), and (4) Cost-Free Cleanup Safeguards.
* **[Lab 00: AWS Account Creation & Security Baseline Walkthrough](./labs/00_Account_Creation_Walkthrough.md)**
* **[Lab 01: Multi-AZ VPC Networking Infrastructure](./labs/lab_01_vpc_networking.md)**
* **[Lab 02: Network Security Controls: Security Groups vs NACLs & Flow Logs](./labs/lab_02_vpc_security_controls.md)**
* **[Lab 03: EC2 Compute, User Data Automation & Elastic IPs](./labs/lab_03_ec2_compute_bootstrap.md)**
* **[Lab 04: High-Availability Web Tier: ALB & Auto Scaling Groups](./labs/lab_04_alb_autoscaling_ha.md)**
* **[Lab 05: Serverless Backend: AWS Lambda & REST API Gateway](./labs/lab_05_serverless_lambda_apigateway.md)**
* **[Lab 06: Serverless Containers: Amazon ECR & ECS Fargate](./labs/lab_06_containers_ecr_ecs_fargate.md)**
* **[Lab 07: S3 Storage Lifecycle Tiering, Versioning & Security](./labs/lab_07_s3_storage_lifecycle.md)**
* **[Lab 08: Persistent Block & Shared File Storage: Amazon EBS vs EFS](./labs/lab_08_ebs_efs_storage.md)**
* **[Lab 09: Relational Database High Availability: Amazon RDS Multi-AZ](./labs/lab_09_rds_database_ha.md)**
* **[Lab 10: NoSQL Scalability & In-Memory Caching: DynamoDB & DAX](./labs/lab_10_dynamodb_nosql_dax.md)**
* **[Lab 11: Global Edge Acceleration & Defense: Route 53, CloudFront & WAF](./labs/lab_11_route53_cloudfront_edge.md)**
* **[Lab 12: Decoupled Enterprise Messaging: SNS, SQS & EventBridge](./labs/lab_12_sqs_sns_eventbridge_messaging.md)**
* **[Lab 13: Enterprise Observability: CloudWatch, CloudTrail & AWS Config](./labs/lab_13_observability_cloudwatch_cloudtrail_config.md)**
* **[Lab 14: FinOps & Cost Governance: Budgets, Cost Explorer & Calculator](./labs/lab_14_billing_cost_management.md)**

### 2. 🏛️ Architectural Multi-Service Tutorials (`tutorials/`)
*Master Index:* **[tutorials/README.md](./tutorials/README.md)**  
End-to-end multi-service architectures showing how individual AWS components interconnect into enterprise systems:
* **[Tutorial 00: AWS Account Creation, Root Securing & Security Baseline](./tutorials/Tutorial_00_AWS_Account_Creation_and_Security_Baseline.md)**
* **[Tutorial 01: Enterprise Multi-Tier VPC and Networking Infrastructure](./tutorials/Tutorial_01_Enterprise_Multi_Tier_VPC_and_Networking.md)**
* **[Tutorial 02: Serverless Microservices API and Asynchronous Data Processing](./tutorials/Tutorial_02_Serverless_Microservices_API_and_Data_Processing.md)**
* **[Tutorial 03: Event-Driven Enterprise Integration & Decoupled Messaging](./tutorials/Tutorial_03_Event_Driven_Integration_and_Decoupled_Messaging.md)**
* **[Tutorial 04: Global Edge Acceleration & Perimeter Security Defense](./tutorials/Tutorial_04_Global_Edge_Acceleration_and_Perimeter_Security.md)**
* **[Tutorial 05: Enterprise Observability, Auditing, and Compliance Loop](./tutorials/Tutorial_05_Enterprise_Observability_Auditing_and_Compliance.md)**
* **[Tutorial 06: Enterprise Multi-Account Governance with Organizations & SCPs](./tutorials/Tutorial_06_Enterprise_Governance_Organizations_and_SCPs.md)**

### 3. 📖 Comprehensive Conceptual & Service Explanations (`explanations/`)
*Master Index:* **[explanations/README.md](./explanations/README.md)**  
Exhaustive domain-by-domain knowledge base covering every single service, framework, and exam trap across all 4 CLF-C02 domains:
* **[Domain 1: Cloud Concepts](./explanations/01_Cloud_Concepts/)** - Cloud Economics & TCO, AWS CAF, Well-Architected Framework, Global Infrastructure, Shared Responsibility, and Disaster Recovery.
* **[Domain 2: Security and Compliance](./explanations/02_Security_and_Compliance/)** - IAM Identity, Shield & WAF, Threat Detection & Compliance (GuardDuty, Inspector, Macie), and KMS Encryption & Secrets Manager.
* **[Domain 3: Cloud Technology and Services](./explanations/03_Technology_and_Services/)** - Compute (EC2, ECS, EKS, Lambda), Storage (S3, EBS, EFS), Databases (RDS, DynamoDB, Aurora), Networking (VPC, Route 53, CloudFront), Management & Observability, Application Integration, and Analytics & AI.
* **[Domain 4: Billing, Pricing, and Support](./explanations/04_Billing_and_Pricing/)** - Pricing Models (Savings Plans, Spot, RI), Cost Allocation Tags, Budgets, Cost Explorer, Support Plans, and AWS Marketplace.

### 4. 📊 Production Architecture Mermaid Blueprints (`diagrams/`)
*Master Index:* **[diagrams/README.md](./diagrams/README.md)**  
10 standalone production blueprints rendering clear data flows, security perimeters, and service topology.

### 5. 🤖 AI Foundation Labs (`ai/foundation/labs/`)
1. **[Lab 1: Bedrock Playgrounds & Prompt Engineering](./ai/foundation/labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md)** - Master Temperature, Top-P, Zero-shot, Few-shot, and Chain-of-Thought prompting.
2. **[Lab 2: Building a RAG Knowledge Base](./ai/foundation/labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md)** - Ingest enterprise documents from S3 into OpenSearch Serverless via Titan Embeddings and query with Claude.
3. **[Lab 3: Responsible AI & PII Masking](./ai/foundation/labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md)** - Configure Denied Topics, content filters, and PII redaction using Amazon Bedrock Guardrails.

---

## 📚 Course Reference Books (Sources)

For comprehensive offline study and deeper explanations, the curriculum references two core textbooks stored locally in `cloud/foundation/sources/` (excluded from git):

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
