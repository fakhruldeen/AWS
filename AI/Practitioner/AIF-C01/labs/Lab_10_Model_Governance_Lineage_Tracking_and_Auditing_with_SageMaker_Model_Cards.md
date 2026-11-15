# Lab 10: Model Governance & Auditing with SageMaker Model Cards

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 4 & Domain 5: Responsible AI & Model Governance  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Minimal storage / metadata catalog charges ($<\$0.05$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Create a standardized **Amazon SageMaker Model Card**.
2. Document intended use, business limitations, and compliance risk ratings.
3. Attach quantitative evaluation benchmarks and SageMaker Clarify bias findings.
4. Publish the model card to the **Amazon SageMaker Model Registry**.
5. Enforce gated multi-stakeholder approval workflows (`PendingManualApproval` to `Approved`).

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Create a Model Card in SageMaker Studio
1. In **Amazon SageMaker Studio**, navigate to **Governance** > **Model Cards**.
2. Click **Create model card**:
   * **Model card name:** `ConsumerCreditScoringModelCard-v1`
   * **Model overview:** Document the model algorithm (XGBoost binary classifier) and developer team contact.
3. Click **Next**.

![Model Card Creator](images/lab10_step01_model_card_creator.png)

### Step 2: Document Intended Uses & Limitations
1. In the **Intended use** tab:
   * **Intended purpose:** Automated credit risk score generation for personal loan applications under \$50,000.
   * **Intended users:** Licensed retail loan underwriting officers.
   * **Out-of-scope / Prohibited uses:** Automated decisioning for commercial mortgages without human appeal review.
2. Click **Next**.

### Step 3: Attach Evaluation Metrics & Bias Reports
1. In the **Model evaluation** tab:
   * Enter test set Accuracy: `88.2%`.
   * Enter AUC-ROC: `0.91`.
   * Attach the SageMaker Clarify bias report from Lab 09 (Class Imbalance: `-0.35`, Disparate Impact: `0.85`).
2. Attach SHAP global feature importance rankings.

![Model Card Evaluation Metrics](images/lab10_step02_model_card_evaluation_metrics.png)

### Step 4: Define Risk Rating and Ownership
1. In the **Risk rating** section:
   * Risk tier: **High Risk** (Financial credit scoring).
   * Compliance owner: Chief Risk & Compliance Officer.
2. Click **Create model card**.

![Model Card Risk Rating](images/lab10_step03_model_card_risk_rating.png)

### Step 5: Enforce Approval Gates in SageMaker Model Registry
1. Navigate to **Governance** > **Model Registry**.
2. Select your registered model package group.
3. Click on version `1`.
4. Review the attached Model Card.
5. In the top action bar, click **Update status**:
   * Change status from `PendingManualApproval` to **Approved**.
   * Add approval comment: `"Clarify bias metrics reviewed and within regulatory tolerances."`
6. Click **Update status**.

![Model Registry Approval Gate](images/lab10_step04_model_registry_approval_gate.png)

---

## 🧹 Teardown & Clean-up
* Model Cards and Registry packages reside in the SageMaker metadata repository and incur negligible costs.
* Delete the model card and model package group in the console if no longer needed.
