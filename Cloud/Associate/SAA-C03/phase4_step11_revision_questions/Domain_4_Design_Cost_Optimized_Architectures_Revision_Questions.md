# AWS Certified Solutions Architect - Associate (SAA-C03)
## Domain 4: Design Cost-Optimized Architectures (20%)

> **Focus:** Official AWS Exam Objectives for Domain 4: Design Cost-Optimized Architectures  
> **Total Scenario Questions:** 24  

---

### Question 01 [SAA-C03-D4-Q097]

**Task Statement 4.1**

A legal firm must archive 500 TB of completed case files in Amazon S3 for 10 years to comply with regulatory mandates. The records are accessed fewer than once or twice a year, and the legal team can wait up to 12 to 48 hours to retrieve any requested case file. Which S3 storage class provides the lowest storage cost?

- **A)** Amazon S3 Standard
- **B)** Amazon S3 Standard-Infrequent Access (Standard-IA)
- **C)** Amazon S3 Glacier Flexible Archive
- **D)** Amazon S3 Glacier Deep Archive

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `D`

**Detailed Explanation:**
Amazon S3 Glacier Deep Archive is Amazon S3's lowest-cost storage class (approximately $0.00099 per GB per month), designed for long-term data retention that is accessed only once or twice a year. Objects can be retrieved within 12 hours (Standard retrieval) or 48 hours (Bulk retrieval), making it the optimal, most cost-effective choice when retrieval delays are acceptable.
- Option A: S3 Standard costs approximately 23x more per GB.
- Option B: S3 Standard-IA is designed for data accessed once a month with millisecond retrieval, but costs significantly more than Glacier Deep Archive.
- Option C: Glacier Flexible Archive costs approximately 4x more than Glacier Deep Archive.

**References:**
- Amazon S3 User Guide: Storage Classes - S3 Glacier Deep Archive
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 02 [SAA-C03-D4-Q098]

**Task Statement 4.1**

An architect is managing an Amazon S3 bucket containing petabytes of data with unpredictable and constantly changing access patterns. Some objects are accessed frequently in the first week, then become dormant for months, and occasionally surge in access. The company wants to optimize storage costs automatically without paying retrieval fees and without operational management overhead. Which S3 storage class should be chosen?

- **A)** Amazon S3 Intelligent-Tiering
- **B)** Amazon S3 Standard-IA with manual lifecycle rules
- **C)** Amazon S3 One Zone-IA
- **D)** Amazon S3 Glacier Instant Retrieval

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon S3 Intelligent-Tiering is the only cloud storage class that delivers automatic cost savings by automatically moving objects between access tiers (Frequent Access, Infrequent Access, Archive Instant Access, and optional Archive/Deep Archive Access) when access patterns change. Crucially, S3 Intelligent-Tiering charges ZERO retrieval fees when objects are accessed from any tier, making it ideal for unpredictable workloads.
- Option B: S3 Standard-IA incurs per-GB retrieval fees every time an object is read, which can lead to massive unexpected costs if access patterns surge unpredictably.
- Option C: One Zone-IA lacks multi-AZ redundancy and also charges retrieval fees.
- Option D: Glacier Instant Retrieval charges significant per-GB retrieval fees on access.

**References:**
- Amazon S3 User Guide: Amazon S3 Intelligent-Tiering
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 03 [SAA-C03-D4-Q099]

**Task Statement 4.4**

A company operates 50 EC2 instances in a private subnet that download and upload 100 TB of data monthly to Amazon S3. The instances currently route traffic out through a NAT Gateway in a public subnet to reach S3 public endpoints. The monthly AWS bill reveals thousands of dollars in NAT Gateway data processing charges ($0.045/GB). What architectural change will completely eliminate these data processing fees?

