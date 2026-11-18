# AWS Management & Governance — Map of Content (MOC)

> **Domain:** 03_Services / Management & Governance  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], SysOps Administrator, Solutions Architect

---

## 1. Architectural Taxonomy of AWS Management & Governance

AWS management and governance services provide continuous visibility, centralized multi-account guardrails, operational automation, and compliance auditing:

```mermaid
flowchart TD
    Mgmt["AWS Management & Governance"]
    
    subgraph Observability["1. Observability & Auditing"]
        CW["Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards)"]
        CT["AWS CloudTrail (API call logging & user governance auditing)"]
        Health["AWS Health Dashboard (Outage notices & scheduled maintenance)"]
    end
    
    subgraph MultiAccount["2. Multi-Account Structure & Guardrails"]
        Org["AWS Organizations (Consolidated billing, OUs, SCP guardrails)"]
        Tower["AWS Control Tower (Automated landing zone & preventive controls)"]
        RAM["AWS RAM (Share subnets & Transit Gateway across accounts)"]
    end
    
    subgraph Operations["3. Operational Automation & Compliance"]
        Config["AWS Config (Configuration history & continuous compliance evaluation)"]
        SSM["AWS Systems Manager (SSM) (Session Manager, Patch Manager, Run Command)"]
        TA["AWS Trusted Advisor (Real-time best practice advisor across 5 pillars)"]
    end
    
    Mgmt --> Observability
    Mgmt --> MultiAccount
    Mgmt --> Operations
```

---

## 2. High-Yield "The Big Three" Observability Comparison

```mermaid
flowchart LR
    CT["AWS_CloudTrail\n'Who made the API call, when, and from where?'"]
    CW["Amazon_CloudWatch\n'How is my application performing right now?'"]
    CFG["AWS_Config\n'What was my resource configuration then vs. now?'"]
```

| Service | Primary Question Answered | Data Artifacts | Target Audience |
| :--- | :--- | :--- | :--- |
| **[[AWS_CloudTrail]]** | *"Who made the API call, when, and from where?"* | Event logs, user identities, source IPs, AWS KMS encryption. | Security, Auditing, Compliance |
| **[[Amazon_CloudWatch]]** | *"How is my application performing right now?"* | Metrics, CloudWatch Logs, Alarms, Container Insights. | DevOps, SysAdmins, SREs |
| **[[AWS_Config]]** | *"What was my resource configuration then vs. now?"* | Configuration Items (CIs), timeline history, rule evaluations. | Governance, Compliance, SecOps |

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[Amazon_CloudWatch]]** | Monitoring & Observability | Metrics (15 months retention), Alarms (EC2 action, SNS), Logs Insights. |
| **[[AWS_CloudTrail]]** | API Governance & Auditing | Multi-region trail, Management vs. Data events, immutable S3 log storage. |
| **[[AWS_Organizations]]** | Centralized Multi-Account Governance | Consolidated Billing, Organizational Units (OUs), Service Control Policies (SCPs). |
| **[[AWS_Control_Tower]]** | Automated Multi-Account Landing Zone | Well-Architected multi-account baseline, Account Factory, Guardrails. |
| **[[AWS_Config]]** | Configuration Management & Rules | Track configuration drift, point-in-time state, automatic remediation. |
| **[[AWS_Systems_Manager]]** | Operations Hub & Node Management | Session Manager (no port 22/bastion), Patch Manager, Parameter Store. |
| **[[AWS_Trusted_Advisor]]** | Cloud Best Practice Advisor | 5 pillars (Cost, Security, Fault Tolerance, Performance, Quotas). |
| **[[AWS_Health_Dashboard]]** | Service Availability & Account Impact | Global service events vs. personal impact alerts on your specific resources. |
| **[[AWS_Resource_Access_Manager_RAM]]** | Cross-Account Resource Sharing | Share VPC subnets, Transit Gateways, Route 53 rules without duplication. |
---

## 7. Post-Topic Question Simulation & Retention Check

Test your understanding of Management & Observability with these 5 exam-style questions:

### Question 1
**Which AWS service records API activity, user logins, and administrative actions across an AWS account, providing an immutable audit trail for security investigations and compliance?**
- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) AWS Config
- D) AWS Trusted Advisor

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS CloudTrail**  
- **Why it's correct:** AWS CloudTrail captures and records every API call made via the Console, CLI, SDKs, or AWS services, answering: *"Who made the call, when was it made, from what IP address, and on what resource?"*
</details>

### Question 2
**A system administrator needs to monitor EC2 CPU utilization, trigger automated scaling actions when metrics exceed 80%, and send SMS alerts to engineers. Which service should be used?**
- A) AWS CloudTrail
- B) Amazon CloudWatch
- C) AWS Config
- D) AWS Systems Manager

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Amazon CloudWatch**  
- **Why it's correct:** Amazon CloudWatch monitors application and operational performance metrics, aggregates logs, and triggers CloudWatch Alarms that can execute EC2 Auto Scaling or send SNS notifications.
</details>

### Question 3
**Which service tracks configuration changes over time, evaluates resource configurations against compliance rules (e.g. ensuring all S3 buckets are encrypted), and provides automated remediation?**
- A) AWS CloudTrail
- B) AWS Config
- C) Amazon Inspector
- D) AWS Trusted Advisor

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS Config**  
- **Why it's correct:** AWS Config records the timeline of configuration changes to AWS resources and compares active configurations against predefined or custom rules to detect compliance drift.
</details>

### Question 4
**An enterprise has 200 member accounts in AWS Organizations. Which feature allows administrators to set central guardrails that restrict which AWS services and API actions can be executed within member accounts?**
- A) AWS IAM Identity Center
- B) Service Control Policies (SCPs)
- C) AWS Trusted Advisor
- D) Amazon CloudWatch Synthetics

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Service Control Policies (SCPs)**  
- **Why it's correct:** Service Control Policies (SCPs) in AWS Organizations define maximum allowed permissions for member accounts or Organizational Units (OUs), acting as boundaries that even account root users cannot bypass.
</details>

### Question 5
**Which online tool provides continuous automated guidance across 5 categories: Cost Optimization, Security, Fault Tolerance, Performance, and Service Quotas?**
- A) AWS Trusted Advisor
- B) AWS Health Dashboard
- C) AWS CloudTrail
- D) AWS Compute Optimizer

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A) AWS Trusted Advisor**  
- **Why it's correct:** AWS Trusted Advisor inspects your environment and compares configurations against AWS best practices across all 5 key categories, providing real-time recommendations and cost savings estimates.
</details>
