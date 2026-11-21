# MLA-C01 Authentic Exam Practice Pool & Community Consensus

> **Total Questions:** 101  
> **Source:** ExamTopics Authentic Community Discussion Pool  
> **Pedagogical Designation:** Professional Exam Practice Suite (Recall Pool)  

---

## Question 1: MLA-C01-ET-Q001
**Domain 2:** ML Model Development  

**Question:**  
Case Study -
A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring.
The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3.
The company needs to use the central model registry to manage different versions of models in the application.
Which action will meet this requirement with the LEAST operational overhead?

**Choices:**
- A) Create a separate Amazon Elastic Container Registry (Amazon ECR) repository for each model.
- B) Use Amazon Elastic Container Registry (Amazon ECR) and unique tags for each model version.
- C) Use the SageMaker Model Registry and model groups to catalog the models.
- D) Use the SageMaker Model Registry and unique tags for each model version.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-models.html
"Each model package in a Model Group corresponds to a trained model. The version of each model package is a numerical value that starts at 1 and is incremented with each new model package added to a Model Group. For example, if 5 model packages are added to a Model Group, the model package versions will be 1, 2, 3, 4, and 5."
---
Selected Answer: C
SageMaker Model Registry is specifically designed for managing ML models within the SageMaker ecosystem.
It provides built-in versioning and cataloging capabilities for ML models.
Model groups in the Model Registry allow for logical organization of related models.
It integrates seamlessly with other SageMaker components like training, deployment, and monitoring.
This solution offers the least operational overhead as it's a native SageMaker feature designed for this exact purpose.
It provides features like model approval workflows, which are crucial for managing models in production environments.
---
Selected Answer: C
The correct answer is C. Use the SageMaker Model Registry and model groups to catalog the models.

SageMaker Model Registry is specifically designed for managing ML models within the SageMaker ecosystem.
It provides built-in versioning and cataloging capabilities for ML models.
Model groups in the Model Registry allow for logical organization of related models.
It integrates seamlessly with other SageMaker components like training, deployment, and monitoring.
This solution offers the least operational overhead as it's a native SageMaker feature designed for this exact purpose.
It provides features like model approval workflows, which are crucial for managing models in production environments.

</details>

---

## Question 2: MLA-C01-ET-Q002
**Domain 2:** ML Model Development  

**Question:**  
Case study -
An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3.
The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data.
Which AWS service or feature can aggregate the data from the various data sources?

**Choices:**
- A) Amazon EMR Spark jobs
- B) Amazon Kinesis Data Streams
- C) Amazon DynamoDB
- D) AWS Lake Formation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (71%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: A
Amazon EMR with Spark is an excellent choice for aggregating, processing, and transforming large datasets from multiple sources (e.g., Amazon S3 and on-premises MySQL database). Spark jobs can handle both structured and unstructured. While Lake Formation is great for managing data lakes, it doesn’t provide the ETL and data processing capabilities required to aggregate and transform datasets from multiple sources.
---
Selected Answer: D
Is it D? AWS Lake Formation ? EMR Spark jobs is more manual.
---
Selected Answer: A
EMR with Spark can aggregate large datasets from multiple sources, including S3 and on-premises MySQL.

</details>

---

## Question 3: MLA-C01-ET-Q003
**Domain 2:** ML Model Development  

**Question:**  
A company is using Amazon SageMaker to develop ML models. The company stores sensitive training data in an Amazon S3 bucket. The model training must have network isolation from the internet.

Which solution will meet this requirement?

**Choices:**
- A) Run the SageMaker training jobs in private subnets. Create a NAT gateway. Route traffic for training through the NAT gateway.
- B) Run the SageMaker training jobs in private subnets. Create an S3 gateway VPC endpoint. Route traffic for training through the S3 gateway VPC endpoint.
- C) Run the SageMaker training jobs in public subnets that have an attached security group. In the security group, use inbound rules to limit traffic from the internet. Encrypt SageMaker instance storage by using server-side encryption with AWS KMS keys (SSE-KMS).
- D) Encrypt traffic to Amazon S3 by using a bucket policy that includes a value of True for the aws:SecureTransport condition key. Use default at-rest encryption for Amazon S3. Encrypt SageMaker instance storage by using server-side encryption with AWS KMS keys (SSE-KMS).

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Use private subnets and S3 gateway VPC endpoint to bypass public Internet.

</details>

---

## Question 4: MLA-C01-ET-Q004
**Domain 2:** ML Model Development  

**Question:**  
A company needs to use Retrieval Augmented Generation (RAG) to supplement an open source large language model (LLM) that runs on Amazon Bedrock. The company's data for RAG is a set of documents in an Amazon S3 bucket. The documents consist of .csv files and .docx files.

Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Create a pipeline in Amazon SageMaker Pipelines to generate a new model. Call the new model from Amazon Bedrock to perform RAG queries.
- B) Convert the data into vectors. Store the data in an Amazon Neptune database. Connect the database to Amazon Bedrock. Call the Amazon Bedrock API to perform RAG queries.
- C) Fine-tune an existing LLM by using an AutoML job in Amazon SageMaker. Configure the S3 bucket as a data source for the AutoML job. Deploy the LLM to a SageMaker endpoint. Use the endpoint to perform RAG queries.
- D) Create a knowledge base for Amazon Bedrock. Configure a data source that references the S3 bucket. Use the Amazon Bedrock API to perform RAG queries.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D is the correct answer.

A The csv and docx files has to be vectorized first. Beside this option does not mention anything about the data
B and C are not applicable in this case.

</details>

---

## Question 5: MLA-C01-ET-Q005
**Domain 2:** ML Model Development  

**Question:**  
A company plans to deploy an ML model for production inference on an Amazon SageMaker endpoint. The average inference payload size will vary from 100 MB to 300 MB. Inference requests must be processed in 60 minutes or less.

Which SageMaker inference option will meet these requirements?

**Choices:**
- A) Serverless inference
- B) Asynchronous inference
- C) Real-time inference
- D) Batch transform

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Agree with B.

In general, real-time inference supports payloads up to 5 MB for synchronous requests, while asynchronous inference can support larger payloads, often up to 5 GB. 

The use case in this questions involves inference payloads of 100 MB to 300 MB and needs to be processed in under 60 minutes, Asynchronous Inference is the best choice for handling large payloads without strict real-time requirements.

</details>

---

## Question 6: MLA-C01-ET-Q006
**Domain 2:** ML Model Development  

**Question:**  
A company is planning to create several ML prediction models. The training data is stored in Amazon S3. The entire dataset is more than 5 ТВ in size and consists of CSV, JSON, Apache Parquet, and simple text files.
The data must be processed in several consecutive steps. The steps include complex manipulations that can take hours to finish running. Some of the processing involves natural language processing (NLP) transformations. The entire process must be automated.
Which solution will meet these requirements?

**Choices:**
- A) Process data at each step by using Amazon SageMaker Data Wrangler. Automate the process by using Data Wrangler jobs.
- B) Use Amazon SageMaker notebooks for each data processing step. Automate the process by using Amazon EventBridge.
- C) Process data at each step by using AWS Lambda functions. Automate the process by using AWS Step Functions and Amazon EventBridge.
- D) Use Amazon SageMaker Pipelines to create a pipeline of data processing steps. Automate the pipeline by using Amazon EventBridge.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Large datasets + Multiple file formats + Complex automation & orchestration of ML workflows + NLP Transformation ---> Sagemaker pipelines + Event bridge for trigger
---
Selected Answer: D
At first sight it sounds like C but because of "complex manipulations that can take hours to finish" for sure sounds like D.

</details>

---

## Question 7: MLA-C01-ET-Q007
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use AWS CloudFormation to create an ML model that an Amazon SageMaker endpoint will host.
Which resource should the ML engineer declare in the CloudFormation template to meet this requirement?

**Choices:**
- A) AWS::SageMaker::Model
- B) AWS::SageMaker::Endpoint
- C) AWS::SageMaker::NotebookInstance
- D) AWS::SageMaker::Pipeline

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS::SageMaker::Model ✅

 This resource defines the model, including:
 Location of model artifacts in S3
 Inference image/container
 IAM role
 It is a prerequisite for deploying a model to an endpoint.
---
Selected Answer: A
Type: AWS::SageMaker::Model
Properties:
 Containers: 
 - ContainerDefinition
 EnableNetworkIsolation: Boolean
 ExecutionRoleArn: String
 InferenceExecutionConfig: 
 InferenceExecutionConfig
 ModelName: String
 PrimaryContainer: 
 ContainerDefinition
 Tags: 
 - Tag
 VpcConfig: 
 VpcConfig
---
Selected Answer: A
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html

</details>

---

## Question 8: MLA-C01-ET-Q008
**Domain 2:** ML Model Development  

**Question:**  
An advertising company uses AWS Lake Formation to manage a data lake. The data lake contains structured data and unstructured data. The company's ML engineers are assigned to specific advertisement campaigns.
The ML engineers must interact with the data through Amazon Athena and by browsing the data directly in an Amazon S3 bucket. The ML engineers must have access to only the resources that are specific to their assigned advertisement campaigns.
Which solution will meet these requirements in the MOST operationally efficient way?

**Choices:**
- A) Configure IAM policies on an AWS Glue Data Catalog to restrict access to Athena based on the ML engineers' campaigns.
- B) Store users and campaign information in an Amazon DynamoDB table. Configure DynamoDB Streams to invoke an AWS Lambda function to update S3 bucket policies.
- C) Use Lake Formation to authorize AWS Glue to access the S3 bucket. Configure Lake Formation tags to map ML engineers to their campaigns.
- D) Configure S3 bucket policies to restrict access to the S3 bucket based on the ML engineers' campaigns.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Lake Formation → Tag resources with campaigns → Map ML engineers to campaigns → Fine-grained access control → Operational efficiency
---
Selected Answer: C
"engineers must have access to only the resources that are specific to their assigned advertisement campaigns" This is a clear use-case for lakeformation

</details>

---

## Question 9: MLA-C01-ET-Q009
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use data with Amazon SageMaker Canvas to train an ML model. The data is stored in Amazon S3 and is complex in structure. The ML engineer must use a file format that minimizes processing time for the data.
Which file format will meet these requirements?

**Choices:**
- A) CSV files compressed with Snappy
- B) JSON objects in JSONL format
- C) JSON files compressed with gzip
- D) Apache Parquet files

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Minimize processing time: -Why Apache Parquet? Columnar, fast I/O; Efficient for complex data; Built-in compression; SageMaker Canvas compatible
---
Selected Answer: D
Parquet is optimized for performance

</details>

---

## Question 10: MLA-C01-ET-Q010
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer is evaluating several ML models and must choose one model to use in production. The cost of false negative predictions by the models is much higher than the cost of false positive predictions.
Which metric finding should the ML engineer prioritize the MOST when choosing the model?

**Choices:**
- A) Low precision
- B) High precision
- C) Low recall
- D) High recall

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A. Low precision: Increases false positives; less relevant here.
B. High precision: Reduces false positives; not the priority.
C. Low recall: Increases false negatives; must be avoided.
D. High recall: Correct; minimizes false negatives.
---
Selected Answer: D
https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html
"High recall means that the classifier returned most of the relevant results."

</details>

---

## Question 11: MLA-C01-ET-Q011
**Domain 2:** ML Model Development  

**Question:**  
A company has trained and deployed an ML model by using Amazon SageMaker. The company needs to implement a solution to record and monitor all the API call events for the SageMaker endpoint. The solution also must provide a notification when the number of API call events breaches a threshold.
Which solution will meet these requirements?

