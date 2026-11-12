# AWS Agent Guidance & Operational Rules

> **Origin:** Official AWS Agent Toolkit (`aws/agent-toolkit-for-aws/rules/aws-agent-rules.md`)  
> **Target Scope:** Antigravity AI Assistant & Pair Programmer on AWS Architectures

---

## 1. Core Operating Principles

* **Prefer the AWS MCP Server for AWS interactions** — it provides sandboxed execution, observability, and audit logging. If unavailable or when performing read-only queries without credentials, use the proxy with `--skip-auth` or the AWS CLI directly.
* **Always verify against current documentation** — For any AWS task or question (building, configuring, migrating, debugging, or operating a service, writing SDK code, authoring CDK/CloudFormation, or answering how a service works), first call `aws___search_documentation` with topic `agent_skills` or documentation queries, and load the matching skill with `aws___retrieve_skill`. Do this even when confident: skills and docs carry current service behavior that static model weights may not.
* **When uncertain about specific AWS details** (API parameters, permissions, service quotas, error codes), verify against official AWS documentation rather than guessing. State uncertainty explicitly if it cannot be confirmed.
* **Infrastructure as Code (IaC):** When creating infrastructure, prefer Infrastructure as Code (AWS CDK, Terraform, or CloudFormation) over direct CLI commands.
* **Well-Architected Alignment:** Follow the 6 pillars of the AWS Well-Architected Framework (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability).
* **Naming Conventions:** Do not use em dashes in AWS resource names or descriptions; use standard hyphens (`-`) instead.

---

## 2. Evidence-Based Diagnostics & Verification

* **To say what a system currently does, read what the runtime uses:** The completed deployment, the alias or version that is invoked, or the active stack template. A newer stored draft or description field is not evidence of live behavior.
* **Present a cause as confirmed only if data, configuration, or logs show it:** Label anything else as unverified, and specify what should be checked next.
* **Read complete error payloads:** Before interpreting records showing failure (error log lines, failed executions, table items), inspect the full record rather than truncating messages prematurely.
* **Identify root inputs for missing values:** When an error states a value was undefined, null, or empty, trace the input or query result that supplied that value before concluding.
* **Confirm or rule out user-raised hypotheses:** When the user asks a specific question or names a suspected root cause, directly confirm or rule out each cause based on verified evidence.

---

## 3. Secret & Credential Safety

* **Never expose plaintext secrets in context:** For any task involving database passwords, API keys, or certificates, use AWS Secrets Manager dynamic references (e.g., `{{resolve:secretsmanager:secret-id:SecretString:json-key}}`) or IAM roles for service-to-service authentication.
* **Never commit secrets to Git repositories:** Ensure `.env`, credentials files, and private keys remain strictly excluded via `.gitignore`.
