# 📖 AWS Certified Cloud Practitioner (`CLF-C02`) — Complete AWS Services Glossary

> **Purpose:** Single-source reference of every AWS service tested in `CLF-C02` with a crisp **What it is** and **When to use it** entry. Every heading serves as a direct anchor target linked across the `CLF-C02` revision sheets and deep-dive guides.

---

## 🧭 Categories Quick Jump
- [Compute & Serverless](#-compute--serverless)
- [Storage & Hybrid Data](#-storage--hybrid-data)
- [Databases & Caching](#-databases--caching)
- [Networking & Content Delivery](#-networking--content-delivery)
- [Security, Identity & Compliance](#-security-identity--compliance)
- [Application Integration](#-application-integration)
- [Management, Observability & DevOps](#-management-observability--devops)
- [Migration & Transfer](#-migration--transfer)
- [Analytics & Big Data](#-analytics--big-data)
- [AI & Machine Learning](#-ai--machine-learning)
- [Developer, Mobile & End-User Computing](#-developer-mobile--end-user-computing)
- [Billing, Pricing & Support](#-billing-pricing--support)

---

## 🖥️ Compute & Serverless

### Amazon EC2
- **What it is:** Elastic Compute Cloud — resizable virtual servers (`IaaS`) in the AWS Cloud.
- **When to use it:** When you need full OS-level control (`Linux`/`Windows`) over compute instances using `On-Demand`, `Savings Plans`, `Reserved`, `Spot`, or `Dedicated Host` pricing.

### Amazon EC2 Auto Scaling
- **What it is:** Automated capacity management that adds or removes `EC2` instances based on demand and health checks.
- **When to use it:** When your workload experiences variable traffic and needs automatic scaling (`Elasticity`) and self-healing (`High Availability`).

### Elastic Load Balancing
- **What it is:** Managed load balancers (`ALB` for HTTP/HTTPS, `NLB` for ultra-fast TCP/UDP, `GWLB` for security appliances) that distribute incoming traffic across healthy targets.
- **When to use it:** When routing traffic across multiple `EC2` instances, containers, or `Lambda` functions across multiple Availability Zones.

### AWS Lambda
- **What it is:** Serverless, event-driven compute service that runs code without provisioning or managing servers (max 15 minutes per invocation).
- **When to use it:** When you want zero server management and pay-per-millisecond billing for event-driven APIs, file processing, or automation tasks.

### Amazon ECS
- **What it is:** Elastic Container Service — AWS-native managed container orchestration service for Docker containers.
- **When to use it:** When running containerized applications on AWS with deep native integration (`IAM`, `ALB`, `CloudWatch`) and minimal orchestration complexity.

### Amazon EKS
- **What it is:** Elastic Kubernetes Service — managed Kubernetes control plane on AWS.
- **When to use it:** When your team already uses standard open-source **Kubernetes** tooling or needs hybrid/multi-cloud container portability.

### Amazon ECR
- **What it is:** Elastic Container Registry — fully managed, private Docker container image registry.
- **When to use it:** When securely storing, versioning, scanning, and deploying container images for `ECS`, `EKS`, or `Fargate`.

### AWS Fargate
- **What it is:** Serverless compute engine for containers that works with both `Amazon ECS` and `Amazon EKS`.
- **When to use it:** When running Docker/Kubernetes containers **without managing underlying `EC2` servers**.

### AWS Elastic Beanstalk
- **What it is:** Platform-as-a-Service (`PaaS`) that automatically provisions `EC2`, `ELB`, and `Auto Scaling` when you upload application code.
- **When to use it:** When developers want to deploy web applications quickly without manually configuring infrastructure (service is free; pay only for underlying resources).

### Amazon Lightsail
- **What it is:** Simplified cloud platform offering pre-configured virtual servers, storage, and networking at fixed monthly prices.
- **When to use it:** For small websites, WordPress blogs, or simple dev/test environments needing predictable monthly billing.

### AWS Outposts
- **What it is:** Fully managed physical AWS hardware racks installed inside your on-premises data center running native AWS APIs.
- **When to use it:** When regulatory data residency or ultra-low local latency requires running AWS services physically on-premises.

### AWS Local Zones
- **What it is:** AWS infrastructure deployments placing compute, storage, and database services closer to large metro populations.
- **When to use it:** When latency-sensitive applications (gaming, live video, CAD) need single-digit millisecond latency in cities without a full AWS Region.

### AWS Wavelength
- **What it is:** Embeds AWS compute and storage directly inside telecommunications providers' **5G networks**.
- **When to use it:** When mobile, IoT, or autonomous vehicle apps require ultra-low latency over 5G without traversing the public internet.

### AWS Batch
- **What it is:** Fully managed batch computing service that dynamically provisions optimal compute resources (`EC2` / `Spot` / `Fargate`).
- **When to use it:** When running hundreds of thousands of asynchronous, high-volume batch processing jobs (e.g., financial modeling, media transcoding).

---

## 💾 Storage & Hybrid Data

### Amazon S3
- **What it is:** Simple Storage Service — virtually unlimited, serverless `Object Storage` with `99.999999999%` (`11 9s`) durability.
- **When to use it:** For storing images, videos, backups, data lakes, static websites, and archival data across 7 cost-optimized Storage Classes (`Standard` to `Glacier Deep Archive`).

### Amazon S3 Glacier
- **What it is:** Low-cost archival storage classes within `Amazon S3` (`Instant Retrieval`, `Flexible Retrieval`, and `Deep Archive`).
- **When to use it:** For long-term compliance archives and rarely accessed backups where lowest storage cost is the top priority (`Deep Archive`: 12–48 hr retrieval).

### Amazon EBS
- **What it is:** Elastic Block Store — persistent, high-performance network block storage volumes attached to a single `EC2` instance in one Availability Zone.
- **When to use it:** For OS boot drives, databases, and application data on `EC2` that must persist after instance stop/restart.

### Amazon EFS
- **What it is:** Elastic File System — serverless, elastic, shared `NFS` file storage for Linux instances across multiple Availability Zones.
- **When to use it:** When multiple Linux `EC2` instances or containers need concurrent read/write access to the same shared file system.

### Amazon FSx
- **What it is:** Fully managed third-party file systems including `FSx for Windows File Server` (`SMB` + Active Directory) and `FSx for Lustre` (`HPC`).
- **When to use it:** When Windows workloads require shared `SMB` file storage or high-performance computing/ML needs sub-millisecond Lustre storage.

### AWS Storage Gateway
- **What it is:** Hybrid cloud storage appliance connecting on-premises environments to AWS cloud storage (`S3`, `EBS`, `Glacier`).
- **When to use it:** When on-premises applications need low-latency local cached access to cloud-backed storage or cloud-based backups.

### AWS Backup
- **What it is:** Centralized, fully managed backup service automating backup policies across AWS services (`EBS`, `RDS`, `DynamoDB`, `EFS`, `S3`).
- **When to use it:** When you need unified, policy-driven backup scheduling, retention, and compliance auditing across your entire AWS estate.

---

## 🗄️ Databases & Caching

### Amazon RDS
- **What it is:** Relational Database Service — managed `SQL` databases supporting `MySQL`, `PostgreSQL`, `MariaDB`, `Oracle`, `SQL Server`, and `Db2`.
- **When to use it:** For traditional transactional (`OLTP`) relational workloads with automated patching, backups, `Multi-AZ` failover, and `Read Replicas`.

### Amazon Aurora
- **What it is:** AWS cloud-native relational database compatible with `MySQL` (up to 5x faster) and `PostgreSQL` (up to 3x faster), replicating 6 copies across 3 AZs.
- **When to use it:** When you want enterprise relational performance and high availability at a fraction of commercial database cost.

### Amazon DynamoDB
- **What it is:** Fully managed, serverless `NoSQL` key-value and document database delivering single-digit millisecond latency at any scale.
- **When to use it:** For high-throughput web, mobile, gaming, and IoT apps needing massive horizontal scaling and zero server administration (`DAX` adds microsecond caching).

### Amazon ElastiCache
- **What it is:** Fully managed in-memory caching service supporting `Redis` and `Memcached`.
- **When to use it:** When offloading frequent read queries from relational/NoSQL databases to achieve sub-millisecond application response times.

### Amazon Redshift
- **What it is:** Fully managed, petabyte-scale cloud **Data Warehouse** optimized for Online Analytical Processing (`OLAP`).
- **When to use it:** For running complex SQL analytics and Business Intelligence (`BI`) reporting across massive historical datasets.

### Amazon DocumentDB
- **What it is:** Managed, scalable document database compatible with `MongoDB`.
- **When to use it:** When migrating or building applications that store and query flexible `JSON` documents using MongoDB drivers.

### Amazon Neptune
- **What it is:** Fully managed **Graph Database** service optimized for storing and querying billions of relationships.
- **When to use it:** For social networks, fraud detection rings, knowledge graphs, and real-time recommendation engines.

### Amazon MemoryDB
- **What it is:** Redis-compatible, durable in-memory database providing Multi-AZ persistence.
- **When to use it:** When an application needs microsecond read/write speeds with primary database durability (not just a disposable cache).

### AWS DMS
- **What it is:** Database Migration Service — migrates relational and NoSQL databases to AWS with near-zero downtime.
- **When to use it:** When migrating on-premises databases to `RDS`, `Aurora`, or `Redshift` (supports heterogeneous engine conversions with `AWS SCT`).

---

## 🌐 Networking & Content Delivery

### Amazon VPC
- **What it is:** Virtual Private Cloud — logically isolated private virtual network in AWS where you control IP ranges (`CIDR`), Subnets, Route Tables, and Gateways.
- **When to use it:** As the foundational network boundary for launching `EC2`, `RDS`, `ECS`, and other private cloud resources.

### Amazon Route 53
- **What it is:** Highly available, scalable global `DNS` web service (port 53) with domain registration, health checks, and intelligent traffic routing.
- **When to use it:** To map domain names to AWS resources and route global users via `Latency`, `Geolocation`, `Weighted`, or `Failover` policies.

### Amazon CloudFront
- **What it is:** Global Content Delivery Network (`CDN`) caching static and dynamic `HTTP/HTTPS` content at 600+ Edge Locations worldwide.
- **When to use it:** To accelerate website/video/API delivery globally with low latency and protect origins using Origin Access Control (`OAC`) and `WAF`.

### AWS Global Accelerator
- **What it is:** Networking service routing `TCP/UDP` user traffic over the private AWS Global Network using 2 Static Anycast IP addresses.
- **When to use it:** For non-HTTP global workloads (online gaming, `VoIP`, `IoT`) requiring static IPs, consistent low latency, and instant multi-Region failover.

### AWS Direct Connect
- **What it is:** Dedicated private physical fiber network connection between your on-premises data center and AWS bypassing the public internet.
- **When to use it:** When hybrid workloads require consistent high bandwidth, predictable low latency, and reduced data transfer costs over time.

### AWS Site-to-Site VPN
- **What it is:** Encrypted `IPsec VPN` tunnel connecting your on-premises network to an `Amazon VPC` over the public internet.
- **When to use it:** When you need quick (minutes/hours), low-cost encrypted hybrid connectivity or a backup link for `Direct Connect`.

### AWS Transit Gateway
- **What it is:** Centralized hub-and-spoke cloud router connecting hundreds of `VPCs` and on-premises networks through a single gateway.
- **When to use it:** When managing complex multi-VPC and hybrid network topologies without creating a mesh of 1-to-1 `VPC Peering` links.

### AWS PrivateLink
- **What it is:** Private connectivity technology powering `Interface VPC Endpoints` so traffic between your VPC and AWS/partner services never touches the public internet.
- **When to use it:** When strict security policies forbid internet routing while accessing AWS APIs (`SQS`, `Secrets Manager`, `Bedrock`) or SaaS services.

---

## 🔒 Security, Identity & Compliance

### AWS IAM
- **What it is:** Identity and Access Management — free global service controlling authentication and authorization (`Users`, `Groups`, `Roles`, `Policies`, `MFA`).
- **When to use it:** To enforce least-privilege access across every user, application, and AWS service in your account.

### AWS IAM Identity Center
- **What it is:** Formerly `AWS Single Sign-On (AWS SSO)` — centralized workforce identity and Single Sign-On portal.
- **When to use it:** When managing employee access across **multiple AWS accounts** (`AWS Organizations`) and third-party business `SaaS` apps from one login.

### AWS IAM Access Analyzer
- **What it is:** Policy analysis tool that detects externally shared AWS resources, flags unused permissions, and generates least-privilege policies from `CloudTrail`.
- **When to use it:** When auditing unintended public/cross-account access or tightening permissions toward strict least privilege.

### Amazon Cognito
- **What it is:** Managed customer identity service providing user sign-up, sign-in, and social/federated login (`Google`, `Apple`, `Facebook`).
- **When to use it:** When adding authentication and authorization for **external web and mobile application users** (millions of customers).

### AWS Organizations
- **What it is:** Free multi-account governance service organizing accounts into `OUs` with **Consolidated Billing** and **Service Control Policies (`SCPs`)**.
- **When to use it:** When managing multiple AWS accounts (`Dev`/`Staging`/`Prod`), enforcing organization-wide guardrails, and pooling volume discounts.

### AWS Control Tower
- **What it is:** Managed service that automates setting up and governing a secure, multi-account AWS **Landing Zone** on top of `AWS Organizations`.
- **When to use it:** When you want the easiest, fastest way to establish pre-configured multi-account guardrails and account vending.

### AWS Resource Access Manager
- **What it is:** `AWS RAM` — securely shares AWS resources (such as `VPC Subnets`, `Transit Gateway`, and `Route 53` rules) across AWS accounts.
- **When to use it:** To reduce resource duplication and operational overhead across accounts in `AWS Organizations`.

### AWS KMS
- **What it is:** Key Management Service — managed multi-tenant service to create, rotate, and control cryptographic keys across AWS services.
- **When to use it:** For seamless `Encryption at Rest` across `S3`, `EBS`, `RDS`, and `Secrets Manager` with full `CloudTrail` auditing.

### AWS CloudHSM
- **What it is:** Single-tenant, dedicated physical Hardware Security Module (`HSM`) inside your VPC (`FIPS 140-2 Level 3`).
- **When to use it:** When strict banking or government compliance mandates exclusive, single-tenant hardware control over encryption keys.

### AWS Certificate Manager
- **What it is:** `ACM` — provisions, deploys, and automatically renews public and private `SSL/TLS` certificates.
- **When to use it:** To enable `HTTPS` (`Encryption in Transit`) for free on `CloudFront`, `ALB`, and `API Gateway` with zero manual renewal risk.

### AWS Secrets Manager
- **What it is:** Managed vault for storing database credentials, API keys, and OAuth tokens with built-in **automatic secret rotation**.
- **When to use it:** When storing sensitive credentials (especially `RDS` passwords) that must rotate automatically on a schedule.

### AWS Shield
- **What it is:** Managed Distributed Denial of Service (`DDoS`) protection (`Standard` is free for all customers; `Advanced` adds 24/7 `SRT` and DDoS cost protection).
- **When to use it:** To protect public-facing AWS workloads from Layer 3/4 volumetric and protocol DDoS attacks.

### AWS WAF
- **What it is:** Web Application Firewall operating at Layer 7 (`HTTP/HTTPS`) to inspect and filter malicious web requests.
- **When to use it:** To block **`SQL Injection`**, **`Cross-Site Scripting (XSS)`**, bots, and specific IPs/countries in front of `CloudFront`, `ALB`, or `API Gateway`.

### AWS Network Firewall
- **What it is:** Managed, stateful VPC-level network firewall providing intrusion detection/prevention (`IDS/IPS`) and domain filtering.
- **When to use it:** When you need deep packet inspection and centralized outbound/inbound traffic filtering across an entire `VPC`.

### AWS Firewall Manager
- **What it is:** Centralized security management tool to configure and enforce `WAF`, `Shield Advanced`, and `Security Group` rules across `AWS Organizations`.
- **When to use it:** When governing consistent firewall policies across dozens or hundreds of AWS accounts automatically.

### Amazon GuardDuty
- **What it is:** ML-powered intelligent threat detection service continuously analyzing `CloudTrail`, `VPC Flow Logs`, and `DNS Logs`.
- **When to use it:** To detect compromised credentials, crypto-mining, anomalous API calls, and malicious network communication automatically.

### Amazon Inspector
- **What it is:** Automated vulnerability management service continuously scanning `EC2`, `ECR` container images, and `Lambda` functions.
- **When to use it:** To detect known software vulnerabilities (`CVEs`) and unintended network exposure across compute workloads.

### Amazon Macie
- **What it is:** ML-powered data security service that scans `Amazon S3` buckets to discover and protect sensitive data.
- **When to use it:** When automatically locating **Personally Identifiable Information (`PII`)** (credit cards, SSNs) and alerting on exposed S3 buckets.

### AWS Security Hub
- **What it is:** Centralized Cloud Security Posture Management (`CSPM`) dashboard aggregating findings from `GuardDuty`, `Inspector`, `Macie`, and `Firewall Manager`.
- **When to use it:** For a single-pane-of-glass security view and automated compliance checks against `CIS`, `PCI-DSS`, and AWS Foundational Security Best Practices.

### Amazon Detective
- **What it is:** Security investigation service that visualizes log data into interactive relationship graphs.
- **When to use it:** After a threat is detected to perform rapid **root cause analysis** and determine the blast radius of an incident.

### AWS Artifact
- **What it is:** Free self-service portal providing on-demand access to AWS compliance reports (`SOC 2`, `ISO 27001`, `PCI-DSS`) and agreements (`BAA`).
- **When to use it:** When auditors or regulators ask for official third-party proof of AWS infrastructure compliance.

### AWS Audit Manager
- **What it is:** Continuous auditing service that automatically collects evidence from your AWS usage against compliance frameworks.
- **When to use it:** To simplify audit preparation and continuously assess risk against `HIPAA`, `GDPR`, or `PCI-DSS` controls.

---

## 🔗 Application Integration

### Amazon SQS
- **What it is:** Simple Queue Service — fully managed serverless message queuing service (`Standard` and `FIFO`) for decoupling distributed components.
- **When to use it:** When buffering requests between microservices so messages are never lost during traffic spikes or downstream outages (`Pull` model).

### Amazon SNS
- **What it is:** Simple Notification Service — fully managed Publish/Subscribe (`Pub/Sub`) messaging service (`Push` model).
- **When to use it:** When broadcasting a single message simultaneously to multiple subscribers via `Email`, `SMS`, mobile push, `Lambda`, or `SQS` fan-out.

### Amazon EventBridge
- **What it is:** Serverless event bus connecting AWS services, custom applications, and third-party `SaaS` apps using rule-based event routing and cron schedules.
- **When to use it:** When building event-driven architectures or reacting automatically to AWS state changes and scheduled triggers.

### AWS Step Functions
- **What it is:** Serverless visual workflow orchestration service coordinating multiple `Lambda` functions and AWS services as state machines.
- **When to use it:** When building multi-step business processes requiring built-in retries, error handling, branching, and long-running state tracking.

### Amazon API Gateway
- **What it is:** Fully managed, serverless front door for creating, publishing, throttling, and securing `REST`, `HTTP`, and `WebSocket` APIs.
- **When to use it:** When exposing `AWS Lambda` or backend microservices securely to web/mobile clients at any scale.

---

## 🛠️ Management, Observability & DevOps

### Amazon CloudWatch
- **What it is:** Unified observability service collecting performance metrics (`CPU`, memory, network), application logs, custom dashboards, and automated alarms.
- **When to use it:** To monitor live system performance, aggregate logs, and trigger `Auto Scaling` or `SNS` alerts on metric thresholds.

### AWS CloudTrail
- **What it is:** Governance and auditing service recording every `API` call and user action across Console, CLI, and SDKs.
- **When to use it:** To answer **"Who did what, when, and from where?"** for security auditing, compliance, and incident forensics.

### AWS Config
- **What it is:** Configuration tracking and compliance service recording resource configuration history over time and evaluating compliance rules.
- **When to use it:** To see how a resource's settings changed over time and automatically flag non-compliant configurations (e.g., unencrypted `EBS` or public `S3`).

### AWS Trusted Advisor
- **What it is:** Automated best-practice advisor inspecting your AWS account across 5 pillars: **Cost Optimization, Performance, Security, Fault Tolerance, and Service Quotas**.
- **When to use it:** To find idle resources, missing root `MFA`, and quota limits (`7 Core Checks` free in Basic; `Full Set` unlocked in Business/Enterprise Support).

### AWS Systems Manager
- **What it is:** `SSM` — unified operational hub for managing `EC2` and on-premises servers (`Patch Manager`, `Session Manager`, `Run Command`, `Parameter Store`).
- **When to use it:** To automate OS patching, securely access instances without opening `SSH` port 22 (`Session Manager`), and store configuration parameters (`Parameter Store`).

### AWS CloudFormation
- **What it is:** Infrastructure as Code (`IaC`) service that provisions and manages AWS resources declaratively using `YAML` or `JSON` templates.
- **When to use it:** To deploy repeatable, version-controlled, consistent environments across Regions or accounts with zero manual console clicking.

### AWS CDK
- **What it is:** Cloud Development Kit — open-source `IaC` framework letting developers define cloud infrastructure using TypeScript, Python, Java, C#, or Go.
- **When to use it:** When engineering teams prefer writing reusable infrastructure in familiar programming languages that synthesize into `CloudFormation`.

### AWS CodeBuild
- **What it is:** Fully managed, serverless continuous integration service that compiles source code, runs unit tests, and produces deployable packages.
- **When to use it:** As the build and automated testing stage in a `CI/CD` pipeline without managing build servers.

### AWS CodeDeploy
- **What it is:** Automated deployment service pushing application updates to `EC2`, `ECS`, `Lambda`, and on-premises servers with minimal downtime.
- **When to use it:** To automate rolling, blue/green, or canary deployments safely with automatic rollback.

### AWS CodePipeline
- **What it is:** Fully managed Continuous Delivery (`CI/CD`) orchestration service automating release pipelines from code commit to production.
- **When to use it:** To connect source repositories, `CodeBuild`, and `CodeDeploy` into a single automated release workflow.

### AWS Well-Architected Tool
- **What it is:** Free self-service console tool for reviewing workloads against the 6 Pillars of the `AWS Well-Architected Framework` and specialized Lenses.
- **When to use it:** To systematically identify High/Medium-Risk architectural issues and generate actionable improvement plans.

### AWS Fault Injection Service
- **What it is:** Managed chaos engineering service for running controlled fault injection experiments on AWS workloads.
- **When to use it:** To test recovery procedures and validate `Reliability` / `High Availability` under simulated outages (`Game Days`).

### AWS Service Catalog
- **What it is:** Governance service enabling IT administrators to publish a curated catalog of pre-approved, compliant `CloudFormation` products.
- **When to use it:** To allow teams to self-service deploy standardized, compliant AWS resources while enforcing corporate governance.

### AWS Health Dashboard
- **What it is:** Real-time visibility into global AWS service health (`Service Health`) and personalized alerts impacting your specific account resources (`Account Health`).
- **When to use it:** To check if an outage is a global AWS issue or if scheduled maintenance/events affect your own instances.

---

## 🚚 Migration & Transfer

### AWS Snow Family
- **What it is:** Rugged, encrypted physical edge-computing and data-transfer devices (`Snowcone`: 8–14 TB; `Snowball Edge`: 80–210 TB).
- **When to use it:** When transferring terabytes/petabytes offline faster than the internet or running local compute in disconnected/edge environments.

### AWS DataSync
- **What it is:** High-speed, automated online data transfer service between on-premises storage and AWS (`S3`, `EFS`, `FSx`).
- **When to use it:** When migrating large active file datasets or scheduling recurring online synchronization to AWS.

### AWS Application Migration Service
- **What it is:** `AWS MGN` — automated **Lift-and-Shift (`Rehost`)** service continuously replicating physical/virtual servers onto `Amazon EC2`.
- **When to use it:** For fast, minimal-downtime server migrations without modifying application code.

### AWS Migration Hub
- **What it is:** Single centralized dashboard tracking the discovery, planning, and progress of application and database migrations across AWS tools.
- **When to use it:** When coordinating and monitoring multi-wave enterprise migrations from one unified console.

### AWS Application Discovery Service
- **What it is:** Discovery tool that collects configuration, usage, and dependency data about on-premises servers before migration.
- **When to use it:** During the **Assess** phase to inventory servers, identify unused apps to `Retire`, and plan migration waves.

### AWS Migration Evaluator
- **What it is:** Free migration assessment service that builds data-driven Total Cost of Ownership (`TCO`) business cases for moving to AWS.
- **When to use it:** When executives need projected AWS cost comparisons before approving a migration project.

---

## 📊 Analytics & Big Data

### Amazon Athena
- **What it is:** Serverless interactive query service that analyzes data directly in `Amazon S3` using standard `SQL` (pay per TB scanned).
- **When to use it:** For ad-hoc SQL analytics on `S3` logs, CSV/JSON/Parquet files, or `CUR` billing reports without spinning up a database.

### AWS Glue
- **What it is:** Serverless Extract, Transform, and Load (`ETL`) service with a centralized Data Catalog.
- **When to use it:** To automatically discover, clean, enrich, and transform raw data in `S3` for analytics in `Athena` or `Redshift`.

### Amazon EMR
- **What it is:** Elastic MapReduce — managed big data platform running open-source frameworks like `Apache Spark`, `Hadoop`, `Hive`, and `Presto`.
- **When to use it:** When processing petabyte-scale big data workloads using existing Hadoop/Spark ecosystems.

### Amazon Kinesis
- **What it is:** Family of managed services for ingesting, buffering, and analyzing **real-time streaming data** at massive scale.
- **When to use it:** For live clickstreams, financial market feeds, IoT sensor telemetry, and real-time log/video streaming.

### Amazon QuickSight
- **What it is:** Serverless, ML-powered cloud Business Intelligence (`BI`) service for building interactive dashboards and visualizations.
- **When to use it:** When executives and analysts need scalable, pay-per-session visual reports over `S3`, `Athena`, `Redshift`, or `RDS`.

### Amazon OpenSearch Service
- **What it is:** Managed search and log analytics engine supporting full-text search, vector search, and real-time operational log visualization.
- **When to use it:** For application search bars, real-time log analytics, and `RAG` vector storage (`OpenSearch Serverless`).

---

## 🤖 AI & Machine Learning

### Amazon Bedrock
- **What it is:** Fully managed, serverless service providing API access to leading **Generative AI Foundation Models (`FMs`)** (`Claude`, `Amazon Nova`, `Llama`) with `Knowledge Bases` (`RAG`), `Agents`, and `Guardrails`.
- **When to use it:** When building Generative AI apps quickly without managing GPU infrastructure or training models from scratch.

### Amazon SageMaker
- **What it is:** End-to-end managed platform enabling data scientists and developers to **build, train, and deploy** custom Machine Learning models at scale.
- **When to use it:** When creating custom ML models, running `Canvas` no-code ML, or managing full `MLOps` pipelines.

### Amazon Rekognition
- **What it is:** Managed Computer Vision service that analyzes images and videos to detect objects, faces, text, and inappropriate content.
- **When to use it:** For automated identity verification, content moderation, and visual media tagging.

### Amazon Textract
- **What it is:** Intelligent Optical Character Recognition (`OCR`) service extracting text, handwriting, forms, and tables from scanned documents and PDFs.
- **When to use it:** When automating data entry from invoices, tax forms, receipts, and contracts.

### Amazon Comprehend
- **What it is:** Managed Natural Language Processing (`NLP`) service extracting insights, entities, key phrases, language, and **sentiment** from text.
- **When to use it:** To analyze customer product reviews, support tickets, or social media sentiment automatically.

### Amazon Polly
- **What it is:** Managed **Text-to-Speech (`TTS`)** service converting written text into lifelike human speech in dozens of languages.
- **When to use it:** For voice-enabled apps, audiobooks, accessibility narration, and automated phone prompts.

### Amazon Transcribe
- **What it is:** Managed **Speech-to-Text (`ASR`)** service converting audio and live speech into accurate text transcripts.
- **When to use it:** For transcribing customer service calls, generating video subtitles, and medical/legal dictation.

### Amazon Translate
- **What it is:** Neural machine translation service providing fast, high-quality, customizable language translation.
- **When to use it:** For real-time localization of websites, chat messages, and multilingual documents.

### Amazon Lex
- **What it is:** Managed conversational AI service for building voice and text **Chatbots** (powered by the same engine as `Amazon Alexa`).
- **When to use it:** For automated self-service customer support chatbots and interactive voice response (`IVR`) bots with `Amazon Connect`.

### Amazon Kendra
- **What it is:** Intelligent, ML-powered enterprise search service answering natural-language questions across internal documents and repositories.
- **When to use it:** When employees need accurate semantic search across SharePoint, `S3`, Confluence, and internal knowledge bases.

### Amazon Personalize
- **What it is:** Managed ML service creating real-time personalized product and content recommendations (same technology as `Amazon.com`).
- **When to use it:** For e-commerce "Recommended for you" feeds, media streaming suggestions, and targeted marketing.

---

## 📱 Developer, Mobile & End-User Computing

### AWS Amplify
- **What it is:** Full-stack development and hosting platform for rapidly building and deploying web and mobile applications with built-in `CI/CD`.
- **When to use it:** When frontend/mobile developers want fast full-stack deployment with managed authentication, APIs, and hosting.

### AWS Device Farm
- **What it is:** Cloud testing service allowing developers to test Android, iOS, and web apps on **real physical mobile devices and desktop browsers**.
- **When to use it:** To catch device-specific crashes, layout bugs, and performance regressions before releasing apps.

### AWS AppSync
- **What it is:** Managed, serverless **`GraphQL` API** service supporting real-time data subscriptions and offline data synchronization.
- **When to use it:** For collaborative web/mobile apps requiring live updates and seamless offline-to-online sync across multiple data sources.

### Amazon AppStream 2.0
- **What it is:** Fully managed **application streaming** service delivering desktop applications securely to any `HTML5` web browser without rewriting code.
- **When to use it:** When users need instant browser access to heavy desktop software (e.g., `CAD`, 3D, enterprise apps) on any device without persistent desktops.

### Amazon WorkSpaces
- **What it is:** Fully managed Desktop-as-a-Service (`DaaS`) providing **persistent cloud-based Windows or Linux virtual desktops**.
- **When to use it:** When provisioning full, persistent virtual desktop environments for remote or hybrid employees.

### Amazon Connect
- **What it is:** Omnichannel, pay-as-you-go **cloud contact center** supporting voice calls, chat, and `Amazon Lex` AI automation.
- **When to use it:** To replace legacy on-premises call centers with a scalable cloud contact center in minutes.

### Amazon SES
- **What it is:** Simple Email Service — cost-effective, high-volume transactional and bulk email sending/receiving service.
- **When to use it:** For application password resets, order confirmations, and high-deliverability email notifications.

### Amazon Pinpoint
- **What it is:** Flexible outbound and inbound **omnichannel marketing engagement** service (`Email`, `SMS`, `Push`, `Voice`) with campaign analytics.
- **When to use it:** For targeted marketing campaigns, user segmentation, and tracking customer engagement across multiple channels.

---

## 💰 Billing, Pricing & Support

### AWS Pricing Calculator
- **What it is:** Free web-based estimation tool to model and calculate projected monthly/annual AWS costs **before deploying**.
- **When to use it:** During planning to compare architectures and estimate `On-Demand` vs `Savings Plans` costs upfront.

### AWS Budgets
- **What it is:** Cost and usage tracking tool that sends automated **alerts** (or executes automated budget actions) when actual or forecasted spend crosses a threshold.
- **When to use it:** To prevent surprise bills with proactive email/`SNS` threshold notifications.

### AWS Cost Explorer
- **What it is:** Visual cost analytics tool showing up to 13 months of historical spending and **12-month future cost forecasts** plus `RI`/`Savings Plans` recommendations.
- **When to use it:** To analyze spending trends by service/tag and forecast upcoming cloud budgets.

### AWS Cost and Usage Report
- **What it is:** `CUR` — the most detailed, hourly, granular billing dataset exported automatically to `Amazon S3`.
- **When to use it:** For deep enterprise financial analysis, chargebacks, and querying exact usage with `Amazon Athena` or `QuickSight`.

### AWS Compute Optimizer
- **What it is:** ML-powered **rightsizing** service analyzing utilization metrics for `EC2`, `EBS`, `Lambda`, and `ECS`.
- **When to use it:** To identify over-provisioned resources and lower bills without sacrificing performance.

### AWS Cost Anomaly Detection
- **What it is:** ML-based monitoring tool that detects unexpected, unusual spikes in AWS spending and identifies the root cause.
- **When to use it:** To catch runaway workloads or misconfigurations early before month-end billing.

### AWS Customer Carbon Footprint Tool
- **What it is:** Free billing console tool measuring historical carbon emissions associated with your AWS cloud usage.
- **When to use it:** To track `Sustainability` goals and report ESG carbon reduction from migrating to AWS.

### AWS Marketplace
- **What it is:** Curated digital catalog of thousands of third-party software solutions, AMIs, containers, and SaaS products billed directly on your AWS invoice.
- **When to use it:** When procuring pre-configured third-party security appliances, databases, or AI tools with consolidated AWS billing.
