# 🏆 AWS Certified AI Practitioner (AIF-C01) Official Full-Length Timed Mock Exam

> **Certification:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Exam Version Alignment:** Official v1.2 (October 2026 - incorporating Agentic AI, MCP, Nova, and Ordering/Matching question types)  
> **Exam Parameters:**
> - **Total Questions:** 65 (50 scored, 15 unscored experimental)
> - **Time Limit:** 90 Minutes (1.38 minutes per question)
> - **Passing Scaled Score:** 700 / 1000 (approx. 70% scaled benchmark)
> - **Question Formats:** Multiple Choice, Multiple Response, **Ordering**, and **Matching**
> **Domain Distribution:**
> - Domain 1: Fundamentals of AI and ML (20% - 13 Questions)
> - Domain 2: Fundamentals of Generative AI (24% - 16 Questions)
> - Domain 3: Applications of Foundation Models (28% - 18 Questions)
> - Domain 4: Guidelines for Responsible AI (14% - 9 Questions)
> - Domain 5: Security, Compliance, and Governance (14% - 9 Questions)

---

## 📝 Practice Exam Questions (1 to 65)

### Question 1 (Domain 1)
A retail company wants to predict whether a website visitor will complete a purchase based on browsing duration, device type, and referral channel. Which type of machine learning task is this?
- [ ] A) Regression
- [ ] B) Binary Classification
- [ ] C) Dimensionality Reduction
- [ ] D) Unsupervised Clustering

### Question 2 (Domain 2)
An AI engineer requires a text-only foundation model that delivers the lowest possible Time to First Token (TTFT) and lowest cost per 1,000 tokens for routing user queries. Which model within the Amazon Nova family should be chosen?
- [ ] A) Amazon Nova Premier
- [ ] B) Amazon Nova Pro
- [ ] C) Amazon Nova Lite
- [ ] D) Amazon Nova Micro

### Question 3 (Domain 3)
A hospital wants to build an internal generative assistant that queries clinical practice guidelines stored in Amazon S3. The assistant must cite exact source document passages and page numbers. Which architecture meets these requirements?
- [ ] A) Full fine-tuning of an open-source model using Amazon SageMaker Training Jobs
- [ ] B) Amazon Bedrock Knowledge Bases connected to S3 and OpenSearch Serverless
- [ ] C) Continued pre-training using AWS Trainium instances
- [ ] D) Storing PDF text in DynamoDB and using table scan filters

### Question 4 (Domain 4)
An insurance company chatbot must be strictly prevented from offering investment advice or suggesting stock picks. Which Amazon Bedrock Guardrail policy should be configured?
- [ ] A) Contextual Grounding Policy
- [ ] B) Sensitive Information Policy
- [ ] C) Denied Topics Policy
- [ ] D) Word Filter Blocklist

### Question 5 (Domain 5)
Under the AWS Generative AI Security Scoping Matrix, what is the customer's responsibility when consuming on-demand foundation models in Amazon Bedrock (Scope 2)?
- [ ] A) Managing physical GPU hardware and hypervisor patches
- [ ] B) Configuring IAM least-privilege policies, prompt guardrails, and classifying input data
- [ ] C) Pre-training base transformer models from raw web data
- [ ] D) Designing custom silicon ASIC accelerators

### Question 6 (Domain 1)
Which tool in Amazon SageMaker allows business analysts to import tabular datasets, automatically evaluate feature correlations, and generate predictive ML models using a visual point-and-click interface?
- [ ] A) SageMaker Studio Code Editor
- [ ] B) SageMaker Canvas
- [ ] C) SageMaker HyperPod
- [ ] D) SageMaker Edge Manager

### Question 7 (Domain 2)
In the Transformer architecture, what is the mathematical function of the Positional Encoding vector added to token embeddings?
- [ ] A) To compress embeddings from 1536 dimensions to 256 dimensions
- [ ] B) To inject word sequence order information since self-attention processes all tokens in parallel
- [ ] C) To encrypt prompt payloads before sending to Bedrock
- [ ] D) To prevent overfitting on imbalanced training data

### Question 8 (Domain 3 - ORDERING QUESTION)
**An architect is building an automated Retrieval-Augmented Generation (RAG) ingestion pipeline using Amazon Bedrock Knowledge Bases. Place the following five procedural steps in the correct chronological execution sequence:**
1. Split documents into smaller text chunks using a chunking strategy (e.g., fixed or hierarchical).
2. Upload source corporate PDF/DOCX policy documents to an encrypted Amazon S3 bucket.
3. Ingest the resulting dense vector embeddings into an Amazon OpenSearch Serverless vector collection index.
4. Pass text chunks through Amazon Titan Text Embeddings v2 to generate high-dimensional numerical vectors.
5. Trigger the Knowledge Base Data Source Sync operation via the Bedrock console or API.