- **A)** Deploy an Interface VPC Endpoint for Amazon S3 in the private subnet.
- **B)** Deploy a Gateway VPC Endpoint for Amazon S3 and update the private subnet route table to route S3 traffic to the gateway endpoint.
- **C)** Assign Elastic IP addresses directly to all 50 private EC2 instances.
- **D)** Replace the NAT Gateway with an EC2 NAT instance.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Gateway VPC Endpoints for Amazon S3 and DynamoDB are provided by AWS at ZERO cost—there are no hourly fees and no data processing charges. By adding a Gateway VPC Endpoint for S3 to the VPC route table, S3 traffic bypasses the NAT Gateway entirely and travels over the private AWS backbone, completely eliminating the $0.045/GB data processing fees ($4,500/month on 100 TB).
- Option A: Interface VPC Endpoints for S3 incur hourly endpoint fees and per-GB data processing fees ($0.01/GB), whereas Gateway Endpoints are completely free.
- Option C violates private subnet security requirements and exposes instances to the internet.
- Option D still incurs compute, EBS, and data transfer costs and requires manual maintenance.

**References:**
- Amazon VPC User Guide: Gateway VPC Endpoints for S3
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 04 [SAA-C03-D4-Q100]

**Task Statement 4.2**

A data analytics company runs stateless batch processing jobs every night that take between 2 to 4 hours to complete. The jobs can be interrupted and resumed from checkpointed data in Amazon S3 without data corruption. The management mandates reducing compute costs by up to 90% compared to On-Demand pricing. Which EC2 purchasing option should be chosen?

- **A)** On-Demand Instances
- **B)** EC2 Spot Instances
- **C)** Dedicated Hosts
- **D)** Standard Reserved Instances

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Amazon EC2 Spot Instances allow you to utilize spare EC2 compute capacity in the AWS cloud at up to a 90% discount compared to On-Demand prices. Spot instances are ideal for fault-tolerant, flexible, stateless, and checkpointed batch workloads that can handle occasional two-minute interruption notices.
- Option A: On-Demand instances pay the highest full retail pricing.
- Option C: Dedicated Hosts are designed for proprietary compliance and bring-your-own-license (BYOL) needs, making them the most expensive EC2 option.
- Option D: Reserved Instances require a 1- or 3-year commitment, saving at most ~72%, and are meant for continuous steady-state workloads, not intermittent batch runs.

**References:**
- Amazon EC2 User Guide: Spot Instances
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 05 [SAA-C03-D4-Q101]

**Task Statement 4.2**

An enterprise has a predictable steady-state microservices workload running across a mix of Amazon EC2 instances, AWS Fargate containers, and AWS Lambda functions across three different AWS Regions. The engineering team plans to migrate from x86 to Graviton processors and change instance families over the next two years. Which AWS discount commitment model provides the greatest flexibility across services, instance families, and regions?

- **A)** EC2 Instance Savings Plans
- **B)** Compute Savings Plans
- **C)** Standard Reserved Instances
- **D)** Volume Discounts for S3

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
Compute Savings Plans offer the greatest flexibility (savings up to 66% in exchange for a 1- or 3-year consistent hourly spend commitment). Compute Savings Plans automatically apply to usage regardless of instance family (e.g., moving from C5 to C7g Graviton), instance size, OS, tenancy, AWS Region, or compute technology (EC2, AWS Fargate, AWS Lambda).
- Option A: EC2 Instance Savings Plans provide up to 72% savings but are locked to a specific instance family in a specific region.
- Option C: Standard Reserved Instances are locked to a specific instance type, OS, and region.
- Option D applies to S3 storage, not compute.

**References:**
- AWS Savings Plans User Guide
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 06 [SAA-C03-D4-Q102]

**Task Statement 4.3**

A software development team runs 30 development and staging relational database environments on Amazon RDS PostgreSQL. These environments are only actively used during business hours (8 hours a day, 5 days a week) and remain completely idle at night and on weekends. The team is looking for a cost-effective solution that scales compute down to near-zero during idle periods without terminating the databases. Which solution should the architect implement?

