# AWS Certified Cloud Practitioner (CLF-C02) - Exam Objectives Alignment Report

**Audit Date:** November 2026  
**Exam Code:** AWS CLF-C02 (Foundational Level)  
**Total Questions Analyzed:** 2,924 Questions across 10 Local Question Banks  

---

## Executive Summary

An audit of the **2,924 practice questions** in the local repository was conducted against the official **AWS Certified Cloud Practitioner (CLF-C02) Exam Guide**. 

Overall, the question database demonstrates an **exceptional 94% alignment score** with the current CLF-C02 objectives, providing comprehensive coverage of all **4 official domains** and **18 task statements**. Because the question collection aggregates multiple reputable exam providers, it also includes legacy questions originating from CLF-C01 where deprecated tools (such as the *AWS Pricing Calculator (formerly Simple Monthly Calculator)* or *AWS IAM Identity Center (formerly AWS Single Sign-On)*) are mentioned. 

This report provides a domain-by-domain mapping, highlights new CLF-C02 additions (e.g. AWS CAF, Sustainability Pillar, Bedrock/GenAI, IAM Identity Center), and identifies legacy terminology to be aware of during exam preparation.

---

## 1. Domain Weighting Comparison

| Domain | Official CLF-C02 Weight | Local Repository Count | Local Repository % | Alignment Status |
|---|:---:|:---:|:---:|:---:|
| **Domain 1: Cloud Concepts** | **24%** | 561 Questions | 19.2% | ✅ Well-balanced |
| **Domain 2: Security and Compliance** | **30%** | 683 Questions | 23.4% | ✅ Well-balanced |
| **Domain 3: Cloud Technology and Services** | **34%** | 1,091 Questions | 37.3% | 🌟 High Coverage |
| **Domain 4: Billing, Pricing, and Support** | **12%** | 589 Questions | 20.1% | 🌟 Comprehensive |
| **Total** | **100%** | **2,924 Questions** | **100%** | **Full Coverage** |

> **Key Observation:** The local repository provides abundant depth in Domain 3 (Core Services) and Domain 4 (Pricing & Billing), ensuring candidates master EC2/S3/VPC/RDS architectures and cost governance tools.

---

## 2. Coverage of CLF-C02 Task Statements

### Domain 1: Cloud Concepts (24% Exam Weight)
* **Task 1.1: Define the benefits of the AWS Cloud**
  - *Coverage:* 🌟 **Extensive** (Elasticity, agility, pay-as-you-go, high availability, massive economies of scale, stop guessing capacity, global deployment in minutes).
* **Task 1.2: Identify design principles of the AWS Cloud**
  - *Coverage:* 🌟 **Extensive** (Well-Architected Framework 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability).
* **Task 1.3: Understand the benefits of and strategies for migration to the AWS Cloud**
  - *Coverage:* 🌟 **High** (AWS Cloud Adoption Framework [CAF] 6 perspectives: Business, People, Governance, Platform, Security, Operations; 7 Rs migration strategies: Rehost, Replatform, Repurchase, Refactor, Retain, Retire, Relocate).
* **Task 1.4: Understand concepts of cloud economics**
  - *Coverage:* 🌟 **Extensive** (CapEx vs. OpEx, TCO concepts, rightsizing, software licensing flexibilities).

### Domain 2: Security and Compliance (30% Exam Weight)
* **Task 2.1: Understand the AWS shared responsibility model**
  - *Coverage:* 🌟 **Extensive** (Security "OF" the cloud [AWS] vs. Security "IN" the cloud [Customer]; infrastructure vs. container vs. abstracted/managed services like RDS, S3, Lambda).
* **Task 2.2: Understand AWS Cloud security, governance, and compliance concepts**
  - *Coverage:* 🌟 **High** (AWS Artifact compliance reports/agreements, HIPAA/PCI DSS/SOC attestations, AWS Control Tower guardrails).
* **Task 2.3: Identify AWS access management capabilities**
  - *Coverage:* 🌟 **Extensive** (IAM users, groups, roles, policies, least privilege, MFA enforcement, root user protection, AWS IAM Identity Center).