**Choices:**
- A) Use SageMaker Debugger to track the inferences and to report metrics. Create a custom rule to provide a notification when the threshold is breached.
- B) Use SageMaker Debugger to track the inferences and to report metrics. Use the tensor_variance built-in rule to provide a notification when the threshold is breached.
- C) Log all the endpoint invocation API events by using AWS CloudTrail. Use an Amazon CloudWatch dashboard for monitoring. Set up a CloudWatch alarm to provide notification when the threshold is breached.
- D) Add the Invocations metric to an Amazon CloudWatch dashboard for monitoring. Set up a CloudWatch alarm to provide notification when the threshold is breached.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `82%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (82%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
I pick C. The company needs to implement a solution to record and monitor all the API call events for the SageMaker endpoint. Its needs to RECORD all events.
---
Selected Answer: C
C. CloudTrail + CloudWatch dashboard + CloudWatch alarm

 ✅ Correcto.

 AWS CloudTrail captura todos los eventos de API, incluidas las invocaciones a endpoints de SageMaker (InvokeEndpoint).

 CloudWatch puede procesar estos logs para generar métricas personalizadas.

 Puedes usar un alarm de CloudWatch para notificar cuando el número de eventos supera un umbral.

 Esto cubre tanto registro como notificación
---
Selected Answer: C
✅ Breakdown of the correct answer:
CloudTrail:

 Logs all SageMaker API calls, including InvokeEndpoint.
 Provides auditing and visibility into who called the endpoint, when, and with what parameters.
 Essential for tracking all invocation events (as required).

CloudWatch Dashboard + Alarm:

 Use a CloudWatch dashboard to monitor invocation patterns and metrics.
 Set up an alarm based on metrics like the number of invocations (from CloudTrail logs or the Invocations metric) to trigger notifications when thresholds are breached.

</details>

---

## Question 12: MLA-C01-ET-Q012
**Domain 2:** ML Model Development  

**Question:**  
A company has AWS Glue data processing jobs that are orchestrated by an AWS Glue workflow. The AWS Glue jobs can run on a schedule or can be launched manually.
The company is developing pipelines in Amazon SageMaker Pipelines for ML model development. The pipelines will use the output of the AWS Glue jobs during the data processing phase of model development. An ML engineer needs to implement a solution that integrates the AWS Glue jobs with the pipelines.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Use AWS Step Functions for orchestration of the pipelines and the AWS Glue jobs.
- B) Use processing steps in SageMaker Pipelines. Configure inputs that point to the Amazon Resource Names (ARNs) of the AWS Glue jobs.
- C) Use Callback steps in SageMaker Pipelines to start the AWS Glue workflow and to stop the pipelines until the AWS Glue jobs finish running.
- D) Use Amazon EventBridge to invoke the pipelines and the AWS Glue jobs in the desired order.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (75%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
✅ Explanation:
SageMaker Pipelines + AWS Glue Integration Goal:

You want SageMaker Pipelines to wait for AWS Glue jobs to finish, since their outputs are needed during the model development phase. You also want to keep operational overhead low.
Why Callback steps are the best option:

 Callback steps in SageMaker Pipelines allow you to pause the pipeline execution until an external process completes.
 You can:
 Use the callback step to trigger an AWS Glue workflow (or job).
 Use a Lambda function or a service like EventBridge or Step Functions to report back to SageMaker when the Glue job completes.
 This approach provides tight integration while maintaining low operational overhead—you don’t need to build a whole orchestration layer.
---
Selected Answer: C
https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/tabular/custom_callback_pipelines_step/sagemaker-pipelines-callback-step.html This shows how to use the Callback Step and how to include a Glue ETL job as part of a SageMaker ML pipeline.
---
Selected Answer: B
I think it's B when I consider 'LEAST operational overhead'.

</details>

---

## Question 13: MLA-C01-ET-Q013
**Domain 2:** ML Model Development  

**Question:**  
A company is using an Amazon Redshift database as its single data source. Some of the data is sensitive.
A data scientist needs to use some of the sensitive data from the database. An ML engineer must give the data scientist access to the data without transforming the source data and without storing anonymized data in the database.
Which solution will meet these requirements with the LEAST implementation effort?

**Choices:**
- A) Configure dynamic data masking policies to control how sensitive data is shared with the data scientist at query time.
- B) Create a materialized view with masking logic on top of the database. Grant the necessary read permissions to the data scientist.
- C) Unload the Amazon Redshift data to Amazon S3. Use Amazon Athena to create schema-on-read with masking logic. Share the view with the data scientist.
- D) Unload the Amazon Redshift data to Amazon S3. Create an AWS Glue job to anonymize the data. Share the dataset with the data scientist.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Redshift database → Sensitive data → Dynamic Data Masking → Query-time masking for data scientist → No transformation or additional storage → Least effort
---
Selected Answer: A
https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html
LEAST effort leads to A.

</details>

---

## Question 14: MLA-C01-ET-Q014
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer is using a training job to fine-tune a deep learning model in Amazon SageMaker Studio. The ML engineer previously used the same pre-trained model with a similar dataset. The ML engineer expects vanishing gradient, underutilized GPU, and overfitting problems.
The ML engineer needs to implement a solution to detect these issues and to react in predefined ways when the issues occur. The solution also must provide comprehensive real-time metrics during the training.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Use TensorBoard to monitor the training job. Publish the findings to an Amazon Simple Notification Service (Amazon SNS) topic. Create an AWS Lambda function to consume the findings and to initiate the predefined actions.
- B) Use Amazon CloudWatch default metrics to gain insights about the training job. Use the metrics to invoke an AWS Lambda function to initiate the predefined actions.
- C) Expand the metrics in Amazon CloudWatch to include the gradients in each training step. Use the metrics to invoke an AWS Lambda function to initiate the predefined actions.
- D) Use SageMaker Debugger built-in rules to monitor the training job. Configure the rules to initiate the predefined actions.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
SageMaker Debugger → Built-in rules → Monitor training (vanishing gradients, GPU use, overfitting) → Predefined actions → Low overhead
---
Selected Answer: D
https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html

</details>

---

## Question 15: MLA-C01-ET-Q015
**Domain 2:** ML Model Development  

**Question:**  
A credit card company has a fraud detection model in production on an Amazon SageMaker endpoint. The company develops a new version of the model. The company needs to assess the new model's performance by using live data and without affecting production end users.
Which solution will meet these requirements?

**Choices:**
- A) Set up SageMaker Debugger and create a custom rule.
- B) Set up blue/green deployments with all-at-once traffic shifting.
- C) Set up blue/green deployments with canary traffic shifting.
- D) Set up shadow testing with a shadow variant of the new model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Shadow testing is a technique used to evaluate a new model's performance by running it alongside the current production model, processing the same live data but without affecting production outcomes.
---
Selected Answer: D
https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-create.html

</details>

---

## Question 17: MLA-C01-ET-Q017
**Domain 2:** ML Model Development  

**Question:**  
A company stores time-series data about user clicks in an Amazon S3 bucket. The raw data consists of millions of rows of user activity every day. ML engineers access the data to develop their ML models.
The ML engineers need to generate daily reports and analyze click trends over the past 3 days by using Amazon Athena. The company must retain the data for 30 days before archiving the data.
Which solution will provide the HIGHEST performance for data retrieval?

**Choices:**
- A) Keep all the time-series data without partitioning in the S3 bucket. Manually move data that is older than 30 days to separate S3 buckets.
- B) Create AWS Lambda functions to copy the time-series data into separate S3 buckets. Apply S3 Lifecycle policies to archive data that is older than 30 days to S3 Glacier Flexible Retrieval.
- C) Organize the time-series data into partitions by date prefix in the S3 bucket. Apply S3 Lifecycle policies to archive partitions that are older than 30 days to S3 Glacier Flexible Retrieval.
- D) Put each day's time-series data into its own S3 bucket. Use S3 Lifecycle policies to archive S3 buckets that hold data that is older than 30 days to S3 Glacier Flexible Retrieval.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Time-series data → Partition by date in S3 → Optimized Athena queries → S3 lifecycle policies → Move partitions >30 days to S3 Glacier Flexible Retrieval
---
Selected Answer: C
This is more an S3 question than a ML one.

</details>

---

## Question 18: MLA-C01-ET-Q018
**Domain 2:** ML Model Development  

**Question:**  
A company has deployed an ML model that detects fraudulent credit card transactions in real time in a banking application. The model uses Amazon SageMaker Asynchronous Inference. Consumers are reporting delays in receiving the inference results.
An ML engineer needs to implement a solution to improve the inference performance. The solution also must provide a notification when a deviation in model quality occurs.
Which solution will meet these requirements?

**Choices:**
- A) Use SageMaker real-time inference for inference. Use SageMaker Model Monitor for notifications about model quality.
- B) Use SageMaker batch transform for inference. Use SageMaker Model Monitor for notifications about model quality.
- C) Use SageMaker Serverless Inference for inference. Use SageMaker Inference Recommender for notifications about model quality.
- D) Keep using SageMaker Asynchronous Inference for inference. Use SageMaker Inference Recommender for notifications about model quality.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Sagemaker Real-Time Inference - Faster predictions to solve delay issues; 
Model Monitor to tracks model quality and sends alerts for deviations
---
Selected Answer: A
The delay comes from using an async inference.

</details>

---

## Question 19: MLA-C01-ET-Q019
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to implement a solution to host a trained ML model. The rate of requests to the model will be inconsistent throughout the day.
The ML engineer needs a scalable solution that minimizes costs when the model is not in use. The solution also must maintain the model's capacity to respond to requests during times of peak usage.
Which solution will meet these requirements?

**Choices:**
- A) Create AWS Lambda functions that have fixed concurrency to host the model. Configure the Lambda functions to automatically scale based on the number of requests to the model.
- B) Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster that uses AWS Fargate. Set a static number of tasks to handle requests during times of peak usage.
- C) Deploy the model to an Amazon SageMaker endpoint. Deploy multiple copies of the model to the endpoint. Create an Application Load Balancer to route traffic between the different copies of the model at the endpoint.
- D) Deploy the model to an Amazon SageMaker endpoint. Create SageMaker endpoint auto scaling policies that are based on Amazon CloudWatch metrics to adjust the number of instances dynamically.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Sagemaker endpoint to host ML models; Cloudwatch metrics like CPU for autoscaling. 
{
 "TargetValue": 50.0,
 "CustomizedMetricSpecification":
 {
 "MetricName": "CPUUtilization",
 "Namespace": "/aws/sagemaker/Endpoints",
 "Dimensions": [
 {"Name": "EndpointName", "Value": "my-endpoint" },
 {"Name": "VariantName","Value": "my-variant"}
 ],
 "Statistic": "Average",
 "Unit": "Percent"
 }
}
---
Selected Answer: D
https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html

</details>

---

## Question 20: MLA-C01-ET-Q020
**Domain 2:** ML Model Development  

**Question:**  
A company uses Amazon SageMaker Studio to develop an ML model. The company has a single SageMaker Studio domain. An ML engineer needs to implement a solution that provides an automated alert when SageMaker compute costs reach a specific threshold.
Which solution will meet these requirements?

**Choices:**
- A) Add resource tagging by editing the SageMaker user profile in the SageMaker domain. Configure AWS Cost Explorer to send an alert when the threshold is reached.
- B) Add resource tagging by editing the SageMaker user profile in the SageMaker domain. Configure AWS Budgets to send an alert when the threshold is reached.
- C) Add resource tagging by editing each user's IAM profile. Configure AWS Cost Explorer to send an alert when the threshold is reached.
- D) Add resource tagging by editing each user's IAM profile. Configure AWS Budgets to send an alert when the threshold is reached.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Sagemaker user profiles tagging: https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-add.html 
Budgets : For cost tracking and setting thresholds
---
Selected Answer: B
This is a clear scenario for using Budgets.

</details>

---

## Question 21: MLA-C01-ET-Q021
**Domain 2:** ML Model Development  

**Question:**  
A company uses Amazon SageMaker for its ML workloads. The company's ML engineer receives a 50 MB Apache Parquet data file to build a fraud detection model. The file includes several correlated columns that are not required.
What should the ML engineer do to drop the unnecessary columns in the file with the LEAST effort?

**Choices:**
- A) Download the file to a local workstation. Perform one-hot encoding by using a custom Python script.
- B) Create an Apache Spark job that uses a custom processing script on Amazon EMR.
- C) Create a SageMaker processing job by calling the SageMaker Python SDK.
- D) Create a data flow in SageMaker Data Wrangler. Configure a transform step.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Parquet data file → SageMaker Data Wrangler → Explore data → Transform → Drop unnecessary columns → Clean and preprocess data → Export to S3 → Fraud detection model
---
Selected Answer: D
https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html

</details>

---

## Question 22: MLA-C01-ET-Q022
**Domain 2:** ML Model Development  

**Question:**  
A company is creating an application that will recommend products for customers to purchase. The application will make API calls to Amazon Q Business. The company must ensure that responses from Amazon Q Business do not include the name of the company's main competitor.
Which solution will meet this requirement?

**Choices:**
- A) Configure the competitor's name as a blocked phrase in Amazon Q Business.
- B) Configure an Amazon Q Business retriever to exclude the competitor’s name.
- C) Configure an Amazon Kendra retriever for Amazon Q Business to build indexes that exclude the competitor's name.
- D) Configure document attribute boosting in Amazon Q Business to deprioritize the competitor's name.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The correct answer is: A. Configure the competitor's name as a blocked phrase in Amazon Q Business.
✅ Explanation:
Requirement:

 Prevent Amazon Q Business from including the name of a specific competitor in its responses.

✅ Option A: Blocked Phrase

 Amazon Q Business supports blocked phrases, which you can configure to filter out or redact sensitive terms (like a competitor’s name) from its responses.
 This is a direct feature designed for this exact use case: ensuring certain words or phrases do not appear in generated content.
 Lowest operational overhead and highest precision.
---
Selected Answer: A
https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BlockedPhrasesConfiguration.html

</details>

---

## Question 23: MLA-C01-ET-Q023
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use Amazon SageMaker to fine-tune a large language model (LLM) for text summarization. The ML engineer must follow a low-code no-code (LCNC) approach.
Which solution will meet these requirements?

**Choices:**
- A) Use SageMaker Studio to fine-tune an LLM that is deployed on Amazon EC2 instances.
- B) Use SageMaker Autopilot to fine-tune an LLM that is deployed by a custom API endpoint.
- C) Use SageMaker Autopilot to fine-tune an LLM that is deployed on Amazon EC2 instances.
- D) Use SageMaker Autopilot to fine-tune an LLM that is deployed by SageMaker JumpStart.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
LCNC solution: SageMaker Autopilot → SageMaker JumpStart → Deploy pre-trained LLM → Fine-tune for text summarization
---
Selected Answer: D
https://d1.awsstatic.com/events/Summits/reinvent2023/AIM217_Democratize-ML-with-no-code-low-code-using-Amazon-SageMaker-Canvas.pdf

</details>

---

## Question 24: MLA-C01-ET-Q024
**Domain 2:** ML Model Development  

**Question:**  
A company has an ML model that needs to run one time each night to predict stock values. The model input is 3 MB of data that is collected during the current day. The model produces the predictions for the next day. The prediction process takes less than 1 minute to finish running.
How should the company deploy the model on Amazon SageMaker to meet these requirements?

**Choices:**
- A) Use a multi-model serverless endpoint. Enable caching.
- B) Use an asynchronous inference endpoint. Set the InitialInstanceCount parameter to 0.
- C) Use a real-time endpoint. Configure an auto scaling policy to scale the model to 0 when the model is not in use.
- D) Use a serverless inference endpoint. Set the MaxConcurrency parameter to 1.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
ServerlessConfig:-
MemorySizeInMB: Set to 2048 MB (options: 1024–6144 MB).
MaxConcurrency: Set to 1 (minimum for nightly predictions).
Efficient and cost-effective for one-time nightly use.
---
Selected Answer: D
"The prediction process takes less than 1 minute to finish running" so why would you provision something in the first place - go serverless

</details>

---

## Question 25: MLA-C01-ET-Q025
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer trained an ML model on Amazon SageMaker to detect automobile accidents from dosed-circuit TV footage. The ML engineer used SageMaker Data Wrangler to create a training dataset of images of accidents and non-accidents.
The model performed well during training and validation. However, the model is underperforming in production because of variations in the quality of the images from various cameras.
Which solution will improve the model's accuracy in the LEAST amount of time?

**Choices:**
- A) Collect more images from all the cameras. Use Data Wrangler to prepare a new training dataset.
- B) Recreate the training dataset by using the Data Wrangler corrupt image transform. Specify the impulse noise option.
- C) Recreate the training dataset by using the Data Wrangler enhance image contrast transform. Specify the Gamma contrast option.
- D) Recreate the training dataset by using the Data Wrangler resize image transform. Crop all images to the same size.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
It's B. Did you guys clearly understand the question? "The model performed well during training and validation. However, the model is underperforming in production because of variations in the quality of the images from various cameras."

https://aws.amazon.com/blogs/machine-learning/prepare-image-data-with-amazon-sagemaker-data-wrangler/
Corrupting an image or creating any kind of noise helps make a model more robust. The model can predict with more accuracy even if it receives a corrupted image because it was trained with corrupt and non-corrupt images.
---
Selected Answer: B
Recreate the training dataset by using the Data Wrangler corrupt image transform. Specify the impulse noise option.

 ✅ Adds noise to images, simulating low-quality or distorted camera feeds.

 ✅ Fast — can be done with existing data.

 ✅ Makes model more robust to variations in image quality.

 ✅ Best for improving accuracy in the least amount of time.
---
Selected Answer: B
Corrupting an image or creating any kind of noise helps make a model more robust. The model can predict with more accuracy even if it receives a corrupted image because it was trained with corrupt and non-corrupt images. https://aws.amazon.com/blogs/machine-learning/prepare-image-data-with-amazon-sagemaker-data-wrangler/

</details>

---

## Question 26: MLA-C01-ET-Q026
**Domain 2:** ML Model Development  

**Question:**  
A company has an application that uses different APIs to generate embeddings for input text. The company needs to implement a solution to automatically rotate the API tokens every 3 months.
Which solution will meet this requirement?

**Choices:**
- A) Store the tokens in AWS Secrets Manager. Create an AWS Lambda function to perform the rotation.
- B) Store the tokens in AWS Systems Manager Parameter Store. Create an AWS Lambda function to perform the rotation.
- C) Store the tokens in AWS Key Management Service (AWS KMS). Use an AWS managed key to perform the rotation.
- D) Store the tokens in AWS Key Management Service (AWS KMS). Use an AWS owned key to perform the rotation.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Secret manager has automatic rotation

</details>

---

## Question 28: MLA-C01-ET-Q028
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer receives datasets that contain missing values, duplicates, and extreme outliers. The ML engineer must consolidate these datasets into a single data frame and must prepare the data for ML.
Which solution will meet these requirements?

**Choices:**
- A) Use Amazon SageMaker Data Wrangler to import the datasets and to consolidate them into a single data frame. Use the cleansing and enrichment functionalities to prepare the data.
- B) Use Amazon SageMaker Ground Truth to import the datasets and to consolidate them into a single data frame. Use the human-in-the-loop capability to prepare the data.
- C) Manually import and merge the datasets. Consolidate the datasets into a single data frame. Use Amazon Q Developer to generate code snippets that will prepare the data.
- D) Manually import and merge the datasets. Consolidate the datasets into a single data frame. Use Amazon SageMaker data labeling to prepare the data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A: SageMaker Data Wrangler simplifies merging and cleaning datasets. (Correct answer)
B: Ground Truth is for labeling, not cleaning.
C: Manual merging is slow and inefficient.
D: Data Labeling adds labels but doesn’t clean data.
---
Selected Answer: A
This is basic use-case for data wrangler

</details>

---

## Question 29: MLA-C01-ET-Q029
**Domain 2:** ML Model Development  

**Question:**  
A company has historical data that shows whether customers needed long-term support from company staff. The company needs to develop an ML model to predict whether new customers will require long-term support.
Which modeling approach should the company use to meet this requirement?

**Choices:**
- A) Anomaly detection
- B) Linear regression
- C) Logistic regression
- D) Semantic segmentation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Anomaly detection: For rare events, not binary classification.
B. Linear regression: For predicting continuous numbers, not Yes/No.
C. Logistic regression: Perfect for Yes/No predictions (binary classification). --> RIGHT
D. Semantic segmentation: For images, not customer prediction.
---
Selected Answer: C
https://aws.amazon.com/what-is/logistic-regression/

</details>

---

## Question 30: MLA-C01-ET-Q030
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer has developed a binary classification model outside of Amazon SageMaker. The ML engineer needs to make the model accessible to a SageMaker Canvas user for additional tuning.
The model artifacts are stored in an Amazon S3 bucket. The ML engineer and the Canvas user are part of the same SageMaker domain.
Which combination of requirements must be met so that the ML engineer can share the model with the Canvas user? (Choose two.)

**Choices:**
- A) The ML engineer and the Canvas user must be in separate SageMaker domains.
- B) The Canvas user must have permissions to access the S3 bucket where the model artifacts are stored.
- C) The model must be registered in the SageMaker Model Registry.
- D) The ML engineer must host the model on AWS Marketplace.
- E) The ML engineer must deploy the model to a SageMaker endpoint.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
For model outside of Amazon SageMaker, canvas user needs access to S3; Model --> Model registry
---
Selected Answer: BC
That's basic how Sagemaker works.

</details>

---

## Question 31: MLA-C01-ET-Q031
**Domain 2:** ML Model Development  

**Question:**  
A company is building a deep learning model on Amazon SageMaker. The company uses a large amount of data as the training dataset. The company needs to optimize the model's hyperparameters to minimize the loss function on the validation dataset.
Which hyperparameter tuning strategy will accomplish this goal with the LEAST computation time?

**Choices:**
- A) Hyperband
- B) Grid search
- C) Bayesian optimization
- D) Random search

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Hyperband: Efficient & best --> Right answer
B. Grid Search: Exhaustive and tries all combos
C. Bayesian Optimization: Smart with best combination
D. Random Search: Random
---
Selected Answer: A
https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-now-provides-up-to-three-times-faster-hyperparameter-tuning-with-hyperband/
"efficient resource utilization and a better time-to-convergence."

</details>

---

## Question 32: MLA-C01-ET-Q032
**Domain 2:** ML Model Development  

**Question:**  
A company is planning to use Amazon Redshift ML in its primary AWS account. The source data is in an Amazon S3 bucket in a secondary account.
An ML engineer needs to set up an ML pipeline in the primary account to access the S3 bucket in the secondary account. The solution must not require public IPv4 addresses.
Which solution will meet these requirements?

**Choices:**
- A) Provision a Redshift cluster and Amazon SageMaker Studio in a VPC with no public access enabled in the primary account. Create a VPC peering connection between the accounts. Update the VPC route tables to remove the route to 0.0.0.0/0.
- B) Provision a Redshift cluster and Amazon SageMaker Studio in a VPC with no public access enabled in the primary account. Create an AWS Direct Connect connection and a transit gateway. Associate the VPCs from both accounts with the transit gateway. Update the VPC route tables to remove the route to 0.0.0.0/0.
- C) Provision a Redshift cluster and Amazon SageMaker Studio in a VPC in the primary account. Create an AWS Site-to-Site VPN connection with two encrypted IPsec tunnels between the accounts. Set up interface VPC endpoints for Amazon S3.
- D) Provision a Redshift cluster and Amazon SageMaker Studio in a VPC in the primary account. Create an S3 gateway endpoint. Update the S3 bucket policy to allow IAM principals from the primary account. Set up interface VPC endpoints for SageMaker and Amazon Redshift.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
VPC endpoints for sagemaker and gateway endpoint for S3 is needed to access without public access to connect to VPC
---
Selected Answer: D
This is privatelink use-case

</details>

---

## Question 33: MLA-C01-ET-Q033
**Domain 2:** ML Model Development  

**Question:**  
A company is using an AWS Lambda function to monitor the metrics from an ML model. An ML engineer needs to implement a solution to send an email message when the metrics breach a threshold.
Which solution will meet this requirement?

**Choices:**
- A) Log the metrics from the Lambda function to AWS CloudTrail. Configure a CloudTrail trail to send the email message.
- B) Log the metrics from the Lambda function to Amazon CloudFront. Configure an Amazon CloudWatch alarm to send the email message.
- C) Log the metrics from the Lambda function to Amazon CloudWatch. Configure a CloudWatch alarm to send the email message.
- D) Log the metrics from the Lambda function to Amazon CloudWatch. Configure an Amazon CloudFront rule to send the email message.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
CloudWatch alarm is the keyword; Needed to alert
---
Selected Answer: C
Simple event-driven architecture

</details>

---

## Question 34: MLA-C01-ET-Q034
**Domain 2:** ML Model Development  

**Question:**  
A company has used Amazon SageMaker to deploy a predictive ML model in production. The company is using SageMaker Model Monitor on the model. After a model update, an ML engineer notices data quality issues in the Model Monitor checks.
What should the ML engineer do to mitigate the data quality issues that Model Monitor has identified?

**Choices:**
- A) Adjust the model's parameters and hyperparameters.
- B) Initiate a manual Model Monitor job that uses the most recent production data.
- C) Create a new baseline from the latest dataset. Update Model Monitor to use the new baseline for evaluations.
- D) Include additional data in the existing training set for the model. Retrain and redeploy the model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (67%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon SageMaker Model Monitor:

 Continuously monitors model endpoints to detect issues like:
 Data quality drift
 Model quality drift
 Bias drift
 Feature attribution drift

Baseline:

 Model Monitor compares incoming data against a baseline dataset that represents "normal" or expected data distributions.
 If the data distribution changes after a model update, the old baseline may no longer be valid—leading to false positives in data quality issues.
---
Selected Answer: C
agree with GiorgioGss - If the problems start appearing "After a model update" then C is the only valid option.
---
Selected Answer: D
the model needs to be retrained

</details>

---

## Question 35: MLA-C01-ET-Q035
**Domain 2:** ML Model Development  

**Question:**  
A company has an ML model that generates text descriptions based on images that customers upload to the company's website. The images can be up to 50 MB in total size.
An ML engineer decides to store the images in an Amazon S3 bucket. The ML engineer must implement a processing solution that can scale to accommodate changes in demand.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Create an Amazon SageMaker batch transform job to process all the images in the S3 bucket.
- B) Create an Amazon SageMaker Asynchronous Inference endpoint and a scaling policy. Run a script to make an inference request for each image.
- C) Create an Amazon Elastic Kubernetes Service (Amazon EKS) cluster that uses Karpenter for auto scaling. Host the model on the EKS cluster. Run a script to make an inference request for each image.
- D) Create an AWS Batch job that uses an Amazon Elastic Container Service (Amazon ECS) cluster. Specify a list of images to process for each AWS Batch job.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-autoscale.html To autoscale asynchronous endpoint -> Register model -> Define and apply scaling policy; Other options are complex to implement
---
Selected Answer: B
LEAST effort = B

</details>

---

## Question 36: MLA-C01-ET-Q036
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use AWS services to identify and extract meaningful unique keywords from documents.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Use the Natural Language Toolkit (NLTK) library on Amazon EC2 instances for text pre-processing. Use the Latent Dirichlet Allocation (LDA) algorithm to identify and extract relevant keywords.
- B) Use Amazon SageMaker and the BlazingText algorithm. Apply custom pre-processing steps for stemming and removal of stop words. Calculate term frequency-inverse document frequency (TF-IDF) scores to identify and extract relevant keywords.
- C) Store the documents in an Amazon S3 bucket. Create AWS Lambda functions to process the documents and to run Python scripts for stemming and removal of stop words. Use bigram and trigram techniques to identify and extract relevant keywords.
- D) Use Amazon Comprehend custom entity recognition and key phrase extraction to identify and extract relevant keywords.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Key phrase extraction and custom entity recognition - Amazon Comprehend helps with least operational overhead.
---
Selected Answer: D
https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html

</details>

---

## Question 37: MLA-C01-ET-Q037
**Domain 2:** ML Model Development  

**Question:**  
A company needs to give its ML engineers appropriate access to training data. The ML engineers must access training data from only their own business group. The ML engineers must not be allowed to access training data from other business groups.
The company uses a single AWS account and stores all the training data in Amazon S3 buckets. All ML model training occurs in Amazon SageMaker.
Which solution will provide the ML engineers with the appropriate access?

**Choices:**
- A) Enable S3 bucket versioning.
- B) Configure S3 Object Lock settings for each user.
- C) Add cross-origin resource sharing (CORS) policies to the S3 buckets.
- D) Create IAM policies. Attach the policies to IAM users or IAM roles.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
IAM policies helps to define the access required and control. Can be applied to user or role.
---
Selected Answer: D
IAM to have 'granular' permissions

</details>

---

## Question 39: MLA-C01-ET-Q039
**Domain 2:** ML Model Development  

**Question:**  
A company needs to host a custom ML model to perform forecast analysis. The forecast analysis will occur with predictable and sustained load during the same 2-hour period every day.
Multiple invocations during the analysis period will require quick responses. The company needs AWS to manage the underlying infrastructure and any auto scaling activities.
Which solution will meet these requirements?

**Choices:**
- A) Schedule an Amazon SageMaker batch transform job by using AWS Lambda.
- B) Configure an Auto Scaling group of Amazon EC2 instances to use scheduled scaling.
- C) Use Amazon SageMaker Serverless Inference with provisioned concurrency.
- D) Run the model on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster on Amazon EC2 with pod auto scaling.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Load is predictable and sustainable with 2 hrs usage pattern; Needs quick response as well; Sagemaker - Provisioned concurrency + Serverless inference will be able to support it. https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html
---
Selected Answer: C
For only 2h each day it does not worth provisioning resources. Go serverless.

</details>

---

## Question 40: MLA-C01-ET-Q040
**Domain 2:** ML Model Development  

**Question:**  
A company's ML engineer has deployed an ML model for sentiment analysis to an Amazon SageMaker endpoint. The ML engineer needs to explain to company stakeholders how the model makes predictions.
Which solution will provide an explanation for the model's predictions?

**Choices:**
- A) Use SageMaker Model Monitor on the deployed model.
- B) Use SageMaker Clarify on the deployed model.
- C) Show the distribution of inferences from A/В testing in Amazon CloudWatch.
- D) Add a shadow endpoint. Analyze prediction differences on samples.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Sentiment analysis model → SageMaker Clarify → Analyze feature impact → Explain predictions to stakeholders

</details>

---

## Question 41: MLA-C01-ET-Q041
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer is using Amazon SageMaker to train a deep learning model that requires distributed training. After some training attempts, the ML engineer observes that the instances are not performing as expected. The ML engineer identifies communication overhead between the training instances.
What should the ML engineer do to MINIMIZE the communication overhead between the instances?

**Choices:**
- A) Place the instances in the same VPC subnet. Store the data in a different AWS Region from where the instances are deployed.
- B) Place the instances in the same VPC subnet but in different Availability Zones. Store the data in a different AWS Region from where the instances are deployed.
- C) Place the instances in the same VPC subnet. Store the data in the same AWS Region and Availability Zone where the instances are deployed.
- D) Place the instances in the same VPC subnet. Store the data in the same AWS Region but in a different Availability Zone from where the instances are deployed.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Distributed training model → Same VPC subnet → Same Region and Availability Zone for data and instances → Minimize communication overhead
---
Selected Answer: C
That's a basic network question.

</details>

---

## Question 42: MLA-C01-ET-Q042
**Domain 2:** ML Model Development  

**Question:**  
A company is running ML models on premises by using custom Python scripts and proprietary datasets. The company is using PyTorch. The model building requires unique domain knowledge. The company needs to move the models to AWS.
Which solution will meet these requirements with the LEAST effort?

**Choices:**
- A) Use SageMaker built-in algorithms to train the proprietary datasets.
- B) Use SageMaker script mode and premade images for ML frameworks.
- C) Build a container on AWS that includes custom packages and a choice of ML frameworks.
- D) Purchase similar production models through AWS Marketplace.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
On-premise PyTorch models → SageMaker script mode → Premade PyTorch images → Minimal effort to migrate
---
Selected Answer: B
https://aws.amazon.com/blogs/machine-learning/bring-your-own-model-with-amazon-sagemaker-script-mode/

"Script mode enables you to write custom training and inference code while still utilizing common ML framework containers "

</details>

---

## Question 43: MLA-C01-ET-Q043
**Domain 2:** ML Model Development  

**Question:**  
A company is using Amazon SageMaker and millions of files to train an ML model. Each file is several megabytes in size. The files are stored in an Amazon S3 bucket. The company needs to improve training performance.
Which solution will meet these requirements in the LEAST amount of time?

**Choices:**
- A) Transfer the data to a new S3 bucket that provides S3 Express One Zone storage. Adjust the training job to use the new S3 bucket.
- B) Create an Amazon FSx for Lustre file system. Link the file system to the existing S3 bucket. Adjust the training job to read from the file system.
- C) Create an Amazon Elastic File System (Amazon EFS) file system. Transfer the existing data to the file system. Adjust the training job to read from the file system.
- D) Create an Amazon ElastiCache (Redis OSS) cluster. Link the Redis OSS cluster to the existing S3 bucket. Stream the data from the Redis OSS cluster directly to the training job.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://aws.amazon.com/blogs/machine-learning/speed-up-training-on-amazon-sagemaker-using-amazon-efs-or-amazon-fsx-for-lustre-file-systems/
---
Selected Answer: B
S3 data → FSx for Lustre → High throughput and low latency → Improved training performance

</details>

---

## Question 44: MLA-C01-ET-Q044
**Domain 2:** ML Model Development  

**Question:**  
A company wants to develop an ML model by using tabular data from its customers. The data contains meaningful ordered features with sensitive information that should not be discarded. An ML engineer must ensure that the sensitive data is masked before another team starts to build the model.
Which solution will meet these requirements?

**Choices:**
- A) Use Amazon Made to categorize the sensitive data.
- B) Prepare the data by using AWS Glue DataBrew.
- C) Run an AWS Batch job to change the sensitive data to random values.
- D) Run an Amazon EMR job to change the sensitive data to random values.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `77%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (77%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Prepare the data by using AWS Glue DataBrew

 ✅ Purpose-built for data preparation — works with tabular data.

 ✅ Offers data masking, pseudonymization, and data transformations.

 ✅ No-code/low-code tool suitable for collaborative workflows between engineers and analysts.

 ✅ Keeps the order and structure of features intact.

 ✅ Best fit for masking sensitive info before ML modeling.
---
Selected Answer: B
AWS Glue DataBrew (Option B) is the most efficient and user-friendly solution for masking sensitive information while retaining the structure and order of tabular data, making it ideal for preparing data for ML model development.
AWS Macie cannot mask data.
---
Selected Answer: A
question error
made -> macie

</details>

---

## Question 45: MLA-C01-ET-Q045
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to deploy ML models to get inferences from large datasets in an asynchronous manner. The ML engineer also needs to implement scheduled monitoring of the data quality of the models. The ML engineer must receive alerts when changes in data quality occur.
Which solution will meet these requirements?

**Choices:**
- A) Deploy the models by using scheduled AWS Glue jobs. Use Amazon CloudWatch alarms to monitor the data quality and to send alerts.
- B) Deploy the models by using scheduled AWS Batch jobs. Use AWS CloudTrail to monitor the data quality and to send alerts.
- C) Deploy the models by using Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Use Amazon EventBridge to monitor the data quality and to send alerts.
- D) Deploy the models by using Amazon SageMaker batch transform. Use SageMaker Model Monitor to monitor the data quality and to send alerts.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html Model Monitor tracks data quality, model quality, bias drift, and feature attribution drift for production models. Model monitor setup with continuous monitoring with batch transform will work
---
Selected Answer: D
A is not valid. Monitoring data quality in model is done by model monitor, not by cloudwatch.

