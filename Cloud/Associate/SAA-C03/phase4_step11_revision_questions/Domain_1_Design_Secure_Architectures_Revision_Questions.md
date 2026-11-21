# AWS Certified Solutions Architect - Associate (SAA-C03)
## Domain 1: Design Secure Architectures (30%)

> **Focus:** Official AWS Exam Objectives for Domain 1: Design Secure Architectures  
> **Total Scenario Questions:** 36  

---

### Question 01 [SAA-C03-D1-Q001]

**Task Statement 1.1**

A company has an application running on Amazon EC2 instances in AWS Account A that needs to read and write objects to an Amazon S3 bucket located in AWS Account B. The security team mandates that credentials must never be hardcoded and access must follow the principle of least privilege. How should the solutions architect configure access?

- **A)** Create an IAM user in Account B with full S3 permissions, generate access keys, and store them securely in AWS Systems Manager Parameter Store in Account A for the EC2 instances to retrieve.
- **B)** Create an IAM role in Account B with an S3 permissions policy. Attach a trust policy to the role allowing Account A's IAM role to assume it. Grant the EC2 instance profile in Account A permission to call sts:AssumeRole.
- **C)** Configure an S3 Access Control List (ACL) on the bucket in Account B granting public read and write access, and restrict IP access via the EC2 instance Elastic IP.
- **D)** Establish a VPC Peering connection between Account A and Account B and configure security groups to allow direct HTTP traffic to Amazon S3.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
The AWS Well-Architected Security Pillar recommends cross-account IAM role assumption (`sts:AssumeRole`) for secure, temporary credential delegation without sharing long-term static keys. An IAM role in Account B defines the S3 access policy, and its trust policy trusts Account A. The EC2 instance profile in Account A assumes this role to obtain short-lived credentials.
- Option A violates security best practices by creating long-term access keys.
- Option C uses public ACLs which expose the bucket and violate least privilege.
- Option D is architecturally incorrect because Amazon S3 is a regional public AWS service, not a VPC resource accessible directly over VPC peering without VPC endpoints.

**References:**
- AWS Well-Architected Framework - Security Pillar
- AWS IAM Documentation: Cross-Account Resource Access

</details>

---

### Question 02 [SAA-C03-D1-Q002]

**Task Statement 1.3**

An enterprise application stores relational database credentials in plaintext configuration files on EC2 instances. The security policy requires that database credentials must be encrypted at rest, rotated automatically every 30 days without application downtime, and audited. Which solution satisfies these requirements with minimal operational overhead?

- **A)** Store the credentials in AWS Key Management Service (AWS KMS) as a custom encrypted payload and write a daily cron job on EC2 to regenerate credentials.
- **B)** Store the credentials in AWS Secrets Manager, enable automatic rotation using a built-in AWS Lambda rotation function every 30 days, and update the application to retrieve secrets via the AWS SDK.
- **C)** Store the credentials in AWS Systems Manager Parameter Store as a SecureString parameter and configure an Amazon EventBridge rule to manually trigger an EC2 reboot every 30 days.
- **D)** Encrypt the credentials file using OpenSSL on the EC2 instances and store the private key in an Amazon S3 bucket with versioning enabled.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Secrets Manager is specifically engineered for managing, retrieving, and automatically rotating database credentials (such as Amazon RDS MySQL, PostgreSQL, Aurora, and SQL Server) using built-in AWS Lambda rotation functions without downtime.
- Option A requires extensive custom scripting and does not natively manage database user passwords.
- Option C: Systems Manager Parameter Store supports SecureString parameters but does not have native out-of-the-box automated credential rotation for RDS databases like Secrets Manager does.
- Option D introduces high operational complexity and leaves keys vulnerable.

**References:**
- AWS Secrets Manager User Guide: Rotating Secrets
- AWS Well-Architected Security Pillar

</details>

---

### Question 03 [SAA-C03-D1-Q003]

**Task Statement 1.2**

A public-facing e-commerce web application running behind an Application Load Balancer (ALB) has experienced repeated SQL injection (SQLi) and Cross-Site Scripting (XSS) attacks. The solutions architect must deploy an automated mitigation solution that inspects incoming HTTP/HTTPS requests and blocks malicious patterns before they reach the web tier. What should be implemented?

- **A)** Configure Network Access Control Lists (Network ACLs) on the public subnets to drop incoming HTTP requests containing malicious SQL fragments.
- **B)** Associate an AWS WAF Web ACL with the Application Load Balancer, and enable AWS Managed Rules for Core Rule Set (CRS) and SQL database rule sets.
- **C)** Deploy AWS Shield Standard and enable automatic Route 53 health-check failover to a static error page.
- **D)** Install host-based intrusion prevention software (HIPS) on every EC2 instance and write custom iptables packet filtering rules.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS WAF (Web Application Firewall) operates at Layer 7 (HTTP/HTTPS) and can be associated with Application Load Balancers, Amazon CloudFront, and Amazon API Gateway. AWS Managed Rules include rule groups for SQL database vulnerabilities (SQLi) and Core Rule Set (XSS, generic web exploits).
- Option A: Network ACLs operate at Layer 4 (IP/port) and cannot inspect HTTP payload strings or query parameters.
- Option C: AWS Shield Standard provides Layer 3/4 DDoS protection automatically, not Layer 7 application vulnerability inspection.
- Option D increases management overhead and fails to block malicious traffic before it hits the compute instances.

**References:**
- AWS WAF Developer Guide: AWS Managed Rules
- AWS Well-Architected Reliability and Security Pillars

</details>

---

### Question 04 [SAA-C03-D1-Q004]

**Task Statement 1.2**

A financial services institution hosts its mission-critical banking portal on Amazon CloudFront and Application Load Balancers. The organization requires enterprise-grade protection against sophisticated Layer 7 distributed denial of service (DDoS) attacks, 24/7 dedicated support from the AWS Shield Response Team (SRT), and financial cost protection against bill spikes caused by DDoS attacks. Which service meets these requirements?

