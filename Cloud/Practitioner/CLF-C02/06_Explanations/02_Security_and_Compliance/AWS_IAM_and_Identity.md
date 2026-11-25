# AWS Identity & Access Management (IAM) & Directory Services

> **Service Category:** Security, Identity & Compliance (Domain 2.3)  
> **Relevant Certifications:** [CLF-C02](../../01_Syllabus/CLF-C02_Master_Blueprint.md), SAA-C03, DVA-C02, SOA-C02  
> **Tags:** `#aws/services` `#aws/security` `#aws/iam` `#clf-c02`

---

## 💡 The Real-World Analogy (ELI5)

> **Corporate Office Security System:**
> - **IAM User:** A permanent employee with a personalized employee ID badge, username, and password. Used by a real human for interactive daily work.
> - **IAM Group:** A department roster (e.g., Marketing, Accounting, DevOps). Adding an employee to the Accounting group automatically gives them physical keycard access to the accounting ledger room.
> - **IAM Role:** A temporary visitor pass or contractor keycard. It has no permanent password; anyone authorized can clip it on temporarily to perform a specific job (e.g., an electrician fixing wiring in the server room), and hand it back when finished. Used by EC2 instances, Lambda functions, or external federated users.
> - **IAM Policy:** The official written building regulation hanging on the wall. Written in standardized JSON syntax, it explicitly states: *"Persons holding Badge X are ALLOWED to enter Room Y between 9 AM and 5 PM, but are EXPLICITLY DENIED access to the Vault under all circumstances."*
> - **AWS Account Root User:** The building owner who holds the master deed, safe combination, and master keys. The owner locks their keys in a safe, enables a retina scanner (MFA), and only unlocks the safe during major financial reorganizations or legal emergencies.

---

## 1. First-Principles Computer Science & Identity Mechanics

Access management in distributed computing is governed by two distinct cryptographic concepts: **Authentication** and **Authorization**:

```mermaid
flowchart LR
    Principal["Principal (User / Service)"] -->|1. Authentication (AuthN)| Authn["Who are you?<br/>(Username/Password, Access Key, MFA Token)"]
    Authn -->|Identity Confirmed| Authz["2. Authorization (AuthZ)<br/>What are you allowed to do?<br/>(IAM Policy Evaluation Engine)"]
    Authz -->|Explicit Allow & No Explicit Deny| Resource["AWS Target Resource (e.g., S3 Bucket, EC2 Instance)"]
    Authz -->|Implicit or Explicit Deny| Denied["HTTP 403 Access Denied"]
```

### 1.1 Authentication (AuthN) vs. Authorization (AuthZ)
* **Authentication ($AuthN$):** Verifying the identity of the principal (human or machine). In AWS, this is verified using:
  - Console Password + Multi-Factor Authentication (MFA) virtual or hardware token.
  - Long-term API Access Keys (`aws_access_key_id` + `aws_secret_access_key`) for CLI/SDK.
  - Temporary session tokens issued by the **AWS Security Token Service (STS)**.
* **Authorization ($AuthZ$):** Determining the permissions granted to an authenticated identity. In AWS, authorization is computed dynamically at the exact millisecond an API request arrives, using mathematical Boolean evaluation of JSON policy documents.

### 1.2 Access Control Paradigms: RBAC vs. ABAC
* **Role-Based Access Control (RBAC):** Permissions are attached to static identities or roles (e.g., "Developers get S3 Read-Only"). As organizations scale to thousands of users, managing hundreds of static roles leads to "role explosion."
* **Attribute-Based Access Control (ABAC):** Permissions are granted dynamically based on metadata tags attached to users and resources (e.g., *"Allow access if `PrincipalTag:Department` == `ResourceTag:Department`"*). ABAC enables granular, scalable security guardrails with far fewer policies.

---

## 2. Historical IT Pain Points: The Enterprise Credential Crisis

Before modern centralized cloud identity platforms, identity and access management was notoriously insecure:

| Enterprise Identity Challenge | Traditional On-Premises Reality | [AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam) Cloud Identity Paradigm |
|---|---|---|
| **Shared "Root / Admin" Credentials** | Multiple system administrators shared the single root password written on sticky notes or saved in shared text files. An administrator leaving the company required changing passwords everywhere. | **Individual IAM Users & Federation**. Every human has a unique identity. Root account access is permanently locked behind hardware MFA and never used for daily work. |
| **Hardcoded API Keys in Source Code** | Developers embedded plaintext database passwords and access tokens directly into application source code, resulting in catastrophic credential leaks on public GitHub repositories. | **IAM Roles for Workloads**. Applications running on [Amazon EC2](../../AWS_SERVICES_GLOSSARY.md#amazon-ec2) or [AWS Lambda](../../AWS_SERVICES_GLOSSARY.md#aws-lambda) automatically retrieve temporary, self-rotating credentials via AWS STS. |
| **Orphaned User Accounts & Privilege Creep** | When employees changed roles or left the company, their individual server SSH keys and database logins lingered for months, leaving backdoor attack vectors. | **Centralized Single Sign-On (IAM Identity Center)**. Deactivating a user in corporate Active Directory/Okta instantly terminates access across all 100+ AWS accounts. |
| **Permission Bloat & Audit Guesswork** | Security teams had no visibility into whether a granted database privilege had actually been exercised in the past two years, making it impossible to enforce least privilege. | **IAM Access Advisor & Access Analyzer**. Automatically analyzes CloudTrail telemetry to identify unused permissions, enabling automated rightsizing. |

---

## 3. Deep-Dive: AWS IAM Architecture & Entities

[AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam) is a **global service** (identity configurations apply universally across all AWS Regions without regional configuration):

```mermaid
graph TD
    IAM["AWS IAM (Global Service)"]
    
    IAM --> Root["1. AWS Account Root User<br/>• Unrestricted access to everything<br/>• Used ONLY for initial setup & account closure<br/>• Must enforce MFA!"]
    IAM --> Users["2. IAM Users<br/>• Individual human employee<br/>• Long-term password + optional Access Keys<br/>• Best practice: Assign via Groups"]
    IAM --> Groups["3. IAM User Groups<br/>• Collection of users (e.g., Finance, DevOps)<br/>• Cannot be nested! (No groups within groups)"]
    IAM --> Roles["4. IAM Roles<br/>• Temporary credentials via AWS STS<br/>• Assigned to EC2, Lambda, or cross-account users<br/>• No permanent passwords or keys"]
    IAM --> Policies["5. IAM Policies<br/>• Formal JSON permission documents<br/>• Evaluates Effect, Action, Resource, Condition"]
```

### 3.1 The AWS Account Root User
* **Complete Omnipotence:** The root user is the identity established when the AWS account is first created (using an email address and password). It has unrestricted administrative access to all resources, billing, and services in the account.
* **Mandatory Best Practice:** 
  1. Lock away the root user credentials immediately after account creation.
  2. Enable Multi-Factor Authentication (MFA) using a virtual authenticator app or physical FIPS-validated hardware security key (YubiKey).
  3. Never use the root user for daily operational or administrative tasks.
  4. Create dedicated administrative IAM users or IAM Identity Center roles for daily operations.
* **Tasks Exclusively Requiring Root User Access:**
  - Closing an AWS account.
  - Modifying the AWS account name, root email, or root password.
  - Changing the AWS Support plan (e.g., upgrading from Developer to Business).
  - Registering as an AWS GovCloud seller.

### 3.2 IAM Users and User Groups
* **IAM Users:** Persistent digital identities representing a specific person or application service. An IAM user can have two credential types:
  - *Console Password:* For logging into the web-based AWS Management Console.
  - *Access Key Pair (`AccessKeyId` + `SecretAccessKey`):* For authenticating CLI, SDK, and programmatic API calls.
* **IAM User Groups:** Logical collections of IAM users. Permissions applied to a group automatically apply to all users within that group.
  - *Important Limitation:* **Groups cannot be nested** (a group cannot contain another group).

### 3.3 IAM Roles and Temporary Credentials (AWS STS)
* **What is an IAM Role?** An identity with specific permissions, but **no permanent credentials (no password, no long-term access keys)**.
* **AWS Security Token Service (STS):** When a principal assumes a role, AWS STS issues temporary security credentials (access key, secret key, and session token) valid from 15 minutes to 12 hours.
* **Primary Use Cases for IAM Roles:**
  1. *AWS Services (EC2 / Lambda):* An EC2 instance retrieves temporary credentials from the Instance Metadata Service (IMDSv2) via its attached IAM Role profile to read from [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3) without hardcoding keys.
  2. *Cross-Account Access:* Granting developers in Account A temporary administrative access to resources in Account B without creating duplicate user accounts.
  3. *Federated Identity:* Enabling corporate employees to log into AWS using their enterprise Active Directory or Google Workspace accounts.

---

## 4. Deep-Dive: IAM Policy Evaluation Logic & JSON Syntax

An IAM policy is a formal JSON document that defines authorization permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadOnlyForFinance",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::finance-reports-2026",
        "arn:aws:s3:::finance-reports-2026/*"
      ],
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

