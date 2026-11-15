# Domain 2: Security & Compliance Revision Questions (30% Exam Weight)

### Question 1
According to the AWS Shared Responsibility Model, which security task remains the sole responsibility of the customer when deploying an Amazon EC2 Linux instance?
- [ ] A) Physical security of the hypervisor host
- [ ] B) Patching the guest operating system and firewall configuration
- [ ] C) Decommissioning defective hard drives
- [ ] D) Maintaining the virtualization hypervisor software
> **Correct Answer:** B  
> **Rationale:** In IaaS (EC2), AWS is responsible for security OF the cloud (physical data centers, host hardware, hypervisor). The customer is strictly responsible for security IN the cloud, including guest OS patching, local firewalls, and application code.

---

### Question 2
An enterprise security team requires on-demand access to AWS compliance reports (e.g., SOC 1, SOC 2, PCI DSS) and agreements to satisfy a government audit. Which AWS service provides self-service access to these documents at no cost?
- [ ] A) AWS Trusted Advisor
- [ ] B) AWS Artifact
- [ ] C) Amazon Inspector
- [ ] D) AWS Security Hub
> **Correct Answer:** B  
> **Rationale:** AWS Artifact is the central portal for on-demand access to AWS compliance documentation, security certifications, and AWS Business Associate Addendums (BAA).

---

### Question 3
An application running on EC2 needs to read customer records stored in an Amazon S3 bucket. Which IAM mechanism represents the most secure, AWS-recommended approach?
- [ ] A) Store root user access keys inside the application code
- [ ] B) Create an IAM User with an access key and commit it to GitHub
- [ ] C) Attach an IAM Role with temporary credentials directly to the EC2 instance profile
- [ ] D) Configure public read permissions on the S3 bucket policy
> **Correct Answer:** C  
> **Rationale:** IAM Roles provide short-lived temporary security credentials through AWS Security Token Service (STS) and eliminate the need to hardcode or rotate permanent credentials.

---

### Question 4
Which intelligent threat detection service continuously analyzes AWS CloudTrail management events, VPC Flow Logs, and DNS query logs to detect compromised EC2 instances or unauthorized Bitcoin mining activity?
- [ ] A) Amazon GuardDuty
- [ ] B) Amazon Macie
- [ ] C) AWS Shield Advanced
- [ ] D) AWS WAF
> **Correct Answer:** A  
> **Rationale:** Amazon GuardDuty is a continuous security monitoring service that uses machine learning and threat intelligence feeds to identify unauthorized or malicious activity.

---

### Question 5
Which AWS service allows customers to discover, classify, and protect sensitive Personally Identifiable Information (PII) such as credit card numbers or passport data stored in Amazon S3 buckets?
- [ ] A) Amazon Inspector
- [ ] B) Amazon Macie
- [ ] C) AWS Secrets Manager
- [ ] D) AWS KMS
> **Correct Answer:** B  
> **Rationale:** Amazon Macie is a fully managed data security service that uses machine learning and pattern matching to discover and protect sensitive PII in S3.
