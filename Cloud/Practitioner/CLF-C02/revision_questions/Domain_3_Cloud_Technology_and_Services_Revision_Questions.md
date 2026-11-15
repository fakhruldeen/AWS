# Domain 3: Cloud Technology & Services Revision Questions (34% Exam Weight)

### Question 1
A solutions architect is designing a high-performance web tier. They need to automatically distribute incoming HTTP/HTTPS traffic across multiple EC2 instances located in different Availability Zones based on the requested URL path. Which service should they choose?
- [ ] A) Network Load Balancer (NLB)
- [ ] B) Application Load Balancer (ALB)
- [ ] C) Amazon Route 53
- [ ] D) AWS Transit Gateway
> **Correct Answer:** B  
> **Rationale:** Application Load Balancer operates at Layer 7 (HTTP/HTTPS) and supports path-based, host-based, and header-based routing to target groups across multiple AZs.

---

### Question 2
A media company needs to store millions of user profile images. The data is accessed frequently during the first 30 days after upload, but rarely accessed afterward. The images must remain immediately retrievable at any time without delay. Which cost-effective strategy is best?
- [ ] A) Store images permanently on an Amazon EBS gp3 volume
- [ ] B) Use an S3 Lifecycle rule to transition objects from S3 Standard to S3 Standard-Infrequent Access (Standard-IA) after 30 days
- [ ] C) Use S3 Glacier Flexible Recovery immediately upon upload
- [ ] D) Attach an Amazon EFS filesystem with provisioned throughput
> **Correct Answer:** B  
> **Rationale:** S3 Standard-IA is designed for data accessed less frequently but requiring immediate, sub-second retrieval when requested, at a much lower storage cost than S3 Standard.

---

### Question 3
An engineering team needs to run background batch processing jobs that can be interrupted and resumed without impacting customers. The team wants to achieve the maximum possible discount on EC2 compute costs. Which instance purchasing option should they select?
- [ ] A) On-Demand Instances
- [ ] B) Spot Instances
- [ ] C) Reserved Instances (Standard 3-year)
- [ ] D) Dedicated Hosts
> **Correct Answer:** B  
> **Rationale:** Spot Instances offer up to a 90% discount compared to On-Demand pricing by leveraging spare EC2 capacity, with the trade-off that AWS can terminate the instance with a 2-minute notice.

---

### Question 4
Which fully managed serverless compute service allows you to execute code in response to events (such as an S3 object upload or DynamoDB table modification) without provisioning or managing virtual machines?
- [ ] A) Amazon EC2
- [ ] B) AWS Elastic Beanstalk
- [ ] C) AWS Lambda
- [ ] D) Amazon ECS on EC2
> **Correct Answer:** C  
> **Rationale:** AWS Lambda is a serverless compute service that runs code in response to events, scales automatically from zero to thousands of concurrent requests, and bills in 1ms increments.

---

### Question 5
Which fully managed NoSQL database service delivers single-digit millisecond performance at any scale, supports key-value and document data models, and provides automated multi-AZ replication?
- [ ] A) Amazon RDS PostgreSQL
- [ ] B) Amazon Aurora
- [ ] C) Amazon DynamoDB
- [ ] D) Amazon Redshift
> **Correct Answer:** C  
> **Rationale:** Amazon DynamoDB is a fully managed serverless NoSQL database providing single-digit millisecond latency, partition-key scaling, and built-in cross-AZ data durability.
