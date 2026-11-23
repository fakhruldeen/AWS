# Module 01: Designing Secure AWS Architectures — Knowledge Check

> **Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Module 1: Identity, Network Security & Data Protection  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 1 materials and completing Lab 01 and Lab 05. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
An application running on EC2 instances in a private subnet needs to access an Amazon S3 bucket in the same region. The company security policy prohibits any internet egress through an Internet Gateway or NAT Gateway. Which solution provides private S3 connectivity at zero additional cost?

- **A.** Deploy an Interface VPC Endpoint (AWS PrivateLink) for Amazon S3 in the private subnet.
- **B.** Deploy a Gateway VPC Endpoint for Amazon S3 and update the private subnet route table.
- **C.** Create an egress-only Internet Gateway and associate it with the private subnet.
- **D.** Configure an AWS Site-to-Site VPN to loop traffic back into the VPC.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Gateway VPC Endpoints** for Amazon S3 and DynamoDB route traffic across the private AWS network backbone without traversing the public internet. Crucially, Gateway Endpoints are completely **free** with zero hourly or data processing charges.
- **Interface VPC Endpoints** for S3 also provide private connectivity via PrivateLink, but incur hourly charges ($0.01/hr per AZ) and per-GB data processing fees ($0.01/GB).
</details>

---

### Question 2
A company needs to store database connection passwords and rotate them automatically every 30 days without application downtime. Which service should be used?

- **A.** AWS Key Management Service (AWS KMS)
- **B.** AWS Systems Manager Parameter Store with standard parameters
- **C.** AWS Secrets Manager with automatic Lambda rotation enabled
- **D.** Amazon S3 with client-side encryption

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- **AWS Secrets Manager** is specifically purpose-built to manage, retrieve, and automatically rotate credentials for databases (RDS MySQL, PostgreSQL, Aurora, SQL Server) using integrated AWS Lambda rotation functions.
- **Parameter Store** supports encrypted `SecureString` parameters but does not include out-of-the-box automated database credential rotation workflows like Secrets Manager.
</details>

---

### Question 3
A web application running behind an Application Load Balancer has been targeted by SQL injection (SQLi) and Cross-Site Scripting (XSS) attacks. What should the solutions architect deploy to automatically inspect and block these HTTP/HTTPS attacks?

- **A.** Network Access Control Lists (Network ACLs)
- **B.** Security Groups on the ALB
- **C.** AWS WAF with AWS Managed Rules associated with the ALB
- **D.** AWS Shield Standard

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- **AWS WAF** operates at Layer 7 (HTTP/HTTPS) and inspects request bodies, query strings, and headers. AWS Managed Rules include dedicated rule groups for Common Vulnerabilities and SQL database (SQLi) protection.
- **Security Groups** and **Network ACLs** operate at Layer 4 (IP/port) and cannot parse HTTP payloads or detect application-level exploits.
</details>

---

### Question 4
An architect must enforce that no member account in an AWS Organization can ever launch unapproved expensive EC2 GPU instance types, even if the user has `AdministratorAccess` in the member account. Which mechanism enforces this guardrail centrally?

- **A.** IAM Permissions Boundary attached to local users
- **B.** Service Control Policy (SCP) attached to the Root or Organizational Unit (OU)
- **C.** Amazon Inspector automated vulnerability scan
- **D.** AWS Config rule with 24-hour evaluation period

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Service Control Policies (SCPs)** define the maximum permissions boundary for accounts in an AWS Organization. An explicit `Deny` in an SCP overrides all permissions granted locally—even for the member account root user.
- **Permissions boundaries** apply only to specific IAM identities within an account and can be bypassed if local admins create new roles without them.
</details>

---

### Question 5
A healthcare organization must retain medical records in Amazon S3 for 10 years to comply with HIPAA regulations. The regulatory mandate specifies that no user, including the AWS account root user, can delete or overwrite any object during the 10-year period. Which feature satisfies this?

