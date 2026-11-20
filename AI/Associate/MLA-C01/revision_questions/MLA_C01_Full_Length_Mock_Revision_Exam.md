# AWS Certified Machine Learning Engineer - Associate (MLA-C01) Full-Length Mock Exam

> **Exam Code:** MLA-C01  
> **Time Limit:** 130 minutes  
> **Total Questions:** 65 scenario-based questions  
> **Passing Score:** 720 / 1000 (~72%)  
> **Domain Weighting:** Strictly calibrated to the official AWS exam blueprint (D1: 28%, D2: 26%, D3: 22%, D4: 24%)

---

## 📌 Exam Instructions
Simulate real testing conditions. Allocate 130 uninterrupted minutes. Commit to an answer for all 65 questions before reviewing the answer key and rationales in the `<details>` blocks.

---

## Question 1 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0131`

Which of the following is a key reason to use SageMaker Model Monitor in a production environment?

- **A) To reduce model training time**
- **B) To improve model interpretability**
- **C) To simplify model deployment**
- **D) To identify drift in ML models**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "To identify drift in ML models"?**

SageMaker Model Monitor is designed to detect and alert on concept drift in deployed models. Concept drift occurs when the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes the model to become less accurate as time passes.

### Incorrect Options:
- **To reduce model training time**  
  SageMaker Model Monitor does not directly reduce model training time. It is used to monitor the performance of deployed models.

- **To improve model interpretability**  
  While model interpretability is important, SageMaker Model Monitor does not directly improve it. It is used to monitor the performance of deployed models.

- **To simplify model deployment**  
  SageMaker Model Monitor does not simplify model deployment. It is used to monitor the performance of deployed models.

</details>

---

## Question 2 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0266`

You are working on a project that requires real-time language translation for a live event.

Which AWS service would be the most appropriate to use for this task?

- **A) Amazon Translate**
- **B) Amazon Transcribe**
- **C) Amazon Rekognition**
- **D) SageMaker JumpStart**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Amazon Translate"?**

Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable language translation. It is suitable for real-time language translation for a live event.

### Incorrect Options:
- **Amazon Transcribe**  
  Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech-to-text capability to their applications. It does not provide language translation.

- **Amazon Rekognition**  
  Amazon Rekognition makes it easy to add image and video analysis to your applications. It does not provide language translation.

- **SageMaker JumpStart**  
  SageMaker JumpStart provides ready-to-use machine learning solutions, but it does not provide capabilities for language translation.

</details>

---

## Question 3 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0143`

A team is comparing two Amazon Bedrock text-generation models on nuanced customer-support responses. Automated metrics cannot reliably judge factuality and tone, and reviewers must compare outputs side by side without seeing which model produced each response. The team needs a managed workflow that assigns evaluation tasks to reviewers and collects their judgments. Which solution best meets these requirements?

- **A) Use Amazon CloudWatch metrics and anomaly detection**
- **B) Use Amazon Bedrock model evaluation with human workers**
- **C) Use SageMaker Ground Truth human review workflows**
- **D) Use Amazon Bedrock Guardrails to score response quality**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Use Amazon Bedrock model evaluation with human workers"?**

Amazon Bedrock model evaluation supports human-based evaluations for foundation models, including side-by-side comparisons of model responses. It can collect reviewer judgments on subjective dimensions such as tone and helpfulness, which automated metrics may not assess reliably.

### Incorrect Options:
- **Use SageMaker Ground Truth human review workflows**  
  Ground Truth can build custom human-review workflows, but it is not the managed Amazon Bedrock model-evaluation capability specified for comparing foundation-model responses.

- **Use Amazon Bedrock Guardrails to score response quality**  
  Guardrails apply configured policies to inputs and outputs; they do not assign comparative evaluation tasks to human reviewers.

- **Use Amazon CloudWatch metrics and anomaly detection**  
  CloudWatch can monitor operational metrics and detect anomalies, but it does not collect human judgments about response quality.

</details>

---

## Question 4 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0331`

A company uses AWS Glue to automate their ETL processes for data stored in various formats. They are planning to optimize the performance of their Glue ETL jobs which currently handle large volumes of Parquet files. What would be the most cost-effective way to optimize these jobs without compromising on performance?

- **A) Manually trigger ETL jobs instead of scheduling them to control when resources are utilized.**
- **B) Implement job bookmarking to track data processed between job runs and reduce data redundancy.**
- **C) Increase the number of DPUs in each ETL job to process data faster.**
- **D) Convert all Parquet files into CSV format to simplify processing.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Correct answer: Implement job bookmarking to track data processed between job runs and reduce data redundancy.**

Job bookmarking in AWS Glue is a feature that allows Glue to track the data it has already processed in previous runs of a job. This is particularly useful when dealing with large datasets that are updated frequently. By using job bookmarking, Glue can avoid reprocessing data that has already been processed, significantly reducing the job's runtime and, consequently, the cost. This is a cost-effective optimization because it reduces the amount of compute resources (DPUs) needed for each job run without requiring any changes to the underlying data format or infrastructure. It directly addresses data redundancy in ETL processes, a key aspect of efficient data engineering.

**Incorrect:**

**A. Manually trigger ETL jobs instead of scheduling them to control when resources are utilized.** - While manually triggering jobs *can* offer some control, it doesn't inherently optimize the job's performance or cost. The job will still process the same amount of data, regardless of whether it's triggered manually or scheduled. It also introduces operational overhead and potential delays. The core issue of processing redundant data remains unaddressed.

**C. Increase the number of DPUs in each ETL job to process data faster.** - Increasing the number of DPUs (Data Processing Units) will likely speed up the job, but it also increases the cost. This is not the *most* cost-effective solution. It's better to optimize the job's efficiency first (e.g., through bookmarking) before simply throwing more resources at the problem. Increasing DPUs should be considered after other optimization techniques have been exhausted.

**D. Convert all Parquet files into CSV format to simplify processing.** - Converting Parquet files to CSV format is generally a *bad* idea for performance and cost. Parquet is a columnar storage format that is highly optimized for analytical queries and ETL processes. It offers better compression and encoding capabilities than CSV, leading to smaller file sizes and faster query performance. Converting to CSV would increase storage costs, slow down processing, and negate the benefits of using a columnar format. This would be a significant step backward in terms of performance and cost.

</details>

---

## Question 5 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0330`

A machine learning team is using SageMaker Pipelines to automate the training and deployment of multiple machine learning models. They want to scale the pipeline to handle thousands of workflows simultaneously while ensuring that steps, such as model training and evaluation, are executed in a specific sequence. Which feature of SageMaker Pipelines ensures that steps are executed in a defined order?

- **A) SageMaker Model Monitor**
- **B) Model Package**
- **C) Pipeline Parameters**
- **D) Directed Acyclic Graph (DAG)**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Correct answer: Directed Acyclic Graph (DAG)**

SageMaker Pipelines uses a Directed Acyclic Graph (DAG) to define the sequence of steps in a machine learning workflow. The DAG ensures that steps are executed in a specific order, with dependencies between steps clearly defined. This allows for the creation of complex workflows where the output of one step is used as the input for another. The DAG structure also enables parallel execution of independent steps, optimizing the overall pipeline execution time. The DAG is a core component of SageMaker Pipelines, enabling scalability and reproducibility in ML workflows.

**Incorrect:**

**A. SageMaker Model Monitor** - SageMaker Model Monitor is used to detect concept drift and data quality issues in deployed models. It does not define or enforce the execution order of steps in a SageMaker Pipeline.

**B. Model Package** - A Model Package is a container that holds all the artifacts needed to deploy a model, including the model itself, inference code, and environment dependencies. While Model Packages are used within SageMaker Pipelines, they do not define the execution order of the pipeline steps.

**C. Pipeline Parameters** - Pipeline Parameters allow you to define variables that can be used throughout the pipeline, such as learning rate or instance type. These parameters can be changed when the pipeline is executed, but they do not control the order in which the pipeline steps are executed.

</details>

---

## Question 6 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0099`

Which AWS service is primarily used for preparing and loading data for analytics, including tasks such as data cleaning and transformation?

- **A) SageMaker Ground Truth**
- **B) SageMaker Feature Store**
- **C) AWS Glue**
- **D) Amazon Mechanical Turk**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "AWS Glue"?**

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load your data for analytics. It is specifically designed for tasks such as data cleaning and transformation.

### Incorrect Options:
- **SageMaker Ground Truth**  
  While SageMaker Ground Truth is used for data labeling, it does not provide functionality for data cleaning and transformation.

- **SageMaker Feature Store**  
  SageMaker Feature Store is used for creating, managing, and sharing ML features, but it does not provide functionality for data cleaning and transformation.

- **Amazon Mechanical Turk**  
  Amazon Mechanical Turk is a crowdsourcing marketplace, but it does not provide functionality for data cleaning and transformation.

</details>

---

## Question 7 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0119`

You are troubleshooting a slow data ingestion process to Amazon S3. The data is being uploaded in large chunks, but the ingestion speed remains slow and inconsistent. You suspect that the issue is related to the way the data is being written to S3.

What is the most effective approach to resolve this issue?

- **A) Use multipart upload to upload large objects in parallel**
- **B) Use S3 Transfer Acceleration to speed up the upload**
- **C) Increase the S3 bucket’s read and write request limits**
- **D) Use Amazon Kinesis to stream data directly into S3**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Use multipart upload to upload large objects in parallel"?**

Multipart upload splits large files into smaller parts and uploads them in parallel, significantly improving the overall upload speed. This reduces the overhead of uploading large objects and is the most efficient way to handle large data ingestion into S3.

### Incorrect Options:
- **Use S3 Transfer Acceleration to speed up the upload**  
  Transfer Acceleration helps with upload speed but does not address the inefficiency of uploading large files in chunks.

- **Increase the S3 bucket’s read and write request limits**  
  S3 auto-scales to handle higher request rates, so increasing limits isn’t necessary and won’t solve slow upload speeds caused by inefficient file handling.

- **Use Amazon Kinesis to stream data directly into S3**  
  Kinesis is more suited for real-time data streaming, not ideal for handling large batch uploads or data being stored in S3 in chunks.

</details>

---

## Question 8 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0529`

Which method is best for choosing the production decision threshold for a binary classifier when you must satisfy a business constraint such as 'recall ≥ 0.9'?

- **A) Always use 0.5**
- **B) Sweep thresholds on validation data and pick one that meets the constraint with maximum precision**
- **C) Use ROC-AUC directly**
- **D) Use cross-entropy loss**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
The default 0.5 threshold rarely matches business constraints. Sweep thresholds on a validation set, build a precision-recall curve, and pick the operating point that meets the constraint with the best trade-off on the other metric. ROC-AUC and cross-entropy don't choose thresholds.

</details>

---

## Question 9 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0022`

When deploying a machine learning model in AWS, which of the following is a key reason to choose Amazon Elastic Kubernetes Service (Amazon EKS) over SageMaker endpoints?

