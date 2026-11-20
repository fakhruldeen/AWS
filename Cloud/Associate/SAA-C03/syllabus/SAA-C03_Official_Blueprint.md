# AWS Certified Solutions Architect - Associate (SAA-C03) Official Blueprint

> **Exam Code:** SAA-C03  
> **Credential:** AWS Certified Solutions Architect - Associate  
> **Passing Score:** 720 / 1000  
> **Format:** 65 questions (multiple choice or multiple response), 130 minutes.

---

## Domain Breakdown

### Domain 1: Design Secure Architectures (30%)
- **Task Statement 1.1:** Design secure access to AWS resources (IAM policies, roles, cross-account access, AWS Organizations SCPs, IAM Identity Center / SSO).
- **Task Statement 1.2:** Design secure workloads and applications (VPC subnets, security groups, Network ACLs, AWS WAF, AWS Shield, VPC Endpoints / PrivateLink).
- **Task Statement 1.3:** Determine appropriate data security controls (KMS envelope encryption, Secrets Manager vs Systems Manager Parameter Store, S3 bucket policies, CloudHSM).

### Domain 2: Design Resilient Architectures (26%)
- **Task Statement 2.1:** Design scalable and loosely coupled architectures (API Gateway, SQS FIFO/Standard, SNS topic fan-out, EventBridge event routing, Step Functions state machines).
- **Task Statement 2.2:** Design highly available and/or fault-tolerant architectures (Multi-AZ EC2 Auto Scaling, Application Load Balancers, Route 53 health checks & routing policies, Amazon Aurora Multi-Region / Global Database, S3 Cross-Region Replication).

### Domain 3: Design High-Performing Architectures (24%)
- **Task Statement 3.1:** Determine high-performing and/or scalable storage solutions (S3 Transfer Acceleration, Amazon EBS `io2` Block Express, Amazon EFS Elastic throughput, Amazon FSx for Lustre).
- **Task Statement 3.2:** Design high-performing and elastic compute solutions (EC2 instance families, AWS Graviton processors, AWS Lambda memory scaling, Amazon ECS / EKS with Fargate).
- **Task Statement 3.3:** Determine high-performing database solutions (Amazon RDS read replicas, Amazon DynamoDB with DAX accelerator, Amazon ElastiCache Redis clusters).
- **Task Statement 3.4:** Determine high-performing network architectures (Amazon CloudFront edge caching, AWS Global Accelerator Anycast routing, AWS Direct Connect with Transit Gateway).

### Domain 4: Design Cost-Optimized Architectures (20%)
- **Task Statement 4.1:** Design cost-optimized storage solutions (S3 Intelligent-Tiering, Lifecycle transitions to Glacier Deep Archive, EBS volume rightsizing).
- **Task Statement 4.2:** Design cost-optimized compute solutions (EC2 Spot Instances, Compute Savings Plans, Lambda serverless architectures).
- **Task Statement 4.3:** Design cost-optimized database solutions (Aurora Serverless v2, DynamoDB on-demand vs provisioned capacity, RDS Reserved Instances).
- **Task Statement 4.4:** Design cost-optimized network architectures (VPC Gateway Endpoints for S3/DynamoDB to eliminate NAT Gateway data processing fees).