</details>

---

## Question 46: MLA-C01-ET-Q046
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer normalized training data by using min-max normalization in AWS Glue DataBrew. The ML engineer must normalize the production inference data in the same way as the training data before passing the production inference data to the model for predictions.
Which solution will meet this requirement?

**Choices:**
- A) Apply statistics from a well-known dataset to normalize the production samples.
- B) Keep the min-max normalization statistics from the training set. Use these values to normalize the production samples.
- C) Calculate a new set of min-max normalization statistics from a batch of production samples. Use these values to normalize all the production samples.
- D) Calculate a new set of min-max normalization statistics from each production sample. Use these values to normalize all the production samples.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Models are sensitive to data distribution. Consistency needed for accurate predictions and hence Option-B keeping the same min-max normalization statistics will help; Option C & D affect model performance; Option-A introduces inconsistency
---
Selected Answer: B
To ensure reliable and accurate model predictions, it's essential to use the same min-max normalization statistics from the training data.

</details>

---

## Question 47: MLA-C01-ET-Q047
**Domain 2:** ML Model Development  

**Question:**  
A company is planning to use Amazon SageMaker to make classification ratings that are based on images. The company has 6 ТВ of training data that is stored on an Amazon FSx for NetApp ONTAP system virtual machine (SVM). The SVM is in the same VPC as SageMaker.
An ML engineer must make the training data accessible for ML models that are in the SageMaker environment.
Which solution will meet these requirements?

