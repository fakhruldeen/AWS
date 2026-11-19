# 🖥️ AWS Certified Cloud Practitioner (CLF-C02) Marp Lecture Slide Decks

> **Module:** Classroom Presentation Slide Decks  
> **Course:** AWS Certified Cloud Practitioner (`CLF-C02`)  
> **Format:** Marp (Markdown Presentation Ecosystem)  
> **Exam Version Alignment:** Official CLF-C02 Blueprint (2026)  
> **Textbook Grounding:** Rajesh Daswani (*Packt 2026*), Tom Taulli (*O'Reilly 2026*), Gaurav Kankaria (*Orange 2026*)

---

## 🗺️ Master Slide Decks Index

| Deck File | Domain Alignment | Exam Weight | Key Covered Topics & Focus |
|:--- |:--- |:---:|---|
| **[Module 01 Slides](./Module_01_Cloud_Concepts_and_Architecture_Slides.md)** | **Domain 1:** Cloud Concepts | 24% | Cloud value proposition, CapEx vs OpEx, agility vs elasticity, Global Infrastructure (Regions, AZs, Edge), Well-Architected Framework (6 Pillars), CAF 3.0 & 7 Rs of Migration. |
| **[Module 02 Slides](./Module_02_Compute_Storage_and_Databases_Slides.md)** | **Domain 3:** Cloud Technology (Compute & Data) | 34% (Part 1) | EC2 purchasing options (On-Demand, Spot, Savings Plans, Dedicated), ECS, EKS, Fargate, Lambda, S3 storage tiers, EBS vs EFS, RDS Multi-AZ vs Read Replicas, Aurora, DynamoDB. |
| **[Module 03 Slides](./Module_03_Networking_Security_and_Identity_Slides.md)** | **Domain 2:** Security & Networking | 30% | Shared Responsibility Model, IAM (Users, Groups, Roles, Policies, MFA, Least Privilege), VPC fundamentals, Security Groups vs NACLs, Route 53, CloudFront, Shield, WAF, KMS, GuardDuty, Macie. |
| **[Module 04 Slides](./Module_04_Monitoring_Governance_and_DevOps_Slides.md)** | **Domain 2 & 3:** Governance & Management | ~15% | CloudWatch vs CloudTrail vs Config, AWS Organizations & Consolidated Billing, SCPs, AWS Control Tower, Systems Manager, CloudFormation, Trusted Advisor, Compute Optimizer. |
| **[Module 05 Slides](./Module_05_Billing_Pricing_and_Support_Slides.md)** | **Domain 4:** Billing & Support | 12% | Pricing Calculator vs Cost Explorer, AWS Budgets, Cost Allocation Tags, Support Plans (Basic, Developer, Business, Enterprise On-Ramp, Enterprise), TAM & Concierge roles. |

---

## 🚀 How to Render & Present with Marp

### 1. Visual Studio Code / Antigravity IDE:
* Install the **Marp for VS Code** extension (`marp-team.marp-vscode`).
* Open any slide deck markdown file and click the **Marp preview** icon in the top right.
* Press `F1` and select **Marp: Export Slide Deck...** to export to PDF, HTML, or PowerPoint (PPTX).

### 2. Command Line Interface (CLI):
```bash
# Export individual deck to PDF
npx @marp-team/marp-cli@latest Module_01_Cloud_Concepts_and_Architecture_Slides.md --pdf -o Module_01_Slides.pdf

# Export all decks to interactive HTML presentations
npx @marp-team/marp-cli@latest *.md --html
```

---

## 🎯 Pedagogical Alignment & Interactive Checkpoints

Each deck is structured into four pedagogical segments:
1. **Mental Model & Blueprint Foundation:** Architectural diagrams and core concepts.
2. **Deep-Dive Mechanics:** Service boundaries, configurations, and console screenshots.
3. **High-Yield Comparison Matrices:** Side-by-side distinction tables resolving exam distractor choices.
4. **Interactive In-Class Quizzes:** 3-4 exam scenario check questions with animated answer reveals for real-time classroom formative assessment.