### 4.1 The 6 Critical Policy Evaluation Steps:

```mermaid
flowchart TD
    Req([Incoming AWS API Request]) --> Step1{1. Is there an Explicit Deny anywhere?}
    Step1 -->|Yes| Denied([DENIED - Explicit Deny Overrides All])
    
    Step1 -->|No| Step2{2. Allowed by Organizations SCP?}
    Step2 -->|No / Denied| Denied
    
    Step2 -->|Yes| Step3{3. Allowed by Resource Policy?}
    Step3 -->|Yes - In Same Account| Allowed([ALLOWED])
    
    Step3 -->|No| Step4{4. Within IAM Permissions Boundary?}
    Step4 -->|No| Denied
    
    Step4 -->|Yes| Step5{5. Allowed by Session Policy?}
    Step5 -->|No| Denied
    
    Step5 -->|Yes| Step6{6. Explicit Allow in Identity Policy?}
    Step6 -->|Yes| Allowed
    Step6 -->|No| ImplicitDeny([DENIED - Default Implicit Deny])
```

1. **Default Deny:** Every request starts with an **implicit deny** (zero access).
2. **Explicit Deny Trumps Everything:** If an explicit `Deny` exists in *any* policy (SCP, Identity Policy, Resource Policy, or Boundary), the request is immediately rejected.
3. **Explicit Allow Required:** Access is granted only if an explicit `Allow` statement matches the request and no explicit `Deny` is present.

---

## 5. Multi-Dimensional Identity Entity Comparison Matrix

| Identity Entity | Long-Lived vs. Temporary | Primary Credential Type | Best Suited For | Can Have Direct Login Password? | MFA Support |
|---|---|---|---|:---:|:---:|
| **Root User** | Long-Lived | Email + Complex Password | Initial account setup; account closure; billing changes | **YES** | **Mandatory** (Hardware/Virtual) |
| **IAM User** | Long-Lived | Password (Console) / Access Keys (CLI) | Legacy human employees; service accounts lacking role support | **YES** | **Recommended** |
| **IAM User Group** | Collection | N/A (Holds shared policies) | Grouping users by department (e.g., Marketing, Admins) | **NO** | N/A |
| **IAM Role** | **Temporary (STS)** | Ephemeral session token (15m–12h) | EC2 instances, Lambda functions, cross-account, federation | **NO** | Inherited from assuming identity |
| **IAM Identity Center** | Centralized SSO | Enterprise credentials (Okta, Azure AD, AD) | Modern multi-account enterprise single sign-on | **YES** (Via IdP portal) | **Enforced via IdP** |

---

## 6. Exam Traps & 'Clue-to-Answer' Decryption