- **A)** Amazon Aurora Serverless v2
- **B)** Amazon RDS for PostgreSQL Multi-AZ with Provisioned IOPS
- **C)** Amazon DynamoDB with Provisioned Capacity
- **D)** Amazon Redshift Dense Compute cluster

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Aurora Serverless v2 automatically scales database capacity up and down in fine-grained increments (Aurora Capacity Units - ACUs) in fractions of a second based on application activity, scaling down to as low as 0.5 ACU during idle off-hours, drastically reducing database spend for development and intermittent workloads.
- Option B: Multi-AZ with Provisioned IOPS is designed for high-availability production, incurring expensive 24/7 compute and IOPS charges even when completely idle.
- Option C: DynamoDB is NoSQL, not relational PostgreSQL.
- Option D is an analytics data warehouse with fixed hourly node costs.

**References:**
- Amazon Aurora User Guide: Aurora Serverless v2
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 07 [SAA-C03-D4-Q103]

**Task Statement 4.3**

A mobile ticketing application experiences extreme spikes in traffic during ticket release days (such as 100,000 writes per second for 15 minutes), followed by weeks of near-zero activity. The application uses Amazon DynamoDB. The architect needs a capacity model that requires no capacity planning, scales instantly to handle peak bursts, and incurs zero charges when no read/write requests are being processed. Which DynamoDB capacity mode should be used?

- **A)** DynamoDB Provisioned Capacity with Auto Scaling
- **B)** DynamoDB On-Demand Capacity
- **C)** DynamoDB Global Tables
- **D)** DynamoDB Accelerator (DAX)

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
DynamoDB On-Demand capacity mode offers simple pay-per-request pricing for read and write requests, so you pay only for what you use. It accommodates unpredictable workloads that spike suddenly without capacity planning or throttle limits, and charges nothing when the table is idle (you pay only for data storage).
- Option A: Provisioned Capacity with Auto Scaling is cost-effective for predictable gradual workloads, but takes several minutes to scale up, causing throttling during sudden instantaneous spikes, and charges a baseline hourly provisioned capacity even when idle.
- Option C replicates data geographically across regions, increasing write costs.
- Option D adds continuous hourly node cluster costs.

**References:**
- Amazon DynamoDB Developer Guide: On-Demand Capacity Mode
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 08 [SAA-C03-D4-Q104]

**Task Statement 4.1**

A company has millions of small log files (each approximately 10 KB in size) uploaded to Amazon S3 Standard daily. A cloud engineer proposes a lifecycle rule to transition all objects to Amazon S3 Standard-Infrequent Access (Standard-IA) after 30 days. Why might this lifecycle rule actually increase the monthly AWS storage bill?

- **A)** S3 Standard-IA has a minimum billable object size of 128 KB and charges a per-request transition fee.
- **B)** S3 Standard-IA does not support encryption.
- **C)** S3 Standard-IA deletes objects after 90 days automatically.
- **D)** S3 Standard-IA cannot store files with a `.log` extension.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
In Amazon S3, the Infrequent Access (Standard-IA and One Zone-IA) and Glacier storage classes enforce a minimum billable object size of 128 KB. If you transition a 10 KB object to S3 Standard-IA, you are billed for 128 KB of storage (a 12.8x increase in billable storage capacity!), plus per-request PUT/transition charges. For files under 128 KB, keeping them in S3 Standard or bundling them into larger archives before upload is far more cost-effective.
- Options B, C, and D are factually false.

**References:**
- Amazon S3 Pricing & User Guide: Storage Classes - Minimum Billable Object Size
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 09 [SAA-C03-D4-Q105]

**Task Statement 4.2**

A solutions architect is conducting a cost optimization review of an AWS account. The team needs automated machine learning recommendations on which EC2 instances are over-provisioned (e.g., average CPU utilization < 5%) and would benefit from downsizing, as well as recommendations for right-sizing EBS volumes and Lambda function memory allocations. Which AWS service provides these AI-driven right-sizing recommendations?

- **A)** AWS Cost Explorer
- **B)** AWS Compute Optimizer
- **C)** AWS Trusted Advisor
- **D)** Amazon CloudWatch Synthetics

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Compute Optimizer uses machine learning to analyze historical resource utilization metrics from CloudWatch (CPU, memory, storage I/O, network) to deliver actionable right-sizing recommendations for Amazon EC2 instances, Auto Scaling groups, Amazon EBS volumes, and AWS Lambda functions, helping eliminate over-provisioning and cut cloud spend by up to 25%.
- Option A: Cost Explorer visualizes historical spending and provides Savings Plans purchase recommendations, but not granular EC2/EBS hardware right-sizing analysis.
- Option C: Trusted Advisor checks high-level best practices, but Compute Optimizer provides deep ML-driven hardware instance recommendations.
- Option D runs synthetic UI tests.

