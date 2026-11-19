# AWS Certified Cloud Practitioner (CLF-C02) - Domain 2: Security and Compliance Revision Questions

> **Weight:** 30% of Scored Content  
> **Questions Count:** 25 Curated Exam-Style Practice Questions  
> **Target Certification:** AWS Certified Cloud Practitioner (`CLF-C02`)  

---

## 📝 Practice Questions

### Question 1 (Category: aws-security-compliance)
Under the AWS Shared Responsibility Model, which of the following is the CUSTOMER'S responsibility?

- [ ] {'label': 'A', 'text': 'Physical security of AWS data centers', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Patching the hypervisor on EC2 host servers', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Configuring security groups and network access control lists', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Maintaining the global network infrastructure between AWS Regions', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Under the Shared Responsibility Model, the customer is responsible for "security IN the cloud," which includes configuring security groups and NACLs to control network access to their resources. AWS is responsible for "security OF the cloud," which includes physical data center security (A), hypervisor patching (B), and maintaining the global network infrastructure (D).
</details>

### Question 2 (Category: aws-security-compliance)
A company is running a web application on Amazon EC2. Under the Shared Responsibility Model, who is responsible for patching the guest operating system on the EC2 instances?

- [ ] {'label': 'A', 'text': 'AWS, because they manage the underlying infrastructure', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'The customer, because they control the guest operating system', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'It is a shared responsibility between AWS and the customer', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'The EC2 service automatically handles all OS patching', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** When using Amazon EC2, the customer is responsible for managing the guest operating system, including installing patches and updates. AWS manages the underlying host infrastructure and hypervisor, but the guest OS is the customer's responsibility. This is not a shared responsibility (C) — it falls squarely on the customer. EC2 does not automatically patch guest operating systems (D), though AWS Systems Manager Patch Manager can help automate this process.
</details>

### Question 3 (Category: aws-security-compliance)
How does the Shared Responsibility Model change when a company uses AWS Lambda instead of Amazon EC2?

- [ ] {'label': 'A', 'text': 'There is no change — the customer has the same responsibilities regardless of service', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS takes on more responsibility because Lambda is a managed service, so the customer no longer manages the OS or runtime', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'The customer takes on more responsibility with Lambda because serverless requires more security configuration', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS is responsible for all security aspects when using Lambda, including application code security', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** With managed and serverless services like AWS Lambda, the shared responsibility model shifts more responsibility to AWS. The customer no longer manages the operating system, runtime, or server patching — AWS handles all of that. The customer remains responsible for their function code, data, and IAM permissions. The responsibilities do change by service type (A is wrong). The customer has fewer infrastructure responsibilities with Lambda (C is wrong). AWS is not responsible for the customer's application code security (D is wrong).
</details>

### Question 4 (Category: aws-security-compliance)
Which of the following is AWS's responsibility under the Shared Responsibility Model?

- [ ] {'label': 'A', 'text': 'Encrypting customer data stored in Amazon S3', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Managing IAM user permissions and access policies', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Decommissioning and destroying storage hardware that reaches end of life', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Configuring VPC routing tables and subnet configurations', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS is responsible for the physical infrastructure, which includes the secure decommissioning and destruction of storage hardware when it reaches end of life. AWS follows industry-standard practices (e.g., DoD 5220.22-M, NIST 800-88) to ensure data cannot be recovered from decommissioned hardware. Encrypting S3 data (A), managing IAM policies (B), and configuring VPC networking (D) are all customer responsibilities.
</details>

### Question 5 (Category: aws-security-compliance)
A company uses Amazon RDS for its database. Under the Shared Responsibility Model, which task is AWS responsible for?

- [ ] {'label': 'A', 'text': 'Creating and managing database user accounts and permissions', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Patching the underlying database engine software', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Encrypting sensitive columns within database tables', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Designing the database schema and optimizing queries', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon RDS is a managed database service, so AWS is responsible for patching the underlying database engine software during customer-specified maintenance windows. However, the customer is responsible for managing database user accounts (A), encrypting specific data columns (C), and designing schemas and queries (D). This illustrates how managed services shift more infrastructure responsibility to AWS while data and application-level responsibilities remain with the customer.
</details>

### Question 6 (Category: aws-security-compliance)
A company has 50 developers who need access to AWS resources. Instead of creating individual policies for each developer, what is the BEST practice for managing their permissions?

- [ ] {'label': 'A', 'text': 'Share a single IAM user account among all developers', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Create an IAM group for developers and attach the appropriate policy to the group', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Give each developer root account credentials', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Create 50 individual IAM policies, one for each developer', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** IAM groups are the recommended way to manage permissions for multiple users with similar access needs. By creating a "Developers" group and attaching the appropriate policy to the group, all members automatically inherit those permissions. Sharing credentials (A) violates security best practices and makes auditing impossible. Using root credentials (C) is extremely dangerous and violates the principle of least privilege. Individual policies (D) create unnecessary management overhead.
</details>

### Question 7 (Category: aws-security-compliance)
An application running on an EC2 instance needs to read objects from an S3 bucket. What is the MOST secure way to grant this access?

- [ ] {'label': 'A', 'text': 'Store AWS access keys in the application code on the EC2 instance', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Store AWS access keys in an environment variable on the EC2 instance', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Attach an IAM role with the appropriate S3 permissions to the EC2 instance', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Make the S3 bucket public so any application can read from it', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** IAM roles are the most secure way to grant AWS service permissions to EC2 instances. When you attach a role to an EC2 instance, temporary security credentials are automatically provided and rotated. Storing access keys in code (A) or environment variables (B) is insecure because keys can be accidentally exposed and do not rotate automatically. Making the S3 bucket public (D) exposes data to the entire internet.
</details>

### Question 8 (Category: aws-security-compliance)
Which IAM security best practice should be applied to the AWS root user account?

- [ ] {'label': 'A', 'text': 'Use the root user for daily administrative tasks', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Share root user credentials with the IT team for emergency access', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Enable multi-factor authentication (MFA) and avoid using the root user for everyday tasks', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Delete the root user account after creating IAM admin users', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS strongly recommends enabling MFA on the root user and avoiding its use for everyday tasks. The root user has unrestricted access to all resources and cannot be limited by IAM policies. Instead, create IAM users with appropriate permissions for daily work. Using root for daily tasks (A) exposes the account to unnecessary risk. Sharing credentials (B) violates security best practices. The root user cannot be deleted (D) — it is the original account identity.
</details>

### Question 9 (Category: aws-security-compliance)
A new IAM user has been created but has not been assigned any policies. What access does this user have to AWS services?

- [ ] {'label': 'A', 'text': 'Full read-only access to all AWS services', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Full access to the services in the same AWS Region', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'No access to any AWS services — all permissions are denied by default', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Access to only IAM and billing services', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** IAM follows the principle of least privilege by default. A newly created IAM user has no permissions whatsoever — all access is implicitly denied until explicit permissions are granted through IAM policies. This ensures that users only receive the minimum access they need. There is no default read-only access (A), regional access (B), or baseline service access (D).
</details>

### Question 10 (Category: aws-security-compliance)
A company wants to allow a third-party auditing firm to read its AWS CloudTrail logs without creating IAM users in the company's account. What is the recommended approach?

- [ ] {'label': 'A', 'text': 'Share the root account credentials with the auditing firm', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Create an IAM role with cross-account access that the auditing firm can assume', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Make the CloudTrail S3 bucket publicly accessible', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Email the CloudTrail log files directly to the auditors', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** IAM cross-account roles are the recommended way to grant third parties access to your AWS resources. You create a role in your account with the necessary permissions, and the third-party account assumes that role to gain temporary access. Sharing root credentials (A) gives unrestricted access and is extremely dangerous. Making logs public (C) exposes sensitive audit data to anyone. Emailing logs (D) is not scalable, secure, or practical for ongoing access.
</details>

### Question 11 (Category: aws-security-compliance)
An IAM policy contains the following statement: {"Effect": "Deny", "Action": "s3:DeleteObject", "Resource": "*"}. Another policy attached to the same user contains: {"Effect": "Allow", "Action": "s3:*", "Resource": "*"}. What is the result when the user tries to delete an S3 object?

- [ ] {'label': 'A', 'text': 'The action is allowed because the Allow policy grants full S3 access', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'The action is denied because an explicit Deny always overrides an Allow', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'The action outcome depends on which policy was attached first', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'The action is allowed because the wildcard (*) in the Allow policy takes precedence', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** In IAM policy evaluation, an explicit Deny always takes precedence over any Allow, regardless of how many policies grant access. This is a fundamental IAM rule. The Deny on s3:DeleteObject will block that specific action even though another policy allows all S3 actions. Policy attachment order (C) does not matter. Wildcards (D) do not override explicit Deny statements. This is a critical security mechanism that prevents accidental over-permissioning.
</details>

### Question 12 (Category: aws-security-compliance)
A company is experiencing a Distributed Denial of Service (DDoS) attack on its web application hosted on AWS. Which AWS service provides automatic DDoS protection at no additional cost?

- [ ] {'label': 'A', 'text': 'AWS WAF', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon GuardDuty', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS Shield Standard', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'AWS Shield Advanced', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS Shield Standard is automatically enabled for all AWS customers at no additional cost. It provides protection against the most common and frequently occurring DDoS attacks (Layer 3 and Layer 4). AWS WAF (A) is a web application firewall that filters HTTP/HTTPS traffic but is not free and is not specifically a DDoS service. Amazon GuardDuty (B) is a threat detection service for monitoring malicious activity, not DDoS mitigation. AWS Shield Advanced (D) provides enhanced DDoS protection but requires an additional paid subscription.
</details>

### Question 13 (Category: aws-security-compliance)
A security team wants to automatically detect unusual API activity, cryptocurrency mining, and potentially compromised EC2 instances in their AWS account. Which service should they enable?

- [ ] {'label': 'A', 'text': 'Amazon Inspector', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon GuardDuty', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Config', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS CloudTrail', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon GuardDuty is an intelligent threat detection service that continuously monitors for malicious activity and unauthorized behavior. It analyzes CloudTrail event logs, VPC Flow Logs, and DNS logs to detect threats like unusual API calls, cryptocurrency mining, and compromised instances. Amazon Inspector (A) assesses EC2 instances for vulnerabilities and deviations from best practices, not threat detection. AWS Config (C) tracks resource configuration changes. AWS CloudTrail (D) logs API activity but does not analyze it for threats.
</details>

### Question 14 (Category: aws-security-compliance)
A company needs to protect its web application from common exploits such as SQL injection and cross-site scripting (XSS) attacks. Which AWS service should they use?

- [ ] {'label': 'A', 'text': 'AWS Shield Standard', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon GuardDuty', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS WAF (Web Application Firewall)', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Amazon Macie', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS WAF is designed to protect web applications from common web exploits like SQL injection, cross-site scripting (XSS), and other OWASP Top 10 vulnerabilities. It lets you create rules to filter HTTP/HTTPS traffic based on conditions you define. AWS Shield Standard (A) protects against DDoS attacks, not application-layer exploits. GuardDuty (B) detects threats but does not filter web traffic. Amazon Macie (D) discovers and protects sensitive data in S3, not web application traffic.
</details>

### Question 15 (Category: aws-security-compliance)
A company stores sensitive customer data, including personally identifiable information (PII) and financial records, in Amazon S3. Which AWS service can automatically discover and classify this sensitive data?

- [ ] {'label': 'A', 'text': 'Amazon GuardDuty', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon Macie', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Shield', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon Inspector', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon Macie is a data security service that uses machine learning and pattern matching to discover and protect sensitive data stored in Amazon S3. It can automatically identify PII, financial data, and other sensitive information and alert you to potential data exposure. GuardDuty (A) detects threats but does not classify data. AWS Shield (C) protects against DDoS attacks. Amazon Inspector (D) assesses infrastructure for vulnerabilities, not data classification.
</details>

### Question 16 (Category: aws-security-compliance)
A security engineer needs to run automated vulnerability assessments on EC2 instances to identify unpatched software and unintended network exposure. Which AWS service should they use?

- [ ] {'label': 'A', 'text': 'AWS Trusted Advisor', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon Inspector', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Security Hub', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon Detective', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon Inspector is an automated vulnerability management service that continually scans EC2 instances (and container images and Lambda functions) for software vulnerabilities and unintended network exposure. It provides detailed findings with remediation guidance. AWS Trusted Advisor (A) provides broad best-practice recommendations but is not a vulnerability scanner. AWS Security Hub (C) aggregates security findings from multiple services but does not perform scans itself. Amazon Detective (D) investigates and analyzes security findings, not scan for vulnerabilities.
</details>

### Question 17 (Category: aws-security-compliance)
A company wants a centralized dashboard that aggregates security findings from Amazon GuardDuty, Amazon Inspector, Amazon Macie, and third-party tools. Which AWS service provides this capability?

- [ ] {'label': 'A', 'text': 'AWS CloudTrail', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Security Hub', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon CloudWatch', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Config', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Security Hub provides a comprehensive view of your security posture across AWS accounts. (AWS now calls these findings-aggregation and best-practice-check features AWS Security Hub CSPM; the newer AWS Security Hub correlates GuardDuty, Inspector, Macie, and Security Hub CSPM signals. The online CLF-C02 in-scope list still says AWS Security Hub.) It aggregates, organizes, and prioritizes security findings from multiple AWS services (GuardDuty, Inspector, Macie, Firewall Manager) and third-party tools in a single dashboard. CloudTrail (A) logs API calls. CloudWatch (C) monitors metrics and logs for operational purposes. AWS Config (D) tracks resource configurations but does not aggregate security findings from multiple services.
</details>

### Question 18 (Category: aws-security-compliance)
After Amazon GuardDuty generates a finding about suspicious activity, a security analyst needs to investigate the root cause by analyzing related events, network flows, and user activity over time. Which AWS service is designed for this investigation workflow?

- [ ] {'label': 'A', 'text': 'Amazon Macie', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS CloudTrail', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Amazon Detective', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'AWS Config', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon Detective makes it easy to analyze, investigate, and identify the root cause of security findings. It automatically collects and processes data from AWS CloudTrail, VPC Flow Logs, and GuardDuty findings to build a unified interactive view for investigation. While CloudTrail (B) provides raw API logs, it does not provide the analysis and visualization capabilities that Detective offers. Macie (A) focuses on data discovery in S3. AWS Config (D) tracks configuration changes.
</details>

### Question 19 (Category: aws-security-compliance)
A healthcare company needs to verify that AWS services it uses are compliant with HIPAA before storing protected health information (PHI). Where can the company find documentation of AWS compliance certifications and reports?

- [ ] {'label': 'A', 'text': 'AWS Trusted Advisor', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Artifact', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Config', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS CloudTrail', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports, certifications, and agreements. This includes SOC reports, PCI DSS attestations, HIPAA-related documentation, and other compliance artifacts. Trusted Advisor (A) provides best practice recommendations but not compliance reports. AWS Config (C) evaluates resource configurations. CloudTrail (D) logs API activity.
</details>

### Question 20 (Category: aws-security-compliance)
A large enterprise with multiple AWS accounts wants to enforce security policies centrally, such as preventing any account from disabling CloudTrail logging. Which AWS feature should they use?

- [ ] {'label': 'A', 'text': "IAM policies attached to each account's admin user", 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Service Control Policies (SCPs) in AWS Organizations', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon GuardDuty across all accounts', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Config rules in each account', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Service Control Policies (SCPs) in AWS Organizations allow you to centrally enforce permission guardrails across all accounts in the organization. SCPs can restrict actions even for account administrators, such as preventing the disabling of CloudTrail. Individual IAM policies (A) can be overridden by account admins. GuardDuty (C) detects threats but cannot prevent actions. AWS Config rules (D) can detect non-compliance but cannot prevent actions in real time.
</details>

### Question 21 (Category: aws-security-compliance)
A company needs to record all API calls made in its AWS account for security auditing and regulatory compliance. Which AWS service should they enable?

- [ ] {'label': 'A', 'text': 'Amazon CloudWatch Logs', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS CloudTrail', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Config', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'VPC Flow Logs', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS CloudTrail records all API calls made in your AWS account, including who made the call, when, from where, and what action was performed. This is essential for security auditing, compliance, and operational troubleshooting. CloudWatch Logs (A) collects application and system logs but does not specifically record API calls. AWS Config (C) tracks resource configuration changes, not API calls. VPC Flow Logs (D) capture network traffic flow information, not API activity.
</details>

### Question 22 (Category: aws-security-compliance)
A company wants to automatically evaluate whether its AWS resources comply with internal security standards, such as ensuring all S3 buckets have encryption enabled and all security groups do not allow unrestricted SSH access. Which AWS service provides this capability?

- [ ] {'label': 'A', 'text': 'AWS CloudTrail', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon Inspector', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS Config with managed rules', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'AWS Trusted Advisor', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS Config continuously monitors and records AWS resource configurations and allows you to evaluate them against desired configurations using Config rules. AWS provides managed rules for common compliance checks like S3 encryption and security group restrictions. CloudTrail (A) logs API activity but does not evaluate configurations. Inspector (B) scans for software vulnerabilities, not resource configuration compliance. Trusted Advisor (D) provides some security checks but is not as comprehensive or customizable as AWS Config for ongoing compliance evaluation.
</details>

### Question 23 (Category: aws-security-compliance)
A company needs to encrypt data stored in Amazon S3 and wants AWS to manage the encryption keys with minimal operational overhead. Which encryption option should they choose?

- [ ] {'label': 'A', 'text': 'Client-side encryption with customer-managed keys', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Server-side encryption with AWS KMS keys (SSE-KMS)', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Server-side encryption with Amazon S3 managed keys (SSE-S3)', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Server-side encryption with customer-provided keys (SSE-C)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** SSE-S3 (Server-Side Encryption with Amazon S3 managed keys) provides the lowest operational overhead because Amazon S3 manages the encryption keys entirely — creating, rotating, and storing keys on your behalf. SSE-KMS (B) gives more control over keys but requires managing KMS key policies. Client-side encryption (A) requires the customer to manage the entire encryption process. SSE-C (D) requires the customer to provide and manage keys with every request, adding significant operational overhead.
</details>

### Question 24 (Category: aws-security-compliance)
A financial services company has a regulatory requirement to use hardware security modules (HSMs) that are dedicated single-tenant devices for cryptographic key storage. Which AWS service meets this requirement?

- [ ] {'label': 'A', 'text': 'AWS Key Management Service (KMS)', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS CloudHSM', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Secrets Manager', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Certificate Manager', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS CloudHSM provides dedicated, single-tenant hardware security modules (HSMs) in the AWS Cloud. Unlike KMS which uses shared multi-tenant HSMs, CloudHSM gives the customer full control over their own HSM instances, meeting strict regulatory requirements for dedicated cryptographic hardware. AWS KMS (A) uses shared infrastructure and does not provide dedicated single-tenant HSMs. Secrets Manager (C) stores secrets like database credentials, not cryptographic keys on dedicated hardware. Certificate Manager (D) manages SSL/TLS certificates.
</details>

### Question 25 (Category: aws-security-compliance)
Which of the following represents encryption in transit?

- [ ] {'label': 'A', 'text': 'Enabling SSE-S3 on an Amazon S3 bucket', 'is_correct': False}
- [ ] {'label': 'B', 'text': "Using HTTPS/TLS to secure communication between a user's browser and an application on AWS", 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Enabling Amazon EBS volume encryption', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Encrypting an Amazon RDS database snapshot', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Encryption in transit protects data as it moves between two points over a network. HTTPS/TLS encrypts data flowing between a user's browser and the application server. SSE-S3 (A), EBS volume encryption (C), and RDS snapshot encryption (D) are all examples of encryption at rest — they protect data while it is stored on disk, not while it is moving across a network.
</details>

---

## 🔑 Quick Answer Key Summary

- 1. **C**
- 2. **B**
- 3. **B**
- 4. **C**
- 5. **B**
- 6. **B**
- 7. **C**
- 8. **C**
- 9. **C**
- 10. **B**
- 11. **B**
- 12. **C**
- 13. **B**
- 14. **C**
- 15. **B**
- 16. **B**
- 17. **B**
- 18. **C**
- 19. **B**
- 20. **B**
- 21. **B**
- 22. **C**
- 23. **C**
- 24. **B**
- 25. **B**
