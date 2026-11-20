# SAA-C03 Diagnostic Knowledge Checks Suite

This directory contains rapid, 10-question diagnostic retention quizzes mapped to the core modules and domains of the **AWS Certified Solutions Architect - Associate (SAA-C03)** examination.

---

## Knowledge Check Modules

| Module | Focus & Core Services | Questions | Target Domain |
|---|---|---|---|
| [Module 01: Secure Architectures](./Module_01_Secure_Architectures_Knowledge_Check.md) | IAM, KMS, Secrets Manager, VPC Endpoints, WAF, Shield | 10 Questions | Domain 1 (30%) |
| [Module 02: Resilient Architectures](./Module_02_Resilient_Architectures_Knowledge_Check.md) | SQS/SNS, Step Functions, Aurora Multi-AZ, NLB, DR Tiers | 10 Questions | Domain 2 (26%) |
| [Module 03: High-Performing Architectures](./Module_03_High_Performing_Architectures_Knowledge_Check.md) | FSx Lustre/Windows, EBS gp3/io2, DAX, Graviton, Global Accelerator | 10 Questions | Domain 3 (24%) |
| [Module 04: Cost-Optimized Architectures](./Module_04_Cost_Optimized_Architectures_Knowledge_Check.md) | S3 Glacier/Intelligent-Tiering, Spot, Savings Plans, FinOps | 10 Questions | Domain 4 (20%) |

---

## Recommended Study Workflow
1. Complete the corresponding guided lab in `labs/`.
2. Review the high-yield decision matrices in `notes/`.
3. Take the corresponding module Knowledge Check here to test retention and reveal common architectural exam traps.
4. Run comprehensive practice drills using the CLI Revision Runner:
   ```bash
   python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 1
   ```
