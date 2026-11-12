# AWS Certified Cloud Practitioner (CLF-C02) - Practice Exam 1 (87 Questions)

Source: [Quban301/Certification-Practice](https://github.com/Quban301/Certification-Practice)

Modular practice paper covering Compute, Storage, Networking, DevOps, AI/ML, and Billing.

Total Questions: **87**

## 📑 Quick Table of Contents

- [Question 1](#q-1): `Module 5 · Compute, Storage & Databases` - An EC2 instance is named m5.large. What does the letter 'm' indicate?... *(Ans: B)*
- [Question 2](#q-2): `Module 5 · Compute, Storage & Databases` - A workload does sustained, consistently heavy CPU processing (media tr... *(Ans: B)*
- [Question 3](#q-3): `Module 5 · Compute, Storage & Databases` - An in-memory database such as Redis or SAP HANA needs a large amount o... *(Ans: C)*
- [Question 4](#q-4): `Module 5 · Compute, Storage & Databases` - A small web app is mostly idle but occasionally spikes. Which EC2 fami... *(Ans: A)*
- [Question 5](#q-5): `Module 5 · Compute, Storage & Databases` - How do burstable (T family) instances handle CPU above their baseline?... *(Ans: B)*
- [Question 6](#q-6): `Module 5 · Compute, Storage & Databases` - Which storage option provides the highest IOPS and lowest latency but ... *(Ans: B)*
- [Question 7](#q-7): `Module 5 · Compute, Storage & Databases` - A single EC2 instance needs a persistent boot volume that survives reb... *(Ans: B)*
- [Question 8](#q-8): `Module 5 · Compute, Storage & Databases` - Thousands of EC2 instances across multiple Availability Zones must rea... *(Ans: C)*
- [Question 9](#q-9): `Module 5 · Compute, Storage & Databases` - Which statement about Amazon S3 durability is correct?... *(Ans: B)*
- [Question 10](#q-10): `Module 5 · Compute, Storage & Databases` - Data is temporary, already replicated elsewhere, and needs the absolut... *(Ans: A)*
- [Question 11](#q-11): `Module 5 · Compute, Storage & Databases` - Which S3 storage class automatically moves objects between access tier... *(Ans: B)*
- [Question 12](#q-12): `Module 5 · Compute, Storage & Databases` - Archived data is rarely accessed (e.g. quarterly) but must still be re... *(Ans: B)*
- [Question 13](#q-13): `Module 5 · Compute, Storage & Databases` - Which S3 storage class is the cheapest and is designed for 7–10+ year ... *(Ans: C)*
- [Question 14](#q-14): `Module 5 · Compute, Storage & Databases` - What do S3 Lifecycle policies let you do without writing any applicati... *(Ans: B)*
- [Question 15](#q-15): `Module 5 · Compute, Storage & Databases` - Which AWS database service is a relational engine supporting MySQL, Po... *(Ans: B)*
- [Question 16](#q-16): `Module 5 · Compute, Storage & Databases` - A workload needs massive, key-based throughput with single-digit-milli... *(Ans: C)*
- [Question 17](#q-17): `Module 5 · Compute, Storage & Databases` - Analysts need to run complex analytical queries across years of histor... *(Ans: B)*
- [Question 18](#q-18): `Module 5 · Compute, Storage & Databases` - You want to reduce load on a relational database by serving repeated r... *(Ans: B)*
- [Question 19](#q-19): `Module 5 · Compute, Storage & Databases` - Which is an advantage of Amazon Aurora over standard Amazon RDS?... *(Ans: B)*
- [Question 20](#q-20): `Module 5 · Compute, Storage & Databases` - Aurora stores how many copies of your data, and across how many Availa... *(Ans: B)*
- [Question 21](#q-21): `Module 5 · Compute, Storage & Databases` - A dev/test database has intermittent, spiky traffic and you want the m... *(Ans: A)*
- [Question 22](#q-22): `Module 5 · Compute, Storage & Databases` - Which Auto Scaling policy works like a thermostat — you set a metric t... *(Ans: B)*
- [Question 23](#q-23): `Module 5 · Compute, Storage & Databases` - You know traffic peaks every weekday at 9 a.m. and want to raise capac... *(Ans: C)*
- [Question 24](#q-24): `Module 5 · Compute, Storage & Databases` - What is the canonical AWS answer for elastic, self-healing, highly ava... *(Ans: B)*
- [Question 25](#q-25): `Module 6 · Integration & DevOps` - What problem does Amazon SQS primarily solve?... *(Ans: B)*
- [Question 26](#q-26): `Module 6 · Integration & DevOps` - A banking workload must process messages exactly once and in strict or... *(Ans: B)*
- [Question 27](#q-27): `Module 6 · Integration & DevOps` - A Standard SQS queue offers which delivery and ordering guarantees?... *(Ans: B)*
- [Question 28](#q-28): `Module 6 · Integration & DevOps` - A malformed 'poison pill' message keeps failing and blocking an SQS qu... *(Ans: B)*
- [Question 29](#q-29): `Module 6 · Integration & DevOps` - What is the SQS visibility timeout?... *(Ans: B)*
- [Question 30](#q-30): `Module 6 · Integration & DevOps` - One 'order placed' event must be delivered simultaneously to a fulfilm... *(Ans: B)*
- [Question 31](#q-31): `Module 6 · Integration & DevOps` - You need to route events to different targets based on the content of ... *(Ans: C)*
- [Question 32](#q-32): `Module 6 · Integration & DevOps` - Which messaging service is pull-based (consumers retrieve messages) ra... *(Ans: B)*
- [Question 33](#q-33): `Module 6 · Integration & DevOps` - In an AWS CI/CD pipeline, which service compiles code, runs tests and ... *(Ans: B)*
- [Question 34](#q-34): `Module 6 · Integration & DevOps` - Which service automates deployments to EC2, Lambda or ECS using in-pla... *(Ans: C)*
- [Question 35](#q-35): `Module 6 · Integration & DevOps` - Which service orchestrates the overall CI/CD workflow (Source → Build ... *(Ans: C)*
- [Question 36](#q-36): `Module 6 · Integration & DevOps` - Which AWS-native, declarative Infrastructure-as-Code service uses JSON... *(Ans: C)*
- [Question 37](#q-37): `Module 6 · Integration & DevOps` - A team wants to define infrastructure using real programming languages... *(Ans: B)*
- [Question 38](#q-38): `Module 6 · Integration & DevOps` - Which IaC tool is third-party, cloud-agnostic, uses HCL, and maintains... *(Ans: C)*
- [Question 39](#q-39): `Module 6 · Integration & DevOps` - Which CloudWatch feature scans centralised logs for a pattern (e.g. 'E... *(Ans: B)*
- [Question 40](#q-40): `Module 6 · Integration & DevOps` - What is the CloudWatch automation chain that lets a system react to pr... *(Ans: B)*
- [Question 41](#q-41): `Module 6 · Integration & DevOps` - You must give administrators shell access to EC2 instances without ope... *(Ans: B)*
- [Question 42](#q-42): `Module 6 · Integration & DevOps` - Which Systems Manager capability provides secure, hierarchical storage... *(Ans: B)*
- [Question 43](#q-43): `Module 6 · Integration & DevOps` - Which Systems Manager capability automates OS/application patching aga... *(Ans: C)*
- [Question 44](#q-44): `Module 6 · Integration & DevOps` - A multi-step workflow needs sequencing, automatic retries with backoff... *(Ans: B)*
- [Question 45](#q-45): `Module 6 · Integration & DevOps` - Which scenario is best served by a single plain Lambda function rather... *(Ans: B)*
- [Question 46](#q-46): `Module 7 · AI/ML, Analytics & Migration` - Which AWS AI service analyses images and video for objects, faces, sce... *(Ans: B)*
- [Question 47](#q-47): `Module 7 · AI/ML, Analytics & Migration` - You need to extract text, forms and tables (key-value pairs) from scan... *(Ans: B)*
- [Question 48](#q-48): `Module 7 · AI/ML, Analytics & Migration` - Which service performs NLP tasks such as sentiment analysis, entity an... *(Ans: A)*
- [Question 49](#q-49): `Module 7 · AI/ML, Analytics & Migration` - Which service converts written text into lifelike speech (text-to-spee... *(Ans: B)*
- [Question 50](#q-50): `Module 7 · AI/ML, Analytics & Migration` - Which service produces speech-to-text transcripts with timestamps and ... *(Ans: B)*
- [Question 51](#q-51): `Module 7 · AI/ML, Analytics & Migration` - Which service is used to build the conversation flow of a voice/text c... *(Ans: A)*
- [Question 52](#q-52): `Module 7 · AI/ML, Analytics & Migration` - Which service gives real-time product recommendations on an e-commerce... *(Ans: B)*
- [Question 53](#q-53): `Module 7 · AI/ML, Analytics & Migration` - A company wants to detect fraud patterns unique to its own historical ... *(Ans: B)*
- [Question 54](#q-54): `Module 7 · AI/ML, Analytics & Migration` - In SageMaker, what do you pay for during model training?... *(Ans: B)*
- [Question 55](#q-55): `Module 7 · AI/ML, Analytics & Migration` - A team with no data scientists wants to build a custom model from tabu... *(Ans: A)*
- [Question 56](#q-56): `Module 7 · AI/ML, Analytics & Migration` - A custom, low-latency application must process each streaming record a... *(Ans: B)*
- [Question 57](#q-57): `Module 7 · AI/ML, Analytics & Migration` - You need a fully managed 'fire-and-forget' pipeline to load streaming ... *(Ans: B)*
- [Question 58](#q-58): `Module 7 · AI/ML, Analytics & Migration` - In a data lake, which service crawls raw S3 data to populate a catalog... *(Ans: B)*
- [Question 59](#q-59): `Module 7 · AI/ML, Analytics & Migration` - Which service runs serverless standard SQL directly against data in S3... *(Ans: B)*
- [Question 60](#q-60): `Module 7 · AI/ML, Analytics & Migration` - Which service provides no-code BI dashboards and reports for business ... *(Ans: B)*
- [Question 61](#q-61): `Module 7 · AI/ML, Analytics & Migration` - Analytics differ mainly by where the data lives. Which fits 'data stay... *(Ans: B)*
- [Question 62](#q-62): `Module 7 · AI/ML, Analytics & Migration` - A large-scale big-data job needs specific open-source frameworks (Spar... *(Ans: B)*
- [Question 63](#q-63): `Module 7 · AI/ML, Analytics & Migration` - Which migration service performs a lift-and-shift 'rehost' by continuo... *(Ans: B)*
- [Question 64](#q-64): `Module 7 · AI/ML, Analytics & Migration` - Which service migrates databases with a full load plus Change Data Cap... *(Ans: B)*
- [Question 65](#q-65): `Module 7 · AI/ML, Analytics & Migration` - You are moving from Oracle to PostgreSQL (a heterogeneous migration). ... *(Ans: A)*
- [Question 66](#q-66): `Module 7 · AI/ML, Analytics & Migration` - A petabyte-scale dataset must reach AWS but the network would take wee... *(Ans: B)*
- [Question 67](#q-67): `Module 7 · AI/ML, Analytics & Migration` - Which service provides automated, online transfer between on-prem NFS/... *(Ans: A)*
- [Question 68](#q-68): `Module 8 · Billing, Pricing & Support` - Which AWS Support plan is free and included with every account?... *(Ans: A)*
- [Question 69](#q-69): `Module 8 · Billing, Pricing & Support` - At which support plan do the FULL set of Trusted Advisor checks (all f... *(Ans: C)*
- [Question 70](#q-70): `Module 8 · Billing, Pricing & Support` - A mission-critical workload needs a dedicated Technical Account Manage... *(Ans: C)*
- [Question 71](#q-71): `Module 8 · Billing, Pricing & Support` - A small team needs business-hours email guidance from Cloud Support As... *(Ans: B)*
- [Question 72](#q-72): `Module 8 · Billing, Pricing & Support` - Which AWS tool is used to VISUALISE and investigate spend and usage ov... *(Ans: B)*
- [Question 73](#q-73): `Module 8 · Billing, Pricing & Support` - Which tool lets you set a cost or usage threshold and get alerted (or ... *(Ans: B)*
- [Question 74](#q-74): `Module 8 · Billing, Pricing & Support` - Which feature uses machine learning to automatically flag unusual spen... *(Ans: A)*
- [Question 75](#q-75): `Module 8 · Billing, Pricing & Support` - Which compute pricing model offers the deepest discount (up to ~90%) b... *(Ans: D)*
- [Question 76](#q-76): `Module 8 · Billing, Pricing & Support` - A steady workload needs discounts that stay flexible across instance f... *(Ans: B)*
- [Question 77](#q-77): `Module 8 · Billing, Pricing & Support` - Which pricing model is the flexible baseline with no commitment and th... *(Ans: A)*
- [Question 78](#q-78): `Module 8 · Billing, Pricing & Support` - Reserved Instances require what kind of commitment?... *(Ans: B)*
- [Question 79](#q-79): `Module 8 · Billing, Pricing & Support` - Which free tool (no AWS account needed) lets you build a cost estimate... *(Ans: B)*
- [Question 80](#q-80): `Module 8 · Billing, Pricing & Support` - A parent company wants ONE invoice covering all its subsidiary account... *(Ans: B)*
- [Question 81](#q-81): `Module 8 · Billing, Pricing & Support` - Under consolidated billing, how do Reserved Instance and Savings Plans... *(Ans: B)*
- [Question 82](#q-82): `Module 8 · Billing, Pricing & Support` - Activating which feature lets you break down spend by team or project ... *(Ans: A)*
- [Question 83](#q-83): `Module 8 · Billing, Pricing & Support` - Which Trusted Advisor category flags idle/underutilised EC2 instances ... *(Ans: C)*
- [Question 84](#q-84): `Module 8 · Billing, Pricing & Support` - Which Trusted Advisor category checks open security-group ports, root-... *(Ans: A)*
- [Question 85](#q-85): `Module 8 · Billing, Pricing & Support` - Which of these are the five Trusted Advisor check categories? (Choose ... *(Ans: A)*
- [Question 86](#q-86): `Module 8 · Billing, Pricing & Support` - When several answers technically work on CLF-C02, which framework is t... *(Ans: B)*
- [Question 87](#q-87): `Module 8 · Billing, Pricing & Support` - On the exam, qualifying phrases like 'LEAST operational overhead' or '... *(Ans: B)*

---

<a id="q-1"></a>

### Question 1

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-001`

> **Scenario:**  
> An EC2 instance is named m5.large. What does the letter 'm' indicate?

#### Options
- **A.** The generation
- **B.** The instance family **[CORRECT]**
- **C.** The size
- **D.** The Region

**Correct Answer:** `B`

#### Explanation & Rationale

In m5.large, 'm' is the family (general purpose), '5' is the generation, and 'large' is the size.

---

<a id="q-2"></a>

### Question 2

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-002`

> **Scenario:**  
> A workload does sustained, consistently heavy CPU processing (media transcoding). Which EC2 instance family fits best?

#### Options
- **A.** T family (burstable)
- **B.** C family (compute optimised) **[CORRECT]**
- **C.** R family (memory optimised)
- **D.** I family (storage optimised)

**Correct Answer:** `B`

#### Explanation & Rationale

Sustained high CPU maps to the Compute-optimised C family; the T family is for bursty, mostly-idle workloads.

---

<a id="q-3"></a>

### Question 3

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-003`

> **Scenario:**  
> An in-memory database such as Redis or SAP HANA needs a large amount of RAM per vCPU. Which instance family is designed for this?

#### Options
- **A.** General purpose (M)
- **B.** Compute optimised (C)
- **C.** Memory optimised (R, X, z1d) **[CORRECT]**
- **D.** Accelerated (P, G)

**Correct Answer:** `C`

#### Explanation & Rationale

Memory-optimised families (R, X, z1d) offer a high memory-to-CPU ratio for large caches and in-memory databases.

---

<a id="q-4"></a>

### Question 4

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-004`

> **Scenario:**  
> A small web app is mostly idle but occasionally spikes. Which EC2 family is the most cost-effective match?

#### Options
- **A.** T family (burstable) **[CORRECT]**
- **B.** C family
- **C.** R family
- **D.** P family

**Correct Answer:** `A`

#### Explanation & Rationale

T-family burstable instances earn CPU credits while idle and spend them to burst — ideal for unpredictable spikes with low average utilisation.

---

<a id="q-5"></a>

### Question 5

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-005`

> **Scenario:**  
> How do burstable (T family) instances handle CPU above their baseline?

#### Options
- **A.** They throttle to zero
- **B.** They earn CPU credits while idle and spend them to burst **[CORRECT]**
- **C.** They automatically switch to a C instance
- **D.** They add more vCPUs permanently

**Correct Answer:** `B`

#### Explanation & Rationale

T instances accumulate CPU credits during idle periods and consume them to burst above baseline.

---

<a id="q-6"></a>

### Question 6

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-006`

> **Scenario:**  
> Which storage option provides the highest IOPS and lowest latency but loses its data when the instance stops or is terminated?

#### Options
- **A.** Amazon EBS
- **B.** Instance store **[CORRECT]**
- **C.** Amazon EFS
- **D.** Amazon S3

**Correct Answer:** `B`

#### Explanation & Rationale

Instance store is local NVMe on the host — fastest, but ephemeral: data is lost on stop/terminate (it survives a reboot).

---

<a id="q-7"></a>

### Question 7

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-007`

> **Scenario:**  
> A single EC2 instance needs a persistent boot volume that survives reboots and can be snapshotted. Which service is appropriate?

#### Options
- **A.** Instance store
- **B.** Amazon EBS **[CORRECT]**
- **C.** Amazon EFS
- **D.** Amazon S3

**Correct Answer:** `B`

#### Explanation & Rationale

EBS is network-attached block storage that persists independently of the instance and snapshots to S3.

---

<a id="q-8"></a>

### Question 8

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-008`

> **Scenario:**  
> Thousands of EC2 instances across multiple Availability Zones must read and write the same POSIX file system simultaneously. Which service fits?

#### Options
- **A.** Amazon EBS
- **B.** Instance store
- **C.** Amazon EFS **[CORRECT]**
- **D.** Amazon S3

**Correct Answer:** `C`

#### Explanation & Rationale

EFS is a managed shared file system mounted by many instances across AZs, scaling capacity automatically.

---

<a id="q-9"></a>

### Question 9

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-009`

> **Scenario:**  
> Which statement about Amazon S3 durability is correct?

#### Options
- **A.** It offers 99% durability in a single AZ
- **B.** It offers 11 nines of durability across multiple AZs **[CORRECT]**
- **C.** Durability depends on the instance type
- **D.** Objects are stored on a single disk

**Correct Answer:** `B`

#### Explanation & Rationale

S3 provides eleven 9s (99.999999999%) of durability by replicating objects across multiple AZs.

---

<a id="q-10"></a>

### Question 10

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-010`

> **Scenario:**  
> Data is temporary, already replicated elsewhere, and needs the absolute fastest I/O. Which storage type is the engineer's choice?

#### Options
- **A.** Instance store **[CORRECT]**
- **B.** EBS gp3
- **C.** EFS
- **D.** S3 Standard

**Correct Answer:** `A`

#### Explanation & Rationale

When data is disposable/replicated and needs maximum I/O, instance store is chosen despite being ephemeral.

---

<a id="q-11"></a>

### Question 11

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-011`

> **Scenario:**  
> Which S3 storage class automatically moves objects between access tiers as usage changes, with no operational effort?

#### Options
- **A.** S3 Standard
- **B.** S3 Intelligent-Tiering **[CORRECT]**
- **C.** S3 One Zone-IA
- **D.** S3 Glacier Deep Archive

**Correct Answer:** `B`

#### Explanation & Rationale

S3 Intelligent-Tiering auto-moves objects between tiers based on changing access patterns — ideal for unknown/changing patterns.

---

<a id="q-12"></a>

### Question 12

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-012`

> **Scenario:**  
> Archived data is rarely accessed (e.g. quarterly) but must still be retrievable in milliseconds when needed. Which class fits?

#### Options
- **A.** S3 Standard-IA
- **B.** S3 Glacier Instant Retrieval **[CORRECT]**
- **C.** S3 Glacier Flexible Retrieval
- **D.** S3 Glacier Deep Archive

**Correct Answer:** `B`

#### Explanation & Rationale

'Instantly/immediately' + 'rarely accessed' points to Glacier Instant Retrieval, which keeps millisecond retrieval.

---

<a id="q-13"></a>

### Question 13

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-013`

> **Scenario:**  
> Which S3 storage class is the cheapest and is designed for 7–10+ year compliance data with retrieval times up to 12 hours?

#### Options
- **A.** S3 Standard-IA
- **B.** S3 Glacier Flexible Retrieval
- **C.** S3 Glacier Deep Archive **[CORRECT]**
- **D.** S3 Intelligent-Tiering

**Correct Answer:** `C`

#### Explanation & Rationale

Glacier Deep Archive is the lowest-cost class, with retrieval up to ~12 hours — for long-term compliance archives.

---

<a id="q-14"></a>

### Question 14

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-014`

> **Scenario:**  
> What do S3 Lifecycle policies let you do without writing any application code?

#### Options
- **A.** Encrypt objects with customer keys
- **B.** Transition and expire objects automatically by age **[CORRECT]**
- **C.** Replicate a bucket to another account
- **D.** Serve objects through a CDN

**Correct Answer:** `B`

#### Explanation & Rationale

Lifecycle rules configured on a bucket/prefix transition objects between classes and expire them based on age — no code.

---

<a id="q-15"></a>

### Question 15

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-015`

> **Scenario:**  
> Which AWS database service is a relational engine supporting MySQL, PostgreSQL, MariaDB, SQL Server and Oracle?

#### Options
- **A.** Amazon DynamoDB
- **B.** Amazon RDS **[CORRECT]**
- **C.** Amazon Redshift
- **D.** Amazon ElastiCache

**Correct Answer:** `B`

#### Explanation & Rationale

Amazon RDS is the managed relational service supporting those five engines.

---

<a id="q-16"></a>

### Question 16

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-016`

> **Scenario:**  
> A workload needs massive, key-based throughput with single-digit-millisecond latency and virtually unlimited scale. Which database fits?

#### Options
- **A.** Amazon RDS
- **B.** Amazon Aurora
- **C.** Amazon DynamoDB **[CORRECT]**
- **D.** Amazon Redshift

**Correct Answer:** `C`

#### Explanation & Rationale

DynamoDB is a serverless NoSQL key-value/document store delivering single-digit-ms latency at any scale.

---

<a id="q-17"></a>

### Question 17

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-017`

> **Scenario:**  
> Analysts need to run complex analytical queries across years of historical data. Which purpose-built service is designed for this (OLAP)?

#### Options
- **A.** Amazon DynamoDB
- **B.** Amazon Redshift **[CORRECT]**
- **C.** Amazon ElastiCache
- **D.** Amazon RDS

**Correct Answer:** `B`

#### Explanation & Rationale

Redshift is a columnar data-warehouse (OLAP) service for complex analytics over large historical datasets.

---

<a id="q-18"></a>

### Question 18

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-018`

> **Scenario:**  
> You want to reduce load on a relational database by serving repeated reads from a sub-millisecond in-memory layer. Which service?

#### Options
- **A.** Amazon Redshift
- **B.** Amazon ElastiCache **[CORRECT]**
- **C.** Amazon Aurora
- **D.** Amazon S3

**Correct Answer:** `B`

#### Explanation & Rationale

ElastiCache (Redis/Memcached) provides a sub-millisecond caching layer that shields the primary database from repeated reads.

---

<a id="q-19"></a>

### Question 19

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-019`

> **Scenario:**  
> Which is an advantage of Amazon Aurora over standard Amazon RDS?

#### Options
- **A.** It supports Oracle and SQL Server
- **B.** Up to 15 read replicas with lower replication lag **[CORRECT]**
- **C.** It is the cheapest option for all workloads
- **D.** It requires no storage at all

**Correct Answer:** `B`

#### Explanation & Rationale

Aurora supports up to 15 read replicas (RDS: 5) with single-digit-ms replication lag and faster failover.

---

<a id="q-20"></a>

### Question 20

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-020`

> **Scenario:**  
> Aurora stores how many copies of your data, and across how many Availability Zones?

#### Options
- **A.** 3 copies across 2 AZs
- **B.** 6 copies across 3 AZs **[CORRECT]**
- **C.** 2 copies across 1 AZ
- **D.** 10 copies across 5 AZs

**Correct Answer:** `B`

#### Explanation & Rationale

Aurora's shared distributed storage layer keeps 6 copies of data across 3 Availability Zones.

---

<a id="q-21"></a>

### Question 21

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-021`

> **Scenario:**  
> A dev/test database has intermittent, spiky traffic and you want the most cost-effective option that scales capacity automatically. Which fits?

#### Options
- **A.** Aurora Serverless v2 **[CORRECT]**
- **B.** A large Redshift cluster
- **C.** Provisioned RDS with max instance size
- **D.** Instance store on EC2

**Correct Answer:** `A`

#### Explanation & Rationale

Aurora Serverless v2 scales capacity in fine-grained steps for intermittent/spiky loads — 'intermittent traffic, most cost-effective'.

---

<a id="q-22"></a>

### Question 22

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-022`

> **Scenario:**  
> Which Auto Scaling policy works like a thermostat — you set a metric target (e.g. 'keep average CPU at 50%') and the group holds it?

#### Options
- **A.** Step scaling
- **B.** Target tracking **[CORRECT]**
- **C.** Scheduled scaling
- **D.** Manual scaling

**Correct Answer:** `B`

#### Explanation & Rationale

Target tracking maintains a chosen metric at a target value; it is the most common ASG policy.

---

<a id="q-23"></a>

### Question 23

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-023`

> **Scenario:**  
> You know traffic peaks every weekday at 9 a.m. and want to raise capacity just before that time. Which scaling policy is best?

#### Options
- **A.** Target tracking
- **B.** Step scaling
- **C.** Scheduled scaling **[CORRECT]**
- **D.** Spot scaling

**Correct Answer:** `C`

#### Explanation & Rationale

Scheduled scaling changes capacity at known times, ahead of predictable peaks.

---

<a id="q-24"></a>

### Question 24

**Set:** `Standard` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-024`

> **Scenario:**  
> What is the canonical AWS answer for elastic, self-healing, highly available compute across multiple AZs?

#### Options
- **A.** A single large EC2 instance
- **B.** An Auto Scaling Group behind an Elastic Load Balancer **[CORRECT]**
- **C.** Instance store volumes
- **D.** A Redshift cluster

**Correct Answer:** `B`

#### Explanation & Rationale

ASG + Elastic Load Balancer across AZs gives elastic, self-healing, highly available compute.

---

<a id="q-25"></a>

### Question 25

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-025`

> **Scenario:**  
> What problem does Amazon SQS primarily solve?

#### Options
- **A.** It encrypts data at rest
- **B.** It decouples producers from consumers so a slow/failed consumer doesn't drag the producer down **[CORRECT]**
- **C.** It provides a relational database
- **D.** It runs container images

**Correct Answer:** `B`

#### Explanation & Rationale

SQS breaks tight coupling: producers send and move on; consumers process at their own pace; messages wait safely.

---

<a id="q-26"></a>

### Question 26

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-026`

> **Scenario:**  
> A banking workload must process messages exactly once and in strict order within a group. Which SQS queue type is required?

#### Options
- **A.** Standard queue
- **B.** FIFO queue **[CORRECT]**
- **C.** Dead-letter queue
- **D.** Priority queue

**Correct Answer:** `B`

#### Explanation & Rationale

FIFO queues give exactly-once processing and strict first-in-first-out ordering within a message group.

---

<a id="q-27"></a>

### Question 27

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-027`

> **Scenario:**  
> A Standard SQS queue offers which delivery and ordering guarantees?

#### Options
- **A.** Exactly-once, strict ordering
- **B.** At-least-once delivery, best-effort ordering **[CORRECT]**
- **C.** At-most-once, no duplicates
- **D.** Exactly-once, no ordering

**Correct Answer:** `B`

#### Explanation & Rationale

Standard queues provide at-least-once delivery with best-effort ordering and near-unlimited throughput — make processing idempotent.

---

<a id="q-28"></a>

### Question 28

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-028`

> **Scenario:**  
> A malformed 'poison pill' message keeps failing and blocking an SQS queue. What should you configure?

#### Options
- **A.** A larger visibility timeout only
- **B.** A dead-letter queue (DLQ) **[CORRECT]**
- **C.** A FIFO queue
- **D.** An SNS topic

**Correct Answer:** `B`

#### Explanation & Rationale

A DLQ receives messages that fail a defined number of times, moving them aside so healthy messages keep flowing.

---

<a id="q-29"></a>

### Question 29

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-029`

> **Scenario:**  
> What is the SQS visibility timeout?

#### Options
- **A.** The time a queue can hold a message before deletion
- **B.** The period a retrieved message is hidden from other consumers until deleted or it reappears **[CORRECT]**
- **C.** The maximum message size
- **D.** The delay before a message is first delivered

**Correct Answer:** `B`

#### Explanation & Rationale

When a consumer retrieves a message SQS hides it for a set period; if not deleted in time it reappears — enabling at-least-once delivery.

---

<a id="q-30"></a>

### Question 30

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-030`

> **Scenario:**  
> One 'order placed' event must be delivered simultaneously to a fulfilment queue, an analytics queue and an email Lambda, with the publisher unaware of them. Which service fits?

#### Options
- **A.** Amazon SQS
- **B.** Amazon SNS **[CORRECT]**
- **C.** AWS Step Functions
- **D.** Amazon RDS

**Correct Answer:** `B`

#### Explanation & Rationale

SNS is push-based pub/sub fan-out: one message to a topic is delivered to every subscriber.

---

<a id="q-31"></a>

### Question 31

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-031`

> **Scenario:**  
> You need to route events to different targets based on the content of the event payload (e.g. status = FAILED vs COMPLETED). Which service is designed for this?

#### Options
- **A.** Amazon SQS
- **B.** Amazon SNS
- **C.** Amazon EventBridge **[CORRECT]**
- **D.** Amazon EFS

**Correct Answer:** `C`

#### Explanation & Rationale

EventBridge does content-based routing on an event bus, plus scheduled (cron-like) rules and many AWS integrations.

---

<a id="q-32"></a>

### Question 32

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-032`

> **Scenario:**  
> Which messaging service is pull-based (consumers retrieve messages) rather than push-based?

#### Options
- **A.** Amazon SNS
- **B.** Amazon SQS **[CORRECT]**
- **C.** Amazon EventBridge
- **D.** Amazon Polly

**Correct Answer:** `B`

#### Explanation & Rationale

SQS is point-to-point and pull-based; SNS and EventBridge are push-based.

---

<a id="q-33"></a>

### Question 33

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-033`

> **Scenario:**  
> In an AWS CI/CD pipeline, which service compiles code, runs tests and produces deployable artifacts in temporary build environments?

#### Options
- **A.** CodeCommit
- **B.** CodeBuild **[CORRECT]**
- **C.** CodeDeploy
- **D.** CodePipeline

**Correct Answer:** `B`

#### Explanation & Rationale

CodeBuild builds/compiles/tests and outputs artifacts in auto-scaling, temporary environments — no build server to maintain.

---

<a id="q-34"></a>

### Question 34

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-034`

> **Scenario:**  
> Which service automates deployments to EC2, Lambda or ECS using in-place, blue/green and canary strategies?

#### Options
- **A.** CodeCommit
- **B.** CodeBuild
- **C.** CodeDeploy **[CORRECT]**
- **D.** CloudFormation

**Correct Answer:** `C`

#### Explanation & Rationale

CodeDeploy handles the deployment stage with in-place, blue/green and canary strategies.

---

<a id="q-35"></a>

### Question 35

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-035`

> **Scenario:**  
> Which service orchestrates the overall CI/CD workflow (Source → Build → Test → Deploy) and can add manual approval gates?

#### Options
- **A.** CodeBuild
- **B.** CodeDeploy
- **C.** CodePipeline **[CORRECT]**
- **D.** CodeCommit

**Correct Answer:** `C`

#### Explanation & Rationale

CodePipeline defines the stages, invokes the other tools in order, and adds approval gates.

---

<a id="q-36"></a>

### Question 36

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-036`

> **Scenario:**  
> Which AWS-native, declarative Infrastructure-as-Code service uses JSON/YAML templates and offers drift detection?

#### Options
- **A.** AWS CDK
- **B.** Terraform
- **C.** AWS CloudFormation **[CORRECT]**
- **D.** AWS CodeBuild

**Correct Answer:** `C`

#### Explanation & Rationale

CloudFormation is the AWS-native declarative IaC service; drift detection flags manual changes that diverge from the template.

---

<a id="q-37"></a>

### Question 37

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-037`

> **Scenario:**  
> A team wants to define infrastructure using real programming languages like Python or TypeScript, with loops and reusable constructs. Which tool fits?

#### Options
- **A.** AWS CloudFormation
- **B.** AWS CDK **[CORRECT]**
- **C.** AWS Budgets
- **D.** Amazon Athena

**Correct Answer:** `B`

#### Explanation & Rationale

The AWS CDK lets you define infra in real languages; it synthesises into a CloudFormation template under the hood.

---

<a id="q-38"></a>

### Question 38

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-038`

> **Scenario:**  
> Which IaC tool is third-party, cloud-agnostic, uses HCL, and maintains its own state file separate from AWS?

#### Options
- **A.** CloudFormation
- **B.** AWS CDK
- **C.** Terraform **[CORRECT]**
- **D.** CodeDeploy

**Correct Answer:** `C`

#### Explanation & Rationale

HashiCorp Terraform uses HCL, works across clouds via providers, and keeps its own state file — best for multi-cloud consistency.

---

<a id="q-39"></a>

### Question 39

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-039`

> **Scenario:**  
> Which CloudWatch feature scans centralised logs for a pattern (e.g. 'ERROR') and turns matches into a metric that can trigger an alarm?

#### Options
- **A.** A dashboard
- **B.** A metric filter **[CORRECT]**
- **C.** A canary
- **D.** A budget

**Correct Answer:** `B`

#### Explanation & Rationale

A CloudWatch Logs metric filter matches a log pattern and produces a metric that alarms can watch.

---

<a id="q-40"></a>

### Question 40

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-040`

> **Scenario:**  
> What is the CloudWatch automation chain that lets a system react to problems without a human?

#### Options
- **A.** Log → dashboard → email
- **B.** Metric → alarm → SNS / Auto Scaling / Lambda **[CORRECT]**
- **C.** Budget → anomaly → report
- **D.** Metric → snapshot → archive

**Correct Answer:** `B`

#### Explanation & Rationale

A metric feeds an alarm which triggers SNS, Auto Scaling, or an EventBridge/Lambda action — automated reaction.

---

<a id="q-41"></a>

### Question 41

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-041`

> **Scenario:**  
> You must give administrators shell access to EC2 instances without opening port 22/3389 or managing SSH keys. Which Systems Manager capability fits?

#### Options
- **A.** Parameter Store
- **B.** Session Manager **[CORRECT]**
- **C.** Patch Manager
- **D.** EventBridge

**Correct Answer:** `B`

#### Explanation & Rationale

SSM Session Manager provides shell access via IAM with no open inbound ports or key pairs — a frequently tested fact.

---

<a id="q-42"></a>

### Question 42

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-042`

> **Scenario:**  
> Which Systems Manager capability provides secure, hierarchical storage for configuration values and secrets (encrypted with KMS) retrieved at runtime?

#### Options
- **A.** Session Manager
- **B.** Parameter Store **[CORRECT]**
- **C.** Patch Manager
- **D.** Step Functions

**Correct Answer:** `B`

#### Explanation & Rationale

SSM Parameter Store holds connection strings, API keys and flags, KMS-encrypted, so credentials aren't hard-coded.

---

<a id="q-43"></a>

### Question 43

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-043`

> **Scenario:**  
> Which Systems Manager capability automates OS/application patching against defined baselines and maintenance windows?

#### Options
- **A.** Parameter Store
- **B.** Session Manager
- **C.** Patch Manager **[CORRECT]**
- **D.** CloudFormation

**Correct Answer:** `C`

#### Explanation & Rationale

SSM Patch Manager automates patching against baselines/maintenance windows — the customer's guest-OS patching duty.

---

<a id="q-44"></a>

### Question 44

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-044`

> **Scenario:**  
> A multi-step workflow needs sequencing, automatic retries with backoff, conditional branching, human-approval steps and a visual view of progress. Which service fits?

#### Options
- **A.** Plain AWS Lambda
- **B.** AWS Step Functions **[CORRECT]**
- **C.** Amazon SQS
- **D.** Amazon SNS

**Correct Answer:** `B`

#### Explanation & Rationale

Step Functions defines a state machine (Amazon States Language) with built-in sequencing, retries, branching and a visual graph.

---

<a id="q-45"></a>

### Question 45

**Set:** `Standard` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-045`

> **Scenario:**  
> Which scenario is best served by a single plain Lambda function rather than Step Functions?

#### Options
- **A.** A multi-step order-fulfilment process with approvals
- **B.** A single function reacting to a single event **[CORRECT]**
- **C.** A workflow needing visual progress tracking
- **D.** A long-running process exceeding Lambda's duration limit

**Correct Answer:** `B`

#### Explanation & Rationale

A single function reacting to a single event is plain Lambda; multi-step orchestrated workflows call for Step Functions.

---

<a id="q-46"></a>

### Question 46

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-046`

> **Scenario:**  
> Which AWS AI service analyses images and video for objects, faces, scenes and content moderation?

#### Options
- **A.** Amazon Textract
- **B.** Amazon Rekognition **[CORRECT]**
- **C.** Amazon Comprehend
- **D.** Amazon Polly

**Correct Answer:** `B`

#### Explanation & Rationale

Rekognition handles general image/video content analysis, including content moderation.

---

<a id="q-47"></a>

### Question 47

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-047`

> **Scenario:**  
> You need to extract text, forms and tables (key-value pairs) from scanned or handwritten documents. Which service fits best?

#### Options
- **A.** Amazon Rekognition
- **B.** Amazon Textract **[CORRECT]**
- **C.** Amazon Translate
- **D.** Amazon Lex

**Correct Answer:** `B`

#### Explanation & Rationale

Textract extracts text, forms and tables from documents — the classic distractor against Rekognition (general images).

---

<a id="q-48"></a>

### Question 48

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-048`

> **Scenario:**  
> Which service performs NLP tasks such as sentiment analysis, entity and key-phrase extraction — e.g. classifying support tickets by tone?

#### Options
- **A.** Amazon Comprehend **[CORRECT]**
- **B.** Amazon Polly
- **C.** Amazon Transcribe
- **D.** Amazon Forecast

**Correct Answer:** `A`

#### Explanation & Rationale

Comprehend is the NLP service for sentiment, entities, key phrases and language detection.

---

<a id="q-49"></a>

### Question 49

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-049`

> **Scenario:**  
> Which service converts written text into lifelike speech (text-to-speech)?

#### Options
- **A.** Amazon Transcribe
- **B.** Amazon Polly **[CORRECT]**
- **C.** Amazon Lex
- **D.** Amazon Comprehend

**Correct Answer:** `B`

#### Explanation & Rationale

Polly is text-to-speech; Transcribe is the reverse (speech-to-text).

---

<a id="q-50"></a>

### Question 50

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-050`

> **Scenario:**  
> Which service produces speech-to-text transcripts with timestamps and speaker identification (e.g. searchable call transcripts)?

#### Options
- **A.** Amazon Polly
- **B.** Amazon Transcribe **[CORRECT]**
- **C.** Amazon Translate
- **D.** Amazon Textract

**Correct Answer:** `B`

#### Explanation & Rationale

Transcribe converts audio to text with timestamps and speaker ID.

---

<a id="q-51"></a>

### Question 51

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-051`

> **Scenario:**  
> Which service is used to build the conversation flow of a voice/text chatbot?

#### Options
- **A.** Amazon Lex **[CORRECT]**
- **B.** Amazon Polly
- **C.** Amazon Comprehend
- **D.** Amazon Personalize

**Correct Answer:** `A`

#### Explanation & Rationale

Lex builds conversational chatbots (the conversation flow); add Translate and Polly for multilingual voice.

---

<a id="q-52"></a>

### Question 52

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-052`

> **Scenario:**  
> Which service gives real-time product recommendations on an e-commerce site?

#### Options
- **A.** Amazon Forecast
- **B.** Amazon Personalize **[CORRECT]**
- **C.** Amazon Comprehend
- **D.** Amazon Rekognition

**Correct Answer:** `B`

#### Explanation & Rationale

Personalize provides real-time recommendations; Forecast does time-series prediction.

---

<a id="q-53"></a>

### Question 53

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-053`

> **Scenario:**  
> A company wants to detect fraud patterns unique to its own historical transaction data. Which choice does the wording signal?

#### Options
- **A.** A pre-built AI service
- **B.** A custom SageMaker model **[CORRECT]**
- **C.** AWS Marketplace generic model
- **D.** Amazon Polly

**Correct Answer:** `B`

#### Explanation & Rationale

'Our own historical data / patterns specific to us' signals a custom model built with SageMaker, not a pre-built service.

---

<a id="q-54"></a>

### Question 54

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-054`

> **Scenario:**  
> In SageMaker, what do you pay for during model training?

#### Options
- **A.** A fixed monthly platform fee
- **B.** Only the training time (infrastructure is provisioned then torn down) **[CORRECT]**
- **C.** Per prediction request
- **D.** Nothing — training is free

**Correct Answer:** `B`

#### Explanation & Rationale

SageMaker provisions compute for training, then tears it down; you pay only for training duration.

---

<a id="q-55"></a>

### Question 55

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-055`

> **Scenario:**  
> A team with no data scientists wants to build a custom model from tabular data with minimal configuration. Which SageMaker features help?

#### Options
- **A.** Autopilot and Canvas **[CORRECT]**
- **B.** Data Wrangler only
- **C.** Ground Truth only
- **D.** Neptune

**Correct Answer:** `A`

#### Explanation & Rationale

SageMaker Autopilot and Canvas automatically build and tune models from tabular data with minimal ML expertise.

---

<a id="q-56"></a>

### Question 56

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-056`

> **Scenario:**  
> A custom, low-latency application must process each streaming record as it arrives, with multiple independent consumers. Which service fits?

#### Options
- **A.** Kinesis Data Firehose
- **B.** Kinesis Data Streams **[CORRECT]**
- **C.** Amazon S3
- **D.** AWS Glue

**Correct Answer:** `B`

#### Explanation & Rationale

Kinesis Data Streams uses shards and lets multiple consumers read the same stream within seconds for custom real-time apps.

---

<a id="q-57"></a>

### Question 57

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-057`

> **Scenario:**  
> You need a fully managed 'fire-and-forget' pipeline to load streaming data into S3 or Redshift with no shard management. Which service fits?

#### Options
- **A.** Kinesis Data Streams
- **B.** Kinesis Data Firehose **[CORRECT]**
- **C.** Amazon EMR
- **D.** Amazon Athena

**Correct Answer:** `B`

#### Explanation & Rationale

Firehose is a managed delivery pipeline into S3/Redshift/OpenSearch with optional Lambda transformation and no shards.

---

<a id="q-58"></a>

### Question 58

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-058`

> **Scenario:**  
> In a data lake, which service crawls raw S3 data to populate a catalog of schemas and can run serverless ETL jobs?

#### Options
- **A.** Amazon Athena
- **B.** AWS Glue **[CORRECT]**
- **C.** Amazon QuickSight
- **D.** Amazon Redshift

**Correct Answer:** `B`

#### Explanation & Rationale

Glue provides the Data Catalog (metadata) and serverless Spark ETL jobs; the data itself stays in S3.

---

<a id="q-59"></a>

### Question 59

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-059`

> **Scenario:**  
> Which service runs serverless standard SQL directly against data in S3, priced per query by data scanned?

#### Options
- **A.** Amazon Redshift
- **B.** Amazon Athena **[CORRECT]**
- **C.** Amazon EMR
- **D.** AWS Glue

**Correct Answer:** `B`

#### Explanation & Rationale

Athena queries S3 in place using the Glue Catalog, priced per data scanned — ideal for ad-hoc analysis.

---

<a id="q-60"></a>

### Question 60

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-060`

> **Scenario:**  
> Which service provides no-code BI dashboards and reports for business users, connecting to Athena, Redshift, RDS and S3?

#### Options
- **A.** AWS Glue
- **B.** Amazon QuickSight **[CORRECT]**
- **C.** Amazon Kinesis
- **D.** Amazon Comprehend

**Correct Answer:** `B`

#### Explanation & Rationale

QuickSight is the BI/dashboarding service for business users.

---

<a id="q-61"></a>

### Question 61

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-061`

> **Scenario:**  
> Analytics differ mainly by where the data lives. Which fits 'data stays in S3, queried occasionally, pay per scan'?

#### Options
- **A.** Redshift
- **B.** Athena **[CORRECT]**
- **C.** EMR
- **D.** DynamoDB

**Correct Answer:** `B`

#### Explanation & Rationale

Athena: data in S3, occasional/ad-hoc queries, per-scan pricing. Redshift = loaded warehouse; EMR = cluster frameworks.

---

<a id="q-62"></a>

### Question 62

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-062`

> **Scenario:**  
> A large-scale big-data job needs specific open-source frameworks (Spark, Hive, Presto) and cluster-level control. Which service fits?

#### Options
- **A.** Amazon Athena
- **B.** Amazon EMR **[CORRECT]**
- **C.** Amazon QuickSight
- **D.** Amazon RDS

**Correct Answer:** `B`

#### Explanation & Rationale

EMR runs Spark/Hadoop/Hive/Presto on clusters you control — for large custom big-data jobs.

---

<a id="q-63"></a>

### Question 63

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-063`

> **Scenario:**  
> Which migration service performs a lift-and-shift 'rehost' by continuously replicating source server disks to AWS for a minimal-downtime cutover to EC2?

#### Options
- **A.** Database Migration Service (DMS)
- **B.** Application Migration Service (MGN) **[CORRECT]**
- **C.** Schema Conversion Tool (SCT)
- **D.** DataSync

**Correct Answer:** `B`

#### Explanation & Rationale

MGN continuously replicates whole servers (physical/virtual/other-cloud) for a minimal-downtime rehost to EC2.

---

<a id="q-64"></a>

### Question 64

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-064`

> **Scenario:**  
> Which service migrates databases with a full load plus Change Data Capture, keeping the target in sync until cutover?

#### Options
- **A.** Application Migration Service (MGN)
- **B.** Database Migration Service (DMS) **[CORRECT]**
- **C.** Transfer Family
- **D.** Snowball

**Correct Answer:** `B`

#### Explanation & Rationale

DMS does a full load then CDC to keep the target synced with the live source until cutover; supports homogeneous and heterogeneous moves.

---

<a id="q-65"></a>

### Question 65

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-065`

> **Scenario:**  
> You are moving from Oracle to PostgreSQL (a heterogeneous migration). Which tool converts tables, views and stored procedures to the target engine's syntax?

#### Options
- **A.** Schema Conversion Tool (SCT) **[CORRECT]**
- **B.** DataSync
- **C.** MGN
- **D.** QuickSight

**Correct Answer:** `A`

#### Explanation & Rationale

The Schema Conversion Tool partners with DMS on heterogeneous moves, converting schema/code and flagging manual work.

---

<a id="q-66"></a>

### Question 66

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-066`

> **Scenario:**  
> A petabyte-scale dataset must reach AWS but the network would take weeks. Which option is appropriate?

#### Options
- **A.** DataSync over the internet
- **B.** A Snow Family physical device **[CORRECT]**
- **C.** Transfer Family (SFTP)
- **D.** Kinesis Firehose

**Correct Answer:** `B`

#### Explanation & Rationale

When network transfer would take too long, ship a Snow Family device; DataSync is for transfers the network can finish in time.

---

<a id="q-67"></a>

### Question 67

**Set:** `Standard` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-067`

> **Scenario:**  
> Which service provides automated, online transfer between on-prem NFS/SMB and S3, EFS or FSx with scheduling and integrity checks?

#### Options
- **A.** AWS DataSync **[CORRECT]**
- **B.** AWS Snowmobile
- **C.** AWS Transfer Family
- **D.** AWS DMS

**Correct Answer:** `A`

#### Explanation & Rationale

DataSync automates online file transfer between on-prem storage and AWS with built-in scheduling and validation.

---

<a id="q-68"></a>

### Question 68

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-068`

> **Scenario:**  
> Which AWS Support plan is free and included with every account?

#### Options
- **A.** Basic **[CORRECT]**
- **B.** Developer
- **C.** Business
- **D.** Enterprise

**Correct Answer:** `A`

#### Explanation & Rationale

The Basic plan is free: account/billing support, core Trusted Advisor checks, docs and forums.

---

<a id="q-69"></a>

### Question 69

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-069`

> **Scenario:**  
> At which support plan do the FULL set of Trusted Advisor checks (all five categories) first become available?

#### Options
- **A.** Basic
- **B.** Developer
- **C.** Business **[CORRECT]**
- **D.** Enterprise

**Correct Answer:** `C`

#### Explanation & Rationale

Full Trusted Advisor checks start at the Business plan; Basic/Developer get only core checks.

---

<a id="q-70"></a>

### Question 70

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-070`

> **Scenario:**  
> A mission-critical workload needs a dedicated Technical Account Manager (TAM) and Infrastructure Event Management. Which plan is required?

#### Options
- **A.** Developer
- **B.** Business
- **C.** Enterprise **[CORRECT]**
- **D.** Basic

**Correct Answer:** `C`

#### Explanation & Rationale

A dedicated TAM and Infrastructure Event Management are Enterprise-only.

---

<a id="q-71"></a>

### Question 71

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-071`

> **Scenario:**  
> A small team needs business-hours email guidance from Cloud Support Associates for non-production work. Which plan is the cheapest fit?

#### Options
- **A.** Basic
- **B.** Developer **[CORRECT]**
- **C.** Business
- **D.** Enterprise

**Correct Answer:** `B`

#### Explanation & Rationale

The Developer plan (from $29/mo) gives business-hours email access for small teams and non-production work.

---

<a id="q-72"></a>

### Question 72

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-072`

> **Scenario:**  
> Which AWS tool is used to VISUALISE and investigate spend and usage over time, filtering by service, account, Region or tag?

#### Options
- **A.** AWS Budgets
- **B.** AWS Cost Explorer **[CORRECT]**
- **C.** AWS Pricing Calculator
- **D.** Trusted Advisor

**Correct Answer:** `B`

#### Explanation & Rationale

Cost Explorer analyses and visualises spend/usage over time and can forecast future costs.

---

<a id="q-73"></a>

### Question 73

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-073`

> **Scenario:**  
> Which tool lets you set a cost or usage threshold and get alerted (or trigger an action) when it is breached or forecast to be?

#### Options
- **A.** Cost Explorer
- **B.** AWS Budgets **[CORRECT]**
- **C.** Pricing Calculator
- **D.** CloudTrail

**Correct Answer:** `B`

#### Explanation & Rationale

AWS Budgets sets thresholds and notifies via SNS/email, and can trigger automated actions on breach.

---

<a id="q-74"></a>

### Question 74

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-074`

> **Scenario:**  
> Which feature uses machine learning to automatically flag unusual spending without you setting manual thresholds?

#### Options
- **A.** Cost Anomaly Detection **[CORRECT]**
- **B.** AWS Budgets
- **C.** Trusted Advisor
- **D.** Consolidated billing

**Correct Answer:** `A`

#### Explanation & Rationale

Cost Anomaly Detection (part of Cost Explorer) uses ML to flag unusual spend automatically.

---

<a id="q-75"></a>

### Question 75

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-075`

> **Scenario:**  
> Which compute pricing model offers the deepest discount (up to ~90%) but can be reclaimed with a two-minute warning?

#### Options
- **A.** On-Demand
- **B.** Reserved Instances
- **C.** Savings Plans
- **D.** Spot Instances **[CORRECT]**

**Correct Answer:** `D`

#### Explanation & Rationale

Spot Instances use spare capacity at up to 90% off but can be reclaimed — only for interruption-tolerant work.

---

<a id="q-76"></a>

### Question 76

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-076`

> **Scenario:**  
> A steady workload needs discounts that stay flexible across instance family, size, Region, and even Fargate and Lambda. Which model fits best?

#### Options
- **A.** Standard Reserved Instances
- **B.** Compute Savings Plans **[CORRECT]**
- **C.** Spot Instances
- **D.** On-Demand

**Correct Answer:** `B`

#### Explanation & Rationale

Compute Savings Plans commit to $/hour of compute and apply across families, sizes, Regions, EC2, Fargate and Lambda.

---

<a id="q-77"></a>

### Question 77

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-077`

> **Scenario:**  
> Which pricing model is the flexible baseline with no commitment and the highest unit price, used as the yardstick for measuring savings?

#### Options
- **A.** On-Demand **[CORRECT]**
- **B.** Reserved Instances
- **C.** Savings Plans
- **D.** Spot

**Correct Answer:** `A`

#### Explanation & Rationale

On-Demand has no commitment and the highest unit price; all savings are measured against it.

---

<a id="q-78"></a>

### Question 78

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-078`

> **Scenario:**  
> Reserved Instances require what kind of commitment?

#### Options
- **A.** No commitment, pay per second
- **B.** A 1- or 3-year commitment to instance attributes **[CORRECT]**
- **C.** A two-minute reclaimable lease
- **D.** A per-request fee

**Correct Answer:** `B`

#### Explanation & Rationale

RIs commit for 1 or 3 years to family/size/Region (Standard) or with in-family flexibility (Convertible).

---

<a id="q-79"></a>

### Question 79

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-079`

> **Scenario:**  
> Which free tool (no AWS account needed) lets you build a cost estimate for a proposed architecture before you deploy it?

#### Options
- **A.** Cost Explorer
- **B.** AWS Pricing Calculator **[CORRECT]**
- **C.** AWS Budgets
- **D.** Trusted Advisor

**Correct Answer:** `B`

#### Explanation & Rationale

The AWS Pricing Calculator builds estimates for planned architectures and is free with no account required.

---

<a id="q-80"></a>

### Question 80

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-080`

> **Scenario:**  
> A parent company wants ONE invoice covering all its subsidiary accounts, with shared discounts and volume tiers. Which capability provides this?

#### Options
- **A.** AWS Budgets
- **B.** AWS Organizations consolidated billing **[CORRECT]**
- **C.** Cost Explorer
- **D.** Trusted Advisor

**Correct Answer:** `B`

#### Explanation & Rationale

Consolidated billing rolls all member accounts into one bill, aggregates volume pricing, and shares RI/Savings Plans discounts.

---

<a id="q-81"></a>

### Question 81

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-081`

> **Scenario:**  
> Under consolidated billing, how do Reserved Instance and Savings Plans discounts behave across linked accounts?

#### Options
- **A.** They apply only to the buying account
- **B.** They automatically apply to matching usage in any linked account (unless sharing is disabled) **[CORRECT]**
- **C.** They must be re-purchased per account
- **D.** They expire monthly

**Correct Answer:** `B`

#### Explanation & Rationale

Commitments bought in one account apply to matching usage in any other account, unless sharing is switched off.

---

<a id="q-82"></a>

### Question 82

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-082`

> **Scenario:**  
> Activating which feature lets you break down spend by team or project (e.g. CostCentre: Marketing) in Cost Explorer and billing reports?

#### Options
- **A.** Cost Allocation Tags **[CORRECT]**
- **B.** Service Control Policies
- **C.** Metric filters
- **D.** Savings Plans

**Correct Answer:** `A`

#### Explanation & Rationale

Cost Allocation Tags let you attribute spend to teams/projects for chargeback or showback.

---

<a id="q-83"></a>

### Question 83

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-083`

> **Scenario:**  
> Which Trusted Advisor category flags idle/underutilised EC2 instances and unattached EBS volumes?

#### Options
- **A.** Security
- **B.** Performance
- **C.** Cost Optimisation **[CORRECT]**
- **D.** Fault Tolerance

**Correct Answer:** `C`

#### Explanation & Rationale

Cost Optimisation checks surface idle resources and RI/Savings Plans opportunities.

---

<a id="q-84"></a>

### Question 84

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-084`

> **Scenario:**  
> Which Trusted Advisor category checks open security-group ports, root-account MFA and S3 bucket permissions?

#### Options
- **A.** Security **[CORRECT]**
- **B.** Performance
- **C.** Service Limits
- **D.** Fault Tolerance

**Correct Answer:** `A`

#### Explanation & Rationale

The Security category checks open ports, root MFA/IAM configuration and S3 permissions.

---

<a id="q-85"></a>

### Question 85

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-085`

> **Scenario:**  
> Which of these are the five Trusted Advisor check categories? (Choose the complete set.)

#### Options
- **A.** Cost, Performance, Security, Fault Tolerance, Service Limits **[CORRECT]**
- **B.** Cost, Speed, Encryption, Backup, Networking
- **C.** Compute, Storage, Database, Network, Billing
- **D.** Availability, Latency, Cost, Identity, Logging

**Correct Answer:** `A`

#### Explanation & Rationale

Trusted Advisor covers Cost Optimisation, Performance, Security, Fault Tolerance and Service Limits.

---

<a id="q-86"></a>

### Question 86

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-086`

> **Scenario:**  
> When several answers technically work on CLF-C02, which framework is the intended tiebreaker for the 'most correct' answer?

#### Options
- **A.** The Cloud Adoption Framework
- **B.** The Well-Architected Framework **[CORRECT]**
- **C.** The Shared Responsibility Model
- **D.** The MoSCoW method

**Correct Answer:** `B`

#### Explanation & Rationale

The Well-Architected Framework is the tiebreaker: prefer the answer reflecting best practice (e.g. Parameter Store over hard-coded creds).

---

<a id="q-87"></a>

### Question 87

**Set:** `Standard` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-087`

> **Scenario:**  
> On the exam, qualifying phrases like 'LEAST operational overhead' or 'MOST cost-effective' should be treated as:

#### Options
- **A.** Filler to ignore
- **B.** The selection criterion that decides among otherwise valid options **[CORRECT]**
- **C.** A hint the question is unscored
- **D.** A sign to pick the cheapest service always

**Correct Answer:** `B`

#### Explanation & Rationale

These qualifiers are the actual selection criteria; CLF-C02 rewards the managed/serverless, least-effort option.

---