| Question Scenario Keyword | Target Entity / Practice | Exam Trap & Distractor Explanation |
|---|---|---|
| *"Grant temporary credentials to an EC2 instance to access [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3)"* | **IAM Role** | Trap: Never store long-term access keys inside an EC2 instance or application code. Always use IAM Roles. |
| *"Securing AWS account root user after initial creation"* | **Enable MFA, lock away root, use IAM admin user** | Trap: The root user should NEVER be used for daily administrative work. |
| *"Granting only the permissions required to complete a specific task"* | **Principle of Least Privilege** | Trap: Avoid broad wildcard permissions (`*`). Start with implicit deny and grant minimal actions. |
| *"Audit list of all account users showing password age, MFA status, and access keys"* | **IAM Credential Report** | Trap: Do not choose IAM Access Advisor. Credential Report downloads as a CSV auditing all user account credentials. |
| *"Identify which IAM permissions have not been used in the past 90 days"* | **IAM Access Advisor** | Trap: Do not choose IAM Access Analyzer. Access Advisor analyzes "service last accessed" data to trim unused rights. |
| *"Identify S3 buckets or KMS keys accessible by external AWS accounts or public internet"* | **IAM Access Analyzer** | Trap: Access Analyzer uses automated mathematical reasoning to detect external resource sharing. |
| *"Centralized single sign-on across multiple AWS accounts in an organization"* | **IAM Identity Center (AWS SSO)** | Trap: Do not create separate IAM users in every account. Centralize access using IAM Identity Center. |

---

## 7. Post-Topic Question Simulation & Retention Check

### Question 1
**What is the AWS Well-Architected recommendation for managing the AWS account root user following initial account registration?**
- A) Generate permanent programmatic access keys and distribute them to the senior development leads
- B) Delete all root user access keys, enable Multi-Factor Authentication (MFA), and use IAM roles or administrative IAM users for daily operations
- C) Share the root user login password with trusted members of the IT management team
- D) Log in as the root user daily to inspect CloudWatch operational billing graphs

<details>
<summary><b>Click to View Answer & Detailed Distractor Analysis</b></summary>

**Correct Answer:** **B) Delete all root user access keys, enable Multi-Factor Authentication (MFA), and use IAM roles or administrative IAM users for daily operations**

* **Why it's correct:** The root user possesses unrestricted, non-revocable administrative access to all resources and financial billing across the account. AWS security best practices dictate deleting all root programmatic access keys, locking down the account with hardware or virtual MFA, and delegating daily administrative responsibilities to IAM Identity Center or dedicated administrative IAM users following least-privilege principles.
* **Distractor Analysis:**
  - *A is incorrect:* Generating permanent access keys for the root user creates an extreme security vulnerability; if leaked, an attacker gains complete control of the AWS account.
  - *C is incorrect:* Sharing root credentials violates basic corporate security compliance and destroys audit traceability (CloudTrail logs would not show which human took an action).
  - *D is incorrect:* Daily administrative tasks must never be performed using the root user; daily monitoring should be performed by IAM identities with scoped permissions.
</details>

---

### Question 2
**An application running on an [Amazon EC2](../../AWS_SERVICES_GLOSSARY.md#amazon-ec2) instance needs to securely read objects from an [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3) bucket. Which approach implements the principle of least privilege without hardcoding credentials?**
- A) Embed IAM user access keys and secret keys directly into the application's configuration file
- B) Store AWS programmatic access keys in a public GitHub code repository
- C) Attach an IAM Role with an [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3) read-only policy to the EC2 instance profile
- D) Configure the [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3) bucket policy to allow unrestricted public read access across the internet

<details>
<summary><b>Click to View Answer & Detailed Distractor Analysis</b></summary>

**Correct Answer:** **C) Attach an IAM Role with an [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3) read-only policy to the EC2 instance profile**