**References:**
- AWS Compute Optimizer User Guide
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 10 [SAA-C03-D4-Q106]

**Task Statement 4.1**

A research laboratory needs to migrate 180 TB of historical research data from on-premises network attached storage (NAS) to Amazon S3. The laboratory's internet connection has an upload bandwidth of only 20 Mbps, which would take over 2 years to transfer the data over the wire. What is the most cost-effective and fastest method to transfer this data to S3?

- **A)** Order an AWS Snowball Edge Storage Optimized device, transfer data locally at high speed, and ship the appliance back to AWS.
- **B)** Purchase a dedicated 10 Gbps AWS Direct Connect connection for 1 month.
- **C)** Use AWS DataSync over the existing 20 Mbps internet connection.
- **D)** Upload data via Amazon S3 Transfer Acceleration.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Snowball Edge Storage Optimized provides up to 80 TB or 210 TB of usable NVMe/SATA storage in a ruggedized, shippable physical appliance. Transferring 180 TB locally over 10G/25G Ethernet takes days, and shipping the appliance to AWS allows direct ingestion into Amazon S3 within a week, avoiding the multi-year bottleneck of a 20 Mbps link at a fraction of the cost.
- Option B: Provisioning Direct Connect takes weeks to months for telecom physical circuit delivery and incurs high setup and contract commitments.
- Option C: 180 TB over 20 Mbps takes ~2.3 years.
- Option D: S3 Transfer Acceleration accelerates edge routing, but cannot overcome a local 20 Mbps internet bandwidth choke.

**References:**
- AWS Snowball Edge Developer Guide
- AWS Well-Architected Cost and Performance Pillars

</details>

---

### Question 11 [SAA-C03-D4-Q107]

**Task Statement 4.4**

A company has 15 VPCs deployed across three AWS accounts in the same Region. Each VPC currently has its own NAT Gateway in a public subnet to allow instances to access the internet. The FinOps team identifies that each NAT Gateway incurs a fixed hourly charge ($0.045/hr) plus data processing fees, resulting in over $500/month just in baseline hourly NAT fees. How can the architect reduce baseline NAT Gateway costs?

- **A)** Consolidate egress traffic by deploying a centralized egress VPC connected to all VPCs via an AWS Transit Gateway, and share a centralized set of NAT Gateways.
- **B)** Assign Elastic IP addresses to every instance in every private subnet.
- **C)** Remove all NAT Gateways and attach Internet Gateways directly to private subnets.
- **D)** Replace all NAT Gateways with an AWS Site-to-Site VPN to on-premises.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
By implementing a centralized egress architecture using AWS Transit Gateway, multiple spoke VPCs route their outbound default traffic (`0.0.0.0/0`) through the Transit Gateway to a centralized Egress VPC containing a single shared pair of Multi-AZ NAT Gateways. This reduces the number of NAT Gateways from 15 to 2, eliminating hundreds of dollars in redundant hourly fixed charges.
- Option B compromises private subnet isolation and costs money for idle Elastic IPs.
- Option C makes private subnets public, exposing private workloads.
- Option D backhauls traffic over VPN, adding latency and on-premises network overhead.

**References:**
- AWS Transit Gateway User Guide: Centralized Egress Architecture
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 12 [SAA-C03-D4-Q108]

**Task Statement 4.4**

An architect is reviewing the monthly AWS invoice and discovers unexpected charges for idle Elastic IP addresses ($0.005 per hour per unused IP). How can the cloud team eliminate these unnecessary recurring charges?

