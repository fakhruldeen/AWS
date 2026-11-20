# Module 03: Deployment & Orchestration of ML Workflows — Knowledge Check

> **Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Module 3: SageMaker 4 Deployment Options, Pipelines, MLOps & Model Registry  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 3 materials and completing Labs 01 & 02. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
An application receives 25 MB high-resolution medical MRI scans and processes them using a deep learning segmentation model. Processing each image takes approximately 3 minutes. The standard Real-Time endpoint returns HTTP 413 Payload Too Large. Which SageMaker deployment option must be used?

- **A.** Amazon SageMaker Asynchronous Inference
- **B.** Amazon SageMaker Serverless Inference
- **C.** Amazon API Gateway REST API with Lambda
- **D.** Real-Time Inference with increased timeout

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
SageMaker **Asynchronous Inference** is designed for workloads with large payloads (up to **1 GB**) and long processing times (up to **1 hour / 3,600s**). It uses built-in managed SQS queues and can scale compute instances down to zero when idle. Real-Time and Serverless endpoints enforce a strict 6 MB and 4 MB limit respectively.
</details>

---

### Question 2
A developer needs to host 800 distinct personalized customer recommendation models. Most models receive only a few requests per hour. Deploying individual real-time endpoints for every customer model would require hundreds of EC2 instances and cost tens of thousands of dollars per month. What is the optimal architectural pattern?

- **A.** Amazon SageMaker Multi-Model Endpoints (MME)
- **B.** Deploying 800 individual real-time endpoints on `c5.xlarge` instances.
- **C.** Hosting models on AWS Lambda with 15-minute execution timeouts.
- **D.** Storing models on Amazon S3 Glacier.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**SageMaker Multi-Model Endpoints (MME)** allow hosting thousands of models on a single shared compute instance fleet. SageMaker dynamically loads models from S3 into container memory on demand and unloads infrequently used models using an LRU cache, slashing hosting costs by up to 90%.
</details>

---

### Question 3
What is the primary role of the **SageMaker Model Registry** in an enterprise MLOps lifecycle?

- **A.** Centralizing model cataloging, versioning, metadata tracking, and enforcing manual or automated deployment approval gates (`PendingManualApproval` $\rightarrow$ `Approved`).
- **B.** Storing raw uncompressed CSV training files.
- **C.** Monitoring real-time GPU temperatures in data centers.
- **D.** Managing DNS records in Route 53.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
The **SageMaker Model Registry** provides a centralized catalog for managing model packages. It tracks model lineage, associated training metrics, deployment artifacts, and approval statuses, ensuring that unapproved models cannot be deployed to production endpoints.
</details>

---

### Question 4
In an Amazon SageMaker Pipeline, what step type is used to conditionally execute a downstream branch (e.g., only registering a model if its validation accuracy is greater than or equal to 0.85)?

- **A.** ConditionStep
- **B.** TrainingStep
- **C.** ProcessingStep
- **D.** FailStep

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
A **ConditionStep** evaluates boolean conditions (such as numerical comparisons: `GreaterThanOrEqualTo`, `LessThan`) based on metric properties from prior steps (like an `evaluation.json` report). If the condition is met, it triggers the `if_steps` (e.g., `RegisterModel`); otherwise, it executes the `else_steps`.
</details>

---

### Question 5
Which SageMaker deployment option automatically scales its compute capacity down to zero instances when no inference requests are being received, incurring **\$0.00 compute costs when idle**?

- **A.** Amazon SageMaker Serverless Inference (and Asynchronous Inference when queue is empty)
- **B.** Amazon SageMaker Real-Time Inference
- **C.** Amazon EC2 Dedicated Hosts
- **D.** Amazon ECS with persistent EC2 instances

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Serverless Inference** automatically provisions and deprovisions compute resources on demand. When there is zero traffic, instance count is 0, costing \$0. Asynchronous inference also integrates with Application Auto Scaling to scale instances to 0 when the queue is empty. Real-Time endpoints require at least 1 running instance.
</details>

---

### Question 6
An engineering team wants to test a newly trained model in production by duplicating 100% of live production traffic to the new model in the background, without returning its predictions to users or impacting existing user latency. What deployment strategy is this?

- **A.** Shadow Deployment
- **B.** Canary Deployment
- **C.** Blue-Green Deployment
- **D.** All-at-Once Deployment

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
In a **Shadow Deployment**, live production requests are mirrored to a new model variant (the shadow variant) in parallel. The shadow variant's predictions are recorded and logged for performance and error analysis, but are never returned to the caller, ensuring zero risk to production traffic.
</details>

---

### Question 7
In a SageMaker Bring-Your-Own-Container (BYOC) deployment, what standard HTTP endpoints must the Docker container implement to successfully serve inference requests?

- **A.** `POST /invocations` and `GET /ping`
- **B.** `GET /health` and `POST /predict`
- **C.** `GET /index.html` and `POST /login`
- **D.** `SSH :22` and `FTP :21`

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
SageMaker's inference contract requires custom containers to listen on port 8080 and implement:
- `GET /ping`: For health checks (must return HTTP 200).
- `POST /invocations`: For processing prediction requests.
</details>

---

### Question 8
Which feature of Amazon Bedrock enables autonomous AI agents to orchestrate multi-step reasoning, plan tasks, interact with enterprise systems via OpenAPI schemas, and execute Lambda functions?

- **A.** Amazon Bedrock Agents (Action Groups)
- **B.** AWS CloudFormation
- **C.** Amazon Polly
- **D.** Amazon Rekognition Custom Labels

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Amazon Bedrock Agents** utilize the ReAct (Reasoning + Acting) framework to automatically break down natural language requests, call APIs via **Action Groups** defined by OpenAPI schemas, invoke AWS Lambda functions for backend execution, and retrieve knowledge from Bedrock Knowledge Bases.
</details>

---

### Question 9
In SageMaker Asynchronous Inference, how does a client application know when a long-running prediction has completed?

- **A.** By configuring an **Amazon SNS Topic** in the asynchronous invocation request or checking the output S3 location.
- **B.** By holding an open HTTP socket connection for 3 hours.
- **C.** By reading CloudWatch CPU alarms.
- **D.** By rebooting the client browser.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
When calling an Asynchronous endpoint, SageMaker returns an HTTP 202 Accepted response with the output S3 URI. Upon completion, SageMaker can publish a completion notification to an **Amazon SNS Topic** (which can trigger a webhook, Lambda, or SQS queue).
</details>

---

### Question 10
What tool in Amazon SageMaker analyzes model performance across multiple EC2 instance families to recommend the most cost-effective instance type and configuration for real-time inference?

- **A.** Amazon SageMaker Inference Recommender
- **B.** AWS Cost Explorer
- **C.** AWS Trusted Advisor
- **D.** AWS Compute Optimizer for EBS

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**SageMaker Inference Recommender** automatically runs load tests across various instance types and configurations to benchmark latency, throughput, and cost per million inferences, recommending the optimal instance type to achieve your latency SLA at the lowest cost.
</details>