**Choices:**
- A) Mount the FSx for ONTAP file system as a volume to the SageMaker Instance.
- B) Create an Amazon S3 bucket. Use Mountpoint for Amazon S3 to link the S3 bucket to the FSx for ONTAP file system.
- C) Create a catalog connection from SageMaker Data Wrangler to the FSx for ONTAP file system.
- D) Create a direct connection from SageMaker Data Wrangler to the FSx for ONTAP file system.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://docs.netapp.com/us-en/netapp-solutions/ai/mlops_fsxn_sagemaker_integration_training.html#introduction Option A would work since you can mount FSx for ONTAP directly to SageMaker, enabling fast access to the 6 TB data in the same VPC without extra steps

</details>

---

## Question 48: MLA-C01-ET-Q048
**Domain 2:** ML Model Development  

**Question:**  
A company regularly receives new training data from the vendor of an ML model. The vendor delivers cleaned and prepared data to the company's Amazon S3 bucket every 3-4 days.
The company has an Amazon SageMaker pipeline to retrain the model. An ML engineer needs to implement a solution to run the pipeline when new data is uploaded to the S3 bucket.
Which solution will meet these requirements with the LEAST operational effort?

**Choices:**
- A) Create an S3 Lifecycle rule to transfer the data to the SageMaker training instance and to initiate training.
- B) Create an AWS Lambda function that scans the S3 bucket. Program the Lambda function to initiate the pipeline when new data is uploaded.
- C) Create an Amazon EventBridge rule that has an event pattern that matches the S3 upload. Configure the pipeline as the target of the rule.
- D) Use Amazon Managed Workflows for Apache Airflow (Amazon MWAA) to orchestrate the pipeline when new data is uploaded.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon EventBridge can automatically trigger the SageMaker pipeline when new data is uploaded to S3, making it a simple and efficient soln.
---
Selected Answer: C
"run the pipeline when new data is uploaded to the S3 bucket." This is plain event-driven architecture.

</details>

---

## Question 50: MLA-C01-ET-Q050
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer is developing a fraud detection model by using the Amazon SageMaker XGBoost algorithm. The model classifies transactions as either fraudulent or legitimate.
During testing, the model excels at identifying fraud in the training dataset. However, the model is inefficient at identifying fraud in new and unseen transactions.
What should the ML engineer do to improve the fraud detection for new transactions?

**Choices:**
- A) Increase the learning rate.
- B) Remove some irrelevant features from the training dataset.
- C) Increase the value of the max_depth hyperparameter.
- D) Decrease the value of the max_depth hyperparameter.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
This is the scenario of overfitting where it works well with trained data and not with new data. Reducing the max_depth hyperparameter makes the model less complex, helping it generalize better to new data.

</details>

---

## Question 51: MLA-C01-ET-Q051
**Domain 2:** ML Model Development  

**Question:**  
A company has a binary classification model in production. An ML engineer needs to develop a new version of the model.
The new model version must maximize correct predictions of positive labels and negative labels. The ML engineer must use a metric to recalibrate the model to meet these requirements.
Which metric should the ML engineer use for the model recalibration?

**Choices:**
- A) Accuracy
- B) Precision
- C) Recall
- D) Specificity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
🔑 Keyword: Maximize correct predictions of both positive and negative labels
✅ Correct Answer: A. Accuracy

Why?

Accuracy measures the proportion of correctly classified instances (both positive and negative).

It is the most appropriate metric when both false positives and false negatives need to be minimized.

Why Others Are Wrong?
❌ B. Precision focuses only on correctly predicted positives, not overall correctness.
❌ C. Recall focuses only on capturing all true positives, ignoring true negatives.
❌ D. Specificity only measures the ability to identify true negatives.
---
Selected Answer: A
For imbalanced data, F1 score is preferred over confusion matrix-derived metrics. Ideally, option A would be "F1 Score". Given the choices, A (Accuracy) is the most reasonable, though not ideal.
---
Selected Answer: A
A. Accuracy: Correct choice; maximizes both true positives and true negatives. Formula: (TP + TN) / Total Predictions
B. Precision: Focuses only on true positives, not negatives. Formula: TP / (TP + FP)
C. Recall: Focuses on capturing all true positives, ignoring negatives. Formula: TP / (TP + FN)
D. Specificity: Focuses only on true negatives, ignoring positives. Formula: TN / (TN + FP)

</details>

---

## Question 52: MLA-C01-ET-Q052
**Domain 2:** ML Model Development  

**Question:**  
A company is using Amazon SageMaker to create ML models. The company's data scientists need fine-grained control of the ML workflows that they orchestrate. The data scientists also need the ability to visualize SageMaker jobs and workflows as a directed acyclic graph (DAG). The data scientists must keep a running history of model discovery experiments and must establish model governance for auditing and compliance verifications.
Which solution will meet these requirements?

**Choices:**
- A) Use AWS CodePipeline and its integration with SageMaker Studio to manage the entire ML workflows. Use SageMaker ML Lineage Tracking for the running history of experiments and for auditing and compliance verifications.
- B) Use AWS CodePipeline and its integration with SageMaker Experiments to manage the entire ML workflows. Use SageMaker Experiments for the running history of experiments and for auditing and compliance verifications.
- C) Use SageMaker Pipelines and its integration with SageMaker Studio to manage the entire ML workflows. Use SageMaker ML Lineage Tracking for the running history of experiments and for auditing and compliance verifications.
- D) Use SageMaker Pipelines and its integration with SageMaker Experiments to manage the entire ML workflows. Use SageMaker Experiments for the running history of experiments and for auditing and compliance verifications.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (67%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: D
SageMaker Pipelines provides a robust way to manage and visualize ML workflows as directed acyclic graphs (DAGs), while SageMaker Experiments helps track and manage the history of model experiments and supports model governance
---
Selected Answer: C
https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html
I don't see how you can manage the "entire ML flow" (as question asks) with something else other than Studio.
---
Selected Answer: C
🔑 Keyword: Fine-grained control, DAG visualization, model governance, auditing
✅ Correct Answer: C. Use SageMaker Pipelines and its integration with SageMaker Studio to manage the entire ML workflows. Use SageMaker ML Lineage Tracking for the running history of experiments and for auditing and compliance verifications.

Why?

SageMaker Pipelines provides workflow orchestration with DAG visualization.

SageMaker ML Lineage Tracking enables experiment history and model governance for auditing.

Why Others Are Wrong?
❌ A & B. AWS CodePipeline is more suited for software CI/CD than for ML workflows.
❌ D. SageMaker Experiments focuses on tracking experiments but lacks full model lineage tracking.

</details>

---

## Question 53: MLA-C01-ET-Q053
**Domain 2:** ML Model Development  

**Question:**  
A company wants to reduce the cost of its containerized ML applications. The applications use ML models that run on Amazon EC2 instances, AWS Lambda functions, and an Amazon Elastic Container Service (Amazon ECS) cluster. The EC2 workloads and ECS workloads use Amazon Elastic Block Store (Amazon EBS) volumes to save predictions and artifacts.
An ML engineer must identify resources that are being used inefficiently. The ML engineer also must generate recommendations to reduce the cost of these resources.
Which solution will meet these requirements with the LEAST development effort?

**Choices:**
- A) Create code to evaluate each instance's memory and compute usage.
- B) Add cost allocation tags to the resources. Activate the tags in AWS Billing and Cost Management.
- C) Check AWS CloudTrail event history for the creation of the resources.
- D) Run AWS Compute Optimizer.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
🔑 Keyword: Identify inefficient ML resources, generate cost recommendations with minimal effort
✅ Correct Answer: D. Run AWS Compute Optimizer.

Why?

AWS Compute Optimizer provides automated recommendations for optimizing EC2 instances, EBS volumes, and Lambda.

It minimizes development effort by analyzing workloads automatically.

Why Others Are Wrong?
❌ A. Writing custom code for resource evaluation is manual and inefficient.
❌ B. Cost allocation tags help track expenses but do not provide recommendations.
❌ C. CloudTrail shows historical logs but does not analyze cost inefficiencies.
---
Selected Answer: D
AWS Compute Optimizer finds wasted resources in EC2, EBS and suggests easy ways to save money and boost performance.
---
Selected Answer: D
All is compute related so, D.

</details>

---

## Question 54: MLA-C01-ET-Q054
**Domain 2:** ML Model Development  

**Question:**  
A company needs to create a central catalog for all the company's ML models. The models are in AWS accounts where the company developed the models initially. The models are hosted in Amazon Elastic Container Registry (Amazon ECR) repositories.
Which solution will meet these requirements?

**Choices:**
- A) Configure ECR cross-account replication for each existing ECR repository. Ensure that each model is visible in each AWS account.
- B) Create a new AWS account with a new ECR repository as the central catalog. Configure ECR cross-account replication between the initial ECR repositories and the central catalog.
- C) Use the Amazon SageMaker Model Registry to create a model group for models hosted in Amazon ECR. Create a new AWS account. In the new account, use the SageMaker Model Registry as the central catalog. Attach a cross-account resource policy to each model group in the initial AWS accounts.
- D) Use an AWS Glue Data Catalog to store the models. Run an AWS Glue crawler to migrate the models from the ECR repositories to the Data Catalog. Configure cross-account access to the Data Catalog.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (88%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The question asks for a "central catalog" so I believe metadata, lineage tracking are also "included". ECR could not be the solution.
---
Selected Answer: C
🔑 Keyword: Central catalog for ML models across AWS accounts, models stored in ECR
✅ Correct Answer: C. Use the Amazon SageMaker Model Registry to create a model group for models hosted in Amazon ECR. Create a new AWS account. In the new account, use the SageMaker Model Registry as the central catalog. Attach a cross-account resource policy to each model group in the initial AWS accounts.

Why?

SageMaker Model Registry provides a central catalog for ML models, supporting cross-account access.

Cross-account resource policies enable access to models across AWS accounts.

Why Others Are Wrong?
❌ A. ECR cross-account replication does not create a centralized catalog.
❌ B. A new ECR repository with replication does not offer model versioning or governance.
❌ D. AWS Glue Data Catalog is for metadata storage, not for ML model management.
---
Selected Answer: B
This approach allows you to centralize all models in a single ECR repository, making it easier to manage and access them across different AWS accounts. Cross-account replication ensures that the models are synchronized between the initial repositories and the central catalog, maintaining consistency and availability.

</details>

---

## Question 55: MLA-C01-ET-Q055
**Domain 2:** ML Model Development  

**Question:**  
A company has developed a new ML model. The company requires online model validation on 10% of the traffic before the company fully releases the model in production. The company uses an Amazon SageMaker endpoint behind an Application Load Balancer (ALB) to serve the model.
Which solution will set up the required online validation with the LEAST operational overhead?

**Choices:**
- A) Use production variants to add the new model to the existing SageMaker endpoint. Set the variant weight to 0.1 for the new model. Monitor the number of invocations by using Amazon CloudWatch.
- B) Use production variants to add the new model to the existing SageMaker endpoint. Set the variant weight to 1 for the new model. Monitor the number of invocations by using Amazon CloudWatch.
- C) Create a new SageMaker endpoint. Use production variants to add the new model to the new endpoint. Monitor the number of invocations by using Amazon CloudWatch.
- D) Configure the ALB to route 10% of the traffic to the new model at the existing SageMaker endpoint. Monitor the number of invocations by using AWS CloudTrail.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
🔑 Keyword: Validate new model on 10% of traffic with minimal overhead
✅ Correct Answer: A. Use production variants to add the new model to the existing SageMaker endpoint. Set the variant weight to 0.1 for the new model. Monitor the number of invocations by using Amazon CloudWatch.

Why?

SageMaker production variants allow traffic splitting across multiple models on a single endpoint.

Setting variant weight to 0.1 ensures only 10% of traffic is sent to the new model.

CloudWatch can monitor invocations for validation.

Why Others Are Wrong?
❌ B. Setting the variant weight to 1 will send all traffic to the new model, defeating the purpose.
❌ C. Creating a new endpoint increases operational overhead unnecessarily.
❌ D. ALB-based routing is more complex than using SageMaker variants for traffic splitting.
---
Selected Answer: A
https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html
---
Selected Answer: A
{
 'ProductionVariants': [
 {
 'VariantName': 'existing-model',
 'ModelName': 'existing-model',
 'InitialVariantWeight': 0.9
 },
 {
 'VariantName': 'new-model',
 'ModelName': 'new-model',
 'InitialVariantWeight': 0.1
 }
 ]
}

</details>

---

## Question 56: MLA-C01-ET-Q056
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer notices class imbalance in an image classification training job.

What should the ML engineer do to resolve this issue?

**Choices:**
- A) Reduce the size of the dataset.
- B) Transform some of the images in the dataset.
- C) Apply random oversampling on the dataset.
- D) Apply random data splitting on the dataset.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The most common family of techniques in this category is resampling, which includes oversampling (adding more instances from the minority classes) and undersampling (removing instances from the majority classes)
---
Selected Answer: C
correct

</details>

---

## Question 57: MLA-C01-ET-Q057
**Domain 2:** ML Model Development  

**Question:**  
A company receives daily .csv files about customer interactions with its ML model. The company stores the files in Amazon S3 and uses the files to retrain the model. An ML engineer needs to implement a solution to mask credit card numbers in the files before the model is retrained.

Which solution will meet this requirement with the LEAST development effort?