*Select the correct sequence order:*
- [ ] A) 2 $\rightarrow$ 5 $\rightarrow$ 1 $\rightarrow$ 4 $\rightarrow$ 3
- [ ] B) 1 $\rightarrow$ 2 $\rightarrow$ 4 $\rightarrow$ 3 $\rightarrow$ 5
- [ ] C) 5 $\rightarrow$ 2 $\rightarrow$ 1 $\rightarrow$ 4 $\rightarrow$ 3
- [ ] D) 2 $\rightarrow$ 1 $\rightarrow$ 5 $\rightarrow$ 4 $\rightarrow$ 3

### Question 9 (Domain 4)
Before deploying a credit decisioning model, a bank uses SageMaker Clarify to evaluate the training dataset. The report displays a Class Imbalance (CI) score of $-0.45$ for applicant age facet $<25$. What does this metric indicate?
- [ ] A) Applicants under 25 are under-represented in the training dataset.
- [ ] B) Applicants under 25 received 45% more loan approvals.
- [ ] C) The model has an error rate of 45%.
- [ ] D) The dataset contains corrupted rows.

### Question 10 (Domain 5)
A financial firm requires that all inference requests between its private VPC and Amazon Bedrock never traverse the public internet. Which networking service feature fulfills this requirement?
- [ ] A) AWS Direct Connect with public VIF
- [ ] B) AWS PrivateLink (VPC Interface Endpoint for `bedrock-runtime`)
- [ ] C) NAT Gateway with an Elastic IP
- [ ] D) Internet Gateway (IGW) with egress-only route table

### Question 11 (Domain 1)
A fraud detection model has a Confusion Matrix of: True Positives = 90, False Positives = 10, False Negatives = 30, True Negatives = 870. What is the Recall of this model?
- [ ] A) 90% ($90 / 100$)
- [ ] B) 75% ($90 / 120$)
- [ ] C) 87% ($870 / 1000$)
- [ ] D) 96.6% ($870 / 900$)

### Question 12 (Domain 2)
What happens to a foundation model's output generation when the Temperature parameter is lowered to 0.0?
- [ ] A) The output becomes maximum creativity and diverse.
- [ ] B) The output becomes deterministic, selecting the single highest-probability token at each step.
- [ ] C) The model stops responding and throws an HTTP 500 error.
- [ ] D) The token context window increases twofold.

### Question 13 (Domain 3)
A developer uses 3 clear input-output demonstrations inside a prompt to guide an LLM to generate customer support tickets in a specific XML schema. Which prompt engineering technique is being utilized?
- [ ] A) Zero-Shot Prompting
- [ ] B) Few-Shot Prompting (In-Context Learning)
- [ ] C) Chain-of-Thought Prompting
- [ ] D) Continued Pre-training

### Question 14 (Domain 4)
Which explainability metric evaluated by SageMaker Clarify quantifies the exact positive or negative contribution of each individual feature toward a single customer's loan rejection?
- [ ] A) Global Feature Importance
- [ ] B) Local SHAP (Shapley Additive exPlanations) values
- [ ] C) ROUGE-2 Score
- [ ] D) Disparate Impact Ratio

### Question 15 (Domain 5)
A compliance auditor must verify whether any S3 buckets designated for a Bedrock Knowledge Base contain unmasked credit card numbers or passport IDs. Which AWS service is purpose-built to automatically discover sensitive data in S3?
- [ ] A) AWS Shield Advanced
- [ ] B) Amazon Macie
- [ ] C) Amazon Inspector
- [ ] D) AWS WAF

### Question 16 (Domain 1)
An e-commerce company wants to extract text, tables, and invoice amounts from scanned receipts uploaded by customers. Which AWS managed service provides this document intelligence capability without custom ML code?
- [ ] A) Amazon Rekognition
- [ ] B) Amazon Textract
- [ ] C) Amazon Comprehend
- [ ] D) Amazon Translate

### Question 17 (Domain 2)
What is the primary architectural purpose of the Model Context Protocol (MCP) in agentic AI systems?
- [ ] A) An encryption algorithm for securing S3 buckets
- [ ] B) A universal open protocol standardizing how AI models discover, inspect, and execute tools and read resources over JSON-RPC
- [ ] C) A GPU driver for compiling CUDA kernels
- [ ] D) A data compression utility for reducing PDF sizes

### Question 18 (Domain 3)
An application uses repetitive system prompts of 15,000 tokens across thousands of daily user sessions. Which Amazon Bedrock feature should be enabled to cut token processing costs by up to 50% and reduce latency?
- [ ] A) Cross-Region Replication
- [ ] B) Prompt Caching
- [ ] C) Model Distillation
- [ ] D) Provisioned Throughput without commitment

