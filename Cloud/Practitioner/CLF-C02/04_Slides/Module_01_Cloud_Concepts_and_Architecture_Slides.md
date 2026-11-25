---
marp: true
theme: default
paginate: true
header: "AWS Cloud Practitioner (CLF-C02) - Student Training"
footer: "© AWS Cloud Training Course | Domain 1: Cloud Concepts"
style: |
  section {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    padding: 40px;
    background-color: #fafafa;
  }
  h1 {
    color: #232f3e;
  }
  h2 {
    color: #ff9900;
  }
  .highlight {
    background-color: #fff3cd;
    padding: 2px 6px;
    border-radius: 4px;
  }
---

# AWS Certified Cloud Practitioner
## Module 1: Cloud Concepts & Global Architecture
**Domain 1 (24% of Exam Blueprint)**

*Instructor Delivery Deck & Student Lecture Notes*

---

# What is Cloud Computing?

Cloud computing is the **on-demand delivery of IT resources over the internet with pay-as-you-go pricing**.

### The 6 Advantages of Cloud Computing:
1. **Trade Capital Expense for Variable Expense (CapEx to OpEx):** No upfront data center investment.
2. **Benefit from Massive Economies of Scale:** Lower prices achieved by AWS aggregated buying power.
3. **Stop Guessing Capacity:** Scale up or down automatically based on actual demand.
4. **Increase Speed and Agility:** Provision servers in seconds instead of waiting months.
5. **Stop Spending Money Running Data Centers:** Eliminate "undifferentiated heavy lifting".
6. **Go Global in Minutes:** Deploy applications across 30+ regions worldwide with minimal latency.

---

# Cloud Deployment Models

```
         ┌─────────────────────────────────────────────────────────┐
         │                 Cloud Computing Models                  │
         └──────────┬───────────────────┬───────────────────┬──────┘
                    │                   │                   │
                    ▼                   ▼                   ▼
           ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
           │   Public Cloud  │ │  Private Cloud  │ │   Hybrid Cloud  │
           │ (100% on AWS)   │ │  (On-Premises)  │ │ (AWS + On-Prem) │
           └─────────────────┘ └─────────────────┘ └─────────────────┘
```

* **Public Cloud (All-in Cloud):** All components of the application run in the cloud (AWS).
* **Private Cloud (On-Premises):** Resources deployed on dedicated physical infrastructure in your own data center (using virtualization like VMware/OpenStack).
* **Hybrid Cloud:** Connected infrastructure bridging on-premises data centers with AWS using **AWS Direct Connect**, **AWS Site-to-Site VPN**, or **AWS Outposts**.

---

# Cloud Service Models: IaaS vs. PaaS vs. SaaS

| Model | What Customer Manages | What Cloud Provider Manages | Real-World AWS Example |
|:---|:---|:---|:---|
| **IaaS** *(Infrastructure as a Service)* | OS, Runtime, Applications, Data, Firewall | Physical servers, virtualization, networking, power | **Amazon EC2**, Amazon EBS |
| **PaaS** *(Platform as a Service)* | Application Code, Data, Configuration | Hardware, OS patching, database software, runtime | **AWS Elastic Beanstalk**, Amazon RDS |
| **SaaS** *(Software as a Service)* | User Settings & Data Input | Everything (end-user software application) | AWS Marketplace SaaS, Google Docs, Slack |

---

# AWS Global Infrastructure: Regions & AZs

### 1. AWS Regions
* Geographically isolated physical locations around the world (e.g., `us-east-1`, `eu-west-1`).
* **Criteria for Selection:** Compliance & Data Sovereignty > Latency > Service Availability > Cost.

### 2. Availability Zones (AZs)
* Each Region contains a minimum of **3 discrete, isolated Availability Zones**.
* An AZ consists of one or more physical data centers with redundant power and networking.
* Connected via ultra-low-latency private dark fiber (<1–2 ms).
* **High Availability Rule:** Always deploy across at least **two AZs (Multi-AZ)**!

