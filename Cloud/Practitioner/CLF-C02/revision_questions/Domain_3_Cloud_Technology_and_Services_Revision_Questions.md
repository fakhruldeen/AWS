# AWS Certified Cloud Practitioner (CLF-C02) - Domain 3: Cloud Technology and Services Revision Questions

> **Weight:** 34% of Scored Content  
> **Questions Count:** 30 Curated Exam-Style Practice Questions  
> **Target Certification:** AWS Certified Cloud Practitioner (`CLF-C02`)  

---

## 📝 Practice Questions

### Question 1 (Category: aws-cloud-technology-services)
A startup wants to run a web application on AWS without managing the underlying servers, operating system patches, or capacity planning. They want to simply upload their code and have AWS handle everything else. Which service best fits this requirement?

- [ ] {'label': 'A', 'text': 'AWS Elastic Beanstalk', 'is_correct': True}
- [ ] {'label': 'B', 'text': 'Amazon EC2', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Amazon Lightsail', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Outposts', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) that allows developers to upload their application code and automatically handles deployment, capacity provisioning, load balancing, auto-scaling, and health monitoring. Amazon EC2 requires you to manage instances, patching, and scaling yourself. Amazon Lightsail is a simplified virtual server offering but still requires some server management. AWS Outposts extends AWS infrastructure to on-premises locations, which is unrelated to this use case.
</details>

### Question 2 (Category: aws-cloud-technology-services)
Which AWS service allows you to run code in response to events (such as an S3 upload or an API Gateway request) without provisioning or managing servers?