### Question 19 (Domain 4)
An enterprise chatbot must redact all customer email addresses, phone numbers, and Social Security numbers by replacing them with generic tags like `[EMAIL]` in chat logs. Which feature natively accomplishes this?
- [ ] A) Amazon Bedrock Guardrails Sensitive Information Filters (Anonymize)
- [ ] B) SageMaker Canvas Standard Build
- [ ] C) Amazon CloudWatch Metric Filters
- [ ] D) AWS IAM Permission Boundaries

### Question 20 (Domain 5)
Does AWS use customer prompts or generated outputs submitted to Amazon Bedrock to train or improve base foundation models?
- [ ] A) Yes, all prompts are retained for 1 year.
- [ ] B) No, AWS never uses customer inputs or completions to train base models and never shares them with third-party model providers.
- [ ] C) Yes, but only for Amazon Titan models.
- [ ] D) Yes, unless an enterprise support plan is purchased.

### Question 21 (Domain 1)
A data scientist evaluates two predictive models. Model A has high training error and high test error. Model B has very low training error and very high test error. What conditions do Model A and Model B exhibit?
- [ ] A) Model A: Overfitting; Model B: Underfitting
- [ ] B) Model A: High Bias (Underfitting); Model B: High Variance (Overfitting)
- [ ] C) Model A: Perfect Generalization; Model B: Data Poisoning
- [ ] D) Both models exhibit low variance.

### Question 22 (Domain 2)
Which Amazon Nova model is designed for high-throughput, cost-effective multimodal processing of text, images, and video frames?
- [ ] A) Amazon Nova Micro
- [ ] B) Amazon Nova Lite
- [ ] C) Amazon Nova Premier
- [ ] D) Amazon Titan Text Embeddings v2

### Question 23 (Domain 3)
Which fine-tuning methodology modifies less than 1% of total model parameters by freezing pre-trained weights and training low-rank adapter matrices?
- [ ] A) Full Parameter Fine-Tuning
- [ ] B) Parameter-Efficient Fine-Tuning (PEFT) using LoRA
- [ ] C) Continued Pre-training
- [ ] D) Unsupervised K-Means

### Question 24 (Domain 4)
What is an Amazon SageMaker Model Card?
- [ ] A) A hardware PCIe accelerator for edge devices
- [ ] B) A standardized digital governance document recording intended use, out-of-scope uses, bias evaluation metrics, and risk ratings for compliance auditing
- [ ] C) A visual credit card payment tool for AWS billing
- [ ] D) A deployment container for Docker images

### Question 25 (Domain 5)
Which AWS service logs data-plane API calls, such as `InvokeModel` and `RetrieveAndGenerate`, capturing the caller identity, timestamp, and source IP?
- [ ] A) AWS CloudTrail Data Events
- [ ] B) AWS CloudTrail Management Events only
- [ ] C) Amazon VPC Flow Logs
- [ ] D) AWS Artifact

### Question 26 (Domain 1 - MATCHING QUESTION)
**Match each AWS AI Service to its primary technical capability:**
- **Service 1:** Amazon Polly
- **Service 2:** Amazon Transcribe
- **Service 3:** Amazon Comprehend
- **Service 4:** Amazon Rekognition

*Capabilities:*
- *Capability W:* Facial analysis, object detection, and visual content moderation in images and video.
- *Capability X:* Natural Language Processing for sentiment analysis, entity extraction, and language detection.
- *Capability Y:* Automatic Speech Recognition (ASR) converting spoken audio into text.
- *Capability Z:* Text-to-Speech (TTS) converting written text into lifelike spoken audio.

*Select the correct matching combination:*
- [ ] A) 1-Z, 2-Y, 3-X, 4-W
- [ ] B) 1-Y, 2-Z, 3-W, 4-X
- [ ] C) 1-X, 2-W, 3-Z, 4-Y
- [ ] D) 1-Z, 2-X, 3-Y, 4-W

### Question 27 (Domain 2)
What is Top-P (Nucleus Sampling) in foundation model configuration?
- [ ] A) The maximum number of output tokens generated
- [ ] B) A parameter that restricts token selection to the smallest cumulative probability pool exceeding threshold $P$
- [ ] C) A parameter that sets the number of GPU cores used
- [ ] D) The total number of layers in the Transformer

### Question 28 (Domain 3)
Which evaluation metric measures $n$-gram recall and is standard for evaluating abstractive text summarization against reference human summaries?
- [ ] A) BLEU
- [ ] B) ROUGE
- [ ] C) Perplexity
- [ ] D) Root Mean Squared Error (RMSE)

