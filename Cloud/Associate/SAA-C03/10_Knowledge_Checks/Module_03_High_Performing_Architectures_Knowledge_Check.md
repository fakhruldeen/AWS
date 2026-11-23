# Module 03: Designing High-Performing Architectures — Knowledge Check

> **Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Module 3: High-Performance Compute, Storage & Caching  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 3 materials and completing Lab 02, Lab 03, and the high-yield decision notes. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
A high-performance computing (HPC) research simulation analyzes hundreds of terabytes of data stored in Amazon S3. The compute cluster requires a POSIX-compliant parallel file system delivering hundreds of gigabytes per second of throughput and sub-millisecond latencies with native bidirectional synchronization to S3. Which service should be selected?

- **A.** Amazon EFS General Purpose
- **B.** Amazon FSx for Lustre
- **C.** Amazon FSx for Windows File Server
- **D.** Amazon EBS gp3

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Amazon FSx for Lustre** is a high-performance parallel file system designed for compute-intensive HPC, machine learning, and video processing. It integrates natively with Amazon S3, allowing transparent reading and writing of data from and to S3 buckets.
</details>

---

### Question 2
An enterprise application running on EC2 requires an attached block storage volume capable of delivering 80,000 IOPS and 2,000 MB/s throughput with sub-millisecond latencies for an online transaction processing (OLTP) database. Which EBS volume type meets these requirements?

- **A.** General Purpose SSD (gp2)
- **B.** General Purpose SSD (gp3)
- **C.** Provisioned IOPS SSD (io2 Block Express)
- **D.** Throughput Optimized HDD (st1)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- **Amazon EBS io2 Block Express** volumes deliver up to 256,000 IOPS and 4,000 MB/s throughput with sub-millisecond latency and 99.999% durability, purpose-built for the most demanding relational database workloads.
- `gp3` maxes out at 16,000 IOPS and 1,000 MB/s throughput.
</details>

---

### Question 3
An architect is optimizing EBS costs for an application requiring 5,000 IOPS and 200 MB/s throughput on a 150 GB storage volume. Currently, the team uses `gp2` and was forced to provision 1.6 TB just to get bursting IOPS. How can they achieve this performance at the lowest cost?

- **A.** Migrate to `gp3` and independently provision 5,000 IOPS and 200 MB/s on the 150 GB volume.
- **B.** Upgrade to `io2` with 5,000 IOPS.
- **C.** Create a RAID 0 array of five 30 GB `gp2` volumes.
- **D.** Migrate to S3 Standard.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon EBS gp3** decouples storage capacity from IOPS and throughput. A 150 GB `gp3` volume comes with 3,000 IOPS and 125 MB/s included, and allows you to independently provision the additional 2,000 IOPS and 75 MB/s without paying for unneeded disk capacity.
</details>

---

### Question 4
A real-time gaming leaderboard uses Amazon DynamoDB. Under peak loads, millions of reads cause latency spikes. The team wants to reduce read latencies from milliseconds to microseconds without rewriting application database queries. What should be deployed?

- **A.** Amazon DynamoDB Accelerator (DAX)
- **B.** Amazon ElastiCache for Memcached
- **C.** Amazon S3 Transfer Acceleration
- **D.** DynamoDB Global Tables

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon DynamoDB Accelerator (DAX)** is a fully managed, in-memory cache purpose-built for DynamoDB that delivers microsecond response times at millions of requests per second. DAX is API-compatible with DynamoDB, requiring zero application query rewrites.
</details>

---

### Question 5
Which Amazon ElastiCache engine should be selected for an in-memory session store requiring complex data structures (sorted sets, hashes), Multi-AZ replication with automatic failover, and pub/sub messaging?

- **A.** Amazon ElastiCache for Memcached
- **B.** Amazon ElastiCache for Redis
- **C.** Amazon MemoryDB for DynamoDB
- **D.** Amazon CloudFront Edge Cache

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Amazon ElastiCache for Redis** supports rich data structures (hashes, sorted sets, lists), Multi-AZ replication with automated failover, data persistence, and pub/sub messaging.
- **Memcached** is a simple, multithreaded key-value cache with no multi-AZ replication, persistence, or complex data types.
</details>

---

### Question 6
An architect needs to run a tightly coupled MPI simulation across 16 EC2 instances requiring ultra-low inter-node latency and maximum network bandwidth. Which placement group should be configured?

- **A.** Spread Placement Group
- **B.** Partition Placement Group
- **C.** Cluster Placement Group
- **D.** Regional Placement Group

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- A **Cluster Placement Group** packs instances close together within a single Availability Zone, enabling low-latency network performance up to 100 Gbps, ideal for tightly coupled MPI and HPC workloads.
</details>

---

### Question 7
A mobile application experiences 3- to 5-second cold-start latency spikes when traffic surges suddenly after marketing push notifications. How can the architect eliminate cold starts for critical AWS Lambda functions?

- **A.** Configure AWS Lambda Provisioned Concurrency
- **B.** Schedule an EventBridge rule to ping Lambda once every hour
- **C.** Increase the Lambda timeout to 15 minutes
- **D.** Increase the API Gateway throttle limit

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Lambda Provisioned Concurrency** allocates pre-warmed execution environments ready to respond immediately within double-digit milliseconds, completely eliminating cold-start initialization latency.
</details>

---

### Question 8
Global field researchers in remote regions need to upload multi-gigabyte video files to an Amazon S3 bucket in `us-east-1`. Uploads over the public internet take hours and fail frequently. What feature should be enabled to accelerate file uploads?

- **A.** Amazon S3 Cross-Region Replication
- **B.** Amazon S3 Transfer Acceleration
- **C.** AWS DataSync
- **D.** AWS Snowball Edge

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Amazon S3 Transfer Acceleration** routes uploads to the nearest CloudFront edge location, and from there data travels to S3 over the optimized AWS private network backbone, dramatically speeding up long-distance uploads.
</details>

---

### Question 9
A company wants to route non-HTTP gaming traffic (UDP and TCP) from global players over the private AWS network to backend EC2 servers in Ireland, with two static Anycast IP addresses for client allowlisting. Which service meets this requirement?

- **A.** Amazon CloudFront
- **B.** AWS Global Accelerator
- **C.** Amazon Route 53 Geolocation
- **D.** AWS Direct Connect

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **AWS Global Accelerator** provides two static Anycast public IP addresses that route TCP and UDP traffic through AWS edge locations over the global AWS private backbone. CloudFront only supports HTTP, HTTPS, and WebSockets.
</details>

---

### Question 10
An architect needs to interconnect 30 VPCs and an on-premises data center with a dedicated 10 Gbps private connection in a hub-and-spoke topology without creating complex meshes of VPC peering connections. Which architecture is recommended?

- **A.** AWS Transit Gateway connected to an AWS Direct Connect Gateway
- **B.** Full mesh of 435 VPC Peering connections
- **C.** Multiple Site-to-Site VPN connections over an Internet Gateway
- **D.** Amazon S3 Multi-Region Access Points

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **AWS Transit Gateway** acts as a central cloud router connecting hundreds of VPCs and on-premises networks via Direct Connect Gateway in a scalable hub-and-spoke topology, avoiding the operational complexity of full-mesh VPC peering.
</details>