- **A) EKS supports larger models**
- **B) EKS provides automatic versioning**
- **C) EKS allows for multi-container deployments**
- **D) EKS has lower latency for inference**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "EKS allows for multi-container deployments"?**

Amazon Elastic Kubernetes Service (Amazon EKS) supports multi-container deployments, which can be useful when you need to deploy multiple models or services together. While SageMaker also supports multi-model endpoints, it does not support multi-container deployments.

### Incorrect Options:
- **EKS supports larger models**  
  The size of the model that can be deployed is not determined by the deployment target (EKS or SageMaker), but by the resources provisioned for the deployment.

- **EKS provides automatic versioning**  
  Versioning is a deployment best practice that needs to be implemented manually, regardless of whether you are using EKS or SageMaker.

- **EKS has lower latency for inference**  
  The latency of inference is not determined by the deployment target, but by factors such as the model's complexity, the compute resources provisioned, and the deployment strategy used.

</details>

---

## Question 10 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0304`

A financial services company is building a fraud detection system to monitor transactions in real-time. They plan to use Amazon Kinesis Data Streams to ingest transaction data and want the system to scale automatically based on demand. They require low-latency for fast fraud detection responses.
Which feature of Amazon Kinesis Data Streams should the company implement to meet these requirements?

- **A) Enable provisioned mode and dynamically add shards.**
- **B) Use Kinesis Firehose to automatically scale the stream based on traffic.**
- **C) Use enhanced fan-out to reduce consumer latency and ensure dedicated throughput per consumer.**
- **D) Manually scale shards based on throughput requirements.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Correct answer: Use enhanced fan-out to reduce consumer latency and ensure dedicated throughput per consumer.**

Enhanced fan-out is a feature of Kinesis Data Streams designed to address the challenges of multiple consumers reading from the same stream. Without enhanced fan-out, consumers share the read throughput of the stream, potentially leading to increased latency and throttling. Enhanced fan-out provides each consumer with its own dedicated read throughput pipe, significantly reducing latency and improving performance, which is crucial for real-time fraud detection. It also allows for more consumers to read from the stream concurrently without impacting each other's performance. This directly addresses the requirement for low-latency and scalability in the fraud detection system.

**Incorrect:**

**A. Enable provisioned mode and dynamically add shards.** - While dynamically adding shards (auto-scaling) is important for handling varying data volumes, it doesn't directly address the latency issues associated with multiple consumers sharing the same read throughput. Provisioned mode itself doesn't inherently reduce latency; it simply allows you to manage the stream's capacity. Auto-scaling helps with throughput capacity but not consumer-specific latency.

**B. Use Kinesis Firehose to automatically scale the stream based on traffic.** - Kinesis Firehose is designed for loading data into data lakes and other storage destinations, not for real-time processing and analysis. It's not suitable for low-latency fraud detection because it focuses on batch delivery and data transformation before storage, adding latency. Kinesis Data Streams is the appropriate service for real-time data ingestion and processing.

**D. Manually scale shards based on throughput requirements.** - Manually scaling shards is a valid approach to managing Kinesis Data Streams capacity, but it's not ideal for a system requiring automatic scaling and low latency. Manual scaling requires constant monitoring and intervention, which is not efficient or responsive enough for real-time fraud detection. Furthermore, manually scaling shards does not address the consumer-specific latency issues that enhanced fan-out solves.

</details>

---

## Question 11 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0063`

You are tasked with storing structured data that needs to be ingested for real-time analytics. The data will be processed frequently, and you need to ensure low latency and cost efficiency.

Considering both the cost and performance of various storage options, which is the most suitable storage solution for your use case?

- **A) Use Amazon S3 with CSV format for simple storage and access**
- **B) Use Amazon EFS for scalable file storage with low latency**
- **C) Use Amazon S3 with Parquet format for optimized querying and cost-efficiency**
- **D) Use Amazon DynamoDB for low-latency, high-throughput storage**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "Use Amazon S3 with Parquet format for optimized querying and cost-efficiency"?**

Parquet is a columnar storage format optimized for analytics, offering efficient querying and reduced storage costs due to its compression. S3 with Parquet is highly cost-effective for structured data that needs frequent access and querying.

### Incorrect Options:
- **Use Amazon S3 with CSV format for simple storage and access**  
  While CSV is easy to use, it’s not optimized for large-scale data analytics due to its inefficiency in storage and querying.

- **Use Amazon EFS for scalable file storage with low latency**  
  EFS is good for file-based workloads but not as cost-effective or optimized for structured data analytics as Parquet in S3.

- **Use Amazon DynamoDB for low-latency, high-throughput storage**  
  DynamoDB is ideal for transactional workloads, but it is not suited for large-scale data analytics or high-volume data storage compared to S3 with Parquet.

</details>

---

## Question 12 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0505`

Which Bedrock foundation model family is created by Amazon and offered for text and embedding tasks?

- **A) Claude**
- **B) Llama**
- **C) Titan**
- **D) Mistral**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
Amazon Titan is AWS's own foundation model family, offering Titan Text models and Titan Embeddings. Claude is from Anthropic, Llama from Meta, Mistral from Mistral AI — all available on Bedrock alongside Titan, Cohere, AI21, and Stability AI.

</details>

---

## Question 13 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0471`

Which validation strategy partitions data into k folds and trains the model k times to estimate generalization error more reliably than a single holdout?

- **A) k-fold cross-validation**
- **B) Holdout validation**
- **C) Bootstrapping**
- **D) Stratified sampling**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
k-fold cross-validation splits data into k folds, trains on k-1 folds and tests on the held-out fold, repeating k times. The averaged metric is a more stable estimate than a single train/test split. Bootstrapping samples with replacement; stratified sampling preserves class proportions but is a sampling approach.

</details>

---

## Question 14 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0048`

A team manages prompts in Amazon Bedrock Prompt Management and needs to test a revised prompt against the current production prompt without changing the prompt version used by the application. They want the application to select either prompt version at runtime through a stable identifier. What should the team do?

- **A) Edit the production prompt in place**
- **B) Copy the prompt into a Bedrock agent**
- **C) Create a prompt version and use a prompt router**
- **D) Create a prompt version and invoke it by version ARN**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "Create a prompt version and invoke it by version ARN"?**

Amazon Bedrock Prompt Management supports creating immutable prompt versions. The team can keep the production version unchanged, create a revised version for testing, and invoke the selected version by its version-specific ARN. This provides explicit version selection, but the application must choose which ARN to invoke; Prompt Management does not provide a prompt router that automatically routes between versions.

### Incorrect Options:
- **Create a prompt version and use a prompt router**
  Prompt Management does not provide a prompt router that selects between prompt versions through a stable identifier.

- **Edit the production prompt in place**
  Changing the production prompt in place would not preserve the current prompt unchanged for comparison and rollback.

- **Copy the prompt into a Bedrock agent**
  An agent is for orchestrating model calls and actions; copying the prompt there does not provide Prompt Management's version-specific prompt selection.

</details>

---

## Question 15 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0197`

Which AWS service is primarily used to automate the steps required for releasing your software changes in a machine learning workflow?

- **A) Amazon SageMaker**
- **B) AWS CodePipeline**
- **C) AWS CodeBuild**
- **D) AWS CodeDeploy**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "AWS CodePipeline"?**

AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define. This makes it the most appropriate service for automating the steps required for releasing software changes in a machine learning workflow.

### Incorrect Options:
- **Amazon SageMaker**  
  Amazon SageMaker is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. It's used for building, training, and deploying ML models, not for automating the release of software changes.

- **AWS CodeBuild**  
  AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. It's used for building and testing the code but not for automating the release of software changes.

- **AWS CodeDeploy**  
  AWS CodeDeploy is a deployment service that automates application deployments to specified compute environments. It's used to deploy the application but not for automating the release of software changes.

</details>

---

## Question 16 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0274`

What is a common method to reduce prediction bias in a dataset before training a machine learning model?

- **A) Increasing the size of the dataset**
- **B) Using a different machine learning algorithm**
- **C) Shuffling the dataset**
- **D) Removing outliers from the dataset**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "Shuffling the dataset"?**

Shuffling the dataset is a common method to reduce prediction bias before training a machine learning model. It ensures that each data point creates an "independent" change on the model, without being biased by the same points before them.

### Incorrect Options:
- **Increasing the size of the dataset**  
  Simply increasing the size of the dataset without addressing the prediction bias will not solve the problem. The prediction bias will persist if the additional data maintains the same distribution.

- **Using a different machine learning algorithm**  
  While some algorithms may be more robust to prediction bias than others, simply changing the algorithm without addressing the underlying prediction bias is not a solution.

- **Removing outliers from the dataset**  
  While this can help improve the performance of a machine learning model, it does not specifically address prediction bias.

</details>

---

## Question 17 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0523`

Which Amazon Bedrock pricing model offers guaranteed throughput (tokens per minute) for production workloads at a committed price?

- **A) On-demand pricing**
- **B) Provisioned Throughput**
- **C) Spot pricing**
- **D) Reserved Instances**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
Bedrock Provisioned Throughput reserves capacity for a model with a committed throughput, suitable for predictable, latency-sensitive workloads. On-demand bills per token without throughput guarantees. Spot/Reserved are EC2 concepts.

</details>

---

## Question 18 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0321`

A Machine Learning Engineer is using Amazon SageMaker to build and train a binary classification model. The training dataset contains a severe class imbalance, with 95% of the data belonging to the negative class and only 5% to the positive class. After training, the model achieves high accuracy but performs poorly on the positive class.
Which two techniques should the engineer consider to address this issue? (Choose TWO.)

- **A) Use precision as the primary evaluation metric instead of accuracy.**
- **B) Use the area under the ROC curve (AUC) as the evaluation metric.**
- **C) Decrease the size of the negative class through undersampling.**
- **D) Apply class weights to penalize misclassification of the minority class.**
- **E) Increase the size of the positive class through oversampling.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D, E`

**Architectural Rationale:**
**Correct answer: Apply class weights to penalize misclassification of the minority class.**

Class weights adjust the loss function during training to penalize misclassifications of the minority class (positive class in this case) more heavily than misclassifications of the majority class. This helps the model to pay more attention to the positive class and improve its performance on that class.  SageMaker algorithms often support class weighting as a hyperparameter. For example, XGBoost has a `scale_pos_weight` parameter, and Linear Learner has a `balance_classes` option.  By increasing the weight of the positive class, the model is incentivized to correctly classify these instances, leading to improved recall and F1-score, which are more appropriate metrics for imbalanced datasets than accuracy.

**Correct answer: Increase the size of the positive class through oversampling.**

Oversampling involves increasing the number of instances in the minority class. This can be achieved by duplicating existing samples (random oversampling) or by creating synthetic samples (e.g., using SMOTE - Synthetic Minority Oversampling Technique). By increasing the representation of the positive class, the model is exposed to more examples of this class during training, which can help it to learn the characteristics of the positive class better and improve its performance. This is a common technique to combat class imbalance and can be implemented using libraries like imbalanced-learn.

**Incorrect:**

**A. Use precision as the primary evaluation metric instead of accuracy.** - While precision is a useful metric, especially when false positives are costly, using it *alone* is insufficient. A model could achieve high precision by only predicting the positive class when it is extremely confident, but this might lead to a very low recall (missing many positive instances).  Therefore, precision should be considered alongside recall (e.g., using the F1-score) or AUC, not as a replacement for all other metrics.

**B. Use the area under the ROC curve (AUC) as the evaluation metric.** - AUC is a good evaluation metric for imbalanced datasets because it measures the model's ability to distinguish between the two classes, regardless of the class distribution. It is less sensitive to class imbalance than accuracy. However, using AUC as the *sole* solution doesn't directly address the underlying problem of the model not learning the positive class effectively. It only helps in evaluating the model's performance.  It should be used in conjunction with techniques that modify the training process to better handle the imbalance.

**C. Decrease the size of the negative class through undersampling.** - Undersampling can help balance the dataset, but it also discards potentially useful information from the majority class. In this scenario, where the positive class is severely underrepresented (only 5%), discarding data from the negative class might further degrade the model's ability to learn the overall data distribution and could lead to a loss of important information that could help in distinguishing between the classes. Oversampling or class weighting are generally preferred when the minority class is very small.

</details>

---

## Question 19 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0394`

