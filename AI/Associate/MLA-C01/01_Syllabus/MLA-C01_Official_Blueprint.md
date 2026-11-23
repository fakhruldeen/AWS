# AWS Certified Machine Learning Engineer - Associate (MLA-C01) Official Blueprint

> **Exam Code:** MLA-C01  
> **Credential:** AWS Certified Machine Learning Engineer - Associate  
> **Passing Score:** 720 / 1000  
> **Format:** 65 questions (multiple choice or multiple response), 130 minutes.

---

## Domain Breakdown

### Domain 1: Data Preparation for Machine Learning (28%)
- **Task Statement 1.1:** Ingest and aggregate data from disparate sources (Amazon S3, Amazon Kinesis, AWS Glue ETL jobs, Amazon EMR Spark clusters, Amazon MSK).
- **Task Statement 1.2:** Perform exploratory data analysis and feature engineering (Amazon SageMaker Data Wrangler, missing value imputation, one-hot encoding, feature normalization and scaling, SageMaker Feature Store online/offline).
- **Task Statement 1.3:** Prepare unstructured data for Generative AI and Foundation Models (tokenization, chunking strategies with overlap, embedding model generation using Amazon Titan Text Embeddings).

### Domain 2: ML Model Development (26%)
- **Task Statement 2.1:** Select appropriate modeling approaches for traditional ML (XGBoost, Linear Learner, Random Cut Forest for anomaly detection).
- **Task Statement 2.2:** Adapt Foundation Models using fine-tuning techniques (Parameter-Efficient Fine-Tuning / LoRA, Continued Pre-training on domain corpora in Amazon Bedrock or SageMaker JumpStart).
- **Task Statement 2.3:** Optimize training jobs and hyperparameters (SageMaker Automatic Model Tuning / HPO, distributed data parallel training on multi-GPU instances, checkpointing to S3).
- **Task Statement 2.4:** Evaluate model performance across relevant metrics (Accuracy, Precision, Recall, F1, AUC-ROC, ROUGE, BLEU, BERTScore, LLM-as-a-Judge).

### Domain 3: Deployment and Orchestration of ML Workflows (22%)
- **Task Statement 3.1:** Deploy models to production inference endpoints (SageMaker Real-Time for sub-second low latency, Serverless for intermittent bursts, Asynchronous for large 1GB payloads / long timeouts, Batch Transform for offline processing).
- **Task Statement 3.2:** Build automated CI/CD and MLOps pipelines (Amazon SageMaker Pipelines, Step Functions, SageMaker Model Registry with model approvals).
- **Task Statement 3.3:** Package custom ML code in Docker containers conforming to SageMaker Bring-Your-Own-Container (BYOC) specifications (Amazon ECR).

### Domain 4: ML Solution Monitoring and Maintenance (24%)
- **Task Statement 4.1:** Monitor data quality and model quality in production (Amazon SageMaker Model Monitor baseline comparisons, detecting feature attribution drift and data drift).
- **Task Statement 4.2:** Enforce responsible AI, bias mitigation, and explainability (Amazon SageMaker Clarify pre-training and post-training bias metrics, SHAP values, Amazon Bedrock Guardrails).
- **Task Statement 4.3:** Maintain model lineage and governance documentation (Amazon SageMaker Model Cards, Model Dashboard, CloudTrail API auditing).
- **Task Statement 4.4:** Optimize operational compute costs and resource allocation (Inference Recommender, AWS Inferentia / Trainium accelerators, Spot training instances with managed checkpointing).
