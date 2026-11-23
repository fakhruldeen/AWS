# AWS Certified Solutions Architect - Associate (SAA-C03)
## Domain 2: Design Resilient Architectures (26%)

> **Focus:** Official AWS Exam Objectives for Domain 2: Design Resilient Architectures  
> **Total Scenario Questions:** 32  

---

### Question 01 [SAA-C03-D2-Q037]

**Task Statement 2.1**

An online retail platform experiences sudden flash sales where thousands of customers place orders simultaneously. The frontend web tier handles the traffic spikes well, but the backend order processing service gets overwhelmed and drops orders. How can the solutions architect decouple the tiers to ensure no orders are lost during traffic surges?

- **A)** Upgrade the backend EC2 instances to the largest available compute-optimized instance type.
- **B)** Place an Amazon SQS Standard queue between the web tier and backend processing workers, and configure an Auto Scaling group for the workers based on the ApproximateNumberOfMessagesVisible metric.
- **C)** Use an Amazon Kinesis Data Firehose delivery stream directly connected to an Amazon Aurora database.
- **D)** Configure sticky sessions on the Application Load Balancer to bind each customer to a single web server.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Decoupling architectural tiers using an Amazon SQS Standard queue allows asynchronous processing and buffers incoming spikes. The web tier writes order payloads directly to the SQS queue, and an Auto Scaling group of backend worker instances scales dynamically based on queue depth (`ApproximateNumberOfMessagesVisible` / backlog per instance metric). This ensures zero order loss and automatic elasticity.
- Option A is vertical scaling; it does not decouple components and still suffers from finite capacity limits.
- Option C is designed for streaming data loading to S3/Redshift, not loosely coupled microservice request processing.
- Option D binds users to specific web servers, which hinders horizontal scaling and does not solve backend database congestion.

**References:**
- AWS Well-Architected Reliability Pillar
- Amazon SQS Developer Guide: Architecture Patterns

</details>

---

### Question 02 [SAA-C03-D2-Q038]

**Task Statement 2.1**

A financial banking service processes stock trading transactions. Business requirements dictate that transactions must be processed in the exact order they were submitted, no transaction can be processed more than once (exactly-once processing), and throughput will not exceed 3,000 transactions per second with batching. Which AWS messaging solution must be selected?

- **A)** Amazon SQS Standard Queue
- **B)** Amazon SQS FIFO Queue with high throughput mode enabled
- **C)** Amazon SNS Standard Topic
- **D)** Amazon SimpleDB

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon SQS FIFO (First-In-First-Out) queues guarantee strict chronological order processing (`MessageGroupId`) and exactly-once processing with duplicate message deduplication (`MessageDeduplicationId`). With high throughput mode enabled, SQS FIFO queues support up to 3,000 transactions per second with batching (or 300 msg/sec without batching).
- Option A: SQS Standard queues provide best-effort ordering and at-least-once delivery (duplicates may occur).
- Option C: SNS Standard topics do not guarantee strict FIFO message order without a FIFO topic and queue.
- Option D is a legacy simple database, not a distributed queue.

**References:**
- Amazon SQS Developer Guide: FIFO Queues
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 03 [SAA-C03-D2-Q039]

**Task Statement 2.1**

When a new customer purchases a product on an e-commerce platform, three distinct downstream services must process the event: the Inventory Service, the Shipping Service, and the Email Notification Service. The architect wants to implement a fan-out architecture where publishing the event once delivers it reliably to all three services simultaneously and asynchronously. How should this be designed?

- **A)** The web tier publishes the purchase event to an Amazon SNS Topic. The three downstream services each have their own Amazon SQS queue subscribed to the SNS Topic.
- **B)** The web tier writes the event to a single Amazon SQS Standard queue and all three services poll the same queue simultaneously.
- **C)** The web tier makes sequential synchronous HTTP POST calls to the REST endpoints of each service with a 5-second timeout.
- **D)** Store the purchase event in an Amazon DynamoDB table and trigger a daily batch cron job to read new records.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
The SNS-to-SQS fan-out pattern is a cornerstone of resilient cloud architecture. Publishing a single message to an Amazon SNS topic replicates and pushes that message to multiple subscribed SQS queues. Each downstream service consumes messages from its own dedicated queue independently, ensuring fault isolation and asynchronous processing.
- Option B: Multiple consumers on a single SQS queue compete for messages; only one worker processes each message, meaning the other two services will not receive it.
- Option C introduces tight coupling: if any single downstream service fails or slows down, the upstream web tier blocks and risks cascading failures.
- Option D introduces high latency (24 hours) and fails real-time processing requirements.

**References:**
- Amazon SNS Developer Guide: Fanout to Amazon SQS Queues
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 04 [SAA-C03-D2-Q040]

**Task Statement 2.1**

An asynchronous message processing system occasionally encounters malformed JSON payloads (poison-pill messages) that cause worker threads to crash repeatedly. As a result, these failed messages remain in the queue, are retried continuously, and prevent other valid messages from being processed. What mechanism should the architect configure to isolate these problematic messages?