* **Why it's correct:** Attaching an IAM Role to an [Amazon EC2](../../AWS_SERVICES_GLOSSARY.md#amazon-ec2) instance profile allows the application to retrieve short-lived, automatically rotated temporary security credentials from the AWS Security Token Service (STS) via the Instance Metadata Service (IMDSv2), eliminating the need to store long-term access keys.
* **Distractor Analysis:**
  - *A is incorrect:* Hardcoding long-term access keys into application files creates severe risk of accidental disclosure and requires manual rotation if compromised.
  - *B is incorrect:* Exposing access keys in a public repository allows unauthorized malicious actors to compromise and hijack the AWS account within seconds.
  - *D is incorrect:* Making the S3 bucket publicly readable exposes confidential corporate data to the entire public internet, violating security compliance.
</details>

---

### Question 3
**Which fundamental security principle dictates that users, applications, and systems should only be granted the minimum permissions necessary to complete their specific business functions?**
- A) Separation of duties
- B) Principle of Least Privilege
- C) Defense-in-depth
- D) Zero-trust perimeter

<details>
<summary><b>Click to View Answer & Detailed Distractor Analysis</b></summary>

**Correct Answer:** **B) Principle of Least Privilege**

* **Why it's correct:** The Principle of Least Privilege is the foundational security rule of [AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam). It mandates starting with zero access (implicit deny) and granting only the specific API actions, resource ARNs, and conditions strictly required to perform the intended job role.
* **Distractor Analysis:**
  - *A is incorrect:* Separation of duties is an operational control ensuring that critical workflows require multiple people to complete (e.g., one person requests a database change, another approves it).
  - *C is incorrect:* Defense-in-depth is an architectural strategy that implements multiple layered defensive barriers (WAF, VPC security groups, encryption, IAM) across the entire stack.
  - *D is incorrect:* Zero-trust perimeter is a modern architectural philosophy requiring continuous verification of all identities regardless of network location.
</details>

---

### Question 4
**An enterprise operates 75 AWS accounts under [AWS Organizations](../../AWS_SERVICES_GLOSSARY.md#aws-organizations). Which service provides a single central portal for workforce employees to sign in with their corporate credentials and access their assigned accounts and business applications?**
- A) [AWS IAM Identity Center](../../AWS_SERVICES_GLOSSARY.md#aws-iam-identity-center) (AWS Single Sign-On)
- B) [AWS Secrets Manager](../../AWS_SERVICES_GLOSSARY.md#aws-secrets-manager)
- C) [Amazon GuardDuty](../../AWS_SERVICES_GLOSSARY.md#amazon-guardduty)
- D) [AWS Shield](../../AWS_SERVICES_GLOSSARY.md#aws-shield) Advanced

<details>
<summary><b>Click to View Answer & Detailed Distractor Analysis</b></summary>

**Correct Answer:** **A) [AWS IAM Identity Center](../../AWS_SERVICES_GLOSSARY.md#aws-iam-identity-center) (AWS Single Sign-On)**

* **Why it's correct:** [AWS IAM Identity Center](../../AWS_SERVICES_GLOSSARY.md#aws-iam-identity-center) (successor to AWS Single Sign-On) centralizes workforce authentication and authorization across multiple AWS accounts, integrating with corporate identity providers (such as Microsoft Entra ID, Okta, or Active Directory) and providing a unified single sign-on user portal.
* **Distractor Analysis:**
  - *B is incorrect:* [AWS Secrets Manager](../../AWS_SERVICES_GLOSSARY.md#aws-secrets-manager) stores, retrieves, and automatically rotates database passwords and API tokens, not workforce employee identities.
  - *C is incorrect:* [Amazon GuardDuty](../../AWS_SERVICES_GLOSSARY.md#amazon-guardduty) is an intelligent threat detection service that analyzes network telemetry and API logs for malicious activity.
  - *D is incorrect:* [AWS Shield](../../AWS_SERVICES_GLOSSARY.md#aws-shield) Advanced is an enterprise Distributed Denial of Service (DDoS) mitigation and protection service.
</details>

---

### Question 5
**What is the evaluation outcome in [AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam) when an attached user identity policy explicitly contains an `Allow` statement for `s3:PutObject`, but the target [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3) bucket policy contains an explicit `Deny` statement for that user?**
- A) Access is Allowed, because identity-based policies always override resource-based policies
- B) Access is Denied, because an explicit Deny statement in any applicable policy always overrides an Allow
- C) The user is prompted to submit a multi-factor authentication (MFA) code before proceeding
- D) Access is Allowed with restricted read-only permissions