**Choices:**
- A) Create a discovery job in Amazon Macie. Configure the job to find and mask sensitive data.
- B) Create Apache Spark code to run on an AWS Glue job. Use the Sensitive Data Detection functionality in AWS Glue to find and mask sensitive data.
- C) Create Apache Spark code to run on an AWS Glue job. Program the code to perform a regex operation to find and mask sensitive data.
- D) Create Apache Spark code to run on an Amazon EC2 instance. Program the code to perform an operation to find and mask sensitive data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (67%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
La empresa necesita una solución automatizada para enmascarar números de tarjetas de crédito en archivos CSV almacenados en Amazon S3, antes de que los datos sean utilizados para reentrenar un modelo de Machine Learning.

La opción B es la mejor solución porque:

✅ AWS Glue tiene integración nativa con S3, lo que facilita el procesamiento de los archivos sin desarrollo adicional.
✅ Glue Studio proporciona detección de datos sensibles (Sensitive Data Detection), lo que reduce el esfuerzo de desarrollo comparado con programar regex manualmente.
✅ Es una solución completamente administrada, eliminando la necesidad de mantener infraestructura en EC2.
✅ Spark en AWS Glue permite manejar grandes volúmenes de datos, ideal para procesamiento de múltiples archivos diarios.
---
Selected Answer: B
Macie can't take any actions, It can be only a discovery service.
---
Selected Answer: A
correct

</details>

---

## Question 58: MLA-C01-ET-Q058
**Domain 2:** ML Model Development  

**Question:**  
A company needs to extract entities from a PDF document to build a classifier model.

Which solution will extract and store the entities in the LEAST amount of time?

**Choices:**
- A) Use Amazon Comprehend to extract the entities. Store the output in Amazon S3.
- B) Use an open source AI optical character recognition (OCR) tool on Amazon SageMaker to extract the entities. Store the output in Amazon S3.
- C) Use Amazon Textract to extract the entities. Use Amazon Comprehend to convert the entities to text. Store the output in Amazon S3.
- D) Use Amazon Textract integrated with Amazon Augmented AI (Amazon A2I) to extract the entities. Store the output in Amazon S3.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `50%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (50%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: A
https://aws.amazon.com/blogs/aws/now-process-pdfs-word-documents-and-images-with-amazon-comprehend-for-idp/
Amazon Comprehend feature for intelligent document processing (IDP). This feature allows you to classify and extract entities from PDF documents, Microsoft Word files, and images directly from Amazon Comprehend without you needing to extract the text first.
---
Selected Answer: C
Agree with C.

Normally Amazon Comprehend is sufficient if the pdf contains only text. Since the question does not mention the exact contents of the pdf files. It would be safer to use Amazon Textract to extract the text, then Amazon Comprehend do the entity extraction.

</details>

---

## Question 59: MLA-C01-ET-Q059
**Domain 2:** ML Model Development  

**Question:**  
A company shares Amazon SageMaker Studio notebooks that are accessible through a VPN. The company must enforce access controls to prevent malicious actors from exploiting presigned URLs to access the notebooks.

Which solution will meet these requirements?

**Choices:**
- A) Set up Studio client IP validation by using the aws:sourceIp IAM policy condition.
- B) Set up Studio client VPC validation by using the aws:sourceVpc IAM policy condition.
- C) Set up Studio client role endpoint validation by using the aws:PrimaryTag IAM policy condition.
- D) Set up Studio client user endpoint validation by using the aws:PrincipalTag IAM policy condition.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `57%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (57%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
VPN - predefined IP range
---
Selected Answer: A
✅ Explanation:
Context:

 The company is using Amazon SageMaker Studio notebooks.
 Access is allowed through a VPN, meaning users are coming from known, fixed IP ranges.
 The concern is unauthorized access via presigned URLs, which could potentially be used outside the trusted network.

✅ Why aws:sourceIp is the right choice:

 The aws:sourceIp condition in IAM policies allows you to restrict access based on the client's IP address.
 This is perfect for VPN-based setups where you know the IP range.
 It ensures that only users accessing from allowed IPs (e.g., your VPN subnet) can access SageMaker Studio resources, even if they have a valid presigned URL.
 This directly mitigates the risk of URL misuse from outside the VPN.
---
Selected Answer: A
A is correct.

https://aws.amazon.com/blogs/machine-learning/secure-amazon-sagemaker-studio-presigned-urls-part-1-foundational-infrastructure/

Studio supports a few methods for enforcing access controls against presigned URL data exfiltration:

Client IP validation using the IAM policy condition aws:sourceIp
Client VPC validation using the IAM condition aws:sourceVpc
Client VPC endpoint validation using the IAM policy condition aws:sourceVpce

</details>

---

## Question 60: MLA-C01-ET-Q060
**Domain 2:** ML Model Development  

**Question:**  
Case study -
An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3.
The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data.
After the data is aggregated, the ML engineer must implement a solution to automatically detect anomalies in the data and to visualize the result.
Which solution will meet these requirements?

**Choices:**
- A) Use Amazon Athena to automatically detect the anomalies and to visualize the result.
- B) Use Amazon Redshift Spectrum to automatically detect the anomalies. Use Amazon QuickSight to visualize the result.
- C) Use Amazon SageMaker Data Wrangler to automatically detect the anomalies and to visualize the result.
- D) Use AWS Batch to automatically detect the anomalies. Use Amazon QuickSight to visualize the result.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
SageMaker Data Wangler identify anomalies as part of the Data Quality and Insights Report (https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-insights.html) and provides various options for data visualization - https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-analyses.html
---
Selected Answer: C
Why Transform Categorical Data into Numerical Data?
 Machine learning algorithms generally require categorical data to be converted into numerical representations (e.g., one-hot encoding or embeddings) for training. Transforming numerical data into categorical data is unnecessary unless the problem explicitly requires it (e.g., binning for some specific applications).

Why Use SageMaker Data Wrangler?
 Minimal Operational Overhead: Amazon SageMaker Data Wrangler provides a user-friendly interface to clean, preprocess, and transform data without needing to write custom code.
 Comprehensive Data Handling: Supports data sources like S3 and on-premises databases, and can handle both categorical and numerical data transformations efficiently.

Why Not AWS Glue?
 AWS Glue is more suitable for large-scale ETL (Extract, Transform, Load) operations, such as schema inference or combining large datasets. It has higher operational overhead for specific ML data preprocessing tasks compared to SageMaker Data Wrangler.
---
Selected Answer: C
https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-analyses.html
"Amazon SageMaker Data Wrangler includes built-in analyses that help you generate visualizations and data analyses in a few clicks. "
This question is tricky because it makes you think you need Quicksight for the "visualization' part.

</details>

---

## Question 61: MLA-C01-ET-Q061
**Domain 2:** ML Model Development  

**Question:**  
A company needs to develop an ML model. The model must identify an item in an image and must provide the location of the item.

Which Amazon SageMaker algorithm will meet these requirements?

**Choices:**
- A) Image classification
- B) XGBoost
- C) Object detection
- D) K-nearest neighbors (k-NN)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
🔑 Keyword: Identify an item in an image and provide its location
✅ Correct Answer: C. Object detection

Why?

Object detection algorithms detect and localize objects within images (bounding boxes).

SageMaker supports built-in object detection using SSD (Single Shot Multibox Detector) and Faster R-CNN.

Why Others Are Wrong?
❌ A. Image classification only identifies the object but does not provide its location.
❌ B. XGBoost is a gradient boosting algorithm for structured/tabular data, not images.
❌ D. k-NN is for classification/regression, not object localization.
---
Selected Answer: C
https://docs.aws.amazon.com/sagemaker/latest/dg/algo-object-detection-tech-notes.html

</details>

---

## Question 62: MLA-C01-ET-Q062
**Domain 2:** ML Model Development  

**Question:**  
A company has an Amazon S3 bucket that contains 1 ТВ of files from different sources. The S3 bucket contains the following file types in the same S3 folder: CSV, JSON, XLSX, and Apache Parquet.

An ML engineer must implement a solution that uses AWS Glue DataBrew to process the data. The ML engineer also must store the final output in Amazon S3 so that AWS Glue can consume the output in the future.

Which solution will meet these requirements?

**Choices:**
- A) Use DataBrew to process the existing S3 folder. Store the output in Apache Parquet format.
- B) Use DataBrew to process the existing S3 folder. Store the output in AWS Glue Parquet format.
- C) Separate the data into a different folder for each file type. Use DataBrew to process each folder individually. Store the output in Apache Parquet format.
- D) Separate the data into a different folder for each file type. Use DataBrew to process each folder individually. Store the output in AWS Glue Parquet format.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `57%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (57%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
🔑 Keyword: Process mixed file types with AWS Glue DataBrew & store for AWS Glue
✅ Correct Answer: A. Use DataBrew to process the existing S3 folder. Store the output in Apache Parquet format.

Why?

AWS Glue performs best with Parquet because it is optimized for analytical queries.

No need to split data into separate folders—DataBrew can handle mixed file types.

Why Others Are Wrong?
❌ B. "AWS Glue Parquet format" is not a valid term. Apache Parquet is the correct format.
❌ C & D. Separating files into different folders is unnecessary—DataBrew can process multiple formats in a single folder.
---
Selected Answer: A
C implies that you have to re-organize all files (1 TB is a lot). This means a lot of work. For me is A, less performance but without initial overhead of organization
---
Selected Answer: C
✅ Explanation:
Problem Summary:

 The data in S3 is mixed file formats: CSV, JSON, XLSX, and Parquet — all in one folder.
 You need to use AWS Glue DataBrew to process the data.
 The processed data must be stored in S3 for AWS Glue to consume later.

Key Considerations:

 DataBrew Input Requirements:
 DataBrew datasets must be in a consistent format (CSV, JSON, XLSX, or Parquet).
 DataBrew cannot process mixed formats in a single dataset. You must split the data by format.

 DataBrew Output Format:
 Apache Parquet is preferred for:
 Efficient storage
 Better performance with AWS Glue and other analytics tools
 Columnar storage benefits in querying and transformations

 "AWS Glue Parquet format" does not exist — this is a distractor in the answer options.

</details>

---

## Question 63: MLA-C01-ET-Q063
**Domain 2:** ML Model Development  

**Question:**  
A manufacturing company uses an ML model to determine whether products meet a standard for quality. The model produces an output of "Passed" or "Failed." Robots separate the products into the two categories by using the model to analyze photos on the assembly line.

Which metrics should the company use to evaluate the model's performance? (Choose two.)

**Choices:**
- A) Precision and recall
- B) Root mean square error (RMSE) and mean absolute percentage error (MAPE)
- C) Accuracy and F1 score
- D) Bilingual Evaluation Understudy (BLEU) score
- E) Perplexity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Precision and recall
C. Accuracy and F1 score

</details>

---

## Question 64: MLA-C01-ET-Q064
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to encrypt all data in transit when an ML training job runs. The ML engineer must ensure that encryption in transit is applied to processes that Amazon SageMaker uses during the training job.

Which solution will meet these requirements?

**Choices:**
- A) Encrypt communication between nodes for batch processing.
- B) Encrypt communication between nodes in a training cluster.
- C) Specify an AWS Key Management Service (AWS KMS) key during creation of the training job request.
- D) Specify an AWS Key Management Service (AWS KMS) key during creation of the SageMaker domain.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
🔑 Keyword: Encrypt data in transit during SageMaker training
✅ Correct Answer: B. Encrypt communication between nodes in a training cluster.

Why?

Encryption in transit refers to securing data as it moves between components of the SageMaker training infrastructure (e.g., between nodes in a distributed training job).

SageMaker automatically encrypts communication between nodes using TLS 1.2 in multi-node training clusters.

Why Others Are Wrong?
❌ A. "Batch processing" is not relevant to SageMaker training jobs.
❌ C. AWS KMS is used for encrypting data at rest, not for securing in-transit data.
❌ D. SageMaker domain encryption is for Studio environments, not training jobs.
---
Selected Answer: B
this is it

</details>

---

## Question 66: MLA-C01-ET-Q066
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use metrics to assess the quality of a time-series forecasting model.

Which metrics apply to this model? (Choose two.)

**Choices:**
- A) Recall
- B) LogLoss
- C) Root mean square error (RMSE)
- D) InferenceLatency
- E) Average weighted quantile loss (wQL)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CE (100%). Contributor Answer: CE.

Community Rationale & Discussion:
Selected Answer: CE
C. Root mean square error (RMSE)
✅ E. Average weighted quantile loss (wQL)
Here's why:

 RMSE is a standard regression metric that measures the average magnitude of the error between predicted and actual values. It penalizes larger errors more than smaller ones.

 Weighted Quantile Loss (wQL) is commonly used in probabilistic forecasting models (e.g., Amazon Forecast, DeepAR). It assesses the accuracy of quantile predictions.
---
Selected Answer: CE
🔑 Keyword: Time-series forecasting model evaluation metrics
✅ Correct Answers: C. Root mean square error (RMSE) & E. Average weighted quantile loss (wQL)

Why?

RMSE (Root Mean Square Error): Measures error magnitude in time-series predictions.

wQL (Weighted Quantile Loss): Used in Amazon Forecast to evaluate quantile forecasts.

Why Others Are Wrong?
❌ A. Recall is a classification metric, not for forecasting.
❌ B. LogLoss is used for classification models, not time-series.
❌ D. Inference latency is about model performance, not accuracy.

</details>

---

## Question 67: MLA-C01-ET-Q067
**Domain 2:** ML Model Development  

**Question:**  
A company runs Amazon SageMaker ML models that use accelerated instances. The models require real-time responses. Each model has different scaling requirements. The company must not allow a cold start for the models.

Which solution will meet these requirements?

**Choices:**
- A) Create a SageMaker Serverless Inference endpoint for each model. Use provisioned concurrency for the endpoints.
- B) Create a SageMaker Asynchronous Inference endpoint for each model. Create an auto scaling policy for each endpoint.
- C) Create a SageMaker endpoint. Create an inference component for each model. In the inference component settings, specify the newly created endpoint. Create an auto scaling policy for each inference component. Set the parameter for the minimum number of copies to at least 1.
- D) Create an Amazon S3 bucket. Store all the model artifacts in the S3 bucket. Create a SageMaker multi-model endpoint. Point the endpoint to the S3 bucket. Create an auto scaling policy for the endpoint. Set the parameter for the minimum number of copies to at least 1.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (67%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
✅ Explanation:
Requirements Recap:

 Real-time inference: Needs low-latency predictions.
 Accelerated instances: Likely GPU-backed, costly to scale inefficiently.
 No cold starts: Endpoints must always be warm and responsive.
 Each model has different scaling needs: Must support independent scaling of each model.

✅ Why Option C is correct:

 Inference components are a new SageMaker feature that allow:
 Hosting multiple models on a single endpoint.
 Independent scaling of each model (component).
 Avoiding cold starts via minimum number of copies.
 Setting min invocations or min replicas ≥ 1 keeps the model always warm, eliminating cold starts.
 This solution meets all requirements efficiently.
---
Selected Answer: A
this is correct

</details>

---

## Question 68: MLA-C01-ET-Q068
**Domain 2:** ML Model Development  

**Question:**  
A company runs training jobs on Amazon SageMaker by using a compute optimized instance. Demand for training runs will remain constant for the next 55 weeks. The instance needs to run for 35 hours each week. The company needs to reduce its model training costs.

Which solution will meet these requirements?

**Choices:**
- A) Use a serverless endpoint with a provisioned concurrency of 35 hours for each week. Run the training on the endpoint.
- B) Use SageMaker Edge Manager for the training. Specify the instance requirement in the edge device configuration. Run the training.
- C) Use the heterogeneous cluster feature of SageMaker Training. Configure the instance_type, instance_count, and instance_groups arguments to run training jobs.
- D) Opt in to a SageMaker Savings Plan with a 1-year term and an All Upfront payment. Run a SageMaker Training job on the instance.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
SageMaker Savings Plans offer a discount for long-term use of SageMaker instances.

</details>

---

## Question 69: MLA-C01-ET-Q069
**Domain 2:** ML Model Development  

**Question:**  
A company has an ML model that uses historical transaction data to predict customer behavior. An ML engineer is optimizing the model in Amazon SageMaker to enhance the model's predictive accuracy. The ML engineer must examine the input data and the resulting predictions to identify trends that could skew the model's performance across different demographics.

Which solution will provide this level of analysis?

**Choices:**
- A) Use Amazon CloudWatch to monitor network metrics and CPU metrics for resource optimization during model training.
- B) Create AWS Glue DataBrew recipes to correct the data based on statistics from the model output.
- C) Use SageMaker Clarify to evaluate the model and training data for underlying patterns that might affect accuracy.
- D) Create AWS Lambda functions to automate data pre-processing and to ensure consistent quality of input data for the model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Option C - SageMaker Clarify is built for bias detection and explainability.   
It can analyze training data and model predictions to identify potential biases.   
It provides insights into how different demographic groups are affected by the model.

</details>

---

## Question 70: MLA-C01-ET-Q070
**Domain 2:** ML Model Development  

**Question:**  
A company uses 10 Reserved Instances of accelerated instance types to serve the current version of an ML model. An ML engineer needs to deploy a new version of the model to an Amazon SageMaker real-time inference endpoint.

The solution must use the original 10 instances to serve both versions of the model. The solution also must include one additional Reserved Instance that is available to use in the deployment process. The transition between versions must occur with no downtime or service interruptions.

Which solution will meet these requirements?

**Choices:**
- A) Configure a blue/green deployment with all-at-once traffic shifting.
- B) Configure a blue/green deployment with canary traffic shifting and a size of 10%.
- C) Configure a shadow test with a traffic sampling percentage of 10%.
- D) Configure a rolling deployment with a rolling batch size of 1.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
this is it
---
Selected Answer: B
should be B.

D doesn’t provide a clear strategy for managing traffic during the transition.

</details>

---

## Question 71: MLA-C01-ET-Q071
**Domain 2:** ML Model Development  

**Question:**  
An IoT company uses Amazon SageMaker to train and test an XGBoost model for object detection. ML engineers need to monitor performance metrics when they train the model with variants in hyperparameters. The ML engineers also need to send Short Message Service (SMS) text messages after training is complete.

Which solution will meet these requirements?

**Choices:**
- A) Use Amazon CloudWatch to monitor performance metrics. Use Amazon Simple Queue Service (Amazon SQS) for message delivery.
- B) Use Amazon CloudWatch to monitor performance metrics. Use Amazon Simple Notification Service (Amazon SNS) for message delivery.
- C) Use AWS CloudTrail to monitor performance metrics. Use Amazon Simple Queue Service (Amazon SQS) for message delivery.
- D) Use AWS CloudTrail to monitor performance metrics. Use Amazon Simple Notification Service (Amazon SNS) for message delivery.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Option A and C out (SQS). Cloudtrail not monitor performance metrcs
---
Selected Answer: B
Cloudwatch with SNS, SQS is for queuing messages and not sending.
CloudTrail options doesn't apply here

</details>

---

## Question 72: MLA-C01-ET-Q072
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer has deployed an Amazon SageMaker model to a serverless endpoint in production. The model is invoked by the InvokeEndpoint API operation.

The model's latency in production is higher than the baseline latency in the test environment. The ML engineer thinks that the increase in latency is because of model startup time.

What should the ML engineer do to confirm or deny this hypothesis?

**Choices:**
- A) Schedule a SageMaker Model Monitor job. Observe metrics about model quality.
- B) Schedule a SageMaker Model Monitor job with Amazon CloudWatch metrics enabled.
- C) Enable Amazon CloudWatch metrics. Observe the ModelSetupTime metric in the SageMaker namespace.
- D) Enable Amazon CloudWatch metrics. Observe the ModelLoadingWaitTime metric in the SageMaker namespace.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (67%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: C
C. Enable Amazon CloudWatch metrics. Observe the ModelSetupTime metric in the SageMaker namespace.

 ✅ Correct: This metric will show if model startup time is contributing to the latency.

 ✅ Directly confirms or denies the cold start hypothesis.

ModelSetupTime 
The time it takes to launch new compute resources for a serverless endpoint. The time can vary depending on the model size, how long it takes to download the model, and the start-up time of the container.

Units: Microseconds

Valid statistics: Average, Min, Max, Sample Count, Percentiles

https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html
---
Selected Answer: D
ModelLoadingWaitTime metric 
measures the time taken to load the model

</details>

---

## Question 73: MLA-C01-ET-Q073
**Domain 2:** ML Model Development  

**Question:**  
A company must install a custom script on any newly created Amazon SageMaker notebook instances.

Which solution will meet this requirement with the LEAST operational overhead?

**Choices:**
- A) Create a lifecycle configuration script to install the custom script when a new SageMaker notebook is created. Attach the lifecycle configuration to every new SageMaker notebook as part of the creation steps.
- B) Create a custom Amazon Elastic Container Registry (Amazon ECR) image that contains the custom script. Push the ECR image to a Docker registry. Attach the Docker image to a SageMaker Studio domain. Select the kernel to run as part of the SageMaker notebook.
- C) Create a custom package index repository. Use AWS CodeArtifact to manage the installation of the custom script. Set up AWS PrivateLink endpoints to connect CodeArtifact to the SageMaker instance. Install the script.
- D) Store the custom script in Amazon S3. Create an AWS Lambda function to install the custom script on new SageMaker notebooks. Configure Amazon EventBridge to invoke the Lambda function when a new SageMaker notebook is initialized.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
correct

</details>

---

## Question 74: MLA-C01-ET-Q074
**Domain 2:** ML Model Development  

**Question:**  
A company is building a real-time data processing pipeline for an ecommerce application. The application generates a high volume of clickstream data that must be ingested, processed, and visualized in near real time. The company needs a solution that supports SQL for data processing and Jupyter notebooks for interactive analysis.

Which solution will meet these requirements?

**Choices:**
- A) Use Amazon Data Firehose to ingest the data. Create an AWS Lambda function to process the data. Store the processed data in Amazon S3. Use Amazon QuickSight to visualize the data.
- B) Use Amazon Kinesis Data Streams to ingest the data. Use Amazon Data Firehose to transform the data. Use Amazon Athena to process the data. Use Amazon QuickSight to visualize the data.
- C) Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to ingest the data. Use AWS Glue with PySpark to process the data. Store the processed data in Amazon S3. Use Amazon QuickSight to visualize the data.
- D) Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to ingest the data. Use Amazon Managed Service for Apache Flink to process the data. Use the built-in Flink dashboard to visualize the data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `50%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (50%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
✅ Why Option D is correct:
Requirements Recap:

 Real-time ingestion of high-volume clickstream data
 SQL-based data processing
 Jupyter notebooks for interactive analysis
 Near real-time visualization

Amazon MSK + Managed Flink (Apache Flink):

 MSK is ideal for handling high-throughput, real-time event streams like clickstream data.
 Amazon Managed Service for Apache Flink:
 Provides stream processing with low latency
 Supports SQL via Apache Flink SQL
 Can integrate with Jupyter Notebooks via Apache Zeppelin or SageMaker notebooks (for interactive analysis)
 Flink dashboard allows for real-time data visualization and monitoring

This stack is purpose-built for real-time streaming analytics, supports SQL for processing, and integrates well with notebooks and dashboards.
---
Selected Answer: B
correct
---
Selected Answer: C
Should be C.

AWS Glue with PySpark supports SQL-like transformations and can be integrated with Jupyter notebooks.

D is incorrect because Apache Flink for processing does not natively support SQL for data processing.

</details>

---

## Question 75: MLA-C01-ET-Q075
**Domain 2:** ML Model Development  

**Question:**  
A medical company needs to store clinical data. The data includes personally identifiable information (PII) and protected health information (PHI).

An ML engineer needs to implement a solution to ensure that the PII and PHI are not used to train ML models.

Which solution will meet these requirements?

**Choices:**
- A) Store the clinical data in Amazon S3 buckets. Use AWS Glue DataBrew to mask the PII and PHI before the data is used for model training.
- B) Upload the clinical data to an Amazon Redshift database. Use built-in SQL stored procedures to automatically classify and mask the PII and PHI before the data is used for model training.
- C) Use Amazon Comprehend to detect and mask the PII before the data is used for model training. Use Amazon Comprehend Medical to detect and mask the PHI before the data is used for model training.
- D) Create an AWS Lambda function to encrypt the PII and PHI. Program the Lambda function to save the encrypted data to an Amazon S3 bucket for model training.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
correct

