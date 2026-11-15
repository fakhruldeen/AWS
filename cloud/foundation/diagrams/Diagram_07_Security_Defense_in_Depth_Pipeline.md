# Master Architecture Blueprint: Multi-Layered Security & Threat Detection

> **Category:** Security, Identity, Governance & Compliance  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#security` `#defense-in-depth`

```mermaid
flowchart TD
    subgraph L1_Perimeter ["Layer 1: Edge & Perimeter Defense"]
        Shield["AWS Shield Standard / Advanced (L3/L4 DDoS Mitigation)"]
        WAF["AWS WAF (Layer 7 Filtering: SQLi, XSS, Rate Limiting)"]
    end

    subgraph L2_Network ["Layer 2: Network & VPC Security"]
        NACL["Network ACLs (Subnet Stateless Firewalls)"]
        SG["Security Groups (Instance Stateful Firewalls)"]
    end

    subgraph L3_Identity ["Layer 3: Identity & Access Management"]
        IAM["AWS IAM (Users, Roles, Least-Privilege Policies & MFA)"]
        IdC["IAM Identity Center (SSO across multi-account organization)"]
    end

    subgraph L4_Data ["Layer 4: Data Protection & Cryptography"]
        KMS["AWS KMS (Envelope Encryption at Rest & In-Transit)"]
        CloudHSM["AWS CloudHSM (Single-Tenant FIPS 140-2 Level 3 Hardware)"]
        SecretsMgr["AWS Secrets Manager (Automatic Credential Rotation)"]
    end

    subgraph L5_AuditDetection ["Layer 5: Continuous Threat Detection & Investigation"]
        CloudTrail["AWS CloudTrail (API Auditing)"]
        GuardDuty["Amazon GuardDuty (Intelligent Threat Detection via ML)"]
        Inspector["Amazon Inspector (Vulnerability CVE Scanning on EC2/ECR/Lambda)"]
        Macie["Amazon Macie (PII Discovery in S3 via ML)"]
        Detective["Amazon Detective (Graph-Based Root-Cause Analysis)"]
        SecurityHub["AWS Security Hub (Aggregated Single Pane of Glass)"]
    end

    Traffic[Internet Traffic] --> L1_Perimeter --> L2_Network --> L3_Identity --> L4_Data
    L2_Network -.-> L5_AuditDetection
    L3_Identity -.-> L5_AuditDetection
    L4_Data -.-> L5_AuditDetection
    GuardDuty --> Detective
    GuardDuty --> SecurityHub
    Inspector --> SecurityHub
    Macie --> SecurityHub
```