A media company wants to build an automated video transcription and translation pipeline. They need to transcribe speech from videos, translate the text into multiple languages, and create audio versions of the translated text. Which AWS services would fulfill these requirements?

- **A) Use AWS Glue for transcription, Amazon Translate for text translation, and AWS Lambda to convert the translated text to speech.**
- **B) Use Amazon Transcribe to convert speech to text, Amazon SageMaker for text translation, and Amazon Rekognition for speech synthesis.**
- **C) Use Amazon Transcribe to convert speech to text, Amazon Translate for text translation, and Amazon Polly to convert translated text to speech.**
- **D) Use Amazon Rekognition for transcription, AWS Lambda for text translation, and Amazon Polly for speech synthesis.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Correct answer: Use Amazon Transcribe to convert speech to text, Amazon Translate for text translation, and Amazon Polly to convert translated text to speech.**

This option provides the correct services for each step of the video transcription and translation pipeline. Amazon Transcribe is specifically designed for converting speech to text. Amazon Translate is a neural machine translation service that accurately translates text between languages. Amazon Polly is a text-to-speech service that converts text into lifelike speech, enabling the creation of audio versions of the translated text. This combination of services directly addresses the requirements of the media company.

**Incorrect:**

**A. Use AWS Glue for transcription, Amazon Translate for text translation, and AWS Lambda to convert the translated text to speech.** - AWS Glue is an ETL (Extract, Transform, Load) service primarily used for data integration and preparing data for analytics. It is not designed for speech-to-text transcription. While AWS Lambda could potentially be used with a third-party text-to-speech library, Amazon Polly is a more suitable and managed service for this purpose.

**B. Use Amazon Transcribe to convert speech to text, Amazon SageMaker for text translation, and Amazon Rekognition for speech synthesis.** - Amazon SageMaker is a comprehensive machine learning platform that can be used for various tasks, including text translation. However, Amazon Translate is a more specialized and cost-effective service for this specific use case. Amazon Rekognition is primarily used for image and video analysis, not speech synthesis. Amazon Polly is the correct service for converting text to speech.

**D. Use Amazon Rekognition for transcription, AWS Lambda for text translation, and Amazon Polly for speech synthesis.** - Amazon Rekognition is designed for image and video analysis, not speech-to-text transcription. Amazon Transcribe is the appropriate service for this task. While AWS Lambda could be used with a third-party translation library, Amazon Translate is a more suitable and managed service for text translation.

</details>

---

## Question 20 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0408`

You are a data scientist at a healthcare company tasked with building a predictive model using SageMaker. Your team wants to avoid the complexity of managing infrastructure and prefers a solution that minimizes setup time.
Which of the following SageMaker features would be MOST appropriate for your use case?

- **A) Build a custom container with proprietary algorithms and manage the infrastructure manually for optimized performance.**
- **B) Build your own deep learning model using TensorFlow or PyTorch and manually deploy it on an Amazon EC2 instance.**
- **C) Use SageMaker’s built-in algorithms, which come pre-packaged in containers, requiring only data input and hyperparameter setup.**
- **D) Use SageMaker Ground Truth to automatically handle infrastructure setup and dataset labeling.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Correct answer: Use SageMaker’s built-in algorithms, which come pre-packaged in containers, requiring only data input and hyperparameter setup.**

SageMaker's built-in algorithms are designed to reduce the complexity of machine learning model development and deployment. These algorithms are pre-packaged in containers, meaning the infrastructure and dependencies are already managed by AWS. This allows data scientists to focus on data input and hyperparameter tuning, significantly minimizing setup time and infrastructure management overhead. This aligns perfectly with the team's desire to avoid infrastructure complexity and minimize setup time.

**Incorrect:**

**A. Build a custom container with proprietary algorithms and manage the infrastructure manually for optimized performance.** - While building a custom container offers maximum flexibility and control for optimizing performance, it introduces significant complexity and management overhead, directly contradicting the requirement to minimize setup time and avoid infrastructure management.

**B. Build your own deep learning model using TensorFlow or PyTorch and manually deploy it on an Amazon EC2 instance.** - Manually deploying a deep learning model on an EC2 instance involves significant infrastructure management, including setting up the environment, installing dependencies, and configuring networking. This approach is time-consuming and complex, failing to meet the requirement of minimizing setup time and avoiding infrastructure management.

**D. Use SageMaker Ground Truth to automatically handle infrastructure setup and dataset labeling.** - SageMaker Ground Truth is primarily used for data labeling, which is a crucial step in the machine learning pipeline, but it doesn't directly address the core issue of simplifying model deployment and minimizing infrastructure management for the model training and inference phases. While helpful, it is not the MOST appropriate feature for the stated use case.

</details>

---

## Question 21 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0155`

A team deploys a tool-using agent on Amazon Bedrock AgentCore Runtime. It must identify which individual agent sessions drive unusually high CPU and memory use over time, while retaining session-level telemetry for analysis in Amazon CloudWatch. Which approach best meets these requirements?

- **A) Enable AgentCore Runtime observability with session tracing**
- **B) Use CloudWatch metrics for the runtime fleet only**
- **C) Inspect Bedrock model invocation logs**
- **D) Set CloudWatch alarms on account-level CPU**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Enable AgentCore Runtime observability with session tracing"?**

AgentCore Runtime observability provides runtime telemetry, including resource utilization, and session-level traces that can be sent to Amazon CloudWatch. This lets the team correlate resource-consumption patterns with individual agent sessions rather than seeing only aggregate usage.

### Incorrect Options:
- **Use CloudWatch metrics for the runtime fleet only**  
  Fleet-level metrics can reveal overall utilization but cannot identify which individual sessions are responsible for unusually high consumption.

- **Inspect Bedrock model invocation logs**  
  Invocation logs help analyze model requests and responses, but they do not provide the session-correlated CPU and memory telemetry required here.

- **Set CloudWatch alarms on account-level CPU**  
  Account-level alarms can signal a broad resource threshold but do not retain or attribute consumption patterns to individual agent sessions.

</details>

---

## Question 22 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0068`

What is a key consideration when implementing data anonymization for a machine learning project?

- **A) Anonymizing only the target variable**
- **B) Ensuring the utility of the data is preserved**
- **C) Anonymizing all data types the same way**
- **D) Anonymizing data after model training**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Ensuring the utility of the data is preserved"?**

While data anonymization is crucial for protecting sensitive information, it's important to ensure that the utility of the data is preserved. If the anonymization process alters the data too much, it can impact the performance of the machine learning model as the model may not be able to learn effectively from the data.

### Incorrect Options:
- **Anonymizing all data types the same way**  
  Different types of data may require different anonymization techniques. It's not advisable to use the same technique for all data types.

- **Anonymizing data after model training**  
  Data should be anonymized before model training to ensure that the model does not learn from sensitive data.

- **Anonymizing only the target variable**  
  It's not sufficient to only anonymize the target variable. Any variable that contains sensitive information should be anonymized.

</details>

---

## Question 23 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0138`

A company uses an Amazon Bedrock knowledge base backed by Amazon OpenSearch Serverless. Documents in Amazon S3 are updated daily, but users continue receiving answers grounded in old content. The ingestion job reports success, and the knowledge base uses the intended embedding model and vector index. What should the team do to ensure the changed S3 documents are reflected in retrieval?

- **A) Change the embedding model to a larger model**
- **B) Increase the number of retrieved results**
- **C) Recreate the OpenSearch Serverless vector index**
- **D) Start a new ingestion job after the S3 updates**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "Start a new ingestion job after the S3 updates"?**

Amazon Bedrock knowledge bases do not automatically re-index changed data source content. Starting an ingestion job synchronizes the data source: it processes new or changed documents, updates their vectors and metadata, and removes records for deleted documents. Running ingestion after the S3 updates makes the refreshed content available for retrieval.

### Incorrect Options:
- **Recreate the OpenSearch Serverless vector index**
  The index is already configured correctly. Recreating it does not ingest the updated S3 documents and can disrupt existing indexed data.

- **Increase the number of retrieved results**
  Retrieving more results cannot surface document versions that have not been re-ingested into the knowledge base.

- **Change the embedding model to a larger model**
  Changing the embedding model is not needed to synchronize updated source documents and can require re-embedding the indexed content.

</details>

---

## Question 24 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0058`

What is a key consideration when using resampling to address class imbalance in a machine learning dataset?

- **A) Resampling after model training**
- **B) Avoiding overfitting to the resampled data**
- **C) Resampling only the majority class**
- **D) Resampling all classes equally**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Avoiding overfitting to the resampled data"?**

Resampling is a common strategy to address class imbalance in a dataset. However, a key consideration when using this strategy is to avoid overfitting to the resampled data. Overfitting occurs when a model learns the training data too well, to the point where it performs poorly on unseen data. If a model is trained on resampled data, it may perform well on that data but poorly on new, real-world data that has not been resampled.

### Incorrect Options:
- **Resampling all classes equally**  
  The purpose of resampling is to address class imbalance, so it would not make sense to resample all classes equally.

- **Resampling only the majority class**  
  Resampling can involve either oversampling the minority class, undersampling the majority class, or a combination of both. Resampling only the majority class may not be sufficient to address the imbalance.

- **Resampling after model training**  
  Resampling should be done before model training, not after. The purpose of resampling is to create a more balanced training set for the model.

</details>

---

## Question 25 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0142`

A financial services company uses a foundation model available in Amazon Bedrock to classify support messages into its proprietary set of categories. The model understands the messages but frequently confuses categories whose distinctions depend on internal policy language. The company has a small labeled dataset, must keep training costs low, and wants to adapt the model’s behavior without updating all of its weights. Which approach best meets these requirements?

- **A) Use few-shot prompts with labeled examples**
- **B) Fine-tune with parameter-efficient adaptation**
- **C) Perform full fine-tuning on labeled messages**
- **D) Continue pre-training on unlabeled messages**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Fine-tune with parameter-efficient adaptation"?**