</details>

---

## Question 76: MLA-C01-ET-Q076
**Domain 2:** ML Model Development  

**Question:**  
Case study -
An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3.
The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data.
The training dataset includes categorical data and numerical data. The ML engineer must prepare the training dataset to maximize the accuracy of the model.
Which action will meet this requirement with the LEAST operational overhead?

**Choices:**
- A) Use AWS Glue to transform the categorical data into numerical data.
- B) Use AWS Glue to transform the numerical data into categorical data.
- C) Use Amazon SageMaker Data Wrangler to transform the categorical data into numerical data.
- D) Use Amazon SageMaker Data Wrangler to transform the numerical data into categorical data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
You need to transform category to numeric as ML model works with numbers, thus it is either A or C. Data Wrangler provides a builtin transformation to encode categorical data - https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-cat-encode while Glue doesn't provide a managed transformation for encoding data - https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-transforms.html
---
Selected Answer: C
Data Wrangler can be used for encoding categorical data, i.e. the process of creating a numerical representation for categories. Categorical encoding encodes categorical data that is in string format into arrays of integers. Data Wrangler supports ordinal and a one-hot encoding, also similarity encoding (more advanced). 
https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-cat-encode

AWS Glue also has Data science recipe steps for One Hot Encoding and Categorical Mapping. 
https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.data-science.html

However Data Wrangler is more user-friendly with visual and natural language interfaces for less operational overhead
---
Selected Answer: C
https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html

</details>

---

## Question 77: MLA-C01-ET-Q077
**Domain 2:** ML Model Development  

**Question:**  
Case study -
An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3.
The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data.
Before the ML engineer trains the model, the ML engineer must resolve the issue of the imbalanced data.
Which solution will meet this requirement with the LEAST operational effort?

**Choices:**
- A) Use Amazon Athena to identify patterns that contribute to the imbalance. Adjust the dataset accordingly.
- B) Use Amazon SageMaker Studio Classic built-in algorithms to process the imbalanced dataset.
- C) Use AWS Glue DataBrew built-in features to oversample the minority class.
- D) Use the Amazon SageMaker Data Wrangler balance data operation to oversample the minority class.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
LEAST effort
https://aws.amazon.com/blogs/machine-learning/balance-your-data-for-machine-learning-with-amazon-sagemaker-data-wrangler/
---
Selected Answer: D
SageMaker Data Wrangler provides a "balance data" operation designed to handle class imbalance.
---
Selected Answer: D
Both Glue DataBrew and Data Wrangler allows data preparation for ML with no-code/low-code (aka low ops effort). However, Data Wrangler provides built-in transformation for balancing dataset (random oversampling, random undersampling and smote) https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-balance-data while DataBrew doesn't provide built-in recipe step for balancing dataset, actually it provides a smaller set of data science recipe steps limited to binarization, bucketization, categorical mapping, one-hot encoding, scaling, skewness and tokenization https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.data-science.html

</details>

---

## Question 78: MLA-C01-ET-Q078
**Domain 2:** ML Model Development  

**Question:**  
Case study -
An ML engineer is developing a fraud detection model on AWS. The training dataset includes transaction logs, customer profiles, and tables from an on-premises MySQL database. The transaction logs and customer profiles are stored in Amazon S3.
The dataset has a class imbalance that affects the learning of the model's algorithm. Additionally, many of the features have interdependencies. The algorithm is not capturing all the desired underlying patterns in the data.
The ML engineer needs to use an Amazon SageMaker built-in algorithm to train the model.
Which algorithm should the ML engineer use to meet this requirement?