- **A)** AWS Shield Standard
- **B)** AWS Shield Advanced
- **C)** AWS GuardDuty
- **D)** AWS Network Firewall

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Shield Advanced provides expanded DDoS protection for Internet-facing resources (CloudFront distributions, Route 53 hosted zones, ALBs, NLBs, and Elastic IPs). It includes 24/7 direct access to the AWS Shield Response Team (SRT), proactive engagement, advanced real-time metrics, and DDoS cost protection (service credits for scaling charges during an attack).
- Option A: AWS Shield Standard is free and automatically active for all AWS customers, but it only covers common Layer 3/4 attacks without SRT support or cost protection.
- Option C: GuardDuty is an intelligent threat detection service, not an active inline DDoS mitigation system.
- Option D: AWS Network Firewall operates within VPCs at Layers 3-7 for stateful traffic inspection, but does not provide DDoS cost protection or SRT engagement.

**References:**
- AWS Shield Advanced Developer Guide
- AWS DDoS Resiliency Whitepaper

</details>

---

### Question 05 [SAA-C03-D1-Q005]

**Task Statement 1.3**

An architect is designing a healthcare application that stores Protected Health Information (PHI) in Amazon DynamoDB. Regulatory compliance requires that encryption keys must be managed by the customer, key access must be audited via AWS CloudTrail, and key rotation must occur annually automatically. Which encryption mechanism satisfies these compliance requirements?

- **A)** AWS owned key (Default DynamoDB encryption)
- **B)** AWS managed key (`aws/dynamodb`)
- **C)** Customer managed key (CMK) in AWS Key Management Service (AWS KMS) with automatic key rotation enabled
- **D)** Client-side encryption using a hardcoded AES-256 key embedded in the application binary

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
AWS KMS Customer Managed Keys (CMKs) give customers full control over key policies, IAM access grants, deletion, and auditing through CloudTrail. Furthermore, AWS KMS provides an option to enable automatic annual key rotation for customer managed KMS keys.
- Option A: AWS owned keys cannot be managed, audited in CloudTrail, or configured with custom key policies by the customer.
- Option B: AWS managed keys are created by AWS on behalf of the user, but customers cannot alter their rotation schedule or manage their key policies directly.
- Option D violates security best practices and compliance by embedding static cryptographic keys in binaries.

**References:**
- AWS KMS Developer Guide: Rotating Customer Managed Keys
- AWS Well-Architected Security Pillar

</details>

---

### Question 06 [SAA-C03-D1-Q006]

**Task Statement 1.2**

A fleet of EC2 instances residing in a private subnet requires access to Amazon S3 to download large scientific dataset files. Due to strict corporate security policies, no internet connectivity, NAT Gateways, or Internet Gateways are permitted in the VPC. What should the solutions architect implement to allow secure, private access to Amazon S3 at no additional data transfer cost?

- **A)** Deploy an Interface VPC Endpoint (AWS PrivateLink) for Amazon S3 in the private subnet.
- **B)** Deploy a Gateway VPC Endpoint for Amazon S3 and update the private subnet's route table.
- **C)** Configure an egress-only Internet Gateway and associate it with the private subnet.
- **D)** Establish an AWS Site-to-Site VPN tunnel looping back to the S3 public endpoint.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
A Gateway VPC Endpoint for Amazon S3 routes traffic directly from private subnets across the AWS network backbone to S3 without passing through the public internet, NAT devices, or internet gateways. Furthermore, Gateway Endpoints for S3 and DynamoDB are completely free with no hourly or data processing charges.
- Option A: Interface VPC Endpoints (AWS PrivateLink) for S3 also provide private connectivity, but they incur hourly endpoint fees and per-GB data processing fees, whereas Gateway Endpoints are free.
- Option C: Egress-only Internet Gateways only work for IPv6 traffic and still route out to the internet.
- Option D is an anti-pattern that creates unnecessary routing complexity and latency.

**References:**
- AWS VPC User Guide: Gateway VPC Endpoints
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 07 [SAA-C03-D1-Q007]

**Task Statement 1.1**

An enterprise with 5,000 employees manages its corporate identity in an on-premises Microsoft Active Directory. The IT leadership wants to provide staff with single sign-on (SSO) access to multiple AWS accounts and third-party business applications without synchronizing employee passwords to the cloud. Which architecture provides the most seamless and secure solution?

- **A)** Create individual IAM users in each AWS account with matching usernames and passwords generated via a weekly PowerShell script.
- **B)** Deploy AWS IAM Identity Center (AWS Single Sign-On) integrated with the on-premises Active Directory using AWS Directory Service AD Connector.
- **C)** Use Amazon Cognito User Pools and manually export Active Directory credentials into Cognito via a nightly batch script.
- **D)** Establish an OpenID Connect (OIDC) identity provider in each AWS account pointing to an unauthenticated public EC2 proxy.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS IAM Identity Center (successor to AWS SSO) combined with AWS Directory Service AD Connector allows enterprise users to sign in to the AWS access portal using their corporate Active Directory credentials. AD Connector proxies authentication requests directly to on-premises domain controllers without caching or synchronizing passwords in the cloud.
- Option A creates immense operational overhead, violates security best practices, and risks credential desynchronization.
- Option C: Cognito User Pools is primarily designed for customer-facing web and mobile applications, not enterprise corporate multi-account workforce federation.
- Option D is insecure and impractical to manage across multiple accounts.

**References:**
- AWS IAM Identity Center User Guide
- AWS Directory Service Administration Guide

</details>

---

### Question 08 [SAA-C03-D1-Q008]

**Task Statement 1.1**

An organization manages 100 AWS accounts organized under AWS Organizations. The Chief Information Security Officer (CISO) mandates that no member account—regardless of local administrator permissions—should ever be allowed to launch unapproved expensive EC2 GPU instance types (such as `p4d.24xlarge`). How can the architect enforce this guardrail centrally?

- **A)** Attach an IAM permissions boundary to all IAM roles across every account using an AWS Systems Manager run command.
- **B)** Create a Service Control Policy (SCP) in the Organizations management account with a Deny effect on `ec2:RunInstances` for the specified instance types, and attach it to the Root or target Organizational Unit (OU).
- **C)** Create an AWS Config rule in each member account that stops non-compliant instances 1 hour after launch.
- **D)** Configure AWS Budgets to alert administrators when GPU instance spend exceeds $100.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Service Control Policies (SCPs) in AWS Organizations act as central guardrails that set the maximum available permissions across member accounts. An explicit `Deny` in an SCP overrides any permissions granted by local account administrators (even the root user of a member account). By specifying condition keys on instance types in an SCP, unauthorized GPU launches are blocked immediately at the API level.
- Option A: Permissions boundaries do not prevent local administrators from modifying other policies or creating unmanaged roles unless heavily restricted.
- Option C is reactive and still allows instances to launch and incur costs before termination.
- Option D is an alert, not an preventative access control.

