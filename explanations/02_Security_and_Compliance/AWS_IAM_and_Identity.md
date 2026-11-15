# AWS Identity & Access Management (IAM) & Directory Services

> **Service Category:** Security, Identity & Compliance (Domain 2.3)  
> **Relevant Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], SAA-C03, DVA-C02, SOA-C02  
> **Tags:** `#aws/services` `#aws/security` `#aws/iam` `#clf-c02`

---

## 1. AWS IAM Core Concepts

**AWS Identity and Access Management (IAM)** is a web service that helps you securely control access to AWS resources. IAM is a **global service** (you do not select a region when configuring IAM).

```mermaid
graph TD
    IAM["AWS IAM Service (Global)"]
    
    IAM --> Root["1. Root User\nComplete unrestricted admin access\nLock away after setup!"]
    IAM --> Users["2. IAM Users\nIndividual human identity\n(e.g., Alice, Bob)"]
    IAM --> Groups["3. User Groups\nCollection of users with shared permissions\n(e.g., Developers, Admins)"]
    IAM --> Roles["4. IAM Roles\nTemporary credentials (STS)\nFor EC2, Lambda, or cross-account access"]
    IAM --> Policies["5. IAM Policies\nJSON permission documents\n(Allow / Deny statements)"]
```

---

## 2. Root User vs. IAM Users vs. IAM Roles

| Identity Type | Long-Lived vs. Temporary | Best Practice / When to Use |
|---|---|---|
| **AWS Account Root User** | Long-Lived (Email + Password) | **DO NOT USE FOR DAILY TASKS!** Only use to create your first administrative IAM user, change account settings, close the account, or change support plans. **Must have Multi-Factor Authentication (MFA) enabled!** |
| **IAM User** | Long-Lived (Password for Console, Access Keys for CLI/SDK) | Individual employees within an organization. Best practice is to assign permissions via **User Groups**, not directly to individual users. |
| **IAM Role** | **Temporary Credentials (via AWS STS)** | Used by AWS services (e.g., EC2 instance needing to access S3), applications, or users needing temporary cross-account access. **Eliminates hardcoded access keys!** |

---

## 3. The Principle of Least Privilege & JSON Policies

* **Principle of Least Privilege:** Grant only the minimum permissions required to perform a specific job, and nothing more.

```mermaid
flowchart LR
    subgraph JSONPolicy ["Structure of an IAM JSON Policy"]
        direction TB
        E["Effect: 'Allow' or 'Deny'"]
        P["Principal: Who is requesting access?"]
        A["Action: What API call? (e.g., 's3:GetObject')"]
        R["Resource: Which specific ARN? (e.g., 'arn:aws:s3:::my-bucket/*')"]
        C["Condition: Optional (e.g., require MFA or specific IP)"]
    end
```

### Complete IAM Policy Evaluation Logic:

```mermaid
flowchart TD
    Req([Incoming API Request]) --> DenyCheck{1. Is there an Explicit Deny anywhere?}
    DenyCheck -->|Yes| Denied([DENIED])
    
    DenyCheck -->|No| OrgSCP{2. Allowed by Organizations SCP?}
    OrgSCP -->|No / Denied| Denied
    
    OrgSCP -->|Yes| ResourcePolicy{3. Allowed by Resource-Based Policy?}
    ResourcePolicy -->|Yes - Principal in same account| Allowed([ALLOWED])
    
    ResourcePolicy -->|No| BoundaryCheck{4. Within IAM Permissions Boundary?}
    BoundaryCheck -->|No| Denied
    
    BoundaryCheck -->|Yes| SessionPolicy{5. Allowed by Session Policy?}
    SessionPolicy -->|No| Denied
    
    SessionPolicy -->|Yes| IdentityPolicy{6. Explicit Allow in Identity Policy?}
    IdentityPolicy -->|Yes| Allowed
    IdentityPolicy -->|No| ImplicitDeny([DENIED - Default Implicit Deny])
```

### IAM Policy Types Comparison:

| Policy Type | Attached To | Purpose & Characteristics | Can Grant Permissions? |
|:---|:---|:---|:---:|
| **Identity-Based Policy** | IAM Users, Groups, Roles | Grants permissions directly to AWS identities (AWS Managed or Customer Managed). | **YES** |
| **Resource-Based Policy** | S3 buckets, KMS keys, SQS queues | Attached directly to resources; specifies which principals can access the resource and under what conditions. | **YES** |
| **Permissions Boundary** | IAM Users, Roles | Sets the **maximum available permissions** an identity can ever be granted. Acts as a guardrail. | **NO** (Only restricts) |
| **Service Control Policy (SCP)** | AWS Organizations OUs / Accounts | Sets maximum allowable permissions across member accounts in an organization. Overrides even the root user! | **NO** (Only restricts) |
| **Session Policy** | Temporary STS sessions | Passed dynamically when assuming a role or federating to scope down session privileges. | **NO** (Only restricts) |

