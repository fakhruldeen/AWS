# AWS Certified Solutions Architect - Associate (SAA-C03)
## Domain 3: Design High-Performing Architectures (24%)

> **Focus:** Official AWS Exam Objectives for Domain 3: Design High-Performing Architectures  
> **Total Scenario Questions:** 28  

---

### Question 01 [SAA-C03-D3-Q069]

**Task Statement 3.1**

A genomic research organization runs high-performance computing (HPC) simulations that analyze hundreds of terabytes of genome sequence files stored in Amazon S3. The compute cluster requires a shared POSIX-compliant parallel file system capable of delivering millions of IOPS and hundreds of gigabytes per second of throughput with sub-millisecond latencies, with native synchronization back to Amazon S3. Which storage service best satisfies this requirement?

- **A)** Amazon Elastic File System (Amazon EFS) General Purpose mode
- **B)** Amazon FSx for Lustre linked to the Amazon S3 bucket
- **C)** Amazon FSx for Windows File Server
- **D)** Amazon EBS Provisioned IOPS io2 volume mounted via NFS

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon FSx for Lustre is a high-performance parallel file system designed for compute-intensive workloads such as HPC, machine learning, and media processing. It provides sub-millisecond latencies, hundreds of gigabytes per second of throughput, and millions of IOPS. Crucially, FSx for Lustre integrates directly with Amazon S3, allowing transparent reading and writing of data directly from and to S3 buckets.
- Option A: Amazon EFS provides scalable NFS storage for general web serving and enterprise apps, but does not provide parallel Lustre architecture throughput for HPC simulations.
- Option C: FSx for Windows File Server is built on Windows SMB, not a Linux HPC POSIX parallel file system.
- Option D: EBS io2 volumes cannot be natively shared across hundreds of HPC compute nodes across AZs with S3 integration.

**References:**
- Amazon FSx for Lustre User Guide
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 02 [SAA-C03-D3-Q070]

**Task Statement 3.1**

An enterprise is migrating its legacy Windows file shares to AWS. The solution must support the Server Message Block (SMB) protocol, integrate natively with on-premises Active Directory for Windows ACL file permissions, and provide Multi-AZ redundancy with automatic failover. Which AWS managed service should be selected?

- **A)** Amazon FSx for Windows File Server Multi-AZ
- **B)** Amazon Elastic File System (Amazon EFS)
- **C)** Amazon S3 File Gateway
- **D)** Amazon FSx for Lustre

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon FSx for Windows File Server provides fully managed native Microsoft Windows file storage built on Windows Server. It natively supports the SMB protocol, integrates with Active Directory for NTFS access control lists (ACLs), supports DFS Namespaces, and offers Multi-AZ deployments with automatic synchronous replication and failover.
- Option B: Amazon EFS supports the NFS protocol for Linux workloads, not native Windows SMB with Active Directory NTFS permissions.
- Option C: S3 File Gateway provides a file interface into S3 for hybrid backups, but is not a fully managed Multi-AZ Windows file server replacement.
- Option D: FSx for Lustre is a high-performance Linux file system, not a Windows SMB file share.

**References:**
- Amazon FSx for Windows File Server User Guide
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 03 [SAA-C03-D3-Q071]

**Task Statement 3.1**

A multinational enterprise wants to migrate mission-critical enterprise applications that require multi-protocol access (concurrent NFS, SMB, and iSCSI access to the same shared dataset), hardware-accelerated data deduplication, compression, and near-instant point-in-time snapshot cloning. Which managed file service fulfills these requirements?

- **A)** Amazon FSx for NetApp ONTAP
- **B)** Amazon EFS Max I/O
- **C)** Amazon FSx for OpenZFS
- **D)** AWS Storage Gateway Tape Gateway

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon FSx for NetApp ONTAP is a fully managed service that delivers NetApp's ONTAP enterprise storage capabilities in AWS. It uniquely supports multi-protocol access (NFS, SMB, and iSCSI) to shared storage volumes, advanced NetApp data management features (FlexClone, SnapMirror, SnapVault), and built-in data deduplication and compression for storage optimization.
- Option B: EFS supports NFS only, not SMB or block-level iSCSI.
- Option C: FSx for OpenZFS supports NFS, but does not provide multi-protocol SMB and iSCSI access like ONTAP.
- Option D is a virtual tape backup solution.

**References:**
- Amazon FSx for NetApp ONTAP User Guide
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 04 [SAA-C03-D3-Q072]

**Task Statement 3.3**