**References:**
- AWS Organizations User Guide: Service Control Policies
- AWS Well-Architected Security Pillar

</details>

---

### Question 09 [SAA-C03-D1-Q009]

**Task Statement 1.2**

A company requires strict egress traffic filtering for all EC2 instances residing in its VPC. Specifically, outbound HTTP/HTTPS connections must only be allowed to a whitelist of approved fully qualified domain names (FQDNs), and non-compliant traffic must be dropped with detailed flow logging. Which managed AWS service satisfies this requirement?

- **A)** Security Groups
- **B)** Network ACLs
- **C)** AWS Network Firewall
- **D)** NAT Gateway

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
AWS Network Firewall provides stateful Layer 7 domain filtering, allowing administrators to restrict outbound HTTP and HTTPS traffic to an explicit whitelist of fully qualified domain names (FQDNs) using Suricata-compatible rules, along with detailed flow logging to CloudWatch Logs or Amazon S3.
- Option A: Security Groups are stateful but operate at Layer 4 (IP addresses and ports); they cannot evaluate domain names (FQDNs).
- Option B: Network ACLs are stateless Layer 4 filters; they only evaluate IP CIDR blocks and port numbers.
- Option D: NAT Gateway translates private IPs to public IPs for outbound connectivity but provides no application-layer filtering or domain whitelisting capabilities.

**References:**
- AWS Network Firewall Developer Guide: Domain List Rule Groups
- AWS Well-Architected Security Pillar

</details>

---

### Question 10 [SAA-C03-D1-Q010]

**Task Statement 1.1**

A mobile fitness tracking application allows users to register using email/password or social identity providers (Google, Apple, and Facebook). Upon successful authentication, the mobile app needs temporary, scoped AWS credentials to upload profile pictures directly to a private user-specific folder in Amazon S3. Which AWS architecture fulfills this pattern?

- **A)** Amazon Cognito User Pools for authentication and Amazon Cognito Identity Pools (Federated Identities) to vend temporary IAM credentials.
- **B)** AWS IAM Identity Center with SAML federation mapped to an on-premises LDAP directory.
- **C)** AWS Key Management Service (AWS KMS) generating temporary access tokens returned directly to the mobile app.
- **D)** Hardcoding an IAM user access key inside the mobile app code with an S3 full access policy.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Cognito User Pools provides user directory, registration, and social sign-in (Google, Apple, Facebook). Amazon Cognito Identity Pools (Federated Identities) exchanges user tokens from the User Pool for temporary, scoped AWS credentials that permit direct upload to Amazon S3 under least-privilege IAM roles.
- Option B is meant for workforce/enterprise employee access, not millions of public mobile app consumers.
- Option C: AWS KMS manages cryptographic keys, it does not manage user identities or vend temporary IAM credentials.
- Option D is an egregious security vulnerability that exposes long-term credentials in mobile binaries.

**References:**
- Amazon Cognito Developer Guide
- AWS Well-Architected Security Pillar

</details>

---

### Question 11 [SAA-C03-D1-Q011]

**Task Statement 1.3**

A legal archive firm must store digital court evidence in Amazon S3 for 7 years to comply with regulatory mandates. The records must follow a Write Once, Read Many (WORM) model where no user—including the AWS account root user—can overwrite or delete any object during the 7-year retention period. Which S3 feature must be configured?

- **A)** S3 Versioning with MFA Delete enabled
- **B)** S3 Object Lock in Governance Mode with a 7-year retention period
- **C)** S3 Object Lock in Compliance Mode with a 7-year retention period
- **D)** S3 Bucket Policy containing an explicit Deny on `s3:DeleteObject` for all IAM principals

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
Amazon S3 Object Lock in Compliance Mode enforces strict WORM retention. In Compliance Mode, a protected object version cannot be overwritten or deleted by ANY user, including the root user in your AWS account. Its retention period cannot be decreased, ensuring compliance with SEC Rule 17a-4 and FINRA regulations.
- Option A: MFA Delete prevents accidental deletion without MFA, but the root user can disable MFA Delete or bypass it.
- Option B: Governance Mode allows users with specific IAM permissions (`s3:BypassGovernanceRetention`) to alter retention settings or delete the object.
- Option D: A bucket policy can be modified or deleted by the account root user.

**References:**
- Amazon S3 User Guide: S3 Object Lock Overview
- AWS Well-Architected Security Pillar

</details>

---

### Question 12 [SAA-C03-D1-Q012]

**Task Statement 1.3**

A solutions architect must conduct an automated data discovery audit across multiple Amazon S3 buckets to identify unencrypted Personally Identifiable Information (PII), credit card numbers, and passport credentials. Which AWS service is specifically designed for this purpose?

- **A)** Amazon Inspector
- **B)** Amazon Macie
- **C)** Amazon GuardDuty
- **D)** AWS CloudTrail

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon Macie is a fully managed data security and privacy service that uses machine learning and pattern matching to automatically discover, classify, and protect sensitive data (such as PII, financial details, and credentials) in Amazon S3.
- Option A: Amazon Inspector is an automated vulnerability management service that scans EC2 instances and ECR container images for software vulnerabilities.
- Option C: Amazon GuardDuty is an intelligent threat detection service that analyzes network and API events, not deep content inspection of S3 objects.
- Option D: AWS CloudTrail records AWS API activity, not sensitive data stored in S3.

**References:**
- Amazon Macie User Guide
- AWS Well-Architected Security Pillar

</details>

---

### Question 13 [SAA-C03-D1-Q013]

**Task Statement 1.2**

A cybersecurity team requires continuous, intelligent threat detection across their entire AWS environment. The system must analyze VPC Flow Logs, DNS query logs, CloudTrail management and data events, and detect anomalies such as compromised EC2 instances communicating with known crypto-mining command-and-control servers. Which service should be enabled?