- **A)** Associate the idle Elastic IP addresses with stopped EC2 instances.
- **B)** Release the unassociated Elastic IP addresses back to the AWS public IP pool.
- **C)** Convert the Elastic IP addresses to IPv6 addresses.
- **D)** Attach the Elastic IPs to a route table.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS charges an hourly fee for Elastic IP addresses that are allocated to an account but NOT associated with a running EC2 instance or active network interface (to prevent public IPv4 address hoarding). Releasing the unassociated Elastic IPs back to the AWS pool eliminates these idle charges completely.
- Option A: AWS still charges for Elastic IPs associated with stopped EC2 instances.
- Option C: Elastic IPs are IPv4 addresses; you cannot convert an allocated IPv4 EIP into an IPv6 address.
- Option D: Elastic IPs cannot be attached directly to route tables.

**References:**
- Amazon EC2 User Guide: Elastic IP Address Pricing
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 13 [SAA-C03-D4-Q109]

**Task Statement 4.4**

A multinational company uses an AWS Organization with 25 member accounts. The management wants to leverage volume pricing discounts across Amazon S3 storage tiers and receive a single consolidated invoice each month. Which AWS feature should be configured?

- **A)** AWS Organizations Consolidated Billing
- **B)** AWS Control Tower Guardrails
- **C)** AWS Budgets Multi-Account alerts
- **D)** AWS Service Catalog

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Consolidated Billing in AWS Organizations combines the usage across all accounts in the organization, enabling the company to qualify for volume pricing discounts (such as S3 tiered storage pricing where price per GB drops above 50 TB and 500 TB) as if the organization were a single account, while providing a single consolidated monthly bill.
- Option B enforces governance and compliance rules, not billing consolidation.
- Option C sends spending threshold alerts, but does not aggregate billing or volume discounts.
- Option D allows organizations to create and manage catalogs of approved IT services.

**References:**
- AWS Organizations User Guide: Consolidated Billing
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 14 [SAA-C03-D4-Q110]

**Task Statement 4.1**

A compliance regulation mandates that VPC Flow Logs must be captured and retained for 7 years for forensic auditing. The logs are never queried unless an active security incident is investigated (expected less than once every 3 years). How should the logging architecture be configured to minimize ongoing storage costs?

- **A)** Publish VPC Flow Logs directly to Amazon S3, and configure an S3 Lifecycle rule to transition logs to S3 Glacier Deep Archive after 30 days and expire after 7 years.
- **B)** Publish VPC Flow Logs to Amazon CloudWatch Logs and keep retention set to Never Expire.
- **C)** Stream VPC Flow Logs to an Amazon OpenSearch Service cluster with 10 master nodes.
- **D)** Store VPC Flow Logs in an Amazon Aurora Multi-AZ database.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Publishing VPC Flow Logs directly to an Amazon S3 bucket allows the use of S3 Lifecycle policies. After a brief period in S3 Standard (e.g., 30 days) for immediate analysis, the logs transition to Amazon S3 Glacier Deep Archive ($0.00099/GB/month), yielding over 95% cost savings compared to keeping petabytes of logs in CloudWatch Logs for 7 years.
- Option B: CloudWatch Logs costs $0.03/GB/month for storage—roughly 30x more expensive than Glacier Deep Archive.
- Option C: OpenSearch requires continuous 24/7 cluster compute and EBS storage, which is cost-prohibitive for unqueried archive logs.
- Option D is an anti-pattern for log storage.

**References:**
- Amazon VPC User Guide: Publishing Flow Logs to Amazon S3
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 15 [SAA-C03-D4-Q111]

**Task Statement 4.2**

An architect is running a short-lived asynchronous ETL data transformation job that executes for 3 minutes once every 4 hours. The job processes 50 MB of data per run. What is the most cost-effective compute solution?

- **A)** An Amazon EC2 instance running 24/7 on an On-Demand m5.large instance.
- **B)** An AWS Lambda function triggered on a schedule by Amazon EventBridge.
- **C)** An Amazon EMR cluster with 3 core nodes running continuously.
- **D)** An AWS Elastic Beanstalk web environment with an Application Load Balancer.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
AWS Lambda is a serverless compute service where you pay strictly for the execution time (in milliseconds) and memory consumed. For a job running only 3 minutes once every 4 hours (18 minutes total compute per day), Lambda costs pennies per month, whereas a running EC2 instance or EMR cluster incurs 24/7 idle infrastructure costs.
- Option A incurs 24 hours of compute billing for 18 minutes of actual work.
- Option C incurs continuous cluster fees for idle nodes.
- Option D is designed for web apps and incurs ALB and EC2 idle fees.