A production relational database running on Amazon RDS for PostgreSQL is experiencing severe performance degradation. Analysis shows that 90% of incoming queries are read-only SELECT queries generated by customer reporting dashboards, while writes account for only 10% of workload. What is the most effective architectural solution to relieve pressure on the primary database?

- **A)** Deploy an Amazon RDS Multi-AZ standby instance and direct reporting queries to the standby instance IP address.
- **B)** Create one or more Amazon RDS Read Replicas and update the reporting dashboard configuration to query the Read Replica endpoints.
- **C)** Migrate the database to Amazon S3 and query it using Amazon Athena.
- **D)** Increase the storage volume of the primary instance by 500%.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon RDS Read Replicas use PostgreSQL's built-in asynchronous replication to offload read-heavy query traffic from the primary DB instance. By directing reporting dashboards to query Read Replica endpoints, the primary instance is freed to handle transactional write operations efficiently.
- Option A: In an RDS Multi-AZ deployment, the standby replica is a passive physical standby that does NOT accept read or write queries; its sole purpose is automated failover.
- Option C requires dismantling the relational OLTP schema and migrating to S3 analytical queries, disrupting application architecture.
- Option D increases storage capacity but does not alleviate compute/memory contention caused by heavy read traffic.

**References:**
- Amazon RDS User Guide: Working with Read Replicas
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 05 [SAA-C03-D3-Q073]

**Task Statement 3.3**

A real-time mobile gaming leaderboard uses Amazon DynamoDB as its backend database. During peak gaming tournaments, millions of players poll the leaderboard simultaneously, resulting in read latency spikes and throttling exceptions. The architect must reduce read response times from milliseconds to microseconds without rewriting application query logic. Which solution should be implemented?

- **A)** Enable Amazon DynamoDB Accelerator (DAX) and update the DynamoDB client SDK to point to the DAX cluster endpoint.
- **B)** Deploy an Amazon ElastiCache for Memcached cluster and rewrite the game application code to handle cache invalidation and queries.
- **C)** Switch the DynamoDB table to Global Tables with active-active replication.
- **D)** Migrate the leaderboard data to Amazon RDS for MySQL.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache purpose-built for DynamoDB that delivers up to a 10x performance improvement—from milliseconds to microseconds—even at millions of requests per second. DAX is API-compatible with DynamoDB, meaning developers simply reconfigure the existing DynamoDB client SDK to point to the DAX endpoint without rewriting data access logic.
- Option B: ElastiCache Memcached requires developers to manually write application caching logic, cache-aside management, and serialization.
- Option C replicates data geographically across regions, but does not provide microsecond in-memory read caching within the region.
- Option D degrades performance and scalability compared to DynamoDB + DAX.

**References:**
- Amazon DynamoDB Developer Guide: In-Memory Acceleration with DAX
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 06 [SAA-C03-D3-Q074]

**Task Statement 3.3**

An architect is designing a high-performance web session store and caching layer for a social media application. The caching layer must support complex data structures (sorted sets, hashes, lists), automated failover across multiple Availability Zones, in-transit and at-rest encryption, and publish/subscribe messaging capabilities. Which caching engine should be selected?

- **A)** Amazon ElastiCache for Memcached
- **B)** Amazon ElastiCache for Redis
- **C)** Amazon DynamoDB On-Demand
- **D)** Amazon CloudFront Edge Cache

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon ElastiCache for Redis is an in-memory data store supporting advanced data structures (strings, hashes, lists, sets, sorted sets), Multi-AZ replication with automatic failover, pub/sub messaging, geospatial indexing, and at-rest/in-transit encryption.
- Option A: ElastiCache for Memcached is a simple, multithreaded key-value cache that does NOT support complex data structures, multi-AZ replication, pub/sub, or automated failover.
- Option C: DynamoDB is a persistent NoSQL database, not a dedicated in-memory sub-millisecond cache.
- Option D: CloudFront caches static and dynamic web content at edge locations, not application state data structures.

**References:**
- Amazon ElastiCache User Guide: Comparing Redis and Memcached
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 07 [SAA-C03-D3-Q075]

**Task Statement 3.4**

A global gaming application deployed on EC2 instances in the `eu-west-1` region experiences packet loss and high latency jitter for players connecting from North America and Asia over the public internet. The application uses custom non-HTTP UDP and TCP protocols for multiplayer game synchronization. Which AWS service should be deployed to route player traffic over the AWS global private fiber network?