- **A.** S3 Versioning with MFA Delete
- **B.** S3 Object Lock in Governance Mode
- **C.** S3 Object Lock in Compliance Mode
- **D.** S3 Bucket Policy with `Deny` on `s3:DeleteObject`

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- **S3 Object Lock in Compliance Mode** enforces strict WORM (Write Once, Read Many) retention. In Compliance Mode, a protected object version cannot be overwritten or deleted by ANY user, including the account root user, and its retention period cannot be shortened.
- In **Governance Mode**, users with the `s3:BypassGovernanceRetention` permission can alter or delete the objects.
</details>

---

### Question 6
An architect needs to allow developers to access Linux EC2 instances in private subnets for debugging without opening inbound port 22 in security groups and without running bastion hosts. Which AWS capability provides secure shell access?

- **A.** AWS Systems Manager Session Manager
- **B.** EC2 Instance Connect with an Internet Gateway
- **C.** AWS Client VPN
- **D.** Amazon Route 53 Private Hosted Zone

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **AWS Systems Manager Session Manager** establishes secure browser-based and CLI shell access over encrypted TLS connections via the SSM Agent. Connections are initiated outbound to the Systems Manager service, eliminating the need to open inbound port 22 or maintain bastion hosts.
</details>

---

### Question 7
Which security service continuously monitors VPC Flow Logs, DNS query logs, and CloudTrail management events using machine learning to detect unauthorized behavior such as crypto-mining command-and-control communication?

- **A.** Amazon Inspector
- **B.** Amazon Macie
- **C.** Amazon GuardDuty
- **D.** AWS WAF

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- **Amazon GuardDuty** is an intelligent threat detection service that analyzes network flow logs, DNS logs, and CloudTrail events to identify anomalous and malicious activity (e.g., Bitcoin mining, compromised credentials, reconnaissance).
- **Amazon Macie** discovers sensitive data (PII) in S3.
- **Amazon Inspector** scans EC2 instances and ECR images for software vulnerabilities (CVEs).
</details>

---

### Question 8
A company wants to grant a SaaS vendor's AWS account access to read metadata from an S3 bucket in their account. What condition should be included in the IAM role's trust policy to prevent the 'confused deputy' security vulnerability?

- **A.** `aws:PrincipalTag`
- **B.** `sts:ExternalId`
- **C.** `aws:RequestedRegion`
- **D.** `aws:MultiFactorAuthPresent`

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- When a third party assumes an IAM role on your behalf, specifying an `sts:ExternalId` in the trust policy ensures that the vendor cannot be tricked by another malicious customer into assuming your role to access your resources (preventing the **confused deputy** problem).
</details>

---

### Question 9
How should security group rules be configured to allow web tier instances in an Auto Scaling group to communicate with private RDS MySQL instances (port 3306) dynamically without updating IP addresses?

- **A.** In the RDS security group, set the source to `0.0.0.0/0`.
- **B.** In the RDS security group, set the source to the Security Group ID of the web tier instances (`sg-xxxxxx`).
- **C.** In the RDS Network ACL, set an inbound allow rule for the private subnet CIDR.
- **D.** Create an IAM DB authentication token mapped to the instance private IP.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- Referencing a **Security Group ID** as the source in an inbound rule dynamically authorizes any instance associated with that security group. As the Auto Scaling group scales instances in or out, new instances are automatically authorized without hardcoding or managing IP addresses.
</details>

---

### Question 10
An enterprise needs to ensure all EBS volumes created across an AWS Region are automatically encrypted at creation time, preventing any unencrypted volume from ever existing. What is the most efficient configuration?

- **A.** Enable EBS Default Encryption in the EC2 Regional settings.
- **B.** Create an AWS Lambda function triggered by `CreateVolume` events to delete unencrypted volumes.
- **C.** Run a nightly Python script on a cron server.
- **D.** Attach an S3 bucket policy denying unencrypted uploads.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **EBS Encryption by Default** is a simple regional toggle in the EC2 console/API. Once enabled, all newly created EBS volumes and snapshot copies in that region are automatically encrypted using the selected KMS key with zero custom scripting.
</details>
