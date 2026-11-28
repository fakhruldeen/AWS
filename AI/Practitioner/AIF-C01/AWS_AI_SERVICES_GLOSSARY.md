# 📖 AWS Certified AI Practitioner (`AIF-C01`) — Complete In-Scope AWS AI & Cloud Services Glossary

> **Purpose:** Single-source reference of **every in-scope AWS service** listed in the Official `AIF-C01` Exam Guide v1.2 (October 29, 2026, pp. 13–15), plus core AI/ML/GenAI concepts. Every heading serves as a direct anchor target linked across the `AIF-C01` quick revision sheets, study guides, and Arabic (`Ar/`) modules.

---

## 🧭 Categories Quick Jump
- [Machine Learning & Generative AI](#-machine-learning--generative-ai)
- [Developer Tools (Agentic AI)](#-developer-tools-agentic-ai)
- [Analytics & Data Preparation](#-analytics--data-preparation)
- [Databases & Vector Stores](#-databases--vector-stores)
- [Compute & Containers](#-compute--containers)
- [Storage](#-storage)
- [Security, Identity & Compliance](#-security-identity--compliance)
- [Management, Governance & FinOps](#-management-governance--finops)
- [Networking & Content Delivery](#-networking--content-delivery)

---

## 🤖 Machine Learning & Generative AI

### Amazon Bedrock
- **What it is:** Fully managed, serverless service providing a single API to access leading Foundation Models (`Amazon Nova`, `Anthropic Claude`, `Meta Llama`, `Mistral`, `Cohere`, `Titan`), plus `Knowledge Bases` (RAG), `Guardrails`, `Prompt Management`, `Model Distillation`, and `Model Evaluation`.
- **When to use it:** When building generative AI applications quickly without managing GPUs or servers, with strong enterprise data privacy (customer data is never used to train base models).

### Amazon Bedrock AgentCore
- **What it is:** Serverless enterprise platform for deploying, scaling, securing, and observing production AI agents across any framework (`Strands Agents`, LangGraph, etc.) and any FM — including `Runtime`, `Memory`, `Gateway` (`MCP`), `AgentCore Identity`, `Policy in AgentCore`, and `Observability`.
- **When to use it:** When moving autonomous AI agents to production with session isolation, managed memory, standardized `MCP` tool access, scoped user-delegated credentials, and deterministic allow/forbid tool policies.

### Amazon Nova
- **What it is:** AWS's family of Foundation Models available in `Amazon Bedrock`, spanning ultra-low-latency text (`Nova Micro`), multimodal understanding (`Nova Lite`, `Nova Pro`), image generation (`Nova Canvas`), and video generation (`Nova Reel`).
- **When to use it:** When you want cost-effective, fast, AWS-native multimodal models tightly integrated with Bedrock features like Prompt Caching, RAG, and Model Distillation.

### Amazon SageMaker AI
- **What it is:** End-to-end managed machine learning platform for data scientists and ML engineers to prepare data (`Data Wrangler`, `Ground Truth`), train custom models, tune hyperparameters, deploy endpoints (`Real-Time`, `Serverless`, `Async`, `Batch`), and run MLOps (`Pipelines`, `Model Monitor`, `Clarify`, `Model Cards`).
- **When to use it:** When you need full control over custom ML algorithms, custom model training, feature engineering, or hosting open-source FMs on dedicated infrastructure.

### Amazon SageMaker JumpStart
- **What it is:** Built-in ML hub inside `SageMaker AI` offering hundreds of pre-trained open-source Foundation Models, algorithms, and solution templates for one-click deployment and fine-tuning.
- **When to use it:** When you want to deploy or fine-tune open-weight FMs (e.g., `Llama`, `Mistral`, `Hugging Face` models) on your own dedicated SageMaker compute instances.

### Amazon Comprehend
- **What it is:** Managed Natural Language Processing (`NLP`) service that uses ML to extract insights from unstructured text (sentiment analysis, named entities, key phrases, language detection, topic modeling, PII detection).
- **When to use it:** When analyzing customer reviews, support tickets, or documents for sentiment/entities without training custom NLP models.

### Amazon Lex
- **What it is:** Fully managed service for building conversational voice and text chatbots using automatic speech recognition (`ASR`) and natural language understanding (`NLU`).
- **When to use it:** When creating interactive customer-service chatbots or contact-center bots (integrates natively with `Amazon Connect` and `AWS Lambda`).

### Amazon Personalize
- **What it is:** Managed ML service that creates real-time personalized product, content, and search recommendations using the same technology behind Amazon.com.
- **When to use it:** When building e-commerce or media recommendation engines without building collaborative filtering models from scratch.

### Amazon Polly
- **What it is:** Managed Text-to-Speech (`TTS`) service that turns text into lifelike spoken audio across dozens of languages and neural/generative voices.
- **When to use it:** When adding voice narration, accessibility audio, or spoken responses to applications.

### Amazon Rekognition
- **What it is:** Managed Computer Vision service for analyzing images and videos (object/scene detection, facial analysis, celebrity recognition, text-in-image, and unsafe content moderation).
- **When to use it:** When automating visual inspection, identity verification, or content moderation via simple API calls.

### Amazon Textract
- **What it is:** Managed Document AI / smart OCR service that automatically extracts printed text, handwriting, **key-value form fields, and structured tables** from scanned documents and PDFs.
- **When to use it:** When digitizing invoices, tax forms, medical intake forms, or financial statements accurately without manual templates.

### Amazon Transcribe
- **What it is:** Managed Automatic Speech Recognition (`ASR` / Speech-to-Text) service that converts audio and video into accurate text transcripts with speaker identification, custom vocabularies, and PII redaction.
- **When to use it:** When transcribing call-center recordings, meetings, or subtitles (including `Transcribe Medical` for clinical speech).

### Amazon Translate
- **What it is:** Managed neural machine translation service delivering fast, fluent language translation for batch and real-time text.
- **When to use it:** When localizing websites, translating customer support tickets, or enabling cross-lingual analytics.

### AWS Transform
- **What it is:** Agentic AI service purpose-built to automate large-scale enterprise modernization and migration of legacy workloads (`.NET`, `Java`, `VMware`, `Mainframe`).
- **When to use it:** When accelerating legacy code upgrades and application modernization using specialized autonomous AI agents.

---

## 🛠️ Developer Tools (Agentic AI)

### Kiro
- **What it is:** AWS's agentic AI IDE built around **spec-driven development**, turning natural-language requirements into structured specifications, design plans, implementation tasks, and verified code.
- **When to use it:** When accelerating software and AI/ML application development from prototype to production with structured agentic engineering workflows.

### Strands Agents
- **What it is:** Open-source, model-driven Python SDK created by AWS for building and running single- and multi-agent AI applications with native **Model Context Protocol (`MCP`)** tool support.
- **When to use it:** When developers want to write clean, model-driven agent code locally and deploy it seamlessly to `Amazon Bedrock AgentCore` or containers.

---

## 📊 Analytics & Data Preparation

### Amazon Quick
- **What it is:** Unified AWS AI-powered business intelligence, natural-language analytics, research, and workflow automation service.
- **When to use it:** When business users need no-code natural-language querying across dashboards, enterprise documents, and corporate workflows with built-in permission governance.

### Amazon OpenSearch Service
- **What it is:** Managed search, log analytics, and **vector database** engine (including `OpenSearch Serverless`) supporting k-NN vector similarity and hybrid search.
- **When to use it:** As the primary scalable vector store for `Amazon Bedrock Knowledge Bases` (RAG) and enterprise semantic search.

### AWS Glue
- **What it is:** Serverless ETL (Extract, Transform, Load) and central Data Catalog service.
- **When to use it:** When discovering schemas, cataloging datasets, and running scalable data preparation pipelines for AI/ML training data.

### AWS Glue DataBrew
- **What it is:** Visual, **no-code** data preparation tool with 250+ pre-built transformations for cleaning, normalizing, and profiling datasets.
- **When to use it:** When analysts or data scientists want to clean anomalies, handle missing values, and mask PII visually without writing Spark code.

### AWS Lake Formation
- **What it is:** Centralized data lake governance service that sets fine-grained (table, column, row, cell-level) permissions across S3 data lakes.
- **When to use it:** When enforcing strict data governance and access control over AI/ML training data lakes.

### Amazon EMR
- **What it is:** Managed big-data processing cluster platform running open-source frameworks like Apache Spark, Hive, and Presto.
- **When to use it:** When processing petabyte-scale distributed datasets for feature engineering or large-scale ML preparation.

### Amazon Redshift
- **What it is:** Fully managed, petabyte-scale cloud data warehouse with SQL-based `Redshift ML` integration.
- **When to use it:** When running complex OLAP analytics over structured enterprise data or invoking ML models directly from SQL.

### AWS Data Exchange
- **What it is:** Managed marketplace for discovering, subscribing to, and integrating third-party datasets directly into AWS (`S3`, `Redshift`).
- **When to use it:** When enriching ML training or RAG pipelines with licensed external datasets (financial, healthcare, geospatial).

---

## 🗄️ Databases & Vector Stores

### Amazon Aurora
- **What it is:** Cloud-native, high-performance MySQL- and PostgreSQL-compatible relational database supporting **`pgvector`** for storing and querying vector embeddings.
- **When to use it:** When storing RAG embeddings alongside transactional relational data in a highly available managed database.

### Amazon RDS
- **What it is:** Managed Relational Database Service (`PostgreSQL`, `MySQL`, `MariaDB`, `Oracle`, `SQL Server`); **RDS for PostgreSQL** supports `pgvector` for vector similarity search.
- **When to use it:** When existing PostgreSQL workloads need vector search for RAG without introducing a separate vector database.

### Amazon Neptune
- **What it is:** Fully managed graph database (`Neptune Database` & `Neptune Analytics`) supporting **GraphRAG** and vector-enhanced relationship queries.
- **When to use it:** When AI applications require traversing complex entity relationships (fraud rings, knowledge graphs, multi-hop RAG).

### Amazon DynamoDB
- **What it is:** Serverless, single-digit millisecond NoSQL key-value and document database.
- **When to use it:** When storing AI agent session state, chat history, prompt metadata, or low-latency ML feature lookups at massive scale.

### Amazon DocumentDB
- **What it is:** Managed JSON document database (with MongoDB compatibility) supporting vector search.
- **When to use it:** When storing semi-structured JSON documents and embeddings for MongoDB-compatible AI apps.

### Amazon ElastiCache
- **What it is:** Managed in-memory caching service (`Valkey`, `Redis OSS`, `Memcached`) delivering sub-millisecond latency.
- **When to use it:** When caching frequent LLM responses (semantic caching), session state, or hot inference features to cut latency and token costs.

---

## 🖥️ Compute & Containers

### Amazon EC2
- **What it is:** Resizable virtual servers (`IaaS`), including specialized AI/ML accelerators (`AWS Trainium` for training, `AWS Inferentia` for inference, and NVIDIA GPU `P`/`G` instances).
- **When to use it:** When you need full OS-level control over self-hosted models or custom deep-learning compute clusters.

### AWS Lambda
- **What it is:** Serverless, event-driven compute running code without provisioning servers (up to 15 min per invocation).
- **When to use it:** As Bedrock Agent **Action Groups**, MCP tool backends, lightweight API glue, or event-driven S3 document preprocessing.

### Amazon ECS & Amazon EKS
- **What it is:** Managed container orchestration services (`ECS` = AWS-native Docker orchestration; `EKS` = managed Kubernetes).
- **When to use it:** When hosting containerized ML microservices, self-managed open-source LLMs, or custom `Strands Agents` / `MCP` servers.

---

## 💾 Storage

### Amazon S3
- **What it is:** Virtually unlimited serverless object storage (`11 9s` durability) — the foundational data lake for AI/ML datasets, RAG source documents, model artifacts, and Bedrock invocation logs.
- **When to use it:** As the central storage layer for raw/processed training data, Knowledge Base source documents, and audit logs.

### Amazon S3 Glacier
- **What it is:** Ultra-low-cost archival S3 storage classes (`Instant`, `Flexible`, `Deep Archive`).
- **When to use it:** For long-term retention of historical training datasets, compliance archives, and old model invocation logs.

---

## 🛡️ Security, Identity & Compliance

### AWS IAM
- **What it is:** Identity and Access Management — controls authentication and least-privilege authorization (`Roles`, `Policies`) across all AWS AI services.
- **When to use it:** Always — attach IAM roles (never hardcoded keys) to Bedrock, SageMaker, Lambda, and AgentCore workloads.

### AWS KMS
- **What it is:** Key Management Service — creates and controls cryptographic keys (`CMKs`) to encrypt training data, vector indexes, custom models, and logs at rest.
- **When to use it:** Whenever enterprise compliance requires customer-managed encryption keys (`SSE-KMS`) and key audit trails.

### Amazon Macie
- **What it is:** Managed data security service using ML to automatically discover and classify **PII and sensitive data stored in Amazon S3**.
- **When to use it:** Before ingesting S3 buckets into ML training jobs or RAG Knowledge Bases to prevent accidental PII leakage.

### AWS Secrets Manager
- **What it is:** Securely stores, retrieves, and automatically rotates database credentials, third-party API keys, and OAuth secrets.
- **When to use it:** When AI agents or ML pipelines need authenticated access to external APIs or databases without hardcoding secrets.

### Amazon Inspector
- **What it is:** Automated vulnerability management service continuously scanning `EC2`, `ECR` container images, and `Lambda` functions for CVEs and unintended network exposure.
- **When to use it:** To continuously scan containerized AI workloads and Lambda agent tools for software vulnerabilities.

### AWS Artifact
- **What it is:** Self-service portal for downloading AWS third-party compliance reports (`SOC`, `ISO`, `PCI`) and managing agreements (`HIPAA BAA`).
- **When to use it:** When auditors require proof of AWS's underlying infrastructure compliance for regulated AI workloads.

---

## 📋 Management, Governance & FinOps

### AWS CloudTrail
- **What it is:** Records all AWS API calls and user/service activity across your AWS account for security auditing and governance.
- **When to use it:** To audit *who* invoked administrative actions on Bedrock, SageMaker, IAM, or S3.

### Amazon CloudWatch
- **What it is:** Observability service for collecting metrics, logs, and alarms (including `Bedrock` invocation latency/token metrics and `SageMaker` endpoint health).
- **When to use it:** To monitor AI latency, error rates, throttling, token consumption, and trigger operational alarms.

### AWS Config
- **What it is:** Continuously records AWS resource configurations and evaluates them against compliance rules (e.g., verifying S3 encryption or VPC endpoint attachment).
- **When to use it:** For continuous configuration compliance auditing and drift detection across AI infrastructure.

### AWS Trusted Advisor
- **What it is:** Automated best-practice advisor checking cost optimization, performance, security, fault tolerance, and service quotas.
- **When to use it:** To check AI service quotas, flag over-provisioned resources, or identify public S3 buckets.

### AWS Well-Architected Tool
- **What it is:** Free console tool to review workloads against the 6 Well-Architected Pillars and specialized Lenses (including the **Generative AI Lens** and **Machine Learning Lens**).
- **When to use it:** When conducting structured architectural and risk reviews of AI/GenAI workloads.

### AWS Budgets & AWS Cost Explorer
- **What they are:** `Cost Explorer` visualizes and forecasts historical AWS/Bedrock/SageMaker spend; `AWS Budgets` sets custom cost/usage thresholds with proactive alerts and actions.
- **When to use them:** For GenAI FinOps — tracking token spend, Provisioned Throughput utilization, and preventing unexpected AI cost spikes.

---

## 🌐 Networking & Content Delivery

### Amazon VPC
- **What it is:** Isolated virtual private cloud network; pairs with **AWS PrivateLink (Interface VPC Endpoints)** so Bedrock and SageMaker traffic stays privately on the AWS backbone without traversing the public internet.
- **When to use it:** Whenever security or regulatory rules mandate private network connectivity for AI inference and training.

### Amazon CloudFront
- **What it is:** Global Content Delivery Network (`CDN`) caching static/dynamic content and routing API requests at 600+ Edge Locations with low latency.
- **When to use it:** To accelerate global user access to AI web applications and protect front-end GenAI endpoints at the edge.
