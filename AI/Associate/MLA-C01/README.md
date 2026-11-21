# AWS Certified Machine Learning Engineer - Associate (MLA-C01) Training Suite

> **Exam Code:** `MLA-C01`  
> **Level:** Associate (Machine Learning Engineering & Generative AI)  
> **Passing Score:** `720 / 1000` (Scaled scoring)  
> **Questions:** 65 scenario-based questions, 130 minutes.

---

## 📂 Suite Directory Structure

```
AI/Associate/MLA-C01/
├── syllabus/              # Official blueprint, domain weighting, MLOps competencies
├── notes/                 # High-yield engineering cheat sheets (Inference types, drift, PEFT)
├── labs/                  # 100% written guided engineering labs (SageMaker, Bedrock)
├── lectures/              # Instructor delivery lesson plans and classroom talking points
├── diagrams/              # Standalone production MLOps & GenAI pipeline blueprints
├── revision_questions/    # Curated scenario-based revision questions
└── knowledge_checks/      # Rapid diagnostic retention quizzes per domain
```

---

## 🎯 Exam Domains & Weightings

```mermaid
pie title MLA-C01 Domain Weighting
    "Domain 1: Data Preparation for Machine Learning" : 28
    "Domain 2: ML Model Development" : 26
    "Domain 4: ML Solution Monitoring and Maintenance" : 24
    "Domain 3: Deployment and Orchestration of ML Workflows" : 22
```

1. **[Domain 1: Data Preparation for Machine Learning (28%)](phase0_step01_syllabus/MLA-C01_Official_Blueprint.md#domain-1-data-preparation-for-machine-learning-28):** Ingestion pipelines (Glue, Kinesis, EMR), feature engineering, handling data imbalances, chunking & vector embeddings.
2. **[Domain 2: ML Model Development (26%)](phase0_step01_syllabus/MLA-C01_Official_Blueprint.md#domain-2-ml-model-development-26):** Algorithm selection (tabular, CV, NLP), foundation model adaptation (PEFT/LoRA, Continued Pre-training), hyperparameter tuning (HPO), model evaluation.
3. **[Domain 3: Deployment and Orchestration of ML Workflows (22%)](phase0_step01_syllabus/MLA-C01_Official_Blueprint.md#domain-3-deployment-and-orchestration-of-ml-workflows-22):** SageMaker 4 inference deployment types (Real-Time, Serverless, Async, Batch Transform), SageMaker Pipelines CI/CD, container packaging.
4. **[Domain 4: ML Solution Monitoring and Maintenance (24%)](phase0_step01_syllabus/MLA-C01_Official_Blueprint.md#domain-4-ml-solution-monitoring-and-maintenance-24):** Detecting data & concept drift (Model Monitor), bias detection and explainability (Clarify / SHAP), model cards, safety guardrails, cost management.

---

## 🛠️ Interactive Tools

- **CLI Revision Engine:** Run interactive drills and simulated exams via:
  ```bash
  python3 scripts/aws_revision_runner.py --cert AIF --mode practice
  ```
- **Integrity Validation:** Run test suite across repositories:
  ```bash
  python3 tests/verify_ecosystem_integrity.py
  ```
