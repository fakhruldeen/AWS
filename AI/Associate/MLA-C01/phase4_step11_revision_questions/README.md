# 🎯 MLA-C01 Student Revision Question Suite

> **Certification:** AWS Certified Machine Learning Engineer - Associate (`MLA-C01`)  
> **Level:** Associate  
> **Total Curated Question Bank:** **542 Deduplicated Questions** across 4 Official Domains.

---

## 🧭 Revision Files Directory

| Resource | Scope | Count | Target Weight |
|---|---|---|---|
| **[MLA_C01_Community_Practice_Pool_106Q.md](./MLA_C01_Community_Practice_Pool_106Q.md)** | **Community Practice Pool with consensus discussion and distractor breakdowns** | **106 Questions** | **All 4 Domains** |
| **[Domain 1: Data Preparation for Machine Learning](./Domain_1_Data_Preparation_Revision_Questions.md)** | Ingestion (Kinesis, Glue, EMR), Feature Store, missing values, normalization, vector chunking & embeddings | 127 Questions | 28% |
| **[Domain 2: ML Model Development](./Domain_2_ML_Model_Development_Revision_Questions.md)** | Algorithm selection, PEFT/LoRA, distributed training, HPO tuning, classification & regression evaluation metrics | 161 Questions | 26% |
| **[Domain 3: Deployment & Orchestration of ML Workflows](./Domain_3_Deployment_and_Orchestration_Revision_Questions.md)** | SageMaker 4 deployment options (Real-Time, Serverless, Async, Batch Transform), SageMaker Pipelines CI/CD, Model Registry | 119 Questions | 22% |
| **[Domain 4: ML Solution Monitoring and Maintenance](./Domain_4_Monitoring_and_Maintenance_Revision_Questions.md)** | Data drift vs. concept drift (Model Monitor), bias detection & SHAP explainability (Clarify), Model Cards, security | 135 Questions | 24% |
| **[Full-Length Mock Revision Exam](./MLA_C01_Full_Length_Mock_Revision_Exam.md)** | Full 65-Question Simulation (130 minutes, 720 passing score) | 65 Questions | 100% |

---

## 💻 Terminal Interactive Revision Runner

Drill these questions interactively with instant feedback or run simulated timed exams:

```bash
# Practice Domain 3 with 10 questions
python3 scripts/aws_revision_runner.py --cert MLA --mode practice --domain 3 --count 10

# Practice from the Community Practice Pool
python3 scripts/aws_revision_runner.py --cert MLA --community --mode practice -n 15 --tricks

# Take the 130-minute 65-question mock exam
python3 scripts/aws_revision_runner.py --cert MLA --mode mock

# Retake previously missed questions
python3 scripts/aws_revision_runner.py --cert MLA --mode weakness
```
