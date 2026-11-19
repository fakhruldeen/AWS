---
marp: true
theme: default
paginate: true
header: "AWS Cloud Practitioner (CLF-C02) - Student Training"
footer: "© AWS Cloud Training Course | Module 2: Compute, Storage & Databases"
style: |
  section {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    padding: 40px;
    background-color: #fafafa;
  }
  h1 {
    color: #232f3e;
  }
  h2 {
    color: #ff9900;
  }
  .highlight {
    background-color: #fff3cd;
    padding: 2px 6px;
    border-radius: 4px;
  }
---

# AWS Certified Cloud Practitioner
## Module 2: Compute, Storage & Purpose-Built Databases
**Domain 3: Cloud Technology and Services**

*Instructor Delivery Deck & Student Lecture Notes*

---

# Amazon EC2: Elastic Compute Cloud

Amazon EC2 provides resizable compute capacity (virtual machines) in the cloud.

### EC2 Core Concepts:
- **AMI (Amazon Machine Image):** Pre-configured template containing the OS, application server, and software packages.
- **Instance Types:** Optimized for specific workloads:
  - **General Purpose (M, T):** Balanced compute, memory, and networking.
  - **Compute Optimized (C):** High-performance processors (batch, web servers).
  - **Memory Optimized (R, X):** Large in-memory datasets (caches, memory DBs).
  - **Storage Optimized (I, D):** High sequential read/write access (data warehouses).
  - **Accelerated Computing (P, G):** Hardware GPUs for machine learning and graphics.

---

# EC2 Purchasing Options: Strategic Cost Optimization

| Model | Commitment | Discount | Best For |
| :--- | :--- | :--- | :--- |
| **On-Demand** | None (Pay per second) | 0% | Short-term, unpredictable workloads, dev/test. |
| **Savings Plans** | 1 or 3 Years (Hourly $ commit) | **Up to 72%** | Flexible, steady-state usage across EC2, Fargate, Lambda. |
| **Reserved Instances (RI)** | 1 or 3 Years (Specific instance) | **Up to 72%** | Steady-state predictable databases or specific configurations. |
| **Spot Instances** | None (AWS unused capacity) | **Up to 90%** | Fault-tolerant, stateless batch jobs (can be interrupted). |
| **Dedicated Hosts** | Physical server dedicated | High | Strict compliance or server-bound software licenses (BYOL). |

---

# Containers & Serverless Compute

### 1. Amazon ECS (Elastic Container Service)
- AWS-native container management service supporting Docker containers.

### 2. Amazon EKS (Elastic Kubernetes Service)
- Managed Kubernetes control plane for running standard Kubernetes workloads.

### 3. AWS Fargate (Serverless Container Engine)
- Run containers on ECS or EKS **without provisioning, patching, or managing EC2 servers**. Pay strictly for vCPU and memory consumed.

### 4. AWS Lambda (Serverless Functions)
- Event-driven compute service: run code without provisioning servers.
- Scales automatically; max execution duration is **15 minutes**.

---

# Amazon S3: Object Storage Essentials

Amazon Simple Storage Service (S3) stores data as **objects** inside **buckets**.

- **Unlimited Scalability:** Store virtually unlimited files (individual objects from 0 bytes up to **5 TB**).
- **Extreme Durability:** Engineered for **99.999999999% (11 9s) of data durability**.
- **Data Model:** Flat object namespace (Key, Value, Metadata, Version ID, Access Control).
- **Core Capabilities:**
  - **Static Website Hosting:** Host HTML/CSS/JS with zero servers.
  - **Versioning:** Protects against accidental overwrites and deletions.
  - **S3 Object Lock:** WORM compliance (Write Once, Read Many).

---

# S3 Storage Classes: Balancing Cost & Access Speed

```
Frequent Access ──────────────────────────────────────> Archival
  [S3 Standard] ──> [S3 Standard-IA] ──> [Glacier Instant] ──> [Glacier Deep Archive]
    (Highest Cost)      (Infrequent Access)     (Milliseconds)         (Lowest Cost / 12h)
```

| Class | Retrieval Speed | Minimum Duration | Ideal Use Case |
| :--- | :--- | :--- | :--- |
| **Standard** | Immediate (ms) | None | Active, frequently accessed website data. |
| **Intelligent-Tiering** | Immediate (ms) | None | Workloads with unknown or changing patterns. |
| **Standard-IA** | Immediate (ms) | 30 days | Long-term data accessed infrequently (disaster recovery). |
| **Glacier Instant** | Immediate (ms) | 90 days | Archive data that still needs millisecond retrieval. |
| **Glacier Flexible** | Minutes to Hours | 90 days | Historical archives (retrieval within 1 min to 5 hours). |
| **Glacier Deep Archive** | **12 to 48 Hours** | 180 days | Legal archives (lowest cost storage in AWS: ~$1/TB/month). |