- [ ] {'label': 'A', 'text': 'Amazon EC2', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Lambda', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon ECS', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Elastic Beanstalk', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources. You pay only for the compute time consumed — there is no charge when your code is not running. Amazon EC2 requires you to provision and manage virtual servers. Amazon ECS is a container orchestration service that still requires infrastructure decisions. AWS Elastic Beanstalk is a PaaS that provisions EC2 instances behind the scenes.
</details>

### Question 3 (Category: aws-cloud-technology-services)
A media company needs to run Docker containers at scale but does not want to manage the underlying EC2 instances or cluster infrastructure. Which combination of AWS services should they use?

- [ ] {'label': 'A', 'text': 'Amazon ECS with AWS Fargate', 'is_correct': True}
- [ ] {'label': 'B', 'text': 'Amazon EC2 with Docker installed manually', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS Lambda with container images', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon Lightsail with Docker containers', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** Amazon ECS (Elastic Container Service) with AWS Fargate is the correct answer. Fargate is a serverless compute engine for containers that removes the need to manage EC2 instances — you define your container requirements and Fargate handles the rest. Installing Docker manually on EC2 requires managing infrastructure. AWS Lambda with container images has a 15-minute execution limit and 10 GB image size limit, making it unsuitable for long-running container workloads. Lightsail has limited container capabilities and is designed for simpler workloads.
</details>

### Question 4 (Category: aws-cloud-technology-services)
Which AWS service is a container orchestration platform that supports Kubernetes and allows you to run, scale, and manage containerized applications?

- [ ] {'label': 'A', 'text': 'Amazon ECS', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon EKS', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Fargate', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS App Runner', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EKS (Elastic Kubernetes Service) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install and maintain your own Kubernetes control plane. Amazon ECS is AWS's own container orchestration service but does not use Kubernetes. AWS Fargate is a serverless compute engine used with ECS or EKS — it is not an orchestration platform itself. AWS App Runner is a fully managed service for deploying containerized web apps but does not provide Kubernetes compatibility.
</details>

### Question 5 (Category: aws-cloud-technology-services)
A small business owner with limited cloud experience wants to quickly launch a simple WordPress website with a predictable monthly cost. Which AWS service is designed for this use case?

- [ ] {'label': 'A', 'text': 'Amazon EC2 with Auto Scaling', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon Lightsail', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Lambda', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon EKS', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon Lightsail is specifically designed for simple workloads, quick deployments, and users with limited cloud experience. It offers virtual servers, storage, databases, and networking with predictable monthly pricing and a simplified management console. EC2 with Auto Scaling is more complex and does not offer a bundled, predictable monthly price. AWS Lambda is serverless and not suitable for hosting traditional WordPress sites. Amazon EKS is a Kubernetes platform far too complex for a simple WordPress site.
</details>

### Question 6 (Category: aws-cloud-technology-services)
An e-commerce company experiences traffic spikes during holiday sales events. They want their application to automatically add EC2 instances when demand increases and remove them when demand decreases. Which AWS feature provides this capability?

- [ ] {'label': 'A', 'text': 'Elastic Load Balancing', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon EC2 Auto Scaling', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS CloudFormation', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon CloudFront', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EC2 Auto Scaling automatically adjusts the number of EC2 instances based on demand conditions you define (such as CPU utilization or request count). It scales out (adds instances) during spikes and scales in (removes instances) when demand drops, optimizing both performance and cost. Elastic Load Balancing distributes traffic across instances but does not add or remove them. AWS CloudFormation is an infrastructure-as-code tool for provisioning resources, not for dynamic scaling. Amazon CloudFront is a CDN for caching content at edge locations.
</details>

### Question 7 (Category: aws-cloud-technology-services)
Which of the following statements about AWS Lambda is correct?

- [ ] {'label': 'A', 'text': 'Lambda functions can run indefinitely with no time limit', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Lambda automatically scales by running code in response to each trigger event', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Lambda requires you to pre-provision the number of concurrent executions', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Lambda functions must be written exclusively in Python', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Lambda automatically scales by running your code in response to each trigger — each event invocation is handled independently, and Lambda can run thousands of instances of your function concurrently. A standard Lambda function invocation can run for at most 15 minutes (the default timeout is 3 seconds), and even Lambda's longer-running options have fixed limits, so functions cannot run indefinitely. You do not need to pre-provision concurrency (though you can optionally set reserved concurrency). Lambda supports multiple languages including Python, Node.js, Java, Go, .NET, Ruby, and custom runtimes.
</details>

### Question 8 (Category: aws-cloud-technology-services)
Which EC2 instance family is optimized for memory-intensive applications such as in-memory databases, real-time big data analytics, and high-performance caching?

- [ ] {'label': 'A', 'text': 'C-family (Compute Optimized)', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'R-family (Memory Optimized)', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'T-family (General Purpose)', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'P-family (Accelerated Computing)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** R-family instances (Memory Optimized) are designed for workloads that process large data sets in memory, such as in-memory databases (Redis, Memcached), real-time processing of large unstructured data, and Apache Spark-based analytics. C-family instances (Compute Optimized) are for compute-bound tasks like batch processing and scientific modeling. T-family instances (General Purpose) provide a balance of compute, memory, and networking. P-family instances (Accelerated Computing) use GPUs for machine learning and graphics-intensive applications.
</details>

### Question 9 (Category: aws-cloud-technology-services)
An application uses Amazon EC2 Auto Scaling with a minimum of 2 instances, a desired capacity of 4, and a maximum of 8. During a sudden traffic surge, CPU utilization spikes to 95% across all instances. What will Auto Scaling do?

- [ ] {'label': 'A', 'text': 'Terminate instances to save costs since CPU is too high', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Launch additional instances up to the maximum of 8 to handle the load', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Do nothing because the desired capacity is already set to 4', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Send a notification but take no scaling action', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EC2 Auto Scaling will launch additional instances to handle the increased load, up to the configured maximum of 8. When scaling policies detect that CPU utilization exceeds the target threshold, Auto Scaling performs a scale-out action by adding instances. It will never exceed the maximum capacity you set (8 in this case). Auto Scaling does not terminate instances in response to high load — it does the opposite. It does not simply sit idle when scaling policies are triggered, nor does it only notify without action (though it can send SNS notifications alongside scaling).
</details>

### Question 10 (Category: aws-cloud-technology-services)
A development team wants to run a microservice that executes for only 200 milliseconds each time it is called, processes approximately 10 million requests per month, and requires no persistent server. How is this workload billed on AWS Lambda?

- [ ] {'label': 'A', 'text': 'By the number of EC2 instances provisioned per hour', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'By the number of requests and the duration of each function execution', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'A flat monthly fee based on the programming language used', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'By the amount of data stored in the Lambda service', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Lambda pricing is based on two factors: the number of requests (invocations) and the duration of each execution (measured in milliseconds), multiplied by the amount of memory allocated to the function. There are no EC2 instances involved — Lambda is serverless. There is no flat monthly fee or per-language pricing. Lambda does not charge for data storage (any persistent storage would use S3 or DynamoDB with their own pricing). Lambda includes a generous free tier of 1 million requests and 400,000 GB-seconds per month.
</details>

### Question 11 (Category: aws-cloud-technology-services)
Which of the following describes the relationship between Amazon ECS, Amazon EKS, and AWS Fargate?

- [ ] {'label': 'A', 'text': 'ECS and EKS are compute engines; Fargate is an orchestration platform', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'ECS and EKS are container orchestration services; Fargate is a serverless compute engine that can run containers for either service', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Fargate is a container orchestration service; ECS and EKS are different compute engines', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'All three are independent container orchestration platforms that cannot work together', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon ECS and Amazon EKS are container orchestration services — ECS is AWS's proprietary orchestrator, while EKS is managed Kubernetes. AWS Fargate is a serverless compute engine that can be used as the launch type for both ECS and EKS, removing the need to manage the underlying EC2 instances. Think of Fargate as the "how" (serverless infrastructure) and ECS/EKS as the "what" (orchestration layer). They work together, not independently.
</details>

### Question 12 (Category: aws-cloud-technology-services)
A company has a web application behind an Elastic Load Balancer. During peak hours, some EC2 instances become unhealthy. What happens when the load balancer detects an unhealthy instance?

- [ ] {'label': 'A', 'text': 'The load balancer terminates the unhealthy instance and launches a replacement', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'The load balancer stops sending traffic to the unhealthy instance and routes requests to healthy instances', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'The load balancer shuts down entirely until all instances are healthy', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'The load balancer sends an alert but continues routing traffic to the unhealthy instance', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Elastic Load Balancing performs health checks on registered targets. When it detects an unhealthy instance, it stops routing new requests to that instance and distributes traffic only among the remaining healthy instances. The load balancer does not terminate instances — that is the responsibility of EC2 Auto Scaling (if configured). The load balancer never shuts itself down due to unhealthy targets. It does not continue routing traffic to instances it has marked as unhealthy.
</details>

### Question 13 (Category: aws-cloud-technology-services)
A company needs to store millions of user-uploaded images that must be accessible from anywhere via a URL. The data should be highly durable and available. Which AWS storage service is best suited for this use case?

- [ ] {'label': 'A', 'text': 'Amazon EBS', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon S3', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon EFS', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Storage Gateway', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon S3 (Simple Storage Service) is an object storage service designed for storing and retrieving any amount of data from anywhere on the internet. It provides 99.999999999% (11 nines) of durability and makes objects accessible via unique URLs. Amazon EBS is block storage attached to a single EC2 instance and cannot be accessed via URL. Amazon EFS is a network file system for EC2 instances, not designed for public URL access. AWS Storage Gateway is a hybrid storage service for connecting on-premises environments to cloud storage.
</details>

### Question 14 (Category: aws-cloud-technology-services)
A company stores compliance documents in Amazon S3 that are accessed frequently for the first 30 days, then rarely accessed afterward but must be retained for 7 years. Which S3 feature can automatically move objects to a cheaper storage class over time?

- [ ] {'label': 'A', 'text': 'S3 Versioning', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'S3 Lifecycle Policies', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'S3 Cross-Region Replication', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'S3 Object Lock', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** S3 Lifecycle Policies allow you to define rules that automatically transition objects between storage classes based on age. For example, you could move objects to S3 Standard-IA after 30 days and to S3 Glacier after 90 days, optimizing costs over time. S3 Versioning keeps multiple versions of an object but does not change storage classes. S3 Cross-Region Replication copies objects to another Region for disaster recovery. S3 Object Lock prevents objects from being deleted or overwritten (for compliance), but does not manage storage class transitions.
</details>

### Question 15 (Category: aws-cloud-technology-services)
Which Amazon S3 storage class is designed for data with unpredictable access patterns and automatically moves objects between frequent and infrequent access tiers to optimize costs?

- [ ] {'label': 'A', 'text': 'S3 Standard', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'S3 Standard-Infrequent Access', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'S3 Intelligent-Tiering', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'S3 Glacier Flexible Retrieval', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** S3 Intelligent-Tiering automatically moves objects between a frequent access tier and an infrequent access tier based on changing access patterns. It charges a small monthly monitoring fee per object but has no retrieval fees and no minimum storage duration. S3 Standard is designed for frequently accessed data but does not automatically tier. S3 Standard-IA is for infrequently accessed data and charges retrieval fees. S3 Glacier Flexible Retrieval is for archival data with retrieval times of minutes to hours.
</details>

### Question 16 (Category: aws-cloud-technology-services)
An application running on Amazon EC2 needs a high-performance block storage volume that persists independently of the instance lifecycle. Which service provides this?

- [ ] {'label': 'A', 'text': 'Amazon S3', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon EBS', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Instance Store', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon S3 Glacier', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EBS (Elastic Block Store) provides persistent block storage volumes for EC2 instances. EBS volumes persist independently of the instance lifecycle — if you stop or terminate an instance, the EBS volume and its data can be retained. Amazon S3 is object storage, not block storage. Instance Store provides temporary block storage that is physically attached to the host machine — data is lost when the instance is stopped or terminated. S3 Glacier is an archival storage service, not block storage.
</details>

### Question 17 (Category: aws-cloud-technology-services)
A research organization must migrate a large data set to Amazon S3, but the available network would take too long. Which AWS offering can transport the data on a shipped device?

- [ ] {'label': 'A', 'text': 'AWS Direct Connect', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Snowball Edge', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'S3 Transfer Acceleration', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS DataSync', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Snowball Edge is a Snow Family device that AWS ships to the customer for offline data transfer and later ingestion into AWS storage. Since November 7, 2025, Snowball Edge is available only to existing customers; AWS points new customers to AWS DataSync for online transfers, AWS Data Transfer Terminal for secure physical transfers, or AWS Partner solutions. Direct Connect, S3 Transfer Acceleration, and DataSync move data over network connections and therefore do not remove the stated bandwidth constraint.
</details>

### Question 18 (Category: aws-cloud-technology-services)
A media production company needs a shared file system that multiple Linux-based EC2 instances can access simultaneously with standard NFS protocol. Which AWS storage service should they use?

- [ ] {'label': 'A', 'text': 'Amazon EBS', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon S3', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Amazon EFS', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Amazon FSx for Windows File Server', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon EFS (Elastic File System) is a fully managed, elastic NFS file system that can be mounted simultaneously by thousands of EC2 instances across multiple Availability Zones. It uses the standard NFSv4 protocol and is designed for Linux workloads. Amazon EBS volumes can only be attached to a single EC2 instance at a time (with the exception of Multi-Attach for io1/io2 volumes). Amazon S3 is object storage and does not support NFS mounting. Amazon FSx for Windows File Server uses the SMB protocol and is designed for Windows workloads, not Linux/NFS.
</details>

### Question 19 (Category: aws-cloud-technology-services)
Which Amazon S3 storage class provides the lowest cost for data archival with a retrieval time of 12 hours or more?

- [ ] {'label': 'A', 'text': 'S3 Glacier Flexible Retrieval', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'S3 Glacier Deep Archive', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'S3 Standard-Infrequent Access', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'S3 One Zone-Infrequent Access', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** S3 Glacier Deep Archive is the lowest-cost S3 storage class, designed for long-term data archival where retrieval times of 12 hours are acceptable. It is ideal for data that is accessed once or twice a year, such as compliance archives and digital preservation. S3 Glacier Flexible Retrieval is cheaper than standard classes but more expensive than Deep Archive, with retrieval times from minutes to hours. S3 Standard-IA and S3 One Zone-IA are designed for infrequently accessed data but provide millisecond access and cost more than either Glacier class.
</details>

### Question 20 (Category: aws-cloud-technology-services)
A company uses Windows-based file shares for their enterprise applications and wants to migrate to a fully managed AWS solution that supports the SMB protocol and Active Directory integration. Which service should they choose?

- [ ] {'label': 'A', 'text': 'Amazon EFS', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon FSx for Windows File Server', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon S3', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Storage Gateway (File Gateway)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon FSx for Windows File Server is a fully managed Windows file system built on Windows Server. It supports the SMB protocol, NTFS, Active Directory (AD) integration, and Distributed File System (DFS) — making it the natural migration path for Windows file shares. Amazon EFS supports the NFS protocol only (Linux workloads). Amazon S3 is object storage that does not support SMB. AWS Storage Gateway (File Gateway) provides a hybrid solution but acts as a cache in front of S3, not a native Windows file server.
</details>

### Question 21 (Category: aws-cloud-technology-services)
An architect needs to create a point-in-time backup of an Amazon EBS volume that can be used to restore data or create new volumes in the same or different Availability Zone. What should they use?

- [ ] {'label': 'A', 'text': 'EBS Snapshots', 'is_correct': True}
- [ ] {'label': 'B', 'text': 'Amazon S3 Versioning', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS Backup', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon Machine Images (AMI)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** EBS Snapshots are incremental backups of EBS volumes stored in Amazon S3 (managed by AWS). You can use snapshots to restore an existing volume or create new EBS volumes in any Availability Zone within the same Region (or copy them to other Regions). S3 Versioning manages versions of S3 objects, not EBS volumes. AWS Backup is a centralized backup service that can manage EBS snapshots but the fundamental mechanism is still EBS Snapshots. AMIs contain the instance configuration and root volume snapshot but are for launching entire instances, not just restoring individual data volumes.
</details>

### Question 22 (Category: aws-cloud-technology-services)
A hospital needs to maintain on-premises access to medical imaging files for low-latency access while also backing up the data to Amazon S3 for durability and compliance. Which AWS service bridges this hybrid storage requirement?

- [ ] {'label': 'A', 'text': 'AWS Snowball', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Storage Gateway', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon EFS', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Direct Connect', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Storage Gateway is a hybrid cloud storage service that provides on-premises applications with seamless access to virtually unlimited cloud storage. It caches frequently accessed data on-premises for low-latency access while storing the full data set in Amazon S3. This is ideal for hybrid environments where you need local performance and cloud durability. AWS Snowball is for offline data transfer, not ongoing hybrid access. Amazon EFS is a cloud-native file system, not a hybrid bridge. AWS Direct Connect provides a dedicated network connection but does not manage storage caching.
</details>

### Question 23 (Category: aws-cloud-technology-services)
Which of the following is a key difference between Amazon S3 Standard-Infrequent Access (S3 Standard-IA) and S3 One Zone-Infrequent Access (S3 One Zone-IA)?

- [ ] {'label': 'A', 'text': 'S3 Standard-IA has lower storage costs than S3 One Zone-IA', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'S3 One Zone-IA stores data in a single Availability Zone, while S3 Standard-IA stores data across multiple Availability Zones', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'S3 One Zone-IA provides higher durability than S3 Standard-IA', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'S3 Standard-IA has faster retrieval times than S3 One Zone-IA', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** The key difference is availability zone redundancy: S3 Standard-IA stores data redundantly across a minimum of three Availability Zones, while S3 One Zone-IA stores data in only a single AZ. This makes S3 One Zone-IA about 20% cheaper but less resilient — if that AZ is destroyed, the data is lost. S3 Standard-IA is more expensive, not less, than One Zone-IA. S3 Standard-IA has higher durability because of multi-AZ storage. Both provide millisecond retrieval with similar performance.
</details>

### Question 24 (Category: aws-cloud-technology-services)
A company wants to centrally manage and automate backups across multiple AWS services including Amazon EBS, Amazon RDS, Amazon DynamoDB, and Amazon EFS. Which service provides this centralized backup management?

- [ ] {'label': 'A', 'text': 'AWS Backup', 'is_correct': True}
- [ ] {'label': 'B', 'text': 'Amazon S3 Lifecycle Policies', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS CloudFormation', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon Data Lifecycle Manager', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** AWS Backup is a fully managed, centralized backup service that enables you to create backup policies (called backup plans) for multiple AWS services from a single console. It supports EBS, RDS, DynamoDB, EFS, FSx, Aurora, and more. S3 Lifecycle Policies only manage S3 object transitions and expirations. AWS CloudFormation is for infrastructure-as-code, not backup management. Amazon Data Lifecycle Manager specifically manages EBS snapshot and AMI lifecycle policies, not backups across all services.
</details>

### Question 25 (Category: aws-cloud-technology-services)
A company wants to run a MySQL database in the cloud without managing the underlying infrastructure, patching, backups, or failover configuration. Which AWS service provides this managed relational database capability?

- [ ] {'label': 'A', 'text': 'Amazon DynamoDB', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon RDS', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon Redshift', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon ElastiCache', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon RDS (Relational Database Service) is a fully managed relational database service that supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora. It handles provisioning, patching, backups, recovery, and optional Multi-AZ failover. Amazon DynamoDB is a NoSQL key-value database, not relational. Amazon Redshift is a data warehouse for analytics, not transactional workloads. Amazon ElastiCache is an in-memory caching service (Redis or Memcached), not a relational database.
</details>

### Question 26 (Category: aws-cloud-technology-services)
A social media application requires a database that can handle millions of requests per second with single-digit millisecond latency at any scale, using a flexible key-value data model. Which AWS database service is best suited?

- [ ] {'label': 'A', 'text': 'Amazon RDS for MySQL', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon Aurora', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Amazon DynamoDB', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Amazon Neptune', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon DynamoDB is a fully managed NoSQL key-value and document database that delivers single-digit millisecond performance at any scale. It supports millions of requests per second and automatically scales throughput capacity. Amazon RDS for MySQL and Aurora are relational databases that use SQL and are better for structured data with complex queries. Amazon Neptune is a graph database designed for highly connected data sets like social networks and recommendation engines — while it could model social data, it is not a key-value store and does not match the stated requirements.
</details>

### Question 27 (Category: aws-cloud-technology-services)
A data analytics team needs to run complex SQL queries against petabytes of structured data from multiple sources to generate business intelligence reports. Which AWS service is designed for this data warehousing use case?

- [ ] {'label': 'A', 'text': 'Amazon RDS', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon DynamoDB', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Amazon Redshift', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Amazon ElastiCache', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon Redshift is a fully managed data warehouse service designed for large-scale data analytics. It uses columnar storage and massively parallel processing (MPP) to run complex SQL queries against petabytes of data quickly. Amazon RDS is for transactional (OLTP) workloads, not analytical (OLAP) queries at petabyte scale. Amazon DynamoDB is a NoSQL database optimized for low-latency key-value access, not complex SQL analytics. Amazon ElastiCache is an in-memory caching layer, not a data warehouse.
</details>

### Question 28 (Category: aws-cloud-technology-services)
A gaming company needs to add a caching layer in front of their Amazon RDS database to reduce read latency from milliseconds to microseconds for frequently accessed leaderboard data. Which AWS service should they use?

- [ ] {'label': 'A', 'text': 'Amazon DynamoDB Accelerator (DAX)', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Amazon ElastiCache', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon CloudFront', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Amazon Aurora Read Replicas', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon ElastiCache is a fully managed in-memory caching service that supports Redis and Memcached. It can reduce database read latency from milliseconds to microseconds by caching frequently accessed data in memory, making it ideal as a caching layer in front of RDS. DynamoDB Accelerator (DAX) is specifically designed to cache DynamoDB queries, not RDS. Amazon CloudFront is a CDN for caching static and dynamic web content at edge locations, not database query results. Aurora Read Replicas reduce read load on the primary instance but still operate at millisecond latency, not microsecond.
</details>

### Question 29 (Category: aws-cloud-technology-services)
An architect wants to ensure their Amazon RDS database remains available if a single Availability Zone experiences an outage. Which RDS feature provides automatic failover to a standby replica in a different AZ?

- [ ] {'label': 'A', 'text': 'RDS Read Replicas', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'RDS Multi-AZ deployment', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'RDS automated backups', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'RDS Enhanced Monitoring', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** RDS Multi-AZ deployment creates a synchronous standby replica in a different Availability Zone. If the primary DB instance fails or an AZ outage occurs, RDS automatically fails over to the standby with no manual intervention, typically within 60-120 seconds. RDS Read Replicas are asynchronous and designed for read scaling, not automatic failover for high availability. RDS automated backups enable point-in-time recovery but do not provide instant failover. RDS Enhanced Monitoring provides real-time metrics but has nothing to do with failover.
</details>

### Question 30 (Category: aws-cloud-technology-services)
Which statement accurately describes AWS Regions, Availability Zones, and Edge Locations?

- [ ] {'label': 'A', 'text': 'A Region contains one Availability Zone, and each AZ has multiple Edge Locations', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'An Availability Zone contains multiple Regions, and Regions contain Edge Locations', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'A Region consists of multiple isolated Availability Zones, and Edge Locations are separate sites used primarily for content caching', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Edge Locations are the same as Availability Zones, just with a different name', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** An AWS Region is a physical location in the world that consists of multiple isolated and physically separate Availability Zones (typically 3 or more). Each AZ has independent power, cooling, and networking. Edge Locations are separate from Regions and AZs — they are sites used by Amazon CloudFront and other services to cache content closer to end users for low-latency delivery. There are far more Edge Locations (400+) than AZs or Regions worldwide.
</details>

---

## 🔑 Quick Answer Key Summary

- 1. **A**
- 2. **B**
- 3. **A**
- 4. **B**
- 5. **B**
- 6. **B**
- 7. **B**
- 8. **B**
- 9. **B**
- 10. **B**
- 11. **B**
- 12. **B**
- 13. **B**
- 14. **B**
- 15. **C**
- 16. **B**
- 17. **B**
- 18. **C**
- 19. **B**
- 20. **B**
- 21. **A**
- 22. **B**
- 23. **B**
- 24. **A**
- 25. **B**
- 26. **C**
- 27. **C**
- 28. **B**
- 29. **B**
- 30. **C**