Parameter-efficient fine-tuning updates a small subset of model parameters while using labeled examples to adapt the model to the company’s task and category distinctions. It fits the requirement to change model behavior at lower training cost without updating all model weights, when supported by the selected model and fine-tuning workflow.

### Incorrect Options:
- **Continue pre-training on unlabeled messages**
  Continued pre-training can help a model learn domain language, but unlabeled data does not directly teach the proprietary classification labels and decision boundaries.

- **Perform full fine-tuning on labeled messages**
  Full fine-tuning can adapt the model to the task, but it updates all model weights and conflicts with the requirement to limit training cost and avoid updating all weights.

- **Use few-shot prompts with labeled examples**
  Few-shot prompting can guide predictions without training, but it does not fine-tune the model and may not reliably resolve persistent confusion in policy-specific category boundaries.

</details>

---

## Question 26 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0332`

A company is using Amazon S3 to store sensitive business documents. To enhance security, they want to grant access to the S3 bucket only to certain IAM users, while denying access to others. Additionally, the company requires the S3 bucket to be accessed by an EC2 instance running in a different AWS account, but only for reading data.
Which combination of AWS IAM features should be used to meet these requirements? (Choose TWO)

- **A) Use a customer-managed IAM policy attached to the S3 bucket to define granular access for the EC2 instance and the IAM users.**
- **B) Use an identity-based policy to attach to IAM users that grants or denies access to the S3 bucket.**
- **C) Create a role in the other AWS account with a trust policy allowing the EC2 instance to assume the role and read from the S3 bucket.**
- **D) Use AWS Lambda to check the IAM users permissions before allowing access to the S3 bucket.**
- **E) Apply a resource-based bucket policy in Amazon S3 to explicitly deny access from all users except the EC2 instance and required IAM users.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B, C`

**Architectural Rationale:**
**Correct answer: Use an identity-based policy to attach to IAM users that grants or denies access to the S3 bucket.**

Identity-based policies (IAM policies) are attached to IAM users, groups, or roles. These policies define what actions the identity can perform on AWS resources. By attaching a policy to specific IAM users, you can grant or deny them access to the S3 bucket, fulfilling the requirement of controlling user access. This is a standard method for managing IAM user permissions.

**Correct answer: Create a role in the other AWS account with a trust policy allowing the EC2 instance to assume the role and read from the S3 bucket.**

To allow the EC2 instance in another AWS account to access the S3 bucket, you should create an IAM role in the *other* account (the account where the EC2 instance resides). This role's trust policy should allow the EC2 instance to assume it. The role should also have permissions to read from the S3 bucket. This cross-account access pattern is a secure way to grant permissions to resources in different AWS accounts.

**Incorrect:**

**A. Use a customer-managed IAM policy attached to the S3 bucket to define granular access for the EC2 instance and the IAM users.** - While you *can* use a resource-based policy (bucket policy) on the S3 bucket, attaching a customer-managed IAM policy to the S3 bucket is not possible. Customer-managed policies are attached to IAM identities (users, groups, roles), not directly to resources. Resource-based policies (like bucket policies) are attached to resources.

**D. Use AWS Lambda to check the IAM users permissions before allowing access to the S3 bucket.** - Using Lambda to gate access to S3 is an overly complex and inefficient approach. IAM and S3 bucket policies provide built-in access control mechanisms. Introducing Lambda adds unnecessary overhead, latency, and operational complexity. It's better to use the native IAM and S3 access control features.

**E. Apply a resource-based bucket policy in Amazon S3 to explicitly deny access from all users except the EC2 instance and required IAM users.** - While a bucket policy is a valid approach for controlling access, it's generally better practice to use *both* identity-based policies (attached to IAM users) *and* resource-based policies (bucket policies). Identity-based policies provide fine-grained control at the user level, while resource-based policies provide an additional layer of security at the bucket level. Furthermore, the question specifically asks about using IAM features. Option E focuses primarily on S3 bucket policies, not IAM.

</details>

---

## Question 27 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0424`

A retail company is using Amazon Personalize to provide personalized product recommendations based on real-time customer behavior on their e-commerce platform. They want to integrate Amazon DynamoDB to store customer session data, use Amazon Kinesis for real-time event streaming, and leverage Amazon S3 for historical data storage. Additionally, they need the solution to scale during peak shopping periods, such as holidays. Which of the following strategies should they implement? (Choose TWO.)

- **A) Use Amazon Personalize to directly process real-time streaming data from Amazon Kinesis and Amazon DynamoDB.**
- **B) Use Amazon EC2 Auto Scaling to manage the increasing number of personalized recommendation requests during peak traffic.**
- **C) Store session data in Amazon RDS for high availability and scalability during peak traffic.**
- **D) Use AWS Lambda to trigger real-time updates to Amazon Personalize when new customer events are detected in Amazon DynamoDB.**
- **E) Store historical customer interaction data in Amazon S3 and periodically feed it into Amazon Personalize for batch training.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D, E`

**Architectural Rationale:**
**Correct answer: Use AWS Lambda to trigger real-time updates to Amazon Personalize when new customer events are detected in Amazon DynamoDB.**

AWS Lambda can be used to create a trigger that automatically updates Amazon Personalize whenever new customer events are added to Amazon DynamoDB. This allows for near real-time personalization based on the latest customer behavior.  Lambda functions can process the new data and send it to Amazon Personalize using the PutEvents API. This ensures that the recommendations are always up-to-date with the most recent customer interactions, which is crucial for a retail company aiming to provide relevant product recommendations.

**Correct answer: Store historical customer interaction data in Amazon S3 and periodically feed it into Amazon Personalize for batch training.**

Amazon S3 is an ideal storage solution for historical customer interaction data due to its scalability and cost-effectiveness. Amazon Personalize uses this historical data to train and improve its recommendation models. Periodically feeding the data from S3 into Amazon Personalize allows the models to learn from past customer behavior and provide more accurate and relevant recommendations. This is a standard practice in machine learning to improve model performance over time.

**Incorrect:**

**A. Use Amazon Personalize to directly process real-time streaming data from Amazon Kinesis and Amazon DynamoDB.** - Amazon Personalize does not directly process data from both Amazon Kinesis and Amazon DynamoDB simultaneously for real-time updates. While it integrates with Kinesis for real-time event ingestion, DynamoDB is typically used to store user and item metadata, which is accessed during model training or through Lambda functions triggered by DynamoDB events.  Directly processing both streams in real-time by Personalize is not the intended architecture.

**B. Use Amazon EC2 Auto Scaling to manage the increasing number of personalized recommendation requests during peak traffic.** - Amazon Personalize is a fully managed service and automatically scales to handle increasing request volumes. You do not need to manage EC2 instances or configure Auto Scaling groups for Personalize itself.  The service handles the scaling of its underlying infrastructure.

**C. Store session data in Amazon RDS for high availability and scalability during peak traffic.** - While Amazon RDS provides high availability and scalability, Amazon DynamoDB is a better choice for storing session data in this scenario. DynamoDB is a NoSQL database that is designed for high-throughput, low-latency access, which is ideal for handling real-time session data. RDS is more suitable for structured data with complex relationships, which is not the primary characteristic of session data. DynamoDB also integrates well with other AWS services like Lambda and Kinesis.

</details>

---

## Question 28 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0054`

Which AWS service is primarily used for data deduplication and transformation in preparation for machine learning tasks?

- **A) Amazon Redshift**
- **B) AWS Glue DataBrew**
- **C) Amazon S3**
- **D) Amazon RDS**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "AWS Glue DataBrew"?**

AWS Glue DataBrew is a visual data preparation tool that makes it easy to clean and normalize data for analysis and machine learning. It provides over 250 pre-built transformations to automate data preparation tasks, such as filtering anomalies, standardizing formats, and deduplicating data, without the need to write any code.

### Incorrect Options:
- **Amazon S3**  
  Amazon S3 is a storage service, it does not provide the functionality for data transformation and cleaning.

- **Amazon Redshift**  
  Amazon Redshift is a data warehousing service, but it does not provide the functionality for data transformation and cleaning.

- **Amazon RDS**  
  Amazon RDS is a relational database service, but it does not provide the functionality for data transformation and cleaning.

</details>

---

## Question 29 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0426`

In SageMaker Pipelines, which component is used to define the sequence of operations such as data pre-processing, model training, and model registration?

- **A) Model Package**
- **B) Model Group**
- **C) Pipeline SDK**
- **D) Pipeline Definition**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Correct answer: Pipeline Definition**

The Pipeline Definition in SageMaker Pipelines is a JSON or YAML file that specifies the entire workflow of your machine learning pipeline. It defines the sequence of steps or components, including data pre-processing, model training, evaluation, and model registration. The Pipeline Definition outlines the dependencies between these steps and how data flows through the pipeline. It's the core component that orchestrates the end-to-end ML process. Using the Pipeline Definition, SageMaker Pipelines can automate the execution of these steps, track lineage, and manage dependencies, ensuring reproducibility and efficient ML workflows.

**Incorrect:**

**A. Model Package** - A Model Package is an archive that contains all the necessary components for deploying a model, such as the model artifacts, inference code, and environment dependencies. While it's a crucial part of the deployment process, it doesn't define the sequence of operations within a pipeline.

**B. Model Group** - A Model Group is a logical grouping of model versions. It's used for managing and tracking different versions of a model, often in the context of model deployment strategies like A/B testing or shadow deployments. It doesn't define the pipeline's structure or the sequence of operations.

**C. Pipeline SDK** - The Pipeline SDK (Software Development Kit) provides the tools and libraries needed to define and create SageMaker Pipelines programmatically. While you use the SDK to *create* a Pipeline Definition, the SDK itself is not the definition. The Pipeline Definition is the resulting specification of the pipeline created using the SDK.

</details>

---

## Question 30 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0378`

A company needs to ensure that its machine learning models are ethically developed by reducing bias and detecting potential vulnerabilities in the output. How can Amazon SageMaker Ground Truth help in this process?

- **A) By using Ground Truth‘s fully automated labeling system to eliminate all bias from the training data.**
- **B) By leveraging Ground Truths human-in-the-loop feedback mechanism to review and correct model outputs for bias and vulnerabilities.**
- **C) By using Ground Truth only for labeling data, leaving bias detection to other AWS services like SageMaker Clarify.**
- **D) By exclusively relying on third-party vendors to detect bias and vulnerabilities in model outputs.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Correct answer: By leveraging Ground Truths human-in-the-loop feedback mechanism to review and correct model outputs for bias and vulnerabilities.**

Amazon SageMaker Ground Truth provides a human-in-the-loop (HITL) mechanism that allows human reviewers to actively participate in the machine learning workflow. This is crucial for identifying and mitigating bias and vulnerabilities in model outputs. Human reviewers can assess model predictions, provide feedback on potentially biased or unfair outcomes, and correct errors. This feedback is then used to retrain the model, improving its fairness and robustness. This iterative process helps ensure that the model is ethically developed and aligned with the company's values.