---

# Block vs. File vs. Object Storage

| Dimension | Amazon EBS (Block) | Amazon EFS (File) | Amazon S3 (Object) |
| :--- | :--- | :--- | :--- |
| **Storage Unit** | Blocks (Raw virtual disk). | Files in a hierarchical tree. | Discrete Objects with metadata. |
| **Attached To** | **Single EC2 instance** in same AZ (like a virtual USB drive). | **Thousands of EC2/Lambda instances** simultaneously across AZs. | Accessible globally via HTTP/HTTPS REST APIs. |
| **Protocols** | Direct block bus attached. | Standard **NFSv4** (Linux). | HTTP / HTTPS (S3 API). |
| **Use Case** | Boot drives, relational database storage, OS disks. | Shared file systems, content management (WordPress), home directories. | Media distribution, backups, big data lakes, static web hosting. |

---

# Purpose-Built Relational Databases: RDS & Aurora

### Amazon RDS (Relational Database Service)
- Managed engines: **PostgreSQL, MySQL, MariaDB, Oracle, SQL Server**.
- Automates patching, automated backups, and snapshot management.
- **Multi-AZ:** Synchronous replication to standby instance in 2nd AZ for **High Availability (Disaster Recovery)**.
- **Read Replicas:** Up to 5 asynchronous replicas for **Read Performance Scaling**.

### Amazon Aurora (AWS Enterprise Cloud-Native Relational DB)
- **5x throughput of MySQL, 3x throughput of PostgreSQL**.
- Decoupled storage: automatically replicates **6 copies across 3 AZs**.
- Storage auto-scales in 10 GB increments up to **128 TB**.
- Supports **Aurora Serverless v2** and **Aurora Global Database**.

---

# Non-Relational & In-Memory Databases

### Amazon DynamoDB (Serverless NoSQL)
- Fully managed, serverless **Key-Value and Document** database.
- Consistently delivers **single-digit millisecond latency at any scale**.
- Seamless horizontal scaling across multiple AZs.
- **DAX (DynamoDB Accelerator):** In-memory cache delivering **microsecond** response times.

### Amazon ElastiCache (In-Memory Caching)
- In-memory data store to offload read-heavy traffic from databases:
  - **Redis:** Multi-AZ failover, persistence, complex data structures.
  - **Memcached:** Simple multi-threaded object caching.

---

# Summary & Key Takeaways

1. **EC2 Instance Types:** Match the prefix letter to the workload (C = Compute, R = RAM, I = I/O Storage).
2. **EBS vs. EFS vs. S3:**
   - EBS is a single instance virtual disk (Block).
   - EFS is multi-instance shared Linux storage (File).
   - S3 is global cloud object storage (11 9s durability).
3. **Multi-AZ vs. Read Replicas:**
   - Multi-AZ = Synchronous standby for High Availability.
   - Read Replicas = Asynchronous copies for Read Scaling.
4. **DynamoDB:** Serverless NoSQL key-value database for predictable millisecond scale.

---

# Module 2 Student Review Quiz

1. **A startup needs a compute service to process JPEG images uploaded to S3. Tasks take 30 seconds and run sporadically. Which service is MOST cost-effective?**
   * A) Amazon EC2 On-Demand
   * B) AWS Lambda *(Correct — serverless, pay per millisecond, zero idle cost)*
   * C) Amazon ECS with dedicated EC2 instances
   * D) AWS Elastic Beanstalk

2. **A healthcare company must retain medical records for 10 years for compliance. Records are rarely accessed, but retrieval within 12–48 hours is acceptable. Which storage class offers the LOWEST cost?**
   * A) Amazon S3 Standard
   * B) Amazon S3 Standard-IA
   * C) Amazon S3 Glacier Deep Archive *(Correct — lowest cost storage at ~$1/TB/month)*
   * D) Amazon EBS Cold HDD (sc1)

3. **Which AWS database service provides fully managed NoSQL key-value storage with single-digit millisecond latency at any scale?**
   * A) Amazon RDS for MySQL
   * B) Amazon Aurora
   * C) Amazon DynamoDB *(Correct — serverless NoSQL key-value with DAX in-memory acceleration)*
   * D) Amazon Redshift

