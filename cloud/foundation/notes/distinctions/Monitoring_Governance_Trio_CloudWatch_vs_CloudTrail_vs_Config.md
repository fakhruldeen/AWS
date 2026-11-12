# Exam Distinction Cheat Sheet: The Governance Trio (CloudWatch vs. CloudTrail vs. AWS Config)

> **Core Topic:** Management & Governance, Monitoring, Auditing & Compliance  
> **Target Exam:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Source Origin:** Rajesh Daswani (*Packt, 2026*), Ch 16; Tom Taulli (*O'Reilly, 2026*), Ch 5 & 7.

---

## The "Governance Trio" Quick Decision Matrix

This is one of the most frequently tested three-way comparisons on AWS exams:

| Exam Dimension | Amazon CloudWatch | AWS CloudTrail | AWS Config |
| :--- | :--- | :--- | :--- |
| **The Core Question** | **"How are my resources performing?"** | **"Who did what, where, and when?"** | **"What does my resource configuration look like, and is it compliant?"** |
| **Primary Domain** | **Performance & Monitoring:** Metrics, logs, alarms, dashboards, auto-scaling triggers. | **Auditing & Governance:** User activity, API call history, security forensics. | **Compliance & Inventory:** Configuration history, resource relationships, compliance rules. |
| **Key Data Tracked** | Time-series metrics (CPU, Memory via Agent, Network, IOPS), application log streams. | JSON audit records of every AWS API call (console logins, CLI commands, SDK calls). | Configuration items (security group rules, S3 bucket encryption, EBS volume settings). |
| **Trigger / Reaction** | Triggers alarms, sends SNS notifications, executes EC2 Auto Scaling policies. | Delivers log files to S3, detects anomalous API spikes using CloudTrail Insights. | Evaluates compliance against rules (e.g. `s3-bucket-ssl-requests-only`), triggers auto-remediation via SSM. |
| **Default Retention** | Metrics stored for **15 months**; Logs stored indefinitely by default. | Event History stored in console for **90 days** for free; Trails store logs in S3 indefinitely. | Configuration history stored in S3 for custom retention periods. |

---

## 🎯 Exam Trigger Scenarios & Keywords

### Scenario 1:
> *"An administrator wants to be notified via email when the CPU utilization of an Amazon EC2 instance exceeds 85% for five consecutive minutes. Which service should they configure?"*  
> **Correct Answer:** **Amazon CloudWatch** (CloudWatch Alarm on the `CPUUtilization` metric with an SNS notification action).

### Scenario 2:
> *"A security auditor needs to determine which IAM user terminated a production Amazon RDS database instance at 2:00 AM last night, including the caller's IP address. Which service should they inspect?"*  
> **Correct Answer:** **AWS CloudTrail** (records the caller identity, timestamp, source IP, and API action: `DeleteDBInstance`).

### Scenario 3:
> *"A cloud compliance officer wants to verify whether any Amazon S3 buckets currently have public read access enabled, and automatically revert any newly created public buckets to private. Which service should they use?"*  
> **Correct Answer:** **AWS Config** (evaluates configuration compliance against rules like `s3-bucket-public-read-prohibited` and triggers remediation).

### Scenario 4:
> *"An operations team wants a visual timeline showing all changes made to a security group over the last six months to understand when port 22 was opened. Which service provides this configuration timeline?"*  
> **Correct Answer:** **AWS Config** (provides visual configuration timeline and resource change history).

---

## 💡 Quick Memory Hook
- **CloudWatch** = **The Heart Rate Monitor** (Monitors vital signs, performance, CPU, memory, alarms).
- **CloudTrail** = **The CCTV Camera** (Records who walked in the room, what button they pushed, and when).
- **AWS Config** = **The Building Inspector** (Checks if the building meets safety codes, building rules, and tracks structural changes over time).