**Incorrect:**

**A. By using Ground Truth‘s fully automated labeling system to eliminate all bias from the training data.** - While Ground Truth can automate labeling tasks, it does not eliminate bias automatically. Automated labeling can even perpetuate existing biases if the underlying data or algorithms are biased. Human review is necessary to identify and correct these biases.

**C. By using Ground Truth only for labeling data, leaving bias detection to other AWS services like SageMaker Clarify.** - While SageMaker Clarify is a valuable tool for bias detection, Ground Truth's human-in-the-loop capabilities are essential for actively mitigating bias during the data labeling and model training phases. Ground Truth and Clarify can be used together for a more comprehensive approach to ethical model development. Ground Truth is not *only* for labeling data.

**D. By exclusively relying on third-party vendors to detect bias and vulnerabilities in model outputs.** - While third-party vendors can provide valuable expertise, relying exclusively on them without leveraging Ground Truth's capabilities is not the most effective approach. Ground Truth allows the company to build internal expertise and control over the bias detection and mitigation process. Furthermore, using Ground Truth allows for continuous monitoring and improvement of the model's fairness and robustness, which may not be possible with a one-time assessment by a third-party vendor.

</details>

---

## Question 31 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0107`

A media company receives images, audio recordings, and text files from thousands of devices. It must preserve the original files durably, accept uploads directly from devices, and organize the objects by device and capture time for later ML processing; the files do not need to be queried as records during ingestion. Which design best meets these requirements?

- **A) Store each file as a DynamoDB binary attribute**
- **B) Stream file contents through Amazon Kinesis Data Streams**
- **C) Load all files into Amazon Redshift as SUPER values**
- **D) Upload objects to Amazon S3 using presigned URLs and partitioned keys**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "Upload objects to Amazon S3 using presigned URLs and partitioned keys"?**

Amazon S3 durably stores files of diverse types as objects without requiring a fixed schema. Presigned URLs let devices upload directly to S3 without receiving AWS credentials, while keys organized by device and capture time support downstream discovery and processing. This matches the requirement to retain original files rather than query them as records during ingestion.

### Incorrect Options:
- **Store each file as a DynamoDB binary attribute**
  DynamoDB is designed for item-based access, not economical storage of large media files. Binary attributes also have a 400 KB item-size limit.

- **Load all files into Amazon Redshift as SUPER values**
  Redshift is a data warehouse for analytics, not a durable object store for original media files. Its semi-structured data support does not make it appropriate for storing arbitrary file objects.

- **Stream file contents through Amazon Kinesis Data Streams**
  Kinesis Data Streams is intended for real-time streaming records, not durable storage of large original media objects. Its record-size limit makes it unsuitable for many images and audio files.

</details>

---

## Question 32 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0174`

Why might you choose to use AWS Cloud Development Kit (CDK) over AWS CloudFormation for automating the provisioning of compute resources in a machine learning solution?

- **A) CDK supports more AWS services**
- **B) CDK is less expensive than CloudFormation**
- **C) CDK has built-in auto-scaling features**
- **D) CDK allows coding in familiar languages**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "CDK allows coding in familiar languages"?**

The AWS Cloud Development Kit (CDK) is an open-source software development framework to define cloud infrastructure in code and provision it through AWS CloudFormation. The main advantage of CDK over CloudFormation is that it allows developers to define their cloud resources using familiar programming languages such as JavaScript, TypeScript, Python, Java, or C#. This can make it easier to manage and update the infrastructure, especially for developers already comfortable with these languages.

### Incorrect Options:
- **CDK supports more AWS services**  
  Both CDK and CloudFormation support a wide range of AWS services. The difference is not in the number of services supported, but in the way resources for these services are defined and managed.

- **CDK is less expensive than CloudFormation**  
  Both CDK and CloudFormation are free to use. You only pay for the AWS resources (such as EC2 instances, Lambda functions, etc.) that you create to store and run your application.

- **CDK has built-in auto-scaling features**  
  Auto-scaling is a feature of the specific AWS service (like EC2, ECS, etc.), not of the infrastructure as code (IaC) tool used to provision the service. Both CDK and CloudFormation can be used to define auto-scaling policies, but the actual scaling is handled by the service itself.

</details>

---

## Question 33 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0265`

A company runs an inference service on Amazon EC2 that invokes Amazon Bedrock foundation models. The service must authenticate without storing long-lived secrets, and its permissions must be limited to invoking approved models in one AWS account. Which credential type should the service use?

- **A) A presigned S3 URL for each model invocation**
- **B) Amazon Bedrock API key stored in Secrets Manager**
- **C) Long-term IAM access keys in environment variables**
- **D) EC2 instance profile with scoped IAM permissions**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "EC2 instance profile with scoped IAM permissions"?**

An EC2 instance profile provides temporary credentials through its IAM role, avoiding stored long-lived secrets. The role can be restricted with permissions such as `bedrock:InvokeModel` for the approved foundation models, satisfying both credential-management and least-privilege requirements.

### Incorrect Options:
- **Amazon Bedrock API key stored in Secrets Manager**  
  Bedrock API keys are a supported authentication option, but storing and managing a key is unnecessary here. The EC2 workload can use its instance profile for temporary credentials and IAM-based access control.

- **Long-term IAM access keys in environment variables**  
  These are long-lived secrets that can be exposed or require rotation. An instance profile supplies temporary credentials without embedding keys in the workload.

- **A presigned S3 URL for each model invocation**  
  Presigned S3 URLs grant time-limited access to S3 objects; they do not authenticate requests to invoke Amazon Bedrock models.

</details>

---

## Question 34 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0383`

You are tasked with building an AI application using Amazon Bedrock. The application will experience variable traffic, with periods of very high usage followed by long idle times. Which pricing option is the MOST cost-effective for this use case?

- **A) Provisioned throughput mode**
- **B) Reserved instance pricing**
- **C) On-demand pricing**
- **D) Spot instance pricing**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Correct answer: On-demand pricing**

On-demand pricing for Amazon Bedrock is the most cost-effective option for applications with variable traffic, characterized by periods of high usage followed by long idle times. With on-demand pricing, you only pay for what you use, meaning you incur costs only during the periods of high usage and pay nothing during idle times. This aligns perfectly with the described traffic pattern, minimizing overall expenses. This is a common cost optimization strategy for workloads with unpredictable or bursty usage patterns.

**Incorrect:**

**A. Provisioned throughput mode** - Provisioned throughput mode is suitable for applications with consistent and predictable traffic patterns. It involves reserving a specific amount of compute capacity for your application. If the application experiences long idle times, you would still be paying for the reserved capacity, making it less cost-effective than on-demand pricing for variable traffic.

**B. Reserved instance pricing** - Reserved instance pricing is generally used for EC2 instances and not directly applicable to Amazon Bedrock's pricing structure. Even if it were, reserved instances are best suited for steady-state, predictable workloads. The long idle times would result in wasted reserved capacity, making it more expensive than on-demand pricing.

**D. Spot instance pricing** - Spot instance pricing is not applicable to Amazon Bedrock. Spot instances are available for EC2 and offer discounted pricing in exchange for the possibility of interruption. Bedrock does not offer spot instance pricing.

</details>

---

## Question 35 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0062`

Which technique is most effective for monitoring both data quality and model performance in a production environment?

- **A) Manual inspection of data**
- **B) Using SageMaker Model Monitor**
- **C) Periodic retraining of the model**
- **D) Running batch predictions regularly**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Using SageMaker Model Monitor"?**

SageMaker Model Monitor is a service provided by AWS that allows for continuous monitoring of both data quality and model performance in a production environment. It can detect drift in data and model behavior, enabling timely updates or retraining of the model.

### Incorrect Options:
- **Manual inspection of data**  
  This is not practical or scalable for large datasets or complex models in production.

- **Periodic retraining of the model**  
  While this can help maintain model performance, it does not directly monitor data quality.

- **Running batch predictions regularly**  
  This can provide insights into model performance but does not directly monitor data quality.

</details>

---

## Question 36 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0194`

In the context of using SageMaker with TensorFlow, which of the following methods can be used to reduce the model training time without compromising the model's performance?

- **A) Use early stopping**
- **B) Increase the batch size**
- **C) Decrease the number of epochs**
- **D) Increase the learning rate**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Use early stopping"?**

Early stopping is a form of regularization used to avoid overfitting when training a learner with an iterative method, such as gradient descent. This method updates the model so as to make it better fit the data, but if the iterations are run for too long, the model will begin to overfit and learn the noise in the training data. Therefore, early stopping can help to reduce the training time without compromising the model's performance.

### Incorrect Options:
- **Increase the batch size**  
  Increasing the batch size can actually lead to worse performance due to less accurate estimates of the gradient.

- **Decrease the number of epochs**  
  Decreasing the number of epochs can lead to underfitting as the model might not have enough iterations to learn the underlying patterns in the data.

- **Increase the learning rate**  
  Increasing the learning rate can cause the model to converge too quickly to a suboptimal solution.

</details>

---

## Question 37 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0094`

What is the best practice when troubleshooting and debugging security issues in a CI/CD pipeline for a Machine Learning project on AWS?

- **A) Ignore minor security alerts**
- **B) Use AWS X-Ray for deep dive diagnostics**
- **C) Disable security controls for easier debugging**
- **D) Avoid using AWS provided tools**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Use AWS X-Ray for deep dive diagnostics"?**

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors. It provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components.

### Incorrect Options:
- **Ignore minor security alerts**  
  Ignoring any security alerts, even minor ones, can lead to larger security issues. It's important to investigate all security alerts.

- **Disable security controls for easier debugging**  
  Disabling security controls can expose your application to potential threats. It's not a recommended practice.

- **Avoid using AWS provided tools**  
  AWS provides a number of tools that are specifically designed to help with troubleshooting and debugging. Avoiding these tools can make the process more difficult and less effective.

</details>

---

## Question 38 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0010`

Which AWS service is best suited for the task of imputing missing data in a dataset?

- **A) Amazon Redshift**
- **B) Amazon RDS**
- **C) SageMaker Data Wrangler**
- **D) Amazon S3**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "SageMaker Data Wrangler"?**

SageMaker Data Wrangler is a service that provides an easy way to prepare your data for machine learning. It includes data transformation capabilities, including imputing missing data. This makes it the best choice among the options provided for this specific task.

### Incorrect Options:
- **Amazon S3**  
  While Amazon S3 is a storage service, it does not provide the functionality for data transformation and cleaning.

- **Amazon RDS**  
  Amazon RDS is a relational database service, but it does not provide the functionality for data transformation and cleaning.

- **Amazon Redshift**  
  Amazon Redshift is a data warehousing service, but it does not provide the functionality for data transformation and cleaning.

</details>

---

## Question 39 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0230`

Which of the following best describes the role of design principles for ML lenses in the context of monitoring a machine learning model in production?

- **A) They guide the monitoring strategy**
- **B) They dictate the model's architecture**
- **C) They determine the model's training speed**
- **D) They increase the model's interpretability**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "They guide the monitoring strategy"?**

