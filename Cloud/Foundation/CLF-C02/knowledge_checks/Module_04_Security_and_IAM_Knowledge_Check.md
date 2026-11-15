# Module 04 Knowledge Check: Security & IAM

### Questions
1. **Under the AWS Shared Responsibility Model, which of the following is AWS responsible for?**
   - A) Managing user passwords and access keys
   - B) Physical security of data centers and server hardware
   - C) Encrypting client-side application data
   - D) Configuring OS firewall rules
2. **Which IAM entity is intended to be assumed by an EC2 instance or Lambda function to obtain temporary security credentials?**
   - A) IAM User
   - B) IAM Group
   - C) IAM Role
   - D) Root User
3. **What is the AWS service that provides managed DDoS protection, with automated Layer 3 and Layer 4 protection enabled by default at no extra charge?**
   - A) AWS WAF
   - B) AWS Shield Standard
   - C) Amazon GuardDuty
   - D) AWS Network Firewall
4. **Which service continuously audits AWS resource configurations against desired compliance rules and records configuration history over time?**
   - A) AWS CloudTrail
   - B) Amazon CloudWatch
   - C) AWS Config
   - D) AWS Systems Manager
5. **Which service records all API calls made across an AWS account, including the caller identity, timestamp, source IP, and request parameters?**
   - A) Amazon CloudWatch Logs
   - B) AWS CloudTrail
   - C) AWS Trusted Advisor
   - D) AWS IAM Access Analyzer
6. **What security mechanism protects the root user account by requiring a six-digit physical or virtual code in addition to email and password?**
   - A) Multi-Factor Authentication (MFA)
   - B) Access Key ID + Secret Key
   - C) AWS SSO Federation
   - D) SSH Key Pair
7. **Which service provides an automated vulnerability assessment that checks EC2 instances, ECR container images, and Lambda functions for software vulnerabilities and unintended network exposure?**
   - A) Amazon GuardDuty
   - B) Amazon Macie
   - C) Amazon Inspector
   - D) AWS Security Hub
8. **Which service manages cryptographic keys and allows you to encrypt data at rest across AWS services using Envelope Encryption?**
   - A) AWS Secrets Manager
   - B) AWS Key Management Service (AWS KMS)
   - C) AWS Certificate Manager (ACM)
   - D) AWS CloudHSM
9. **What web application firewall lets you monitor HTTP/HTTPS requests forwarded to an ALB, Amazon API Gateway, or CloudFront, and block malicious SQL injection or cross-site scripting attacks?**
   - A) AWS Shield Standard
   - B) AWS WAF
   - C) Amazon GuardDuty
   - D) AWS Firewall Manager
10. **What is the golden rule regarding the AWS account root user credentials?**
    - A) Share root credentials with all developers for faster deployments
    - B) Lock away the root user credentials, enable hardware/virtual MFA, and use IAM administrative users for daily tasks
    - C) Generate access keys for the root user and hardcode them into application configuration files
    - D) Delete the root user account immediately after creating the account

---

### Answer Key & Explanations
| Q# | Answer | Key Concept Reference |
| :---: | :---: | :--- |
| **1** | **B** | AWS owns physical datacenter security, hardware infrastructure, and hypervisor maintenance. |
| **2** | **C** | IAM Roles provide temporary STS credentials to AWS services and applications without hardcoded keys. |
| **3** | **B** | AWS Shield Standard protects all customers from common Layer 3/4 DDoS attacks automatically for free. |
| **4** | **C** | AWS Config evaluates configurations against compliance rules and records point-in-time configuration state. |
| **5** | **B** | AWS CloudTrail records API management events across the account for governance and forensic auditing. |
| **6** | **A** | Multi-Factor Authentication (MFA) is mandatory on the root account to prevent unauthorized takeovers. |
| **7** | **C** | Amazon Inspector scans EC2, ECR container images, and Lambda for known software CVE vulnerabilities. |
| **8** | **B** | AWS KMS creates and controls cryptographic keys used to encrypt data across all AWS services. |
| **9** | **B** | AWS WAF operates at Layer 7 to block web exploits like SQL injection and XSS via customizable rules. |
| **10** | **B** | Root credentials provide unrestricted access and must be protected with MFA and never used for daily work. |