- **A)** Amazon GuardDuty
- **B)** Amazon CloudWatch Synthetics
- **C)** AWS WAF
- **D)** AWS Systems Manager Patch Manager

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon GuardDuty is an intelligent threat detection service that continuously monitors and processes AWS CloudTrail events, VPC Flow Logs, DNS logs, and EKS audit logs. It uses machine learning, anomaly detection, and integrated threat intelligence to identify unauthorized activity, such as crypto-mining or credential exfiltration.
- Option B: CloudWatch Synthetics runs canaries to test customer-facing endpoints and user flows.
- Option C: AWS WAF inspects web traffic at Layer 7, not internal VPC flows or DNS lookups.
- Option D: Patch Manager automates operating system patching on servers.

**References:**
- Amazon GuardDuty User Guide
- AWS Well-Architected Security Pillar

</details>

---

### Question 14 [SAA-C03-D1-Q014]

**Task Statement 1.1**

An architect is designing an application on Amazon EC2 that connects to an Amazon RDS for PostgreSQL database. To eliminate the risk of compromised database passwords, the security team requires that EC2 instances authenticate to PostgreSQL using temporary IAM tokens instead of static passwords. How can this be accomplished?

- **A)** Enable IAM database authentication on the RDS PostgreSQL instance, create a database user mapped to an IAM role, and have the EC2 instance generate an authentication token using the AWS SDK.
- **B)** Store the database password in an S3 bucket and assign an IAM policy allowing the EC2 instance to read the file.
- **C)** Use Amazon Cognito Identity Pools to authenticate the EC2 instance directly to PostgreSQL via LDAP.
- **D)** Create a bastion host in a public subnet with an open port 5432 and configure IP whitelist authentication.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon RDS supports IAM database authentication for MySQL and PostgreSQL. With IAM database authentication, you do not need to use passwords to connect to your DB instance. Instead, you authenticate using an IAM role and temporary authentication tokens generated by the AWS SDK (valid for 15 minutes), ensuring short-lived access without static credentials.
- Option B maintains static credentials in S3, which fails the requirement.
- Option C is invalid because RDS does not authenticate directly via Cognito Identity Pools for backend server connections.
- Option D exposes the database port to a public bastion host and does not use IAM token authentication.

**References:**
- Amazon RDS User Guide: IAM Database Authentication
- AWS Well-Architected Security Pillar

</details>

---

### Question 15 [SAA-C03-D1-Q015]

**Task Statement 1.2**

A company wants to expose an internal REST API built on Amazon API Gateway exclusively to applications running inside its VPC. The API must not be accessible over the public internet, and traffic between the VPC and API Gateway must not traverse the internet. Which solution meets these criteria?

- **A)** Deploy an Edge-optimized API Gateway and associate an AWS WAF Web ACL to block all public IPs.
- **B)** Deploy a Regional API Gateway and assign it an Elastic IP address.
- **C)** Deploy a Private API Gateway, create an Interface VPC Endpoint (`execute-api`) in the VPC, and attach a resource policy to the API restricting access to the VPC endpoint.
- **D)** Deploy an HTTP API with mutual TLS (mTLS) enabled over public Route 53 DNS records.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
A Private API Gateway can only be accessed from within an Amazon VPC through an Interface VPC Endpoint (powered by AWS PrivateLink) using the `com.amazonaws.[region].execute-api` service name. Attaching an API Gateway resource policy with an `aws:sourceVpce` condition ensures that only traffic originating from that specific VPC endpoint can execute the API.
- Option A: Edge-optimized APIs are routed through CloudFront edge locations and are public.
- Option B: Regional APIs are also public endpoints; API Gateway does not support attaching Elastic IPs directly.
- Option D routes traffic across the public internet, violating the non-public requirement.

**References:**
- Amazon API Gateway Developer Guide: Creating a Private API
- AWS Well-Architected Security Pillar

</details>

---

### Question 16 [SAA-C03-D1-Q016]

**Task Statement 1.2**

A two-tier web application consists of web servers in a public subnet and backend database instances in a private subnet. The database instances should only accept incoming MySQL traffic on port 3306 from the web servers. As the web server tier scales out dynamically with Auto Scaling, new instances must automatically gain database access without manual rule updates. How should the security group rules be configured?

- **A)** In the database security group, add an inbound rule allowing port 3306 with the source set to 0.0.0.0/0.
- **B)** In the database security group, add an inbound rule allowing port 3306 with the source set to the Security Group ID of the web servers.
- **C)** In the database Network ACL, add an inbound rule allowing port 3306 from the web server subnet CIDR block.
- **D)** Configure a cron job on database instances that dynamically discovers web server IP addresses and updates local firewall rules.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Security groups support referencing other security groups by their ID (`sg-xxxxxx`). By setting the source of the database security group's inbound rule to the web server security group ID, any EC2 instance launched by the Auto Scaling group with the web security group is automatically authorized to communicate with the database on port 3306, without needing to know specific IP addresses.
- Option A completely opens the database port to the entire internet.
- Option C uses Network ACLs with CIDR blocks; while this allows the subnet, security groups provide instance-level stateful control and cross-referencing.
- Option D adds unnecessary operational complexity and maintenance overhead.

**References:**
- Amazon VPC User Guide: Security Groups
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 17 [SAA-C03-D1-Q017]

**Task Statement 1.3**

A company hosts a web portal with an Application Load Balancer in the `us-east-1` region. The portal requires HTTPS encryption in transit. The engineering team wants to provision a trusted public SSL/TLS certificate that renews automatically every year without operational intervention. Which service and approach should be selected?

- **A)** Generate a self-signed certificate using OpenSSL and import it into AWS IAM SSL certificate storage.
- **B)** Request a public certificate using AWS Certificate Manager (ACM) with DNS validation, and configure the CNAME record in Amazon Route 53.
- **C)** Purchase a commercial certificate from an external CA and set up an AWS Lambda function to re-upload it annually.
- **D)** Configure an AWS KMS asymmetric key pair and assign it directly as the SSL listener certificate on the ALB.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Certificate Manager (ACM) provisions, manages, and deploys public SSL/TLS certificates for use with AWS services like ALBs and CloudFront. When DNS validation is used (especially with Route 53), ACM automatically renews certificates before expiration without requiring any manual intervention.
- Option A: Self-signed certificates generate browser security warnings and do not renew automatically.
- Option C incurs unnecessary commercial costs and manual renewal overhead.
- Option D is invalid because AWS KMS keys cannot be bound directly as SSL/TLS X.509 listener certificates on ALBs.

