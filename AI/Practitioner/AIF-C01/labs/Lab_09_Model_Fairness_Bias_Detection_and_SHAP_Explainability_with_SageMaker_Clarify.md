# Lab 09: Model Fairness, Bias Detection & SHAP with SageMaker Clarify

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 4: Guidelines for Responsible AI  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** SageMaker Processing Job minimal compute ($<\$0.15$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Configure an **Amazon SageMaker Clarify** processing job.
2. Analyze pre-training bias metrics: **Class Imbalance (CI)** and **Difference in Positive Proportions in Labels (DPL)**.
3. Evaluate post-training bias metrics: **Disparate Impact (DI)**.
4. Calculate and visualize **SHAP (Shapley Additive exPlanations)** values for local and global model explainability.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Open Clarify Analysis in SageMaker Studio
1. In **Amazon SageMaker Studio**, navigate to your trained model from SageMaker Canvas or Training Jobs.
2. Select the **Explainability and Bias** tab.
3. Click **Configure Clarify Analysis**.

![Clarify Analysis Config](images/lab09_step01_clarify_analysis_config.png)

### Step 2: Define Demographic Facets and Target Labels
1. In the configuration dialog:
   * **Target column:** `Approved` (Positive label = `1`, Negative label = `0`).
   * **Sensitive demographic facet:** Select `Gender` (Favored group = `Male`, Disfavored group = `Female`).
2. Select **Pre-training bias metrics** and **Post-training bias metrics**.
3. Enable **SHAP feature attribution**.
4. Click **Run analysis**.

### Step 3: Interpret Pre-Training Bias Metrics
1. Open the generated Clarify Bias Report:
   * **Class Imbalance (CI):** Measures whether females are under-represented in the dataset. A value of `-0.35` indicates female applicants constitute only 32% of total rows.
   * **Difference in Positive Proportions (DPL):** Measures whether historical lending granted approvals to males at a higher rate. A DPL of `+0.22` shows significant historical bias in the training labels.

![Pre-Training Bias Metrics](images/lab09_step02_pre_training_bias_metrics.png)

### Step 4: Interpret Post-Training Disparate Impact (DI)
1. In the report, inspect the **Disparate Impact** chart:
   $$\text{DI} = \frac{P(\hat{Y}=1 | \text{Female})}{P(\hat{Y}=1 | \text{Male})}$$
2. Review if DI falls below the regulatory threshold of $0.80$ (adverse impact). If the model outputs a DI of $0.68$, mitigation (data re-weighting or feature suppression) is required.

![Post-Training Disparate Impact](images/lab09_step03_post_training_disparate_impact.png)

### Step 5: Analyze SHAP Feature Importance
1. Click the **Explainability** tab in the report.
2. Review the **Global Feature Importance** bar plot:
   * Identifies `DebtToIncomeRatio` and `CreditScore` as the two strongest drivers across all predictions.
3. Review an individual applicant's **Local SHAP Attribution**:
   * Observe how specific negative factors pushed an applicant below the approval threshold.

![SHAP Feature Importance Plot](images/lab09_step04_shap_feature_importance_plot.png)

---

## 🧹 Teardown & Clean-up
* Clarify processing jobs run on ephemeral instances and terminate automatically upon completion.
* Delete any temporary output files saved to S3 if desired.
