# Lecture 03: Inference Hosting Architecture & MLOps Pipelines

> **Course Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Domain 3: Deployment and Orchestration of ML and AI Workflows (22%)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Select the optimal SageMaker deployment option (Real-Time vs. Serverless vs. Asynchronous vs. Batch Transform).
2. Design and deploy Multi-Model Endpoints (MME) and Multi-Container Inference Pipelines.
3. Construct automated Directed Acyclic Graphs (DAGs) using Amazon SageMaker Pipelines.
4. Implement model governance approval workflows using the SageMaker Model Registry.

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:15] 1. The 4 SageMaker Deployment Types: Architectural Decision Tree
[01:15 - 02:30] 2. Advanced Endpoint Patterns: Multi-Model (MME) & Shadow Testing
[02:30 - 04:00] 3. Building Automated MLOps Workflows with SageMaker Pipelines
[04:00 - 05:15] 4. SageMaker Model Registry: Approval Gates & Production CD
[05:15 - 06:00] 5. Exam Scenarios, Payload Limits & Architecture Traps
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. The Inference Hosting Decision Tree
- Draw the 4 Quadrants on the Whiteboard:
  1. **Real-Time:** Persistent compute, sub-100ms latency, max 6 MB payload, max 60s timeout.
  2. **Serverless:** Sporadic traffic, cold start acceptable, scales to 0 ($0 when idle), max 4 MB payload.
  3. **Asynchronous:** Payloads up to 1 GB, processing up to 1 hour, built-in SQS queue, scales to 0 instances.
  4. **Batch Transform:** Offline scoring on petabytes in S3, no live endpoint, cluster shuts down on completion.

### 2. SageMaker Pipelines DAG Architecture
- Walk through the pipeline step sequence:
  - `ProcessingStep`: Cleans raw S3 data and outputs train/validation splits.
  - `TrainingStep`: Consumes S3 outputs from ProcessingStep; outputs `model.tar.gz`.
  - `EvaluationStep`: Runs evaluation script and produces `evaluation.json`.
  - `ConditionStep`: Evaluates if `Accuracy >= 0.80`. If true, triggers `RegisterModel`.
  - `RegisterModel`: Creates an unapproved model package in the SageMaker Model Registry.

### 3. Model Registry Governance Gate
- Explain why direct automated deployment from training jobs is a high-risk anti-pattern.
- The Model Registry acts as the bridge between Data Science (CI) and DevOps/SRE (CD):
  - Model status starts as `PendingManualApproval`.
  - Automated integration tests and human lead approval transition status to `Approved`.
  - An EventBridge rule on status change triggers AWS CodePipeline or CDK to deploy the endpoint.

---

## 💻 Classroom Live Demo Walkthrough (5 Minutes)

1. Show a running SageMaker Pipeline graph in SageMaker Studio.
2. Demonstrate transitioning a Model Package from `PendingManualApproval` to `Approved` via AWS CLI:
   ```bash
   aws sagemaker update-model-package \
     --model-package-arn "arn:aws:sagemaker:eu-north-1:ACCOUNT:model-package/churn/1" \
     --model-approval-status "Approved"
   ```

---

## 🎯 High-Yield Exam Traps for this Lecture

1. **Trap:** Increasing API Gateway limits when an image prediction payload is 15 MB.  
   *Correction:* Real-Time endpoints enforce a hard 6 MB ceiling. Use **SageMaker Asynchronous Inference** (up to 1 GB).
2. **Trap:** Hardcoding S3 paths between steps in a SageMaker Pipeline.  
   *Correction:* Always reference step properties dynamically (e.g., `step_process.properties.ProcessingOutputConfig.Outputs[...]`).