**References:**
- AWS Certificate Manager User Guide: DNS Validation and Managed Renewal
- AWS Well-Architected Security Pillar

</details>

---

### Question 18 [SAA-C03-D1-Q018]

**Task Statement 1.1**

An organization has 50 AWS accounts managed under AWS Organizations. The compliance officer requires a centralized, tamper-proof repository of all management and API activity across all accounts in a central security account. Individual account root users or administrators must not be able to delete or modify the collected audit logs. How should this be implemented?

- **A)** Create an AWS CloudTrail trail in each individual member account pointing to a local S3 bucket in each account.
- **B)** Create an Organization Trail in the AWS Organizations management account that delivers CloudTrail logs to an Amazon S3 bucket located in the designated central security account, protected by an S3 bucket policy and Object Lock.
- **C)** Use Amazon CloudWatch Logs agent on all EC2 instances and stream logs to an Amazon Kinesis Data Stream.
- **D)** Export AWS Config snapshots to an Amazon EFS file system shared across VPCs via Direct Connect.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
An AWS Organizations Trail enables centralized logging of all AWS API activity across all accounts in the organization. The trail is managed from the management account and logs are delivered to an S3 bucket in a dedicated security account. Individual member account administrators cannot modify or disable this organization trail. Applying S3 Object Lock and restrictive bucket policies ensures logs are tamper-proof.
- Option A creates decentralized logging where local account administrators can disable or delete logs.
- Option C only logs operating system and server logs, not AWS API management events.
- Option D is complex and does not capture CloudTrail API activity.

**References:**
- AWS CloudTrail User Guide: Creating an Organization Trail
- AWS Well-Architected Security Pillar

</details>

---

### Question 19 [SAA-C03-D1-Q019]

**Task Statement 1.2**

A solutions architect needs to allow developers to securely administer private EC2 instances running Linux in private subnets. The security policy strictly prohibits opening inbound SSH port 22 in security groups, running bastion hosts, or managing public IP addresses. Which AWS service provides secure browser-based and CLI shell access conforming to these rules?

- **A)** AWS Systems Manager Session Manager
- **B)** EC2 Instance Connect with an Internet Gateway
- **C)** AWS Client VPN with a NAT Gateway
- **D)** AWS Cloud9 with an Elastic IP

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Systems Manager Session Manager provides secure, auditable instance management without needing to open inbound ports, maintain bastion hosts, or manage SSH keys. Communication is initiated outbound from the SSM Agent installed on the EC2 instance to the Systems Manager service endpoint (via NAT or VPC Interface Endpoints).
- Option B: EC2 Instance Connect requires network reachability (public IP or bastion/VPN) to port 22 on the instance.
- Option C requires deploying and maintaining client VPN certificates and client infrastructure.
- Option D violates the private subnet and no public IP policy.

**References:**
- AWS Systems Manager User Guide: Session Manager
- AWS Well-Architected Security Pillar

</details>

---

### Question 20 [SAA-C03-D1-Q020]

**Task Statement 1.3**

A banking institution is migrating a cryptographic application to AWS. Government regulations require that cryptographic keys must be stored in single-tenant, dedicated Hardware Security Modules (HSMs) certified under FIPS 140-2 Level 3, where AWS personnel have no administrative access to the hardware keys. Which service must be chosen?

- **A)** AWS Key Management Service (AWS KMS) multi-tenant keys
- **B)** AWS CloudHSM
- **C)** AWS Secrets Manager
- **D)** AWS Systems Manager Parameter Store

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS CloudHSM provides dedicated, single-tenant FIPS 140-2 Level 3 validated HSM hardware under the customer's direct administrative control inside their VPC. AWS provides hardware maintenance but has no access to the customer's cryptographic keys.
- Option A: Standard AWS KMS uses multi-tenant HSMs certified to FIPS 140-2 Level 3 (or Level 2 depending on mode), but the hardware is multi-tenant and managed by AWS.
- Options C and D are secret and parameter storage services, not dedicated cryptographic hardware security modules.

**References:**
- AWS CloudHSM User Guide
- AWS Well-Architected Security Pillar

</details>

---

### Question 21 [SAA-C03-D1-Q021]

**Task Statement 1.2**

An architect notices that a specific external IPv4 address (`198.51.100.25`) is launching a denial of service attack against a web application. The architect needs to immediately drop all traffic from this specific IP address before it enters the subnet. Which configuration achieves this with the lowest latency?

- **A)** Add a Deny rule for `198.51.100.25/32` to the Security Group associated with the instances.
- **B)** Add a Deny rule for `198.51.100.25/32` with a low rule number to the inbound rules of the subnet's Network ACL.
- **C)** Configure an AWS WAF rate-based rule with an evaluation window of 24 hours.
- **D)** Create an Amazon Route 53 Geolocation record that points the IP to 127.0.0.1.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Network Access Control Lists (NACLs) operate at the subnet boundary as stateless packet filters that support explicit `ALLOW` and `DENY` rules evaluated in numbered order. By placing a `DENY` rule with a low number (e.g., rule 50) for `198.51.100.25/32`, packets from this IP are dropped at the subnet boundary before reaching instances.
- Option A: Security Groups do NOT support `DENY` rules; they only support `ALLOW` rules (implicit deny).
- Option C: While WAF can block IPs, Network ACLs drop packets earlier at the network layer without incurring WAF inspection fees.
- Option D: Route 53 Geolocation routes by geographic country/state, not individual arbitrary client IP addresses.

**References:**
- Amazon VPC User Guide: Network ACLs
- AWS Well-Architected Security Pillar

</details>

---

### Question 22 [SAA-C03-D1-Q022]

**Task Statement 1.2**

A software company builds containerized microservices pushed to Amazon Elastic Container Registry (ECR) and runs them on Amazon EC2. The security team mandates that all container images and EC2 instances must be automatically scanned for Common Vulnerabilities and Exposures (CVEs) with prioritized severity ratings. Which service fulfills this mandate?

- **A)** Amazon Inspector
- **B)** Amazon Macie
- **C)** AWS Shield Standard
- **D)** Amazon GuardDuty

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Inspector is an automated vulnerability management service that scans AWS workloads (Amazon EC2 instances, AWS Lambda functions, and container images in Amazon ECR) for software vulnerabilities and unintended network exposure, assigning normalized risk scores.
- Option B: Amazon Macie discovers and classifies sensitive data (PII) in Amazon S3.
- Option C: AWS Shield Standard mitigates DDoS attacks.
- Option D: Amazon GuardDuty detects suspicious runtime behavior and compromised credentials, but does not perform static CVE vulnerability scans on software packages.

