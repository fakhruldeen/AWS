# Lab 03: Automated Data Drift and Concept Drift Detection with Amazon SageMaker Model Monitor

> **Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Domain:** Domain 4: ML Solution Monitoring and Maintenance  
> **Level:** Associate (Hands-on Engineering Lab)  
> **Estimated Time:** 45 minutes  
> **Cost Profile:** Low Cost / Free-Tier Eligible

---

## 🏗️ 1. Architecture Overview

In production machine learning systems, model predictive accuracy inevitably degrades over time due to shifts in input data distributions (**Data Drift**) and changes in the relationship between input features and target labels (**Concept Drift**). This lab demonstrates how to configure **Amazon SageMaker Model Monitor** to continuously capture live inference traffic, baseline distributions, and alert SRE/MLOps teams before degradation impacts business operations.

```mermaid
flowchart TD
    Client["Client / User Requests"] -->|Inference Payload| Endpoint["SageMaker Production Endpoint"]

    subgraph DataCapture ["SageMaker Data Capture (Zero Code)"]
        Endpoint -->|JSON Line Buffer| S3_Capture["Amazon S3: Captured Payloads<br/>(Inputs & Model Predictions)"]
    end

    subgraph ModelMonitor ["SageMaker Model Monitor (Cron / Event Trigger)"]
        Baseline["S3: Baseline Constraints & Statistics<br/>(Generated from Training Holdout)"]
        Monitor_Job["Model Monitor Hourly Processing Job"]
        
        S3_Capture --> Monitor_Job
        Baseline --> Monitor_Job

        Monitor_Job -->|Compare Distributions (K-L Divergence / KS Test)| Analysis["Violations Report (constraint_violations.json)"]
    end

    subgraph Alerting ["Observability & Automated Retraining"]
        Analysis --> CW_Metric["CloudWatch Metrics & Alarms<br/>(e.g., drift_detected > 0)"]
        CW_Metric --> SNS["Amazon SNS Alert to MLOps Team"]
        SNS --> EventBridge["Amazon EventBridge"]
        EventBridge -.Trigger Pipeline.-> Retrain["SageMaker Retraining Pipeline"]
    end
```

### The 4 Types of Drift Monitored by SageMaker:
1. **Data Quality Drift:** Input features deviate from baseline schema rules (e.g., null values, unexpected data types, or out-of-bounds ranges).
2. **Model Quality Drift:** Model performance metrics (Accuracy, F1, MSE) degrade over time when compared against ground-truth labels uploaded post-inference.
3. **Model Bias Drift:** Demographic bias metrics (e.g., Disparate Impact, DPPL) increase over time on live traffic.
4. **Feature Attribution Drift:** The ranking of which features drive model decisions shifts (monitored via SHAP values).

---

## 📋 2. Prerequisites & Environment Setup

- Existing SageMaker Real-Time Endpoint.
- S3 bucket for baseline statistics, captured data, and violation reports.
- IAM Role with `AmazonSageMakerFullAccess`.
- Target Region: `eu-north-1`.

---

## 🛠️ 3. Step-by-Step Guided Implementation

### Step 3.1: Enable Data Capture on the SageMaker Endpoint

1. When configuring or updating a SageMaker Endpoint Configuration:
   - Expand **Data capture settings**.
   - Check **Enable data capture**.
   - **Initial sampling percentage:** `100`% (or 20% for massive throughput).
   - **Capture modes:** Select both **Input** and **Output**.
   - **Destination S3 URI:** `s3://YOUR_BUCKET/captured-traffic/`.
   - **Capture content types:** `text/csv`, `application/json`.
2. Apply the configuration to the live endpoint. SageMaker now transparently captures all incoming HTTP payloads and output predictions into date-partitioned folders in S3.

---

### Step 3.2: Generate Baseline Constraints and Statistics

1. In Amazon SageMaker Studio (or via Python SDK / CLI):
   - Run a **Model Monitor Baseline Job** against your clean training dataset (`training_baseline.csv`).
2. SageMaker generates two critical JSON artifacts:
   - `statistics.json`: Computes mean, median, standard deviation, min, max, and quantiles for every numerical feature, along with distinct category frequencies for categorical features.
   - `constraints.json`: Inferred rules defining acceptable data boundaries (e.g., `feature "Age" must be >= 18 and <= 100`, `null_count == 0`).

---

### Step 3.3: Schedule the Continuous Monitoring Job

1. Under **SageMaker Console > Inference > Model monitor**:
   - Click **Create monitoring schedule**.
   - **Schedule type:** Data quality.
   - **Endpoint:** Select your live endpoint.
   - **Baseline datasets:** Point to `statistics.json` and `constraints.json`.
   - **Monitoring frequency:** Hourly (or daily).
   - **Output path:** `s3://YOUR_BUCKET/monitoring-reports/`.
2. **How it executes:** Every hour, SageMaker automatically launches a managed processing container, reads the captured inference payloads from S3, executes statistical checks (Kolmogorov-Smirnov tests) against the baseline constraints, and writes a `constraint_violations.json` report.

---

### Step 3.4: Configure CloudWatch Alarms for Automated Retraining

1. Model Monitor emits metrics to CloudWatch under the namespace `aws/sagemaker/Endpoints/data-metrics`.
2. Create an Alarm on metric `feature_baseline_drift_Age`:
   - Condition: Greater than threshold `0.1` for 2 consecutive periods.
   - Action: Send SNS notification and trigger an EventBridge rule that starts a SageMaker Retraining Pipeline!

---

## 💻 4. AWS CLI v2 Executable Runbook