---

# Edge Infrastructure: CloudFront vs. Local Zones

```
[Global Internet Users]
          │
          ▼
   [Edge Locations] ───► Amazon CloudFront (CDN Caching) & Route 53 (DNS)
          │
          ▼
   [AWS Local Zones] ──► Single-digit ms latency to urban centers (LA, Chicago)
          │
   [AWS Wavelength] ───► Embedded inside 5G telecom carrier networks
          │
   [AWS Outposts] ─────► Physical AWS racks installed in customer on-prem facility
```

---

# The AWS Well-Architected Framework: 6 Pillars

1. **Operational Excellence:** Perform operations as code, make small reversible changes, learn from failures. *(CloudFormation, Systems Manager)*
2. **Security:** Least privilege, trace all actions, defense-in-depth, protect data in transit & at rest. *(IAM, KMS, WAF, GuardDuty)*
3. **Reliability:** Automatically recover from failure, test recovery, scale horizontally. *(ELB, Auto Scaling, Route 53)*
4. **Performance Efficiency:** Democratize advanced tech, use serverless, go global in minutes. *(Lambda, CloudFront)*
5. **Cost Optimization:** Adopt a consumption model, analyze expenditure, stop heavy lifting. *(Cost Explorer, Budgets, Spot)*
6. **Sustainability:** Minimize environmental impact, right-size compute, use AWS Graviton chips.

---

# AWS Cloud Adoption Framework (AWS CAF 3.0)

Organizes transformation guidance into **6 Perspectives**:

```
      Business Capabilities                     Technical Capabilities
┌───────────────────────────────┐         ┌───────────────────────────────┐
│ 1. Business (Value & ROI)     │         │ 4. Platform (Cloud Arch)      │
│ 2. People (Skills & Training) │         │ 5. Security (Risk & Privacy)  │
│ 3. Governance (Priorities)    │         │ 6. Operations (Monitoring/SLA)│
└───────────────────────────────┘         └───────────────────────────────┘
```

### The 7 Rs of Cloud Migration:
1. **Rehost (Lift-and-Shift):** Move without code changes (*AWS Application Migration Service - MGN*).
2. **Replatform (Lift, Tinker & Shift):** Minor cloud optimization (*move DB to Amazon RDS*).
3. **Refactor (Rearchitect):** Redesign for cloud-native (*microservices, AWS Lambda*).
4. **Repurchase (Drop & Shop):** Switch to SaaS product (*AWS Marketplace*).
5. **Retain:** Keep legacy on-premises for now.
6. **Retire:** Decommission unneeded applications.
7. **Relocate:** Hypervisor-level VM migration (*VMware Cloud on AWS*).

---

# Cloud Economics: CapEx vs. OpEx

* **CapEx (Capital Expenditure):** Large upfront investment in physical data centers, servers, and software licenses that depreciate over time.
* **OpEx (Operational Expenditure):** Ongoing day-to-day operational expenses where you pay only for resources consumed (Pay-As-You-Go).

### The Total Cost of Ownership (TCO) Equation:

$$
TCO_{OnPrem} = Hardware + RealEstate + Power + Cooling + Cabling + AdminStaff
$$

AWS eliminates the **indirect costs** (real estate, electricity, cooling, physical security, hardware repairs).

---

# Module 1 Student Review Quiz

1. **Which factor is the MOST CRITICAL when selecting an AWS Region for a bank governed by national financial privacy laws?**
   * A) Proximity to development team
   * B) Compliance and legal data sovereignty requirements *(Correct)*
   * C) The cheapest compute pricing
   * D) Highest number of Edge Locations

2. **A company wants to migrate 100 on-prem servers to AWS as quickly as possible with zero code changes. Which strategy should they select?**
   * A) Refactor
   * B) Rehost (Lift-and-Shift) using AWS MGN *(Correct)*
   * C) Repurchase
   * D) Retain