### IAM Role Assumption & Temporary Credentials Sequence:

```mermaid
sequenceDiagram
    autonumber
    actor App as Application / EC2 / Developer
    participant STS as AWS Security Token Service (STS)
    participant IAM as AWS IAM Service
    participant Target as Amazon S3 / DynamoDB
    
    App->>STS: 1. Call AssumeRole(RoleArn, SessionName)
    STS->>IAM: 2. Validate Trust Policy (Principal allowed to assume?)
    IAM-->>STS: 3. Trust Policy Verified
    STS-->>App: 4. Returns Temporary Security Credentials<br/>(AccessKeyId, SecretAccessKey, SessionToken, Expiration)
    App->>Target: 5. Access resource with temporary credentials
    Target-->>App: 6. Request Authorized & Completed
```

### Critical IAM Policy Evaluation Rules:
1. **Default Deny:** By default, all requests are denied.
2. **Explicit Allow:** An explicit Allow in any policy grants permission.
3. **Explicit Deny ALWAYS Trumps Allow:** If any policy contains an explicit `Deny`, the request is **DENIED**, even if ten other policies grant an explicit `Allow`!

---

## 4. Multi-Account Workforce: AWS IAM Identity Center

* **Formerly known as:** AWS Single Sign-On (AWS SSO).
* **What it is:** A centralized identity service that connects to your corporate Identity Provider (IdP) like Microsoft Entra ID (Azure AD), Okta, or Google Workspace.
* **Functionality:** Provides employees with a **single sign-on portal** to access multiple AWS accounts across an AWS Organization with predefined **Permission Sets**.

---

## 5. External Customers: Amazon Cognito

While IAM handles internal employees and AWS services, **Amazon Cognito** handles customer-facing mobile and web applications:

```mermaid
flowchart TD
    User["External Mobile / Web App User"]
    
    subgraph Cognito ["Amazon Cognito Architecture"]
        UP["1. Cognito User Pools (CUP)\nAuthentication Directory\n(Sign-up, sign-in, MFA, Social Login via Google/Apple)"]
        IP["2. Cognito Identity Pools (Federated Identities)\nAuthorization Engine\n(Exchanges user token for temporary AWS STS credentials)"]
    end
    
    subgraph Backend ["AWS Backend Services"]
        S3["Amazon S3 User Folder"]
        DDB["Amazon DynamoDB Table"]
    end
    
    User -->|"Sign in / Sign up"| UP
    UP -->|"JWT Token"| IP
    IP -->|"Temporary AWS Credentials (STS)"| User
    User -->|"Secure Direct Access"| S3
    User -->|"Secure Direct Access"| DDB
```

---

## 6. Enterprise Microsoft AD: AWS Directory Service

Enables your AWS resources to connect to and use Microsoft Active Directory:
1. **AWS Managed Microsoft AD:** A real Microsoft Windows Server Active Directory hosted in the AWS Cloud. Supports Group Policies (GPOs), Kerberos, and trusts to on-premises AD domains.
2. **AD Connector:** A directory gateway / proxy to redirect directory requests directly to your existing on-premises Microsoft Active Directory without caching credentials in AWS.
3. *Simple AD:* (Lifecycle Update: AWS closed Simple AD to new customers as of mid-2026, transitioning customers to Managed Microsoft AD or AD Connector).

---

## 7. Credential Management: Secrets Manager vs. Parameter Store

| Feature | AWS Secrets Manager | Systems Manager Parameter Store |
|---|---|---|
| **Primary Use Case** | Managing database credentials, API keys, OAuth tokens. | Managing configuration parameters (URLs, license keys, strings). |
| **Automatic Rotation** | **YES (Built-in automated rotation via Lambda)** for RDS, Aurora, DocumentDB. | No native automated rotation (requires custom scripting). |
| **Cross-Account Secret Access**| Supported natively. | Limited. |
| **Cost** | Paid per secret per month + API requests. | Standard parameters are **FREE**; Advanced tiers have small fee. |

---

## 8. IAM Governance & Audit Tools: Access Advisor, Access Analyzer & Credential Reports