### Step 4.1: Enable Data Capture on Endpoint via CLI
```bash
# 1. Update Endpoint Config with DataCaptureConfig
aws sagemaker create-endpoint-config \
  --endpoint-config-name monitored-config-cli \
  --production-variants VariantName=AllTraffic,ModelName=churn-model-cli,InitialInstanceCount=1,InstanceType=ml.m5.large \
  --data-capture-config '{
    "EnableCapture": true,
    "InitialSamplingPercentage": 100,
    "DestinationS3Uri": "s3://'$BUCKET_NAME'/captured-traffic",
    "CaptureOptions": [{"CaptureMode": "Input"}, {"CaptureMode": "Output"}]
  }'

# 2. Update live endpoint to use monitored configuration
aws sagemaker update-endpoint \
  --endpoint-name live-churn-endpoint \
  --endpoint-config-name monitored-config-cli
echo "Data capture enabled on live endpoint."
```

### Step 4.2: Create Monitoring Schedule via CLI
```bash
# Create Data Quality Monitoring Schedule
aws sagemaker create-data-quality-job-definition \
  --job-definition-name churn-data-quality-job \
  --data-quality-app-specification ImageUri=683313688378.dkr.ecr.eu-north-1.amazonaws.com/sagemaker-model-monitor-analyzer:latest \
  --data-quality-job-input '{
    "EndpointInput": {
      "EndpointName": "live-churn-endpoint",
      "LocalPath": "/opt/ml/processing/input/endpoint"
    }
  }' \
  --data-quality-job-output-config '{
    "MonitoringOutputs": [{
      "S3Output": {
        "S3Uri": "s3://'$BUCKET_NAME'/monitoring-output",
        "LocalPath": "/opt/ml/processing/output"
      }
    }]
  }' \
  --data-quality-baseline-config '{
    "ConstraintsResource": {"S3Uri": "s3://'$BUCKET_NAME'/baseline/constraints.json"},
    "StatisticsResource": {"S3Uri": "s3://'$BUCKET_NAME'/baseline/statistics.json"}
  }' \
  --job-resources ClusterConfig='{"InstanceCount":1,"InstanceType":"ml.m5.xlarge","VolumeSizeInGB":20}' \
  --role-arn $SAGEMAKER_ROLE_ARN

# Create Hourly Schedule
aws sagemaker create-monitoring-schedule \
  --monitoring-schedule-name hourly-drift-monitor \
  --monitoring-schedule-config '{
    "ScheduleConfig": {"ScheduleExpression": "cron(0 * ? * * *)"},
    "MonitoringJobDefinitionName": "churn-data-quality-job",
    "MonitoringType": "DataQuality"
  }'
echo "Monitoring schedule created."
```

---

## 🎯 5. Exam Practice: Scenarios & Traps (MLA-C01)

| Scenario / Exam Trap | What the Exam Asks | Architecturally Correct Decision | Why Alternatives Are Traps |
|---|---|---|---|
| **Trap 1: Data Drift vs Concept Drift Distinction** | *"In a credit risk model, the demographic age of applicants shifts from 40–60 to 20–30. What type of drift is this?"* | This is **Data Drift (Covariate Shift)**: the distribution of input features $P(X)$ changed. If macroeconomic default rates changed for the same age group ($P(y\|X)$ changes), that would be **Concept Drift**. | Confusing data drift with concept drift leads to incorrect monitoring remediation strategies. |
| **Trap 2: Model Quality Monitoring without Ground Truth** | *"An ML engineer enables Model Quality monitoring, but the hourly monitoring job fails to produce accuracy or F1-score violation metrics."* | Model Quality monitoring **requires uploading ground-truth labels** to S3 post-inference. SageMaker cannot compute Accuracy or F1 without knowing the actual true outcomes! | Data Quality monitoring works with inputs alone, but Model Quality strictly requires ground-truth label matching. |
| **Trap 3: Feature Attribution Drift** | *"A fraud model's predictions remain accurate, but customer support reports that the features explaining loan decisions have radically changed."* | Enable **SageMaker Model Monitor Feature Attribution Monitoring** (powered by SageMaker Clarify). Tracks whether the relative SHAP importance of features deviates from the baseline. | Data quality monitoring only checks individual column distributions; it cannot detect multivariate feature attribution shifts. |
| **Trap 4: Sampling Rate Cost vs Accuracy Trade-off** | *"An endpoint processes 10,000 requests per second. Enabling 100% data capture results in massive S3 storage costs."* | Adjust the **Data Capture Sampling Percentage** (e.g., reduce from 100% to 5% or 10%). A statistically representative sample is sufficient for Kolmogorov-Smirnov drift detection. | Storing every single request on ultra-high throughput endpoints is wasteful and unnecessary for statistical drift tracking. |
| **Trap 5: Automated Retraining Trigger Architecture** | *"How should an MLOps engineer automatically trigger a retraining pipeline when drift is detected?"* | Configure Model Monitor to emit CloudWatch metrics, attach a **CloudWatch Alarm** to the metric, and route the alarm state change through **Amazon EventBridge to start a SageMaker Pipeline**. | Writing custom cron pollers to inspect S3 violation reports introduces operational overhead and latency. |

---

## 🧹 6. Resource Cleanup

```bash
# Delete monitoring schedule and job definition
aws sagemaker delete-monitoring-schedule --monitoring-schedule-name hourly-drift-monitor
aws sagemaker delete-data-quality-job-definition --job-definition-name churn-data-quality-job
echo "Lab 03 cleanup complete."
```