<details>
<summary><b>Click to View Answer & Detailed Distractor Analysis</b></summary>

**Correct Answer:** **B) Access is Denied, because an explicit Deny statement in any applicable policy always overrides an Allow**

* **Why it's correct:** In the [AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam) policy evaluation engine, an **explicit Deny** statement in *any* applicable policy (whether a Service Control Policy, Permissions Boundary, Identity Policy, or Resource Policy) permanently overrides all Allow statements, resulting in an immediate HTTP 403 Access Denied.
* **Distractor Analysis:**
  - *A is incorrect:* Identity policies do not override resource policies; both are evaluated together, and any explicit Deny immediately blocks the request.
  - *C is incorrect:* IAM policy evaluation does not dynamically prompt for MFA at the evaluation stage unless an explicit MFA condition is configured in an Allow policy.
  - *D is incorrect:* If `s3:PutObject` is denied, the write operation completely fails; it does not partially degrade to read-only access.
</details>

---

## 🧠 Master MCQ Solving Blueprint: Pattern Decryption & Elimination Tricks

> *This blueprint distills recurring patterns, keyword triggers, and trap options extracted from over 450 questions on [AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam), Identity Center, and Access Governance across the official CLF-C02 question bank.*

### 1. The "Clue-to-Service" Linguistic Decryption Matrix
When reading a question scenario, search for these exact phrasing triggers:

