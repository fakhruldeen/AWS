# 🎯 Cloud Practitioner (CLF-C02) Student Revision Questions Library

> **Module:** Targeted Exam Revision Questions with Detailed Rationale & Trap Breakdowns  
> **Target Certification:** AWS Certified Cloud Practitioner (`CLF-C02`)  
> **Structure:** Mapped 1-to-1 against the 4 official exam domains + Full-Length Mock Exam.  
> **Master Knowledge Brain Link:** For the complete offline repository of **2,716 unique deduplicated practice questions** across all 4 domains (with redundancy eliminated from across industry practice pools), see the Knowledge Vault at `Brain/AWS/Questions_Bank/Unique_Revision_Banks/Cloud_Practitioner_CLF-C02/`.

---

## 🗺️ Revision Sets Catalog

| Document | Exam Domain | Official Weight | Focus & Key Traps |
| :--- | :--- | :---: | :--- |
| **[CLF_C02_Top_200_Most_Frequent_Exam_Questions.md](./CLF_C02_Top_200_Most_Frequent_Exam_Questions.md)** | **🏆 Top 200 Most Frequent (3–5x Repeated)** | **All 4 Domains (Exact Blueprint)** | **200 highest-frequency questions repeated across 3–5 exam pools (48 D1 / 60 D2 / 68 D3 / 24 D4) covering all 20 blueprint topics** |
| **[November_2026_Actual_Exam_Release_393Q.md](./November_2026_Actual_Exam_Release_393Q.md)** | **🔥 Nov 2026 Practice Release** | **All 4 Domains** | **Complete 393-question authentic candidate practice pool from November 2026 with 3-tier priority categorization** |
| **[CLF_C02_Community_Practice_Pool_718Q.md](./CLF_C02_Community_Practice_Pool_718Q.md)** | **🌐 Community Practice Pool** | **All 4 Domains** | **Comprehensive 718-question community practice suite with community consensus and rationale** |
| **[Community_High_Yield_Focus_Set.md](./Community_High_Yield_Focus_Set.md)** | **⭐ Community High Yield Focus** | **Top Priority** | **65 high-frequency community questions with verified consensus & distractor traps** |
| **[Domain_1_Cloud_Concepts_Revision_Questions.md](./Domain_1_Cloud_Concepts_Revision_Questions.md)** | Domain 1: Cloud Concepts | **24%** | Cloud economics, CAF perspectives, Well-Architected 6 pillars, DR tiers |
| **[Domain_2_Security_and_Compliance_Revision_Questions.md](./Domain_2_Security_and_Compliance_Revision_Questions.md)** | Domain 2: Security & Compliance | **30%** | IAM policies, Shared Responsibility boundaries, Shield/WAF, KMS, Artifact |
| **[Domain_3_Cloud_Technology_and_Services_Revision_Questions.md](./Domain_3_Cloud_Technology_and_Services_Revision_Questions.md)** | Domain 3: Technology & Services | **34%** | Compute options, S3 tiers, RDS vs DynamoDB, VPC routing, SQS vs SNS |
| **[Domain_4_Billing_and_Pricing_Revision_Questions.md](./Domain_4_Billing_and_Pricing_Revision_Questions.md)** | Domain 4: Billing & Pricing | **12%** | Savings Plans vs Spot, Support plan tiers (TAM), Budgets vs Cost Explorer |
| **[CLF_C02_Full_Length_Mock_Revision_Exam.md](./CLF_C02_Full_Length_Mock_Revision_Exam.md)** | Comprehensive Simulation | **100%** | 65-question timed mock simulation with score rubric |

---

## 💻 Interactive Terminal Revision Engine

Run the interactive CLI revision runner with the `--release-2026` or `--community` flags to drill specifically on authentic question pools:

```bash
# 1. Practice 15 questions from the November 2026 release with trick decryption
python3 scripts/aws_revision_runner.py --cert CLF --release-2026 --mode practice -n 15 --tricks

# 2. Drill by specific domain on the November 2026 pool
python3 scripts/aws_revision_runner.py --cert CLF --release-2026 --domain 2 --count 20

# 3. Practice questions from the 718-question Community Practice Pool
python3 scripts/aws_revision_runner.py --cert CLF --community --mode practice -n 20 --tricks

# 4. Take a full 65-question timed mock exam using the November 2026 release
python3 scripts/aws_revision_runner.py --cert CLF --release-2026 --mode mock
```
