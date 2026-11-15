# Lab 07: Data Preparation & Feature Engineering with SageMaker Data Wrangler

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 1: Fundamentals of AI and Machine Learning  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** SageMaker Studio free tier (t3.medium instance included)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Launch **Amazon SageMaker Data Wrangler** within SageMaker Studio.
2. Ingest raw structured datasets with missing and unformatted data.
3. Apply visual transformations: missing value imputation, outlier handling, and one-hot encoding.
4. Generate automated **Data Quality and Insights Reports**.
5. Export the data pipeline to **Amazon S3** or **SageMaker Feature Store**.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Open Data Wrangler in SageMaker Studio
1. In the **AWS Management Console**, navigate to **Amazon SageMaker** > **Studio**.
2. Open your Studio domain.
3. In the left navigation menu, click **Data** > **Data Wrangler** > **New data flow**.
4. Set the name to `CustomerCreditDataFlow`.

![Data Flow Canvas](images/lab07_step01_data_flow_canvas.png)

### Step 2: Import Raw Data and Run Insights Report
1. Select data source: **Amazon S3**.
2. Point to the credit dataset CSV.
3. Click **Add data flow**.
4. In the visual flow canvas, click the `+` icon on the dataset node and select **Get data insights**.
5. Choose target column `Approved`.
6. Review the generated report:
   * Identifies columns with high missing value rates.
   * Highlights duplicate rows.
   * Warns of anomalous outliers in `AnnualIncome`.

### Step 3: Impute Missing Values
1. Click the `+` icon on the dataset node and select **Add transform**.
2. Select **Handle missing values**:
   * Transform: **Impute**
   * Input column: `MonthlyExpenses`
   * Imputing strategy: **Median**
3. Click **Preview**, then click **Add**.

![Missing Value Imputation](images/lab07_step02_missing_value_imputation.png)

### Step 4: Encode Categorical Variables (One-Hot Encoding)
1. In the transform catalog, select **Encode categorical**.
2. Transform: **One-hot encode**.
3. Input column: `EmploymentType` (contains: Full-time, Part-time, Self-employed, Unemployed).
4. Output style: **Columns**.
5. Click **Preview**, observe the new binary columns generated, and click **Add**.

![One-Hot Encoding Step](images/lab07_step03_one_hot_encoding_step.png)

### Step 5: Export Data Pipeline
1. On the final step in the data flow, click the `+` icon and select **Export**.
2. Choose **Amazon S3 (via SageMaker Processing Job)**.
3. Review the generated pipeline configuration and export the clean dataset to your designated S3 bucket.

![Export Pipeline Destination](images/lab07_step04_export_pipeline_destination.png)

---

## 🧹 Teardown & Clean-up
* In SageMaker Studio, save and close the Data Wrangler tab.
* In the **Running instances** panel in Studio, shut down the Data Wrangler kernel session to prevent unnecessary compute charges.
