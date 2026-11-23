# AWS Certification, Training & Delivery Repository

> **GitHub Repository:** `fakhruldeen/AWS`  
> **Author & Trainer:** Mohamed Fakhruldeen  
> **Knowledge Base Sync:** Mirrored 1-to-1 with Obsidian Second Brain (`Documents/Obsidian Vault/Brain/AWS`)  
> **Active Certification Tracks:**
> 1. **Cloud Foundation:** AWS Certified Cloud Practitioner (`CLF-C02`)
> 2. **Cloud Architecture Associate:** AWS Certified Solutions Architect - Associate (`SAA-C03`)
> 3. **AI Foundation:** AWS Certified AI Practitioner (`AIF-C01`)
> 4. **AI Engineering Associate:** AWS Certified Machine Learning Engineer - Associate (`MLA-C01`)

---

## 🎯 Dual-Track Mission

This repository is engineered for two strategic purposes:
1. **Personal Certification Mastery:** Concise, high-yield study notes, architectural trade-off comparison matrices ("X vs Y"), distractor analysis tricks, and verified candidate practice question pools mapped against official exam domains.
2. **Professional Student Delivery & Training:** Pedagogically paced lecture decks, Marp presentation slides, visual architecture diagrams, step-by-step hands-on lab manuals, and end-to-end multi-service build tutorials for classroom delivery.

---

## 🧭 The Unified 12-Step Pedagogical Model

Every certification curriculum is completely self-contained and follows a standardized 6-phase, 12-step pedagogical lifecycle:

```text
Phase 0: Orientation & Foundations
  ├── 01_Syllabus              Official blueprint, domain weighting, study schedules
  └── 02_Prerequisites         Underlying CS, networking, math & cloud fundamentals

Phase 1: Conceptual Delivery & Architecture
  ├── 03_Lectures              Instructor delivery lesson plans with embedded exam questions
  ├── 04_Slides                Marp presentation slides for classroom delivery
  ├── 05_Diagrams              Standalone production Mermaid architecture blueprints
  └── 06_Explanations          Comprehensive domain-by-domain concept & service guides

Phase 2: Practical Implementation
  ├── 07_Hands_On_Labs                  100% Free-Tier / cost-aware hands-on labs with CLI runbooks
  └── 08_Tutorials             End-to-end multi-service production build tutorials

Phase 3: Synthesis & Retention
  └── 09_Notes_and_Cheatsheets                 High-yield study notes, distinction tables & cheat sheets

Phase 4: Assessment & Exam Simulation
  ├── 10_Knowledge_Checks      Module-by-module rapid diagnostic retention quizzes
  └── 11_Practice_Exams    Curated scenario sets, community pools & timed mock exams

Phase 5: Authority & Provenance
  └── 12_Sources               Reference textbooks, whitepapers & documentation indices
```

---