| If You See This Trigger Phrase in the Question Stem... | The Correct Identity Concept / Tool Is... | Trap Distractor to Immediately Discard |
|---|---|---|
| *"Grant permissions to an EC2 instance or Lambda function without hardcoding access keys"* | **IAM Role** | *IAM User* (Never put permanent access keys on EC2!) |
| *"Grant only the permissions required to perform a specific job, and nothing more"* | **Principle of Least Privilege** | *Separation of Duties* or *Defense-in-Depth* |
| *"Centralized single sign-on (SSO) across multiple AWS accounts with corporate Active Directory"* | **[AWS IAM Identity Center](../../AWS_SERVICES_GLOSSARY.md#aws-iam-identity-center)** | *[Amazon Cognito](../../AWS_SERVICES_GLOSSARY.md#amazon-cognito)* (Cognito is for customer-facing web/mobile apps) |
| *"Download a CSV report listing all account users, password age, and MFA status"* | **IAM Credential Report** | *IAM Access Advisor* or *[AWS CloudTrail](../../AWS_SERVICES_GLOSSARY.md#aws-cloudtrail)* |
| *"Identify unused permissions to reduce excess access privileges based on activity history"* | **IAM Access Advisor** | *IAM Credential Report* |
| *"Mathematically analyze S3 bucket or KMS policies to identify unintended external public sharing"* | **IAM Access Analyzer** | *[Amazon Inspector](../../AWS_SERVICES_GLOSSARY.md#amazon-inspector)* |
| *"Root user initial setup and security best practices"* | **Lock away root, enable MFA, delete root access keys, create admin IAM identity** | *Generate root access keys for automation* |
| *"An IAM policy has an Explicit Allow and an Explicit Deny for the same action"* | **Access is DENIED (Explicit Deny ALWAYS wins)** | *Access is Allowed* or *MFA prompt* |
| *"Enforce organization-wide maximum permission guardrails across all member accounts"* | **Service Control Policies (SCPs)** | *IAM Identity Policies* |

### 2. The 3-Step Rapid Elimination Heuristic
When evaluating an IAM question:
1. **Step 1: Check the Entity Type (User vs. Group vs. Role vs. Root):**
   - Is it a **human employee** logging into the AWS Console? → **IAM User** (or **IAM Identity Center**).
   - Is it a **team of humans** sharing identical job functions? → **IAM Group**.
   - Is it an **AWS service (EC2, Lambda)** or **external federated user**? → **IAM Role** (Uses STS temporary credentials).
   - Is it **account billing, changing support plans, or closing the account**? → **Root User** only!
2. **Step 2: Check Policy Logic:**
   - Starts with: **Implicit Deny** (No access).
   - If an **Explicit Allow** exists: Access granted, **UNLESS**...
   - An **Explicit Deny** exists anywhere: Immediate **DENY** (Overrules everything!).
3. **Step 3: Differentiate IAM Auditing Tools:**
   - Need a **CSV spreadsheet of passwords & MFA**? → **IAM Credential Report**.
   - Need to see **which permissions a user has NOT used in 90 days**? → **IAM Access Advisor**.
   - Need to detect if an **S3 bucket is exposed to the public internet**? → **IAM Access Analyzer**.

### 3. High-Frequency Decoy Autopsy: Why AWS Tries to Trick You
* **Decoy #1: "IAM Role" vs. "IAM User Access Keys" for EC2 Instances**
  - *The Trap:* A Python script running on EC2 needs to upload files to [Amazon S3](../../AWS_SERVICES_GLOSSARY.md#amazon-s3). How should credentials be supplied?
  - *The Autopsy:* AWS tests this incessantly. Options will suggest storing access keys in a config file, environment variable, or S3. The ONLY well-architected answer is an **IAM Role attached to the EC2 Instance Profile**.
* **Decoy #2: "IAM Identity Center" vs. "[Amazon Cognito](../../AWS_SERVICES_GLOSSARY.md#amazon-cognito)"**
  - *The Trap:* A company needs single sign-on for their application users vs. corporate employees.
  - *The Autopsy:* If the users are **internal corporate employees** accessing AWS management accounts → **IAM Identity Center**. If the users are **external public consumers** signing into a custom mobile/web app via Google or Apple → **[Amazon Cognito](../../AWS_SERVICES_GLOSSARY.md#amazon-cognito)**.
* **Decoy #3: "IAM Groups as Policy Principals"**
  - *The Trap:* Asking whether an IAM policy can define an IAM Group as the "Principal".
  - *The Autopsy:* In [AWS IAM](../../AWS_SERVICES_GLOSSARY.md#aws-iam), an IAM Group is strictly a management container for users. A group **cannot** be listed as a Principal in a resource-based policy, and cannot be assumed like a role!

### 4. 10-Second Visual Decision Flowchart

```mermaid
flowchart TD
    Start["What is the IAM scenario?"] --> Target{"Who or what needs access?"}
    
    Target -->|"AWS Service (EC2, Lambda) or Container"| Role["✅ IAM Role (Temporary STS Credentials)"]
    Target -->|"Human Employee (Console/CLI)"| Human{"Single Account or Multi-Account SSO?"}
    Human -->|"Single AWS Account"| User["✅ IAM User (with MFA & Group)"]
    Human -->|"Enterprise Multi-Account & Active Directory"| IdC["✅ AWS IAM Identity Center"]
    Target -->|"External Mobile/Web App End Users"| Cog["✅ Amazon Cognito"]
    Target -->|"Account Ownership & Closing Account"| Root["✅ Root User (MFA Protected)"]
    
    Start --> Audit{"What is being audited?"}
    Audit -->|"Passwords, Key Age, MFA in CSV"| CredRep["✅ IAM Credential Report"]
    Audit -->|"Unused service permissions"| AccAdv["✅ IAM Access Advisor"]
    Audit -->|"Public/external resource exposure"| AccAnlz["✅ IAM Access Analyzer"]
```
