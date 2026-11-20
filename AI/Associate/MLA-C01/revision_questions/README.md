# 🎯 MLA-C01 Student Revision Question Suite

> **Certification:** AWS Certified Machine Learning Engineer - Associate (`MLA-C01`)  
> **Level:** Associate  
> **Total Curated Question Bank:** **542 Deduplicated Questions** across 4 Official Domains.

---

## 🧭 Revision Files Directory

1. **[Domain 1: Data Preparation for Machine Learning (127 Questions)](./Domain_1_Data_Preparation_Revision_Questions.md)** (28% of exam)
   - Ingestion (Kinesis, Glue, EMR), Feature Store, missing values, normalization, vector chunking & embeddings.
2. **[Domain 2: ML Model Development (161 Questions)](./Domain_2_ML_Model_Development_Revision_Questions.md)** (26% of exam)
   - Algorithm selection, PEFT/LoRA, distributed training, HPO tuning, classification & regression evaluation metrics.
3. **[Domain 3: Deployment & Orchestration of ML Workflows (119 Questions)](./Domain_3_Deployment_and_Orchestration_Revision_Questions.md)** (22% of exam)
   - SageMaker 4 deployment options (Real-Time, Serverless, Async, Batch Transform), SageMaker Pipelines CI/CD, Model Registry.
4. **[Domain 4: ML Solution Monitoring and Maintenance (135 Questions)](./Domain_4_Monitoring_and_Maintenance_Revision_Questions.md)** (24% of exam)
   - Data drift vs. concept drift (Model Monitor), bias detection & SHAP explainability (Clarify), Model Cards, security.
5. **[Full-Length 65-Question Timed Mock Exam](./MLA_C01_Full_Length_Mock_Revision_Exam.md)** (130 minutes, 720 passing score)

---

## 💻 Terminal Interactive Revision Runner

Drill these questions interactively with instant feedback or run simulated timed exams:
```bash
# Practice Domain 3 with 10 questions
python3 scripts/aws_revision_runner.py --cert MLA --mode practice --domain 3 --count 10

# Take the 130-minute 65-question mock exam
python3 scripts/aws_revision_runner.py --cert MLA --mode mock

# Retake previously missed questions
python3 scripts/aws_revision_runner.py --cert MLA --mode weakness
```
