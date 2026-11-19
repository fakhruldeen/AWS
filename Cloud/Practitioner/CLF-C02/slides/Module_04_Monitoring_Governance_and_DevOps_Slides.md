---
marp: true
theme: default
paginate: true
header: "AWS Cloud Practitioner (CLF-C02) - Student Training"
footer: "© AWS Cloud Training Course | Module 4: Monitoring, Governance & DevOps"
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
## Module 4: Monitoring, Governance & DevOps Automation
**Domains 2 & 3: Security, Governance & Technology**

*Instructor Delivery Deck & Student Lecture Notes*

---

# The Governance Trio: CloudWatch vs. CloudTrail vs. Config

```
       [ Amazon CloudWatch ]          [ AWS CloudTrail ]           [ AWS Config ]
        Performance & Logs            Auditing & Who Did It     Configuration & Rules
    "How are resources running?"     "Who made the API call?"   "Is it compliant with rules?"
```

| Dimension | CloudWatch | CloudTrail | AWS Config |
| :--- | :--- | :--- | :--- |
| **Focus** | Performance metrics, logs, alarms. | User API history & audit logs. | Resource inventory & compliance. |
| **Data Type** | Numbers (CPU, Network) & Log lines. | JSON audit events (`DeleteBucket`). | Configuration Items (CIs). |
| **Action** | Triggers Auto Scaling or SNS alerts. | Delivers audit records to S3. | Automatically remediates drift via SSM. |
| **Key Note** | Requires **Agent** to monitor RAM! | Retains 90 days in console for free. | Generates historical visual timeline. |

---

# AWS Organizations & Service Control Policies (SCPs)

Consolidated governance and billing across multiple AWS accounts.

```
                         [ Organization Root Account ]
                                      │
                 ┌────────────────────┴────────────────────┐
                 ▼                                         ▼
         [ Core Services OU ]                     [ Workloads OU ]
         ├── Security Account                     ├── [ Dev OU ] (Dev Accounts)
         └── Log Archive Account                  └── [ Prod OU ] (Prod Accounts)
```

- **Organizational Units (OUs):** Logical groupings of accounts sharing policies.
- **Service Control Policies (SCPs):**
  - **Guardrails that define the maximum permissions** member accounts can have.
  - Can **DENY** actions to all users, **including the root user of member accounts**!
  - SCPs do **not** grant permissions; an IAM policy is still required.

---

# AWS Trusted Advisor & AWS Health Dashboard

### AWS Trusted Advisor (Automated Architecture Consultant)
Scans your environment against **5 Well-Architected Pillars**:
1. **Cost Optimization** (Unused resources, idle instances).
2. **Performance** (High connection usage, CloudFront rules).
3. **Security** (MFA on root, open security group ports).
4. **Fault Tolerance** (Multi-AZ missing, unbacked-up EBS).
5. **Service Limits** (Alerts when reaching 80%+ of regional quotas).

### AWS Health Dashboard
- **Service Health Dashboard (Global):** Public webpage displaying global service outages.
- **Health Dashboard – Your Account (Personal):** Logged-in view showing upcoming scheduled maintenance and outages **affecting your specific resources**.

---

# Loosely Coupled Architecture: SQS vs. SNS

### Amazon SQS (Simple Queue Service)
- **Pull-Based Queue:** Consumer processes pull messages.
- Buffers messages durably (1 min to 14 days) to absorb traffic surges.
- **Standard:** Nearly unlimited throughput, at-least-once delivery, best-effort ordering.
- **FIFO:** Strictly ordered, exactly-once processing (names end in `.fifo`).

### Amazon SNS (Simple Notification Service)
- **Push-Based Pub/Sub:** Instantly broadcasts messages to multiple subscribers (1-to-many).
- Sends **Email**, **SMS**, **Mobile Push**, or triggers **Lambda** and **SQS**.

### The Fan-Out Pattern
- Publish once to an **SNS Topic**; SNS duplicates and pushes to multiple **SQS Queues** simultaneously for independent microservice processing.

---

# DevOps Automation & Infrastructure as Code (IaC)

### AWS CloudFormation (Infrastructure as Code)
- Declarative templates (**JSON or YAML**) modeling entire cloud environments.
- **Stacks:** Collections of resources created, updated, or deleted as a single unit.
- **Change Sets:** Previews the exact changes, modifications, or replacements CloudFormation will execute before applying updates!

### AWS Elastic Beanstalk (Platform as a Service - PaaS)
- Developers simply upload application code (Java, Python, Node.js, Docker).
- Elastic Beanstalk provisions and manages EC2, Auto Scaling, Load Balancers, and databases automatically while retaining full administrative control.

---

# Modern Full-Stack & Application Testing

### AWS Amplify
- Framework and hosting service designed for **frontend web and mobile developers**.
- Accelerates building full-stack apps with built-in authentication (Cognito), data APIs (AppSync), database storage (DynamoDB), and automated Git-based CDN hosting.

### AWS Device Farm
- Cloud testing service to run automated tests on **real physical mobile devices and web browsers**.
- Simulates real hardware gestures, battery drains, location data, and network variations without maintaining an on-premises device laboratory.

---

# Summary & Key Takeaways

1. **Governance Trio:**
   - CloudWatch = Resource Performance & Alarms.
   - CloudTrail = API Auditing ("Who Did What").
   - AWS Config = Compliance evaluation & configuration history.
2. **SCPs:** Act as non-negotiable guardrails that can restrict the root user of child accounts.
3. **Decoupling:** Use SQS to buffer spikes and SNS to broadcast notifications.
4. **CloudFormation Change Sets:** Always preview the impact of template changes before updating production stacks.
5. **Amplify vs. Device Farm:**
   - Amplify builds and hosts full-stack apps.
   - Device Farm tests apps on real physical mobile phones in the cloud.

---

# Module 4 Student Review Quiz

1. **An IT auditor needs a complete record of who terminated a critical production EC2 instance, including the IAM username, IP address, and timestamp. Which service should they query?**
   * A) Amazon CloudWatch Metrics
   * B) AWS CloudTrail Event History *(Correct — audits API calls and management events)*
   * C) AWS Config Configuration History
   * D) Amazon Inspector Assessment Reports

2. **A company wants to continuously evaluate whether all Amazon S3 buckets in their account have server-side encryption enabled, and trigger automated remediation if non-compliant. Which service should they use?**
   * A) AWS Trusted Advisor
   * B) AWS Config *(Correct — continuously monitors, tracks, and evaluates resource configurations)*
   * C) AWS Systems Manager Parameter Store
   * D) Amazon GuardDuty

3. **Which service enables teams to model, provision, and version their entire cloud infrastructure using declarative JSON or YAML templates?**
   * A) AWS CodeBuild
   * B) AWS CloudFormation *(Correct — Infrastructure as Code / IaC)*
   * C) AWS Elastic Beanstalk
   * D) AWS CodeDeploy