### Question 29 (Domain 4)
In SageMaker Clarify post-training evaluation, what does a Disparate Impact (DI) score of $0.65$ indicate for a loan underwriting model?
- [ ] A) The model is 65% accurate.
- [ ] B) The disfavored demographic group receives favorable loan approvals at only 65% of the rate of the favored group, indicating adverse disparate impact.
- [ ] C) The model requires 65% less training time.
- [ ] D) The model complies with the 80% legal rule.

### Question 30 (Domain 5)
Where are the weights of fine-tuned custom models created via Amazon Bedrock stored?
- [ ] A) In public Amazon S3 buckets without encryption
- [ ] B) In an isolated private partition dedicated to the customer's account and encrypted at rest using customer-managed AWS KMS keys
- [ ] C) On partner servers outside AWS
- [ ] D) On local browser storage

### Question 31 (Domain 1)
A data scientist needs to convert a nominal categorical column (`Region`: North, South, East, West) into numerical format for an algorithm that cannot process text strings. Which technique is standard?
- [ ] A) Min-Max Normalization
- [ ] B) One-Hot Encoding
- [ ] C) Principal Component Analysis
- [ ] D) Sentiment Analysis

### Question 32 (Domain 2)
What is the primary difference between discriminative AI and generative AI?
- [ ] A) Discriminative AI generates text; generative AI classifies images.
- [ ] B) Discriminative AI models $P(Y|X)$ to classify inputs or predict values; generative AI models data distributions $P(X)$ to create new data instances.
- [ ] C) Generative AI runs only on CPUs; discriminative AI runs on GPUs.
- [ ] D) Generative AI cannot use embeddings.

### Question 33 (Domain 3)
What is the primary advantage of Low-Rank Adaptation (LoRA) over Full Fine-Tuning when adapting a foundation model to proprietary enterprise formatting?
- [ ] A) LoRA alters 100% of the model weights, ensuring highest accuracy.
- [ ] B) LoRA freezes base weights and trains small adapter matrices, drastically reducing GPU training memory and preventing catastrophic forgetting.
- [ ] C) LoRA eliminates the need for any labeled training data.
- [ ] D) LoRA automatically translates prompts to French.

### Question 34 (Domain 4)
Which Amazon Bedrock Guardrail policy specifically checks whether a response hallucinated information not found in the reference documents retrieved during RAG?
- [ ] A) Word Filters
- [ ] B) Contextual Grounding Policy
- [ ] C) Content Policy
- [ ] D) Denied Topics

### Question 35 (Domain 5)
Under the AWS Generative AI Security Scoping Matrix, which deployment scope involves pre-training a foundation model from scratch using billions of tokens on AWS Trainium clusters, requiring the customer to own 100% of data governance and ethics?
- [ ] A) Scope 1
- [ ] B) Scope 2
- [ ] C) Scope 3
- [ ] D) Scope 4

### Question 36 (Domain 1)
Which metric is the harmonic mean of Precision and Recall, making it ideal for evaluating models trained on imbalanced datasets?
- [ ] A) Accuracy
- [ ] B) $F_1$-Score
- [ ] C) Mean Squared Error
- [ ] D) $R^2$

### Question 37 (Domain 2)
Which foundation model in the Amazon Nova family is designed for complex reasoning, multi-step math, high-capability coding, and autonomous agent orchestration?
- [ ] A) Amazon Nova Micro
- [ ] B) Amazon Nova Lite
- [ ] C) Amazon Nova Pro
- [ ] D) Amazon Titan Text Lite

### Question 38 (Domain 3)
What component in an Amazon Bedrock Agent connects the foundation model's reasoning engine to external backend systems via AWS Lambda and OpenAPI 3.0 schemas?
- [ ] A) Knowledge Base
- [ ] B) Action Group
- [ ] C) Guardrail
- [ ] D) Prompt Cache

### Question 39 (Domain 4)
What legal protection does AWS provide to enterprise customers using Amazon Titan foundation models against third-party copyright claims?
- [ ] A) Free tier credit rebates
- [ ] B) Intellectual Property (IP) Indemnification
- [ ] C) Automatic patent registration
- [ ] D) Exemption from GDPR audits

### Question 40 (Domain 5)
How is model access configured when an AWS account is initially created for Amazon Bedrock?
- [ ] A) All models are enabled automatically.
- [ ] B) Foundation models are disabled by default; an administrator must explicitly request and gain access per region.
- [ ] C) Access is granted only to root credentials.
- [ ] D) Third-party models require purchasing physical GPU servers.

### Question 41 (Domain 1)
Which AWS service translates natural language text between dozens of languages in real-time or batch mode?
- [ ] A) Amazon Transcribe
- [ ] B) Amazon Polly
- [ ] C) Amazon Translate
- [ ] D) Amazon Kendra