- **A)** Amazon CloudFront
- **B)** AWS Global Accelerator
- **C)** Amazon Route 53 Geolocation Routing
- **D)** AWS Direct Connect

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Global Accelerator provides static Anycast IP addresses that act as fixed entry points to your application endpoints in single or multiple AWS Regions. It ingests traffic at the closest AWS edge location and routes it over the congestion-free AWS global private network backbone. Crucially, Global Accelerator supports both TCP and UDP protocols (making it ideal for gaming and VoIP), whereas CloudFront is limited to HTTP/HTTPS/WebSockets.
- Option A: Amazon CloudFront is a Content Delivery Network designed for HTTP/HTTPS web traffic and static media caching; it does not support raw UDP gaming traffic.
- Option C: Route 53 performs DNS resolution; traffic still traverses the unpredictable public internet.
- Option D: Direct Connect provides dedicated physical circuits between on-premises corporate data centers and AWS, not global internet gaming consumers.

**References:**
- AWS Global Accelerator Developer Guide
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 08 [SAA-C03-D3-Q076]

**Task Statement 3.4**

A media company serves millions of international users with a dynamic web application hosted on an Application Load Balancer in `us-east-1`. Users outside North America experience high page load times due to multiple SSL handshakes and slow round-trip times across the public internet. The company wants to cache static content at edge locations and terminate SSL/TLS connections closer to end users. Which solution should be deployed?

- **A)** Amazon CloudFront distribution configured with the Application Load Balancer as its custom origin
- **B)** AWS Transit Gateway connecting all regions
- **C)** VPC Peering across multiple AWS Regions
- **D)** Amazon Route 53 Multivalue Answer Routing

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon CloudFront is a global Content Delivery Network (CDN) with hundreds of Point of Presence (PoP) edge locations worldwide. It caches static content close to viewers, terminates SSL/TLS connections at the nearest edge to drastically shorten handshake latency, and reuses persistent TCP connections back to the origin ALB over the optimized AWS global network.
- Option B: Transit Gateway is for VPC and on-premises network routing, not consumer web acceleration.
- Option C: Cross-region VPC peering connects VPCs, not end-user web traffic.
- Option D only balances DNS queries among multiple IP addresses without edge caching or SSL termination.

**References:**
- Amazon CloudFront Developer Guide: Optimizing Performance with CloudFront
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 09 [SAA-C03-D3-Q077]

**Task Statement 3.1**

A mission-critical financial trading database running on Amazon EC2 requires sustained, predictable storage performance of 80,000 IOPS and 2,000 MB/s throughput with sub-millisecond I/O latencies. Which Amazon EBS volume type must the solutions architect configure?

- **A)** General Purpose SSD (gp2)
- **B)** General Purpose SSD (gp3)
- **C)** Provisioned IOPS SSD (io2 Block Express)
- **D)** Throughput Optimized HDD (st1)

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
Amazon EBS `io2` Block Express volumes are designed for mission-critical, high-IOPS, low-latency relational database workloads (such as Oracle, SAP HANA, Microsoft SQL Server). `io2` Block Express volumes deliver up to 256,000 IOPS, 4,000 MB/s throughput, and sub-millisecond latencies with 99.999% durability.
- Option A: `gp2` maxes out at 16,000 IOPS and ties IOPS to volume size.
- Option B: `gp3` maxes out at 16,000 IOPS and 1,000 MB/s throughput, which is insufficient for 80,000 IOPS.
- Option D: `st1` is a magnetic spinning disk volume type intended for large sequential streaming workloads (500 IOPS max), not low-latency random transactional databases.

**References:**
- Amazon EBS User Guide: Provisioned IOPS SSD Volumes (io2 Block Express)
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 10 [SAA-C03-D3-Q078]

**Task Statement 3.1**

An architect is optimizing storage costs and performance for a fleet of EC2 instances currently using EBS `gp2` volumes. The application requires 6,000 IOPS and 250 MB/s throughput, but the dataset size is only 100 GB. Under `gp2`, the team was forced to over-provision storage to 2 TB just to gain bursting IOPS. How can the architect satisfy the performance requirements at the lowest cost?

- **A)** Migrate the volumes from `gp2` to `gp3` and independently provision 6,000 IOPS and 250 MB/s on the 100 GB volume.
- **B)** Upgrade the volumes to `io2` with 6,000 IOPS.
- **C)** Add 5 additional `gp2` volumes in a RAID 0 software array.
- **D)** Migrate storage to Amazon S3 Standard.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon EBS General Purpose SSD `gp3` volumes decouple storage capacity from performance. A `gp3` volume provides a baseline of 3,000 IOPS and 125 MB/s throughput for free at any volume size, and allows customers to independently scale IOPS (up to 16,000) and throughput (up to 1,000 MB/s) without provisioning unnecessary gigabytes of disk space, reducing costs by up to 20% compared to `gp2`.
- Option B: `io2` is much more expensive per provisioned IOPS than `gp3` and is unnecessary for moderate 6,000 IOPS requirements.
- Option C increases operational complexity and failure risk without decoupling IOPS from capacity.
- Option D is object storage and cannot serve as an attached POSIX block volume for local EC2 operations.