## 📁 Repository Directory Structure

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
│   ├── README.md                              (Cloud domain roadmap and track index)
│   ├── Practitioner/
│   │   ├── README.md                          (Cloud Practitioner track overview)
│   │   └── CLF-C02/                           <-- AWS Certified Cloud Practitioner (ACTIVE)
│   │       ├── 00_START_HERE.md               (🚀 Student Study Dashboard & 7-Day Fast-Track Plan)
│   │       ├── README.md                      (CLF-C02 Master Course Portal)
│   │       ├── 01_Syllabus/
│   │       ├── 02_Prerequisites/
│   │       ├── 03_Lectures/
│   │       ├── 04_Slides/
│   │       ├── 05_Diagrams/
│   │       ├── 06_Explanations/
│   │       ├── 07_Hands_On_Labs/
│   │       ├── 08_Tutorials/
│   │       ├── 09_Notes_and_Cheatsheets/
│   │       ├── 10_Knowledge_Checks/
│   │       ├── 11_Practice_Exams/
│   │       └── 12_Sources/
│   │
│   └── Associate/
│       ├── README.md                          (Cloud Associate track overview)
│       └── SAA-C03/                           <-- Solutions Architect - Associate (ACTIVE)
│           ├── 00_START_HERE.md               (🚀 Student Study Dashboard & Associate Roadmap)
│           ├── README.md                      (SAA-C03 Master Course Portal)
│           ├── 01_Syllabus/
│           ├── 02_Prerequisites/
│           ├── 03_Lectures/
│           ├── 04_Slides/
│           ├── 05_Diagrams/
│           ├── 06_Explanations/
│           ├── 07_Hands_On_Labs/
│           ├── 08_Tutorials/
│           ├── 09_Notes_and_Cheatsheets/
│           ├── 10_Knowledge_Checks/
│           ├── 11_Practice_Exams/
│           └── 12_Sources/
│
├── AI/                                        <-- Domain 2: Artificial Intelligence & Machine Learning
│   ├── README.md                              (AI domain roadmap and track index)
│   ├── Practitioner/
│   │   ├── README.md                          (AI Practitioner track overview)
│   │   └── AIF-C01/                           <-- AWS Certified AI Practitioner (ACTIVE)
│   │       ├── 00_START_HERE.md               (🚀 Student Study Dashboard & 7-Day Fast-Track Plan)
│   │       ├── README.md                      (AIF-C01 Master Course Portal)
│   │       ├── 01_Syllabus/
│   │       ├── 02_Prerequisites/
│   │       ├── 03_Lectures/
│   │       ├── 04_Slides/
│   │       ├── 05_Diagrams/
│   │       ├── 06_Explanations/
│   │       ├── 07_Hands_On_Labs/
│   │       ├── 08_Tutorials/
│   │       ├── 09_Notes_and_Cheatsheets/
│   │       ├── 10_Knowledge_Checks/
│   │       ├── 11_Practice_Exams/
│   │       └── 12_Sources/
│   │
│   └── Associate/
│       ├── README.md                          (AI Associate track overview)
│       └── MLA-C01/                           <-- Machine Learning Engineer - Associate (ACTIVE)
│           ├── 00_START_HERE.md               (🚀 Student Study Dashboard & Associate Roadmap)
│           ├── README.md                      (MLA-C01 Master Course Portal)
│           ├── 01_Syllabus/
│           ├── 02_Prerequisites/
│           ├── 03_Lectures/
│           ├── 04_Slides/
│           ├── 05_Diagrams/
│           ├── 06_Explanations/
│           ├── 07_Hands_On_Labs/
│           ├── 08_Tutorials/
│           ├── 09_Notes_and_Cheatsheets/
│           ├── 10_Knowledge_Checks/
│           ├── 11_Practice_Exams/
│           └── 12_Sources/
│
├── scripts/                                   <-- Automation, exam runner & synchronization tools
│   ├── README.md                              (Tool documentation & CLI usage manual)
│   ├── aws_revision_runner.py                 (Interactive terminal revision & simulation engine)
│   ├── embed_questions_into_lessons.py        (Embeds scenario questions in lessons & tutorials)
│   ├── ingest_community_practice_pool.py      (Sanitizes and ingests community pools)
│   ├── merge_community_into_banks.py          (Merges deduplicated questions into banks)
│   ├── generate_community_focus_sets.py       (Extracts high-consensus priority sets)
│   ├── sync_community_practice_pool.sh        (Full-cycle synchronization orchestrator)
│   └── populate_associate_phases.py           (Harmonizes Associate 12-step directories)
│
└── tests/                                     <-- Quality, secret scanning & integrity validation
    └── verify_ecosystem_integrity.py          (Automated test suite with 148 validations)