### Question 42 (Domain 2)
In Large Language Models, what is the term for a single fundamental unit of text processing (where 1,000 units roughly equal 750 English words)?
- [ ] A) Vector
- [ ] B) Token
- [ ] C) Attention Head
- [ ] D) Neuron

### Question 43 (Domain 3)
Which prompt engineering technique explicitly instructs a foundation model to "think step-by-step" before providing a final answer to reduce reasoning and arithmetic errors?
- [ ] A) Few-Shot Prompting
- [ ] B) Chain-of-Thought (CoT) Prompting
- [ ] C) Zero-Shot Prompting
- [ ] D) Directional Stimulus Prompting

### Question 44 (Domain 4)
In SageMaker Clarify pre-training evaluation, what does a Difference in Positive Proportions in Labels (DPL) of $+0.30$ favoring Group A over Group B indicate?
- [ ] A) Historical training labels awarded positive outcomes to Group A at a 30% higher rate than Group B.
- [ ] B) Group A has 30% more data rows than Group B.
- [ ] C) The model is 30% inaccurate.
- [ ] D) Group B is underfitting.

### Question 45 (Domain 5)
Which AWS service provides on-demand access to AWS compliance reports, such as SOC 1/2/3, ISO certifications, and PCI-DSS compliance packages?
- [ ] A) AWS Trusted Advisor
- [ ] B) AWS Artifact
- [ ] C) AWS Config
- [ ] D) AWS CloudTrail

### Question 46 (Domain 1)
A real estate portal wants to predict home sale prices in dollars based on square footage, bedrooms, and location. Which type of ML algorithm should be used?
- [ ] A) Binary Classification
- [ ] B) Regression
- [ ] C) K-Means Clustering
- [ ] D) Named Entity Recognition

### Question 47 (Domain 2)
Which generative AI architecture uses a forward process that adds Gaussian noise to training data and a reverse process that removes noise to synthesize realistic images?
- [ ] A) Transformer Decoder
- [ ] B) Diffusion Model (e.g., Amazon Titan Image Generator)
- [ ] C) Recurrent Neural Network
- [ ] D) Logistic Regression

### Question 48 (Domain 3)
When evaluating machine translation models, which metric calculates $n$-gram precision against human reference translations?
- [ ] A) ROUGE
- [ ] B) BLEU
- [ ] C) Perplexity
- [ ] D) Mean Absolute Error

### Question 49 (Domain 4)
In the Amazon SageMaker Model Registry, what status must a newly registered model be transitioned to before automated CI/CD deployment pipelines release it to production?
- [ ] A) `PendingManualApproval`
- [ ] B) `Approved`
- [ ] C) `Archived`
- [ ] D) `Draft`

### Question 50 (Domain 5)
Which IAM permission allows an application to invoke an Amazon Bedrock model for runtime text generation?
- [ ] A) `bedrock:CreateModelCustomizationJob`
- [ ] B) `bedrock:InvokeModel`
- [ ] C) `s3:GetObject`
- [ ] D) `ec2:RunInstances`

### Question 51 (Domain 1 - MULTIPLE RESPONSE)
A machine learning engineer wants to prevent a Decision Tree model from overfitting on a small training dataset. Which TWO techniques should be applied? (Select TWO.)
- [ ] A) Pruning the decision tree depth
- [ ] B) Setting a minimum number of samples required to split an internal node
- [ ] C) Increasing tree depth to infinity
- [ ] D) Removing all regularization penalties
- [ ] E) Deleting the test dataset
*Select TWO.*

### Question 52 (Domain 2)
In modern agentic AI systems, what sequence of actions defines the autonomous reasoning loop?
- [ ] A) Thought $\rightarrow$ Action $\rightarrow$ Observation $\rightarrow$ Reflection
- [ ] B) Predict $\rightarrow$ Delete $\rightarrow$ Train $\rightarrow$ Test
- [ ] C) Encode $\rightarrow$ Decode $\rightarrow$ Encrypt $\rightarrow$ Decrypt
- [ ] D) Compile $\rightarrow$ Execute $\rightarrow$ Commit $\rightarrow$ Push

### Question 53 (Domain 3)
A business application requires dedicated model throughput with zero risk of `ThrottlingException` errors during critical holiday sales. Which Bedrock purchasing option should be selected?
- [ ] A) On-Demand Token Pricing
- [ ] B) Provisioned Throughput (Model Units)
- [ ] C) Spot Fleet Instances
- [ ] D) Free Tier Allocation

### Question 54 (Domain 4)
What technology does Amazon Titan Image Generator use to assist in identifying AI-generated content and mitigating the spread of deepfakes?
- [ ] A) A visible red border on every image
- [ ] B) An invisible, tamper-resistant digital watermark embedded into the generated image pixels
- [ ] C) Mandatory email registration
- [ ] D) Restricting image sizes to 128x128 pixels

