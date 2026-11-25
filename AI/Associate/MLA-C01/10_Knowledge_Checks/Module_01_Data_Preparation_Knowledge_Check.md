# Module 01: Data Preparation for Machine Learning — Knowledge Check

> **Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Module 1: Data Preparation, Feature Engineering & Vector Storage  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 1 materials and completing Lab 01. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
An ML engineer is building a feature engineering pipeline that ingests continuous IoT sensor telemetry from thousands of devices. The pipeline must compute rolling 10-minute averages and store features for both low-latency real-time online inference and batch offline training. Which architecture should be deployed?

- **A.** Amazon Kinesis Data Streams → Amazon SageMaker Feature Store (with Online Store for real-time reads and Offline Store in Amazon S3).
- **B.** Amazon CloudWatch Logs → AWS CloudTrail → Amazon DynamoDB.
- **C.** Amazon SQS → AWS Lambda → Amazon EBS volume.
- **D.** AWS Glue ETL running on a monthly batch schedule.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
Amazon SageMaker Feature Store provides a purpose-built repository for ML features:
- **Online Store:** High-throughput, ultra-low latency (<10ms) read access for real-time inference (backed by DynamoDB).
- **Offline Store:** Append-only historical record stored in Amazon S3 for batch training, model retraining, and point-in-time time-travel queries via Amazon Athena.
</details>

---

### Question 2
A tabular dataset for credit risk modeling contains a categorical column `Education_Level` with values `['High School', 'Bachelors', 'Masters', 'Doctorate']`. What is the most appropriate feature encoding technique?

- **A.** Ordinal Encoding (preserving the natural hierarchical ranking: 0, 1, 2, 3).
- **B.** One-Hot Encoding with 4 independent binary columns.
- **C.** SHA-256 Cryptographic Hashing.
- **D.** Dropping the column to prevent data leakage.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
Because `Education_Level` has a clear, intrinsic natural order (`High School < Bachelors < Masters < Doctorate`), **Ordinal Encoding** preserves the ordinal relationship. For nominal data without intrinsic order (e.g., `City: ['Paris', 'Tokyo', 'New York']`), One-Hot Encoding is used.
</details>

---

### Question 3
An unstructured document dataset of 500-page financial filings must be indexed into a vector database for a Retrieval-Augmented Generation (RAG) assistant. Why is fixed-size chunking with an overlap buffer (e.g., 512 tokens with 15% overlap) standard practice?

- **A.** To prevent key semantic context and entity relationships from being severed at chunk boundaries.
- **B.** To bypass S3 bucket size limitations.
- **C.** To force the embedding model to run on CPU instances.
- **D.** To encrypt the vectors with AWS KMS.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
Chunk overlap ensures that sentences or entities that span across split boundaries retain their semantic meaning in adjacent chunks, significantly improving vector similarity retrieval accuracy.
</details>

---

### Question 4
A machine learning engineer notices that 98% of values in a `Salary` column are between \$40,000 and \$120,000, but a few data entry errors exist with values exceeding \$50,000,000. Which normalization technique is most robust to these extreme outliers?

- **A.** Robust Scaler (using median and Interquartile Range - IQR) or Quantile Transformer.
- **B.** Min-Max Normalization (scaling strictly between 0 and 1).
- **C.** Standard Z-score scaling without clipping.
- **D.** Multiplying all salaries by zero.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
Min-Max scaling and standard Z-score scaling are severely distorted by extreme outliers because they rely on minimum/maximum or mean/variance. **RobustScaler** scales features using statistics that are robust to outliers: median and IQR (Q₃ - Q₁).
</details>

---

### Question 5
In an imbalanced binary fraud detection dataset where fraudulent transactions represent only 0.2% of all samples, what data-level technique can be used during data preparation to balance the class distribution?

- **A.** SMOTE (Synthetic Minority Over-sampling Technique) applied strictly to the training split.
- **B.** SMOTE applied to the entire dataset prior to splitting into train/test sets.
- **C.** Removing all negative instances until only fraud remains.
- **D.** Setting all feature values to 1.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**SMOTE** generates synthetic examples of the minority class along the feature-space line segments connecting k-nearest neighbors. **Crucial Rule:** Oversampling or data transformation MUST be applied **only to the training split**; applying it before splitting causes severe **data leakage** and invalidates test set evaluation.
</details>

---

### Question 6
Which AWS service allows data scientists to visually inspect, clean, and transform multi-gigabyte tabular datasets with over 300 built-in transformations and automatically export the transformation steps as an executable SageMaker Processing job?

- **A.** Amazon SageMaker Data Wrangler
- **B.** Amazon CloudFront
- **C.** AWS CodeDeploy
- **D.** Amazon Route 53

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Amazon SageMaker Data Wrangler** is designed specifically to simplify and accelerate data preparation and feature engineering for machine learning. It offers over 300 built-in transforms, data quality insights, and one-click export to SageMaker Processing pipelines or Feature Store.
</details>

---

### Question 7
What is the primary technical distinction between a **Local Secondary Index (LSI)** and a **Global Secondary Index (GSI)** when querying feature tables in Amazon DynamoDB?

- **A.** An LSI must use the same Partition Key as the base table with a different Sort Key, whereas a GSI can define an entirely new Partition Key and Sort Key.
- **B.** An LSI is multi-region while a GSI is single-AZ.
- **C.** A GSI supports strongly consistent reads while an LSI does not.
- **D.** An LSI can only store text while a GSI stores binary.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
In DynamoDB:
- **LSI:** Same Partition Key, different Sort Key; must be created at table creation time; supports strong consistency.
- **GSI:** Can have a completely different Partition Key and Sort Key; can be created or deleted anytime; supports eventual consistency.
</details>

---

### Question 8
Which file format provides the fastest columnar reading performance and most efficient compression for large-scale ML data preprocessing on Apache Spark (Amazon EMR / AWS Glue)?

- **A.** Apache Parquet
- **B.** Uncompressed CSV
- **C.** Raw JSON Lines
- **D.** Plain text (.txt)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Apache Parquet** is a columnar storage format optimized for analytical queries. It provides columnar compression (Snappy), column projection (reading only needed columns), and predicate pushdown (skipping unneeded row groups), drastically reducing S3 I/O and accelerating ETL jobs.
</details>

---

### Question 9
During an exploratory data analysis step, an ML engineer finds that 15% of records in an `Income` column are null (missing). Which imputation method is statistically most appropriate for skewed numerical data?

- **A.** Median Imputation
- **B.** Mean Imputation
- **C.** Replacing all nulls with zero
- **D.** Deleting all features from the dataset

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
When numerical data is skewed or contains outliers, the **median** is a much more robust measure of central tendency than the mean. Mean imputation is heavily distorted by extreme values.
</details>

---

### Question 10
What is the primary risk of "Data Leakage" during feature engineering?

- **A.** Information from the target label or future test data inadvertently contaminates the training features, causing unrealistically high training performance that collapses in production.
- **B.** Data is transmitted over unencrypted HTTP.
- **C.** S3 buckets are accidentally made public.
- **D.** CPU instances run out of memory.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Data Leakage** occurs when data outside the training dataset (e.g., information from the test split, or features computed using future outcomes that won't be available at prediction time) is used to train the model. The model learns spurious shortcuts and fails completely when deployed to production.
</details>
