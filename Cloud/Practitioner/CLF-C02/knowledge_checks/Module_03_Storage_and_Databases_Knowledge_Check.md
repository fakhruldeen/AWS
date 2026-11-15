# Module 03 Knowledge Check: Storage & Databases

### Questions
1. **Which Amazon S3 storage class automatically moves objects between access tiers based on changing access patterns without operational overhead or retrieval fees?**
   - A) S3 Standard
   - B) S3 Intelligent-Tiering
   - C) S3 One Zone-IA
   - D) S3 Glacier Flexible Recovery
2. **What is the designed data durability of the Amazon S3 Standard storage class over a given year?**
   - A) 99.9% (Three 9s)
   - B) 99.99% (Four 9s)
   - C) 99.999999999% (Eleven 9s)
   - D) 100%
3. **Which block storage service provides persistent, low-latency virtual disk volumes for Amazon EC2 instances within a single Availability Zone?**
   - A) Amazon S3
   - B) Amazon EBS
   - C) Amazon EFS
   - D) AWS Storage Gateway
4. **Which storage service provides a fully managed, serverless, POSIX-compliant shared file system that can be mounted concurrently by hundreds of EC2 instances across multiple AZs?**
   - A) Amazon EBS
   - B) Amazon EFS
   - C) Amazon S3
   - D) AWS Snowball Edge
5. **Which Amazon S3 storage class offers the lowest storage cost when data is accessed less than once a year and retrieval times of several hours are acceptable?**
   - A) S3 Standard-IA
   - B) S3 Glacier Deep Archive
   - C) S3 Express One Zone
   - D) S3 Outposts
6. **What is the primary architectural purpose of deploying an Amazon RDS database in a Multi-AZ configuration?**
   - A) Scaling read performance across worldwide locations
   - B) High Availability and automated synchronous failover in case of AZ outage
   - C) Reducing database licensing fees
   - D) Running complex analytical aggregation queries
7. **Which database engine is fully managed, serverless, and provides single-digit millisecond latency with a NoSQL key-value data model?**
   - A) Amazon RDS MySQL
   - B) Amazon Aurora
   - C) Amazon DynamoDB
   - D) Amazon Redshift
8. **What feature of Amazon S3 allows you to keep multiple versions of an object in the same bucket to protect against accidental deletions and overwrites?**
   - A) S3 Object Lock
   - B) S3 Versioning
   - C) S3 Cross-Region Replication
   - D) S3 Transfer Acceleration
9. **Which AWS database service is designed specifically for complex Online Analytical Processing (OLAP) and petabyte-scale data warehousing?**
   - A) Amazon DynamoDB
   - B) Amazon RDS PostgreSQL
   - C) Amazon Redshift
   - D) Amazon DocumentDB
10. **Which managed in-memory caching service supports Redis and Memcached to accelerate database read operations?**
    - A) Amazon ElastiCache
    - B) Amazon MemoryDB
    - C) Amazon DynamoDB DAX
    - D) AWS AppSync

---

### Answer Key & Explanations
| Q# | Answer | Key Concept Reference |
| :---: | :---: | :--- |
| **1** | **B** | S3 Intelligent-Tiering automatically moves objects between tiers with zero retrieval fees. |
| **2** | **C** | Amazon S3 is architected for 99.999999999% (11 9s) annual data durability across AZs. |
| **3** | **B** | Amazon EBS provides network-attached block storage volumes for individual EC2 instances. |
| **4** | **B** | Amazon EFS provides concurrent POSIX shared file storage accessible across multiple AZs. |
| **5** | **B** | S3 Glacier Deep Archive provides the lowest storage cost in AWS (\$0.00099/GB/month). |
| **6** | **B** | Multi-AZ RDS synchronously replicates to a standby instance in another AZ for high availability. |
| **7** | **C** | Amazon DynamoDB is AWS's flagship serverless NoSQL key-value and document database. |
| **8** | **B** | S3 Versioning stores current and noncurrent versions, preventing permanent accidental deletes. |
| **9** | **C** | Amazon Redshift is a columnar data warehouse optimized for analytical queries at petabyte scale. |
| **10** | **A** | Amazon ElastiCache delivers sub-millisecond responses by caching frequently queried data in RAM. |