**References:**
- AWS Lambda Pricing Documentation
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 16 [SAA-C03-D4-Q112]

**Task Statement 4.4**

An architect wants to host a public company marketing website consisting entirely of static HTML, CSS, JavaScript, and image assets. The website receives around 100,000 visitors per month. The business wants the lowest possible cost, high availability across multiple regions, and zero server maintenance overhead. What architecture should be deployed?

- **A)** Deploy an Amazon S3 bucket configured for static website hosting behind an Amazon CloudFront distribution with Origin Access Control (OAC).
- **B)** Launch an Auto Scaling group of EC2 instances running Apache web server across two AZs behind an Application Load Balancer.
- **C)** Deploy an AWS Elastic Beanstalk single-container Docker environment on a t3.medium instance.
- **D)** Run a self-managed NGINX container on Amazon ECS on EC2 with an attached EBS volume.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon S3 static website hosting combined with Amazon CloudFront provides the industry standard serverless static hosting architecture. CloudFront caches static content globally at edge locations, while S3 provides 99.999999999% (11 9s) durability. For 100,000 visitors/month, the total monthly cost is typically under $1.00, with zero server patching or OS management.
- Options B, C, and D all require managing virtual machines, load balancers, and operating system runtimes, costing $20 to $50+/month.

**References:**
- Amazon CloudFront Developer Guide: Using Amazon S3 Origins
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 17 [SAA-C03-D4-Q113]

**Task Statement 4.1**

A solutions architect is auditing an AWS account and observes that an Amazon EBS Provisioned IOPS `io1` volume of 1 TB is provisioned with 3,000 IOPS and attached to a database instance. The database consistently consumes 2,500 IOPS and 100 MB/s throughput. How can the architect reduce EBS costs by at least 20% while maintaining the exact same storage and performance?

- **A)** Migrate the volume from `io1` to a General Purpose SSD `gp3` volume with default 3,000 IOPS and 125 MB/s throughput.
- **B)** Change the volume to a Cold HDD `sc1` volume.
- **C)** Reduce the volume size from 1 TB to 100 GB.
- **D)** Enable EBS encryption with a customer-managed key.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon EBS General Purpose SSD `gp3` volumes provide a baseline of 3,000 IOPS and 125 MB/s throughput included with the base storage cost ($0.08/GB-month vs $0.125/GB-month for `io1` plus $0.065 per provisioned IOPS). Migrating from `io1` to `gp3` delivers the exact required performance (3,000 IOPS and 125 MB/s) while saving more than 50% on EBS costs.
- Option B: `sc1` is magnetic storage delivering max 250 IOPS and cannot handle a 2,500 IOPS database.
- Option C cuts storage capacity by 90%, risking disk full outages.
- Option D adds security but does not alter volume pricing.

**References:**
- Amazon EBS User Guide: General Purpose SSD Volumes (gp3)
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 18 [SAA-C03-D4-Q114]

**Task Statement 4.3**

A software engineering team runs a staging RDS MySQL database that is only needed between 9:00 AM and 5:00 PM Monday through Friday. Running the database 24/7 over the weekend and overnight incurs unnecessary compute costs. What is the most cost-effective and automated way to reduce staging database costs?

- **A)** Use AWS Systems Manager State Manager or an AWS Lambda function triggered by Amazon EventBridge to automatically stop the RDS DB instance at 5:00 PM and start it at 9:00 AM on weekdays.
- **B)** Delete the RDS instance at 5:00 PM every day and restore it from snapshot at 9:00 AM.
- **C)** Convert the database to Amazon Redshift.
- **D)** Downgrade the database instance to `t4g.micro` every night manually.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon RDS allows stopping and starting DB instances for up to 7 days at a time. While stopped, you pay only for database storage (EBS and backups), completely saving on hourly compute and software licensing charges (~65% cost reduction). Automating this using an AWS Lambda function or AWS Systems Manager Automation scheduled by Amazon EventBridge requires zero manual effort.
- Option B involves deleting and restoring multi-gigabyte snapshots daily, which takes significant time, risks snapshot corruption, and changes database endpoints.
- Option C is an analytical warehouse, not an OLTP database.
- Option D requires tedious manual instance type modifications twice daily.

