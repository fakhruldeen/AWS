# 🔥 AWS Certified Cloud Practitioner (`CLF-C02`) — Top 300 Most Frequent Repeated Exam Questions

> **Selection Methodology:** Extracted from the canonical 2,716-question Master Bank by selecting the **highest-frequency repeated questions** (292 questions repeated across **3 to 5 independent exam pools**, plus 8 targeted **AWS CAF** questions for balanced 100% blueprint coverage), stratified proportionally to the official **CLF-C02 Exam Blueprint** across all 4 Domains and all 20 sub-topics.

---

## 📊 Domain & Frequency Breakdown

| Domain | Official Weight | Questions Selected | Frequency Distribution (Exam Sources) | Topics Covered |
| :--- | :---: | :---: | :--- | :---: |
| **Domain 1: Cloud Concepts** | 24% | **72** | **5x**: 1 Qs, **4x**: 32 Qs, **3x**: 31 Qs, **2x**: 6 Qs, **1x**: 2 Qs | 5 Topics |
| **Domain 2: Security and Compliance** | 30% | **90** | **4x**: 52 Qs, **3x**: 38 Qs | 5 Topics |
| **Domain 3: Cloud Technology and Services** | 34% | **102** | **5x**: 1 Qs, **4x**: 48 Qs, **3x**: 53 Qs | 6 Topics |
| **Domain 4: Billing, Pricing, and Support** | 12% | **36** | **4x**: 17 Qs, **3x**: 19 Qs | 4 Topics |
| **TOTAL** | **100%** | **300** | **High-Frequency Repeated + Full CAF Coverage** | **20 / 20 Topics** |

---

## 🎯 Domain 1: Cloud Concepts (24% — 72 Questions)

### Question 1 — `CLF-U0495` | 🔁 Repeated in 5 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which of the following is an AWS Well-Architected Framework design principle for operational excellence in the AWS Cloud?**

- A) Deployment to a single Availability Zone
- B) Ability to recover from failure
- C) Design for cost optimization
- D) Perform operations as code

<details>
<summary><strong>Reveal Answer & Explanation (Question 1)</strong></summary>

**Correct Answer:** `D`

**Perform operations as code** (`D`) is a core design principle of the **Operational Excellence** pillar in the AWS Well-Architected Framework. It means defining your entire workload (applications, infrastructure, and operational procedures) as code (e.g., via AWS CloudFormation or CDK) so updates can be automated, versioned, and executed consistently.

- *A is incorrect:* Deploying to a single Availability Zone is an anti-pattern that creates a single point of failure.
- *B is incorrect:* Automatically recovering from failure is a design principle of the **Reliability** pillar, not Operational Excellence.
- *C is incorrect:* Designing for cost optimization belongs to the **Cost Optimization** pillar.

</details>

---

### Question 2 — `CLF-U0390` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which of the following is one of the benefits of moving infrastructure from an on-premises data center to AWS?**

- A) Free support for all enterprise customers.
- B) Automatic data protection.
- C) Reduced Capital Expenditure (CapEx).
- D) AWS holds responsibility for managing customer applications.

<details>
<summary><strong>Reveal Answer & Explanation (Question 2)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Reduced Capital Expenditure (CapEx)**

Moving infrastructure to AWS significantly reduces Capital Expenditure (CapEx). CapEx refers to upfront investments in physical infrastructure like servers, networking equipment, and data centers. By using AWS, you shift from owning and maintaining these resources to renting them on demand. This eliminates the need for large upfront investments, allowing you to pay only for the resources you consume. This shift to an "as-a-service" model is a core benefit of cloud computing.

**Incorrect:**

**A. Automatic data protection** - While AWS offers various data protection services like backups, replication, and disaster recovery, data protection is not automatic. Customers are responsible for configuring and managing these services to meet their specific requirements. AWS provides the tools, but the customer must implement and manage the data protection strategy.

**C. AWS holds responsibility for managing customer applications** - AWS manages the infrastructure layer (hardware, virtualization, networking), but customers are responsible for managing their applications, including operating systems, middleware, runtime environments, and application data. This division of responsibility is known as the Shared Responsibility Model.

**D. Free support for all enterprise customers** - AWS offers different support plans with varying levels of service and pricing. Free support is limited and does not provide the comprehensive assistance that enterprise customers typically require. Enterprise customers usually need to pay for a higher-tier support plan to get the necessary level of support and service level agreements (SLAs).

</details>

---

### Question 3 — `CLF-U0400` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Your application has recently experienced significant global growth, and international users are complaining of high latency. What is the AWS characteristic that can help improve your international users’ experience?**

- A) Elasticity.
- B) Global reach.
- C) Data durability.
- D) High availability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 3)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Global reach**

Global reach refers to AWS's extensive network of data centers and infrastructure distributed around the world. This allows you to deploy your application closer to your international users, reducing latency and improving their experience. By utilizing AWS Regions and Availability Zones in different geographic locations, you can minimize the distance data needs to travel, resulting in faster response times and a better user experience. AWS services like Amazon CloudFront (a CDN) also contribute to global reach by caching content closer to users.

**Incorrect:**

**A. Data durability** - Data durability refers to the ability of data to survive failures or corruption. While important for data protection, it doesn't directly address the issue of latency experienced by international users.

**B. Elasticity** - Elasticity refers to the ability of AWS resources to scale up or down automatically based on demand. While elasticity can help handle increased traffic from international users, it doesn't directly reduce latency caused by geographic distance.

**D. High availability** - High availability refers to the ability of a system to remain operational even if some of its components fail. While important for ensuring your application is always accessible, it doesn't directly address the issue of latency experienced by international users. High availability ensures uptime, but not necessarily low latency for globally distributed users.

</details>

---

### Question 4 — `CLF-U0401` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**What are the connectivity options that can be used to build hybrid cloud architectures? (Choose TWO)**

- A) AWS Artifact.
- B) AWS Cloud9.
- C) AWS Direct Connect.
- D) AWS CloudTrail.
- E) AWS VPN.

<details>
<summary><strong>Reveal Answer & Explanation (Question 4)</strong></summary>

**Correct Answer:** `C, E`

**Correct answer: AWS Direct Connect**

AWS Direct Connect establishes a dedicated network connection from your premises to AWS. This private connection allows you to create hybrid cloud environments by providing a consistent and reliable network experience, often with lower latency and increased bandwidth compared to internet-based connections. It bypasses the public internet, enhancing security and predictability for data transfer between your on-premises infrastructure and AWS.

**Correct answer: AWS VPN**

AWS VPN provides secure connections between your on-premises networks, remote offices, client devices, and the AWS global network. AWS VPN has two services: AWS Site-to-Site VPN and AWS Client VPN. AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to your Amazon VPC. AWS Client VPN enables you to securely connect users to AWS resources or your on-premises network.

**Incorrect:**

**A. AWS Artifact** - AWS Artifact is a service that provides on-demand access to AWS' compliance reports and agreements. It is a compliance service and does not provide network connectivity for hybrid cloud architectures.

**C. AWS Cloud9** - AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug code with just a browser. It is a development tool and does not provide network connectivity for hybrid cloud architectures.

**D. AWS CloudTrail** - AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. It records AWS API calls and delivers log files to you. It is an auditing and logging service and does not provide network connectivity for hybrid cloud architectures.

</details>

---

### Question 5 — `CLF-U0579` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which of the following should be considered when performing a TCO analysis to compare the costs of running an application on AWS instead of on-premises?**

- A) Application development.
- B) Market research.
- C) Business analysis.
- D) Physical hardware.

<details>
<summary><strong>Reveal Answer & Explanation (Question 5)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Physical hardware**

When performing a Total Cost of Ownership (TCO) analysis to compare running an application on AWS versus on-premises, physical hardware is a crucial consideration. On-premises environments require upfront investment in servers, networking equipment, storage, and other hardware components. These costs are largely eliminated when migrating to AWS, as AWS handles the infrastructure management. The TCO analysis should include the cost of purchasing, maintaining, and replacing this hardware, as well as the associated costs of power, cooling, and data center space. AWS offers a pay-as-you-go model, which can significantly reduce capital expenditure and operational expenses related to physical hardware.

**Incorrect:**

**A. Market research** - Market research is important for understanding the competitive landscape and customer needs, but it is not a direct factor in comparing the costs of running an application on AWS versus on-premises. While market research might influence business decisions related to the application, it doesn't directly impact the TCO analysis itself.

**B. Business analysis** - Business analysis helps in understanding the requirements and objectives of the application, but it is not a direct cost factor in a TCO analysis. Business analysis informs the overall strategy and design, but the TCO focuses on the tangible costs associated with infrastructure and operations.

**D. Application development** - Application development costs are generally independent of the infrastructure choice (AWS or on-premises). The cost of developing the application will be incurred regardless of where it is hosted. While some AWS services might offer tools to accelerate development, the core development effort is not a primary factor in a TCO comparison focused on infrastructure costs.

</details>

---

### Question 6 — `CLF-U0597` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**The TCO gap between AWS infrastructure and traditional infrastructure has widened over the recent years. Which of the following could be the reason for that?**

- A) AWS helps customers invest more in capital expenditures.
- B) AWS automates all infrastructure operations, so customers save more on human resources costs.
- C) AWS continues to lower the cost of cloud computing for its customers.
- D) AWS secures AWS resources at no additional charge.

<details>
<summary><strong>Reveal Answer & Explanation (Question 6)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS continues to lower the cost of cloud computing for its customers**

AWS consistently strives to reduce the cost of its services through various optimizations, such as economies of scale, improved hardware, and increased efficiency. These cost reductions are often passed on to customers, widening the TCO gap between AWS and traditional infrastructure. Traditional infrastructure typically involves significant upfront capital expenditure, ongoing maintenance costs, and limited scalability, making it less cost-effective than AWS over time. AWS's pay-as-you-go model and continuous cost optimization efforts contribute to a lower TCO for its customers.

**Incorrect:**

**A. AWS secures AWS resources at no additional charge** - While AWS provides a secure infrastructure and some basic security features at no additional charge, advanced security services and configurations often incur costs. Therefore, this is not the primary reason for the widening TCO gap. Security is a shared responsibility, and customers are responsible for securing their applications and data within the AWS cloud.

**B. AWS automates all infrastructure operations, so customers save more on human resources costs** - AWS provides many automation tools and services, but it doesn't automate *all* infrastructure operations. Customers still need to manage and configure their resources, and some level of human resources is required. While automation does contribute to cost savings, it's not the sole or primary driver of the widening TCO gap.

**C. AWS helps customers invest more in capital expenditures** - AWS is designed to reduce capital expenditures (CapEx) by allowing customers to pay for resources on demand, rather than investing in physical hardware. This shift from CapEx to OpEx (operational expenditure) is a key benefit of cloud computing and contributes to the TCO gap, but AWS does not help customers invest more in CapEx.

</details>

---

### Question 7 — `CLF-U0588` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**What is the framework created by AWS Professional Services that helps organizations design a road map to successful cloud adoption?**

- A) AWS Secrets Manager.
- B) AWS WAF.
- C) AWS CAF.
- D) Amazon EFS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 7)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS CAF**

The AWS Cloud Adoption Framework (AWS CAF) is a framework created by AWS Professional Services to help organizations develop and execute cloud adoption strategies. It provides a structured approach to cloud transformation, enabling organizations to identify and address gaps in skills, processes, and technology. The CAF organizes guidance into perspectives, including Business, People, Governance, Platform, Security, and Operations. By using the AWS CAF, organizations can accelerate their cloud journey and achieve their desired business outcomes.

**Incorrect:**

**A. AWS WAF** - AWS WAF (Web Application Firewall) is a service that protects web applications from common web exploits and bots. It filters malicious traffic and allows legitimate traffic to reach your application. It is not a framework for cloud adoption.

**C. Amazon EFS** - Amazon EFS (Elastic File System) is a fully managed, scalable, elastic, cloud-native NFS file system. It is designed to provide shared file storage for use with AWS cloud services and on-premises resources. It is not a framework for cloud adoption.

**D. AWS Secrets Manager** - AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycle. It is focused on security and secret management, not on providing a roadmap for cloud adoption.

</details>

---

### Question 8 — `CLF-U0035` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which of the following are important design principles you should adopt when designing systems on AWS? (Choose TWO)**

- A) Always use Global Services in your architecture rather than Regional Services.
- B) Always choose to pay as you go.
- C) Treat servers as fixed resources.
- D) Automate wherever possible.
- E) Remove single points of failure.

<details>
<summary><strong>Reveal Answer & Explanation (Question 8)</strong></summary>

**Correct Answer:** `D, E`

**Correct answer: Automate wherever possible**

Automation is a key design principle in cloud computing. By automating tasks such as infrastructure provisioning (using services like AWS CloudFormation or Terraform), deployment (using AWS CodeDeploy), and scaling (using Auto Scaling), you can reduce manual errors, improve efficiency, and respond quickly to changes in demand. Automation also enables infrastructure as code, making your infrastructure more manageable and repeatable.

**Correct answer: Remove single points of failure**

Designing for high availability and fault tolerance is crucial in cloud environments. Single points of failure can cause significant disruptions. To mitigate this, you should distribute your application across multiple Availability Zones (AZs) within a Region, use load balancers to distribute traffic, and implement data replication and backup strategies. Services like Amazon S3 are designed for high availability and durability, reducing the risk of data loss.

**Incorrect:**

**A. Always choose to pay as you go** - While pay-as-you-go is a fundamental aspect of AWS pricing, it's not always the most cost-effective option. Depending on your usage patterns, reserved instances or savings plans might offer significant cost savings. The best approach depends on workload characteristics and commitment levels.

**B. Treat servers as fixed resources** - In the cloud, servers should be treated as disposable or replaceable resources. This is a core principle of cloud computing. Instead of relying on individual servers, you should design your applications to be resilient to server failures and able to scale horizontally by adding or removing instances as needed. This is often achieved using services like Auto Scaling and Elastic Load Balancing.

**D. Always use Global Services in your architecture rather than Regional Services** - The choice between Global and Regional services depends on the specific requirements of your application. Global services like Amazon CloudFront and Route 53 are used for content delivery and DNS management, respectively, and are designed to operate globally. Regional services, such as EC2 and RDS, are deployed within specific AWS Regions and provide compute and database resources. Using only Global services would limit your ability to deploy applications close to your users and leverage the benefits of Regional services for compute and data residency.

</details>

---

### Question 9 — `CLF-U0392` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which statement best describes the operational excellence pillar of the AWS Well-Architected Framework?**

- A) The ability of a system to recover gracefully from failure.
- B) The efficient use of computing resources to meet requirements.
- C) The ability to monitor systems and improve supporting processes and procedures.
- D) The ability to manage datacenter operations more efficiently.

<details>
<summary><strong>Reveal Answer & Explanation (Question 9)</strong></summary>

**Correct Answer:** `C`

**Correct answer: The ability to monitor systems and improve supporting processes and procedures**

The Operational Excellence pillar of the AWS Well-Architected Framework focuses on running and monitoring systems to deliver business value and to continually improve processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations. Monitoring systems allows for identifying areas of improvement and implementing changes to enhance efficiency and reliability. This includes using tools like Amazon CloudWatch for monitoring and AWS CloudTrail for auditing.

**Incorrect:**

**B. The ability of a system to recover gracefully from failure** - This statement describes the Reliability pillar of the AWS Well-Architected Framework, not the Operational Excellence pillar. Reliability focuses on the ability of a system to recover from failures and continue to function as intended.

**C. The efficient use of computing resources to meet requirements** - This statement describes the Efficiency pillar (or more formally, the Performance Efficiency pillar) of the AWS Well-Architected Framework. It focuses on using computing resources in the most efficient way to meet system requirements, including selecting the right instance types and optimizing resource utilization.

**D. The ability to manage datacenter operations more efficiently** - While operational excellence can contribute to efficient datacenter management, this option is too narrow. The Operational Excellence pillar is broader than just datacenter operations; it encompasses all aspects of running and monitoring systems, including automation, event response, and continuous improvement, regardless of the underlying infrastructure.

</details>

---

### Question 10 — `CLF-U0448` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which of the following are pillars of the AWS Well-Architected Framework? (Select TWO)**

- A) Multiple Availability Zones.
- B) Performance efficiency.
- C) Security.
- D) Encryption usage.
- E) High availability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 10)</strong></summary>

**Correct Answer:** `B, C`

The AWS Well-Architected Framework has six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability. Performance Efficiency and Security are both official pillars.
Multiple Availability Zones is an infrastructure concept and a deployment strategy, not a Well-Architected pillar. Encryption usage is a security practice that falls under the Security pillar, not a pillar in its own right. High availability is a design goal associated with the Reliability pillar, not a standalone pillar.

</details>

---

### Question 11 — `CLF-U0011` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which service provides DNS in the AWS cloud?**

- A) Route 53.
- B) AWS Config.
- C) Amazon CloudFront.
- D) Amazon EMR.

<details>
<summary><strong>Reveal Answer & Explanation (Question 11)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Route 53**

Route 53 is AWS's scalable and highly available Domain Name System (DNS) web service. It translates human-readable domain names (like example.com) into the IP addresses that computers use to connect to each other. Route 53 connects user requests to infrastructure running in AWS, such as EC2 instances, Elastic Load Balancers, or S3 buckets, and can also be used to route users to infrastructure outside of AWS. It offers features like health checking to ensure traffic is routed only to healthy endpoints, and traffic flow policies to manage complex routing configurations.

**Incorrect:**

**B. AWS Config** - AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. It continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. It is not related to DNS.

**C. Amazon CloudFront** - Amazon CloudFront is a content delivery network (CDN) service. While CloudFront can work with Route 53 to route users to the nearest edge location for faster content delivery, CloudFront itself does not provide DNS services. It caches content and delivers it to users from edge locations around the world.

**D. Amazon EMR** - Amazon EMR (Elastic MapReduce) is a managed cluster platform that lets you run big data frameworks like Apache Hadoop and Apache Spark to process and analyze vast amounts of data. It is not related to DNS services.

</details>

---

### Question 12 — `CLF-U0019` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**A company is planning to host an educational website on AWS. Their video courses will be streamed all around the world. Which of the following AWS services will help achieve high transfer speeds?**

- A) Amazon SNS.
- B) Amazon Kinesis Video Streams.
- C) AWS CloudFormation.
- D) Amazon CloudFront.

<details>
<summary><strong>Reveal Answer & Explanation (Question 12)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Amazon CloudFront**

Amazon CloudFront is a content delivery network (CDN) service that accelerates the delivery of static and dynamic web content to users all over the world. CloudFront works by caching content in edge locations, which are geographically distributed data centers. When a user requests content, CloudFront delivers it from the nearest edge location, resulting in lower latency and faster transfer speeds. This is especially beneficial for streaming video content globally, as it ensures a smooth viewing experience for users regardless of their location. CloudFront integrates seamlessly with other AWS services, such as Amazon S3 (for storing the video files) and AWS Shield (for DDoS protection).

**Incorrect:**

**A. AWS CloudFormation** - AWS CloudFormation is an Infrastructure as Code (IaC) service that allows you to define and provision AWS infrastructure using code. While CloudFormation is useful for automating the deployment of the website, it does not directly improve content transfer speeds.

**C. Amazon SNS** - Amazon Simple Notification Service (SNS) is a messaging service that enables you to send notifications to subscribers. While SNS can be used to notify users about new video courses, it does not directly improve content transfer speeds.

**D. Amazon Kinesis Video Streams** - Amazon Kinesis Video Streams is a service for securely streaming video from devices to AWS for analytics, machine learning (ML), and other processing. It is designed for capturing and processing video streams, not for delivering pre-recorded video content to end-users for viewing. Therefore, it's not the appropriate service for achieving high transfer speeds for an educational website's video courses.

</details>

---

### Question 13 — `CLF-U0043` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following procedures will help reduce your Amazon S3 costs?**

- A) Use the Import/Export feature to move old files automatically to Amazon Glacier.
- B) Use the right combination of storage classes based on different use cases.
- C) Pick the right Availability Zone for your S3 bucket.
- D) Move all the data stored in S3 standard to EBS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 13)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Use the right combination of storage classes based on different use cases**

Amazon S3 offers various storage classes optimized for different access patterns and storage durations. Using the appropriate storage class for your data can significantly reduce costs. For example, frequently accessed data should be stored in S3 Standard, while infrequently accessed data can be stored in S3 Standard-IA (Infrequent Access) or S3 One Zone-IA, which have lower storage costs but higher retrieval costs. For archival data, S3 Glacier and S3 Glacier Deep Archive offer the lowest storage costs but have longer retrieval times. By analyzing your data access patterns and choosing the most suitable storage class, you can optimize your S3 costs.

**Incorrect:**

**A. Use the Import/Export feature to move old files automatically to Amazon Glacier** - AWS Import/Export (now AWS Snow Family) is used for transferring large amounts of data into and out of AWS using physical storage devices. It's not an automated feature for moving files to Glacier. While moving old files to Glacier is a good cost-saving strategy, Import/Export isn't the right tool for automating this.

**C. Move all the data stored in S3 standard to EBS** - EBS (Elastic Block Storage) is designed for persistent block storage for use with EC2 instances. It is generally more expensive than S3 for storing large amounts of data, especially data that is not actively being used by a running EC2 instance. Moving data from S3 Standard to EBS would likely increase your storage costs, not reduce them.

**D. Pick the right Availability Zone for your S3 bucket** - S3 is a regional service, not an Availability Zone-specific service. When you create an S3 bucket, you choose an AWS Region, not a specific Availability Zone. S3 automatically stores your data across multiple Availability Zones within the chosen Region for high availability and durability. Therefore, selecting an Availability Zone is not a relevant factor in S3 cost optimization.

</details>

---

### Question 14 — `CLF-U0044` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following activities may help reduce your AWS monthly costs?**

- A) Enabling Amazon EC2 Auto Scaling for all of your workloads.
- B) Using the AWS Network Load Balancer (NLB) to load balance the incoming HTTP requests.
- C) Removing all of your Cost Allocation Tags.
- D) Deploying your AWS resources across multiple Availability Zones.

<details>
<summary><strong>Reveal Answer & Explanation (Question 14)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Enabling Amazon EC2 Auto Scaling for all of your workloads**

Amazon EC2 Auto Scaling helps you maintain application availability and allows you to automatically add or remove EC2 instances based on demand. By scaling down during periods of low demand, you reduce the number of running instances, which directly translates to lower EC2 costs. This is an example of optimizing resource utilization to reduce costs.

**Correct answer: Creating a lifecycle policy to move infrequently accessed data to less expensive storage tiers**

Lifecycle policies automate the movement of data to more cost-effective storage tiers based on access patterns. For example, infrequently accessed data in Amazon S3 can be moved from the Standard tier to S3 Standard-IA (Infrequent Access) or S3 Glacier, which have lower storage costs. This optimizes storage costs based on data usage.

**Incorrect:**

**A. Deploying your AWS resources across multiple Availability Zones** - Deploying resources across multiple Availability Zones (AZs) increases availability and fault tolerance, but it generally increases costs. You are running duplicate resources in different locations. While beneficial for resilience, it does not directly reduce monthly costs.

**D. Using the AWS Network Load Balancer (NLB) to load balance the incoming HTTP requests** - Using an NLB itself doesn't inherently reduce costs. While load balancing is important for distributing traffic and improving application performance, the NLB has its own associated costs. It's a necessary component for many architectures, but not a cost-saving measure in isolation.

**E. Removing all of your Cost Allocation Tags** - Cost Allocation Tags are used to organize and track your AWS costs. Removing them would make it harder to understand where your money is being spent, hindering your ability to identify cost-saving opportunities. Removing tags does not reduce costs, it reduces visibility into costs.

</details>

---

### Question 15 — `CLF-U0045` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which AWS services can be used to improve the performance of a global application and reduce latency for its users? (Choose TWO)**

- A) AWS KMS.
- B) AWS Global accelerator.
- C) AWS Direct Connect.
- D) AWS Glue.
- E) Amazon CloudFront.

<details>
<summary><strong>Reveal Answer & Explanation (Question 15)</strong></summary>

**Correct Answer:** `B, E`

**Correct answer: AWS Global accelerator**

AWS Global Accelerator improves global application performance by directing traffic to optimal endpoints over the AWS global network. It uses Anycast static IP addresses, minimizing latency and improving reliability for users worldwide. By routing traffic to the nearest healthy endpoint, it ensures a consistent and fast user experience, regardless of their location.

**Correct answer: Amazon CloudFront**

Amazon CloudFront is a content delivery network (CDN) service that caches content at edge locations around the world. When a user requests content, CloudFront serves it from the nearest edge location, reducing latency and improving performance. This is especially beneficial for applications with a global user base, as it ensures fast content delivery regardless of the user's location.

**Incorrect:**

**B. AWS KMS** - AWS Key Management Service (KMS) is a managed service that lets you easily create and control the keys used to encrypt your data. While important for security, it does not directly improve application performance or reduce latency for users.

**D. AWS Glue** - AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. It is used for data processing and does not directly impact the performance or latency of a global application for end-users.

**E. AWS Direct Connect** - AWS Direct Connect establishes a dedicated network connection from your on-premises environment to AWS. While it can improve network performance compared to public internet, it doesn't inherently reduce latency for a global application's users in the same way that content caching (CloudFront) or intelligent traffic routing (Global Accelerator) does. It's more about consistent bandwidth and private connectivity.

</details>

---

### Question 16 — `CLF-U0055` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**What are the Amazon RDS features that can be used to improve the availability of your database? (Choose TWO)**

- A) AWS Regions.
- B) Multi-AZ Deployment.
- C) Automatic patching.
- D) Read Replicas.
- E) Edge Locations.

<details>
<summary><strong>Reveal Answer & Explanation (Question 16)</strong></summary>

**Correct Answer:** `B, D`

**Correct answer: Read Replicas**

Read Replicas are used to increase the read performance and availability of your database. They allow you to offload read traffic from the primary database instance, reducing the load and improving responsiveness. In the event of a primary database failure, a Read Replica can be promoted to become a standalone database instance, providing a failover mechanism and improving availability.

**Correct answer: Multi-AZ Deployment**

Multi-AZ deployments provide enhanced availability and durability for database instances. When you provision a Multi-AZ database instance, Amazon RDS automatically creates a synchronous standby replica in a different Availability Zone. In case of a planned or unplanned outage, Amazon RDS automatically fails over to the standby replica, minimizing downtime and improving availability.

**Incorrect:**

**B. AWS Regions** - While AWS Regions provide geographical redundancy, they do not directly improve the availability of a single database instance. Regions are more relevant for disaster recovery strategies involving replicating data across different geographical locations, not for immediate failover within the same region.

**C. Edge Locations** - Edge Locations are part of the Amazon CloudFront content delivery network (CDN) and are used to cache and distribute content closer to users, reducing latency. They are not directly related to database availability.

**D. Automatic patching** - Automatic patching helps maintain the security and stability of the database by applying software updates. While important for overall database health, it does not directly provide a mechanism for high availability or failover in the event of an outage. Patching typically involves a brief period of unavailability, which Multi-AZ deployments are designed to mitigate.

</details>

---

### Question 17 — `CLF-U0059` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Savings Plans are available for which of the following AWS compute services? (Choose TWO)**

- A) AWS Batch.
- B) AWS Outposts.
- C) Amazon Lightsail.
- D) Amazon EC2.
- E) AWS Lambda.

<details>
<summary><strong>Reveal Answer & Explanation (Question 17)</strong></summary>

**Correct Answer:** `D, E`

**Correct answer: AWS Lambda**

Savings Plans provide a flexible pricing model that offers lower prices on AWS compute usage in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a 1- or 3-year term. Compute Savings Plans apply to AWS Lambda usage. This means you can reduce your Lambda costs by committing to a certain amount of compute power over a period of time.

**Correct answer: Amazon EC2**

Savings Plans are indeed applicable to Amazon EC2 instances. There are two types of Savings Plans for EC2: Compute Savings Plans and EC2 Instance Savings Plans. Compute Savings Plans provide the most flexibility and automatically apply to EC2 instance usage regardless of instance family, size, AZ, Region, OS, or tenancy. EC2 Instance Savings Plans provide the lowest prices and offer savings in exchange for commitment to usage of individual instance families in a Region.

**Incorrect:**

**B. AWS Outposts** - Savings Plans do not directly apply to AWS Outposts. AWS Outposts has its own pricing structure, which typically involves an upfront fee for the Outpost rack and ongoing charges for services consumed on the Outpost.

**D. AWS Batch** - AWS Batch itself doesn't directly have Savings Plans. However, AWS Batch jobs often run on Amazon EC2 instances. If the Batch jobs are running on EC2, then Savings Plans for EC2 can help reduce the cost of the underlying EC2 instances used by AWS Batch.

**E. Amazon Lightsail** - Savings Plans are not available for Amazon Lightsail. Lightsail offers simple, bundled pricing plans that include compute, storage, and data transfer. The pricing is fixed and does not integrate with Savings Plans.

</details>

---

### Question 18 — `CLF-U0060` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**A company has business critical workloads hosted on AWS and they are unwilling to accept any downtime. Which of the following is a recommended best practice to protect their workloads in the event of an unexpected natural disaster?**

- A) Replicate data across multiple Edge Locations worldwide and use Amazon CloudFront to perform automatic failover in the event of an outage.
- B) Deploy AWS resources across multiple Availability Zones within the same AWS Region.
- C) Create point-in-time backups in another subnet and recover this data when a disaster occurs.
- D) Deploy AWS resources to another AWS Region and implement an Active-Active disaster recovery strategy.

<details>
<summary><strong>Reveal Answer & Explanation (Question 18)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Deploy AWS resources to another AWS Region and implement an Active-Active disaster recovery strategy**

An Active-Active disaster recovery strategy involves running workloads simultaneously in multiple AWS Regions. In the event of a disaster in one Region, traffic is automatically routed to the other Region, ensuring minimal to no downtime. This approach provides the highest level of resilience and is suitable for business-critical workloads that cannot tolerate any interruption. Utilizing multiple AWS Regions provides geographic diversity, mitigating the risk of a single event impacting all resources. An Active-Active setup requires careful planning and configuration to ensure data consistency and seamless failover, but it's the best option for near-zero downtime requirements.

**Incorrect:**

**B. Deploy AWS resources across multiple Availability Zones within the same AWS Region** - While deploying across multiple Availability Zones (AZs) within a Region improves availability and fault tolerance, it does not protect against a Region-wide disaster. A natural disaster could potentially impact the entire Region, rendering this strategy ineffective for complete disaster recovery.

**C. Create point-in-time backups in another subnet and recover this data when a disaster occurs** - Creating backups is a good practice for data protection, but recovering from backups can take a significant amount of time, leading to downtime. This approach is not suitable for workloads that require near-zero downtime. Also, subnets are a networking concept within a VPC, not a disaster recovery location.

**D. Replicate data across multiple Edge Locations worldwide and use Amazon CloudFront to perform automatic failover in the event of an outage** - Edge Locations and Amazon CloudFront are primarily used for content delivery and caching. While CloudFront can improve performance and availability for static content, it is not designed for running business-critical workloads or providing full disaster recovery capabilities for applications and databases. CloudFront is not a substitute for a comprehensive disaster recovery strategy involving multiple AWS Regions.

</details>

---

### Question 19 — `CLF-U0083` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following are use cases for Amazon S3? (Choose TWO)**

- A) Hosting static websites.
- B) Hosting websites that require sustained high CPU utilization.
- C) Cost-effective database and log storage.
- D) A media store for the CloudFront service.
- E) Processing data streams at any scale.

<details>
<summary><strong>Reveal Answer & Explanation (Question 19)</strong></summary>

**Correct Answer:** `A, D`

**Correct answer: A media store for the CloudFront service**

Amazon S3 is often used as the origin store for Amazon CloudFront, a content delivery network (CDN). CloudFront caches content from S3 (or other origins) and distributes it to edge locations globally, providing faster access for users. S3 provides durable and scalable storage for the media files that CloudFront distributes.

**Correct answer: Hosting static websites**

Amazon S3 can host static websites. This means websites that consist of HTML, CSS, JavaScript, images, and other static files. S3 provides the storage and retrieval of these files, and you can configure S3 buckets for website hosting. This is a cost-effective and scalable way to host static websites.

**Incorrect:**

**A. Hosting websites that require sustained high CPU utilization** - Amazon S3 is an object storage service, not a compute service. Websites requiring sustained high CPU utilization are better suited for services like Amazon EC2, AWS Elastic Beanstalk, or AWS Lambda.

**C. Processing data streams at any scale** - While S3 can store data streams, it's not designed for real-time processing. Services like Amazon Kinesis Data Streams or Amazon Managed Streaming for Apache Kafka (MSK) are better suited for processing data streams at any scale.

**E. Cost-effective database and log storage** - While S3 can be used for log storage, it's not a database service. For database storage, services like Amazon RDS, Amazon DynamoDB, or Amazon Aurora are more appropriate. While S3 can be cost-effective for storing large volumes of data, other services may be more suitable for database storage depending on the specific requirements.

</details>

---

### Question 20 — `CLF-U0398` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Sarah has deployed an application in the Northern California (us-west-1) region. After examining the application’s traffic, she notices that about 30% of the traffic is coming from Asia. What can she do to reduce latency for the users in Asia?**

- A) Replicate the current resources across multiple Availability Zones within the same region.
- B) Migrate the application to a hosting provider in Asia.
- C) Recreate the website content.
- D) Create a CDN using CloudFront, so that content is cached at Edge Locations close to and in Asia.

<details>
<summary><strong>Reveal Answer & Explanation (Question 20)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Create a CDN using CloudFront, so that content is cached at Edge Locations close to and in Asia**

CloudFront is AWS's Content Delivery Network (CDN) service. A CDN caches content (like website images, videos, or even entire web pages) at Edge Locations, which are geographically distributed data centers. When a user in Asia requests content, CloudFront serves it from the nearest Edge Location, reducing latency compared to fetching it from the origin server in Northern California. This significantly improves the user experience for users in Asia.

**Incorrect:**

**A. Replicate the current resources across multiple Availability Zones within the same region** - While deploying across multiple Availability Zones (AZs) within the same region (us-west-1) improves the application's availability and fault tolerance, it does not reduce latency for users in Asia. The data is still served from the us-west-1 region, and the geographical distance remains the same.

**B. Migrate the application to a hosting provider in Asia** - Migrating the entire application to a hosting provider in Asia could reduce latency for Asian users, but it's a much more complex and potentially expensive solution than using a CDN. It involves significant effort to move the application, data, and infrastructure. CloudFront provides a simpler and more cost-effective way to address latency issues for geographically dispersed users.

**C. Recreate the website content** - Recreating the website content itself will not reduce latency for users in Asia. The location of the content server is the primary factor affecting latency due to geographical distance. Recreating the content doesn't change where the content is being served from.

</details>

---

### Question 21 — `CLF-U0402` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following will impact the price paid for an EC2 instance? (Choose TWO)**

- A) Instance type.
- B) The Availability Zone where the instance is provisioned.
- C) Load balancing.
- D) Number of buckets.
- E) Number of private IPs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 21)</strong></summary>

**Correct Answer:** `A, B`

**Correct answer: Instance type**

The instance type is a major factor in EC2 pricing. Different instance types offer varying amounts of CPU, memory, storage, and network capacity. Instance types are grouped into families (e.g., general purpose, compute optimized, memory optimized) and sizes (e.g., small, medium, large), each with a different hourly or on-demand price. Choosing the right instance type for your workload is crucial for cost optimization.

**Correct answer: The Availability Zone where the instance is provisioned**

While less common, the Availability Zone (AZ) can impact EC2 pricing. AWS occasionally offers different pricing in different AZs due to varying supply and demand. This is not always the case, but it is a factor to consider. Data transfer costs between AZs also contribute to the overall cost.

**Incorrect:**

**A. Number of buckets** - The number of S3 buckets does not directly impact the price of an EC2 instance. S3 pricing is based on storage used, data transfer, and requests made to the S3 service, not the number of buckets. EC2 and S3 are separate services with independent pricing models.

**C. Load balancing** - Load balancing itself is a separate service (Elastic Load Balancing or ELB) with its own pricing model based on the number of connections, data processed, and rules evaluated. While an EC2 instance behind a load balancer is part of the overall architecture, the load balancing configuration does not directly change the price of the EC2 instance itself. The instance type and usage do.

**E. Number of private IPs** - The number of private IP addresses assigned to an EC2 instance does not directly impact the price. AWS does not charge for private IP addresses within the VPC. You are charged for the EC2 instance itself and any public IP addresses (Elastic IPs) that are not associated with a running instance.

</details>

---

### Question 22 — `CLF-U0403` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following statements describes the AWS Cloud’s agility?**

- A) AWS allows you to host your applications in multiple regions around the world.
- B) AWS provides customizable hardware at the lowest possible cost.
- C) AWS allows you to provision resources in minutes.
- D) AWS allows you to pay upfront to reduce costs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 22)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS allows you to provision resources in minutes**

Agility in the context of cloud computing, and specifically AWS, refers to the ability to rapidly develop, test, and launch new applications and services. AWS provides a vast array of services that can be provisioned and configured very quickly, often in minutes, through the AWS Management Console, AWS CLI, or Infrastructure as Code tools like AWS CloudFormation or Terraform. This speed allows organizations to experiment more, iterate faster, and respond quickly to changing market conditions. The ability to quickly provision resources is a key characteristic of the cloud's agility.

**Incorrect:**

**A. AWS allows you to pay upfront to reduce costs** - While AWS offers Reserved Instances and Savings Plans that allow you to pay upfront or commit to a certain usage level to reduce costs, this is primarily related to cost optimization and pricing models, not agility. Agility is about speed and flexibility in resource deployment.

**B. AWS allows you to host your applications in multiple regions around the world** - Hosting applications in multiple regions is related to high availability, disaster recovery, and reducing latency for users in different geographic locations. While this is a benefit of AWS, it's not the primary definition of agility. This is more about global reach and resilience.

**D. AWS provides customizable hardware at the lowest possible cost** - AWS offers a wide variety of instance types with different hardware configurations, and it strives to provide cost-effective solutions. However, the key aspect of agility is not about customizable hardware or the lowest possible cost, but rather the speed and ease with which resources can be provisioned and scaled. While cost optimization is important, it's distinct from agility.

</details>

---

### Question 23 — `CLF-U0405` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following is a benefit of running an application in multiple Availability Zones?**

- A) Allows you to exceed AWS service limits.
- B) Reduces application response time between servers and global users.
- C) Increases available compute capacity.
- D) Increases the availability of your application.

<details>
<summary><strong>Reveal Answer & Explanation (Question 23)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Increases the availability of your application**

Running an application in multiple Availability Zones (AZs) is a key strategy for achieving high availability in AWS. Availability Zones are physically isolated locations within an AWS region. By deploying your application across multiple AZs, you ensure that if one AZ experiences an outage, your application can continue to run in the other AZs. This redundancy minimizes downtime and increases the overall availability of your application. This is a fundamental concept in cloud computing for fault tolerance and business continuity.

**Incorrect:**

**A. Allows you to exceed AWS service limits** - Running an application in multiple Availability Zones does not directly allow you to exceed AWS service limits. Service limits are account-wide and region-specific, and are not affected by the number of AZs you use. To exceed service limits, you need to request an increase from AWS support.

**C. Reduces application response time between servers and global users** - While deploying resources closer to users can reduce latency, running an application in multiple Availability Zones within a single region primarily improves availability, not necessarily response time for global users. To reduce latency for global users, you would typically use services like Amazon CloudFront (a CDN) or deploy your application in multiple AWS Regions.

**D. Increases available compute capacity** - Running an application in multiple Availability Zones does not inherently increase the total compute capacity available to you. It allows you to distribute your existing compute capacity across multiple isolated locations for redundancy. To increase compute capacity, you would need to provision more instances or use services like Auto Scaling.

</details>

---

### Question 24 — `CLF-U0406` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**How do ELBs improve the reliability of your application?**

- A) By distributing traffic across multiple S3 buckets.
- B) By replicating data to multiple availability zones.
- C) By creating database Read Replicas.
- D) By ensuring that only healthy targets receive traffic.

<details>
<summary><strong>Reveal Answer & Explanation (Question 24)</strong></summary>

**Correct Answer:** `D`

**Correct answer: By ensuring that only healthy targets receive traffic**

Elastic Load Balancers (ELBs) improve application reliability by continuously monitoring the health of registered targets (e.g., EC2 instances, containers, IP addresses). If a target fails a health check, the ELB automatically stops sending traffic to it and redirects traffic to healthy targets. This ensures that users experience minimal disruption and that the application remains available even if some components fail. This automated failover mechanism is a key aspect of high availability and fault tolerance.

**Incorrect:**

**A. By replicating data to multiple availability zones** - ELBs do not replicate data. Data replication is typically handled by other services like databases (e.g., RDS with Multi-AZ deployments) or object storage (e.g., S3 with its inherent redundancy). ELBs distribute traffic, not data.

**B. By creating database Read Replicas** - ELBs do not create or manage database read replicas. Read replicas are a database feature used to offload read traffic from the primary database, improving performance. While read replicas contribute to application availability, they are not directly managed or created by ELBs.

**D. By distributing traffic across multiple S3 buckets** - ELBs distribute traffic to compute resources like EC2 instances, containers, or IP addresses. They do not distribute traffic across S3 buckets. S3 is an object storage service, and traffic to S3 is typically direct, not routed through a load balancer.

</details>

---

### Question 25 — `CLF-U0410` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which statement best describes the concept of an AWS region?**

- A) An AWS Region is a geographical location with a collection of Edge locations.
- B) An AWS Region is a virtual network dedicated only to a single AWS customer.
- C) An AWS Region is a geographical location with a collection of Availability Zones.
- D) An AWS Region represents the country where the AWS infrastructure exist.

<details>
<summary><strong>Reveal Answer & Explanation (Question 25)</strong></summary>

**Correct Answer:** `C`

**Correct answer: An AWS Region is a geographical location with a collection of Availability Zones**

An AWS Region is a fundamental concept in AWS. It represents a distinct geographical location containing a collection of Availability Zones. Availability Zones are physically separate data centers within a Region, designed to be isolated from failures in other Availability Zones. This architecture provides high availability and fault tolerance for applications deployed in AWS. Regions allow you to deploy your applications closer to your users, reducing latency and improving performance. Each region is independent and isolated from other regions.

**Incorrect:**

**A. An AWS Region is a virtual network dedicated only to a single AWS customer** - An AWS Region is not a virtual network. While customers create Virtual Private Clouds (VPCs) within a Region to define their own isolated networks, the Region itself is a broader concept encompassing multiple physical data centers and shared infrastructure. Regions are multi-tenant environments.

**C. An AWS Region is a geographical location with a collection of Edge locations** - Edge locations are part of the AWS Content Delivery Network (CDN) service, CloudFront. They are geographically dispersed locations used to cache content closer to users, reducing latency. While Edge Locations are related to AWS infrastructure, they are distinct from and not contained within Regions. Regions contain Availability Zones.

**D. An AWS Region represents the country where the AWS infrastructure exist** - While a Region is a geographical area, it doesn't necessarily represent an entire country. Some countries may have multiple Regions, and some Regions might span multiple countries. The key aspect of a Region is its collection of Availability Zones within a specific geographic location.

</details>

---

### Question 26 — `CLF-U0414` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Why do many startup companies prefer AWS over traditional on-premises solutions? (Choose TWO)**

- A) AWS allows them to pay later when their business succeed.
- B) AWS can build complete data centers faster than any other Cloud provider.
- C) Using AWS, they can reduce time-to-market by focusing on business activities rather than on building and managing data centers.
- D) AWS removes the need to invest in operational expenditure.
- E) Using AWS allows companies to replace large capital expenditure with low variable costs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 26)</strong></summary>

**Correct Answer:** `C, E`

**Correct answer: Using AWS, they can reduce time-to-market by focusing on business activities rather than on building and managing data centers**

Startups often choose AWS because it allows them to focus on their core business and innovate quickly. By leveraging AWS's infrastructure, startups avoid the time-consuming and complex task of building and managing their own data centers. This reduction in operational overhead translates to a faster time-to-market for their products and services.

**Correct answer: Using AWS allows companies to replace large capital expenditure with low variable costs**

AWS's pay-as-you-go pricing model is a significant advantage for startups. Instead of investing heavily in hardware and infrastructure upfront (capital expenditure or CapEx), they can pay only for the resources they consume (operational expenditure or OpEx). This reduces the financial risk and allows startups to allocate their limited capital to other critical areas of their business.

**Incorrect:**

**A. AWS allows them to pay later when their business succeed** - AWS does not offer deferred payment plans contingent on business success. AWS operates on a pay-as-you-go model, where customers are billed for the resources they consume, regardless of their business outcomes.

**B. AWS removes the need to invest in operational expenditure** - AWS shifts the type of operational expenditure, but it doesn't eliminate it. While startups avoid the OpEx associated with managing physical data centers (e.g., power, cooling, physical security), they still incur OpEx related to AWS resource usage, data transfer, and other services.

**C. AWS can build complete data centers faster than any other Cloud provider** - While AWS has extensive infrastructure and can deploy resources rapidly, this option is not directly related to why startups *prefer* AWS. Startups benefit from the existing infrastructure and services, not AWS's ability to build data centers quickly. The speed of AWS's infrastructure build-out is more relevant to AWS's own operations than to the immediate benefits experienced by a startup.

</details>

---

### Question 27 — `CLF-U0417` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the below options is a best practice for making your application on AWS highly available?**

- A) Deploy the application to at least two Availability Zones.
- B) Use Elastic Load Balancing (ELB) across multiple AWS Regions.
- C) Deploy the application code on at least two servers in the same Availability Zone.
- D) Rewrite the application code to handle all incoming requests.

<details>
<summary><strong>Reveal Answer & Explanation (Question 27)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Deploy the application to at least two Availability Zones**

High availability in AWS means ensuring your application remains accessible even if one or more components fail. Availability Zones (AZs) are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones. By deploying your application across multiple AZs, you protect it from single points of failure, such as a power outage or network issue in one AZ. If one AZ becomes unavailable, the application can continue to run in the other AZs, maintaining availability. This is a core principle of building resilient and highly available applications in AWS.

**Incorrect:**

**A. Rewrite the application code to handle all incoming requests** - While robust application code is important, rewriting the code itself doesn't inherently make the application highly available. High availability is primarily achieved through infrastructure design and redundancy, not solely through code changes. Code improvements can enhance performance and stability, but they don't address the risk of infrastructure failures.

**B. Deploy the application code on at least two servers in the same Availability Zone** - Deploying multiple servers within the same Availability Zone increases capacity and can improve performance, but it does not provide high availability. If the entire Availability Zone experiences an outage, all servers within that AZ will be affected, and the application will become unavailable. High availability requires distributing resources across multiple, isolated AZs.

**C. Use Elastic Load Balancing (ELB) across multiple AWS Regions** - Using ELB across multiple AWS Regions is a strategy for disaster recovery and global availability, not simply high availability. While it contributes to overall resilience, it's more complex and typically used for scenarios where an entire region becomes unavailable. High availability within a region is primarily achieved by distributing resources across multiple Availability Zones, not Regions.

</details>

---

### Question 28 — `CLF-U0420` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following is true regarding the AWS availability zones and edge locations?**

- A) Edge locations are located in separate Availability Zones worldwide to serve global customers.
- B) An availability zone exists within an edge location to distribute content globally with low latency.
- C) An Availability Zone is a geographic location where AWS provides multiple, physically separated and isolated edge locations.
- D) An AWS Availability Zone is an isolated location within an AWS Region, however edge locations are located in multiple cities worldwide.

<details>
<summary><strong>Reveal Answer & Explanation (Question 28)</strong></summary>

**Correct Answer:** `D`

**Correct answer: An AWS Availability Zone is an isolated location within an AWS Region, however edge locations are located in multiple cities worldwide**

This statement accurately describes the relationship between Availability Zones and Edge Locations. An Availability Zone (AZ) is a physically isolated location within an AWS Region. Each Region contains multiple AZs. Edge locations, on the other hand, are CDN (Content Delivery Network) endpoints for services like CloudFront. They are strategically located in numerous cities globally to provide low-latency access to cached content for users worldwide. They are not tied to specific regions in the same way AZs are.

**Incorrect:**

**B. An Availability Zone is a geographic location where AWS provides multiple, physically separated and isolated edge locations** - This is incorrect because Availability Zones are isolated locations within a Region, not the other way around. Edge locations are not contained within Availability Zones.

**C. An availability zone exists within an edge location to distribute content globally with low latency** - This is incorrect. Edge locations are used to distribute content globally with low latency, and they are separate from Availability Zones. Availability Zones are for compute, storage, and database services.

**D. Edge locations are located in separate Availability Zones worldwide to serve global customers** - This is incorrect. Edge locations are globally distributed and independent of Availability Zones. They are used for caching and content delivery, while Availability Zones are for running applications and storing data within a specific AWS Region.

</details>

---

### Question 29 — `CLF-U0796` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**According to the AWS Shared responsibility model, which of the following are the responsibility of the customer? (Choose TWO)**

- A) Managing environmental events of AWS data centers.
- B) Protecting the confidentiality of data in transit in Amazon S3.
- C) Controlling physical access to AWS Regions.
- D) Ensuring that the underlying EC2 host is configured properly.
- E) Patching applications installed on Amazon EC2.

<details>
<summary><strong>Reveal Answer & Explanation (Question 29)</strong></summary>

**Correct Answer:** `B, E`

**Correct answer: Protecting the confidentiality of data in transit in Amazon S3**

According to the AWS Shared Responsibility Model, AWS is responsible for the security *of* the cloud, while the customer is responsible for security *in* the cloud. Protecting the confidentiality of data in transit, such as encrypting data before it is uploaded to Amazon S3 using services like AWS Key Management Service (KMS) or client-side encryption, falls under the customer's responsibility. AWS provides the tools and services, but the customer must configure and utilize them correctly to ensure data confidentiality.

**Correct answer: Patching applications installed on Amazon EC2**

Customers are responsible for managing the operating system, patching, and security of the applications they install on Amazon EC2 instances. AWS manages the underlying infrastructure, but the customer is responsible for everything within the EC2 instance itself, including application security.

**Incorrect:**

**A. Controlling physical access to AWS Regions** - AWS is responsible for the physical security of its data centers and Regions. This includes controlling physical access to the facilities.

**C. Managing environmental events of AWS data centers** - AWS is responsible for managing the environmental controls (e.g., power, cooling, and physical security) of its data centers. This is part of AWS's responsibility for the security *of* the cloud.

**D. Ensuring that the underlying EC2 host is configured properly** - AWS is responsible for the security and configuration of the underlying EC2 host. The customer is responsible for the guest operating system and applications installed on the EC2 instance.

</details>

---

### Question 30 — `CLF-U0817` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**When running a workload in AWS, the customer is NOT responsible for: (Select TWO)**

- A) Running penetration tests.
- B) Reserving capacity.
- C) Data center operations.
- D) Auditing and regulatory compliance.
- E) Infrastructure security.

<details>
<summary><strong>Reveal Answer & Explanation (Question 30)</strong></summary>

**Correct Answer:** `C, E`

**Correct answer: Data center operations**

AWS operates and manages the global infrastructure, including the physical data centers. This includes the physical security, power, networking, and hardware. Customers do not have direct access to or responsibility for the physical data centers. This is a core tenet of the AWS shared responsibility model.

**Correct answer: Infrastructure security**

AWS is responsible for the security *of* the cloud. This includes protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services. Customers are responsible for security *in* the cloud.

**Incorrect:**

**B. Auditing and regulatory compliance** - While AWS provides a secure infrastructure and services that can be used to meet compliance requirements, the customer is ultimately responsible for ensuring their applications and data meet all applicable auditing and regulatory compliance standards. This is part of the "security in the cloud" aspect of the shared responsibility model.

**C. Running penetration tests** - Customers are responsible for the security of their applications and data, which includes testing the security of their systems. AWS permits customers to conduct penetration tests on their own AWS resources, following AWS's penetration testing policy. Therefore, this is a customer responsibility.

**D. Reserving capacity** - Reserving capacity, such as through Reserved Instances or Savings Plans, is a customer responsibility. Customers choose the instance types, availability zones, and terms that best meet their needs and budget. AWS provides the tools and services to manage capacity, but the customer makes the decisions about what to reserve.

</details>

---

### Question 31 — `CLF-U0825` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**Which of the following factors should be considered when determining the region in which AWS Resources will be deployed? (Choose TWO)**

- A) The AWS Region’s security level.
- B) Data sovereignty.
- C) Cost.
- D) The planned number of VPCs.
- E) Geographic proximity to the company's location.

<details>
<summary><strong>Reveal Answer & Explanation (Question 31)</strong></summary>

**Correct Answer:** `B, C`

**Correct answer: Data sovereignty**

Data sovereignty refers to the concept that data is subject to the laws and governance structures within the geographic borders where the data is located. When choosing an AWS Region, companies must consider data sovereignty requirements to ensure compliance with local laws and regulations regarding data storage, processing, and transfer. Some countries have strict rules about where certain types of data (e.g., personal data, financial data) must reside. Selecting a region that aligns with these requirements is crucial for legal and regulatory compliance.

**Correct answer: Cost**

Cost is a significant factor when determining the AWS Region for deployment. AWS pricing can vary between regions due to factors such as local taxes, infrastructure costs, and demand. Evaluating the pricing differences for services like EC2, S3, and data transfer across different regions is essential for optimizing costs. Using the AWS Pricing Calculator can help compare costs across regions.

**Incorrect:**

**A. Geographic proximity to the company‘s location** - While geographic proximity can reduce latency and improve performance for users, it is not always the primary factor. Other factors like data sovereignty and cost may outweigh the benefits of proximity. Content Delivery Networks (CDNs) like Amazon CloudFront can also mitigate latency issues for globally distributed users, reducing the need to deploy resources in every region where users are located.

**B. The planned number of VPCs** - The number of VPCs (Virtual Private Clouds) a company plans to use does not directly influence the choice of AWS Region. AWS Regions can support multiple VPCs, and the number of VPCs is more related to network segmentation and organizational structure within AWS rather than a constraint imposed by the region itself. You can create and manage VPCs independently within any AWS Region.

**C. The AWS Region’s security level** - All AWS Regions adhere to the same high security standards and compliance certifications. AWS implements a shared responsibility model, where AWS is responsible for the security of the cloud, and the customer is responsible for security in the cloud. There is no inherent difference in the security level offered by different AWS Regions. Therefore, this is not a differentiating factor when choosing a region.

</details>

---

### Question 32 — `CLF-U0828` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.4: AWS Global Infrastructure*

**An external auditor is requesting a log of all accesses to the AWS resources in the company’s account. Which of the following services will provide the auditor with the requested information?**

- A) AWS CloudTrail.
- B) Amazon CloudFront.
- C) AWS CloudFormation.
- D) Amazon CloudWatch.

<details>
<summary><strong>Reveal Answer & Explanation (Question 32)</strong></summary>

**Correct Answer:** `A`

**Correct answer: AWS CloudTrail**

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail logs API calls made to AWS services, capturing information such as the identity of the caller, the time of the API call, the source IP address, the request parameters, and the response elements returned by the AWS service. This detailed log of activity is exactly what an external auditor would need to review access to AWS resources within the company's account.

**Incorrect:**

**A. AWS CloudFormation** - AWS CloudFormation is a service that allows you to model and provision AWS infrastructure as code. While it helps manage resources, it doesn't directly provide logs of access to those resources. It's used for infrastructure deployment and management, not auditing access.

**B. Amazon CloudFront** - Amazon CloudFront is a content delivery network (CDN) service. While CloudFront does generate access logs related to content requests served through the CDN, these logs are specific to CloudFront activity and do not provide a comprehensive log of all accesses to all AWS resources in the account. It's focused on content delivery, not general AWS resource access auditing.

**D. Amazon CloudWatch** - Amazon CloudWatch is a monitoring and observability service. It collects metrics and logs, and can be used to set alarms and visualize data. While CloudWatch can collect logs from various AWS services, it doesn't, by default, log all API calls made to AWS resources. CloudTrail is the service specifically designed for that purpose, and CloudWatch would typically be used to monitor the logs generated by CloudTrail, not replace it.

</details>

---

### Question 33 — `CLF-U0415` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 1.5: High Availability, Fault Tolerance & Disaster Recovery*

**A company is using EC2 Instances to run their e-commerce site on the AWS platform. If the site becomes unavailable, the company will lose a significant amount of money for each minute the site is unavailable. Which design principle should the company use to minimize the risk of an outage?**

- A) Least Privilege.
- B) Pilot Light.
- C) Fault Tolerance.
- D) Multi-threading.

<details>
<summary><strong>Reveal Answer & Explanation (Question 33)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Fault Tolerance**

Fault tolerance is the ability of a system to continue operating properly in the event of the failure of some of its components. In the context of an e-commerce site running on EC2 instances, implementing fault tolerance means designing the system to automatically recover from failures, such as an EC2 instance becoming unavailable. This can be achieved by using multiple EC2 instances behind a load balancer, so if one instance fails, the others can continue to serve traffic. Auto Scaling groups can also be used to automatically replace failed instances. This minimizes the risk of an outage and ensures high availability, which is crucial for a business that loses money for every minute of downtime.

**Incorrect:**

**B. Pilot Light** - Pilot Light is a disaster recovery strategy where a minimal version of the environment is always running in the cloud. While it can reduce recovery time compared to a full backup and restore, it doesn't provide the immediate failover needed to minimize downtime during an outage. It's more suited for disaster recovery scenarios than preventing outages in the first place.

**C. Multi-threading** - Multi-threading is a programming technique that allows a single process to execute multiple threads concurrently. While it can improve the performance of an application, it does not directly address the issue of system outages. If the EC2 instance running the multi-threaded application fails, the application will still be unavailable.

**D. Least Privilege** - Least Privilege is a security principle that grants users only the permissions they need to perform their job. While important for security, it does not directly contribute to minimizing the risk of outages. It focuses on limiting access to resources to prevent unauthorized actions, not on ensuring system availability.

</details>

---

### Question 34 — `CLF-U0004` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**What does AWS Snowball provide? (Choose TWO)**

- A) Built-in computing capabilities that allow customers to process data locally.
- B) A catalog of third-party software solutions that customers need to build solutions and run their businesses.
- C) A hybrid cloud storage between on-premises environments and the AWS Cloud.
- D) An Exabyte-scale data transfer service that allows you to move extremely large amounts of data to AWS.
- E) Secure transfer of large amounts of data into and out of the AWS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 34)</strong></summary>

**Correct Answer:** `A, E`

**Correct answer: Built-in computing capabilities that allow customers to process data locally**

AWS Snowball Edge devices provide on-board compute capabilities. This allows customers to perform local processing and analysis of data before transferring it to AWS. This is particularly useful in environments with limited or no network connectivity.

**Correct answer: Secure transfer of large amounts of data into and out of the AWS Cloud**

AWS Snowball is designed for securely transferring large datasets into and out of AWS. The data is encrypted, and the physical devices are ruggedized and tracked to ensure data security during transit.

**Incorrect:**

**A. A catalog of third-party software solutions that customers need to build solutions and run their businesses** - This describes the AWS Marketplace, not AWS Snowball. AWS Marketplace is where customers can find, buy, and deploy software that runs on AWS.

**B. A hybrid cloud storage between on-premises environments and the AWS Cloud** - While Snowball facilitates data transfer between on-premises and AWS, it is not a hybrid cloud storage solution. Hybrid cloud storage typically involves a more continuous and integrated storage environment. Services like AWS Storage Gateway are better suited for hybrid cloud storage.

**E. An Exabyte-scale data transfer service that allows you to move extremely large amounts of data to AWS** - While Snowball can handle large amounts of data, Snowball *Edge* is better suited for petabyte-scale transfers. AWS Snowmobile is the exabyte-scale data transfer service.

</details>

---

### Question 35 — `CLF-U0179` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**A company is running a large web application that needs to always be available. The application tends to slow down when CPU usage is greater than 60%. How can they track when CPU usage goes above 60% for any of the EC2 Instances in their account?**

- A) Use CloudFront to monitor the CPU usage.
- B) Set the AWS Config CPU threshold to 60% to receive a notification when EC2 usage exceeds that value.
- C) Use CloudWatch Alarms to monitor the CPU and alert when the CPU usage is >= 60%.
- D) Use SNS to monitor the utilization of the server.

<details>
<summary><strong>Reveal Answer & Explanation (Question 35)</strong></summary>

**Correct Answer:** `C`

Amazon CloudWatch Alarms let you define thresholds on metrics such as CPU utilization and trigger notifications or automated actions when the threshold is breached, making it the purpose-built solution for alerting when CPU usage exceeds 60%.
Amazon CloudFront is a content delivery network that caches and distributes content at edge locations worldwide to reduce latency for end users, and has no capability to monitor instance-level performance metrics such as CPU usage. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance and detect configuration changes, and does not monitor real-time performance metrics or support CPU threshold alerting. Amazon Simple Notification Service is a messaging service that delivers notifications to subscribers, and while it can be used alongside CloudWatch to deliver alerts, it cannot itself monitor or evaluate CPU utilization metrics.

</details>

---

### Question 36 — `CLF-U0383` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Adjusting compute capacity dynamically to reduce cost is an implementation of which AWS cloud best practice?**

- A) Build security in every layer.
- B) Parallelize tasks.
- C) Implement elasticity.
- D) Adopt monolithic architecture.

<details>
<summary><strong>Reveal Answer & Explanation (Question 36)</strong></summary>

**Correct Answer:** `C`

Elasticity is the cloud best practice of dynamically adjusting compute capacity up or down in response to demand, avoiding over-provisioning during low-traffic periods and under-provisioning during peaks, which directly reduces cost.
Build security in every layer is the Defense in Depth principle from the Security pillar of the Well-Architected Framework, which addresses threat protection rather than capacity management. Parallelizing tasks is a performance design principle that distributes workloads across multiple smaller components to increase throughput, not a mechanism for dynamically adjusting capacity to control costs. Adopting monolithic architecture consolidates all application components into a single tightly coupled unit, which is the opposite of a cloud best practice and does not support dynamic scaling.

</details>

---

### Question 37 — `CLF-U0384` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**What are the benefits of having infrastructure hosted in AWS? (Choose TWO)**

- A) Increasing speed and agility.
- B) There is no need to worry about security.
- C) Gaining complete control over the physical infrastructure.
- D) Operating applications on behalf of customers.
- E) All of the physical security and most of the data/network security are taken care of for you.

<details>
<summary><strong>Reveal Answer & Explanation (Question 37)</strong></summary>

**Correct Answer:** `A, E`

AWS increases speed and agility by allowing customers to provision resources in minutes rather than weeks, and handles physical security along with most data and network security so customers can focus on building applications rather than managing infrastructure.
Unlimited free storage is not an AWS benefit, as storage services such as Amazon S3 and EBS are billed based on the amount of data stored and retrieved. Complete control over physical infrastructure is not available to AWS customers, as AWS owns and manages all physical hardware, data centers, and networking equipment on the customer's behalf. Operating applications on behalf of customers is not an AWS benefit, as customers remain responsible for building, deploying, and managing their own applications under the shared responsibility model.

</details>

---

### Question 38 — `CLF-U0386` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**One of the most important AWS best-practices to follow is the cloud architecture principle of elasticity. How does this principle improve your architecture’s design?**

- A) By automatically scaling your on-premises resources based on changes in demand.
- B) By automatically scaling your AWS resources using an Elastic Load Balancer.
- C) By reducing interdependencies between application components wherever possible.
- D) By automatically provisioning the required AWS resources based on changes in demand.

<details>
<summary><strong>Reveal Answer & Explanation (Question 38)</strong></summary>

**Correct Answer:** `D`

Elasticity in AWS means the platform automatically provisions and de-provisions resources in response to real-time changes in demand, so workloads consume only what they need and scale back when demand drops.
Automatically scaling on-premises resources is not what elasticity describes in the AWS context; elasticity is a cloud characteristic that removes the need to invest in on-premises hardware at all, as the cloud provider dynamically adjusts compute capacity. An Elastic Load Balancer distributes incoming traffic across existing instances to prevent any single instance from being overwhelmed, but it does not add or remove instances in response to demand; that capacity adjustment is performed by Auto Scaling. Reducing interdependencies between application components describes the design principle of loose coupling, which improves resilience and maintainability, but is a separate architectural concept from elasticity.

</details>

---

### Question 39 — `CLF-U0421` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which of the following are advantages of using AWS as a cloud computing provider? (Choose TWO)**

- A) Eliminates the need to monitor servers and applications.
- B) Manages all the compliance and auditing tasks.
- C) Provides custom hardware to meet any specification.
- D) Eliminates the need to guess on infrastructure capacity needs.
- E) Enables customers to trade their capital expenses for operational expenses.

<details>
<summary><strong>Reveal Answer & Explanation (Question 39)</strong></summary>

**Correct Answer:** `D, E`

AWS eliminates the need to guess infrastructure capacity through on-demand scaling, and enables customers to trade large upfront capital expenses for smaller variable operational expenses based on actual usage.
Customers remain responsible for monitoring their own servers and applications, as AWS provides the tools but does not perform monitoring on the customer's behalf. Compliance and auditing responsibilities are shared, with customers accountable for their own data, access controls, and application-level compliance regardless of using AWS. AWS does not provide custom hardware to individual customer specifications, as customers select from standardized instance types and managed services within the shared infrastructure.

</details>

---

### Question 40 — `CLF-U0424` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**What does the term “Economies of scale” mean?**

- A) It means that you save more when you consume more.
- B) It means as more time passes using AWS, you pay more for its services.
- C) It means that AWS will continuously lower costs as it grows.
- D) It means that you have the ability to pay as you go.

<details>
<summary><strong>Reveal Answer & Explanation (Question 40)</strong></summary>

**Correct Answer:** `C`

Economies of scale means that as AWS grows and aggregates more customer usage, it achieves lower per-unit costs and continuously passes those savings on to customers through regular price reductions.
Saving more when you consume more describes volume-based discounts such as Reserved Instances or tiered pricing, which is a separate pricing concept rather than the definition of economies of scale. Paying more over time as usage increases describes the opposite of what economies of scale delivers, as AWS prices have consistently decreased over time rather than increased. The ability to pay as you go describes the pay-as-you-go billing model, which is a separate cloud adoption benefit unrelated to the cost reductions driven by aggregated purchasing power.

</details>

---

### Question 41 — `CLF-U0425` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which statement best describes the AWS Pay-As-You-Go pricing model?**

- A) With AWS, you replace low upfront expenses with large variable payments.
- B) With AWS, you replace low upfront expenses with large fixed payments.
- C) With AWS, you replace large upfront expenses with low fixed payments.
- D) With AWS, you replace large capital expenses with low variable payments.

<details>
<summary><strong>Reveal Answer & Explanation (Question 41)</strong></summary>

**Correct Answer:** `D`

The Pay-As-You-Go model replaces large upfront capital expenses with low variable payments based on actual consumption, so you only pay for the resources you use.
Replacing low upfront expenses with large variable payments inverts the AWS pricing model, which specifically eliminates large upfront capital costs rather than introducing new large variable costs. Replacing low upfront expenses with large fixed payments describes neither the on-premises nor the AWS model accurately. On-premises typically has large upfront expenses, and AWS replaces those with low variable costs rather than fixed ones. Replacing large upfront expenses with low fixed payments partially captures the idea of reducing upfront costs, but AWS pricing is variable rather than fixed, scaling directly with actual resource consumption.

</details>

---

### Question 42 — `CLF-U0444` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which AWS characteristics make AWS cost effective for a workload with dynamic user demand? (Select TWO)**

- A) High availability.
- B) Shared security model.
- C) Elasticity.
- D) Pay-as-you-go pricing.
- E) Reliability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 42)</strong></summary>

**Correct Answer:** `C, D`

Elasticity lets you automatically scale resources up or down with demand, and pay-as-you-go pricing ensures you only pay for what you actually use, making both ideal for workloads with unpredictable, dynamic demand.
High availability ensures that applications remain accessible despite failures by using redundancy across multiple Availability Zones, and while it contributes to reliability it does not directly reduce costs for workloads with dynamic demand. The shared security model defines the division of security responsibilities between AWS and the customer, and is a governance principle rather than a characteristic that makes AWS cost effective for variable workloads. Reliability refers to the ability of a workload to perform its intended function correctly and consistently, and while important for system design it is not itself a pricing or cost efficiency characteristic that reduces costs for dynamic demand.

</details>

---

### Question 43 — `CLF-U0466` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**How can a company reduce its Total Cost of Ownership (TCO) using AWS?**

- A) By minimizing large capital expenditures.
- B) By having no responsibility for third-party license costs.
- C) By having no operational expenditures.
- D) By having AWS manage applications.

<details>
<summary><strong>Reveal Answer & Explanation (Question 43)</strong></summary>

**Correct Answer:** `A`

AWS shifts infrastructure spending from large upfront capital expenditures to smaller, ongoing operational expenses, directly reducing TCO by eliminating the need to over-provision for peak demand.
Having no responsibility for third-party license costs is not a general AWS benefit, as customers still manage and pay for their own software licenses when running applications on AWS, unless they use AWS-provided licenses through services such as Amazon RDS. AWS does not eliminate operational expenditures. Customers continue to pay ongoing usage-based costs for the AWS services they consume, which are operational expenses rather than capital expenses. AWS does not manage customer applications by default. Application-level management including code, configuration, and updates remains the customer's responsibility under the shared responsibility model.

</details>

---

### Question 44 — `CLF-U0471` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**A company will be moving from an on-premises data center to the AWS Cloud. What would be one financial difference after the move?**

- A) Moving from variable operational expense ( opex ) to upfront capital expense (capex).
- B) Moving from upfront capital expense (capex) to variable capital expense (capex).
- C) Moving from upfront capital expense (capex) to variable operational expense ( opex ).
- D) Elimination of upfront capital expense (capex) and elimination of variable operational expense ( opex ).

<details>
<summary><strong>Reveal Answer & Explanation (Question 44)</strong></summary>

**Correct Answer:** `C`

On-premises infrastructure requires large upfront capital expenditures for hardware and facilities, while AWS converts that spending to variable operational expense where you pay only for what you consume with no hardware purchases required.
Moving from variable operational expense (opex) to upfront capital expense (capex) this reverses the actual direction of the shift, and on-premises environments are characterized by capex, not opex, as the starting point. Moving from upfront capital expense (capex) to variable capital expense (capex) AWS usage is billed as operational expense, not capital expense, so the destination category in this option is incorrect. Elimination of upfront capital expense (capex) and elimination of variable operational expense (opex) moving to AWS eliminates capex but introduces opex rather than eliminating it, as ongoing usage costs are paid as operational expense.

</details>

---

### Question 45 — `CLF-U0480` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**A solution that is able to support growth in users, traffic, or data size with no drop in performance aligns with which cloud architecture principle?**

- A) Think parallel.
- B) Implement elasticity.
- C) Decouple your components.
- D) Design for failure.

<details>
<summary><strong>Reveal Answer & Explanation (Question 45)</strong></summary>

**Correct Answer:** `B`

Elasticity is the ability to scale resources up or down automatically to handle increases in users, traffic, or data size without any degradation in performance, making it the principle that directly addresses growth support.
Think parallel refers to the principle of designing systems to handle tasks simultaneously across multiple resources to improve throughput and speed, not specifically to handle growth in users or data size without performance loss. Decouple your components refers to reducing dependencies between application components so failures do not cascade, which improves resilience rather than addressing performance under growth. Design for failure refers to building systems that anticipate and recover from component failures automatically, which addresses resilience and availability rather than scaling to support growth.

</details>

---

### Question 46 — `CLF-U0481` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which AWS Cloud benefit eliminates the need for users to try estimating future infrastructure usage?**

- A) Easy and fast deployment of applications in multiple Regions around the world.
- B) Security of the AWS Cloud.
- C) Elasticity of the AWS Cloud.
- D) Lower variable costs due to massive economies of scale.

<details>
<summary><strong>Reveal Answer & Explanation (Question 46)</strong></summary>

**Correct Answer:** `C`

Cloud elasticity allows resources to scale up or down on demand, eliminating the need to predict and provision for peak future capacity in advance.
Easy and fast deployment of applications in multiple Regions is a benefit of AWS's global infrastructure, enabling speed and reach, but does not remove the need to estimate future infrastructure usage. Security of the AWS Cloud refers to the protections AWS provides for its infrastructure under the shared responsibility model, which is unrelated to capacity planning or infrastructure estimation. Lower variable costs due to massive economies of scale means AWS can offer reduced pricing as its customer base grows, but lower costs do not eliminate the underlying need to estimate how much infrastructure will be required.

</details>

---

### Question 47 — `CLF-U0485` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**What is an example of agility in the AWS Cloud?**

- A) Access to multiple instance types.
- B) Access to managed services.
- C) Using Consolidated Billing to produce one bill.
- D) Decreased acquisition time for new compute resources.

<details>
<summary><strong>Reveal Answer & Explanation (Question 47)</strong></summary>

**Correct Answer:** `D`

Agility in the AWS Cloud is best illustrated by the dramatically reduced time to acquire and provision new compute resources, from weeks on-premises to minutes in the cloud, enabling teams to experiment and iterate faster.
Access to multiple instance types is a flexibility benefit that allows customers to match compute to workload requirements, but does not directly describe the speed of acquiring new resources. Access to managed services reduces operational overhead by offloading infrastructure management to AWS, but is an example of reduced complexity rather than agility. Consolidated Billing is a cost management feature that combines charges from multiple accounts into a single bill, which is a billing convenience and unrelated to the speed of resource acquisition.

</details>

---

### Question 48 — `CLF-U0599` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which of the following should be taken into account when performing a TCO analysis regarding the costs of running an application on AWS VS on-premises? (Choose TWO)**

- A) Labor and IT costs.
- B) Cooling and power consumption.
- C) Amazon EBS computing power.
- D) Software architecture.
- E) Software compatibility.

<details>
<summary><strong>Reveal Answer & Explanation (Question 48)</strong></summary>

**Correct Answer:** `A, B`

A TCO analysis compares on-premises costs including labor, IT staff, cooling, and power consumption against AWS costs, where these physical infrastructure expenses are eliminated.
Amazon EBS computing power is an AWS service cost rather than an on-premises infrastructure expense, so it does not belong in a TCO comparison of what customers stop paying for when they migrate. Software architecture refers to how an application is designed and structured, which is a technical consideration rather than an infrastructure cost factored into a TCO analysis. Software compatibility refers to whether applications can run in a new environment, which is a migration planning concern rather than a cost category included in a TCO comparison.

</details>

---

### Question 49 — `CLF-U0633` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**The financial benefits of using AWS are: (Select TWO)**

- A) Reduced Total Cost of Ownership (TCO).
- B) Increased capital expenditure (capex).
- C) Reduced operational expenditure ( opex ).
- D) Deferred payment plans for startups.
- E) Business credit lines for startups.

<details>
<summary><strong>Reveal Answer & Explanation (Question 49)</strong></summary>

**Correct Answer:** `A, C`

AWS reduces Total Cost of Ownership by eliminating data center capital expenses, and reduces operational expenditure through pay-as-you-go pricing and managed services that lower staffing and maintenance costs.
Increased capital expenditure describes the opposite of an AWS financial benefit. Moving to AWS replaces large upfront hardware investments with variable operational costs, reducing rather than increasing capital expenditure. Deferred payment plans for startups is not a standard AWS financial benefit. AWS charges are billed monthly based on actual usage, and there are no deferred payment arrangements offered as a general benefit to startup customers. Business credit lines for startups are not provided by AWS as a standard financial benefit. AWS does have programs such as AWS Activate that provide credits to startups, but these are promotional credits rather than credit lines or financing arrangements.

</details>

---

### Question 50 — `CLF-U0802` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which of the following services will help businesses ensure compliance in AWS?**

- A) CloudFront.
- B) CloudEndure Migration.
- C) CloudWatch.
- D) CloudTrail.

<details>
<summary><strong>Reveal Answer & Explanation (Question 50)</strong></summary>

**Correct Answer:** `D`

AWS CloudTrail logs all API activity and account events, creating a complete audit trail that helps organizations demonstrate compliance with regulatory requirements and investigate security incidents.
Amazon CloudFront is a global content delivery network that caches and distributes web content to users at low latency through edge locations, and is a performance and distribution service with no capability to record audit logs or help with regulatory compliance. AWS Migration Hub provides a central dashboard for tracking the progress of application migrations to AWS, and is a migration management tool rather than a compliance or audit service. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, providing visibility into performance and operational health, but it does not create the comprehensive API audit trail needed for regulatory compliance.

</details>

---

### Question 51 — `CLF-U1445` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.1: Cloud Economics & Benefits*

**Which AWS Cloud benefit is shown by an architecture’s ability to withstand failures with minimal downtime?**

- A) Agility
- B) Elasticity
- C) Scalability
- D) High availability

<details>
<summary><strong>Reveal Answer & Explanation (Question 51)</strong></summary>

**Correct Answer:** `D`

Understanding High Availability: High availability (HA) refers to systems that are durable
and likely to operate continuously without failure for a long time. HA ensures that an
architecture can withstand failures with minimal downtime.
Importance of High Availability:
Redundancy: Systems are designed with redundancy to prevent single points of failure.
Fault Tolerance: Ensures that failures do not result in significant downtime, maintaining
service continuity.
Automated Recovery: Utilizes automated recovery mechanisms to quickly restore services
in the event of a failure.
AWS Services for High Availability:
Multi-AZ Deployments: Services like RDS, DynamoDB, and others support Multi-AZ
deployments for fault tolerance.
Elastic Load Balancing: Distributes traffic across multiple instances or availability zones to
ensure no single point of failure.
Auto Scaling: Automatically adjusts the number of instances based on demand, ensuring
availability even during traffic spikes.
AWS Well-Archit

</details>

---

### Question 52 — `CLF-U1465` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**Which option is a perspective that includes foundational capabilities of the AWS Cloud Adoption Framework (AWS CAF)?**

- A) Sustainability
- B) Security
- C) Performance efficiency
- D) Reliability

<details>
<summary><strong>Reveal Answer & Explanation (Question 52)</strong></summary>

**Correct Answer:** `B`

Operations is an option that is a perspective that includes foundational capabilities of the
AWS Cloud Adoption Framework (AWS CAF). Operations is one of the six perspectives of
the AWS CAF, along with business, people, governance, platform, and security.
Operations focuses on the processes and procedures to support the ongoing management
and maintenance of the cloud-based IT assets. It covers topics such as monitoring, backup
and recovery, change management, incident management, and automation5.
Sustainability is not a perspective of the AWS CAF, but a concept that refers to the ability
of a system to operate in an environmentally friendly and socially responsible manner.
Performance efficiency is not a perspective of the AWS CAF, but a pillar of the AWS WellArchitected Framework. It focuses on using the right resources and services for the
workload, monitoring performance, and continuously improving the efficiency of the
solution. Reliability is not a perspective of the AWS CAF, but

</details>

---

### Question 53 — `CLF-U0207` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which of the following is a cloud architectural design principle?**

- A) Scale up not out.
- B) Loosely couple components.
- C) Build monolithic systems.
- D) Use commercial database software.

<details>
<summary><strong>Reveal Answer & Explanation (Question 53)</strong></summary>

**Correct Answer:** `B`

Loosely coupling components means designing them to interact through well-defined interfaces such as queues or APIs, so that changes or failures in one component do not directly impact others.
Scaling up not out describes vertical scaling, which is an on-premises approach that cloud best practices discourage in favor of horizontal scaling through adding more instances. Building monolithic systems consolidates all application components into a single tightly coupled unit, which is the opposite of the cloud design principle of breaking applications into loosely coupled, independently deployable components. Using commercial database software is a technology procurement decision rather than an architectural design principle, and cloud best practices favor managed and purpose-built database services over proprietary commercial software where appropriate.

</details>

---

### Question 54 — `CLF-U0439` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which pillar of the AWS Well-Architected Framework provides recommendations to help customers select the right compute resources based on workload requirements?**

- A) Operational Excellence.
- B) Security.
- C) Performance Efficiency.
- D) Reliability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 54)</strong></summary>

**Correct Answer:** `C`

The Performance Efficiency pillar of the Well-Architected Framework focuses on selecting the right resource types and sizes based on workload requirements to use computing resources efficiently.
Operational Excellence focuses on running and monitoring systems to deliver business value and continually improving processes and procedures, and does not specifically address compute resource selection based on workload requirements. Security focuses on protecting information and systems through risk assessment, access management, and controls, and is not concerned with matching compute resources to workload performance needs. Reliability focuses on ensuring a workload can recover from failures and dynamically acquire resources to meet demand, but its emphasis is on resilience and recovery rather than on selecting the right compute resource types for efficiency.

</details>

---

### Question 55 — `CLF-U0445` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**An administrator needs to rapidly deploy a popular IT solution and start using it immediately. Where can the administrator find assistance?**

- A) AWS Well-Architected Framework documentation.
- B) Amazon CloudFront.
- C) AWS CodeCommit.
- D) AWS Quick Start reference deployments.

<details>
<summary><strong>Reveal Answer & Explanation (Question 55)</strong></summary>

**Correct Answer:** `D`

AWS Quick Start reference deployments provide automated gold-standard templates that deploy popular IT solutions on AWS in minutes, giving administrators a fast path to production-ready environments built on AWS best practices.
AWS Well-Architected Framework documentation provides architectural guidance and best practices for designing cloud workloads across six pillars, but is a reference document rather than a deployment tool that can provision a solution immediately. Amazon CloudFront is a content delivery network that caches and distributes content to users at edge locations worldwide, and has no capability to deploy or provision IT solutions. AWS CodeCommit is a managed Git-based source control service for storing and versioning code repositories, and is a developer tool with no rapid deployment or solution provisioning capability.

</details>

---

### Question 56 — `CLF-U0449` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which design principles for cloud architecture are recommended when re-architecting a large monolithic application? (Select TWO)**

- A) Use manual monitoring.
- B) Use fixed servers.
- C) Implement loose coupling.
- D) Rely on individual components.
- E) Design for scalability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 56)</strong></summary>

**Correct Answer:** `C, E`

Loose coupling reduces inter-component dependencies so that a failure in one part of the application does not cascade to others, and designing for scalability ensures each component can independently handle varying loads, both being essential principles when breaking apart a monolithic architecture.
Manual monitoring relies on human observation rather than automated alerting and is an anti-pattern in cloud architecture. Fixed servers contradict the cloud principle of elasticity and scalability, locking capacity to a predetermined amount regardless of demand. Relying on individual components is the defining characteristic of a monolithic architecture and is the problem being solved, not a recommended design principle.

</details>

---

### Question 57 — `CLF-U0459` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which of the following is an important architectural design principle when designing cloud applications?**

- A) Use multiple Availability Zones.
- B) Use tightly coupled components.
- C) Use open source software.
- D) Provision extra capacity.

<details>
<summary><strong>Reveal Answer & Explanation (Question 57)</strong></summary>

**Correct Answer:** `A`

Using multiple Availability Zones ensures high availability by distributing your application across physically isolated data centers, so that a failure in any single zone does not take the entire application offline.
Using tightly coupled components is an anti-pattern in cloud architecture, as tight dependencies between components mean a failure in one can cascade and bring down others. Using open source software is a development and licensing choice that has no bearing on cloud architectural design principles for availability or resilience. Provisioning extra capacity contradicts the cloud principle of elasticity, which favors scaling dynamically based on actual demand rather than guessing and over-provisioning upfront.

</details>

---

### Question 58 — `CLF-U0470` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which of the following is an AWS Cloud architecture design principle?**

- A) Implement single points of failure.
- B) Implement loose coupling.
- C) Implement monolithic design.
- D) Implement vertical scaling.

<details>
<summary><strong>Reveal Answer & Explanation (Question 58)</strong></summary>

**Correct Answer:** `B`

Loose coupling is a core AWS cloud architecture principle where components interact through well-defined interfaces, allowing each to scale, update, or fail independently without cascading effects on other parts of the system.
Implementing single points of failure is an anti-pattern that directly contradicts cloud architecture best practices, as the goal is to eliminate dependencies that could bring down an entire system. Monolithic design tightly couples all application components into a single unit, making it harder to scale, update, or recover individual parts independently. Vertical scaling increases the capacity of a single instance rather than distributing workloads, which limits scalability and creates potential single points of failure.

</details>

---

### Question 59 — `CLF-U1305` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which pillar of the AWS Well-Architected Framework focuses on running workloads effectively, gaining operational insights, and continuously improving processes?**

- A) Security
- B) Reliability
- C) Performance Efficiency
- D) Operational Excellence

<details>
<summary><strong>Reveal Answer & Explanation (Question 59)</strong></summary>

**Correct Answer:** `B`

The Reliability pillar focuses on the ability of a workload to perform its intended function correctly and consistently, including the ability to recover from failures and meet availability requirements over time.
Security focuses on protecting data, systems, and assets through access controls, encryption, and detective mechanisms. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes. Operational Excellence focuses on running and monitoring systems to deliver business value and continuously improving processes and procedures.

</details>

---

### Question 60 — `CLF-U1309` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**Which pillar of the AWS Well-Architected Framework focuses on the ability to run workloads effectively, gain insight into operations, and continuously improve supporting processes and procedures?**

- A) Operational Excellence
- B) Reliability
- C) Security
- D) Performance Efficiency

<details>
<summary><strong>Reveal Answer & Explanation (Question 60)</strong></summary>

**Correct Answer:** `C`

The Security pillar focuses on protecting data, systems, and assets through risk assessments, mitigation strategies, and controls covering confidentiality, integrity, and identity management.
Operational Excellence focuses on running workloads effectively, monitoring operations, and continuously improving processes and procedures. Reliability focuses on ensuring a workload performs its intended function correctly and recovers automatically from failures. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes over time.

</details>

---

### Question 61 — `CLF-U2529` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.3: AWS Well-Architected Framework*

**A company wants to protect its AWS Cloud information, systems, and assets while performing risk assessment and mitigation tasks. Which pillar of the AWS Well-Architected Framework is supported by these goals?**

- A) Reliability
- B) Security
- C) Operational excellence
- D) Performance efficiency

<details>
<summary><strong>Reveal Answer & Explanation (Question 61)</strong></summary>

**Correct Answer:** `B`

**Correct Answer: B (Security)**

This question (# 194) is directly sourced from authentic **Community Consensus Pool** community discussions.
**Why this is correct:** The scenario specifically tests AWS best practices. 'Security' directly satisfies the architectural requirement defined in the prompt.

**Key Option Breakdown:**
- **Option A (Reliability)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option B (Security)** [CORRECT]: Satisfies the prompt requirements directly.
- **Option C (Operational excellence)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option D (Performance efficiency)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.

</details>

---

### Question 62 — `CLF-U0249` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.5: High Availability, Fault Tolerance & Disaster Recovery*

**Which disaster recovery scenario offers the lowest probability of down time?**

- A) Backup and restore.
- B) Pilot light.
- C) Warm standby.
- D) Multi-site active-active.

<details>
<summary><strong>Reveal Answer & Explanation (Question 62)</strong></summary>

**Correct Answer:** `D`

Multi-site active-active runs fully redundant live copies of your application across multiple sites simultaneously, so if one site fails the other immediately serves all traffic with essentially zero downtime.
Backup and restore has the highest recovery time of all DR strategies. Data is restored from backups after a failure, meaning significant downtime is expected. Pilot light keeps a minimal version of the environment running and scales up during a disaster, resulting in a short but non-zero recovery time. Warm standby runs a scaled-down but fully functional version of the environment, which requires scaling up before handling full traffic load.

</details>

---

### Question 63 — `CLF-U0477` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.5: High Availability, Fault Tolerance & Disaster Recovery*

**Which feature of the AWS Cloud will support an international company’s requirement for low latency to all of its customers?**

- A) Fault tolerance.
- B) Global reach.
- C) Pay-as-you-go pricing.
- D) High availability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 63)</strong></summary>

**Correct Answer:** `B`

AWS's global reach, with Regions and edge locations spread worldwide, allows companies to deploy resources close to their international customers, directly reducing network latency.
Fault tolerance refers to a system's ability to continue operating despite component failures, not to reducing geographic latency. Pay-as-you-go pricing is a billing model and has no effect on network latency or geographic reach. High availability ensures systems remain operational with minimal downtime, but does not address the physical proximity needed to reduce latency for international customers.

</details>

---

### Question 64 — `CLF-U0478` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 1.5: High Availability, Fault Tolerance & Disaster Recovery*

**What are the benefits of developing and running a new application in the AWS Cloud compared to on-premises? (Select TWO)**

- A) AWS automatically distributes the data globally for higher durability.
- B) AWS will take care of operating the application.
- C) AWS makes it easy to architect for high availability.
- D) AWS can easily accommodate application demand changes.
- E) AWS takes care of application security patching.

<details>
<summary><strong>Reveal Answer & Explanation (Question 64)</strong></summary>

**Correct Answer:** `C, D`

AWS makes it easy to architect for high availability using multi-AZ deployments, load balancers, and managed services, and the cloud's elasticity allows applications to scale up or down to match demand changes quickly.
AWS does not automatically distribute all data globally by default, as data residency and replication are configuration choices the customer makes depending on the services and settings they select. AWS does not take care of operating the application, as customers remain responsible for deploying, managing, and maintaining their own application code and runtime environments. AWS does not take care of application security patching, as patching the application layer is the customer's responsibility under the Shared Responsibility Model.

</details>

---

### Question 65 — `ACTUAL-393-Q041` | 🔁 Repeated in 2 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**A company is planning to migrate a monolithic application to AWS. The company wants to modernize the application by splitting it into microservices. The company will deploy the microservices on AWS. Which migration strategy should the company use?**

- A) Rehost
- B) Repurchase
- C) Replatform
- D) Refactor

<details>
<summary><strong>Reveal Answer & Explanation (Question 65)</strong></summary>

**Correct Answer:** `D`

Refactoring involves re-architecting and modifying an application to take advantage of
cloud-native features. In this case, the company wants to modernize a monolithic
application by breaking it into microservices. This process aligns with the Refactor
strategy, which is aimed at modernizing and re-architecting applications. Rehost,
Repurchase, and Replatform do not involve the level of re-architecting needed to move
from a monolithic to a microservices architecture.

</details>

---

### Question 66 — `ACTUAL-393-Q053` | 🔁 Repeated in 2 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**Which options are perspectives that include foundational capabilities of the AWS Cloud Adoption Framework (AWS CAF)? (Select TWO.)**

- A) Sustainability
- B) Security
- C) Operations
- D) Performance efficiency
- E) Reliability

<details>
<summary><strong>Reveal Answer & Explanation (Question 66)</strong></summary>

**Correct Answer:** `CD`

The options that are perspectives that include foundational capabilities of the AWS Cloud
Adoption Framework (AWS CAF) are operations and performance efficiency. The AWS
CAF is a guidance that helps organizations design and travel an accelerated path to
successful cloud adoption. The AWS CAF organizes the cloud adoption process into six
areas of focus, called perspectives, which are business, people, governance, platform,
security, and operations. Each perspective is divided into capabilities, which are further
divided into skills and responsibilities. The operations perspective focuses on the
management and monitoring of the cloud resources and applications, as well as the
automation and optimization of the operational processes. The operations perspective
capabilities are operations support, operations integration, and service management. The
performance efficiency perspective focuses on the selection and configuration of the right
cloud resources and services to meet the performance

</details>

---

### Question 67 — `ACTUAL-393-Q392` | 🔁 Repeated in 2 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**Which perspective in the AWS Cloud Adoption Framework (AWS CAF) includes a capability for well-designed data and analytics architecture?**

- A) Security
- B) Governance
- C) Operations
- D) Platform

<details>
<summary><strong>Reveal Answer & Explanation (Question 67)</strong></summary>

**Correct Answer:** `C`

The correct answer is D. Platform.
The Platform perspective in the AWS Cloud Adoption Framework (AWS CAF) includes a
capability for well-designed data and analytics architecture. This capability helps you
design, implement, and optimize your data and analytics solutions on AWS, using services
such as Amazon S3, Amazon Redshift, Amazon EMR, Amazon Kinesis, Amazon Athena,
and Amazon QuickSight.A well-designed data and analytics architecture enables you to
collect, store, process, analyze, and visualize data from various sources, and derive
insights that can drive your business decisions12.
The Security perspective does not include a capability for data and analytics architecture,
but it does include a capability for data protection, which helps you secure your data at rest
and in transit using encryption, key management, access control, and auditing13.
The Governance perspective does not include a capability for data and analytics
architecture, but it does include a capability for data g

</details>

---

### Question 68 — `CLF-U1324` | 🔁 Repeated in 2 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**Which AWS Cloud Adoption Framework (AWS CAF) perspective focuses on designing and implementing new cloud environments with enterprise-grade scalability?**

- A) Operations
- B) Security
- C) Platform
- D) People

<details>
<summary><strong>Reveal Answer & Explanation (Question 68)</strong></summary>

**Correct Answer:** `C`

The Platform perspective focuses on building an enterprise-grade, scalable cloud platform by designing the target architecture for networking, compute, storage, and database services, and establishing patterns for provisioning and managing cloud resources.
The Operations perspective focuses on delivering and managing cloud services to meet day-to-day business needs through monitoring, incident management, and process improvement, not on designing the underlying platform architecture. The Security perspective focuses on protecting data and workloads through identity management, threat detection, and security controls, rather than designing the cloud infrastructure platform. The People perspective focuses on workforce readiness, organizational change, and skills development, which is unrelated to technical platform architecture.

</details>

---

### Question 69 — `CLF-U1335` | 🔁 Repeated in 2 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**A company wants to move its on-premises application to AWS as quickly as possible with minimal changes to the existing code. Which migration strategy does this describe?**

- A) Replatform
- B) Refactor
- C) Rehost
- D) Repurchase

<details>
<summary><strong>Reveal Answer & Explanation (Question 69)</strong></summary>

**Correct Answer:** `C`

Rehosting, also known as lift and shift, involves moving an application to the cloud without making any changes to the application code or architecture, making it the fastest migration strategy for getting workloads into AWS.
Replatforming involves making targeted optimizations during migration, such as moving a database to a managed service like Amazon RDS, which requires some changes beyond a simple lift and shift. Refactoring involves redesigning the application to take advantage of cloud-native features such as serverless computing or microservices, which requires significant development effort and is not a minimal-change approach. Repurchasing involves replacing the existing application with a different product, typically a SaaS solution, which is not a strategy for moving existing code to AWS.

</details>

---

### Question 70 — `CLF-U1437` | 🔁 Repeated in 2 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**Which options are AWS Cloud Adoption Framework (AWS CAF) cloud transformation journey recommendations? (Select TWO.)**

- A) Envision phase
- B) AIign phase
- C) Assess phase
- D) Mobilize phase
- E) Migrate and modernize phase

<details>
<summary><strong>Reveal Answer & Explanation (Question 70)</strong></summary>

**Correct Answer:** `AB`

The AWS Cloud Adoption Framework (AWS CAF) cloud transformation journey is a fourphase process that helps customers plan and execute their cloud migration and digital
transformation. The four phases are:
Envision phase: This phase focuses on demonstrating how cloud will help accelerate the
business outcomes of the customer. It involves identifying and prioritizing transformation
opportunities across four domains: business, people, governance, and platform. It also
involves associating the transformation initiatives with key stakeholders and measurable
business outcomes1.
Align phase: This phase focuses on identifying capability gaps across six perspectives:
business, people, governance, platform, security, and operations. It also involves
identifying cross-organizational dependencies and surfacing stakeholder concerns and
challenges. The goal of this phase is to create strategies for improving the cloud readiness,
ensure stakeholder alignment, and facilitate relevant organizational cha

</details>

---

### Question 71 — `CLF-U1311` | 🔁 Repeated in 1 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**Which TWO of the following are perspectives of the AWS Cloud Adoption Framework (AWS CAF)?**

- A) Governance
- B) Financial
- C) People
- D) Infrastructure
- E) Agility

<details>
<summary><strong>Reveal Answer & Explanation (Question 71)</strong></summary>

**Correct Answer:** `A, C`

The AWS CAF organizes guidance into six perspectives: Business, People, Governance, Platform, Security, and Operations. Governance focuses on orchestrating cloud initiatives while maximizing organizational benefits and minimizing transformation-related risks, and People focuses on developing an organization-wide change management strategy and building cloud skills across the workforce.
Financial is not one of the six AWS CAF perspectives; financial and cost-related guidance falls within the Business perspective, which addresses how cloud adoption drives business value and return on investment rather than existing as its own separate financial perspective. Infrastructure is not one of the six AWS CAF perspectives; guidance on building and provisioning the technology foundation for cloud workloads falls under the Platform perspective rather than a perspective named Infrastructure. Agility is a benefit and characteristic of cloud computing but is not one of the six CAF perspectives; it does not appear in the CAF framework structure alongside Business, People, Governance, Platform, Security, and Operations.

</details>

---

### Question 72 — `CLF-U1312` | 🔁 Repeated in 1 Exam Sources
*Topic: Topic 1.2: AWS Cloud Adoption Framework (CAF 3.0)*

**According to the AWS Cloud Adoption Framework (AWS CAF), which TWO of the following are benefits that organizations can achieve through successful cloud adoption?**

- A) Reduced business risk
- B) Elimination of all operational expenditure
- C) Improved environmental, social, and governance (ESG) performance
- D) Immediate compliance with all regulatory requirements
- E) Guaranteed elimination of all security vulnerabilities

<details>
<summary><strong>Reveal Answer & Explanation (Question 72)</strong></summary>

**Correct Answer:** `A, C`

The AWS CAF identifies four key benefits of cloud adoption: reduced business risk through improved reliability, increased performance, and enhanced security posture; improved ESG performance through reduced carbon footprint and greater energy efficiency enabled by cloud infrastructure; increased revenue through the ability to develop and deliver new products faster; and increased operational efficiency through optimized cost structures and workforce productivity.
Elimination of all operational expenditure is not an AWS CAF benefit; moving to the cloud converts large upfront capital expenditure to variable operational expenditure rather than eliminating ongoing costs, as customers continue to pay for cloud services based on actual consumption and operational costs such as staffing and tooling remain. Immediate compliance with all regulatory requirements is not a benefit the CAF promises; while AWS provides compliance certifications and tools to support customers' compliance programs, each customer is still responsible for applying the appropriate controls to their own workloads and meeting their specific regulatory obligations. Guaranteed elimination of all security vulnerabilities is not a CAF-defined benefit; while cloud adoption can improve the security posture of an organization through shared responsibility and access to advanced security services, the CAF does not promise that cloud migration eliminates all security risk.

</details>

---

## 🎯 Domain 2: Security and Compliance (30% — 90 Questions)

### Question 73 — `CLF-U0013` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**You are working on a project that involves creating thumbnails of millions of images. Consistent uptime is not an issue, and continuous processing is not required. Which EC2 buying option would be the most cost-effective?**

- A) Reserved Instances.
- B) On-demand Instances.
- C) Dedicated Instances.
- D) Spot Instances.

<details>
<summary><strong>Reveal Answer & Explanation (Question 73)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Spot Instances**

Spot Instances offer significant cost savings compared to On-Demand or Reserved Instances. They allow you to bid on spare EC2 computing capacity. Because consistent uptime isn't a requirement and continuous processing isn't needed (the project can tolerate interruptions), Spot Instances are a good fit. If your bid exceeds the current spot price, your instances run. If the spot price goes above your bid, AWS can terminate your instances, but you only pay for the partial hour that the instance ran. For tasks like image thumbnail creation, where interruptions are acceptable and the work can be resumed later, Spot Instances provide the most cost-effective solution.

**Incorrect:**

**B. On-demand Instances** - On-demand Instances are a pay-as-you-go model, suitable for short-term, irregular workloads that cannot be interrupted. They are more expensive than Spot Instances and are not the most cost-effective option when consistent uptime is not a requirement.

**C. Reserved Instances** - Reserved Instances provide a significant discount compared to On-Demand Instances, but require a commitment of 1 or 3 years. They are best suited for steady-state, predictable workloads. Since the project doesn't require continuous processing, the commitment of Reserved Instances is not necessary, making them less cost-effective than Spot Instances.

**D. Dedicated Instances** - Dedicated Instances run in a VPC on hardware that's dedicated to a single customer. They are the most expensive EC2 option and are typically used for compliance or regulatory requirements. Since the project doesn't have specific hardware isolation needs, Dedicated Instances are not a cost-effective choice.

</details>

---

### Question 74 — `CLF-U0032` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following AWS services can be used as a compute resource? (Choose TWO)**

- A) Amazon VPC.
- B) Amazon CloudWatch.
- C) Amazon S3.
- D) Amazon EC2.
- E) AWS Lambda.

<details>
<summary><strong>Reveal Answer & Explanation (Question 74)</strong></summary>

**Correct Answer:** `D, E`

**Correct answer: AWS Lambda**

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. You upload your code as a "Lambda function," and AWS Lambda runs your code in response to events, automatically managing the underlying compute resources. This makes it a compute resource.

**Correct answer: Amazon EC2**

Amazon Elastic Compute Cloud (EC2) provides virtual servers in the cloud. You have full control over the operating system, applications, and security settings of your EC2 instances. EC2 is a fundamental compute service in AWS, allowing you to run a wide variety of workloads.

**Incorrect:**

**A. Amazon S3** - Amazon S3 (Simple Storage Service) is an object storage service. While you can host static websites on S3, it's primarily designed for storing and retrieving data, not for running code or performing computations. It is not a compute resource.

**B. Amazon CloudWatch** - Amazon CloudWatch is a monitoring and observability service. It collects and tracks metrics, collects and monitors log files, and sets alarms. While it processes data, it doesn't execute code in the same way as compute services like EC2 or Lambda. It is not a compute resource.

**C. Amazon VPC** - Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. It provides networking capabilities, not compute. It is not a compute resource.

</details>

---

### Question 75 — `CLF-U0057` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**What does Amazon Elastic Beanstalk provide?**

- A) A PaaS solution to automate application deployment.
- B) A compute engine for Amazon ECS.
- C) A scalable file storage solution for use with AWS and on-premises servers.
- D) A NoSQL database service.

<details>
<summary><strong>Reveal Answer & Explanation (Question 75)</strong></summary>

**Correct Answer:** `A`

**Correct answer: A PaaS solution to automate application deployment**

Amazon Elastic Beanstalk is a Platform as a Service (PaaS) that simplifies the deployment and management of web applications and services. It allows developers to upload their code, and Elastic Beanstalk automatically handles the infrastructure provisioning, operating system management, application deployment, and health monitoring. This reduces the operational burden on developers, enabling them to focus on writing code rather than managing infrastructure. Elastic Beanstalk supports various programming languages and platforms like Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.

**Incorrect:**

**B. A compute engine for Amazon ECS** - Amazon ECS (Elastic Container Service) is a container orchestration service. While Elastic Beanstalk can deploy applications packaged as Docker containers, it is not a compute engine *for* ECS. ECS has its own compute engine options, such as EC2 instances or AWS Fargate.

**C. A scalable file storage solution for use with AWS and on-premises servers** - This describes Amazon S3 (Simple Storage Service) or AWS Storage Gateway, not Elastic Beanstalk. S3 provides object storage, while Storage Gateway connects on-premises environments to AWS storage services.

**D. A NoSQL database service** - This describes services like Amazon DynamoDB. Elastic Beanstalk can *deploy* applications that use NoSQL databases, but it is not a database service itself.

</details>

---

### Question 76 — `CLF-U0063` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**A company has deployed a new web application on multiple Amazon EC2 instances. Which of the following should they use to ensure that the incoming HTTP traffic is distributed evenly across the instances?**

- A) AWS EC2 Auto Recovery.
- B) AWS Auto Scaling.
- C) AWS Network Load Balancer.
- D) AWS Application Load Balancer.

<details>
<summary><strong>Reveal Answer & Explanation (Question 76)</strong></summary>

**Correct Answer:** `D`

**Correct answer: AWS Application Load Balancer**

An Application Load Balancer (ALB) is designed for HTTP and HTTPS traffic. It operates at the application layer (Layer 7 of the OSI model) and can make routing decisions based on the content of the request, such as the URL path or host header. This allows for advanced routing capabilities, such as routing traffic to different EC2 instances based on the requested URL. ALBs are well-suited for distributing web application traffic evenly across multiple EC2 instances, ensuring high availability and scalability.

**Incorrect:**

**B. AWS Gateway Load Balancer** - A Gateway Load Balancer is designed for deploying and managing virtual appliances, such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems. It is not designed for distributing HTTP traffic to EC2 instances.

**C. AWS Network Load Balancer** - A Network Load Balancer (NLB) operates at the transport layer (Layer 4 of the OSI model). While it can distribute TCP traffic, it is not optimized for HTTP traffic and does not have the content-based routing capabilities of an Application Load Balancer. NLBs are better suited for applications that require extremely high performance and low latency, such as gaming or streaming.

**D. AWS Auto Scaling** - AWS Auto Scaling is a service that automatically adjusts the number of EC2 instances in your Auto Scaling group based on demand. While Auto Scaling helps maintain the desired capacity of EC2 instances, it does not distribute incoming traffic across those instances. A load balancer is required to distribute the traffic evenly.

</details>

---

### Question 77 — `CLF-U0078` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following AWS services scale automatically without your intervention? (Choose TWO)**

- A) Amazon EC2.
- B) Amazon S3.
- C) AWS Lambda.
- D) Amazon EMR.
- E) Amazon EBS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 77)</strong></summary>

**Correct Answer:** `B, C`

**Correct answer: Amazon S3**

Amazon S3 (Simple Storage Service) is designed to automatically scale to store and retrieve any amount of data, at any time, from anywhere. It handles scaling transparently without requiring any manual intervention from the user. You don't need to provision storage in advance; S3 automatically scales to accommodate your data as you upload it.

**Correct answer: AWS Lambda**

AWS Lambda automatically scales your function execution by running your code in response to each trigger. Lambda handles the scaling automatically, so you don't need to worry about provisioning or managing servers. Lambda scales almost instantaneously to handle incoming requests, up to the account concurrency limits.

**Incorrect:**

**A. Amazon EC2** - While EC2 can be scaled using Auto Scaling groups, this requires configuration and is not automatic out-of-the-box. You need to define scaling policies and triggers for EC2 to scale automatically. Without this configuration, EC2 instances do not automatically scale.

**B. Amazon EBS** - Amazon EBS (Elastic Block Storage) volumes do not automatically scale in size or performance. You must manually modify the volume size or type to increase capacity or performance. While you can use EBS snapshots and restore them to larger volumes, this is not an automatic scaling process.

**C. Amazon EMR** - Amazon EMR (Elastic MapReduce) clusters can be scaled, but this requires configuration of instance groups and scaling rules. It doesn't happen automatically without user intervention. You need to define how and when the cluster should scale based on metrics like CPU utilization or YARN memory usage.

</details>

---

### Question 78 — `CLF-U0080` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**A company needs to migrate their website from on-premises to AWS. Security is a major concern for them, so they need to host their website on hardware that is NOT shared with other AWS customers. Which of the following EC2 instance options meets this requirement?**

- A) On-demand instances.
- B) Spot instances.
- C) Dedicated instances.
- D) Reserved instances.

<details>
<summary><strong>Reveal Answer & Explanation (Question 78)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Dedicated instances**

Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. This means that no other AWS customers will share the same physical hardware as your Dedicated Instances. This provides the highest level of isolation and is suitable for workloads with strict compliance or regulatory requirements, or for organizations that want to control the physical hardware their instances run on. This addresses the company's security concerns related to shared hardware.

**Incorrect:**

**A. On-demand instances** - On-demand instances are the default EC2 instance type and run on shared hardware. This means that your instance may share the same physical server with instances belonging to other AWS customers. Therefore, on-demand instances do not meet the requirement of dedicated hardware.

**B. Reserved instances** - Reserved Instances are a billing option that provides a discount compared to On-Demand pricing, in exchange for a commitment to use the instance for a specified period. Reserved Instances can run on shared hardware, unless specifically configured as Dedicated Instances or Dedicated Hosts. Therefore, simply using Reserved Instances does not guarantee dedicated hardware.

**C. Spot instances** - Spot instances allow you to bid on unused EC2 capacity and can provide significant cost savings. However, Spot Instances always run on shared hardware. They are also subject to interruption with a two-minute warning if the Spot price exceeds your bid. Therefore, Spot Instances do not meet the requirement of dedicated hardware and are not suitable for production workloads requiring high availability or security.

</details>

---

### Question 79 — `CLF-U0089` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following is NOT a characteristic of Amazon Elastic Compute Cloud (Amazon EC2)?**

- A) Amazon EC2 is considered a Serverless Web Service.
- B) Amazon EC2 eliminates the need to invest in hardware upfront.
- C) Amazon EC2 can launch as many or as few virtual servers as needed.
- D) Amazon EC2 offers scalable computing.

<details>
<summary><strong>Reveal Answer & Explanation (Question 79)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon EC2 is considered a Serverless Web Service**

Amazon EC2 (Elastic Compute Cloud) provides virtual servers in the cloud, giving users control over the operating system, applications, and other configurations. EC2 instances require you to manage the underlying infrastructure, including patching, scaling, and server maintenance. Serverless computing, on the other hand, abstracts away the underlying infrastructure, allowing developers to focus solely on writing and deploying code without managing servers. Services like AWS Lambda are examples of serverless offerings. Therefore, EC2 is not a serverless service.

**Incorrect:**

**A. Amazon EC2 offers scalable computing** - Amazon EC2 provides scalable computing capacity. You can easily increase or decrease the number of EC2 instances based on your application's needs, making it a scalable solution. This is a core characteristic of EC2.

**B. Amazon EC2 eliminates the need to invest in hardware upfront** - One of the key benefits of Amazon EC2 is that it eliminates the need for upfront investment in physical hardware. You pay only for the compute capacity you use, reducing capital expenditure. This is a fundamental advantage of cloud computing and EC2.

**D. Amazon EC2 can launch as many or as few virtual servers as needed** - Amazon EC2 allows you to launch as many or as few virtual servers (instances) as needed, providing flexibility and control over your computing resources. This dynamic provisioning is a defining characteristic of EC2 and cloud computing in general.

</details>

---

### Question 80 — `CLF-U0104` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**A company is seeking to deploy an existing .NET application onto AWS as quickly as possible. Which AWS Service should the customer use to achieve this goal?**

- A) Amazon SNS.
- B) AWS Elastic Beanstalk.
- C) AWS Systems Manager.
- D) AWS Trusted Advisor.

<details>
<summary><strong>Reveal Answer & Explanation (Question 80)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS Elastic Beanstalk**

AWS Elastic Beanstalk is a Platform as a Service (PaaS) that makes it easy for developers to deploy and manage web applications and services. It supports various platforms, including .NET. Elastic Beanstalk handles the underlying infrastructure provisioning (e.g., EC2 instances, load balancers), operating system maintenance, and application health monitoring, allowing the developer to focus on writing code. This makes it the quickest way to deploy an existing application to AWS, as it automates much of the deployment process.

**Incorrect:**

**A. AWS Amplify** - AWS Amplify is a set of tools and services designed to help front-end web and mobile developers build and deploy scalable full-stack applications, particularly those with serverless backends. While it can be used with .NET applications, it's not the primary service for quickly deploying an existing .NET application. It's more focused on building new applications from scratch or adding cloud capabilities to existing front-end applications.

**B. AWS Systems Manager** - AWS Systems Manager is a management service that helps you automatically manage your AWS resources. It is used for operational tasks like patching, configuration management, and automation. While it can be used to manage .NET applications running on AWS, it doesn't provide a simplified deployment process like Elastic Beanstalk.

**C. AWS Trusted Advisor** - AWS Trusted Advisor is an online tool that provides real-time guidance to help you provision your resources following AWS best practices. It inspects your AWS environment and makes recommendations for cost optimization, security, fault tolerance, service limits, and performance improvements. It does not deploy applications.

</details>

---

### Question 81 — `CLF-U0387` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following does NOT belong to the AWS Cloud Computing models?**

- A) Platform as a Service (PaaS).
- B) Infrastructure as a Service (IaaS).
- C) Software as a Service (SaaS).
- D) Networking as a Service (NaaS).

<details>
<summary><strong>Reveal Answer & Explanation (Question 81)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Networking as a Service (NaaS)**

Networking as a Service (NaaS) is not one of the core cloud computing models recognized by AWS. The fundamental cloud computing models are Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). While networking is a critical component of cloud services, it's typically delivered as part of IaaS or PaaS offerings, rather than being a standalone cloud computing model in the same vein as IaaS, PaaS, and SaaS.

**Incorrect:**

**B. Software as a Service (SaaS)** - SaaS is a cloud computing model where users access software applications over the internet. Examples include Salesforce, Gmail, and Microsoft Office 365. This is a valid cloud computing model.

**C. Platform as a Service (PaaS)** - PaaS provides a platform allowing customers to develop, run, and manage applications without the complexity of managing the underlying infrastructure. AWS Elastic Beanstalk and AWS Lambda are examples of PaaS offerings. This is a valid cloud computing model.

**D. Infrastructure as a Service (IaaS)** - IaaS provides access to fundamental computing resources – virtual machines, storage, networks – over the internet. AWS EC2, S3, and VPC are examples of IaaS. This is a valid cloud computing model.

</details>

---

### Question 82 — `CLF-U0391` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**What are two advantages of using Cloud Computing over using traditional data centers? (Choose TWO)**

- A) Reserved Compute capacity.
- B) Eliminating Single Points of Failure (SPOFs).
- C) Distributed infrastructure.
- D) Virtualized compute resources.
- E) Dedicated hosting.

<details>
<summary><strong>Reveal Answer & Explanation (Question 82)</strong></summary>

**Correct Answer:** `B, C`

**Correct answer: Eliminating Single Points of Failure (SPOFs)**

Cloud computing, when architected correctly, can eliminate single points of failure (SPOFs). This is achieved through redundancy and distribution of resources across multiple availability zones or regions. If one component fails, the application can continue to operate using resources in another zone or region. This is a significant advantage over traditional data centers, where a single hardware failure can bring down an entire system.

**Correct answer: Distributed infrastructure**

Cloud computing provides a distributed infrastructure, meaning resources are spread across multiple geographic locations. This distribution offers several advantages, including improved availability, reduced latency for users in different regions, and the ability to comply with data sovereignty regulations. Traditional data centers are often limited to a single location, making it difficult to achieve the same level of distribution.

**Incorrect:**

**A. Virtualized compute resources** - While cloud computing utilizes virtualized compute resources, traditional data centers can also implement virtualization. Therefore, virtualization itself is not a unique advantage of cloud computing over traditional data centers.

**B. Dedicated hosting** - Dedicated hosting is a characteristic of traditional data centers, where a physical server is dedicated to a single tenant. Cloud computing, on the other hand, often utilizes shared resources, although dedicated instances are also available. Dedicated hosting is not an advantage of cloud computing over traditional data centers.

**C. Reserved Compute capacity** - Both cloud computing and traditional data centers can offer reserved compute capacity. In the cloud, this is often achieved through reserved instances or savings plans. In traditional data centers, it involves purchasing and maintaining hardware in advance. Therefore, reserved compute capacity is not a differentiating advantage of cloud computing.

</details>

---

### Question 83 — `CLF-U0394` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**What are the AWS services/features that can help you maintain a highly available and fault-tolerant architecture in AWS? (Choose TWO)**

- A) AWS Direct Connect.
- B) Amazon EC2 Auto Scaling.
- C) Elastic Load Balancer.
- D) CloudFormation.
- E) Network ACLs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 83)</strong></summary>

**Correct Answer:** `B, C`

**Correct answer: Elastic Load Balancer**

Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. This distribution enhances fault tolerance by ensuring that if one target fails, traffic is automatically routed to the remaining healthy targets. ELB also supports health checks to monitor the health of registered targets and automatically removes unhealthy targets from the load balancing rotation, further improving availability.

**Correct answer: Amazon EC2 Auto Scaling**

Amazon EC2 Auto Scaling helps you maintain application availability and allows you to automatically add or remove EC2 instances in response to changing application demand. You can define scaling policies that trigger the launch of new instances when demand increases or terminate instances when demand decreases. This dynamic scaling ensures that your application always has the necessary resources to handle traffic, even during peak periods, and helps maintain high availability by automatically replacing failed instances.

**Incorrect:**

**A. CloudFormation** - CloudFormation is an Infrastructure as Code (IaC) service that allows you to define and provision AWS infrastructure using templates. While CloudFormation can be used to deploy highly available architectures, it doesn't directly provide the mechanisms for maintaining availability and fault tolerance at runtime. It's a deployment tool, not a runtime availability service.

**C. Network ACLs** - Network Access Control Lists (ACLs) are used to control inbound and outbound traffic at the subnet level. They act as a firewall for controlling network traffic. While important for security, they do not directly contribute to high availability or fault tolerance. They can potentially *reduce* availability if misconfigured.

**D. AWS Direct Connect** - AWS Direct Connect establishes a dedicated network connection from your on-premises environment to AWS. While it can improve network performance and reduce latency, it doesn't directly provide high availability or fault tolerance for your application architecture within AWS. It's primarily for hybrid cloud connectivity.

</details>

---

### Question 84 — `CLF-U0396` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**What is the AWS serverless service that allows you to run your applications without any administrative burden?**

- A) Amazon LightSail.
- B) AWS Lambda.
- C) Amazon RDS instances.
- D) Amazon EC2 instances.

<details>
<summary><strong>Reveal Answer & Explanation (Question 84)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS Lambda**

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. You only pay for the compute time you consume, making it a cost-effective solution for many types of applications. Lambda handles all the underlying infrastructure, including server and operating system maintenance, capacity provisioning and automatic scaling, and code monitoring and logging. This allows developers to focus on writing code without the administrative burden of managing servers.

**Incorrect:**

**A. Amazon EC2 instances** - Amazon EC2 instances are virtual servers in the cloud. While EC2 provides flexibility and control, it requires you to manage the operating system, patching, and scaling, which introduces administrative overhead. This is the opposite of a serverless service.

**B. Amazon LightSail** - Amazon Lightsail is designed to be easy to use and offers virtual servers, containers, databases, and more at a predictable monthly price. While it simplifies server management compared to EC2, it still requires you to manage the underlying infrastructure, making it not a serverless solution.

**D. Amazon RDS instances** - Amazon RDS (Relational Database Service) instances are managed database services. While RDS simplifies database administration tasks like patching and backups, you are still responsible for managing the database instance, including sizing, scaling, and performance tuning. This is not a serverless compute service.

</details>

---

### Question 85 — `CLF-U0411` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**What are AWS shared controls?**

- A) Controls that are solely the responsibility of the customer based on the application they are deploying within AWS services.
- B) Controls that a customer inherits from AWS.
- C) Controls that apply to both the infrastructure layer and customer layers.
- D) Controls that the customer and AWS collaborate together upon to secure the infrastructure.

<details>
<summary><strong>Reveal Answer & Explanation (Question 85)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Controls that apply to both the infrastructure layer and customer layers**

AWS shared controls are security controls that are the responsibility of both AWS and the customer. This means that AWS is responsible for the underlying infrastructure and the customer is responsible for configuring and using the services securely. For example, patch management is a shared control. AWS is responsible for patching the underlying infrastructure, while the customer is responsible for patching their operating systems and applications running on EC2 instances. Another example is awareness and training; AWS trains its employees, and customers are responsible for training their own employees. This shared responsibility model is a core concept in AWS security.

**Incorrect:**

**A. Controls that the customer and AWS collaborate together upon to secure the infrastructure** - While collaboration is implied in the shared responsibility model, this option is too vague. Shared controls are specifically those that *apply* to both layers, not just any area where collaboration might occur.

**C. Controls that are solely the responsibility of the customer based on the application they are deploying within AWS services** - These are customer-specific controls, not shared controls. Shared controls, by definition, involve responsibilities for both AWS and the customer.

**D. Controls that a customer inherits from AWS** - These are inherited controls. Inherited controls are controls that the customer fully inherits from AWS. For example, physical security of the data centers is an inherited control.

</details>

---

### Question 86 — `CLF-U0412` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which design principles relate to performance efficiency in AWS? (Choose TWO)**

- A) Build multi-region architectures to better serve global customers.
- B) Apply security at all layers.
- C) Implement strong Identity and Access controls.
- D) Use serverless architectures.
- E) Enable audit logging.

<details>
<summary><strong>Reveal Answer & Explanation (Question 86)</strong></summary>

**Correct Answer:** `A, D`

**Correct answer: Use serverless architectures**

Serverless architectures, such as AWS Lambda, are a key design principle for performance efficiency. They allow you to run code without provisioning or managing servers. This eliminates the overhead of managing infrastructure, automatically scales based on demand, and you only pay for the compute time you consume, leading to cost optimization and improved performance. The underlying infrastructure is managed by AWS, allowing developers to focus on writing and deploying code.

**Correct answer: Build multi-region architectures to better serve global customers**

Building multi-region architectures improves performance efficiency by reducing latency for users in different geographic locations. By deploying applications and data closer to users, you minimize the distance data needs to travel, resulting in faster response times and a better user experience. This also enhances availability and fault tolerance, contributing to overall performance efficiency.

**Incorrect:**

**A. Enable audit logging** - While audit logging is crucial for security and compliance, it primarily addresses security and governance concerns rather than directly impacting performance efficiency. Audit logs help track user activity and system events, but they don't inherently improve the speed or resource utilization of applications.

**B. Apply security at all layers** - Applying security at all layers is essential for protecting data and systems, but it doesn't directly relate to performance efficiency. Security measures can sometimes introduce overhead, but the primary goal is to mitigate risks, not to optimize performance. Security is a separate pillar in the AWS Well-Architected Framework.

**E. Implement strong Identity and Access controls** - Strong Identity and Access Management (IAM) controls are vital for security, ensuring that only authorized users and services have access to resources. However, IAM primarily focuses on controlling access and permissions, not on optimizing the performance or resource utilization of applications. While proper IAM can prevent unauthorized resource usage, it doesn't directly enhance performance efficiency.

</details>

---

### Question 87 — `CLF-U0576` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following EC2 instance purchasing options supports the Bring Your Own License (BYOL) model for almost every BYOL scenario?**

- A) Dedicated Instances.
- B) Dedicated Hosts.
- C) On-demand Instances.
- D) Reserved Instances.

<details>
<summary><strong>Reveal Answer & Explanation (Question 87)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Dedicated Hosts**

Dedicated Hosts are physical servers with EC2 instance capacity dedicated for your use. Using Dedicated Hosts allows you to use your existing server-bound software licenses, including Windows Server, SQL Server, and SUSE Linux Enterprise Server. This is the best option for Bring Your Own License (BYOL) scenarios, especially those with complex licensing requirements or compliance needs, as it provides the most control and isolation. You can launch EC2 instances onto Dedicated Hosts, and AWS ensures that no other customers' instances will run on that hardware. This helps meet compliance requirements and reduces the risk of license violations.

**Incorrect:**

**A. On-demand Instances** - While you can technically use BYOL with On-demand instances, it's not the ideal or most compliant option for all BYOL scenarios. Some licenses require dedicated hardware, which On-demand instances do not provide by default. You would need to ensure your license terms allow for use on shared hardware, which is not always the case.

**B. Dedicated Instances** - Dedicated Instances run in a VPC on hardware that's dedicated to a single customer. While better than On-demand for BYOL, they don't offer the same level of control and visibility as Dedicated Hosts. You don't have control over the specific physical server, which can be a problem for certain licensing agreements. Dedicated Hosts offer more granular control and are therefore better suited for most BYOL scenarios.

**C. Reserved Instances** - Reserved Instances are a billing discount applied to On-demand instances. They do not change the underlying hardware or tenancy of the instances. Therefore, they don't inherently support BYOL any better than On-demand instances do. The BYOL compatibility depends on the instance type and the specific license terms, not the Reserved Instance billing model.

</details>

---

### Question 88 — `CLF-U0788` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which statement is true regarding the AWS Shared Responsibility Model?**

- A) Responsibilities vary depending on the services used.
- B) Security of the IaaS services is the responsibility of AWS.
- C) Patching the guest OS is always the responsibility of AWS.
- D) Security of the managed services is the responsibility of the customer.

<details>
<summary><strong>Reveal Answer & Explanation (Question 88)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Responsibilities vary depending on the services used**

The AWS Shared Responsibility Model defines the security responsibilities between AWS and the customer. AWS is responsible for the security *of* the cloud, while the customer is responsible for security *in* the cloud. The exact division of these responsibilities depends on the specific AWS services being used. For example, with IaaS services like EC2, the customer is responsible for managing the guest operating system (including updates and security patches), while with PaaS services like RDS or serverless services like Lambda, AWS manages much of the underlying infrastructure, reducing the customer's operational burden. Therefore, responsibilities vary based on the service.

**Incorrect:**

**A. Patching the guest OS is always the responsibility of AWS** - This is incorrect. For IaaS services like EC2, the customer is responsible for patching the guest operating system. AWS is only responsible for patching the underlying infrastructure that supports EC2.

**B. Security of the IaaS services is the responsibility of AWS** - While AWS is responsible for the security *of* the underlying infrastructure for IaaS services, the customer retains responsibility for securing their applications, data, and operating systems running *on* those services. Therefore, this statement is too broad.

**D. Security of the managed services is the responsibility of the customer** - This is incorrect. For managed services like RDS or DynamoDB, AWS assumes more responsibility for security, including patching the underlying infrastructure and managing the database software. The customer is still responsible for securing their data and access to the service, but AWS handles more of the operational security aspects.

</details>

---

### Question 89 — `CLF-U0794` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**In the AWS Shared responsibility Model, which of the following are the responsibility of the customer? (Choose TWO)**

- A) Disk disposal.
- B) Controlling physical access to compute resources.
- C) Patching the Network infrastructure.
- D) Setting password complexity rules.
- E) Configuring network access rules.

<details>
<summary><strong>Reveal Answer & Explanation (Question 89)</strong></summary>

**Correct Answer:** `D, E`

**Correct answer: Configuring network access rules**

Configuring network access rules, such as security groups and network ACLs, is a customer responsibility under the AWS Shared Responsibility Model. Customers are responsible for controlling access to their AWS resources by defining rules that specify which traffic is allowed to enter and exit their virtual networks and instances. These rules govern network security and are a key aspect of securing your applications in the cloud.

**Correct answer: Setting password complexity rules**

Setting password complexity rules is a customer responsibility. This includes defining password policies for user accounts, such as minimum length, required character types, and password expiration. These policies are crucial for maintaining the security of user accounts and protecting against unauthorized access to AWS resources. AWS Identity and Access Management (IAM) allows customers to configure these password policies.

**Incorrect:**

**A. Patching the Network infrastructure** - Patching the network infrastructure is AWS's responsibility. AWS manages the underlying infrastructure, including network devices, and is responsible for ensuring its security and reliability. Customers do not have access to the physical network infrastructure.

**B. Controlling physical access to compute resources** - Controlling physical access to compute resources is AWS's responsibility. AWS is responsible for the physical security of its data centers and the hardware within them. Customers do not have physical access to the servers or other infrastructure components.

**D. Disk disposal** - Disk disposal is AWS's responsibility. When hardware is decommissioned, AWS is responsible for securely erasing or destroying the data on the disks to prevent data leakage. Customers do not have to handle physical disk disposal.

</details>

---

### Question 90 — `CLF-U0800` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following aspects of security are managed by AWS? (Choose TWO)**

- A) Encryption of EBS volumes.
- B) VPC security.
- C) Access permissions.
- D) Hardware patching.
- E) Securing global physical infrastructure.

<details>
<summary><strong>Reveal Answer & Explanation (Question 90)</strong></summary>

**Correct Answer:** `D, E`

**Correct answer: Securing global physical infrastructure**

AWS is responsible for the security *of* the cloud. This includes protecting the physical infrastructure that runs all of the AWS services. This encompasses the physical security of data centers, hardware, and the network infrastructure. This is a key component of the AWS shared responsibility model.

**Correct answer: Hardware patching**

AWS manages the underlying hardware and infrastructure. This includes patching and maintaining the hardware to ensure its security and reliability. Customers do not have access to the underlying hardware and therefore cannot patch it themselves. This is part of AWS's responsibility in the shared responsibility model.

**Incorrect:**

**A. Encryption of EBS volumes** - While AWS provides services and features to encrypt EBS volumes (like AWS Key Management Service (KMS) and EBS encryption), the customer is responsible for enabling and managing the encryption of their data at rest and in transit. AWS provides the tools, but the responsibility for using them correctly lies with the customer.

**C. Access permissions** - Managing access permissions is primarily the customer's responsibility. AWS Identity and Access Management (IAM) allows customers to define users, groups, and roles with specific permissions to access AWS resources. The customer is responsible for configuring these permissions according to the principle of least privilege to ensure that users only have access to the resources they need. AWS provides the service (IAM), but the configuration and management are the customer's responsibility.

**E. VPC security** - While AWS provides services like Security Groups and Network ACLs to secure VPCs, the configuration and management of these services are the customer's responsibility. The customer defines the rules for inbound and outbound traffic, thereby controlling access to the resources within the VPC. AWS provides the tools, but the customer is responsible for using them correctly to secure their VPC.

</details>

---

### Question 91 — `CLF-U0806` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Under the Shared Responsibility Model, which of the following controls do customers fully inherit from AWS? (Choose TWO)**

- A) Patch management controls.
- B) Database controls.
- C) Awareness & Training.
- D) Environmental controls.
- E) Physical controls.

<details>
<summary><strong>Reveal Answer & Explanation (Question 91)</strong></summary>

**Correct Answer:** `D, E`

**Correct answer: Environmental controls**

AWS is responsible for the physical environment in which its cloud infrastructure operates. This includes controls related to climate control, power, and other environmental factors within AWS data centers. Customers fully inherit these controls because they have no direct control or responsibility for the AWS physical infrastructure.

**Correct answer: Physical controls**

AWS is responsible for the physical security of its data centers, including measures such as security guards, surveillance, and access controls. Customers fully inherit these controls as they do not have physical access to AWS data centers and rely on AWS to maintain the physical security of the infrastructure.

**Incorrect:**

**A. Patch management controls** - While AWS manages patching of the underlying infrastructure, customers are responsible for patching their operating systems, applications, and databases running on AWS services like EC2. Therefore, customers do not fully inherit patch management controls.

**D. Database controls** - Customers are responsible for managing and securing their databases, including access control, encryption, and backups, even when using managed database services like RDS. AWS manages the underlying infrastructure, but the customer controls the database itself. Therefore, customers do not fully inherit database controls.

**E. Awareness & Training** - Customers are responsible for the security awareness and training of their own employees regarding cloud security best practices and their responsibilities within the Shared Responsibility Model. AWS provides security awareness training for its own employees, but this does not extend to the customer's workforce. Therefore, customers do not fully inherit awareness & training controls.

</details>

---

### Question 92 — `CLF-U0826` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**Which of the following are examples of the customer’s responsibility to implement “security IN the cloud”? (Choose TWO)**

- A) Building a schema for an application.
- B) Replacing physical hardware.
- C) Creating a new hypervisor.
- D) Patch management of the underlying infrastructure.
- E) File system encryption.

<details>
<summary><strong>Reveal Answer & Explanation (Question 92)</strong></summary>

**Correct Answer:** `A, E`

**Correct answer: File system encryption**

File system encryption is a customer responsibility under the shared responsibility model. The customer is responsible for encrypting their data at rest within the file system of their EC2 instances or other storage services. AWS provides tools and services to facilitate encryption, but the customer is responsible for implementing and managing it.

**Correct answer: Building a schema for an application**

Building a schema for an application is a customer responsibility. The customer is responsible for the design, security, and management of their applications and data, including the schema that defines the structure of the data. AWS provides database services, but the customer defines how those services are used.

**Incorrect:**

**A. Replacing physical hardware** - Replacing physical hardware is an AWS responsibility. AWS manages the underlying infrastructure, including replacing faulty hardware. This is part of "security OF the cloud."

**B. Creating a new hypervisor** - Creating and maintaining the hypervisor is an AWS responsibility. The hypervisor is part of the underlying infrastructure that AWS manages. This is part of "security OF the cloud."

**D. Patch management of the underlying infrastructure** - Patch management of the underlying infrastructure is an AWS responsibility. AWS is responsible for patching and maintaining the operating systems and software on the infrastructure that supports its services. This is part of "security OF the cloud."

</details>

---

### Question 93 — `CLF-U1460` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.1: AWS Shared Responsibility Model*

**A company needs to host a highly available application in the AWS Cloud. The application runs infrequently for short periods of time. > Which AWS service will meet these requirements with the **LEAST** amount of operational overhead? #### Options - **A.** AWS Lambda **[CORRECT]** - **B.** AWS Fargate - **C.** Amazon Aurora - **D.** Amazon EC2**

- A) Amazon EC2
- B) AWS Fargate
- C) AWS Lambda
- D) Amazon Aurora

<details>
<summary><strong>Reveal Answer & Explanation (Question 93)</strong></summary>

**Correct Answer:** `C`

The AWS service that will meet the requirements of the company that needs to host a
highly available application in the AWS Cloud that runs infrequently for short periods of
time with the least amount of operational overhead is AWS Lambda. AWS Lambda is a
serverless compute service that allows customers to run code without provisioning or
managing servers. The company can use AWS Lambda to create and deploy their
application as functions that are triggered by events, such as API calls, messages, or
schedules. AWS Lambda automatically scales the compute resources based on the
demand, and customers only pay for the compute time they consume. AWS Lambda also
simplifies the management and maintenance of the application, as customers do not need
to worry about the underlying infrastructure, security, or availability. Amazon EC2, AWS
Fargate, and Amazon Aurora are not the best services to use for this purpose. Amazon
EC2 is a service that provides scalable compute capacity in t

</details>

---

### Question 94 — `CLF-U0017` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following must an IAM user provide to interact with AWS services using the AWS Command Line Interface (AWS CLI)?**

- A) Access keys.
- B) Secret token.
- C) UserID.
- D) User name and password.

<details>
<summary><strong>Reveal Answer & Explanation (Question 94)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Access keys**

To interact with AWS services using the AWS Command Line Interface (AWS CLI), an IAM user must configure the AWS CLI with their access key ID and secret access key. These access keys are used to digitally sign requests to AWS, allowing the AWS services to verify the identity of the user and ensure that they have the necessary permissions to perform the requested actions. Access keys are long-term credentials for an IAM user or the AWS account root user. It is a security best practice to use IAM users instead of the root user, and to rotate access keys periodically.

**Incorrect:**

**B. User ID** - While a User ID is a unique identifier for an IAM user, it is not used for authentication with the AWS CLI. Access keys (Access Key ID and Secret Access Key) are required for authentication.

**C. User name and password** - User names and passwords are used for logging into the AWS Management Console, not for authenticating with the AWS CLI. The AWS CLI uses access keys for authentication.

**D. Secret token** - Secret tokens are used in conjunction with temporary security credentials, such as those obtained through AWS STS (Security Token Service) when assuming an IAM role. While access keys are used directly for IAM users, a secret token is used when assuming a role and is not a direct credential for an IAM user.

</details>

---

### Question 95 — `CLF-U0040` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**What are the default security credentials that are required to access the AWS management console for an IAM user account?**

- A) MFA.
- B) Security tokens.
- C) A user name and password.
- D) Access keys.

<details>
<summary><strong>Reveal Answer & Explanation (Question 95)</strong></summary>

**Correct Answer:** `C`

**Correct answer: A user name and password**

To access the AWS Management Console using an IAM user account, you typically need a user name and password. These are the primary credentials used for authentication. When you create an IAM user, you can either generate an access key (for programmatic access via the AWS CLI, SDKs, or APIs) or enable console access, which requires setting a password. The username and password combination is the default and most common way for IAM users to log in to the AWS Management Console.

**Incorrect:**

**A. Security tokens** - Security tokens are temporary credentials used to grant limited-privilege access to AWS resources. They are often used in conjunction with IAM roles or when using multi-factor authentication (MFA), but they are not the default credentials required for logging into the AWS Management Console as an IAM user.

**B. MFA** - Multi-Factor Authentication (MFA) adds an extra layer of security to your AWS account. While highly recommended, MFA is not the default credential required to access the AWS Management Console. It is an additional security measure that you can enable after you have already authenticated with your username and password.

**C. Access keys** - Access keys (access key ID and secret access key) are used for programmatic access to AWS services via the AWS CLI, SDKs, or APIs. They are not used to log in to the AWS Management Console. Access keys are used by applications or command-line tools to make requests to AWS services without requiring a user to manually enter their credentials.

</details>

---

### Question 96 — `CLF-U0072` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**App development companies move their business to AWS to reduce time-to-market and improve customer satisfaction, what are the AWS automation tools that help them deploy their applications faster? (Choose TWO)**

- A) AWS CloudFormation.
- B) AWS Migration Hub.
- C) AWS IAM.
- D) AWS Elastic Beanstalk.
- E) Amazon Macie.

<details>
<summary><strong>Reveal Answer & Explanation (Question 96)</strong></summary>

**Correct Answer:** `A, D`

**Correct answer: AWS Elastic Beanstalk**

AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) that simplifies the deployment and management of web applications and services. Developers can upload their code, and Elastic Beanstalk automatically handles the infrastructure provisioning, operating system management, application deployment, and health monitoring. This allows app development companies to deploy applications faster by abstracting away the underlying infrastructure complexities.

**Correct answer: AWS CloudFormation**

AWS CloudFormation is an Infrastructure-as-Code (IaC) service that allows you to define and provision AWS infrastructure as code. You create templates that describe the desired state of your AWS resources, and CloudFormation automates the creation and configuration of those resources. This enables app development companies to deploy applications faster by automating the infrastructure setup process, ensuring consistency, and reducing manual errors.

**Incorrect:**

**A. AWS IAM** - AWS Identity and Access Management (IAM) is a service that enables you to manage access to AWS services and resources securely. While IAM is crucial for security and access control, it does not directly automate the deployment of applications. Its primary function is to define and manage user permissions and roles.

**B. Amazon Macie** - Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect sensitive data in AWS. Macie helps organizations comply with regulations and protect their data, but it does not directly contribute to the automation of application deployment.

**C. AWS Migration Hub** - AWS Migration Hub provides a central location to track the progress of application migrations to AWS. It helps you discover existing servers and applications, plan migrations, and track the status of each migration. While it aids in the overall migration process, it does not directly automate the deployment of applications once they are in AWS.

</details>

---

### Question 97 — `CLF-U0115` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following can be used to enable the Virtual Multi-Factor Authentication? (Choose TWO)**

- A) Amazon Connect.
- B) AWS CLI.
- C) AWS Identity and Access Management (IAM).
- D) Amazon SNS.
- E) Amazon Virtual Private Cloud.

<details>
<summary><strong>Reveal Answer & Explanation (Question 97)</strong></summary>

**Correct Answer:** `B, C`

**Correct answer: AWS CLI**

The AWS Command Line Interface (CLI) can be used to configure and manage AWS services, including enabling and managing virtual Multi-Factor Authentication (MFA) for IAM users. You can use CLI commands to activate MFA devices, associate them with users, and manage MFA settings.

**Correct answer: AWS Identity and Access Management (IAM)**

AWS Identity and Access Management (IAM) is the AWS service that allows you to manage access to AWS services and resources securely. IAM enables you to create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. A key security feature of IAM is the ability to enable MFA for users, adding an extra layer of security beyond just a username and password. You can enable virtual MFA devices directly within the IAM console or through the AWS CLI, which interacts with the IAM service.

**Incorrect:**

**A. AWS Secrets Manager** - AWS Secrets Manager helps you manage, retrieve, and rotate secrets, such as database credentials, API keys, and other sensitive information. While it enhances security, it doesn't directly enable or manage virtual MFA for IAM users.

**C. Amazon SNS** - Amazon Simple Notification Service (SNS) is a messaging service for sending notifications. While SNS can be used in conjunction with security measures (e.g., sending alerts about security events), it is not directly involved in enabling or managing virtual MFA for IAM users.

**E. Amazon Connect** - Amazon Connect is a cloud-based contact center service. It is not related to enabling or managing virtual MFA for IAM users.

</details>

---

### Question 98 — `CLF-U0575` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**What is the AWS service that enables you to manage all of your AWS accounts from a single master account?**

- A) AWS WAF.
- B) AWS Trusted Advisor.
- C) AWS Organizations.
- D) Amazon Config.

<details>
<summary><strong>Reveal Answer & Explanation (Question 98)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS Organizations**

AWS Organizations is an AWS service that allows you to centrally manage and govern multiple AWS accounts. It enables you to create organizational units (OUs), group accounts together, and apply policies across those accounts. This includes features like consolidated billing, which allows you to pay for all accounts in your organization from a single master account. You can also use service control policies (SCPs) to define guardrails and control which AWS services and actions are allowed in each account. This makes it easier to manage security, compliance, and resource allocation across your AWS environment.

**Incorrect:**

**A. Amazon Config** - Amazon Config is an AWS service that provides a detailed view of the configuration of AWS resources in your AWS accounts. It enables you to assess, audit, and evaluate the configurations of your resources. While Config is useful for governance and compliance, it doesn't manage multiple accounts from a single master account in the way that AWS Organizations does.

**B. AWS Trusted Advisor** - AWS Trusted Advisor is an online tool that provides real-time guidance to help you provision your resources following AWS best practices. Trusted Advisor checks help optimize your AWS infrastructure, increase security and performance, reduce costs, and monitor service limits. It provides recommendations on individual accounts, but it doesn't manage multiple accounts from a single master account.

**C. AWS WAF** - AWS WAF (Web Application Firewall) is a web application firewall that helps protect your web applications from common web exploits and bots. WAF can be deployed on Amazon CloudFront, Application Load Balancer, or Amazon API Gateway. While WAF is a crucial security service, it does not manage multiple AWS accounts from a single master account.

</details>

---

### Question 99 — `CLF-U0591` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**AWS recommends some practices to help organizations avoid unexpected charges on their bill. Which of the following is NOT one of these practices?**

- A) Deleting unused EBS volumes after terminating an EC2instance.
- B) Deleting unused AutoScaling launch configuration.
- C) Deleting unused Elastic Load Balancers.
- D) Releasing unused Elastic IPs after terminating an EC2instance.

<details>
<summary><strong>Reveal Answer & Explanation (Question 99)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Deleting unused AutoScaling launch configuration**

Deleting unused Auto Scaling launch configurations is a good practice for organization, but it does not directly impact AWS billing. Launch configurations are templates used to create EC2 instances within an Auto Scaling group. They don't consume resources or incur costs when they are not actively used by an Auto Scaling group. Therefore, keeping unused launch configurations around will not result in unexpected charges.

**Incorrect:**

**A. Deleting unused EBS volumes after terminating an EC2 instance** - EBS (Elastic Block Storage) volumes persist even after the EC2 instance they are attached to is terminated. If you don't delete these unused volumes, you will continue to be charged for the storage they consume. Deleting unused EBS volumes is a critical practice for cost optimization.

**B. Releasing unused Elastic IPs after terminating an EC2 instance** - Elastic IPs (EIPs) are static IPv4 addresses designed for dynamic cloud computing. While there's no charge for an Elastic IP when it's associated with a running EC2 instance, there is a small charge for Elastic IPs that are allocated but not associated with a running instance or are associated with a stopped instance. Releasing unused Elastic IPs is an important cost-saving measure.

**C. Deleting unused Elastic Load Balancers** - Elastic Load Balancers (ELBs) distribute incoming application traffic across multiple targets, such as EC2 instances. If you have an ELB that is no longer in use (i.e., no traffic is being routed through it), you will still be charged for it. Deleting unused ELBs is a key step in avoiding unnecessary costs.

</details>

---

### Question 100 — `CLF-U0789` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**An organization has a large number of technical employees who operate their AWS Cloud infrastructure. What does AWS provide to help organize them into teams and then assign the appropriate permissions for each team?**

- A) IAM roles.
- B) IAM users.
- C) IAM user groups.
- D) AWS Organizations.

<details>
<summary><strong>Reveal Answer & Explanation (Question 100)</strong></summary>

**Correct Answer:** `C`

**Correct answer: IAM user groups**

IAM user groups are a way to manage multiple IAM users. You can assign permissions to a user group, and all users in the group will inherit those permissions. This simplifies permission management, especially in organizations with many users. Instead of assigning permissions to individual users, you assign them to groups based on their roles or responsibilities. This aligns with the principle of least privilege by ensuring users only have the permissions necessary to perform their tasks. AWS recommends using groups to manage permissions.

**Incorrect:**

**A. IAM roles** - IAM roles are used to grant permissions to AWS services and applications running on AWS resources (like EC2 instances) to access other AWS services. They are not primarily designed for managing permissions for human users organized into teams.

**B. AWS Organizations** - AWS Organizations is used to centrally manage and govern multiple AWS accounts. While it helps with overall governance and can be used to apply policies across accounts, it doesn't directly organize individual users into teams or assign permissions to them within a single account. It operates at the account level, not the user level.

**C. IAM users** - While you can assign permissions directly to IAM users, this becomes difficult to manage as the number of users grows. It's not an efficient way to organize users into teams and manage permissions at scale. Assigning permissions to individual users is less scalable and more error-prone than using groups.

</details>

---

### Question 101 — `CLF-U0797` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following is equivalent to a user name and password and is used to authenticate your programmatic access to AWS services and APIs?**

- A) Instance Password.
- B) Key pairs.
- C) Access Keys.
- D) MFA.

<details>
<summary><strong>Reveal Answer & Explanation (Question 101)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Access Keys**

Access keys, consisting of an access key ID and a secret access key, are used to make programmatic calls to AWS services from the AWS Command Line Interface (CLI), AWS SDKs, and other development tools. They serve the same purpose as a username and password for programmatic access, allowing you to authenticate and authorize your requests to AWS APIs without needing to manually enter credentials each time. It is crucial to protect your access keys as you would a password, and follow security best practices such as rotating them regularly and using IAM roles where possible.

**Incorrect:**

**A. MFA** - Multi-Factor Authentication (MFA) is an extra layer of security that requires a user to provide two or more factors to verify their identity. While it enhances security, it is not a direct replacement for a username and password or access keys. MFA is often used in conjunction with passwords or access keys.

**B. Key pairs** - Key pairs are used for securely connecting to Amazon EC2 instances. They consist of a public key that AWS stores and a private key that you store. They are not used for general programmatic access to AWS services like access keys are. Key pairs are specific to EC2 instance authentication.

**C. Instance Password** - An instance password is the password used to log in to the operating system of an EC2 instance. It is not used for authenticating programmatic access to AWS services through the CLI or SDKs. The instance password allows you to access the virtual machine itself, not the AWS APIs.

</details>

---

### Question 102 — `CLF-U0798` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following services can help protect your web applications from SQL injection and other vulnerabilities in your application code?**

- A) Amazon Cognito.
- B) AWS IAM.
- C) Amazon Aurora.
- D) AWS WAF.

<details>
<summary><strong>Reveal Answer & Explanation (Question 102)</strong></summary>

**Correct Answer:** `D`

**Correct answer: AWS WAF**

AWS WAF (Web Application Firewall) is a service that helps protect your web applications from common web exploits and bots that may affect availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web application by defining customizable web security rules. These rules can help protect against attacks such as SQL injection and cross-site scripting (XSS), which exploit vulnerabilities in application code. AWS WAF can be deployed on Amazon CloudFront, Application Load Balancer (ALB), and Amazon API Gateway.

**Incorrect:**

**A. Amazon Cognito** - Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. While it helps secure your application by managing user identities, it doesn't directly protect against application-level vulnerabilities like SQL injection.

**B. Amazon Aurora** - Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. While database security is important, Aurora itself doesn't provide protection against web application vulnerabilities like SQL injection. It's the responsibility of the application and other security services (like WAF) to prevent these attacks.

**C. AWS IAM** - AWS IAM (Identity and Access Management) enables you to manage access to AWS services and resources securely. IAM controls who (authenticated) and what (authorized) have access to AWS resources. While IAM is crucial for overall security, it does not directly protect against application-level attacks such as SQL injection. IAM focuses on controlling access to AWS services, not inspecting web traffic for malicious code.

</details>

---

### Question 103 — `CLF-U0803` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following AWS security features is associated with an EC2 instance and functions to filter incoming traffic requests?**

- A) AWS X-Ray.
- B) Network ACL.
- C) Security Groups.
- D) VPC Flow logs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 103)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Security Groups**

Security Groups act as a virtual firewall for your EC2 instances to control inbound and outbound traffic. You associate a security group with an EC2 instance, and it filters traffic at the instance level. Security groups are stateful, meaning that if you allow inbound traffic on a specific port, the outbound traffic in response to that inbound traffic is automatically allowed, regardless of outbound rules. Security groups operate at the instance level, providing granular control over network access to individual EC2 instances.

**Incorrect:**

**B. Network ACL** - Network Access Control Lists (NACLs) are an optional layer of security that acts as a firewall for controlling traffic in and out of one or more subnets. They operate at the subnet level, not at the instance level like Security Groups.

**C. AWS Systems Manager Session Manager** - AWS Systems Manager Session Manager allows you to manage your EC2 instances through a browser-based interactive shell or through the AWS CLI. It provides secure and auditable instance management without the need to open inbound ports, but it does not function to filter incoming traffic requests.

**D. VPC Flow logs** - VPC Flow Logs enable you to capture information about the IP traffic going to, from, and within your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. While useful for monitoring and security analysis, VPC Flow Logs do not actively filter or control network traffic.

</details>

---

### Question 104 — `CLF-U0808` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**A company uses AWS Organizations to manage all of its AWS accounts. Which of the following allows the company to restrict what services and actions are allowed in each individual account?**

- A) IAM Principals.
- B) AWS Service Control Policies (SCPs).
- C) IAM policies.
- D) AWS Fargate.

<details>
<summary><strong>Reveal Answer & Explanation (Question 104)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS Service Control Policies (SCPs)**

AWS Service Control Policies (SCPs) are a feature of AWS Organizations that allow you to centrally control the AWS services and actions that are allowed in the accounts within your organization. SCPs act as guardrails, defining the maximum permissions available to accounts. Even if an IAM user or role within an account has permissions granted to them, the SCP can restrict those permissions, effectively limiting what actions can be performed. This is crucial for enforcing compliance and security policies across multiple AWS accounts managed under AWS Organizations.

**Incorrect:**

**A. AWS Fargate** - AWS Fargate is a serverless compute engine for containers. It does not provide a mechanism for restricting services and actions within AWS accounts. Fargate is used for running containerized applications without managing servers, and it's unrelated to access control or policy enforcement.

**B. IAM Principals** - IAM principals (users, groups, roles) are identities that can be granted permissions to access AWS resources. While IAM principals are fundamental to AWS security, they are not the mechanism used to centrally restrict services and actions across multiple accounts within AWS Organizations. IAM principals operate within the scope of a single AWS account.

**C. IAM policies** - IAM policies define permissions for IAM principals within a single AWS account. While IAM policies are essential for granting permissions, they do not provide a centralized way to restrict services and actions across multiple accounts in an AWS Organization. SCPs, on the other hand, are specifically designed for this purpose.

</details>

---

### Question 105 — `CLF-U0821` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following are types of AWS Identity and Access Management (IAM) identities? (Choose TWO)**

- A) AWS Resource Groups.
- B) IAM Policies.
- C) IAM Roles.
- D) IAM Users.
- E) AWS Organizations.

<details>
<summary><strong>Reveal Answer & Explanation (Question 105)</strong></summary>

**Correct Answer:** `C, D`

**Correct answer: IAM Roles**

IAM Roles are an IAM identity that you can create in your AWS account. An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Roles are commonly used to grant permissions to applications running on EC2 instances or other AWS services, allowing them to access other AWS resources securely without embedding credentials directly in the application.

**Correct answer: IAM Users**

IAM Users are an IAM identity that represents a person or service that uses AWS. An IAM user consists of a name and credentials. When you first create an IAM user, it has no permissions. You grant permissions to a user by creating policies that specify the actions that the user can perform. IAM users are typically used by individuals who need to access AWS resources directly, such as developers or administrators.

**Incorrect:**

**B. AWS Resource Groups** - AWS Resource Groups allow you to organize your AWS resources, such as EC2 instances or S3 buckets. They are not IAM identities, but rather a way to manage and organize your existing AWS resources.

**C. IAM Policies** - IAM Policies define permissions in AWS and are attached to IAM identities (users, groups, or roles). They are not identities themselves, but rather define what actions an identity is allowed to perform.

**D. AWS Organizations** - AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. While Organizations helps manage accounts and apply policies across them, it is not an IAM identity.

</details>

---

### Question 106 — `CLF-U0824` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**A company is seeking to better secure its AWS account from unauthorized access. Which of the below options can the customer use to achieve this goal?**

- A) Restrict any API call made through SDKs or CLI.
- B) Create one IAM account for each department in the company (Development, QA, Production), and share it across all staff in that department.
- C) Require Multi-Factor Authentication (MFA) for all IAM User access.
- D) Set up two login passwords.

<details>
<summary><strong>Reveal Answer & Explanation (Question 106)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Require Multi-Factor Authentication (MFA) for all IAM User access**

Requiring Multi-Factor Authentication (MFA) for all IAM users is a security best practice that adds an extra layer of protection beyond just a username and password. MFA requires users to provide a second authentication factor, such as a code from a mobile app or a security key, making it significantly harder for unauthorized users to gain access to the AWS account, even if they have the password. This helps to protect the account from unauthorized access and potential security breaches.

**Incorrect:**

**B. Set up two login passwords** - While using a strong password is good practice, simply having two passwords does not provide the same level of security as MFA. If one password is compromised, the account is still vulnerable. MFA requires a separate, time-sensitive factor that is much harder to obtain.

**C. Create one IAM account for each department in the company (Development, QA, Production), and share it across all staff in that department** - Sharing IAM accounts is a very bad security practice. It makes it impossible to track individual user activity, audit logs, and enforce least privilege. If one shared account is compromised, the entire department's access is at risk. Each individual should have their own IAM user.

**D. Restrict any API call made through SDKs or CLI** - Restricting all API calls made through SDKs or CLI would severely limit the functionality of the AWS account and prevent legitimate users and applications from interacting with AWS services. While restricting access based on the principle of least privilege is important, completely blocking SDK and CLI access is not a practical or recommended security measure.

</details>

---

### Question 107 — `CLF-U0831` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**When granting permissions to applications running on Amazon EC2 instances, which of the following is considered best practice?**

- A) Generate new IAM access keys every time you delegate permissions.
- B) Store the required AWS credentials directly within the application code.
- C) Use temporary security credentials (IAM roles) instead of long-term access keys.
- D) Do nothing; Applications that run on Amazon EC2 instances do not need permission to interact with other AWS services or resources.

<details>
<summary><strong>Reveal Answer & Explanation (Question 107)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Use temporary security credentials (IAM roles) instead of long-term access keys**

Using IAM roles to grant permissions to applications running on EC2 instances is a security best practice. IAM roles provide temporary security credentials, which are automatically rotated, eliminating the need to manage long-term access keys directly within the application or on the EC2 instance. This reduces the risk of compromised credentials. When an EC2 instance is launched with an IAM role, any application running on the instance can assume that role and obtain temporary credentials to access AWS resources. This approach adheres to the principle of least privilege and simplifies credential management.

**Incorrect:**

**A. Store the required AWS credentials directly within the application code** - Embedding AWS credentials directly in application code is a major security risk. If the code is compromised or exposed (e.g., through a public code repository), the credentials can be used to gain unauthorized access to your AWS resources.

**B. Generate new IAM access keys every time you delegate permissions** - While generating new access keys isn't inherently wrong, it's not the best practice for EC2 instances. Managing and rotating numerous access keys becomes complex and error-prone. IAM roles provide a more streamlined and secure approach with temporary credentials.

**D. Do nothing; Applications that run on Amazon EC2 instances do not need permission to interact with other AWS services or resources** - Applications often need to interact with other AWS services (e.g., S3, DynamoDB, SQS). If an application requires access to these services, it needs appropriate permissions. Denying all permissions would prevent the application from functioning correctly.

</details>

---

### Question 108 — `CLF-U0053` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**A company is developing a new application using a microservices framework. The new application is having performance and latency issues. Which AWS Service should be used to troubleshoot these issues?**

- A) AWS CodePipeline.
- B) AWS X-Ray.
- C) Amazon Inspector.
- D) AWS CloudTrail.

<details>
<summary><strong>Reveal Answer & Explanation (Question 108)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS X-Ray**

AWS X-Ray helps developers analyze and debug distributed applications, such as those built using a microservices architecture. It provides an end-to-end view of requests as they travel through your application, showing the latency of each component. This allows you to pinpoint performance bottlenecks and troubleshoot latency issues effectively. X-Ray integrates with other AWS services and supports various programming languages and frameworks, making it a powerful tool for optimizing application performance.

**Incorrect:**

**A. AWS CloudTrail** - AWS CloudTrail tracks user activity and API calls within your AWS environment. While useful for auditing and security, it does not provide the detailed performance tracing needed to troubleshoot application latency issues.

**B. AWS CodePipeline** - AWS CodePipeline is a continuous integration and continuous delivery (CI/CD) service. It automates the release process but does not directly address application performance or latency problems.

**C. Amazon Inspector** - Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It focuses on identifying security vulnerabilities, not performance bottlenecks or latency issues.

</details>

---

### Question 109 — `CLF-U0058` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**What is the AWS service that performs automated network assessments of Amazon EC2 instances to check for vulnerabilities?**

- A) Amazon Kinesis.
- B) Security groups.
- C) Amazon Inspector.
- D) AWS Network Access Control Lists.

<details>
<summary><strong>Reveal Answer & Explanation (Question 109)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon Inspector**

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by severity. These findings can be reviewed directly or as part of detailed assessment reports. Amazon Inspector performs network assessments of EC2 instances, checking for vulnerabilities by analyzing network configurations and instance behavior.

**Incorrect:**

**A. Amazon Kinesis** - Amazon Kinesis is a service for collecting, processing, and analyzing real-time, streaming data at scale. It is not used for network assessments or vulnerability scanning of EC2 instances.

**C. Security groups** - Security groups act as virtual firewalls for your EC2 instances, controlling inbound and outbound traffic. While they are a crucial security component, they don't perform automated vulnerability assessments like Amazon Inspector. Security groups define rules, but they don't actively scan for vulnerabilities.

**D. AWS Network Access Control Lists** - Network Access Control Lists (NACLs) are an optional layer of security that act as a firewall for controlling traffic in and out of one or more subnets. Like security groups, they define rules for network traffic but do not perform automated vulnerability assessments.

</details>

---

### Question 110 — `CLF-U0816` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following AWS services can help you perform security analysis and regulatory compliance auditing? (Choose TWO)**

- A) Amazon Inspector.
- B) AWS Virtual Private Gateway.
- C) AWS Batch.
- D) Amazon ECS.
- E) AWS Config.

<details>
<summary><strong>Reveal Answer & Explanation (Question 110)</strong></summary>

**Correct Answer:** `A, E`

**Correct answer: AWS Config**

AWS Config enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine overall compliance against the configurations specified in your internal policies.

**Correct answer: Amazon Inspector**

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of automated assessment reports.

**Incorrect:**

**A. Amazon ECS** - Amazon ECS (Elastic Container Service) is a container orchestration service that allows you to run and manage Docker containers. While security is a consideration when using ECS, ECS itself doesn't directly perform security analysis or regulatory compliance auditing. You would use other services, like Inspector or Config, to assess the security of applications running on ECS.

**B. AWS Batch** - AWS Batch enables you to run batch computing workloads on the AWS Cloud. It dynamically provisions compute resources and manages job execution. While security is important for batch processing, AWS Batch itself does not provide security analysis or regulatory compliance auditing capabilities.

**D. AWS Virtual Private Gateway** - An AWS Virtual Private Gateway is used to create VPN connections between your VPC and your on-premises network. While it provides secure connectivity, it does not perform security analysis or regulatory compliance auditing. Its primary function is to establish a secure tunnel for network traffic.

</details>

---

### Question 111 — `CLF-U0867` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which security service automatically recognizes and classifies sensitive data or intellectual property on AWS?**

- A) Amazon GuardDuty.
- B) Amazon Macie.
- C) Amazon Inspector.
- D) AWS Shield.

<details>
<summary><strong>Reveal Answer & Explanation (Question 111)</strong></summary>

**Correct Answer:** `B`

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data such as personally identifiable information and intellectual property stored in Amazon S3, making it the correct service for automatically recognizing and classifying sensitive data.
Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and focuses on detecting security threats rather than classifying data. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not classify or discover sensitive data stored in S3. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to recognize or classify sensitive data.

</details>

---

### Question 112 — `CLF-U0884` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which AWS service is used to track record, and audit configuration changes made to AWS resources?**

- A) AWS Shield.
- B) AWS Config.
- C) AWS IAM.
- D) Amazon Inspector.

<details>
<summary><strong>Reveal Answer & Explanation (Question 112)</strong></summary>

**Correct Answer:** `B`

AWS Config continuously records configuration changes to AWS resources and maintains a history of those changes, enabling audit and compliance reviews of how resources have been configured over time.
AWS Shield is a managed DDoS protection service that safeguards AWS applications against distributed denial-of-service attacks, and has no capability to track or audit resource configuration changes. AWS Identity and Access Management (IAM) is a service for controlling who can authenticate and what actions they are authorised to perform, and manages permissions and identities rather than recording configuration changes to AWS resources. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security testing tool rather than a configuration change tracking or auditing service.

</details>

---

### Question 113 — `CLF-U0890` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which AWS security service protects applications from distributed denial of service attacks with always-on detection and automatic inline mitigations?**

- A) Amazon Inspector.
- B) AWS Web Application Firewall (AWS WAF).
- C) Elastic Load Balancing (ELB).
- D) AWS Shield.

<details>
<summary><strong>Reveal Answer & Explanation (Question 113)</strong></summary>

**Correct Answer:** `D`

AWS Shield provides always-on DDoS protection at no extra cost for all AWS customers, automatically detecting and mitigating the most common volumetric and protocol-based DDoS attacks without any customer configuration.
AWS WAF is a web application firewall that filters application-layer HTTP and HTTPS traffic based on configurable rules, and while it helps mitigate application-layer attacks, it is a separate service from Shield and requires customer configuration rather than providing automatic always-on protection. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts, and is an alerting and detection service rather than a service that actively blocks DDoS traffic. AWS CloudTrail records API calls and management events for auditing and compliance purposes, and has no capability to detect or protect against distributed denial of service attacks.

</details>

---

### Question 114 — `CLF-U0071` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**Which AWS Service can be used to register a new domain name?**

- A) Amazon Personalize.
- B) Amazon Route 53.
- C) AWS KMS.
- D) AWS Config.

<details>
<summary><strong>Reveal Answer & Explanation (Question 114)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Amazon Route 53**

Amazon Route 53 is a scalable and highly available Domain Name System (DNS) web service. One of its core functionalities is domain registration. You can use Route 53 to purchase and manage domain names, configure DNS settings, and route internet traffic to your applications. Route 53 translates domain names into IP addresses, which computers use to connect to each other. It supports various DNS record types, including A, AAAA, CNAME, MX, and TXT records, allowing for flexible configuration of your domain.

**Incorrect:**

**A. Amazon Personalize** - Amazon Personalize is a machine learning service that enables you to create individualized recommendations for your customers. It is not related to domain name registration.

**B. AWS Config** - AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. It helps with compliance and security by tracking resource configurations and changes over time. It does not handle domain name registration.

**C. AWS KMS** - AWS KMS (Key Management Service) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. It is used for managing cryptographic keys and has nothing to do with domain registration.

</details>

---

### Question 115 — `CLF-U0822` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**How does AWS notify customers about security and privacy events pertaining to AWS services?**

- A) Using the AWS ACM service.
- B) Using Security Bulletins.
- C) Using the AWS Management Console.
- D) Using Compliance Resources.

<details>
<summary><strong>Reveal Answer & Explanation (Question 115)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Using Security Bulletins**

AWS uses Security Bulletins to notify customers about security and privacy events related to AWS services. These bulletins provide details about vulnerabilities, potential impacts, and remediation steps. They are a primary channel for communicating important security-related information to AWS customers, ensuring they are informed and can take appropriate action to protect their AWS environments. These bulletins are typically published on the AWS Security Blog and other official AWS communication channels.

**Incorrect:**

**A. Using the AWS Management Console** - While the AWS Management Console provides access to security-related services and configurations, it is not the primary mechanism for proactively notifying customers about security and privacy events. The console is more for managing and monitoring security settings rather than receiving direct notifications of incidents.

**C. Using the AWS ACM service** - AWS Certificate Manager (ACM) is a service for provisioning, managing, and deploying SSL/TLS certificates for use with AWS services. It is not used for general security and privacy event notifications. ACM focuses on certificate management, not broader security alerts.

**D. Using Compliance Resources** - Compliance Resources, such as AWS Artifact, provide access to compliance reports and documentation. While compliance is related to security, these resources are not the primary channel for notifying customers about specific security and privacy events. They are more about demonstrating AWS's compliance with various standards and regulations.

</details>

---

### Question 116 — `CLF-U0022` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**You have deployed your application on multiple Amazon EC2 instances. Your customers complain that sometimes they can’t reach your application. Which AWS service allows you to monitor the performance of your EC2 instances to assist in troubleshooting these issues?**

- A) AWS Lambda.
- B) AWS Config.
- C) Amazon CloudWatch.
- D) AWS CloudTrail.

<details>
<summary><strong>Reveal Answer & Explanation (Question 116)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon CloudWatch**

Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights to monitor your applications, respond to system-wide performance changes, and optimize resource utilization. It collects metrics and logs from AWS services, including EC2 instances, and allows you to set alarms based on these metrics. This makes it ideal for troubleshooting performance issues and identifying the root cause of unavailability.

**Incorrect:**

**A. AWS Config** - AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. While it's useful for compliance and governance, it doesn't directly monitor the real-time performance of EC2 instances in the way CloudWatch does. Config focuses on configuration changes, not performance metrics.

**B. AWS CloudTrail** - AWS CloudTrail records API calls made within your AWS account. It's useful for auditing and security analysis, as it tracks who did what and when. However, it doesn't provide real-time performance monitoring of EC2 instances. CloudTrail logs actions, not performance metrics.

**C. AWS Lambda** - AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. While Lambda functions can be used for monitoring tasks, Lambda itself is not a monitoring service for EC2 instances. It's a compute service, not a monitoring tool.

</details>

---

### Question 117 — `CLF-U0067` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**A customer spent a lot of time configuring a newly deployed Amazon EC2 instance. After the workload increases, the customer decides to provision another EC2 instance with an identical configuration. How can the customer achieve this?**

- A) By creating an AWS Config template from the old instance and launching a new instance from it.
- B) By creating an EBS Snapshot of the old instance.
- C) By installing Aurora on EC2 and launching a new instance from it.
- D) By creating an AMI from the old instance and launching a new instance from it.

<details>
<summary><strong>Reveal Answer & Explanation (Question 117)</strong></summary>

**Correct Answer:** `D`

**Correct answer: By creating an AMI from the old instance and launching a new instance from it**

An Amazon Machine Image (AMI) provides the information required to launch an instance, which is a virtual server in the cloud. You specify an AMI when you launch an instance, and you can launch multiple instances from a single AMI when you need multiple instances with the same configuration. AMIs include: a template for the root volume for the instance (for example, an operating system, an application server, and applications), launch permissions that control which AWS accounts can use the AMI to launch instances, and a block device mapping that specifies the volumes to attach to the instance when it's launched. Creating an AMI from the configured EC2 instance captures its exact state, including the OS, installed software, and configurations. Launching a new instance from this AMI will result in an identical copy of the original instance.

**Incorrect:**

**A. By installing Aurora on EC2 and launching a new instance from it** - Amazon Aurora is a MySQL and PostgreSQL-compatible relational database engine. Installing Aurora on an EC2 instance doesn't create a template or image of the instance's configuration that can be used to launch identical instances. Aurora is for database services, not instance replication.

**B. By creating an EBS Snapshot of the old instance** - An EBS snapshot is a point-in-time copy of an EBS volume. While you can create a volume from a snapshot and attach it to a new EC2 instance, this only copies the data on the volume. It doesn't capture the entire configuration of the original EC2 instance, such as instance type, security groups, or IAM role. You would still need to configure the new instance separately.

**C. By creating an AWS Config template from the old instance and launching a new instance from it** - AWS Config can be used to assess, audit, and evaluate the configurations of your AWS resources. While AWS Config can help you track configuration changes and ensure compliance, it doesn't directly create a template that can be used to launch a new EC2 instance with an identical configuration. AWS Config focuses on configuration management and compliance, not instance replication.

</details>

---

### Question 118 — `CLF-U0203` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which mechanism allows developers to access AWS services from application code?**

- A) AWS Software Development Kit.
- B) AWS Management Console.
- C) AWS CodePipeline.
- D) AWS Config.

<details>
<summary><strong>Reveal Answer & Explanation (Question 118)</strong></summary>

**Correct Answer:** `A`

**Correct Answer: A** (**A** (AWS Software Development Kit.))

> **Domain Focus:** Security and Compliance | **Blueprint Area:** Topic 2.5: Compliance, Auditing & Artifact

### 💡 Architectural Rationale & Why It Is Correct:
Under AWS Well-Architected principles and official CLF-C02 specifications for `point:comp_config_resource_rules`: **A** (AWS Software Development Kit.) directly satisfies the requirements stated in the scenario.
In production AWS environments, this architectural pattern ensures compliance, maximum operational efficiency, and least-privilege alignment.

### 🔍 Detailed Option Breakdown & Distractor Analysis:
- **Option A (AWS Software Development Kit.)** ✅ **[CORRECT]**: Directly addresses the operational and governance goals of this scenario under the AWS Shared Responsibility and service boundary model.
- **Option B (AWS Management Console.)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).
- **Option C (AWS CodePipeline.)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).
- **Option D (AWS Config.)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).

### ⚠️ Exam Trap & Heuristic Decryption:
Watch out for distractors testing similar AWS service boundaries. When the question asks for `Compliance, Auditing & Artifact`, prioritize native managed AWS services over manual or third-party administration.

</details>

---

### Question 119 — `CLF-U0585` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**How can AWS customers track and avoid over-spending on underutilized reserved instances?**

- A) Customers can add all AWS accounts to an AWS Organization, enable Consolidated Billing, and turn off Reserved Instance sharing.
- B) Customers can use Amazon Neptune to track and analyze their usage patterns, detect underutilized reserved instances, and then sell them on the Amazon EC2 Reserved Instance Marketplace.
- C) Customers can use the AWS Budgets service to track the reserved instances usage and set up alert notifications when their utilization drops below the threshold that they define.
- D) Customers can use Amazon CloudTrail to automatically check for unused reservations and get recommendations to reduce their bill.

<details>
<summary><strong>Reveal Answer & Explanation (Question 119)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Customers can use the AWS Budgets service to track the reserved instances usage and set up alert notifications when their utilization drops below the threshold that they define**

AWS Budgets allows you to set custom budgets that track your AWS usage, including Reserved Instance (RI) utilization. You can configure alerts to notify you when your RI utilization falls below a defined threshold, enabling you to take action to improve utilization and avoid overspending. This proactive approach helps optimize costs and ensure you're getting the most value from your RI commitments.

**Incorrect:**

**A. Customers can use Amazon Neptune to track and analyze their usage patterns, detect underutilized reserved instances, and then sell them on the Amazon EC2 Reserved Instance Marketplace** - Amazon Neptune is a graph database service and is not designed for tracking RI utilization or managing RI sales. While you *can* sell unused RIs on the EC2 Reserved Instance Marketplace, Neptune is not the tool for tracking utilization and identifying RIs to sell.

**C. Customers can add all AWS accounts to an AWS Organization, enable Consolidated Billing, and turn off Reserved Instance sharing** - While AWS Organizations with Consolidated Billing provides cost visibility across multiple accounts, and turning off RI sharing *could* help isolate usage, this approach doesn't directly track RI utilization or provide alerts for underutilization. It's more about overall cost management than specific RI tracking. You still need a mechanism to monitor RI usage within each account. 

**D. Customers can use Amazon CloudTrail to automatically check for unused reservations and get recommendations to reduce their bill** - Amazon CloudTrail tracks API calls and events within your AWS account for auditing and security purposes. While CloudTrail provides valuable information about your AWS environment, it doesn't directly analyze RI utilization or provide recommendations for cost optimization related to RIs. It's not designed for cost management in the way AWS Budgets or Cost Explorer is.

</details>

---

### Question 120 — `CLF-U0590` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**As part of the AWS Migration Acceleration Program (MAP), what does AWS provide to accelerate Enterprise adoption of AWS? (Choose TWO)**

- A) AWS Partners.
- B) AWS Artifact.
- C) AWS Professional Services.
- D) Amazon Athena.
- E) Amazon PinPoint.

<details>
<summary><strong>Reveal Answer & Explanation (Question 120)</strong></summary>

**Correct Answer:** `A, C`

**Correct answer: AWS Partners**

AWS Partners are a crucial component of the AWS Migration Acceleration Program (MAP). They provide expertise, tools, and services to help enterprises migrate to AWS. These partners have demonstrated experience in various aspects of migration, such as assessment, planning, execution, and optimization. Leveraging AWS Partners allows enterprises to accelerate their cloud adoption journey by tapping into specialized skills and proven methodologies.

**Correct answer: AWS Professional Services**

AWS Professional Services is a team of AWS experts that works directly with enterprises to provide guidance and support throughout their cloud migration journey. They offer a range of services, including strategic planning, architecture design, implementation, and operational support. AWS Professional Services helps enterprises overcome challenges, mitigate risks, and accelerate the adoption of AWS by providing deep technical expertise and best practices.

**Incorrect:**

**A. Amazon Athena** - Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. While Athena can be used in a migration scenario for data analysis, it is not a core component of the AWS Migration Acceleration Program (MAP) in terms of providing direct assistance or resources to accelerate enterprise adoption.

**C. Amazon PinPoint** - Amazon Pinpoint is a flexible and scalable outbound and inbound marketing communications service. It is used for engaging with customers through various channels. While Pinpoint might be relevant for some applications after a migration, it is not directly related to accelerating the migration process itself within the AWS MAP program.

**E. AWS Artifact** - AWS Artifact is a service that provides on-demand access to AWS security and compliance reports and agreements. While compliance is important during a migration, AWS Artifact itself doesn't directly accelerate the migration process in the same way that partners or professional services do.

</details>

---

### Question 121 — `CLF-U0801` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**What are the change management tools that helps AWS customers audit and monitor all resource changes in their AWS environment? (Choose TWO)**

- A) AWS CloudTrail.
- B) Amazon Comprehend.
- C) AWS Transit Gateway.
- D) AWS X-Ray.
- E) AWS Config.

<details>
<summary><strong>Reveal Answer & Explanation (Question 121)</strong></summary>

**Correct Answer:** `A, E`

**Correct answer: AWS Config**

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your compliance against internal policies and regulatory standards.

**Correct answer: AWS CloudTrail**

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail logs API calls made on or behalf of your AWS account, including calls made by the AWS Management Console, command line tools, and other AWS services. This allows you to track user activity and resource changes within your AWS environment, providing a detailed audit trail for security analysis and compliance purposes.

**Incorrect:**

**A. Amazon Comprehend** - Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. It is not a change management or auditing tool.

**B. AWS Transit Gateway** - AWS Transit Gateway is a network transit hub that you can use to interconnect your virtual private clouds (VPCs) and on-premises networks. While it plays a role in network architecture and connectivity, it does not directly provide change management or auditing capabilities for resource configurations.

**C. AWS X-Ray** - AWS X-Ray helps developers analyze and debug distributed applications, such as those built using a microservices architecture. X-Ray provides an end-to-end view of requests as they travel through your application, and shows a map of your application's underlying components. It is not a change management or auditing tool.

</details>

---

### Question 122 — `CLF-U0811` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**A company needs to track resource changes using the API call history. Which AWS service can help the company achieve this goal?**

- A) AWS Config.
- B) Amazon CloudWatch.
- C) AWS CloudTrail.
- D) AWS CloudFormation.

<details>
<summary><strong>Reveal Answer & Explanation (Question 122)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS CloudTrail**

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services' APIs. This allows you to track resource changes by logging API calls made on your AWS resources. CloudTrail logs can be stored in Amazon S3 for long-term retention and analysis.

**Incorrect:**

**A. AWS Config** - AWS Config tracks the configuration of your AWS resources and can notify you of changes. While it does track changes, it focuses on the configuration state of resources, not the API calls that initiated those changes. CloudTrail is specifically designed for tracking API call history.

**B. Amazon CloudWatch** - Amazon CloudWatch is a monitoring and observability service. It collects metrics and logs, and can set alarms. While CloudWatch can monitor API calls, it's not primarily designed for tracking the history of API calls for auditing and compliance purposes. CloudTrail is the dedicated service for this.

**D. AWS CloudFormation** - AWS CloudFormation is an Infrastructure as Code (IaC) service that allows you to define and provision AWS infrastructure. While CloudFormation templates define the desired state of resources, it doesn't track the history of API calls made to create or modify those resources. CloudTrail is the service that provides this API call history.

</details>

---

### Question 123 — `CLF-U0814` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**A company has discovered that multiple S3 buckets were deleted, but it is unclear who deleted the buckets. Which of the following can the company use to determine the identity that deleted the buckets?**

- A) SNS logs.
- B) SQS logs.
- C) CloudWatch Logs.
- D) CloudTrail logs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 123)</strong></summary>

**Correct Answer:** `D`

**Correct answer: CloudTrail logs**

CloudTrail is an AWS service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail logs API calls made to AWS services, including S3. By enabling CloudTrail, the company can track which IAM user or role made the API calls to delete the S3 buckets, providing the identity of the user who performed the action. CloudTrail provides detailed information about each API call, including the caller's identity, the time of the call, the source IP address, and the parameters used in the call. This information is crucial for security investigations and compliance audits.

**Incorrect:**

**A. SNS logs** - SNS (Simple Notification Service) is a messaging service for sending notifications. It does not log API calls or user actions related to S3 bucket deletions. SNS is used for sending alerts or messages based on events, but it doesn't provide an audit trail of actions performed in the AWS environment.

**B. SQS logs** - SQS (Simple Queue Service) is a message queuing service. Similar to SNS, it doesn't log API calls or user actions. SQS is used for decoupling and scaling microservices, distributed systems, and serverless applications, but it is not an auditing tool.

**D. CloudWatch Logs** - CloudWatch Logs is a service for monitoring, storing, and accessing log files from various AWS services and applications. While CloudWatch Logs can collect logs from various sources, it doesn't automatically capture API calls related to S3 bucket deletions unless specifically configured to do so through other services like CloudTrail. CloudTrail is the dedicated service for logging API activity.

</details>

---

### Question 124 — `CLF-U0962` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which AWS service gives users on-demand, self-service access to AWS compliance control reports?**

- A) AWS Config
- B) Amazon GuardDuty
- C) AWS Trusted Advisor
- D) AWS Artifact

<details>
<summary><strong>Reveal Answer & Explanation (Question 124)</strong></summary>

**Correct Answer:** `D`

AWS Artifact provides on-demand, self-service access to AWS compliance control reports including SOC, PCI, ISO, and HIPAA documentation directly from the AWS Management Console without requiring a request through AWS Support.
AWS Config tracks the configuration state of resources and audits how those configurations change over time, and is a resource configuration auditing service rather than a portal for downloading compliance control reports. Amazon GuardDuty is a threat detection service that uses machine learning to monitor accounts and workloads for malicious activity, and is security focused rather than a compliance documentation portal. AWS Trusted Advisor inspects an account and provides best practice recommendations across cost optimization, performance, security, fault tolerance, and service limits, and is an advisory tool rather than a source of compliance control reports.

</details>

---

### Question 125 — `CLF-U0151` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following can help secure your sensitive data in Amazon S3? (Choose TWO)**

- A) Delete the encryption keys once your data is encrypted.
- B) With AWS you do not need to worry about encryption.
- C) Enable S3 Encryption.
- D) Encrypt the data prior to uploading it.
- E) Delete all IAM users that have access to S3.

<details>
<summary><strong>Reveal Answer & Explanation (Question 125)</strong></summary>

**Correct Answer:** `C, D`

Enabling S3 encryption through server-side encryption with S3-managed keys, KMS keys, or customer-provided keys protects object confidentiality at rest, and encrypting data before uploading it provides client-side encryption that ensures data is protected before it ever leaves the client. Both are valid approaches to securing sensitive data in Amazon S3.
Deleting encryption keys once data is encrypted would permanently prevent decryption of the stored data, making it impossible to read or use the data again; encryption keys must be retained and managed carefully to ensure continued access to encrypted data. AWS does not automatically handle all security concerns by default; customers are responsible for configuring appropriate encryption, access controls, and bucket policies to protect their data, as the shared responsibility model requires active customer participation in data security. Deleting all IAM users with access to S3 would prevent all legitimate users from accessing the data and disrupt normal operations; proper access control involves granting least privilege permissions to the appropriate users rather than eliminating all access.

</details>

---

### Question 126 — `CLF-U0834` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which of the following strategies helps protect your AWS root account?**

- A) Delete root user access keys if you do not need them.
- B) Apply MFA for the root account and use it for all of your work.
- C) Access the root account only from your personal Mobile Phone.
- D) Only share your AWS account password or access keys with trusted persons.

<details>
<summary><strong>Reveal Answer & Explanation (Question 126)</strong></summary>

**Correct Answer:** `A`

Deleting root user access keys removes a persistent attack vector, since the root account has unrestricted access to all AWS services and resources, and AWS best practice recommends using IAM users for daily tasks and eliminating root access keys entirely to protect the account.
Applying MFA for the root account is correct but the second part of the option is wrong; AWS recommends enabling MFA on the root account but using it as infrequently as possible and relying on IAM users for day-to-day work, not using the root account for all tasks. Accessing the root account only from a personal mobile phone does not constitute a recognized security control; MFA using an authenticator app on a mobile device is recommended, but restricting access to a specific physical device is not an AWS security best practice and introduces its own risks. Sharing your AWS account password or access keys with trusted persons violates fundamental security principles; credentials should never be shared as this removes individual accountability and increases the risk of credential exposure.

</details>

---

### Question 127 — `CLF-U0835` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**You have just set up your AWS environment and have created six IAM user accounts for the DevOps team. What is the AWS recommendation when granting permissions to these IAM accounts?**

- A) Attach a separate IAM policy for each individual account.
- B) Apply the Principle of Least Privilege.
- C) For security purposes, you should not grant any permission to the DevOps team.
- D) Create six different IAM passwords.

<details>
<summary><strong>Reveal Answer & Explanation (Question 127)</strong></summary>

**Correct Answer:** `B`

The Principle of Least Privilege means granting each IAM user only the minimum permissions necessary to perform their assigned job functions, reducing the impact of any accidental or malicious use of credentials.
Attaching a separate IAM policy to each individual account is a valid approach for highly differentiated permissions but is operationally complex; using IAM groups to assign shared policies to all DevOps team members with similar roles is the recommended approach for teams rather than managing policies per user individually. For security purposes, you should not withhold all permissions from the DevOps team; the team needs appropriate permissions to perform their infrastructure management tasks, and the goal is to define those permissions carefully rather than provide none at all. Creating six different IAM passwords involves setting distinct password requirements per user, but password variation does not address the core security concern of permission scope; applying least privilege principles to what each user is allowed to do is the AWS recommendation.

</details>

---

### Question 128 — `CLF-U0883` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**How can a customer increase security to AWS account logons? (Select TWO)**

- A) Configure AWS Certificate Manager
- B) Enable Multi-Factor Authentication (MFA)
- C) Use Amazon Cognito to manage access
- D) Configure a strong password policy
- E) Enable AWS Organizations

<details>
<summary><strong>Reveal Answer & Explanation (Question 128)</strong></summary>

**Correct Answer:** `B, D`

Correct answer: Enable Multi-Factor Authentication (MFA); Configure a strong password policy. Multi-factor authentication — requires a second factor in addition to the password, and is the single highest-value control to apply to the root user. - Your root account should always be protected by Multi-Factor Authentication (MFA). - This additional layer of security helps protect against unauthorized logins to your account by requiring two factors: something you know (a password) and something you have (for example, an MFA device). - AWS supports virtual and hardware MFA devices and U2F security keys. - Cognito can be used as an Identity Provider (IdP), where it stores and maintains users and credentials securely for your applications, or it can be integrated with OpenID Connect, SAML, and other popular web identity providers like Amazon.com. - Using Amazon Cognito, you can generate temporary access credentials for your clients to access AWS services, eliminating the need to store long-term credentials in client applications. This item belongs to the Security and Compliance domain, under Identity and access.

</details>

---

### Question 129 — `CLF-U1394` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which AWS service or tool can be used to consolidate payments for a company with multiple AWS accounts?**

- A) AWS Cost and Usage Report
- B) AWS Organizations
- C) AWS Cost Explorer
- D) AWS Budgets

<details>
<summary><strong>Reveal Answer & Explanation (Question 129)</strong></summary>

**Correct Answer:** `B`

**Correct Answer: B** (**B** (AWS Organizations))

> **Domain Focus:** Security and Compliance | **Blueprint Area:** Topic 2.2: IAM, Identity & Access Governance

### 💡 Architectural Rationale & Why It Is Correct:
Under AWS Well-Architected principles and official CLF-C02 specifications for `point:orgs_service_control_policies`: **B** (AWS Organizations) directly satisfies the requirements stated in the scenario.
In production AWS environments, this architectural pattern ensures compliance, maximum operational efficiency, and least-privilege alignment.

### 🔍 Detailed Option Breakdown & Distractor Analysis:
- **Option A (AWS Cost and Usage Report)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).
- **Option B (AWS Organizations)** ✅ **[CORRECT]**: Directly addresses the operational and governance goals of this scenario under the AWS Shared Responsibility and service boundary model.
- **Option C (AWS Cost Explorer)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).
- **Option D (AWS Budgets)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).

### ⚠️ Exam Trap & Heuristic Decryption:
Watch out for distractors testing similar AWS service boundaries. When the question asks for `IAM, Identity & Access Governance`, prioritize native managed AWS services over manual or third-party administration.

</details>

---

### Question 130 — `CLF-U2486` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.2: IAM, Identity & Access Governance*

**Which actions are best practices for an AWS account root user? (Choose two.)**

- A) Share root user credentials with team members.
- B) Create multiple root users for the account, separated by environment.
- C) Enable multi-factor authentication (MFA) on the root user.
- D) Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.
- E) Use programmatic access instead of the root user and password.

<details>
<summary><strong>Reveal Answer & Explanation (Question 130)</strong></summary>

**Correct Answer:** `CD`

**Correct Answer: CD (Enable multi-factor authentication (MFA) on the root user., Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.)**

This question (# 148) is directly sourced from authentic **Community Consensus Pool** community discussions.
**Why this is correct:** The scenario specifically tests AWS best practices. 'Enable multi-factor authentication (MFA) on the root user., Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.' directly satisfies the architectural requirement defined in the prompt.

**Key Option Breakdown:**
- **Option A (Share root user credentials with team members.)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option B (Create multiple root users for the account, separated by environment.)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option C (Enable multi-factor authentication (MFA) on the root user.)** [CORRECT]: Satisfies the prompt requirements directly.
- **Option D (Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.)** [CORRECT]: Satisfies the prompt requirements directly.
- **Option E (Use programmatic access instead of the root user and password.)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.

</details>

---

### Question 131 — `CLF-U0158` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Your web application currently faces performance issues and suffers from long load times. Which of the following AWS services could help fix these issues and improve performance?**

- A) Amazon Detective.
- B) AWS X-Ray.
- C) AWS Security Hub.
- D) AWS Shield.

<details>
<summary><strong>Reveal Answer & Explanation (Question 131)</strong></summary>

**Correct Answer:** `B`

AWS X-Ray traces requests as they travel through your application, identifying performance bottlenecks and helping you pinpoint the root cause of long load times and latency issues.
Amazon Detective is a security investigation service that analyzes and visualises data from AWS logs to help identify the root cause of security findings and suspicious activity, and has no capability to diagnose application performance issues or load times. AWS Security Hub aggregates and prioritizes security findings from multiple AWS services and third-party tools into a centralized dashboard, and is a security posture management tool rather than an application performance diagnostics service. AWS Shield is a managed DDoS protection service that safeguards applications against distributed denial-of-service attacks, and does not address application performance bottlenecks or load time issues.

</details>

---

### Question 132 — `CLF-U0165` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following services allows you to install and run custom relational database software?**

- A) Amazon EC2.
- B) Amazon Cognito.
- C) Amazon RDS.
- D) Amazon Inspector.

<details>
<summary><strong>Reveal Answer & Explanation (Question 132)</strong></summary>

**Correct Answer:** `A`

Amazon EC2 provides virtual servers with full operating system-level access, allowing you to install and run any custom database software of your choice on the underlying instance.
Amazon Cognito is a user identity and authentication service for web and mobile applications that manages user sign-up, sign-in, and access control, and has no capability to host or run database software. Amazon RDS is a managed relational database service that supports specific pre-configured database engines such as MySQL, PostgreSQL, and SQL Server, and does not allow you to install or run custom database software outside of those supported engines. Amazon Inspector is an automated security assessment service that scans AWS workloads for software vulnerabilities and unintended network exposure, and has no role in hosting or running database software.

</details>

---

### Question 133 — `CLF-U0188` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following AWS services integrates with AWS Shield and AWS Web Application Firewall (AWS WAF) to protect against network and application layer DDoS attacks?**

- A) Amazon EFS.
- B) AWS Secrets Manager.
- C) AWS Systems Manager.
- D) Amazon CloudFront.

<details>
<summary><strong>Reveal Answer & Explanation (Question 133)</strong></summary>

**Correct Answer:** `D`

Amazon CloudFront integrates natively with AWS Shield for DDoS protection at the network layer and with AWS WAF for application-layer traffic filtering, providing a layered defense against both network and application layer DDoS attacks at the edge.
Amazon EFS is a fully managed elastic file system for providing shared file storage to EC2 instances and other compute services, and is a storage service with no capability to integrate with Shield or WAF for DDoS protection. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service rather than a service that integrates with Shield and WAF for traffic protection. AWS Systems Manager provides operational tools for managing AWS resources at scale including patching, configuration management, and session management, and is an operations service rather than a content delivery or traffic filtering service.

</details>

---

### Question 134 — `CLF-U0194` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following steps should be taken by a customer when conducting penetration testing on AWS?**

- A) Conduct penetration testing using Amazon Inspector, and then notify AWS support.
- B) Request and wait for approval from the customer’s internal security team, and then conduct testing.
- C) Notify AWS support, and then conduct testing immediately.
- D) Request and wait for approval from AWS support, and then conduct testing.

<details>
<summary><strong>Reveal Answer & Explanation (Question 134)</strong></summary>

**Correct Answer:** `D`

Since 2019, AWS allows customers to perform penetration testing on permitted services including EC2, RDS, CloudFront, and API Gateway without prior AWS approval, so customers should follow their own internal security review and authorisation process before conducting tests.
Amazon Inspector is an automated vulnerability assessment service that scans for known vulnerabilities and network misconfigurations, but it is not a penetration testing tool and using it does not substitute for or require notification to AWS support before conducting actual penetration testing. AWS no longer requires customers to notify AWS support before conducting penetration testing on permitted services; the policy changed to allow testing without prior approval, so notifying and then conducting testing immediately is based on an outdated requirement. Requesting and waiting for approval from AWS support before conducting penetration testing is no longer required for permitted services; AWS updated its policy to allow customers to test their own resources without prior approval, removing the requirement for a formal approval process.

</details>

---

### Question 135 — `CLF-U0204` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**What is Amazon CloudWatch?**

- A) A code repository with customizable build and team commit features.
- B) A metrics repository with customizable notification thresholds and channels.
- C) A security configuration repository with threat analytics.
- D) A rule repository of a web application firewall with automated vulnerability prevention features.

<details>
<summary><strong>Reveal Answer & Explanation (Question 135)</strong></summary>

**Correct Answer:** `B`

Amazon CloudWatch is a monitoring service that acts as a metrics repository, collecting performance and operational data from AWS resources and allowing you to set customizable notification thresholds and alarm channels.
AWS CloudTrail records all API calls and account activity across an AWS environment and produces audit logs for governance and compliance purposes, but does not collect resource performance metrics or send operational alarms. AWS X-Ray traces requests as they travel through distributed application components to identify performance bottlenecks and errors, but is an application debugging tool rather than an infrastructure-wide metrics and alerting service. Amazon Kinesis captures and processes real-time data streams from applications and infrastructure at scale, but is a data streaming and ingestion service rather than a monitoring and observability platform.

</details>

---

### Question 136 — `CLF-U0572` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**A company has moved to AWS recently. Which of the following AWS Services will help ensure that they have the proper security settings? (Choose TWO)**

- A) AWS Trusted Advisor.
- B) Amazon Inspector.
- C) Amazon SNS.
- D) Amazon CloudWatch.
- E) Concierge Support Team.

<details>
<summary><strong>Reveal Answer & Explanation (Question 136)</strong></summary>

**Correct Answer:** `A, B`

AWS Trusted Advisor provides automated security checks identifying vulnerabilities such as unrestricted security group access and missing MFA, and Amazon Inspector performs automated security assessments of EC2 instances to identify vulnerabilities and unintended network access. Both help ensure proper security settings.
Amazon SNS is a fully managed publish/subscribe messaging service for sending notifications to subscribers, and does not evaluate or ensure AWS security settings or configurations. Amazon CloudWatch monitors operational metrics and logs for observability and alerting, and while it can trigger notifications on specific metrics or log patterns, it does not actively assess or validate AWS resource security configurations. The Concierge Support Team assists Enterprise support plan customers with billing and account management, and does not perform technical security assessments or review resource security settings.

</details>

---

### Question 137 — `CLF-U0611` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following strategies help analyze costs in AWS?**

- A) Using tags to group resources.
- B) Using AWS CloudFormation to automate the deployment of resources.
- C) Deploying resources of the same type in different regions.
- D) Configuring Amazon Inspector to automatically analyze costs and email reports.

<details>
<summary><strong>Reveal Answer & Explanation (Question 137)</strong></summary>

**Correct Answer:** `A`

Using tags to group and label AWS resources by project, department, or environment enables detailed cost analysis and allocation through AWS Cost Explorer and Cost and Usage Reports.
Using AWS CloudFormation to automate the deployment of resources improves operational efficiency and repeatability, but automating deployments does not itself provide visibility into how costs are distributed across different parts of the organization. Deploying resources of the same type in different regions may be necessary for latency or compliance reasons, but distributing resources geographically does not help analyze which projects or teams are driving specific costs without tags to identify resource ownership. Configuring Amazon Inspector to automatically analyze costs is incorrect because Amazon Inspector is an automated security assessment service that scans for software vulnerabilities and unintended network exposure, and has no capability to analyze AWS costs or generate billing reports.

</details>

---

### Question 138 — `CLF-U0630` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which AWS service identifies security groups that allow unrestricted access to a user’s AWS resources?**

- A) AWS Trusted Advisor.
- B) Amazon Inspector.
- C) Amazon CloudWatch.
- D) AWS CloudTrail.

<details>
<summary><strong>Reveal Answer & Explanation (Question 138)</strong></summary>

**Correct Answer:** `A`

AWS Trusted Advisor checks your security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports such as SSH and RDP, flagging potential security risks in its Security category checks.
Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and while it identifies network reachability issues, the simplest tool for checking security groups for unrestricted access is Trusted Advisor. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability service rather than a tool that audits security group configurations for overly permissive rules. AWS CloudTrail records all API calls and management events for auditing, capturing who created or modified security group rules and when, but it records actions after the fact rather than proactively identifying groups with unrestricted access.

</details>

---

### Question 139 — `CLF-U0787` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**You have noticed that several critical Amazon EC2 instances have been terminated. Which of the following AWS services would help you determine who took this action?**

- A) Amazon Inspector.
- B) AWS CloudTrail.
- C) AWS Trusted Advisor.
- D) EC2 Instance Usage Report.

<details>
<summary><strong>Reveal Answer & Explanation (Question 139)</strong></summary>

**Correct Answer:** `B`

AWS CloudTrail records all API calls and account activity across an AWS environment, capturing who performed each action, from which IP address, and at what time, making it the definitive source for identifying who terminated EC2 instances.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not record who performed API actions or management events. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool rather than an audit log of account activity. EC2 Instance Usage Report provides billing and usage data about EC2 instances and does not contain API call logs or identity information about who terminated instances.

</details>

---

### Question 140 — `CLF-U0842` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following services enables you to easily generate and use your own encryption keys in the AWS Cloud?**

- A) AWS Shield.
- B) AWS Certificate Manager.
- C) AWS CloudHSM.
- D) AWS WAF.

<details>
<summary><strong>Reveal Answer & Explanation (Question 140)</strong></summary>

**Correct Answer:** `C`

AWS CloudHSM provides dedicated, single-tenant hardware security modules in the AWS Cloud, giving you full control over encryption key generation and management with FIPS 140-2 Level 3 validated hardware for customers requiring hardware-based key control.
AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to generate or manage encryption keys. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service rather than a general-purpose encryption key generation service. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block web exploits, and is a traffic filtering service with no capability to generate or manage customer encryption keys.

</details>

---

### Question 141 — `CLF-U0852` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**What does Amazon GuardDuty do to protect AWS accounts and workloads?**

- A) Notifies AWS customers about abuse events once they are reported.
- B) Continuously monitors AWS infrastructure and helps detect threats such as attacker reconnaissance or account compromise.
- C) Helps AWS customers identify the root cause of potential security issues.
- D) Checks security groups for rules that allow unrestricted access to AWS. resources.

<details>
<summary><strong>Reveal Answer & Explanation (Question 141)</strong></summary>

**Correct Answer:** `B`

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads using machine learning and threat intelligence to identify suspicious activity such as attacker reconnaissance, compromised instances, or unusual API calls.
Notifying customers about abuse events once they are reported is the function of the AWS Abuse Team, which handles reports of AWS resources being used for malicious activity and communicates with affected account holders, rather than a capability of GuardDuty. Helping customers identify the root cause of potential security issues describes Amazon Detective, which analyzes and visualises security data from GuardDuty and CloudTrail to trace the origin and scope of suspicious activity rather than detecting threats in real time. Checking security groups for rules that allow unrestricted access to AWS resources is a function of AWS Trusted Advisor, which performs security checks including identification of overly permissive security group configurations, not GuardDuty.

</details>

---

### Question 142 — `CLF-U0854` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which of the following services is used when encrypting EBS volumes?**

- A) AWS WAF.
- B) AWS KMS.
- C) Amazon Macie.
- D) Amazon GuardDuty.

<details>
<summary><strong>Reveal Answer & Explanation (Question 142)</strong></summary>

**Correct Answer:** `B`

AWS KMS manages the encryption keys used for EBS volume encryption, handling key creation, storage, rotation, and access control, integrating transparently with EBS to encrypt data at rest.
AWS WAF is a web application firewall that filters HTTP and HTTPS traffic to block common web exploits such as SQL injection and cross-site scripting, and is a traffic filtering service with no role in managing encryption keys for EBS volumes. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification service for S3 rather than a key management service for EBS encryption. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and is a security monitoring service rather than a key management service for encrypting EBS volumes.

</details>

---

### Question 143 — `CLF-U0876` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**If a customer needs to audit the change management of AWS resources, which of the following AWS services should the customer use?**

- A) AWS Config.
- B) AWS Trusted Advisor.
- C) Amazon CloudWatch.
- D) Amazon Inspector.

<details>
<summary><strong>Reveal Answer & Explanation (Question 143)</strong></summary>

**Correct Answer:** `A`

AWS Config continuously records resource configurations and changes over time, providing a detailed audit trail of what changed, when it changed, and who made the change, making it the purpose-built service for auditing change management of AWS resources.
AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, but does not record or audit configuration changes to individual resources over time. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and does not track resource configuration history or change management. Amazon Inspector is an automated security assessment service that scans for software vulnerabilities and unintended network exposure, and is a security testing tool rather than a configuration change auditing service.

</details>

---

### Question 144 — `CLF-U0953` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.3: Perimeter Defense, Threat Detection & Firewalls*

**Which AWS service allows users to download security and compliance reports about the AWS infrastructure on demand?**

- A) Amazon GuardDuty
- B) AWS Security Hub
- C) AWS Artifact
- D) AWS Shield

<details>
<summary><strong>Reveal Answer & Explanation (Question 144)</strong></summary>

**Correct Answer:** `C`

AWS Artifact provides on-demand access to AWS security and compliance reports including SOC, PCI DSS, ISO, and HIPAA documentation, available for download directly from the AWS Management Console without contacting AWS.
Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability and alerting service rather than a repository of AWS security and compliance reports. AWS CloudTrail records all API calls and management events across an AWS account for auditing purposes, and produces customer-specific activity logs rather than AWS security certification and compliance documentation. Amazon GuardDuty is a threat detection service that continuously monitors accounts and workloads for malicious activity, and is a real-time security monitoring service rather than a source of downloadable compliance reports.

</details>

---

### Question 145 — `CLF-U0667` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**What can assist in evaluating an application for migration to the cloud? (Select TWO)**

- A) AWS Trusted Advisor.
- B) AWS Professional Services.
- C) AWS Systems Manager.
- D) AWS Partner Network (APN).
- E) AWS Secrets Manager.

<details>
<summary><strong>Reveal Answer & Explanation (Question 145)</strong></summary>

**Correct Answer:** `B, D`

AWS Professional Services provides expert consulting engagements to help evaluate and plan migrations, and AWS Partner Network partners offer specialized migration expertise through certified consulting and technology firms.
AWS Trusted Advisor scans existing AWS environments for best practice recommendations across cost, performance, security, and fault tolerance, but does not evaluate whether an application is suitable for migration to the cloud. AWS Systems Manager is an operational management service for configuring, patching, and managing AWS resources at scale, and is not a migration advisory or evaluation service. AWS Secrets Manager is a service for storing and rotating application secrets such as database credentials and API keys, and has no role in evaluating applications for cloud migration.

</details>

---

### Question 146 — `CLF-U0830` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**Which AWS service enables you to quickly purchase and deploy SSL/TLS certificates?**

- A) Amazon GuardDuty.
- B) AWS ACM.
- C) Amazon Detective.
- D) AWS WAF.

<details>
<summary><strong>Reveal Answer & Explanation (Question 146)</strong></summary>

**Correct Answer:** `B`

AWS Certificate Manager lets you provision, manage, and deploy SSL/TLS certificates for use with AWS services such as Elastic Load Balancers and CloudFront distributions, offering free public certificates that renew automatically.
Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and has no capability to provision or manage SSL/TLS certificates. Amazon Detective helps analyze and visualise security data to investigate the root cause of suspicious activity, providing forensic investigation capabilities rather than SSL/TLS certificate provisioning. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block common web exploits, and is a traffic filtering service rather than a certificate provisioning service.

</details>

---

### Question 147 — `CLF-U0839` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**Which of the following would you use to manage your encryption keys in the AWS Cloud? (Choose TWO)**

- A) AWS KMS.
- B) AWS Certificate Manager.
- C) AWS CodeDeploy.
- D) AWS CodeCommit.
- E) CloudHSM.

<details>
<summary><strong>Reveal Answer & Explanation (Question 147)</strong></summary>

**Correct Answer:** `A, E`

AWS KMS provides centralized software-based key management with AWS-managed infrastructure and integrates natively with most AWS services for encryption at rest, and AWS CloudHSM provides dedicated hardware security modules for customers requiring hardware-based key control for regulatory compliance. Both are valid services for managing encryption keys in the AWS Cloud.
AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate provisioning service rather than a key management service for creating and storing encryption keys. AWS CodeDeploy is an automated deployment service that delivers application code to EC2 instances, Lambda functions, and on-premises servers, and is a deployment automation tool with no encryption key management capability. AWS CodeCommit is a fully managed source control service for hosting Git repositories for version-controlled code storage, and is a code collaboration tool rather than an encryption key management service.

</details>

---

### Question 148 — `CLF-U0848` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**What is the main benefit of attaching security groups to an Amazon RDS instance?**

- A) Manages user access and encryption keys.
- B) Controls what IP address ranges can connect to your database instance.
- C) Deploys SSL/TLS certificates for use with your database instance.
- D) Distributes incoming traffic across multiple targets.

<details>
<summary><strong>Reveal Answer & Explanation (Question 148)</strong></summary>

**Correct Answer:** `B`

Security groups attached to an RDS instance act as a virtual firewall controlling which IP address ranges and EC2 instances are allowed to establish connections to the database, restricting network access to only authorised sources.
Managing user access and encryption keys describes AWS IAM and AWS KMS respectively, which are separate services for identity management and key management rather than functions provided by security groups attached to an RDS instance. Deploying SSL/TLS certificates for database connections is performed by AWS Certificate Manager and the RDS parameter group configuration, not by security groups, which control network connectivity rather than certificate provisioning. Distributing incoming traffic across multiple targets describes an Elastic Load Balancer, which routes requests to multiple backend instances, and is not a function of security groups attached to a database instance.

</details>

---

### Question 149 — `CLF-U0862` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**Where can AWS compliance and certification reports be downloaded?**

- A) AWS Artifact.
- B) AWS Concierge.
- C) AWS Certificate Manager.
- D) AWS Trusted Advisor.

<details>
<summary><strong>Reveal Answer & Explanation (Question 149)</strong></summary>

**Correct Answer:** `A`

AWS Artifact is the self-service portal where customers can download AWS compliance and certification reports including SOC, PCI, ISO, and HIPAA eligibility documentation without needing to contact AWS directly.
AWS Concierge is a dedicated support resource for Enterprise support plan customers that assists with billing and account management, and is not a portal for downloading compliance reports or technical certification documents. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate provisioning service rather than a repository of AWS compliance and audit reports. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and while it includes security checks, it does not provide downloadable AWS compliance certification reports.

</details>

---

### Question 150 — `CLF-U0966` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**Which AWS service can be used to retrieve compliance reports on demand?**

- A) AWS Secrets Manager
- B) AWS Artifact
- C) AWS Security Hub
- D) AWS Certificate Manager

<details>
<summary><strong>Reveal Answer & Explanation (Question 150)</strong></summary>

**Correct Answer:** `B`

AWS Artifact provides on-demand access to AWS compliance reports including SOC, PCI, ISO, and other certifications, available for download directly from the AWS Management Console.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no capability to retrieve or provide compliance documentation. AWS Security Hub provides a centralized view of security alerts and compliance status across an AWS environment by aggregating findings from multiple security services, and is a security posture management tool rather than a repository of AWS compliance reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate management service with no connection to compliance report retrieval.

</details>

---

### Question 151 — `CLF-U1397` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.4: Data Protection, Cryptography & Secrets*

**A user has been granted permission to change their own IAM user password. Which AWS services can the user use to change the password? (Select TWO.)**

- A) AWS Command Line Interface (AWS CLI)
- B) AWS Key Management Service (AWS KMS)
- C) AWS Management Console
- D) AWS Resource Access Manager (AWS RAM)
- E) AWS Secrets Manager

<details>
<summary><strong>Reveal Answer & Explanation (Question 151)</strong></summary>

**Correct Answer:** `AC`

Users can change their own IAM user password using:
AWS Management Console: The graphical interface allows users to navigate to the "My
Security Credentials" page and change their password.
AWS Command Line Interface (CLI): Users with the appropriate permissions can use
theaws iam change-passwordcommand to change their password.
Why other options are not suitable:
B . AWS Key Management Service (AWS KMS): Used for creating and managing
encryption keys, not for managing user passwords.
D . AWS Resource Access Manager (AWS RAM): Used for resource sharing between
accounts, not for password management.
E . AWS Secrets Manager: A service for securely storing and managing secrets, not for
changing IAM user passwords.
Reference:
AWS IAM User Guide - Changing Your Own Password

</details>

---

### Question 152 — `CLF-U0199` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which AWS service or feature can be used to monitor CPU usage?**

- A) AWS CloudTrail.
- B) VPC Flow Logs.
- C) Amazon CloudWatch.
- D) AWS Config.

<details>
<summary><strong>Reveal Answer & Explanation (Question 152)</strong></summary>

**Correct Answer:** `C`

**Correct Answer: C** (**C** (Amazon CloudWatch.))

> **Domain Focus:** Security and Compliance | **Blueprint Area:** Topic 2.5: Compliance, Auditing & Artifact

### 💡 Architectural Rationale & Why It Is Correct:
Under AWS Well-Architected principles and official CLF-C02 specifications for `point:comp_cloudtrail_api_governance`: **C** (Amazon CloudWatch.) directly satisfies the requirements stated in the scenario.
In production AWS environments, this architectural pattern ensures compliance, maximum operational efficiency, and least-privilege alignment.

### 🔍 Detailed Option Breakdown & Distractor Analysis:
- **Option A (AWS CloudTrail.)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).
- **Option B (VPC Flow Logs.)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).
- **Option C (Amazon CloudWatch.)** ✅ **[CORRECT]**: Directly addresses the operational and governance goals of this scenario under the AWS Shared Responsibility and service boundary model.
- **Option D (AWSConfig.)** ❌ **[INCORRECT]**: Suboptimal or introduces architectural anti-patterns for this specific requirement (either refers to an unrelated service, violates security boundaries, or increases operational overhead).

### ⚠️ Exam Trap & Heuristic Decryption:
Watch out for distractors testing similar AWS service boundaries. When the question asks for `Compliance, Auditing & Artifact`, prioritize native managed AWS services over manual or third-party administration.

</details>

---

### Question 153 — `CLF-U0233` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which AWS service can be used to automatically scale an application up and down without making capacity planning decisions?**

- A) Amazon AutoScaling.
- B) Amazon Redshift.
- C) AWS CloudTrail.
- D) AWS Lambda.

<details>
<summary><strong>Reveal Answer & Explanation (Question 153)</strong></summary>

**Correct Answer:** `A`

AWS Auto Scaling automatically adjusts the number of EC2 instances based on defined policies, eliminating the need for manual capacity planning decisions and ensuring the application always has the right amount of compute capacity.
Amazon Redshift is a fully managed data warehouse service designed for running analytical queries across large datasets, and has no capability to automatically scale application infrastructure. AWS CloudTrail is a logging and auditing service that records API calls and account activity across an AWS environment, and does not manage or adjust application capacity. AWS Lambda is a serverless compute service that runs code in response to events without provisioning servers, but it is an event-driven execution environment rather than a service that scales existing application infrastructure up and down.

</details>

---

### Question 154 — `CLF-U0819` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which AWS Service allows customers to download AWS SOC & PCI reports?**

- A) AWS Well-Architected Tool.
- B) AWS Artifact.
- C) AWS Glue.
- D) Amazon Chime.

<details>
<summary><strong>Reveal Answer & Explanation (Question 154)</strong></summary>

**Correct Answer:** `B`

AWS Artifact is a self-service portal for on-demand access to AWS compliance reports including SOC and PCI reports, and agreement documents such as Business Associate Addenda, making it the correct service for downloading AWS SOC and PCI compliance reports.
AWS Well-Architected Tool is a service that helps you review the state of your workloads and compare them against AWS architectural best practices across the six pillars, and is a workload review and guidance tool rather than a compliance report repository. AWS Glue is a fully managed extract, transform, and load service for preparing and transforming data for analytics, and is a data integration service with no connection to compliance documentation. Amazon Chime is a unified communications service for online meetings, video conferencing, and chat, and has no relationship to compliance reports or AWS certification documents.

</details>

---

### Question 155 — `CLF-U0836` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which of the following services provide real-time auditing for compliance and vulnerabilities? (Choose TWO)**

- A) AWS Config.
- B) Amazon Redshift.
- C) Amazon MQ.
- D) AWS Trusted Advisor.
- E) Amazon Cognito.

<details>
<summary><strong>Reveal Answer & Explanation (Question 155)</strong></summary>

**Correct Answer:** `A, D`

AWS Config continuously monitors and records resource configurations to evaluate compliance against desired rules, and AWS Trusted Advisor provides real-time checks across security, performance, cost, and fault tolerance categories. Both provide real-time auditing capabilities.
Amazon Redshift is a fully managed cloud data warehouse service for running analytical queries on large datasets, and is a data analytics service rather than a real-time auditing tool for compliance or vulnerability assessment. Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that enables application messaging and decoupling, and is a messaging infrastructure service with no auditing or compliance checking capability. Amazon Cognito is a user identity and authentication service for web and mobile applications that handles sign-up, sign-in, and access control, and is an identity service rather than a compliance auditing or vulnerability assessment tool.

</details>

---

### Question 156 — `CLF-U0837` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which of the following services gives you access to all AWS auditor-issued reports and certifications?**

- A) AWS Artifact.
- B) AWS Config.
- C) Amazon CloudWatch.
- D) AWS CloudTrail.

<details>
<summary><strong>Reveal Answer & Explanation (Question 156)</strong></summary>

**Correct Answer:** `A`

AWS Artifact provides on-demand, self-service access to AWS compliance reports and auditor-issued certifications such as SOC, PCI DSS, and ISO documents, directly from the AWS Management Console without needing to contact AWS support.
AWS Config continuously monitors and records resource configurations against compliance rules to help manage configuration drift and evaluate resource compliance, and is a resource configuration compliance tool rather than a repository of AWS auditor-issued certifications. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications to support observability and alerting, and has no connection to providing access to AWS compliance reports or third-party audit certifications. AWS CloudTrail records all API calls and management events across an AWS account for auditing and security analysis, and produces customer-specific activity logs rather than auditor-issued AWS compliance certifications.

</details>

---

### Question 157 — `CLF-U0856` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**A financial services company decides to migrate one of its applications to AWS. The application deals with sensitive data, such as credit card information, and must run on a PCI-compliant environment. Which of the following is the company’s responsibility when building a PCI-compliant environment in AWS? (Choose TWO)**

- A) Start the migration process immediately as all AWS services are PCI compliant.
- B) Ensure that AWS services are configured properly to meet all PCI DSS standards.
- C) Restrict any access to cardholder data and create a policy that addresses information security for all personnel.
- D) Configure the underlying infrastructure of AWS services to meet all PCI DSS requirements.
- E) Ensure that all PCI DSS physical security requirements are met.

<details>
<summary><strong>Reveal Answer & Explanation (Question 157)</strong></summary>

**Correct Answer:** `B, C`

Customers must properly configure AWS services to meet PCI DSS standards as AWS's compliance certifications cover the infrastructure layer but not the customer's specific service configurations, and customers must restrict cardholder data access and maintain an information security policy as these are customer responsibilities under PCI DSS.
Not all AWS services are PCI DSS compliant by default; only specific AWS services are in scope for PCI compliance, and customers must verify that the services they use are in scope and configured correctly to maintain a PCI-compliant environment. Configuring the underlying AWS infrastructure to meet PCI DSS requirements is not the customer's responsibility; AWS manages and maintains the physical infrastructure, hardware, and network to meet PCI standards, and customers are responsible only for how they configure the services built on top of that infrastructure. Ensuring that all PCI DSS physical security requirements are met is AWS's responsibility; the physical security of data centers, including access controls, surveillance, and hardware handling, is managed by AWS under the shared responsibility model.

</details>

---

### Question 158 — `CLF-U0861` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which service enables risk auditing by continuously monitoring and logging account activity, including user actions in the AWS Management Console and AWS SDKs?**

- A) Amazon CloudWatch.
- B) AWS CloudTrail.
- C) AWS Config.
- D) AWS Health.

<details>
<summary><strong>Reveal Answer & Explanation (Question 158)</strong></summary>

**Correct Answer:** `B`

AWS CloudTrail continuously logs all account activity and API calls across AWS infrastructure, providing a complete audit trail that supports risk auditing, compliance monitoring, and security analysis.
Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational visibility into performance and health, and while it can monitor logs, it does not record API calls or user actions for risk auditing and compliance purposes. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance against desired settings, and focuses on resource configuration changes rather than logging user actions and API calls for risk auditing. AWS Health provides personalized alerts and remediation guidance when AWS is experiencing events that may affect your resources, and is a service health notification tool rather than an account activity logging or risk auditing service.

</details>

---

### Question 159 — `CLF-U0864` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Which AWS service would you use to obtain compliance reports and certificates?**

- A) AWS Artifact.
- B) AWS Lambda.
- C) Amazon Inspector.
- D) AWS Certificate Manager.

<details>
<summary><strong>Reveal Answer & Explanation (Question 159)</strong></summary>

**Correct Answer:** `A`

AWS Artifact provides on-demand access to AWS compliance reports and certifications including SOC, PCI DSS, ISO, and HIPAA documents, available directly from the AWS Management Console without needing to engage AWS support.
AWS Lambda is a serverless compute service that runs code in response to events without requiring server provisioning or management, and is a compute service with no connection to compliance reports or certification documentation. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces customer-specific vulnerability findings rather than AWS compliance certifications. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services, and is a certificate management service rather than a repository of compliance reports or regulatory certifications.

</details>

---

### Question 160 — `CLF-U0888` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**Where are AWS compliance documents, such as an SOC 1 report, located?**

- A) Amazon Inspector.
- B) AWS CloudTrail.
- C) AWS Artifact.
- D) AWS Certificate Manager.

<details>
<summary><strong>Reveal Answer & Explanation (Question 160)</strong></summary>

**Correct Answer:** `C`

AWS Artifact is the dedicated self-service portal for accessing AWS compliance documentation, including SOC 1, SOC 2, ISO 27001, and PCI DSS reports, allowing customers to download these documents for their own audit and compliance purposes.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and network exposure risks, and does not provide or store AWS compliance certifications or SOC reports. AWS CloudTrail logs all API calls and management events in an AWS account for auditing purposes, and produces customer-specific activity logs rather than AWS compliance certifications or third-party audit reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service rather than a repository of compliance reports.

</details>

---

### Question 161 — `CLF-U0964` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**A company has a compliance requirement to record and evaluate configuration changes, as well as perform remediation actions on AWS resources. Which AWS service should the company use?**

- A) AWS Config
- B) AWS Secrets Manager
- C) AWS CloudTrail
- D) AWS Trusted Advisor

<details>
<summary><strong>Reveal Answer & Explanation (Question 161)</strong></summary>

**Correct Answer:** `A`

AWS Config records configuration changes, evaluates them against compliance rules, and can trigger automated remediation actions when resources become non-compliant, meeting all three requirements of recording, evaluating, and remediating.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no capability to record configuration changes or trigger compliance remediation. AWS CloudTrail logs all API calls and account activity for auditing purposes, and while it records who made changes and when, it does not evaluate resources against compliance rules or trigger remediation actions. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and offers advisory guidance rather than automated compliance rule evaluation or remediation capability.

</details>

---

### Question 162 — `CLF-U1469` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 2.5: Compliance, Auditing & Artifact*

**A company plans to migrate its custom marketing application and order-processing application to AWS. The company needs to deploy the applications on different types of instances with various configurations of CPU, memory, storage, and networking capacity. Which AWS service should the company use to meet these requirements?**

- A) AWS Lambda
- B) Amazon Cognito
- C) Amazon Athena
- D) Amazon EC2

<details>
<summary><strong>Reveal Answer & Explanation (Question 162)</strong></summary>

**Correct Answer:** `D`

Amazon EC2 (Elastic Compute Cloud)provides scalable computing capacity in the AWS
Cloud, allowing customers to run virtual servers (instances) with different configurations of
CPU, memory, storage, and networking capacity. This flexibility is ideal for applications
that require specific infrastructure configurations, such as custom marketing and orderprocessing applications.
A . AWS Lambda: Incorrect, as it is a serverless compute service that automatically
manages the computing resources needed to run code but does not offer the flexibility of
choosing different instance types.
B . Amazon Cognito: Incorrect, as it is used for user authentication and authorization, not
for deploying applications.
C . Amazon Athena: Incorrect, as it is an interactive query service for analyzing data in
Amazon S3 using standard SQL.
AWS Cloud Reference:
Amazon EC2

</details>

---

## 🎯 Domain 3: Cloud Technology and Services (34% — 102 Questions)

### Question 163 — `CLF-U0242` | 🔁 Repeated in 5 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is stopped or terminated?**

- A) Amazon EBS.
- B) Amazon EC2 instance store.
- C) Amazon EFS.
- D) Amazon S3.

<details>
<summary><strong>Reveal Answer & Explanation (Question 163)</strong></summary>

**Correct Answer:** `B`

**Correct Answer: B (Amazon EC2 instance store)**

This question (# 98) is directly sourced from authentic **Community Consensus Pool** community discussions.
**Why this is correct:** The scenario specifically tests AWS best practices. 'Amazon EC2 instance store' directly satisfies the architectural requirement defined in the prompt.

**Key Option Breakdown:**
- **Option A (Amazon Elastic Block Store (Amazon EBS))** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option B (Amazon EC2 instance store)** [CORRECT]: Satisfies the prompt requirements directly.
- **Option C (Amazon Elastic File System (Amazon EFS))** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option D (Amazon S3)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.

</details>

---

### Question 164 — `CLF-U0001` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**AWS allows users to manage their resources using a web based user interface. What is the name of this interface?**

- A) AWS CLI.
- B) AWS API.
- C) AWS SDK.
- D) AWS Management Console.

<details>
<summary><strong>Reveal Answer & Explanation (Question 164)</strong></summary>

**Correct Answer:** `D`

**Correct answer: AWS Management Console**

The AWS Management Console is a web-based interface that allows users to access and manage AWS services. It provides a graphical user interface (GUI) for interacting with AWS resources, making it easier to perform tasks such as launching EC2 instances, configuring S3 buckets, and monitoring CloudWatch metrics. The console simplifies AWS management, especially for users who prefer a visual interface over command-line tools or APIs.

**Incorrect:**

**A. AWS API** - The AWS API (Application Programming Interface) is a set of request and response protocols that allow developers to programmatically interact with AWS services. While it's a way to manage resources, it's not a web-based user interface.

**C. AWS SDK** - The AWS SDK (Software Development Kit) provides language-specific libraries and tools that enable developers to build applications that interact with AWS services. Like the API, it's a programmatic interface, not a web-based GUI.

**D. AWS CLI** - The AWS CLI (Command Line Interface) is a tool that allows users to interact with AWS services using commands in a terminal or command prompt. It's a powerful tool for automation and scripting, but it's not a web-based user interface.

</details>

---

### Question 165 — `CLF-U0002` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which of the following is an example of horizontal scaling in the AWS Cloud?**

- A) Replacing an existing EC2 instance with a larger, more powerful one.
- B) Increasing the compute capacity of a single EC2 instance to address the growing demands of an application.
- C) Adding more RAM capacity to an EC2 instance.
- D) Adding more EC2 instances of the same size to handle an increase in traffic.

<details>
<summary><strong>Reveal Answer & Explanation (Question 165)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Adding more EC2 instances of the same size to handle an increase in traffic**

Horizontal scaling (also known as scaling out) involves increasing the number of instances for your application. In the AWS Cloud, this typically means adding more EC2 instances to a load balancer or auto-scaling group to handle increased traffic or workload. This approach distributes the load across multiple smaller instances, improving availability and fault tolerance. It contrasts with vertical scaling, which involves increasing the resources of a single instance.

**Incorrect:**

**A. Adding more RAM capacity to an EC2 instance** - Adding more RAM to an EC2 instance is an example of vertical scaling (scaling up), not horizontal scaling. Vertical scaling involves increasing the resources (CPU, RAM, storage) of a single instance.

**B. Replacing an existing EC2 instance with a larger, more powerful one** - Replacing an EC2 instance with a larger one is also an example of vertical scaling. You are increasing the capacity of a single instance, rather than adding more instances.

**C. Increasing the compute capacity of a single EC2 instance to address the growing demands of an application** - Increasing the compute capacity (e.g., adding more CPUs) to a single EC2 instance is vertical scaling. Horizontal scaling focuses on distributing the load across multiple instances.

</details>

---

### Question 166 — `CLF-U0020` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**A developer is planning to build a two-tier web application that has a MySQL database layer. Which of the following AWS database services would provide automated backups for the application?**

- A) A MySQL database installed on an EC2 instance.
- B) Amazon Aurora.
- C) Amazon DynamoDB.
- D) Amazon Neptune.

<details>
<summary><strong>Reveal Answer & Explanation (Question 166)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Amazon Aurora**

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database service that combines the speed and availability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. Aurora provides automated backups by default. These backups are continuous and incremental, allowing for point-in-time recovery. This feature greatly simplifies database administration and ensures data durability.

**Incorrect:**

**A. Amazon DynamoDB** - Amazon DynamoDB is a NoSQL database service. While DynamoDB offers backup and restore capabilities, it is not a MySQL database service as required by the question. Therefore, it's not the correct choice for a MySQL database layer.

**C. Amazon Neptune** - Amazon Neptune is a graph database service. It is designed for applications that require highly connected data, such as social networking, recommendation engines, and knowledge graphs. It is not a MySQL database service and does not fit the requirements of the question.

**D. A MySQL database installed on an EC2 instance** - While you can install a MySQL database on an EC2 instance, automated backups are not provided by default. You would need to configure and manage the backups yourself using tools like `mysqldump` or by creating EBS snapshots. This option requires more manual effort compared to using a managed database service like Amazon Aurora, which provides automated backups out-of-the-box.

</details>

---

### Question 167 — `CLF-U0042` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which of the following services allows you to run containerized applications on a cluster of EC2 instances?**

- A) Amazon ECS.
- B) AWS Data Pipeline.
- C) AWS Cloud9.
- D) AWS Health Dashboard (formerly AWS AWS Health Dashboard (Your Account Health)).

<details>
<summary><strong>Reveal Answer & Explanation (Question 167)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon ECS**

Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that makes it easy for you to deploy, manage, and scale containerized applications on AWS. ECS allows you to run your containers on a cluster of EC2 instances, or on AWS Fargate for serverless compute. ECS simplifies the process of managing the underlying infrastructure and provides features such as task scheduling, service discovery, and load balancing for your containerized applications.

**Correct answer: Amazon Elastic Kubernetes Service**

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service that makes it easy for you to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane. EKS allows you to run containerized applications on a cluster of EC2 instances, managed by Kubernetes. EKS handles the complexities of Kubernetes management, allowing you to focus on building and deploying your applications.

**Incorrect:**

**A. AWS Health Dashboard** - The AWS Health Dashboard provides personalized view of the health of AWS services and resources. It does not allow you to run containerized applications.

**B. AWS Cloud9** - AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug code with just a browser. While you can develop containerized applications using Cloud9, it doesn't directly run them on a cluster of EC2 instances.

**E. AWS Data Pipeline** - AWS Data Pipeline is a web service that helps you reliably process and move data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals. It is not used for running containerized applications.

</details>

---

### Question 168 — `CLF-U0051` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**A company is migrating its on-premises database to Amazon RDS. What should the company do to ensure Amazon RDS costs are kept to a minimum?**

- A) Right-size before and after migration.
- B) Use a Multi-Region Active-Passive architecture.
- C) Combine On-demand Capacity Reservations with Saving Plans.
- D) Use a Multi-Region Active-Active architecture.

<details>
<summary><strong>Reveal Answer & Explanation (Question 168)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Right-size before and after migration**

Right-sizing your Amazon RDS instance involves selecting the appropriate instance type and storage capacity to meet your workload requirements. Before migrating, analyze your on-premises database's resource utilization (CPU, memory, storage, I/O) to determine the optimal RDS instance size. After migration, continuously monitor performance and adjust the instance size as needed. Over-provisioning leads to unnecessary costs, while under-provisioning can impact performance. Right-sizing ensures you pay only for the resources you actually need, minimizing costs.

**Incorrect:**

**A. Use a Multi-Region Active-Passive architecture** - A Multi-Region Active-Passive architecture, while providing disaster recovery benefits, increases costs due to the need to maintain a standby database instance in another region. This is not a cost-minimization strategy.

**C. Use a Multi-Region Active-Active architecture** - A Multi-Region Active-Active architecture is even more expensive than Active-Passive, as it involves running multiple active database instances across different regions. This is for high availability and low latency in geographically distributed applications, not cost optimization.

**D. Combine On-demand Capacity Reservations with Saving Plans** - On-Demand Capacity Reservations guarantee that compute capacity is available for your Amazon EC2 instances when you need it in a specific Availability Zone. Savings Plans provide a lower price than On-Demand pricing, in exchange for a commitment to a consistent amount of usage (measured in dollars per hour) for a 1- or 3-year term. While Savings Plans can reduce costs, they apply to compute resources (like EC2) and are not directly related to right-sizing your RDS instance. Capacity Reservations are also not directly related to RDS cost optimization.

</details>

---

### Question 169 — `CLF-U0062` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**What is the AWS tool that enables you to use scripts to manage all AWS services and resources?**

- A) AWS Console.
- B) AWS Service Catalog.
- C) AWS OpsWorks.
- D) AWS CLI.

<details>
<summary><strong>Reveal Answer & Explanation (Question 169)</strong></summary>

**Correct Answer:** `D`

**Correct answer: AWS CLI**

The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool, you can control multiple AWS services from the command line and automate them through scripts. The AWS CLI allows you to interact with AWS services using commands in your command-line shell. This is particularly useful for automating tasks and managing infrastructure as code.

**Incorrect:**

**A. AWS Console** - The AWS Management Console is a web-based interface for accessing and managing AWS services. While it's a graphical user interface (GUI) that allows you to manage AWS resources, it is not primarily designed for scripting and automation in the same way as the AWS CLI.

**C. AWS Service Catalog** - AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. It focuses on enabling self-service access to predefined and standardized resources, rather than providing a general-purpose scripting interface for managing all AWS services.

**D. AWS OpsWorks** - AWS OpsWorks is a configuration management service that helps you automate operational tasks like server configuration, deployment, and scaling. While it involves automation, it's more focused on managing application stacks and server configurations, not providing a general-purpose scripting interface for all AWS services like the AWS CLI does.

</details>

---

### Question 170 — `CLF-U0066` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**How are AWS customers billed for Linux-based Amazon EC2 usage?**

- A) EC2 instances will be billed on one second increments, with a minimum of one minute.
- B) EC2 instances will be billed on one hour increments, with a minimum of one day.
- C) EC2 instances will be billed on one minute increments, with a minimum of one hour.
- D) EC2 instances will be billed on one day increments, with a minimum of one month.

<details>
<summary><strong>Reveal Answer & Explanation (Question 170)</strong></summary>

**Correct Answer:** `A`

**Correct answer: EC2 instances will be billed on one second increments, with a minimum of one minute**

AWS bills for Linux-based Amazon EC2 instances on a per-second basis, with a minimum of 60 seconds (one minute). This billing model applies to many Linux distributions available on EC2. This granularity allows you to pay only for the compute time you actually use, optimizing costs, especially for workloads that have variable usage patterns or short execution times. Note that some older EC2 instance types or operating systems might have different billing increments, but the per-second billing with a one-minute minimum is the standard for current Linux-based instances.

**Incorrect:**

**A. EC2 instances will be billed on one minute increments, with a minimum of one hour** - While older EC2 billing models might have involved hourly increments, the current standard for Linux-based instances is per-second billing with a one-minute minimum. Therefore, this option is incorrect.

**B. EC2 instances will be billed on one day increments, with a minimum of one month** - EC2 billing does not operate on a daily or monthly increment basis. The billing is much more granular, allowing for cost optimization based on actual usage. This option is incorrect as it misrepresents the billing structure.

**D. EC2 instances will be billed on one hour increments, with a minimum of one day** - This option is incorrect because EC2 instances are not billed on an hourly increment with a one-day minimum. The billing is per-second with a one-minute minimum for Linux-based instances.

</details>

---

### Question 171 — `CLF-U0068` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**What are the benefits of using the Amazon Relational Database Service? (Choose TWO)**

- A) Lower administrative burden.
- B) Complete control over the underlying host.
- C) Resizable compute capacity.
- D) Scales automatically to larger or smaller instance types.
- E) Supports the document and key-value data structure.

<details>
<summary><strong>Reveal Answer & Explanation (Question 171)</strong></summary>

**Correct Answer:** `A, C`

**Correct answer: Resizable compute capacity**

Amazon RDS allows you to easily scale the compute resources (CPU, memory) allocated to your database instances. You can choose from a variety of instance types optimized for different workloads, and you can resize these instances as your needs change. This flexibility is a key benefit of using a managed database service like RDS.

**Correct answer: Lower administrative burden**

Amazon RDS automates many of the administrative tasks associated with managing a database, such as patching, backups, and recovery. This reduces the operational overhead for database administrators and allows them to focus on other tasks.

**Incorrect:**

**A. Supports the document and key-value data structure** - While Amazon offers document and key-value database services, these are provided by Amazon DocumentDB and Amazon DynamoDB, respectively. Amazon RDS is primarily for relational databases.

**B. Complete control over the underlying host** - Amazon RDS is a managed service, which means that AWS manages the underlying infrastructure. You do not have complete control over the host operating system or hardware. If you require full control, you should consider running a database on an EC2 instance.

**D. Scales automatically to larger or smaller instance types** - While RDS supports auto scaling of read replicas and storage, it does not automatically scale to larger or smaller instance types. You can resize the instance type, but this is a manual operation or can be automated using scripts, not built-in autoscaling.

</details>

---

### Question 172 — `CLF-U0091` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Both AWS and traditional IT distributors provide a wide range of virtual servers to meet their customers’ requirements. What is the name of these virtual servers in AWS?**

- A) Amazon EBS Snapshots.
- B) Amazon VPC.
- C) AWS Managed Servers.
- D) Amazon EC2 Instances.

<details>
<summary><strong>Reveal Answer & Explanation (Question 172)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Amazon EC2 Instances**

Amazon Elastic Compute Cloud (EC2) instances are virtual servers in AWS. They provide scalable computing capacity in the AWS cloud, allowing users to run applications. EC2 offers a variety of instance types with different combinations of CPU, memory, storage, and networking capacity, giving users flexibility in choosing the appropriate resources for their workloads. This aligns with the question's reference to virtual servers offered by both AWS and traditional IT distributors.

**Incorrect:**

**A. AWS Managed Servers** - This is not a standard term used to describe virtual servers in AWS. While AWS offers managed services, the virtual servers themselves are referred to as EC2 instances, not "AWS Managed Servers."

**B. Amazon EBS Snapshots** - Amazon Elastic Block Storage (EBS) snapshots are backups of EBS volumes, which are persistent block storage volumes used with EC2 instances. Snapshots are not virtual servers themselves, but rather a mechanism for data protection and disaster recovery related to EC2 instances.

**D. Amazon Virtual Private Cloud** - Amazon VPC (Virtual Private Cloud) is a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. It is a networking service, not a virtual server. While EC2 instances are often launched within a VPC, the VPC itself is not the virtual server.

</details>

---

### Question 173 — `CLF-U0385` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**What is the advantage of the AWS-recommended practice of "decoupling" applications?**

- A) Allows treating an application as a single, cohesive unit.
- B) Reduces inter-dependencies so that failures do not impact other components of the application.
- C) Allows updates of any monolithic application quickly and easily.
- D) Allows tracking of any API call made to any AWS service.

<details>
<summary><strong>Reveal Answer & Explanation (Question 173)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Reduces inter-dependencies so that failures do not impact other components of the application**

Decoupling in application architecture is a design principle that aims to minimize dependencies between different components of a system. In a decoupled architecture, components operate independently and communicate through well-defined interfaces, such as APIs or message queues (e.g., Amazon SQS). This isolation ensures that if one component fails, it doesn't necessarily bring down other parts of the application. This enhances the overall resilience and availability of the system. Decoupling also allows for independent scaling and updates of individual components.

**Incorrect:**

**B. Allows treating an application as a single, cohesive unit** - Decoupling is the opposite of treating an application as a single cohesive unit. Monolithic applications are single cohesive units, and decoupling breaks them down into smaller, independent services.

**C. Allows updates of any monolithic application quickly and easily** - While decoupling can eventually lead to easier updates, it's not an immediate consequence. Monolithic applications are notoriously difficult to update quickly and easily. Decoupling is a strategy to move *away* from monolithic architectures.

**D. Allows tracking of any API call made to any AWS service** - Tracking API calls is primarily achieved through services like AWS CloudTrail, which logs API calls made to AWS services. Decoupling does not directly provide this functionality, although a decoupled architecture might make it easier to monitor individual components.

</details>

---

### Question 174 — `CLF-U0397` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Jessica is managing an e-commerce web application in AWS. The application is hosted on six EC2 instances. One day, three of the instances crashed; but none of her customers were affected. What has Jessica done correctly in this scenario?**

- A) She has properly built an elastic system.
- B) She has properly built a fault tolerant system.
- C) She has properly built an encrypted system.
- D) She has properly built a scalable system.

<details>
<summary><strong>Reveal Answer & Explanation (Question 174)</strong></summary>

**Correct Answer:** `B`

**Correct answer: She has properly built a fault tolerant system**

Fault tolerance is the ability of a system to continue operating properly in the event of the failure of some of its components. In this scenario, three EC2 instances crashed, but the application remained available to customers. This indicates that Jessica implemented redundancy and failover mechanisms, which are key characteristics of a fault-tolerant system. For example, she might have used a load balancer to distribute traffic across multiple instances and configured the system to automatically replace failed instances. This ensures that the application remains available even if some instances fail.

**Incorrect:**

**A. She has properly built an elastic system** - Elasticity refers to the ability of a system to automatically scale up or down based on demand. While the scenario might involve an elastic system, the key point is that the application remained available despite instance failures. Elasticity doesn't directly address fault tolerance. The question specifically highlights the system's ability to withstand failures without impacting users, which is the core of fault tolerance.

**B. She has properly built an encrypted system** - Encryption focuses on protecting data confidentiality and integrity. While encryption is an important security practice, it doesn't directly relate to the system's ability to withstand failures. The scenario describes a situation where the system remained operational despite failures, which is a characteristic of fault tolerance, not encryption.

**D. She has properly built a scalable system** - Scalability refers to the ability of a system to handle increasing amounts of traffic or data. While a scalable system might also be fault-tolerant, scalability alone doesn't guarantee that the system will remain available in the event of failures. The scenario specifically highlights the system's ability to withstand failures without impacting users, which is the core of fault tolerance.

</details>

---

### Question 175 — `CLF-U0408` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**What is the benefit of using an API to access AWS Services?**

- A) It improves the performance of AWS resources.
- B) It reduces the time needed to provision AWS resources.
- C) It reduces the number of developers necessary.
- D) It allows for programmatic management of AWS resources.

<details>
<summary><strong>Reveal Answer & Explanation (Question 175)</strong></summary>

**Correct Answer:** `D`

**Correct answer: It allows for programmatic management of AWS resources**

Using APIs (Application Programming Interfaces) to access AWS services enables programmatic management of AWS resources. This means you can use code (e.g., using the AWS SDKs or CLI) to create, modify, and delete resources such as EC2 instances, S3 buckets, and IAM roles. This allows for automation, infrastructure-as-code (IaC), and integration with other systems, leading to more efficient and scalable operations. For example, you can write a script to automatically provision a new EC2 instance based on certain triggers or schedule tasks using AWS Lambda and the AWS SDK.

**Incorrect:**

**B. It improves the performance of AWS resources** - While automation and efficient management through APIs can indirectly contribute to better performance (e.g., by quickly scaling resources to meet demand), the API itself doesn't directly improve the performance of the underlying AWS resources. Performance is primarily determined by the resource configuration, instance type, network bandwidth, and application code.

**C. It reduces the number of developers necessary** - While automation through APIs can streamline operations and potentially reduce manual effort, it doesn't necessarily reduce the number of developers required. In fact, it might require developers with specific skills in scripting, API integration, and automation to build and maintain the automation workflows.

**D. It reduces the time needed to provision AWS resources** - Using APIs and automation can significantly reduce the time needed to provision AWS resources compared to manual processes through the AWS Management Console. However, the API itself doesn't inherently reduce the time; it's the automation built on top of the API that achieves this reduction.

</details>

---

### Question 176 — `CLF-U0418` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**A key practice when designing solutions on AWS is to minimize dependencies between components so that the failure of a single component does not impact other components. What is this practice called?**

- A) Elastic coupling.
- B) Loosely coupling.
- C) Scalable coupling.
- D) Tightly coupling.

<details>
<summary><strong>Reveal Answer & Explanation (Question 176)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Loosely coupling**

Loosely coupling is a design principle in which components of a system are designed to be as independent as possible. This means that changes to one component should not require changes to other components. In the context of AWS, this is achieved by using services like SQS (Simple Queue Service) for asynchronous communication, SNS (Simple Notification Service) for pub/sub messaging, and API Gateway to decouple front-end and back-end services. By minimizing dependencies, the failure of one component is less likely to cascade and affect other parts of the system, improving overall resilience and availability.

**Incorrect:**

**A. Scalable coupling** - This term is not a standard or recognized concept in cloud architecture or software design. While scalability is important, "scalable coupling" doesn't describe a specific architectural pattern or practice. The focus is on how well a system can handle increased load, not on the dependencies between components.

**C. Elastic coupling** - This term is not a standard or recognized concept in cloud architecture or software design. Elasticity refers to the ability of a system to automatically scale resources up or down based on demand. While elasticity is a key benefit of the cloud, "elastic coupling" is not a defined architectural principle.

**D. Tightly coupling** - Tightly coupling is the opposite of what the question describes. It refers to a design where components are highly dependent on each other. Changes to one component often require changes to other components, making the system more fragile and difficult to maintain. This is generally an anti-pattern in cloud architecture.

</details>

---

### Question 177 — `CLF-U0799` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Based on the AWS Shared Responsibility Model, which of the following are the sole responsibility of AWS? (Choose TWO)**

- A) Monitoring network performance.
- B) Installing software on EC2 instances.
- C) Creating hypervisors.
- D) Configuring Access Control Lists (ACLs).
- E) Hardware maintenance.

<details>
<summary><strong>Reveal Answer & Explanation (Question 177)</strong></summary>

**Correct Answer:** `C, E`

**Correct answer: Hardware maintenance**

Hardware maintenance is the responsibility of AWS. This includes the physical security of the data centers, replacing failed hardware components, and ensuring the underlying infrastructure is functioning correctly. The customer does not have access to the physical hardware and relies on AWS to maintain it.

**Correct answer: Creating hypervisors**

AWS is responsible for creating and maintaining the hypervisors that enable virtualization. Customers use these hypervisors to run their EC2 instances, but AWS manages the underlying hypervisor technology. This is a core part of the AWS infrastructure.

**Incorrect:**

**A. Monitoring network performance** - While AWS provides tools and services to monitor network performance (e.g., CloudWatch), the customer is ultimately responsible for monitoring the performance of their applications and network configurations within their VPC. AWS monitors the underlying network infrastructure, but the customer monitors their specific network configurations and traffic.

**B. Configuring Access Control Lists (ACLs)** - Configuring Access Control Lists (ACLs) is the responsibility of the customer. ACLs are used to control traffic at the subnet level within a VPC. Customers define the rules to allow or deny traffic based on source and destination IP addresses, ports, and protocols. AWS provides the functionality, but the customer configures it.

**E. Installing software on EC2 instances** - Installing software on EC2 instances is the responsibility of the customer. EC2 instances are virtual servers that customers manage. Customers choose the operating system and are responsible for installing and configuring any software required for their applications.

</details>

---

### Question 178 — `CLF-U0810` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.2: Container Technologies (ECS, EKS, Fargate, ECR)*

**Which AWS Service is used to manage user permissions?**

- A) Security Groups.
- B) Amazon ECS.
- C) AWS IAM.
- D) AWS Support.

<details>
<summary><strong>Reveal Answer & Explanation (Question 178)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS IAM**

AWS Identity and Access Management (IAM) is the AWS service used to manage user permissions and control access to AWS resources. IAM enables you to create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. IAM is a fundamental service for security and compliance in the AWS Cloud. You can define granular permissions specifying which actions a user or group can perform on which resources. This follows the principle of least privilege, granting only the permissions required to perform a specific task.

**Incorrect:**

**A. Security Groups** - Security Groups act as a virtual firewall for your EC2 instances to control inbound and outbound traffic at the instance level. While they are related to security, they do not manage user permissions across the AWS account.

**B. AWS Support** - AWS Support provides technical assistance and guidance for using AWS services. It does not manage user permissions.

**D. Amazon ECS** - Amazon Elastic Container Service (ECS) is a container orchestration service that allows you to run and manage Docker containers. It does not directly manage user permissions.

</details>

---

### Question 179 — `CLF-U0007` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**What should you do in order to keep the data on EBS volumes safe? (Choose TWO)**

- A) Regularly update firmware on EBS devices.
- B) Create EBS snapshots.
- C) Ensure that EBS data is encrypted at rest.
- D) Store a backup daily in an external drive.
- E) Prevent any unauthorized access to AWS data centers.

<details>
<summary><strong>Reveal Answer & Explanation (Question 179)</strong></summary>

**Correct Answer:** `B, C`

**Correct answer: Create EBS snapshots**

EBS snapshots are point-in-time copies of your EBS volumes. They are stored in Amazon S3 and provide a durable backup of your data. In the event of data loss or corruption on your EBS volume, you can restore it from a snapshot. This is a fundamental data protection strategy for EBS volumes.

**Correct answer: Ensure that EBS data is encrypted at rest**

Encrypting EBS volumes at rest protects the data stored on them from unauthorized access. If an unauthorized user gains physical access to the underlying storage, the data remains unreadable without the encryption key. AWS provides EBS encryption using keys managed by AWS Key Management Service (KMS) or you can use your own keys.

**Incorrect:**

**B. Store a backup daily in an external drive** - While backing up data to an external drive is a valid backup strategy in general, it's not the most practical or scalable solution for EBS volumes in the AWS cloud. EBS snapshots are a more integrated and efficient method. Transferring large volumes of data to an external drive daily would be time-consuming and introduce logistical challenges.

**D. Regularly update firmware on EBS devices** - EBS is a managed service provided by AWS. AWS is responsible for maintaining the underlying infrastructure, including firmware updates. Users do not have direct access to the physical EBS devices or the ability to update their firmware.

**E. Prevent any unauthorized access to AWS data centers** - While physical security of AWS data centers is paramount, it's AWS's responsibility, not the user's. Furthermore, even with strong physical security, logical security measures like encryption and backups are still crucial for protecting data. This option addresses a broader security concern but is not a specific action a user would take to protect data on EBS volumes.

</details>

---

### Question 180 — `CLF-U0012` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A company is deploying a new two-tier web application in AWS. Where should the most frequently accessed data be stored so that the application’s response time is optimal?**

- A) AWS OpsWorks.
- B) AWS Storage Gateway.
- C) Amazon EBS volume.
- D) Amazon ElastiCache.

<details>
<summary><strong>Reveal Answer & Explanation (Question 180)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Amazon ElastiCache**

Amazon ElastiCache is a fully managed, in-memory data store and caching service by AWS. It is designed to improve the performance of web applications by retrieving information from fast, managed, in-memory caches, instead of relying entirely on slower disk-based databases. By caching frequently accessed data, ElastiCache reduces database load, improves application responsiveness, and enhances the overall user experience. This makes it the optimal choice for storing the most frequently accessed data to minimize response time.

**Incorrect:**

**A. AWS Storage Gateway** - AWS Storage Gateway is a hybrid cloud storage service that connects on-premises environments to AWS Cloud storage. It is used for backup and disaster recovery, tiered storage, and migration. It is not designed for caching frequently accessed data for optimal application response time.

**B. Amazon EBS volume** - Amazon EBS (Elastic Block Storage) volumes provide block-level storage for use with EC2 instances. While EBS volumes offer persistent storage, they are not optimized for caching frequently accessed data for rapid retrieval. Accessing data from an EBS volume is slower than accessing data from an in-memory cache like ElastiCache.

**C. AWS OpsWorks** - AWS OpsWorks is a configuration management service that helps you automate operational tasks like server configuration, deployment, and scaling. It does not provide data storage or caching capabilities and is therefore not suitable for storing frequently accessed data to optimize application response time.

</details>

---

### Question 181 — `CLF-U0023` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which of the following is not a benefit of Amazon S3? (Choose TWO)**

- A) Amazon S3 provides unlimited storage for any type of data.
- B) Amazon S3 can run any type of application or backend system.
- C) Amazon S3 stores any number of objects, but with object size limits.
- D) Amazon S3 can be scaled manually to store and retrieve any amount of data from anywhere.
- E) Amazon S3 provides 99.999999999% (11 9’s) of data durability.

<details>
<summary><strong>Reveal Answer & Explanation (Question 181)</strong></summary>

**Correct Answer:** `B, D`

**Correct answer: Amazon S3 can run any type of application or backend system**

Amazon S3 is object storage. It stores data as objects within buckets. It is not a compute service and cannot run applications or backend systems. Services like EC2, ECS, EKS, or Lambda are used for running applications.

**Correct answer: Amazon S3 can be scaled manually to store and retrieve any amount of data from anywhere**

Amazon S3 is designed to automatically scale to handle virtually any amount of data. You don't manually scale S3. It scales automatically based on demand. S3 is designed for high availability and scalability without manual intervention.

**Incorrect:**

**A. Amazon S3 stores any number of objects, but with object size limits** - Amazon S3 can store virtually unlimited number of objects. However, individual objects have a size limit of 5 TB. This statement is a benefit of S3.

**C. Amazon S3 provides 99.999999999% (11 9’s) of data durability** - Amazon S3 is designed for 99.999999999% (11 9's) of data durability. This is a key benefit, indicating a very low risk of data loss.

**D. Amazon S3 provides unlimited storage for any type of data** - Amazon S3 provides virtually unlimited storage, meaning you can store any amount of data up to the object size limit. This is a benefit of using S3.

</details>

---

### Question 182 — `CLF-U0033` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Your company is designing a new application that will store and retrieve photos and videos. Which of the following services should you recommend as the underlying storage mechanism?**

- A) Amazon EBS.
- B) Amazon SQS.
- C) Amazon S3.
- D) Amazon Instance store.

<details>
<summary><strong>Reveal Answer & Explanation (Question 182)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon S3**

Amazon S3 (Simple Storage Service) is object storage built for storing and retrieving any amount of data from anywhere. It is designed for high durability, availability, and scalability, making it ideal for storing photos and videos for a new application. S3 offers various storage classes optimized for different access patterns and cost requirements, such as S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, and S3 Glacier. This flexibility allows you to choose the most cost-effective storage option based on how frequently the data is accessed.

**Incorrect:**

**B. Amazon EBS** - Amazon EBS (Elastic Block Storage) provides block-level storage volumes for use with EC2 instances. While you could technically store photos and videos on an EBS volume attached to an EC2 instance, it's not the most efficient or scalable solution for this use case. EBS is better suited for persistent storage for operating systems, databases, and applications that require direct block-level access. S3 is more cost-effective and easier to manage for storing large amounts of unstructured data like photos and videos.

**C. Amazon Instance store** - Amazon Instance Store provides temporary block-level storage for EC2 instances. Data stored in instance store is ephemeral, meaning it is lost when the instance is stopped, terminated, or fails. This makes it unsuitable for storing important data like photos and videos that need to be persistently stored.

**D. Amazon SQS** - Amazon SQS (Simple Queue Service) is a message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It is used for sending, storing, and receiving messages between software components, not for storing large files like photos and videos.

</details>

---

### Question 183 — `CLF-U0041` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**In your on-premises environment, you can create as many virtual servers as you need from a single template. What can you use to perform the same in AWS?**

- A) IAM.
- B) An internet gateway.
- C) EBS Snapshot.
- D) AMI.

<details>
<summary><strong>Reveal Answer & Explanation (Question 183)</strong></summary>

**Correct Answer:** `D`

**Correct answer: AMI**

An Amazon Machine Image (AMI) provides the information required to launch an instance, which is a virtual server in the cloud. You can think of it as a template for your virtual server. AMIs include the operating system, application server, and applications required to launch your instance. You can use AWS-provided AMIs, community AMIs, or create your own custom AMIs. Creating multiple instances from a single AMI is a fundamental way to quickly provision and scale your applications in AWS.

**Incorrect:**

**B. An internet gateway** - An internet gateway allows your VPC to connect to the internet. It's not related to creating virtual servers from a template.

**C. IAM** - IAM (Identity and Access Management) controls access to AWS services and resources. While important for security, it doesn't serve as a template for creating virtual servers.

**D. EBS Snapshot** - An EBS snapshot is a point-in-time copy of an EBS volume. While you can create a volume from a snapshot, and then create an AMI from that volume, the EBS snapshot itself is not the direct equivalent of a server template. The AMI is the correct answer because it contains the OS and software configuration.

</details>

---

### Question 184 — `CLF-U0048` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Where can you store files in AWS? (Choose TWO)**

- A) Amazon EFS.
- B) Amazon SNS.
- C) Amazon EBS.
- D) Amazon ECS.
- E) Amazon EMR.

<details>
<summary><strong>Reveal Answer & Explanation (Question 184)</strong></summary>

**Correct Answer:** `A, C`

**Correct answer: Amazon EFS**

Amazon Elastic File System (EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. You can use it to store files that need to be shared between multiple EC2 instances or accessed by other services. EFS grows and shrinks automatically as you add and remove files, so you don't need to provision storage in advance.

**Correct answer: Amazon EBS**

Amazon Elastic Block Storage (EBS) provides block-level storage volumes for use with EC2 instances. EBS volumes are like virtual hard drives that you can attach to your EC2 instances to store persistent data. EBS is suitable for storing operating systems, applications, and data that require fast and consistent performance.

**Incorrect:**

**B. Amazon ECS** - Amazon Elastic Container Service (ECS) is a container orchestration service that allows you to run, manage, and scale containerized applications. It does not directly store files; instead, it uses storage solutions like EFS or EBS to persist data used by the containers.

**D. Amazon SNS** - Amazon Simple Notification Service (SNS) is a messaging service for sending notifications. It is not used for storing files. SNS is used for sending messages to subscribers via various protocols, such as email, SMS, and HTTP.

**E. Amazon EMR** - Amazon EMR (Elastic MapReduce) is a managed cluster platform that lets you run big data frameworks such as Apache Hadoop and Apache Spark. While EMR clusters process data, they typically use storage services like S3 or HDFS (on EBS volumes) for storing the data, rather than EMR itself being a storage service.

</details>

---

### Question 185 — `CLF-U0049` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which AWS service can be used to store and reliably deliver messages across distributed systems?**

- A) Amazon Simple Queue Service.
- B) AWS Storage Gateway.
- C) Amazon Simple Email Service.
- D) Amazon Simple Storage Service.

<details>
<summary><strong>Reveal Answer & Explanation (Question 185)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon Simple Queue Service**

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS allows you to send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be always available. This makes it ideal for reliably delivering messages across distributed systems.

**Incorrect:**

**B. Amazon Simple Email Service** - Amazon Simple Email Service (SES) is a cloud-based email sending service designed to help digital marketers and application developers send marketing, notification, and transactional emails. It is not designed for general-purpose message queuing between distributed systems.

**C. AWS Storage Gateway** - AWS Storage Gateway is a hybrid cloud storage service that lets you seamlessly connect on-premises environments to AWS Cloud. It provides on-premises access to virtually unlimited cloud storage. It is not a message queuing service.

**D. Amazon Simple Storage Service** - Amazon Simple Storage Service (S3) is an object storage service that offers scalability, data availability, security, and performance. While S3 can be used to store data related to messages, it does not provide the message queuing and delivery functionality of SQS.

</details>

---

### Question 186 — `CLF-U0052` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**What is the primary storage service used by Amazon RDS database instances?**

- A) Amazon Glacier.
- B) Amazon EBS.
- C) Amazon EFS.
- D) Amazon S3.

<details>
<summary><strong>Reveal Answer & Explanation (Question 186)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Amazon EBS**

Amazon RDS (Relational Database Service) primarily uses Amazon EBS (Elastic Block Storage) volumes for its database storage. When you create an RDS instance, you specify the size and type of EBS volume to be associated with the instance. This EBS volume is where the database data, logs, and other persistent data are stored. EBS provides durable, block-level storage that is ideal for the transactional nature of databases. RDS manages the EBS volume on your behalf, handling tasks like backups, snapshots, and encryption.

**Incorrect:**

**B. AWS Storage Gateway** - AWS Storage Gateway is a hybrid cloud storage service that connects on-premises environments to AWS cloud storage. It is not directly used as the primary storage for RDS database instances. Storage Gateway is used for integrating on-premises data with AWS, not for providing the underlying storage for RDS.

**C. Amazon EFS** - Amazon EFS (Elastic File System) provides a scalable, elastic, cloud-native NFS file system. While EFS can be used in conjunction with compute services like EC2, it is not the primary storage mechanism for Amazon RDS. RDS requires block storage, which is provided by EBS, rather than a file system like EFS.

**D. Amazon S3** - Amazon S3 (Simple Storage Service) is object storage designed for storing and retrieving any amount of data. While S3 can be used for database backups and storing other related files, it is not used as the primary storage for the database itself. RDS requires block storage for its database files, which is provided by EBS.

</details>

---

### Question 187 — `CLF-U0054` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which of the following AWS services is designed with native Multi-AZ fault tolerance in mind? (Choose TWO)**

- A) Amazon Redshift.
- B) AWS Snowball.
- C) Amazon Simple Storage Service.
- D) Amazon EBS.
- E) Amazon DynamoDB.

<details>
<summary><strong>Reveal Answer & Explanation (Question 187)</strong></summary>

**Correct Answer:** `C, E`

**Correct answer: Amazon DynamoDB**

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. It is designed with native Multi-AZ fault tolerance. DynamoDB automatically replicates data across multiple Availability Zones within an AWS Region to provide high availability and data durability. This means that even if one Availability Zone experiences an outage, your DynamoDB table remains available and accessible.

**Correct answer: Amazon Simple Storage Service**

Amazon S3 (Simple Storage Service) is an object storage service offering industry-leading scalability, data availability, security, and performance. S3 is inherently designed for high availability and durability by storing data across multiple devices and facilities. While not explicitly Multi-AZ in the same way as a database, S3's architecture provides resilience against the loss of an Availability Zone. Data is automatically replicated across multiple facilities.

**Incorrect:**

**B. AWS Snowball** - AWS Snowball is a data migration service that uses physical storage devices to transfer large amounts of data into and out of AWS. It is not designed with native Multi-AZ fault tolerance in mind because it is a physical device used for data transport, not a service running within AWS Availability Zones.

**C. Amazon Redshift** - Amazon Redshift is a data warehouse service. While Redshift supports deploying clusters in multiple Availability Zones for enhanced availability, this is not a native, built-in feature in the same way as DynamoDB or S3. Redshift requires specific configuration to enable Multi-AZ, and it is not automatically enabled by default. Therefore, it's not considered to be designed with native Multi-AZ fault tolerance.

**E. Amazon EBS** - Amazon EBS (Elastic Block Storage) provides block-level storage volumes for use with EC2 instances. EBS volumes are AZ-specific. While you can create snapshots of EBS volumes and restore them to other AZs, EBS volumes themselves are not inherently Multi-AZ. To achieve high availability with EBS, you would typically use RAID configurations or replicate data at the application level, which is not native Multi-AZ fault tolerance.

</details>

---

### Question 188 — `CLF-U0077` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A developer needs to set up an SSL security certificate for a client's eCommerce website in order to use the HTTPS protocol. Which of the following AWS services can be used to deploy the required SSL server certificates? (Choose TWO)**

- A) Amazon Route 53.
- B) AWS ACM.
- C) AWS Directory Service.
- D) AWS Identity & Access Management.
- E) AWS Data Pipeline.

<details>
<summary><strong>Reveal Answer & Explanation (Question 188)</strong></summary>

**Correct Answer:** `A, B`

**Correct answer: AWS Identity & Access Management**

AWS IAM can be used to securely store and manage SSL/TLS certificates. While AWS Certificate Manager (ACM) is the preferred service for provisioning, managing, and deploying SSL/TLS certificates with AWS services, IAM provides an alternative method for uploading and managing certificates, especially when they are obtained from a third-party Certificate Authority. The certificate can then be used with services like Elastic Load Balancing (ELB) or Amazon CloudFront.

**Correct answer: AWS ACM**

AWS Certificate Manager (ACM) is the preferred AWS service for provisioning, managing, and deploying SSL/TLS certificates for use with AWS services. ACM integrates directly with services like Elastic Load Balancing, Amazon CloudFront, and API Gateway to simplify the process of enabling HTTPS for websites and applications. ACM can provision public and private SSL/TLS certificates.

**Incorrect:**

**B. AWS Directory Service** - AWS Directory Service is used to connect your AWS resources with an existing on-premises Microsoft Active Directory or to set up a new directory in the AWS Cloud. It is not used for deploying SSL certificates.

**C. Amazon Route 53** - Amazon Route 53 is a scalable DNS (Domain Name System) web service. While Route 53 is essential for directing internet traffic to your website, it does not directly deploy or manage SSL certificates. You would use Route 53 to point your domain to a load balancer or CloudFront distribution that is configured with an SSL certificate managed by ACM or IAM.

**E. AWS Data Pipeline** - AWS Data Pipeline is a service for moving and processing data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals. It has nothing to do with SSL certificate management or deployment.

</details>

---

### Question 189 — `CLF-U0084` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A company is planning to migrate a database with high read/write activity to AWS. What is the best storage option to use?**

- A) AWS Storage Gateway.
- B) Amazon S3.
- C) Amazon EBS.
- D) Amazon Glacier.

<details>
<summary><strong>Reveal Answer & Explanation (Question 189)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon EBS**

Amazon Elastic Block Storage (EBS) provides block-level storage volumes for use with EC2 instances. EBS volumes are designed for high performance and low latency, making them suitable for databases with high read/write activity. EBS volumes can be attached to EC2 instances and formatted with a file system, allowing the database to directly access the storage. EBS also offers features like snapshots for backups and the ability to increase volume size without downtime.

**Incorrect:**

**A. Amazon ECR** - Amazon Elastic Container Registry (ECR) is a fully managed container registry that allows you to store, manage, and deploy Docker container images. It is not suitable for storing database data with high read/write activity.

**C. Amazon S3** - Amazon Simple Storage Service (S3) is object storage, designed for storing and retrieving large amounts of data. While S3 is highly scalable and durable, it is not optimized for the low-latency, high-performance requirements of a database with high read/write activity. S3 is better suited for storing backups, static assets, or infrequently accessed data.

**D. AWS Storage Gateway** - AWS Storage Gateway is a hybrid cloud storage service that connects on-premises applications to AWS storage. While it can be used to store data in AWS, it is not the best option for a database with high read/write activity that is being migrated to AWS. Storage Gateway introduces latency due to the network connection between the on-premises environment and AWS. EBS provides direct, low-latency storage for EC2 instances.

</details>

---

### Question 190 — `CLF-U0106` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which AWS Service helps enterprises extend their on-premises storage to AWS in a cost-effective manner?**

- A) AWS Data Pipeline.
- B) AWS Storage Gateway.
- C) Amazon Aurora.
- D) Amazon EFS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 190)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS Storage Gateway**

AWS Storage Gateway is a hybrid cloud storage service that allows on-premises applications to seamlessly use AWS cloud storage. It connects an organization's on-premises environment to AWS, enabling them to store data in AWS while maintaining local access to frequently used data. This is cost-effective because infrequently accessed data can be stored in cheaper AWS storage tiers, while frequently accessed data remains locally accessible. Storage Gateway supports various storage types, including file, volume, and tape.

**Incorrect:**

**A. Amazon EFS** - Amazon EFS (Elastic File System) provides scalable, elastic, cloud-native file storage for use with AWS Cloud services and on-premises resources. While EFS can be mounted on-premises using Direct Connect or VPN, it's primarily designed as a cloud-native service. It doesn't directly extend on-premises storage in the same way as Storage Gateway, which offers different gateway types for various use cases, including file, volume, and tape storage.

**B. Amazon Aurora** - Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. It is a database service, not a storage service designed to extend on-premises storage to the cloud. Aurora is used for database workloads, not for general-purpose storage extension.

**C. AWS Data Pipeline** - AWS Data Pipeline is a data orchestration service that helps you move and transform data between different AWS compute and storage services, as well as on-premises data sources. While it can be used to move data to AWS, it doesn't provide a direct mechanism for extending on-premises storage in a cost-effective and seamless manner like AWS Storage Gateway.

</details>

---

### Question 191 — `CLF-U0111` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A customer is seeking to store objects in their AWS environment and to make those objects downloadable over the internet. Which AWS Service can be used to accomplish this?**

- A) Amazon EBS.
- B) Amazon EFS.
- C) Amazon S3.
- D) Amazon Instance Store.

<details>
<summary><strong>Reveal Answer & Explanation (Question 191)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon S3**

Amazon S3 (Simple Storage Service) is an object storage service that offers scalability, data availability, security, and performance. It is designed to store and retrieve any amount of data from anywhere. S3 buckets can be configured to allow public access, making objects downloadable over the internet. This aligns directly with the customer's requirement to store objects and make them downloadable.

**Incorrect:**

**A. Amazon EBS** - Amazon EBS (Elastic Block Storage) provides block-level storage volumes for use with EC2 instances. While you can store data on EBS volumes, they are not directly accessible over the internet. EBS volumes are attached to EC2 instances and are used for persistent storage for those instances, not for direct public downloads.

**B. Amazon Instance Store** - Amazon Instance Store provides temporary block-level storage for EC2 instances. Data stored on instance store volumes is ephemeral, meaning it is lost when the instance is stopped, terminated, or fails. It's not suitable for long-term storage or for making objects available for download over the internet.

**D. Amazon EFS** - Amazon EFS (Elastic File System) provides a scalable, elastic, cloud-native NFS file system. While EFS can be used to store files, it is designed for shared file storage between multiple EC2 instances. It is not directly designed for making objects downloadable over the internet in the same way that S3 is. While you *could* configure an EC2 instance to serve files from EFS, S3 is the more direct and appropriate service for this use case.

</details>

---

### Question 192 — `CLF-U0570` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which S3 storage class is best for data with unpredictable access patterns?**

- A) Amazon S3 Intelligent-Tiering.
- B) Amazon S3 Glacier Flexible Retrieval.
- C) Amazon S3 Standard.
- D) Amazon S3 Standard-Infrequent Access.

<details>
<summary><strong>Reveal Answer & Explanation (Question 192)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon S3 Intelligent-Tiering**

Amazon S3 Intelligent-Tiering is designed to optimize storage costs automatically when data access patterns are unpredictable or unknown. It works by moving objects between frequent, infrequent, and archive access tiers based on changing access patterns. This eliminates the need to manually move data to different storage classes to save money. It automatically transitions data to the most cost-effective access tier without performance impact or operational overhead. This is ideal when you don't know how often data will be accessed.

**Incorrect:**

**A. Amazon S3 Standard-Infrequent Access** - S3 Standard-IA is suitable for data that is accessed less frequently but requires rapid access when needed. While it offers lower storage costs than S3 Standard, it's not the best choice for unpredictable access patterns because it doesn't automatically optimize storage costs based on changing access patterns. You would need to manually move data to this class.

**C. Amazon S3 Standard** - S3 Standard is designed for frequently accessed data. While it provides high availability and performance, it is not cost-effective for data with unpredictable access patterns, as you'll pay the higher Standard rate even when the data is infrequently accessed. Intelligent-Tiering is better suited for cost optimization in this scenario.

**D. Amazon S3 Glacier Flexible Retrieval** - Amazon S3 Glacier Flexible Retrieval (formerly S3 Glacier) is designed for long-term archive storage with infrequent access and retrieval times ranging from minutes to hours. It is not suitable for data that may need to be accessed with unpredictable frequency, as retrieval can be slower and more costly than other S3 storage classes. It is best for archival data where immediate access is not a primary concern.

</details>

---

### Question 193 — `CLF-U0006` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**A company has decided to migrate its Oracle database to AWS. Which AWS service can help achieve this without negatively impacting the functionality of the source database?**

- A) AWS OpsWorks.
- B) AWS Database Migration Service.
- C) AWS Server Migration Service.
- D) AWS Application Discovery Service.

<details>
<summary><strong>Reveal Answer & Explanation (Question 193)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS Database Migration Service**

AWS Database Migration Service (DMS) is a cloud service that enables you to migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime. DMS supports homogeneous migrations (e.g., Oracle to Oracle) and heterogeneous migrations (e.g., Oracle to Amazon Aurora). It can migrate data, database schemas, stored procedures, and other database objects. This makes it ideal for migrating an Oracle database to AWS without negatively impacting the functionality of the source database.

**Incorrect:**

**A. AWS Application Migration Service** - AWS Application Migration Service (MGN) is primarily used for migrating entire servers and applications to AWS, not specifically for database migrations. While it could be used in conjunction with other tools, it's not the primary service for migrating databases while minimizing impact on the source database's functionality.

**B. AWS OpsWorks** - AWS OpsWorks is a configuration management service that helps you automate operational tasks like server configuration, deployment, and scaling. It is not designed for database migration. It's focused on managing application stacks and infrastructure, not moving data between databases.

**D. AWS Application Discovery Service** - AWS Application Discovery Service helps you gather information about your on-premises servers to plan a migration to AWS. It discovers server specifications, performance data, and dependencies. While useful for planning, it does not perform the actual database migration itself.

</details>

---

### Question 194 — `CLF-U0016` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Your company has a data store application that requires access to a NoSQL database. Which AWS database offering would meet this requirement?**

- A) Amazon Aurora.
- B) Amazon DynamoDB.
- C) Amazon Elastic Block Store.
- D) Amazon Redshift.

<details>
<summary><strong>Reveal Answer & Explanation (Question 194)</strong></summary>

**Correct Answer:** `B`

**Correct answer: Amazon DynamoDB**

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. It is designed for running high-performance applications at any scale. DynamoDB supports both document and key-value data models, making it suitable for a wide range of use cases that require a flexible and scalable NoSQL database.

**Incorrect:**

**A. Amazon Aurora** - Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. It is not a NoSQL database.

**B. Amazon Redshift** - Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. It is designed for analytical workloads and is not a NoSQL database.

**C. Amazon Elastic Block Store** - Amazon Elastic Block Store (EBS) provides block-level storage volumes for use with EC2 instances. It is not a database service itself, but rather a storage solution that can be used by databases.

</details>

---

### Question 195 — `CLF-U0027` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What is the AWS database service that allows you to upload data structured in key-value format?**

- A) Amazon DynamoDB.
- B) Amazon Aurora.
- C) Amazon Redshift.
- D) Amazon RDS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 195)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon DynamoDB**

Amazon DynamoDB is a fully managed NoSQL database service that supports key-value and document data structures. It's designed for high performance and scalability. You can upload data structured in key-value format directly into DynamoDB tables. Each item in a DynamoDB table is uniquely identified by a key, and it can contain attributes (values) associated with that key.

**Incorrect:**

**A. Amazon Aurora** - Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. It's not designed for key-value data storage. It requires a structured schema and SQL queries.

**C. Amazon Redshift** - Amazon Redshift is a fully managed data warehouse service designed for large-scale data analytics. It's not suitable for storing data in a simple key-value format. It's optimized for complex queries on large datasets.

**D. Amazon RDS** - Amazon RDS (Relational Database Service) is a managed service that allows you to run relational databases like MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB. While you can store data in key-value pairs within a relational database, RDS itself is not specifically designed or optimized for this purpose. DynamoDB is the better choice for native key-value storage.

</details>

---

### Question 196 — `CLF-U0028` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**You work as an on-premises MySQL DBA. The work of database configuration, backups, patching, and DR can be time-consuming and repetitive. Your company has decided to migrate to the AWS Cloud. Which of the following can help save time on database maintenance so you can focus on data architecture and performance?**

- A) Amazon RDS.
- B) Amazon Redshift.
- C) Amazon DynamoDB.
- D) Amazon CloudWatch.

<details>
<summary><strong>Reveal Answer & Explanation (Question 196)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon RDS**

Amazon Relational Database Service (RDS) is a managed database service that simplifies the setup, operation, and scaling of relational databases in the AWS Cloud. RDS automates many of the time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups. By using RDS, the DBA can focus on higher-value activities such as data architecture, schema design, query optimization, and performance tuning, rather than the repetitive tasks of database maintenance. RDS supports various database engines, including MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.

**Incorrect:**

**B. Amazon CloudWatch** - Amazon CloudWatch is a monitoring and observability service. While CloudWatch is essential for monitoring the performance and health of your database, it does not automate database maintenance tasks like patching or backups. It helps you observe and react to issues, but doesn't directly reduce the time spent on routine maintenance.

**C. Amazon Redshift** - Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. Redshift is designed for analytics and business intelligence, not for general-purpose database tasks. While it simplifies data warehousing, it is not a replacement for a MySQL database and would not be suitable for the described scenario.

**D. Amazon DynamoDB** - Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. While DynamoDB reduces operational overhead, it is a NoSQL database, not a relational database like MySQL. Migrating from MySQL to DynamoDB would require significant application changes and is not the best solution for simply reducing database maintenance time while retaining the relational database paradigm.

</details>

---

### Question 197 — `CLF-U0034` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What does Amazon ElastiCache provide?**

- A) In-memory caching for read-heavy applications.
- B) An Ehcache compatible in-memory data store.
- C) An online software store that allows Customers to launch pre-configured software with just few clicks.
- D) A domain name system in the cloud.

<details>
<summary><strong>Reveal Answer & Explanation (Question 197)</strong></summary>

**Correct Answer:** `A`

**Correct answer: In-memory caching for read-heavy applications**

Amazon ElastiCache is a fully managed, in-memory data store and caching service by AWS. It supports two open-source caching engines: Redis and Memcached. ElastiCache is designed to improve the performance of web applications by retrieving information from fast, managed, in-memory caches, instead of relying solely on slower disk-based databases. This is particularly beneficial for read-heavy applications where the same data is frequently accessed, reducing latency and improving overall application responsiveness.

**Incorrect:**

**A. A domain name system in the cloud** - This describes Amazon Route 53, which is AWS's scalable and highly available Domain Name System (DNS) web service. ElastiCache is not related to DNS or domain name management.

**B. An Ehcache compatible in-memory data store** - While ElastiCache provides in-memory data storage, it is primarily compatible with Redis and Memcached, not Ehcache. Ehcache is a Java-based cache. While you *could* potentially use Ehcache in conjunction with an application that also uses ElastiCache, ElastiCache itself is not specifically "Ehcache compatible".

**D. An online software store that allows Customers to launch pre-configured software with just few clicks** - This describes AWS Marketplace. AWS Marketplace is a digital catalog with thousands of software listings from independent software vendors that make it easy to find, test, buy, and deploy software that runs on AWS. ElastiCache is a caching service, not a software marketplace.

</details>

---

### Question 198 — `CLF-U0039` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What is the AWS service that provides you the highest level of control over the underlying virtual infrastructure?**

- A) Amazon Redshift.
- B) Amazon DynamoDB.
- C) Amazon EC2.
- D) Amazon RDS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 198)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon EC2**

Amazon EC2 (Elastic Compute Cloud) provides the most control over the underlying virtual infrastructure. With EC2, you choose the operating system, instance type (CPU, memory, storage), networking, and security settings. You have root access to the instance, allowing you to install and configure software as needed. This level of control is essential for applications that require specific configurations or custom environments.

**Incorrect:**

**A. Amazon RDS** - Amazon RDS (Relational Database Service) is a managed database service. While you can configure database parameters, you don't have control over the underlying operating system or server infrastructure. AWS manages patching, backups, and other administrative tasks.

**B. Amazon Redshift** - Amazon Redshift is a data warehouse service. Similar to RDS, Redshift is a managed service, abstracting away the underlying infrastructure. You configure the data warehouse, but AWS handles the server management.

**D. Amazon DynamoDB** - Amazon DynamoDB is a NoSQL database service that is fully managed. You have very little control over the underlying infrastructure. DynamoDB focuses on scalability and availability, with AWS handling all the server management and maintenance.

</details>

---

### Question 199 — `CLF-U0046` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Using Amazon RDS falls under the shared responsibility model. Which of the following are customer responsibilities? (Choose TWO)**

- A) Building the relational database schema.
- B) Performing backups.
- C) Managing the database settings.
- D) Patching the database software.
- E) Installing the database software.

<details>
<summary><strong>Reveal Answer & Explanation (Question 199)</strong></summary>

**Correct Answer:** `A, C`

**Correct answer: Building the relational database schema**

As the customer, you are responsible for designing and creating the database schema within your Amazon RDS instance. This includes defining tables, relationships, indexes, and other database objects that structure your data. AWS manages the underlying infrastructure, but the data model is your responsibility.

**Correct answer: Managing the database settings**

While AWS manages the underlying infrastructure, the customer is responsible for configuring database settings such as character sets, time zones, and other database-specific parameters. These settings affect how the database operates and stores data, and are therefore the customer's responsibility to manage appropriately.

**Incorrect:**

**B. Installing the database software** - AWS handles the installation of the database software (e.g., MySQL, PostgreSQL, SQL Server) when you provision an RDS instance. The customer selects the database engine and version, but AWS takes care of the installation process.

**D. Performing backups** - While customers can initiate backups, AWS RDS automatically performs backups of your database. These automated backups are a key feature of RDS and are managed by AWS. Customers are responsible for configuring backup retention policies, but the actual backup process is handled by AWS.

**E. Patching the database software** - AWS is responsible for patching the database software to ensure security and stability. This includes applying security updates and bug fixes to the underlying database engine. Customers are typically notified of maintenance windows during which patching will occur.

</details>

---

### Question 200 — `CLF-U0047` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**A company has a large amount of structured data stored in their on-premises data center. They are planning to migrate all the data to AWS, what is the most appropriate AWS database option?**

- A) Amazon DynamoDB.
- B) Amazon SNS.
- C) Amazon RDS.
- D) Amazon ElastiCache.

<details>
<summary><strong>Reveal Answer & Explanation (Question 200)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon RDS**

Amazon Relational Database Service (RDS) is the most appropriate choice for migrating structured data from an on-premises data center to AWS. RDS supports various database engines like MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB. Since the data is structured, it likely resides in a relational database on-premises. RDS allows you to easily migrate this data to a compatible database engine in the AWS cloud, maintaining the relational structure and integrity of the data. RDS simplifies database management tasks such as patching, backups, and scaling.

**Incorrect:**

**B. Amazon DynamoDB** - Amazon DynamoDB is a NoSQL database service. It's suitable for unstructured or semi-structured data, or when you need extreme scalability and performance. Migrating structured data to DynamoDB would require significant data transformation and application changes, making it less appropriate than RDS.

**C. Amazon ElastiCache** - Amazon ElastiCache is a caching service that supports Memcached and Redis. It's used to improve the performance of applications by caching frequently accessed data. It is not a database for storing large amounts of structured data.

**D. Amazon SNS** - Amazon Simple Notification Service (SNS) is a messaging service for sending notifications. It is not a database service and is not suitable for storing or migrating structured data.

</details>

---

### Question 201 — `CLF-U0065` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What is the AWS data warehouse service that supports a high level of query performance on large amounts of datasets?**

- A) Amazon Redshift.
- B) Amazon Kinesis.
- C) Amazon DynamoDB.
- D) Amazon RDS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 201)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon Redshift**

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. It is designed for online analytical processing (OLAP) and business intelligence (BI) applications, enabling you to run complex analytical queries against large datasets with high performance. Redshift uses columnar storage, data compression, and massively parallel processing (MPP) to achieve fast query execution. This makes it ideal for analyzing large volumes of data to gain insights and make data-driven decisions.

**Incorrect:**

**A. Amazon RDS** - Amazon Relational Database Service (RDS) is a collection of managed relational database services. While RDS can handle large datasets, it is optimized for online transaction processing (OLTP) workloads, which involve frequent, small transactions. It is not designed for the complex analytical queries that are characteristic of data warehousing.

**B. Amazon Kinesis** - Amazon Kinesis is a platform for streaming data on AWS, offering services to load and analyze streaming data. Kinesis is used for real-time data ingestion and processing, not for data warehousing and complex analytical queries on large, stored datasets.

**C. Amazon DynamoDB** - Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB is well-suited for key-value and document database workloads, but it is not designed for data warehousing or complex analytical queries. It is optimized for fast reads and writes, not for analytical processing.

</details>

---

### Question 202 — `CLF-U0087` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**For managed services like Amazon DynamoDB, which of the below is AWS responsible for? (Choose TWO)**

- A) Protecting credentials.
- B) Logging access activity.
- C) Patching the database software.
- D) Operating system maintenance.
- E) Creating access policies.

<details>
<summary><strong>Reveal Answer & Explanation (Question 202)</strong></summary>

**Correct Answer:** `C, D`

**Correct answer: Patching the database software**

As a managed service, AWS handles the underlying infrastructure and software maintenance for Amazon DynamoDB. This includes patching the database software to ensure security and stability. Customers do not have access to the underlying operating system or database software to perform patching themselves.

**Correct answer: Operating system maintenance**

Operating system maintenance, including patching and updates, is the responsibility of AWS for managed services like DynamoDB. This allows customers to focus on their data and application logic without needing to manage the underlying infrastructure.

**Incorrect:**

**B. Logging access activity** - While AWS provides tools for logging access activity (e.g., CloudTrail), configuring and managing these logs, and analyzing the data, is primarily the customer's responsibility. AWS provides the capability, but the customer must enable and manage it.

**D. Protecting credentials** - While AWS provides services like IAM to help protect credentials, the ultimate responsibility for protecting credentials, such as IAM user credentials or access keys, lies with the customer. AWS provides the tools and best practices, but the customer must implement and enforce them. AWS also protects its own internal credentials used to manage the service.

**E. Creating access policies** - Creating access policies using IAM (Identity and Access Management) is the responsibility of the customer. Customers define who has access to DynamoDB resources and what actions they can perform. AWS provides the IAM service, but the customer defines the policies.

</details>

---

### Question 203 — `CLF-U0093` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What are the benefits of using DynamoDB? (Choose TWO)**

- A) Automatically scales to meet required throughput capacity.
- B) Provides resizable instances to match the current demand.
- C) Supports both relational and non-relational data models.
- D) Offers extremely low (single-digit millisecond) latency.
- E) Supports the most popular NoSQL database engines such as CouchDB and MongoDB.

<details>
<summary><strong>Reveal Answer & Explanation (Question 203)</strong></summary>

**Correct Answer:** `A, D`

**Correct answer: Offers extremely low (single-digit millisecond) latency**

DynamoDB is a NoSQL database service known for its high performance and scalability. One of its key benefits is providing extremely low latency, often in the single-digit millisecond range, for read and write operations. This makes it suitable for applications requiring real-time data access and responsiveness.

**Correct answer: Automatically scales to meet required throughput capacity**

DynamoDB is designed to automatically scale its throughput capacity based on the demands of the application. This means that as the workload increases or decreases, DynamoDB can adjust its resources to maintain consistent performance without manual intervention. This scalability is a major advantage for applications with variable traffic patterns.

**Incorrect:**

**B. Provides resizable instances to match the current demand** - DynamoDB is a serverless database. You don't manage or resize instances. Instead, you provision read and write capacity units, and DynamoDB automatically handles the underlying infrastructure scaling.

**C. Supports both relational and non-relational data models** - DynamoDB is a NoSQL database, which means it is designed for non-relational data models. Relational databases like Amazon RDS are used for relational data.

**E. Supports the most popular NoSQL database engines such as CouchDB and MongoDB** - DynamoDB is its own NoSQL database engine. It does not directly support other NoSQL database engines like CouchDB or MongoDB. While you can migrate data between these databases, DynamoDB doesn't natively run them.

</details>

---

### Question 204 — `CLF-U0804` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**An organization runs many systems and uses many AWS products. Which of the following services enables them to control how each developer interacts with these products?**

- A) AWS Identity and Access Management.
- B) Amazon RDS.
- C) Network Access Control Lists.
- D) Amazon EMR.

<details>
<summary><strong>Reveal Answer & Explanation (Question 204)</strong></summary>

**Correct Answer:** `A`

**Correct answer: AWS Identity and Access Management**

AWS Identity and Access Management (IAM) is the AWS service that enables you to control access to AWS services and resources. With IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. IAM allows you to control which actions each developer can perform on which AWS resources, ensuring that they only have the necessary permissions to do their job, following the principle of least privilege. This is crucial for security and compliance.

**Incorrect:**

**B. Network Access Control Lists** - Network Access Control Lists (NACLs) are used to control network traffic at the subnet level. They act as a firewall for controlling traffic in and out of subnets, but they do not control individual user or developer access to AWS services and resources.

**C. Amazon EMR** - Amazon EMR (Elastic MapReduce) is a managed cluster platform that lets you run big data frameworks such as Apache Hadoop and Apache Spark to process and analyze vast amounts of data. It does not directly control developer access to other AWS services.

**D. Amazon RDS** - Amazon RDS (Relational Database Service) is a managed database service that makes it easy to set up, operate, and scale a relational database in the cloud. While RDS has its own access control mechanisms for database access, it does not control developer access to other AWS services.

</details>

---

### Question 205 — `CLF-U0030` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which service is used to ensure that messages between software components are not lost if one or more components fail?**

- A) Amazon SQS.
- B) Amazon SES.
- C) AWS Direct Connect.
- D) Amazon Connect.

<details>
<summary><strong>Reveal Answer & Explanation (Question 205)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon SQS**

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS ensures that messages between software components are not lost if one or more components fail by storing them in a queue until they are successfully processed. This provides fault tolerance and reliability in distributed systems. SQS offers different queue types, including standard queues for high throughput and best-effort ordering, and FIFO (First-In-First-Out) queues for guaranteed ordering and exactly-once processing.

**Incorrect:**

**A. AWS Direct Connect** - AWS Direct Connect establishes a dedicated network connection from your on-premises environment to AWS. While it improves network performance and reduces network costs, it does not provide message queuing or ensure message delivery in the event of component failures.

**B. Amazon SES** - Amazon Simple Email Service (SES) is a cloud-based email sending service. It is used for sending transactional emails, marketing emails, and other types of email communication. It does not provide message queuing capabilities for general software components.

**D. Amazon Connect** - Amazon Connect is a cloud-based contact center service. It provides tools for managing customer interactions, such as phone calls, chat, and email. It does not provide message queuing capabilities for decoupling software components.

</details>

---

### Question 206 — `CLF-U0098` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which methods can be used by customers to interact with AWS Identity and Access Management (IAM)? (Choose TWO)**

- A) AWS CLI.
- B) AWS Security Groups.
- C) AWS SDKs.
- D) AWS Network Access Control Lists.
- E) AWS CodeCommit.

<details>
<summary><strong>Reveal Answer & Explanation (Question 206)</strong></summary>

**Correct Answer:** `A, C`

**Correct answer: AWS SDKs**

The AWS SDKs (Software Development Kits) allow developers to interact with AWS services, including IAM, programmatically. Developers can use the SDKs in various programming languages to create, update, and manage IAM users, groups, roles, and policies within their applications. The SDKs provide a set of APIs and tools that simplify the process of interacting with AWS services.

**Correct answer: AWS CLI**

The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. You can control multiple AWS services from the command line and automate them through scripts. The AWS CLI allows you to interact with IAM to manage users, groups, roles, and policies. It provides a command-line interface for making API calls to AWS services.

**Incorrect:**

**A. AWS CodeCommit** - AWS CodeCommit is a fully-managed source control service that hosts secure Git-based repositories. It is not directly used to interact with IAM. While you can use IAM roles to control access to CodeCommit repositories, CodeCommit itself is not a method for interacting with IAM.

**D. AWS Security Groups** - AWS Security Groups act as a virtual firewall for your EC2 instances to control inbound and outbound traffic. They operate at the instance level and are not directly used to interact with IAM. IAM is used to manage authentication and authorization for AWS services, while Security Groups control network traffic to EC2 instances.

**E. AWS Network Access Control Lists** - AWS Network Access Control Lists (NACLs) are an optional layer of security that act as a firewall for controlling traffic in and out of one or more subnets. NACLs operate at the subnet level and are not directly used to interact with IAM. IAM is used to manage authentication and authorization for AWS services, while NACLs control network traffic at the subnet level.

</details>

---

### Question 207 — `CLF-U0353` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**What is the purpose of having an internet gateway within a VPC?**

- A) To create a VPN connection to the VPC
- B) To allow communication between the VPC and the Internet
- C) To impose bandwidth constraints on internet traffic
- D) To load balance traffic from the Internet across Amazon EC2 instances

<details>
<summary><strong>Reveal Answer & Explanation (Question 207)</strong></summary>

**Correct Answer:** `B`

An internet gateway enables communication between resources in a VPC and the public internet, allowing instances in public subnets to send and receive traffic from the internet.
Creating a VPN connection to the VPC is the function of a Virtual Private Gateway, not an internet gateway, as VPN connections are used to link a VPC to an on-premises network. Imposing bandwidth constraints on internet traffic is not a function of any VPC gateway component, as bandwidth management is handled at the application or network policy level. Load balancing traffic from the internet across EC2 instances is the function of an Elastic Load Balancer, not an internet gateway.

</details>

---

### Question 208 — `CLF-U0038` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**An organization needs to analyze and process a large number of data sets. Which AWS service should they use?**

- A) Amazon EMR.
- B) Amazon MQ.
- C) Amazon SNS.
- D) Amazon SQS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 208)</strong></summary>

**Correct Answer:** `A`

**Correct answer: Amazon EMR**

Amazon EMR (Elastic MapReduce) is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts of data. It allows organizations to efficiently and cost-effectively process large datasets using distributed computing. EMR handles the provisioning, scaling, and management of the underlying infrastructure, enabling users to focus on their data processing tasks.

**Incorrect:**

**A. Amazon MQ** - Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ. It's used for decoupling and integrating distributed systems, not for analyzing and processing large datasets.

**B. Amazon SQS** - Amazon SQS (Simple Queue Service) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. While it can handle large volumes of messages, it's not designed for the direct analysis and processing of large datasets. It's more about queuing messages for processing by other services.

**D. Amazon SNS** - Amazon SNS (Simple Notification Service) is a fully managed messaging service for application-to-application (A2A) and application-to-person (A2P) communication. It's used for sending notifications, not for analyzing and processing large datasets.

</details>

---

### Question 209 — `CLF-U0086` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**What does AWS Service Catalog provide?**

- A) It enables customers to quickly find descriptions and use cases for AWS services.
- B) It enables customers to explore the different catalogs of AWS services.
- C) It simplifies organizing and governing commonly deployed IT services.
- D) It allows developers to deploy infrastructure on AWS using familiar programming languages.

<details>
<summary><strong>Reveal Answer & Explanation (Question 209)</strong></summary>

**Correct Answer:** `C`

**Correct answer: It simplifies organizing and governing commonly deployed IT services**

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. Service Catalog enables central governance and standardization, ensuring users deploy only approved resources, reducing risk and improving compliance. It simplifies the process for end-users to find and deploy these services, while maintaining control and visibility for IT administrators.

**Incorrect:**

**B. It allows developers to deploy infrastructure on AWS using familiar programming languages** - While developers can use programming languages to deploy infrastructure on AWS, this is primarily achieved through Infrastructure as Code (IaC) tools like AWS CloudFormation, AWS CDK (Cloud Development Kit), or Terraform, not AWS Service Catalog directly. Service Catalog focuses on cataloging and governing pre-defined services, not on enabling arbitrary infrastructure deployment via code.

**C. It enables customers to quickly find descriptions and use cases for AWS services** - While AWS provides extensive documentation and resources describing its services, this is primarily found on the AWS website and in the AWS documentation, not through AWS Service Catalog. Service Catalog focuses on managing and deploying approved IT services within an organization, not on providing general information about AWS services.

**D. It enables customers to explore the different catalogs of AWS services** - AWS Service Catalog is used to create *private* catalogs of services *within* an organization. It doesn't provide a general catalog of *all* AWS services for exploration. The AWS website and documentation serve that purpose.

</details>

---

### Question 210 — `CLF-U0095` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which AWS service can be used to send promotional text messages (SMS) to more than 200 countries worldwide?**

- A) Amazon Simple Email Service (Amazon SES).
- B) Amazon Simple Storage Service (Amazon S3).
- C) Amazon Simple Notification Service (Amazon SNS).
- D) Amazon Simple Queue Service (Amazon SQS).

<details>
<summary><strong>Reveal Answer & Explanation (Question 210)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Amazon Simple Notification Service (Amazon SNS)**

Amazon Simple Notification Service (SNS) is a fully managed messaging service that enables you to decouple microservices, distributed systems, and serverless applications. SNS provides a pub/sub (publish-subscribe) messaging model. One of the key features of SNS is its ability to send messages to a wide variety of endpoints, including SMS text messages. SNS supports sending SMS messages to more than 200 countries worldwide, making it the correct choice for sending promotional text messages globally. SNS handles the complexities of SMS delivery, such as carrier regulations and message formatting.

**Incorrect:**

**A. Amazon Simple Queue Service (Amazon SQS)** - Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS is used for asynchronous communication between components, but it is not designed for sending SMS messages to end-users. SQS queues store messages until they are retrieved by a consumer, which is different from the direct delivery of SMS messages provided by SNS.

**B. Amazon Simple Storage Service (Amazon S3)** - Amazon S3 is an object storage service that offers scalability, data availability, security, and performance. S3 is used for storing and retrieving files (objects). It is not a messaging service and cannot be used to send SMS messages.

**D. Amazon Simple Email Service (Amazon SES)** - Amazon SES is a cloud-based email sending service designed to help digital marketers and application developers send marketing, notification, and transactional emails. While SES is used for sending emails, it is not used for sending SMS messages. SNS is the AWS service specifically designed for sending SMS messages.

</details>

---

### Question 211 — `CLF-U0244` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which AWS service provides the ability to manage infrastructure as code?**

- A) AWS CodePipeline.
- B) AWS CodeDeploy.
- C) AWS Direct Connect.
- D) AWS CloudFormation.

<details>
<summary><strong>Reveal Answer & Explanation (Question 211)</strong></summary>

**Correct Answer:** `D`

AWS CloudFormation allows you to define AWS infrastructure in JSON or YAML templates, enabling repeatable and automated provisioning of entire environments through infrastructure as code.
AWS CodePipeline automates the stages of a software release pipeline including source, build, and deploy phases, but does not provision or manage AWS infrastructure through templates. AWS CodeDeploy automates the deployment of application code to EC2 instances, Lambda functions, and on-premises servers, and does not manage infrastructure provisioning. AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS, and is a networking service entirely unrelated to infrastructure as code.

</details>

---

### Question 212 — `CLF-U0029` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**According to the AWS Acceptable Use Policy, which of the following statements is true regarding penetration testing of EC2 instances?**

- A) Penetration testing is not allowed in AWS.
- B) Penetration testing is performed automatically by AWS to determine vulnerabilities in your AWS infrastructure.
- C) Penetration testing can be performed by the customer on their own instances without prior authorization from AWS.
- D) The AWS customers are only allowed to perform penetration testing on services managed by AWS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 212)</strong></summary>

**Correct Answer:** `C`

AWS's Acceptable Use Policy allows customers to perform penetration testing on their own EC2 instances and certain other permitted services without prior authorisation from AWS, provided the testing complies with the AUP conditions.
Penetration testing is not prohibited in AWS; the Acceptable Use Policy explicitly permits customers to conduct penetration testing on their own resources within defined guidelines, making the claim that it is not allowed incorrect. AWS does not perform automated penetration testing on behalf of customers; Amazon Inspector performs automated security assessments for vulnerabilities and network exposure, but this is not the same as penetration testing, and AWS does not conduct adversarial testing of customer infrastructure. AWS customers are permitted to perform penetration testing on their own services and resources, not only on services managed by AWS; the restriction is that testing must target the customer's own resources rather than AWS shared infrastructure.

</details>

---

### Question 213 — `CLF-U0161` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**The owner of an E-Commerce application notices that the compute capacity requirements vary heavily from time to time. What makes AWS more economical than traditional data centers for this type of application?**

- A) AWS allows customers to launch powerful EC2 instances to handle spikes in load.
- B) AWS allows customers to pay upfront to get bigger discounts.
- C) AWS allows customers to launch and terminate EC2 instances based on demand.
- D) AWS allows customers to choose cheaper types of EC2 instances that best fit their needs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 213)</strong></summary>

**Correct Answer:** `C`

AWS allows customers to launch and terminate EC2 instances based on real-time demand, so during low-traffic periods they stop paying for unused capacity, unlike traditional data centers where hardware sits idle regardless of utilization.
Launching powerful instances to handle spikes in load describes vertical scaling, which still results in over-provisioned and idle capacity during low-traffic periods and does not address the core economic inefficiency of traditional data centers. Paying upfront to get bigger discounts describes Reserved Instance pricing, which is a commitment-based model that reduces per-unit cost but does not eliminate the problem of paying for capacity during periods of low demand. Choosing cheaper instance types reduces the unit cost of compute but does not eliminate idle capacity costs, as the instances would still run and incur charges regardless of whether they are actively being used.

</details>

---

### Question 214 — `CLF-U0166` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Your application requirements for CPU and RAM are changing in an unpredictable way. Which service can be used to dynamically adjust these resources based on load?**

- A) Auto Scaling.
- B) ELB.
- C) Amazon Route53.
- D) Amazon Elastic Container Service.

<details>
<summary><strong>Reveal Answer & Explanation (Question 214)</strong></summary>

**Correct Answer:** `A`

AWS Auto Scaling dynamically adjusts the number of EC2 instances based on real-time demand metrics such as CPU and memory utilization, automatically adding or removing capacity as workload requirements change.
Elastic Load Balancing distributes incoming traffic across multiple targets to improve availability and prevent any single instance from being overwhelmed, but it does not add or remove compute resources in response to changing CPU and RAM requirements. Amazon Route 53 is a DNS and traffic routing service that resolves domain names and directs users to application endpoints, and has no capability to provision or adjust compute resources. Amazon Elastic Container Service is a container orchestration service for running and managing containerised applications, and while it can scale tasks, it is not the purpose-built solution for dynamically adjusting EC2 compute resources based on unpredictable load.

</details>

---

### Question 215 — `CLF-U0186` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Engineers are wasting a lot of time and effort managing batch computing software in traditional data centers. Which of the following AWS services allows them to easily run thousands of batch computing jobs?**

- A) Amazon EC2.
- B) AWS Batch.
- C) Lambda@Edge.
- D) AWS Fargate.

<details>
<summary><strong>Reveal Answer & Explanation (Question 215)</strong></summary>

**Correct Answer:** `B`

AWS Batch automatically provisions the optimal quantity and type of compute resources based on the volume and requirements of batch jobs, removing the need to manage batch computing infrastructure manually and allowing engineers to focus on their workloads rather than the underlying infrastructure.
Amazon EC2 provides virtual servers that could run batch workloads, but requires engineers to manually provision, configure, and manage the instances and batch scheduling software themselves, which is exactly the problem the scenario describes. Lambda@Edge runs AWS Lambda functions at CloudFront edge locations to process content closer to end users, and is designed for lightweight event-driven tasks rather than large-scale batch computing jobs. AWS Fargate is a serverless compute engine for running containers without managing servers, but is designed for containerised application workloads rather than purpose-built batch job scheduling and management at scale.

</details>

---

### Question 216 — `CLF-U0252` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which of the following are valid ways for a customer to interact with AWS services? (Select TWO)**

- A) Command line interface.
- B) On-premises.
- C) Software Development Kits.
- D) Software-as-a-service.
- E) Hybrid.

<details>
<summary><strong>Reveal Answer & Explanation (Question 216)</strong></summary>

**Correct Answer:** `A, C`

The AWS Command Line Interface allows command-based interaction with AWS services from a terminal, and AWS Software Development Kits provide programmatic access to AWS services from application code written in multiple programming languages. Both are direct, supported methods for interacting with AWS services.
On-premises refers to infrastructure and software hosted in a company's own physical data center rather than in the cloud, and is a deployment model rather than a method of interacting with AWS services. Software-as-a-service is a cloud delivery model in which software applications are provided over the internet by a vendor, and is a service consumption model rather than a way for customers to interact with AWS services directly. Hybrid refers to an architecture that combines on-premises infrastructure with cloud resources, and is a deployment strategy rather than an interaction method for AWS services.

</details>

---

### Question 217 — `CLF-U0262` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**A company is considering using AWS for a self-hosted database that requires a nightly shutdown for maintenance and cost-saving purposes. Which service should the company use?**

- A) Amazon Redshift.
- B) Amazon DynamoDB.
- C) Amazon Elastic Compute Cloud (Amazon EC2) with Amazon EC2 instance store.
- D) Amazon EC2 with Amazon Elastic Block Store (Amazon EBS).

<details>
<summary><strong>Reveal Answer & Explanation (Question 217)</strong></summary>

**Correct Answer:** `D`

EC2 with EBS is the right choice because EBS volumes persist independently from the instance. When the instance is stopped nightly, the data on EBS is retained.
Amazon Redshift is a fully managed data warehouse service optimized for analytical SQL queries across large datasets, and as a managed service it cannot be stopped on a nightly schedule the way an EC2 instance can, making it unsuitable for a workload with a nightly shutdown requirement. Amazon DynamoDB is a fully managed NoSQL database service that scales automatically and operates continuously as a managed service, and cannot be stopped on a schedule for maintenance or cost-saving purposes. Amazon EC2 with Amazon EC2 instance store provides temporary block storage that is physically attached to the host machine, and this storage is lost when the instance is stopped, making it unsuitable for a database that requires data persistence across nightly shutdowns.

</details>

---

### Question 218 — `CLF-U0443` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which is a recommended pattern for designing a highly available architecture on AWS?**

- A) Ensure that components have low-latency network connectivity.
- B) Run enough Amazon EC2 instances to operate at peak load.
- C) Ensure that the application is designed to accommodate failure of any single component.
- D) Use a monolithic application that handles all operations.

<details>
<summary><strong>Reveal Answer & Explanation (Question 218)</strong></summary>

**Correct Answer:** `C`

Designing an application to accommodate the failure of any single component, through redundancy, health checks, and automatic failover, is the core principle of designing for failure and is the recommended pattern for achieving high availability on AWS.
Ensuring low-latency network connectivity is a performance optimization consideration that improves user experience, but low latency alone does not protect an application from component failures or maintain availability during an outage. Running enough EC2 instances to handle peak load addresses capacity planning but does not build in redundancy or fault tolerance, meaning a single component failure could still bring down the application. A monolithic application that handles all operations consolidates functionality into a single unit, which creates a single point of failure and is the opposite of a highly available architecture that can survive individual component failures.

</details>

---

### Question 219 — `CLF-U0571` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which of the following is NOT correct regarding Amazon EC2 On-demand instances?**

- A) You have to pay a start-up fee when launching a new instance for the first time.
- B) The on-demand instances follow the AWS pay-as-you-go pricing model.
- C) With on-demand instances, no longer-term commitments or upfront payments are needed.
- D) When using on-demand Linux instances, you are charged per second based on an hourly rate.

<details>
<summary><strong>Reveal Answer & Explanation (Question 219)</strong></summary>

**Correct Answer:** `A`

On-Demand EC2 instances have no start-up fee. You simply pay for the compute time you use with no upfront charges. On-Demand instances follow pay-as-you-go pricing, require no commitments, and Linux instances are billed per second.
There is no start-up fee when launching an On-Demand EC2 instance for the first time. AWS charges only for the compute time the instance runs, with no additional fees for initial provisioning or launch. The AWS pay-as-you-go pricing model for On-Demand instances means you are charged only for the time the instance runs, with no additional start-up fees, fixed monthly charges, or minimum usage requirements. With On-Demand instances there are no longer-term commitments or upfront payments required, allowing you to start and stop instances at any time based on your needs. Linux-based EC2 instances are indeed billed per second based on an hourly rate, with a minimum charge of one full minute, which is an accurate statement and not the incorrect one the question asks you to identify.

</details>

---

### Question 220 — `CLF-U0807` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which of the following can help protect your EC2 instances from DDoS attacks? (Choose TWO)**

- A) AWS CloudHSM.
- B) Security Groups.
- C) AWS Batch.
- D) AWS IAM.
- E) Network Access Control Lists (Network ACLs).

<details>
<summary><strong>Reveal Answer & Explanation (Question 220)</strong></summary>

**Correct Answer:** `B, E`

Security groups are stateful instance-level firewalls that can block unwanted traffic before it reaches EC2 instances, and Network ACLs are stateless subnet-level controls that can block volumetric attack traffic at the network perimeter. Both can help protect EC2 instances from DDoS traffic.
AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys within the AWS Cloud, and is a key management service with no capability to block or mitigate DDoS traffic targeting EC2 instances. AWS Batch is a fully managed batch computing service that dynamically provisions compute resources for batch jobs, and is a job scheduling and compute service with no network traffic filtering or DDoS protection capability. AWS IAM manages user permissions and access to AWS services and resources, and is an identity and access management service rather than a network defense tool that can block DDoS traffic.

</details>

---

### Question 221 — `CLF-U1478` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.1: Compute Services (EC2, Lambda, Elastic Beanstalk)*

**Which AWS service or feature captures information about the network traffic to and from an Amazon EC2 instance?**

- A) VPC Reachability Analyzer
- B) Amazon Athena
- C) VPC Flow Logs
- D) AWS X-Ray

<details>
<summary><strong>Reveal Answer & Explanation (Question 221)</strong></summary>

**Correct Answer:** `C`

The correct answer is C because VPC Flow Logs is an AWS service or feature that
captures information about the network traffic to and from an Amazon EC2 instance. VPC
Flow Logs is a feature that enables customers to capture information about the IP traffic
going to and from network interfaces in their VPC. VPC Flow Logs can help customers to
monitor and troubleshoot connectivity issues, such as traffic not reaching an instance or
traffic being rejected by a security group. The other options are incorrect because they are
not AWS services or features that capture information about the network traffic to and from
an Amazon EC2 instance. VPC Reachability Analyzer is an AWS service or feature that
enables customers to perform connectivity testing between resources in their VPC and
identify configuration issues that prevent connectivity. Amazon Athena is an AWS service
that enables customers to query data stored in Amazon S3 using standard SQL. AWS XRay is an AWS service that enables custom

</details>

---

### Question 222 — `CLF-U0141` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.2: Container Technologies (ECS, EKS, Fargate, ECR)*

**Which of the following are use cases for Amazon EMR? (Choose TWO)**

- A) Enables you to backup extremely large amounts of data at very low costs.
- B) Enables you to move Exabyte-scale data from on-premises datacenters into AWS.
- C) Enables you to analyze and process extremely large amounts of data in a timely manner.
- D) Enables you to easily run and scale Apache Spark, Hadoop,and other Big Data frameworks.
- E) Enables you to easily run and manage Docker containers.

<details>
<summary><strong>Reveal Answer & Explanation (Question 222)</strong></summary>

**Correct Answer:** `C, D`

Amazon EMR provides a managed cluster platform for running big data frameworks like Apache Spark and Hadoop, enabling both the analysis and processing of extremely large datasets at scale.
Backing up extremely large amounts of data at very low costs describes Amazon S3 combined with S3 Glacier storage classes, which are purpose-built for durable, low-cost data storage and archival. Moving exabyte-scale data from on-premises data centers into AWS describes AWS Snowmobile, which is a physical data transfer service for migrating extremely large datasets using a secure shipping container. Running and managing Docker containers describes Amazon ECS or AWS Fargate, which are container orchestration services unrelated to big data processing frameworks.

</details>

---

### Question 223 — `CLF-U0879` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.2: Container Technologies (ECS, EKS, Fargate, ECR)*

**What credential components are required to gain programmatic access to an AWS account? (Select TWO)**

- A) An access key ID.
- B) A primary key.
- C) A secret access key.
- D) A user ID.
- E) A secondary key.

<details>
<summary><strong>Reveal Answer & Explanation (Question 223)</strong></summary>

**Correct Answer:** `A, C`

Programmatic AWS access requires an access key ID to identify the calling entity and a secret access key to sign requests, together authenticating API calls made via the CLI or SDKs.
A primary key is not a valid AWS IAM credential component; it is a database term for a unique row identifier and has no role in AWS programmatic authentication. A user ID is an internal AWS identifier assigned to IAM users for tracking purposes but cannot be supplied as a credential to authenticate programmatic API requests. A secondary key is not a recognized AWS IAM credential type, and no such concept exists in the AWS authentication model for programmatic access.

</details>

---

### Question 224 — `CLF-U0082` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A company plans to migrate a large amount of archived data to AWS. The archived data must be maintained for a period of 5 years and must be retrievable within 5 hours of a request. What is the most cost-effective AWS storage service to use?**

- A) Amazon S3 Glacier.
- B) Amazon EFS.
- C) Amazon S3 Standard.
- D) Amazon EBS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 224)</strong></summary>

**Correct Answer:** `A`

Amazon S3 Glacier provides low-cost archival storage with retrieval options including Expedited (1 to 5 minutes), Standard (3 to 5 hours), and Bulk (5 to 12 hours). For a five-hour retrieval requirement, S3 Glacier Standard retrieval meets the SLA at the lowest cost.
Amazon EFS is a managed shared network file system that provides concurrent file access from multiple instances, and is designed for active file workloads rather than long-term archival storage where cost is the primary concern. Amazon S3 Standard provides durable, highly available object storage with immediate millisecond retrieval, and while it meets the retrieval requirement it is significantly more expensive per gigabyte than S3 Glacier for storing five years of infrequently accessed archival data. Amazon EBS provides persistent block storage volumes attached directly to EC2 instances for low-latency disk access, and is a compute-attached storage service not designed for long-term archival or for storing data independently of a running instance.

</details>

---

### Question 225 — `CLF-U0107` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A company is building an online cloud storage platform. They need a storage service that can scale capacity automatically, while minimizing cost. Which AWS storage service should the company use to meet these requirements?**

- A) Amazon Simple Storage Service.
- B) Amazon Elastic Block Store.
- C) Amazon Elastic Container Service.
- D) AWS Storage Gateway.

<details>
<summary><strong>Reveal Answer & Explanation (Question 225)</strong></summary>

**Correct Answer:** `A`

Amazon S3 provides virtually unlimited object storage that scales automatically with usage and charges only for what you store, making it ideal for cloud storage platforms that need elastic capacity at low cost.
Amazon Elastic Block Store provides persistent block storage volumes that attach directly to EC2 instances for low-latency disk access, and has a fixed provisioned capacity model where you pay for the volume size you provision rather than scaling automatically based on objects stored. Amazon Elastic Container Service is a container orchestration service that manages the deployment and scaling of containerised applications, and is a compute service rather than a storage service for an object storage platform. AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage integration, and is designed for bridging on-premises infrastructure with AWS rather than serving as the underlying storage for a cloud-native storage platform.

</details>

---

### Question 226 — `CLF-U0108` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**You have just hired a skilled sys-admin to join your team. As usual, you have created a new IAM user for him to interact with AWS services. On his first day, you ask him to create snapshots of all existing Amazon EBS volumes and save them in a new Amazon S3 bucket. However, the new member reports back that he is unable to create neither EBS snapshots nor S3 buckets. What might prevent him from doing this simple task?**

- A) EBS and S3 are accessible only to the root account owner.
- B) The systems administrator must contact AWS Support first to activate his new IAM account.
- C) There is not enough space in S3 to store the snapshots.
- D) There is a non-explicit deny to all new users.

<details>
<summary><strong>Reveal Answer & Explanation (Question 226)</strong></summary>

**Correct Answer:** `D`

By default, new IAM users have no permissions attached to them, meaning all actions are implicitly denied until explicit permissions are granted through policies, which is why the new administrator cannot create EBS snapshots or S3 buckets.
EBS and S3 are not accessible only to the root account owner; they can be accessed by any IAM user, group, or role that has been granted the appropriate permissions through IAM policies, making this statement factually incorrect. A new IAM user does not need to contact AWS Support to activate their account; IAM users are created and active immediately, and the issue is the absence of permissions rather than an account activation requirement. There is no inherent storage limit in S3 that would prevent creating a new bucket for snapshots; S3 scales automatically to accommodate any amount of data, and the inability to create the bucket is due to missing permissions rather than a storage capacity issue.

</details>

---

### Question 227 — `CLF-U0130` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which of the following S3 storage classes is most appropriate to host static assets for a popular e-commerce website with stable access patterns?**

- A) S3 Standard-IA.
- B) S3 Intelligent-Tiering.
- C) S3 Glacier Deep Archive.
- D) S3 Standard.

<details>
<summary><strong>Reveal Answer & Explanation (Question 227)</strong></summary>

**Correct Answer:** `D`

S3 Standard is designed for frequently accessed data with low latency and high throughput, making it the most appropriate storage class for static assets on a popular e-commerce site with consistent, stable access patterns.
S3 Standard-IA is designed for data that is accessed infrequently but requires rapid access when needed, and carries a per-retrieval charge that makes it more expensive than S3 Standard for assets that are accessed consistently and frequently. S3 Intelligent-Tiering automatically moves objects between access tiers based on changing access patterns, making it better suited for data with unpredictable or unknown access frequency rather than assets with stable, predictable demand. S3 Glacier Deep Archive is the lowest-cost storage class designed for long-term archival of data that is rarely if ever accessed, and is entirely unsuitable for serving live website assets that require immediate low-latency retrieval.

</details>

---

### Question 228 — `CLF-U0146` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**To protect against data loss, you need to backup your database regularly. What is the most cost-effective storage option that provides immediate retrieval of your backups?**

- A) Amazon S3 Glacier Deep Archive.
- B) Amazon S3 Standard-Infrequent Access.
- C) Amazon S3 Glacier.
- D) Instance Store.

<details>
<summary><strong>Reveal Answer & Explanation (Question 228)</strong></summary>

**Correct Answer:** `B`

Amazon S3 Standard-Infrequent Access offers lower storage costs than S3 Standard while still providing immediate, millisecond retrieval, making it cost-effective for backups that are accessed infrequently but need to be available instantly.
Amazon S3 Glacier Deep Archive is the lowest-cost storage class for long-term archival data that is accessed very rarely, with retrieval times of 12 hours or more, making it unsuitable for backups that require immediate retrieval. Amazon S3 Glacier provides low-cost archival storage with retrieval options ranging from minutes to hours depending on the retrieval tier selected, and while less expensive than S3 Standard it does not provide the immediate millisecond retrieval required for backup recovery. Instance Store provides temporary block storage physically attached to the host machine running an EC2 instance, and is ephemeral storage that is lost when the instance stops, making it entirely unsuitable for durable backup storage.

</details>

---

### Question 229 — `CLF-U0219` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which AWS services should be used for read/write of constantly changing data? (Select TWO)**

- A) Amazon Glacier.
- B) Amazon RDS.
- C) AWS Snowball.
- D) Amazon Redshift.
- E) Amazon EFS.

<details>
<summary><strong>Reveal Answer & Explanation (Question 229)</strong></summary>

**Correct Answer:** `B, E`

Amazon RDS supports frequent read/write operations on relational data with full ACID transaction support, making it well suited for applications with constantly changing structured data. Amazon EFS provides a shared network file system with concurrent read/write access for multiple EC2 instances, making it appropriate for workloads that require continuous file-level changes.
Amazon S3 Glacier is an archival storage service designed for data that is rarely accessed and does not support the frequent read/write operations that constantly changing data requires. AWS Snowball is a physical device used to transfer large volumes of data into or out of AWS and has no capability to serve as a read/write data store for active workloads. Amazon Redshift is a data warehouse service optimized for running complex analytical queries across large datasets, not for handling frequent transactional read/write operations on constantly changing data.

</details>

---

### Question 230 — `CLF-U0247` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**Which of the following AWS services can be used to serve large amounts of online video content with the lowest possible latency? (Select TWO)**

- A) appGateway.
- B) Amazon S3.
- C) Amazon Elastic File System (EFS).
- D) Amazon Glacier.
- E) Amazom CloudFront.

<details>
<summary><strong>Reveal Answer & Explanation (Question 230)</strong></summary>

**Correct Answer:** `B, E`

Amazon S3 stores video content with high durability and scalability, and Amazon CloudFront caches and delivers that content from edge locations worldwide with low latency, making them the purpose-built combination for serving large-scale online video efficiently.
AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage integration, and is not designed for serving or distributing online video content to end users. Amazon Elastic File System is a managed shared network file system for use with AWS compute services, and is not optimized for delivering large volumes of video content at low latency to a distributed audience. Amazon S3 Glacier is an archival storage service designed for data that is rarely accessed and can tolerate retrieval times of minutes to hours, making it entirely unsuitable for serving online video content that requires immediate low-latency delivery.

</details>

---

### Question 231 — `CLF-U0769` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**What does the Amazon S3 Intelligent-Tiering storage class offer?**

- A) Payment flexibility by reserving storage capacity
- B) Long-term retention of data by copying the data to an encrypted Amazon Elastic Block Store (Amazon EBS) volume
- C) Automatic cost savings by moving objects between tiers based on access pattern changes
- D) Secure, durable, and lowest cost storage for data archival

<details>
<summary><strong>Reveal Answer & Explanation (Question 231)</strong></summary>

**Correct Answer:** `C`

S3 Intelligent-Tiering automatically monitors access patterns and moves objects between a frequent access tier and an infrequent access tier without performance impact or operational overhead, reducing storage costs for data with unpredictable or changing access patterns.
Payment flexibility by reserving storage capacity describes a commitment-based pricing model that does not exist for Amazon S3, which charges based on actual usage rather than reserved capacity. Long-term retention of data by copying it to an encrypted EBS volume is not how S3 Intelligent-Tiering works. EBS is block storage attached to EC2 instances and is entirely separate from S3 storage classes, and Intelligent-Tiering manages data within S3 itself. Secure, durable, and lowest cost storage for data archival describes Amazon S3 Glacier, which is a separate storage class designed specifically for infrequently accessed archival data with retrieval times ranging from minutes to hours, not S3 Intelligent-Tiering.

</details>

---

### Question 232 — `CLF-U1459` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.3: Storage Services (S3, EBS, EFS, Storage Gateway)*

**A company wants to store its files in the AWS Cloud. Users need to be able to download these files directly using a public URL. Which AWS service or feature will meet this requirement?**

- A) Amazon Redshift
- B) Amazon Elastic Block Store (Amazon EBS)
- C) Amazon Elastic File System (Amazon EFS)
- D) Amazon S3

<details>
<summary><strong>Reveal Answer & Explanation (Question 232)</strong></summary>

**Correct Answer:** `D`

Amazon S3 (Simple Storage Service)is a scalable object storage service that allows users
to store and retrieve any amount of data at any time from anywhere on the web. S3
provides the ability to make objects (files) publicly accessible via a public URL, which
allows users to download files directly. S3 is highly durable, scalable, and secure, making it
an ideal service for storing files that need to be accessed publicly.
Why other options are not suitable:
A . Amazon Redshift: A data warehouse service designed for complex queries and
analytics, not for storing and publicly sharing files.
B . Amazon Elastic Block Store (Amazon EBS): Provides block storage for use with EC2
instances, but does not support public URLs or direct file access from the web.
C . Amazon Elastic File System (Amazon EFS): A managed file storage service for use
with EC2 instances, not designed for public access via URLs.
Reference:
Amazon S3 Documentation

</details>

---

### Question 233 — `CLF-U0015` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Which of the following are examples of AWS-Managed Services, where AWS is responsible for the operational and maintenance burdens of running the service? (Choose TWO)**

- A) Amazon VPC.
- B) Amazon DynamoDB.
- C) Amazon Elastic MapReduce.
- D) AWS IAM.
- E) Amazon Elastic Compute Cloud.

<details>
<summary><strong>Reveal Answer & Explanation (Question 233)</strong></summary>

**Correct Answer:** `B, C`

Amazon DynamoDB and Amazon EMR are fully managed services where AWS handles provisioning, patching, scaling, and maintenance automatically, freeing customers from managing the underlying infrastructure.
Amazon VPC is a networking construct that customers configure and manage themselves, including subnets, route tables, internet gateways, and security groups, making it a customer-configured resource rather than a fully managed service. AWS IAM is a service customers use to manage their own users, roles, and permissions, and while AWS maintains the IAM infrastructure, customers are responsible for all identity and access configuration. Amazon Elastic Compute Cloud provides virtual servers where customers are responsible for the operating system, installed software, patches, and configuration, making it an infrastructure service where the customer manages the virtual machine layer rather than a fully managed one.

</details>

---

### Question 234 — `CLF-U0024` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What does AWS provide to deploy popular technologies such as IBM MQ on AWS with the least amount of effort and time?**

- A) Amazon Aurora.
- B) Amazon CloudWatch.
- C) AWS Quick Start reference deployments.
- D) AWS OpsWorks.

<details>
<summary><strong>Reveal Answer & Explanation (Question 234)</strong></summary>

**Correct Answer:** `C`

AWS Quick Start reference deployments provide automated gold-standard templates that deploy popular IT solutions on AWS in minutes, giving administrators a fast path to production-ready environments built on AWS best practices.
Amazon Aurora is a fully managed relational database compatible with MySQL and PostgreSQL, and is a database service with no capability to deploy or provision third-party technologies or solutions. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and is a monitoring service with no deployment or provisioning capability. AWS OpsWorks (deprecated) was a configuration management service that used Chef and Puppet to automate server configuration, and while it could automate some infrastructure tasks it is not a pre-built deployment resource for rapidly deploying popular third-party technologies with minimal effort. Note: AWS OpsWorks was deprecated in 2024.

</details>

---

### Question 235 — `CLF-U0064` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Which of the following AWS offerings is a MySQL-compatible relational database service that can scale capacity automatically based on demand?**

- A) Amazon Neptune.
- B) Amazon Aurora.
- C) Amazon RDS for SQL Server.
- D) Amazon RDS for PostgreSQL.

<details>
<summary><strong>Reveal Answer & Explanation (Question 235)</strong></summary>

**Correct Answer:** `B`

Amazon Aurora is a MySQL and PostgreSQL-compatible managed relational database that automatically scales storage as needed, making it the purpose-built solution for applications requiring MySQL compatibility with automatic capacity scaling.
Amazon Neptune is a fully managed graph database service designed for storing and querying highly connected data such as social networks and knowledge graphs, and is not a MySQL-compatible relational database. Amazon RDS for SQL Server is a managed relational database running Microsoft's SQL Server engine, which is not MySQL-compatible and does not automatically scale storage capacity on demand. Amazon RDS for PostgreSQL is a managed relational database running the PostgreSQL engine which, while sharing some compatibility with Aurora, does not auto-scale storage the way Aurora does.

</details>

---

### Question 236 — `CLF-U0085` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What is the AWS service that provides five times the performance of a standard MySQL database?**

- A) Amazon Aurora.
- B) Amazon Redshift.
- C) Amazon DynamoDB.
- D) Amazon Neptune.

<details>
<summary><strong>Reveal Answer & Explanation (Question 236)</strong></summary>

**Correct Answer:** `A`

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database that delivers up to five times the throughput of standard MySQL, with the reliability and availability of a commercial database at a fraction of the cost.
Amazon Redshift is a fully managed data warehouse service optimized for running complex analytical queries across large datasets, and is not a MySQL-compatible relational database designed for high-throughput transactional workloads. Amazon DynamoDB is a fully managed NoSQL database that supports key-value and document data models, and does not offer MySQL compatibility or the relational capabilities that Aurora provides. Amazon Neptune is a fully managed graph database service designed for storing and querying highly connected data, and has no MySQL compatibility or relation to the performance characteristics described.

</details>

---

### Question 237 — `CLF-U0150` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**You have a real-time IoT application that requires sub-millisecond latency. Which of the following services should you use?**

- A) Amazon Redshift.
- B) Amazon Athena.
- C) AWS Cloud9.
- D) Amazon ElastiCache for Redis.

<details>
<summary><strong>Reveal Answer & Explanation (Question 237)</strong></summary>

**Correct Answer:** `D`

Amazon ElastiCache for Redis is an in-memory data store that delivers sub-millisecond response times, making it the appropriate choice for a real-time IoT application requiring extremely low latency.
Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is designed for throughput-oriented batch analytics rather than sub-millisecond real-time data access. Amazon Athena is a serverless query service that analyzes data stored in Amazon S3 using SQL, and involves query execution times measured in seconds rather than the sub-millisecond latency that real-time IoT applications require. AWS Cloud9 is a cloud-based integrated development environment for writing, running, and debugging code, and is a developer tool with no data storage or low-latency serving capability.

</details>

---

### Question 238 — `CLF-U0209` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What is the benefit of using AWS managed services, such as Amazon ElastiCache and Amazon Relational Database Service (Amazon RDS)?**

- A) They require the customer to monitor and replace failing instances.
- B) They have better performance than customer-managed services.
- C) They simplify patching and updating underlying OSs.
- D) They do not require the customer to optimize instance type or size selections.

<details>
<summary><strong>Reveal Answer & Explanation (Question 238)</strong></summary>

**Correct Answer:** `C`

AWS managed services like Amazon ElastiCache and Amazon RDS handle patching and updating the underlying operating systems and database engines, freeing customers from these time-consuming maintenance tasks.
Requiring the customer to monitor and replace failing instances describes the opposite of a managed service benefit, as AWS managed services handle failure detection and recovery automatically, removing that burden from customers. Having better performance than customer-managed services is not guaranteed as a universal benefit, since performance depends on instance type, configuration, and workload rather than simply on whether a service is managed. Not requiring the customer to optimize instance type or size selections is incorrect, as customers are still responsible for choosing the appropriate instance type and size to match their workload requirements even when using managed services.

</details>

---

### Question 239 — `CLF-U0212` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Which of the following is a fast and reliable NoSQL database service?**

- A) Amazon Redshift.
- B) Amazon RDS.
- C) Amazon DynamoDB.
- D) Amazon S3.

<details>
<summary><strong>Reveal Answer & Explanation (Question 239)</strong></summary>

**Correct Answer:** `C`

Amazon DynamoDB is a fully managed NoSQL database that delivers single-digit millisecond performance at any scale, with built-in security, backup, and in-memory caching.
Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is a relational columnar store rather than a NoSQL database service. Amazon RDS is a fully managed relational database service supporting engines such as MySQL, PostgreSQL, and SQL Server, and uses structured schemas and SQL rather than the flexible schema-less data models that NoSQL databases provide. Amazon S3 is an object storage service for storing and retrieving files and unstructured data, and while it can store large volumes of data it is not a database service and does not support the query patterns or data models of a NoSQL database.

</details>

---

### Question 240 — `CLF-U0620` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**A company is migrating production workloads to AWS, and they are concerned about cost management across different departments. Which option should the company implement to categorize and track AWS spending?**

- A) Use the AWS Pricing Calculator service to monitor the costs incurred by each department.
- B) Use Amazon Aurora to forecast AWS spending based on usage.
- C) Apply cost allocation tags to segment AWS costs by different e projects and departments.
- D) Configure AWS Price List API to receive billing updates for each department automatically.

<details>
<summary><strong>Reveal Answer & Explanation (Question 240)</strong></summary>

**Correct Answer:** `C`

Cost allocation tags are key-value metadata that you apply to AWS resources, enabling you to segment and categorize costs by project, department, or environment in Cost Explorer and billing reports.
The AWS Pricing Calculator is used to estimate future costs for new AWS service configurations before deploying them, and does not monitor or categorize actual spending incurred by active workloads. Amazon Aurora is a fully managed relational database service compatible with MySQL and PostgreSQL, and is a database engine with no capability to forecast AWS spending or categorize costs by department. The AWS Price List API provides programmatic access to AWS service pricing data for building custom pricing tools, and delivers pricing information rather than automatically updating billing categories based on department usage.

</details>

---

### Question 241 — `CLF-U0812` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**What is the AWS’ recommendation regarding access keys?**

- A) Delete all access keys and use passwords instead.
- B) Only share them with trusted people.
- C) Rotate them regularly.
- D) Save them within your application code.

<details>
<summary><strong>Reveal Answer & Explanation (Question 241)</strong></summary>

**Correct Answer:** `C`

AWS recommends rotating access keys regularly to limit the window of exposure if a key is ever compromised, as shorter-lived credentials reduce the risk of unauthorised access going undetected.
Deleting all access keys and using passwords instead is not a valid approach, as passwords are used for console access while access keys are required for programmatic access through the CLI and API, and both have legitimate roles in a well-managed AWS account. Sharing access keys only with trusted people still violates the principle of least privilege, as access keys should be scoped to individual IAM users or roles rather than shared between people. Saving access keys within application code is a significant security risk as code repositories can be exposed publicly or internally, and AWS recommends using IAM roles for applications running on AWS resources instead of embedding credentials in code.

</details>

---

### Question 242 — `CLF-U0844` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Who is responsible for scaling a DynamoDB database in the AWS Shared Responsibility Model?**

- A) Your security team.
- B) Your development team.
- C) AWS.
- D) Your internal DevOps team.

<details>
<summary><strong>Reveal Answer & Explanation (Question 242)</strong></summary>

**Correct Answer:** `C`

Amazon DynamoDB is a fully managed NoSQL database service where AWS handles all scaling automatically, including read and write capacity adjustments, so customers do not need to manage or plan for database scaling themselves.
The customer's security team focuses on security policies, access controls, and compliance rather than the operational scaling of a managed database service, and DynamoDB's autoscaling is handled by AWS infrastructure rather than any customer team. The development team builds and maintains application code, and while they configure DynamoDB table settings during development, the actual scaling of a fully managed service is performed automatically by AWS rather than manually by developers. The internal DevOps team manages infrastructure, deployments, and operational workflows, but the scaling of a fully managed service like DynamoDB is handled automatically by AWS and does not require DevOps intervention.

</details>

---

### Question 243 — `CLF-U2514` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.4: Database & In-Memory Caching Services*

**Which AWS services are supported by Savings Plans? (Choose two.)**

- A) Amazon EC2
- B) Amazon RDS
- C) Amazon SageMaker
- D) Amazon Redshift
- E) Amazon DynamoDB

<details>
<summary><strong>Reveal Answer & Explanation (Question 243)</strong></summary>

**Correct Answer:** `AC`

**Correct Answer: AC (Amazon EC2, Amazon SageMaker)**

This question (# 177) is directly sourced from authentic **Community Consensus Pool** community discussions.
**Why this is correct:** The scenario specifically tests AWS best practices. 'Amazon EC2, Amazon SageMaker' directly satisfies the architectural requirement defined in the prompt.

**Key Option Breakdown:**
- **Option A (Amazon EC2)** [CORRECT]: Satisfies the prompt requirements directly.
- **Option B (Amazon RDS)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option C (Amazon SageMaker)** [CORRECT]: Satisfies the prompt requirements directly.
- **Option D (Amazon Redshift)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.
- **Option E (Amazon DynamoDB)** [INCORRECT]: Does not meet the scenario requirements or introduces suboptimal design for this specific workload.

</details>

---

### Question 244 — `CLF-U0014` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which of the following can be described as a global content delivery network (CDN) service?**

- A) AWS VPN.
- B) AWS Direct Connect.
- C) AWS Regions.
- D) Amazon CloudFront.

<details>
<summary><strong>Reveal Answer & Explanation (Question 244)</strong></summary>

**Correct Answer:** `D`

Amazon CloudFront is AWS's global CDN service that caches and delivers content from edge locations worldwide, reducing latency for end users regardless of their location.
AWS VPN creates encrypted network connections between on-premises infrastructure and AWS over the public internet, and has no content delivery or caching capability. AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, and is a connectivity service rather than a content delivery network. AWS Regions are geographic areas containing multiple Availability Zones where AWS infrastructure is hosted, and are a component of global infrastructure rather than a CDN service.

</details>

---

### Question 245 — `CLF-U0069` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**What is the connectivity option that uses Internet Protocol Security (IPSec) to establish encrypted connectivity between an on-premises network and the AWS Cloud?**

- A) Internet Gateway.
- B) AWS IQ.
- C) AWS Direct Connect.
- D) AWS Site-to-Site VPN.

<details>
<summary><strong>Reveal Answer & Explanation (Question 245)</strong></summary>

**Correct Answer:** `D`

AWS Site-to-Site VPN uses IPSec to create an encrypted tunnel between an on-premises network and an AWS VPC over the public internet, providing secure connectivity without dedicated physical infrastructure.
Internet Gateway connects a VPC to the public internet for inbound and outbound traffic, but does not establish encrypted tunnels to on-premises networks. AWS IQ is a marketplace for connecting customers with AWS-certified experts for professional services, unrelated to network connectivity. AWS Direct Connect provides a dedicated private circuit between on-premises infrastructure and AWS, but does not use IPSec and does not travel over the public internet.

</details>

---

### Question 246 — `CLF-U0137` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which of the below options is true of Amazon VPC?**

- A) Amazon VPC allows customers to control user interactions with all other AWS resources.
- B) AWS Customers have complete control over their Amazon VPC virtual networking environment.
- C) AWS is responsible for all the management and configuration details of Amazon VPC.
- D) Amazon VPC helps customers to review their AWS architecture and adopt best practices.

<details>
<summary><strong>Reveal Answer & Explanation (Question 246)</strong></summary>

**Correct Answer:** `B`

Amazon VPC gives customers complete control over their virtual networking environment, including selection of IP address ranges, creation of subnets, and configuration of route tables and network gateways.
Controlling user interactions with AWS resources is the function of AWS IAM, which manages permissions and access policies, not Amazon VPC. AWS is not responsible for all management and configuration of Amazon VPC, as customers retain full responsibility for configuring their own subnets, route tables, security groups, and network ACLs. Reviewing AWS architecture and adopting best practices describes the AWS Well-Architected Tool, not Amazon VPC, which is a networking service rather than an architectural review service.

</details>

---

### Question 247 — `CLF-U0144` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**A media company has an application that requires the transfer of large data sets to and from AWS every day. This data is business critical and should be transferred over a consistent connection. Which AWS service should the company use?**

- A) AWS Direct Connect.
- B) Amazon Comprehend.
- C) AWS Snowmobile.
- D) AWS VPN.

<details>
<summary><strong>Reveal Answer & Explanation (Question 247)</strong></summary>

**Correct Answer:** `A`

AWS Direct Connect establishes a dedicated private network connection between an on-premises data center and AWS, providing consistent throughput and lower latency than internet-based connections, making it the right choice for daily large-scale business-critical data transfers.
Amazon Comprehend is a natural language processing service for extracting insights and relationships from text and has no role in network connectivity or data transfer. AWS Snowmobile is a physical data transfer service for one-time migration of extremely large datasets to AWS, not for recurring daily transfers requiring a consistent network connection. AWS VPN establishes an encrypted connection over the public internet, which does not provide the consistent throughput and reliability guarantees required for business-critical daily large data transfers.

</details>

---

### Question 248 — `CLF-U0148` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which of the below options are use cases of the Amazon Route 53 service? (Choose TWO)**

- A) Point-to-point connectivity between an on-premises data center and AWS.
- B) Detects configuration changes in the AWS environment.
- C) DNS configuration and management.
- D) Manages global application traffic through a variety of routing types.
- E) Provides infrastructure security optimization recommendations.

<details>
<summary><strong>Reveal Answer & Explanation (Question 248)</strong></summary>

**Correct Answer:** `C, D`

Amazon Route 53 is a scalable DNS service that translates domain names to IP addresses, and it manages global application traffic through routing policies including latency-based, geolocation, weighted, and failover routing.
Point-to-point connectivity between an on-premises data center and AWS describes AWS Direct Connect, which provides a dedicated private network link between on-premises infrastructure and AWS. Detecting configuration changes in the AWS environment describes AWS Config, which continuously monitors and records resource configurations and evaluates them against desired settings. Providing infrastructure security optimization recommendations describes AWS Trusted Advisor, which analyzes your environment against best practice checks across security, cost, performance, and fault tolerance.

</details>

---

### Question 249 — `CLF-U0220` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which of the following is an AWS managed Domain Name System (DNS) web service?**

- A) Amazon Route 53.
- B) Amazon Neptune.
- C) Amazon SageMaker.
- D) Amazon Lightsail.

<details>
<summary><strong>Reveal Answer & Explanation (Question 249)</strong></summary>

**Correct Answer:** `A`

Amazon Route 53 is AWS's managed DNS web service that translates domain names into IP addresses and also provides traffic routing policies, health checks, and domain registration.
Amazon Neptune is a fully managed graph database service for applications that work with highly connected datasets, unrelated to DNS or traffic routing. Amazon SageMaker is a managed machine learning platform for building, training, and deploying ML models, entirely unrelated to DNS. Amazon Lightsail provides simplified virtual private servers with pre-configured compute and networking for straightforward workloads, not a DNS service.

</details>

---

### Question 250 — `CLF-U0809` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**Which of the following is used to control network traffic in AWS? (Choose TWO)**

- A) Network Access Control Lists (NACLs).
- B) Key Pairs.
- C) Access Keys.
- D) IAM Policies.
- E) Security Groups.

<details>
<summary><strong>Reveal Answer & Explanation (Question 250)</strong></summary>

**Correct Answer:** `A, E`

Network ACLs are stateless subnet-level firewalls that evaluate all inbound and outbound traffic based on numbered rules, and security groups are stateful instance-level firewalls that control traffic to and from EC2 instances. Both are used to control network traffic in AWS.
Key pairs are RSA public/private key combinations used to authenticate SSH connections to EC2 instances, and are an instance access credential rather than a network traffic control mechanism. Access keys consisting of an access key ID and secret access key are used to authenticate programmatic API calls to AWS services, and are an API authentication credential rather than a tool for controlling network traffic within a VPC. IAM policies are JSON documents that define permissions for users, groups, and roles to access AWS services and resources, and operate at the API authorisation layer rather than controlling IP-level network traffic flow.

</details>

---

### Question 251 — `CLF-U0849` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.5: Networking & Content Delivery (VPC, Route 53, CloudFront)*

**You have been tasked with auditing the security of your VPC. As part of this process, you need to start by analyzing what inbound and outbound traffic is allowed on your EC2 instances. What two parts of the VPC do you need to check to accomplish this task?**

- A) Network ACLs and Traffic Manager.
- B) Network ACLs and Subnets.
- C) Security Groups and Internet Gateways.
- D) Security Groups and Network ACLs.

<details>
<summary><strong>Reveal Answer & Explanation (Question 251)</strong></summary>

**Correct Answer:** `D`

Security groups control inbound and outbound traffic at the EC2 instance level with stateful evaluation, and Network ACLs control traffic at the subnet level with stateless rule evaluation. Checking both gives a complete picture of what traffic is allowed to and from EC2 instances in the VPC.
Network ACLs and Traffic Manager is not a valid combination for VPC traffic analysis; AWS Traffic Manager does not exist as an AWS service name, and the correct subnet-level control is Network ACLs rather than a non-existent Traffic Manager. Network ACLs and Subnets is partially correct in that subnets are VPC components, but subnets themselves are network segments rather than traffic control mechanisms, and checking subnets does not tell you what traffic rules are applied; you need to check the ACLs attached to those subnets. Security groups and Internet Gateways is partially correct in that Internet Gateways allow internet traffic into the VPC, but they do not define granular allow/deny rules for instance-level traffic; checking security groups alone misses the subnet-level controls provided by Network ACLs.

</details>

---

### Question 252 — `CLF-U0021` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**What is the AWS service that enables AWS architects to manage infrastructure as code?**

- A) AWS CloudFormation.
- B) AWS Config.
- C) Amazon SES.
- D) Amazon EMR.

<details>
<summary><strong>Reveal Answer & Explanation (Question 252)</strong></summary>

**Correct Answer:** `A`

AWS CloudFormation lets you define your entire AWS infrastructure as code using JSON or YAML templates, enabling repeatable and automated provisioning of resources without manual configuration.
AWS Config continuously monitors and records the configuration state of AWS resources and evaluates them against desired settings, but it does not provision or manage infrastructure. Amazon SES is a cloud-based email sending and receiving service, entirely unrelated to infrastructure management. Amazon EMR is a managed big data processing service for running frameworks such as Apache Spark and Hadoop, unrelated to infrastructure as code.

</details>

---

### Question 253 — `CLF-U0092` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which of the following activities supports the Operational Excellence pillar of the AWS Well-Architected Framework?**

- A) Using AWS Trusted Advisor to find underutilized resources.
- B) Using AWS CloudTrail to record user activities.
- C) Using AWS CloudFormation to manage infrastructure as code.
- D) Deploying an application in multiple Availability Zones.

<details>
<summary><strong>Reveal Answer & Explanation (Question 253)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Using AWS CloudFormation to manage infrastructure as code**

AWS CloudFormation allows you to define and provision AWS infrastructure as code. This supports the Operational Excellence pillar of the AWS Well-Architected Framework by enabling you to automate deployments, manage infrastructure consistently, and easily replicate environments. Infrastructure as code promotes version control, auditability, and repeatable processes, leading to improved operational efficiency and reduced risk of manual errors. It allows for faster recovery from failures and easier scaling of resources.

**Incorrect:**

**B. Using AWS Trusted Advisor to find underutilized resources** - While AWS Trusted Advisor helps optimize costs and improve performance, it primarily addresses the Cost Optimization and Performance Efficiency pillars of the AWS Well-Architected Framework, not Operational Excellence directly. Identifying underutilized resources is more about reducing waste and improving resource utilization than improving operational processes.

**C. Using AWS CloudTrail to record user activities** - AWS CloudTrail is primarily focused on security and compliance. While it contributes to operational monitoring and auditing, its main purpose is to track user activity and API calls for security analysis, resource change tracking, and compliance purposes, aligning with the Security pillar.

**D. Deploying an application in multiple Availability Zones** - Deploying an application across multiple Availability Zones (AZs) enhances the reliability and availability of the application. This primarily supports the Reliability pillar of the AWS Well-Architected Framework by providing fault tolerance and redundancy. While it indirectly contributes to operational stability, it doesn't directly address the automation and process improvements emphasized by the Operational Excellence pillar.

</details>

---

### Question 254 — `CLF-U0128` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**What are some key benefits of using AWS CloudFormation? (Choose TWO)**

- A) It helps AWS customers deploy their applications without worrying about the underlying infrastructure.
- B) It applies advanced IAM security features automatically.
- C) It automates the provisioning and updating of your infrastructure in a safe and controlled manner.
- D) It allows you to model your entire infrastructure in just a text file.
- E) It compiles and builds application code in a timely manner.

<details>
<summary><strong>Reveal Answer & Explanation (Question 254)</strong></summary>

**Correct Answer:** `C, D`

AWS CloudFormation allows you to model your entire infrastructure in a JSON or YAML text file, and automates the provisioning and updating of resources in a safe, controlled, and repeatable manner.
Deploying applications without worrying about underlying infrastructure describes AWS Elastic Beanstalk, which abstracts infrastructure management for application deployment, not CloudFormation. Applying advanced IAM security features automatically is not a CloudFormation capability, as IAM policies and security configurations must still be defined and managed by the customer. Compiling and building application code is a function of build tools such as AWS CodeBuild, not CloudFormation, which deals with infrastructure provisioning rather than application code.

</details>

---

### Question 255 — `CLF-U0181` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**You are working as a site reliability engineer (SRE) in an AWS environment, which of the following services helps monitor your applications?**

- A) Amazon CloudWatch.
- B) Amazon CloudSearch.
- C) Amazon Elastic MapReduce.
- D) Amazon CloudHSM.

<details>
<summary><strong>Reveal Answer & Explanation (Question 255)</strong></summary>

**Correct Answer:** `A`

Amazon CloudWatch monitors applications and infrastructure by collecting metrics, logs, and events, providing dashboards and alarms that help SREs identify and respond to operational issues.
Amazon CloudSearch is a managed search service for building search functionality into applications, and is a search indexing tool with no application monitoring or observability capability. Amazon EMR is a managed big data platform for processing large datasets using frameworks such as Apache Hadoop and Spark, and is a data processing service with no application monitoring capability. Amazon CloudHSM provides dedicated hardware security modules for managing cryptographic keys, and is a security and key management service with no role in monitoring application performance or health.

</details>

---

### Question 256 — `CLF-U0210` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which services can be used across hybrid AWS Cloud architectures? (Select TWO)**

- A) Amazon Route 53.
- B) Virtual Private Gateway.
- C) Classic Load Balancer.
- D) Auto Scaling.
- E) Amazon CloudWatch default metrics.

<details>
<summary><strong>Reveal Answer & Explanation (Question 256)</strong></summary>

**Correct Answer:** `A, B`

Amazon Route 53 provides DNS services that work across both cloud and on-premises environments, and a Virtual Private Gateway enables encrypted VPN connections between a VPC and an on-premises data center, both making them suitable for hybrid architectures.
Classic Load Balancer distributes traffic across EC2 instances within AWS and operates entirely within the cloud, with no hybrid connectivity capability. Auto Scaling automatically adjusts the number of EC2 instances based on demand within AWS, and does not extend to or integrate with on-premises infrastructure. Amazon CloudWatch default metrics monitor AWS resource performance within the cloud, and while it can be extended to on-premises with a custom agent, it is not itself a hybrid architecture service.

</details>

---

### Question 257 — `CLF-U0215` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which of the following are features of Amazon CloudWatch Logs? (Select TWO)**

- A) Summaries by Amazon Simple Notification Service (Amazon SNS).
- B) Free Amazon Elasticsearch Service analytics.
- C) Provided at no charge.
- D) Real-time monitoring.
- E) Adjustable retention.

<details>
<summary><strong>Reveal Answer & Explanation (Question 257)</strong></summary>

**Correct Answer:** `D, E`

Amazon CloudWatch Logs supports real-time monitoring of log data and configurable retention periods, allowing you to control exactly how long log data is kept before it is automatically deleted.
Amazon SNS is a notification and messaging service that can be triggered by CloudWatch alarms, but summarizing log data is not a native feature of CloudWatch Logs. Amazon CloudWatch Logs is not free, as charges apply based on the volume of data ingested, stored, and analyzed. Amazon OpenSearch Service is a separate analytics service that can be integrated with CloudWatch Logs as a destination, but free OpenSearch analytics is not a native feature of CloudWatch Logs.

</details>

---

### Question 258 — `CLF-U0223` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which AWS service can be used to query stored datasets directly from Amazon S3 using standard SQL?**

- A) AWS Glue.
- B) AWS Data Pipeline.
- C) Amazon CloudSearch.
- D) Amazon Athena.

<details>
<summary><strong>Reveal Answer & Explanation (Question 258)</strong></summary>

**Correct Answer:** `D`

Amazon Athena lets you run standard SQL queries directly against data stored in S3 without loading it into a database first, making it the purpose-built service for querying datasets directly from S3.
AWS Glue is a serverless ETL service for discovering, preparing, and transforming data for analytics pipelines, not for running ad hoc SQL queries directly against S3. Amazon EMR provides managed clusters for processing large datasets using frameworks like Spark and Hadoop, but requires provisioning infrastructure rather than querying S3 directly with standard SQL. Amazon CloudSearch is a managed search service for adding full-text search functionality to applications and has no capability for SQL-based data querying.

</details>

---

### Question 259 — `CLF-U0371` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**A company is building an application that requires the ability to send, store, and receive messages between application components. The company has another requirement to process messages in first-in, first-out (FIFO) order. Which AWS service should the company use?**

- A) AWS Step Functions
- B) Amazon Simple Notification Service (Amazon SNS)
- C) Amazon Kinesis Data Streams
- D) Amazon Simple Queue Service (Amazon SQS)

<details>
<summary><strong>Reveal Answer & Explanation (Question 259)</strong></summary>

**Correct Answer:** `D`

Amazon SQS supports FIFO queues that guarantee messages are processed exactly once in the exact order they are received, making it the correct service for applications that require strict first-in, first-out message ordering with deduplication.
AWS Step Functions is a workflow orchestration service that coordinates distributed application components through visual workflows and state machines, and while it sequences steps in a defined order, it is not a message queuing service for decoupling application components that need to exchange messages in FIFO order. Amazon SNS is a fully managed pub/sub notification service that broadcasts messages to multiple subscribed endpoints simultaneously, and it does not support FIFO guarantees for ordered message delivery between specific senders and receivers. Amazon Kinesis Data Streams is a real-time data streaming service designed for processing large volumes of streaming data from multiple producers, and while it preserves order within a shard, it is designed for high-throughput analytics pipelines rather than application-to-application message queuing with FIFO guarantees.

</details>

---

### Question 260 — `CLF-U0612` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**You have migrated your application to AWS recently. How can you view the AWS costs applied to your account?**

- A) Using the AWS Cost & Usage Report.
- B) Using the AWS Total Cost of Ownership (TCO) dashboard.
- C) Using the AWS CloudWatch logs dashboard.
- D) Using the Amazon VPC dashboard.

<details>
<summary><strong>Reveal Answer & Explanation (Question 260)</strong></summary>

**Correct Answer:** `A`

The AWS Cost and Usage Report provides the most comprehensive view of your actual AWS costs, breaking down charges by service, resource, and time period so you can see exactly what you are being charged for.
AWS Cost Explorer provides interactive visualisations and analysis of AWS spending patterns over time and is well-suited for exploring costs, but the Cost and Usage Report provides the most granular and complete raw data for detailed cost review. The AWS Pricing Calculator is used to estimate future costs for AWS services before provisioning them, and does not display actual charges already applied to your account. The Amazon VPC dashboard is a networking console for managing virtual private clouds, subnets, and network configuration, and has no connection to cost viewing or billing information.

</details>

---

### Question 261 — `CLF-U0624` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which of the following makes it easier for you to categorize, manage and filter your resources?**

- A) Amazon CloudWatch.
- B) AWS Service Catalog.
- C) AWS Directory Service.
- D) AWS Tagging.

<details>
<summary><strong>Reveal Answer & Explanation (Question 261)</strong></summary>

**Correct Answer:** `D`

AWS tags are key-value metadata pairs attached to resources, making it easy to categorize, filter, search, and manage resources by project, environment, owner, or any other custom criteria.
Amazon CloudWatch is a monitoring and observability service for collecting metrics, logs, and alarms on AWS resources, not a resource categorization or filtering tool. AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal deployment, not for tagging or filtering existing resources. AWS Directory Service provides managed Microsoft Active Directory for user authentication and access management, unrelated to resource categorization or metadata management.

</details>

---

### Question 262 — `CLF-U0675` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**How should a customer forecast the future costs for running a new web application?**

- A) Amazon Aurora Backtrack.
- B) Amazon CloudWatch Billing Alarms.
- C) AWS Pricing Calculator (formerly Simple Monthly Calculator).
- D) AWS Cost and Usage report.

<details>
<summary><strong>Reveal Answer & Explanation (Question 262)</strong></summary>

**Correct Answer:** `C`

The AWS Pricing Calculator allows customers to model AWS service configurations and estimate future costs before deploying them, making it the purpose-built tool for forecasting the cost of a new application.
Amazon Aurora Backtrack is a feature that allows an Aurora database to be rewound to a previous point in time without restoring from a backup, and is a database recovery feature with no connection to cost forecasting. Amazon CloudWatch Billing Alarms trigger notifications when actual AWS spending exceeds a defined threshold, and are a cost alerting tool for active workloads rather than a forecasting tool for new applications. AWS Cost and Usage Reports provide the most detailed breakdown of actual AWS charges already incurred, and are a historical cost analysis tool rather than a future cost estimation service.

</details>

---

### Question 263 — `CLF-U0850` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Which AWS service provides the EASIEST way to set up and manage a secure, well-architected, multi-account AWS environment?**

- A) AWS Control Tower.
- B) Amazon Macie.
- C) AWS Systems Manager Patch Manager.
- D) AWS Security Hub.

<details>
<summary><strong>Reveal Answer & Explanation (Question 263)</strong></summary>

**Correct Answer:** `A`

AWS Control Tower automates the setup of a secure, well-architected multi-account environment based on AWS best practices, providing pre-configured guardrails and a landing zone dashboard for centralized governance.
Amazon Macie is a data security service that uses machine learning to discover and protect sensitive data stored in Amazon S3, and has no role in multi-account environment setup or governance. AWS Systems Manager Patch Manager automates the patching of operating systems and applications on EC2 instances and is not related to account architecture or multi-account management. AWS Security Hub aggregates and prioritizes security findings from multiple AWS services into a centralized dashboard, but does not set up or manage multi-account environments.

</details>

---

### Question 264 — `CLF-U0915` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 3.6: Management, Monitoring & Application Integration*

**Treating infrastructure as code in the AWS Cloud allows users to:**

- A) automate migration of on-premises hardware to AWS data centers.
- B) let a third party automate an audit of the AWS infrastructure.
- C) turn over application code to AWS so it can run on the AWS infrastructure.
- D) automate the infrastructure provisioning process.

<details>
<summary><strong>Reveal Answer & Explanation (Question 264)</strong></summary>

**Correct Answer:** `D`

Infrastructure as code allows users to define and automate the provisioning of AWS resources using templates, enabling repeatable, version-controlled deployments without manual configuration.
Automating migration of on-premises hardware to AWS data centers is not possible through infrastructure as code, as physical hardware migration is a separate process managed outside of code-based provisioning. Letting a third party automate an audit of AWS infrastructure describes a compliance or security activity unrelated to infrastructure provisioning. Turning over application code to AWS to run on its infrastructure misrepresents how AWS works, as customers are always responsible for their own application code and deployment.

</details>

---

## 🎯 Domain 4: Billing, Pricing, and Support (12% — 36 Questions)

### Question 265 — `CLF-U0050` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which of the following describes the payment model that AWS makes available for customers that can commit to using Amazon EC2 over a one or 3-year term to reduce their total computing costs?**

- A) Pay less as AWS grows.
- B) Pay as you go.
- C) Pay less by using more.
- D) Save when you reserve.

<details>
<summary><strong>Reveal Answer & Explanation (Question 265)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Save when you commit**

The "Save when you commit" payment model accurately describes AWS's approach to offering discounts for long-term usage commitments, specifically with Amazon EC2 Reserved Instances and Savings Plans. By committing to a consistent usage level (e.g., a specific EC2 instance type and size) for a 1-year or 3-year term, customers can significantly reduce their EC2 costs compared to On-Demand pricing. This model rewards customers for their commitment with lower hourly rates.

**Incorrect:**

**A. Pay as you go** - "Pay as you go" is a general pricing principle for many AWS services, including EC2 On-Demand instances. While it offers flexibility, it doesn't provide the cost savings associated with a long-term commitment like Reserved Instances or Savings Plans.

**B. Pay less by using more** - While AWS often offers volume discounts (e.g., for S3 storage), this option doesn't directly relate to the specific scenario of committing to EC2 usage over a 3-year term. The primary cost reduction in that scenario comes from the commitment itself, not necessarily the overall volume of usage across all AWS services.

**C. Pay less as AWS grows** - While AWS may reduce prices over time due to economies of scale, this is not a specific payment model offered to customers for committing to EC2 usage. It's a general trend in cloud pricing, not a direct mechanism for reducing costs through commitment.

</details>

---

### Question 266 — `CLF-U0558` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**You have set up consolidated billing for several AWS accounts. One of the accounts has purchased a number of reserved instances for 3 years. Which of the following is true regarding this scenario?**

- A) The Reserved Instance discounts can only be shared with the master account.
- B) All accounts can receive the hourly cost benefit of the Reserved Instances.
- C) The purchased instances will have better performance than On-demand instances.
- D) There are no cost benefits from using consolidated billing; It is for informational purposes only.

<details>
<summary><strong>Reveal Answer & Explanation (Question 266)</strong></summary>

**Correct Answer:** `B`

**Correct answer: All accounts can receive the hourly cost benefit of the Reserved Instances**

With consolidated billing in AWS Organizations, the cost benefits of Reserved Instances (RIs) are shared across all accounts within the organization. When an account purchases RIs, the hourly cost benefit is applied to any matching usage across all accounts in the organization. This means that if another account in the organization uses an instance type that matches the RI, that account will receive the discounted rate. This ensures maximum utilization of the RIs and cost savings for the entire organization. The primary benefit of consolidated billing is to aggregate usage across multiple accounts to achieve volume discounts and efficient RI utilization.

**Incorrect:**

**B. There are no cost benefits from using consolidated billing; It is for informational purposes only** - This is incorrect. Consolidated billing provides significant cost benefits, including volume discounts and the sharing of Reserved Instance discounts across all accounts in the organization. It's not just for informational purposes; it directly impacts the overall AWS bill.

**C. The purchased instances will have better performance than On-demand instances** - This is incorrect. Reserved Instances do not inherently provide better performance than On-Demand instances. The performance of an instance is determined by its instance type (e.g., memory, CPU), not by the purchasing option (On-Demand vs. Reserved). Reserved Instances provide a billing discount, not a performance boost.

**D. The Reserved Instance discounts can only be shared with the master account** - This is incorrect. With consolidated billing, the Reserved Instance discounts are shared across all linked accounts in the organization, not just the master account. Any account that uses a matching instance type will benefit from the RI discount.

</details>

---

### Question 267 — `CLF-U0561` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**What do you gain from setting up consolidated billing for five different AWS accounts under another master account?**

- A) AWS services’ costs will be reduced to half the original price.
- B) The consolidated billing feature is just for organizational purpose.
- C) Each AWS account gets volume discounts.
- D) Each AWS account gets five times the free-tier services capacity.

<details>
<summary><strong>Reveal Answer & Explanation (Question 267)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Each AWS account gets volume discounts**

Consolidated billing in AWS allows you to combine billing and payment for multiple AWS accounts into one master account. A key benefit of this is that it can help you achieve volume discounts. AWS offers tiered pricing for many services, meaning the more you use, the lower the price per unit. By aggregating the usage across multiple accounts, you're more likely to reach higher usage tiers and qualify for these discounts, which are then applied across all participating accounts. This can result in significant cost savings compared to managing each account separately.

**Incorrect:**

**A. AWS services’ costs will be reduced to half the original price** - Consolidated billing facilitates volume discounts, but it does not automatically reduce costs to half the original price. The actual discount depends on the specific services used and the overall usage volume across all accounts.

**C. Each AWS account gets five times the free-tier services capacity** - Consolidated billing does not multiply the AWS Free Tier benefits for each account. The Free Tier is generally limited to one per organization, and its benefits are not scaled based on the number of accounts in a consolidated billing setup.

**D. The consolidated billing feature is just for organizational purposes** - While consolidated billing does offer organizational benefits by simplifying billing management, its primary advantage is the potential for cost savings through volume discounts. It's not solely for organizational purposes; the financial benefits are a significant driver for its adoption.

</details>

---

### Question 268 — `CLF-U0026` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**A company is concerned that they are spending money on underutilized compute resources in AWS. Which AWS feature will help ensure that their applications are automatically adding/removing EC2 compute capacity to closely match the required demand?**

- A) AWS Elastic Load Balancer.
- B) AWS Budgets.
- C) AWS Auto Scaling.
- D) AWS Cost Explorer.

<details>
<summary><strong>Reveal Answer & Explanation (Question 268)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS Auto Scaling**

AWS Auto Scaling automatically adjusts the number of EC2 instances in your application based on demand. It allows you to define scaling policies that specify how your application should respond to changes in traffic or resource utilization. When demand increases, Auto Scaling launches new instances to handle the load. When demand decreases, it terminates instances to reduce costs. This ensures that you have the right amount of compute capacity at all times, optimizing performance and minimizing expenses related to underutilized resources. Auto Scaling groups can be configured using metrics like CPU utilization, network traffic, or custom metrics.

**Incorrect:**

**A. AWS Cost Explorer** - AWS Cost Explorer helps you visualize, understand, and manage your AWS costs and usage over time. While it can identify potential cost savings opportunities, it doesn't automatically adjust compute capacity based on demand. It's a reporting and analysis tool, not an automation tool.

**B. AWS Budgets** - AWS Budgets allows you to set custom budgets that alert you when your costs or usage exceed your budgeted amount. It helps you track your spending and receive notifications when you're approaching or exceeding your budget limits. However, it doesn't automatically adjust compute capacity. It's a monitoring and alerting tool, not an automation tool.

**C. AWS Elastic Load Balancer** - An Elastic Load Balancer (ELB) distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. While ELB is essential for distributing traffic and improving application availability, it does not automatically add or remove EC2 instances based on demand. It works in conjunction with Auto Scaling to distribute traffic to the instances that Auto Scaling provisions.

</details>

---

### Question 269 — `CLF-U0076` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**Data security is one of the top priorities of AWS. How does AWS deal with old storage devices that have reached the end of their useful life?**

- A) AWS sells the old devices to other hosting providers.
- B) AWS destroys the old devices in accordance with industry-standard practices.
- C) AWS sends the old devices for remanufacturing.
- D) AWS stores the old devices in a secure place.

<details>
<summary><strong>Reveal Answer & Explanation (Question 269)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS destroys the old devices in accordance with industry-standard practices**

AWS prioritizes data security, including the secure disposal of storage devices that have reached the end of their useful life. AWS destroys these devices using industry-standard practices, which often involve physical destruction techniques like shredding or degaussing. This ensures that the data on these devices cannot be recovered, protecting customer data and maintaining compliance with security regulations. This process is a critical part of AWS's commitment to data security and compliance.

**Incorrect:**

**A. AWS sells the old devices to other hosting providers** - Selling old storage devices to other hosting providers would create a significant security risk, as the data on those devices could potentially be accessed by unauthorized parties. This is against AWS's security policies.

**C. AWS stores the old devices in a secure place** - Simply storing old devices, even in a secure location, does not eliminate the risk of data breaches. The data remains on the devices and could potentially be accessed if the storage location is compromised. Secure destruction is a more robust approach.

**D. AWS sends the old devices for remanufacturing** - Sending old storage devices for remanufacturing without proper data sanitization poses a significant security risk. Data could be recovered from the devices during the remanufacturing process or by unauthorized parties who gain access to the devices. This is not a secure practice.

</details>

---

### Question 270 — `CLF-U0126` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**There is a requirement to grant a DevOps team full administrative access to all resources in an AWS account. Who can grant them these permissions?**

- A) AWS account owner.
- B) AWS technical account manager.
- C) AWS security team.
- D) AWS cloud support engineers.

<details>
<summary><strong>Reveal Answer & Explanation (Question 270)</strong></summary>

**Correct Answer:** `A`

**Correct answer: AWS account owner**

The AWS account owner has ultimate control over the AWS account and is the only entity that can grant full administrative access to all resources within the account. This is because the account owner has root user privileges, which bypass all other permissions and access controls. Granting full administrative access typically involves creating an IAM role with the `AdministratorAccess` policy and then providing the DevOps team with credentials or a mechanism (like assuming the role) to use that role. Only the account owner, or someone with equivalent root user privileges, can make these fundamental changes to the account's security posture.

**Incorrect:**

**A. AWS security team** - While an AWS security team might exist within an organization using AWS, they do not have inherent privileges to grant administrative access at the AWS account level. They would need to be delegated those permissions by the AWS account owner.

**B. AWS cloud support engineers** - AWS Cloud Support engineers provide technical assistance and troubleshooting but do not have the authority to grant permissions within a customer's AWS account. Their access is limited and controlled by AWS.

**C. AWS technical account manager** - An AWS Technical Account Manager (TAM) is a designated point of contact for technical guidance and best practices. However, TAMs do not have the authority to make changes to a customer's AWS account permissions. Their role is advisory, not administrative.

</details>

---

### Question 271 — `CLF-U0564` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**How can you view the distribution of AWS spending in one of your AWS accounts?**

- A) By using Amazon VPC console.
- B) By contacting the AWS Support team.
- C) By using AWS Cost Explorer.
- D) By contacting the AWS Finance team.

<details>
<summary><strong>Reveal Answer & Explanation (Question 271)</strong></summary>

**Correct Answer:** `C`

**Correct answer: By using AWS Cost Explorer**

AWS Cost Explorer is a service that enables you to visualize, understand, and manage your AWS costs and usage over time. You can use Cost Explorer to identify cost drivers, understand spending trends, and detect anomalies. It provides detailed reports and visualizations of your AWS spending, allowing you to analyze your costs by service, region, account, and other dimensions. This helps you understand the distribution of your AWS spending and optimize your cloud infrastructure for cost efficiency.

**Incorrect:**

**A. By using Amazon VPC console** - The Amazon VPC console is used for managing your virtual private cloud (VPC) resources, such as subnets, route tables, and security groups. It does not provide information about AWS spending or cost distribution.

**B. By contacting the AWS Support team** - While the AWS Support team can assist with billing inquiries, they are not the primary tool for viewing the distribution of AWS spending. AWS Cost Explorer provides a self-service interface for analyzing cost data.

**D. By contacting the AWS Finance team** - The AWS Finance team is not directly involved in providing customers with access to their AWS spending data. AWS provides tools like Cost Explorer for customers to manage and analyze their own cost information.

</details>

---

### Question 272 — `CLF-U0583` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**Which AWS service provides cost-optimization recommendations?**

- A) AWS Trusted Advisor.
- B) AWS Pricing Calculator.
- C) Amazon QuickSight.
- D) AWS X-Ray.

<details>
<summary><strong>Reveal Answer & Explanation (Question 272)</strong></summary>

**Correct Answer:** `A`

**Correct answer: AWS Trusted Advisor**

AWS Trusted Advisor is an online tool that provides real-time guidance to help you provision your resources following AWS best practices. Trusted Advisor checks help optimize your AWS infrastructure, increase security and performance, reduce costs, and monitor service limits. It provides recommendations across five categories: Cost Optimization, Security, Fault Tolerance, Performance, and Service Limits. Therefore, it is the correct answer as it directly provides cost-optimization recommendations.

**Incorrect:**

**A. AWS X-Ray** - AWS X-Ray is a service that helps developers analyze and debug distributed applications. It provides insights into the performance of applications and helps identify bottlenecks. It does not provide cost optimization recommendations.

**C. AWS Pricing Calculator** - AWS Pricing Calculator lets you estimate the cost of using AWS services. While it helps in planning and understanding costs before deployment, it doesn't provide ongoing recommendations for optimizing existing infrastructure costs. It's a planning tool, not an optimization advisor.

**D. Amazon QuickSight** - Amazon QuickSight is a business intelligence service that allows you to create and share interactive dashboards and reports. It helps visualize data and gain insights, but it does not provide cost optimization recommendations.

</details>

---

### Question 273 — `CLF-U0586` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**A company is trying to analyze the costs applied to their AWS account recently. Which of the following provides them the most granular data about their AWS costs and usage?**

- A) Amazon Machine Image.
- B) AWS Cost Explorer.
- C) AWS Cost & Usage Report.
- D) Amazon CloudWatch.

<details>
<summary><strong>Reveal Answer & Explanation (Question 273)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS Cost & Usage Report**

The AWS Cost & Usage Report (CUR) provides the most granular data about your AWS costs and usage. It contains detailed information about your AWS usage, including hourly, daily, or monthly data aggregation, and resource-level details. This allows for in-depth analysis of spending patterns and identification of cost optimization opportunities. The CUR can be delivered to an Amazon S3 bucket in CSV or Parquet format, enabling further analysis using tools like Amazon Athena or Amazon QuickSight.

**Incorrect:**

**A. Amazon CloudWatch** - Amazon CloudWatch is a monitoring and observability service. While it can track metrics related to resource utilization that indirectly impact costs, it doesn't provide detailed cost breakdowns or billing information. CloudWatch primarily focuses on performance monitoring, logging, and event management, not cost analysis.

**C. AWS Cost Explorer** - AWS Cost Explorer is a tool that allows you to visualize and forecast your AWS costs. While helpful for understanding spending trends and identifying areas for optimization, it presents aggregated data and doesn't offer the same level of granularity as the Cost & Usage Report. Cost Explorer uses the data from the Cost & Usage Report to create its visualizations.

**D. Amazon Machine Image** - An Amazon Machine Image (AMI) is a template containing a software configuration (operating system, application server, and applications) required to launch your instances. It has no direct relevance to cost analysis or providing cost and usage data.

</details>

---

### Question 274 — `CLF-U0592` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**What is the AWS tool that can help a company visualize their AWS spending in the last few months?**

- A) AWS Cost Explorer.
- B) AWS Pricing Calculator.
- C) AWS Budgets.
- D) AWS Consolidated Billing.

<details>
<summary><strong>Reveal Answer & Explanation (Question 274)</strong></summary>

**Correct Answer:** `A`

**Correct answer: AWS Cost Explorer**

AWS Cost Explorer is a tool that enables you to visualize your AWS spending patterns over time. It provides interactive graphs and tables that allow you to analyze your costs by service, region, availability zone, and other dimensions. You can use Cost Explorer to identify trends, understand cost drivers, and forecast future spending. It is specifically designed for analyzing historical cost data and identifying opportunities for cost optimization.

**Incorrect:**

**A. AWS Consolidated Billing** - AWS Consolidated Billing allows you to consolidate billing and payment for multiple AWS accounts into one bill. While it simplifies billing management, it doesn't provide the visualization capabilities for analyzing spending patterns that Cost Explorer offers. It's primarily for organizational and payment convenience, not for cost analysis.

**C. AWS Pricing Calculator** - AWS Pricing Calculator is used to estimate the cost of AWS services before you deploy them. It helps you plan your architecture and understand the potential costs, but it doesn't provide historical spending data or visualization of past costs. It's a planning tool, not an analysis tool.

**D. AWS Budgets** - AWS Budgets allows you to set custom budgets that track your AWS costs and usage. You can receive alerts when your costs exceed your budget thresholds. While Budgets helps you control and monitor spending, it doesn't provide the detailed visualization and analysis capabilities of Cost Explorer for understanding past spending patterns.

</details>

---

### Question 275 — `CLF-U0559` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**A company has an AWS Enterprise Support plan. They want quick and efficient guidance with their billing and account inquiries. Which of the following should the company use?**

- A) AWS Health Dashboard.
- B) AWS Support Concierge.
- C) AWS Customer Service.
- D) AWS Operations Support.

<details>
<summary><strong>Reveal Answer & Explanation (Question 275)</strong></summary>

**Correct Answer:** `B`

**Correct answer: AWS Support Concierge**

The AWS Support Concierge is a billing and account support team that provides quick and efficient answers to your billing and account inquiries. They can assist with billing and account questions, but do not provide technical support. This is a key benefit of the Enterprise Support plan.

**Incorrect:**

**B. AWS Operations Support** - AWS Operations Support is not a defined service or feature within AWS support plans. The Enterprise Support plan includes access to technical account managers and other resources, but "Operations Support" is not a specific offering.

**C. AWS Health Dashboard** - The AWS Health Dashboard provides personalized view of the health of AWS services and resources. While it can help identify potential issues that might impact billing (e.g., unexpected resource usage due to a service outage), it doesn't directly provide guidance on billing and account inquiries.

**D. AWS Customer Service** - While AWS Customer Service exists, the AWS Support Concierge is the dedicated resource for billing and account inquiries under the Enterprise Support plan. The Concierge provides a more specialized and efficient service for these specific types of questions compared to general AWS Customer Service.

</details>

---

### Question 276 — `CLF-U0563` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**As part of the Enterprise support plan, who is the primary point of contact for ongoing support needs?**

- A) AWS Identity and Access Management (IAM) user.
- B) Infrastructure Event Management (IEM) engineer.
- C) AWS Consulting Partners.
- D) Technical Account Manager (TAM).

<details>
<summary><strong>Reveal Answer & Explanation (Question 276)</strong></summary>

**Correct Answer:** `D`

**Correct answer: Technical Account Manager (TAM)**

The Technical Account Manager (TAM) is the primary point of contact for customers with the Enterprise support plan. The TAM provides technical expertise and guidance to help customers plan, build, and optimize their AWS environments. They act as a trusted advisor, proactively working with the customer to understand their business goals and technical needs, and then providing recommendations and best practices to help them achieve those goals. The TAM also helps coordinate support efforts across different AWS teams, ensuring that the customer receives timely and effective assistance.

**Incorrect:**

**A. Infrastructure Event Management (IEM) engineer** - Infrastructure Event Management (IEM) is a service offered under the Enterprise Support plan, but the IEM engineer is not the primary point of contact for ongoing support needs. IEM is focused on providing support during critical events and outages.

**B. AWS Identity and Access Management (IAM) user** - An IAM user is an identity within AWS that represents a person or application. IAM users are used to control access to AWS resources, but they are not related to AWS support plans or providing support.

**D. AWS Consulting Partners** - AWS Consulting Partners can provide support and guidance, but they are not the primary point of contact within AWS for Enterprise support plan customers. While partners may be engaged, the TAM is the direct AWS contact.

</details>

---

### Question 277 — `CLF-U0566` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**What does the AWS Health Dashboard provide? (Choose TWO)**

- A) Detailed troubleshooting guidance to address AWS events impacting your resources.
- B) Health checks for Auto Scaling instances.
- C) Recommendations for Cost Optimization.
- D) A dashboard detailing vulnerabilities in your applications.
- E) Personalized view of AWS service health.

<details>
<summary><strong>Reveal Answer & Explanation (Question 277)</strong></summary>

**Correct Answer:** `A, E`

**Correct answer: Detailed troubleshooting guidance to address AWS events impacting your resources**

The AWS Health Dashboard provides detailed information and troubleshooting guidance related to AWS events that might affect your resources. This includes explanations of the event, affected services and regions, and recommended actions to mitigate the impact. It helps users understand and respond to AWS-related issues promptly.

**Correct answer: Personalized view of AWS service health**

The AWS Health Dashboard offers a personalized view of the health of AWS services that you are using. It displays information relevant to your specific AWS account and the services you are utilizing, allowing you to quickly assess the status of your resources and identify any potential issues affecting your environment.

**Incorrect:**

**A. Recommendations for Cost Optimization** - The AWS Health Dashboard primarily focuses on the operational health of AWS services. Cost optimization recommendations are typically provided by services like AWS Trusted Advisor or AWS Cost Explorer, not the Health Dashboard.

**C. Health checks for Auto Scaling instances** - Health checks for Auto Scaling instances are configured and managed within the Auto Scaling service itself, using Elastic Load Balancing (ELB) or custom health check configurations. The AWS Health Dashboard provides broader service health information, not instance-level health checks within Auto Scaling groups.

**D. A dashboard detailing vulnerabilities in your applications** - The AWS Health Dashboard focuses on the health of AWS services, not vulnerabilities within your applications. Services like AWS Inspector or third-party vulnerability scanners are used to identify and manage vulnerabilities in your applications.

</details>

---

### Question 278 — `CLF-U0573` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**A company is introducing a new product to their customers, and is expecting a surge in traffic to their web application. As part of their Enterprise Support plan, which of the following provides the company with architectural and scaling guidance?**

- A) AWS Knowledge Center.
- B) AWS Health Dashboard.
- C) Infrastructure Event Management.
- D) AWS Support Concierge Service.

<details>
<summary><strong>Reveal Answer & Explanation (Question 278)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Infrastructure Event Management**

Infrastructure Event Management, offered as part of the AWS Enterprise Support plan, provides architectural and scaling guidance for specific events, such as a new product launch or a large marketing campaign that is expected to drive significant traffic. AWS experts will work with the company to review their architecture, identify potential bottlenecks, and provide recommendations for scaling their infrastructure to handle the anticipated load. This proactive approach helps ensure a smooth and successful event.

**Incorrect:**

**A. AWS Support Concierge Service** - The AWS Support Concierge Service focuses on billing and account support. It assists with navigating AWS, understanding billing, and managing accounts, but it does not provide architectural or scaling guidance.

**B. AWS Health Dashboard** - The AWS Health Dashboard provides a personalized view of the health of AWS services and resources. While it can help identify issues that might impact performance, it doesn't offer proactive architectural or scaling guidance in anticipation of an event.

**D. AWS Knowledge Center** - The AWS Knowledge Center is a repository of articles and documentation that can help answer common questions about AWS services. While it's a valuable resource for general information, it doesn't provide the personalized architectural and scaling guidance offered by Infrastructure Event Management.

</details>

---

### Question 279 — `CLF-U0584` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**Which support plan includes AWS Support Concierge Service?**

- A) Premium Support.
- B) Business Support.
- C) Enterprise Support.
- D) Standard Support.

<details>
<summary><strong>Reveal Answer & Explanation (Question 279)</strong></summary>

**Correct Answer:** `C`

**Correct answer: Enterprise Support**

The Enterprise Support plan is the only AWS Support plan that includes the AWS Support Concierge service. The Concierge provides assistance with billing and account inquiries. It also helps navigate AWS and provides guidance on billing best practices. This is a key differentiator for the Enterprise Support plan, which is designed for mission-critical workloads and provides the highest level of support.

**Incorrect:**

**A. Business Support** - Business Support provides access to technical support engineers via email, chat, and phone. While it offers a higher level of support than Developer or Basic, it does not include the Concierge service for billing and account management.

**B. Standard Support** - Standard Support is intended for customers who are experimenting with AWS or running production workloads. It provides access to basic technical support and general guidance, but it does not include the Concierge service.

**C. Premium Support** - There is no AWS Support plan called "Premium Support." The available support plans are Basic, Developer, Standard, Business, and Enterprise.

</details>

---

### Question 280 — `CLF-U0596` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**What is the AWS Support feature that allows customers to manage support cases programmatically?**

- A) AWS Trusted Advisor.
- B) AWS Operations Support.
- C) AWS Support API.
- D) AWS Health Dashboard (formerly AWS AWS Health Dashboard (Your Account Health)).

<details>
<summary><strong>Reveal Answer & Explanation (Question 280)</strong></summary>

**Correct Answer:** `C`

**Correct answer: AWS Support API**

The AWS Support API provides programmatic access to AWS Support features. This allows customers to create, manage, and close support cases using code. This is useful for automating support workflows, integrating support processes with other systems, and building custom support tools. The API allows you to interact with AWS Support programmatically, enabling automation and integration with other systems.

**Incorrect:**

**B. AWS Trusted Advisor** - AWS Trusted Advisor is an online tool that provides real-time guidance to help you provision your resources following AWS best practices. It inspects your AWS environment and makes recommendations for saving money, improving system performance and reliability, and closing security gaps. It does not manage support cases.

**C. AWS Health Dashboard** - The AWS Health Dashboard provides personalized view of the health of AWS services and resources. While it provides information about AWS service availability and events that might affect your applications, it does not allow you to manage support cases programmatically.

**D. AWS Operations Support** - AWS Operations Support is a general term referring to the support provided by AWS operations teams. While these teams are involved in resolving issues, there isn't a specific "AWS Operations Support" feature that allows programmatic management of support cases. The AWS Support API is the correct tool for this purpose.

</details>

---

### Question 281 — `CLF-U0604` | 🔁 Repeated in 4 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**Which features are included in the AWS Business Support Plan? (Choose TWO)**

- A) 24x7 access to customer service.
- B) Access to Cloud Support Engineers via email only during business hours.
- C) Access to the Infrastructure Event Management (IEM) feature for additional fee.
- D) 24x7 access to the TAM feature.
- E) Partial access to the core Trusted Advisor checks.

<details>
<summary><strong>Reveal Answer & Explanation (Question 281)</strong></summary>

**Correct Answer:** `A, C`

**Correct answer: Access to the Infrastructure Event Management (IEM) feature for additional fee**

The AWS Business Support plan includes access to Infrastructure Event Management (IEM) for an additional fee. IEM provides architectural and scaling guidance during events such as product launches and marketing campaigns. This helps ensure your infrastructure is prepared for increased demand and potential issues. This feature is not included in the Developer or Basic support plans.

**Correct answer: 24x7 access to customer service**

The AWS Business Support plan provides 24x7 access to customer service. This means you can contact AWS support at any time of day or night for assistance with billing, account, and other non-technical issues. This is a key benefit over the Basic support plan, which does not offer this level of access.

**Incorrect:**

**A. Partial access to the core Trusted Advisor checks** - The Business Support plan provides full access to all Trusted Advisor checks, not just partial access. Partial access to Trusted Advisor checks is available in the Basic and Developer support plans. The Business and Enterprise support plans offer full access.

**B. 24x7 access to the TAM feature** - 24x7 access to a Technical Account Manager (TAM) is a feature of the Enterprise Support plan, not the Business Support plan. A TAM provides proactive guidance and support to help you optimize your AWS environment.

**C. Access to Cloud Support Engineers via email only during business hours** - The Business Support plan provides access to Cloud Support Engineers via email, chat, and phone, with 24x7 availability. The response time depends on the severity of the issue. This option incorrectly states that access is email-only and limited to business hours.

</details>

---

### Question 282 — `CLF-U0101` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which AWS Service offers volume discounts based on usage?**

- A) Amazon VPC.
- B) Amazon S3.
- C) Amazon Lightsail.
- D) AWS Cost Explorer.

<details>
<summary><strong>Reveal Answer & Explanation (Question 282)</strong></summary>

**Correct Answer:** `B`

Amazon S3 uses a tiered pricing model where the per-GB storage cost decreases as your total usage increases, automatically providing volume discounts to customers who store more data.
Amazon VPC is a networking service that lets you provision isolated virtual networks within AWS, and while VPC itself is free the resources deployed within it such as NAT Gateways are charged individually without volume-based discounts. Amazon Lightsail is a simplified compute service with straightforward bundled pricing for virtual servers and web applications, and uses fixed pricing tiers rather than volume discounts based on usage. AWS Cost Explorer provides visualisation and analysis of AWS spending patterns over time, and is a cost management tool rather than an AWS service that applies volume-based pricing discounts.

</details>

---

### Question 283 — `CLF-U0574` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which of the below is a best-practice when designing solutions on AWS?**

- A) Invest heavily in architecting your environment, as it is not easy to change your design later.
- B) Use AWS reservations to reduce costs when testing your production environment.
- C) Automate wherever possible to make architectural (© ) experimentation easier.
- D) Provision a large compute capacity to handle any spikes in load

<details>
<summary><strong>Reveal Answer & Explanation (Question 283)</strong></summary>

**Correct Answer:** `C`

AWS best practice is to automate infrastructure and deployment wherever possible, which makes architectural experimentation faster and reduces human error.
Investing heavily in upfront architectural design contradicts the cloud principle that infrastructure should be treated as flexible and changeable, with automation enabling rapid iteration rather than requiring heavy planning before deployment. Using AWS reservations to reduce costs when testing production environments misapplies Reserved Instances, which are a billing commitment for predictable steady-state workloads rather than a cost reduction tool for testing environments. Provisioning large compute capacity to handle any spikes in load describes over-provisioning, which is an on-premises anti-pattern that cloud best practices replace with elastic scaling that dynamically matches capacity to actual demand.

</details>

---

### Question 284 — `CLF-U0598` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**A user has opened a "Production System Down" support case to get help from AWS Support after a production system disruption. What is the expected response time for this type of support case?**

- A) 12 hours.
- B) 15 minutes.
- C) 24 hours.
- D) One hour.

<details>
<summary><strong>Reveal Answer & Explanation (Question 284)</strong></summary>

**Correct Answer:** `D`

For a Production System Down case on the Business or Enterprise Support plan, the expected response time is one hour, ensuring critical production outages receive rapid attention from AWS Support.
A 12-hour response time corresponds to the general guidance response target for Developer Support customers on a system-impaired case, not the production system-down response time for Business or Enterprise Support. A 15-minute response time is the SLA for business-critical system failures under the Enterprise Support plan, which is a faster tier than the one-hour production system-down SLA available starting at Business Support. A 24-hour response time is the general guidance response target for Developer Support customers on general guidance cases, and does not apply to production system outages at the Business or Enterprise Support level.

</details>

---

### Question 285 — `CLF-U0623` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which statement is true regarding AWS pricing? (Choose TWO)**

- A) With the AWS pay-as-you-go pricing model, you don't have to pay any upfront fee.
- B) You have no responsibility for third-party software license costs.
- C) You only pay for the individual services that you need with no long-term contracts.
- D) For some services, you have to pay a startup fee in order to get the service running.
- E) There are no reservations on AWS, you only pay for what you use.

<details>
<summary><strong>Reveal Answer & Explanation (Question 285)</strong></summary>

**Correct Answer:** `A, C`

AWS pay-as-you-go pricing requires no upfront fees or long-term contracts. You pay only for the individual services you use with no minimum commitments.
Customers do retain responsibility for third-party software license costs when running applications on AWS, unless they use AWS-provided licenses through services such as Amazon RDS. AWS does not take on software licensing obligations on the customer's behalf. For some services AWS does offer a startup fee, and Reserved Instances require upfront payment. However, the pay-as-you-go model for On-Demand services requires no startup fee. AWS does offer reservations such as Reserved Instances and Savings Plans that provide discounts in exchange for usage commitments, so the claim that there are no reservations on AWS is incorrect.

</details>

---

### Question 286 — `CLF-U0638` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which of the following BEST describe the AWS pricing model? (Select TWO)**

- A) Fixed-term.
- B) Pay-as-you-go.
- C) Colocation.
- D) Planned.
- E) Variable cost.

<details>
<summary><strong>Reveal Answer & Explanation (Question 286)</strong></summary>

**Correct Answer:** `B, E`

AWS pricing is pay-as-you-go and variable cost. There are no fixed terms required, no colocation fees, and no mandatory upfront plans.
Fixed-term pricing requires a commitment to a set contract duration, which is the opposite of the AWS pay-as-you-go model where usage can scale up or down at any time without contractual obligations. Colocation refers to housing customer-owned servers in a third-party data center, which is an on-premises model rather than a cloud pricing principle. Planned pricing implies predetermined usage schedules and costs, which contradicts the AWS model where customers pay based on actual consumption without mandatory advance planning.

</details>

---

### Question 287 — `CLF-U0652` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which of the following are advantages of AWS consolidated billing? (Select TWO)**

- A) The ability to receive one bill for multiple accounts.
- B) Service limits increasing by default in all accounts.
- C) A fixed discount on the monthly bill.
- D) Potential volume discounts, as usage in all accounts is combined.
- E) The automatic extension of the master account’s AWS support plan to all accounts.

<details>
<summary><strong>Reveal Answer & Explanation (Question 287)</strong></summary>

**Correct Answer:** `A, D`

Consolidated billing produces a single combined invoice for all accounts in an AWS Organization, and it pools usage across all accounts to qualify for volume pricing tiers.
Service limits do not automatically increase for all accounts under consolidated billing. Service limit increases must be requested individually through AWS Support on a per-service and per-region basis. Consolidated billing does not provide a fixed discount on the monthly bill. Volume discounts are applied progressively based on combined usage tiers and vary by service rather than applying a uniform percentage reduction. The master account's AWS Support plan is not automatically extended to all member accounts. Each account within an AWS Organization must maintain its own support plan, and support plan costs and benefits remain account-specific.

</details>

---

### Question 288 — `CLF-U1485` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.1: Pricing Models & Purchasing Options*

**Which of the following is an architectural design principle of the AWS Well-Architected Framework?**

- A) Loosely couple components
- B) Build monolithic systems
- C) Scale vertically, not horizontally
- D) Use third-party software

<details>
<summary><strong>Reveal Answer & Explanation (Question 288)</strong></summary>

**Correct Answer:** `A`

- **Option A** ✅ (CORRECT): Option A directly satisfies the requirement based on AWS architectural best practices and official documentation.
- **Option B** ❌ (INCORRECT): Option B does not meet the specified criteria or refers to a different AWS service capability.
- **Option C** ❌ (INCORRECT): Option C does not meet the specified criteria or refers to a different AWS service capability.
- **Option D** ❌ (INCORRECT): Option D does not meet the specified criteria or refers to a different AWS service capability.

</details>

---

### Question 289 — `CLF-U0170` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**Which of the following security resources are available to any user for free? (Choose TWO)**

- A) AWS Bulletins.
- B) AWS TAM.
- C) AWS Support APl.
- D) AWS Security Blog.
- E) AWS Classroom Training.

<details>
<summary><strong>Reveal Answer & Explanation (Question 289)</strong></summary>

**Correct Answer:** `A, D`

AWS documentation provides comprehensive technical guides and API references for all AWS services at no cost and is freely accessible to any user, and AWS discussion forums allow any user to post questions and share knowledge about AWS services at no charge. Both are free security resources.
AWS Support Center provides technical case support that requires a paid support plan to submit cases, and while some basic content is available for free, the case submission feature for getting direct engineering assistance is not a free resource available to all users without a qualifying support plan. AWS Managed Services provides ongoing management of AWS infrastructure on behalf of enterprise customers for a fee, and is a paid service rather than a free security resource available to any user. Amazon Inspector is an automated vulnerability assessment service that requires configuration and generates findings, and while there is a free trial period, it is a paid service rather than a free resource available to all users without any cost.

</details>

---

### Question 290 — `CLF-U0609` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**What best describes penetration testing?**

- A) Testing your application’s response time from different locations.
- B) Testing your network to find security vulnerabilities that an attacker could exploit.
- C) Testing your instances to check for the unhealthy ones.
- D) Testing your software for bugs and errors.

<details>
<summary><strong>Reveal Answer & Explanation (Question 290)</strong></summary>

**Correct Answer:** `B`

Penetration testing is the practice of simulating cyberattacks against your own systems to discover exploitable security vulnerabilities before malicious attackers can find and use them, allowing you to remediate weaknesses proactively.
Testing application response time from different locations describes performance and latency testing, which evaluates how quickly an application responds to requests from various geographic locations rather than identifying security vulnerabilities that attackers could exploit. Testing instances to check for unhealthy ones describes health checking or monitoring, which verifies that compute instances are operational and responsive rather than assessing the security posture of the network for exploitable weaknesses. Testing software for bugs and errors describes functional or quality assurance testing, which validates that code behaves as expected rather than specifically probing for security vulnerabilities that an attacker could use to gain unauthorised access.

</details>

---

### Question 291 — `CLF-U0615` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**Which AWS Cost Governance best practice recommends refining workloads regularly to make the most of existing AWS resources and reduce costs?**

- A) Tagging Enforcement.
- B) Architecture Optimization.
- C) Budgeting Processes.
- D) Resource Controls.

<details>
<summary><strong>Reveal Answer & Explanation (Question 291)</strong></summary>

**Correct Answer:** `B`

Architecture Optimization involves regularly reviewing and refining workloads to ensure they use the most efficient AWS resource types, sizes, and configurations, directly reducing costs while maintaining performance.
Tagging Enforcement is a cost governance practice that requires resources to be labeled with specific tags before they can be created or used, which improves cost visibility and attribution but is a compliance and visibility mechanism rather than a practice focused on refining workloads to better utilize existing resources. Budgeting Processes involve setting cost and usage thresholds and tracking actual spending against those budgets, which helps manage financial expectations but does not itself involve reviewing and optimizing underlying resource configurations. Resource Controls restrict which resources users can provision or how they can be configured, and while they prevent unnecessary resource creation they are a governance guardrail rather than a practice of regularly reviewing existing workloads.

</details>

---

### Question 292 — `CLF-U0673` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.2: Cost Management, Governance & Budgets*

**Which of the following security-related services does AWS offer? (Select TWO)**

- A) Multi-factor authentication physical tokens.
- B) AWS Trusted Advisor security checks.
- C) Data encryption.
- D) Automated penetration testing.
- E) Amazon S3 copyrighted content detection.

<details>
<summary><strong>Reveal Answer & Explanation (Question 292)</strong></summary>

**Correct Answer:** `B, C`

AWS Trusted Advisor includes security checks that flag vulnerabilities such as open security groups, and AWS provides data encryption capabilities through services like KMS and native encryption across storage and database services. Both are genuine AWS security-related offerings.
Multi-factor authentication physical tokens are hardware MFA devices that customers purchase independently rather than a service provided by AWS; customers configure them with their accounts but AWS does not supply or manufacture the hardware tokens. Automated penetration testing is not an AWS service offering; AWS permits customers to conduct their own penetration testing on permitted services, but AWS does not perform automated penetration testing on customer workloads as a service. Amazon S3 copyrighted content detection is not an AWS service; Amazon Macie detects sensitive data categories such as PII in S3, but copyright detection is not within the scope of available AWS security services.

</details>

---

### Question 293 — `CLF-U0616` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**Which of the following AWS support plans provides access to only the seven core AWS Trusted Advisor checks?**

- A) Business & Enterprise Support.
- B) Basic & Developer Support.
- C) Developer & Enterprise Support.
- D) Developer & Business Support.

<details>
<summary><strong>Reveal Answer & Explanation (Question 293)</strong></summary>

**Correct Answer:** `B`

Basic and Developer Support plans provide access to only the seven core Trusted Advisor checks. The full set of Trusted Advisor checks requires a Business or Enterprise Support plan.
Business and Enterprise Support plans both provide access to the full suite of Trusted Advisor checks rather than only the seven core checks, so this option describes the plans with the most Trusted Advisor access rather than those limited to seven checks. Developer and Enterprise Support is an incorrect pairing because Developer Support is limited to the seven core checks while Enterprise Support has access to the full suite, meaning they are at opposite ends of the Trusted Advisor access spectrum. Developer and Business Support is an incorrect pairing because Business Support provides the full suite of Trusted Advisor checks while Developer Support is limited to the seven core checks, so only Developer Support belongs in this limited-access category.

</details>

---

### Question 294 — `CLF-U0653` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**Which is the MINIMUM AWS Support plan that allows for one-hour target response time for support cases?**

- A) Enterprise.
- B) Business.
- C) Developer
- D) Basic

<details>
<summary><strong>Reveal Answer & Explanation (Question 294)</strong></summary>

**Correct Answer:** `B`

AWS Business Support guarantees a one-hour response time for production system-down cases and provides 24/7 phone, email, and chat access. Developer Support offers business-hours email only; Basic has no case support; Enterprise offers faster response but at higher cost.
Enterprise Support provides faster response times including a 15-minute SLA for business-critical system failures, and also meets the one-hour production system-down SLA, but it is a higher-cost plan than Business Support and therefore not the minimum required. Developer Support provides business-hours email access to Cloud Support Engineers with response times measured in hours rather than one hour, and does not include 24/7 access or a one-hour production system-down SLA. Basic Support provides access to documentation and the seven core Trusted Advisor checks but includes no technical case support and no defined response time SLAs.

</details>

---

### Question 295 — `CLF-U0654` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**What AWS team assists customers with accelerating cloud adoption through paid engagements in any of several specialty practice areas?**

- A) AWS Enterprise Support.
- B) AWS Solutions Architects.
- C) AWS Professional Services.
- D) AWS Account Managers.

<details>
<summary><strong>Reveal Answer & Explanation (Question 295)</strong></summary>

**Correct Answer:** `C`

AWS Professional Services is a global team of experts that helps customers achieve their desired business outcomes on AWS through paid engagements across specialty practice areas including migration, security, and data analytics.
AWS Enterprise Support is a paid support plan that provides access to a Technical Account Manager and 24/7 access to senior cloud support engineers, but it is a support tier rather than a consulting engagement team that works on specialty practice projects. AWS Solutions Architects advise customers on designing well-architected solutions and are available through various AWS programs, but they provide architectural guidance rather than leading paid consulting engagements across specialty practice areas. AWS Account Managers manage the overall commercial relationship between AWS and a customer, but they handle account and sales activities rather than delivering hands-on technical consulting engagements.

</details>

---

### Question 296 — `CLF-U0968` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.3: AWS Support Plans & Trusted Advisor*

**An external auditor has requested that a company provide a list of all its IAM users, including the status of users' credentials and access keys. What it the SIMPLEST way to provide this information?**

- A) Create an IAM user account for the auditor, granting the auditor administrator permissions.
- B) Take a screenshot of each user's page in the AWS Management Console, then provide the screenshots to the auditor.
- C) Download the IAM credential report, then provide the report to the auditor.
- D) Download the AWS Trusted Advisor report, then provide the report to the auditor.

<details>
<summary><strong>Reveal Answer & Explanation (Question 296)</strong></summary>

**Correct Answer:** `C`

The IAM credential report is a downloadable CSV file that lists all IAM users in the account along with the status of their credentials including passwords, access keys, MFA devices, and last-used timestamps, providing exactly what is needed for a user access audit.
AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules, and is a resource configuration compliance tool rather than an IAM user listing service. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability service rather than a source of IAM user account information or credential status reports. AWS CloudTrail records all API calls and management events including IAM-related actions, and while it logs who created users and when, it does not provide a current consolidated list of all users and their credential status in the way the credential report does.

</details>

---

### Question 297 — `CLF-U0577` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.4: AWS Marketplace & Partner Ecosystem*

**A company has created a solution that helps AWS customers improve their architectures on AWS. Which AWS program may support this company?**

- A) APN Consulting Partners.
- B) AWS TAM.
- C) APN Technology Partners.
- D) AWS Professional Services.

<details>
<summary><strong>Reveal Answer & Explanation (Question 297)</strong></summary>

**Correct Answer:** `A`

APN Consulting Partners are professional services firms certified by AWS to design, build, and manage customer workloads on AWS, including solutions that help other customers improve their architectures.
AWS TAM is a Technical Account Manager, which is a direct AWS resource assigned to enterprise support customers rather than an independent partner program a company can join to offer consulting services. APN Technology Partners are companies that provide software products and solutions that run on or integrate with AWS, rather than consulting or professional services that help customers improve their architectures. AWS Professional Services is a global team of AWS experts that works directly with customers on their own projects, and is not a program that external companies can join to deliver services to other customers.

</details>

---

### Question 298 — `CLF-U0618` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.4: AWS Marketplace & Partner Ecosystem*

**What AWS service allows you to buy third-party software solutions and services that run on AWS resources?**

- A) AWS Application Discovery service.
- B) Amazon DevPay.
- C) AWS Marketplace.
- D) Resource Groups.

<details>
<summary><strong>Reveal Answer & Explanation (Question 298)</strong></summary>

**Correct Answer:** `C`

AWS Marketplace is a digital catalog where customers can find, buy, and deploy third-party software solutions that run on AWS, including AMIs, SaaS applications, and data products.
AWS Application Discovery Service collects information about on-premises servers and workloads to help plan cloud migrations, and is a migration planning tool with no capability to purchase or deploy third-party software. AWS Cost Explorer provides visualisation and analysis of AWS spending and usage patterns over time, and is a cost management tool rather than a software procurement platform. AWS Resource Groups organizes AWS resources into logical groups based on tags or CloudFormation stacks for easier management, and has no role in discovering or purchasing third-party software solutions.

</details>

---

### Question 299 — `CLF-U0626` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.4: AWS Marketplace & Partner Ecosystem*

**What are the benefits of the AWS Marketplace service? (Choose TWO)**

- A) Protects customers by performing periodic security checks on listed products.
- B) Per-second billing.
- C) Provides cheaper options for purchasing Amazon EC2 on-demand instances.
- D) Provides flexible pricing options that suit most customer needs.
- E) Provides software solutions that run on AWS or any other Cloud vendor.

<details>
<summary><strong>Reveal Answer & Explanation (Question 299)</strong></summary>

**Correct Answer:** `D, E`

AWS Marketplace offers flexible pricing options including hourly, monthly, annual, and bring-your-own-license models, and provides software solutions that can run on AWS or other cloud platforms, giving customers broad choice and cost flexibility.
AWS Marketplace does not perform periodic security checks on listed products. Responsibility for product security remains with the independent software vendors who list their products. Per-second billing is an EC2 pricing feature, not a benefit of AWS Marketplace. Providing cheaper options for purchasing EC2 on-demand instances is not a function of AWS Marketplace, which is a catalog for third-party software, not a mechanism for discounting AWS compute pricing.

</details>

---

### Question 300 — `CLF-U0650` | 🔁 Repeated in 3 Exam Sources
*Topic: Topic 4.4: AWS Marketplace & Partner Ecosystem*

**A customer would like to design and build a new workload on AWS Cloud but does not have the AWS-related software technical expertise in-house. Which of the following AWS programs can a customer take advantage of to achieve that outcome?**

- A) AWS Partner Network Technology Partners.
- B) AWS Marketplace.
- C) AWS Partner Network Consulting Partners.
- D) AWS Service Catalog.

<details>
<summary><strong>Reveal Answer & Explanation (Question 300)</strong></summary>

**Correct Answer:** `C`

AWS Partner Network Consulting Partners are professional services firms that help customers design, build, migrate, and manage AWS workloads. Technology Partners provide software and tools; the Marketplace is for purchasing software.
AWS Partner Network Technology Partners develop software, tools, and services that complement AWS, and are product companies rather than professional services firms that help customers directly design and build workloads from scratch. AWS Marketplace is a digital catalog where customers can discover and purchase third-party software solutions, and is a procurement platform rather than a professional services resource for technical expertise and hands-on workload development. AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal use and self-service provisioning, and is an internal governance tool rather than a professional services program.

</details>

---


## ✅ Quick-Revision Master Answer Key (Q1–Q300)

| Q# | ID | Domain | Freq | Answer | Q# | ID | Domain | Freq | Answer |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **1** | `CLF-U0495` | D1 | 5x | **`D`** | **151** | `CLF-U1397` | D2 | 3x | **`AC`** |
| **2** | `CLF-U0390` | D1 | 4x | **`C`** | **152** | `CLF-U0199` | D2 | 3x | **`C`** |
| **3** | `CLF-U0400` | D1 | 4x | **`B`** | **153** | `CLF-U0233` | D2 | 3x | **`A`** |
| **4** | `CLF-U0401` | D1 | 4x | **`C, E`** | **154** | `CLF-U0819` | D2 | 3x | **`B`** |
| **5** | `CLF-U0579` | D1 | 4x | **`D`** | **155** | `CLF-U0836` | D2 | 3x | **`A, D`** |
| **6** | `CLF-U0597` | D1 | 4x | **`C`** | **156** | `CLF-U0837` | D2 | 3x | **`A`** |
| **7** | `CLF-U0588` | D1 | 4x | **`C`** | **157** | `CLF-U0856` | D2 | 3x | **`B, C`** |
| **8** | `CLF-U0035` | D1 | 4x | **`D, E`** | **158** | `CLF-U0861` | D2 | 3x | **`B`** |
| **9** | `CLF-U0392` | D1 | 4x | **`C`** | **159** | `CLF-U0864` | D2 | 3x | **`A`** |
| **10** | `CLF-U0448` | D1 | 4x | **`B, C`** | **160** | `CLF-U0888` | D2 | 3x | **`C`** |
| **11** | `CLF-U0011` | D1 | 4x | **`A`** | **161** | `CLF-U0964` | D2 | 3x | **`A`** |
| **12** | `CLF-U0019` | D1 | 4x | **`D`** | **162** | `CLF-U1469` | D2 | 3x | **`D`** |
| **13** | `CLF-U0043` | D1 | 4x | **`B`** | **163** | `CLF-U0242` | D3 | 5x | **`B`** |
| **14** | `CLF-U0044` | D1 | 4x | **`A`** | **164** | `CLF-U0001` | D3 | 4x | **`D`** |
| **15** | `CLF-U0045` | D1 | 4x | **`B, E`** | **165** | `CLF-U0002` | D3 | 4x | **`D`** |
| **16** | `CLF-U0055` | D1 | 4x | **`B, D`** | **166** | `CLF-U0020` | D3 | 4x | **`B`** |
| **17** | `CLF-U0059` | D1 | 4x | **`D, E`** | **167** | `CLF-U0042` | D3 | 4x | **`A`** |
| **18** | `CLF-U0060` | D1 | 4x | **`D`** | **168** | `CLF-U0051` | D3 | 4x | **`A`** |
| **19** | `CLF-U0083` | D1 | 4x | **`A, D`** | **169** | `CLF-U0062` | D3 | 4x | **`D`** |
| **20** | `CLF-U0398` | D1 | 4x | **`D`** | **170** | `CLF-U0066` | D3 | 4x | **`A`** |
| **21** | `CLF-U0402` | D1 | 4x | **`A, B`** | **171** | `CLF-U0068` | D3 | 4x | **`A, C`** |
| **22** | `CLF-U0403` | D1 | 4x | **`C`** | **172** | `CLF-U0091` | D3 | 4x | **`D`** |
| **23** | `CLF-U0405` | D1 | 4x | **`D`** | **173** | `CLF-U0385` | D3 | 4x | **`B`** |
| **24** | `CLF-U0406` | D1 | 4x | **`D`** | **174** | `CLF-U0397` | D3 | 4x | **`B`** |
| **25** | `CLF-U0410` | D1 | 4x | **`C`** | **175** | `CLF-U0408` | D3 | 4x | **`D`** |
| **26** | `CLF-U0414` | D1 | 4x | **`C, E`** | **176** | `CLF-U0418` | D3 | 4x | **`B`** |
| **27** | `CLF-U0417` | D1 | 4x | **`A`** | **177** | `CLF-U0799` | D3 | 4x | **`C, E`** |
| **28** | `CLF-U0420` | D1 | 4x | **`D`** | **178** | `CLF-U0810` | D3 | 4x | **`C`** |
| **29** | `CLF-U0796` | D1 | 4x | **`B, E`** | **179** | `CLF-U0007` | D3 | 4x | **`B, C`** |
| **30** | `CLF-U0817` | D1 | 4x | **`C, E`** | **180** | `CLF-U0012` | D3 | 4x | **`D`** |
| **31** | `CLF-U0825` | D1 | 4x | **`B, C`** | **181** | `CLF-U0023` | D3 | 4x | **`B, D`** |
| **32** | `CLF-U0828` | D1 | 4x | **`A`** | **182** | `CLF-U0033` | D3 | 4x | **`C`** |
| **33** | `CLF-U0415` | D1 | 4x | **`C`** | **183** | `CLF-U0041` | D3 | 4x | **`D`** |
| **34** | `CLF-U0004` | D1 | 3x | **`A, E`** | **184** | `CLF-U0048` | D3 | 4x | **`A, C`** |
| **35** | `CLF-U0179` | D1 | 3x | **`C`** | **185** | `CLF-U0049` | D3 | 4x | **`A`** |
| **36** | `CLF-U0383` | D1 | 3x | **`C`** | **186** | `CLF-U0052` | D3 | 4x | **`B`** |
| **37** | `CLF-U0384` | D1 | 3x | **`A, E`** | **187** | `CLF-U0054` | D3 | 4x | **`C, E`** |
| **38** | `CLF-U0386` | D1 | 3x | **`D`** | **188** | `CLF-U0077` | D3 | 4x | **`A, B`** |
| **39** | `CLF-U0421` | D1 | 3x | **`D, E`** | **189** | `CLF-U0084` | D3 | 4x | **`C`** |
| **40** | `CLF-U0424` | D1 | 3x | **`C`** | **190** | `CLF-U0106` | D3 | 4x | **`B`** |
| **41** | `CLF-U0425` | D1 | 3x | **`D`** | **191** | `CLF-U0111` | D3 | 4x | **`C`** |
| **42** | `CLF-U0444` | D1 | 3x | **`C, D`** | **192** | `CLF-U0570` | D3 | 4x | **`A`** |
| **43** | `CLF-U0466` | D1 | 3x | **`A`** | **193** | `CLF-U0006` | D3 | 4x | **`B`** |
| **44** | `CLF-U0471` | D1 | 3x | **`C`** | **194** | `CLF-U0016` | D3 | 4x | **`B`** |
| **45** | `CLF-U0480` | D1 | 3x | **`B`** | **195** | `CLF-U0027` | D3 | 4x | **`A`** |
| **46** | `CLF-U0481` | D1 | 3x | **`C`** | **196** | `CLF-U0028` | D3 | 4x | **`A`** |
| **47** | `CLF-U0485` | D1 | 3x | **`D`** | **197** | `CLF-U0034` | D3 | 4x | **`A`** |
| **48** | `CLF-U0599` | D1 | 3x | **`A, B`** | **198** | `CLF-U0039` | D3 | 4x | **`C`** |
| **49** | `CLF-U0633` | D1 | 3x | **`A, C`** | **199** | `CLF-U0046` | D3 | 4x | **`A, C`** |
| **50** | `CLF-U0802` | D1 | 3x | **`D`** | **200** | `CLF-U0047` | D3 | 4x | **`C`** |
| **51** | `CLF-U1445` | D1 | 3x | **`D`** | **201** | `CLF-U0065` | D3 | 4x | **`A`** |
| **52** | `CLF-U1465` | D1 | 3x | **`B`** | **202** | `CLF-U0087` | D3 | 4x | **`C, D`** |
| **53** | `CLF-U0207` | D1 | 3x | **`B`** | **203** | `CLF-U0093` | D3 | 4x | **`A, D`** |
| **54** | `CLF-U0439` | D1 | 3x | **`C`** | **204** | `CLF-U0804` | D3 | 4x | **`A`** |
| **55** | `CLF-U0445` | D1 | 3x | **`D`** | **205** | `CLF-U0030` | D3 | 4x | **`A`** |
| **56** | `CLF-U0449` | D1 | 3x | **`C, E`** | **206** | `CLF-U0098` | D3 | 4x | **`A, C`** |
| **57** | `CLF-U0459` | D1 | 3x | **`A`** | **207** | `CLF-U0353` | D3 | 4x | **`B`** |
| **58** | `CLF-U0470` | D1 | 3x | **`B`** | **208** | `CLF-U0038` | D3 | 4x | **`A`** |
| **59** | `CLF-U1305` | D1 | 3x | **`B`** | **209** | `CLF-U0086` | D3 | 4x | **`C`** |
| **60** | `CLF-U1309` | D1 | 3x | **`C`** | **210** | `CLF-U0095` | D3 | 4x | **`C`** |
| **61** | `CLF-U2529` | D1 | 3x | **`B`** | **211** | `CLF-U0244` | D3 | 4x | **`D`** |
| **62** | `CLF-U0249` | D1 | 3x | **`D`** | **212** | `CLF-U0029` | D3 | 3x | **`C`** |
| **63** | `CLF-U0477` | D1 | 3x | **`B`** | **213** | `CLF-U0161` | D3 | 3x | **`C`** |
| **64** | `CLF-U0478` | D1 | 3x | **`C, D`** | **214** | `CLF-U0166` | D3 | 3x | **`A`** |
| **65** | `ACTUAL-393-Q041` | D1 | 2x | **`D`** | **215** | `CLF-U0186` | D3 | 3x | **`B`** |
| **66** | `ACTUAL-393-Q053` | D1 | 2x | **`CD`** | **216** | `CLF-U0252` | D3 | 3x | **`A, C`** |
| **67** | `ACTUAL-393-Q392` | D1 | 2x | **`C`** | **217** | `CLF-U0262` | D3 | 3x | **`D`** |
| **68** | `CLF-U1324` | D1 | 2x | **`C`** | **218** | `CLF-U0443` | D3 | 3x | **`C`** |
| **69** | `CLF-U1335` | D1 | 2x | **`C`** | **219** | `CLF-U0571` | D3 | 3x | **`A`** |
| **70** | `CLF-U1437` | D1 | 2x | **`AB`** | **220** | `CLF-U0807` | D3 | 3x | **`B, E`** |
| **71** | `CLF-U1311` | D1 | 1x | **`A, C`** | **221** | `CLF-U1478` | D3 | 3x | **`C`** |
| **72** | `CLF-U1312` | D1 | 1x | **`A, C`** | **222** | `CLF-U0141` | D3 | 3x | **`C, D`** |
| **73** | `CLF-U0013` | D2 | 4x | **`D`** | **223** | `CLF-U0879` | D3 | 3x | **`A, C`** |
| **74** | `CLF-U0032` | D2 | 4x | **`D, E`** | **224** | `CLF-U0082` | D3 | 3x | **`A`** |
| **75** | `CLF-U0057` | D2 | 4x | **`A`** | **225** | `CLF-U0107` | D3 | 3x | **`A`** |
| **76** | `CLF-U0063` | D2 | 4x | **`D`** | **226** | `CLF-U0108` | D3 | 3x | **`D`** |
| **77** | `CLF-U0078` | D2 | 4x | **`B, C`** | **227** | `CLF-U0130` | D3 | 3x | **`D`** |
| **78** | `CLF-U0080` | D2 | 4x | **`C`** | **228** | `CLF-U0146` | D3 | 3x | **`B`** |
| **79** | `CLF-U0089` | D2 | 4x | **`A`** | **229** | `CLF-U0219` | D3 | 3x | **`B, E`** |
| **80** | `CLF-U0104` | D2 | 4x | **`B`** | **230** | `CLF-U0247` | D3 | 3x | **`B, E`** |
| **81** | `CLF-U0387` | D2 | 4x | **`D`** | **231** | `CLF-U0769` | D3 | 3x | **`C`** |
| **82** | `CLF-U0391` | D2 | 4x | **`B, C`** | **232** | `CLF-U1459` | D3 | 3x | **`D`** |
| **83** | `CLF-U0394` | D2 | 4x | **`B, C`** | **233** | `CLF-U0015` | D3 | 3x | **`B, C`** |
| **84** | `CLF-U0396` | D2 | 4x | **`B`** | **234** | `CLF-U0024` | D3 | 3x | **`C`** |
| **85** | `CLF-U0411` | D2 | 4x | **`D`** | **235** | `CLF-U0064` | D3 | 3x | **`B`** |
| **86** | `CLF-U0412` | D2 | 4x | **`A, D`** | **236** | `CLF-U0085` | D3 | 3x | **`A`** |
| **87** | `CLF-U0576` | D2 | 4x | **`B`** | **237** | `CLF-U0150` | D3 | 3x | **`D`** |
| **88** | `CLF-U0788` | D2 | 4x | **`A`** | **238** | `CLF-U0209` | D3 | 3x | **`C`** |
| **89** | `CLF-U0794` | D2 | 4x | **`D, E`** | **239** | `CLF-U0212` | D3 | 3x | **`C`** |
| **90** | `CLF-U0800` | D2 | 4x | **`D, E`** | **240** | `CLF-U0620` | D3 | 3x | **`C`** |
| **91** | `CLF-U0806` | D2 | 4x | **`D, E`** | **241** | `CLF-U0812` | D3 | 3x | **`C`** |
| **92** | `CLF-U0826` | D2 | 4x | **`A, E`** | **242** | `CLF-U0844` | D3 | 3x | **`C`** |
| **93** | `CLF-U1460` | D2 | 4x | **`C`** | **243** | `CLF-U2514` | D3 | 3x | **`AC`** |
| **94** | `CLF-U0017` | D2 | 4x | **`A`** | **244** | `CLF-U0014` | D3 | 3x | **`D`** |
| **95** | `CLF-U0040` | D2 | 4x | **`C`** | **245** | `CLF-U0069` | D3 | 3x | **`D`** |
| **96** | `CLF-U0072` | D2 | 4x | **`A, D`** | **246** | `CLF-U0137` | D3 | 3x | **`B`** |
| **97** | `CLF-U0115` | D2 | 4x | **`B, C`** | **247** | `CLF-U0144` | D3 | 3x | **`A`** |
| **98** | `CLF-U0575` | D2 | 4x | **`C`** | **248** | `CLF-U0148` | D3 | 3x | **`C, D`** |
| **99** | `CLF-U0591` | D2 | 4x | **`B`** | **249** | `CLF-U0220` | D3 | 3x | **`A`** |
| **100** | `CLF-U0789` | D2 | 4x | **`C`** | **250** | `CLF-U0809` | D3 | 3x | **`A, E`** |
| **101** | `CLF-U0797` | D2 | 4x | **`C`** | **251** | `CLF-U0849` | D3 | 3x | **`D`** |
| **102** | `CLF-U0798` | D2 | 4x | **`D`** | **252** | `CLF-U0021` | D3 | 3x | **`A`** |
| **103** | `CLF-U0803` | D2 | 4x | **`C`** | **253** | `CLF-U0092` | D3 | 3x | **`C`** |
| **104** | `CLF-U0808` | D2 | 4x | **`B`** | **254** | `CLF-U0128` | D3 | 3x | **`C, D`** |
| **105** | `CLF-U0821` | D2 | 4x | **`C, D`** | **255** | `CLF-U0181` | D3 | 3x | **`A`** |
| **106** | `CLF-U0824` | D2 | 4x | **`C`** | **256** | `CLF-U0210` | D3 | 3x | **`A, B`** |
| **107** | `CLF-U0831` | D2 | 4x | **`C`** | **257** | `CLF-U0215` | D3 | 3x | **`D, E`** |
| **108** | `CLF-U0053` | D2 | 4x | **`B`** | **258** | `CLF-U0223` | D3 | 3x | **`D`** |
| **109** | `CLF-U0058` | D2 | 4x | **`C`** | **259** | `CLF-U0371` | D3 | 3x | **`D`** |
| **110** | `CLF-U0816` | D2 | 4x | **`A, E`** | **260** | `CLF-U0612` | D3 | 3x | **`A`** |
| **111** | `CLF-U0867` | D2 | 4x | **`B`** | **261** | `CLF-U0624` | D3 | 3x | **`D`** |
| **112** | `CLF-U0884` | D2 | 4x | **`B`** | **262** | `CLF-U0675` | D3 | 3x | **`C`** |
| **113** | `CLF-U0890` | D2 | 4x | **`D`** | **263** | `CLF-U0850` | D3 | 3x | **`A`** |
| **114** | `CLF-U0071` | D2 | 4x | **`B`** | **264** | `CLF-U0915` | D3 | 3x | **`D`** |
| **115** | `CLF-U0822` | D2 | 4x | **`B`** | **265** | `CLF-U0050` | D4 | 4x | **`D`** |
| **116** | `CLF-U0022` | D2 | 4x | **`C`** | **266** | `CLF-U0558` | D4 | 4x | **`B`** |
| **117** | `CLF-U0067` | D2 | 4x | **`D`** | **267** | `CLF-U0561` | D4 | 4x | **`C`** |
| **118** | `CLF-U0203` | D2 | 4x | **`A`** | **268** | `CLF-U0026` | D4 | 4x | **`C`** |
| **119** | `CLF-U0585` | D2 | 4x | **`C`** | **269** | `CLF-U0076` | D4 | 4x | **`B`** |
| **120** | `CLF-U0590` | D2 | 4x | **`A, C`** | **270** | `CLF-U0126` | D4 | 4x | **`A`** |
| **121** | `CLF-U0801` | D2 | 4x | **`A, E`** | **271** | `CLF-U0564` | D4 | 4x | **`C`** |
| **122** | `CLF-U0811` | D2 | 4x | **`C`** | **272** | `CLF-U0583` | D4 | 4x | **`A`** |
| **123** | `CLF-U0814` | D2 | 4x | **`D`** | **273** | `CLF-U0586` | D4 | 4x | **`C`** |
| **124** | `CLF-U0962` | D2 | 4x | **`D`** | **274** | `CLF-U0592` | D4 | 4x | **`A`** |
| **125** | `CLF-U0151` | D2 | 3x | **`C, D`** | **275** | `CLF-U0559` | D4 | 4x | **`B`** |
| **126** | `CLF-U0834` | D2 | 3x | **`A`** | **276** | `CLF-U0563` | D4 | 4x | **`D`** |
| **127** | `CLF-U0835` | D2 | 3x | **`B`** | **277** | `CLF-U0566` | D4 | 4x | **`A, E`** |
| **128** | `CLF-U0883` | D2 | 3x | **`B, D`** | **278** | `CLF-U0573` | D4 | 4x | **`C`** |
| **129** | `CLF-U1394` | D2 | 3x | **`B`** | **279** | `CLF-U0584` | D4 | 4x | **`C`** |
| **130** | `CLF-U2486` | D2 | 3x | **`CD`** | **280** | `CLF-U0596` | D4 | 4x | **`C`** |
| **131** | `CLF-U0158` | D2 | 3x | **`B`** | **281** | `CLF-U0604` | D4 | 4x | **`A, C`** |
| **132** | `CLF-U0165` | D2 | 3x | **`A`** | **282** | `CLF-U0101` | D4 | 3x | **`B`** |
| **133** | `CLF-U0188` | D2 | 3x | **`D`** | **283** | `CLF-U0574` | D4 | 3x | **`C`** |
| **134** | `CLF-U0194` | D2 | 3x | **`D`** | **284** | `CLF-U0598` | D4 | 3x | **`D`** |
| **135** | `CLF-U0204` | D2 | 3x | **`B`** | **285** | `CLF-U0623` | D4 | 3x | **`A, C`** |
| **136** | `CLF-U0572` | D2 | 3x | **`A, B`** | **286** | `CLF-U0638` | D4 | 3x | **`B, E`** |
| **137** | `CLF-U0611` | D2 | 3x | **`A`** | **287** | `CLF-U0652` | D4 | 3x | **`A, D`** |
| **138** | `CLF-U0630` | D2 | 3x | **`A`** | **288** | `CLF-U1485` | D4 | 3x | **`A`** |
| **139** | `CLF-U0787` | D2 | 3x | **`B`** | **289** | `CLF-U0170` | D4 | 3x | **`A, D`** |
| **140** | `CLF-U0842` | D2 | 3x | **`C`** | **290** | `CLF-U0609` | D4 | 3x | **`B`** |
| **141** | `CLF-U0852` | D2 | 3x | **`B`** | **291** | `CLF-U0615` | D4 | 3x | **`B`** |
| **142** | `CLF-U0854` | D2 | 3x | **`B`** | **292** | `CLF-U0673` | D4 | 3x | **`B, C`** |
| **143** | `CLF-U0876` | D2 | 3x | **`A`** | **293** | `CLF-U0616` | D4 | 3x | **`B`** |
| **144** | `CLF-U0953` | D2 | 3x | **`C`** | **294** | `CLF-U0653` | D4 | 3x | **`B`** |
| **145** | `CLF-U0667` | D2 | 3x | **`B, D`** | **295** | `CLF-U0654` | D4 | 3x | **`C`** |
| **146** | `CLF-U0830` | D2 | 3x | **`B`** | **296** | `CLF-U0968` | D4 | 3x | **`C`** |
| **147** | `CLF-U0839` | D2 | 3x | **`A, E`** | **297** | `CLF-U0577` | D4 | 3x | **`A`** |
| **148** | `CLF-U0848` | D2 | 3x | **`B`** | **298** | `CLF-U0618` | D4 | 3x | **`C`** |
| **149** | `CLF-U0862` | D2 | 3x | **`A`** | **299** | `CLF-U0626` | D4 | 3x | **`D, E`** |
| **150** | `CLF-U0966` | D2 | 3x | **`B`** | **300** | `CLF-U0650` | D4 | 3x | **`C`** |
