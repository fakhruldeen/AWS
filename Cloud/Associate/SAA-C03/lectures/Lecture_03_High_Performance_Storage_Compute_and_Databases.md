# Lecture 03: High-Performance Storage, Compute & Caching

> **Course Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Domain 3: Design High-Performing Architectures (24% Exam Weighting)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Select optimal block, file, and object storage solutions based on throughput, IOPS, and latency requirements.
2. Differentiate between Amazon EBS `gp3` and `io2` Block Express, and understand EFS Elastic Throughput mode.
3. Choose the appropriate Amazon FSx file system: FSx for Lustre (HPC), FSx for Windows (Active Directory SMB), and FSx for NetApp ONTAP (multi-protocol).
4. Evaluate compute placement groups (Cluster, Spread, Partition) to balance network throughput against hardware failure isolation.
5. Accelerate database reads using Amazon DynamoDB Accelerator (DAX) and Amazon ElastiCache for Redis.
6. Design global network acceleration architectures using Amazon CloudFront and AWS Global Accelerator.

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:00] 1. Performance Dimensions: Latency, Throughput & IOPS
[01:00 - 02:30] 2. Storage Selection: EBS (gp3 vs. io2), EFS & The Amazon FSx Family
[02:30 - 04:00] 3. Compute Optimization: Graviton, Placement Groups & Serverless (Fargate / Lambda)
[04:00 - 05:00] 4. Database Acceleration: Read Replicas, ElastiCache Redis & DynamoDB DAX
[05:00 - 05:45] 5. Global Networking: CloudFront vs. AWS Global Accelerator
[05:45 - 06:00] 6. Exam Scenarios & High-Performance Decision Matrices
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. Storage Decision Framework (Whiteboard Prompt)
- *Whiteboard Decision Tree:*
  - Need block storage attached to a single EC2 instance? $\implies$ **Amazon EBS**.
    - Baseline 3,000 IOPS / 125 MB/s up to 16,000 IOPS? $\implies$ **EBS gp3** (decoupled IOPS from size!).
    - Extreme OLTP up to 256,000 IOPS and 4,000 MB/s? $\implies$ **EBS io2 Block Express**.
  - Need POSIX shared Linux storage across hundreds of instances in multiple AZs? $\implies$ **Amazon EFS** (use Elastic Throughput mode!).
  - Need Windows file share with Active Directory NTFS permissions? $\implies$ **Amazon FSx for Windows File Server**.
  - Need massive parallel throughput for Linux HPC/ML reading from S3? $\implies$ **Amazon FSx for Lustre**.
  - Need multi-protocol (NFS + SMB + iSCSI) with snapshots and deduplication? $\implies$ **Amazon FSx for NetApp ONTAP**.

### 2. Compute Placement Groups: Three Distinct Strategies
- **Cluster Placement Group:** Instances packed closely together in a single AZ. Maximizes network throughput (up to 100 Gbps+) and delivers lowest inter-node latency. *Risk:* If the rack fails, all instances fail. Used for HPC, MPI, tightly coupled clusters.
- **Spread Placement Group:** Each instance placed on a strictly distinct underlying hardware rack with its own network and power. Max 7 instances per AZ. Used for small, critical production instances that must avoid correlated hardware failures.
- **Partition Placement Group:** Divides an AZ into logical partitions; partitions do not share hardware with other partitions. Used for large distributed systems (HDFS, Cassandra, Kafka).

### 3. In-Memory Caching: DAX vs. ElastiCache
- **DynamoDB Accelerator (DAX):** Microsecond read latencies for DynamoDB. API-compatible (zero code refactoring—just point the SDK at DAX endpoint). Solves the read-heavy gaming leaderboard or product catalog problem.
- **Amazon ElastiCache for Redis:** In-memory key-value and data structure store. Supports clustering, multi-AZ with auto-failover, sorted sets, hashes, pub/sub. Requires application code to query Redis directly.

### 4. Global Acceleration: CloudFront vs. Global Accelerator
| Dimension | Amazon CloudFront | AWS Global Accelerator |
|---|---|---|
| **Protocol Support** | HTTP, HTTPS, WebSockets | TCP, UDP (non-HTTP friendly!) |
| **Edge Behavior** | Caches static/dynamic web content at edge locations | Does NOT cache data; routes packets via Anycast IPs |
| **IP Addresses** | Dynamic DNS hostnames | Two static Anycast public IPv4 addresses |
| **Primary Use Case** | Web acceleration, CDN, video streaming, API caching | Multiplayer gaming, IoT, VoIP, non-HTTP enterprise apps |

---

## 🚨 SAA-C03 Exam Traps & Anti-Patterns

1. **Over-provisioning gp2 for IOPS:** In older exams, students were taught to increase `gp2` volume size to get burst IOPS (3 IOPS per GB). In SAA-C03, the correct answer is **EBS gp3**, which provisions IOPS independently of storage size!
2. **Global Accelerator vs. CloudFront for Gaming:** If the exam scenario mentions **UDP protocol** or multiplayer gaming, CloudFront is a wrong answer! CloudFront only supports HTTP/HTTPS. The correct answer is **AWS Global Accelerator**.
3. **Lambda Cold Starts:** When an exam question specifies that users experience 3 to 5 second latency spikes during traffic bursts on serverless APIs, the fix is **Lambda Provisioned Concurrency**.

---

## 🔬 Hands-on Lab & Homework Alignment
- **Decision Matrix Review:** Study [Storage Architecture Decision Matrix](../notes/Storage_Architecture_Decision_Matrix.md) and [Database Architecture Decision Matrix](../notes/Database_Architecture_Decision_Matrix.md).
- **Knowledge Check:** Assign [Module 03 Knowledge Check](../knowledge_checks/Module_03_High_Performing_Architectures_Knowledge_Check.md).
- **Revision Questions:** Direct students to practice [Domain 3 Revision Questions](../revision_questions/Domain_3_Design_High_Performing_Architectures_Revision_Questions.md).