Design principles for ML lenses are crucial in guiding the monitoring strategy for a machine learning model in production. They help in defining what to monitor, how to monitor, and when to trigger alerts.

### Incorrect Options:
- **They dictate the model's architecture**  
  While design principles can influence model architecture indirectly, their primary role is not to dictate it.

- **They determine the model's training speed**  
  Design principles do not directly determine the model's training speed. Their main role is to guide the monitoring strategy.

- **They increase the model's interpretability**  
  While design principles can indirectly contribute to model interpretability by ensuring robust monitoring, their primary role is not to increase interpretability.

</details>

---

## Question 40 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0385`

A company is preparing a machine learning pipeline using Amazon SageMaker Data Wrangler. The data engineer needs to integrate multiple data sources, clean and transform the data, and output it to an Amazon S3 bucket for training. What steps should the engineer take to ensure the data is properly prepared for training in SageMaker?

- **A) Use SageMaker Data Wrangler to create a pipeline, automatically export the transformed data to S3 in Apache Parquet format, and then use SageMaker training jobs to access the data.**
- **B) Export the transformed dataset from Data Wrangler directly to SageMaker Feature Store for training.**
- **C) Use Data Wrangler to import, clean, and transform the data, and then export the final dataset to Amazon S3 in CSV format.**
- **D) Clean and transform the data using SageMaker Processing jobs, and then manually upload it to an Amazon S3 bucket.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Correct answer: Use SageMaker Data Wrangler to create a pipeline, automatically export the transformed data to S3 in Apache Parquet format, and then use SageMaker training jobs to access the data.**

This is the most efficient and recommended approach. SageMaker Data Wrangler is designed to create data preparation pipelines. It allows you to connect to various data sources, perform data cleaning and transformations, and then export the processed data to Amazon S3.  Exporting in Apache Parquet format is beneficial because Parquet is a columnar storage format optimized for analytical queries and machine learning.  It provides efficient data compression and encoding schemes, which can significantly reduce storage costs and improve the speed of data access during training. SageMaker training jobs can then directly access the Parquet files in S3 for model training.

**Incorrect:**

**B. Export the transformed dataset from Data Wrangler directly to SageMaker Feature Store for training.** - While exporting to Feature Store is a valid option for storing features for real-time inference and model monitoring, it's not the primary method for preparing data for initial model training. Feature Store is more suited for serving features to models, not for the initial bulk training dataset.  Data Wrangler's primary output for training is S3.

**C. Use Data Wrangler to import, clean, and transform the data, and then export the final dataset to Amazon S3 in CSV format.** - While exporting to S3 is correct, exporting in CSV format is less efficient than Parquet. CSV files are row-based and lack the compression and encoding benefits of columnar formats like Parquet. This can lead to larger storage costs and slower data loading during training. Parquet is generally preferred for ML training datasets.

**D. Clean and transform the data using SageMaker Processing jobs, and then manually upload it to an Amazon S3 bucket.** - While SageMaker Processing jobs can be used for data preparation, using Data Wrangler provides a more integrated and user-friendly experience for data exploration, cleaning, and transformation. Manually uploading the data to S3 after processing adds an unnecessary step and potential for errors. Data Wrangler automates the export process to S3.

</details>

---

## Question 41 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0323`

A company wants to use Amazon SageMaker to deploy a real-time machine learning model for high-traffic online predictions. The model has moderate memory and CPU requirements, but scalability and low latency are critical due to unpredictable traffic spikes.
Which of the following deployment options is best suited for this scenario?

- **A) Deploy the model on an Amazon EC2 instance to manually manage scaling.**
- **B) Use AWS Lambda to serve predictions from the model, scaling as per incoming requests.**
- **C) Use Amazon SageMaker batch transform to process requests in large batches.**
- **D) Deploy the model on an Amazon SageMaker endpoint with auto-scaling enabled.**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Correct answer: Deploy the model on an Amazon SageMaker endpoint with auto-scaling enabled.**

This is the best option because Amazon SageMaker endpoints with auto-scaling are designed for real-time inference with variable traffic. Auto-scaling automatically adjusts the number of instances behind the endpoint based on traffic, ensuring low latency and high availability even during traffic spikes. SageMaker handles the infrastructure management, allowing the company to focus on the model itself. This aligns with the requirements of high traffic, low latency, and scalability.

**Incorrect:**

**A. Deploy the model on an Amazon EC2 instance to manually manage scaling.** - While deploying on EC2 is possible, manually managing scaling is not ideal for unpredictable traffic spikes. It requires constant monitoring and manual intervention, which can lead to delays and increased operational overhead. This approach does not provide the automated scalability needed for the scenario.

**B. Use AWS Lambda to serve predictions from the model, scaling as per incoming requests.** - AWS Lambda is suitable for event-driven, short-running tasks. While Lambda can scale automatically, it has limitations on execution time and memory. Deploying a model with moderate memory and CPU requirements on Lambda might be challenging and could result in cold starts and higher latency, especially for complex models. SageMaker endpoints are better suited for serving ML models directly.

**C. Use Amazon SageMaker batch transform to process requests in large batches.** - Amazon SageMaker batch transform is designed for offline inference on large datasets, not for real-time predictions. It processes data in batches and is not suitable for low-latency requirements. This option is inappropriate for high-traffic online predictions where immediate responses are needed.

</details>

---

## Question 42 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0206`

What is the primary concern when dealing with a significant difference in proportions of labels (DPL) in a machine learning dataset?

- **A) Overfitting the model**
- **B) Inefficient model training**
- **C) Bias in model predictions**
- **D) Underfitting the model**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "Bias in model predictions"?**

A significant difference in proportions of labels (DPL) in a dataset can lead to bias in model predictions. This is because the model may become biased towards predicting the class that has a higher proportion in the dataset, leading to inaccurate predictions for the underrepresented class.

### Incorrect Options:
- **Overfitting the model**  
  Overfitting generally occurs when a model learns the training data too well and performs poorly on unseen data. While DPL can contribute to model bias, it does not directly lead to overfitting.

- **Underfitting the model**  
  Underfitting occurs when a model fails to capture the underlying pattern of the data. DPL does not directly lead to underfitting, but rather to bias in model predictions.

- **Inefficient model training**  
  While DPL can lead to bias in model predictions, it does not directly impact the efficiency of model training.

</details>

---

## Question 43 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0452`

Which SageMaker capability tracks lineage across data, code, hyperparameters, and metrics for ML training runs to make experiments reproducible and comparable?

- **A) SageMaker Model Registry**
- **B) SageMaker Experiments**
- **C) SageMaker Pipelines**
- **D) SageMaker Studio**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
SageMaker Experiments organizes training runs into trials and trial components, automatically logging hyperparameters, metrics, datasets, and artifacts so engineers can compare runs side by side. The Model Registry catalogs deployable models, Pipelines define DAGs of steps, and Studio is the IDE.

</details>

---

## Question 44 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0103`

Which AWS service provides real-time guidance to help provision resources following best practices and also assists in optimizing costs and setting cost quotas?

- **A) AWS Cost Explorer**
- **B) Amazon CloudWatch**
- **C) AWS Trusted Advisor**
- **D) AWS Budgets**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "AWS Trusted Advisor"?**

AWS Trusted Advisor is a tool that provides real-time guidance to help you provision your resources following AWS best practices. It checks your AWS environment and provides recommendations to help you save money, improve system performance, or close security gaps. Therefore, it assists in optimizing costs and setting cost quotas.

### Incorrect Options:
- **AWS Cost Explorer**  
  AWS Cost Explorer is a tool that enables you to view and analyze your costs and usage. While it provides detailed cost reports, it doesn't provide real-time guidance or help set cost quotas.

- **Amazon CloudWatch**  
  Amazon CloudWatch is a monitoring and observability service. It provides data and actionable insights to monitor applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. However, it doesn't provide real-time guidance or help set cost quotas.

- **AWS Budgets**  
  AWS Budgets allows you to set custom cost and usage budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount. While it helps manage costs and usage, it doesn't provide real-time guidance.

</details>

---

## Question 45 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0263`

A production retrieval-augmented generation system uses Amazon Bedrock for generation and embeddings, and Amazon OpenSearch Serverless for vector search. Monthly spend has risen sharply, but request volume and response quality are stable. CloudWatch metrics show many repeated prompts and documents being embedded multiple times; the vector index also contains duplicate chunks. The team must reduce recurring costs without changing the foundation model or weakening retrieval quality. Which change best targets both identified cost drivers?

- **A) Reduce OpenSearch Serverless OCUs immediately**
- **B) Cache repeated outputs and deduplicate before embedding**
- **C) Shorten every chunk and re-embed the corpus**
- **D) Lower the generation model's maximum token limit**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Cache repeated outputs and deduplicate before embedding"?**

Caching responses for repeated prompts can reduce redundant Amazon Bedrock generation calls, while deduplicating documents or chunks before embedding avoids repeated embedding computation and unnecessary vector storage. This directly addresses both measured sources of excess cost while preserving the model and retrieval content.

### Incorrect Options:
- **Lower the generation model's maximum token limit**  
  This may reduce output-token costs only if responses are currently reaching the limit. It does not address repeated prompt processing, duplicate embeddings, or duplicate vectors.

- **Reduce OpenSearch Serverless OCUs immediately**  
  Reducing capacity may lower compute costs, but could harm search performance and does not remove duplicate vectors or redundant embedding calls. The scenario provides no evidence that provisioned search capacity is excessive.

- **Shorten every chunk and re-embed the corpus**  
  Re-embedding the entire corpus incurs additional embedding computation and may change retrieval quality. It does not reliably eliminate duplicate content or repeated prompt costs.

</details>

---

## Question 46 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0376`

A machine learning engineer is using SageMaker Data Wrangler to understand relationships between features in the dataset. The engineer wants to visualize the distribution of numerical data and identify relationships between features. Which of the following visualization methods should be used in Data Wrangler to achieve these objectives? (Choose TWO)

- **A) ROC curves for model evaluation**
- **B) Line plots for analyzing trends over time**
- **C) Confusion matrix for evaluating model predictions**
- **D) Partial Dependence Plots (PDP) for feature impact**
- **E) Histograms for understanding data distribution**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B, E`

**Architectural Rationale:**
**Correct answer: Line plots for analyzing trends over time**

Line plots are effective for visualizing trends and patterns in data over a continuous interval, such as time. In SageMaker Data Wrangler, line plots can help identify temporal relationships between features, understand how they change over time, and detect anomalies or seasonal variations. This is useful for exploratory data analysis to understand feature behavior and potential relationships.

**Correct answer: Histograms for understanding data distribution**

Histograms are a fundamental visualization tool for understanding the distribution of numerical data. They display the frequency of data points within specified bins, allowing you to quickly assess the shape, center, and spread of the data. In SageMaker Data Wrangler, histograms help identify skewness, outliers, and potential data quality issues, which are crucial for feature engineering and model selection.

**Incorrect:**

**A. ROC curves for model evaluation** - ROC curves are used to evaluate the performance of binary classification models by plotting the true positive rate against the false positive rate at various threshold settings. They are not used for understanding relationships between features in the dataset during exploratory data analysis.

**C. Confusion matrix for evaluating model predictions** - A confusion matrix is a table that summarizes the performance of a classification model by showing the counts of true positive, true negative, false positive, and false negative predictions. It is used for model evaluation, not for understanding relationships between features in the dataset.

**D. Partial Dependence Plots (PDP) for feature impact** - Partial Dependence Plots (PDP) are used to visualize the marginal effect of one or two features on the predicted outcome of a machine learning model. While they show feature impact, they are typically used after a model is trained, not during the initial exploratory data analysis phase to understand relationships between features in the raw dataset.

</details>

---

## Question 47 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0004`