- **A)** Increase the SQS queue Default Visibility Timeout to 12 hours.
- **B)** Configure an Amazon SQS Dead-Letter Queue (DLQ) with a Redrive Policy specifying `maxReceiveCount = 3`.
- **C)** Enable S3 Lifecycle expiration on the SQS queue.
- **D)** Write a Lambda function to purge the entire queue every 15 minutes.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
An Amazon SQS Dead-Letter Queue (DLQ) isolates messages that fail processing after a specified number of attempts (`maxReceiveCount`). When a message is received and returned to the queue without successful deletion `maxReceiveCount` times, Amazon SQS automatically moves it to the DLQ. This unblocks the main queue and allows engineers to inspect and debug malformed payloads.
- Option A merely delays reprocessing of the poison pill and does not isolate it.
- Option C: S3 lifecycle rules apply to Amazon S3 buckets, not SQS queues.
- Option D wipes all pending valid messages in the queue, causing catastrophic data loss.

**References:**
- Amazon SQS Developer Guide: Dead-Letter Queues
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 05 [SAA-C03-D2-Q041]

**Task Statement 2.1**

An architect is designing an e-commerce order fulfillment pipeline that involves multiple distributed steps: validating inventory, charging the customer credit card, scheduling shipment, and sending a receipt. If the credit card payment fails, the allocated inventory must be automatically released (compensating transaction). Which AWS service should orchestrate this stateful workflow?

- **A)** AWS Step Functions Standard Workflows
- **B)** Amazon SQS Standard Queues
- **C)** AWS Systems Manager Run Command
- **D)** Amazon CloudWatch Events

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Step Functions Standard Workflows coordinates distributed microservices, Lambda functions, and AWS services into visual serverless state machines. It natively supports the Saga pattern: handling retries, error catching, conditional branching, human approvals, and triggering compensating transactions (e.g., releasing inventory if payment fails) while maintaining state history for up to 1 year.
- Option B provides simple message buffering, but does not manage workflow state, branching, or compensating rollbacks.
- Option C is for running administrative shell commands across EC2 fleets.
- Option D (EventBridge) routes discrete events, but does not maintain end-to-end multi-step state machine execution state.

**References:**
- AWS Step Functions Developer Guide: Saga Pattern
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 06 [SAA-C03-D2-Q042]

**Task Statement 2.2**

An enterprise requires a highly available relational database deployment for a production ERP application across multiple Availability Zones. The database must support automated failover with minimal downtime (< 30 seconds), zero data loss, independent scaling of read replicas (up to 15 replicas) that share a common distributed storage volume, and automated storage volume growth up to 128 TiB. Which database engine best meets these requirements?

- **A)** Amazon RDS for MySQL Single-AZ
- **B)** Amazon Aurora MySQL Multi-AZ Cluster
- **C)** Amazon DynamoDB with Global Tables
- **D)** Amazon EC2 instance running self-managed PostgreSQL on EBS gp3

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon Aurora is a cloud-native relational database that replicates storage 6 ways across 3 Availability Zones on a self-healing, distributed storage volume that auto-scales up to 128 TiB. Aurora supports up to 15 read replicas that share the same underlying storage without replication lag bottlenecks, and achieves automated failover in typically under 30 seconds.
- Option A: Single-AZ RDS has no automated failover and represents a single point of failure.
- Option C: DynamoDB is a NoSQL key-value/document database, not a relational SQL engine for ERP.
- Option D requires significant administrative overhead for self-managed clustering, failover scripts, and storage scaling.

**References:**
- Amazon Aurora User Guide: Aurora Storage and Replication
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 07 [SAA-C03-D2-Q043]

**Task Statement 2.2**

A multinational corporation operates an Amazon Aurora PostgreSQL database in `us-east-1`. Disaster recovery governance mandates that in the event of an entire regional AWS outage, the database must be recoverable in a secondary region (`us-west-2`) with an RPO of less than 1 second and an RTO of less than 1 minute. Which Aurora feature delivers this level of business continuity?

- **A)** Amazon Aurora Global Database
- **B)** Automated snapshot copy across regions using a daily AWS Lambda function
- **C)** AWS Database Migration Service (AWS DMS) running over public internet
- **D)** Amazon S3 Cross-Region Replication of exported CSV dumps

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Aurora Global Database provides cross-region replication directly at the storage layer with typical replication latencies of under 1 second (RPO < 1 sec). In the event of a regional failure, a secondary region can be promoted to take full read-write workloads in under 1 minute (RTO < 1 min) with zero data loss on clean failovers.
- Option B has an RPO of up to 24 hours (snapshot interval) and an RTO of tens of minutes to restore a multi-terabyte cluster.
- Option C introduces latency, operational overhead, and replication instability compared to Aurora's dedicated storage replication engine.
- Option D is an asynchronous batch dump that cannot achieve sub-second RPO.

**References:**
- Amazon Aurora User Guide: Aurora Global Databases
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 08 [SAA-C03-D2-Q044]

**Task Statement 2.2**

A web application hosted on an Auto Scaling group of EC2 instances behind an Application Load Balancer experiences unpredictable traffic bursts during marketing campaigns. The solutions architect wants the fleet to automatically scale in and out to maintain the target metric of 1,000 HTTP requests per target instance. Which Auto Scaling policy should be configured?

- **A)** Simple Scaling Policy based on EC2 NetworkIn
- **B)** Target Tracking Scaling Policy based on the `ALBRequestCountPerTarget` metric
- **C)** Step Scaling Policy based on EBS ReadBytes
- **D)** Scheduled Scaling Policy executing every 2 hours

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
A Target Tracking Scaling Policy works like a thermostat: you specify a target value for a predefined metric, such as `ALBRequestCountPerTarget = 1000`. Amazon EC2 Auto Scaling automatically adjusts the capacity of the group by creating and managing the necessary CloudWatch alarms to keep the metric at or near the target value.
- Option A: Simple scaling policies are slower to react to varying load magnitudes compared to target tracking.
- Option C: EBS ReadBytes does not correlate directly with incoming HTTP traffic spikes.
- Option D: Scheduled scaling only works for predictable, scheduled traffic, not unpredictable marketing bursts.