AWS provides three built-in governance mechanisms to audit IAM permissions, identify over-privileged users, and enforce least privilege:

```mermaid
flowchart TD
    subgraph IAM_Audit ["IAM Governance & Least-Privilege Verification"]
        AA["1. IAM Access Advisor\n(Shows Service Permissions Granted vs. Last Accessed Date)\nPrunes unused permissions"]
        AZ["2. IAM Access Analyzer\n(Automated Mathematical Reasoning)\nIdentifies resources shared publicly or cross-account"]
        CR["3. IAM Credential Report\n(Account-wide CSV audit of passwords, MFA status & Access Key age)"]
    end

    Admin["Security Officer / Cloud Architect"] --> AA
    Admin --> AZ
    Admin --> CR
```

### 1. IAM Access Advisor (Service Last Accessed Data)
* **What it does:** Displays the timestamp of when each service was **last accessed** by an IAM user, group, role, or policy.
* **Why it matters:** If an engineer was granted permissions to 40 services 6 months ago, but Access Advisor shows they only ever call `ec2` and `s3`, the administrator can safely revoke the unused 38 service permissions without breaking workloads.
* **Granularity:** Reports service-level last accessed information down to specific actions for core services (e.g., S3, IAM, EC2).

### 2. IAM Access Analyzer
* **What it does:** Uses **automated reasoning** (mathematical logic proofs) to continuously analyze resource-based policies across your account or organization.
* **Resources Analyzed:** Amazon S3 bucket policies, AWS KMS key policies, Amazon SQS queue policies, AWS IAM role trust policies, AWS Secrets Manager secrets, and Amazon SNS topics.
* **Outcome:** Generates findings whenever a resource is shared with an external AWS account, an anonymous public user, or unauthorized internet principals.

### 3. IAM Credential Report
* **What it does:** Generates an account-level CSV file listing all users and the exact status of their credentials:
  - Password enabled/disabled, password last used, password last changed.
  - Active MFA status (Yes/No).
  - Access Key 1 and Access Key 2 active state, last used date, and rotation age.

---

## 9. Verified AWS CLI Commands for IAM & Identity

```bash
# 1. Get current caller identity (Who am I?)
aws sts get-caller-identity

# 2. Generate and retrieve an account Credential Report
aws iam generate-credential-report
aws iam get-credential-report --query "Content" --output text | base64 -d

# 3. Generate Service Last Accessed details (Access Advisor)
JOB_ID=$(aws iam generate-service-last-accessed-details \
    --arn "arn:aws:iam::123456789012:user/dev-operator" \
    --query "JobId" --output text)

aws iam get-service-last-accessed-details --job-id ${JOB_ID}

# 4. List external findings from IAM Access Analyzer
aws accessanalyzer list-findings \
    --analyzer-arn "arn:aws:access-analyzer:us-east-1:123456789012:analyzer/ConsoleAnalyzer"

# 5. List all active access keys for a user and check age
aws iam list-access-keys --user-name dev-operator

# 6. List attached policies on a role
aws iam list-attached-role-policies --role-name LambdaExecutionRole
```

---

## 10. Exam Tip Matrix

| Question Scenario | Correct Choice |
|---|---|
| *"Give an EC2 instance permission to read and write files to an Amazon S3 bucket without storing access keys on the instance"* | **Attach an IAM Role to the EC2 instance (Instance Profile)** |
| *"Best practice for securing the AWS account root user"* | **Enable Multi-Factor Authentication (MFA) and do not use for everyday tasks** |
| *"Centrally manage single sign-on access across multiple AWS accounts for corporate employees"* | **AWS IAM Identity Center** |
| *"Customer-facing mobile application requiring social sign-in (Google, Facebook, Apple) and access to S3"* | **Amazon Cognito** |
| *"Store database passwords and automatically rotate them every 30 days without application downtime"* | **AWS Secrets Manager** |
| *"An IAM policy has an explicit Allow for S3, but another policy attached to the user has an explicit Deny"* | **Access is DENIED (Explicit Deny always overrides Allow)** |
| *"Identify which IAM permissions granted to a user have never been used in the past 90 days so they can be removed"* | **IAM Access Advisor** (Service Last Accessed Data) |
| *"Identify which Amazon S3 buckets or KMS keys are accessible by external accounts or public internet users"* | **IAM Access Analyzer** |
| *"Generate a comprehensive audit of all IAM users in an account showing password age and whether MFA is enabled"* | **IAM Credential Report** |