### Question 55 (Domain 5)
What cryptographic control allows an enterprise to maintain full ownership of its encryption keys and immediately revoke access to Bedrock custom model weights by disabling the key?
- [ ] A) AWS Owned Keys
- [ ] B) AWS Managed Keys
- [ ] C) AWS KMS Customer Managed Keys (CMKs)
- [ ] D) S3 Default Encryption

### Question 56 (Domain 1)
Which AWS service provides an enterprise intelligent search engine powered by machine learning, allowing users to search across SharePoint, Confluence, and S3 using natural language questions?
- [ ] A) Amazon OpenSearch Service
- [ ] B) Amazon Kendra
- [ ] C) Amazon CloudSearch
- [ ] D) Amazon Athena

### Question 57 (Domain 2)
What is the role of the Causal Mask in decoder-only Transformers (such as Amazon Nova or Claude)?
- [ ] A) To prevent the model from looking at future tokens during autoregressive text generation
- [ ] B) To filter out toxic profanity words
- [ ] C) To compress model weights into 8-bit integers
- [ ] D) To encrypt the prompt in memory

### Question 58 (Domain 3)
What is the "LLM-as-a-Judge" methodology?
- [ ] A) Using a human court to litigate model training data copyright
- [ ] B) Using a high-capability frontier model to automatically evaluate and score the outputs of smaller models against a defined rubric
- [ ] C) An automated compiler optimization in PyTorch
- [ ] D) A regulatory filing required by the SEC

### Question 59 (Domain 4)
Which pillar of Responsible AI focuses on verifying that a model's statements are factually accurate and truthful, mitigating fabricated hallucinations?
- [ ] A) Fairness
- [ ] B) Veracity
- [ ] C) Inclusivity
- [ ] D) Scalability

### Question 60 (Domain 5)
Under the Generative AI Security Scoping Matrix, what scope represents an organization using third-party consumer SaaS chatbots where the enterprise has zero control over underlying data and infrastructure?
- [ ] A) Scope 1
- [ ] B) Scope 2
- [ ] C) Scope 3
- [ ] D) Scope 4

### Question 61 (Domain 1)
What is the primary function of Amazon SageMaker JumpStart?
- [ ] A) A visual drag-and-drop tool for business analysts
- [ ] B) A machine learning hub providing pre-trained foundation models, open-source models, and end-to-end solutions that can be deployed with a single click
- [ ] C) A serverless billing optimization dashboard
- [ ] D) An automated code compiler for Python 2.7

### Question 62 (Domain 2)
When configuring foundation model inference, what does a Stop Sequence do?
- [ ] A) Terminates the EC2 GPU instance
- [ ] B) Immediately halts token generation when a specified character string is emitted
- [ ] C) Deletes the Amazon S3 document bucket
- [ ] D) Prevents prompt injection attacks

### Question 63 (Domain 3)
What is "Catastrophic Forgetting" in foundation model fine-tuning?
- [ ] A) When an S3 bucket is accidentally emptied
- [ ] B) When a model loses its generalized reasoning abilities after aggressive fine-tuning on a narrow task
- [ ] C) When the GPU runs out of VRAM
- [ ] D) When the context window reaches 200,000 tokens

### Question 64 (Domain 4)
Which SageMaker capability computes Shapley values to provide both global feature importance rankings and local individual prediction explanations?
- [ ] A) SageMaker Canvas
- [ ] B) SageMaker Clarify
- [ ] C) SageMaker Edge Manager
- [ ] D) SageMaker Model Cards

### Question 65 (Domain 5)
Which IAM policy element ensures that an application can only invoke Amazon Nova Pro in the Stockholm region (`eu-north-1`)?
- [ ] A) Setting `Action: "bedrock:*"` on `Resource: "*"`
- [ ] B) Restricting the `Resource` ARN to `arn:aws:bedrock:eu-north-1::foundation-model/amazon.nova-pro-v1:0` and using an `aws:RequestedRegion` condition
- [ ] C) Deleting the AWS KMS key
- [ ] D) Disabling CloudTrail logging

---

## 🔑 Master Answer Key & Diagnostic Scoring Table