Which SageMaker feature would be most useful for identifying convergence issues in your machine learning model during training?

- **A) SageMaker Ground Truth**
- **B) SageMaker Clarify**
- **C) SageMaker Studio**
- **D) SageMaker Model Debugger**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "SageMaker Model Debugger"?**

Amazon SageMaker Model Debugger provides visibility into the training process of machine learning models by capturing real-time metrics such as learning gradients and weights. These metrics can be used to identify and fix training issues, such as model convergence problems.

### Incorrect Options:
- **SageMaker Ground Truth**  
  Amazon SageMaker Ground Truth is used to build highly accurate training datasets for machine learning, not for identifying convergence issues.

- **SageMaker Clarify**  
  Amazon SageMaker Clarify provides insights into your data and models, helping you detect potential bias and explain the predictions made by your models. It is not specifically designed for identifying convergence issues.

- **SageMaker Studio**  
  Amazon SageMaker Studio is an integrated development environment for machine learning that allows you to build, train, and deploy models, but it does not specifically provide tools for identifying convergence issues.

</details>

---

## Question 48 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0393`

A machine learning team wants to track the history of model versions, including training data, hyperparameters, and performance metrics over time. Which feature of SageMaker should they use?

- **A) SageMaker Training Jobs**
- **B) SageMaker Model Registry**
- **C) SageMaker Pipelines**
- **D) SageMaker Notebook Instances**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Correct answer: SageMaker Model Registry**

The SageMaker Model Registry is specifically designed to track model versions, associated metadata (training data locations, hyperparameters), and performance metrics over time. It provides a central repository for managing the lifecycle of your models, from initial training to deployment and monitoring. This allows the machine learning team to easily compare different model versions, understand their lineage, and select the best model for a given task. The Model Registry supports versioning, approval workflows, and integration with CI/CD pipelines for automated model deployment.

**Incorrect:**

**A. SageMaker Training Jobs** - SageMaker Training Jobs are used to execute the training process for a machine learning model. While they generate model artifacts and logs, they don't inherently provide a mechanism for tracking the history of model versions and their associated metadata over time in a structured, centralized way. Training jobs are a component *used* by the Model Registry, but not the registry itself.

**C. SageMaker Pipelines** - SageMaker Pipelines are used to create and manage end-to-end machine learning workflows, including data preprocessing, model training, evaluation, and deployment. While pipelines can incorporate model versioning as part of their workflow, they don't provide the dedicated model tracking and management capabilities of the Model Registry. Pipelines orchestrate the steps, while the Model Registry manages the model artifacts and metadata produced by those steps.

**D. SageMaker Notebook Instances** - SageMaker Notebook Instances are compute environments for interactive development and experimentation with machine learning models. They are useful for exploring data, prototyping models, and running training jobs. However, they do not provide a built-in feature for tracking the history of model versions, training data, hyperparameters, and performance metrics over time. Notebooks are a development environment, not a model management tool.

</details>

---

## Question 49 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0013`

A company is preparing policy manuals for a RAG application using an Amazon Bedrock knowledge base. The manuals contain headings, tables, and paragraphs, and users must retrieve relevant passages without losing section context; each result must also be filterable by department and document version. Which preparation approach best meets these requirements?

- **A) Chunk on semantic sections; attach filterable metadata**
- **B) Embed each full manual; filter using prompt instructions**
- **C) Chunk by fixed token count; add metadata after retrieval**
- **D) Split at every newline; store headings as separate chunks**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Chunk on semantic sections; attach filterable metadata"?**

Chunking along meaningful section boundaries helps keep related content and heading context together, improving the relevance and interpretability of retrieved passages. Attaching department and version as metadata during ingestion allows the knowledge base to apply metadata filters at retrieval time.

### Incorrect Options:
- **Chunk by fixed token count; add metadata after retrieval**  
  Fixed-size chunking can split sections or tables and lose context. Metadata added only after retrieval cannot filter the knowledge base's candidate results.

- **Embed each full manual; filter using prompt instructions**  
  Embedding entire manuals can exceed practical retrieval granularity and return overly broad results. Prompt instructions do not enforce metadata-based filtering.

- **Split at every newline; store headings as separate chunks**  
  Newline boundaries do not reliably correspond to semantic units, and separating headings from their content can remove useful context.

</details>

---

## Question 50 of 65

> **Domain:** Domain 4: ML Solution Monitoring and Maintenance (24%) | **ID:** `MLA-U0420`

Which of the following types of drift is best described as a systematic favoring of certain groups in the model‘s predictions over time?

- **A) Data drift**
- **B) Model quality drift**
- **C) Feature attribution drift**
- **D) Bias drift**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Correct answer: Bias drift**

Bias drift refers to the phenomenon where a model's systematic favoring of certain groups in its predictions changes over time. This means that the model's inherent biases, which might have been present from the beginning or developed later, become more pronounced or shift in their impact on different groups. This can lead to unfair or discriminatory outcomes. Monitoring for bias drift is crucial in maintaining fairness and ethical standards in machine learning models, and techniques like re-training with debiased data or using fairness-aware algorithms can help mitigate it.

**Incorrect:**

**A. Data drift** - Data drift refers to changes in the input data distribution over time. While data drift can contribute to other types of drift, including bias drift, it is not the systematic favoring of certain groups itself. Data drift is a change in the statistical properties of the input data, such as feature distributions.

**B. Model quality drift** - Model quality drift refers to the degradation of a model's performance over time, typically measured by metrics like accuracy, precision, or recall. While bias drift can contribute to model quality drift, model quality drift is a broader term that encompasses any decline in performance, regardless of the underlying cause.

**C. Feature attribution drift** - Feature attribution drift refers to changes in the importance or influence of different features on the model's predictions over time. While feature attribution drift can indirectly affect bias, it is not the direct systematic favoring of certain groups that defines bias drift. Feature attribution drift focuses on how the model weighs different input features.

</details>

---

## Question 51 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0190`

Which of the following metrics is most suitable for evaluating a binary classification model when the cost of false negatives is very high?

- **A) Recall**
- **B) Accuracy**
- **C) Precision**
- **D) F1 score**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Recall"?**

Recall (also known as sensitivity or true positive rate) is the ratio of true positives to the sum of true positives and false negatives. In situations where the cost of false negatives is high (for example, in medical diagnosis where a false negative could mean missing a critical disease), recall is a particularly important metric as it measures the model's ability to correctly identify all positive instances.

### Incorrect Options:
- **Accuracy**  
  Accuracy is the ratio of correct predictions to total predictions. While it is a commonly used metric, it can be misleading if the classes are imbalanced. It does not specifically focus on the cost of false negatives.

- **Precision**  
  Precision is the ratio of true positives to the sum of true positives and false positives. It measures the model's ability to correctly identify only positive instances, but does not take into account the cost of false negatives.

- **F1 score**  
  The F1 score is the harmonic mean of precision and recall. While it tries to balance both precision and recall, it may not be the best choice when the cost of false negatives is very high, as it does not specifically focus on minimizing false negatives.

</details>

---

## Question 52 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0463`

Which encoding technique converts a categorical feature with three values (red, green, blue) into three binary columns?

- **A) Label encoding**
- **B) One-hot encoding**
- **C) Target encoding**
- **D) Frequency encoding**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
One-hot encoding creates one binary indicator column per category, avoiding ordinal assumptions. Label encoding maps categories to integers (0,1,2), implying ordering — bad for nominal features. Target encoding replaces each category with the mean of the target, and frequency encoding uses category counts.

</details>

---

## Question 53 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0044`

When deploying machine learning models using AWS SageMaker, which of the following is not a best practice?

- **A) Provisioning appropriate compute resources**
- **B) Choosing appropriate containers**
- **C) Using the same version for all deployments**
- **D) Optimizing models on edge devices**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "Using the same version for all deployments"?**

Using the same version for all deployments is not a best practice when deploying machine learning models using AWS SageMaker. It is important to manage different versions of models to track changes, improve models over time, and rollback to a previous version if needed.

### Incorrect Options:
- **Provisioning appropriate compute resources**  
  Provisioning appropriate compute resources is a best practice. It ensures that the model has the necessary resources to run efficiently.

- **Choosing appropriate containers**  
  Choosing appropriate containers is a best practice. Containers provide the runtime environment for the model, and choosing the right one can affect the model's performance.

- **Optimizing models on edge devices**  
  Optimizing models on edge devices is a best practice. It helps to improve the model's performance and reduce latency.

</details>

---

## Question 54 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0041`

When deploying a machine learning solution, why might you choose to use Amazon EC2 instances?

- **A) EC2 instances offer flexible configurations**
- **B) EC2 instances automatically scale**
- **C) EC2 instances are always the cheapest option**
- **D) EC2 instances can host any type of model**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "EC2 instances offer flexible configurations"?**

Amazon EC2 provides a variety of instance types optimized to fit different use cases, including various machine learning workloads. Instances are virtual servers that can run applications. They offer varying combinations of CPU, memory, storage, and networking capacity, giving you the flexibility to choose the appropriate mix of resources for your applications.

### Incorrect Options:
- **EC2 instances automatically scale**  
  EC2 instances do not automatically scale. You need to configure auto-scaling groups or use services like AWS Elastic Beanstalk that provide automatic scaling features.

- **EC2 instances are always the cheapest option**  
  The cost of EC2 instances varies based on the instance type, region, and pricing model (On-Demand, Reserved, Spot). Other services like AWS Lambda or AWS Fargate may be cheaper depending on the use case.

- **EC2 instances can host any type of model**  
  While EC2 instances are capable of hosting a wide variety of applications, including machine learning models, the ability to host a model is not exclusive to EC2. Other services like AWS SageMaker also provide model hosting capabilities.

</details>

---

## Question 55 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0132`

What is a crucial factor to consider when classifying data for a machine learning project?

- **A) Classifying data based on its sensitivity**
- **B) Classifying data after model training**
- **C) Classifying data based on its source**
- **D) Classifying all data as sensitive**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Classifying data based on its sensitivity"?**

Data classification is a crucial step in data management and protection. It involves categorizing data based on its sensitivity level. This helps in applying appropriate security measures and in compliance with regulations. It is not advisable to classify all data as sensitive as it may lead to unnecessary security measures and costs.