**References:**
- Amazon EC2 Auto Scaling User Guide: Target Tracking Scaling Policies
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 09 [SAA-C03-D2-Q045]

**Task Statement 2.2**

An Auto Scaling group terminates an EC2 instance during a scale-in event. However, active users currently connected to that instance experience broken sessions and connection reset errors. What two configurations should the architect apply to ensure graceful termination without dropping active in-flight requests? (Choose TWO)

- **A)** Enable Deregistration Delay (Connection Draining) on the Application Load Balancer target group.
- **B)** Configure an Auto Scaling Lifecycle Hook for instance termination (`EC2_INSTANCE_TERMINATING`) to allow the instance to complete processing before termination.
- **C)** Assign Elastic IPs to all instances in the private subnet.
- **D)** Disable Cross-Zone Load Balancing on the ALB.
- **E)** Enable sticky sessions with a cookie expiration of 365 days.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A, B`

**Detailed Explanation:**
Enabling Deregistration Delay on the ALB target group tells the load balancer to stop sending new requests to the terminating instance while allowing in-flight connections to complete (up to the deregistration timeout, default 300 seconds). Combining this with an Auto Scaling Lifecycle Hook (`EC2_INSTANCE_TERMINATING`) pauses the termination sequence, putting the instance into a `Terminating:Wait` state until active work completes or the hook times out.
- Option C does not prevent connection termination during instance shutdown.
- Option D degrades traffic distribution across Availability Zones.
- Option E forces users to stay on specific instances and does not help when the instance is being terminated.

**References:**
- Elastic Load Balancing User Guide: Deregistration Delay
- Amazon EC2 Auto Scaling User Guide: Lifecycle Hooks

</details>

---

### Question 10 [SAA-C03-D2-Q046]

**Task Statement 2.2**

A multiplayer gaming platform requires an architectural solution capable of handling millions of concurrent raw TCP connections with sub-millisecond latencies. The clients require static public IP addresses to allowlist in firewall rules across 3 Availability Zones. Which AWS load balancer must be chosen?

- **A)** Application Load Balancer (ALB)
- **B)** Network Load Balancer (NLB)
- **C)** Classic Load Balancer (CLB)
- **D)** Gateway Load Balancer (GWLB)

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Network Load Balancer (NLB) operates at the transport layer (Layer 4 - TCP/UDP/TLS) and is capable of handling millions of requests per second with ultra-low latencies. Crucially, NLBs provide a dedicated, static Anycast IP address per Availability Zone (or allow bringing your own Elastic IPs), satisfying strict corporate firewall allowlisting requirements.
- Option A: Application Load Balancers operate at Layer 7 (HTTP/HTTPS) and do not provide static IPs per AZ; their DNS records resolve to changing IP addresses.
- Option C: Classic Load Balancers are legacy and do not provide static IP addresses.
- Option D: Gateway Load Balancers are designed for deploying third-party virtual network appliances (firewalls, IDS/IPS).

**References:**
- Elastic Load Balancing User Guide: Network Load Balancers
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 11 [SAA-C03-D2-Q047]

**Task Statement 2.2**

An Application Load Balancer distributes incoming web requests across EC2 instances deployed in two Availability Zones (`us-east-1a` with 8 instances, and `us-east-1b` with 2 instances). By default, instances in `us-east-1b` are receiving 400% more traffic per instance than those in `us-east-1a`, causing high CPU utilization in `us-east-1b`. What feature should be enabled on the ALB to distribute requests evenly across all 10 instances regardless of their AZ?

- **A)** Sticky Sessions (Cookie Affinity)
- **B)** Cross-Zone Load Balancing
- **C)** Path-Based Routing
- **D)** ALB Deletion Protection

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Cross-Zone Load Balancing ensures that the load balancer nodes distribute incoming traffic evenly across all registered targets in all enabled Availability Zones. On an Application Load Balancer, cross-zone load balancing is enabled by default at the load balancer level (and configurable at the target group level). Without it, traffic is split 50/50 between the two AZs, causing the 2 instances in `us-east-1b` to absorb half of all traffic.
- Option A binds users to specific instances and exacerbates traffic imbalances.
- Option C routes traffic based on URL path (`/api`, `/images`), not across instances.
- Option D prevents accidental deletion of the load balancer via the console or API.

**References:**
- Elastic Load Balancing User Guide: Cross-Zone Load Balancing
- AWS Well-Architected Performance Efficiency Pillar

</details>

---

### Question 12 [SAA-C03-D2-Q048]

**Task Statement 2.2**

A global company hosts identical production web application stacks in `eu-west-1` (Ireland) and `ap-southeast-1` (Singapore). To minimize latency, European users should be directed to Ireland and Asian users should be directed to Singapore. Additionally, if the Ireland stack experiences an outage, European users must be automatically rerouted to Singapore. Which Amazon Route 53 configuration provides this capability?

- **A)** Route 53 Simple Routing with two A records.
- **B)** Route 53 Latency-Based Routing (or Geolocation Routing) associated with Route 53 Health Checks on both endpoints.
- **C)** Route 53 Weighted Routing with both weights set to 0.
- **D)** Route 53 Multivalue Answer Routing without health checks.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Route 53 Latency-Based Routing directs users to the AWS Region that provides the lowest network latency. When configured alongside Route 53 Health Checks, if an endpoint in `eu-west-1` becomes unhealthy, Route 53 detects the health-check failure and automatically falls back to routing queries to the healthy endpoint in `ap-southeast-1`.
- Option A: Simple routing cannot provide intelligent routing or automatic failover.
- Option C: A weight of 0 stops all traffic from routing to an endpoint.
- Option D: Multivalue routing returns multiple IP addresses randomly and does not provide latency-optimized geographic routing.

**References:**
- Amazon Route 53 Developer Guide: Latency-Based Routing
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 13 [SAA-C03-D2-Q049]

**Task Statement 2.2**

A corporate IT department is evaluating disaster recovery (DR) strategies for a non-critical internal billing reporting system. The business has determined that an RPO of 24 hours and an RTO of 12 hours are completely acceptable, and the primary objective is to minimize ongoing infrastructure running costs in the secondary region to near zero. Which DR strategy should the architect recommend?

- **A)** Multi-Site Active-Active
- **B)** Warm Standby
- **C)** Pilot Light
- **D)** Backup and Restore

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `D`

**Detailed Explanation:**
The Backup and Restore strategy is the most cost-effective disaster recovery approach. Data and server images (AMIs, snapshots) are backed up regularly to a secondary region (e.g., using AWS Backup). No compute or database instances run continuously in the secondary region during normal operations, keeping running costs at zero until a disaster requires restoring resources from backups.
- Option A (Multi-Site Active-Active) has the highest cost (running full infrastructure in both regions 24/7) with RPO/RTO near zero.
- Option B (Warm Standby) keeps a scaled-down but running duplicate of the stack, incurring continuous compute/database charges.
- Option C (Pilot Light) keeps core databases continuously running and replicating, which is unnecessary and costlier than Backup & Restore for a 24h RPO.

**References:**
- AWS Whitepaper: Disaster Recovery of Workloads on AWS
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 14 [SAA-C03-D2-Q050]

**Task Statement 2.2**

A company wants to implement a Pilot Light disaster recovery strategy between `us-east-1` (Primary) and `us-west-2` (DR). What characterizes a Pilot Light architecture?

- **A)** All web, application, and database servers are running at 100% full capacity in both regions at all times.
- **B)** Core data storage and databases are continuously running and replicating to the DR region, while compute servers (EC2 instances) are kept stopped or provisioned on demand via Infrastructure-as-Code (IaC) upon disaster declaration.
- **C)** Backups are saved on tape drives and shipped physically to an AWS data center once per month.
- **D)** Traffic is split 50/50 between both regions using an Application Load Balancer.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
In a Pilot Light disaster recovery strategy, the critical core foundation of the application—the database and persistent storage—is continuously running and replicating live data to the DR region (the 'pilot light'). The compute and application tiers are not running during normal operations; instead, AMIs and CloudFormation/Terraform templates are ready to quickly spin up the compute fleet when a failover occurs, yielding an RTO in tens of minutes with low idle cost.
- Option A describes Multi-Site Active-Active.
- Option C is obsolete on-premises physical backup.
- Option D describes Active-Active load sharing.

**References:**
- AWS Whitepaper: Disaster Recovery of Workloads on AWS - Pilot Light
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 15 [SAA-C03-D2-Q051]

**Task Statement 2.2**

A SaaS provider requires a Disaster Recovery plan that provides an RTO of under 10 minutes and an RPO of under 1 minute. The architecture must maintain a continuously running, scaled-down version of all core services (web, application, and database) in the secondary region, capable of immediately handling low-volume synthetic health checks and quickly scaling out to full production capacity during a primary outage. Which strategy is this?

- **A)** Backup and Restore
- **B)** Pilot Light
- **C)** Warm Standby
- **D)** Cold Standby

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `C`

**Detailed Explanation:**
Warm Standby maintains a scaled-down, but fully functional, running copy of the entire production environment in the secondary region at all times. Because all tiers (web, app, database) are already running and passing live health checks, failover can occur in minutes by simply scaling out the Auto Scaling groups and redirecting DNS traffic via Route 53.
- Option A (Backup and Restore) requires hours to provision infrastructure from scratch.
- Option B (Pilot Light) only runs the database; compute servers are not running and must be launched, taking longer than Warm Standby.
- Option D is another term for backup/restore or off-line systems.

**References:**
- AWS Whitepaper: Disaster Recovery of Workloads on AWS - Warm Standby
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 16 [SAA-C03-D2-Q052]

**Task Statement 2.2**

An architect is designing an active-active multi-region architecture for a global SaaS application running in `us-east-1` and `eu-west-1`. Users must experience near-zero RTO and RPO, and writes initiated in either region must be reflected in the other region within seconds with conflict resolution. Which combination of database and routing services should be selected?

- **A)** Amazon DynamoDB Global Tables and Amazon Route 53 with Geolocation Routing (or AWS Global Accelerator)
- **B)** Amazon RDS for MySQL with a cross-region Read Replica promoted via manual script
- **C)** Amazon S3 Standard with Glacier Lifecycle rules
- **D)** Amazon Redshift with a single leader node in `us-east-1`

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon DynamoDB Global Tables provides fully managed, multi-region, active-active multi-master replication with built-in conflict resolution ('last writer wins'). Paired with Route 53 Geolocation/Latency routing or AWS Global Accelerator, users in both North America and Europe write and read locally with single-digit millisecond latencies and automatic multi-region fault tolerance.
- Option B: RDS read replicas are read-only; they do not support active-active writes in both regions simultaneously.
- Option C: S3 and Glacier are object storage services, not transactional multi-master databases.
- Option D: Redshift is an analytical data warehouse, not an active-active transactional OLTP engine.

**References:**
- Amazon DynamoDB Developer Guide: Global Tables
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 17 [SAA-C03-D2-Q053]

**Task Statement 2.2**

A compliance framework requires financial records uploaded to an Amazon S3 bucket in `us-east-1` to be replicated to a destination bucket in `eu-central-1` within a strictly monitored Service Level Agreement (SLA) of 15 minutes, with CloudWatch metrics alerting if replication exceeds this threshold. What S3 feature satisfies this requirement?

- **A)** S3 Same-Region Replication (SRR)
- **B)** S3 Cross-Region Replication (CRR) with S3 Replication Time Control (S3 RTC)
- **C)** AWS DataSync running a scheduled job every 24 hours
- **D)** S3 Batch Operations executing weekly

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
S3 Replication Time Control (S3 RTC) is a feature of S3 Replication that provides a guaranteed SLA to replicate 99.99% of new objects within 15 minutes of upload. It includes detailed CloudWatch replication metrics (replication latency, pending bytes, pending operations) and alarm events.
- Option A replicates within the same region, failing the cross-region compliance mandate.
- Option C: DataSync scheduled every 24 hours cannot meet a 15-minute SLA.
- Option D: Batch Operations is for one-off manual batch jobs, not continuous SLA-backed automated replication.

**References:**
- Amazon S3 User Guide: S3 Replication Time Control (S3 RTC)
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 18 [SAA-C03-D2-Q054]

**Task Statement 2.1**

A company wants to route operational events from third-party SaaS vendors (such as Zendesk and Datadog) as well as internal microservices to multiple AWS targets (Lambda, SQS, Step Functions) based on the specific JSON content of the event payload. Which serverless event bus service should be utilized?

- **A)** Amazon Simple Queue Service (Amazon SQS)
- **B)** Amazon EventBridge
- **C)** Amazon Simple Notification Service (Amazon SNS)
- **D)** AWS CloudFormation

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon EventBridge is a serverless event bus service that ingests events from SaaS partners, custom microservices, and AWS services. It uses declarative Event Rules and JSON pattern matching (content-based filtering) to inspect event payloads and route them to over 20 AWS targets without writing custom polling or routing code.
- Option A: SQS is a point-to-point message queue; it does not evaluate JSON payload content or route to diverse targets.
- Option B: While SNS supports message attribute filtering, EventBridge is specifically integrated with SaaS partner sources and deep JSON payload schema filtering.
- Option D is an Infrastructure-as-Code service.

**References:**
- Amazon EventBridge User Guide
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 19 [SAA-C03-D2-Q055]

**Task Statement 2.2**

An architect is designing an asynchronous video transcoding workflow. When users upload videos to an S3 bucket, an event triggers an AWS Lambda function to initiate transcoding. The transcoding job can occasionally fail due to transient network issues. The architect must ensure that failed invocations are automatically captured and retained for developer debugging without losing any payload data. What should be configured?

- **A)** Increase the Lambda function memory to 10 GB.
- **B)** Configure an On-Failure Lambda Destination pointing to an Amazon SQS Dead-Letter Queue.
- **C)** Disable S3 event notifications and write a cron job on EC2.
- **D)** Deploy an Application Load Balancer in front of the Lambda function.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
For asynchronous Lambda invocations (such as those triggered by Amazon S3 bucket events), configuring an On-Failure Lambda Destination (or a Dead-Letter Queue pointing to Amazon SQS or Amazon SNS) ensures that when an invocation exhausts its built-in retry attempts (default 2 retries), the full execution context, stack trace, and original event payload are sent to the SQS queue for inspection.
- Option A increases compute resources but does not handle application errors or capture failed events.
- Option C replaces real-time event-driven processing with batch polling, increasing latency and operational overhead.
- Option D converts the invocation into a synchronous HTTP call, changing the architecture.

**References:**
- AWS Lambda Developer Guide: Configuring Destinations for Asynchronous Invocations
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 20 [SAA-C03-D2-Q056]

**Task Statement 2.2**

A solutions architect is deploying an Amazon RDS for MySQL database for a mission-critical web application. The application requires high availability, automated database maintenance failover, and zero data loss in the event of an Availability Zone outage. Which RDS configuration should be chosen?

- **A)** RDS MySQL Single-AZ with automated backups enabled
- **B)** RDS MySQL Multi-AZ deployment with a synchronous physical standby replica in another AZ
- **C)** RDS MySQL with an asynchronous Read Replica in the same AZ
- **D)** RDS MySQL deployed in a public subnet with an open security group

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
An Amazon RDS Multi-AZ deployment provisions a primary DB instance and synchronously replicates data to a standby physical replica in a different Availability Zone. In the event of an infrastructure failure, AZ outage, or planned maintenance, RDS automatically fails over to the standby replica with zero data loss (RPO = 0) and without changing the application connection string (the DB DNS endpoint automatically flips).
- Option A: Single-AZ has no standby; recovering from an AZ outage requires restoring a snapshot to a new instance (RPO > 0, RTO in tens of minutes).
- Option C: Read Replicas use asynchronous replication (potential data loss) and require manual promotion.
- Option D provides no resilience and introduces a massive security hazard.

**References:**
- Amazon RDS User Guide: Multi-AZ Deployments
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 21 [SAA-C03-D2-Q057]

**Task Statement 2.2**

An e-commerce enterprise hosts its web application across a multi-tier architecture on EC2 instances behind an Application Load Balancer. The database tier uses Amazon RDS for MySQL. During peak checkout periods, sudden surges in concurrent user logins cause the database to run out of memory due to thousands of direct open connections, leading to connection dropouts. How can the architect stabilize connection scaling without modifying the underlying database instance class?

- **A)** Deploy Amazon RDS Proxy between the application tier and the RDS database instance.
- **B)** Migrate the database to Amazon S3 Standard.
- **C)** Increase the connection timeout on the Application Load Balancer to 3600 seconds.
- **D)** Add an elastic IP address directly to the primary RDS database.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon RDS Proxy is a fully managed, highly available database proxy that pools and shares connections established with the database, improving application scalability and resilience to connection spikes. It maintains a pool of established database connections, preventing applications from opening thousands of memory-intensive database connections, and reduces failover times for Multi-AZ databases by up to 66%.
- Option B: S3 is an object store, not a relational SQL transactional database.
- Option C increases ALB idle timeouts, keeping backend connections open longer and worsening database connection exhaustion.
- Option D does not address connection concurrency or pooling.

**References:**
- Amazon RDS User Guide: Amazon RDS Proxy
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 22 [SAA-C03-D2-Q058]

**Task Statement 2.2**

A company is designing a disaster recovery mechanism for a website hosted on EC2 instances. If the primary on-premises data center fails, all incoming traffic must be automatically redirected to a static maintenance and error landing page hosted on an Amazon S3 website bucket. Which Route 53 routing policy accomplishes this?

- **A)** Route 53 Geoproximity Routing
- **B)** Route 53 Failover Routing with a Primary record (on-premises) and a Secondary record (S3 bucket) tied to a health check
- **C)** Route 53 Weighted Routing with 50/50 weights
- **D)** Route 53 Simple Routing

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Route 53 Failover Routing is explicitly designed for active-passive disaster recovery configurations. You configure a Primary record pointing to your primary data center and associate it with a Route 53 Health Check, and configure a Secondary record pointing to the backup location (such as an Amazon S3 static website bucket). When the health check detects that the primary endpoint is unhealthy, Route 53 automatically directs DNS queries to the secondary resource.
- Option A routes traffic based on geographic coordinates and bias.
- Option C sends half of all traffic to the maintenance page even during normal operations.
- Option D does not support health checks or automated failover.

**References:**
- Amazon Route 53 Developer Guide: Configuring Failover Routing
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 23 [SAA-C03-D2-Q059]

**Task Statement 2.2**

An architect is designing an Auto Scaling policy for an EC2 worker fleet processing messages from an Amazon SQS queue. CPU utilization on the worker instances does not change significantly whether processing 10 messages or 10,000 messages. What metric should the architect use to drive autoscaling so the fleet expands when the queue backlog increases?

- **A)** EC2 CPUUtilization
- **B)** A custom CloudWatch metric calculating the Backlog per Instance (`ApproximateNumberOfMessagesVisible / Number of Running Instances`)
- **C)** EC2 NetworkOut
- **D)** SQS NumberOfMessagesDeleted

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Well-Architected guidance for queue-based worker scaling specifies using a custom metric representing the Backlog per Instance, calculated by dividing the SQS queue depth (`ApproximateNumberOfMessagesVisible`) by the current running capacity of the Auto Scaling group. Scaling based on this ratio ensures the fleet scales out proportionally to handle the workload backlog accurately, regardless of CPU metrics.
- Option A fails because CPU does not correlate with queue load.
- Option C measures network bandwidth, which is not an indicator of message backlog.
- Option D measures processed/deleted messages, not the pending backlog waiting to be processed.

**References:**
- Amazon EC2 Auto Scaling User Guide: Scaling Based on Amazon SQS
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 24 [SAA-C03-D2-Q060]

**Task Statement 2.2**

A shared Linux file storage solution is required for a cluster of 50 EC2 instances deployed across multiple Availability Zones in the `us-east-1` region. The file system must support standard POSIX file system semantics, concurrent read/write operations from all instances simultaneously, and automatic multi-AZ redundancy. Which AWS storage service meets these requirements?

- **A)** Amazon Elastic Block Store (EBS) General Purpose gp3 volume
- **B)** Amazon Elastic File System (Amazon EFS) with Standard storage class
- **C)** Amazon S3 Standard
- **D)** Amazon EBS Provisioned IOPS io2 volume without Multi-Attach

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon EFS is a managed POSIX-compliant network file system (NFSv4) that can be mounted concurrently by hundreds of EC2 instances across multiple Availability Zones. The EFS Standard storage class stores data redundantly across multiple AZs within an AWS Region, delivering multi-AZ durability and high availability.
- Option A: EBS gp3 volumes can only be attached to a single EC2 instance in a single AZ at a time.
- Option C: Amazon S3 is an object store accessed via REST APIs, not a POSIX file system supporting local filesystem mounts and atomic file locking.
- Option D: EBS volumes are tied to a single AZ.

**References:**
- Amazon EFS User Guide: Storage Classes
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 25 [SAA-C03-D2-Q061]

**Task Statement 2.2**

An enterprise runs an internal web portal accessible only within its private network. The company has 10 distinct VPCs that all require private domain name resolution for the internal domain `internal.corp`. How can the architect provide high-availability internal DNS resolution across all 10 VPCs with minimal operational management?

- **A)** Create a Route 53 Private Hosted Zone for `internal.corp` and associate all 10 VPCs with this hosted zone.
- **B)** Deploy two EC2 instances running BIND DNS servers in every single VPC and configure DNS forwarding.
- **C)** Create a public Route 53 Hosted Zone and protect it with AWS WAF.
- **D)** Hardcode IP addresses in the `/etc/hosts` file of every server.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Route 53 Private Hosted Zones allow you to resolve internal domain names within your private Amazon VPCs. You can create a single private hosted zone for `internal.corp` and associate multiple VPCs (including cross-account VPCs) with it. Route 53 automatically provides high-availability managed DNS resolution within those VPCs.
- Option B introduces 20 EC2 servers that require patching, configuration, and maintenance overhead.
- Option C exposes internal corporate server records to the public internet.
- Option D is unmanageable at scale and brittle to IP changes.

**References:**
- Amazon Route 53 Developer Guide: Working with Private Hosted Zones
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 26 [SAA-C03-D2-Q062]

**Task Statement 2.2**

An architect is configuring an Auto Scaling group that must balance high availability with cost efficiency. The application is stateless and resilient to individual node interruptions. The management wants to use EC2 Spot Instances to reduce costs by 70%, but requires a guaranteed baseline of 5 On-Demand instances to handle minimum steady-state customer load at all times. How should the ASG be configured?

- **A)** Create two separate Auto Scaling groups: one with 5 On-Demand instances, and another with Spot instances, and manage them with custom scripts.
- **B)** Configure an Auto Scaling group with a Mixed Instances Policy specifying a Base Capacity of 5 On-Demand Instances, and satisfy remaining capacity with Spot Instances using the `capacity-optimized` allocation strategy.
- **C)** Launch Spot instances manually from the AWS CLI and attach them to the ALB target group.
- **D)** Use only Reserved Instances across all tiers.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon EC2 Auto Scaling supports Mixed Instances Policies within a single Auto Scaling group. You can define a base number of On-Demand instances (e.g., `OnDemandBaseCapacity = 5`) to guarantee minimum baseline availability, and configure the remaining instances to launch as Spot Instances using the `capacity-optimized` allocation strategy to draw from the deepest Spot capacity pools and minimize interruption risk.
- Option A creates dual-ASG management overhead and complicates target group balancing.
- Option C loses all Auto Scaling elasticity, self-healing, and replacement automation.
- Option D locks the company into full On-Demand commitments without capturing Spot savings.

**References:**
- Amazon EC2 Auto Scaling User Guide: Auto Scaling Groups with Multiple Instance Types and Purchase Options
- AWS Well-Architected Cost and Reliability Pillars

</details>

---

### Question 27 [SAA-C03-D2-Q063]

**Task Statement 2.1**

A company receives hundreds of image upload files per minute via Amazon S3. Each image requires thumbnail generation, watermarking, and metadata extraction. These tasks can run independently and take between 10 to 60 seconds each. If one image fails processing, other images must not be affected. What is the most resilient, cost-effective serverless architecture?

- **A)** Run a single large EC2 instance with a multi-threaded Python script polling S3.
- **B)** Configure Amazon S3 Event Notifications to send an event to an Amazon SQS queue when objects are created. Use an AWS Lambda function triggered by the SQS queue to process images concurrently with automated retries and dead-letter queueing.
- **C)** Trigger an AWS Batch job with an array size of 10,000 on a single On-Demand instance.
- **D)** Use an Amazon EMR cluster with Apache Spark running continuously.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Using S3 Event Notifications with an Amazon SQS buffer and AWS Lambda provides a completely serverless, event-driven, decoupled image processing architecture. SQS buffers sudden upload bursts, and Lambda scales out automatically to process messages in parallel. Failed items are automatically retried and sent to a Dead-Letter Queue without impacting other jobs.
- Option A creates a single point of failure and suffers from capacity limits.
- Option C is unnecessarily heavy for sub-minute image processing tasks.
- Option D incurs high continuous idle costs for an Apache Spark cluster.

**References:**
- AWS Serverless Application Lens: Event-Driven Architectures
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 28 [SAA-C03-D2-Q064]

**Task Statement 2.2**

An architect needs to configure automated, centralized backups across Amazon EBS volumes, Amazon RDS databases, Amazon DynamoDB tables, and Amazon EFS file systems across 10 AWS accounts. The backup policy must enforce daily snapshots, retain backups for 90 days, and automatically copy backups to a secondary AWS Region for disaster recovery. Which service delivers this capability natively?

- **A)** Custom cron scripts running on an EC2 instance executing AWS CLI snapshot commands
- **B)** AWS Backup with AWS Organizations integration and cross-region backup copy policies
- **C)** Amazon S3 Glacier direct vault lock
- **D)** AWS Storage Gateway Volume Gateway

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Backup is a fully managed, policy-based service that centralizes and automates data protection across AWS services (EBS, RDS, DynamoDB, EFS, EC2, S3). Through integration with AWS Organizations, backup policies can be defined centrally and applied organization-wide, including automated lifecycle transitions (to cold storage) and automated cross-region and cross-account backup copying.
- Option A is brittle, insecure, error-prone, and requires heavy operational maintenance.
- Option C applies to S3 object vaults, not native cross-service snapshot coordination.
- Option D is for hybrid on-premises to cloud storage caching.

**References:**
- AWS Backup Developer Guide: Managing Backups with AWS Organizations
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 29 [SAA-C03-D2-Q065]

**Task Statement 2.2**

A company runs an application behind an Application Load Balancer. The security and network operations team requires that client source IP addresses must be preserved and accessible to the backend application servers in the private subnet for security analytics and geolocation tracking. How does the ALB pass the client IP address to the backend targets?

- **A)** The ALB rewrites the IP packet header with the client's public IP.
- **B)** The ALB inserts the original client IP address into the `X-Forwarded-For` HTTP request header before forwarding to the target instances.
- **C)** The ALB disables Network Address Translation (NAT).
- **D)** The backend EC2 instances must run in promiscuous mode.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Application Load Balancers (ALBs) operate as reverse proxies at Layer 7. When forwarding HTTP/HTTPS requests to backend targets, the source IP of the packet becomes the private IP address of the ALB node. To preserve the original client IP, the ALB automatically appends the client IP address to the `X-Forwarded-For` HTTP header, which backend applications can parse.
- Option A: ALBs do not rewrite IP packet headers; Network Load Balancers with instance targets preserve client IP at the packet level, but ALBs use HTTP headers.
- Options C and D are technically invalid.

**References:**
- Elastic Load Balancing User Guide: HTTP Headers and Application Load Balancers
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 30 [SAA-C03-D2-Q066]

**Task Statement 2.1**

An architect is designing an event-driven workflow. High-frequency IoT sensors generate 5,000 JSON status events every second. A downstream microservice needs to consume these events, but occasionally crashes and needs up to 24 hours to replay all unprocessed events in sequence from the exact point of failure. Which service provides durable, replayable stream ingestion?

- **A)** Amazon SQS Standard Queue with 1-minute message retention
- **B)** Amazon Kinesis Data Streams with data retention configured up to 365 days
- **C)** Amazon SNS Topic with email subscriptions
- **D)** Amazon CloudWatch Logs

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon Kinesis Data Streams is built for real-time streaming data ingestion at scale. Streams store records sequentially across shards and retain data for 24 hours by default (configurable up to 365 days). Consumers read from shards using shard iterators, allowing multiple independent consumer applications to read and replay the data stream from any point in time.
- Option A: In SQS, once a message is deleted by a consumer, it is gone; it cannot be replayed by other consumers.
- Option C: SNS does not store messages for replay (publish-subscribe push model).
- Option D is a log aggregation service, not a high-throughput event streaming engine for microservices.

**References:**
- Amazon Kinesis Data Streams Developer Guide: Reading Data from Amazon Kinesis Data Streams
- AWS Well-Architected Reliability Pillar

</details>

---

### Question 31 [SAA-C03-D2-Q067]

**Task Statement 2.2**

A company has a multi-tier web application running in a single Availability Zone. The database is an RDS for PostgreSQL instance. To ensure business continuity against hardware failures and data center disasters, what two modifications should be made to achieve high availability? (Choose TWO)

- **A)** Convert the Amazon RDS instance to a Multi-AZ deployment.
- **B)** Deploy the EC2 instances in an Auto Scaling group span across at least two Availability Zones behind an Application Load Balancer.
- **C)** Create an S3 bucket in a different region and configure daily snapshots.
- **D)** Assign Elastic IPs to every EC2 instance.
- **E)** Migrate the web application to a single large EC2 bare metal instance.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A, B`

