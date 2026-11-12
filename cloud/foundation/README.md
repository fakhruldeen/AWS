# AWS Certified Cloud Practitioner (CLF-C02) Track

> **Course Track:** Cloud Foundation  
> **Instructor:** Mohamed Fakhruldeen  
> **Target Certification:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Repository:** `fakhruldeen/AWS` -> `cloud/foundation/`

---

## 🎯 Track Overview

The Cloud Foundation curriculum prepares learners for the **AWS Certified Cloud Practitioner (CLF-C02)** exam through foundational cloud architecture, security best practices, core AWS services, and cost management.

```mermaid
flowchart LR
    Syllabus["1. Exam Blueprint & Domains\n(syllabus/)"] --> Notes["2. Conceptual & Service Notes\n(notes/)"]
    Notes --> Slides["3. Marp Lecture Slides\n(slides/)"]
    Slides --> Labs["4. 100% Free-Tier Labs\n(labs/)"]
    Labs --> Refs["5. Reference Books\n(sources/ - Local Reference)"]
    Refs --> Questions["6. Practice Questions Bank\n(questions_bank/ - GitIgnored)"]
```

---

## 📁 Directory Structure

```text
cloud/foundation/
├── README.md                      <-- (This file)
│
├── syllabus/                      <-- Official CLF-C02 Exam Blueprint & Domain Roadmaps
│   ├── CLF-C02_Master_Blueprint.md
│   ├── Domain_1_Cloud_Concepts.md (24%)
│   ├── Domain_2_Security_Compliance.md (30%)
│   ├── Domain_3_Cloud_Technology.md (34%)
│   ├── Domain_4_Billing_Pricing.md (12%)
│   └── Exam_Distinction_CheatSheet.md
│
├── notes/                         <-- Atomic Study Notes & Architectural Deep Dives
│   ├── concepts/                  (Global Infra, Well-Architected, Shared Responsibility, CAF)
│   └── services/                  (Compute, Storage, Database, Networking, Security, Billing, AI)
│
├── slides/                        <-- Student Presentation Slide Decks (Marp Format)
│   └── Module_01_Cloud_Concepts_and_Architecture_Slides.md
│
├── labs/                          <-- Hands-On Student Lab Manuals (100% Free-Tier Compliant)
│   ├── Lab_01_AWS_IAM_Least_Privilege_and_MFA.md
│   ├── Lab_02_Static_Website_S3_and_CloudFront.md
│   ├── Lab_03_Resilient_MultiAZ_Web_Tier_EC2.md
│   └── Lab_04_Proactive_Budget_Alerts_AWS_Budgets.md
│
├── sources/                       <-- Offline Reference Literature (GitIgnored / Local Only)
│   ├── Rajesh Daswani - AWS Certified Cloud Practitioner Certification (Packt)
│   └── Tom Taulli - AWS Certified Cloud Practitioner Study Guide (O'Reilly)
│
└── questions_bank/                <-- 2,924 Offline Practice Questions (GitIgnored)
    ├── README.md                  (Catalog index and source attribution)
    ├── EXAM_OBJECTIVES_ALIGNMENT_REPORT.md
    ├── CloudCertPrep_Questions/   (1,050 questions)
    ├── AwsCcpTrainer_Questions/   (987 questions)
    ├── ExamTopics_Questions/      (290 questions)
    ├── Quban301_Practice_Questions/ (174 questions)
    ├── CertPrep_Offline_Questions/ (136 questions)
    ├── Edurely_Questions/         (115 questions)
    ├── CertSafari_Questions/      (79 questions)
    ├── SecByte_Questions/         (72 questions)
    ├── FreeCram_Questions/        (13 questions)
    └── ExamDumpsNet_Questions/    (8 questions)
```

---

## 📚 Recommended Reference Books (Course Sources)

Students seeking further in-depth explanations, alternative analogies, or extended enterprise case studies can refer to these two foundational textbooks available locally in the `sources/` directory:

| Reference Book | Author & Publisher | Edition & ISBN | Key Focus & Strengths |
|---|---|---|---|
| **AWS Certified Cloud Practitioner (CLF-C02) Certification Guide** | **Rajesh Daswani**<br>*Packt Publishing* | 2nd Edition (2026)<br>`ISBN: 978-1-83546-429-8` | **Hands-On Exam Preparation:** Focused chapter reviews, scenario walk-throughs, practical console tips, and domain-by-domain summaries mapped to CLF-C02 objectives. |
| **AWS Certified Cloud Practitioner (CLF-C02) Study Guide** | **Tom Taulli**<br>*O'Reilly Media* | 1st Edition (2026)<br>`ISBN: 978-8-34164-022-2` | **Architectural & Business Concepts:** Deep explanations of cloud economics, Total Cost of Ownership (TCO), organizational governance, and enterprise cloud migration strategies. |

> [!NOTE]
> *Notice on Local References:* The `sources/` and `questions_bank/` directories contain copyrighted literary and assessment assets and are strictly excluded from online version control (`.gitignore`). Students access them locally during classroom instruction.

---

## 🚀 Hands-On Student Labs

All labs are designed to run within the **AWS Free Tier** with zero infrastructure cost:
1. **[Lab 1: IAM Least Privilege & MFA](./labs/Lab_01_AWS_IAM_Least_Privilege_and_MFA.md)** - Root account hardening, password policy enforcement, and group-based RBAC.
2. **[Lab 2: Static S3 & CloudFront Distribution](./labs/Lab_02_Static_Website_S3_and_CloudFront.md)** - Global HTTPS content delivery using CloudFront Origin Access Control (OAC).
3. **[Lab 3: Fault-Tolerant Multi-AZ EC2 Tier](./labs/Lab_03_Resilient_MultiAZ_Web_Tier_EC2.md)** - Deploying dual Availability Zone Apache instances behind an Application Load Balancer.
4. **[Lab 4: Proactive Budget Alerts with AWS Budgets](./labs/Lab_04_Proactive_Budget_Alerts_AWS_Budgets.md)** - Setting automated actual and forecasted spending thresholds.