**Choices:**
- A) LightGBM
- B) Linear learner
- C) К-means clustering
- D) Neural Topic Model (NTM)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `57%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (57%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://docs.aws.amazon.com/en_kr/sagemaker/latest/dg/lightgbm.html
---
Selected Answer: B
Answer is B
---
Selected Answer: A
1. Clase desbalanceada:

LightGBM (Light Gradient Boosted Machine) es muy eficaz para trabajar con datasets desbalanceados, gracias a su capacidad para ajustar los pesos de clases y usar técnicas como el weighted loss o boosting adaptativo.
2. Interdependencia entre variables:

LightGBM puede capturar relaciones no lineales e interacciones entre variables gracias a su estructura basada en árboles de decisión. Esto lo hace más adecuado que modelos lineales como el Linear Learner, que solo captura relaciones lineales.
3. No captura de patrones complejos:

La descripción indica que el algoritmo actual no está capturando patrones subyacentes complejos, lo que sugiere la necesidad de un modelo más robusto como LightGBM, capaz de modelar relaciones complejas y no lineales en los datos

</details>

---

## Question 79: MLA-C01-ET-Q079
**Domain 2:** ML Model Development  

**Question:**  
A company has deployed an XGBoost prediction model in production to predict if a customer is likely to cancel a subscription. The company uses Amazon SageMaker Model Monitor to detect deviations in the F1 score.
During a baseline analysis of model quality, the company recorded a threshold for the F1 score. After several months of no change, the model's F1 score decreases significantly.
What could be the reason for the reduced F1 score?

**Choices:**
- A) Concept drift occurred in the underlying customer data that was used for predictions.
- B) The model was not sufficiently complex to capture all the patterns in the original baseline data.
- C) The original baseline data had a data quality issue of missing values.
- D) Incorrect ground truth labels were provided to Model Monitor during the calculation of the baseline.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Yes, concept drift is an evolution of data that invalidates the data model. It happens when the statistical properties of the target variable, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions become less accurate as time passes. 
B. No, if it was the case the F1 would have been low since the begin and this is not justifying a change after months
C. No, same as B
D. No, incorrect labels in the baseline calculations would undermine F1 baseline value, but this is not explain a significant drop after months
---
Selected Answer: A
Concept Drift: Occurs when the statistical properties of the data used for predictions change over time, causing the model to underperform on current data.

Why Not the Other Options?

B. If the model complexity was insufficient, the issue would have been detected during the initial evaluation or baseline analysis, not after months of stable performance.
C. A data quality issue would have impacted the model's performance immediately after deployment, not months later.
D. Incorrect labels during baseline calculation could result in an inaccurate baseline F1 score, but it wouldn't explain a significant drop after stable performance over months.
---
Selected Answer: A
Concept Drift: Refers to the change in the statistical properties of the underlying data distribution over time --> Decrease F1 score --> perform poorly on new data

</details>

---

## Question 80: MLA-C01-ET-Q080
**Domain 2:** ML Model Development  

**Question:**  
A company has a team of data scientists who use Amazon SageMaker notebook instances to test ML models. When the data scientists need new permissions, the company attaches the permissions to each individual role that was created during the creation of the SageMaker notebook instance.
The company needs to centralize management of the team's permissions.
Which solution will meet this requirement?

**Choices:**
- A) Create a single IAM role that has the necessary permissions. Attach the role to each notebook instance that the team uses.
- B) Create a single IAM group. Add the data scientists to the group. Associate the group with each notebook instance that the team uses.
- C) Create a single IAM user. Attach the AdministratorAccess AWS managed IAM policy to the user. Configure each notebook instance to use the IAM user.
- D) Create a single IAM group. Add the data scientists to the group. Create an IAM role. Attach the AdministratorAccess AWS managed IAM policy to the role. Associate the role with the group. Associate the group with each notebook instance that the team uses.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Yet another unclear question from AWS ... anyway, I am basically picking A as all the other options are not applicable or are unclear.

A. Yes, this make sense
B. No, you cannot assign (aka associate) group to notebook instances
C. No, for two reason: AdministratorAccess policy is overly broad (violate least privilege principle) and you cannot assign IAM user to notebook instance
D. No, for many reasons: AdministratorAccess policy is overly broad, not clear what associating a role to a group means (maybe a group has permissions to assume a role ...) and you cannot assign a group to a notebook
---
Selected Answer: A
Creating a single IAM role allows centralized management of permissions for all SageMaker notebook instances. When permissions need to be updated, the changes are applied to the role, and all notebook instances automatically inherit the updated permissions.
 Why IAM Roles?
 IAM roles are the recommended way to provide permissions to AWS services like SageMaker because they securely delegate permissions without requiring long-term credentials.

Why Not the Other Options?
B. IAM groups manage permissions for users, not for AWS services or resources like SageMaker notebook instances. Groups cannot be attached directly to notebook instances.
C. Using an IAM user with AdministratorAccess violates the principle of least privilege, granting unnecessary permissions. Additionally, IAM users are not intended to be attached to resources like notebook instances.
D. This option combines unnecessary complexity (group and role association) and grants excessive permissions (AdministratorAccess), which is not secure or efficient.
---
Selected Answer: A
Actually this is a best practice when working with notebooks in SageMaker. 
https://docs.aws.amazon.com/sagemaker/latest/dg/gs-setup-working-env.html

</details>

---

## Question 81: MLA-C01-ET-Q081
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use an ML model to predict the price of apartments in a specific location.
Which metric should the ML engineer use to evaluate the model's performance?

**Choices:**
- A) Accuracy
- B) Area Under the ROC Curve (AUC)
- C) F1 score
- D) Mean absolute error (MAE)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
The only one for regression is D. Other 3 are for classification.
---
Selected Answer: D
prediction the price of apartments is regression.
---
Selected Answer: D
This is a regression problem, thus MAE is the right answer. Accuracy, AUC-ROC and F1 are for classification.

</details>

---

## Question 82: MLA-C01-ET-Q082
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer has trained a neural network by using stochastic gradient descent (SGD). The neural network performs poorly on the test set. The values for training loss and validation loss remain high and show an oscillating pattern. The values decrease for a few epochs and then increase for a few epochs before repeating the same cycle.
What should the ML engineer do to improve the training process?

**Choices:**
- A) Introduce early stopping.
- B) Increase the size of the test set.
- C) Increase the learning rate.
- D) Decrease the learning rate.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
The oscillating pattern of training and validation loss indicates that the learning rate is too high. A high learning rate causes the model to overshoot the optimal point in the loss landscape, leading to oscillations instead of convergence. Reducing the learning rate allows the model to make smaller, more precise updates to the weights, improving convergence.

A. Early stopping prevents overfitting by halting training when validation performance stops improving. However, it does not address the root cause of oscillating loss.
B. The size of the test set does not affect the training dynamics or loss patterns.
C. Increasing the learning rate would worsen the oscillations and prevent the model from converging.
---
Selected Answer: D
A. No, early stopping is for preventing overfitting
B. No, increasing test will not help with oscillating loss
C. No, increasing learning rate will make things worsening
D. Oscillating loss in training is a sign that the training is not converging, this can happen when learning rate is too high. Reducing learning rate will help here
---
Selected Answer: D
Oscillating patterns in a train/validation loss shows it's not converging to a minima. Low learning rate will make it converge.

</details>

---

## Question 83: MLA-C01-ET-Q083
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to process thousands of existing CSV objects and new CSV objects that are uploaded. The CSV objects are stored in a central Amazon S3 bucket and have the same number of columns. One of the columns is a transaction date. The ML engineer must query the data based on the transaction date.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Use an Amazon Athena CREATE TABLE AS SELECT (CTAS) statement to create a table based on the transaction date from data in the central S3 bucket. Query the objects from the table.
- B) Create a new S3 bucket for processed data. Set up S3 replication from the central S3 bucket to the new S3 bucket. Use S3 Object Lambda to query the objects based on transaction date.
- C) Create a new S3 bucket for processed data. Use AWS Glue for Apache Spark to create a job to query the CSV objects based on transaction date. Configure the job to store the results in the new S3 bucket. Query the objects from the new S3 bucket.
- D) Create a new S3 bucket for processed data. Use Amazon Data Firehose to transfer the data from the central S3 bucket to the new S3 bucket. Configure Firehose to run an AWS Lambda function to query the data based on transaction date.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Yes, Athena is the right service to query data in S3.
B. No, maybe this might also work, but it is quite cumbersome
C. No, SparkSQL can be used to query files on data, but it is more work than Athena and creating a new S3 bucket is not needed
D. No, Data Firehose cannot consume from S3 directly
---
Selected Answer: A
Using Amazon Athena with a CREATE TABLE AS SELECT (CTAS) statement is the simplest and most efficient way to query the CSV objects based on the transaction date, while requiring minimal operational effort.
---
Selected Answer: A
Athena allows direct querying of data stored in Amazon S3 using SQL without requiring data movement or transformation. CTAS (CREATE TABLE AS SELECT): Creates a new table based on a filtered or transformed dataset, such as transaction dates, and stores the results in S3.
Why Not the Other Options?
B. S3 Object Lambda is designed for on-the-fly data transformation, not querying data efficiently. Adding replication increases complexity without addressing the querying requirement directly.
C. Glue is suited for complex ETL workflows, but it introduces significant operational overhead for a task that Athena can handle more easily.
D. Firehose is designed for streaming data, not processing large existing datasets.

</details>

---

## Question 84: MLA-C01-ET-Q084
**Domain 2:** ML Model Development  

**Question:**  
Case Study -
A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring.
The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3.
The company is experimenting with consecutive training jobs.
How can the company MINIMIZE infrastructure startup times for these jobs?

**Choices:**
- A) Use Managed Spot Training.
- B) Use SageMaker managed warm pools.
- C) Use SageMaker Training Compiler.
- D) Use the SageMaker distributed data parallelism (SMDDP) library.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
SageMaker managed warm pools allow instances to stay in a ready state between consecutive training jobs, which minimizes infrastructure startup times. This feature is ideal for scenarios with frequent or consecutive training jobs, as it avoids the time-consuming process of provisioning infrastructure for each job.
---
Selected Answer: B
SageMaker managed warm pools allow instances to stay in a ready state between consecutive training jobs, which minimizes infrastructure startup times. This feature is ideal for scenarios with frequent or consecutive training jobs, as it avoids the time-consuming process of provisioning infrastructure for each job.
---
Selected Answer: B
A. No, Managed Spot Training is used to reduce the compute cost for training
B. Yes, Warm Pool allow to retain and re-use provisioned infrastructure, also use a persistent cache to store data across training job and help reduce infrastructure startup time as well as cost - https://docs.aws.amazon.com/sagemaker/latest/dg/train-warm-pools.html
C. No, SageMaker Training Compiler is used to optimize your code for a specific target architecture
D. No, the SageMaker distributed data parallelism (SMDDP) library is used parallelize training by distributing data across multiple instances. This doesn't reduce infrastructure startu ptime

</details>

---

## Question 85: MLA-C01-ET-Q085
**Domain 2:** ML Model Development  

**Question:**  
A company has a large, unstructured dataset. The dataset includes many duplicate records across several key attributes.
Which solution on AWS will detect duplicates in the dataset with the LEAST code development?

**Choices:**
- A) Use Amazon Mechanical Turk jobs to detect duplicates.
- B) Use Amazon QuickSight ML Insights to build a custom deduplication model.
- C) Use Amazon SageMaker Data Wrangler to pre-process and detect duplicates.
- D) Use the AWS Glue FindMatches transform to detect duplicates.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (80%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Glue FindMatches is specifically designed to identify duplicate or matching records in datasets without requiring labeled training data. It uses machine learning to find fuzzy matches and allows customization to fine-tune the matching process, making it ideal for this scenario.
---
Selected Answer: D
https://aws.amazon.com/about-aws/whats-new/2021/11/aws-glue-findmatches-new-data-existing-dataset/
"allows you to identify duplicate or matching records in your dataset"
---
Selected Answer: C
I would argue you can should use Data Wrangler if you want to have the least code development. See https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-insights.html#data-wrangler-data-insights-samples
"You can remove duplicate samples from the dataset using the Drop duplicates transform under Manage rows."

</details>

---

## Question 86: MLA-C01-ET-Q086
**Domain 2:** ML Model Development  

**Question:**  
A company needs to run a batch data-processing job on Amazon EC2 instances. The job will run during the weekend and will take 90 minutes to finish running. The processing can handle interruptions. The company will run the job every weekend for the next 6 months.
Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) Spot Instances
- B) Reserved Instances
- C) On-Demand Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Cost effective + Interruptions + Short duration 90mins = Spot instance
---
Selected Answer: A
key: "The processing can handle interruptions"

</details>

---

## Question 87: MLA-C01-ET-Q087
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer has an Amazon Comprehend custom model in Account A in the us-east-1 Region. The ML engineer needs to copy the model to Account В in the same Region.
Which solution will meet this requirement with the LEAST development effort?

**Choices:**
- A) Use Amazon S3 to make a copy of the model. Transfer the copy to Account B.
- B) Create a resource-based IAM policy. Use the Amazon Comprehend ImportModel API operation to copy the model to Account B.
- C) Use AWS DataSync to replicate the model from Account A to Account B.
- D) Create an AWS Site-to-Site VPN connection between Account A and Account В to transfer the model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy-importing.html
---
Selected Answer: B
Amazon Comprehend - ImportModel API to facilitate the transfer of custom models between AWS accounts. STEPS:
1. Exporting the model from Account A.
2. Creating a resource-based IAM policy in Account A to grant access to Account B.
3. Using the ImportModel API in Account B to import the model.
---
Selected Answer: B
https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ImportModel.html
"The source model can be in your AWS account or another one."

</details>

---

## Question 88: MLA-C01-ET-Q088
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer is training a simple neural network model. The ML engineer tracks the performance of the model over time on a validation dataset. The model's performance improves substantially at first and then degrades after a specific number of epochs.
Which solutions will mitigate this problem? (Choose two.)

**Choices:**
- A) Enable early stopping on the model.
- B) Increase dropout in the layers.
- C) Increase the number of layers.
- D) Increase the number of neurons.
- E) Investigate and reduce the sources of model bias.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AB`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AB (100%). Contributor Answer: AB.

Community Rationale & Discussion:
Selected Answer: AB
The issue is overfitting. Soln:- 
A. Early stopping:- Stops training when validation performance declines
B. Increase dropout:- reduces overfitting by randomly disabling neurons
---
Selected Answer: AB
"improves substantially at first and then degrades after a specific number of epochs."
Clear sign to stop it early and to drop

</details>

---

## Question 89: MLA-C01-ET-Q089
**Domain 2:** ML Model Development  

**Question:**  
A company has a Retrieval Augmented Generation (RAG) application that uses a vector database to store embeddings of documents. The company must migrate the application to AWS and must implement a solution that provides semantic search of text files. The company has already migrated the text repository to an Amazon S3 bucket.
Which solution will meet these requirements?

**Choices:**
- A) Use an AWS Batch job to process the files and generate embeddings. Use AWS Glue to store the embeddings. Use SQL queries to perform the semantic searches.
- B) Use a custom Amazon SageMaker notebook to run a custom script to generate embeddings. Use SageMaker Feature Store to store the embeddings. Use SQL queries to perform the semantic searches.
- C) Use the Amazon Kendra S3 connector to ingest the documents from the S3 bucket into Amazon Kendra. Query Amazon Kendra to perform the semantic searches.
- D) Use an Amazon Textract asynchronous job to ingest the documents from the S3 bucket. Query Amazon Textract to perform the semantic searches.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Kendra for semantic search
---
Selected Answer: C
https://docs.aws.amazon.com/kendra/latest/dg/data-source-s3.html

</details>

---

## Question 90: MLA-C01-ET-Q090
**Domain 2:** ML Model Development  

**Question:**  
A company uses Amazon Athena to query a dataset in Amazon S3. The dataset has a target variable that the company wants to predict.
The company needs to use the dataset in a solution to determine if a model can predict the target variable.
Which solution will provide this information with the LEAST development effort?

**Choices:**
- A) Create a new model by using Amazon SageMaker Autopilot. Report the model's achieved performance.
- B) Implement custom scripts to perform data pre-processing, multiple linear regression, and performance evaluation. Run the scripts on Amazon EC2 instances.
- C) Configure Amazon Macie to analyze the dataset and to create a model. Report the model's achieved performance.
- D) Select a model from Amazon Bedrock. Tune the model with the data. Report the model's achieved performance.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Bedrock provides foundation models (LLMs) for tasks like text generation but is not used for structured data prediction.
---
Selected Answer: A
Best answere
---
Selected Answer: A
A is the most logical answer.

B. There is too much effort to set up those scripts and EC2.
C. Macie does not fit this use case.
D. Lots of effort to set up bedrock for this purpose.

</details>

---

## Question 91: MLA-C01-ET-Q091
**Domain 2:** ML Model Development  

**Question:**  
A company wants to predict the success of advertising campaigns by considering the color scheme of each advertisement. An ML engineer is preparing data for a neural network model. The dataset includes color information as categorical data.
Which technique for feature engineering should the ML engineer use for the model?

**Choices:**
- A) Apply label encoding to the color categories. Automatically assign each color a unique integer.
- B) Implement padding to ensure that all color feature vectors have the same length.
- C) Perform dimensionality reduction on the color categories.
- D) One-hot encode the color categories to transform the color scheme feature into a binary matrix.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
1. Label Encoding: Ordinal relationship
2. Padding: Sequence data
3. Dimensionality Reduction: High-dimensional data
4. One-Hot Encoding: Categorical data (Right)
---
Selected Answer: D
Label encoding is not ideal for categorical data in neural networks because the model might assume a numerical relationship (e.g., Blue is twice more important than Red), which is incorrect.
---
Selected Answer: D
Categorical data one hot always

</details>

---

## Question 92: MLA-C01-ET-Q092
**Domain 2:** ML Model Development  

**Question:**  
A company uses a hybrid cloud environment. A model that is deployed on premises uses data in Amazon 53 to provide customers with a live conversational engine.
The model is using sensitive data. An ML engineer needs to implement a solution to identify and remove the sensitive data.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Deploy the model on Amazon SageMaker. Create a set of AWS Lambda functions to identify and remove the sensitive data.
- B) Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster that uses AWS Fargate. Create an AWS Batch job to identify and remove the sensitive data.
- C) Use Amazon Macie to identify the sensitive data. Create a set of AWS Lambda functions to remove the sensitive data.
- D) Use Amazon Comprehend to identify the sensitive data. Launch Amazon EC2 instances to remove the sensitive data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Macie: Automate processe helps in handle the sensitive data
---
Selected Answer: C
Macie - Identify sensitive data
---
Selected Answer: C
This is the purpose of Macie. Comprehend will work also for PII but that EC2...

</details>

---

## Question 93: MLA-C01-ET-Q093
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to create data ingestion pipelines and ML model deployment pipelines on AWS. All the raw data is stored in Amazon S3 buckets.
Which solution will meet these requirements?

**Choices:**
- A) Use Amazon Data Firehose to create the data ingestion pipelines. Use Amazon SageMaker Studio Classic to create the model deployment pipelines.
- B) Use AWS Glue to create the data ingestion pipelines. Use Amazon SageMaker Studio Classic to create the model deployment pipelines.
- C) Use Amazon Redshift ML to create the data ingestion pipelines. Use Amazon SageMaker Studio Classic to create the model deployment pipelines.
- D) Use Amazon Athena to create the data ingestion pipelines. Use an Amazon SageMaker notebook to create the model deployment pipelines.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon Kinesis Data Firehose is for real-time streaming ingestion, the question implies batch processing (raw data is in S3).
---
Selected Answer: B
Data ingestion - Glue ; Model deployment pipeline - sagemaker studio classic
---
Selected Answer: B
This is the main use-case for Glue.

</details>

---

## Question 94: MLA-C01-ET-Q094
**Domain 2:** ML Model Development  

