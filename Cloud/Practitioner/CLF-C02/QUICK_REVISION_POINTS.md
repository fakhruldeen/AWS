# ⚡ AWS Certified Cloud Practitioner (`CLF-C02`) — Full-Course Quick Revision (Bullet Points Only)

> **Exam Specs:** 65 Questions (50 scored + 15 unscored) • 90 mins (+30 mins free `ESL +30`) • Pass: `700 / 1000`

---

## 1️⃣ Domain 1: Cloud Concepts (`24%`)

### Cloud Value & Models
- **6 Advantages of Cloud:**
  - Trade fixed expense (`CapEx`) for variable expense (`OpEx`).
  - Benefit from massive **economies of scale** (lower prices via aggregate AWS usage).
  - **Stop guessing capacity** (scale up/down on demand).
  - Increase speed and **agility** (launch in minutes, experiment cheaply, fail fast).
  - Stop spending money running/maintaining data centers (**undifferentiated heavy lifting**).
  - **Go global in minutes** (deploy in multiple Regions for low latency).
- **Service Models:** `IaaS` (EC2, VPC — you manage OS) • `PaaS` (Elastic Beanstalk, RDS — AWS manages OS/infra) • `SaaS` (QuickSight, WorkMail — ready-to-use app).
- **Deployment Models:** `Cloud-Based` (100% AWS) • `On-Premises` (private data center) • `Hybrid` (On-Premises + AWS connected).

