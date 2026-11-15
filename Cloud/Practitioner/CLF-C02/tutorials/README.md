# 🏗️ AWS End-to-End Architectural Build Tutorials

> **Workspace:** `/home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/tutorials/`  
> **Target Audience:** Engineering Students, Cloud Architects, and Practitioners  
> **Methodology:** Multi-service, production-grade architectural builds with architecture diagrams, step-by-step console instructions, and CLI verification.

---

## 🗺️ Architectural Tutorials Catalog

| Tutorial # | Title & Architecture | Services Orchestrated | Target Enterprise Pattern |
| :--- | :--- | :--- | :--- |
| **Tutorial 00** | [Account Creation & Security Baseline](Tutorial_00_AWS_Account_Creation_and_Security_Baseline.md) | AWS Signup, Root MFA, IAM Admin, Budgets | Day-1 Account security baseline & zero-spend alert |
| **Tutorial 01** | [Multi-Tier VPC & Bastion Host](Tutorial_01_Multi_Tier_VPC_and_Bastion_Host.md) | VPC, Public/Private Subnets, IGW, NAT, Bastion EC2 | 3-Tier Enterprise network segmentation & secure jump-host |
| **Tutorial 02** | [High Availability Auto Scaling Web Tier](Tutorial_02_Highly_Available_AutoScaling_Web_Tier.md) | ALB, Auto Scaling Group, Launch Templates, Apache | Fault-tolerant horizontal scaling across 2 Availability Zones |
| **Tutorial 03** | [Secure Multi-AZ RDS with Secrets Manager](Tutorial_03_Secure_Multi_AZ_RDS_with_Secrets_Manager.md) | Amazon RDS MySQL, Secrets Manager, Lambda Rotation | Zero hardcoded passwords & automated credential rotation |
| **Tutorial 04** | [Serverless Event-Driven Pipeline](Tutorial_04_Serverless_Event_Driven_Pipeline.md) | Amazon S3, AWS Lambda (Python), Amazon SNS | Asynchronous event processing without managing servers |
| **Tutorial 05** | [Infrastructure as Code with CloudFormation](Tutorial_05_Automating_Infrastructure_with_CloudFormation.md) | AWS CloudFormation, YAML Stacks, Change Sets | Declarative, repeatable multi-environment infrastructure |
| **Tutorial 06** | [Multi-Account Governance with SCPs](Tutorial_06_Enterprise_Governance_Organizations_and_SCPs.md) | AWS Organizations, Service Control Policies, Control Tower | Multi-account guardrails, region restrictions, consolidated billing |

---

## 🔒 Execution Standards

1. **Dual Track Delivery:** Every tutorial supports visual management console execution and command-line automation.
2. **Region Consistency:** All resources target `eu-north-1` (Stockholm).
3. **Automated Teardown:** Every tutorial concludes with cleanup instructions to ensure zero ongoing cloud spend.