**Question:**  
A company that has hundreds of data scientists is using Amazon SageMaker to create ML models. The models are in model groups in the SageMaker Model Registry.
The data scientists are grouped into three categories: computer vision, natural language processing (NLP), and speech recognition. An ML engineer needs to implement a solution to organize the existing models into these groups to improve model discoverability at scale. The solution must not affect the integrity of the model artifacts and their existing groupings.
Which solution will meet these requirements?

**Choices:**
- A) Create a custom tag for each of the three categories. Add the tags to the model packages in the SageMaker Model Registry.
- B) Create a model group for each category. Move the existing models into these category model groups.
- C) Use SageMaker ML Lineage Tracking to automatically identify and tag which model groups should contain the models.
- D) Create a Model Registry collection for each of the three categories. Move the existing model groups into the collections.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Because according to the documentation - 
"Any operation you perform on your Collections does not affect the integrity of the individual Model Groups they contain—the underlying Model Group artifacts in Amazon S3 and Amazon ECR are not modified."
---
Selected Answer: D
Option-D Any operation you perform on your Collections does not affect the integrity of the individual Model Groups they contain—the underlying Model Group artifacts in Amazon S3 and Amazon ECR are not modified.
---
Selected Answer: D
https://docs.aws.amazon.com/sagemaker/latest/dg/modelcollections.html

</details>

---

## Question 95: MLA-C01-ET-Q095
**Domain 2:** ML Model Development  

**Question:**  
Case Study -
A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring.
The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3.
The company must implement a manual approval-based workflow to ensure that only approved models can be deployed to production endpoints.
Which solution will meet this requirement?

**Choices:**
- A) Use SageMaker Experiments to facilitate the approval process during model registration.
- B) Use SageMaker ML Lineage Tracking on the central model registry. Create tracking entities for the approval process.
- C) Use SageMaker Model Monitor to evaluate the performance of the model and to manage the approval.
- D) Use SageMaker Pipelines. When a model version is registered, use the AWS SDK to change the approval status to "Approved."

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
The SageMaker Model Registry within the pipeline provides functionality to manually or programmatically approve models for production deployment.
---
Selected Answer: D
SageMaker Pipelines is designed to orchestrate machine learning workflows, including manual approval steps for model registration. You can define a step in the pipeline where a manual approval process is required before the model's status is changed to "Approved" for deployment.
---
Selected Answer: D
This tricked my as option D is not clearly worded:
A. No, SageMaker Experiments allows to track and organize your experiment but not for approving models
B. No, SageMaker ML Lineage Tracking allows to track model lineage but do not allow to approve a model
C. No, SageMaker Model Monitor allows to monitor data quality, model quality, bias and feature attribution
D. Yes, After you create a model version, you typically evaluate its performance and then update the approval status of the model version. You can update the approval status of a model version by using the SDK, SageMaker Studio console or with a condition step in a SageMaker AI pipeline

</details>

---

## Question 96: MLA-C01-ET-Q096
**Domain 2:** ML Model Development  

**Question:**  
A company runs an Amazon SageMaker domain in a public subnet of a newly created VPC. The network is configured properly, and ML engineers can access the SageMaker domain.
Recently, the company discovered suspicious traffic to the domain from a specific IP address. The company needs to block traffic from the specific IP address.
Which update to the network configuration will meet this requirement?

**Choices:**
- A) Create a security group inbound rule to deny traffic from the specific IP address. Assign the security group to the domain.
- B) Create a network ACL inbound rule to deny traffic from the specific IP address. Assign the rule to the default network Ad for the subnet where the domain is located.
- C) Create a shadow variant for the domain. Configure SageMaker Inference Recommender to send traffic from the specific IP address to the shadow endpoint.
- D) Create a VPC route table to deny inbound traffic from the specific IP address. Assign the route table to the domain.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
There is no deny in SG's - only allows- So NACL is the clear answer here
---
Selected Answer: B
Protection at subnet level: Network ACL. Specific IP addresses can be denied at inbound connection level
---
Selected Answer: B
That's basic network topic.

</details>

---

## Question 97: MLA-C01-ET-Q097
**Domain 2:** ML Model Development  

**Question:**  
A company is gathering audio, video, and text data in various languages. The company needs to use a large language model (LLM) to summarize the gathered data that is in Spanish.
Which solution will meet these requirements in the LEAST amount of time?

**Choices:**
- A) Train and deploy a model in Amazon SageMaker to convert the data into English text. Train and deploy an LLM in SageMaker to summarize the text.
- B) Use Amazon Transcribe and Amazon Translate to convert the data into English text. Use Amazon Bedrock with the Jurassic model to summarize the text.
- C) Use Amazon Rekognition and Amazon Translate to convert the data into English text. Use Amazon Bedrock with the Anthropic Claude model to summarize the text.
- D) Use Amazon Comprehend and Amazon Translate to convert the data into English text. Use Amazon Bedrock with the Stable Diffusion model to summarize the text.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
For Spanish : https://docs.ai21.com/docs/jurassic-2-models
---
Selected Answer: B
LEAST amount of time -> A is out
C is out because Claude does NOT fit for summarization
D is out because that's for image generation

</details>

---

## Question 98: MLA-C01-ET-Q098
**Domain 2:** ML Model Development  

**Question:**  
A financial company receives a high volume of real-time market data streams from an external provider. The streams consist of thousands of JSON records every second.
The company needs to implement a scalable solution on AWS to identify anomalous data points.
Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Ingest real-time data into Amazon Kinesis data streams. Use the built-in RANDOM_CUT_FOREST function in Amazon Managed Service for Apache Flink to process the data streams and to detect data anomalies.
- B) Ingest real-time data into Amazon Kinesis data streams. Deploy an Amazon SageMaker endpoint for real-time outlier detection. Create an AWS Lambda function to detect anomalies. Use the data streams to invoke the Lambda function.
- C) Ingest real-time data into Apache Kafka on Amazon EC2 instances. Deploy an Amazon SageMaker endpoint for real-time outlier detection. Create an AWS Lambda function to detect anomalies. Use the data streams to invoke the Lambda function.
- D) Send real-time data to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Create an AWS Lambda function to consume the queue messages. Program the Lambda function to start an AWS Glue extract, transform, and load (ETL) job for batch processing and anomaly detection.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (86%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: B
Tricky question. RANDOM_CUT_FOREST is not available as a function in flink. it is a legacy function of Kinesis Data Analytics SQL. there is a RandomCutForestOperator, but is different that the mentioned function. ( https://aws.amazon.com/blogs/big-data/real-time-anomaly-detection-via-random-cut-forest-in-amazon-managed-service-for-apache-flink/)
---
Selected Answer: A
Option A 
High-volume real-time: Kinesis Data Streams
Scalable: Managed Apache Flink
Anomaly detection: RANDOM_CUT_FOREST
Low overhead: Fully managed services
---
Selected Answer: A
https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sqlrf-random-cut-forest.html
"Detects anomalies in your data stream."

</details>

---

## Question 99: MLA-C01-ET-Q099
**Domain 2:** ML Model Development  

**Question:**  
A company has a large collection of chat recordings from customer interactions after a product release. An ML engineer needs to create an ML model to analyze the chat data. The ML engineer needs to determine the success of the product by reviewing customer sentiments about the product.
Which action should the ML engineer take to complete the evaluation in the LEAST amount of time?

**Choices:**
- A) Use Amazon Rekognition to analyze sentiments of the chat conversations.
- B) Train a Naive Bayes classifier to analyze sentiments of the chat conversations.
- C) Use Amazon Comprehend to analyze sentiments of the chat conversations.
- D) Use random forests to classify sentiments of the chat conversations.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Prebuilt sentiment analysis + Fast setup + NLP --Comprehend
---
Selected Answer: C
https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html

</details>

---

## Question 100: MLA-C01-ET-Q100
**Domain 2:** ML Model Development  

**Question:**  
A company has a conversational AI assistant that sends requests through Amazon Bedrock to an Anthropic Claude large language model (LLM). Users report that when they ask similar questions multiple times, they sometimes receive different answers. An ML engineer needs to improve the responses to be more consistent and less random.
Which solution will meet these requirements?

**Choices:**
- A) Increase the temperature parameter and the top_k parameter.
- B) Increase the temperature parameter. Decrease the top_k parameter.
- C) Decrease the temperature parameter. Increase the top_k parameter.
- D) Decrease the temperature parameter and the top_k parameter.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Lower temperature: High probable output 
Lower Top k : Focus on likely output
---
Selected Answer: D
https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html

</details>

---

## Question 101: MLA-C01-ET-Q101
**Domain 2:** ML Model Development  

**Question:**  
A company is using ML to predict the presence of a specific weed in a farmer's field. The company is using the Amazon SageMaker linear learner built-in algorithm with a value of multiclass_dassifier for the predictorjype hyperparameter.
What should the company do to MINIMIZE false positives?

**Choices:**
- A) Set the value of the weight decay hyperparameter to zero.
- B) Increase the number of training epochs.
- C) Increase the value of the target_precision hyperparameter.
- D) Change the value of the predictorjype hyperparameter to regressor.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Weight decay = 0 → No regularization, doesn’t target false positives.
B. More epochs → Longer training, risks overfitting, no direct impact on false positives.
C. Higher precision → Prioritizes correct positives, reduces false positives.
D. Regressor → Predicts continuous values, unsuitable for classification.
---
Selected Answer: C
https://docs.aws.amazon.com/sagemaker/latest/dg/ll_hyperparameters.html

</details>

---

## Question 102: MLA-C01-ET-Q102
**Domain 2:** ML Model Development  

**Question:**  
A company has implemented a data ingestion pipeline for sales transactions from its ecommerce website. The company uses Amazon Data Firehose to ingest data into Amazon OpenSearch Service. The buffer interval of the Firehose stream is set for 60 seconds. An OpenSearch linear model generates real-time sales forecasts based on the data and presents the data in an OpenSearch dashboard.
The company needs to optimize the data ingestion pipeline to support sub-second latency for the real-time dashboard.
Which change to the architecture will meet these requirements?

**Choices:**
- A) Use zero buffering in the Firehose stream. Tune the batch size that is used in the PutRecordBatch operation.
- B) Replace the Firehose stream with an AWS DataSync task. Configure the task with enhanced fan-out consumers.
- C) Increase the buffer interval of the Firehose stream from 60 seconds to 120 seconds.
- D) Replace the Firehose stream with an Amazon Simple Queue Service (Amazon SQS) queue.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Use zero buffering to minimize latency by delivering data immediate.
Tune batch size to optimize throughput & ensures sub-second delivery for real-time dashboards.
---
Selected Answer: A
Although is quite new solution , A will do the trick:
https://aws.amazon.com/about-aws/whats-new/2023/12/amazon-kinesis-data-firehose-zero-buffering/

</details>

---

## Question 103: MLA-C01-ET-Q103
**Domain 2:** ML Model Development  

**Question:**  
A company has trained an ML model in Amazon SageMaker. The company needs to host the model to provide inferences in a production environment.
The model must be highly available and must respond with minimum latency. The size of each request will be between 1 KB and 3 MB. The model will receive unpredictable bursts of requests during the day. The inferences must adapt proportionally to the changes in demand.
How should the company deploy the model into production to meet these requirements?

**Choices:**
- A) Create a SageMaker real-time inference endpoint. Configure auto scaling. Configure the endpoint to present the existing model.
- B) Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster. Use ECS scheduled scaling that is based on the CPU of the ECS cluster.
- C) Install SageMaker Operator on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Deploy the model in Amazon EKS. Set horizontal pod auto scaling to scale replicas based on the memory metric.
- D) Use Spot Instances with a Spot Fleet behind an Application Load Balancer (ALB) for inferences. Use the ALBRequestCountPerTarget metric as the metric for auto scaling.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
SageMaker real-time endpoint: Purpose built for Auto scaling, low latency, handles bursts.
---
Selected Answer: A
https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/

</details>

---

## Question 104: MLA-C01-ET-Q104
**Domain 2:** ML Model Development  

**Question:**  
An ML engineer needs to use an Amazon EMR cluster to process large volumes of data in batches. Any data loss is unacceptable.
Which instance purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) Run the primary node, core nodes, and task nodes on On-Demand Instances.
- B) Run the primary node, core nodes, and task nodes on Spot Instances.
- C) Run the primary node on an On-Demand Instance. Run the core nodes and task nodes on Spot Instances.
- D) Run the primary node and core nodes on On-Demand Instances. Run the task nodes on Spot Instances.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Acceptable data loss: Spot can be used but
you can't change an instance purchasing option while a cluster is running. To change from On-Demand to Spot Instances or vice versa, for the primary and core nodes, you must terminate the cluster and launch a new one. For task nodes, you can launch a new task instance group or instance fleet, and remove the old one.
---
Selected Answer: D
https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html#emr-plan-spot-instances
"The task nodes process data but do not hold persistent data in HDFS. If they terminate because the Spot price has risen above your maximum Spot price, no data is lost"

</details>

---

## Question 105: MLA-C01-ET-Q105
**Domain 2:** ML Model Development  

**Question:**  
A company wants to improve the sustainability of its ML operations.
Which actions will reduce the energy usage and computational resources that are associated with the company's training jobs? (Choose two.)

**Choices:**
- A) Use Amazon SageMaker Debugger to stop training jobs when non-converging conditions are detected.
- B) Use Amazon SageMaker Ground Truth for data labeling.
- C) Deploy models by using AWS Lambda functions.
- D) Use AWS Trainium instances for training.
- E) Use PyTorch or TensorFlow with the distributed training option.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
Blog: https://aws.amazon.com/blogs/machine-learning/optimizing-mlops-for-sustainability/
Sustainability Goals: instances are up to 25% more energy efficient than comparable accelerated computing EC2 instances;
https://aws.amazon.com/ai/machine-learning/trainium/

SageMaker debugger helps to optimize resource consumption by detecting under-utilization of system resources, identifying training problems, and using built-in rules to monitor and stop training jobs as soon as bugs are detected.
---
Selected Answer: AD
I will go with A and D... they seems the most logic ones here.

</details>

---

## Question 106: MLA-C01-ET-Q106
**Domain 2:** ML Model Development  

**Question:**  
Case Study -
A company is building a web-based AI application by using Amazon SageMaker. The application will provide the following capabilities and features: ML experimentation, training, a central model registry, model deployment, and model monitoring.
The application must ensure secure and isolated use of training data during the ML lifecycle. The training data is stored in Amazon S3.
The company needs to run an on-demand workflow to monitor bias drift for models that are deployed to real-time endpoints from the application.
Which action will meet this requirement?

**Choices:**
- A) Configure the application to invoke an AWS Lambda function that runs a SageMaker Clarify job.
- B) Invoke an AWS Lambda function to pull the sagemaker-model-monitor-analyzer built-in SageMaker image.
- C) Use AWS Glue Data Quality to monitor bias.
- D) Use SageMaker notebooks to compare the bias.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Yes, Clarify allows to get bias - https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html
B. No, the built-in image sagemaker-model-monitor-analyzer provides a range of model monitoring capabilities (constraint suggestion, statistics generation, constraint validation against a baseline, and emitting Amazon CloudWatch metrics) but you need Clarify for bias
C. No, Glue Data Quality doesn't analyze bias
D. No, well from a Notebook you can execute pretty much everything including a Clarify Job, however notebooks are for experiments and models development not for enabling real-time application features
---
Selected Answer: A
SageMaker Clarify can be used to analyze bias drift in models. By integrating this with a Lambda function, the workflow can be triggered on-demand whenever the application requires bias monitoring.
---
Selected Answer: A
SageMaker Clarify can be used to analyze bias drift in models. By integrating this with a Lambda function, the workflow can be triggered on-demand whenever the application requires bias monitoring.

</details>

---