```

---

## 🗺️ Certification Tracks & Domain Blueprints

### 1. ☁️ AWS Certified Cloud Practitioner (`CLF-C02`)
* **Target Audience:** Foundational cloud practitioners, architects, and technical sales.
* **Format:** 65 questions, 90 minutes, 700 passing score.
* **Portal:** **[Cloud/Practitioner/CLF-C02/README.md](./Cloud/Practitioner/CLF-C02/README.md)**

| Domain | Title | Weight | Practice Questions Pool | Key Practical Lab |
|:---:|:---|:---:|:---:|:---|
| **Domain 1** | Cloud Concepts | **24%** | ~580 Qs | [Lab 03: Multi-AZ Web Tier](./Cloud/Practitioner/CLF-C02/07_Hands_On_Labs/lab_03_ec2_compute_bootstrap.md) |
| **Domain 2** | Security and Compliance | **30%** | ~735 Qs | [Lab 01: IAM Least Privilege & MFA](./Cloud/Practitioner/CLF-C02/07_Hands_On_Labs/fast_track/Lab_01_AWS_IAM_Least_Privilege_and_MFA.md) |
| **Domain 3** | Cloud Technology and Services | **34%** | ~1,140 Qs | [Lab 07: S3 Storage Lifecycle](./Cloud/Practitioner/CLF-C02/07_Hands_On_Labs/lab_07_s3_storage_lifecycle.md) |
| **Domain 4** | Billing, Pricing, and Support | **12%** | ~469 Qs | [Lab 14: FinOps Cost Governance](./Cloud/Practitioner/CLF-C02/07_Hands_On_Labs/lab_14_billing_cost_management.md) |
| **TOTAL** | | **100%** | **2,716 Unique Questions** | **14 Visual Guided Labs** |

---

### 2. 🏛️ AWS Certified Solutions Architect - Associate (`SAA-C03`)
* **Target Audience:** Cloud architects designing highly available, cost-effective, and secure distributed systems.
* **Format:** 65 scenario questions, 130 minutes, 720 passing score.
* **Portal:** **[Cloud/Associate/SAA-C03/README.md](./Cloud/Associate/SAA-C03/README.md)**

| Domain | Title | Weight | Practice Questions Pool | Key Practical Lab |
|:---:|:---|:---:|:---:|:---|
| **Domain 1** | Design Secure Architectures | **30%** | 36 Curated + 1,019 Pool | [Lab 01: Multi-Tier Resilient VPC](./Cloud/Associate/SAA-C03/07_Hands_On_Labs/lab_01_multi_tier_resilient_vpc_architecture.md) |
| **Domain 2** | Design Resilient Architectures | **26%** | 32 Curated + 1,019 Pool | [Lab 02: Scalable Web Tier (ASG/ALB)](./Cloud/Associate/SAA-C03/07_Hands_On_Labs/lab_02_ha_scalable_web_tier_asg_alb.md) |
| **Domain 3** | Design High-Performing Architectures | **24%** | 28 Curated + 1,019 Pool | [Lab 03: Fault-Tolerant Aurora](./Cloud/Associate/SAA-C03/07_Hands_On_Labs/lab_03_aurora_fault_tolerant_relational_database.md) |
| **Domain 4** | Design Cost-Optimized Architectures | **20%** | 24 Curated + 1,019 Pool | [Lab 04: Decoupled SQS/SNS](./Cloud/Associate/SAA-C03/07_Hands_On_Labs/lab_04_decoupled_asynchronous_microservices_sqs_sns.md) |
| **TOTAL** | | **100%** | **1,019Q Community Practice Pool** | **5 Guided Architecture Labs** |

---

### 3. 🤖 AWS Certified AI Practitioner (`AIF-C01`)
* **Target Audience:** Developers, analysts, and business leaders deploying AI/ML and Generative AI on AWS.
* **Format:** 65 questions, 90 minutes, 700 passing score.
* **Portal:** **[AI/Practitioner/AIF-C01/README.md](./AI/Practitioner/AIF-C01/README.md)**

| Domain | Title | Weight | Core AWS Tooling Covered | Key Practical Lab |
|:---:|:---|:---:|:---|:---|
| **Domain 1** | Fundamentals of AI and ML | **20%** | SageMaker Studio, Canvas, Data Wrangler, Ground Truth | [Lab 01: Bedrock Playgrounds](./AI/Practitioner/AIF-C01/07_Hands_On_Labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) |
| **Domain 2** | Fundamentals of Generative AI | **24%** | Foundation Models, Tokens, Context Window, Embeddings | [Lab 01: Prompt Engineering](./AI/Practitioner/AIF-C01/07_Hands_On_Labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) |
| **Domain 3** | Applications of Foundation Models | **28%** | Amazon Bedrock, Knowledge Bases (RAG), Agents, Amazon Q | [Lab 02: Bedrock RAG Knowledge Base](./AI/Practitioner/AIF-C01/07_Hands_On_Labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md) |
| **Domain 4** | Guidelines for Responsible AI | **14%** | SageMaker Clarify (Bias & SHAP), Bedrock Guardrails | [Lab 03: Bedrock Guardrails & PII Masking](./AI/Practitioner/AIF-C01/07_Hands_On_Labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) |
| **Domain 5** | Security, Compliance, and Governance | **14%** | Bedrock Data Privacy, KMS encryption, PrivateLink | [Lab 03: Responsible AI & Safety](./AI/Practitioner/AIF-C01/07_Hands_On_Labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) |
| **TOTAL** | | **100%** | **1,825 Unique Questions Bank** | **12 Visual Hands-On Labs** |

---

### 4. 🧠 AWS Certified Machine Learning Engineer - Associate (`MLA-C01`)
* **Target Audience:** Data scientists and ML engineers building, scaling, and monitoring production ML and GenAI pipelines.
* **Format:** 65 scenario questions, 130 minutes, 720 passing score.
* **Portal:** **[AI/Associate/MLA-C01/README.md](./AI/Associate/MLA-C01/README.md)**

| Domain | Title | Weight | Core AWS Tooling Covered | Key Practical Lab |
|:---:|:---|:---:|:---|:---|
| **Domain 1** | Data Preparation for ML | **28%** | Glue, Kinesis, EMR, SageMaker Feature Store | [Lab 01: SageMaker Pipelines MLOps](./AI/Associate/MLA-C01/07_Hands_On_Labs/lab_01_sagemaker_pipelines_mlops_and_model_registry.md) |
| **Domain 2** | ML Model Development | **26%** | PEFT/LoRA, Continued Pre-training, SageMaker HPO | [Lab 04: PEFT/LoRA Fine-Tuning](./AI/Associate/MLA-C01/07_Hands_On_Labs/lab_04_peft_lora_fine_tuning_foundation_models.md) |
| **Domain 3** | Deployment & Orchestration | **22%** | Real-Time, Serverless, Async, Batch Transform | [Lab 02: SageMaker Inference Endpoints](./AI/Associate/MLA-C01/07_Hands_On_Labs/lab_02_sagemaker_inference_endpoints_comparison.md) |
| **Domain 4** | ML Solution Monitoring & Maintenance | **24%** | Model Monitor, Clarify (Bias/SHAP), Model Cards | [Lab 03: Automated Drift Detection](./AI/Associate/MLA-C01/07_Hands_On_Labs/lab_03_automated_drift_detection_model_monitor.md) |
| **TOTAL** | | **100%** | **542 Unique Questions Bank** | **5 Guided Engineering Labs** |

---

## 💻 Interactive Terminal Exam Simulation Engine

The repository includes a unified, high-performance terminal revision runner (**`scripts/aws_revision_runner.py`**) that supports all four certifications:

```bash
# -------------------------------------------------------------
# 1. PRACTICE MODE (Domain-specific drill with trick explanations)
# -------------------------------------------------------------
python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 2 -n 15 --tricks
python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 3 -n 10 --tricks
python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 1 -n 15
python3 scripts/aws_revision_runner.py --cert MLA --mode practice --domain 2 -n 10