**References:**
- Amazon Inspector User Guide
- AWS Well-Architected Security Pillar

</details>

---

### Question 23 [SAA-C03-D1-Q023]

**Task Statement 1.1**

A security audit reveals that several Amazon S3 buckets across a company's production account have been accidentally configured with public read access. The solutions architect needs a single centralized setting to ensure that no existing or future S3 buckets in the account can ever be made publicly accessible. What should be configured?

- **A)** Enable Amazon S3 Block Public Access at the AWS Account level.
- **B)** Write an AWS Lambda function to poll all buckets every 5 minutes and delete public policies.
- **C)** Attach an IAM policy denying `s3:*` to all users in the account.
- **D)** Delete all Internet Gateways attached to the account's VPCs.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon S3 Block Public Access provides centralized account-level settings that override all bucket policies and access control lists (ACLs) to prevent public access across all existing and future buckets in that account.
- Option B introduces latency and operational overhead when a native S3 control exists.
- Option C disables all S3 access, preventing legitimate authorized application workflows.
- Option D does not affect S3 public access because S3 is accessed via public endpoints over the internet, not solely through a specific VPC's Internet Gateway.

**References:**
- Amazon S3 User Guide: S3 Block Public Access
- AWS Well-Architected Security Pillar

</details>

---

### Question 24 [SAA-C03-D1-Q024]

**Task Statement 1.3**

An architect is tasked with preventing accidental or malicious permanent deletion of objects in an Amazon S3 bucket used for data lake storage. Even if an IAM principal has `s3:DeleteObject` permissions, permanently deleting an object version or altering bucket versioning must require a physical hardware security token. Which S3 capability fulfills this?

- **A)** S3 Object Lock Legal Hold
- **B)** S3 MFA Delete with S3 Versioning enabled
- **C)** S3 Lifecycle rule with NoncurrentVersionExpiration
- **D)** S3 Server-Side Encryption with Customer-Provided Keys (SSE-C)

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
S3 MFA Delete adds an extra layer of security on S3 versioned buckets. When MFA Delete is enabled, the bucket owner must supply an authentication code generated by a hardware or virtual MFA device to permanently delete an object version or change the versioning state of the bucket.
- Option A: Legal Holds prevent object deletion during retention, but do not specifically require a physical MFA code to alter bucket versioning state.
- Option C automatically deletes old versions, which is the opposite of preventing deletion.
- Option D encrypts objects but does not restrict deletion operations.

**References:**
- Amazon S3 User Guide: Configuring MFA Delete
- AWS Well-Architected Security Pillar

</details>

---

### Question 25 [SAA-C03-D1-Q025]

**Task Statement 1.1**

A SaaS vendor provides an application running in Account A that needs to query metadata from customers' AWS accounts (such as Account B). The vendor must ensure that a malicious customer cannot trick Account A's service into accessing another customer's AWS resources (the confused deputy problem). Which IAM mechanism solves this issue?

- **A)** Using long-term IAM access keys generated in each customer account.
- **B)** Configuring cross-account IAM roles with an `ExternalId` condition required in the role trust policy.
- **C)** Enabling VPC Peering between the vendor VPC and all customer VPCs.
- **D)** Granting `AdministratorAccess` to Account A's root user in all customer accounts.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
The confused deputy problem occurs when an entity (the vendor application) is coerced by a malicious third party into acting on resources it has access to in another customer's account. To prevent this, the trust policy of the cross-account IAM role must include a condition check for an `sts:ExternalId` unique to each customer.
- Option A increases exposure of static credentials and does not prevent confused deputy risks.
- Option C provides network peering, not IAM authentication or role assumption security.
- Option D is an extreme security anti-pattern.

**References:**
- AWS IAM User Guide: How to use an external ID when granting access to your AWS resources
- AWS Well-Architected Security Pillar

</details>

---

### Question 26 [SAA-C03-D1-Q026]

**Task Statement 1.3**

A security engineer must ensure that all new Elastic Block Store (EBS) volumes created across an AWS Region are automatically encrypted at rest using an AWS KMS key, preventing any unencrypted volume from ever being created. What is the most efficient architectural approach?

- **A)** Write an AWS Lambda function that triggers on EC2 `CreateVolume` events to delete unencrypted volumes.
- **B)** Enable Amazon EBS Encryption by Default in the EC2 console settings for that specific Region.
- **C)** Configure a local bash script in the `/etc/rc.local` file of each EC2 instance.
- **D)** Attach an IAM policy to all developers denying `ec2:RunInstances` without encrypted AMI tags.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon EBS encryption by default is a regional account setting. Once enabled, all new EBS volumes and snapshot copies created in that region are automatically encrypted at rest using the specified KMS key (default AWS-managed or customer-managed CMK), with zero custom code or operational overhead.
- Option A is reactive and leaves a brief window where unencrypted data could be written.
- Option C only runs after the instance is already launched and volume attached.
- Option D leaves gaps for volumes created independently via the console or CLI.

**References:**
- Amazon EC2 User Guide: Encryption by Default
- AWS Well-Architected Security Pillar

</details>

---

### Question 27 [SAA-C03-D1-Q027]

**Task Statement 1.2**

An internal company dashboard running on EC2 behind an Application Load Balancer requires user authentication before displaying sensitive business analytics. The company uses an external OpenID Connect (OIDC) identity provider. The architect wants to offload authentication from the backend EC2 web servers without modifying application code. How can this be accomplished?

- **A)** Configure the Application Load Balancer listener rule with an 'Authenticate: OIDC' action to authenticate users before forwarding traffic to the target group.
- **B)** Deploy an Amazon CloudFront distribution and write a CloudFront Function to query the OIDC provider on every request.
- **C)** Install Apache Shiro on each EC2 instance and synchronize credentials manually.
- **D)** Place a Network Load Balancer in front of the ALB and enable TCP mutual TLS (mTLS).

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Application Load Balancers natively support user authentication. By configuring an ALB listener rule to authenticate requests through an OpenID Connect (OIDC) compliant Identity Provider (or Amazon Cognito), the ALB intercepts unauthenticated requests, handles the OAuth/OIDC handshake, and forwards authenticated claims in HTTP headers to the target EC2 instances without requiring changes to application code.
- Option B requires complex custom code maintenance in edge functions.
- Option C requires modifying the backend web servers, violating the requirement.
- Option D uses mTLS for client certificates, which does not authenticate against an OIDC web identity provider.

