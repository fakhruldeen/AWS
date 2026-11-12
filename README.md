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
├── cloud/
│   └── foundation/                            <-- Track 1: AWS Certified Cloud Practitioner (CLF-C02)
│       ├── README.md                          (Track roadmap, syllabus, and module index)
│       │
│       ├── syllabus/                          <-- Exam Blueprint & Domain Breakdowns
│       │   ├── CLF-C02_Master_Blueprint.md
│       │   └── Exam_Distinction_CheatSheet.md
│       │
│       ├── slides/                            <-- Student Lecture Decks (Marp Format)
│       │   └── Module_01_Cloud_Concepts_and_Architecture_Slides.md
│       │
│       ├── labs/                              <-- Hands-On Student Lab Manuals (100% Free Tier)
│       │   ├── Lab_01_AWS_IAM_Least_Privilege_and_MFA.md
│       │   ├── Lab_02_Static_Website_S3_and_CloudFront.md
│       │   ├── Lab_03_Resilient_MultiAZ_Web_Tier_EC2.md
│       │   └── Lab_04_Proactive_Budget_Alerts_AWS_Budgets.md
│       │
│       ├── notes/                             <-- Mirrored Atomic Study Notes
│       │   ├── concepts/                      (Global Infra, Well-Architected, Shared Responsibility, CAF)
│       │   └── services/                      (Compute, Storage, Database, Networking, Security, Billing)
│       │
│       ├── sources/                           <-- Reference Literature (Packt & O'Reilly - GitIgnored)
│       │
│       └── questions_bank/                    <-- 2,924 Offline Practice Questions (GitIgnored)
│           ├── README.md                      (Questions library catalog & source attribution)
│           ├── EXAM_OBJECTIVES_ALIGNMENT_REPORT.md (Detailed 2,924-question blueprint audit)
│           ├── CloudCertPrep_Questions/       (1,050 questions)
│           ├── AwsCcpTrainer_Questions/       (987 questions)
│           ├── ExamTopics_Questions/          (290 questions)
│           ├── Quban301_Practice_Questions/   (174 questions)
│           ├── CertPrep_Offline_Questions/    (136 questions)
│           ├── Edurely_Questions/             (115 questions)
│           ├── CertSafari_Questions/          (79 questions)
│           ├── SecByte_Questions/             (72 questions)
│           ├── FreeCram_Questions/            (13 questions)
│           └── ExamDumpsNet_Questions/        (8 questions)
│
└── ai/
    └── foundation/                            <-- Track 2: AWS Certified AI Practitioner (AIF-C01)
        ├── syllabus/                          <-- Course Syllabus & Official Exam Guide
        │   ├── AIF-C01_Course_Syllabus.md
        │   └── AIF-C01_Exam_Guide_and_Blueprint.md
        │
        ├── slides/                            <-- Student Lecture Decks (Marp Format)
        │   ├── Module_01_AI_and_GenAI_Foundations_Slides.md
        │   └── Module_02_Amazon_Bedrock_and_RAG_Slides.md
        │
        ├── labs/                              <-- Hands-On Student Lab Manuals
        │   ├── Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md
        │   ├── Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md
        │   └── Lab_03_Responsible_AI_Bedrock_Guardrails.md
        │
        └── notes/                             <-- Atomic Study Notes & Cheat Sheets
            ├── 01_GenAI_Fundamentals.md
            ├── 02_Prompt_Engineering_Guide.md
            ├── 03_Amazon_Bedrock_and_RAG.md
            ├── 04_Amazon_SageMaker_Suite.md
            ├── 05_Responsible_AI_and_Governance.md
            └── 06_AIF-C01_Exam_CheatSheet.md
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

## 🚀 Student Hands-On Learning Paths

### Cloud Foundation Labs:
1. **[Lab 1: IAM Least Privilege & MFA](./cloud/foundation/labs/Lab_01_AWS_IAM_Least_Privilege_and_MFA.md)** - Secure the root user, enforce password policies, and test role-based access.
2. **[Lab 2: Global Static S3 & CloudFront](./cloud/foundation/labs/Lab_02_Static_Website_S3_and_CloudFront.md)** - Host private S3 assets and distribute over HTTPS via CloudFront with OAC.
3. **[Lab 3: Fault-Tolerant Multi-AZ Web Tier](./cloud/foundation/labs/Lab_03_Resilient_MultiAZ_Web_Tier_EC2.md)** - Deploy EC2 across two Availability Zones behind an Application Load Balancer.
4. **[Lab 4: Proactive Cost Alerts with AWS Budgets](./cloud/foundation/labs/Lab_04_Proactive_Budget_Alerts_AWS_Budgets.md)** - Set budget alerts to guarantee zero surprise bills.

### AI Foundation Labs:
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
