#!/usr/bin/env python3
"""
reorganize_to_option_a.py

Reorganizes the entire repository into clean, student-friendly Option A:
  00_START_HERE.md
  01_Syllabus
  02_Prerequisites
  03_Lectures
  04_Slides
  05_Diagrams
  06_Explanations
  07_Hands_On_Labs
  08_Tutorials
  09_Notes_and_Cheatsheets
  10_Knowledge_Checks
  11_Practice_Exams
  12_Sources

Updates all internal links across markdown, code, and scripts.
Generates comprehensive 00_START_HERE.md guides for every track.
"""

import os
import re
import subprocess
from pathlib import Path

WORK_DIR = Path("/home/mohamed/Desktop/Work/aws")

TRACKS = [
    WORK_DIR / "Cloud/Practitioner/CLF-C02",
    WORK_DIR / "Cloud/Associate/SAA-C03",
    WORK_DIR / "AI/Practitioner/AIF-C01",
    WORK_DIR / "AI/Associate/MLA-C01"
]

MAPPING = [
    ("01_Syllabus", "01_Syllabus"),
    ("02_Prerequisites", "02_Prerequisites"),
    ("03_Lectures", "03_Lectures"),
    ("04_Slides", "04_Slides"),
    ("05_Diagrams", "05_Diagrams"),
    ("06_Explanations", "06_Explanations"),
    ("07_Hands_On_Labs", "07_Hands_On_Labs"),
    ("08_Tutorials", "08_Tutorials"),
    ("09_Notes_and_Cheatsheets", "09_Notes_and_Cheatsheets"),
    ("10_Knowledge_Checks", "10_Knowledge_Checks"),
    ("11_Practice_Exams", "11_Practice_Exams"),
    ("12_Sources", "12_Sources"),
]

def rename_directories():
    print("--- 1. Renaming Directories to Option A Schema ---")
    for track in TRACKS:
        print(f"Processing track: {track.relative_to(WORK_DIR)}")
        for old_name, new_name in MAPPING:
            old_path = track / old_name
            new_path = track / new_name
            if old_path.exists():
                res = subprocess.run(["git", "mv", str(old_path), str(new_path)], cwd=WORK_DIR, capture_output=True, text=True)
                if res.returncode != 0:
                    # Fallback to os.rename if git mv fails (e.g. untracked or gitignored files)
                    os.rename(old_path, new_path)
                print(f"  Renamed: {old_name} -> {new_name}")

def update_internal_links():
    print("\n--- 2. Updating Internal Links Across All Files ---")
    extensions = {".md", ".py", ".sh", ".json", ".txt"}
    modified_count = 0

    for root, dirs, files in os.walk(WORK_DIR):
        # Skip git and graphify-out
        if ".git" in root or "graphify-out" in root:
            continue
        for file in files:
            ext = Path(file).suffix
            if ext in extensions:
                file_path = Path(root) / file
                try:
                    content = file_path.read_text(encoding="utf-8")
                except Exception:
                    continue

                new_content = content
                for old_name, new_name in MAPPING:
                    if old_name in new_content:
                        new_content = new_content.replace(old_name, new_name)

                if new_content != content:
                    file_path.write_text(new_content, encoding="utf-8")
                    modified_count += 1

    print(f"Updated links in {modified_count} files across workspace.")