**Detailed Explanation:**
To transform a single-AZ architecture into a highly available multi-AZ architecture: 1) Deploy the EC2 application servers in an Auto Scaling group that spans across at least two Availability Zones behind an Application Load Balancer to ensure compute redundancy. 2) Convert the Amazon RDS instance to a Multi-AZ deployment to enable synchronous physical replication to a standby instance in a second AZ with automated failover.
- Option C provides disaster recovery backups, but does not achieve high availability.
- Option D does not provide redundancy across AZs.
- Option E exacerbates single point of failure risks.

**References:**
- AWS Well-Architected Framework: Reliability Pillar
- Amazon RDS Multi-AZ Documentation

</details>

---

### Question 32 [SAA-C03-D2-Q068]

**Task Statement 2.1**

A document indexing application processes PDF files uploaded to Amazon S3. The processing steps involve OCR text extraction, entity recognition, and database insertion. If the OCR step fails due to a corrupted PDF, the application must immediately log the error, send an alert to an admin Slack channel, and abort without executing subsequent steps. Which AWS service provides native conditional branching and error-catch mechanisms for such workflows?

- **A)** AWS Step Functions
- **B)** Amazon SQS Standard
- **C)** Amazon SNS
- **D)** AWS CodeDeploy

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Step Functions provides state machine orchestration with built-in `Catch` and `Retry` blocks for fine-grained error handling. You can define specific error handlers on individual task states to catch exceptions (e.g., `States.TaskFailed`), route execution to an alerting state, and stop further execution cleanly.
- Options B and C are messaging transports that do not execute state machine logic or manage multi-step conditional error branching.
- Option D is an application deployment service.

**References:**
- AWS Step Functions Developer Guide: Error Handling in Step Functions
- AWS Well-Architected Reliability Pillar

</details>

---