| Q# | Answer | Domain | Key Concept Tested | Detailed Examination Rationale |
|:---:|:---:|:---:|:--- |:--- |
| **1** | **B** | 1 | Binary Classification | Predicting a two-class outcome (purchase vs no purchase) is binary classification. |
| **2** | **D** | 2 | Amazon Nova Micro | Nova Micro is text-only, lowest latency (fastest TTFT), and lowest cost in the Nova family. |
| **3** | **B** | 3 | Bedrock Knowledge Bases (RAG) | Knowledge Bases automates RAG, vector search, and appends citations without retraining. |
| **4** | **C** | 4 | Denied Topics | Denied Topics blocks specified conversational domains using natural language instructions. |
| **5** | **B** | 5 | Security Scope 2 | Customers own IAM, prompt guardrails, and data classification in managed Bedrock services. |
| **6** | **B** | 1 | SageMaker Canvas | Canvas is AWS's visual, no-code AutoML tool for business analysts. |
| **7** | **B** | 2 | Positional Encodings | Self-attention processes tokens in parallel; positional encodings restore word order. |
| **8** | **A** | 3 | RAG Execution Sequence | 2 (S3 upload) $\rightarrow$ 5 (Trigger Sync) $\rightarrow$ 1 (Chunk text) $\rightarrow$ 4 (Generate Embeddings) $\rightarrow$ 3 (Store in OpenSearch). |
| **9** | **A** | 4 | Class Imbalance (CI) | Negative CI indicates the demographic facet is under-represented relative to other groups. |
| **10** | **B** | 5 | AWS PrivateLink | VPC Interface Endpoints keep inference traffic strictly within AWS's private network fabric. |
| **11** | **B** | 1 | Recall Calculation | $\text{Recall} = TP / (TP + FN) = 90 / (90 + 30) = 90 / 120 = 75\%$. |
| **12** | **B** | 2 | Temperature 0.0 | Temperature 0 forces greedy decoding, selecting the highest-probability token deterministically. |
| **13** | **B** | 3 | Few-Shot Prompting | Providing 2–5 structured demonstrations in the prompt is Few-Shot / In-Context Learning. |
| **14** | **B** | 4 | Local SHAP Values | Local SHAP values quantify the positive or negative impact of each feature on a single decision. |
| **15** | **B** | 5 | Amazon Macie | Macie scans Amazon S3 buckets to discover and alert on unmasked sensitive PII. |
| **16** | **B** | 1 | Amazon Textract | Textract extracts forms, tables, and text from receipts and PDFs without custom code. |
| **17** | **B** | 2 | Model Context Protocol | MCP is an open standard enabling models to discover and execute tools over JSON-RPC. |
| **18** | **B** | 3 | Prompt Caching | Caching large static preambles in GPU memory reduces latency by 80% and costs by 50%. |
| **19** | **A** | 4 | Sensitive Info Filters | Bedrock Guardrails can mask/anonymize PII entities across all foundation models. |
| **20** | **B** | 5 | Bedrock Zero-Training | AWS never uses customer inputs or completions to train base foundation models. |
| **21** | **B** | 1 | Bias vs Variance | Model A: High Bias (Underfitting); Model B: High Variance (Overfitting). |
| **22** | **B** | 2 | Amazon Nova Lite | Nova Lite is a cost-effective, high-speed multimodal model for text, images, and video. |
| **23** | **B** | 3 | PEFT / LoRA | LoRA trains low-rank adapter matrices ($<1\%$ of weights), saving compute and preserving weights. |
| **24** | **B** | 4 | SageMaker Model Cards | Model Cards provide an auditable record of model intended use, bias scores, and risk ratings. |
| **25** | **A** | 5 | CloudTrail Data Events | CloudTrail Data Events log runtime operations like `InvokeModel` and `RetrieveAndGenerate`. |
| **26** | **A** | 1 | AI Services Matching | 1-Z (Polly=TTS), 2-Y (Transcribe=ASR), 3-X (Comprehend=NLP), 4-W (Rekognition=Vision). |
| **27** | **B** | 2 | Top-P Sampling | Top-P restricts candidate tokens to the smallest cumulative probability pool exceeding $P$. |
| **28** | **B** | 3 | ROUGE Metric | ROUGE measures $n$-gram recall and is standard for evaluating text summarization. |
| **29** | **B** | 4 | Disparate Impact (DI) | Scores below 0.80 indicate that the disfavored group receives favorable outcomes at a lower rate. |
| **30** | **B** | 5 | Custom Model Security | Fine-tuned weights reside in private customer tenant partitions encrypted with customer KMS keys. |
| **31** | **B** | 1 | One-Hot Encoding | One-Hot Encoding converts nominal categories into binary indicator columns. |
| **32** | **B** | 2 | Generative vs Discriminative | Discriminative models $P(Y|X)$; Generative models $P(X)$ to generate novel instances. |
| **33** | **B** | 3 | LoRA Benefits | LoRA avoids catastrophic forgetting and slashes training compute by training lightweight adapters. |
| **34** | **B** | 4 | Contextual Grounding | Grounding checks verify that generated claims adhere factually to retrieved RAG snippets. |
| **35** | **D** | 5 | Security Scope 4 | Scope 4 is custom pre-training from scratch; customer owns 100% of data and architecture. |
| **36** | **B** | 1 | $F_1$-Score | The $F_1$-score is the harmonic mean of Precision and Recall: $2(P \times R) / (P + R)$. |
| **37** | **C** | 2 | Amazon Nova Pro | Nova Pro is Amazon's frontier multimodal model for complex math, coding, and agent planning. |
| **38** | **B** | 3 | Action Groups | Action Groups connect Bedrock Agents to Lambda functions using OpenAPI 3.0 schemas. |
| **39** | **B** | 4 | IP Indemnification | AWS offers intellectual property indemnification for customers using Amazon Titan models. |
| **40** | **B** | 5 | Model Access Control | All Bedrock models are disabled by default; access must be requested per account and region. |
| **41** | **C** | 1 | Amazon Translate | Amazon Translate delivers neural machine translation across dozens of languages. |
| **42** | **B** | 2 | Tokens | A token is the base textual unit processed by an LLM (1,000 tokens $\approx$ 750 words). |
| **43** | **B** | 3 | Chain-of-Thought (CoT) | Instructing models to "think step-by-step" breaks down reasoning to reduce errors. |
| **44** | **A** | 4 | DPL Interpretation | DPL ($+0.30$) shows historical data awarded favorable labels to Group A at a 30% higher rate. |
| **45** | **B** | 5 | AWS Artifact | AWS Artifact provides on-demand downloads of official security and compliance reports. |
| **46** | **B** | 1 | Regression | Predicting continuous numerical values (dollar amounts) is a regression task. |
| **47** | **B** | 2 | Diffusion Models | Diffusion models add and reverse Gaussian noise to generate realistic images. |
| **48** | **B** | 3 | BLEU Metric | BLEU measures $n$-gram precision and is the gold standard for evaluating machine translation. |
| **49** | **B** | 4 | Model Registry Approval | Models must be marked `Approved` before automated CI/CD pipelines can deploy them. |
| **50** | **B** | 5 | `bedrock:InvokeModel` | `bedrock:InvokeModel` is the IAM action authorizing model inference requests. |
| **51** | **A, B** | 1 | Decision Tree Pruning | Pruning tree depth and increasing minimum split samples prevents decision tree overfitting. |
| **52** | **A** | 2 | ReAct Loop | Agents iterate through: Thought $\rightarrow$ Action $\rightarrow$ Observation $\rightarrow$ Reflection. |
| **53** | **B** | 3 | Provisioned Throughput | Provisioned Throughput allocates Model Units (MUs) guaranteeing capacity without throttling. |
| **54** | **B** | 4 | Invisible Watermarking | Titan Image Generator embeds invisible digital watermarks to verify AI provenance. |
| **55** | **C** | 5 | KMS Customer Managed Keys | CMKs allow customers to control key rotation and immediately revoke decryption rights. |
| **56** | **B** | 1 | Amazon Kendra | Kendra is an intelligent enterprise semantic search service powered by NLP. |
| **57** | **A** | 2 | Causal Masking | Causal masking prevents decoder models from looking at future tokens during text generation. |
| **58** | **B** | 3 | LLM-as-a-Judge | Using frontier models (Nova Pro) to automatically evaluate smaller model outputs on a rubric. |
| **59** | **B** | 4 | Veracity | Veracity focuses on factual truthfulness and preventing hallucinated fabrications. |
| **60** | **A** | 5 | Security Scope 1 | Scope 1 covers consumer third-party apps where the customer has zero infrastructure control. |
| **61** | **B** | 1 | SageMaker JumpStart | JumpStart provides a hub of 1-click deployable foundation models and ML solutions. |
| **62** | **B** | 2 | Stop Sequences | Stop sequences immediately halt token generation when a specific string is emitted. |
| **63** | **B** | 3 | Catastrophic Forgetting | Overwriting too many base weights causes a model to forget its broader reasoning skills. |
| **64** | **B** | 4 | SageMaker Clarify (SHAP) | Clarify computes SHAP values for both local individual and global population explainability. |
| **65** | **B** | 5 | Least-Privilege IAM | Restricting the Resource ARN and using `aws:RequestedRegion` restricts model invocation. |

---

## 📊 Score Diagnostic Breakdown

To calculate your scaled score:
$$\text{Percentage Score} = \left(\frac{\text{Number of Correct Answers}}{65}\right) \times 100$$
$$\text{Estimated Scaled Score} = 100 + (\text{Percentage Score} \times 9.0)$$

* **$\ge 700$ Scaled Score ($\ge 46$ / 65 correct):** **PASS** — Ready for the official AWS exam.
* **$600 - 690$ Scaled Score ($39 - 45$ correct):** **BORDERLINE** — Review weak domains in the table above before sitting the exam.
* **$< 600$ Scaled Score ($< 39$ correct):** **NEEDS REVISION** — Review the 5 Domain Explanations and re-take the Knowledge Checks.
