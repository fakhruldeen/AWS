# 🛠️ AWS Certified Cloud Practitioner (CLF-C02) Hands-On Student Lab Manual

> **Course Workspace:** `/home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/phase2_step07_labs`  
> **Author & Lead Trainer:** Mohamed Fakhruldeen  
> **Region:** `eu-north-1` (Stockholm) — 100% Free-Tier / Zero-Cost Optimized  
> **Architecture:** Conceptual Refresher ➔ Detailed Step-by-Step Console Walkthrough ➔ AWS CLI v2 Verification ➔ Dedicated Exam Practice Matrices (Scenarios & Traps) ➔ Cost Teardown Safeguards  
> **Format:** 100% Self-Contained Written Guided Labs (No reliance on external screenshots)  
> **Master Safety Guide & Cleanup Runbook:** [LAB_SAFETY_AND_VERIFICATION_GUIDE.md](LAB_SAFETY_AND_VERIFICATION_GUIDE.md)


---

## 🗺️ Master Curriculum Lab Index

| Lab # | Lab Manual Guide | Key Services Covered | Target Skills Developed |
| :--- | :--- | :--- | :--- |
| **Lab 00** | [Lab 00: Account Creation & Day-1 Security](00_Account_Creation_Walkthrough.md) | AWS Signup, Root MFA, IAM Admin, Billing Alerts | Account bootstrap, Root credential lockdown, $0 spend alarm |
| **Lab 01** | [Lab 01: Multi-Tier VPC & Networking](lab_01_vpc_networking.md) | VPC, Subnets, Internet Gateway, NAT Gateway, Route Tables | CIDR math, public/private network segmentation, NAT routing |
| **Lab 02** | [Lab 02: VPC Security Controls](lab_02_vpc_security_controls.md) | Security Groups, Network ACLs, VPC Flow Logs | Stateful vs stateless firewalls, ephemeral ports, explicit IP deny |
| **Lab 03** | [Lab 03: Compute Tier: EC2 & Bootstrap](lab_03_ec2_compute_bootstrap.md) | EC2, AMI, User Data, Status Checks, Elastic IPs | Instance families, automated bash bootstrapping, static IPs |
| **Lab 04** | [Lab 04: High Availability (ALB & ASG)](lab_04_alb_autoscaling_ha.md) | ALB, Target Groups, Launch Templates, Auto Scaling | Horizontal scaling, self-healing recovery, multi-AZ load balancing |
| **Lab 05** | [Lab 05: Serverless Compute & APIs](lab_05_serverless_lambda_apigateway.md) | AWS Lambda, Amazon API Gateway, CloudWatch Logs | FaaS event-driven compute, sub-second billing, HTTP REST routing |
| **Lab 06** | [Lab 06: Containerized Microservices](lab_06_containers_ecr_ecs_fargate.md) | Amazon ECR, Amazon ECS, AWS Fargate | Docker container registries, serverless task definitions, ECS services |
| **Lab 07** | [Lab 07: Object Storage & Lifecycle](lab_07_s3_storage_lifecycle.md) | Amazon S3, Versioning, Lifecycle Rules, Bucket Policies | 11 9s durability, Delete markers, automated tiering, TLS enforcement |
| **Lab 08** | [Lab 08: Block & File Storage](lab_08_ebs_efs_storage.md) | Amazon EBS (`gp3`), Snapshots, Amazon EFS | Block vs file, single-AZ EBS vs multi-AZ concurrent NFS sharing |
| **Lab 09** | [Lab 09: Relational Databases (RDS)](lab_09_rds_database_ha.md) | Amazon RDS PostgreSQL, DB Subnet Groups, Multi-AZ | ACID compliance, synchronous multi-AZ failover, read replicas |
| **Lab 10** | [Lab 10: NoSQL & Caching (DynamoDB)](lab_10_dynamodb_nosql_dax.md) | Amazon DynamoDB, DAX, DynamoDB Streams | Key-value data modeling, partition keys, Query vs Scan, streams |
| **Lab 11** | [Lab 11: Edge Acceleration & DNS](lab_11_route53_cloudfront_edge.md) | Amazon Route 53, Amazon CloudFront, AWS WAF | Hosted zones, Alias records, OAC S3 protection, edge WAF rules |
| **Lab 12** | [Lab 12: Application Decoupling](lab_12_sqs_sns_eventbridge_messaging.md) | Amazon SQS, Amazon SNS, Amazon EventBridge | Loose coupling, SNS-to-SQS fan-out, reactive JSON event filtering |
| **Lab 13** | [Lab 13: Observability Triad](lab_13_observability_cloudwatch_cloudtrail_config.md) | CloudWatch, AWS CloudTrail, AWS Config | Metrics vs logs vs API auditing vs continuous compliance tracking |
| **Lab 14** | [Lab 14: Financial Governance (FinOps)](lab_14_billing_cost_management.md) | Cost Explorer, Budgets, Pricing Calculator, Optimizer | CapEx vs OpEx, cost allocation tags, forecasting, ML rightsizing |

---

## 🔒 Golden Rules for Hands-On Practice

1. **Always Verify Your Region:** Anchor your session to **Stockholm (`eu-north-1`)** for consistent Free-Tier quotas and lower network latency.
2. **Never Hardcode Secrets:** Always use IAM roles, parameter stores, or secrets manager rather than embedding plaintext keys in code or User Data scripts.
3. **Execute Teardown Immediately:** After completing each lab, follow the **Free Tier Cleanup & Cost Safeguard** section at the bottom of the manual to guarantee zero unwanted charges.
