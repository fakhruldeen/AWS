# Exam Distinction Cheat Sheet: AWS Health Dashboard (Global vs. Account)

> **Core Topic:** Management & Governance / Operational Health  
> **Target Exam:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Source Origin:** Classroom - Manara Course Revision Notes & Official AWS Documentation

---

## The "X vs. Y" Comparison Matrix

| Exam Dimension | AWS Service Health Dashboard (Global) | AWS Health Dashboard – Your Account (Personal) |
| :--- | :--- | :--- |
| **Authentication & Access** | **Publicly accessible website** (`health.aws.amazon.com`). Requires **NO AWS login or credentials**. | Accessed via the **AWS Management Console** after logging in (or via AWS Health API for Business/Enterprise support). |
| **Scope of View** | **Global public status:** Displays operational uptime/outages of **all AWS services across all 30+ AWS Regions globally**. | **Personalized account status:** Displays operational events, degradations, and maintenance **directly affecting YOUR specific running resources**. |
| **Scheduled Changes** | Broad announcements of general regional maintenance windows. | Alerts you to **specific scheduled maintenance dates** for your specific EC2 host instances, RDS maintenance windows, or SSL certificate renewals. |
| **Troubleshooting Guidance** | General status notices and AWS engineering progress updates. | Delivers **targeted, resource-level remediation steps** and troubleshooting advice tailored to your active infrastructure. |
| **Notification Integration** | Public RSS feeds only. | Native integration with **Amazon EventBridge**, CloudWatch, email, Slack, or SMS for automated proactive incident response. |

---

## 🎯 Exam Trigger Scenarios & Keywords

### Scenario 1:
> *"A company wants to check if there is an active global outage affecting Amazon DynamoDB in Europe (Frankfurt) without signing into the AWS Management Console. Which tool should they check?"*  
> **Correct Answer:** **AWS Service Health Dashboard** (public URL, no sign-in required).

### Scenario 2:
> *"An operations team receives an alert that an underlying physical hardware host running one of their production Amazon EC2 instances is scheduled for retirement next week. Where can the team view the impacted instance ID and migration guidance?"*  
> **Correct Answer:** **AWS Health Dashboard – Your Account** (formerly Personal Health Dashboard - provides account-specific impacted resources and remediation guidance).

---

## 💡 Quick Memory Hook
- **Service Health Dashboard** = **Everyone's Health** (Public weather report for the entire cloud).
- **Health Dashboard (Your Account)** = **Your Medical Chart** (Personalized health report specifically for your account's infrastructure).