**References:**
- Amazon EBS User Guide: General Purpose SSD Volumes (gp3)
- AWS Well-Architected Cost and Performance Pillars

</details>

---

### Question 11 [SAA-C03-D3-Q079]

**Task Statement 3.2**

A technology company wants to optimize the compute performance and cost of its containerized microservices running on Amazon EC2. The applications are written in Go, Python, and Node.js. Benchmarks indicate that migrating from x86 architecture to ARM-based processors will improve price-performance by up to 40%. Which EC2 instance families should the architect evaluate?

- **A)** AWS Graviton-powered instances (such as C7g, M7g, R7g)
- **B)** Intel Xeon-powered instances (such as C6i, M6i)
- **C)** AMD EPYC-powered instances (such as C6a, M6a)
- **D)** Mac mini instances (such as mac1.metal)

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Graviton processors are custom-built by AWS using 64-bit Arm Neoverse cores to deliver the best price-performance for cloud workloads in Amazon EC2. Graviton3 and Graviton4-based instance families (identified by the 'g' suffix, e.g., C7g, M7g, R7g) deliver up to 40% better price-performance over comparable current-generation x86-based instances.
- Option B: Intel instances ('i' suffix) use x86_64 architecture.
- Option C: AMD instances ('a' suffix) use x86_64 architecture.
- Option D: Mac instances are dedicated to building and testing macOS/iOS applications.

**References:**
- Amazon EC2 User Guide: AWS Graviton Instances
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 12 [SAA-C03-D3-Q080]

**Task Statement 3.4**

A multinational corporation has a hybrid cloud architecture where its on-premises data center in Frankfurt must connect with 25 Amazon VPCs spread across multiple AWS accounts in `eu-central-1`. The corporate network requires a dedicated, private, low-latency 10 Gbps physical network connection that bypasses the public internet completely. Which hybrid networking architecture should be deployed?

- **A)** An AWS Direct Connect connection with an AWS Transit Gateway associated with an AWS Direct Connect Gateway.
- **B)** 25 separate AWS Site-to-Site VPN connections over the public internet.
- **C)** 25 VPC Peering connections linked directly to an on-premises hardware router.
- **D)** AWS Storage Gateway running over public IP endpoints.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
An AWS Direct Connect dedicated connection provides a physical fiber-optic link between the on-premises network and AWS with consistent, ultra-low latency. By terminating Direct Connect into an AWS Direct Connect Gateway and associating it with an AWS Transit Gateway, the on-premises data center can seamlessly connect to hundreds of VPCs across multiple AWS accounts in a clean hub-and-spoke topology.
- Option B: Site-to-Site VPNs traverse the public internet, suffering from variable latencies and bandwidth limits.
- Option C: VPC Peering only connects VPC to VPC within AWS; it cannot peer directly to an on-premises router.
- Option D is a storage gateway service, not an enterprise network transport.

**References:**
- AWS Direct Connect User Guide: Transit Gateway Associations
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 13 [SAA-C03-D3-Q081]

**Task Statement 3.2**

An architect is deploying a tightly coupled high-performance computing (HPC) weather modeling simulation on Amazon EC2. The simulation nodes run Message Passing Interface (MPI) libraries and require ultra-low inter-node network latency and maximum bisection bandwidth within a single Availability Zone. Which two EC2 configurations should be used? (Choose TWO)

