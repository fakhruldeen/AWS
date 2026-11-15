# Lab 06: No-Code Predictive ML with Amazon SageMaker Canvas

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 1: Fundamentals of AI and Machine Learning  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** SageMaker Canvas free tier (2 months free, up to 10 session hours/month)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Launch the visual **Amazon SageMaker Canvas** studio interface.
2. Import structured tabular datasets from **Amazon S3**.
3. Configure automated feature correlation and select target columns for binary classification.
4. Execute **Quick Build** and **Standard Build** training runs.
5. Evaluate model performance (Accuracy, F1-Score, Confusion Matrix) and generate batch/single predictions.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Launch SageMaker Canvas
1. In the **AWS Management Console**, navigate to **Amazon SageMaker**.
2. In the left navigation pane under **Applications**, select **Canvas**.
3. Choose your SageMaker User Profile and click **Open Canvas**.
4. The visual Canvas workspace opens in a dedicated browser tab.

### Step 2: Import Tabular Dataset
1. In the Canvas left sidebar, click **Datasets**.
2. Click **Import data** > **Tabular** > **Amazon S3**.
3. Select a sample customer churn dataset (e.g., `customer_churn.csv`).
4. Review preview columns: `Tenure`, `MonthlyCharges`, `TotalCharges`, `ContractType`, `ChurnStatus`.
5. Click **Import data**.

![Canvas Import Dataset](images/lab06_step01_canvas_import_dataset.png)

### Step 3: Build Predictive Model
1. In the left menu, select **My models** > **New model**.
2. **Model name:** `CustomerChurnPredictor`
3. Select problem type: **Predictive analysis**.
4. Choose the imported dataset.
5. In the **Select target column** dropdown, choose `ChurnStatus`.
6. Canvas automatically identifies the problem as **2-Category (Binary Classification)**.
7. Click **Data visualizer** to review the automated correlation heatmaps between `ContractType` and `ChurnStatus`.

![Canvas Target Selection](images/lab06_step02_canvas_target_selection.png)

### Step 4: Train and Evaluate Model
1. Click **Quick build** (builds a model prototype in ~2-15 minutes).
2. Once the build completes, click the **Analyze** tab:
   * Review overall **Accuracy** (e.g., 86.4%) and **F1-Score**.
   * Inspect the **Feature Importance** ranking: observe which features (e.g., `ContractType` and `MonthlyCharges`) contributed most to the prediction.
   * Click **Advanced metrics** to view the **Confusion Matrix** (True Positives, False Positives, True Negatives, False Negatives).

![Canvas Model Metrics](images/lab06_step03_canvas_model_metrics.png)

### Step 5: Generate Predictions
1. Click the **Predict** tab.
2. Select **Single prediction**.
3. Adjust the slider values for `Tenure` (e.g., change from 2 months to 36 months) and toggle `ContractType` (Month-to-Month vs Two-Year).
4. Observe how the churn probability updates dynamically in real-time.

![Canvas Single Prediction](images/lab06_step04_canvas_single_prediction.png)

---

## 🧹 Teardown & Clean-up
* **Important:** In SageMaker Canvas, active user sessions incur hourly workspace charges if left open.
* In the bottom-left corner of the Canvas workspace, click the **User Profile icon** and select **Log out** (or in the SageMaker Console, click **Stop application** under Canvas user profiles).