### AWS Global Infrastructure
- **Region:** Isolated geographic area (`us-east-1`, `eu-north-1`); data never leaves unless you move it. Choose by: **Compliance**, **Latency/Proximity**, **Available Services**, **Pricing**.
- **Availability Zone (`AZ`):** 1+ isolated data centers inside a Region (min 3 AZs/Region), independent power/cooling, connected via ultra-low latency fiber.
- **Edge Locations (600+ PoPs):** Used by `CloudFront` (caching static/dynamic content), `Route 53`, `WAF`, `Shield`.
- **Local Zones:** Place compute/storage closer to large metro cities (single-digit ms latency).
- **Wavelength:** Embeds AWS compute inside **5G telco carrier networks**.
- **[AWS Outposts](./AWS_SERVICES_GLOSSARY.md#aws-outposts):** Physical AWS hardware racks installed **on-premises** running native AWS APIs.

### AWS Well-Architected Framework (`6 Pillars`)
- **Operational Excellence:** Perform operations as code (`CloudFormation`), frequent small reversible changes, refine runbooks, anticipate & learn from failures.
- **Security:** Strong identity (`IAM`, `MFA`, least privilege), traceability (`CloudTrail`), defense in depth, automate security, encrypt at rest & in transit, keep people away from data.
- **Reliability:** Automatically recover from failure, test recovery procedures, scale horizontally (`Auto Scaling`), stop guessing capacity, manage change in automation.
- **Performance Efficiency:** Democratize advanced technologies (managed services), go global in minutes, use serverless (`Lambda`), experiment more often, mechanical sympathy.
- **Cost Optimization:** Cloud Financial Management (`FinOps`), consumption model, measure efficiency, stop undifferentiated heavy lifting, attribute expenditure (`Tags`).
- **Sustainability:** Minimize carbon/energy impact (`Customer Carbon Footprint Tool`), maximize utilization, use `AWS Graviton` processors & managed services.
- **[AWS Well-Architected Tool](./AWS_SERVICES_GLOSSARY.md#aws-well-architected-tool):** Free Console tool to review workloads against the 6 pillars + Lenses (`Serverless`, `SaaS`, `GenAI`) and identify High/Medium-Risk Issues.

### AWS Cloud Adoption Framework (`AWS CAF 3.0`)
- **4 Business Outcomes:** Reduced business risk • Improved ESG performance • Increased revenue • Increased operational efficiency.
- **4 Transformation Domains:** `Technology` • `Process` • `Organization` (`CCoE`) • `Product`.
- **6 Perspectives:**
  - *Business Capabilities:* **Business** (ROI, strategy) • **People** (training, culture, change management) • **Governance** (portfolio, risk, `FinOps`).
  - *Technical Capabilities:* **Platform** (cloud architecture, `Landing Zones`, data architecture) • **Security** (`IAM`, compliance, threat defense) • **Operations** (observability, `SLAs`, incident management).
- **4 Transformation Phases:** `Envision` → `Align` → `Launch` (pilots) → `Scale` (enterprise-wide).

### Migration Strategies (`7 Rs`) & Disaster Recovery (`DR`)
- **7 Rs:**
  - **Rehost** (*Lift-and-Shift*): Zero code changes, fastest (`AWS MGN`).
  - **Replatform** (*Lift, Tinker & Shift*): Minor optimization to managed service ([`Amazon RDS`](./AWS_SERVICES_GLOSSARY.md#amazon-rds), `Elastic Beanstalk`).
  - **Repurchase** (*Drop-and-Shop*): Move to commercial `SaaS` ([`AWS Marketplace`](./AWS_SERVICES_GLOSSARY.md#aws-marketplace)).
  - **Refactor / Rearchitect:** Rewrite cloud-native/serverless (`Lambda`, `DynamoDB`); slowest, highest long-term benefit.
  - **Relocate:** Hypervisor-level VM lift (`VMware Cloud on AWS`).
  - **Retain:** Keep on-premises for now.
  - **Retire:** Decommission unused apps (instant savings).
- **3 MAP Phases:** `Assess` (`Migration Evaluator`, `Application Discovery Service`) → `Mobilize` (`Control Tower` Landing Zone) → `Migrate & Modernize` (`MGN`, `DMS`, `Migration Hub`).
- **Scalability vs Elasticity:** `Scalability` = ability to grow (`Vertical` bigger server / `Horizontal` more servers) • `Elasticity` = auto scale **out AND in** with demand.
- **HA vs Fault Tolerance:** `HA` = minimal downtime (Multi-AZ) • `Fault Tolerance` = zero downtime.
- **DR Metrics:** `RTO` = max acceptable downtime • `RPO` = max acceptable data loss (time).
- **4 DR Tiers (cheapest/slowest → costliest/fastest):** `Backup & Restore` → `Pilot Light` → `Warm Standby` → `Multi-Site Active-Active`.

---

## 2️⃣ Domain 2: Security & Compliance (`30%`)

### Shared Responsibility Model
- **AWS (`Security OF the Cloud`):** Physical data center security, hardware, global network, hypervisor, host OS, and OS patching for managed services (`RDS`, `Lambda`, `S3`).
- **Customer (`Security IN the Cloud`):** Customer data, encryption (at rest & in transit), `IAM`, `Security Groups` / `NACLs`, and **Guest OS patching on `EC2`**.
- **Shared Controls:** Patch Management, Configuration Management, Awareness & Training.

### Identity & Multi-Account Governance
- **IAM (Global & Free):**
  - **Root User:** Enable `MFA`, **never** use for daily tasks, **never** create access keys.
  - **IAM Users & Groups:** Users belong to Groups; Groups cannot be nested.
  - **IAM Policies:** `JSON` permissions; default = **Implicit Deny**; **Explicit Deny** always wins; enforce **Least Privilege**.
  - **IAM Roles:** Temporary credentials (`AWS STS`) attached to AWS services (e.g., `EC2` → `S3`) with no hardcoded keys.
  - **IAM Access Analyzer:** Identifies externally shared resources, detects unused access, generates least-privilege policies.
  - **IAM Identity Center (`AWS SSO`):** Centralized workforce Single Sign-On across multiple AWS accounts & business `SaaS` apps.
  - **[Amazon Cognito](./AWS_SERVICES_GLOSSARY.md#amazon-cognito):** Sign-up, sign-in, and social login (Google/Apple/Facebook) for **external web/mobile app users**.
- **Multi-Account:**
  - **[AWS Organizations](./AWS_SERVICES_GLOSSARY.md#aws-organizations):** Free central management via `OUs`, **Consolidated Billing** (volume discounts + RI/Savings Plans sharing), and **`SCPs`** (max permission guardrails).
  - **[AWS Control Tower](./AWS_SERVICES_GLOSSARY.md#aws-control-tower):** Easiest way to set up a secure, well-architected multi-account **Landing Zone** with guardrails.
  - **AWS RAM (Resource Access Manager):** Share AWS resources (`Subnets`, `Transit Gateway`) across accounts.

### Encryption, Secrets & Network Defense
- **[AWS KMS](./AWS_SERVICES_GLOSSARY.md#aws-kms):** Managed multi-tenant encryption keys across AWS services (`CloudTrail` integrated).
- **[AWS CloudHSM](./AWS_SERVICES_GLOSSARY.md#aws-cloudhsm):** Single-tenant **dedicated hardware** security module (`FIPS 140-2 Level 3`).
- **[AWS Certificate Manager](./AWS_SERVICES_GLOSSARY.md#aws-certificate-manager) (`ACM`):** Free provisioning & auto-renewal of public `SSL/TLS` certificates for `HTTPS`.
- **[AWS Secrets Manager](./AWS_SERVICES_GLOSSARY.md#aws-secrets-manager):** Stores DB credentials/API keys with **automatic rotation** (paid).
- **SSM Parameter Store:** Stores config data & simple secrets (Standard tier free, no built-in auto-rotation).
- **Security Groups:** `EC2 Instance` level • **`Allow` only** • **`Stateful`**.
- **Network ACLs (`NACLs`):** `Subnet` level • **`Allow` & `Deny`** (block specific IPs) • **`Stateless`**.
- **[AWS Shield](./AWS_SERVICES_GLOSSARY.md#aws-shield):** `DDoS` protection (L3/L4) — `Standard` (free, always on) • `Advanced` (paid, 24/7 `SRT`, DDoS cost protection).
- **[AWS WAF](./AWS_SERVICES_GLOSSARY.md#aws-waf):** Layer 7 HTTP/HTTPS firewall blocking **`SQL Injection`** and **`XSS`** (attaches to `CloudFront`, `ALB`, `API Gateway`).
- **[AWS Network Firewall](./AWS_SERVICES_GLOSSARY.md#aws-network-firewall):** Managed VPC-level stateful firewall (`IDS/IPS`).
- **[AWS Firewall Manager](./AWS_SERVICES_GLOSSARY.md#aws-firewall-manager):** Centrally manage `WAF`, `Shield`, and `Security Groups` across [`AWS Organizations`](./AWS_SERVICES_GLOSSARY.md#aws-organizations).

### Threat Detection & Compliance
- **[Amazon GuardDuty](./AWS_SERVICES_GLOSSARY.md#amazon-guardduty):** ML-powered **intelligent threat detection** (analyzes `CloudTrail`, `VPC Flow Logs`, `DNS Logs` for crypto-mining/compromise).
- **[Amazon Inspector](./AWS_SERVICES_GLOSSARY.md#amazon-inspector):** Automated **software vulnerability scanning (`CVEs`)** for `EC2`, `ECR`, and `Lambda`.
- **[Amazon Macie](./AWS_SERVICES_GLOSSARY.md#amazon-macie):** ML discovery of **sensitive data / `PII`** inside [`Amazon S3`](./AWS_SERVICES_GLOSSARY.md#amazon-s3) buckets.
- **[AWS Security Hub](./AWS_SERVICES_GLOSSARY.md#aws-security-hub):** Centralized security findings aggregator (`GuardDuty`, `Inspector`, `Macie`) + compliance standards (`CIS`, `PCI-DSS`).
- **[Amazon Detective](./AWS_SERVICES_GLOSSARY.md#amazon-detective):** Root cause investigation & security relationship graphs.
- **[AWS Artifact](./AWS_SERVICES_GLOSSARY.md#aws-artifact):** Free portal to download AWS compliance reports (`SOC 2`, `ISO 27001`, `PCI-DSS`) and manage agreements (`BAA`).
- **[AWS Audit Manager](./AWS_SERVICES_GLOSSARY.md#aws-audit-manager):** Continuously collects audit evidence to prepare for compliance audits.
- **[AWS CloudTrail](./AWS_SERVICES_GLOSSARY.md#aws-cloudtrail):** Logs **all API calls** ("Who did what, when, and from where?").

---

## 3️⃣ Domain 3: Cloud Technology & Services (`34%`)

### Compute
- **[Amazon EC2](./AWS_SERVICES_GLOSSARY.md#amazon-ec2) Families:** `T`/`M` (General) • `C` (Compute) • `R`/`X` (Memory) • `I`/`D` (Storage) • `P`/`G` (GPU/Accelerated).
- **EC2 Pricing Models:**
  - `On-Demand`: Pay per second/hour, no commitment, short/unpredictable workloads.
  - `Savings Plans`: 1 or 3-yr $/hr commitment, up to **72% off**, flexible across `EC2`, `Fargate`, `Lambda`.
  - `Reserved Instances (RI)`: 1 or 3-yr instance commitment, up to **72% off**, steady-state workloads.
  - `Spot Instances`: Up to **90% off**, 2-min interruption notice; fault-tolerant/stateless/batch only (**never** DBs).
  - `Dedicated Hosts`: Physical server for `BYOL` (per-socket/core) or strict compliance.
- **ELB:** `ALB` (Layer 7 HTTP/HTTPS, path/host routing) • `NLB` (Layer 4 TCP/UDP, ultra-low latency, static IP) • `GWLB` (3P security appliances).
- **EC2 Auto Scaling:** Auto scale out/in based on demand/metrics (`High Availability` + `Elasticity`).
- **[AWS Lambda](./AWS_SERVICES_GLOSSARY.md#aws-lambda):** `Serverless`, event-driven code, pay per ms/request, **15-min max** per execution.
- **Containers:** [`Amazon ECS`](./AWS_SERVICES_GLOSSARY.md#amazon-ecs) (AWS-native) • [`Amazon EKS`](./AWS_SERVICES_GLOSSARY.md#amazon-eks) (Kubernetes) • [`Amazon ECR`](./AWS_SERVICES_GLOSSARY.md#amazon-ecr) (container image registry) • **[`AWS Fargate`](./AWS_SERVICES_GLOSSARY.md#aws-fargate)** (Serverless containers — zero EC2 management).
- **[AWS Elastic Beanstalk](./AWS_SERVICES_GLOSSARY.md#aws-elastic-beanstalk) (`PaaS`):** Upload code; AWS provisions `EC2`, `ELB`, `Auto Scaling` (service free, pay for resources).
- **[Amazon Lightsail](./AWS_SERVICES_GLOSSARY.md#amazon-lightsail):** Simple fixed monthly pricing for small apps/WordPress.

### Storage
- **[Amazon S3](./AWS_SERVICES_GLOSSARY.md#amazon-s3) (`Object Storage`):** Unlimited scale, max `5 TB`/object, globally unique bucket names, **`11 9s` (`99.999999999%`) durability**, `Versioning`, `Lifecycle Policies`, static website hosting.
- **S3 Storage Classes:**
  - `Standard` (frequent) • `Intelligent-Tiering` (**unknown/changing access patterns**) • `Standard-IA` (infrequent, instant) • `One Zone-IA` (1 AZ, 20% cheaper, re-creatable data).
  - `Glacier Instant Retrieval` (quarterly archive, ms) • `Glacier Flexible Retrieval` (mins–hours) • `Glacier Deep Archive` (**cheapest**, 12–48 hrs).
- **[Amazon EBS](./AWS_SERVICES_GLOSSARY.md#amazon-ebs) (`Block`):** Persistent network disk for **1 `EC2`** in **1 `AZ`**; survives Stop; `EBS Snapshots` stored in `S3`.
- **EC2 Instance Store:** Ephemeral high-IOPS local disk; **data lost on Stop/Terminate**.
- **[Amazon EFS](./AWS_SERVICES_GLOSSARY.md#amazon-efs) (`File`):** Managed Linux **`NFS`** shared across multiple `EC2` instances & multiple `AZs`, auto-scales.
- **[Amazon FSx](./AWS_SERVICES_GLOSSARY.md#amazon-fsx) (`File`):** Managed **`Windows File Server (SMB)`** with AD integration, or `Lustre` (`HPC`).
- **[AWS Storage Gateway](./AWS_SERVICES_GLOSSARY.md#aws-storage-gateway):** Hybrid bridge connecting on-premises storage to AWS Cloud (`S3`).
- **[AWS Backup](./AWS_SERVICES_GLOSSARY.md#aws-backup):** Centralized automated backups across `EBS`, `RDS`, `DynamoDB`, `EFS`, `S3`.

### Databases
- **[Amazon RDS](./AWS_SERVICES_GLOSSARY.md#amazon-rds) (`SQL`):** Managed `MySQL`, `PostgreSQL`, `MariaDB`, `Oracle`, `SQL Server`, `Db2`.
  - **`Multi-AZ`:** Synchronous standby in another AZ for **HA / Auto Failover** (cannot read from it).
  - **`Read Replicas`:** Async copies for **Read Scaling / Performance**.
- **[Amazon Aurora](./AWS_SERVICES_GLOSSARY.md#amazon-aurora) (`SQL`):** Cloud-native (`MySQL`/`PostgreSQL`), 5x/3x faster, 6 copies across 3 AZs, auto-scales to `128 TB`.
- **[Amazon DynamoDB](./AWS_SERVICES_GLOSSARY.md#amazon-dynamodb) (`NoSQL`):** Serverless Key-Value, single-digit ms latency, `Global Tables` • **`DAX`** = in-memory cache (microseconds).
- **[Amazon ElastiCache](./AWS_SERVICES_GLOSSARY.md#amazon-elasticache):** Managed `Redis` / `Memcached` in-memory caching (`sub-ms` reads).
- **[Amazon Redshift](./AWS_SERVICES_GLOSSARY.md#amazon-redshift):** Petabyte-scale **Data Warehouse (`OLAP` / BI analytics)**.
- **[Amazon DocumentDB](./AWS_SERVICES_GLOSSARY.md#amazon-documentdb):** Managed `MongoDB`-compatible document DB.
- **[Amazon Neptune](./AWS_SERVICES_GLOSSARY.md#amazon-neptune):** Managed **Graph Database** (social networks, fraud detection, recommendations).
- **[Amazon MemoryDB](./AWS_SERVICES_GLOSSARY.md#amazon-memorydb):** Durable Redis-compatible in-memory primary DB.
- **[AWS DMS](./AWS_SERVICES_GLOSSARY.md#aws-dms):** Near-zero downtime database migration (`On-Premises` → AWS; supports heterogeneous migrations with `AWS SCT`).

### Networking & Content Delivery
- **[Amazon VPC](./AWS_SERVICES_GLOSSARY.md#amazon-vpc):** Isolated virtual network (`Public Subnet` → `IGW` • `Private Subnet` → no direct internet).
- **NAT Gateway:** Placed in `Public Subnet`; allows `Private Subnet` instances **outbound-only** internet access (updates).
- **VPC Peering:** 1-to-1 private link between 2 VPCs (non-transitive).
- **[AWS Transit Gateway](./AWS_SERVICES_GLOSSARY.md#aws-transit-gateway):** Central hub-and-spoke router connecting **hundreds of VPCs + on-prem**.
- **VPC Endpoints:** Private VPC-to-AWS traffic without public internet:
  - **`Gateway Endpoint`:** Free (`Route Table`) — **`S3` & `DynamoDB` ONLY**.
  - **`Interface Endpoint` ([`AWS PrivateLink`](./AWS_SERVICES_GLOSSARY.md#aws-privatelink)):** `ENI` with Private IP — most other AWS services.
- **[Amazon Route 53](./AWS_SERVICES_GLOSSARY.md#amazon-route-53):** Global `DNS` (port 53), domain registration, health checks, routing policies (`Latency`, `Geolocation`, `Failover`, `Weighted`).
- **[Amazon CloudFront](./AWS_SERVICES_GLOSSARY.md#amazon-cloudfront) (`CDN`):** Caches static/dynamic `HTTP/HTTPS` content at Edge Locations globally.
- **[AWS Global Accelerator](./AWS_SERVICES_GLOSSARY.md#aws-global-accelerator):** Routes `TCP/UDP` traffic over AWS Global Network using **2 Static Anycast IPs** (gaming, VoIP, IoT).
- **Site-to-Site VPN:** Quick, low-cost encrypted `IPsec` tunnel over **public internet**.
- **[AWS Direct Connect](./AWS_SERVICES_GLOSSARY.md#aws-direct-connect) (`DX`):** Dedicated private **physical fiber** (weeks to set up, consistent low latency, high bandwidth).

### Integration, Observability, DevOps, Migration, Analytics, AI/ML & EUC
- **Integration:** `SQS` (decoupling message queue — Pull; `Standard` vs `FIFO`) • `SNS` (`Pub/Sub` push notifications — Email/SMS/Fan-out) • `EventBridge` (serverless event bus & SaaS events/cron) • `Step Functions` (visual workflow orchestration) • `API Gateway` (serverless REST/HTTP/WebSocket front door).
- **Monitoring Trio:** `CloudWatch` (Metrics, Logs, Alarms — *performance*) • `CloudTrail` (API calls — *who did what*) • [`AWS Config`](./AWS_SERVICES_GLOSSARY.md#aws-config) (configuration history & compliance rules).
- **Management & IaC:** `Trusted Advisor` (5 checks: Cost, Performance, Security, Fault Tolerance, Service Quotas) • `Systems Manager (SSM)` (`Patch Manager`, `Session Manager` no-SSH access, `Parameter Store`) • `CloudFormation` (`YAML`/`JSON` IaC) • [`AWS CDK`](./AWS_SERVICES_GLOSSARY.md#aws-cdk) (IaC in Python/TS/Java) • `CodeBuild`/`CodeDeploy`/`CodePipeline` (`CI/CD`).
- **Developer & Mobile:** [`AWS Amplify`](./AWS_SERVICES_GLOSSARY.md#aws-amplify) (full-stack web/mobile hosting & CI/CD) • [`AWS Device Farm`](./AWS_SERVICES_GLOSSARY.md#aws-device-farm) (test apps on **real physical devices**) • [`AWS AppSync`](./AWS_SERVICES_GLOSSARY.md#aws-appsync) (serverless `GraphQL` with real-time & offline sync).
- **Migration Tools:** `Snowcone` (8–14 TB) • `Snowball Edge` (80–210 TB + edge compute) • `DataSync` (fast online file transfer) • `AWS MGN` (Lift-and-Shift servers) • `Migration Hub` (central tracking).
- **Analytics:** `Athena` (serverless `SQL` directly on `S3`) • `Glue` (serverless `ETL`) • `EMR` (`Spark`/`Hadoop` big data) • `Kinesis` (real-time streaming data) • `QuickSight` (`BI` dashboards) • `OpenSearch` (search & log analytics).
- **AI / ML:** `Bedrock` (serverless GenAI / Foundation Models) • `SageMaker` (build/train/deploy custom ML) • `Rekognition` (images/video) • `Textract` (OCR text/tables from PDFs) • `Comprehend` (`NLP` / sentiment analysis) • `Polly` (Text-to-Speech) • `Transcribe` (Speech-to-Text) • `Translate` (language translation) • `Lex` (chatbots / Alexa tech) • `Kendra` (enterprise AI search) • `Personalize` (product recommendations).
- **End-User Computing & Business Apps:** `AppStream 2.0` (stream desktop apps to any browser) • `WorkSpaces` (persistent cloud virtual desktops) • [`Amazon Connect`](./AWS_SERVICES_GLOSSARY.md#amazon-connect) (cloud contact center) • `SES` (bulk transactional email) • `Pinpoint` (omnichannel marketing engagement).

---

## 4️⃣ Domain 4: Billing, Pricing & Support (`12%`)

### Pricing & Free Tier
- **3 Pricing Principles:** Pay-as-you-go • Save when you reserve (`Savings Plans`/`RI`) • Pay less by using more (volume discounts).
- **3 Cost Drivers:** Compute • Storage • **Outbound Data Transfer** (`Data Transfer IN` = **FREE**; `Data Transfer OUT` = **PAID**).
- **Free Tier:** `Always Free` (Lambda 1M reqs, DynamoDB 25 GB, SQS 1M) • `12 Months Free` (EC2 750 hrs, S3 5 GB, RDS 750 hrs) • `Short-Term Trials` (SageMaker, Redshift, GuardDuty).

### Billing & Cost Management Tools
- **[AWS Pricing Calculator](./AWS_SERVICES_GLOSSARY.md#aws-pricing-calculator):** Estimate monthly cost **before** deploying.
- **[AWS Budgets](./AWS_SERVICES_GLOSSARY.md#aws-budgets):** Set custom spend/usage thresholds & trigger **alerts** (or automated actions).
- **[AWS Cost Explorer](./AWS_SERVICES_GLOSSARY.md#aws-cost-explorer):** Visualize historical spend (13 months) & **forecast** future spend (12 months).
- **AWS Cost & Usage Report (`CUR`):** Most detailed/granular hourly billing file stored in `S3`.
- **Cost Allocation Tags:** Track costs by department, project, or environment.
- **[AWS Compute Optimizer](./AWS_SERVICES_GLOSSARY.md#aws-compute-optimizer):** ML-powered **rightsizing** recommendations (`EC2`, `EBS`, `Lambda`, `ECS`).
- **[AWS Cost Anomaly Detection](./AWS_SERVICES_GLOSSARY.md#aws-cost-anomaly-detection):** ML detection of unusual spend spikes.
- **Consolidated Billing (`Organizations`):** Single bill across accounts + combined volume discounts + shared RIs/Savings Plans.

### AWS Support Plans, Health & Marketplace
- **Basic (`$0`):** Billing/account support only (no tech support), [`AWS Health Dashboard`](./AWS_SERVICES_GLOSSARY.md#aws-health-dashboard), **7 Core** `Trusted Advisor` checks.
- **Developer (`$29+/mo`):** Email tech support during business hours (`12–24 hr` SLA), 1 contact.
- **Business (`$100+/mo`):** **Lowest-cost plan with 24/7 tech support**, **`1 hr` SLA** (Production Down), **Full `Trusted Advisor` checks**, `Support API`, 3P software support.
- **Enterprise On-Ramp (`$5,500+/mo`):** **`30 min` SLA** (Business-Critical Down), **Pool of TAMs**, `Concierge Support`.
- **Enterprise (`$15,000+/mo`):** **`15 min` SLA** (Business-Critical Down), **Designated `TAM`**, `Concierge Support`, free `Infrastructure Event Management (IEM)`.
- **[AWS Health Dashboard](./AWS_SERVICES_GLOSSARY.md#aws-health-dashboard):** `Service Health` (public global AWS status) vs **`Account Health`** (personalized alerts for outages/maintenance impacting *your* resources).
- **[AWS Marketplace](./AWS_SERVICES_GLOSSARY.md#aws-marketplace):** Digital catalog to buy/deploy 3rd-party software billed on your AWS invoice.
- **AWS Partner Network (`APN`):** `Consulting Partners` (design/build/migrate workloads) & `Technology Partners` (software/tools) • `AWS Professional Services` (AWS's own advisory team).

---

## ⚡ 30-Second Rapid Distinctions (`X vs Y`)
- `Security Groups` (Instance, Allow-only, Stateful) **vs** `NACLs` (Subnet, Allow+Deny, Stateless).
- `Shield` (DDoS L3/L4) **vs** `WAF` (SQLi/XSS L7).
- `GuardDuty` (ML Threat Detection) **vs** `Inspector` (CVE Vulnerabilities) **vs** `Macie` (`PII` in `S3`).
- `CloudWatch` (Performance/Alarms) **vs** `CloudTrail` (API Audit — Who?) **vs** `Config` (Config History/Compliance).
- `IAM Identity Center` (Workforce SSO across AWS/SaaS) **vs** `Cognito` (External web/mobile app customers).
- `Secrets Manager` (Auto-rotation, paid) **vs** `Parameter Store` (Config/secrets, free Standard tier).
- `KMS` (Multi-tenant managed) **vs** `CloudHSM` (Single-tenant dedicated hardware).
- `S3` (Object, unlimited) **vs** `EBS` (Block, 1 EC2/1 AZ) **vs** `EFS` (Linux NFS, Multi-AZ shared).
- `EBS` (Persistent) **vs** `Instance Store` (Ephemeral — lost on Stop).
- `RDS Multi-AZ` (HA/Failover, no reads) **vs** `Read Replicas` (Read scaling/Performance).
- `CloudFront` (HTTP/HTTPS caching CDN) **vs** `Global Accelerator` (TCP/UDP, 2 Static Anycast IPs).
- `VPN` (Quick, public internet) **vs** `Direct Connect` (Private physical fiber, consistent low latency).
- `SQS` (Queue/Decoupling — Pull) **vs** `SNS` (Pub/Sub Notifications — Push).
- `AppStream 2.0` (Browser desktop app streaming) **vs** `WorkSpaces` (Full persistent virtual desktop).
- `Budgets` (Alerts on spend thresholds) **vs** `Cost Explorer` (Charts & 12-month forecast).