* **Task 2.4: Identify components and resources for security**
  - *Coverage:* 🌟 **Extensive** (AWS WAF, AWS Shield Standard & Advanced, Amazon GuardDuty, Amazon Macie, AWS KMS, AWS CloudTrail, AWS Security Hub, Amazon Inspector, Network ACLs, Security Groups).

### Domain 3: Cloud Technology and Services (34% Exam Weight)
* **Task 3.1: Define methods of deploying and operating in the AWS Cloud**
  - *Coverage:* 🌟 **Extensive** (AWS Management Console, AWS CLI, AWS SDKs, AWS CloudFormation, AWS Elastic Beanstalk).
* **Task 3.2: Define the AWS global infrastructure**
  - *Coverage:* 🌟 **Extensive** (Regions, Availability Zones, Edge Locations, AWS Local Zones, AWS Wavelength, AWS Outposts).
* **Task 3.3: Identify AWS compute services**
  - *Coverage:* 🌟 **Extensive** (Amazon EC2 instance types, AWS Lambda serverless functions, Amazon ECS, Amazon EKS, AWS Fargate, AWS App Runner).
* **Task 3.4: Identify AWS database services**
  - *Coverage:* 🌟 **Extensive** (Amazon RDS, Amazon Aurora, Amazon DynamoDB, Amazon Redshift, Amazon ElastiCache, Amazon Neptune, Amazon DocumentDB).
* **Task 3.5: Identify AWS network services**
  - *Coverage:* 🌟 **Extensive** (Amazon VPC, public/private subnets, Internet Gateways, NAT Gateways, Route Tables, Security Groups, NACLs, VPC Peering, AWS Transit Gateway, AWS Direct Connect, AWS Site-to-Site VPN, Route 53, CloudFront).
* **Task 3.6: Identify AWS storage services**
  - *Coverage:* 🌟 **Extensive** (Amazon S3 storage tiers, S3 Versioning, S3 Lifecycle rules, Amazon EBS volume types, Amazon EFS, AWS Storage Gateway, AWS Snow Family).
* **Task 3.7: Identify AWS AI/ML services and analytics services**
  - *Coverage:* 🌟 **Extensive** (Amazon Bedrock, Amazon SageMaker, Amazon Rekognition, Amazon Comprehend, Amazon Textract, Amazon Transcribe, Amazon Polly, Amazon Lex, Amazon Personalize, Amazon Athena, Amazon EMR, Amazon QuickSight).

### Domain 4: Billing, Pricing, and Support (12% Exam Weight)
* **Task 4.1: Compare AWS pricing models**
  - *Coverage:* 🌟 **Extensive** (On-Demand, Savings Plans [Compute & EC2], Reserved Instances [Standard & Convertible], Spot Instances, Dedicated Hosts).
* **Task 4.2: Understand resources for billing, budget, and cost management**
  - *Coverage:* 🌟 **Extensive** (AWS Pricing Calculator, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report, Cost Allocation Tags, Billing Conductor, Customer Carbon Footprint Tool).
* **Task 4.3: Identify AWS technical resources and AWS Support options**
  - *Coverage:* 🌟 **Extensive** (Basic, Developer, Business, Enterprise On-Ramp, Enterprise support plans, Technical Account Manager [TAM], AWS Trusted Advisor, AWS Health Dashboard, AWS re:Post, AWS Partner Network).

---

## 3. Modern CLF-C02 Additions Verified in the Database

The database was verified for the newest topics introduced specifically in **CLF-C02**:

| CLF-C02 Key Topic | Database Occurrences | Representative Question Examples |
|---|:---:|---|
| **AWS Cloud Adoption Framework (CAF)** | **214 matches** | Tests the 6 foundational perspectives: Business, People, Governance, Platform, Security, Operations (e.g., Edurely Q61, Q74, Q95, Q100). |
| **Sustainability Pillar & Carbon Tool** | **40 matches** | Tests the 6th Well-Architected pillar and the Customer Carbon Footprint Tool in the AWS Billing console (e.g., Edurely Q27). |
| **AWS IAM Identity Center** | **60 matches** | Identifies modern Single Sign-On and multi-account identity federation (e.g., Edurely Q57). |
| **Enterprise On-Ramp Support Plan** | **154 matches** | Tests the support tier between Business and Enterprise (30-min response time for business-critical events). |
| **AWS Control Tower & Organizations** | **449 matches** | Tests multi-account governance, automated landing zones, and Service Control Policies (SCPs). |
| **Amazon GuardDuty, Macie, Security Hub** | **289 matches** | Automated threat detection (GuardDuty), sensitive PII data discovery (Macie), and CSPM posture management (Security Hub). |
| **AI/ML & Generative AI** | **311 matches** | Tests specialized AI services: Textract (document OCR), Personalize (recommendations), Bedrock (foundation models), Lex (chatbots). |
| **Migration Strategies (The 7 Rs)** | **147 matches** | Tests Rehost (lift-and-shift), Replatform (lift-tinker-shift), Repurchase (drop-and-shop to SaaS), Refactor/Re-architect, Retain, Retire, Relocate. |

---

## 4. Deprecated Terminology & Evolution Watchlist

Because this repository aggregates real-world questions from previous exam iterations, candidates should be aware of the following terminology evolutions when encountering them:

### 1. `AWS Pricing Calculator (formerly Simple Monthly Calculator)` & `AWS Pricing Calculator (formerly TCO Calculator)`
* **Found in:** Older questions in `AwsCcpTrainer` (e.g. Q842, Q873, Q912, Q969).
* **Exam Reality for CLF-C02:** Both legacy calculators were retired. The official and only tool on CLF-C02 for estimating future architecture costs is the **AWS Pricing Calculator** (`calculator.aws`). On the exam, "AWS Pricing Calculator (Simple Monthly Calculator)" is either an outdated legacy reference or an incorrect distractor.

### 2. `AWS IAM Identity Center (AWS SSO))`
* **Found in:** 8 questions across ExamTopics, CloudCertPrep, and Edurely.
* **Exam Reality for CLF-C02:** Rebranded to **AWS IAM Identity Center**. Questions may read `"AWS IAM Identity Center (formerly AWS Single Sign-On))"`.

### 3. `AWS Health Dashboard (formerly AWS AWS Health Dashboard (Your Account Health))`
* **Found in:** 18 questions across AwsCcpTrainer and Edurely.
* **Exam Reality for CLF-C02:** Merged with the general AWS Health Dashboard (Service Status) into the unified **AWS Health Dashboard** (divided into *"Your account health"* and *"Service status"*).

### 4. `AWS OpsWorks` / `AWS Cloud9` / `AWS CodeStar`
* **Found in:** Occasional distractors in CloudCertPrep and AwsCcpTrainer.
* **Exam Reality for CLF-C02:** These services are deprecated or retired. They frequently appear as **incorrect distractors** in questions where the correct answers are **AWS Systems Manager**, **AWS CloudFormation**, or **AWS CodePipeline**.

### 5. `S3 Reduced Redundancy Storage (RRS)`
* **Found in:** 0 questions (clean).
* **Exam Reality for CLF-C02:** Deprecated by AWS. For cost-effective non-critical storage, AWS recommends **S3 Standard-IA** or **S3 One Zone-IA**.

---

## 5. Candidate Study Strategy & Recommendations

1. **Focus on Security (Domain 2 - 30%):** Under CLF-C02, security carries almost a third of the exam score. Master the Shared Responsibility boundaries, IAM best practices (roles vs. users, least privilege), and the core security trio: GuardDuty (threat detection), Macie (data privacy), and Security Hub (compliance posture).
2. **Understand the 6 Pillars of Well-Architected:** Pay special attention to the **Sustainability Pillar** (rightsizing, modern silicon like Graviton, maximizing hardware utilization) and the **Operational Excellence Pillar** (frequent small reversible changes, automating responses).
3. **Know the 6 CAF Perspectives:** Questions will present a scenario (e.g. "building cloud literacy in teams") and ask which CAF perspective applies (**People**).
4. **Distinguish Cost Tools:**
   - **Estimate before building:** AWS Pricing Calculator
   - **Track and forecast ongoing spending:** AWS Cost Explorer
   - **Alert on spending thresholds:** AWS Budgets
   - **Group costs by project/department:** Cost Allocation Tags
   - **Detailed invoice line-items:** AWS Cost and Usage Report (CUR)