### Incorrect Options:
- **Classifying all data as sensitive**  
  This approach can lead to unnecessary security measures and costs. Not all data is sensitive and requires the same level of protection.

- **Classifying data based on its source**  
  The source of data is not always an accurate indicator of its sensitivity. Data should be classified based on its content and the level of sensitivity.

- **Classifying data after model training**  
  Data should be classified before model training. This helps in ensuring that sensitive data is appropriately protected during the model training process.

</details>

---

## Question 56 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0177`

In a CI/CD pipeline, which type of test is typically used to verify that individual units of source code work as expected?

- **A) Integration tests**
- **B) Unit tests**
- **C) End-to-end tests**
- **D) System tests**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "Unit tests"?**

Unit tests are typically used in a CI/CD pipeline to verify that individual units of source code, such as functions or methods, work as expected. They are designed to test a small piece of code in isolation, which makes it easier to pinpoint any issues or bugs.

### Incorrect Options:
- **Integration tests**  
  Integration tests are used to verify that different components of the system work together as expected. They are not designed to test individual units of code in isolation.

- **End-to-end tests**  
  End-to-end tests are used to verify that a system works together as a whole and meets its requirements. They are not designed to test individual units of code in isolation.

- **System tests**  
  System tests are used to verify that the entire system, including all its components, works as expected under real-world conditions. They are not designed to test individual units of code in isolation.

</details>

---

## Question 57 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0175`

When scaling your machine learning solution, why might you choose to dynamically add Spot Instances to your Amazon EC2 fleet?

- **A) Spot Instances offer guaranteed availability**
- **B) Spot Instances are ideal for real-time inference**
- **C) Spot Instances support larger models**
- **D) Spot Instances can reduce costs significantly**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "Spot Instances can reduce costs significantly"?**

Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity in the AWS cloud. Spot Instances are available at up to a 90% discount compared to On-Demand prices, making them a cost-effective choice for applications with flexible start and end times, or that can withstand interruptions.

### Incorrect Options:
- **Spot Instances offer guaranteed availability**  
  Spot Instances do not offer guaranteed availability. They use spare EC2 capacity and can be interrupted with two minutes of notification when AWS needs the capacity back.

- **Spot Instances are ideal for real-time inference**  
  Spot Instances are not specifically designed for real-time inference. They are best for flexible workloads that can tolerate interruptions.

- **Spot Instances support larger models**  
  The size of the model that can be deployed is not determined by the instance type (Spot or On-Demand), but by the resources provisioned for the deployment.

</details>

---

## Question 58 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0316`

A data scientist is building a machine learning pipeline using Amazon SageMaker Pipelines. The pipeline includes data preprocessing, model training, and model registration. The data scientist wants to ensure that parameters used for model training can be easily adjusted without modifying the pipeline itself. Which feature of SageMaker Pipelines should the data scientist use to achieve this?

- **A) Pipeline Parameters**
- **B) SageMaker Model Registry**
- **C) Pipeline Steps**
- **D) Directed Acyclic Graph (DAG)**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Correct answer: Pipeline Parameters**

Pipeline Parameters in SageMaker Pipelines are designed to allow users to define values that can be adjusted when a pipeline is executed, without requiring modifications to the pipeline definition itself. This is crucial for experimentation and hyperparameter tuning. By defining parameters for model training, such as learning rate or batch size, the data scientist can easily run the pipeline with different configurations, optimizing model performance without altering the underlying pipeline structure. These parameters are resolved at runtime, providing flexibility and reusability.

**Incorrect:**

**B. SageMaker Model Registry** - The SageMaker Model Registry is a repository for managing and versioning trained models. While it's an important part of the ML lifecycle, it doesn't directly address the need to adjust training parameters without modifying the pipeline definition. It's used for storing and tracking models after they have been trained.

**C. Pipeline Steps** - Pipeline Steps define the individual tasks within a SageMaker Pipeline, such as data preprocessing, training, or evaluation. While you can configure parameters within a step, changing these parameters typically requires modifying the pipeline definition itself, which is what the data scientist wants to avoid.

**D. Directed Acyclic Graph (DAG)** - The Directed Acyclic Graph (DAG) defines the structure and dependencies of the pipeline steps. It represents the flow of data and execution order. While the DAG is essential for defining the pipeline, it doesn't provide a mechanism for easily adjusting training parameters without modifying the pipeline definition.

</details>

---

## Question 59 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0109`

You are working on a machine learning project where you need to detect and treat outliers in your dataset. The dataset is large and requires an AWS tool for this task.

Which AWS tool would be most suitable for this task?

- **A) Use SageMaker Data Wrangler for outlier detection**
- **B) Use AWS Glue DataBrew for data preparation**
- **C) Use Spark on Amazon EMR for distributed processing**
- **D) Use AWS Glue for ETL operations**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `A`

**Architectural Rationale:**
**Why "Use SageMaker Data Wrangler for outlier detection"?**

SageMaker Data Wrangler reduces the time it takes to aggregate and prepare data for machine learning from weeks to minutes. With SageMaker Data Wrangler, you can simplify the process of data preparation and feature engineering, and complete each step of the data preparation workflow, including data selection, cleansing, exploration, and visualization from a single visual interface. Therefore, it is the most suitable tool for detecting and treating outliers in the dataset.

### Incorrect Options:
- **Use AWS Glue for ETL operations**  
  While AWS Glue is a fully managed ETL service that can handle data transformation, it might not be the best choice for detecting and treating outliers.

- **Use AWS Glue DataBrew for data preparation**  
  AWS Glue DataBrew is a visual data preparation tool that's great for cleaning and normalizing data, but it might not be the best choice for detecting and treating outliers.

- **Use Spark on Amazon EMR for distributed processing**  
  Spark on Amazon EMR is a powerful tool for processing large datasets, but it might not be the best choice for detecting and treating outliers.

</details>

---

## Question 60 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0495`

Which SageMaker Studio component is built on Amazon Linux Code Editor (a fork of Code-OSS / VS Code) and provides a familiar IDE for ML developers?

- **A) SageMaker Studio Classic**
- **B) SageMaker Studio Code Editor**
- **C) SageMaker Studio Lab**
- **D) SageMaker Notebook Instances**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
SageMaker Studio Code Editor (released 2024) is a managed VS Code-compatible IDE within Studio. Studio Classic uses the JupyterServer interface; Studio Lab is a free notebook offering for learning; Notebook Instances are standalone EC2-backed Jupyter notebooks (predecessor to Studio).

</details>

---

## Question 61 of 65

> **Domain:** Domain 1: Data Preparation for Machine Learning (28%) | **ID:** `MLA-U0288`

What is a common strategy to address class imbalance in a dataset for machine learning?

- **A) Using a different machine learning algorithm**
- **B) Increasing the size of the dataset**
- **C) Removing outliers from the dataset**
- **D) Oversampling the minority class**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `D`

**Architectural Rationale:**
**Why "Oversampling the minority class"?**

Oversampling the minority class is a common strategy to address class imbalance in a dataset. This can be achieved by duplicating examples from the minority class in the training dataset prior to fitting a model. This can balance the class distribution but does not provide any additional information to the model.

### Incorrect Options:
- **Removing outliers from the dataset**  
  While this can help improve the performance of a machine learning model, it does not specifically address class imbalance.

- **Increasing the size of the dataset**  
  Simply increasing the size of the dataset without addressing the class imbalance will not solve the problem. The class imbalance will persist if the additional data maintains the same distribution.

- **Using a different machine learning algorithm**  
  While some algorithms may be more robust to class imbalance than others, simply changing the algorithm without addressing the underlying class imbalance is not a solution.

</details>

---

## Question 62 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0182`

What is a primary benefit of using L2 regularization in a machine learning model?

- **A) It reduces training time**
- **B) It prevents overfitting**
- **C) It increases model complexity**
- **D) It induces feature selection**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
**Why "It prevents overfitting"?**

L2 regularization, also known as Ridge regularization, adds a penalty equal to the square of the magnitude of coefficients. This type of regularization can help to prevent overfitting by discouraging complex models, without completely eliminating any features.

### Incorrect Options:
- **It reduces training time**  
  Regularization techniques, including L2, do not directly reduce training time. In fact, they can sometimes increase training time because they add an additional term to the loss function that the model needs to compute.

- **It increases model complexity**  
  Regularization techniques, including L2, are used to prevent overfitting by discouraging overly complex models, not by increasing model complexity.

- **It induces feature selection**  
  While L1 regularization can lead to feature selection because it can reduce some coefficients to zero, L2 regularization does not have this property. It tends to spread coefficient values out more evenly across features.

</details>

---

## Question 63 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0497`

What does the precision metric measure in a binary classifier?

- **A) Fraction of actual positives correctly identified**
- **B) Fraction of predicted positives that are actually positive**
- **C) Fraction of all predictions that are correct**
- **D) Fraction of actual negatives correctly identified**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
Precision = TP / (TP + FP) — of all items predicted positive, how many really were. It's the right metric when false positives are costly (e.g., flagging legitimate email as spam). Recall is the first option, accuracy is the third, specificity the fourth.

</details>

---

## Question 64 of 65

> **Domain:** Domain 2: ML Model Development (26%) | **ID:** `MLA-U0024`

In the context of machine learning, what is the primary purpose of using early stopping during the training process?

- **A) To increase the number of epochs**
- **B) To increase model complexity**
- **C) To reduce overfitting**
- **D) To enhance feature selection**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `C`

**Architectural Rationale:**
**Why "To reduce overfitting"?**

Early stopping is a form of regularization used to avoid overfitting when training a learner with an iterative method, such as gradient descent. This is done by stopping the training process before it has a chance to overfit to the training data.

### Incorrect Options:
- **To increase the number of epochs**  
  Early stopping is actually used to prevent the model from training for too many epochs, not to increase them. Training for too many epochs can lead to overfitting.

- **To increase model complexity**  
  Early stopping is used to prevent overfitting, which is often a result of excessive model complexity. Therefore, it does not increase model complexity.

- **To enhance feature selection**  
  Early stopping does not directly influence feature selection. It simply stops the training process based on a specified condition (like no improvement in validation loss after a certain number of epochs), which helps to prevent overfitting.

</details>

---

## Question 65 of 65

> **Domain:** Domain 3: Deployment and Orchestration of ML Workflows (22%) | **ID:** `MLA-U0476`

Which CloudWatch capability allows automatic scaling of a SageMaker endpoint based on InvocationsPerInstance metric thresholds?

- **A) CloudWatch Logs**
- **B) CloudWatch target-tracking auto scaling policy**
- **C) CloudWatch Synthetics**
- **D) CloudWatch Events**

<details>
<summary><b>Click to View Answer & Detailed Explanation</b></summary>

**Correct Answer:** `B`

**Architectural Rationale:**
Application Auto Scaling target-tracking policies on InvocationsPerInstance let SageMaker endpoints scale instances up/down to keep traffic per instance within a target range. CloudWatch Logs stores logs; Synthetics runs canaries; Events (now EventBridge) handles event routing.

</details>

---