**References:**
- Amazon RDS User Guide: Stopping and Starting an Amazon RDS DB Instance
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 19 [SAA-C03-D4-Q115]

**Task Statement 4.2**

An architect is launching a Spot Fleet to run compute-intensive batch image processing. The jobs can run on various instance types (e.g., `m5.large`, `c5.large`, `r5.large`). To minimize the probability of Spot interruptions halting the fleet, which Spot allocation strategy should be configured?

- **A)** lowest-price
- **B)** capacity-optimized
- **C)** diversified
- **D)** single-pool

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `B`

**Detailed Explanation:**
The `capacity-optimized` Spot allocation strategy allocates instances from the Spot capacity pools that have the deepest available capacity for the chosen instance types. By drawing from the pools with the highest spare capacity, the probability of Spot interruptions is significantly minimized.
- Option A: `lowest-price` selects the cheapest pool, which often has the highest demand and greatest interruption rate.
- Option C: `diversified` distributes instances evenly across all pools regardless of capacity depth.
- Option D is not a recognized Spot allocation strategy.

**References:**
- Amazon EC2 User Guide: Spot Fleet Allocation Strategies
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 20 [SAA-C03-D4-Q116]

**Task Statement 4.4**

A finance team wants to set up automated alerts whenever AWS spending approaches 80% and 100% of their monthly allocated cloud budget of $10,000, and automatically execute an action to restrict further resource provisioning if spending reaches 110%. Which AWS service natively provides this budget tracking and automated action capability?

- **A)** AWS Budgets and AWS Budgets Actions
- **B)** AWS Cost Explorer
- **C)** AWS Pricing Calculator
- **D)** Amazon CloudWatch Billing Alarms

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
AWS Budgets allows you to set custom cost and usage budgets with email or SNS notifications when actual or forecasted spending exceeds specified thresholds (e.g., 80%, 100%). Furthermore, AWS Budget Actions can automatically execute remediation actions (such as attaching an SCP to deny new resource provisioning or stopping specific EC2/RDS instances) when budget limits are breached.
- Option B: Cost Explorer visualizes past and forecasted costs, but does not execute automated enforcement actions.
- Option C: Pricing Calculator is an estimation tool prior to launching workloads.
- Option D: CloudWatch billing alarms notify via SNS, but do not natively provide automated budget action policies.

**References:**
- AWS Budgets User Guide: Managing Your Costs with AWS Budgets
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 21 [SAA-C03-D4-Q117]

**Task Statement 4.1**

An organization has 200 Amazon S3 buckets across multiple AWS accounts. The management wants a comprehensive organizational dashboard that visualizes storage usage, identifies cost-optimization opportunities (such as incomplete multipart uploads and non-current versions), and scores data protection metrics across all accounts. Which S3 feature provides this capability?

- **A)** Amazon S3 Storage Lens
- **B)** AWS CloudTrail Insights
- **C)** Amazon S3 Inventory
- **D)** AWS Config

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon S3 Storage Lens is a cloud storage analytics feature that delivers organization-wide visibility into object storage usage and activity. It provides an interactive dashboard with over 30 metrics, including cost-optimization recommendations (such as identifying buckets without lifecycle rules or with high percentage of non-current versions) across an entire AWS Organization.
- Option B: CloudTrail Insights detects unusual API call activity.
- Option C: S3 Inventory provides a daily flat CSV list of objects in a single bucket, without multi-account visual dashboards or optimization scoring.
- Option D audits resource configuration rules, but lacks deep S3 storage tier visualization.

**References:**
- Amazon S3 User Guide: Assessing Your Storage with Amazon S3 Storage Lens
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 22 [SAA-C03-D4-Q118]