**References:**
- Elastic Load Balancing User Guide: Authenticate Users Using an Application Load Balancer
- AWS Well-Architected Security Pillar

</details>

---

### Question 28 [SAA-C03-D1-Q028]

**Task Statement 1.3**

A media streaming company allows paid subscribers to download video files stored in an Amazon S3 bucket. The download links must only be valid for 15 minutes and accessible only by the specific authenticated user who requested the link. What is the recommended architectural solution?

- **A)** Create an IAM user for each subscriber and grant read permissions to the S3 bucket.
- **B)** Generate Amazon S3 Presigned URLs with an expiration time of 15 minutes using temporary IAM credentials.
- **C)** Change the S3 bucket policy to public read and use a Lambda function to revert permissions after 15 minutes.
- **D)** Establish an AWS Direct Connect link between each subscriber and the AWS S3 endpoint.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon S3 Presigned URLs grant time-limited permission to download or upload specific S3 objects. The URL contains cryptographic signature parameters created using IAM credentials, and expires automatically after the designated duration (e.g., 15 minutes), ensuring secure, scalable delivery without creating IAM users for consumers.
- Option A does not scale (IAM is limited to 5,000 users per account and is designed for internal staff, not end customers).
- Option C exposes the entire bucket to the public internet.
- Option D is impossible and cost-prohibitive for consumer media streaming.

**References:**
- Amazon S3 User Guide: Sharing Objects Using Presigned URLs
- AWS Well-Architected Security Pillar

</details>

---

### Question 29 [SAA-C03-D1-Q029]

**Task Statement 1.1**

An architect needs to audit and track resource configuration changes across 20 AWS accounts over time, evaluate whether resources comply with internal security benchmarks (such as ensuring restricted SSH port access and encrypted S3 buckets), and generate compliance reports. Which service is designed for this?

- **A)** AWS Config and AWS Config Conformance Packs
- **B)** AWS CloudTrail
- **C)** Amazon CloudWatch Logs Insights
- **D)** AWS Trusted Advisor

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Config continuously assesses, audits, and evaluates the configurations of AWS resources against desired configuration rules. AWS Config Conformance Packs allow organizations to package collections of rules and remediation actions across multiple accounts to evaluate compliance against standards (e.g., CIS benchmarks, PCI-DSS).
- Option B: CloudTrail records API calls and events ('who did what and when'), but does not record point-in-time resource state snapshots or automated compliance evaluation.
- Option C searches log files, not AWS resource configuration history.
- Option D provides high-level architectural recommendations, not customizable multi-account compliance rules.

**References:**
- AWS Config Developer Guide: Conformance Packs
- AWS Well-Architected Security Pillar

</details>

---

### Question 30 [SAA-C03-D1-Q030]

**Task Statement 1.2**

A private subnet in a VPC contains application servers that must initiate outbound connections to the internet to download software updates, but must never accept inbound connections initiated from the public internet. What infrastructure components must be configured?

- **A)** Attach an Internet Gateway directly to the private subnet's route table.
- **B)** Deploy a NAT Gateway in a public subnet, add a route in the private subnet's route table directing `0.0.0.0/0` traffic to the NAT Gateway, and ensure the public subnet routes `0.0.0.0/0` to an Internet Gateway.
- **C)** Assign Elastic IP addresses directly to the private EC2 instances and disable security groups.
- **D)** Deploy an Application Load Balancer in the private subnet and associate an Elastic IP.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
A NAT (Network Address Translation) Gateway deployed in a public subnet translates private IP addresses to its public IP address for outbound internet requests while preventing external internet entities from initiating inbound connections to the private instances. The private subnet route table directs default traffic (`0.0.0.0/0`) to the NAT Gateway, and the public subnet route table directs traffic to the Internet Gateway (IGW).
- Option A makes the subnet public, allowing inbound reachability if instances have public IPs.
- Option C gives instances public reachability and strips stateful security group protection.
- Option D: ALBs distribute inbound traffic; they do not function as outbound NAT routers for EC2 instances.

**References:**
- Amazon VPC User Guide: NAT Gateways
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 31 [SAA-C03-D1-Q031]

**Task Statement 1.3**

A company must encrypt data stored in Amazon S3. The security team mandates that encryption keys must be managed on-premises, keys must never be stored or cached in AWS, and encryption/decryption must be performed on the client side before data is transmitted over the network to S3. Which method satisfies these requirements?

- **A)** Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3)
- **B)** Server-Side Encryption with AWS KMS Keys (SSE-KMS)
- **C)** Client-Side Encryption using an on-premises Master Key with the Amazon S3 Encryption Client
- **D)** Server-Side Encryption with Customer-Provided Keys (SSE-C)

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
With Client-Side Encryption, the client application encrypts data locally before sending it across the network to Amazon S3, and decrypts it locally after retrieval. Cryptographic keys remain exclusively within the customer's on-premises environment and are never transmitted to AWS.
- Options A and B are server-side encryption schemes where AWS manages the encryption process and keys.
- Option D (SSE-C): While the customer provides the key, the key is sent via HTTPS headers to AWS S3, which performs the actual encryption on AWS servers.

**References:**
- Amazon S3 Developer Guide: Protecting Data Using Client-Side Encryption
- AWS Well-Architected Security Pillar

</details>

---

### Question 32 [SAA-C03-D1-Q032]

**Task Statement 1.2**

An architect is configuring a Gateway VPC Endpoint for Amazon S3 to enable private EC2 instances to access S3. To adhere to least privilege, the architect must ensure that instances in this VPC can ONLY access a specific corporate bucket named `corporate-data-archive` and no other external S3 buckets. How should this constraint be applied?

