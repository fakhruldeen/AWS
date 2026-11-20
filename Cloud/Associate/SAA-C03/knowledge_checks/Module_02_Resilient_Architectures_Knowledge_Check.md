# Module 02: Designing Resilient & High-Availability Architectures — Knowledge Check

> **Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Module 2: Decoupled Messaging, High Availability & Disaster Recovery  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 2 materials and completing Lab 02, Lab 03, and Lab 04. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
A web application frontend handles sudden flash sales by putting orders into a queue for backend processing. Which service decouples the tiers so that backend workers can consume messages asynchronously without losing requests?

- **A.** Amazon SQS Standard Queue
- **B.** Amazon Route 53
- **C.** Amazon CloudFront
- **D.** AWS Direct Connect

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon SQS** provides a durable, loosely coupled buffer between the web tier and worker instances. Spikes in order traffic are stored safely in the queue while backend workers process messages at a steady pace.
</details>

---

### Question 2
A financial system requires transactions to be processed in strict chronological sequence, with duplicates automatically detected and suppressed. What messaging solution must be selected?

- **A.** Amazon SQS Standard Queue
- **B.** Amazon SQS FIFO Queue
- **C.** Amazon SNS Standard Topic
- **D.** Amazon Kinesis Data Firehose

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Amazon SQS FIFO** (First-In-First-Out) queues preserve the exact order in which messages are sent and received, and enforce exactly-once processing via duplicate message deduplication (`MessageDeduplicationId`).
</details>

---

### Question 3
An e-commerce order event needs to be delivered simultaneously to three separate microservices (Inventory, Shipping, and Billing). What design pattern achieves this?

- **A.** Publish to an Amazon SNS Topic with subscriptions to three separate Amazon SQS Queues (Fan-Out pattern).
- **B.** Publish to a single Amazon SQS Queue read by all three services simultaneously.
- **C.** Make three sequential synchronous HTTP POST requests from the web server.
- **D.** Write data to Amazon S3 and trigger a daily batch job.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- The **SNS-to-SQS Fan-Out pattern** publishes an event once to an SNS topic, which fans out and delivers duplicate copies to multiple subscribed SQS queues. Each downstream microservice polls its own queue independently without interfering with others.
</details>

---

### Question 4
An architect is designing an automated failover strategy for an Amazon RDS for MySQL database. If an Availability Zone fails, the database must fail over automatically with zero data loss. Which configuration provides this?

- **A.** RDS MySQL Single-AZ with automated backups
- **B.** RDS MySQL Multi-AZ deployment with synchronous physical standby
- **C.** RDS MySQL with an asynchronous Read Replica in the same AZ
- **D.** RDS MySQL with an S3 cross-region export

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- An **Amazon RDS Multi-AZ deployment** provisions a synchronous physical standby replica in a different Availability Zone. Writes are committed synchronously to both AZs. If the primary instance fails, RDS automatically flips the DNS endpoint to the standby in under 60 seconds with zero data loss (RPO = 0).
</details>

---

### Question 5
A company needs a cross-region disaster recovery solution for an Aurora relational database with an RPO of less than 1 second and an RTO of less than 1 minute. Which feature fulfills this?

- **A.** Amazon Aurora Global Database
- **B.** Daily automated snapshot copy across regions
- **C.** AWS Database Migration Service (DMS)
- **D.** Amazon S3 Cross-Region Replication of database logs

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon Aurora Global Database** uses storage-level replication to replicate database writes to up to 5 secondary AWS regions in under 1 second (RPO < 1s). In the event of a regional outage, a secondary region can be promoted to a read-write primary in under 1 minute (RTO < 1m).
</details>

---

### Question 6
An Auto Scaling group scales in during low traffic, terminating an EC2 instance. However, in-flight customer HTTP connections are abruptly terminated with connection reset errors. What feature should be enabled on the Application Load Balancer target group?

- **A.** Sticky Sessions
- **B.** Deregistration Delay (Connection Draining)
- **C.** Cross-Zone Load Balancing
- **D.** Deletion Protection

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Deregistration Delay** (also known as Connection Draining) instructs the ALB to stop sending new incoming requests to the terminating instance while allowing active in-flight requests to complete up to a configurable timeout (default 300 seconds).
</details>

---

### Question 7
A company requires static public IP addresses for firewall allowlisting across 3 Availability Zones, and needs to handle millions of low-latency raw TCP/UDP requests per second. Which load balancer should be used?

- **A.** Application Load Balancer (ALB)
- **B.** Network Load Balancer (NLB)
- **C.** Classic Load Balancer (CLB)
- **D.** Gateway Load Balancer (GWLB)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Network Load Balancer (NLB)** operates at Layer 4 (TCP/UDP/TLS), can process millions of requests per second with ultra-low latency, and provides a fixed, static Anycast IP address (or Elastic IP) per Availability Zone.
</details>

---

### Question 8
Which Disaster Recovery strategy maintains a running, scaled-down duplicate of the entire production stack in a secondary region at all times, ready to quickly scale out during an emergency?

- **A.** Backup and Restore
- **B.** Pilot Light
- **C.** Warm Standby
- **D.** Multi-Site Active-Active

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**

**Explanation:**
- **Warm Standby** maintains a scaled-down but fully functional running copy of the entire production environment in the secondary region. Failover takes minutes by scaling out the compute fleet and updating DNS.
- **Pilot Light** only keeps the core database running; compute is not running.
</details>

---

### Question 9
An Auto Scaling worker fleet processes messages from an SQS queue. CPU utilization is consistently low (<10%) even when 50,000 messages are waiting in the queue. How should the Auto Scaling policy be driven?

- **A.** Scale based on EC2 NetworkIn
- **B.** Scale based on a custom CloudWatch metric calculating Backlog per Instance (`Queue Depth / Number of Instances`)
- **C.** Scale based on EC2 DiskReadOps
- **D.** Use a scheduled scaling policy every hour

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- For queue-driven workloads where CPU does not correlate with backlog, the AWS Well-Architected recommendation is to compute the **Backlog per Instance** ratio. This tells the Auto Scaling group exactly how many worker instances are needed to process the pending message backlog within an acceptable time window.
</details>

---

### Question 10
An architect needs a central service to coordinate multi-step workflows with sequential tasks, parallel execution, retries, and automated rollback logic (compensating transactions) if a payment fails. Which service should be used?

- **A.** AWS Step Functions
- **B.** Amazon SQS
- **C.** Amazon SNS
- **D.** AWS CodePipeline

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **AWS Step Functions** coordinates distributed microservices into visual serverless state machines. It natively supports the Saga pattern: handling retries, error catching, conditional branching, and triggering compensating rollbacks while tracking execution history.
</details>
