# AWS Certified Cloud Practitioner (CLF-C02) - Domain 2: Security and Compliance (30% of Exam)

This document contains 18 verified practice questions with complete answer keys and comprehensive explanations for every option, extracted from [CertSafari](https://www.certsafari.com/aws/cloud-practitioner-foundational).

## Table of Contents
- [Question 20](#question-20): An organization sets up AWS IAM Identity Center so employees can sign in wi...
- [Question 21](#question-21): Under the shared responsibility model, who is responsible for the physical ...
- [Question 22](#question-22): An Availability Zone experiences a hardware failure that disrupts part of A...
- [Question 23](#question-23): An attacker exploits an unpatched vulnerability in the guest operating syst...
- [Question 24](#question-24): A company processes credit card payments and must comply with PCI DSS. Duri...
- [Question 25](#question-25): A company operating in a heavily regulated industry needs to demonstrate to...
- [Question 26](#question-26): A security team wants every object written to an Amazon S3 bucket to be aut...
- [Question 27](#question-27): A healthcare startup is evaluating whether AWS can support a workload that ...
- [Question 28](#question-28): A company migrating sensitive workloads to AWS wants to reduce the risk tha...
- [Question 29](#question-29): A security team suspects an Amazon EC2 instance in their account may be com...
- [Question 30](#question-30): An operations team needs to store plain configuration values, such as an ap...
- [Question 31](#question-31): A finance team stores database passwords for an application directly inside...
- [Question 32](#question-32): A developer needs an application running on an Amazon EC2 instance to read ...
- [Question 33](#question-33): Which AWS service allows a customer to create rules that filter web request...
- [Question 34](#question-34): A cloud architect is evaluating AWS Firewall Manager to decide whether it f...
- [Question 35](#question-35): Where would a customer go to find a centralized, high-level overview of AWS...
- [Question 36](#question-36): After Amazon GuardDuty raises a finding that an EC2 instance may be comprom...
- [Question 37](#question-37): After enabling Amazon GuardDuty, a company notices a finding indicating tha...

---

### Question 20

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.1: Understand the AWS shared responsibility model.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> An organization sets up AWS IAM Identity Center so employees can sign in with a corporate identity provider across multiple AWS accounts. Who is responsible for configuring this federated access?

#### Options
- **A.** The customer configures federated access settings, since authentication design is part of security in the cloud. **[CORRECT]**
- **B.** AWS configures federated access settings automatically once a new AWS account is created within the organization.
- **C.** AWS Artifact configures federated access settings as part of its automated compliance reporting for the organization.
- **D.** AWS Shield configures federated access settings to protect the organization from account takeover attempts.

**Correct Answer:** `A`
> **Summary:** The customer configures federated access settings, since authentication design is part of security in the cloud.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Deciding how employees authenticate, including connecting a corporate identity provider through IAM Identity Center, is a configuration choice the customer makes under security in the cloud.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Creating a new AWS account does not automatically set up federated identity; the customer must explicitly configure the identity provider connection.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Artifact provides access to compliance documentation; it has no role in configuring identity federation or authentication settings.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Shield protects against distributed denial-of-service attacks and does not configure identity federation or authentication settings.

---

### Question 21

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.1: Understand the AWS shared responsibility model.`  
**Origin:** *Live Quiz Engine (ID: 80433)*

> **Scenario:**  
> Under the shared responsibility model, who is responsible for the physical security of the data centers hosting AWS services?

#### Options
- **A.** AWS is responsible for physical security, including controlling access to the data center facilities and hardware. **[CORRECT]**
- **B.** The customer is responsible for physical security, since AWS only manages the software layer of its services.
- **C.** The customer's compliance team audits and enforces physical access controls inside AWS data center buildings.
- **D.** AWS delegates physical facility security to the customer through a shared responsibility matrix agreement.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Physical facility security, including controlling who can access data center buildings and hardware, is part of security of the cloud and is entirely AWS's responsibility.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS manages hardware and physical infrastructure, not just software; customers never take on physical data center security under this model.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Customers do not have physical access to AWS data centers and cannot audit or enforce access controls inside AWS facilities.

- **Option D:** ❌ **Why it is INCORRECT:**  
  There is no mechanism by which AWS hands physical facility security to a customer; this responsibility remains with AWS across all services.

---

### Question 22

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.1: Understand the AWS shared responsibility model.`  
**Origin:** *Live Quiz Engine (ID: 80441)*

> **Scenario:**  
> An Availability Zone experiences a hardware failure that disrupts part of AWS's underlying infrastructure. The customer's application also goes offline because it was deployed in only that single Availability Zone. Which responsibilities does this scenario illustrate?

#### Options
- **A.** AWS is responsible for the underlying hardware failure, while the customer is responsible for its Availability Zone design. **[CORRECT]**
- **B.** AWS is responsible for both the hardware failure and the customer's decision to deploy in a single Availability Zone.
- **C.** The customer is responsible for the hardware failure, since AWS delegates all infrastructure uptime to the account owner.
- **D.** Neither AWS nor the customer holds responsibility, since Availability Zone failures fall outside the shared responsibility model.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS owns the hardware and infrastructure that failed, while architecting for resilience, such as spreading a workload across multiple Availability Zones, is a customer design decision.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Architecture decisions like which Availability Zones to deploy into are made by the customer, not AWS, so AWS cannot be responsible for that design choice.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS retains responsibility for the physical infrastructure and hardware within its data centers; this is never delegated to the customer.

- **Option D:** ❌ **Why it is INCORRECT:**  
  This scenario falls squarely within the model: AWS owns the infrastructure layer that failed, and the customer owns the resiliency design of its application.

---

### Question 23

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.1: Understand the AWS shared responsibility model.`  
**Origin:** *Live Quiz Engine (ID: 80440)*

> **Scenario:**  
> An attacker exploits an unpatched vulnerability in the guest operating system of a customer's EC2 instance. Under the shared responsibility model, whose gap in duties allowed this exposure?

#### Options
- **A.** The customer's gap, since guest operating system patching for EC2 instances is a customer responsibility. **[CORRECT]**
- **B.** AWS's gap, since AWS is responsible for patching every guest operating system running on EC2 instances.
- **C.** AWS Inspector's gap, since it is responsible for automatically patching vulnerable guest operating systems.
- **D.** AWS Shield's gap, since it is responsible for blocking exploitation attempts against unpatched guest systems.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Because EC2 leaves guest operating system patching with the customer, an unpatched vulnerability at that layer reflects a gap in the customer's own security-in-the-cloud duties.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS does not patch guest operating systems on EC2 instances, so this exposure cannot be attributed to an AWS patching failure.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon Inspector scans for vulnerabilities and reports findings, but it does not apply patches itself, so it cannot be responsible for the unpatched state.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Shield mitigates distributed denial-of-service attacks; it plays no role in patching or protecting against guest operating system vulnerabilities.

---

### Question 24

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.2: Understand AWS Cloud security, governance, and compliance concepts.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> A company processes credit card payments and must comply with PCI DSS. During due diligence, the security team learns that not every AWS service carries the same compliance certifications. What does this mean for their architecture decisions?

#### Options
- **A.** They must verify each AWS service used for the cardholder data workload appears on the relevant compliance scope before adopting it. **[CORRECT]**
- **B.** They can use any AWS service for the workload, since AWS Artifact automatically restricts non-compliant services from being launched.
- **C.** They only need to verify compliance for the AWS Region selected, since all services within a compliant Region inherit the same certifications.
- **D.** They can rely on AWS Trusted Advisor to automatically reconfigure any non-compliant service selection to a certified alternative.

**Correct Answer:** `A`
> **Summary:** They must verify each AWS service used for the cardholder data workload appears on the relevant compliance scope before adopting it.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Because compliance certifications apply per service rather than uniformly, the team must confirm each service handling cardholder data is within the relevant compliance scope, which is exactly the architectural discipline this fact requires.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS Artifact only provides access to documentation; it does not technically prevent an account from launching a service that lacks a particular certification.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Region selection affects data residency, but it does not mean every service available in that Region automatically shares the same compliance certifications as every other service there.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Trusted Advisor offers best-practice recommendations but does not automatically substitute or reconfigure service choices based on compliance certification status.

---

### Question 25

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.2: Understand AWS Cloud security, governance, and compliance concepts.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> A company operating in a heavily regulated industry needs to demonstrate to a government regulator that AWS's data centers meet specific physical and operational security standards. Which AWS resource provides evidence for this claim?

#### Options
- **A.** Third-party audit reports available through AWS Artifact, which attest to AWS's physical and operational security controls. **[CORRECT]**
- **B.** Amazon CloudWatch dashboards, which display operational metrics about the performance of the company's own deployed resources.
- **C.** AWS Config compliance rules, which evaluate the company's resource configurations against internally defined rules.
- **D.** IAM access reports, which summarize which users in the company's account have used which permissions recently.

**Correct Answer:** `A`
> **Summary:** Third-party audit reports available through AWS Artifact, which attest to AWS's physical and operational security controls.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Third-party audit reports obtained through AWS Artifact are the evidence that independently attest to AWS's physical and operational security controls, which is what a regulator would need to see.

- **Option B:** ❌ **Why it is INCORRECT:**  
  CloudWatch dashboards show performance metrics for the company's own resources, not independent attestations about AWS's physical data center security.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Config rules evaluate the company's own resource configurations, not the physical or operational security of AWS's underlying data centers.

- **Option D:** ❌ **Why it is INCORRECT:**  
  IAM access reports describe how the company's own users are using permissions, which is unrelated to demonstrating AWS's physical data center security standards.

---

### Question 26

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.2: Understand AWS Cloud security, governance, and compliance concepts.`  
**Origin:** *Live Quiz Engine (ID: 80534)*

> **Scenario:**  
> A security team wants every object written to an Amazon S3 bucket to be automatically encrypted on the storage media without the application needing to manage encryption keys itself. Which capability meets this requirement?

#### Options
- **A.** Server-side encryption at rest, which AWS applies to objects as they are written to storage without application-level key handling. **[CORRECT]**
- **B.** Client-side encryption, which requires the application to encrypt and manage the key for each object locally before uploading it to the bucket.
- **C.** AWS Shield, which inspects incoming requests to the bucket and blocks traffic associated with denial-of-service attacks.
- **D.** Amazon GuardDuty, which analyzes account and network activity logs to detect potentially malicious or unauthorized behavior.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Server-side encryption at rest is correct because AWS handles encrypting the object on the storage media, removing the need for the application to manage the encryption process itself.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Client-side encryption places the encryption burden on the application before upload, which is the opposite of what the requirement asks for.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Shield defends against distributed denial-of-service traffic; it does not encrypt object data stored in a bucket.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon GuardDuty is a threat detection service that analyzes logs for suspicious activity; it plays no role in encrypting stored objects.

---

### Question 27

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.2: Understand AWS Cloud security, governance, and compliance concepts.`  
**Origin:** *Live Quiz Engine (ID: 80531)*

> **Scenario:**  
> A healthcare startup is evaluating whether AWS can support a workload that must meet HIPAA requirements. What should the team do to confirm AWS's eligible services and obligations?

#### Options
- **A.** Review AWS compliance documentation for HIPAA eligibility and sign the AWS Business Associate Addendum before storing protected health data. **[CORRECT]**
- **B.** Assume any AWS service is automatically HIPAA eligible once the account owner enables encryption at rest and access logging for all storage volumes.
- **C.** Contact AWS Trusted Advisor support to request a manual compliance certificate confirming the workload meets HIPAA requirements.
- **D.** Enable AWS Shield Advanced on the account, since DDoS protection alone satisfies the technical safeguards required by HIPAA.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS publishes which services are HIPAA eligible and requires customers handling protected health information to sign a Business Associate Addendum, making this the correct way to confirm eligibility and obligations.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Not every AWS service is HIPAA eligible, and enabling encryption alone does not make an ineligible service compliant or replace the need to review the eligible-services list.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Trusted Advisor produces configuration recommendations for an account; it does not issue HIPAA compliance certificates on request.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Shield Advanced protects against distributed denial-of-service attacks, which addresses only one narrow risk and does not by itself satisfy the broader HIPAA technical safeguard requirements.

---

### Question 28

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.2: Understand AWS Cloud security, governance, and compliance concepts.`  
**Origin:** *Live Quiz Engine (ID: 80552)*

> **Scenario:**  
> A company migrating sensitive workloads to AWS wants to reduce the risk that a stolen database backup file could expose customer data, even if the backup storage itself were somehow accessed by an unauthorized party. Which cloud security benefit most directly addresses this concern?

#### Options
- **A.** Encryption at rest applied to the backup files, which renders the stored data unreadable without the associated decryption key. **[CORRECT]**
- **B.** Elastic scaling of backup storage capacity, which automatically increases available space as backup file sizes continue to grow.
- **C.** Automated backup scheduling, which ensures backups are created at consistent intervals without manual intervention.
- **D.** Consolidated billing across linked accounts, which centralizes payment for backup storage costs under one account.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Encryption at rest directly addresses this concern because it makes the backup file's contents unreadable without the decryption key, protecting confidentiality even if the storage were accessed.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Elastic scaling of storage capacity manages growth in size, not the confidentiality of the data itself, so it does not address unauthorized access to backup contents.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Automated backup scheduling improves reliability and consistency of backups, but it has no effect on whether the backup data is protected from unauthorized reading.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Consolidated billing simplifies payment management across accounts and has no relationship to protecting the confidentiality of backup file contents.

---

### Question 29

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.2: Understand AWS Cloud security, governance, and compliance concepts.`  
**Origin:** *Live Quiz Engine (ID: 80539)*

> **Scenario:**  
> A security team suspects an Amazon EC2 instance in their account may be compromised and is being used to communicate with a known command-and-control server. Which service continuously analyzes account and network activity to detect this kind of threat?

#### Options
- **A.** Amazon GuardDuty, which analyzes logs and network activity to identify potentially malicious or unauthorized behavior. **[CORRECT]**
- **B.** Amazon Inspector, which scans workloads such as EC2 instances and container images for known software vulnerabilities.
- **C.** AWS Security Hub, which aggregates findings from multiple security services into a single consolidated dashboard view.
- **D.** AWS Config, which records resource configuration changes and evaluates them against defined compliance rules.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon GuardDuty continuously analyzes sources like VPC flow logs and DNS logs to detect threats such as communication with known malicious endpoints, matching the scenario's need for active threat detection.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon Inspector focuses on scanning workloads for known software vulnerabilities and unintended network exposure, which is a proactive assessment rather than detecting active malicious behavior.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Security Hub consolidates findings that other services like GuardDuty and Inspector already generated; it does not itself perform the underlying threat analysis described.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Config tracks configuration state and compliance against rules, which does not extend to detecting active network-based threats like command-and-control communication.

---

### Question 30

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.3: Identify AWS access management capabilities.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> An operations team needs to store plain configuration values, such as an application's API endpoint URL and a feature-flag setting, that change occasionally but are not sensitive secrets. Which AWS capability is the most appropriate fit for this use case?

#### Options
- **A.** AWS Systems Manager Parameter Store, which lets applications retrieve named configuration values through a simple API call. **[CORRECT]**
- **B.** AWS Secrets Manager, which is purpose-built for storing highly sensitive credentials with mandatory automatic rotation schedules.
- **C.** AWS IAM Identity Center, which centralizes workforce sign-in but does not provide a mechanism for storing configuration data.
- **D.** AWS Key Management Service, which manages encryption keys rather than acting as a general configuration value store.

**Correct Answer:** `A`
> **Summary:** AWS Systems Manager Parameter Store, which lets applications retrieve named configuration values through a simple API call.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Parameter Store is designed to hold configuration data and non-secret or lightly-protected values that applications fetch by name, making it a lightweight fit for endpoint URLs and feature flags.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Secrets Manager targets sensitive credentials like database passwords and API keys with rotation built in; using it for plain, non-sensitive configuration values adds unnecessary cost and complexity.

- **Option C:** ❌ **Why it is INCORRECT:**  
  IAM Identity Center manages workforce identities and access to accounts and applications; it has no facility for storing arbitrary configuration values for an application to read.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS KMS creates and manages cryptographic keys used to encrypt data elsewhere; it does not itself provide a place to store and retrieve configuration strings.

---

### Question 31

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.3: Identify AWS access management capabilities.`  
**Origin:** *Live Quiz Engine (ID: 80611)*

> **Scenario:**  
> A finance team stores database passwords for an application directly inside environment variables in application code, and rotates them manually every few months by editing the deployment scripts. Which change would best align this practice with AWS credential storage guidance?

#### Options
- **A.** Move the passwords into AWS Secrets Manager and configure automatic rotation so the application retrieves current credentials at runtime. **[CORRECT]**
- **B.** Encrypt the deployment scripts with a customer-managed KMS key while continuing to store the passwords as plaintext environment variables.
- **C.** Move the passwords into an Amazon S3 bucket with default settings and reference the object path from the deployment scripts.
- **D.** Store the passwords inside AWS CloudTrail log records so the security team can review historical values during scheduled audits.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Secrets Manager is built specifically to store database credentials and secrets, retrieve them at runtime via API calls, and rotate them automatically, removing hardcoded passwords from code and scripts.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Encrypting the scripts protects the file at rest but the passwords are still embedded as plaintext once decrypted for use, and manual rotation through script edits remains unchanged and error-prone.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon S3 is general-purpose object storage without built-in secret rotation, fine-grained secret versioning, or credential-specific access controls, making it a poor fit for storing live application passwords.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS CloudTrail records API activity for auditing and is not a credential store; writing passwords into audit logs would expose them broadly and serves no rotation or retrieval purpose.

---

### Question 32

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.3: Identify AWS access management capabilities.`  
**Origin:** *Live Quiz Engine (ID: 80618)*

> **Scenario:**  
> A developer needs an application running on an Amazon EC2 instance to read objects from a specific Amazon S3 bucket. The security team wants to avoid storing any long-term access keys on the instance. Which IAM feature should be used?

#### Options
- **A.** An IAM role attached to the EC2 instance profile that supplies temporary credentials the application retrieves. **[CORRECT]**
- **B.** An IAM user with access keys embedded directly into the application's configuration file on the instance's local disk.
- **C.** The account root user's access keys, configured as environment variables in the application's runtime environment.
- **D.** A shared IAM group password that the application enters programmatically each time it needs to reach the S3 bucket.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  An IAM role attached via an instance profile lets EC2 automatically retrieve short-lived, automatically rotated temporary credentials for the application, avoiding any long-term keys stored on the instance.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Embedding an IAM user's long-term access keys in a configuration file on disk creates a durable secret that can be exposed if the instance or its image is compromised, which the security team wants to avoid.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Root user access keys grant unrestricted access to the entire account; placing them on an instance as environment variables is far riskier than the scoped, temporary credentials a role provides.

- **Option D:** ❌ **Why it is INCORRECT:**  
  IAM groups organize users and their permissions; they do not have passwords of their own and applications cannot authenticate to AWS using a group credential.

---

### Question 33

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.4: Identify components and resources for security.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> Which AWS service allows a customer to create rules that filter web requests based on conditions such as IP address ranges, HTTP headers, or request rate, and apply those rules to CloudFront distributions, Application Load Balancers, and API Gateway?

#### Options
- **A.** AWS WAF, a web application firewall that filters web requests using customizable rules matched against IP ranges, headers, body content. **[CORRECT]**
- **B.** AWS Shield, a managed service that automatically protects internet-facing resources against distributed denial-of-service network flood attacks.
- **C.** Amazon GuardDuty, an intelligent threat detection service that continuously monitors account activity for malicious or unauthorized behavior.
- **D.** AWS Firewall Manager, a management tool that centrally administers WAF, Shield Advanced, and security group policies across an organization.

**Correct Answer:** `A`
> **Summary:** AWS WAF, a web application firewall that filters web requests using customizable rules matched against IP ranges, headers, body content.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS WAF is purpose-built to define web request filtering rules based on IP ranges, headers, body patterns, and rate limits, and to attach those rules directly to CloudFront, ALB, and API Gateway.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Shield focuses on absorbing and mitigating denial-of-service flood traffic rather than evaluating individual request attributes like headers or rate.

- **Option C:** ❌ **Why it is INCORRECT:**  
  GuardDuty is a detection service that surfaces findings from log analysis; it does not create or attach request-filtering rules to resources.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Firewall Manager orchestrates the deployment of WAF and other policies across many accounts, but the rule engine described in the stem is WAF itself.

---

### Question 34

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.4: Identify components and resources for security.`  
**Origin:** *Practice Questions Page*

> **Scenario:**  
> A cloud architect is evaluating AWS Firewall Manager to decide whether it fits the team's need to centrally manage WAF rules, Shield Advanced protections, and security groups across many accounts. Which statement correctly describes what the service does?

#### Options
- **A.** It centrally configures and manages firewall-related services, including AWS WAF rules, AWS Shield Advanced protections, and VPC security groups. **[CORRECT]**
- **B.** It is a standalone network firewall appliance that customers install on individual EC2 instances to filter traffic at the operating system level.
- **C.** It is a machine learning service that automatically classifies and labels sensitive data discovered inside Amazon S3 buckets across an account.
- **D.** It is a credential vault that stores database passwords and API keys and rotates them automatically on a schedule defined by the account owner.

**Correct Answer:** `A`
> **Summary:** It centrally configures and manages firewall-related services, including AWS WAF rules, AWS Shield Advanced protections, and VPC security groups.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Firewall Manager centrally manages firewall-related protections such as WAF rules, Shield Advanced, and security groups across the accounts in an AWS Organization, which is its actual role.

- **Option B:** ❌ **Why it is INCORRECT:**  
  There is no per-instance firewall appliance called Firewall Manager; it is a management layer over existing account-level and organization-level firewall services.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Discovering and classifying sensitive data inside S3 describes Amazon Macie's function, not Firewall Manager's centralized policy management role.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Storing and rotating credentials describes AWS Secrets Manager, a completely different service from the network policy management Firewall Manager performs.

---

### Question 35

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.4: Identify components and resources for security.`  
**Origin:** *Live Quiz Engine (ID: 80591)*

> **Scenario:**  
> Where would a customer go to find a centralized, high-level overview of AWS security offerings, security-related announcements, and links to deeper resources like whitepapers and the Security Blog, as an entry point before drilling into a specific topic?

#### Options
- **A.** The AWS Security Center, which serves as a landing page linking to AWS security offerings, announcements, whitepapers. **[CORRECT]**
- **B.** AWS Secrets Manager, which stores and rotates application credentials and does not serve as an entry point for browsing security resources.
- **C.** Amazon Inspector, which scans compute resources for vulnerabilities and does not host a landing page of security resources or announcements.
- **D.** AWS Config, which records resource configuration changes over time and does not function as a hub for security documentation and announcements.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  The Security Center is the entry-point landing page AWS maintains for security offerings, announcements, and links out to deeper resources like whitepapers and the Security Blog, matching this description.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Secrets Manager is a credential storage and rotation service with no role as a landing page for browsing general security resources.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Inspector is a vulnerability scanning service for compute resources; it does not host or link to general security documentation.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Config tracks configuration history for compliance and auditing purposes; it is not a documentation hub linking to security resources.

---

### Question 36

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.4: Identify components and resources for security.`  
**Origin:** *Live Quiz Engine (ID: 80582)*

> **Scenario:**  
> After Amazon GuardDuty raises a finding that an EC2 instance may be compromised, a security analyst wants to visually trace how that instance's network connections, IAM role usage, and API calls relate to each other over time, to determine the root cause. Which service supports this kind of investigation?

#### Options
- **A.** Amazon Detective, which automatically collects log data and builds an interactive visual graph of resource behavior to help analysts investigate findings. **[CORRECT]**
- **B.** AWS Trusted Advisor, which checks account configuration against best-practice categories but does not build visual graphs of historical resource behavior.
- **C.** AWS WAF, which filters incoming HTTP and HTTPS requests against rules but does not provide any historical investigation or visualization capability.
- **D.** AWS Artifact, which provides on-demand access to compliance reports and agreements rather than any tooling for security incident investigation.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Detective is purpose-built to ingest logs and build an interactive graph of resource, IAM, and network relationships over time, which is exactly the root-cause investigation workflow described.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Trusted Advisor produces point-in-time configuration recommendations and has no historical, graph-based investigation capability for tracing a finding's cause.

- **Option C:** ❌ **Why it is INCORRECT:**  
  WAF's role is filtering live web traffic against rules; it has no facility for visualizing or investigating past resource behavior.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Artifact is a static compliance document repository and offers no investigative tooling for tracing the cause of a security finding.

---

### Question 37

**Classification:** `Domain 2: Security and Compliance` | `Subdomain 2.4: Identify components and resources for security.`  
**Origin:** *Live Quiz Engine (ID: 80573)*

> **Scenario:**  
> After enabling Amazon GuardDuty, a company notices a finding indicating that an EC2 instance in its account is communicating with an IP address known to be associated with command-and-control infrastructure. How did GuardDuty most likely identify this activity?

#### Options
- **A.** By comparing the instance's VPC flow log and DNS query data against threat intelligence feeds and machine learning anomaly models. **[CORRECT]**
- **B.** By installing a lightweight agent on the EC2 instance that inspects running processes and open file handles for known malware signatures.
- **C.** By scanning the instance's attached Amazon EBS volumes offline and comparing file hashes against a database of previously identified malicious files.
- **D.** By requiring the security team to manually upload suspicious IP addresses into GuardDuty before it can generate any related finding.

**Correct Answer:** `A`

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  GuardDuty works by continuously analyzing existing log sources like VPC flow logs and DNS queries against threat intelligence feeds and anomaly-detection models, which is exactly how it recognized the command-and-control communication.

- **Option B:** ❌ **Why it is INCORRECT:**  
  GuardDuty is agentless by design; it does not install software on instances to inspect running processes, which distinguishes it from endpoint protection tools.

- **Option C:** ❌ **Why it is INCORRECT:**  
  GuardDuty does not perform offline volume or file-hash scanning; that kind of static file analysis is not part of how it generates findings.

- **Option D:** ❌ **Why it is INCORRECT:**  
  GuardDuty findings are generated automatically from its own analysis; customers do not need to pre-upload indicators for it to detect known malicious IP communication.

---