- **A)** Launch instances in a Cluster Placement Group.
- **B)** Attach an Elastic Fabric Adapter (EFA) network interface to each instance.
- **C)** Launch instances across multiple AWS Regions using Latency Routing.
- **D)** Launch instances in a Spread Placement Group.
- **E)** Use T4g burstable instances with unlimited CPU credits.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A, B`

**Detailed Explanation:**
A Cluster Placement Group packs instances close together inside an Availability Zone to achieve the highest network throughput (up to 100 Gbps+) and lowest latency. Combining this with an Elastic Fabric Adapter (EFA)—a custom network device that bypasses the OS kernel using Libfabric to handle inter-node communications—delivers the ultra-low latency required for tightly coupled MPI and machine learning workloads.
- Option C increases latency by traversing continents.
- Option D: Spread placement groups place instances on separate physical hardware racks across AZs, which increases inter-node latency.
- Option E: Burstable instances are not suitable for intense HPC simulations.

**References:**
- Amazon EC2 User Guide: Elastic Fabric Adapter
- Amazon EC2 User Guide: Placement Groups

</details>

---

### Question 14 [SAA-C03-D3-Q082]

**Task Statement 3.2**

An architect is launching 7 critical application server instances. The business requirements mandate that no two instances can share the same underlying hardware rack or power supply in an Availability Zone, so that a rack-level hardware failure will impact at most one single instance. Which placement strategy must be configured?

- **A)** Cluster Placement Group
- **B)** Partition Placement Group
- **C)** Spread Placement Group
- **D)** Distributed Auto Scaling Group

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
A Spread Placement Group places instances on distinct physical hardware racks, each with its own network and power source. A spread placement group can have a maximum of 7 running instances per Availability Zone per group, making it the ideal placement strategy for small groups of critical instances that must be isolated from correlated hardware failures.
- Option A (Cluster) places instances on the same rack to maximize throughput, which increases correlated failure risk.
- Option B (Partition) divides the group into partitions of multiple instances, typically used for large distributed systems like Hadoop, HDFS, and Cassandra.
- Option D is not a recognized AWS placement group type.

**References:**
- Amazon EC2 User Guide: Placement Groups - Spread
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 15 [SAA-C03-D3-Q083]

**Task Statement 3.2**

A company operates an Apache Kafka cluster and an Apache Cassandra database on Amazon EC2 instances across 3 Availability Zones. Each cluster consists of hundreds of nodes. The architecture must ensure that groups of instances (partitions) do not share underlying hardware racks with other partitions within the same AZ, and the application must be able to inspect which partition an instance belongs to. Which placement group should be selected?

- **A)** Partition Placement Group
- **B)** Cluster Placement Group
- **C)** Spread Placement Group
- **D)** Single-AZ Placement Group

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Partition Placement Groups divide each Availability Zone into logical partitions, where each partition contains a group of instances that share hardware racks with each other, but do not share racks with instances in other partitions. This is explicitly designed for large distributed and replicated workloads like Apache HDFS, HBase, Cassandra, and Kafka.
- Option B (Cluster) is for tightly coupled low-latency nodes, not distributed partition-isolated racks.
- Option C (Spread) is strictly limited to 7 instances per AZ, which cannot accommodate hundreds of nodes.
- Option D is not an AWS placement group type.

**References:**
- Amazon EC2 User Guide: Placement Groups - Partition
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 16 [SAA-C03-D3-Q084]

**Task Statement 3.2**

An AWS Lambda function performs complex scientific calculations. The function is taking 45 seconds to complete execution when allocated 512 MB of memory. The developer wants to accelerate computation time significantly without changing code. How can the architect tune the function's execution performance?

- **A)** Increase the allocated memory of the Lambda function up to 10,240 MB.
- **B)** Enable Provisioned Concurrency with a value of 1.
- **C)** Change the function execution role to have full administrator permissions.
- **D)** Deploy the Lambda function inside a public subnet with an Internet Gateway.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
In AWS Lambda, memory allocation is the primary lever for compute performance. When you increase memory (configurable from 128 MB up to 10,240 MB in 1 MB increments), AWS Lambda proportionally allocates CPU power, network bandwidth, and I/O throughput. Increasing memory from 512 MB to a higher tier adds dedicated vCPUs, accelerating compute-bound calculations dramatically.
- Option B: Provisioned Concurrency pre-warms execution environments to eliminate cold-start latencies, but does not increase CPU speed during computation.
- Option C: IAM permissions control authorization, not CPU/hardware execution speed.
- Option D: Placing Lambda in a VPC subnet actually adds network interface attachment overhead and does not increase CPU performance.

**References:**
- AWS Lambda Developer Guide: Configuring Lambda Function Memory
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 17 [SAA-C03-D3-Q085]

**Task Statement 3.2**

A mobile application calls an API backed by Amazon API Gateway and AWS Lambda. While steady-state requests respond in 50 milliseconds, during sudden traffic spikes after push notifications, first-time users experience 3 to 5 second delays due to container cold starts. How can the architect eliminate cold-start latencies for critical endpoints?

- **A)** Configure AWS Lambda Provisioned Concurrency for the production alias.
- **B)** Write a cron job in Amazon EventBridge to ping the Lambda function every 60 minutes.
- **C)** Increase the API Gateway integration timeout to 60 seconds.
- **D)** Convert the Lambda function to run on an Amazon EC2 t3.nano instance.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Lambda Provisioned Concurrency initializes a requested number of execution environments in advance so that they are warm, ready, and able to respond immediately within double-digit milliseconds, completely eliminating cold-start latency spikes.
- Option B: Pinging every 60 minutes only warms a single container and cannot handle concurrent bursts.
- Option C masks slow performance by waiting longer, frustrating mobile app users.
- Option D reintroduces server management, patching, and scaling bottlenecks.

**References:**
- AWS Lambda Developer Guide: Provisioned Concurrency
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 18 [SAA-C03-D3-Q086]

**Task Statement 3.1**

Global field researchers in remote locations across South America, Africa, and Australia need to upload multi-gigabyte geological survey video files to an Amazon S3 bucket located in `us-east-1`. Uploads over the public internet are frequently interrupted and take hours to complete. What feature should the architect enable to accelerate global file uploads to S3?

- **A)** Amazon S3 Transfer Acceleration
- **B)** Amazon S3 Cross-Region Replication
- **C)** AWS DataSync
- **D)** Amazon CloudFront Signed URLs

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. It takes advantage of Amazon CloudFront's globally distributed edge locations. As data arrives at an edge location, it is routed to Amazon S3 over an optimized, congestion-free network path on the AWS private backbone.
- Option B: CRR replicates objects between S3 buckets after they have already been uploaded.
- Option C: DataSync requires deploying an on-premises agent VM, which remote mobile field researchers cannot deploy.
- Option D: Signed URLs authorize downloads/uploads, but do not route traffic over CloudFront edge ingress acceleration.

**References:**
- Amazon S3 User Guide: Amazon S3 Transfer Acceleration
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 19 [SAA-C03-D3-Q087]

**Task Statement 3.1**

An architect is designing an application that will write over 50,000 objects per second to an Amazon S3 bucket. In the past, applications experienced 503 Slow Down throttling errors when uploading at this volume. How does Amazon S3 handle prefix scaling, and what is the best practice for high request rates?

- **A)** S3 automatically scales to support at least 3,500 PUT/POST/DELETE and 5,500 GET/HEAD requests per second per prefix. Distributing objects across multiple distinct prefixes allows horizontal request rate scaling.
- **B)** S3 requires prepending a random hex hash to the beginning of the bucket name to force rebalancing.
- **C)** The architect must open a support ticket 24 hours in advance to pre-warm the S3 bucket.
- **D)** All files must be combined into a single 5 TB archive before uploading.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon S3 automatically scales to handle high request rates. S3 delivers at least 3,500 PUT/COPY/POST/DELETE or 5,500 GET/HEAD requests per second per partitioned prefix. By distributing object keys across multiple distinct logical prefixes (e.g., `bucket/folder1/`, `bucket/folder2/`), an application can achieve hundreds of thousands of requests per second horizontally.
- Option B: Prepending random hex hashes was an old legacy requirement prior to S3's automated prefix partitioning upgrade in 2018; it is no longer necessary.
- Option C: S3 buckets do not require pre-warming tickets.
- Option D is an anti-pattern that creates single-object bottlenecks.

**References:**
- Amazon S3 User Guide: Optimizing S3 Performance
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 20 [SAA-C03-D3-Q088]

**Task Statement 3.1**

A data analytics pipeline processes files on an Amazon EFS file system. Workload demand is spiky and unpredictable: for several hours a day, hundreds of compute workers read and write data simultaneously at speeds exceeding 1,000 MB/s, while during the rest of the day activity is minimal. The architect wants throughput to scale automatically to match workload activity without pre-provisioning throughput or managing burst credits. Which EFS throughput mode should be chosen?

- **A)** Bursting Throughput mode
- **B)** Provisioned Throughput mode
- **C)** Elastic Throughput mode
- **D)** Static Throughput mode

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
Amazon EFS Elastic Throughput mode automatically scales throughput capacity up or down to meet unpredictable application demands, supporting throughput up to multiple gigabytes per second with zero provisioning or management overhead. You pay only for the throughput consumed.
- Option A: Bursting throughput ties throughput to storage capacity; small storage volumes run out of burst credits during intense spikes.
- Option B: Provisioned throughput requires estimating and paying for fixed throughput 24/7, resulting in high idle costs during off-peak hours.
- Option D is not an EFS mode.

**References:**
- Amazon EFS User Guide: Elastic Throughput
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 21 [SAA-C03-D3-Q089]

**Task Statement 3.2**

A financial company needs to deploy a containerized microservices application using Docker. The operations team wants a serverless compute engine where they do not have to provision, configure, patch, or scale underlying EC2 virtual machine instances or manage cluster capacity. Which compute platform should be selected?

- **A)** Amazon ECS with an EC2 Launch Type
- **B)** Amazon ECS with AWS Fargate Launch Type
- **C)** Amazon EC2 Spot Fleet
- **D)** AWS Elastic Beanstalk Multicontainer Docker on EC2

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Fargate is a serverless, pay-as-you-go compute engine for containers compatible with Amazon ECS and Amazon EKS. With Fargate, you do not have to manage servers, handle OS patching, or provision cluster capacity; AWS manages the underlying infrastructure automatically and you pay only for the vCPU and memory resources requested by your container tasks.
- Option A requires managing, scaling, and patching an EC2 cluster.
- Option C requires managing EC2 instances and handling Spot interruptions.
- Option D provisions and manages EC2 instances behind the scenes.

**References:**
- Amazon ECS User Guide: AWS Fargate
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 22 [SAA-C03-D3-Q090]

**Task Statement 3.3**

An e-commerce business needs to run interactive ad-hoc SQL queries against 50 TB of web clickstream data stored in Apache Parquet format in an Amazon S3 data lake. The queries are run occasionally by business analysts, and the team does not want to manage or pay for a continuously running 24/7 database cluster. Which service is best suited?

- **A)** Amazon Athena
- **B)** Amazon Redshift with a 4-node cluster
- **C)** Amazon RDS for PostgreSQL
- **D)** Amazon OpenSearch Service

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL. Athena is completely serverless—there is no infrastructure to manage or cluster to maintain, and you pay only for the queries you run (priced per terabyte of data scanned). Using columnar formats like Parquet drastically reduces costs and accelerates query performance.
- Option B: Redshift requires maintaining an active cluster with continuous running costs, which is uneconomical for occasional queries.
- Option C: RDS requires loading data into a relational database with fixed EBS storage limits.
- Option D is an indexing search engine, not an ad-hoc serverless SQL engine for S3 Parquet data.

**References:**
- Amazon Athena User Guide
- AWS Well-Architected Performance and Cost Pillars

</details>

---

### Question 23 [SAA-C03-D3-Q091]

**Task Statement 3.3**

A gaming company requires a database that provides sub-millisecond read and write latencies for player inventory data, but also requires full transactional ACID compliance with zero data loss across multi-AZ hardware failures. Traditional caching solutions lose data on unexpected reboots. Which AWS database service meets this requirement?

- **A)** Amazon ElastiCache for Memcached
- **B)** Amazon MemoryDB for Redis
- **C)** Amazon S3 Standard
- **D)** Amazon Redshift

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon MemoryDB for Redis is a Redis-compatible, durable, in-memory database service designed for ultra-fast performance. Unlike traditional caches, MemoryDB uses a distributed Multi-AZ transaction log to ensure durability and zero data loss, delivering microsecond read latencies, single-digit millisecond write latencies, and full ACID compliance.
- Option A: Memcached is volatile and has no persistence or multi-AZ replication.
- Option C: S3 has millisecond latencies, not in-memory microsecond transactional speeds.
- Option D: Redshift is an analytical OLAP warehouse, not an ultra-fast transactional OLTP store.

**References:**
- Amazon MemoryDB for Redis Developer Guide
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 24 [SAA-C03-D3-Q092]

**Task Statement 3.4**

A company wants to connect two Amazon VPCs (`VPC-A` and `VPC-B`) in the same AWS Region so that EC2 instances can communicate with each other using private IPv4 addresses. The connection must provide the lowest possible network latency, maximum bandwidth, no single point of failure, and no bandwidth bottlenecks. Which networking feature should be deployed?

- **A)** VPC Peering Connection
- **B)** AWS Site-to-Site VPN over an Internet Gateway
- **C)** NAT Gateway to NAT Gateway connection
- **D)** AWS Storage Gateway

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
A VPC Peering connection is a direct networking connection between two VPCs that routes traffic entirely over existing AWS infrastructure using private IP addresses. It introduces no single point of failure and no bandwidth bottlenecks (instances communicate at full line-rate capacity without hardware hops), providing the lowest latency connection possible between two VPCs.
- Option B: Site-to-Site VPN limits bandwidth to 1.25 Gbps per tunnel, incurs encryption overhead, and travels over public endpoints.
- Option C is technically nonsensical.
- Option D is for hybrid storage integration.

**References:**
- Amazon VPC User Guide: What is VPC Peering?
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 25 [SAA-C03-D3-Q093]

**Task Statement 3.3**

A retail analytics team queries a multi-terabyte Amazon Redshift data warehouse. During end-of-quarter financial audits, hundreds of analysts submit complex queries simultaneously, causing queries to queue up and wait for compute resources. What Redshift feature should be enabled to automatically handle sudden bursts in query concurrency without manual intervention?

- **A)** Amazon Redshift Concurrency Scaling
- **B)** Cross-Region Snapshot Copy
- **C)** Single-AZ Standby Node
- **D)** Amazon Redshift Spectrum with EC2 instances

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Redshift Concurrency Scaling automatically provisions and adds transient cluster capacity in seconds as query concurrency surges. It supports virtually unlimited concurrent users and queries with consistently fast query performance, automatically scaling down when demand subsides.
- Option B is for disaster recovery snapshot backups.
- Option C does not expand query concurrency.
- Option D (Spectrum) allows querying data in S3, but does not dynamically burst Redshift warehouse cluster compute capacity for concurrent queries.

**References:**
- Amazon Redshift Database Developer Guide: Working with Concurrency Scaling
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 26 [SAA-C03-D3-Q094]

**Task Statement 3.4**

A media streaming company delivers premium on-demand video to paid subscribers via Amazon CloudFront. The company wants to prevent unauthorized sharing of video links by ensuring that only authenticated users who purchased a specific movie can access its files, and requests must expire after 2 hours. What CloudFront security feature satisfies this requirement?

- **A)** CloudFront Signed URLs or Signed Cookies
- **B)** Origin Access Control (OAC) with public bucket policy
- **C)** AWS WAF IP Set allowlist
- **D)** Route 53 Geoproximity routing

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon CloudFront Signed URLs and Signed Cookies allow you to control access to private content. By generating a signed URL with an expiration policy (e.g., 2 hours) and signed by a trusted key group, only users possessing the cryptographically signed link can stream the video through CloudFront.
- Option B: OAC ensures only CloudFront can read from the S3 origin, but does not authenticate individual end users.
- Option C: IP allowlisting fails because mobile users have dynamic IPs.
- Option D is for geographic DNS routing, not private media entitlement.

**References:**
- Amazon CloudFront Developer Guide: Serving Private Content with Signed URLs
- AWS Well-Architected Security and Performance Pillars

</details>

---

### Question 27 [SAA-C03-D3-Q095]

**Task Statement 3.2**

An architect is designing an event-driven architecture that processes lightweight HTTP requests requiring minimal compute overhead (such as HTTP header normalization and URL rewrites) directly at the CloudFront edge locations with sub-millisecond execution latencies and scale of up to 10,000,000 requests per second. Which edge computing option should be selected?

- **A)** CloudFront Functions
- **B)** Lambda@Edge
- **C)** Amazon EC2 C7g instances in each region
- **D)** AWS Fargate containers

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
CloudFront Functions is a lightweight edge compute capability natively integrated into CloudFront. It executes short-lived JavaScript functions directly at hundreds of CloudFront edge locations with sub-millisecond execution times and massive scale (millions of RPS) at 1/6th the cost of Lambda@Edge, ideal for viewer-request and viewer-response header manipulations, URL rewrites, and access token validation.
- Option B: Lambda@Edge runs in regional edge caches (not all edge locations), supports longer executions (up to 30 seconds) and network access, but has higher latency and cost.
- Options C and D require routing traffic back to regional compute, introducing geographic network latency.

**References:**
- Amazon CloudFront Developer Guide: Choosing Between CloudFront Functions and Lambda@Edge
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 28 [SAA-C03-D3-Q096]

**Task Statement 3.4**

An enterprise connects its corporate data center to AWS using two AWS Site-to-Site VPN connections. Each VPN tunnel provides 1.25 Gbps of bandwidth. The company needs to aggregate the bandwidth of both VPN connections to achieve up to 2.5 Gbps of combined throughput for heavy file transfers. What routing protocol configuration must be enabled?

- **A)** Static routing with equal metric weights
- **B)** Dynamic routing using BGP (Border Gateway Protocol) with Equal-Cost Multi-Path (ECMP) routing enabled on an AWS Transit Gateway
- **C)** Spanning Tree Protocol (STP)
- **D)** DNS round-robin routing

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Transit Gateway supports Equal-Cost Multi-Path (ECMP) routing across multiple BGP-enabled VPN connections. By configuring dynamic BGP routing with ECMP, traffic is load-balanced across multiple VPN tunnels simultaneously, allowing customers to aggregate bandwidth beyond the 1.25 Gbps limit of a single tunnel.
- Option A: Static routing does not support active-active ECMP aggregation on standard VPNs.
- Option C is a Layer 2 protocol used on Ethernet switches, not routed AWS VPN connections.
- Option D operates at the DNS layer and does not aggregate IP tunnel bandwidth.

**References:**
- AWS Transit Gateway User Guide: Transit Gateway Route Tables and ECMP
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