# -------------------------------------------------------------
# 2. AUTHENTIC CANDIDATE PRACTICE SUITE DRILLS
# -------------------------------------------------------------
# SAA-C03: 1,019-question Community Practice Pool
python3 scripts/aws_revision_runner.py --cert SAA --community --mode practice -n 20 --tricks

# CLF-C02: 718-question Community Practice Pool
python3 scripts/aws_revision_runner.py --cert CLF --community --mode practice -n 20 --tricks

# CLF-C02: November 2026 Actual Release (393 questions)
python3 scripts/aws_revision_runner.py --cert CLF --release-2026 --mode practice -n 15 --tricks

# AIF-C01: 233-question Community Practice Pool
python3 scripts/aws_revision_runner.py --cert AIF --community --mode practice -n 15 --tricks

# MLA-C01: 106-question Community Practice Pool
python3 scripts/aws_revision_runner.py --cert MLA --community --mode practice -n 15 --tricks

# -------------------------------------------------------------
# 3. FULL-LENGTH TIMED EXAM SIMULATION (Official Clock & Passing Scores)
# -------------------------------------------------------------
python3 scripts/aws_revision_runner.py --cert CLF --mode mock
python3 scripts/aws_revision_runner.py --cert AIF --mode mock
python3 scripts/aws_revision_runner.py --cert SAA --mode mock
python3 scripts/aws_revision_runner.py --cert MLA --mode mock

# -------------------------------------------------------------
# 4. TARGETED WEAKNESS ADAPTIVE REVIEW
# -------------------------------------------------------------
python3 scripts/aws_revision_runner.py --cert CLF --mode weakness
python3 scripts/aws_revision_runner.py --cert SAA --mode weakness
```

---

## 🛡️ Repository Integrity & Quality Assurance

A dedicated integrity test suite (**`tests/verify_ecosystem_integrity.py`**) enforces zero broken links, schema validity, and secret safety:

```bash
python3 tests/verify_ecosystem_integrity.py
```

* **148 Automated Checks:** Validates JSON question bank schemas, unique IDs, domain coverage, lab scenario matrices, AWS CLI runbooks, and secret scanning across 767 repository files.
* **100% Free-Tier & Cost Guardrails:** All practical labs include cleanup instructions and use cost-conscious configurations.
* **Zero Broken Wiki-Links:** All Markdown documentation strictly utilizes relative paths.
* **Zero Third-Party Scraping Terminology:** Candidate questions are curated and attributed professionally under community consensus rubrics.

---

## 🛠️ Agent Toolkit for AWS Integration

This workspace natively integrates with the **[Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html)**:

* **AWS MCP Server (`.vscode/mcp.json` / `mcp.json`):** Connects to the AWS MCP server to search live documentation (`aws___search_documentation`) and retrieve official guides (`aws___read_documentation`) dynamically.
* **Agent Rules (`.agents/rules/aws-agent-rules.md`):** Strict verification against current AWS service capabilities, Well-Architected Framework guidelines, and Infrastructure as Code standards.
* **Agent Skills (`.agents/skills/`):** 26 specialized AWS runbooks covering Bedrock, SageMaker AI, IAM, VPC, and CloudFormation.
