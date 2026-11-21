# SAA-C03 Student Revision Questions Suite

Welcome to the comprehensive, domain-mapped revision question package for the **AWS Certified Solutions Architect - Associate (SAA-C03)** examination.

---

## Structure of the Suite

| Resource | Scope | Count | Target Weight |
|---|---|---|---|
| **[SAA_C03_Community_Practice_Pool_1019Q.md](./SAA_C03_Community_Practice_Pool_1019Q.md)** | **Comprehensive Community Practice Pool with consensus & answer breakdown** | **1,019 Questions** | **All 4 Domains** |
| [Domain 1 Revision Questions](./Domain_1_Design_Secure_Architectures_Revision_Questions.md) | IAM, KMS, Secrets Manager, VPC Security, WAF, Shield | 36 Questions | 30% |
| [Domain 2 Revision Questions](./Domain_2_Design_Resilient_Architectures_Revision_Questions.md) | ASG, ALB/NLB, SQS/SNS/EventBridge, Aurora, Disaster Recovery | 32 Questions | 26% |
| [Domain 3 Revision Questions](./Domain_3_Design_High_Performing_Architectures_Revision_Questions.md) | EFS, FSx, EBS gp3/io2, Graviton, Lambda, CloudFront, Direct Connect | 28 Questions | 24% |
| [Domain 4 Revision Questions](./Domain_4_Design_Cost_Optimized_Architectures_Revision_Questions.md) | S3 Intelligent-Tiering, Spot, Savings Plans, Gateway Endpoints | 24 Questions | 20% |
| [Full-Length Mock Revision Exam](./SAA_C03_Full_Length_Mock_Revision_Exam.md) | Full 65-Question Simulation (130 mins, 720 pass threshold) | 65 Questions | 100% |

---

## Interactive CLI Revision Runner

You can practice these questions interactively in your terminal with timed examination clocks:

```bash
# Practice by Domain
python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 1

# Practice from the 1,019-question Community Practice Pool
python3 scripts/aws_revision_runner.py --cert SAA --community --mode practice -n 20 --tricks

# Rapid Knowledge Drill (20 random questions)
python3 scripts/aws_revision_runner.py --cert SAA --mode drill

# Full Timed 65-Question Mock Exam (130 minutes)
python3 scripts/aws_revision_runner.py --cert SAA --mode mock

# Focused Review of Historical Weaknesses
python3 scripts/aws_revision_runner.py --cert SAA --mode weakness
```
