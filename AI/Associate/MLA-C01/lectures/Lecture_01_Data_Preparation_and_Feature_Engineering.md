# Lecture 01: Data Preparation, Feature Engineering & Vector Data

> **Course Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Domain 1: Data Preparation for Machine Learning (28%)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Architect scalable ingestion pipelines using Amazon Kinesis, AWS Glue ETL, and Amazon EMR.
2. Select appropriate feature engineering transformations (scaling, encoding, missing value imputation) without causing data leakage.
3. Design and operate the Amazon SageMaker Feature Store for low-latency online inference and offline batch training.
4. Prepare unstructured data for Generative AI applications (chunking, overlap, embeddings, and vector databases).

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:00] 1. The Reality of Production MLOps (80% Data Prep, 20% Modeling)
[01:00 - 02:30] 2. Ingestion Patterns: Streaming (Kinesis) vs. Batch (Glue / EMR)
[02:30 - 04:00] 3. Feature Engineering Best Practices & The Cardinal Sin: Data Leakage
[04:00 - 05:00] 4. Deep Dive: Amazon SageMaker Feature Store
[05:00 - 05:45] 5. Unstructured Data Preparation for GenAI (Chunking & Embeddings)
[05:45 - 06:00] 6. Exam Strategy, Traps & Knowledge Check Recap
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. Ingestion Patterns: When to Use What
- **Amazon Kinesis Data Streams:** Sub-second real-time streaming ingestion. Used when features must be computed on-the-fly (e.g., clickstream tracking, fraudulent payment detection).
- **AWS Glue (Serverless Apache Spark):** Ideal for batch data transformations on tabular/JSON/Parquet files in S3. Use Glue DataBrew for visual data preparation and Glue Crawlers for automatic schema cataloging.
- **Amazon EMR (Managed Hadoop/Spark):** Preferred over Glue when you require fine-grained cluster tuning, custom open-source libraries, Presto/Trino, or long-running big data clusters.

### 2. Feature Engineering & Avoiding Data Leakage (Whiteboard Prompt)
- *Whiteboard Diagram:* Draw the Split Line between Training Set and Test Set.
- **Key Instructor Emphasis:** *"Never fit scalers or imputers on the full dataset before splitting! Fit on the training set ONLY, then transform both train and test. Anything else is data leakage and will cause production models to fail catastrophically."*
- **Encoding:**
  - Nominal data (no order: Paris, London, Tokyo) $\implies$ **One-Hot Encoding**.
  - Ordinal data (natural rank: Bronze, Silver, Gold) $\implies$ **Ordinal Encoding**.
- **Scaling:**
  - Normal distribution $\implies$ **StandardScaler (Z-Score)**.
  - Uniform distribution, bounded range $\implies$ **MinMaxScaler**.
  - Significant outliers $\implies$ **RobustScaler (Median / IQR)**.

### 3. SageMaker Feature Store: The Dual-Store Pattern
- Explain why enterprise teams use a Feature Store: to eliminate training-serving skew (where training code calculates a feature differently than production API code).
- **Online Store:** Low-latency read access (backed by DynamoDB), used by SageMaker Real-Time endpoints during live inference.
- **Offline Store:** Append-only parquet records in S3, used for model training and historical time-travel analysis via Athena.

---

## 💻 Classroom Live Demo Walkthrough (5 Minutes)

1. Open AWS CloudShell.
2. Show how SageMaker Data Wrangler exports clean Python processing scripts directly into Amazon S3.
3. Query the Feature Store online record via AWS CLI:
   ```bash
   aws sagemaker-featurestore-runtime get-record \
     --feature-group-name customer-features \
     --record-identifier-value-as-string "CUST-1049"
   ```

---

## 🎯 High-Yield Exam Traps for this Lecture

1. **Trap:** Using SMOTE before splitting data into train/test sets.  
   *Correction:* SMOTE must be executed exclusively on the training split.
2. **Trap:** Using SageMaker Feature Store Online store for training large models.  
   *Correction:* Training reads from the **Offline Store** in S3; the Online store is strictly for single-record real-time lookup.
