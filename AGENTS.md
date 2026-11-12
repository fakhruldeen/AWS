# Agent Guidelines & Operational Rules for AWS Repository

> **Repository:** `fakhruldeen/AWS` (`/home/mohamed/Desktop/Work/aws`)  
> **Author & Trainer:** Mohamed Fakhruldeen  

---

## 🚨 Mandatory Architectural Rule: Vault vs. Work Repo Separation

Always maintain the strict separation between the **Obsidian Vault** and the **Work Directory**:

1. **Obsidian Vault (`/home/mohamed/Documents/Obsidian Vault/Brain/AWS`)**
   * **Role:** The comprehensive knowledge brain.
   * **Contents:** Full documentation, in-depth service guides, architectural deep dives, complete tutorials, and foundational knowledge. Zero duplication across certifications.

2. **Work Directory (`/home/mohamed/Desktop/Work/aws`)**
   * **Role:** The public training, delivery, and exam preparation workspace.
   * **Contents:**
     * `notes/`: High-yield exam prep notes, distinction tables ("X vs Y"), and cheat sheets.
     * `slides/`: Marp presentation slide decks for student delivery.
     * `labs/`: 100% Free-Tier / low-cost step-by-step hands-on student labs.
     * `syllabus/`: Official blueprints and course syllabi.
     * `questions_bank/`: Offline practice questions (**never publish online - gitignored**).
     * `sources/`: Reference textbooks (**never publish online - gitignored**).

---

## 🛠️ Operational Rules

1. **Verify Against Current AWS Documentation:** Always use `aws___search_documentation` and `aws___read_documentation` via the AWS MCP Server to verify latest service features, quotas, and APIs.
2. **Infrastructure as Code (IaC):** Prioritize AWS CDK, CloudFormation, or Terraform over one-off manual CLI changes.
3. **Secret Safety:** Never commit API keys, credentials, or plaintext secrets. Use AWS Secrets Manager dynamic references or IAM roles.
4. **Git Hygiene:** Keep `questions_bank/`, `sources/`, and temporary build artifacts excluded in `.gitignore`.