**Task Statement 4.2**

A financial analytics firm has an existing fleet of 100 Linux EC2 instances running continuous steady-state web servers in `us-east-1` for a long-term contract. The company wants to maximize cost savings and is willing to commit to a 3-year term. They do not plan to change instance families (staying on `m5.large`) or switch regions. Which commitment option provides the absolute highest percentage discount?

- **A)** Standard Reserved Instances (3-Year All Upfront)
- **B)** Convertible Reserved Instances (1-Year No Upfront)
- **C)** Compute Savings Plans (1-Year Partial Upfront)
- **D)** On-Demand Instances

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Standard Reserved Instances with a 3-year commitment and All Upfront payment provide the highest discount rate (up to 72% savings off On-Demand rates) for predictable, steady-state workloads where instance family, operating system, and region are known and fixed.
- Option B: Convertible RIs sacrifice discount depth for flexibility to change instance families.
- Option C: 1-Year Partial Upfront Savings Plans offer lower discounts (~40-50%) than a 3-Year All Upfront Standard RI (~72%).
- Option D pays the highest full retail price with 0% discount.

**References:**
- Amazon EC2 User Guide: Reserved Instances
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 23 [SAA-C03-D4-Q119]

**Task Statement 4.4**

A startup is deploying an application where two microservices communicate frequently across different Availability Zones within the same AWS Region. The network billing shows high inter-AZ data transfer charges ($0.01/GB in each direction). If application latency requirements permit, how can the team minimize inter-AZ data transfer costs?

- **A)** Co-locate communicating instances in the same Availability Zone (or single-AZ deployment for non-critical services) where data transfer within the same AZ using private IPs is free.
- **B)** Route traffic through an Internet Gateway.
- **C)** Deploy an Application Load Balancer in each AZ.
- **D)** Use public IPv4 addresses for communication.

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Data transfer between EC2 instances in different Availability Zones within the same Region incurs inter-AZ data transfer charges ($0.01 per GB in each direction = $0.02/GB total). However, data transfer between EC2 instances in the same Availability Zone using private IP addresses is completely FREE. Where high-availability multi-AZ redundancy is not required for a specific internal processing pipeline, co-locating instances in the same AZ eliminates these charges.
- Option B routes traffic through the internet, incurring NAT Gateway and Internet egress charges.
- Option C adds ALB hourly and LCU charges without eliminating inter-AZ transport.
- Option D incurs additional public IP charges.

**References:**
- Amazon EC2 Pricing: Data Transfer
- AWS Well-Architected Cost Optimization Pillar

</details>

---

### Question 24 [SAA-C03-D4-Q120]

**Task Statement 4.3**

An architect is evaluating database options for an internal inventory lookup tool that is only accessed during office hours, with unpredictable bursts of read traffic and negligible writes. The team wants a relational PostgreSQL-compatible database that scales compute down to 0.5 ACU during idle periods, automatically scales up under load, and avoids paying for fixed provisioned IOPS. Which service is best suited?

- **A)** Amazon Aurora Serverless v2
- **B)** Amazon RDS for PostgreSQL with Provisioned IOPS
- **C)** Amazon Redshift Serverless
- **D)** Amazon DocumentDB with MongoDB compatibility

<details>
<summary><b>View Answer and Architectural Rationale</b></summary>

**Correct Answer:** `A`

**Detailed Explanation:**
Amazon Aurora Serverless v2 is an on-demand, autoscaling configuration for Amazon Aurora. It automatically adjusts compute capacity from 0.5 ACUs up to 128 ACUs in fine-grained fractions of an ACU based on application workload demand, saving up to 90% in database costs compared to provisioning for peak capacity.
- Option B requires provisioning and paying for peak instance compute and expensive IOPS 24/7.
- Option C is for data warehousing and analytics, not operational transactional inventory lookups.
- Option D is a NoSQL document database, not a PostgreSQL-compatible relational database.

**References:**
- Amazon Aurora User Guide: Aurora Serverless v2
- AWS Well-Architected Cost Optimization Pillar

</details>

---