def create_start_here_guides():
    print("\n--- 3. Creating 00_START_HERE.md Dashboards ---")

    # 1. CLF-C02
    clf_start = """# 🚀 AWS Certified Cloud Practitioner (CLF-C02) — Student Study Dashboard

> **Target Exam:** AWS Certified Cloud Practitioner (`CLF-C02`)  
> **Passing Score:** `700 / 1000` (Scaled Scoring)  
> **Exam Format:** 65 Questions | 90 Minutes  
> **Course Mission:** Zero-to-Certified in 1 to 2 Weeks with high-yield concepts, hands-on labs, and verified question drills.

---

## 🧭 Your Study Roadmap: The 3-Step Daily Routine

Follow this cycle every day for rapid, stress-free retention:

```mermaid
flowchart LR
    Learn["Step 1: Learn (20m)<br/>03_Lectures/"] --> Review["Step 2: Review (10m)<br/>09_Notes_and_Cheatsheets/"]
    Review --> Drill["Step 3: Drill (15m)<br/>scripts/aws_revision_runner.py"]
```

---

## ⚡ Fast-Track 7-Day Study Timetable

| Day | Focus Area | 📖 Study Materials | 💻 Practice Command |
|:---:|:---|:---|:---|
| **Day 1** | **Cloud Concepts & Global Infra** (Domain 1 - 24%) | [Lecture 01](./03_Lectures/Lecture_01_Introduction_to_Cloud_and_Global_Infra.md)<br>[Rapid Review](./09_Notes_and_Cheatsheets/Rapid_Review_Cheatsheet.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 1 -n 15 --tricks` |
| **Day 2** | **Compute: EC2, Lambda, Fargate** (Domain 3 - 34%) | [Lecture 02](./03_Lectures/Lecture_02_Compute_Virtualization_and_Containers.md)<br>[Lab 03: EC2 Bootstrap](./07_Hands_On_Labs/lab_03_ec2_compute_bootstrap.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 3 -n 15 --tricks` |
| **Day 3** | **Storage & Databases: S3, EBS, RDS, DynamoDB** | [Lecture 03](./03_Lectures/Lecture_03_Storage_and_Database_Architectures.md)<br>[S3 Cheatsheet](./09_Notes_and_Cheatsheets/distinctions/S3_Storage_Classes_Comparison.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 3 -n 20 --tricks` |
| **Day 4** | **Networking & Security Perimeter: VPC, Route 53, WAF** | [Lecture 04](./03_Lectures/Lecture_04_Networking_Perimeter_Security_and_Identity.md)<br>[SGs vs NACLs](./09_Notes_and_Cheatsheets/distinctions/Security_Groups_vs_NACLs_Comparison.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 2 -n 15 --tricks` |
| **Day 5** | **Identity, KMS, Governance & Artifact** (Domain 2 - 30%) | [Lecture 05](./03_Lectures/Lecture_05_Observability_Auditing_and_Governance.md)<br>[Lab 01: IAM MFA](./07_Hands_On_Labs/fast_track/Lab_01_AWS_IAM_Least_Privilege_and_MFA.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 2 -n 20 --tricks` |
| **Day 6** | **Billing, Pricing Models & Support Plans** (Domain 4 - 12%) | [Lecture 06](./03_Lectures/Lecture_06_Billing_FinOps_and_Exam_Strategy.md)<br>[Support Plans Table](./09_Notes_and_Cheatsheets/distinctions/AWS_Support_Plans_Comparison.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode practice --domain 4 -n 15 --tricks` |
| **Day 7** | **Final Timed Mock & Weakness Elimination** | [Exam Decryption Playbook](./09_Notes_and_Cheatsheets/Exam_Decryption_Playbook_and_Mnemonics.md) | `python3 scripts/aws_revision_runner.py --cert CLF --mode mock`<br>`python3 scripts/aws_revision_runner.py --cert CLF --mode weakness` |

---

## 🎯 Progress Checklist

Track your completion by checking off each module as you study:

- [ ] **Module 1 (Cloud Concepts):** Read Lecture 01 & Drill 15 Domain 1 Questions
- [ ] **Module 2 (Compute Services):** Read Lecture 02 & Complete Lab 03 (EC2)
- [ ] **Module 3 (Storage & DBs):** Read Lecture 03 & Review S3 Storage Classes
- [ ] **Module 4 (Networking & VPC):** Read Lecture 04 & Review Security Groups vs NACLs
- [ ] **Module 5 (Security & Identity):** Read Lecture 05 & Complete Lab 01 (IAM & MFA)
- [ ] **Module 6 (Billing & Support):** Read Lecture 06 & Review Support Plan SLAs
- [ ] **Authentic Practice Pool:** Completed 25 questions from the November 2026 Release (`--release-2026`)
- [ ] **Mock Simulation:** Scored $\ge 85\%$ on the 65-question timed mock exam (`--mode mock`)

---

## 📂 Clean Directory Quick-Index

| Directory | What You Will Find | Best For |
|:---|:---|:---|
| **[`01_Syllabus/`](./01_Syllabus/)** | Official exam blueprint, scoring rubric, domain weightings | Exam alignment & requirements |
| **[`02_Prerequisites/`](./02_Prerequisites/)** | Foundational computer science, networking & virtualization | Refreshing foundational basics |
| **[`03_Lectures/`](./03_Lectures/)** | 6 Classroom lesson plans with embedded practice scenarios | **Core daily study (Start Here!)** |
| **[`04_Slides/`](./04_Slides/)** | Presentation slides in Marp format | Quick visual overview |
| **[`05_Diagrams/`](./05_Diagrams/)** | Standalone production Mermaid architecture blueprints | Visual architecture mental models |
| **[`06_Explanations/`](./06_Explanations/)** | In-depth service and framework guides across all domains | Deep reference & concept clarification |
| **[`07_Hands_On_Labs/`](./07_Hands_On_Labs/)** | 14 Guided Free-Tier labs with real console screenshots & CLI runbooks | Building practical muscle memory |
| **[`08_Tutorials/`](./08_Tutorials/)** | 7 End-to-end multi-service production architectural builds | Understanding how services connect |
| **[`09_Notes_and_Cheatsheets/`](./09_Notes_and_Cheatsheets/)** | High-yield distinction tables ("X vs Y"), mnemonics & exam traps | Quick review & cramming |
| **[`10_Knowledge_Checks/`](./10_Knowledge_Checks/)** | Rapid diagnostic retention quizzes per domain | Checking retention after each lecture |
| **[`11_Practice_Exams/`](./11_Practice_Exams/)** | 2,716 Canonical Questions, 718Q Community Pool, 393Q Nov 2026 Release | Final exam drills & full simulations |
"""
    (WORK_DIR / "Cloud/Practitioner/CLF-C02/00_START_HERE.md").write_text(clf_start, encoding="utf-8")
    print("  Created: Cloud/Practitioner/CLF-C02/00_START_HERE.md")

    # 2. SAA-C03
    saa_start = """# 🏛️ AWS Certified Solutions Architect - Associate (SAA-C03) — Student Dashboard

> **Target Exam:** AWS Certified Solutions Architect - Associate (`SAA-C03`)  
> **Passing Score:** `720 / 1000` (Scaled Scoring)  
> **Exam Format:** 65 Scenario Questions | 130 Minutes  
> **Course Mission:** Enterprise-grade distributed systems design covering Security, Resilience, Performance, and Cost Optimization.

---

## 🧭 Your Study Roadmap

```mermaid
flowchart LR
    Syllabus["01_Syllabus/"] --> Lectures["03_Lectures/"]
    Lectures --> Labs["07_Hands_On_Labs/"]
    Labs --> Cheatsheets["09_Notes_and_Cheatsheets/"]
    Cheatsheets --> Exams["11_Practice_Exams/"]
```

---

## ⚡ Recommended 4-Week Study Schedule

| Week | Focus Area | 📖 Study Materials | 💻 Practice Command |
|:---:|:---|:---|:---|
| **Week 1** | **Domain 1: Design Secure Architectures (30%)** | [Lecture 01](./03_Lectures/Lecture_01_Designing_Secure_AWS_Architectures.md)<br>[Lab 01: Multi-Tier Resilient VPC](./07_Hands_On_Labs/lab_01_multi_tier_resilient_vpc_architecture.md) | `python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 1 -n 20 --tricks` |
| **Week 2** | **Domain 2: Design Resilient Architectures (26%)** | [Lecture 02](./03_Lectures/Lecture_02_Designing_Resilient_and_High_Availability_Systems.md)<br>[Lab 02: Scalable ASG & ALB](./07_Hands_On_Labs/lab_02_ha_scalable_web_tier_asg_alb.md)<br>[Lab 03: Fault-Tolerant Aurora](./07_Hands_On_Labs/lab_03_aurora_fault_tolerant_relational_database.md) | `python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 2 -n 20 --tricks` |
| **Week 3** | **Domain 3: High-Performing Architectures (24%)** | [Lecture 03](./03_Lectures/Lecture_03_High_Performance_Storage_Compute_and_Databases.md)<br>[Lab 04: Decoupled SQS/SNS](./07_Hands_On_Labs/lab_04_decoupled_asynchronous_microservices_sqs_sns.md) | `python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 3 -n 20 --tricks` |
| **Week 4** | **Domain 4: Cost-Optimized & Timed Mocks (20%)** | [Lecture 04](./03_Lectures/Lecture_04_Cost_Optimization_FinOps_and_Exam_Strategy.md)<br>[Storage Decision Matrix](./09_Notes_and_Cheatsheets/Storage_Architecture_Decision_Matrix.md) | `python3 scripts/aws_revision_runner.py --cert SAA --community --mode practice -n 25`<br>`python3 scripts/aws_revision_runner.py --cert SAA --mode mock` |

---

## 🎯 Progress Checklist

- [ ] **Domain 1 (Security):** Completed Lecture 01 & Lab 01 (VPC)
- [ ] **Domain 2 (Resilience):** Completed Lecture 02, Lab 02 (ASG/ALB) & Lab 03 (Aurora)
- [ ] **Domain 3 (Performance):** Completed Lecture 03 & Lab 04 (SQS/SNS Decoupling)
- [ ] **Domain 4 (Cost Optimization):** Completed Lecture 04 & Storage/DB Decision Matrices
- [ ] **1,019Q Community Pool:** Drilled 100+ questions with `--community`
- [ ] **Full Timed Mock Simulation:** Scored $\ge 80\%$ on the 65-question timed mock exam (`--mode mock`)
"""
    (WORK_DIR / "Cloud/Associate/SAA-C03/00_START_HERE.md").write_text(saa_start, encoding="utf-8")
    print("  Created: Cloud/Associate/SAA-C03/00_START_HERE.md")

    # 3. AIF-C01
    aif_start = """# 🤖 AWS Certified AI Practitioner (AIF-C01) — Student Dashboard

> **Target Exam:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Passing Score:** `700 / 1000` (Scaled Scoring)  
> **Exam Format:** 65 Questions | 90 Minutes  
> **Course Mission:** Master Artificial Intelligence, Machine Learning lifecycles, Generative AI architecture, Amazon Bedrock, Prompt Engineering, and Responsible AI Governance.

---

## 🧭 Your Study Roadmap

```mermaid
flowchart LR
    Lectures["03_Lectures/"] --> Labs["07_Hands_On_Labs/"]
    Labs --> Cheatsheets["09_Notes_and_Cheatsheets/"]
    Cheatsheets --> Drills["11_Practice_Exams/"]
```

---

## ⚡ Recommended 10-Day Study Schedule

| Day | Focus Area | 📖 Study Materials | 💻 Practice Command |
|:---:|:---|:---|:---|
| **Day 1-2** | **Domain 1: Fundamentals of AI & ML (20%)** | [Lecture 01](./03_Lectures/Lecture_01_AI_ML_Fundamentals_and_Terminology.md) | `python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 1 -n 15 --tricks` |
| **Day 3-4** | **Domain 2: Generative AI Fundamentals (24%)** | [Lecture 02](./03_Lectures/Lecture_02_Generative_AI_and_Foundation_Models.md)<br>[Lab 01: Prompt Engineering](./07_Hands_On_Labs/Lab_01_Amazon_Bedrock_Playground_and_Prompt_Engineering.md) | `python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 2 -n 15 --tricks` |
| **Day 5-6** | **Domain 3: Applications of FMs (28%)** | [Lecture 03](./03_Lectures/Lecture_03_Applications_of_Foundation_Models_and_Bedrock.md)<br>[Lab 02: Bedrock RAG KB](./07_Hands_On_Labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md) | `python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 3 -n 20 --tricks` |
| **Day 7-8** | **Domain 4 & 5: Responsible AI & Security (28%)** | [Lecture 04](./03_Lectures/Lecture_04_Responsible_AI_Guidelines.md)<br>[Lab 03: Bedrock Guardrails](./07_Hands_On_Labs/Lab_03_Responsible_AI_Bedrock_Guardrails.md) | `python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 4 -n 15 --tricks`<br>`python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 5 -n 15 --tricks` |
| **Day 9-10**| **233Q Community Pool & Timed Mocks** | [Prompt Engineering Guide](./09_Notes_and_Cheatsheets/02_Prompt_Engineering_Guide.md) | `python3 scripts/aws_revision_runner.py --cert AIF --community --mode practice -n 25`<br>`python3 scripts/aws_revision_runner.py --cert AIF --mode mock` |

---

## 🎯 Progress Checklist

- [ ] **Domain 1:** Mastered Supervised vs Unsupervised vs Reinforcement learning
- [ ] **Domain 2:** Completed Lab 01 (Bedrock Playgrounds, Temperature, Top-P, Prompting)
- [ ] **Domain 3:** Completed Lab 02 (Building RAG with Bedrock Knowledge Bases & OpenSearch)
- [ ] **Domain 4:** Completed Lab 03 (Responsible AI, PII Redaction, Bedrock Guardrails)
- [ ] **Domain 5:** Mastered Bedrock Data Privacy, Encryption with KMS, and PrivateLink
- [ ] **233-Question Community Pool:** Drilled 50+ questions with `--community`
- [ ] **Full Timed Mock Simulation:** Scored $\ge 85\%$ on the 65-question timed mock exam (`--mode mock`)
"""
    (WORK_DIR / "AI/Practitioner/AIF-C01/00_START_HERE.md").write_text(aif_start, encoding="utf-8")
    print("  Created: AI/Practitioner/AIF-C01/00_START_HERE.md")

    # 4. MLA-C01
    mla_start = """# 🧠 AWS Certified Machine Learning Engineer - Associate (MLA-C01) — Student Dashboard

> **Target Exam:** AWS Certified Machine Learning Engineer - Associate (`MLA-C01`)  
> **Passing Score:** `720 / 1000` (Scaled Scoring)  
> **Exam Format:** 65 Scenario Questions | 130 Minutes  
> **Course Mission:** Master production MLOps, SageMaker Pipelines, Model Registry, Inference Hosting, PEFT/LoRA Fine-Tuning, and Drift Monitoring.

---

## 🧭 Your Study Roadmap

```mermaid
flowchart LR
    Lectures["03_Lectures/"] --> Labs["07_Hands_On_Labs/"]
    Labs --> Cheatsheets["09_Notes_and_Cheatsheets/"]
    Cheatsheets --> Exams["11_Practice_Exams/"]
```

---

## ⚡ Recommended 4-Week Study Schedule

| Week | Focus Area | 📖 Study Materials | 💻 Practice Command |
|:---:|:---|:---|:---|
| **Week 1** | **Domain 1: Data Preparation for ML (28%)** | [Lecture 01](./03_Lectures/Lecture_01_Data_Preparation_and_Feature_Engineering.md) | `python3 scripts/aws_revision_runner.py --cert MLA --mode practice --domain 1 -n 20 --tricks` |
| **Week 2** | **Domain 2: ML Model Development & PEFT (26%)** | [Lecture 02](./03_Lectures/Lecture_02_Model_Development_and_PEFT_Adaptation.md)<br>[Lab 04: PEFT/LoRA Fine-Tuning](./07_Hands_On_Labs/lab_04_peft_lora_fine_tuning_foundation_models.md) | `python3 scripts/aws_revision_runner.py --cert MLA --mode practice --domain 2 -n 20 --tricks` |
| **Week 3** | **Domain 3: Deployment & Orchestration (22%)** | [Lecture 03](./03_Lectures/Lecture_03_Inference_Hosting_and_MLOps_Pipelines.md)<br>[Lab 01: SageMaker Pipelines](./07_Hands_On_Labs/lab_01_sagemaker_pipelines_mlops_and_model_registry.md)<br>[Lab 02: Inference Types](./07_Hands_On_Labs/lab_02_sagemaker_inference_endpoints_comparison.md) | `python3 scripts/aws_revision_runner.py --cert MLA --mode practice --domain 3 -n 20 --tricks` |
| **Week 4** | **Domain 4: Monitoring, Drift & Governance (24%)** | [Lecture 04](./03_Lectures/Lecture_04_Monitoring_Explainability_and_Governance.md)<br>[Lab 03: Model Monitor](./07_Hands_On_Labs/lab_03_automated_drift_detection_model_monitor.md)<br>[Lab 05: Clarify Bias/SHAP](./07_Hands_On_Labs/lab_05_model_fairness_bias_shap_explainability.md) | `python3 scripts/aws_revision_runner.py --cert MLA --community --mode practice -n 20`<br>`python3 scripts/aws_revision_runner.py --cert MLA --mode mock` |

---

## 🎯 Progress Checklist

- [ ] **Domain 1:** Completed Lecture 01 (Glue, Kinesis, EMR, Feature Store, vector chunking)
- [ ] **Domain 2:** Completed Lecture 02 & Lab 04 (PEFT, LoRA, Continued Pre-training, HPO)
- [ ] **Domain 3:** Completed Lecture 03, Lab 01 (SageMaker Pipelines) & Lab 02 (4 Inference Modes)
- [ ] **Domain 4:** Completed Lecture 04, Lab 03 (Model Monitor Drift) & Lab 05 (Clarify SHAP)
- [ ] **106Q Community Practice Pool:** Completed drills with `--community`
- [ ] **Full Timed Mock Simulation:** Scored $\ge 80\%$ on the 65-question timed mock exam (`--mode mock`)
"""
    (WORK_DIR / "AI/Associate/MLA-C01/00_START_HERE.md").write_text(mla_start, encoding="utf-8")
    print("  Created: AI/Associate/MLA-C01/00_START_HERE.md")

def update_gitignore():
    print("\n--- 4. Updating .gitignore ---")
    gi_path = WORK_DIR / ".gitignore"
    content = gi_path.read_text(encoding="utf-8")
    if "12_Sources/" not in content:
        content = content.replace("12_Sources/", "12_Sources/\n12_Sources/")
        content = content.replace("**/12_Sources/", "**/12_Sources/\n**/12_Sources/")
        gi_path.write_text(content, encoding="utf-8")
        print("  Updated .gitignore with 12_Sources/ exclusion.")

def update_verify_script():
    print("\n--- 5. Updating tests/verify_ecosystem_integrity.py ---")
    test_path = WORK_DIR / "tests/verify_ecosystem_integrity.py"
    content = test_path.read_text(encoding="utf-8")
    for old_name, new_name in MAPPING:
        content = content.replace(old_name, new_name)
    test_path.write_text(content, encoding="utf-8")
    print("  Updated tests/verify_ecosystem_integrity.py paths.")

def main():
    rename_directories()
    update_internal_links()
    create_start_here_guides()
    update_gitignore()
    update_verify_script()
    print("\n✅ Reorganization to Option A Completed Successfully!")

if __name__ == "__main__":
    main()
