# Master Architecture Blueprint: Enterprise Organizations & Consolidated Billing

> **Category:** Cloud Financial Management & Governance  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#organizations` `#billing` `#finops`

```mermaid
flowchart TD
    subgraph OrgRoot ["AWS Organizations Root Container"]
        direction TB
        
        ManagementAcc["Management (Payer) Account
- Single Consolidated Monthly Bill
- Volume Tier Aggregation across all accounts
- Administers Master Service Control Policies (SCPs)"]

        subgraph OUs ["Organizational Units (OUs)"]
            direction LR
            OU_Core["Security & Core OU"]
            OU_Prod["Production Workloads OU"]
            OU_Dev["Dev / Sandbox OU"]
        end

        ManagementAcc --> OU_Core
        ManagementAcc --> OU_Prod
        ManagementAcc --> OU_Dev

        subgraph Accounts ["Member Accounts"]
            Acc_Log["Log Archive Account (CloudTrail in S3)"]
            Acc_Sec["Security Tooling (GuardDuty / Security Hub)"]
            Acc_Prod1["Production App 1 (EC2 / RDS)"]
            Acc_Prod2["Production App 2 (EKS)"]
            Acc_Dev1["Developer Sandbox Account"]
        end

        OU_Core --> Acc_Log
        OU_Core --> Acc_Sec
        OU_Prod --> Acc_Prod1
        OU_Prod --> Acc_Prod2
        OU_Dev --> Acc_Dev1
    end

    SCP_Deny["SCP: Deny Root User Usage & Unencrypted S3"] -.->|Inherited by all accounts| OU_Prod
    SCP_Limit["SCP: Disallow High-Cost GPU Instances"] -.->|Enforced strictly| OU_Dev

    subgraph FinOpsTooling ["Enterprise Billing Tools"]
        CUR["Cost & Usage Reports (CUR) in S3 -> Athena SQL"]
        Budgets["AWS Budgets (Forecasted Spend Alerts)"]
        CE["Cost Explorer (Historical Trend Analysis)"]
    end

    ManagementAcc --> FinOpsTooling
```