- **A)** Attach a VPC Endpoint Policy to the Gateway Endpoint restricting allowed actions to the `arn:aws:s3:::corporate-data-archive` resource.
- **B)** Configure the EC2 instance operating system hosts file to redirect all S3 DNS queries.
- **C)** Apply an S3 Access Control List (ACL) granting read access to the VPC ID.
- **D)** Add an outbound rule to the private subnet's Network ACL denying port 443 to all other buckets.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
VPC Endpoint Policies are IAM resource policies attached directly to VPC endpoints (Gateway or Interface). By defining a VPC Endpoint Policy that specifies `Resource: [arn:aws:s3:::corporate-data-archive, arn:aws:s3:::corporate-data-archive/*]`, you prevent data exfiltration to unauthorized personal or external S3 buckets through that endpoint.
- Option B is fragile and easily bypassed by processes using IP addresses or alternative resolvers.
- Option C: S3 ACLs cannot evaluate VPC IDs.
- Option D: Network ACLs evaluate IP addresses and ports, not S3 bucket names or ARN resources.

**References:**
- Amazon VPC User Guide: Endpoint Policies for Amazon S3
- AWS Well-Architected Security Pillar

</details>

---

### Question 33 [SAA-C03-D1-Q033]

**Task Statement 1.1**

A financial auditor requires a monthly report of all IAM user access keys in an AWS account that have not been used for over 90 days, as well as accounts where MFA is not enabled on the root user. What AWS IAM feature provides this consolidated credential audit report with minimal effort?

- **A)** IAM Credential Report
- **B)** AWS CloudTrail Event History
- **C)** Amazon CloudWatch Alarms
- **D)** AWS Systems Manager Inventory

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
The IAM Credential Report is a downloadable CSV report listing all users in your AWS account and the status of their various credentials, including passwords, access keys, MFA devices, and signing certificates, along with their last used timestamps. It allows easy identification of inactive keys (>90 days) and MFA compliance.
- Option B logs historical API events, requiring complex log parsing to determine key inactivity.
- Option C monitors metrics, not static IAM credential lifecycles.
- Option D inventories operating system applications and metadata on EC2 instances.

**References:**
- AWS IAM User Guide: Getting Credential Reports
- AWS Well-Architected Security Pillar

</details>

---

### Question 34 [SAA-C03-D1-Q034]

**Task Statement 1.2**

A security operations team wants to automatically detect when any security group in their AWS environment has an inbound rule allowing unrestricted traffic (0.0.0.0/0) on port 22 (SSH) or port 3389 (RDP), and automatically revoke the rule. What is the most effective serverless solution?

- **A)** Deploy an AWS Config managed rule (`restricted-ssh` / `restricted-common-ports`) with automatic remediation using an AWS Systems Manager Automation document.
- **B)** Schedule a cron job on an EC2 instance that runs every 60 seconds to execute `aws ec2 describe-security-groups`.
- **C)** Use Amazon GuardDuty to automatically terminate instances associated with open security groups.
- **D)** Create an Amazon SNS topic subscribed to all CloudWatch alarms to notify the sysadmin to manually edit the rules.
- **answer)** A

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Config provides pre-built managed rules such as `restricted-ssh` and `restricted-common-ports` that continuously evaluate security group configurations. When a non-compliant rule is detected, AWS Config can trigger automatic remediation via an AWS Systems Manager Automation runbook (e.g., `AWS-DisablePublicAccessForSecurityGroup`) to immediately revoke the rule without human delay.
- Option B introduces server maintenance and scaling bottlenecks.
- Option C: GuardDuty detects threats; it does not automatically terminate instances out of the box or modify security group rules natively.
- Option D is manual and does not achieve automated remediation.

**References:**
- AWS Config Developer Guide: Remediating Noncompliant AWS Resources
- AWS Well-Architected Security Pillar

</details>

---

### Question 35 [SAA-C03-D1-Q035]

**Task Statement 1.1**

An architect is designing an authorization model where employees should only be able to manage EC2 instances that match their own department. For example, members of the 'Finance' department can only start and stop EC2 instances tagged with `Department=Finance`. Which IAM strategy minimizes the number of policies required?

- **A)** Create a distinct IAM policy for every department explicitly listing the instance IDs of their servers.
- **B)** Use Attribute-Based Access Control (ABAC) with IAM policies that compare the principal's tag `aws:PrincipalTag/Department` against the resource tag `aws:ResourceTag/Department` using a condition element.
- **C)** Deploy separate AWS accounts for each department with separate VPCs connected by a Transit Gateway.
- **D)** Use AWS KMS key policies to grant instance start permissions.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Attribute-Based Access Control (ABAC) uses tags on both the IAM principal (user/role) and the AWS resource. A single policy with the condition `StringEquals: {'aws:ResourceTag/Department': '${aws:PrincipalTag/Department}'}` allows employees to manage only instances tagged with their department, scaling effortlessly as new departments or instances are added without authoring new policies.
- Option A creates immense administrative overhead as instances are launched and terminated.
- Option C adds high architectural complexity and cross-account networking cost for a simple authorization requirement.
- Option D: KMS key policies control cryptographic operations, not EC2 instance state transitions.

**References:**
- AWS IAM User Guide: What is ABAC for AWS?
- AWS Well-Architected Security Pillar

</details>

---

### Question 36 [SAA-C03-D1-Q036]

**Task Statement 1.1**

A healthcare enterprise requires that developers must be able to create new IAM roles for Lambda functions in their development accounts, but must NEVER be able to grant those roles permissions beyond a specific predefined set of permissions (e.g., they must never grant `iam:*` or `administrator` permissions). How can the cloud architect enforce this constraint?

- **A)** Require an IAM Permissions Boundary to be attached to every newly created IAM role, enforced via an IAM policy condition on the developer's role.
- **B)** Remove all IAM permissions from developers and submit manual support tickets for every role creation.
- **C)** Use Amazon Macie to inspect IAM role policies on a weekly schedule.
- **D)** Attach an AWS Organizations SCP in the development account with `Allow *`.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
An IAM Permissions Boundary is an advanced IAM feature that uses a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM role or user. By adding a condition to the developer's IAM policy requiring that any role they create MUST have the specified permissions boundary attached, developers can create roles autonomously without being able to elevate their privileges (privilege escalation prevention).
- Option B slows down agile development and creates heavy operational bottlenecks.
- Option C is reactive and Macie scans S3 data, not IAM policies.
- Option D: An SCP with `Allow *` provides no security restriction.

**References:**
- AWS IAM User Guide: Permissions Boundaries for IAM Entities
- AWS Well-Architected Security Pillar

</details>

---

