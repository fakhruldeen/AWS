# Lecture 01: Designing Secure AWS Architectures

> **Course Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Domain 1: Design Secure Architectures (30% Exam Weighting)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Design multi-account governance and access control using AWS Organizations Service Control Policies (SCPs) and IAM Identity Center.
2. Delegate cross-account permissions securely using `sts:AssumeRole` with external IDs to prevent the confused deputy problem.
3. Architect multi-tier VPC security perimeters combining Security Groups, Network ACLs, and AWS Network Firewall.
4. Eliminate public internet traversal for AWS service traffic using Gateway and Interface VPC Endpoints (AWS PrivateLink).
5. Implement end-to-end data protection at rest using AWS KMS Customer Managed Keys (envelope encryption) and in transit with ACM.
6. Evaluate intelligent threat detection and automated vulnerability remediation with GuardDuty, Macie, Inspector, and AWS Config.

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:00] 1. The AWS Well-Architected Security Pillar & Defense-in-Depth
[01:00 - 02:30] 2. Identity & Access: Cross-Account Roles, SCPs & IAM Identity Center
[02:30 - 04:00] 3. VPC Perimeter Defense: SGs vs. NACLs, VPC Endpoints & WAF/Shield
[04:00 - 05:00] 4. Cryptographic Protection: KMS Envelope Encryption, Secrets Manager & S3 Object Lock
[05:00 - 05:45] 5. Detection & Compliance: GuardDuty, Macie, Inspector & AWS Config Remediation
[05:45 - 06:00] 6. SAA-C03 High-Yield Scenarios, Exam Traps & Q&A
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. Identity & Cross-Account Access (Whiteboard Prompt)
- *Whiteboard Diagram:* Draw two AWS accounts: Account A (Workload/EC2) and Account B (Data/S3).
- **Key Talking Point:** *"Never generate static IAM access keys for servers. Instead, attach an instance profile to EC2 in Account A. In Account B, create an IAM role with an S3 policy and a trust policy that trusts Account A. The EC2 instance assumes the role using `sts:AssumeRole` to receive short-lived temporary credentials."*
- **The Confused Deputy Trap:** When granting role assumption to a third-party SaaS vendor, explain why an `sts:ExternalId` condition is mandatory to prevent cross-customer spoofing.
- **AWS Organizations SCPs:** SCPs are guardrails that set the *maximum available permissions*. An explicit `Deny` in an SCP blocks everyone in the member account—including root!

### 2. Network Security & VPC Endpoints (Whiteboard Prompt)
- *Whiteboard Diagram:* Compare Layer 4 vs. Layer 7 inspection.
  - **Security Groups:** Stateful Layer 4 firewall at the instance level. Only supports `ALLOW` rules (implicit deny). Return traffic is automatically allowed.
  - **Network ACLs:** Stateless Layer 4 packet filter at the subnet boundary. Evaluates numbered rules in ascending order with explicit `ALLOW` and `DENY` rules. Ephemeral ports (1024-65535) must be opened for return traffic!
- **Gateway vs. Interface Endpoints (Crucial SAA Exam Distinction):**
  - **Gateway Endpoints:** Only for **Amazon S3** and **Amazon DynamoDB**. Free! Directs traffic via subnet route tables.
  - **Interface Endpoints (PrivateLink):** For almost all other AWS services (and also S3). Provisions an Elastic Network Interface (ENI) with a private IP in your subnet. Incurs an hourly fee plus per-GB data processing fees.

### 3. Data Protection: Secrets Manager vs. Parameter Store
- **AWS Secrets Manager:** Automatic database credential rotation via Lambda, cross-account sharing, secret replication across regions.
- **AWS SSM Parameter Store:** Hierarchical key-value store. Free for standard parameters. Supports `SecureString` encrypted with KMS, but does *not* natively manage database password rotation out of the box.

### 4. Detection Services Comparison Matrix
| Service | Data Sources Analyzed | Primary Function |
|---|---|---|
| **Amazon GuardDuty** | CloudTrail, VPC Flow Logs, DNS Logs, EKS | Intelligent threat detection (crypto-mining, credential theft) |
| **Amazon Macie** | Amazon S3 Buckets | Automated discovery & classification of sensitive PII |
| **Amazon Inspector** | EC2 Instances, ECR Images, Lambda | Vulnerability assessment (CVE scanning & unintended network exposure) |
| **AWS Config** | AWS Resource Configurations | Configuration history, compliance rules & automated remediation |

---

## 🚨 SAA-C03 Exam Traps & Anti-Patterns

1. **The Public Bastion Host Anti-Pattern:** Opening port 22 to `0.0.0.0/0` on a bastion host is an immediate wrong answer on the exam. The modern AWS recommended solution is **AWS Systems Manager Session Manager** (no open inbound ports, no public IPs).
2. **Denying a Specific IP in Security Groups:** Security groups do not support `DENY` rules! To block a single malicious IP (`198.51.100.25/32`), you must add a `DENY` rule to the inbound **Network ACL** with a low rule number.
3. **S3 Object Lock Modes:** If the question states that *even the root user must not be able to delete objects*, the answer is **Compliance Mode**, NOT Governance Mode.

---

## 🔬 Hands-on Lab & Homework Alignment
- **Hands-on Lab:** Guide students through [Lab 01: Multi-Tier Resilient VPC Architecture](../labs/lab_01_multi_tier_resilient_vpc_architecture.md) and [Lab 05: Hybrid & Private Connectivity](../labs/lab_05_hybrid_private_connectivity_transit_gateway_endpoints.md).
- **Knowledge Check:** Assign [Module 01 Knowledge Check](../knowledge_checks/Module_01_Secure_Architectures_Knowledge_Check.md).
- **Revision Questions:** Direct students to practice [Domain 1 Revision Questions](../revision_questions/Domain_1_Design_Secure_Architectures_Revision_Questions.md).
