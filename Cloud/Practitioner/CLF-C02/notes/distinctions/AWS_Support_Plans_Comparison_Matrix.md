# Exam Distinction Cheat Sheet: AWS Support Plans Comparison Matrix

> **Core Topic:** Billing, Pricing, and Support  
> **Target Exam:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Source Origin:** Tom Taulli (*O'Reilly, 2026*), Ch 15; Official AWS Pricing Documentation

---

## The 4 Support Plans Comprehensive Comparison Matrix

AWS offers four distinct support tiers: **Basic**, **Developer**, **Business**, and **Enterprise Support** (plus Enterprise On-Ramp for mid-tier enterprise needs):

| Support Dimension | Basic Support | Developer Support | Business Support | Enterprise Support |
| :--- | :--- | :--- | :--- | :--- |
| **Monthly Cost** | **Included Free** with every AWS account. | Greater of **$29/month** or **3% of monthly AWS usage**. | Greater of **$100/month** or tiered % of monthly AWS usage. | Greater of **$15,000/month** or tiered % of monthly AWS usage. |
| **Target Workload** | Exploring AWS, experimental, personal sandbox. | Experimenting or testing in non-production development environments. | Running **production workloads** in AWS. | Running **business-critical workloads** with 24/7 mission-critical operations. |
| **Who Can Open Cases?** | Customer Service & Billing cases only (zero technical support cases). | **1 primary contact** can open unlimited technical cases. | **Unlimited contacts** can open unlimited technical cases. | **Unlimited contacts** can open unlimited technical cases. |
| **Support Channels** | Web ticketing for billing/account questions only. | Email / Web ticketing via AWS Console (business hours only). | **24/7 phone, email, and live chat access** to Cloud Support Engineers. | **24/7 phone, email, and live chat access** to Senior Cloud Support Engineers. |
| **Case Response Times** | No SLA for technical cases. | • General Guidance: **< 24 business hours**<br>• System Impaired: **< 12 business hours** | • General Guidance: **< 24 hrs**<br>• System Impaired: **< 12 hrs**<br>• Production System Impaired: **< 4 hrs**<br>• Production System Down: **< 1 hr** | • General Guidance: **< 24 hrs**<br>• System Impaired: **< 12 hrs**<br>• Prod System Impaired: **< 4 hrs**<br>• Prod System Down: **< 1 hr**<br>• **Business-Critical System Down: < 15 minutes** |
| **AWS Trusted Advisor** | **7 core checks** (Root MFA, basic security groups, S3 permissions, service limits). | **7 core checks** (Same as Basic). | **Full library of all Trusted Advisor checks** across all 5 pillars + API access. | **Full library of all Trusted Advisor checks** across all 5 pillars + API access. |
| **Technical Account Manager (TAM)** | None. | None. | None. | **Designated Technical Account Manager (TAM)** dedicated to your organization. |
| **Concierge Support Team** | None. | None. | None. | Dedicated Concierge team for billing, account, and payment assistance. |
| **Infrastructure Event Management (IEM)** | None. | None. | Available for an **additional fee**. | **Included at no additional fee** (architectural guidance for major product launches/Black Friday). |
| **Third-Party Software Support** | None. | None. | Troubleshooting common operating systems (Linux/Windows) and 3rd party software (Apache, SQL Server). | Full guidance for complex hybrid stacks and third-party software integrations. |

---

## 🎯 Exam Trigger Scenarios & Keywords

### Scenario 1:
> *"A startup is launching its production e-commerce store on AWS and needs 24/7 phone and live chat access to AWS technical support engineers, with a response time of under 1 hour if the production system goes down. What is the MINIMUM cost-effective support plan required?"*  
> **Correct Answer:** **Business Support** (minimum tier for 24/7 phone/chat support and <1 hr production system down response time).

### Scenario 2:
> *"An enterprise running mission-critical banking applications requires a 15-minute response time for business-critical outages and a designated Technical Account Manager (TAM) who provides proactive architectural reviews and coordinates support engineers. Which support plan must they subscribe to?"*  
> **Correct Answer:** **Enterprise Support** (the only plan that includes a designated TAM and 15-minute response time SLA).

### Scenario 3:
> *"A company wants access to the complete library of AWS Trusted Advisor checks across all five pillars (Cost, Performance, Security, Fault Tolerance, and Service Limits). What is the lowest-cost support plan that provides this?"*  
> **Correct Answer:** **Business Support** (Basic and Developer only provide 7 core checks; Business unlocks the full check library).

### Scenario 4:
> *"A retail company is preparing for its annual Black Friday sale and wants AWS cloud engineers to review its architectural capacity and monitor operational events during the launch week. Which program provides this, and which plan includes it?"*  
> **Correct Answer:** **AWS Infrastructure Event Management (IEM)**, included at no additional charge in **Enterprise Support** (available for an extra fee in Business).

---

## 💡 Quick Memory Hook
- **Basic** = **Free** (Billing questions only, 7 Trusted Advisor checks).
- **Developer** = **Business Hours Web Only** ($29/mo, 12–24h response, 1 contact).
- **Business** = **24/7 Phone/Chat + Production Down in <1h** ($100/mo, Full Trusted Advisor).
- **Enterprise** = **TAM + 15-Minute Response** ($15k/mo, Concierge, IEM included).
