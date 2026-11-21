# CLF-C02 Authentic Exam Practice Pool & Community Consensus

> **Total Questions:** 718  
> **Source:** Verified Community Consensus & Discussion Pool  
> **Pedagogical Designation:** Professional Exam Practice Suite (Recall Pool)  

---

## Question 1: CLF-C02-ET-Q001
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company plans to use an Amazon Snowball Edge device to transfer files to the AWS Cloud.
Which activities related to a Snowball Edge device are available to the company at no cost?

**Choices:**
- A) Use of the Snowball Edge appliance for a 10-day period
- B) The transfer of data out of Amazon S3 and to the Snowball Edge appliance
- C) The transfer of data from the Snowball Edge appliance into Amazon S3
- D) Daily use of the Snowball Edge appliance after 10 days

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `98%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (98%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
It's Just had this question on my exam, and it’s all about understanding the cost-related activities with an Amazon Snowball Edge device. The correct answer revolves around the 10-day free use period (A) and other key processes that don’t incur charges, like transferring data from the appliance into S3 (C). I remember this being clearly explained in the examforusre.com guide, which detailed how AWS billing works for Snowball devices. The pro version broke down these activities step by step, making it much easier to grasp. Pro tip: Watch out for hints like “no-cost activities” to quickly eliminate irrelevant options!
---
C is valid discussion
---
Selected Answer: C
Main ways to lose money on AWS are compute, storage and outbound data transfer. Inbound data transfer is by default not charged.

</details>

---

## Question 2: CLF-C02-ET-Q002
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are benefits of using AWS Trusted Advisor? (Choose two.)

**Choices:**
- A) Providing high-performance container orchestration
- B) Creating and rotating encryption keys
- C) Detecting underutilized resources to save costs
- D) Improving security by proactively monitoring the AWS environment
- E) Implementing enforced tagging across AWS resources

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (100%). Contributor Answer: CD.

Community Rationale & Discussion:
C & D are correct.

Benefits of Trusted Advisor:
• Cost optimization - Trusted Advisor can help you save cost with actionable recommendations by analyzing usage, configuration and spend.
• Performance - Trusted Advisor can help improve the performance of your services with actionable recommendations by analyzing usage and configuration.
• Security - Trusted Advisor can help improve the security of your AWS environment by suggesting foundational security best practices curated by security experts.
• Fault tolerance - Trusted Advisor can help improve the reliability of your services. 
• Service quotas - Service quotas are the maximum number of resources that you can create in an AWS account.

Reference: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
---
Selected Answer: CD
AWS Trusted Advisor is a service that provides real-time guidance to help optimize AWS infrastructure in terms of cost, security, performance, fault tolerance, and service limits.
---
Selected Answer: CD
Option C and D are correct

</details>

---

## Question 3: CLF-C02-ET-Q003
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to automate infrastructure deployment by using infrastructure as code (IaC). The company wants to scale production stacks so the stacks can be deployed in multiple AWS Regions.
Which AWS service will meet these requirements?

**Choices:**
- A) Amazon CloudWatch
- B) AWS Config
- C) AWS Trusted Advisor
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
"AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles, by treating infrastructure as code. A CloudFormation template describes your desired resources and their dependencies so you can launch and configure them together as a stack. You can use a template to create, update, and delete an entire stack as a single unit, as often as you need to, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions."

Reference: https://aws.amazon.com/cloudformation/features/
---
Selected Answer: D
D. AWS CloudFormation: A service that allows you to define and provision AWS infrastructure as code. You can use CloudFormation templates to describe the resources needed, and CloudFormation handles the provisioning and deployment. It supports the automated deployment and scaling of infrastructure stacks across multiple AWS Regions, making it suitable for IaC and scaling production stacks.
---
Selected Answer: D
D Cloud Formation

</details>

---

## Question 4: CLF-C02-ET-Q004
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is an AWS Cloud Adoption Framework (AWS CAF) platform perspective capability?

**Choices:**
- A) Data architecture
- B) Data protection
- C) Data governance
- D) Data science

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `79%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (79%). Contributor Answer: A.

Community Rationale & Discussion:
Cloud Adoption Framework:
1) Business capabilities
1.1) Business
1.2) People
1.3) Governance (CORRECT ANSWER)
2) Technical capabilities
2.1) Platform
2.2) Security
2.3) Operations
---
Selected Answer: A
The correct answer is A, the clue is "Platform perspective capabilities" and only "Data Architecture" include in the list.

ref: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/platform-perspective.html
---
Selected Answer: A
100% the answer is A

</details>

---

## Question 5: CLF-C02-ET-Q005
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is running a workload in the AWS Cloud.
Which AWS best practice ensures the MOST cost-effective architecture for the workload?

**Choices:**
- A) Loose coupling
- B) Rightsizing
- C) Caching
- D) Redundancy

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Right sizing is the process of matching instance types and sizes to your workload performance and capacity requirements at the lowest possible cost.

Ref link: https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/#:~:text=Right%20sizing%20is%20the%20process,at%20the%20lowest%20possible%20cost.
---
Selected Answer: B
A. Loose coupling: This is a design principle that promotes independence between components in a system. It enhances flexibility and scalability by reducing dependencies. While beneficial for system architecture, it doesn't directly target cost optimization.

B. Rightsizing: Involves selecting the appropriate size and type of AWS resources to match the workload's actual needs. The focus is on optimizing costs by avoiding overprovisioning and ensuring resources are efficiently utilized. Regular reviews and adjustments contribute to ongoing cost-effectiveness.

C. Caching: Involves storing frequently accessed data to reduce the need to fetch it repeatedly from the original source. It improves performance and can indirectly contribute to cost savings by reducing the load on backend resources. The primary focus, however, is on enhancing application performance rather than direct cost optimization.

D. Redundancy: Involves having duplicate components to ensure high availability and fault tolerance. While crucial for reliability and minimizing downtime, redundancy's primary goal is not direct cost optimization. It can prevent costs associated with disruptions and downtime.
---
Selected Answer: B
B. Rightsizing: Right sizing is the process of matching instance types and sizes to your workload performance and capacity requirements at the lowest possible cost.

</details>

---

## Question 6: CLF-C02-ET-Q006
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is using a central data platform to manage multiple types of data for its customers. The company wants to use AWS services to discover, transform, and visualize the data.
Which combination of AWS services should the company use to meet these requirements? (Choose two.)

**Choices:**
- A) AWS Glue
- B) Amazon Elastic File System (Amazon EFS)
- C) Amazon Redshift
- D) Amazon QuickSight
- E) Amazon Quantum Ledger Database (Amazon QLDB)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
The answer is AD.

AWS Glue is a serverless data integration service that makes it easier to discover, prepare, move, and integrate data from multiple sources for analytics, machine learning (ML), and application development.
https://aws.amazon.com/glue/

Amazon QuickSight powers data-driven organizations with unified business intelligence (BI) at hyperscale. With QuickSight, all users can meet varying analytic needs from the same source of truth through modern interactive dashboards, paginated reports, embedded analytics, and natural language queries.
https://aws.amazon.com/quicksight/
---
Selected Answer: AD
A. AWS Glue: AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to discover, prepare, and load data for analysis. It automates the time-consuming tasks of data discovery, transformation, and job scheduling, allowing users to focus on analyzing the data.

B. Amazon Elastic File System (Amazon EFS): Fully managed file system for shared access to file-based data. Not primarily used for data discovery, transformation, or visualization.

C. Amazon Redshift: Fully managed data warehouse service for running complex queries on large datasets. Not used for data discovery, transformation, or visualization.

D. Amazon QuickSight: Amazon QuickSight is a fully managed business intelligence (BI) service that enables users to create and visualize interactive dashboards and reports. It connects to various data sources, making it suitable for visualizing data prepared by services like AWS Glue.

E. Amazon Quantum Ledger Database (Amazon QLDB): Fully managed ledger database service for ensuring data integrity. Not designed for data discovery, transformation, or visualization.
---
Selected Answer: AD
o manage and analyze data effectively, the company needs services that support data discovery, transformation, and visualization.

</details>

---

## Question 7: CLF-C02-ET-Q007
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS services can a company use to achieve a loosely coupled architecture? (Choose two.)

**Choices:**
- A) Amazon WorkSpaces
- B) Amazon Simple Queue Service (Amazon SQS)
- C) Amazon Connect
- D) AWS Trusted Advisor
- E) AWS Step Functions

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
A: Amazon WorkSpaces is a managed desktop service
B: Amazon Simple Queue Service (Amazon SQS) allows components of a system to communicate asynchronously
C: Amazon Connect is a cloud-based contact center service
D: AWS Trusted Advisor provides recommendations for optimizing AWS environments
E: AWS Step Functions AWS Step Functions is a service that helps you coordinate multiple AWS services
---
Selected Answer: BE
B. Amazon Simple Queue Service (Amazon SQS)
E. AWS Step Functions
---
Selected Answer: BE
Amazon Connect is not correct because it is a cloud-based contact center service that helps businesses provide superior customer service at a lower cost.
Amazon Workspaces is a desktop virtualization service.

</details>

---

## Question 8: CLF-C02-ET-Q008
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud service can send alerts to customers if custom spending thresholds are exceeded?

**Choices:**
- A) AWS Budgets
- B) AWS Cost Explorer
- C) AWS Cost Allocation Tags
- D) AWS Organizations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A: AWS Budgets allows users to set custom budget alerts that notify them when their spending exceeds predefined thresholds.
B: AWS Cost Explorer is a tool for visualizing and understanding AWS spend over time
C: AWS Cost Allocation Tags help organize and track costs by tagging resources
D: AWS Organizations allows management of multiple AWS accounts
---
Selected Answer: A
A. AWS Budgets is the AWS Cloud service that allows users to set custom spending thresholds and receive alerts when those thresholds are exceeded. It helps users to keep track of their AWS spending by providing notifications based on their budget limits.
---
Selected Answer: A
A.AWS Budgets

</details>

---

## Question 9: CLF-C02-ET-Q009
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to migrate to the AWS Cloud. The company wants to use the AWS Cloud Adoption Framework (AWS CAF) to define and track business outcomes as part of its cloud transformation journey.

Which AWS CAF governance perspective capability will meet these requirements?

**Choices:**
- A) Benefits management
- B) Risk management
- C) Application portfolio management
- D) Cloud financial management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `76%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (76%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
"Benefits management – Ensure that the business benefits associated with your cloud investments are realized and sustained. The success of your transformation is determined by the resulting business benefits. Clear identification of the desired benefits upfront will allow you to prioritize your cloud investments and track transformation progress over time. Identify metrics, quantify desired benefits, and communicate to the relevant stakeholders. Align the timing and life-span of benefits with your strategic goals. Incorporate benefits delivery into a benefits realization roadmap. Regularly measure realized benefits, evaluate progress against the benefits realization roadmap, and adjust the expected benefits as required."

Reference: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/governance-perspective.html
---
This question is BS
---
Selected Answer: A
A. Benefits management – Ensure that the business benefits associated with your cloud investments are realized and sustained. The success of your transformation is determined by the resulting business benefits. Clear identification of the desired benefits upfront will allow you to prioritize your cloud investments and track transformation progress over time. Identify metrics, quantify desired benefits, and communicate to the relevant stakeholders. Align the timing and life-span of benefits with your strategic goals. Incorporate benefits delivery into a benefits realization roadmap. Regularly measure realized benefits, evaluate progress against the benefits realization roadmap, and adjust the expected benefits as required.

</details>

---

## Question 10: CLF-C02-ET-Q010
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to quickly and securely move files over long distances between its client and an Amazon S3 bucket.

Which S3 feature will meet this requirement?

**Choices:**
- A) S3 Versioning
- B) S3 Transfer Acceleration
- C) S3ACLs
- D) S3 Intelligent-Tiering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. S3 Transfer Acceleration

S3 Transfer Acceleration is a feature that utilizes Amazon CloudFront's globally distributed edge locations to accelerate the upload of objects to an S3 bucket. It optimizes data transfer by using Amazon's backbone network, reducing latency and improving speeds when transferring files over long distances.
---
Key word: quickly*
---
Selected Answer: B
B. S3 Transfer Acceleration

</details>

---

## Question 11: CLF-C02-ET-Q011
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is hosting a web application on Amazon EC2 instances. The company wants to implement custom conditions to filter and control inbound web traffic.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon GuardDuty
- B) AWS WAF
- C) Amazon Macie
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS WAF
---
"AWS WAF helps you protect against common web exploits and bots that can affect availability, compromise security, or consume excessive resources."
---
Selected Answer: B
I think B is correct

</details>

---

## Question 12: CLF-C02-ET-Q012
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to maintain bandwidth throughput and provide a more consistent network experience than public internet-based connections.

Which AWS service should the company choose?

**Choices:**
- A) AWS VPN
- B) AWS Direct Connect
- C) Amazon Connect
- D) Amazon CloudFront

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (80%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Direct Connect - establishes a dedicated, private connection between your on-premises data center or colocation facility and AWS.
---
Selected Answer: B
AWS Direct Connect establishes a dedicated network connection from your premises to AWS, which can reduce network costs, increase bandwidth throughput, and provide a more consistent network experience compared to internet-based connections1.
Amazon CloudFront is a content delivery network (CDN) service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. While it improves the delivery speed and performance of your content, it does not provide a dedicated network connection or address the need for consistent bandwidth throughput and network experience
---
Selected Answer: B
AWS Direct Connect (B): This service allows you to establish a dedicated network connection from your on-premises data center to AWS. Direct Connect provides a private, high-bandwidth connection that bypasses the public internet, resulting in more consistent network performance and lower latency. This is ideal for applications requiring stable and high-throughput network connections.

</details>

---

## Question 13: CLF-C02-ET-Q013
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has temporary workload that is also variable. The company needs to use Amazon EC2 instances for the workload. The EC2 instances need to handle short bursts of work that cannot stop before finishing.

Which purchase option will meet these requirements?

**Choices:**
- A) Spot Instances
- B) On-Demand Instances
- C) Savings Plan
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. On-Demand Instances
---
Selected Answer: B
Keyword: short bursts of work that cannot stop before finishing.

Answer is B. On-demand Instances
---
B is correct. 

Need help with discussion on 549 551 ~ 562. Thanks.

</details>

---

## Question 14: CLF-C02-ET-Q014
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company's employees are working from home. The company wants its employees to use their personal devices to connect to a managed workstation in the AWS Cloud.

Which AWS service should the company use to provide the remote environment?

**Choices:**
- A) Amazon Workspaces
- B) AWS Cloud9
- C) AWS Outposts
- D) Amazon Lightsail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon Workspaces
---
Amazon WorkSpaces is a fully managed, secure Desktop-as-a-Service (DaaS) solution that provides virtual cloud desktops. With Amazon WorkSpaces, employees can access a managed workstation environment in the AWS Cloud from their personal devices, using either a web browser or a client application. This is ideal for remote work, as it ensures secure access to work resources

</details>

---

## Question 15: CLF-C02-ET-Q015
**Domain 3:** Cloud Technology and Services  

**Question:**  
To reduce costs, a company is planning to migrate a NoSQL database to AWS.
Which AWS service is fully managed and can automatically scale throughput capacity to meet database workload demands?

**Choices:**
- A) Amazon Redshift
- B) Amazon Aurora
- C) Amazon DynamoDB
- D) Amazon RDS

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `96%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (96%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon DynamoDB: DynamoDB is a fully managed NoSQL database service provided by AWS. It is designed to provide low-latency, high-throughput performance for applications. DynamoDB can automatically scale throughput capacity based on the application's demand, making it a suitable choice for workloads with varying traffic patterns.

 Amazon Redshift: Amazon Redshift is a fully managed data warehouse service, but it is not a NoSQL database, and its scaling behavior is optimized for analytical queries rather than transactional workloads.

 Amazon Aurora: Amazon Aurora is a fully managed relational database service. While it offers automatic scaling, it may not be the optimal choice for a NoSQL database.

 Amazon RDS: Amazon RDS (Relational Database Service) is a managed relational database service that supports various database engines. It may not be the best fit for a NoSQL database with automatic scaling requirements.
---
C is correct. DynamoDB is a non-relational database which means it is a NONSQL database. 

Aurora and RDS are relational, as for Redshift that is for exabytes of data and complex queries.
---
Selected Answer: C
Amazon DynamoDB is a fully managed NoSQL database service that automatically scales to meet the throughput capacity required for your database workloads. DynamoDB provides built-in support for scaling read and write capacity without manual intervention. It also offers on-demand capacity mode that automatically adjusts to your workload demands, making it a cost-effective solution for databases with variable traffic patterns.

</details>

---

## Question 16: CLF-C02-ET-Q016
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to use SQL syntax to perform a direct query of objects in an Amazon S3 bucket.

Which AWS service can the company use to meet this requirement?

**Choices:**
- A) AWS Glue
- B) Amazon Athena
- C) AWS Lambda
- D) Amazon Kinesis

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Athena - serverless interactive query service that allows you to use standard SQL to query data stored in Amazon S3.
---
>B. Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.
---
B is correct

Please help with discussion on 551~562. Thanks.

</details>

---

## Question 17: CLF-C02-ET-Q017
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company uses Amazon RDS for a product database. The company wants to ensure the database is highly available.

Which feature of Amazon RDS will meet this requirement?

**Choices:**
- A) Read replicas
- B) Blue/green deployment
- C) Multi-AZ deployment
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Multi-AZ deployment - key word "highly available"

</details>

---

## Question 18: CLF-C02-ET-Q018
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides serverless compute for use with containers?

**Choices:**
- A) Amazon Simple Queue Service (Amazon SQS)
- B) AWS Fargate
- C) AWS Elastic Beanstalk
- D) Amazon SageMaker

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Fargate is a serverless compute engine for containers that allows you to run containers without managing servers
---
Selected Answer: B
B. AWS Fargate

</details>

---

## Question 19: CLF-C02-ET-Q019
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is using multiple AWS accounts for different business teams. The finance team wants to receive one bill for all of the company's accounts.

Which AWS service or tool should the finance team use to meet this requirement?

**Choices:**
- A) AWS Organizations
- B) AWS Trusted Advisor
- C) Cost Explorer
- D) AWS Budgets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Organizations - service that allows you to consolidate billing across multiple AWS accounts.

</details>

---

## Question 20: CLF-C02-ET-Q020
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs a firewall that will control network connections to and from a single Amazon EC2 instance. This firewall will not control network connections to and from other instances that are in the same subnet.

Which AWS service or feature can the company use to meet these requirements?

**Choices:**
- A) Network ACL
- B) AWS WAF
- C) Route table
- D) Security group

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Security group - EC2 instances = security group

</details>

---

## Question 21: CLF-C02-ET-Q021
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to use the Amazon EC2 instances as web servers. Customers from around the world will use the web servers. Most customers will use the web servers only during certain hours of the day.

How should the company deploy the EC2 instances to achieve the LOWEST operational cost?

**Choices:**
- A) In multiple Availability Zones
- B) In an Auto Scaling group
- C) In a placement group
- D) In private subnets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. In an Auto Scaling group - automatically adjusts number of EC2 instances based on demand. Most cost effective option.

</details>

---

## Question 22: CLF-C02-ET-Q022
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which benefit is always free of charge with AWS, regardless of a user’s AWS Support plan?

**Choices:**
- A) AWS Developer Support
- B) AWS Developer Forums
- C) Programmatic case management
- D) AWS technical account manager (TAM)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Developer Forums
---
B. AWS Developer Forums

</details>

---

## Question 23: CLF-C02-ET-Q023
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company uses Amazon EC2 instances to run its application. The application needs to be available and running continuously for three or more years.

What type of EC2 instance should the company purchase for a discount on the EC2 pricing?

**Choices:**
- A) Reserved Instances
- B) Spot Instances
- C) On-Demand Instances
- D) EC2 Fleet

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Reserved Instances

</details>

---

## Question 24: CLF-C02-ET-Q024
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to perform an audit of recent AWS account activity. The audit will investigate who initiated an event and what actions were performed.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS Config
- B) Amazon Rekognition
- C) AWS CloudTrail
- D) Amazon Simple Notification Service (Amazon SNS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS CloudTrail = audit

</details>

---

## Question 25: CLF-C02-ET-Q025
**Domain 1:** Cloud Concepts  

**Question:**  
Which design principles are included in the reliability pillar of the AWS Well-Architected Framework? (Choose two.)

**Choices:**
- A) Automatically recover from failure.
- B) Grant everyone access to increase AWS service quotas.
- C) Stop guessing capacity.
- D) Design applications to run in a single Availability Zone.
- E) Plan to increase AWS service quotas first in a secondary AWS Region.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
A & C are the best choices

</details>

---

## Question 26: CLF-C02-ET-Q026
**Domain 2:** Security and Compliance  

**Question:**  
A company is using Amazon DynamoDB.
Which task is the company’s responsibility, according to the AWS shared responsibility model?

**Choices:**
- A) Patch the operating system.
- B) Provision hosts.
- C) Manage database access permissions.
- D) Secure the operating system.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
ccording to the AWS shared responsibility model, AWS manages the security of the cloud (e.g., physical infrastructure, hardware, and network), while the customer is responsible for security in the cloud (e.g., managing access, configuring services, and securing data).
---
Selected Answer: C
But the questions ask for the company's responsibility
---
Selected Answer: C
Manage database access permissions: This is the customer's responsibility. Customers are responsible for defining and managing access permissions to their DynamoDB tables, specifying who can perform various operations on the tables.

</details>

---

## Question 27: CLF-C02-ET-Q027
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to use AWS technology to deploy a static website.

Which solution meets this requirement with the LEAST amount of operational overhead?

**Choices:**
- A) Deploy the website on Amazon EC2.
- B) Host the website on AWS Elastic Beanstalk.
- C) Deploy the website with Amazon Lightsail.
- D) Host the website on Amazon S3.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
This is a tricky question because Amazon has made improvements to Lightsail over the past few years that make it good for static content as well. However, S3 still has the lowest overhead compared to Lightsail.
---
Selected Answer: D
D. Host the website on Amazon S3.
---
Amazon S3 (Simple Storage Service) is ideal for hosting static websites with minimal operational overhead. It allows you to store and serve static content (like HTML, CSS, and JavaScript files) directly from S3 buckets without needing to manage any servers or complex infrastructure. Additionally, Amazon S3 is highly scalable, cost-effective, and requires very little maintenance.

</details>

---

## Question 28: CLF-C02-ET-Q028
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which recommendation can AWS Cost Explorer provide to help reduce cost?

**Choices:**
- A) Use a specific database engine.
- B) Change the programming language for an application.
- C) Deploy a specific operating system.
- D) Terminate an idle instance.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Terminate an idle instance.
---
D. Stop guessing your capacity needs: If you make a poor capacity decision when deploying a workload, you might end up sitting on expensive idle resources or dealing with the performance implications of limited capacity. With cloud computing, these problems can go away. You can use as much or as little capacity as you need, and scale in and out automatically.

</details>

---

## Question 29: CLF-C02-ET-Q029
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to deploy an application in multiple Availability Zones in a single AWS Region.

Which benefit will this deployment provide to the company?

**Choices:**
- A) Improved connection performance for global customers
- B) Resilient architecture and a highly available solution
- C) Reduced overall data storage costs
- D) Ability to shut down an Availability Zone during periods of low demand

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Resilient architecture and a highly available solution

</details>

---

## Question 30: CLF-C02-ET-Q030
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can companies use to subscribe to RSS feeds for updates about all AWS service issues?

**Choices:**
- A) Amazon Simple Notification Service (Amazon SNS)
- B) AWS Health Dashboard
- C) AWS Config
- D) AWS CodeCommit

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Health Dashboard
---
Selected Answer: B
AWS Health Dashboard: The AWS Health Dashboard provides a comprehensive view of the health of AWS services and your AWS resources. It includes notifications about service disruptions, upcoming maintenance, and other critical information about AWS services. While the dashboard itself does not directly provide RSS feeds, it is the primary tool for monitoring AWS service health and can be used to track issues and updates. For RSS feed subscriptions, you would need to use the specific AWS Health Dashboard RSS feed URLs provided by AWS or subscribe through the AWS Support Center for notifications.
---
Correct answer is A

</details>

---

## Question 31: CLF-C02-ET-Q031
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which Amazon EC2 Reserved Instances term commitment will give users the MOST cost savings?

**Choices:**
- A) 1 year
- B) 2 years
- C) 3 years
- D) 5 years

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. 3 years
---
Amazon EC2 Reserved Instances offer cost savings in exchange for a commitment to use EC2 capacity over a set term, with the 3-year term providing the highest savings compared to the 1-year option. AWS does not offer a 5-year term for Reserved Instances, so 3 years is the longest available and the most cost-effective option.

Summary: A 3-year Reserved Instance term provides the greatest cost savings, making option C the correct answer.
---
c is correct. 

Please help with discussion on 565. Thanks.

</details>

---

## Question 32: CLF-C02-ET-Q032
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is running big data analytics and massive parallel computations on its AWS test and development servers. The company can tolerate occasional downtime.

What is the MOST cost-effective Amazon EC2 purchasing option for the company to use?

**Choices:**
- A) On-Demand Instances
- B) Spot Instances
- C) Reserved Instances
- D) Savings Plans

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Spot Instances - most cost effective solution when you can tolerate occasional downtime.

</details>

---

## Question 33: CLF-C02-ET-Q033
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company runs Amazon EC2 instances in a research lab. The instances run for 3 hours each week and cannot be interrupted.

What is the MOST cost-effective instance purchasing option to meet these requirements?

**Choices:**
- A) Compute Savings Plan
- B) On-Demand Instances
- C) Convertible Reserved Instances
- D) Spot Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `70%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (70%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The most cost-effective instance purchasing option for this scenario is B. On-Demand Instances. Here’s why:
On-Demand Instances are ideal for workloads that run for short durations and cannot be interrupted. They provide the flexibility to pay for compute capacity by the hour or second, with no long-term commitments.
Compute Savings Plans and Convertible Reserved Instances are more cost-effective for longer-term, consistent usage but require a commitment over a 1 or 3-year term.
Spot Instances offer the lowest prices but can be interrupted by AWS with little notice, making them unsuitable for workloads that cannot be interrupted.
---
Selected Answer: C
C. Convertible Reserved Instances
---
There is a 60% to 40% split between the answers. In such scenarios, does the Admin provide the correct response?

</details>

---

## Question 34: CLF-C02-ET-Q034
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A new AWS user needs to interact with AWS Support by using API calls.

Which AWS Support plan will meet this requirement MOST cost-effectively?

**Choices:**
- A) AWS Basic Support
- B) AWS Developer Support
- C) AWS Business Support
- D) AWS Enterprise Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `52%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (52%). Contributor Answer: C.

Community Rationale & Discussion:
Answer C is correct.
According to AWD Developer support doesn't support API calls, Business, Ent on Ramp and EMT does, 
https://aws.amazon.com/premiumsupport/plans/
---
Selected Answer: C
https://www.scaler.com/topics/aws/aws-support-plans/
---
Selected Answer: C
Developer Support DOES NOT allow you to interact with AWS Support using API calls. The Developer plan provides access to AWS Support through email only.

</details>

---

## Question 35: CLF-C02-ET-Q035
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company migrated to the AWS Cloud. Now the company pays for services on an as-needed basis.

Which advantage of cloud computing is the company benefiting from?

**Choices:**
- A) Stop spending money running and maintaining data centers
- B) Increase speed and agility
- C) Go global in minutes
- D) Trade fixed expense for variable expense

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Trade fixed expense for variable expense
---
Selected Answer: D
Answer is D
---
Selected Answer: D
The four answer are advantages of cloud computing but only one is pay for services:

Trade fixed expense for variable expense – Instead of having to invest heavily in data centers and servers before you know how you’re going to use them, you can pay only when you consume computing resources, and pay only for how much you consume.

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html

</details>

---

## Question 36: CLF-C02-ET-Q036
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company will run a predictable compute workload on Amazon EC2 instances for the next 3 years. The workload is critical for the company. The company wants to optimize costs to run the workload.

Which solution will meet these requirements?

**Choices:**
- A) Spot Instances
- B) Dedicated Hosts
- C) Savings Plans
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Savings Plans - most cost-effective option for predictable, long-term use
---
c is correct

please help discussion on 570 ~ 574
---
Why not D?

</details>

---

## Question 37: CLF-C02-ET-Q037
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a test AWS environment. A company is planning on testing an application within AWS. The application testing can be interrupted and does not need to run continuously.
Which Amazon EC2 purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) On-Demand Instances
- B) Dedicated Instances
- C) Spot Instances
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
On-Demand Instances: On-Demand Instances are suitable for workloads that need flexibility and are short-term or unpredictable. However, they are priced higher than other options.

 Dedicated Instances: Dedicated Instances run on hardware dedicated to a single customer account but are priced higher than On-Demand Instances. They may not be the most cost-effective for interruptible workloads.

 Spot Instances: Spot Instances allow you to bid for unused EC2 capacity at potentially lower costs. They are suitable for interruptible workloads where you can tolerate potential interruptions. However, they can be terminated with short notice if the capacity is needed by On-Demand or Reserved Instances.

 Reserved Instances: Reserved Instances provide a capacity reservation and offer cost savings over On-Demand pricing for a commitment of 1 or 3 years. They are more suitable for steady-state workloads with predictable usage.
---
Selected Answer: C
Spot Instances are the most cost-effective option for workloads that can be interrupted, as they allow you to bid for unused EC2 capacity at a significantly lower price than On-Demand Instances. Since the application testing in this scenario can be interrupted and doesn't need to run continuously, Spot Instances would meet the requirements while minimizing costs.
---
Selected Answer: C
Spot Instances are a good fit for stateless, fault-tolerant workloads that can be interrupted without any impact on the overall job.

</details>

---

## Question 38: CLF-C02-ET-Q038
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to estimate the cost for its AWS architecture solution before migration.

Which AWS service or feature will meet this requirement?

**Choices:**
- A) Amazon Detective
- B) AWS Budgets
- C) AWS Resource Explorer
- D) AWS Pricing Calculator

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Pricing Calculator: AWS Pricing Calculator is a web-based tool that helps you estimate the cost of using various AWS services based on your specific usage patterns. You can input details about your planned AWS architecture, including the types and quantities of services you plan to use, and the calculator will provide a detailed estimate of the costs associated with those services. This tool is designed to help with cost planning and budgeting before actual deployment.
---
Selected Answer: D
Price calculator
---
D is correct

please help with discussion on 571~574

</details>

---

## Question 39: CLF-C02-ET-Q039
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to centrally manage its employee's access to multiple AWS accounts.

Which AWS service or feature should the company use to meet this requirement?

**Choices:**
- A) AWS Identity and Access Management Access Analyzer
- B) AWS Secrets Manager
- C) AWS IAM Identity Center
- D) AWS Security Token Service (AWS STS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS IAM Identity Center
---
Selected Answer: C
C. AWS IAM Identity Center
AWS IAM Identity Center (formerly AWS Single Sign-On) is the ideal solution for centrally managing employee access to multiple AWS accounts.

</details>

---

## Question 40: CLF-C02-ET-Q040
**Domain 3:** Cloud Technology and Services  

**Question:**  
A university receives a grant to conduct research by using AWS services. The research team needs to make sure the grant money lasts for the entire school year. The team has decided on a monthly allocation that adds up to the total grant amount.

Which AWS service or feature will notify the team if spending exceeds the planned amount?

**Choices:**
- A) AWS Budgets
- B) Cost Explorer
- C) Cost allocation tags
- D) Cost categories

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Budgets
---
Keyword is monthly allocation, so user can set the limit if the cost is not exceed the amount by using AWS Budgets only.

Answer is A.AWS Budgets

</details>

---

## Question 41: CLF-C02-ET-Q041
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has migrated its workload to the AWS Cloud. The company wants to optimize existing Amazon EC2 resources.

Which AWS services or tools provide this functionality? (Choose two.)

**Choices:**
- A) AWS Elastic Beanstalk
- B) AWS Cost Explorer
- C) Amazon Detective
- D) AWS Compute Optimizer
- E) AWS Billing Conductor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
B. AWS Cost Explorer and D. AWS Compute Optimizer.

</details>

---

## Question 42: CLF-C02-ET-Q042
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company with multiple accounts and teams wants to set up a new multi-account AWS environment.

Which AWS service supports this requirement?

**Choices:**
- A) AWS CloudFormation
- B) AWS Control Tower
- C) AWS Config
- D) Amazon Virtual Private Cloud (Amazon VPC)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Control Tower - The easiest way to set up and govern a secure multi account AWS environment
---
Selected Answer: B
B. AWS Control Tower - service that helps you set up and govern a multi-account AWS environment based on AWS best practices.

</details>

---

## Question 43: CLF-C02-ET-Q043
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company needs access to checks and recommendations that help the company follow AWS best practices for cost optimization, security, fault tolerance, performance, and service quotas.

Which combination of an AWS service and AWS Support plan on the AWS account will meet these requirements?

**Choices:**
- A) AWS Trusted Advisor with AWS Developer Support
- B) AWS Health Dashboard with AWS Enterprise Support
- C) AWS Trusted Advisor with AWS Business Support
- D) AWS Health Dashboard with AWS Enterprise On-Ramp Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (86%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Full Trusted Advisor is available for Business & Enterprise
support plans
---
Selected Answer: C
C. AWS Trusted Advisor with AWS Business Support
---
Selected Answer: C
AWS Trusted Advisor, included with AWS Business Support, offers numerous features and benefits. It provides comprehensive checks in areas such as Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits. This helps users improve AWS efficiency and security comprehensively.

</details>

---

## Question 44: CLF-C02-ET-Q044
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service helps users plan and track their server and application inventory migration data to AWS?

**Choices:**
- A) Amazon CloudWatch
- B) AWS DataSync
- C) AWS Migration Hub
- D) AWS Application Migration Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (75%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Migration Hub - AWS service designed to help users plan, track, and manage their server and application inventory during the migration process to AWS.
---
Selected Answer: C
C. AWS Migration Hub : helps users plan, track, and manage the migration of their server and application inventory to AWS. It provides a single place to monitor and track the progress of migrations across various AWS and partner migration tools.
---
Selected Answer: C
C. AWS Migration Hub

Explanation: AWS Migration Hub helps users plan and track their server and application inventory migration data to AWS. It provides a single location to monitor the progress of application migrations across multiple AWS and partner solutions. Migration Hub offers visibility into the status of each migration and helps in tracking and planning the migration process effectively.

</details>

---

## Question 45: CLF-C02-ET-Q045
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS team or offering helps users accelerate cloud adoption through paid engagements in any of several specialty practice areas?

**Choices:**
- A) AWS Enterprise Support
- B) AWS solutions architects
- C) AWS Professional Services
- D) AWS account managers

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Professional Services - offering that helps customers accelerate their cloud adoption by providing expert guidance and specialized knowledge across various practice areas.
---
Keyword is Paid service, In AWS will provide the Professional service to give the solution for our problem in person service.
---
Keyword Paid services

Answer is C

</details>

---

## Question 46: CLF-C02-ET-Q046
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to purchase Amazon EC2 instances to support an application that will run continuously for more than 1 year.

Which EC2 instance purchasing option meets these requirements MOST cost-effectively?

**Choices:**
- A) Dedicated Instances
- B) Spot Instances
- C) Reserved Instances
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Reserved Instances - most cost effective option when running continuously for 1 year or more.

</details>

---

## Question 47: CLF-C02-ET-Q047
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which programming languages does AWS Cloud Development Kit (AWS CDK) currently support? (Choose two.)

**Choices:**
- A) Python
- B) Swift
- C) TypeScript
- D) Ruby
- E) PHP

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
The AWS Cloud Development Kit (AWS CDK) supports: JavaScript/TypeScript, Python, Java, and .NET
---
The AWS Cloud Development Kit (AWS CDK) supports:

Python
TypeScript
Java
C#/.NET
Languages like Swift, Ruby, and PHP are not supported by AWS CDK at this time.
---
Selected Answer: AC
https://docs.aws.amazon.com/cdk/v2/guide/languages.html
The AWS Cloud Development Kit (AWS CDK) has first-class support for the following general-purpose programming languages:
TypeScript
JavaScript
Python
Java
C#
Go

</details>

---

## Question 48: CLF-C02-ET-Q048
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service gives users the ability to discover and protect sensitive data that is stored in Amazon S3 buckets?

**Choices:**
- A) Amazon Macie
- B) Amazon Detective
- C) Amazon GuardDuty
- D) AWS IAM Access Analyzer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Can I pass the exam by just looking at these questions?
---
Selected Answer: A
Amazon Macie: A security service that uses machine learning to automatically discover, classify, and protect sensitive data, such as personally identifiable information (PII), in Amazon S3.

 Amazon Detective: A security service that helps users investigate and identify the root cause of potential security issues or suspicious activities.

 Amazon GuardDuty: A threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect AWS accounts and workloads.

 AWS IAM Access Analyzer: Helps users identify resources that can be accessed by external principals (such as IAM roles or resource-based policies) and provides findings to help ensure resources are shared securely.
---
Selected Answer: A
Amazon Macie is a fully managed service that helps discover, classify, and protect sensitive data in Amazon S3. It uses machine learning to automatically detect sensitive data, such as personally identifiable information (PII), within your S3 buckets. Macie helps ensure that sensitive data is properly secured and protected.

</details>

---

## Question 49: CLF-C02-ET-Q049
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature gives users the ability to provision AWS infrastructure programmatically?

**Choices:**
- A) AWS Cloud Development Kit (AWS CDK)
- B) Amazon CodeGuru
- C) AWS Config
- D) AWS CodeCommit

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Answer is A
---
Selected Answer: A
The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.

</details>

---

## Question 50: CLF-C02-ET-Q050
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature allows a company to have its own logically isolated section of the AWS Cloud?

**Choices:**
- A) AWS VPN
- B) Availability Zones
- C) Amazon Virtual Private Cloud (Amazon VPC)
- D) AWS Regions

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon Virtual Private Cloud (Amazon VPC)
---
C. Amazon Virtual Private Cloud (Amazon VPC)

</details>

---

## Question 51: CLF-C02-ET-Q051
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following actions are controlled with AWS Identity and Access Management (IAM)? (Choose two.)

**Choices:**
- A) Control access to AWS service APIs and to other specific resources.
- B) Provide intelligent threat detection and continuous monitoring.
- C) Protect the AWS environment using multi-factor authentication (MFA).
- D) Grant users access to AWS data centers.
- E) Provide firewall protection for applications from common web attacks.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
My choices are A & C

</details>

---

## Question 52: CLF-C02-ET-Q052
**Domain 3:** Cloud Technology and Services  

**Question:**  
Why are AWS CloudFormation templates used?

**Choices:**
- A) To reduce provisioning time by using automation.
- B) To transfer existing infrastructure to another company.
- C) To reuse on-premises infrastructure in the AWS Cloud.
- D) To deploy large infrastructure with no cost implications.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. To reduce provisioning time by using automation.

</details>

---

## Question 53: CLF-C02-ET-Q053
**Domain 2:** Security and Compliance  

**Question:**  
A company is using AWS Identity and Access Management (IAM).

Who can manage the access keys of the AWS account root user?

**Choices:**
- A) IAM users in the same account that have been granted permission
- B) IAM roles in any account that have been granted permission
- C) IAM users and roles that have been granted permission
- D) The AWS account owner

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. The AWS account owner
---
D. The AWS account owner

</details>

---

## Question 54: CLF-C02-ET-Q054
**Domain 2:** Security and Compliance  

**Question:**  
Which group shares responsibility with AWS for security and compliance of AWS accounts and resources?

**Choices:**
- A) Third-party vendors
- B) Customers
- C) Reseller partners
- D) Internet providers

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Customers

</details>

---

## Question 55: CLF-C02-ET-Q055
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs an event history of which AWS resources the company has created.

Which AWS service will provide this information?

**Choices:**
- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) Amazon Aurora
- D) Amazon EventBridge

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS CloudTrail
---
For tracking a historical record of AWS resource creation and changes, AWS CloudTrail remains the appropriate choice.

</details>

---

## Question 56: CLF-C02-ET-Q056
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run relationship databases in the AWS Cloud. The company wants to use a managed service that will install the database and run regular software updates.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon S3
- B) Amazon RDS
- C) Amazon Elastic Block Store (Amazon EBS)
- D) Amazon DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon RDS - fully managed service that allows you to run relational databases in AWS. Backups, patching, etc. are taken care of.

</details>

---

## Question 57: CLF-C02-ET-Q057
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides a fully managed graph database for highly connected datasets?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon RDS
- C) Amazon Neptune
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Neptune is Fully Managed NoSQL graph database that can store, map and query relationships between data sets.
---
Selected Answer: C
C. Amazon Neptune - think "graph" as the keyword here.

</details>

---

## Question 58: CLF-C02-ET-Q058
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company's cloud environment includes Amazon EC2 instances and Application Load Balancers. The company wants to improve protections for its cloud resources against DDoS attacks. The company also wants to have real-time visibility into any DDoS attacks.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Shield Standard
- B) AWS Firewall Manager
- C) AWS Shield Advanced
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Shield Advanced
---
C. Enhanced visibility into DDoS events and attacks – Shield Advanced gives you access to advanced, real-time metrics and reports for extensive visibility into events and attacks on your protected AWS resources. You can access this information through the Shield Advanced API and console, and through Amazon CloudWatch metrics.

</details>

---

## Question 59: CLF-C02-ET-Q059
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following services can be used to block network traffic to an instance? (Choose two.)

**Choices:**
- A) Security groups
- B) Amazon Virtual Private Cloud (Amazon VPC) flow logs
- C) Network ACLs
- D) Amazon CloudWatch
- E) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
Security groups: Act as a virtual firewall for instances, controlling inbound and outbound traffic. They are associated with instances and operate at the instance level. You can configure security group rules to allow or deny traffic based on IP addresses, port ranges, and protocols.

 Network ACLs: Are an additional layer of security for your VPC. They operate at the subnet level and are stateless, meaning they evaluate rules for inbound and outbound traffic separately. Network ACLs can be used to allow or deny traffic based on IP addresses, port ranges, and protocols.

 Amazon Virtual Private Cloud (Amazon VPC) flow logs: Capture information about the IP traffic going to and from network interfaces in a VPC. While they provide visibility into network traffic, they don't block or control traffic.

 Amazon CloudWatch: A monitoring service that collects and tracks metrics, logs, and events from various AWS resources. It is not used for blocking network traffic to an instance.

 AWS CloudTrail: Provides a record of actions taken by users, roles, or services within an AWS account. It does not block network traffic but helps in auditing and tracking API calls.
---
A. Security groups
C. Network ACLs

Security groups are stateful firewalls that control inbound and outbound traffic at the instance level. You can configure security groups to allow or deny specific types of network traffic to and from your instances.

Network ACLs (Access Control Lists) are stateless firewalls that control traffic at the subnet level. Network ACLs define rules to allow or deny traffic based on source and destination IP addresses, ports, and protocols.
---
Selected Answer: AC
oth Security groups and Network ACLs are used to control and block network traffic to and from Amazon EC2 instances.

</details>

---

## Question 60: CLF-C02-ET-Q060
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to update its online data processing application by implementing container-based services that run for 4 hours at a time. The company does not want to provision or manage server instances.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Lambda
- B) AWS Fargate
- C) Amazon EC2
- D) AWS Elastic Beanstalk

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Oops, got ahead of myself. Correct answer is B. Fargate
---
Selected Answer: A
A. AWS Lambda
---
Key word is container-based services, so among the following option AWS Fargate is a container service in AWS.

Answer is B.AWS Fargate

</details>

---

## Question 61: CLF-C02-ET-Q061
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to continuously run an experimental workload on an Amazon EC2 instance and stop the instance after 12 hours.

Which instance purchasing option will meet this requirement MOST cost-effectively?

**Choices:**
- A) On-Demand Instances
- B) Reserved Instances
- C) Spot Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `76%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (76%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The on-the-spot choice was C) Spot Instances, but after re-reading the question several times, I realized that the company needs a CONTINUOUSLY running workload for 12 hours. Spot Instances can be interrupted by AWS, making them less reliable.
---
Selected Answer: A
I think Answes is A - on demand, because - company needs a CONTINUOUSLY running workload

AHAHA, I use AI to check the question, Here is Answer:

The most cost-effective option for running an experimental workload on an Amazon EC2 instance for 12 hours and then stopping it is:
✅ Spot Instances

Than i say - But spot instances can be interrupted by amazon and question have this words "needs to continuously run".

Answer: You're absolutely right! Since the question states that the workload "needs to continuously run" for 12 hours, Spot Instances may not be the best option because they can be interrupted by AWS at any time.

The best cost-effective option in this case would be:

✅ On-Demand Instances
---
Selected Answer: A
Its says 'continuously'

</details>

---

## Question 62: CLF-C02-ET-Q062
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which cloud transformation journey phase of the AWS Cloud Adoption Framework (AWS CAF) focuses on demonstrating how the cloud helps accelerate business outcomes?

**Choices:**
- A) Scale
- B) Envision
- C) Align
- D) Launch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Envision

Identify and prioritize transformation opportunities in line with your strategic objectives. Associating your transformation initiatives with key stakeholders and measurable business outcomes will help you demonstrate value as you progress through your transformation journey.
---
Envision
---
Selected Answer: B
Envision
Identify and prioritize transformation opportunities in line with your strategic objectives. Associating your transformation initiatives with key stakeholders and measurable business outcomes will help you demonstrate value as you progress through your transformation journey.

</details>

---

## Question 63: CLF-C02-ET-Q063
**Domain 2:** Security and Compliance  

**Question:**  
Which option is a customer responsibility under the AWS shared responsibility model?

**Choices:**
- A) Maintenance of underlying hardware of Amazon EC2 instances
- B) Application data security
- C) Physical security of data centers
- D) Maintenance of VPC components

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Application data security
---
B: 
The customer is responsible for operating-system patches and updates on EC2 Instances, as well as data security on the instances, Security Groups rules, etc.
---
B. Application data security

</details>

---

## Question 64: CLF-C02-ET-Q064
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants its Amazon EC2 instances to operate in a highly available environment, even if there is a natural disaster in a particular geographic area.

Which approach will achieve this goal?

**Choices:**
- A) Use EC2 instances in multiple AWS Regions.
- B) Use EC2 instances in multiple Amazon CloudFront locations.
- C) Use EC2 instances in multiple edge locations.
- D) Use EC2 instances in AWS Local Zones.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Use EC2 instances in multiple AWS Regions.
---
A. Use EC2 instances in multiple AWS Regions.
---
A is the viable option

</details>

---

## Question 65: CLF-C02-ET-Q065
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to modernize and convert a monolithic application into microservices. The company wants to move the application to AWS.

Which migration strategy should the company use?

**Choices:**
- A) Rehost
- B) Replatform
- C) Repurchase
- D) Refactor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
It should be D. Refactor:

Lift and shift—moving applications to the cloud as-is. This is also sometimes referred to as rehosting. Refactor—modifying applications to better support the cloud environment.Replatform—moving applications to the cloud without major changes, but taking advantage of benefits of the cloud environment.Rebuild—rewrite the application from scratch.Replace—retire the application and replace it with a new cloud-native application.
---
is it D? can anyone confirm?
---
Selected Answer: D
D. Refactor (also called re-architect) is the migration strategy where an application is redesigned and modified to take full advantage of modern cloud-native features, such as microservices architectures. In this approach, a monolithic application is broken down into smaller, loosely coupled services (microservices) to improve scalability, flexibility, and maintainability.

Why Refactor is the Best Choice:
Breaking a monolithic application into microservices typically requires significant changes to the application's architecture and codebase.
Refactoring ensures the application leverages cloud-native features like containerization (using AWS services like Amazon ECS, Amazon EKS, or AWS Fargate) and serverless components (e.g., AWS Lambda).
It aligns with the goal of modernization and preparing the application for long-term agility and scalability in the cloud.

</details>

---

## Question 66: CLF-C02-ET-Q066
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS service enables users to create copies of resources across AWS Regions?

**Choices:**
- A) Amazon ElastiCache
- B) AWS CloudFormation
- C) AWS CloudTrail
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS CloudFormation
---
AWS CloudFormation is an infrastructure as code (IaC) service that allows you to easily model, provision, and manage AWS and third-party resources. 
Developers can define and provision AWS infrastructure resources using a JSON- or YAML-formatted infrastructure as code template.

Once Developer or Architect write the code to Infrastructure provision as a code (template),they can use multiple times without using GUI configuration

It automatically creates Infrastructure by using the what in our template

Answer is B.AWS CloudFormation
---
B. CloudFormation - uses templates to define collection of resources also known as stacks*

</details>

---

## Question 67: CLF-C02-ET-Q067
**Domain 2:** Security and Compliance  

**Question:**  
Which task is the responsibility of AWS, according to the AWS shared responsibility model?

**Choices:**
- A) Apply guest operating system patches to Amazon EC2 instances.
- B) Provide monitoring of human resources information management (HRIM) systems.
- C) Perform automated backups of Amazon RDS instances.
- D) Optimize the costs of running AWS services.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C - AWS manages the infrastructure underlying Amazon RDS, including the ability to automatically back up databases.

</details>

---

## Question 68: CLF-C02-ET-Q068
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user needs to perform a one-time backup of an Amazon Elastic Block Store (Amazon EBS) volume that is attached to an Amazon EC2 instance.

What is the MOST operationally efficient way to perform this backup?

**Choices:**
- A) Attach another EBS volume to the EC2 instance, and copy the contents.
- B) Copy the EBS volume to a server that is running outside AWS and is connected with AWS Direct Connect.
- C) Create an EBS snapshot of the volume.
- D) Create a custom script to copy the EBS file contents to Amazon S3.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Create an EBS snapshot of the volume.
---
"Protect block storage data in the cloud, as well as on-premises block data using Amazon EBS Snapshots – a point-in-time copy that can be used to enable disaster recovery, migrate data across regions and accounts, and improve backup compliance. AWS further simplifies the lifecycle management of your snapshots through integration with Amazon Data Lifecycle Manager..."
---
The MOST operationally efficient way to perform a one-time backup of an Amazon Elastic Block Store (Amazon EBS) volume that is attached to an Amazon EC2 instance is:

C. Create an EBS snapshot of the volume.

</details>

---

## Question 69: CLF-C02-ET-Q069
**Domain 3:** Cloud Technology and Services  

**Question:**  
A developer who has no AWS Cloud experience wants to use AWS technology to build a web application.

Which AWS service should the developer use to start building the application?

**Choices:**
- A) Amazon SageMaker
- B) AWS Lambda
- C) Amazon Lightsail
- D) Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Lightsail is a virtual private server (VPS) and is the easiest way to get started with AWS for
people with little cloud experience!
---
Selected Answer: C
C. Amazon Lightsail - best for someone with no cloud experience
---
Keyword- who has no AWS Cloud experience 
If any one does not have experience in web servers, AWS provides the VPS- Virtual Private Server to host our website without prior knowledge about web hosting.

The AWS provide Amazon Lightsail service for VPS web hosting

Answer is- Amazon Lightsail

</details>

---

## Question 70: CLF-C02-ET-Q070
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to manage access and permissions for its third-party software as a service (SaaS) applications. The company wants to use a portal where end users can access assigned AWS accounts and AWS Cloud applications.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon Cognito
- B) AWS IAM Identity Center (AWS Single Sign-On)
- C) AWS Identity and Access Management (IAM)
- D) AWS Directory Service for Microsoft Active Directory

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS IAM Identity Center (AWS Single Sign-On)
---
B. IAM Identity Center helps you securely create, or connect, your workforce identities and manage their access centrally across AWS accounts and applications.
---
B. AWS IAM Identity Center (AWS Single Sign-On) aka AWS IAM Identity Center*

</details>

---

## Question 71: CLF-C02-ET-Q071
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is designed for users running workloads that include a NoSQL database?

**Choices:**
- A) Amazon RDS
- B) Amazon S3
- C) Amazon Redshift
- D) Amazon DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
DynamoDB- Fully managed Non-relational database in AWS
---
Selected Answer: D
D. Amazon DynamoDB = noSQL

</details>

---

## Question 72: CLF-C02-ET-Q072
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a website on AWS. The company wants to deliver the website to a worldwide audience and provide low-latency response times for global users.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS CloudFormation
- B) Amazon CloudFront
- C) Amazon ElastiCache
- D) Amazon DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon CloudFront = low latency for global users

</details>

---

## Question 73: CLF-C02-ET-Q073
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to add a conversational chatbot to its website.

Which AWS service can the company use to meet this requirement?

**Choices:**
- A) Amazon Textract
- B) Amazon Lex
- C) AWS Glue
- D) Amazon Rekognition

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon Lex: Conversational AI for Chatbots
---
Selected Answer: B
B. Amazon Lex
---
Amazon Lex is an AWS service specifically designed for building conversational chatbots and voice assistants. It allows you to create, deploy, and integrate chatbots into applications such as websites or mobile apps.

</details>

---

## Question 74: CLF-C02-ET-Q074
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature can be used to monitor for potential disk write spikes on a system that is running on Amazon EC2?

**Choices:**
- A) AWS CloudTrail
- B) AWS Health Dashboard
- C) AWS Trusted Advisor
- D) Amazon CloudWatch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Amazon CloudWatch is designed to monitor AWS resources and applications, including Amazon EC2 instances. It provides metrics, including those related to disk performance, such as disk write and read operations. By using CloudWatch, you can set up alarms to notify you of potential disk write spikes or other performance issues, allowing for real-time monitoring and proactive response.
---
D. Amazon CloudWatch is a service used for monitoring and observing resources in real-time by providing users with data and actionable insights to monitor their respective applications, stimulate system-wide performance changes, and optimize resource utilization.
---
D. Amazon CloudWatch

</details>

---

## Question 75: CLF-C02-ET-Q075
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is a perspective that includes foundational capabilities of the AWS Cloud Adoption Framework (AWS CAF)?

**Choices:**
- A) Sustainability
- B) Performance efficiency
- C) Governance
- D) Reliability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
This question is outdated since document revision October 3, 2023
https://docs.aws.amazon.com/wellarchitected/latest/framework/document-revisions.html
Pillars:
- Operational excellence
- Security
- Reliability
- Performance efficiency
- Cost optimization
- Sustainability

"AWS CAF perspectives and foundational capabilities" is not used anymore.
---
There are 3 perspective options for AWS CAF
1-Business
2-People
3-Governance
https://aws.amazon.com/cloud-adoption-framework/
---
Selected Answer: C
Governance

</details>

---

## Question 76: CLF-C02-ET-Q076
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can identify when an Amazon EC2 instance was terminated?

**Choices:**
- A) AWS Identity and Access Management (IAM)
- B) AWS CloudTrail
- C) AWS Compute Optimizer
- D) Amazon EventBridge

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B. AWS CloudTrail

AWS CloudTrail is a service that records all API activity in your AWS account, including the termination of EC2 instances. It creates log entries for various events, providing an audit trail of actions taken on resources. By reviewing CloudTrail logs, you can identify when an EC2 instance was terminated, who initiated the termination, and other relevant details about the event.
---
Selected Answer: B
AWS CloudTrail: A service that records API calls and related events for your AWS account. It provides visibility into user activity, resource changes, and important events. CloudTrail logs can be used to identify when an Amazon EC2 instance was terminated, along with other activities and events within your AWS environment.

The other options do not specifically focus on tracking and logging events related to instance termination:

 AWS Identity and Access Management (IAM): Is used for managing access to AWS services and resources. It does not provide detailed logs of instance termination events.

 AWS Compute Optimizer: Analyzes the configuration and utilization of EC2 instances to make recommendations for optimal performance. It does not log specific events like instance termination.

 Amazon EventBridge: A serverless event bus service that makes it easy to connect different applications using events. While it can be used for event-driven architectures, it doesn't focus on logging and tracking instance termination events.
---
Selected Answer: B
AWS CloudTrail records API calls made on your AWS account, including when an Amazon EC2 instance is terminated. CloudTrail logs events such as starting, stopping, and terminating instances, along with details about who made the request, when it occurred, and other relevant information. This makes it the appropriate service to track the termination of EC2 instances

</details>

---

## Question 77: CLF-C02-ET-Q077
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has applications that control on-premises factory equipment.

Which AWS service should the company use to run these applications with the LEAST latency?

**Choices:**
- A) AWS Outposts
- B) Amazon EC2
- C) AWS Lambda
- D) AWS Fargate

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Outposts allow you to extend and run AWS services on premises
---
A. AWS Outposts supports workloads and devices requiring low latency access to on-premises systems, local data processing, data residency, and application migration with local system interdependencies.
---
A. AWS Outposts

</details>

---

## Question 78: CLF-C02-ET-Q078
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud Adoption Framework (AWS CAF) perspective focuses on organizing an inventory of data products in a data catalog?

**Choices:**
- A) Operations
- B) Governance
- C) Business
- D) Platform

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Governance
Data curation – Collect, organize, access, and enrich metadata and use it to organize an inventory of data products in a Data Catalog. A Data Catalog can help facilitate data monetization and self-service analytics by helping data consumers quickly locate relevant data products as well as understand their context, such as provenance and quality.
---
Selected Answer: B
It's B.

It's the very first line of governance perspective's data curation:

https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/data-curation.html
---
C. Business

</details>

---

## Question 79: CLF-C02-ET-Q079
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company runs its production workload in the AWS Cloud. The company needs to choose one of the AWS Support Plans.

Which of the AWS Support Plans will meet these requirements at the LOWEST cost?

**Choices:**
- A) Developer
- B) Enterprise On-Ramp
- C) Enterprise
- D) Business

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `85%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (85%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
I assume D.Business is correct.
Developer - Recommended if you are experimenting or testing in AWS
Business - Minimum recommended tier if you have production workloads in AWS
Enterprise On-Ramp - Recommended if you have production and/or business critical workloads in AWS
Enterprise - Recommended if you have business and/or mission critical workloads in AWS
https://aws.amazon.com/premiumsupport/plans/
---
Selected Answer: D
D. Business - since they are running a production workload
---
for a production workload, the D. Business plan is the most appropriate choice, though it is not the lowest cost option.

</details>

---

## Question 80: CLF-C02-ET-Q080
**Domain 2:** Security and Compliance  

**Question:**  
What is the primary use case for Amazon GuardDuty?

**Choices:**
- A) Prevention of DDoS attacks
- B) Protection against SQL injection attacks
- C) Automatic monitoring for threats to AWS workloads
- D) Automatic provisioning of AWS resources

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon GuardDuty - threat detection service that continuously monitors your AWS environment.
---
Selected Answer: C
C. Automatic monitoring for threats to AWS workloads
---
C. Automatic monitoring for threats to AWS workloads

</details>

---

## Question 81: CLF-C02-ET-Q081
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which VPC component can a company use to set up a virtual firewall at the Amazon EC2 instance level?

**Choices:**
- A) Network ACL
- B) Security group
- C) Route table
- D) NAT gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Security group = instance level
---
B. Security group

</details>

---

## Question 82: CLF-C02-ET-Q082
**Domain 2:** Security and Compliance  

**Question:**  
A developer needs to interact with AWS by using the AWS CLI.

Which security feature or AWS service must be provisioned in the developer's account to meet this requirement?

**Choices:**
- A) User name and password
- B) AWS Systems Manager
- C) Root password access
- D) AWS access key

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Access key for programmatic access*
---
Selected Answer: D
D. AWS access key
---
D. AWS access key

</details>

---

## Question 83: CLF-C02-ET-Q083
**Domain 3:** Cloud Technology and Services  

**Question:**  
A food delivery company needs to block users in certain countries from accessing its website.

Which AWS service should the company use to meet this requirement?

**Choices:**
- A) AWS WAF
- B) AWS Control Tower
- C) Amazon Fraud Detector
- D) Amazon Pinpoint

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS WAF
---
A. AWS WAF

</details>

---

## Question 84: CLF-C02-ET-Q084
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to use Amazon S3 to store audio files that are each 5 megabytes in size. The company will rarely access the files, but the company must be able to retrieve the files immediately.

Which S3 storage class will meet these requirements MOST cost-effectively?

**Choices:**
- A) S3 Standard
- B) S3 Standard-Infrequent Access (S3 Standard-IA)
- C) S3 Glacier Flexible Retrieval
- D) S3 Glacier Deep Archive

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Answer is B:
Amazon S3 Glacier Flexible Retrieval is a storage class within Amazon S3 designed for archiving data that doesn't require immediate access (this rules out Glacier).
---
Selected Answer: C
S3 Standard IA - Storage Cost: $0.0125 × 100 = $1.25/month
S3 Glacier Flexible Retrieval: Storage Cost: $0.004 × 100 = $0.40/month
---
Selected Answer: B
B. S3 Standard-Infrequent Access (S3 Standard-IA) - Best suited for data that is rarely accessed, but needs to be retrieved immediately when needed.

</details>

---

## Question 85: CLF-C02-ET-Q085
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to set up a secure network connection from on premises to the AWS Cloud within 1 week.

Which solution will meet these requirements?

**Choices:**
- A) AWS Direct Connect
- B) Amazon VPC
- C) AWS Site-to-Site VPN
- D) Edge location

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The key word here is "1 week". The Direct Connect needs more times as it involves multiple parties and configurations...
---
Selected Answer: C
AWS Site-to-Site VPN is a fully-managed service that creates a secure connection between your data center or branch office and your AWS resources using IP Security (IPSec) tunnels
---
Selected Answer: C
C. AWS Site-to-Site VPN - best for the short set up time

</details>

---

## Question 86: CLF-C02-ET-Q086
**Domain 2:** Security and Compliance  

**Question:**  
What is a customer responsibility under the AWS shared responsibility model when using AWS Lambda?

**Choices:**
- A) Maintenance of the underlying Lambda hardware.
- B) Maintenance of the Lambda networking infrastructure.
- C) The code and libraries that run in the Lambda functions.
- D) The Lambda server software.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. The code and libraries that run in the Lambda functions. 

AWS is responsible for all the other options.
---
C. The code and libraries that run in the Lambda functions.

</details>

---

## Question 87: CLF-C02-ET-Q087
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is a fully managed MySQL-compatible database?

**Choices:**
- A) Amazon S3
- B) Amazon DynamoDB
- C) Amazon Redshift
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon S3: Amazon S3 (Simple Storage Service) is an object storage service and is not a database.

 Amazon DynamoDB: A fully managed NoSQL database service, but it is not MySQL-compatible.

 Amazon Redshift: A fully managed data warehouse service, not a MySQL-compatible database.

 Amazon Aurora: A fully managed relational database engine compatible with MySQL and PostgreSQL. It offers the performance and availability of commercial databases with the simplicity and cost-effectiveness of open-source databases.
---
Selected Answer: D
mazon Aurora is a fully managed relational database service that is MySQL-compatible (as well as PostgreSQL-compatible). It is designed for high performance, availability, and scalability. Amazon Aurora automatically handles tasks like patching, backups, and scaling without requiring manual intervention.
---
Selected Answer: D
Amazon Aurora: A fully managed relational database engine compatible with MySQL and PostgreSQL. It offers the performance and availability of commercial databases with the simplicity and cost-effectiveness of open-source databases.
 upvoted 7 times

</details>

---

## Question 88: CLF-C02-ET-Q088
**Domain 2:** Security and Compliance  

**Question:**  
Which tasks are the responsibility of AWS according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Configure AWS Identity and Access Management (IAM).
- B) Configure security groups on Amazon EC2 instances.
- C) Secure the access of physical AWS facilities.
- D) Patch applications that run on Amazon EC2 instances.
- E) Perform infrastructure patching and maintenance.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CE (100%). Contributor Answer: CE.

Community Rationale & Discussion:
Selected Answer: CE
C and E are the answers
---
Selected Answer: CE
C & E are AWS responsibilities.
---
C. Secure the access of physical AWS facilities.

E. Perform infrastructure patching and maintenance.

</details>

---

## Question 89: CLF-C02-ET-Q089
**Domain 2:** Security and Compliance  

**Question:**  
A company's compliance officer wants to review the AWS Service Organization Control (SOC) reports.

Which AWS service or feature should the compliance officer use to complete this task?

**Choices:**
- A) AWS Artifact
- B) AWS Concierge Support
- C) AWS Support
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The answer is A. AWS Artifact.
AWS Artifact is your go-to resource for on-demand access to AWS compliance reports, including SOC reports, PCI DSS attestations, and ISO certifications. It provides a central repository where you can download these documents for review.
Here's why the other options are not the correct choice:
 * AWS Concierge Support & AWS Support: These are support channels for getting help with AWS services. While they might be able to point you to where the reports are located, they don't directly provide the reports themselves. Artifact is the self-service portal for this.
 * AWS Trusted Advisor: Trusted Advisor provides recommendations for optimizing your AWS environment for cost optimization, performance, security, and operational excellence. It doesn't provide compliance reports like SOC reports.
---
Selected Answer: A
Answer is AWS Artifact
---
Selected Answer: A
A. AWS Artifact

</details>

---

## Question 90: CLF-C02-ET-Q090
**Domain 2:** Security and Compliance  

**Question:**  
A company has a compliance requirement to record and evaluate configuration changes, as well as perform remediation actions on AWS resources.

Which AWS service should the company use?

**Choices:**
- A) AWS Config
- B) AWS Secrets Manager
- C) AWS CloudTrail
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
answer is AWS Config
---
Selected Answer: A
A. AWS Config is specifically designed for monitoring and recording configuration changes to AWS resources.
---
A. AWS Config

AWS Config provides detailed historical configuration data, allows you to evaluate configurations against policies, and supports automated remediation of non-compliant configurations. It helps with continuous monitoring and auditing of AWS resource configurations.

</details>

---

## Question 91: CLF-C02-ET-Q091
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to perform a one-time migration of a large dataset with millions of files from its on-premises data center to the AWS Cloud.

Which AWS service should the company use for the migration?

**Choices:**
- A) AWS Database Migration Service (AWS DMS)
- B) AWS DataSync
- C) AWS Migration Hub
- D) AWS Application Migration Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS DataSync - best option for one-time transfer of large amounts of data
---
one-time-key for AWS DataSync
---
B. AWS DataSync

AWS DataSync is designed for transferring large amounts of data quickly and securely between on-premises storage and AWS. It is well-suited for one-time migrations of large datasets and can handle millions of files efficiently.

</details>

---

## Question 92: CLF-C02-ET-Q092
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS network services or features allow CIDR block notation when providing an IP address range? (Choose two.)

**Choices:**
- A) Security groups
- B) Amazon Machine Image (AMI)
- C) Network access control list (network ACL)
- D) AWS Budgets
- E) Amazon Elastic Block Store (Amazon EBS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
A & C are the correct answers
---
C. Network access control list (network ACL)

A. Security groups

</details>

---

## Question 93: CLF-C02-ET-Q093
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to develop an accessibility application that will convert text into audible speech.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon MQ
- B) Amazon Polly
- C) Amazon Neptune
- D) Amazon Timestream

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Polly - text to life-like speech
---
Answer is B.
Here's why: 
A. Amazon MQ - is a managed message broker service that enables software applications and components to communicate through various programming languages.
C. Amazon Neptune - is a fast, fully managed database service for graph analytics and serverless applications.
D. Amazon Timestream - is a fast, scalable, and fully managed time series database that simplifies data lifecycle management and analysis.
---
B. Amazon Polly

</details>

---

## Question 94: CLF-C02-ET-Q094
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to set up dedicated network connectivity between its on-premises data center and the AWS Cloud. The network cannot use the public internet.

Which AWS service or feature will meet these requirements?

**Choices:**
- A) AWS Transit Gateway
- B) AWS VPN
- C) Amazon CloudFront
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Direct Connect - provides dedicated network connectivity between your on-premises data center and AWS, bypassing the public internet.
---
D. AWS Direct Connect

AWS Direct Connect provides a dedicated network connection from your on-premises data center to AWS. This connection bypasses the public internet, offering a more secure and reliable connection with potentially lower latency and higher bandwidth.

</details>

---

## Question 95: CLF-C02-ET-Q095
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to use dashboards and charts to analyze insights from business data.

Which AWS service will provide the dashboards and charts for these insights?

**Choices:**
- A) Amazon Macie
- B) Amazon Aurora
- C) Amazon QuickSight
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon QuickSight - dashboards and charts
---
C. Amazon QuickSight

</details>

---

## Question 96: CLF-C02-ET-Q096
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its on-premises infrastructure to the AWS Cloud.

Which advantage of cloud computing will help the company reduce upfront costs?

**Choices:**
- A) Go global in minutes
- B) Increase speed and agility
- C) Benefit from massive economies of scale
- D) Trade fixed expense for variable expense

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Trade fixed expense for variable expense - reduces upfront costs
---
D. Trade fixed expense for variable expense

</details>

---

## Question 97: CLF-C02-ET-Q097
**Domain 1:** Cloud Concepts  

**Question:**  
A company is designing workloads in the AWS Cloud. The company wants the workloads to perform their intended function correctly and consistently throughout their lifecycle.

Which pillar of the AWS Well-Architected Framework does this goal represent?

**Choices:**
- A) Operational excellence
- B) Security
- C) Reliability
- D) Performance efficiency

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Reliability - consistency
---
C. Reliability

</details>

---

## Question 98: CLF-C02-ET-Q098
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service supports a hybrid architecture that gives users the ability to extend AWS infrastructure, AWS services, APIs, and tools to data centers, co-location environments, or on-premises facilities?

**Choices:**
- A) AWS Snowmobile
- B) AWS Local Zones
- C) AWS Outposts
- D) AWS Fargate

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Snowmobile: AWS Snowmobile is a service designed for large-scale data transfers, not for extending AWS infrastructure to on-premises facilities.

 AWS Local Zones: AWS Local Zones are a type of AWS infrastructure deployment that places compute, storage, database, and other services closer to a specific geographic area, but they are not specifically designed for hybrid architectures.

 AWS Outposts: AWS Outposts is designed to bring native AWS services, infrastructure, and operating models to virtually any data center, co-location space, or on-premises facility.

 AWS Fargate: AWS Fargate is a serverless compute engine for containers and is not focused on hybrid architectures.
---
C. AWS Outposts

AWS Outposts enables you to run AWS infrastructure and services on premises while seamlessly connecting to the AWS cloud. This service extends the AWS ecosystem to your on-premises locations, allowing you to take advantage of cloud benefits while addressing the requirements of data residency, low-latency applications, and specific regulatory needs in hybrid environments.
---
Selected Answer: C
AWS Outposts is a fully managed service that extends AWS infrastructure, AWS services, APIs, and tools to on-premises data centers, co-location environments, or other facilities. It allows you to run AWS services on-premises, creating a hybrid environment where you can seamlessly run applications across on-premises and AWS infrastructur

</details>

---

## Question 99: CLF-C02-ET-Q099
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service is used to temporarily provide federated security credentials to access AWS resources?

**Choices:**
- A) Amazon GuardDuty
- B) AWS Simple Token Service (AWS STS)
- C) AWS Secrets Manager
- D) AWS Certificate Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The correct answer is:

B. AWS Simple Token Service (AWS STS)

AWS STS (Security Token Service) is used to provide temporary, limited-privilege security credentials for accessing AWS resources. These credentials are often used in federated scenarios, where users authenticate through an external identity provider (e.g., Active Directory, SAML, or social identity providers) and are granted temporary access to AWS resources.

The other options are not designed for this purpose:

A. Amazon GuardDuty: A threat detection service that monitors for malicious activity and unauthorized behavior.

C. AWS Secrets Manager: Used to securely store and manage secrets such as database credentials, API keys, and other sensitive information.

D. AWS Certificate Manager: Used to provision, manage, and deploy SSL/TLS certificates for use with AWS services.
---
Answer is B. since C. assists with using and storing of secrets with AWS services and applications
---
B. AWS Security Token Service (AWS STS)

</details>

---

## Question 100: CLF-C02-ET-Q100
**Domain 3:** Cloud Technology and Services  

**Question:**  
What is a benefit of using an Elastic Load Balancing (ELB) load balancer with applications running in the AWS Cloud?

**Choices:**
- A) An ELB will automatically scale resources to meet capacity needs.
- B) An ELB can balance traffic across multiple compute resources.
- C) An ELB can span multiple AWS Regions.
- D) An ELB can balance traffic between multiple internet gateways.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs)
---
B. An ELB can balance traffic across multiple compute resources.

</details>

---

## Question 101: CLF-C02-ET-Q101
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to convert video files and audio files to a format that will play on smartphones.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Comprehend
- B) Amazon Rekognition
- C) Amazon Elastic Transcoder
- D) Amazon Polly

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Elastic Transcoder : Convert media files in S3 storage into consumer
friendly formats.
---
Selected Answer: C
Answer is C
---
Selected Answer: C
https://aws.amazon.com/elastictranscoder/#:~:text=Amazon%20Elastic%20Transcoder%20is%20media,like%20smartphones%2C%20tablets%20and%20PCs.

</details>

---

## Question 102: CLF-C02-ET-Q102
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to securely store Amazon RDS database credentials and automatically rotate user passwords periodically.

Which AWS service or capability will meet these requirements?

**Choices:**
- A) Amazon S3
- B) AWS Systems Manager Parameter Store
- C) AWS Secrets Manager
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Answer is C.
Here's why:
Systems Manager Parameter Store - designed to cater to a wider use case, not just secrets or passwords, but also application configuration variables like URLs, Custom settings, AMI IDs, License keys, etc.
---
C. AWS Secrets Manager

AWS Secrets Manager is designed for securely storing and managing sensitive information, such as database credentials. It also supports automatic rotation of secrets, including database passwords, which helps to maintain security and compliance by regularly updating credentials without manual intervention.

</details>

---

## Question 103: CLF-C02-ET-Q103
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to have the ability to set up infrastructure for new applications in minutes.

Which advantage of cloud computing will help the company meet this requirement?

**Choices:**
- A) Trade fixed expense for variable expense
- B) Go global in minutes
- C) Increase speed and agility
- D) Stop guessing capacity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. Increase speed and agility

</details>

---

## Question 104: CLF-C02-ET-Q104
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs a managed NFS file system that the company can use with its AWS compute resources.

Which AWS service or feature will meet these requirements?

**Choices:**
- A) Amazon Elastic Block Store (Amazon EBS)
- B) AWS Storage Gateway Tape Gateway
- C) Amazon S3 Glacier Flexible Retrieval
- D) Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Amazon Elastic File System (Amazon EFS)

</details>

---

## Question 105: CLF-C02-ET-Q105
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to migrate to the AWS Cloud. The company wants to gather information about its on-premises data center.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS Application Discovery Service
- B) AWS DataSync
- C) AWS Storage Gateway
- D) AWS Database Migration Service (AWS DMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Application Discovery Service: AWS Application Discovery Service helps you plan your migration to the AWS cloud by collecting usage and configuration data about your on-premises servers and databases.
---
Selected Answer: A
A. AWS Application Discovery Service
---
A. AWS Application Discovery Service

</details>

---

## Question 106: CLF-C02-ET-Q106
**Domain 2:** Security and Compliance  

**Question:**  
Which tasks are responsibilities of the customer, according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Secure the virtualization layer.
- B) Encrypt data and maintain data integrity.
- C) Patch the Amazon RDS operating system.
- D) Maintain identity and access management controls.
- E) Secure Availability Zones.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B & D are responsibilities of the customer.
---
B. Encrypt data and maintain data integrity.

D. Maintain identity and access management controls.

</details>

---

## Question 107: CLF-C02-ET-Q107
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
An online retail company wants to migrate its on-premises workload to AWS. The company needs to automatically handle a seasonal workload increase in a cost-effective manner.

Which AWS Cloud features will help the company meet this requirement? (Choose two.)

**Choices:**
- A) Cross-Region workload deployment
- B) Pay-as-you-go pricing
- C) Built-in AWS CloudTrail audit capabilities
- D) Auto Scaling policies
- E) Centralized logging

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B & D are the best options
---
B. Pay-as-you-go pricing

D. Auto Scaling policies

</details>

---

## Question 108: CLF-C02-ET-Q108
**Domain 3:** Cloud Technology and Services  

**Question:**  
A developer needs to use a standardized template to create copies of a company's AWS architecture for development, test, and production environments.

Which AWS service should the developer use to meet this requirement?

**Choices:**
- A) AWS Cloud Map
- B) AWS CloudFormation
- C) Amazon Cloud Front
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Keyword: Template, development, test, and production environments
---
Selected Answer: B
B. AWS CloudFormation

</details>

---

## Question 109: CLF-C02-ET-Q109
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can run a managed PostgreSQL database that provides online transaction processing (OLTP)?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon Athena
- C) Amazon RDS
- D) Amazon EMR

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon DynamoDB: Amazon DynamoDB is a fully managed NoSQL database service and is not specifically designed for PostgreSQL databases.

 Amazon Athena: Amazon Athena is an interactive query service that allows you to analyze data in Amazon S3 using standard SQL. It is not designed for managing PostgreSQL databases.

 Amazon RDS: Amazon RDS (Relational Database Service) provides managed database services, including PostgreSQL. It is suitable for online transaction processing (OLTP) workloads.

 Amazon EMR: Amazon EMR (Elastic MapReduce) is a cloud-based big data platform that uses Apache Hadoop and other open-source frameworks. It is not designed for managing PostgreSQL databases.
---
C. Amazon RDS (Relational Database Service)

Amazon RDS supports various database engines, including PostgreSQL, and offers a managed database service suitable for OLTP workloads. With Amazon RDS for PostgreSQL, you can easily set up, operate, and scale a PostgreSQL database without the administrative overhead of managing the infrastructure.
---
Selected Answer: C
mazon RDS (Relational Database Service) is a managed database service that supports multiple database engines, including PostgreSQL. It provides an easy-to-use, fully managed solution for setting up, operating, and scaling relational databases in the cloud. Amazon RDS can be used for Online Transaction Processing (OLTP), which involves handling transactional workloads such as financial systems, e-commerce websites, and customer relationship management (CRM) systems

</details>

---

## Question 110: CLF-C02-ET-Q110
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can create a private network connection from on premises to the AWS Cloud?

**Choices:**
- A) AWS Config
- B) Virtual Private Cloud (Amazon VPC)
- C) AWS Direct Connect
- D) Amazon Route 53

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Direct Connect: Private dedicated connection between on premises and AWS
---
Selected Answer: C
C. AWS Direct Connect
---
C. AWS Direct Connect

</details>

---

## Question 111: CLF-C02-ET-Q111
**Domain 2:** Security and Compliance  

**Question:**  
Under the AWS shared responsibility model, which of the following is a responsibility of the customer?

**Choices:**
- A) Shred disk drives before they leave a data center.
- B) Prevent customers from gathering packets or collecting traffic at the hypervisor level.
- C) Patch the guest operating system with the latest security patches.
- D) Maintain security systems that provide physical monitoring of data centers.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Patch the guest operating system with the latest security patches.
---
C. Patch the guest operating system with the latest security patches.

</details>

---

## Question 112: CLF-C02-ET-Q112
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service uses speech-to-text conversion to help users create meeting notes?

**Choices:**
- A) Amazon Polly
- B) Amazon Textract
- C) Amazon Rekognition
- D) Amazon Transcribe

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon Transcribe: Makes it easy for developers to add speech to text capabilities to their
applications.
---
Selected Answer: D
D. Amazon Transcribe
---
D. Amazon Transcribe

</details>

---

## Question 113: CLF-C02-ET-Q113
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool provides users with a graphical interface that they can use to manage AWS services?

**Choices:**
- A) AWS Copilot
- B) AWS CLI
- C) AWS Management Console
- D) AWS software development kits (SDKs)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Management Console
---
C. AWS Management Console

</details>

---

## Question 114: CLF-C02-ET-Q114
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a workload that will run continuously for 1 year. The workload cannot tolerate service interruptions.

Which Amazon EC2 purchasing option will be MOST cost-effective?

**Choices:**
- A) All Upfront Reserved Instances
- B) Partial Upfront Reserved Instances
- C) Dedicated Instances
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. All Upfront Reserved Instances - results in lowest cost
---
A. All Upfront Reserved Instances

</details>

---

## Question 115: CLF-C02-ET-Q115
**Domain 2:** Security and Compliance  

**Question:**  
A company migrated its systems to the AWS Cloud. The systems are rightsized, and a security review did not reveal any issues. The company must ensure that additional developments, integrations, changes, and system usage growth do not jeopardize this optimized AWS infrastructure.

Which AWS service should the company use to report ongoing optimization and security?

**Choices:**
- A) AWS Trusted Advisor
- B) AWS Health Dashboard
- C) Amazon Connect
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Trusted Advisor
---
A. Helps to build trust with the company by inspecting the AWS environment and providing recommendations when it detects opportunities.

</details>

---

## Question 116: CLF-C02-ET-Q116
**Domain 2:** Security and Compliance  

**Question:**  
A systems administrator created a new IAM user for a developer and assigned the user an access key instead of a user name and password. What is the access key used for?

**Choices:**
- A) To access the AWS account as the AWS account root user
- B) To access the AWS account through the AWS Management Console
- C) To access the AWS account through a CLI
- D) To access all of a company’s AWS accounts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C is correct 
"Use Access Keys for Programmatic Access (CLI / SDK)"
---
Selected Answer: C
An access key consists of an Access Key ID and a Secret Access Key. It is used to programmatically interact with AWS services via the AWS Command Line Interface (CLI), AWS SDKs, or API calls. Access keys are not used for logging into the AWS Management Console.
---
secret key 
access key is for CLI if you ever solved labs assignment 
C is the answer

</details>

---

## Question 117: CLF-C02-ET-Q117
**Domain 3:** Cloud Technology and Services  

**Question:**  
A global company wants to migrate its third-party applications to the AWS Cloud. The company wants help from a global team of experts to complete the migration faster and more reliably in accordance with AWS internal best practices.
Which AWS service or resource will meet these requirements?

**Choices:**
- A) AWS Support
- B) AWS Professional Services
- C) AWS Launch Wizard
- D) AWS Managed Services (AMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. AWS Support: Provides technical support plans, but not focused on hands-on migration assistance.

B. AWS Professional Services: Global team of experts for hands-on assistance with planning, executing, and optimizing AWS migrations.

C. AWS Launch Wizard: Simplifies application deployment, but not specifically designed for third-party application migrations.

D. AWS Managed Services (AMS): Fully managed service for ongoing operational support, not designed for the initial migration phase.

In summary, option B (AWS Professional Services) is the best choice for hands-on assistance with third-party application migrations.
---
Selected Answer: B
The Correct answer is B.

The AWS Professional Services organization is a global team of experts that can help you realize your desired business outcomes when using the AWS Cloud. We work together with your team and your chosen member of the AWS Partner Network (APN) to execute your enterprise cloud computing initiatives.
https://aws.amazon.com/professional-services/
---
Selected Answer: B
AWS ProServe helps with complex migrations, including third-party applications, by offering best-practice guidance and expert assistance.

</details>

---

## Question 118: CLF-C02-ET-Q118
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is an environment that consists of one or more data centers?

**Choices:**
- A) Amazon CloudFront
- B) Availability Zone
- C) VPC
- D) AWS Outposts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (93%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A: Amazon CloudFront accelerates the delivery of static and dynamic content, including images and videos, to users globally.
B: Availability Zone is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region.
C: Amazon VPC: A service that lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources..
D: AWS Outposts is designed to bring native AWS services, infrastructure, and operating models to virtually any data center, its not a collection of data centers.
---
Selected Answer: B
B. Availability Zone
---
Selected Answer: B
B, no doubt.

</details>

---

## Question 119: CLF-C02-ET-Q119
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is moving an on-premises data center to the AWS Cloud. The company must migrate 50 petabytes of file storage data to AWS with the least possible operational overhead.

Which AWS service or resource should the company use to meet these requirements?

**Choices:**
- A) AWS Snowmobile
- B) AWS Snowball Edge
- C) AWS Data Exchange
- D) AWS Database Migration Service (AWS DMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (88%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Snowmobile is the appropriate choice for migrating 50 petabytes of file storage data to AWS with the least possible operational overhead. Snowmobile is a data transfer service that physically transports massive amounts of data to the AWS Cloud. It is a secure and efficient solution for extremely large data transfers.
---
Selected Answer: A
A. AWS Snowmobile is specifically designed for transferring large-scale data (up to 100 petabytes) from on-premises data centers to AWS. It is a physical data transport solution where a secure truck (essentially a data center on wheels) is used to transport massive amounts of data. This method minimizes operational overhead and is highly efficient for very large data migrations like the 50 petabytes mentioned.

Other Options:
B. AWS Snowball Edge: While AWS Snowball Edge is suitable for transferring large amounts of data (up to tens of terabytes per device), it would require hundreds of devices to transfer 50 petabytes, resulting in significantly more operational overhead compared to Snowmobile.
---
Selected Answer: A
Snow edge is in TBs where as snow mobile is in PB

</details>

---

## Question 120: CLF-C02-ET-Q120
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company has an application with robust hardware requirements. The application must be accessed by students who are using lightweight, low-cost laptops.

Which AWS service will help the company deploy the application without investing in backend infrastructure or high-end client hardware?

**Choices:**
- A) Amazon AppStream 2.0
- B) AWS AppSync
- C) Amazon WorkLink
- D) AWS Elastic Beanstalk

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `79%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (79%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A: Amazon AppStream 2.0 allows you to stream desktop applications from AWS to any device, without requiring high-end client hardware.
B: AWS AppSync is a managed service that simplifies application development by creating a flexible API to securely access, manipulate, and combine data from one or more data sources
C: Amazon WorkLink is a service that provides secure, easy mobile access to internal websites and applications.
D: AWS Elastic AWS Elastic Beanstalk – Used to deploy and manage applications.
---
Selected Answer: A
A. Amazon AppStream 2.0

Amazon AppStream 2.0 is a fully managed application streaming service that allows you to run resource-intensive applications on virtual machines in the cloud and stream them to end users. This service is ideal for situations where users have lightweight or low-cost devices (like laptops) but need access to applications that require robust hardware resources.
---
Selected Answer: A
"lightweight, low-cost laptops" means that they can only use web browsers to run the application, which is a software-as-a-service.

</details>

---

## Question 121: CLF-C02-ET-Q121
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service integrates with other AWS services to provide the ability to encrypt data at rest?

**Choices:**
- A) AWS Key Management Service (AWS KMS)
- B) AWS Certificate Manager (ACM)
- C) AWS Identity and Access Management (IAM)
- D) AWS Security Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
KMS = at rest
Certificates = in transit
---
Selected Answer: A
A. AWS Key Management Service (AWS KMS)
---
A. AWS Key Management Service (AWS KMS)

</details>

---

## Question 122: CLF-C02-ET-Q122
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to track the monthly cost and usage of all Amazon EC2 instances in a specific AWS environment.

Which AWS service or tool will meet these requirements?

**Choices:**
- A) AWS Cost Anomaly Detection
- B) AWS Budgets
- C) AWS Compute Optimizer
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The correct answer is:

B. AWS Budgets

AWS Budgets allows you to track your monthly costs and usage for AWS services, including Amazon EC2 instances. You can set custom budgets to monitor your spending and usage, and receive alerts when you exceed or are forecasted to exceed your budgeted thresholds.
---
AWS Budgets gives you access to a number of filtering dimensions (i.e., AWS Service, Availability Zone, and Member Account), and allows you to create budgets that are tracked on a monthly, quarterly, or yearly cadence.

Meanwhile, AWS Cost Anomaly Detection allows you to define the spend segments you want to evaluate, e.g. individual AWS services, member account, cost allocation tags, cost categories, and define your alert preferences
---
B. AWS Budgets

</details>

---

## Question 123: CLF-C02-ET-Q123
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants the ability to automatically acquire resources as needed and release the resources when they are no longer needed.

Which cloud concept describes this functionality?

**Choices:**
- A) Availability
- B) Elasticity
- C) Durability
- D) Reliability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Elasticity is “The ability to acquire resources as you need them and release resources when you no longer need them
---
B. Elasticity.

</details>

---

## Question 124: CLF-C02-ET-Q124
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a cost-effective option when running its applications in an Amazon EC2 instance for short time periods. The applications can be interrupted.

Which EC2 instance type will meet these requirements?

**Choices:**
- A) Spot Instances
- B) On-Demand Instances
- C) Reserved Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. Spot Instances

</details>

---

## Question 125: CLF-C02-ET-Q125
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to provide managed Windows virtual desktops and applications to its remote employees over secure network connections.
Which AWS services can the company use to meet these requirements? (Choose two.)

**Choices:**
- A) Amazon Connect
- B) Amazon AppStream 2.0
- C) Amazon WorkSpaces
- D) AWS Site-to-Site VPN
- E) Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `66%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (66%). Contributor Answer: BC.

Community Rationale & Discussion:
B. Amazon AppStream 2.0: Amazon AppStream 2.0 is a service that enables you to stream desktop applications to users through web browsers. You can deliver Windows applications securely to remote users without the need to provision and manage full virtual desktops.

C. Amazon WorkSpaces: Amazon WorkSpaces is a fully managed desktop-as-a-service (DaaS) solution that provides Windows desktops to users. You can configure and manage virtual desktops for remote employees using WorkSpaces.
---
Selected Answer: BC
Amazon Connect: A cloud-based contact center service and is not designed for providing managed Windows virtual desktops.

 Amazon AppStream 2.0: A fully managed application streaming service that allows you to securely deliver desktop applications to users. It is suitable for providing managed Windows virtual desktops and applications.

 Amazon WorkSpaces: A fully managed desktop computing service that provides virtual Windows desktops to users. It allows remote employees to access Windows desktops and applications securely.

 AWS Site-to-Site VPN: A networking service for securely connecting on-premises networks to AWS, and it is not directly related to providing managed Windows virtual desktops.

 Amazon Elastic Container Service (Amazon ECS): A container orchestration service and is not designed for providing managed Windows virtual desktops.
---
Selected Answer: BC
Los servicios de AWS que pueden usarse para proporcionar escritorios virtuales y aplicaciones administradas para empleados remotos con conexiones seguras son:

B. Amazon AppStream 2.0 → Permite la transmisión segura de aplicaciones de Windows y escritorios virtuales sin necesidad de instalación local.
 C. Amazon WorkSpaces → Proporciona escritorios virtuales totalmente administrados y seguros en la nube, con soporte para Windows y Linux.

</details>

---

## Question 126: CLF-C02-ET-Q126
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company has an AWS Business Support plan. The company needs to gain access to the AWS DDoS Response Team (DRT) to help mitigate DDoS events.

Which AWS service or resource must the company use to meet these requirements?

**Choices:**
- A) AWS Shield Standard
- B) AWS Enterprise Support
- C) AWS WAF
- D) AWS Shield Advanced

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. AWS Shield Advanced

</details>

---

## Question 127: CLF-C02-ET-Q127
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool provides a visualization of historical AWS spending patterns and projections of future AWS costs?

**Choices:**
- A) AWS Cost and Usage Report
- B) AWS Budgets
- C) Cost Explorer
- D) Amazon Cloud Watch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. Cost Explorer

</details>

---

## Question 128: CLF-C02-ET-Q128
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is migrating to the AWS Cloud instead of running its infrastructure on premises.

Which of the following are advantages of this migration? (Choose two.)

**Choices:**
- A) Elimination of the need to perform security auditing
- B) Increased global reach and agility
- C) Ability to deploy globally in minutes
- D) Elimination of the cost of IT staff members
- E) Redundancy by default for all compute services

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
B. Increased global reach and agility
C. Ability to deploy globally in minutes

</details>

---

## Question 129: CLF-C02-ET-Q129
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS service uses edge locations to cache content?

**Choices:**
- A) Amazon Kinesis
- B) Amazon Simple Queue Service (Amazon SQS)
- C) Amazon CloudFront
- D) Amazon Route 53

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon CloudFront = edge locations
---
C. Amazon CloudFront.

</details>

---

## Question 130: CLF-C02-ET-Q130
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to securely access an Amazon S3 bucket from an Amazon EC2 instance without accessing the internet.

What should the company use to accomplish this goal?

**Choices:**
- A) VPN connection
- B) Internet gateway
- C) VPC endpoint
- D) NAT gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. VPC endpoint
---
C. VPC endpoint is a powerful cloud virtual device used in Amazon VPC to enable communication between instances, without any need for internet connectivity.
---
C. VPC endpoint

</details>

---

## Question 131: CLF-C02-ET-Q131
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants an AWS service that can automate software deployment in Amazon EC2 instances and on-premises instances.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS CodeCommit
- B) AWS CodeBuild
- C) AWS CodeDeploy
- D) AWS CodePipeline

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS CodeDeploy: Automates code deployments to any instance, including EC2 instances and instances running on premises
---
Answer is C.
Here's why:
AWS CodeCommit - is a fully managed source control service that hosts private Git repositories without having to manage scaling its infrastructure.
AWS CodeBuild - is used for compiling your source code, runs unit tests, and produces artifacts that are ready for deployment.
AWS CodePipeline - is a fully managed, continuous delivery service used for releasing pipelines for fast and reliable application and infrastructure updates.
---
C. AWS CodeDeploy.

</details>

---

## Question 132: CLF-C02-ET-Q132
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS services are serverless? (Choose two.)

**Choices:**
- A) AWS Fargate
- B) Amazon Managed Streaming for Apache Kafka
- C) Amazon EMR
- D) Amazon S3
- E) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
A& D. Fargate and S3 are serverless.
---
S3 or Simple Storage Service is classified as a cloud storage service which forms a functional base for all serverless solutions without having to configure any OS or management of any underlying infrastructure.
---
A. AWS Fargate and D. Amazon S3.

</details>

---

## Question 133: CLF-C02-ET-Q133
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to continuously improve processes and procedures to deliver business value.

Which pillar of the AWS Well-Architected Framework does this goal represent?

**Choices:**
- A) Performance efficiency
- B) Operational excellence
- C) Reliability
- D) Sustainability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B. Operational excellence.
---
Selected Answer: B
business = operational

</details>

---

## Question 134: CLF-C02-ET-Q134
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following is a customer responsibility according to the AWS shared responsibility model?

**Choices:**
- A) Apply security patches for Amazon S3 infrastructure devices.
- B) Provide physical security for AWS datacenters.
- C) Install operating system updates on Lambda@Edge.
- D) Implement multi-factor authentication (MFA) for IAM user accounts.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Implement multi-factor authentication (MFA) for IAM user accounts.

</details>

---

## Question 135: CLF-C02-ET-Q135
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service should a company use to organize, characterize, and search large numbers of images?

**Choices:**
- A) Amazon Transcribe
- B) Amazon Rekognition
- C) Amazon Aurora
- D) Amazon QuickSight

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Rekognition = images
---
B. Amazon Rekognition

</details>

---

## Question 136: CLF-C02-ET-Q136
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to monitor for misconfigured security groups that are allowing unrestricted access to specific ports.
Which AWS service will meet this requirement?

**Choices:**
- A) AWS Trusted Advisor
- B) Amazon CloudWatch
- C) Amazon GuardDuty
- D) AWS Health Dashboard

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `74%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (74%). Contributor Answer: A.

Community Rationale & Discussion:
This question seems to go a little bit too far into the weeds for what this test is supposed to be. The AWS documentation specifically mentions TrustedAdvisor in the article about unrestricted security groups, but Trusted advisor isn't focused on security specifically like GuardDuty. However, GuardDuty doesn't focus on this issue specifically, either.

A. AWS Trusted Advisor: A service that provides best practices and recommendations for your AWS environment. It includes security checks, such as identifying security groups with unrestricted access.

B. Amazon CloudWatch: A monitoring service, and while it can provide insights into resource utilization and logs, it doesn't specifically focus on identifying misconfigured security groups.

C. Amazon GuardDuty: A threat detection service that continuously monitors for malicious activity and unauthorized behavior in AWS accounts. GuardDuty doesn't specifically perform configuration checks for security groups with unrestricted access.

D. AWS Health Dashboard: Provides information about the status of AWS services. It doesn't typically perform detailed security configuration checks.
---
Based on Chat GPT:

C. Amazon GuardDuty

Amazon GuardDuty is an AWS service that is designed to monitor and detect potential security threats in your AWS environment. It helps to identify unusual and unauthorized activities, including misconfigured security groups that may be allowing unrestricted access to specific ports. GuardDuty uses machine learning and threat intelligence to analyze data and generate alerts, making it an effective tool for enhancing the security of your AWS infrastructure.

While options like AWS Trusted Advisor and Amazon CloudWatch offer valuable monitoring capabilities, they do not specifically focus on detecting security group misconfigurations. Therefore, in this scenario, Amazon GuardDuty is the most appropriate choice.
---
Selected Answer: A
The correct answer is:

A. AWS Trusted Advisor

AWS Trusted Advisor provides real-time guidance to help provision your resources following AWS best practices. It includes a security check that identifies security groups with rules that allow unrestricted access (0.0.0.0/0) to specific ports, which could pose a security risk. This service helps you monitor and remediate misconfigured security groups.

Why not the others?
B. Amazon CloudWatch: CloudWatch is used for monitoring and observability, such as collecting logs, metrics, and setting alarms. It does not specifically identify misconfigured security groups.

C. Amazon GuardDuty: GuardDuty is a threat detection service that uses machine learning to identify malicious activity or unauthorized behavior. It does not focus on identifying misconfigured security groups.

D. AWS Health Dashboard: This service provides information about the health of AWS services and resources, but it does not monitor for misconfigured security groups.

</details>

---

## Question 137: CLF-C02-ET-Q137
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is always available free of charge to users?

**Choices:**
- A) Amazon Athena
- B) AWS Identity and Access Management (IAM)
- C) AWS Secrets Manager
- D) Amazon ElastiCache

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The correct answer is **B. AWS Identity and Access Management (IAM)**. AWS IAM is always available free of charge to users¹². It allows you to securely manage access to AWS services and resources for your users.

(1) Get started with the AWS Free Tier - How AWS Pricing Works. https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/get-started-with-the-aws-free-tier.html.
(2) Did You Know About AWS Always-Free Services - DEV Community. https://dev.to/aws-builders/did-you-know-about-aws-always-free-services-3lgk.
(3) Trying services using AWS Free Tier. https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html.
---
B. AWS Identity and Access Management (IAM)

</details>

---

## Question 138: CLF-C02-ET-Q138
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to run some of its workloads on premises to comply with regulatory guidelines. The company wants to use the AWS Cloud to run workloads that are not required to be on premises. The company also wants to be able to use the same API calls for the on-premises workloads and the cloud workloads.

Which AWS service or feature should the company use to meet these requirements?

**Choices:**
- A) Dedicated Hosts
- B) AWS Outposts
- C) Availability Zones
- D) AWS Wavelength

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Using AWS cloud on-prem = Outposts
---
B. AWS Outposts

</details>

---

## Question 139: CLF-C02-ET-Q139
**Domain 3:** Cloud Technology and Services  

**Question:**  
What is the recommended use case for Amazon EC2 On-Demand Instances?

**Choices:**
- A) A steady-state workload that requires a particular EC2 instance configuration for a long period of time
- B) A workload that can be interrupted for a project that requires the lowest possible cost
- C) An unpredictable workload that does not require a long-term commitment
- D) A workload that is expected to run for longer than 1 year

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Not B, On Demand is uninterrupted
---
Selected Answer: C
C. An unpredictable workload that does not require a long-term commitment
---
C. An unpredictable workload that does not require a long-term commitment

</details>

---

## Question 140: CLF-C02-ET-Q140
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use an AWS networking solution that can act as a centralized gateway between multiple VPCs and on-premises networks.

Which AWS service or feature will meet this requirement?

**Choices:**
- A) Gateway VPC endpoint
- B) AWS Direct Connect
- C) AWS Transit Gateway
- D) AWS PrivateLink

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Transit Gateway connects VPCs and on premises networks through a central hub and spoke (star) connection.
---
C. AWS Transit Gateway

</details>

---

## Question 141: CLF-C02-ET-Q141
**Domain 3:** Cloud Technology and Services  

**Question:**  
An administrator observed that multiple AWS resources were deleted yesterday.

Which AWS service will help identify the cause and determine which user deleted the resources?

**Choices:**
- A) AWS CloudTrail
- B) Amazon Inspector
- C) Amazon GuardDuty
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. AWS CloudTrail

AWS CloudTrail records API calls and events for your AWS account, including who performed actions, what actions were performed, and when. This makes it the most suitable service for tracking and auditing resource changes and deletions.
---
Selected Answer: A
AWS CloudTrail =audit + logs
B. Amazon Inspector = vulnability
C. Amazon GuardDuty = vairus+ malicious 
D. AWS Trusted Advisor = recomendations

</details>

---

## Question 142: CLF-C02-ET-Q142
**Domain 2:** Security and Compliance  

**Question:**  
To assist companies with Payment Card Industry Data Security Standard (PCI DSS) compliance in the cloud, AWS provides:

**Choices:**
- A) physical Inspections of data centers by appointment.
- B) required PCI compliance certifications for any application running on AWS.
- C) an AWS Attestation of Compliance (AOC) report for specific AWS services.
- D) professional PCI compliance services.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. Through AWS Artifact, The PCI DSS Attestation of Compliance (AOC) and Responsibility Summary is available to customers.
---
C. an AWS Attestation of Compliance (AOC) report for specific AWS services.

</details>

---

## Question 143: CLF-C02-ET-Q143
**Domain 2:** Security and Compliance  

**Question:**  
In which situations should a company create an IAM user instead of an IAM role?

**Choices:**
- A) When an application that runs on Amazon EC2 instances requires access to other AWS services
- B) When the company creates AWS access credentials for individuals
- C) When the company creates an application that runs on a mobile phone that makes requests to AWS
- D) When the company needs to add users to IAM groups
- E) When users are authenticated in the corporate network and want to be able to use AWS without having to sign in a second time

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `60%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (60%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: B
IAM Users are for people who access AWS through the Management Console or CLI/SDKs. D is a structural choice, not a reason to create an IAM user in the first place.
---
Selected Answer: D
Also D
---
Selected Answer: B
B. When the company creates AWS access credentials for individuals

</details>

---

## Question 144: CLF-C02-ET-Q144
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company hosts a web application on AWS. The company has improved the availability of its application by provisioning multiple Amazon EC2 instances. The company wants to distribute its traffic across the EC2 instances while providing a single point of contact to the web clients.

Which AWS service can distribute the traffic to multiple EC2 instances as targets?

**Choices:**
- A) VPC endpoints
- B) Application Load Balancer
- C) NAT gateway
- D) Internet gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B. Application Load Balancer
---
Selected Answer: B
keyword is distribute

</details>

---

## Question 145: CLF-C02-ET-Q145
**Domain 3:** Cloud Technology and Services  

**Question:**  
What is the total volume of data that can be stored in Amazon S3?

**Choices:**
- A) 10 PB
- B) 50 PB
- C) 100 PB
- D) Virtually unlimited

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon S3 offers virtually unlimited storage capacity, meaning there's no limit to the total volume of data you can store
---
D. Virtually unlimited

</details>

---

## Question 146: CLF-C02-ET-Q146
**Domain 1:** Cloud Concepts  

**Question:**  
Which design principle is related to the reliability pillar according to the AWS Well-Architected Framework?

**Choices:**
- A) Test recovery procedures
- B) Experiment more often
- C) Go global in minutes
- D) Analyze and attribute to expenditure

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. Test recovery procedures

</details>

---

## Question 147: CLF-C02-ET-Q147
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is a key-value database that provides sub-millisecond latency on a large scale?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon Aurora
- C) Amazon DocumentDB (with MongoDB compatibility)
- D) Amazon Neptune

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon DynamoDB: A key-value and document database that provides single-digit millisecond latency at any scale. It is a fully managed NoSQL database service designed for applications that require consistent, single-digit millisecond latency, regardless of the volume of requests.

B. Amazon Aurora: A MySQL and PostgreSQL-compatible relational database engine that offers high performance and availability. While it provides low-latency reads, it is not specifically designed as a key-value database.

C. Amazon DocumentDB (with MongoDB compatibility): A fully managed document database service that is compatible with MongoDB. It is designed for applications that work with JSON-like documents, and it provides the scalability and availability of a NoSQL database.

D. Amazon Neptune: A fully managed graph database service that supports graph models. It is designed for applications with highly connected data, and it is not specifically focused on providing sub-millisecond latency for key-value access.
---
Selected Answer: A
A. Amazon DynamoDB: A key-value and document database that provides single-digit millisecond latency at any scale. It is a fully managed NoSQL database service designed for applications that require consistent, single-digit millisecond latency, regardless of the volume of requests.
---
Selected Answer: A
Non relational databases are faster since they are simpler

</details>

---

## Question 148: CLF-C02-ET-Q148
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company stores data in an Amazon S3 bucket.

Which task is the responsibility of AWS?

**Choices:**
- A) Configure an S3 Lifecycle policy.
- B) Activate S3 Versioning.
- C) Configure S3 bucket policies.
- D) Protect the infrastructure that supports S3 storage.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Protect the infrastructure that supports S3 storage.

</details>

---

## Question 149: CLF-C02-ET-Q149
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to transfer a virtual Windows Server 2022 that is currently running in its own data center to AWS. The company wants to automatically convert the existing server to run directly on AWS infrastructure instead of visualized hardware.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS DataSync
- B) AWS Database Migration Service (AWS DMS)
- C) AWS Application Discovery Service
- D) AWS Application Migration Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Company wants to convert the data server to application based
---
Selected Answer: D
keyword=existing server to run

</details>

---

## Question 150: CLF-C02-ET-Q150
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is a fully managed NoSQL database service?

**Choices:**
- A) Amazon RDS
- B) Amazon Redshift
- C) Amazon DynamoDB
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. Amazon DynamoDB

</details>

---

## Question 151: CLF-C02-ET-Q151
**Domain 1:** Cloud Concepts  

**Question:**  
A company deployed an application in multiple AWS Regions around the world. The company wants to improve the application’s performance and availability.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Global Accelerator
- B) Amazon DataZone
- C) AWS Cloud Map
- D) AWS Auto Scaling

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Global Accelerator- Improve global application availability and performance
---
A. AWS Global Accelerator

</details>

---

## Question 152: CLF-C02-ET-Q152
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its on-premises SQL Server database to the AWS Cloud. The company wants AWS to handle the day-to-day administration of the database.

Which AWS service will meet the company's requirements?

**Choices:**
- A) Amazon EC2 for Microsoft SQL Server
- B) Amazon DynamoDB
- C) Amazon RDS
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon RDS. Though Aurora would be a better choice for relational databases to further reduce administration, it does not support SQL Server.
---
C. Amazon RDS

</details>

---

## Question 153: CLF-C02-ET-Q153
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs stateless network filtering for its VPC.

Which AWS service, tool, or feature will meet this requirement?

**Choices:**
- A) AWS PrivateLink
- B) Security group
- C) Network access control list (ACL)
- D) AWS WAF

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Network access control list (ACL): Stateless. You should explicitly allow return traffic.
---
C. Network access control list (ACL)

</details>

---

## Question 154: CLF-C02-ET-Q154
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is an advantage of AWS Cloud computing that minimizes variable costs?

**Choices:**
- A) High availability
- B) Economies of scale
- C) Global reach
- D) Agility

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Devil question
---
B. Economies of scale

</details>

---

## Question 155: CLF-C02-ET-Q155
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to migrate its server-based applications to the AWS Cloud. The company wants to determine the total cost of ownership for its compute resources that will be hosted on the AWS Cloud.

Which combination of AWS services or tools will meet these requirements? (Choose two.)

**Choices:**
- A) AWS Pricing Calculator
- B) Migration Evaluator
- C) AWS Support Center
- D) AWS Application Discovery Service
- E) AWS Database Migration Service (AWS DMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AB`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AB (100%). Contributor Answer: AB.

Community Rationale & Discussion:
Selected Answer: AB
To determine the total cost of ownership (TCO) for compute resources in AWS, use the AWS Pricing Calculator (for direct costs) and Migration Evaluator (for right-sizing, which is essential for accurate cost estimation)
---
Selected Answer: AB
A. AWS Pricing Calculator
B. Migration Evaluator
---
A. AWS Pricing Calculator
B. Migration Evaluator

</details>

---

## Question 156: CLF-C02-ET-Q156
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has data lakes designed for high performance computing (HPC) workloads.

Which Amazon EC2 instance type should the company use to meet these requirements?

**Choices:**
- A) General purpose instances
- B) Compute optimized instances
- C) Memory optimized instances
- D) Storage optimized instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (67%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Compute optimized all the way
---
Selected Answer: B
Compute optimized instances are specifically designed for compute-intensive tasks and are ideal for High-Performance Computing (HPC) workloads.
---
Selected Answer: B
Compute optimized instances are ideal for high performance computing (HPC) workloads because they are specifically designed to deliver high performance for compute-intensive applications.

</details>

---

## Question 157: CLF-C02-ET-Q157
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which benefits does a company gain when the company moves from on-premises IT architecture to the AWS Cloud? (Choose two.)

**Choices:**
- A) Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and procurement
- B) Elimination of the need for trained IT staff
- C) Automatic security configuration of all applications that are migrated to the cloud
- D) Elimination of the need for disaster recovery planning
- E) Faster deployment of new features and applications

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AE (100%). Contributor Answer: AE.

Community Rationale & Discussion:
A. Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and procurement
E. Faster deployment of new features and applications

</details>

---

## Question 158: CLF-C02-ET-Q158
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is deploying a machine learning (ML) research project that will require a lot of compute power over several months. The ML processing jobs do not need to run at specific times.
Which Amazon EC2 instance purchasing option will meet these requirements at the lowest cost?

**Choices:**
- A) On-Demand Instances
- B) Spot Instances
- C) Reserved Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Alright guys, I found this. Pretty sure it settles things.
https://naterar.medium.com/a-deep-dive-into-aws-instance-types-solving-high-cpu-workload-and-memory-spikes-57e8b5623777

Spot: Spot instances can be valuable for handling sporadic high CPU workloads and memory spikes. >>>However, the inherent uncertainty of availability makes them less reliable for consistent, high-demand workloads.<<<

On-Demand: provide the necessary computational horsepower exactly when needed, making them ideal for dealing with unexpected CPU and memory demands.

So, yeah, I'd say 'A'.
---
Selected Answer: B
A. On-Demand Instances: On-Demand Instances provide the highest level of flexibility and do not require any upfront commitment. On-Demand Instances are suitable for workloads with variable usage patterns, but they are generally more expensive than other purchasing options.

B. Spot Instances: Spot Instances are the most cost-effective option for scenarios where the workload is flexible and can be interrupted. Spot Instances allow you to use spare EC2 capacity at a significantly lower cost than On-Demand Instances. Spot Instances are suitable for workloads like batch processing, data analysis, and machine learning jobs that do not require continuous, uninterrupted operation

C. Reserved Instances: Reserved Instances involve a commitment to a specific instance type in a particular region for a term of 1 or 3 years. In exchange for this commitment, users receive a significant discount compared to On-Demand Instances. 

D. Dedicated Instances: Dedicated Instances are instances that run on hardware dedicated to a single customer. They are typically used in scenarios where compliance or regulatory requirements mandate dedicated hardware.
---
Selected Answer: A
The problem statement doesn't specify the runtime duration, but it also doesn't mention that interruptions are allowed. Therefore, if we choose a spot instance and a spot instance machine goes down while the program is running, it is likely to impact the process. Hence, opting for an on-demand instance would probably be more suitable.

</details>

---

## Question 159: CLF-C02-ET-Q159
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate to the AWS Cloud. The company is conducting organizational transformation and wants to become more responsive to customer inquiries and feedback.

Which task should the company perform to meet these requirements, according to the AWS Cloud Adoption Framework (AWS CAF)? (Choose two.)

**Choices:**
- A) Realign teams to focus on products and value streams.
- B) Create new value propositions with new products and services.
- C) Use agile methods to rapidly iterate and evolve.
- D) Use a new data and analytics platform to create actionable insights.
- E) Migrate and modernize legacy infrastructure.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
A Realign teams to focus on products and value streams: This helps ensure that teams are structured around delivering value to customers, making the organization more agile and customer-centric.
C Use agile methods to rapidly iterate and evolve: Agile methodologies enable the company to quickly respond to customer feedback and continuously improve their products and services¹².

(1) AWS Cloud Adoption Framework (AWS CAF) - aws.amazon.com. https://aws.amazon.com/cloud-adoption-framework/.
(2) What is a Cloud Adoption Framework? - CAF Explained - AWS. https://aws.amazon.com/what-is/cloud-adoption-framework/.
(3) An Overview of the AWS Cloud Adoption Framework. https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html.
---
B. is about the business side of things, so answers are A. and C. as agile is about rapid releases of software for customer feedback.
---
A. Realign teams to focus on products and value streams.
C. Use agile methods to rapidly iterate and evolve.

</details>

---

## Question 160: CLF-C02-ET-Q160
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company that is planning to migrate to the AWS Cloud is based in an isolated area that has limited internet connectivity. The company needs to perform local data processing on premises. The company needs a solution that can operate without a stable internet connection.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon S3
- B) AWS Snowball Edge
- C) AWS Storage Gateway
- D) AWS Backup

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Snowball Edge
---
B. AWS Snowball Edge

</details>

---

## Question 161: CLF-C02-ET-Q161
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to build graph queries for real-time fraud pattern detection.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Neptune
- B) Amazon DynamoDB
- C) Amazon Timestream
- D) Amazon Forecast

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Neptune is Fully Managed NoSQL
graph database that can store, map and query
relationships between data sets.
---
Selected Answer: A
A. Amazon Neptune
---
A. Amazon Neptune

</details>

---

## Question 162: CLF-C02-ET-Q162
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate to the AWS Cloud. The company needs the ability to acquire resources when the resources are necessary. The company also needs the ability to release those resources when the resources are no longer necessary.

Which architecture concept of the AWS Cloud meets these requirements?

**Choices:**
- A) Elasticity
- B) Availability
- C) Reliability
- D) Durability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Elasticity
---
elasticity is the concept that aligns with the requirement to acquire and release resources based on necessity.

</details>

---

## Question 163: CLF-C02-ET-Q163
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to deploy a web application as a containerized application. The company wants to use a managed service that can automatically create container images from source code and deploy the containerized application.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Elastic Beanstalk
- B) Amazon Elastic Container Service (Amazon ECS)
- C) AWS App Runner
- D) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (75%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS App Runner is a fully managed container application service that simplifies deploying and running web applications and API services on AWS without needing to manage infrastructure or container orchestration.
---
Selected Answer: C
C. is the correct answer
AWS App Runner is a fully managed service that allows developers to deploy containerized applications directly from source code or container images without managing the underlying infrastructure. It provides:

Automatic container image creation from source code (such as Git repositories).
Automatic scaling and load balancing.
Simplified deployment process for web applications.
---
Selected Answer: B
B is the correct answer

B : Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you to more efficiently deploy, manage, and scale containerized applications. It deeply integrates with the AWS environment to provide an easy-to-use solution for running container workloads in the cloud and on premises with advanced security features using Amazon ECS Anywhere.

C: AWS App Runner builds and deploys web applications automatically, load balances traffic with encryption, scales to meet your traffic needs, and allows for the configuration of how services are accessed and communicate with other AWS applications in a private Amazon VPC

</details>

---

## Question 164: CLF-C02-ET-Q164
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company has moved all its infrastructure to the AWS Cloud. To plan ahead for each quarter, the finance team wants to track the cost and usage data of all resources from previous months. The finance team wants to automatically generate reports that contains the data.

Which AWS service or feature should the finance team use to meet these requirements?

**Choices:**
- A) Amazon Detective
- B) AWS Pricing Calculator
- C) AWS Budgets
- D) AWS Savings Plans

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Budgets - generate reports for historical usage and costs
---
C. AWS Budgets

</details>

---

## Question 165: CLF-C02-ET-Q165
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud Adoption Framework (AWS CAF) perspective focuses on real-time insights and answers questions about strategy?

**Choices:**
- A) Operations
- B) People
- C) Business
- D) Platform

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Business
---
C. Business

</details>

---

## Question 166: CLF-C02-ET-Q166
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to migrate critical on-premises production systems to Amazon EC2 instances. The production instances will be used for at least 3 years. The company wants a pricing option that will minimize cost.

Which solution will meet these requirements?

**Choices:**
- A) On-Demand Instances
- B) Reserved Instances
- C) Spot Instances
- D) AWS Free Tier

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B. Reserved Instances

</details>

---

## Question 167: CLF-C02-ET-Q167
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS Well-Architected Framework concept represents a system's ability to remain functional when the system encounters operational problems?

**Choices:**
- A) Consistency
- B) Elasticity
- C) Durability
- D) Latency

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. Durability

</details>

---

## Question 168: CLF-C02-ET-Q168
**Domain 1:** Cloud Concepts  

**Question:**  
Which pillar of the AWS Well-Architected Framework focuses on the ability to recover automatically from service interruptions?

**Choices:**
- A) Security
- B) Performance efficiency
- C) Operational excellence
- D) Reliability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Automatically recover from failure --> Reliability
---
D. Reliability

</details>

---

## Question 169: CLF-C02-ET-Q169
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS services or features provide disaster recovery solutions for Amazon EC2 instances? (Choose two.)

**Choices:**
- A) EC2 Reserved Instances
- B) EC2 Amazon Machine Images (AMIs)
- C) Amazon Elastic Block Store (Amazon EBS) snapshots
- D) AWS Shield
- E) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
B. EC2 Amazon Machine Images (AMIs): AMIs are used to create backups of EC2 instances, and they can be used to launch replacement instances in the event of a disaster or data loss. AMIs are essential for creating recovery points for your EC2 instances.

C. Amazon Elastic Block Store (Amazon EBS) snapshots: EBS snapshots allow you to create point-in-time backups of your EBS volumes. These snapshots can be used to restore data or create new EBS volumes, making them a key component of disaster recovery for EC2 instances.
---
Selected Answer: BC
B. EC2 Amazon Machine Images (AMIs): Creating AMIs is a common practice for disaster recovery. AMIs allow you to capture the configuration, data, and permissions of your EC2 instances. In the event of a failure, you can launch new instances from the saved AMIs to quickly recover.

C. Amazon Elastic Block Store (Amazon EBS) snapshots: Enable you to create point-in-time copies of your EBS volumes. Snapshots are often used as part of a disaster recovery strategy, allowing you to restore volumes or create new volumes in case of data loss or instance failure.

EC2 Reserved Instances (Option A) are a billing discount model for reserved capacity, and they are not inherently designed for disaster recovery.

AWS Shield (Option D) is a managed Distributed Denial of Service (DDoS) protection service, and Amazon GuardDuty (Option E) is a threat detection service. While they contribute to overall security, they are not specific disaster recovery solutions for EC2 instances
---
Selected Answer: BC
B. EC2 Amazon Machine Images (AMIs)
C. Amazon Elastic Block Store (Amazon EBS) snapshots

</details>

---

## Question 170: CLF-C02-ET-Q170
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company has multiple SQL-based databases located in a data center. The company needs to migrate all database servers to the AWS Cloud to reduce the cost of operating physical servers.

Which AWS service or resource will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Amazon EC2 instances
- B) Amazon RDS
- C) Amazon DynamoDB
- D) OpenSearch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Amazon RDS is the best choice for migrating SQL-based databases with the least operational overhead.

</details>

---

## Question 171: CLF-C02-ET-Q171
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to query its server logs to gain insights about its customers’ experiences.

Which AWS service will store this data MOST cost-effectively?

**Choices:**
- A) Amazon Aurora
- B) Amazon Elastic File System (Amazon EFS)
- C) Amazon Elastic Block Store (Amazon EBS)
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
For cost-effective storage and querying of large volumes of data, especially log data, Amazon S3 (Simple Storage Service) is the most suitable option. Amazon S3 is an object storage service designed to store and retrieve any amount of data from anywhere on the web.
---
Selected Answer: D
D. Amazon S3
---
Selected Answer: D
D. Amazon S3

Explanation:

For cost-effective storage and querying of large volumes of data, especially log data, Amazon S3 (Simple Storage Service) is the most suitable option. Amazon S3 is an object storage service designed to store and retrieve any amount of data from anywhere on the web.

</details>

---

## Question 172: CLF-C02-ET-Q172
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is a recommended design principle for AWS Cloud architecture?

**Choices:**
- A) Design tightly coupled components.
- B) Build a single application component that can handle all the application functionality.
- C) Make large changes on fewer iterations to reduce chances of failure.
- D) Avoid monolithic architecture by segmenting workloads.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Avoid monolithic architecture
---
Selected Answer: D
D. Avoid monolithic architecture by segmenting workloads.

In AWS Cloud architecture, one of the key design principles is to avoid monolithic architectures and instead use a microservices or segmented approach for workloads. This promotes flexibility, scalability, and maintainability by breaking down applications into smaller, independent components. This makes it easier to deploy, scale, and manage applications, and it improves fault isolation.
---
Why not A?

</details>

---

## Question 173: CLF-C02-ET-Q173
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service helps users audit API activity across their AWS account?

**Choices:**
- A) AWS CloudTrail
- B) Amazon Inspector
- C) AWS WAF
- D) AWS Config

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS CloudTrail: A service that records API calls and related events for your AWS account.
B. Amazon Inspector is designed to help assess applications for vulnerabilities and deviations from best practices, but it does not audit API activity.
C. AWS WAF: Protects web applications from common web exploits
D. AWS Config - is used for assessing, auditing, and evaluating the configurations of your AWS resources. but it's more focused on resource configuration states rather than API activity monitoring.
---
Selected Answer: A
AWS Cloudtrail
---
Selected Answer: A
A. AWS CloudTrail

</details>

---

## Question 174: CLF-C02-ET-Q174
**Domain 2:** Security and Compliance  

**Question:**  
Which task is a customer’s responsibility, according to the AWS shared responsibility model?

**Choices:**
- A) Management of the guest operating systems
- B) Maintenance of the configuration of infrastructure devices
- C) Management of the host operating systems and virtualization
- D) Maintenance of the software that powers Availability Zones

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Management of the guest operating system
---
Selected Answer: A
The correct answer is: 
A. Management of the guest operating systems.

Explanation:
Under the AWS shared responsibility model, AWS is responsible for the security of the cloud (the infrastructure, hardware, and software that supports AWS services), while the customer is responsible for security in the cloud (the configuration and security of their own applications, data, and services).

The customer is responsible for managing their guest operating systems, which are the operating systems they install and manage on their EC2 instances. This includes ensuring the operating system is updated, patched, and secured.
---
A is the best

</details>

---

## Question 175: CLF-C02-ET-Q175
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to automatically add and remove Amazon EC2 instances. The company wants the EC2 instances to adjust to varying workloads dynamically.

Which service or feature will meet these requirements?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon EC2 Spot Instances
- C) AWS Snow Family
- D) Amazon EC2 Auto Scaling

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon EC2 Auto Scaling

Amazon EC2 Auto Scaling is a service that allows you to automatically adjust the number of Amazon EC2 instances in your application to meet changing demand. It can add or remove instances based on predefined conditions, ensuring that you have the right number of instances to handle varying workloads, while optimizing costs.
---
Auto scaling
---
Selected Answer: D
https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html

</details>

---

## Question 176: CLF-C02-ET-Q176
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to build, train, and deploy machine learning (ML) models.

Which AWS service can the company use to meet this requirement?

**Choices:**
- A) Amazon Personalize
- B) Amazon Comprehend
- C) Amazon Forecast
- D) Amazon SageMaker

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Ability to build, train, and deploy machine learning (ML) models quickly
.
---
Selected Answer: D
Amazon SageMaker is a fully managed service that provides every tool and workflow needed to build, train, and deploy machine learning (ML) models at scale.
---
Selected Answer: D
Amazon SageMaker is a fully managed machine learning service that provides tools and infrastructure to build, train, and deploy ML models at scale, including large foundation models for generative AI. It offers an integrated development environment with notebooks, debuggers, pipelines, MLOps capabilities, and human-in-the-loop tools. SageMaker supports responsible AI with governance controls and access to pretrained models.

</details>

---

## Question 177: CLF-C02-ET-Q177
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool provides recommendations to help users get rightsized Amazon EC2 instances based on historical workload usage data?

**Choices:**
- A) AWS Pricing Calculator
- B) AWS Compute Optimizer
- C) AWS App Runner
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Compute Optimizer is a service that analyzes your AWS resources' configuration and utilization metrics to provide you with rightsizing recommendations.
---
Selected Answer: B
AWS Compute Optimizer is a service that analyzes your AWS resources' configuration and utilization metrics to provide you with rightsizing recommendations. It reports whether your resources are optimal, and generates optimization recommendations to reduce the cost and improve the performance of your workloads. Compute Optimizer also provides graphs showing recent utilization metric history data, as well as projected utilization for recommendations, which you can use to evaluate which recommendation provides the best price-performance trade-off. The analysis and visualization of your usage patterns can help you decide when to move or resize your running resources, and still meet your performance and capacity requirements.
---
B. AWS Compute Optimizer

</details>

---

## Question 178: CLF-C02-ET-Q178
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to explore and analyze data in Amazon S3 by using a programming language.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Kendra
- B) Amazon Athena
- C) Amazon Comprehend
- D) Amazon SageMaker

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using
standard SQL
---
Selected Answer: B
B. Amazon Athena - an interactive query service that allows you to analyze data stored in Amazon S3 using standard SQL queries.
---
B. Amazon Athena

Explanation:
Amazon Athena is a fully managed service that enables you to explore and analyze data stored in Amazon S3 using SQL queries. Athena is serverless and allows you to use SQL directly on S3 data without needing to set up complex infrastructure, which makes it ideal for interactive analysis and data exploration.

</details>

---

## Question 179: CLF-C02-ET-Q179
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to run an application on Amazon EC2 instances without interruption.

Which EC2 instance purchasing option will meet this requirement MOST cost-effectively?

**Choices:**
- A) Standard Reserved Instances
- B) Convertible Reserved Instances
- C) On-Demand Instances
- D) Spot Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. Standard Reserved Instances

</details>

---

## Question 180: CLF-C02-ET-Q180
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a fully managed service that centralizes and automates data protection across AWS services and hybrid workloads.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Artifact
- B) AWS Backup
- C) AWS Batch
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Central data protection policy that works across AWS services for resources
Centralizes and automates data protection
---
AWS Backup is specifically designed for centralized, automated data protection across various AWS services and hybrid environments.

</details>

---

## Question 181: CLF-C02-ET-Q181
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to migrate its application from on premises to the AWS Cloud. The company needs to gather usage and configuration data for the application components.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Database Migration Service (AWS DMS)
- B) AWS Transfer Family
- C) AWS Application Discovery Service
- D) AWS Global Accelerator

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. AWS Application Discovery Service

AWS Application Discovery Service helps gather usage and configuration data for your application components. It assists in understanding the on-premises environment and helps plan the migration to the AWS Cloud by collecting data about your existing infrastructure, applications, and dependencies.

</details>

---

## Question 182: CLF-C02-ET-Q182
**Domain 1:** Cloud Concepts  

**Question:**  
Which design principle aligns with performance efficiency pillar of the AWS Well-Architected Framework?

**Choices:**
- A) Using serverless architectures
- B) Scaling horizontally
- C) Measuring the cost of workloads
- D) Using managed services

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `68%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (68%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Design Principles
• Democratize advanced technologies - Advance technologies become services
and hence you can focus more on product development
• Go global in minutes - Easy deployment in multiple regions
• Use serverless architectures - Avoid burden of managing servers
• Experiment more often - Easy to carry out comparative testing
• Mechanical sympathy - Be aware of all AWS services
---
Selected Answer: A
Both A & B are correct answers. Leaning more towards A since Scaling horizontally (Option B) is also crucial but is more about handling increased load efficiently rather than optimizing resource usage per se. Both are important, but serverless architectures can offer more direct benefits in terms of performance efficiency by automatically managing resource allocation.
---
Selected Answer: A
According https://aws.amazon.com/blogs/apn/the-6-pillars-of-the-aws-well-architected-framework correct answer is A because:
There are five design principles for performance efficiency in the cloud:
-Democratize advanced technologies
-Go global in minutes
-Use serverless architectures
-Experiment more often
-Consider mechanical sympathy

AND 
Scale horizontally to increase aggregate workload availability - is part of the principles for reliability in the cloud.

</details>

---

## Question 183: CLF-C02-ET-Q183
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to provide low latency to its users around the world.

Which feature of the AWS Cloud meet this requirement?

**Choices:**
- A) Global infrastructure
- B) Pay as-you-go pricing
- C) Managed services
- D) Economy of scale

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Global infrastructure is the key feature that allows AWS to provide low latency to users by placing resources and services closer to their geographic locations.

</details>

---

## Question 184: CLF-C02-ET-Q184
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which type of workload should a company run on Amazon EC2 Spot Instances?

**Choices:**
- A) A steady-state workload that requires a particular EC2 instance configuration for a long period of time
- B) A workload that can be interrupted and can control costs
- C) A steady-state workload that does not require a long-term commitment
- D) A workload that cannot be interrupted and can control costs

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Spot Instances – short workloads, cheap, can lose instances (less reliable)
---
Selected Answer: B
B. A workload that can be interrupted and can control costs
---
B. A workload that can be interrupted and can control costs

</details>

---

## Question 185: CLF-C02-ET-Q185
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides command line access to AWS tools and resources directly from a web browser?

**Choices:**
- A) AWS CloudHSM
- B) AWS CloudShell
- C) Amazon WorkSpaces
- D) AWS Cloud Map

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS CloudShell: A browser-based shell provided by AWS that enables command-line access to AWS resources directly from the AWS Management Console. Users can use AWS CloudShell to run AWS CLI commands and use various AWS tools without installing any additional software. It provides a convenient and secure way to interact with AWS resources in the cloud.

The other options (A, C, D) are not correct in the context of providing command line access to AWS tools and resources directly from a web browser:

A. AWS CloudHSM: AWS CloudHSM (Hardware Security Module) is a service that provides hardware-based key storage for sensitive data and cryptographic operations. It is not designed for providing command line access to AWS tools and resources from a web browser.

C. Amazon WorkSpaces: Amazon WorkSpaces is a managed desktop computing service, providing virtual desktops in the cloud. It is not specifically designed for providing command line access.

D. AWS Cloud Map: AWS Cloud Map is a service for dynamic, highly available DNS-based service discovery. It is not designed for providing command line access to AWS tools and resources from a web browser.
---
Selected Answer: B
B. AWS CloudShell: A browser-based shell provided by AWS that enables command-line access to AWS resources directly from the AWS Management Console. Users can use AWS CloudShell to run AWS CLI commands and use various AWS tools without installing any additional software. It provides a convenient and secure way to interact with AWS resources in the cloud.
---
Selected Answer: B
AWS CloudShell

</details>

---

## Question 186: CLF-C02-ET-Q186
**Domain 2:** Security and Compliance  

**Question:**  
A company has multiple AWS accounts. The company needs to receive a consolidated bill from AWS and must centrally manage security and compliance.

Which AWS service or feature should the company use to meet these requirements?

**Choices:**
- A) AWS Cost and Usage Report
- B) AWS Organizations
- C) AWS Config
- D) AWS Security Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Organizations
• Global service
• Allows to manage multiple AWS accounts
• The main account is the master account
• Cost Benefits:
• Consolidated Billing across all accounts - single payment method
• Pricing benefits from aggregated usage (volume discount for EC2, S3…)
• Pooling of Reserved EC2 instances for optimal savings
---
B. AWS Organizations

</details>

---

## Question 187: CLF-C02-ET-Q187
**Domain 3:** Cloud Technology and Services  

**Question:**  
For which use case are Amazon EC2 On-Demand Instances MOST cost-effective?

**Choices:**
- A) Compute-intensive video transcoding that can be restarted if necessary
- B) An instance in continual use for 1 month to conduct quality assurance tests
- C) An instance that runs a web server that will run for 1 year
- D) An instance that runs a database that will run for 3 years

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. An instance in continual use for 1 month to conduct quality assurance tests
---
Selected Answer: B
B looks like the right answer as it's shorter than the time required for the reserved instances like 1 year or 3 years.
---
B. An instance in continual use for 1 month to conduct quality assurance tests

</details>

---

## Question 188: CLF-C02-ET-Q188
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has developed a new In-house application. The company does not have a way to determine or predict the usage demand that the application will create.

Which AWS Cloud computing benefit is the company seeking?

**Choices:**
- A) Easy to use
- B) Cost-effective
- C) Secure
- D) Scalable and high performance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Scalable and high performance
---
D. Scalable and high performance

</details>

---

## Question 189: CLF-C02-ET-Q189
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS offering can analyze a company’s AWS environment to discover security vulnerabilities on Amazon EC2 instances?

**Choices:**
- A) Amazon Inspector
- B) Amazon Macie
- C) AWS Shield Standard
- D) Security groups

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
• Inspector: find software vulnerabilities in EC2, ECR Images, and Lambda
functions
---
Selected Answer: A
A. Amazon Inspector
---
A. Amazon Inspector

</details>

---

## Question 190: CLF-C02-ET-Q190
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to onboard new employees that will be working remotely. The company needs to set up Windows virtual desktops to create a working environment for the new employees. The employees must be able access the working environment from anywhere and by using their computer or a web browser.

Which AWS service or feature will meet these requirements?

**Choices:**
- A) Dedicated Hosts
- B) AWS Global Accelerator
- C) Amazon Workspaces
- D) Amazon CloudFront

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon WorkSpaces
• Managed Desktop as a Service (DaaS) solution to easily provision Windows or Linux desktops
---
Selected Answer: C
C. Amazon Workspaces
---
C. Amazon Workspaces

</details>

---

## Question 191: CLF-C02-ET-Q191
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to visualize and manage AWS Cloud costs and usage for a specific period of time.

Which AWS service or feature will meet these requirements?

**Choices:**
- A) Cost Explorer
- B) Consolidated billing
- C) AWS Organizations
- D) AWS Budgets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Cost Explorer
• Visualize, understand, and manage your AWS costs and usage over time
---
A. Cost Explorer

AWS Cost Explorer is a tool that enables you to visualize and manage AWS Cloud costs and usage. It provides a range of features for analyzing cost and usage patterns over specific periods, allowing you to create custom reports and forecasts.
---
Selected Answer: A
A. Cost Explorer is the service designed to help visualize and manage AWS Cloud costs and usage for specific periods of time. It provides detailed insights and reports on your spending patterns.

</details>

---

## Question 192: CLF-C02-ET-Q192
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service supports MySQL database engines?

**Choices:**
- A) Amazon Dynamo DВ
- B) Amazon RDS
- C) Amazon DocumentDB (with MongoDB compatibility)
- D) Amazon ElastiCache

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
• Integration with Amazon RDS (MySQL, PostgreSQL, Aurora)
---
Selected Answer: B
B. Amazon RDS
---
B. Amazon RDS

</details>

---

## Question 193: CLF-C02-ET-Q193
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company purchased Amazon EC2 Standard Reserved Instances (RIs) for a workload in the AWS Cloud. The company needs to move part of the workload to an instance family that does not match the instance family of these Standard RIs.

How can the company take advantage of the Standard RIs that it no longer needs?

**Choices:**
- A) Contact the AWS Support team, and ask the team to sell the Standard RIs
- B) Sell the Standard RIs on the Amazon EC2 Reserved Instance Marketplace
- C) Sell the Standard RIs as a third-party seller on the AWS Marketplace
- D) Convert the Standard RIs to Savings Plans

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Sell the Standard RIs on the Amazon EC2 Reserved Instance Marketplace
---
B. Sell the Standard RIs on the Amazon EC2 Reserved Instance Marketplace

</details>

---

## Question 194: CLF-C02-ET-Q194
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is releasing a business-critical application. Before the release, the company needs strategic planning assistance from AWS. During the release, the company needs AWS infrastructure event management and real-time support.

What should the company do to meet these requirements?

**Choices:**
- A) Access AWS Trusted Advisor
- B) Contact the AWS Partner Network (APN)
- C) Sign up for AWS Enterprise Support
- D) Contact AWS Professional Services

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
The company needs strategic planning assistance and real-time infrastructure event management during the release of its business-critical application. These requirements align with AWS Professional Services, which provides expertise for strategic planning, implementation, and support during critical projects, including application releases, whereas while AWS Enterprise Support provides 24/7 access to technical assistance and guidance, it does not focus on strategic planning or deployment assistance to the same degree as AWS Professional Services.
---
C. Sign up for AWS Enterprise Support

AWS Enterprise Support provides strategic planning assistance, infrastructure event management, and real-time support for critical business applications. It includes access to a Technical Account Manager (TAM) who can assist with planning and operational support, as well as 24/7 access to AWS experts for help with infrastructure events and real-time issues.

D. AWS Professional Services: This service offers consulting for strategic planning and implementation but does not include ongoing real-time support or infrastructure event management, which is provided by AWS Enterprise Support.

</details>

---

## Question 195: CLF-C02-ET-Q195
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to improve employee productivity by providing a way for employees to search for questions and retrieve specific answers. The company wants to use a single intelligent search interface.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Connect
- B) Amazon Kendra
- C) Amazon Lex
- D) Amazon Comprehend

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (80%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Kendra
---
Selected Answer: B
B - Amazon Kendra offers an intelligent enterprise search solution that increases employee productivity and improves customer satisfaction.
---
Selected Answer: A
Amazon Kendra
• Fully managed document search service powered by Machine Learning
• Extract answers from within a document (text, pdf, HTML, PowerPoint, MS Word, FAQs…)
• Natural language search capabilities
• Learn from user interactions/feedback to promote preferred results (Incremental Learning)

</details>

---

## Question 196: CLF-C02-ET-Q196
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is running and managing its own Docker environment on Amazon EC2 instances. The company wants an alternative to help manage cluster size, scheduling, and environment maintenance.
Which AWS service meets these requirements?

**Choices:**
- A) AWS Lambda
- B) Amazon RDS
- C) AWS Fargate
- D) Amazon Athena

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
The Anaswer is C, AWS Fargate 
AWS Fargate: A technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.
AWS Lambda: A serverless service to enable developers to run code without provisioning. 
AWS RDS : Fully managed relational database service.
AWS Athena: An interactive query service that makes it simple to analyze data directly in Amazon S3 using standard SQL.
---
Selected Answer: C
AWS Fargate is a serverless compute engine for containers that lets you run containers without managing the underlying infrastructure. It simplifies the process of managing clusters, scheduling tasks, and handling environment maintenance for containerized applications. With AWS Fargate, you only need to focus on your containers and applications, and AWS takes care of the underlying infrastructure. This makes it a suitable alternative for companies looking to simplify container management on Amazon EC2 instances.
---
Selected Answer: C
Fargate

</details>

---

## Question 197: CLF-C02-ET-Q197
**Domain 3:** Cloud Technology and Services  

**Question:**  
A network engineer needs to build a hybrid cloud architecture connecting on-premises networks to the AWS Cloud using AWS Direct Connect. The company has a few VPCs in a single AWS Region and expects to increase the number of VPCs to hundreds over time.
Which AWS service or feature should the engineer use to simplify and scale this connectivity as the VPCs increase in number?

**Choices:**
- A) VPC endpoints
- B) AWS Transit Gateway
- C) Amazon Route 53
- D) AWS Secrets Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
I choose to answer B

AWS Transit Gateway connects your Amazon Virtual Private Clouds (VPCs) and on-premises networks through a central hub. This connection simplifies your network and puts an end to complex peering relationships. Transit Gateway acts as a highly scalable cloud router—each new connection is made only once.

https://aws.amazon.com/transit-gateway/
---
Selected Answer: B
A. VPC endpoints: Enable private connectivity between your VPC and supported AWS services. While useful for accessing AWS services without going over the internet, it doesn't directly address the need for connecting multiple VPCs and on-premises networks.

B. AWS Transit Gateway: A service that enables customers to connect multiple Amazon Virtual Private Clouds (VPCs) and on-premises networks through a central hub. It simplifies the connectivity and routing between VPCs, making it easier to scale as the number of VPCs increases. With AWS Transit Gateway, network engineers can manage the connectivity centrally, making it a suitable solution for scenarios where multiple VPCs need to connect to on-premises networks.

C. Amazon Route 53: A scalable domain name system (DNS) web service. 

D. AWS Secrets Manager: A service for managing sensitive information such as API keys, passwords, and database credentials.
---
Selected Answer: B
B. AWS Transit Gateway: A service that enables customers to connect multiple Amazon Virtual Private Clouds (VPCs) and on-premises networks through a central hub. It simplifies the connectivity and routing between VPCs, making it easier to scale as the number of VPCs increases. With AWS Transit Gateway, network engineers can manage the connectivity centrally, making it a suitable solution for scenarios where multiple VPCs need to connect to on-premises networks.

</details>

---

## Question 198: CLF-C02-ET-Q198
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants an Amazon S3 solution that provides access to object storage within single-digit milliseconds.

Which solution will meet these requirements?

**Choices:**
- A) S3 Express One Zone
- B) S3 Standard
- C) S3 Glacier Flexible Retrieval
- D) S3 Glacier Instant Retrieval

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `56%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (56%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon S3 Express One Zone is designed for high-performance, low-latency object storage.
It provides single-digit millisecond access times, making it ideal for real-time applications, big data analytics, and machine learning workloads.

❌ B. S3 Standard – While S3 Standard is fast, it is not explicitly optimized for the lowest latency like S3 Express One Zone.
❌ C. S3 Glacier Flexible Retrieval – Designed for archival storage, takes minutes to hours to retrieve data.
❌ D. S3 Glacier Instant Retrieval – Provides millisecond access but is optimized for archival workloads, not high-performance storage.
---
Selected Answer: A
https://aws.amazon.com/tw/s3/storage-classes/express-one-zone/
Amazon S3 Express One Zone is a high-performance, single-Availability Zone storage class purpose-built to deliver consistent single-digit millisecond data access for your most frequently accessed data and latency-sensitive applications.
---
Selected Answer: A
"Amazon S3 Express One Zone is a high-performance, single-Availability Zone storage class purpose-built to deliver consistent single-digit millisecond data access for your most frequently accessed data and latency-sensitive applications."

https://aws.amazon.com/s3/storage-classes/

</details>

---

## Question 199: CLF-C02-ET-Q199
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company runs an uninterruptible Amazon EC2 workload on AWS 24 hours a day, 7 days a week. The company will require the same instance family and instance type to run the workload for the next 12 months.

Which combination of purchasing options should the company choose to MOST optimize costs? (Choose two.)

**Choices:**
- A) Standard Reserved Instance
- B) Convertible Reserved Instance
- C) Compute Savings Plan
- D) Spot Instance
- E) All Upfront payment

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AE (100%). Contributor Answer: AE.

Community Rationale & Discussion:
Selected Answer: AE
Reserved instances: • Up to 75% discount compared to On
-deman1d on hourly rate 1 or 3 years commitment
• All upfront, partial upfront, no upfront
---
Selected Answer: AE
A. Standard Reserved Instance:
Standard Reserved Instances (RIs) are ideal for workloads that run 24/7 and are predictable over a long period (e.g., 12 months). By committing to a specific instance family and type, the company can get significant discounts compared to On-Demand pricing.
E. All Upfront payment:
Choosing the All Upfront payment option for Reserved Instances provides the maximum discount. This option allows the company to pay for the entire 12-month commitment upfront, further reducing costs compared to monthly payments or partial upfront payments.
---
For the most cost-effective combination of purchasing options for an uninterruptible Amazon EC2 workload running continuously with the same instance family and type for the next 12 months, you should choose:

A. Standard Reserved Instance
E. All Upfront payment

</details>

---

## Question 200: CLF-C02-ET-Q200
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run its application's code without having to provision and manage servers.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Glue
- B) AWS Lambda
- C) AWS CodeDeploy
- D) Amazon CodeGuru

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Lambda: • 
Time limit • Limited runtimes • Limited temporary disk space • Serverless
---
Selected Answer: B
B. AWS Lambda - serverless
---
B. AWS Lambda

AWS Lambda allows you to run your code without provisioning or managing servers. You can upload your code to Lambda, and it automatically handles the compute resources needed to execute your code, scaling as required and managing the underlying infrastructure.

</details>

---

## Question 201: CLF-C02-ET-Q201
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate to the AWS Cloud. The company needs to understand the existing on-premises usage and configuration. The company does not want to replicate its workloads to AWS, yet.

Which AWS service or tool will meet these requirements?

**Choices:**
- A) AWS Application Discovery Service
- B) AWS Application Migration Service
- C) Cloud Migration Factory
- D) AWS Transfer Family

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Application Discovery Service
---
A. AWS Application Discovery Service

AWS Application Discovery Service helps you understand your existing on-premises usage and configuration by collecting data on your on-premises infrastructure, including application dependencies, server configurations, and usage patterns. This information helps in planning your migration to the AWS Cloud without requiring you to replicate or migrate your workloads at this stage.
---
Selected Answer: A
A. AWS Application Discovery Service: This service helps you collect detailed information about your on-premises environment, including server configurations, resource utilization, and network dependencies. It's specifically designed for companies that want to assess and understand their existing infrastructure before migrating to AWS, without actually replicating or migrating workloads yet.

</details>

---

## Question 202: CLF-C02-ET-Q202
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to allow its employees to work remotely from home. The company's employees use Windows or Linux desktops. The company's employees need access from anywhere and at anytime by using any supported devices.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Workspaces
- B) Amazon AppStream 2.0
- C) Amazon Keyspaces (for Apache Cassandra)
- D) AWS Cloud9

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon WorkSpaces - managed Desktop-as-a-Service (DaaS) solution that allows users to access secure and scalable virtual desktops from anywhere, using a variety of devices such as Windows PCs, macOS, Chromebooks, iPads, Android tablets, and web browsers.
---
A. Amazon WorkSpaces

</details>

---

## Question 203: CLF-C02-ET-Q203
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to test a new application.

Which AWS principle will help the company test the application?

**Choices:**
- A) Make long-term commitments in exchange for a cost discount.
- B) Scale up and down when needed without any long-term commitments.
- C) Have total control over the application infrastructure.
- D) Manage all of the maintenance tasks associated with the cloud.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Scale up and down when needed without any long-term commitments.
---
B. Scale up and down when needed without any long-term commitments.

</details>

---

## Question 204: CLF-C02-ET-Q204
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company plans to launch an ecommerce website that contains many images for a product catalog. The company wants to keep the cost of running the website within a specific budget.

Which AWS service or tool should the company use to monitor the ongoing costs of the website?

**Choices:**
- A) AWS Cost Explorer
- B) AWS SDKs
- C) EC2 Image Builder
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (67%). Contributor Answer: A.

Community Rationale & Discussion:
A. AWS Cost Explorer
---
Selected Answer: A
Only option that monitor's cost to my knowledge is A
---
Selected Answer: A
To meet the company’s need to monitor the ongoing costs of the e-commerce website and keep expenses within a specific budget, the most suitable AWS service is AWS Cost Explorer. Cost Explorer provides detailed cost analysis, budget monitoring, and forecasting capabilities, allowing the company to track the website’s operational costs (e.g., S3 storage for product images, EC2 compute costs) and ensure they don’t exceed the budget.

Final Answer: A. AWS Cost Explorer.

</details>

---

## Question 205: CLF-C02-ET-Q205
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has deployed several public applications behind Application Load Balancers. The company wants to improve the performance of the applications.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Global Accelerator
- B) Amazon Connect
- C) Amazon ElastiCache
- D) Amazon CloudWatch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Global Accelerator
• Improve global application availability and performance using the AWS global network
---
Selected Answer: A
Keyword: Improve performance 
A. AWS Global Accelerator
---
Selected Answer: A
A. AWS Global Accelerator

</details>

---

## Question 206: CLF-C02-ET-Q206
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company has an on-premises application. The application has processing times of less than 5 minutes and is invoked only a few times each day. The company wants to move the application to the AWS Cloud.

Which AWS service will support this application MOST cost-effectively?

**Choices:**
- A) Amazon Elastic Container Service (Amazon ECS)
- B) AWS Lambda
- C) Amazon Elastic Kubernetes Service (Amazon EKS)
- D) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
benefit lambda :
• Event-Driven: functions get invoked by AWS when needed
---
Selected Answer: B
B. AWS Lambda
---
B. AWS Lambda

</details>

---

## Question 207: CLF-C02-ET-Q207
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is learning about the perspectives of the AWS Cloud Adoption Framework (AWS CAF).

Which perspective of the AWS CAF addresses the strategy management capability?

**Choices:**
- A) Business perspective
- B) People perspective
- C) Governance perspective
- D) Operations perspective

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Answer A:
Business Perspective helps ensure that your cloud investments
accelerate your digital transformation ambitions and business outcomes
---
Business perspective: Focuses on aligning cloud initiatives with business goals and managing strategy to ensure that cloud adoption supports and drives business value.
The People perspective focuses on organizational change and skill development, the Governance perspective addresses policies and compliance, and the Operations perspective deals with the efficient operation of cloud resources.
---
A. Business perspective

</details>

---

## Question 208: CLF-C02-ET-Q208
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to assess its operational readiness. It also wants to identify and mitigate any operational risks ahead of a new product launch.
Which AWS Support plan offers guidance and support for this kind of event at no additional charge?

**Choices:**
- A) AWS Business Support
- B) AWS Basic Support
- C) AWS Developer Support
- D) AWS Enterprise Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `79%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (79%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Business Support: This plan provides a higher level of support than AWS Basic Support and includes 24/7 access to Cloud Support Engineers. It is suitable for businesses running production workloads.

AWS Basic Support: This is the free plan that provides access to documentation, forums, and basic support features. It is ideal for customers who are getting started with AWS.

AWS Developer Support: This plan is designed for developers running non-production workloads. It includes business hours access to Cloud Support Engineers and is suitable for development and testing environments.

AWS Enterprise Support: This is the premium support plan providing a wide range of benefits, including 24/7 access to Cloud Support Engineers, a Technical Account Manager (TAM), and more. It is suitable for enterprises running business-critical workloads

For assessing operational readiness, identifying, and mitigating operational risks ahead of a new product launch, AWS Enterprise Support offers guidance and support at no additional charge.
---
Selected Answer: D
Shouldn't this be Enterprise support? Keywords "event" and "no additional cost"

AWS Infrastructure Event Management (IEM) offers architecture and scaling guidance and operational support during the preparation and execution of planned events, such as shopping holidays, product launches, and migrations. For these events, AWS Infrastructure Event Management will help you assess operational readiness, identify and mitigate risks, and execute your event confidently with AWS experts by your side. The program is included in the Enterprise Support plan and is available to Business Support customers for an additional fee.
---
Selected Answer: C
AWS Developer Support: This plan is designed for developers running non-production workloads. It includes business hours access to Cloud Support Engineers and is suitable for development and testing environments.

</details>

---

## Question 209: CLF-C02-ET-Q209
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to consolidate its call centers to improve the customer voice and chat experience with call center agents.

Which AWS service or tool will meet these requirements?

**Choices:**
- A) Amazon Simple Notification Service (Amazon SNS)
- B) AWS Support Center
- C) Amazon Cognito
- D) Amazon Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon Connect:
• Receive calls, create contact flows, cloud-based virtual contact center
---
Selected Answer: D
D. Amazon Connect - AWS service designed to set up and manage a cloud-based contact center that provides voice and chat support.
---
D. Amazon Connect: Amazon Connect is a cloud-based contact center service that provides a seamless voice and chat experience. It allows companies to consolidate and manage their call centers efficiently, providing advanced features for improving customer interactions with agents.

</details>

---

## Question 210: CLF-C02-ET-Q210
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to provision uninterruptible Amazon EC2 instances, when needed, and pay for compute capacity by the second.

Which EC2 instance purchasing option will meet these requirements?

**Choices:**
- A) Reserved Instances
- B) Spot Instances
- C) On-Demand Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
On-Demand Instances – short workload, predictable pricing, pay by second
---
C. On-Demand Instances

</details>

---

## Question 211: CLF-C02-ET-Q211
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can migrate Amazon EC2 instances from one AWS Region to another?

**Choices:**
- A) AWS Application Migration Service
- B) AWS Database Migration Service (AWS DMS)
- C) AWS DataSync
- D) AWS Migration Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Application Migration Service (formerly known as AWS Server Migration Service or AWS SMS) is designed to migrate Amazon EC2 instances (and their associated workloads) from one AWS Region to another.
---
A. AWS Application Migration Service
---
Selected Answer: A
A. AWS Application Migration Service: This service can be used to migrate Amazon EC2 instances between AWS Regions. It replicates entire server instances and converts them to run on AWS infrastructure, including across different regions.

</details>

---

## Question 212: CLF-C02-ET-Q212
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to block SQL injection attacks.

Which AWS service or feature provides this functionality?

**Choices:**
- A) AWS WAF
- B) Network ACLs
- C) Security groups
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS WAF
---
A. AWS WAF

</details>

---

## Question 213: CLF-C02-ET-Q213
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to run its application on Amazon EC2 instances. The company needs to keep the application on-premises to meet a compliance requirement.

Which AWS offering will meet these requirements?

**Choices:**
- A) Dedicated Instances
- B) Amazon CloudFront
- C) AWS Fargate
- D) AWS Outposts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Outposts - extends AWS' infrastructure to on-prem environments.
---
AWS Outposts is needed when a company wants to use AWS cloud services but must keep some workloads or data on-premises due to compliance, low-latency requirements, or other reasons. It allows you to run AWS infrastructure in your own data center while still managing it like you would in the cloud. So, you get the benefits of AWS services, but the hardware stays at your location.

</details>

---

## Question 214: CLF-C02-ET-Q214
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to connect its supported AWS services and VPCs. The company does not want to expose its internal traffic to the public internet.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Inspector
- B) AWS PrivateLink
- C) Amazon Connect
- D) AWS Internet Gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS PrivateLink provides a private network connection between VPCs and AWS services
---
Selected Answer: B
AWS PrivateLink (VPC Endpoint Services)
• Most secure & scalable way to expose a service to 1000s of VPCs
---
Selected Answer: B
B is the right answer by the process of elimination .

</details>

---

## Question 215: CLF-C02-ET-Q215
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can manage permissions for AWS resources by using policies?

**Choices:**
- A) Amazon Inspector
- B) Amazon Detective
- C) AWS Identity and Access Management (IAM)
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. AWS Identity and Access Management (IAM).

</details>

---

## Question 216: CLF-C02-ET-Q216
**Domain 2:** Security and Compliance  

**Question:**  
A company needs to run some of its workload in the AWS Cloud. The company needs to keep some of the workload in its own on-site data center due to compliance reasons.

Which AWS service will meet these requirements?

**Choices:**
- A) AWSConfig
- B) AWS Outposts
- C) Amazon Lightsail
- D) Amazon Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B. AWS Outposts.

AWS Outposts extends AWS infrastructure, services, APIs, and tools to your on-premises data center. It enables you to run some of your workloads in the AWS Cloud while keeping others on-premises to meet compliance requirements.

</details>

---

## Question 217: CLF-C02-ET-Q217
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to deploy an application that stores data in a relational database. The company wants database tasks, such as automated backups and database snapshots, to be managed by AWS.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon DocumentDB
- B) Amazon RDS
- C) Amazon Elastic Block Store (Amazon EBS)
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (67%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
RDS ya'll.
---
Selected Answer: B
AWS RDS, Relational Database Service
---
Selected Answer: B
Amazon EBS is a block storage service, not a managed database service.

</details>

---

## Question 218: CLF-C02-ET-Q218
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company that operates on-premises servers decides to start a new line of business. The company determines that additional servers are required for the new workloads.

Which advantage of cloud computing can help the company to provision additional infrastructure as quickly as possible?

**Choices:**
- A) Benefit from massive economies of scale
- B) Increase speed and agility
- C) Trade fixed expense for variable expense
- D) Go global in minutes

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
quick-agility

</details>

---

## Question 219: CLF-C02-ET-Q219
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to establish a schedule for rotating database user credentials.
Which AWS service will support this requirement with the LEAST amount of operational overhead?

**Choices:**
- A) AWS Systems Manager
- B) AWS Secrets Manager
- C) AWS License Manager
- D) AWS Managed Services

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Systems Manager: It is a management service that allows you to automate operational tasks across your AWS resources. While it provides a wide range of automation capabilities, it is not specialized for the specific task of rotating database credentials.

 AWS Secrets Manager: This service is specifically designed for managing sensitive information like API keys, passwords, and database credentials. It includes automatic rotation of secrets to enhance security and reduce operational overhead.

 AWS License Manager: This service focuses on helping you manage your software licenses and ensure compliance. It does not offer specific features for rotating database credentials.

 AWS Managed Services: This service is designed to provide ongoing management of your AWS infrastructure. While it covers various operational aspects, it doesn't have specific features for credential rotation.
---
Selected Answer: B
https://aws.amazon.com/secrets-manager/
AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycles.
---
Selected Answer: B
AWS Secrets Manager

</details>

---

## Question 220: CLF-C02-ET-Q220
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature can be used to create a private connection between an on-premises workload and an AWS Cloud workload?

**Choices:**
- A) Amazon Route 53
- B) Amazon Macie
- C) AWS Direct Connect
- D) AWS PrivateLink

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `77%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (77%). Contributor Answer: C.

Community Rationale & Discussion:
The correct answer is C. AWS Direct Connect.

Here's a breakdown of the options and why Direct Connect is the most suitable:

A. Amazon Route 53 is a domain name system (DNS) web service, not a private connection service.

B. Amazon Macie is a security service for data protection in AWS, not a connectivity service.

C. AWS Direct Connect establishes a dedicated private connection between your on-premises infrastructure and AWS. It offers:

Increased bandwidth
Reduced latency
Improved security compared to internet-based connections
Bypass the public internet for sensitive data transfers
D. AWS PrivateLink facilitates private connectivity between AWS services and VPCs within the AWS cloud, but it doesn't extend to on-premises environments.

Therefore, AWS Direct Connect is the most appropriate service for establishing private connections between on-premises workloads and AWS cloud workloads.
---
Selected Answer: C
Amazon Route 53: This is a scalable domain name system (DNS) web service and is not directly related to creating private connections between on-premises and AWS Cloud workloads.

Amazon Macie: This is a security service that uses machine learning to automatically discover, classify, and protect sensitive data. It is not designed for creating private connections.

AWS Direct Connect: Establishes dedicated network connections from your on-premises data centers to AWS. It can enhance network performance, reduce latency, and provide a more reliable connection compared to public internet connections. AWS Direct Connect is specifically designed for creating private and dedicated connections between on-premises infrastructure and AWS resources.

AWS PrivateLink: Designed for secure and scalable access to AWS services directly from your VPC without traversing the public internet. It's particularly useful when you want to access AWS services from your VPC without using public IP addresses and want to keep the traffic within the AWS network.

For creating a private connection between on-premises and AWS, AWS Direct Connect is the most suitable option.
---
Selected Answer: D
Option D - AWS Private Link - the keyword is private connection 
Private connection - AWS Private Link
Dedicated Connection :- AWS Direct Connect
AWS PrivateLink provides private connectivity between virtual private clouds (VPCs), supported services and resources, and your on-premises networks, without exposing your traffic to the public internet. Interface VPC endpoints, powered by PrivateLink, connect you to services hosted by AWS and AWS Partners and supported solutions available in AWS Marketplace. Gateway Load Balancer VPC endpoints connect you to appliances. Resource VPC endpoints powered by PrivateLink connect you to VPC resources such as Amazon Relational Database Service (Amazon RDS) databases, and domain names and IP addresses in other VPCs and accounts. Service network VPC endpoints connect you to Amazon VPC Lattice service networks.
https://aws.amazon.com/privatelink/

</details>

---

## Question 221: CLF-C02-ET-Q221
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service is used to provide encryption for Amazon EBS?

**Choices:**
- A) AWS Certificate Manager
- B) AWS Systems Manager
- C) AWS KMS
- D) AWS Config

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. AWS Certificate Manager (ACM): Primarily used for managing SSL/TLS certificates used in conjunction with AWS services like Elastic Load Balancer (ELB) or Amazon CloudFront to enable secure communication over HTTPS. It is not directly related to encrypting Amazon EBS volumes.

B. AWS Systems Manager: Allows you to automate operational tasks across your AWS resources. While it provides features for managing system configurations, patching, and automation, it is not specifically designed for encrypting Amazon EBS volumes.

C. AWS Key Management Service (AWS KMS): A fully managed service that makes it easy for you to create, control, and manage encryption keys used to encrypt your data. It integrates seamlessly with other AWS services, including Amazon EBS, for encryption purposes.

D. AWS Config: Enables you to assess, audit, and evaluate the configurations of your AWS resources. It does not directly provide encryption for Amazon EBS volumes.
---
Selected Answer: C
C. AWS Key Management Service (AWS KMS): A fully managed service that makes it easy for you to create, control, and manage encryption keys used to encrypt your data. It integrates seamlessly with other AWS services, including Amazon EBS, for encryption purposes.
---
C. AWS Key Management Service (AWS KMS): A fully managed service that makes it easy for you to create, control, and manage encryption keys used to encrypt your data. It integrates seamlessly with other AWS services, including Amazon EBS, for encryption purposes.

</details>

---

## Question 222: CLF-C02-ET-Q222
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to manage its AWS Cloud resources through a web interface.
Which AWS service will meet this requirement?

**Choices:**
- A) AWS Management Console
- B) AWS CLI
- C) AWS SDK
- D) AWS Cloud9

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Management Console: A web-based interface that allows users to access and manage their AWS resources using a graphical user interface (GUI). This console provides an easy-to-use platform for various AWS services.

B. AWS CLI (Command Line Interface): Command-line tool that allows users to interact with AWS services using commands in the terminal or command prompt. It is not a web interface but a command-line tool.

C. AWS SDK (Software Development Kit): Libraries and tools provided by AWS to help developers interact with AWS services programmatically. They are used for developing applications and are not a web interface.

D. AWS Cloud9: An integrated development environment (IDE) that allows users to write, run, and debug code directly in the browser. While it provides an interface, it is specifically designed for development tasks rather than general resource management.
---
Selected Answer: A
A. AWS Management Console: A web-based interface that allows users to access and manage their AWS resources using a graphical user interface (GUI). This console provides an easy-to-use platform for various AWS services.
---
A. AWS Management Console: A web-based interface that allows users to access and manage their AWS resources using a graphical user interface (GUI). This console provides an easy-to-use platform for various AWS services.

</details>

---

## Question 223: CLF-C02-ET-Q223
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are advantages of the AWS Cloud? (Choose two.)

**Choices:**
- A) Trade variable expenses for capital expenses
- B) High economies of scale
- C) Launch globally in minutes
- D) Focus on managing hardware infrastructure
- E) Overprovision to ensure capacity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (94%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
B. High economies of scale
C. Launch globally in minutes
---
B. High economies of scale: AWS Cloud leverages high economies of scale, allowing customers to benefit from cost savings due to the massive scale of AWS infrastructure. This enables cost-effective solutions for businesses.

C. Launch globally in minutes: One of the advantages of the AWS Cloud is the ability to deploy applications and resources globally in a matter of minutes. This quick global deployment facilitates flexibility and responsiveness to changing business needs.
---
Selected Answer: BC
B. High economies of scale: AWS Cloud leverages high economies of scale, allowing customers to benefit from cost savings due to the massive scale of AWS infrastructure. This enables cost-effective solutions for businesses.

C. Launch globally in minutes: One of the advantages of the AWS Cloud is the ability to deploy applications and resources globally in a matter of minutes. This quick global deployment facilitates flexibility and responsiveness to changing business needs.

Option A is not accurate. The AWS Cloud allows organizations to shift from capital expenses (CapEx) to variable expenses (OpEx), not the other way around. 

Option D is not accurate. With AWS Cloud, customers can focus on building and innovating applications rather than managing the hardware infrastructure. 

Option E is not accurate. Overprovisioning is not considered an advantage in the AWS Cloud. Instead, AWS provides scalability, allowing users to scale resources up or down based on demand, avoiding the need for unnecessary overprovisioning.

</details>

---

## Question 224: CLF-C02-ET-Q224
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud benefit is shown by an architecture’s ability to withstand failures with minimal downtime?

**Choices:**
- A) Agility
- B) Elasticity
- C) Scalability
- D) High availability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `97%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (97%). Contributor Answer: D.

Community Rationale & Discussion:
The correct answer is D. High availability.

Here's why:

Agility refers to the ability to quickly adapt to changing needs, which isn't directly related to handling failures.
Elasticity focuses on scaling resources up or down based on demand, not necessarily surviving component failures.
Scalability allows increasing resources to handle larger workloads, but doesn't guarantee uninterrupted operation if individual components fail.
High availability specifically ensures continuous service in the face of failures by implementing redundancy and fault tolerance mechanisms. Therefore, an architecture able to withstand failures with minimal downtime demonstrates high availability as its primary benefit.
Remember, high availability prioritizes minimizing downtime, while other options address different aspects of cloud computing.
---
I'm starting to think some of these answers are intentionally meant to be wrong
---
Selected Answer: D
D. High availability

</details>

---

## Question 225: CLF-C02-ET-Q225
**Domain 3:** Cloud Technology and Services  

**Question:**  
A developer needs to maintain a development environment infrastructure and a production environment infrastructure in a repeatable fashion.
Which AWS service should the developer use to meet these requirements?

**Choices:**
- A) AWS Ground Station
- B) AWS Shield
- C) AWS IoT Device Defender
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A. AWS Ground Station: AWS Ground Station is a service for satellite data processing.

B. AWS Shield: AWS Shield is a managed Distributed Denial of Service (DDoS) protection service. It is focused on protecting applications from DDoS attacks.

C. AWS IoT Device Defender: AWS IoT Device Defender is a service that helps you secure your IoT devices.

D. AWS CloudFormation: A service that allows you to define and provision AWS infrastructure as code in a safe, predictable, and repeatable manner. It enables the developer to create and manage a collection of AWS resources by describing the infrastructure in a template. This helps in maintaining both development and production environments consistently.
---
Selected Answer: D
D. AWS CloudFormation: A service that allows you to define and provision AWS infrastructure as code in a safe, predictable, and repeatable manner. It enables the developer to create and manage a collection of AWS resources by describing the infrastructure in a template. This helps in maintaining both development and production environments consistently.
---
Selected Answer: D
D. AWS CloudFormation

</details>

---

## Question 226: CLF-C02-ET-Q226
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user wants to securely automate the management and rotation of credentials that are shared between applications, while spending the least amount of time on managing tasks.

Which AWS service or feature can be used to accomplish this?

**Choices:**
- A) AWS CloudHSM
- B) AWS Key Management Service (AWS KMS)
- C) AWS Secrets Manager
- D) Server-side encryption

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
AWS Secrets Manager helps in the secure storage, rotation, and retrieval of sensitive credentials such as API keys, database passwords, and other secrets used by applications. 
AWS CloudHSM provides hardware-based key storage for cryptographic keys and is more focused on custom key storage and compliance needs, which might be an overkill for just credential management and rotation.

AWS Key Management Service (AWS KMS) is used for creating and managing encryption keys. While it's crucial for encryption, it doesn’t directly handle the automated management and rotation of credentials shared between applications.
---
Selected Answer: C
A. AWS CloudHSM: AWS CloudHSM (Hardware Security Module) is a service that provides hardware-based key storage for sensitive data and cryptographic operations.
B. AWS Key Management Service (AWS KMS) is used for creating and controlling encryption keys used to encrypt your data
C. AWS Secrets Manager is designed specifically for storing, managing, and rotating credentials securely and automatically
D. Server-side encryption process where data is encrypted at the server level before it is stored, which is primarily used to protect data at rest
---
Selected Answer: C
C. AWS Secrets Manager

</details>

---

## Question 227: CLF-C02-ET-Q227
**Domain 2:** Security and Compliance  

**Question:**  
Which security service automatically recognizes and classifies sensitive data or intellectual property on AWS?

**Choices:**
- A) Amazon GuardDuty
- B) Amazon Macie
- C) Amazon Inspector
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Macie
---
B. Amazon Macie

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data, such as personally identifiable information (PII) and intellectual property, across your AWS environment.
---
B. Amazon Macie

</details>

---

## Question 228: CLF-C02-ET-Q228
**Domain 3:** Cloud Technology and Services  

**Question:**  
An e-learning platform needs to run an application for 2 months each year. The application will be deployed on Amazon EC2 instances. Any application downtime during those 2 months must be avoided.
Which EC2 purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) Reserved Instances
- B) Dedicated Hosts
- C) Spot Instances
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `95%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (95%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A. Reserved Instances (RIs): Reserved Instances provide capacity reservation for a specified term (usually one or three years), offering cost savings compared to On-Demand Instances. However, RIs may not be the most suitable for a short duration like 2 months, as they typically involve longer-term commitments.

B. Dedicated Hosts: Dedicated Hosts may not be cost-effective for short-term workloads and lack the flexibility needed.

C. Spot Instances: Spot Instances offer cost savings but can be terminated with short notice, potentially causing interruptions.

D. On-Demand Instances: On-Demand Instances provide capacity on a pay-as-you-go basis with no upfront commitment. They are suitable for short-term, variable workloads, offering flexibility without the need for long-term commitments. In this scenario, On-Demand Instances would be a cost-effective option for the 2-month duration while avoiding downtime.
---
D - On-Demand Instances is correct.

"On-Demand Instances are recommended for:
• Users that prefer the low cost and flexibility of EC2 without any upfront payment or long-term commitment
• Applications with short-term, spiky, or unpredictable workloads that cannot be interrupted
• Applications being developed or tested on EC2 for the first time"

Reference: https://aws.amazon.com/ec2/pricing/
---
Selected Answer: D
On-Demand Instances provide capacity on a pay-as-you-go basis with no upfront commitment. They are suitable for short-term, variable workloads, offering flexibility without the need for long-term commitments. In this scenario, On-Demand Instances would be a cost-effective option for the 2-month duration while avoiding downtime.

</details>

---

## Question 229: CLF-C02-ET-Q229
**Domain 2:** Security and Compliance  

**Question:**  
Which actions are best practices for an AWS account root user? (Choose two.)

**Choices:**
- A) Share root user credentials with team members.
- B) Create multiple root users for the account, separated by environment.
- C) Enable multi-factor authentication (MFA) on the root user.
- D) Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.
- E) Use programmatic access instead of the root user and password.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (100%). Contributor Answer: CD.

Community Rationale & Discussion:
Selected Answer: CD
C. Enable multi-factor authentication (MFA) on the root user:
Enabling MFA adds an extra layer of security to the root user account. Even if someone gains access to the root user credentials, they would also need the second factor (such as a phone or hardware token) to access the account.

D. Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user:
It is a best practice to avoid using the root user for day-to-day tasks because the root user has unrestricted access to all resources and can make significant changes to your account. Instead, you should create an IAM user with administrator privileges and use that for routine management tasks.
---
Selected Answer: CD
The best practices for an AWS account root user are:

C. Enable multi-factor authentication (MFA) on the root user.
Enabling MFA adds an extra layer of security to protect the root user account from unauthorized access.

D. Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.
It's recommended to create an IAM user with the necessary permissions for daily administrative tasks rather than using the root user. This practice helps in maintaining better security and accountability by reducing the reliance on the highly privileged root user account.

So, the correct options are C and D
---
Selected Answer: CD
CD are correct

</details>

---

## Question 230: CLF-C02-ET-Q230
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is running a critical workload on an Amazon RDS DB instance. The company needs the DB instance to be highly available with a recovery time of less than 5 minutes.

Which solution will meet these requirements?

**Choices:**
- A) Create a read replica of the DB instance.
- B) Create a template of the DB instance by using AWS CloudFormation.
- C) Take frequent snapshots of the DB instance. Store the snapshots in Amazon S3.
- D) Modify the DB instance to be a Multi-AZ deployment.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database (DB) instance and synchronously replicates the data to an instance in a different AZ. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention.
---
Selected Answer: D
In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database (DB) instance and synchronously replicates the data to an instance in a different AZ. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention.
---
Selected Answer: D
Keyword: Highly Available

</details>

---

## Question 231: CLF-C02-ET-Q231
**Domain 2:** Security and Compliance  

**Question:**  
Which task is the customer’s responsibility, according to the AWS shared responsibility model?

**Choices:**
- A) Maintain the security of the AWS Cloud.
- B) Configure firewalls and networks.
- C) Patch the operating system of Amazon RDS instances.
- D) Implement physical and environmental controls.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Generally I don’t like the context of this question. B. could also mean network ACLs, not just security groups at the instance level.
---
Selected Answer: B
B. Configure firewalls and networks: This is a customer responsibility. Customers have control over configuring security groups, network access control lists (ACLs), and other network-related configurations to control traffic to and from their resources.
---
B. Configure firewalls and networks: This is a customer responsibility. Customers have control over configuring security groups, network access control lists (ACLs), and other network-related configurations to control traffic to and from their resources.

</details>

---

## Question 232: CLF-C02-ET-Q232
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run a NoSQL database on Amazon EC2 instances.
Which task is the responsibility of AWS in this scenario?

**Choices:**
- A) Update the guest operating system of the EC2 instances.
- B) Maintain high availability at the database layer.
- C) Patch the physical infrastructure that hosts the EC2 instances.
- D) Configure the security group firewall.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `96%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (96%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A is incorrect because when we set up an instance of ec2 we choose the operating system.
B is incorrect because we are configuring and running the database on the ec2 instances so that would be our responsibility.
D is incorrect because the firewall rules are our job.
C is correct because the physical infrastructure where the ec2 instances run is amazon's responsibility
---
Selected Answer: C
A. Update the guest operating system of the EC2 instances:

 Responsibility of the customer: Customers are responsible for managing the software environment within their EC2 instances, including updating the guest operating system.

B. Maintain high availability at the database layer:

 Shared responsibility: While AWS ensures high availability at the infrastructure level, customers are responsible for configuring and managing the database layer to achieve high availability. This involves setting up replication, failover mechanisms, and ensuring that the database software is configured appropriately.

C. Patch the physical infrastructure that hosts the EC2 instances:

 Responsibility of AWS: AWS manages the physical infrastructure, including patching and updates at the hardware level. Customers do not have direct control over the physical infrastructure.

D. Configure the security group firewall:

 Responsibility of the customer: Security groups are a customer-managed feature that controls inbound and outbound traffic to and from EC2 instances. Customers are responsible for configuring security groups to meet their specific security requirements.
---
Selected Answer: C
Physical == AWS responsibility

</details>

---

## Question 233: CLF-C02-ET-Q233
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service helps deliver highly available applications with fast failover for multi-Region and Multi-AZ architectures?

**Choices:**
- A) AWS WAF
- B) AWS Global Accelerator
- C) AWS Shield
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Global Accelerator: A service that uses static IP addresses to route traffic over the AWS global network to optimal AWS endpoints based on health, geography, and routing policies. It provides highly available and performant applications with features like fast failover for multi-Region and Multi-AZ (Availability Zone) architectures.

 AWS WAF (Web Application Firewall): It is a web application firewall that helps protect web applications from common web exploits. 
 AWS Shield: It is a managed Distributed Denial of Service (DDoS) protection service.
 AWS Direct Connect: It provides dedicated network connections from on-premises data centers to AWS, enhancing network performance.
---
Selected Answer: B
B. AWS Global Accelerator: A service that uses static IP addresses to route traffic over the AWS global network to optimal AWS endpoints based on health, geography, and routing policies. It provides highly available and performant applications with features like fast failover for multi-Region and Multi-AZ (Availability Zone) architectures.
---
B. AWS Global Accelerator is a service that improves the availability and performance of your applications with local or global users

</details>

---

## Question 234: CLF-C02-ET-Q234
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a set of ecommerce applications. The applications need to be able to send messages to each other.
Which AWS service meets this requirement?

**Choices:**
- A) AWS Auto Scaling
- B) Elastic Load Balancing
- C) Amazon Simple Queue Service (Amazon SQS)
- D) Amazon Kinesis Data Streams

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Simple Queue Service (SQS): SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It allows one application to send messages to a queue, and another application to retrieve those messages from the queue. This can be helpful in scenarios where the sender and receiver are not required to interact with each other in real-time.
---
Selected Answer: C
Amazon Simple Queue Service (SQS): SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It allows one application to send messages to a queue, and another application to retrieve those messages from the queue. This can be helpful in scenarios where the sender and receiver are not required to interact with each other in real-time.
---
Amazon Simple Queue Service (SQS): SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It allows one application to send messages to a queue, and another application to retrieve those messages from the queue. This can be helpful in scenarios where the sender and receiver are not required to interact with each other in real-time.

</details>

---

## Question 235: CLF-C02-ET-Q235
**Domain 3:** Cloud Technology and Services  

**Question:**  
What are the benefits of consolidated billing for AWS Cloud services? (Choose two.)

**Choices:**
- A) Volume discounts
- B) A minimal additional fee for use
- C) One bill for multiple accounts
- D) Installment payment options
- E) Custom cost and usage budget creation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `87%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (87%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
Consolidated billing has the following benefits:
- ONE BILL – You get one bill for multiple accounts.
- Combined usage – You can combine the usage across all accounts in the organization to share the VOLUME PRICING DISCOUNTS, Reserved Instance discounts, and Savings Plans. This can result in a lower charge for your project, department, or company than with individual standalone accounts.

Ref: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html
---
Selected Answer: AC
A. Volume discounts: Consolidated billing combines usage for potential higher volume discounts.

 B. A minimal additional fee for use: Consolidated billing focuses on simplifying billing, without introducing additional fees.

 C. One bill for multiple accounts: Consolidated billing provides a single bill for all linked AWS accounts, simplifying the billing process.

 D. Installment payment options: Payment options are part of AWS billing but not exclusive to consolidated billing.

 E. Custom cost and usage budget creation: Creating custom budgets is not directly related to consolidated billing but can be managed separately with AWS Budgets.
---
Selected Answer: AC
A. Volume discounts: Consolidated billing combines usage for potential higher volume discounts.
C. One bill for multiple accounts: Consolidated billing provides a single bill for all linked AWS accounts, simplifying the billing process.

</details>

---

## Question 236: CLF-C02-ET-Q236
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user wants to review all Amazon S3 buckets with ACLs and S3 bucket policies in the S3 console.
Which AWS service or resource will meet this requirement?

**Choices:**
- A) S3 Multi-Region Access Points
- B) S3 Storage Lens
- C) AWS IAM Identity Center (AWS Single Sign-On)
- D) Access Analyzer for S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `97%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (97%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A. S3 Multi-Region Access Points: This service is designed for multi-region access to S3 data.

B. S3 Storage Lens: This service provides organization-wide visibility into object storage usage and activity.

C. AWS IAM Identity Center (AWS Single Sign-On): This service is related to identity and access management, but it doesn't provide a direct interface for reviewing S3 bucket ACLs and policies.

D. Access Analyzer for S3: This service is designed to review and analyze access policies for S3 buckets, providing insights into who has access to your buckets and how that access is granted. It is the most suitable option for the specified requirement.
---
Selected Answer: D
D. Access Analyzer for S3: This service is designed to review and analyze access policies for S3 buckets, providing insights into who has access to your buckets and how that access is granted. It is the most suitable option for the specified requirement.
---
Selected Answer: D
D. Access Analyzer for S3

</details>

---

## Question 237: CLF-C02-ET-Q237
**Domain 2:** Security and Compliance  

**Question:**  
What is the best resource for a user to find compliance-related information and reports about AWS?

**Choices:**
- A) AWS Artifact
- B) AWS Marketplace
- C) Amazon Inspector
- D) AWS Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Artifact: A portal that provides on-demand access to AWS compliance reports, certifications, and attestations. It is a centralized location for various compliance-related documents.
---
A. AWS Artifact: A portal that provides on-demand access to AWS compliance reports, certifications, and attestations. It is a centralized location for various compliance-related documents.
---
Selected Answer: A
A. AWS Artifact: A portal that provides on-demand access to AWS compliance reports, certifications, and attestations. It is a centralized location for various compliance-related documents.

B. AWS Marketplace: An online store where customers can find, buy, and deploy software that runs on AWS.

C. Amazon Inspector: An automated security assessment service that helps improve the security and compliance of applications deployed on AWS. 

D. AWS Support: Provides technical support for AWS services. While AWS Support may assist with compliance-related inquiries, it is not the primary resource for compliance reports.

</details>

---

## Question 238: CLF-C02-ET-Q238
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service enables companies to deploy an application close to end users?

**Choices:**
- A) Amazon CloudFront
- B) AWS Auto Scaling
- C) AWS AppSync
- D) Amazon Route 53

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon CloudFront: A content delivery network (CDN) service that enables companies to deliver static and dynamic web content, including applications, to end users with low latency and high transfer speeds. It helps deploy an application close to end users.

B. AWS Auto Scaling: Automatically adjusts the number of Amazon EC2 instances in a group based on changing application demand. 

C. AWS AppSync: Afully managed service that makes it easy to develop GraphQL APIs. It helps applications securely connect to data sources like AWS DynamoDB. 

D. Amazon Route 53: A scalable domain name system (DNS) web service designed to route end-user requests to globally distributed endpoints. It facilitates domain registration and management of DNS records, contributing to efficient application deployment.
---
Selected Answer: A
"Amazon CloudFront speeds up distribution of your static and dynamic web content, such as .html, .css, .php, image, and media files. When users request your content, CloudFront delivers it through a worldwide network of edge locations that provide low latency and high performance."

Reference: https://docs.aws.amazon.com/cloudfront/
---
Selected Answer: A
A. Amazon CloudFront: A content delivery network (CDN) service that enables companies to deliver static and dynamic web content, including applications, to end users with low latency and high transfer speeds. It helps deploy an application close to end users.

</details>

---

## Question 239: CLF-C02-ET-Q239
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature improves network performance by sending traffic through the AWS worldwide network infrastructure?

**Choices:**
- A) Route table
- B) AWS Transit Gateway
- C) AWS Global Accelerator
- D) Amazon VPC

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Route table: A route table in Amazon VPC contains a set of rules, called routes, that are used to determine where network traffic is directed. While it is essential for routing within a VPC, it doesn't specifically improve network performance by leveraging the AWS worldwide network infrastructure.

B. AWS Transit Gateway: A service that simplifies network connectivity across multiple Amazon VPCs, on-premises data centers, and remote offices. It helps with managing and scaling connectivity but doesn't focus on improving network performance globally.

C. AWS Global Accelerator: A service that uses the AWS global network to optimize the routing of traffic to applications. It improves the availability and performance of applications by utilizing anycast IP addresses. It specifically improves network performance globally.

D. Amazon VPC: A service that lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources. While VPC is fundamental for networking in AWS, it doesn't directly improve network performance through the global infrastructure.
---
Selected Answer: C
C. AWS Global Accelerator: A service that uses the AWS global network to optimize the routing of traffic to applications. It improves the availability and performance of applications by utilizing anycast IP addresses. It specifically improves network performance globally.
---
C. AWS Global Accelerator: A service that uses the AWS global network to optimize the routing of traffic to applications. It improves the availability and performance of applications by utilizing anycast IP addresses. It specifically improves network performance globally.

</details>

---

## Question 240: CLF-C02-ET-Q240
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides highly durable object storage?

**Choices:**
- A) Amazon S3
- B) Amazon Elastic File System (Amazon EFS)
- C) Amazon Elastic Block Store (Amazon EBS)
- D) Amazon FSx

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon S3 (Simple Storage Service): Provides highly durable object storage with 99.999999999% (11 9's) durability. It is suitable for storing and retrieving any amount of data.

B. Amazon Elastic File System (Amazon EFS): Provides scalable file storage, but it is not specifically designed for object storage. It is more suitable for file-based workloads.

C. Amazon Elastic Block Store (Amazon EBS): Provides block-level storage volumes for use with Amazon EC2 instances. It is not object storage; instead, it is used for attaching persistent block storage to instances.

D. Amazon FSx: Provides fully managed file storage, and it is not focused on object storage. It is designed for Windows File Server or Lustre file systems.
---
Selected Answer: A
A. Amazon S3 (Simple Storage Service): Provides highly durable object storage with 99.999999999% (11 9's) durability. It is suitable for storing and retrieving any amount of data.
---
A. Amazon S3 is the answer 
the keyword is durable and object 
S3 SLA is 11 9's highly available.

EBS is for EC2 
FSx and EFS are suitable for File storage!

</details>

---

## Question 241: CLF-C02-ET-Q241
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which responsibility belongs to AWS when a company hosts its databases on Amazon EC2 instances?

**Choices:**
- A) Database backups
- B) Database software patches
- C) Operating system patches
- D) Operating system installations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `63%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (63%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS provides the infrastructure and services (like EC2) that include a range of Amazon Machine Images (AMIs) with pre-installed operating systems. This means AWS is responsible for ensuring that these AMIs are available and that the underlying infrastructure to run these instances is secure and reliable.

The other responsibilities listed - database backups (A), database software patches (B), and operating system patches (C) - are under the purview of the customer when using Amazon EC2 instances.
---
Selected Answer: D
A. Database backups - Customer responsibility. Customers are responsible for managing and maintaining backups of their data. AWS provides tools and services, but it's up to the customer to implement and manage backup strategies for their databases.

B. Database software patches - Customer responsibility. The customer is responsible for applying patches and updates to the database software running on their EC2 instances. This includes managing the software lifecycle, updates, and security patches.

C. Operating system patches - Customer responsibility. Similar to database software patches, the customer is responsible for applying patches and updates to the operating system of the EC2 instances. AWS manages the infrastructure, but the customer is responsible for the configuration and maintenance of their instance's operating systems.

D. Operating system installations - AWS responsibility. AWS takes care of installing and maintaining the operating system on the EC2 instances. This is part of the underlying infrastructure managed by AWS as a cloud service provider.
---
Selected Answer: C
Operating system patches

</details>

---

## Question 242: CLF-C02-ET-Q242
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are advantages of moving to the AWS Cloud? (Choose two.)

**Choices:**
- A) The ability to turn over the responsibility for all security to AWS.
- B) The ability to use the pay-as-you-go model.
- C) The ability to have full control over the physical infrastructure.
- D) No longer having to guess what capacity will be required.
- E) No longer worrying about users access controls.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B. The ability to use the pay-as-you-go model - AWS provides a flexible and cost-effective pay-as-you-go pricing model, allowing users to pay only for the resources they consume without upfront costs or long-term commitments.

D. No longer having to guess what capacity will be required - AWS offers scalable resources, enabling users to dynamically scale up or down based on their actual needs. This eliminates the need for upfront capacity planning and allows for efficient resource utilization.
---
B. The ability to use the pay-as-you-go model - AWS provides a flexible and cost-effective pay-as-you-go pricing model, allowing users to pay only for the resources they consume without upfront costs or long-term commitments.

D. No longer having to guess what capacity will be required - AWS offers scalable resources, enabling users to dynamically scale up or down based on their actual needs. This eliminates the need for upfront capacity planning and allows for efficient resource utilization.
---
Selected Answer: BD
B. The ability to use the pay-as-you-go model - AWS provides a flexible and cost-effective pay-as-you-go pricing model, allowing users to pay only for the resources they consume without upfront costs or long-term commitments.

D. No longer having to guess what capacity will be required - AWS offers scalable resources, enabling users to dynamically scale up or down based on their actual needs. This eliminates the need for upfront capacity planning and allows for efficient resource utilization.

Options A, C, and E are not accurate:

A. While AWS provides a secure cloud infrastructure, the overall responsibility for security is shared between AWS and the customer. Customers are responsible for securing their data and applications in the cloud.

C. AWS abstracts the physical infrastructure from users, providing a managed and abstracted environment. Users have control over their virtual resources, but AWS manages the physical infrastructure.

E. Users are still responsible for managing access controls and permissions for their applications and data in the AWS Cloud. AWS provides tools and services to assist in implementing access controls, but the responsibility remains with the customer.

</details>

---

## Question 243: CLF-C02-ET-Q243
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS services or tools can identify rightsizing opportunities for Amazon EC2 instances? (Choose two.)

**Choices:**
- A) AWS Cost Explorer
- B) AWS Billing Conductor
- C) Amazon CodeGuru
- D) Amazon SageMaker
- E) AWS Compute Optimizer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AE (100%). Contributor Answer: AE.

Community Rationale & Discussion:
Selected Answer: AE
A. AWS Cost Explorer

 AWS Cost Explorer provides cost and usage reports, allowing you to analyze your historical costs and usage patterns. While it doesn't directly identify rightsizing opportunities, it can help you understand your current spending and identify areas where rightsizing might be beneficial.

E. AWS Compute Optimizer

 AWS Compute Optimizer is a service that recommends optimal AWS resources for your workloads. It analyzes the historical utilization of your Amazon EC2 instances and provides recommendations for rightsizing, which involves changing the instance type to a better fit based on the workload's requirements.

B. AWS Billing Conductor

 There is no service called AWS Billing Conductor. 

C. Amazon CodeGuru

 Amazon CodeGuru is a service for automated code reviews and application performance recommendations. It is not specifically designed for identifying rightsizing opportunities.

D. Amazon SageMaker

 Amazon SageMaker is a service for building, training, and deploying machine learning models.
---
Selected Answer: AE
Both AWS Cost Explorer and AWS Compute Optimizer can help identify rightsizing opportunities for Amazon EC2 instances by analyzing usage patterns and recommending cost-effective options
---
Selected Answer: AE
valid answer

</details>

---

## Question 244: CLF-C02-ET-Q244
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is a hybrid cloud storage service that provides on-premises users access to virtually unlimited cloud storage?

**Choices:**
- A) AWS DataSync
- B) Amazon S3 Glacier
- C) AWS Storage Gateway
- D) Amazon Elastic Block Store (Amazon EBS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. AWS DataSync: A data transfer service that simplifies, automates, and accelerates moving large amounts of data between on-premises storage systems and AWS Cloud storage. It is focused on efficient data transfer.

B. Amazon S3 Glacier: A storage service designed for archiving and long-term backup of infrequently accessed data. It is suitable for data that is rarely accessed and requires low-cost storage. While it is a cloud storage service, it is not specifically designed for on-premises users to access virtually unlimited cloud storage.

C. AWS Storage Gateway: A hybrid cloud storage service that enables on-premises applications to use cloud storage seamlessly. It provides file, volume, and tape gateway interfaces to integrate on-premises environments with AWS Cloud storage. This service allows on-premises users to access virtually unlimited cloud storage while maintaining a hybrid storage infrastructure.

D. Amazon Elastic Block Store (Amazon EBS): Provides block-level storage volumes for use with Amazon EC2 instances. It is primarily focused on providing scalable and high-performance block storage for EC2 instances.
---
Selected Answer: C
C. AWS Storage Gateway: A hybrid cloud storage service that enables on-premises applications to use cloud storage seamlessly. It provides file, volume, and tape gateway interfaces to integrate on-premises environments with AWS Cloud storage. This service allows on-premises users to access virtually unlimited cloud storage while maintaining a hybrid storage infrastructure.
---
C. AWS Storage Gateway AWS Storage Gatewayneun onpeulemiseu aepeullikeisyeon-i AWS keullaudeu giban seutolijie wonhwalhage aegseseuhal su issdolog jiwonhaneun haibeulideu keullaudeu seutoliji seobiseu-ibnida. jaju aegseseuhaneun deiteoe daehan lokeol kaesileul jegonghayeo daegi sigan-i jjalb-eun aegseseuleul bojanghaneun dongsie naeguseong-gwa hwagjangseong-eul wihae deiteoleul keullaudeue jeojanghabnida.
자세히
204 / 5,000
번역 결과
번역 결과
C. AWS Storage Gateway AWS Storage Gateway is a hybrid cloud storage service that allows on-premises applications to seamlessly access AWS cloud-based storage. It provides a local cache for frequently accessed data to ensure low-latency access, while storing data in the cloud for durability and scalability.

</details>

---

## Question 245: CLF-C02-ET-Q245
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company plans to migrate to AWS and wants to create cost estimates for its AWS use cases.
Which AWS service or tool can the company use to meet these requirements?

**Choices:**
- A) AWS Pricing Calculator
- B) Amazon CloudWatch
- C) AWS Cost Explorer
- D) AWS Budgets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Pricing Calculator: A web-based tool that allows users to estimate the cost of using AWS services. It helps in understanding and estimating the costs associated with various AWS resources based on usage patterns, regions, and other parameters. Users can input their specific requirements to get an estimated monthly cost.

B. Amazon CloudWatch: A monitoring and observability service for AWS resources. 

C. AWS Cost Explorer: A tool within the AWS Management Console that provides visualization and analysis of AWS costs and usage. It allows users to view, understand, and analyze their historical AWS costs and usage data. While it provides insights into existing costs, it is not primarily a tool for creating initial cost estimates.

D. AWS Budgets: A service that allows users to set custom cost and usage budgets that alert them when they exceed their thresholds. It helps in managing costs by providing notifications based on cost and usage performance against defined budget targets. While it helps in budgeting and monitoring, it may not be the primary tool for creating detailed initial cost estimates.
---
Selected Answer: A
A. AWS Pricing Calculator: A web-based tool that allows users to estimate the cost of using AWS services. It helps in understanding and estimating the costs associated with various AWS resources based on usage patterns, regions, and other parameters. Users can input their specific requirements to get an estimated monthly cost.
---
A. Calculadora de precios de AWS

</details>

---

## Question 246: CLF-C02-ET-Q246
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which tool should a developer use to integrate AWS service features directly into an application?

**Choices:**
- A) AWS Software Development Kit
- B) AWS CodeDeploy
- C) AWS Lambda
- D) AWS Batch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Software Development Kit (SDK): A set of libraries and tools that allows developers to interact with AWS services directly from their applications. It provides APIs in various programming languages, enabling developers to integrate AWS services seamlessly into their applications. It abstracts the complexity of making direct API calls and provides a convenient way to interact with AWS resources.

B. AWS CodeDeploy: A service that automates code deployments to Amazon EC2 instances, on-premises instances, or serverless Lambda functions. 

C. AWS Lambda: A serverless compute service that lets developers run code without provisioning or managing servers. Developers can use Lambda to execute code in response to events, such as changes to data in an Amazon S3 bucket or an update to a DynamoDB table. 

D. AWS Batch: Enables developers to run batch computing workloads on the AWS Cloud. It allows users to define and run batch computing jobs efficiently.
---
Selected Answer: A
A. AWS Software Development Kit (SDK): A set of libraries and tools that allows developers to interact with AWS services directly from their applications. It provides APIs in various programming languages, enabling developers to integrate AWS services seamlessly into their applications. It abstracts the complexity of making direct API calls and provides a convenient way to interact with AWS resources.
---
Selected Answer: A
A is the correct answer

</details>

---

## Question 247: CLF-C02-ET-Q247
**Domain 1:** Cloud Concepts  

**Question:**  
Which of the following is a recommended design principle of the AWS Well-Architected Framework?

**Choices:**
- A) Reduce downtime by making infrastructure changes infrequently and in large increments.
- B) Invest the time to configure infrastructure manually.
- C) Learn to improve from operational failures.
- D) Use monolithic application design for centralization.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Reduce downtime by making infrastructure changes infrequently and in large increments: This statement goes against the best practices recommended by the AWS Well-Architected Framework. It's generally recommended to make frequent and smaller changes to infrastructure to reduce the risk of issues and improve overall system agility.

B. Invest the time to configure infrastructure manually: The AWS Well-Architected Framework encourages the use of automation to configure and manage infrastructure. Manual configuration is prone to errors, less scalable, and harder to maintain compared to automated approaches.

C. Learn to improve from operational failures: This is a key principle of the AWS Well-Architected Framework. It emphasizes the importance of learning from failures and continuously improving the architecture based on operational experiences. This involves implementing mechanisms for monitoring, logging, and analyzing failures to enhance system resilience.

D. Use monolithic application design for centralization: The AWS Well-Architected Framework generally favors a microservices architecture over a monolithic design. Microservices promote modularity, scalability, and flexibility.
---
Selected Answer: C
C. Learn to improve from operational failures: This is a key principle of the AWS Well-Architected Framework. It emphasizes the importance of learning from failures and continuously improving the architecture based on operational experiences. This involves implementing mechanisms for monitoring, logging, and analyzing failures to enhance system resilience.
---
C. Learn to improve from operational failures: This is a key principle of the AWS Well-Architected Framework. It emphasizes the importance of learning from failures and continuously improving the architecture based on operational experiences. This involves implementing mechanisms for monitoring, logging, and analyzing failures to enhance system resilience.

</details>

---

## Question 248: CLF-C02-ET-Q248
**Domain 2:** Security and Compliance  

**Question:**  
Using AWS Identity and Access Management (IAM) to grant access only to the resources needed to perform a task is a concept known as:

**Choices:**
- A) restricted access.
- B) as-needed access.
- C) least privilege access.
- D) token access.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `92%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (92%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Least privilege access: Least privilege access means granting users or entities the minimum level of permissions required to perform their tasks, reducing the risk of unintended or malicious actions.
---
C. Least privilege access: Least privilege access means granting users or entities the minimum level of permissions required to perform their tasks, reducing the risk of unintended or malicious actions.
---
Selected Answer: C
A. Restricted access: While the term "restricted access" is used in the context of limiting access, it is not a specific concept associated with IAM in AWS. It doesn't convey the principle of granting the minimum necessary permissions for a task.

B. As-needed access: This term is not a standard concept associated with IAM. However, it aligns somewhat with the idea of granting access based on specific needs.

C. Least privilege access: Least privilege access means granting users or entities the minimum level of permissions required to perform their tasks, reducing the risk of unintended or malicious actions.

D. Token access: "Token access" is not a standard term in the context of AWS IAM. Tokens are often associated with authentication and authorization, but the specific concept of least privilege access is better described by option C.

</details>

---

## Question 249: CLF-C02-ET-Q249
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool can be used to set up a firewall to control traffic going into and coming out of an Amazon VPC subnet?

**Choices:**
- A) Security group
- B) AWS WAF
- C) AWS Firewall Manager
- D) Network ACL

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `76%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (76%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
ACL = subnet, Security Groups = instances
---
Selected Answer: C
The Question states "AWS service or tool can be 'used' to set up a firewall" So option is C. And Network ACL is not a AWS service or tool. Correct me if i am wrong.
---
Selected Answer: C
Read carefully its`s a TRAP : "control traffic going into and coming out of an Amazon VPC subnet" - NOT AT SUBNET LEVEL 

in my opinion it means that - control traffic at higher level that VPC subnet. 

My answer is C - AWS Firewall manager

My explanation: 
network (ACL) allows or denies specific inbound or outbound traffic AT THE subnet level

</details>

---

## Question 250: CLF-C02-ET-Q250
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to operate a data warehouse to analyze data without managing the data warehouse infrastructure.
Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Aurora
- B) Amazon Redshift Serverless
- C) AWS Lambda
- D) Amazon RDS

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. Amazon Aurora: A relational database engine offered as part of Amazon RDS (Relational Database Service). While it is a high-performance database engine, it is optimized for transactional workloads rather than analytical processing typical of data warehouses.

B. Amazon Redshift: A fully managed, petabyte-scale data warehouse service in the cloud. It is specifically designed for analytics and data warehousing, offering fast query performance using SQL queries and integration with various business intelligence tools.

C. AWS Lambda: A serverless compute service that allows you to run code without provisioning or managing servers. It is event-driven and primarily used for executing code in response to events, such as changes in data or system state. 

D. Amazon RDS: A managed relational database service that supports various database engines like MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB. Similar to Amazon Aurora, it is optimized for transactional workloads rather than analytical processing.
---
Selected Answer: B
B. Amazon Redshift: A fully managed, petabyte-scale data warehouse service in the cloud. It is specifically designed for analytics and data warehousing, offering fast query performance using SQL queries and integration with various business intelligence tools.
---
Selected Answer: B
B. Amazon Redshift Serverless - key words "data warehouse"

</details>

---

## Question 251: CLF-C02-ET-Q251
**Domain 3:** Cloud Technology and Services  

**Question:**  
How does AWS Cloud computing help businesses reduce costs? (Choose two.)

**Choices:**
- A) AWS charges the same prices for services in every AWS Region.
- B) AWS enables capacity to be adjusted on demand.
- C) AWS offers discounts for Amazon EC2 instances that remain idle for more than 1 week.
- D) AWS does not charge for data sent from the AWS Cloud to the internet.
- E) AWS eliminates many of the costs of building and maintaining on-premises data centers.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
B. AWS enables capacity to be adjusted on demand: AWS provides the flexibility to scale resources up or down based on demand. This allows businesses to optimize costs by only paying for the resources they actually use, avoiding unnecessary expenses during periods of lower demand.

E. AWS eliminates many of the costs of building and maintaining on-premises data centers: With AWS, businesses can leverage cloud infrastructure without the need to invest in and maintain physical data centers. This eliminates upfront capital expenses, ongoing maintenance costs, and the need to overprovision resources for future growth, leading to significant cost savings.
---
Selected Answer: BE
B and E
---
Selected Answer: BE
Selected Answer: BE

</details>

---

## Question 252: CLF-C02-ET-Q252
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to grant users in one AWS account access to resources in another AWS account. The users do not currently have permission to access the resources.
Which AWS service will meet this requirement?

**Choices:**
- A) IAM group
- B) IAM role
- C) IAM tag
- D) IAM Access Analyzer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `92%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (92%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. IAM group: Containers for IAM users. They are used to simplify the management of IAM policies by allowing you to attach policies to a group and automatically apply those policies to all users in the group. However, IAM groups are not directly used for cross-account access.

B. IAM role: Are used to delegate permissions to users, applications, or services. In the context of cross-account access, you can create an IAM role in the target account and define policies that grant access to the necessary resources. Users in the source account can assume the role to access resources in the target account. IAM roles are commonly used for cross-account access scenarios.

C. IAM tag: Are metadata that you can assign to IAM users, groups, roles, and policies. While tags are useful for organizing and managing resources, they are not the primary mechanism for granting cross-account access.

D. IAM Access Analyzer: A tool that helps identify resources that are shared with an external entity or are publicly accessible. It is used for analyzing access across accounts, but not specifically for setting up cross-account access.
---
Selected Answer: B
B. IAM role: Are used to delegate permissions to users, applications, or services. In the context of cross-account access, you can create an IAM role in the target account and define policies that grant access to the necessary resources. Users in the source account can assume the role to access resources in the target account. IAM roles are commonly used for cross-account access scenarios.
---
Selected Answer: B
B. IAM role

</details>

---

## Question 253: CLF-C02-ET-Q253
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which task is the responsibility of AWS when using AWS services?

**Choices:**
- A) Management of IAM user permissions
- B) Creation of security group rules for outbound access
- C) Maintenance of physical and environmental controls
- D) Application of Amazon EC2 operating system patches

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `99%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (99%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Who set this answers, seriously??
---
Admin! Don't expect me to pay for premium when many of the questions are marked incorrect. Plus, not sure how the pricing is determined but it's very costly already.
---
Selected Answer: C
C. Maintenance of physical and environmental controls: This task is the responsibility of AWS. AWS manages the physical infrastructure, including data center security, environmental controls (such as cooling and power), and other aspects related to the underlying infrastructure.

</details>

---

## Question 254: CLF-C02-ET-Q254
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to migrate its application to AWS and run the application on Amazon EC2 instances. The application will have continuous usage for 1 year.

Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) Reserved Instances
- B) Spot Instances
- C) On-Demand Instances
- D) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (86%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Why not savings plan?
---
Selected Answer: A
Reserved Instances are well-suited for applications with steady, predictable workloads over a term commitment, such as one year
---
Selected Answer: A
A. Reserved Instances is correct

</details>

---

## Question 255: CLF-C02-ET-Q255
**Domain 2:** Security and Compliance  

**Question:**  
A company needs to transfer data between an Amazon S3 bucket and an on-premises application.

Who is responsible for the security of this data, according to the AWS shared responsibility model?

**Choices:**
- A) The company
- B) AWS
- C) Firewall vendor
- D) AWS Marketplace partner

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (86%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. The company

According to the AWS shared responsibility model, the customer is responsible for the security of data in transit between AWS services (such as an Amazon S3 bucket) and their on-premises applications. This includes implementing encryption, secure transfer protocols (e.g., HTTPS or SFTP), and network configurations to ensure data security.
---
Networking and traffic protection are a customer responsibility.
And of course Identity and Access Management which are needed when accessing an S3 bucket
---
Selected Answer: A
Networking and traffic protection are a customer responsibility. 
And of course Identity and Access Management which are needed when accessing an S3 bucket.

</details>

---

## Question 256: CLF-C02-ET-Q256
**Domain 1:** Cloud Concepts  

**Question:**  
Which pillar of the AWS Well-Architected Framework refers to the ability of a system to recover from infrastructure or service disruptions and dynamically acquire computing resources to meet demand?

**Choices:**
- A) Security
- B) Reliability
- C) Performance efficiency
- D) Cost optimization

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Reliability
---
Recover is the key word = B
---
https://aws.amazon.com/blogs/apn/the-6-pillars-of-the-aws-well-architected-framework/

</details>

---

## Question 257: CLF-C02-ET-Q257
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to identify Amazon S3 buckets that are shared with another AWS account.

Which AWS service or feature will meet these requirements?

**Choices:**
- A) AWS Lake Formation
- B) IAM credential report
- C) Amazon CloudWatch
- D) IAM Access Analyzer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D is correct
"IAM Access Analyzer:
• Find out which resources are shared
externally
• S3 Buckets
• IAM Roles
• KMS Keys
• Lambda Functions and Layers
• SQS queues
• Secrets Manager Secrets"
 upvoted 1
---
Selected Answer: D
D. IAM Access Analyzer
---
D. IAM Access Analyzer

IAM Access Analyzer helps you identify resources in your AWS account, such as S3 buckets, that are shared with external principals (including other AWS accounts). It continuously monitors resource policies for public and cross-account access to identify any unintended or risky configurations.

</details>

---

## Question 258: CLF-C02-ET-Q258
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service gives users the ability to build interactive business intelligence dashboards that include machine learning insights?

**Choices:**
- A) Amazon Athena
- B) Amazon Kendra
- C) Amazon QuickSight
- D) Amazon Redshift

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon QuickSight
Amazon QuickSight is a business intelligence (BI) service that enables users to create interactive dashboards and visualizations. It integrates with AWS data sources (e.g., Amazon S3, Amazon Redshift) and supports machine learning (ML) insights like anomaly detection and forecasting. These features allow users to gain deeper insights into their data and make data-driven decisions.
---
https://docs.aws.amazon.com/quicksight/
---
Selected Answer: C
https://docs.aws.amazon.com/quicksight/

</details>

---

## Question 259: CLF-C02-ET-Q259
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is an AWS value proposition that describes a user’s ability to scale infrastructure based on demand?

**Choices:**
- A) Speed of innovation
- B) Resource elasticity
- C) Decoupled architecture
- D) Global deployment

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Resource elasticity
---
Elasticity
---
Selected Answer: B
https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.elasticity.en.html
Elasticity
The ability to acquire resources as you need them and release resources when you no longer need them. In the cloud, you want to do this automatically.

</details>

---

## Question 260: CLF-C02-ET-Q260
**Domain 2:** Security and Compliance  

**Question:**  
Which action is a security best practice for access to sensitive data that is stored in an Amazon S3 bucket?

**Choices:**
- A) Enable S3 Cross-Region Replication (CRR) on the S3 bucket.
- B) Use IAM roles for applications that require access to the S3 bucket.
- C) Configure AWS WAF to prevent unauthorized access to the S3 bucket.
- D) Configure Amazon GuardDuty to prevent unauthorized access to the S3 bucket.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B is correct.

D: GuardDuty is a threat detection service, but it does not directly prevent unauthorized access to S3 buckets; it can identify suspicious activities.
---
Selected Answer: B
B. Use IAM roles for applications that require access to the S3 bucket
---
Selected Answer: B
Refer : https://docs.aws.amazon.com/AmazonS3/latest/userguide/list_amazons3.html

</details>

---

## Question 261: CLF-C02-ET-Q261
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to know more about the benefits offered by cloud computing. The company wants to understand the operational advantage of agility. How does AWS provide agility for users?

**Choices:**
- A) The ability the ensure high availability by deploying workloads to multiple regions
- B) A pay-as-you-go model for many services and resources
- C) The ability to transfer infrastructure management to the AWS Cloud
- D) The ability to provision and deprovision resources quickly with minimal effort

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. The ability to provision and deprovision resources quickly with minimal effort
---
Selected Answer: D
D. The ability to provision and deprovision resources quickly with minimal effort
---
D correct answer

</details>

---

## Question 262: CLF-C02-ET-Q262
**Domain 3:** Cloud Technology and Services  

**Question:**  
A developer wants to deploy an application quickly on AWS without manually creating the required resources.
Which AWS service will meet these requirements?

**Choices:**
- A) Amazon EC2
- B) AWS Elastic Beanstalk
- C) AWS CodeBuild
- D) Amazon Personalize

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
With Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.
---
Selected Answer: B
A. Amazon EC2: Amazon EC2 (Elastic Compute Cloud) provides resizable compute capacity in the cloud. While it allows you to manually create and configure virtual servers (EC2 instances), it involves more manual setup and is not as streamlined for quick application deployment as other services.

B. AWS Elastic Beanstalk: a fully managed service that simplifies the deployment of applications on AWS. It abstracts the underlying infrastructure, allowing developers to quickly deploy applications without manual resource creation. It is suitable for rapid application deployment.

C. AWS CodeBuild: a fully managed continuous integration service that compiles source code, runs tests, and produces software packages. While it is part of the CI/CD process, it is not focused on quick application deployment and resource provisioning.

D. Amazon Personalize: Amazon Personalize is a machine learning service for building personalized recommendation models. It is not designed for general application deployment and does not provide the infrastructure for quick deployment.
---
Selected Answer: B
AWS Elastic Beanstalk is a Platform as a Service (PaaS) that allows developers to deploy applications quickly without manually provisioning and managing the underlying infrastructure. It automatically handles resource provisioning, scaling, load balancing, and monitoring.

</details>

---

## Question 263: CLF-C02-ET-Q263
**Domain 2:** Security and Compliance  

**Question:**  
A company needs a central user portal so that users can log in to third-party business applications that support Security Assertion Markup Language (SAML) 2.0.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Identity and Access Management (IAM)
- B) Amazon Cognito
- C) AWS IAM Identity Center (AWS Single Sign-On)
- D) AWS CLI

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `51%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (51%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Cognito is correct answer. The user wants to login to THIRD PARTY APPLICATION Not to AWS SERVICES. Definition of Cognito - Amazon Cognito supports authentication with identity providers (IdPs) through Security Assertion Markup Language 2.0 (SAML 2.0). You can use an IdP that supports SAML with Amazon Cognito to provide a simple onboarding flow for your users. Support page - https://docs.aws.amazon.com/cognito/latest/developerguide/saml-identity-provider.html
---
Selected Answer: B
Cognito allows access by utilizing 3rd party identity provider. Providers include google, Amazon, Facebook. SAML 2.0 PROVIDERS, MICOROSFT Active Directory
---
Selected Answer: C
https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html

</details>

---

## Question 264: CLF-C02-ET-Q264
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service should users use to learn about AWS service availability and operations?

**Choices:**
- A) Amazon EventBridge
- B) AWS Service Catalog
- C) AWS Control Tower
- D) AWS Health Dashboard

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (91%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Health Dashboard. 

It provides personalized information about AWS service health events that might affect your resources. This dashboard gives visibility into the health of AWS services, enabling users to stay informed and take action as needed.
---
The correct answer is D.
---
The correct answer is D. AWS Health Dashboard.

The AWS Health Dashboard is a centralized location where users can find information about the availability and operation of AWS services. It provides an overview of the current status of AWS services, including planned and unplanned events. Users can also search for specific services to get more detailed information.

</details>

---

## Question 265: CLF-C02-ET-Q265
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool can be used to capture information about inbound and outbound traffic in an Amazon VPC?

**Choices:**
- A) VPC Flow Logs
- B) Amazon Inspector
- C) VPC endpoint services
- D) NAT gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. VPC Flow Logs
---
https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html
---
Selected Answer: A
https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

</details>

---

## Question 266: CLF-C02-ET-Q266
**Domain 2:** Security and Compliance  

**Question:**  
What is the customer ALWAYS responsible for managing, according to the AWS shared responsibility model?

**Choices:**
- A) Software licenses
- B) Networking
- C) Customer data
- D) Encryption keys

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
customers are always responsible for managing their own customer data
---
I think we have two answers: A and C
Software Licenses and Customer Data
---
Selected Answer: C
https://aws.amazon.com/compliance/shared-responsibility-model/

</details>

---

## Question 267: CLF-C02-ET-Q267
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service can be used to retrieve compliance reports on demand?

**Choices:**
- A) AWS Secrets Manager
- B) AWS Artifact
- C) AWS Security Hub
- D) AWS Certificate Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
correct
---
Selected Answer: B
B is correct!

</details>

---

## Question 268: CLF-C02-ET-Q268
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service enables users to check for vulnerabilities on Amazon EC2 instances by using predefined assessment templates?

**Choices:**
- A) AWS WAF
- B) AWS Trusted Advisor
- C) Amazon Inspector
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Inspector
---
Answer: C
https://aws.amazon.com/pt/inspector/
---
Selected Answer: C
C is correct

</details>

---

## Question 269: CLF-C02-ET-Q269
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to migrate to the AWS Cloud. The company is gathering information about its on-premises infrastructure and requires information such as the hostname, IP address, and MAC address.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS DataSync
- B) AWS Application Migration Service
- C) AWS Application Discovery Service
- D) AWS Database Migration Service (AWS DMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Application Discovery Service collects both server and database configuration information. Server information includes hostnames, IP addresses, MAC addresses, as well as the resource allocation and utilization details of key resources such as CPU, network, memory, and disk.
---
Selected Answer: C
https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html

https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html

https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html

https://aws.amazon.com/datasync/
---
C - AWS Application Discovery Service collects both server and database configuration information

</details>

---

## Question 270: CLF-C02-ET-Q270
**Domain 2:** Security and Compliance  

**Question:**  
Which action will help increase security in the AWS Cloud?

**Choices:**
- A) Enable programmatic access for all IAM users.
- B) Use IAM users instead of IAM roles to delegate permissions.
- C) Rotate access keys on a reoccurring basis.
- D) Use inline policies instead of customer managed policies.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
IAM access keys work as credentials for programmatic access. Credentials should be rotated or changed on a periodic time frame. For this reason it is considered a security best practice to rotate access keys.
---
Selected Answer: C
IAM access keys work as credentials for programmatic access. Credentials should be rotated or changed on a periodic time frame. For this reason it is considered a security best practice to rotate access keys.
---
C should rotate

</details>

---

## Question 271: CLF-C02-ET-Q271
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate its application to the AWS Cloud.

Which AWS tool or set of resources should the company use to analyze and assess its readiness for migration?

**Choices:**
- A) AWS Cloud Adoption Framework (AWS CAF)
- B) AWS Pricing Calculator
- C) AWS Well-Architected Framework
- D) AWS Budgets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `78%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (78%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-readiness/welcome.html
---
Selected Answer: A
A. AWS Cloud Adoption Framework (AWS CAF)

The AWS Cloud Adoption Framework (AWS CAF) is indeed designed to help organizations develop an effective strategy for adopting the AWS Cloud. It provides guidance on key aspects of cloud adoption, including business, people, governance, and technology considerations. While the AWS CAF does not directly offer a tool for analyzing readiness for migration, it does provide a comprehensive framework that can help organizations assess their readiness and plan their migration strategy effectively.
---
keywords = planning to migrate its application to the AWS Cloud

</details>

---

## Question 272: CLF-C02-ET-Q272
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following describes some of the core functionality of Amazon S3?

**Choices:**
- A) Amazon S3 is a high-performance block storage service that is designed for use with Amazon EC2.
- B) Amazon S3 is an object storage service that provides high-level performance, security, scalability, and data availability.
- C) Amazon S3 is a fully managed, highly reliable, and scalable file storage system that is accessible over the industry-standard SMB protocol.
- D) Amazon S3 is a scalable, fully managed elastic NFS for use with AWS Cloud services and on-premises resources.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
---
Selected Answer: B
S3 bucket = object storage
---
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

</details>

---

## Question 273: CLF-C02-ET-Q273
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is storing sensitive customer data in an Amazon S3 bucket. The company wants to protect the data from accidental deletion or overwriting.
Which S3 feature should the company use to meet these requirements?

**Choices:**
- A) S3 Lifecycle rules
- B) S3 Versioning
- C) S3 bucket policies
- D) S3 server-side encryption

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The Correct answer is B.

Versioning in Amazon S3 is a means of keeping multiple variants of an object in the same bucket. You can use the S3 Versioning feature to preserve, retrieve, and restore every version of every object stored in your buckets. 
Versioning-enabled buckets can help you recover objects from accidental deletion or overwrite. For example, if you delete an object, Amazon S3 inserts a delete marker instead of removing the object permanently. 
https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html
---
Selected Answer: B
A. S3 Lifecycle rules: Manages object lifecycle for storage optimization, not specifically designed for accidental deletion protection.

B. S3 Versioning: S3 Versioning is a feature that allows you to preserve, retrieve, and restore every version of every object stored in a bucket. Enabling versioning helps protect against accidental deletion or overwriting of data. When versioning is enabled, each new version of an object is assigned a unique version ID, and you can easily restore previous versions if needed.

C. S3 bucket policies: Defines access permissions, but does not inherently protect against accidental deletion or overwriting.

D. S3 server-side encryption: Encrypts data at rest for security but does not directly address accidental deletion or overwriting.
---
Selected Answer: B
S3 Versioning is a feature that protects data in an S3 bucket from accidental deletion or overwriting by keeping multiple versions of each object. When enabled, you can preserve, retrieve, and restore every version of an object stored in your bucket, ensuring that previous versions of an object remain intact even if it is deleted or overwritten.

</details>

---

## Question 274: CLF-C02-ET-Q274
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS benefit is demonstrated by on-demand technology services that enable companies to replace upfront fixed expenses with variable expenses?

**Choices:**
- A) High availability
- B) Economies of scale
- C) Pay-as-you-go pricing
- D) Global reach

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C IS Correct
---
c is correct
---
c is correct

</details>

---

## Question 275: CLF-C02-ET-Q275
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS services or features enable users to connect on-premises networks to a VPC? (Choose two.)

**Choices:**
- A) AWS VPN
- B) Elastic Load Balancing
- C) AWS Direct Connect
- D) VPC peering
- E) Amazon CloudFront

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
A. AWS VPN
B. Elastic Load Balancing - automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs)
C. AWS Direct Connect
D. VPC peering - Connection between VPC(not on premises)
E. Amazon CloudFront - content delivery network (CDN) service globally
---
Selected Answer: AC
A and C
---
Selected Answer: AC
A and C

</details>

---

## Question 276: CLF-C02-ET-Q276
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user needs to quickly deploy a nonrelational database on AWS. The user does not want to manage the underlying hardware or the database software.

Which AWS service can be used to accomplish this?

**Choices:**
- A) Amazon RDS
- B) Amazon DynamoDB
- C) Amazon Aurora
- D) Amazon Redshift

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Keyword: Deploy a nonrelational database on AWS

RDS- Fully managed Relational Database
Aurora- Relational Database for MySql and PostgreSql
Redshift- Data warehouse
DynamoDB- Fully managed Non-relational database in AWS

Answer is B. Amazon DynamoDB
---
Key= nonrelational database
---
Selected Answer: B
Amazon DynamoDB is nonrelational database on AWS

</details>

---

## Question 277: CLF-C02-ET-Q277
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which actions are examples of a company’s effort to rightsize its AWS resources to control cloud costs? (Choose two.)

**Choices:**
- A) Switch from Amazon RDS to Amazon DynamoDB to accommodate NoSQL datasets.
- B) Base the selection of Amazon EC2 instance types on past utilization patterns.
- C) Use Amazon S3 Lifecycle policies to move objects that users access infrequently to lower-cost storage tiers.
- D) Use Multi-AZ deployments for Amazon RDS.
- E) Replace existing Amazon EC2 instances with AWS Elastic Beanstalk.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (80%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
B. Base the selection of Amazon EC2 instance types on past utilization patterns and C. Use Amazon S3 Lifecycle policies to move objects that users access infrequently to lower-cost storage tiers.
---
Why not E? Can someone please explain to make the discussion complete?
---
Selected Answer: AC
This one is hard. I think it could be A, B and C. if the current workload demands for NoSQL capabilities are better suited for DynamoDB and the existing RDS resources are underutilized, migrating to DynamoDB can be a form of rightsizing. This migration aligns the resources more closely with the actual needs of the workload, potentially resulting in cost savings compared to maintaining underutilized RDS instances.

B is more an up front decision in the design phase, so A and C may be better answers here.

</details>

---

## Question 278: CLF-C02-ET-Q278
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service or feature can a company use to apply security rules to specific Amazon EC2 instances?

**Choices:**
- A) Network ACLs
- B) Security groups
- C) AWS Trusted Advisor
- D) AWS WAF

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Security groups = EC2 access control
ACL = VPC access control
---
Selected Answer: B
B is correct
---
Selected Answer: B
https://aviatrix.com/learn-center/cloud-security/aws-security-groups/#:~:text=As%20said%20earlier%2C%20security%20groups,them%20from%20the%20source%20IP.

</details>

---

## Question 279: CLF-C02-ET-Q279
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is using a third-party service to back up 10 TB of data to a tape library. The on-premises backup server is running out of space. The company wants to use AWS services for the backups without changing its existing backup workflows.
Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon Elastic Block Store (Amazon EBS)
- B) AWS Storage Gateway
- C) Amazon Elastic Container Service (Amazon ECS)
- D) AWS Lambda

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. Amazon Elastic Block Store (Amazon EBS): This service provides block-level storage volumes primarily used with Amazon EC2 instances. It may not be the best fit for backup scenarios involving tape libraries.

B. AWS Storage Gateway: This is a hybrid cloud storage service that seamlessly integrates on-premises applications with cloud storage. It supports various storage protocols, including Amazon S3 and Amazon Glacier, and allows on-premises data to be backed up to AWS without changing existing workflows.

C. Amazon Elastic Container Service (Amazon ECS): This service is for container orchestration and managing containerized applications. It is not directly related to back up scenarios or large-scale data storage.

D. AWS Lambda: This is a serverless compute service for running code in response to events.
---
Selected Answer: B
B. AWS Storage Gateway: This is a hybrid cloud storage service that seamlessly integrates on-premises applications with cloud storage. It supports various storage protocols, including Amazon S3 and Amazon Glacier, and allows on-premises data to be backed up to AWS without changing existing workflows.
---
Selected Answer: B
B AWS Storage Gateway

</details>

---

## Question 280: CLF-C02-ET-Q280
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS tool gives users the ability to plan their service usage, service costs, and instance reservations, and also allows them to set custom alerts when their costs or usage exceed established thresholds?

**Choices:**
- A) Cost Explorer
- B) AWS Budgets
- C) AWS Cost and Usage Report
- D) Reserved Instance reporting

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. Cost Explorer: Provides insights into AWS costs and usage, allowing users to analyze spending trends and breakdown costs by services, regions, and tags.

B. AWS Budgets: Enables users to plan service usage, set custom cost and usage budgets, and receive alerts when costs or usage exceed predefined thresholds.

C. AWS Cost and Usage Report: Provides detailed data on AWS costs and usage, offering hourly or daily usage, costs, and resource-level details for in-depth analysis and auditing.

D. Reserved Instance Reporting: Provides insights into the utilization and coverage of Reserved Instances, helping users understand how effectively Reserved Instances are utilized.
---
Selected Answer: B
B. AWS Budgets: Enables users to plan service usage, set custom cost and usage budgets, and receive alerts when costs or usage exceed predefined thresholds.
---
Selected Answer: B
You can create alerts on Budgets. Hence B is correct.

</details>

---

## Question 281: CLF-C02-ET-Q281
**Domain 2:** Security and Compliance  

**Question:**  
Which tasks are the customer’s responsibility, according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Establish the global infrastructure.
- B) Perform client-side data encryption.
- C) Configure IAM credentials.
- D) Secure edge locations.
- E) Patch Amazon RDS DB instances.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
Perform client-side data encryption: This task is the responsibility of the customer to encrypt data on the client side before sending it to AWS. It ensures that data is secure during transit.

Configure IAM credentials: Customers are responsible for configuring Identity and Access Management (IAM) credentials. This includes managing user accounts, permissions, and authentication mechanisms for accessing AWS resources.

Establish the global infrastructure: This is typically a task managed by AWS. AWS is responsible for setting up and managing the global infrastructure, including data centers and the underlying network.

Secure edge locations: AWS is responsible for securing its edge locations. This includes ensuring the physical security and proper operation of these locations.

Patch Amazon RDS DB instances: This is typically a task managed by AWS. AWS is responsible for applying updates and security patches to Amazon RDS DB instances to keep them up to date and secure. Customers are responsible for their data and configurations within the RDS instances.
---
Selected Answer: BC
B. Perform client-side data encryption.
C. Configure IAM credentials.
---
Perform client-side data encryption: This task is the responsibility of the customer to encrypt data on the client side before sending it to AWS. It ensures that data is secure during transit.

Configure IAM credentials: Customers are responsible for configuring Identity and Access Management (IAM) credentials. This includes managing user accounts, permissions, and authentication mechanisms for accessing AWS resources.

</details>

---

## Question 282: CLF-C02-ET-Q282
**Domain 2:** Security and Compliance  

**Question:**  
A developer has been hired by a large company and needs AWS credentials.
Which are security best practices that should be followed? (Choose two.)

**Choices:**
- A) Grant the developer access to only the AWS resources needed to perform the job.
- B) Share the AWS account root user credentials with the developer.
- C) Add the developer to the administrator’s group in AWS IAM.
- D) Configure a password policy that ensures the developer’s password cannot be changed.
- E) Ensure the account password policy requires a minimum length.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AE`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AE (91%). Contributor Answer: AE.

Community Rationale & Discussion:
Selected Answer: AE
A. Grant the developer access to only the AWS resources needed to perform the job: Following the principle of least privilege, it is advisable to provide the developer with access only to the specific AWS resources necessary for their job role. This minimizes the potential impact of security incidents and limits the scope of actions the developer can perform.

E. Ensure the account password policy requires a minimum length: Implementing a password policy that requires a minimum length is a good security practice. It helps enhance the strength of passwords and contributes to better overall account security. Longer passwords are generally more resistant to brute-force attacks.
---
A. Grant the developer access to only the AWS resources needed to perform the job: Following the principle of least privilege, it is advisable to provide the developer with access only to the specific AWS resources necessary for their job role. This minimizes the potential impact of security incidents and limits the scope of actions the developer can perform.

E. Ensure the account password policy requires a minimum length: Implementing a password policy that requires a minimum length is a good security practice. It helps enhance the strength of passwords and contributes to better overall account security. Longer passwords are generally more resistant to brute-force attacks.

Options B and C and D are not recommended
---
Selected Answer: AE
A. Grant the developer access to only the AWS resources needed to perform the job: Following the principle of least privilege, it is advisable to provide the developer with access only to the specific AWS resources necessary for their job role. This minimizes the potential impact of security incidents and limits the scope of actions the developer can perform.

E. Ensure the account password policy requires a minimum length: Implementing a password policy that requires a minimum length is a good security practice. It helps enhance the strength of passwords and contributes to better overall account security. Longer passwords are generally more resistant to brute-force attacks.

Options B and C and D are not recommended

</details>

---

## Question 283: CLF-C02-ET-Q283
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has multiple AWS accounts that include compute workloads that cannot be interrupted. The company wants to obtain billing discounts that are based on the company’s use of AWS services.
Which AWS feature or purchasing option will meet these requirements?

**Choices:**
- A) Resource tagging
- B) Consolidated billing
- C) Pay-as-you-go pricing
- D) Spot Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `97%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (97%). Contributor Answer: B.

Community Rationale & Discussion:
this site has lot of wrong answers lol..
---
Selected Answer: B
B. Consolidated billing.

Consolidated billing allows you to combine multiple AWS accounts and aggregate the usage and spending across those accounts. This simplifies billing and enables you to take advantage of volume discounts, which can lead to cost savings. Each account can still maintain its own resource tagging and pricing options, so it's possible to manage compute workloads in individual accounts as needed.
---
Selected Answer: B
pay-as-you-go pricing does not really offer volume discounts as much as it is a pay only for what you use, consolidated billing on the other hand provides discounts for users based on usage

</details>

---

## Question 284: CLF-C02-ET-Q284
**Domain 1:** Cloud Concepts  

**Question:**  
Which design principles support the reliability pillar of the AWS Well-Architected Framework? (Choose two.)

**Choices:**
- A) Perform operations as code.
- B) Enable traceability.
- C) Automatically scale to meet demand.
- D) Deploy resources globally to improve response time.
- E) Automatically recover from failure.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CE`  
**Community Consensus:** `73%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CE (73%). Contributor Answer: CE.

Community Rationale & Discussion:
Selected Answer: CE
C. Automatically scale to meet demand and E. Automatically recover from failure.
---
Selected Answer: CE
C. Automatically scale to meet demand: This principle ensures that your system can handle fluctuations in workload by automatically adjusting resources to match demand. By scaling resources dynamically, you can maintain performance and availability during periods of increased traffic or demand, thus enhancing the reliability of your application.

E. Automatically recover from failure: This principle emphasizes designing systems that can recover from failures automatically without manual intervention. Implementing automated recovery mechanisms such as auto-scaling groups, load balancers, and fault-tolerant architectures helps ensure that your application remains resilient in the face of failures, thereby improving reliability.
---
A. Perform operations as code --> Operational Excellence
B. Enable traceability --> Security
C. Automatically scale to meet demand --> Reliability
D. Deploy resources globally to improve response time --> Performance Efficiency
E. Automatically recover from failure --> Reliability

</details>

---

## Question 285: CLF-C02-ET-Q285
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company that uses AWS needs to transfer 2 TB of data.

Which type of transfer of that data would result in no cost for the company?

**Choices:**
- A) Inbound data transfer from the internet
- B) Outbound data transfer to the internet
- C) Data transfer between AWS Regions
- D) Data transfer between Availability Zones

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (71%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Ingress = Free
Egress =$$$
---
Selected Answer: D
D. Data transfer between Availability Zones. Both A and D would be the free options, but I would choose D since the questions states the company is already using AWS.
---
Hi team
i need to go from 1 to 719 or 719 to 1 which one is important can yuou please suggest

</details>

---

## Question 286: CLF-C02-ET-Q286
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to create templates that the company can reuse to deploy multiple AWS resources.

Which AWS service or feature can the company use to meet this requirement?

**Choices:**
- A) AWS Marketplace
- B) Amazon Machine Image (AMI)
- C) AWS CloudFormation
- D) AWS OpsWorks

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS CloudFormation

AWS CloudFormation allows users to define and provision AWS infrastructure and resources using templates. These templates are JSON or YAML files that describe the resources and their configurations in a declarative manner. With CloudFormation, users can create reusable templates that define the desired state of their infrastructure, including EC2 instances, VPCs, databases, and more. CloudFormation manages the provisioning and orchestration of resources, ensuring consistent and reliable deployments across environments.
---
Can someone please explain why AMI is not the right answer or whay in this case CloudFormation is a better answer?
---
Selected Answer: C
C is answer

</details>

---

## Question 287: CLF-C02-ET-Q287
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is building an application that requires the ability to send, store, and receive messages between application components. The company has another requirement to process messages in first-in, first-out (FIFO) order.

Which AWS service should the company use?

**Choices:**
- A) AWS Step Functions
- B) Amazon Simple Notification Service (Amazon SNS)
- C) Amazon Kinesis Data Streams
- D) Amazon Simple Queue Service (Amazon SQS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D for sure
---
Selected Answer: D
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
---
Selected Answer: D
Amazon SQS FIFO queues preserve the order in which messages are sent and received, and avoid that a message is processed more than once. This ensures that the messages are processed in first-in, first-out (FIFO) order1.

</details>

---

## Question 288: CLF-C02-ET-Q288
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature is a browser-based, pre-authenticated service that can be launched directly from the AWS Management Console?

**Choices:**
- A) AWS API
- B) AWS Lightsail
- C) AWS Cloud9
- D) AWS CloudShell

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console.
https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html
---
Selected Answer: D
AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console
---
Selected Answer: D
D is correct

</details>

---

## Question 289: CLF-C02-ET-Q289
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides the ability to manage infrastructure as code?

**Choices:**
- A) AWS CodePipeline
- B) AWS CodeDeploy
- C) AWS Direct Connect
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A. AWS CodePipeline: Focuses on continuous integration and delivery.

B. AWS CodeDeploy: Automates application deployments.

C. AWS Direct Connect: Provides dedicated network connections.

D. AWS CloudFormation: AWS CloudFormation is a service that allows you to define and provision AWS infrastructure as code. It enables you to use a template to describe and provision AWS resources in a repeatable and automated manner. With CloudFormation, you can manage your infrastructure as code, making it easier to version, replicate, and share infrastructure configurations.
---
Selected Answer: D
The Correct answer is D.

AWS CloudFormation lets you model, provision, and manage AWS and third-party resources by treating infrastructure as code.
https://aws.amazon.com/cloudformation/
---
Selected Answer: D
AWS CloudFormation allows you to manage and provision AWS resources as infrastructure as code (IaC). It uses templates to define the resources and configurations needed for your applications, enabling automated deployment and management of infrastructure.

</details>

---

## Question 290: CLF-C02-ET-Q290
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its database to a managed AWS service that is compatible with PostgreSQL.

Which AWS services will meet these requirements? (Choose two.)

**Choices:**
- A) Amazon Athena
- B) Amazon RDS
- C) Amazon EC2
- D) Amazon DynamoDB
- E) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
Amazon Aurora PostgreSQL is a fully managed, PostgreSQL–compatible.
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html
In addition to the benefits of Aurora, Aurora PostgreSQL offers a convenient migration pathway from Amazon RDS into Aurora, with push-button migration tools that convert your existing RDS for PostgreSQL applications to Aurora PostgreSQL.
---
Selected Answer: BE
BE is correct answer
---
Selected Answer: BE
BE are correct

</details>

---

## Question 291: CLF-C02-ET-Q291
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a fleet of cargo ships. The cargo ships have sensors that collect data at sea, where there is intermittent or no internet connectivity. The company needs to collect, format, and process the data at sea and move the data to AWS later.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS IoT Core
- B) Amazon Lightsail
- C) AWS Storage Gateway
- D) AWS Snowball Edge

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
You can import or export data between your local environments and Amazon S3, and physically transport the data with one or more devices without using the internet.
https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html
---
AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities
---
Selected Answer: D
D is correct

</details>

---

## Question 292: CLF-C02-ET-Q292
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company hosts an application on multiple Amazon EC2 instances. The application uses Amazon Simple Notification Service (Amazon SNS) to send messages.

Which AWS service or feature will give the application permission to access required AWS services?

**Choices:**
- A) AWS Certificate Manager (ACM)
- B) IAM roles
- C) AWS Security Hub
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Agree with IAM roles.
---
IAM provides fine-grained access control across all of AWS

</details>

---

## Question 293: CLF-C02-ET-Q293
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user has limited knowledge of AWS services, but wants to quickly deploy a scalable Node.js application in the AWS Cloud.

Which service should be used to deploy the application?

**Choices:**
- A) AWS CloudFormation
- B) AWS Elastic Beanstalk
- C) Amazon EC2
- D) AWS OpsWorks

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. AWS CloudFormation - is an infrastructure as code (IaC) service
B. AWS Elastic Beanstalk - deploying and scaling web applications and services developed with Java, . NET, PHP, Node. js, Python, Ruby
C. Amazon EC2 - Compute Service
D. AWS OpsWorks -help you automate operational tasks on AWS or on-premises
---
Selected Answer: B
Yes B is the correct answer.

AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, . NET, PHP, Node. js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and Internet Information Services (IIS).

</details>

---

## Question 294: CLF-C02-ET-Q294
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs a content delivery network that provides secure delivery of data, videos, applications, and APIs to users globally with low latency and high transfer speeds.

Which AWS service meets these requirements?

**Choices:**
- A) Amazon CloudFront
- B) Elastic Load Balancing
- C) Amazon S3
- D) Amazon Elastic Transcoder

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon CloudFront is a content delivery network (CDN) that helps deliver web content to users faster
---
Selected Answer: A
A is correct answer
---
Selected Answer: A
https://aws.amazon.com/cloudfront/

</details>

---

## Question 295: CLF-C02-ET-Q295
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to use third-party software for its workload on AWS.

Which AWS service or feature can the company use to purchase the software?

**Choices:**
- A) AWS Resource Access Manager
- B) AWS Managed Services
- C) AWS License Manager
- D) AWS Marketplace

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Marketplace is a curated digital catalog that you can use to find, buy, deploy, and manage third-party software, data, and services that you need to build solutions and run your businesses.
---
Selected Answer: D
https://docs.aws.amazon.com/marketplace/latest/userguide/what-is-marketplace.html
---
Selected Answer: D
https://docs.aws.amazon.com/marketplace/latest/userguide/what-is-marketplace.html

</details>

---

## Question 296: CLF-C02-ET-Q296
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs fully managed, highly reliable, and scalable file storage that is accessible over the Server Message Block (SMB) protocol.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon S3
- B) Amazon Elastic File System (Amazon EFS)
- C) Amazon FSx for Windows File Server
- D) Amazon Elastic Block Store (Amazon EBS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
. Amazon FSx for Windows File Server

(provides fully managed, highly reliable, and scalable file storage that is accessible over the industry-standard Service Message Block (SMB) protocol.

It is built on Windows Server, delivering a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration.)
---
Selected Answer: C
Amazon FSx for Windows File Server provides fully managed, highly reliable, and scalable file storage that is accessible over the industry-standard Server Message Block (SMB) protocol.
---
Selected Answer: C
C is correct

</details>

---

## Question 297: CLF-C02-ET-Q297
**Domain 2:** Security and Compliance  

**Question:**  
A company needs to centrally configure and manage Amazon VPC security groups across multiple AWS accounts within an organization in AWS Organizations.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS Firewall Manager
- B) Amazon GuardDuty
- C) Amazon Detective
- D) AWS WAF

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Firewall Manager is a security management service that allows you to centrally configure and manage firewall rules across your accounts and applications
---
Selected Answer: A
https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html
---
Selected Answer: A
A is correct

</details>

---

## Question 298: CLF-C02-ET-Q298
**Domain 2:** Security and Compliance  

**Question:**  
Which task is a responsibility of AWS, according to the AWS shared responsibility model?

**Choices:**
- A) Configure identity and access management for applications.
- B) Manage encryption options for data that is stored on AWS.
- C) Configure security groups for Amazon EC2 instances.
- D) Maintain the physical hardware of the infrastructure.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (90%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D is correct
---
A. Configure identity and access management for applications- customer responsibility
B. Manage encryption options for data that is stored on AWS- customer responsibility
C. Configure security groups for Amazon EC2 instances- customer responsibility
D. Maintain the physical hardware of the infrastructure- AWS responsibility
Correct answer is D
---
Selected Answer: D
D. Maintain the physical hardware of the infrastructure.

</details>

---

## Question 299: CLF-C02-ET-Q299
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has an Amazon EC2 instance in a private subnet. The company wants to initiate a connection to the internet to pull operating system updates while preventing traffic from the internet from accessing the EC2 instance.

Which AWS managed service allows this?

**Choices:**
- A) VPC endpoint
- B) NAT gateway
- C) Amazon PrivateLink
- D) VPC peering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. NAT gateway. NAT gateway allows instances in a private subnet to initiate outbound connections to the Internet, while preventing inbound connections.
---
Selected Answer: B
“ The NAT gateway lets the streaming instances in your private subnets connect to the internet or other AWS services, but prevents the internet from initiating a connection with those instances.”
---
Selected Answer: B
A NAT Gateway is an AWS service that allows a private subnet to have access to the Internet, but prevents the Internet from initiating a connection directly to the instances

</details>

---

## Question 300: CLF-C02-ET-Q300
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has deployed applications on Amazon EC2 instances. The company needs to assess application vulnerabilities and must identify infrastructure deployments that do not meet best practices.
Which AWS service can the company use to meet these requirements?

**Choices:**
- A) AWS Trusted Advisor
- B) Amazon Inspector
- C) AWS Config
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
Amazon Inspector for Audit
CloudWatch for monitoring
Config for compliance
---
Selected Answer: B
Inspector is all about security assessments of AWS based applications and their configurations against known vulnerabilities. GuardDuty is all about continuously and automatically process different foundational data sources such as CloudTrail event logs, VPC flow logs and DNS logs to find potential security threat over an entire AWS account not just only with applications and it also uses threat intelligence feeds, such as lists of malicious IP addresses and domains, and machine learning to identify unexpected, potentially unauthorized, and malicious activity within AWS environment. So as far as assessment is concerned Inspector is the right answer.
---
Selected Answer: B
Inspector for security assessments of applications

</details>

---

## Question 301: CLF-C02-ET-Q301
**Domain 3:** Cloud Technology and Services  

**Question:**  
An online gaming company needs to choose a purchasing option to run its Amazon EC2 instances for 1 year. The web traffic is consistent, and any increases in traffic are predictable. The EC2 instances must be online and available without any disruption.
Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) On-Demand Instances
- B) Reserved Instances
- C) Spot Instances
- D) Spot Fleet

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Reserved Instances are the most cost-effective purchasing option for workloads with predictable, steady usage patterns (like the online gaming company's consistent and predictable traffic). By committing to a one-year term, the company can save up to 75% compared to On-Demand pricing.
---
Selected Answer: B
Reserved instances
---
Selected Answer: B
B. Reserved Instances: Reserved Instances (RIs) provide a significant discount (compared to On-Demand Instances) in exchange for a commitment of one or three years. They are suitable for consistent, predictable workloads. RIs offer cost-effectiveness while ensuring the EC2 instances are online and available without disruptions

</details>

---

## Question 302: CLF-C02-ET-Q302
**Domain 2:** Security and Compliance  

**Question:**  
Which actions are the responsibility of AWS, according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Securing the virtualization layer
- B) Patching the operating system on Amazon EC2 instances
- C) Enforcing a strict password policy for IAM users
- D) Patching the operating system on Amazon RDS instances
- E) Configuring security groups and network ACLs

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (80%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
AD is correct answer
---
Selected Answer: AD
A. Securing the virtualization layer - AWS is responsible for securing physical hardware and the virtualization layer that runs AWS services. 
D. Patching the operating system on Amazon RDS instances. - AWS manages the underlying operating system and software stack with RDS.
---
Selected Answer: AD
A. Securing the virtualization layer
D. Patching the operating system on Amazon RDS instances

</details>

---

## Question 303: CLF-C02-ET-Q303
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is storing data that will not be frequently accessed in the AWS Cloud. If the company needs to access the data, the data needs to be retrieved within 12 hours. The company wants a solution that is cost-effective for storage costs for each gigabyte.

Which Amazon S3 storage class will meet these requirements?

**Choices:**
- A) S3 Standard
- B) S3 Glacier Flexible Retrieval
- C) S3 One Zone-Infrequent Access (S3 One Zone-IA)
- D) S3 Standard-Infrequent Access (S3 Standard-IA)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `65%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (65%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. S3 Glacier Flexible Retrieval - most cost-effective solution and standard retrievals can take up to 12 hours for retrieval, which suits the company's needs here.
---
S3 Glacier Flexible Retrieval: This storage class is designed for long-term archival of data that is infrequently accessed and where retrieval times of several hours are acceptable. It is the most cost-effective storage class for data that is retained for months, years, or decades. However, data retrieval times can range from a few minutes to several hours.

S3 One Zone-Infrequent Access (S3 One Zone-IA): This storage class is designed for data that is infrequently accessed but requires rapid access when needed. It stores data in a single availability zone, which makes it less expensive than other S3 storage classes, but also less resilient to availability zone failures. Data retrieval is typically instantaneous.

In the context of the question, if the company needs to access the data within 12 hours, both S3 Glacier Flexible Retrieval and S3 One Zone-IA could meet this requirement. However, S3 One Zone-IA would provide faster access times when the data is needed.
---
Selected Answer: C
. S3 One Zone-Infrequent Access (S3 One Zone-IA)

</details>

---

## Question 304: CLF-C02-ET-Q304
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or resource can be used to identify services that have been used by a user within a specified date range?

**Choices:**
- A) Amazon S3 access control lists (ACLs)
- B) AWS Certificate Manager (ACM)
- C) Network Access Analyzer
- D) AWS Identity and Access Management Access Analyzer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
IAM Access Analyzer is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in IAM Access Analyzer.
https://docs.aws.amazon.com/IAM/latest/UserGuide/logging-using-cloudtrail.html
---
Selected Answer: D
D looks correct

</details>

---

## Question 305: CLF-C02-ET-Q305
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to engage third-party consultants to help maintain and support its AWS environment and the company’s business needs.

Which AWS service or resource will meet these requirements?

**Choices:**
- A) AWS Support
- B) AWS Organizations
- C) AWS Service Catalog
- D) AWS Partner Network (APN)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. AWS Partner Network (APN)

The AWS Partner Network (APN) is designed to help companies find qualified third-party consultants, software vendors, and managed service providers who are specialized in working with AWS services. APN Partners offer various levels of support and expertise to assist with maintaining and optimizing AWS environments based on specific business needs.
---
Selected Answer: D
https://aws.amazon.com/partners/
---
Selected Answer: D
D is correct

</details>

---

## Question 306: CLF-C02-ET-Q306
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to create Amazon QuickSight dashboards every week by using its billing data.

Which AWS feature or tool can the company use to meet these requirements?

**Choices:**
- A) AWS Budgets
- B) AWS Cost Explorer
- C) AWS Cost and Usage Report
- D) AWS Cost Anomaly Detection

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
How Cost and Usage Reports work

After you create a Cost and Usage Report, AWS sends your report to the Amazon S3 bucket that you specify. AWS updates your report at least once a day until your charges are finalized.

Your report files consist of a .csv file or a collection of .csv files and a manifest file. You can choose to configure your report data for integration with Amazon Athena, Amazon Redshift, or Amazon QuickSight.
https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html
---
Selected Answer: C
QuickSight: create interactive dashboards, serverless
---
key word: create*, so it can't be B.

</details>

---

## Question 307: CLF-C02-ET-Q307
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to move data backups to the AWS Cloud. The company needs to replace on-premises storage with storage that is cloud-based but locally cached.

Which AWS service meets these requirements?

**Choices:**
- A) AWS Storage Gateway
- B) AWS Snowcone
- C) AWS Backup
- D) Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (91%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The correct answer is A. AWS Storage Gateway.

AWS Storage Gateway is a service that connects on-premises storage systems to AWS Cloud Storage Systems. It offers several deployment options, including an option that provides locally cached Cloud Storage.
---
Selected Answer: A
A. AWS Storage Gateway.
---
A. AWS Storage Gateway: It provides a hybrid cloud storage solution that allows you to seamlessly integrate on-premises environments with cloud storage. It offers different storage interfaces, including file, volume, and tape, and allows you to cache data locally for frequently accessed information while storing the entire dataset in the AWS Cloud. This setup enables efficient access to data stored in AWS while maintaining a local cache for performance.

</details>

---

## Question 308: CLF-C02-ET-Q308
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to organize its resources and track AWS costs on a detailed level. The company needs to categorize costs by business department, environment, and application.

Which solution will meet these requirements?

**Choices:**
- A) Access the AWS Cost Management console to organize resources, set an AWS budget, and receive notifications of unintentional usage.
- B) Use tags to organize the resources. Activate cost allocation tags to track AWS costs on a detailed level.
- C) Create Amazon CloudWatch dashboards to visually organize and track costs individually.
- D) Access the AWS Billing and Cost Management dashboard to organize and track resource consumption on a detailed level.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `83%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (83%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
tag is a label that you or AWS assigns to an AWS resource.You can use tags to organize your resources or billing purposes.
---
Selected Answer: B
B is correct answer
---
Selected Answer: B
B. Use tags to organize the resources. Activate cost allocation tags to track AWS costs on a detailed level.

</details>

---

## Question 309: CLF-C02-ET-Q309
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to plan, schedule, and run hundreds of thousands of computing jobs on AWS.

Which AWS service can the company use to meet this requirement?

**Choices:**
- A) AWS Step Functions
- B) AWS Service Catalog
- C) Amazon Simple Queue Service (Amazon SQS)
- D) AWS Batch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Batch is a service that allows you to run batch workloads on AWS.
---
Selected Answer: D
D looks pretty obvious
---
Selected Answer: D
D is correct
"AWS Batch
Fully managed batch processing at any scale
• Efficiently run 100,000s of computing batch jobs on AWS
• A “batch” job is a job with a start and an end (opposed to continuous)
• Batch will dynamically launch EC2 instances or Spot Instances
• AWS Batch provisions the right amount of compute / memory"

</details>

---

## Question 310: CLF-C02-ET-Q310
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS services or features provide high availability and low latency by enabling failover across different AWS Regions? (Choose two.)

**Choices:**
- A) Amazon Route 53
- B) Network Load Balancer
- C) Amazon S3 Transfer Acceleration
- D) AWS Global Accelerator
- E) Application Load Balancer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (86%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
AD is across regions
BE is across the smaller availability zones
---
Selected Answer: AD
A. Amazon Route 53 and D. AWS Global Accelerator.
---
Selected Answer: AD
A. Amazon Route 53: Amazon Route 53 is a scalable and highly available Domain Name System (DNS) web service. It supports routing policies that enable failover across different AWS Regions, ensuring high availability and low latency for end-users.

D. AWS Global Accelerator: AWS Global Accelerator improves the availability and performance of your applications with local or global users. It uses the AWS global network to optimize the path from your users to your applications, improving the availability and performance of your applications by sending user traffic to the closest healthy endpoint. It supports failover across different AWS Regions for enhanced availability.

</details>

---

## Question 311: CLF-C02-ET-Q311
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is a way to use Amazon EC2 Auto Scaling groups to scale capacity in the AWS Cloud?

**Choices:**
- A) Scale the number of EC2 instances in or out automatically, based on demand.
- B) Use serverless EC2 instances.
- C) Scale the size of EC2 instances up or down automatically, based on demand.
- D) Transfer unused CPU resources between EC2 instances.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
From what I remember, it works horizontally, so the first one makes most sense.
---
Selected Answer: A
A. Scale the number of EC2 instances in or out automatically, based on demand. - EC2 Auto Scaling adjusts the number of EC2 instances based on defined policies and demand.
---
Selected Answer: A
A is the right one since auto scaling is horizontal and answer C is about vertical scaling

</details>

---

## Question 312: CLF-C02-ET-Q312
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature allows a user to establish a dedicated network connection between a company’s on-premises data center and the AWS Cloud?

**Choices:**
- A) AWS Direct Connect
- B) VPC peering
- C) AWS VPN
- D) Amazon Route 53

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Direct Connect: AWS Direct Connect allows a user to establish a dedicated network connection between a company's on-premises data center and the AWS Cloud. It provides a private, dedicated network connection to enhance network performance and reliability.

B. VPC Peering: Connects two Virtual Private Clouds (VPCs) within AWS, allowing them to communicate with each other. 

C. AWS VPN: Provides a secure, encrypted connection between on-premises networks and AWS VPCs over the internet. 

D. Amazon Route 53: A scalable and highly available domain name system (DNS) web service.
---
Selected Answer: A
Which is used a s a direct connect
---
Selected Answer: A
WS Direct Connect provides a dedicated, private network connection between a company's on-premises data center and the AWS Cloud. This direct connection can help reduce network costs, improve bandwidth, and provide a more consistent network experience compared to internet-based connections.

</details>

---

## Question 313: CLF-C02-ET-Q313
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which abilities are benefits of the AWS Cloud? (Choose two.)

**Choices:**
- A) Trade variable expenses for capital expenses.
- B) Deploy globally in minutes.
- C) Plan capacity in advance of deployments.
- D) Take advantage of economies of scale.
- E) Reduce dependencies on network connectivity.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
A is wrong because is OpEx instead of CapEx.
C is wrong because do not have to plan capacity
E is wrong because Network connectivity is still required.
---
Selected Answer: BD
BD is correct
---
Selected Answer: BD
B and D

</details>

---

## Question 314: CLF-C02-ET-Q314
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS security service protects applications from distributed denial of service attacks with always-on detection and automatic inline mitigations?

**Choices:**
- A) Amazon Inspector
- B) AWS Web Application Firewall (AWS WAF)
- C) Elastic Load Balancing (ELB)
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS shield is a managed Distributed Denial of Service (DDoS) protection service
---
Selected Answer: D
D is correct
---
Selected Answer: D
D. AWS Shield

</details>

---

## Question 315: CLF-C02-ET-Q315
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service allows users to model and provision AWS resources using common programming languages?

**Choices:**
- A) AWS CloudFormation
- B) AWS CodePipeline
- C) AWS Cloud Development Kit (AWS CDK)
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `68%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (68%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Define your cloud infrastructure using a familiar programming language:
JavaScript/TypeScript, Python, Java, and .NET
Use existing IDE, testing tools, and workflow patterns
---
Selected Answer: C
C. AWS Cloud Development Kit (AWS CDK). - AWS CDK allows users to model and provision resources using familiar programming languages.
---
Selected Answer: C
YAML and JSON supported by CloudFormation are not programming languages.

</details>

---

## Question 316: CLF-C02-ET-Q316
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which Amazon EC2 instance pricing model can provide discounts of up to 90%?

**Choices:**
- A) Reserved Instances
- B) On-Demand
- C) Dedicated Hosts
- D) Spot Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (88%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Spot Instances: Get up to 90% discount compared to On demand
---
Selected Answer: D
D is correct
---
Selected Answer: D
D. Spot Instances

</details>

---

## Question 317: CLF-C02-ET-Q317
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following acts as an instance-level firewall to control inbound and outbound access?

**Choices:**
- A) Network access control list
- B) Security groups
- C) AWS Trusted Advisor
- D) Virtual private gateways

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Security Groups
---
Selected Answer: B
B. Security Groups - instance level
---
Selected Answer: B
B. Security groups.
Security groups act as a virtual firewall for your instances to control inbound and outbound traffic. They allow you to specify rules that control the traffic to and from your instances.

</details>

---

## Question 318: CLF-C02-ET-Q318
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company must be able to develop, test, and launch an application in the AWS Cloud quickly.

Which advantage of cloud computing will meet these requirements?

**Choices:**
- A) Stop guessing capacity
- B) Trade fixed expense for variable expense
- C) Achieve economies of scale
- D) Increase speed and agility

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Increase speed and agility
---
Selected Answer: D
D is correct
---
Selected Answer: D
Quickly = Agility

</details>

---

## Question 319: CLF-C02-ET-Q319
**Domain 2:** Security and Compliance  

**Question:**  
A company has teams that have different job roles and responsibilities. The company’s employees often change teams. The company needs to manage permissions for the employees so that the permissions are appropriate for the job responsibilities.

Which IAM resource should the company use to meet this requirement with the LEAST operational overhead?

**Choices:**
- A) IAM user groups
- B) IAM roles
- C) IAM instance profiles
- D) IAM policies for individual users

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `52%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (52%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: A
IAM user groups allow you to group users with similar job roles or responsibilities together. Instead of managing individual user permissions, you can assign IAM policies to these groups. When an employee changes teams or job roles, you can simply add or remove them from relevant user groups, and the permissions associated with the group will be applied automatically to the user.
---
Selected Answer: B
IAM roles are the most suitable resource for managing permissions in a scenario where employees frequently change teams and have different job roles and responsibilities. IAM roles allow you to define a set of permissions and policies and then assign those roles to users or AWS services as needed. This way, you can grant temporary access based on the user's current job responsibilities, and the users do not have to be directly assigned specific permissions.

IAM user groups (option A) are typically used to simplify the management of permissions for sets of users who share common job responsibilities. However, roles provide more flexibility in dynamic scenarios where users move between teams.
---
Selected Answer: A
IAM user groups allow you to group users with similar job roles or responsibilities together. Instead of managing individual user permissions, you can assign IAM policies to these groups. When an employee changes teams or job roles, you can simply add or remove them from relevant user groups, and the permissions associated with the group will be applied automatically to the user.
 upvoted 12 tim

</details>

---

## Question 320: CLF-C02-ET-Q320
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can a company use to securely store and encrypt passwords for a database?

**Choices:**
- A) AWS Shield
- B) AWS Secrets Manager
- C) AWS Identity and Access Management (IAM)
- D) Amazon Cognito

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Secrets Manager : Enables you to easily rotate, manage, and retrieve database
credentials, API keys, and other secrets throughout their lifecycle.
---
Selected Answer: B
B. AWS Secrets Manager.

AWS Secrets Manager is a service specifically designed for securely storing, retrieving, and managing sensitive information such as database credentials, API keys, and other secrets. It provides built-in encryption and integrates with AWS IAM for fine-grained access control. This makes it a suitable choice for securely managing passwords for a database.
---
Selected Answer: B
https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

</details>

---

## Question 321: CLF-C02-ET-Q321
**Domain 2:** Security and Compliance  

**Question:**  
What can a cloud practitioner use to retrieve AWS security and compliance documents and submit them as evidence to an auditor or regulator?

**Choices:**
- A) AWS Certificate Manager
- B) AWS Systems Manager
- C) AWS Artifact
- D) Amazon Inspector

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Artifact.

AWS Artifact is a portal that provides access to AWS security and compliance documents, including reports and certifications. It offers a central location for retrieving various documents, such as SOC reports, PCI DSS reports, and other compliance-related materials. These documents can then be submitted as evidence to auditors or regulators to demonstrate compliance with relevant standards and regulations.
---
Selected Answer: C
C is correct

</details>

---

## Question 322: CLF-C02-ET-Q322
**Domain 2:** Security and Compliance  

**Question:**  
Which encryption types can be used to protect objects at rest in Amazon S3? (Choose two.)

**Choices:**
- A) Server-side encryption with Amazon S3 managed encryption keys (SSE-S3)
- B) Server-side encryption with AWS KMS managed keys (SSE-KMS)
- C) TLS
- D) SSL
- E) Transparent Data Encryption (TDE)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AB`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AB (100%). Contributor Answer: AB.

Community Rationale & Discussion:
Selected Answer: AB
The encryption types that can be used to protect objects at rest in Amazon S3 are:

A. Server-side encryption with Amazon S3 managed encryption keys (SSE-S3)

B. Server-side encryption with AWS KMS managed keys (SSE-KMS)

These options provide encryption for data stored in Amazon S3. SSE-S3 and SSE-KMS encrypt data at the object level using encryption keys managed by Amazon S3 and AWS Key Management Service (KMS), respectively.
---
Selected Answer: AB
SSE S3/KMS correct answer
---
Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. T

Unless you specify otherwise, buckets use SSE-S3 by default to encrypt objects. However, you can choose to configure buckets to use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) instead.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html

</details>

---

## Question 323: CLF-C02-ET-Q323
**Domain 1:** Cloud Concepts  

**Question:**  
Which option is a physical location of the AWS global infrastructure?

**Choices:**
- A) AWS DataSync
- B) AWS Region
- C) Amazon Connect
- D) AWS Organizations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. AWS DataSync: AWS DataSync is a service for transferring large amounts of data between on-premises storage and Amazon S3. It is not related to the physical location of the AWS global infrastructure.

B. AWS Region: An AWS Region is a physical location in the world where AWS has multiple data centers. It represents a geographic area with multiple Availability Zones to provide fault tolerance and stability.

C. Amazon Connect: Amazon Connect is a cloud-based contact center service. It is not related to the physical infrastructure but rather provides customer service solutions.

D. AWS Organizations: AWS Organizations is a service for consolidating multiple AWS accounts into an organization. It is not related to the physical location of the AWS global infrastructure.
---
Selected Answer: B
A region is a physical location
---
Selected Answer: B
An AWS Region is a physical location where AWS has multiple data centers, known as Availability Zones. Each region is isolated from other regions to provide high availability and fault tolerance.

</details>

---

## Question 324: CLF-C02-ET-Q324
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to integrate its online shopping website with social media login credentials.

Which AWS service can the company use to make this integration?

**Choices:**
- A) AWS Directory Service
- B) AWS Identity and Access Management (IAM)
- C) Amazon Cognito
- D) AWS IAM Identity Center (AWS Single Sign-On)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon Cognito
---
Right answer is C
---
Selected Answer: C
The AWS service that the company can use to integrate its online shopping website with social media login credentials is:

C. Amazon Cognito.

Amazon Cognito provides user identity and data synchronization services that can be used to easily integrate social media login functionality into applications and websites. It supports various social identity providers such as Facebook, Google, and Amazon, allowing users to sign in with their existing social media accounts. Additionally, Cognito offers features for user authentication, authorization, and user management, making it well-suited for this integration scenario.

</details>

---

## Question 325: CLF-C02-ET-Q325
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is used to track, record, and audit configuration changes made to AWS resources?

**Choices:**
- A) AWS Shield
- B) AWS Config
- C) AWS IAM
- D) Amazon Inspector

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The AWS service used to track, record, and audit configuration changes made to AWS resources is:

B. AWS Config.

AWS Config provides a detailed inventory of your AWS resources and continuously records configuration changes to these resources. It allows you to assess, audit, and evaluate the configurations of your AWS infrastructure over time, helping you to maintain compliance, troubleshoot issues, and track changes.
---
Selected Answer: B
AWS Config:

AWS Config provides a detailed view of the resources associated with your AWS account, including how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time.
---
Selected Answer: B
AWS Config - does auditing and recording compliance of your AWS resources, record configurations and changes over time"

</details>

---

## Question 326: CLF-C02-ET-Q326
**Domain 3:** Cloud Technology and Services  

**Question:**  
A customer runs an On-Demand Amazon Linux EC2 instance for 3 hours, 5 minutes, and 6 seconds.

For how much time will the customer be billed?

**Choices:**
- A) 3 hours, 5 minutes
- B) 3 hours, 5 minutes, and 6 seconds
- C) 3 hours, 6 minutes
- D) 4 hours

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `56%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (56%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
You’ll be billed for the exact time used, so in this case, it’s 3 hours, 5 minutes, and 6 seconds—like paying for a movie ticket based on the exact runtime.
---
Selected Answer: B
Based on AWS docs https://aws.amazon.com/ec2/pricing/on-demand/
"Pricing is per instance-hour consumed for each instance, from the time an instance is launched until it is terminated or stopped. Each partial instance-hour consumed will be billed per-second for Linux, Windows, Windows with SQL Enterprise, Windows with SQL Standard, and Windows with SQL Web Instances, and as a full hour for all other OS types."

The question is about Linux, so it will be billed per second.
---
Selected Answer: D
EC2 bills in hours, so its rounded up

</details>

---

## Question 327: CLF-C02-ET-Q327
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company website is experiencing DDoS attacks.

Which AWS service can help protect the company website against these attacks?

**Choices:**
- A) AWS Resource Access Manager
- B) AWS Amplify
- C) AWS Shield
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Shield
---
Selected Answer: C
Maximize application availability and responsiveness with managed DDoS protection
https://aws.amazon.com/shield/
---
Selected Answer: C
C is correct: AWS Shield

</details>

---

## Question 328: CLF-C02-ET-Q328
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a customized assessment of its current on-premises environment. The company wants to understand its projected running costs in the AWS Cloud.

Which AWS service or tool will meet these requirements?

**Choices:**
- A) AWS Trusted Advisor
- B) Amazon Inspector
- C) AWS Control Tower
- D) Migration Evaluator

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Migration Evaluator provides the insights you need to build a data-driven business case for migration to AWS, helping define next steps in your migration journey.
---
Selected Answer: D
https://aws.amazon.com/about-aws/whats-new/2020/07/introducing-migration-evaluator-fast-track-business-case-aws/
---
Selected Answer: D
https://aws.amazon.com/free/migration/?trk=f3dc8b8f-681f-4a87-9d8d-371111880513&sc_channel=ps&ef_id=CjwKCAiAjrarBhAWEiwA2qWdCHWBrttn0ZH0CFTzhT7mfiSFlp2wwGSUP-qq9oKzb6ob1SYit_nSWxoCaAgQAvD_BwE:G:s&s_kwcid=AL!4422!3!536458997690!p!!g!!aws%20server%20migration!11543056234!112002961149&gclid=CjwKCAiAjrarBhAWEiwA2qWdCHWBrttn0ZH0CFTzhT7mfiSFlp2wwGSUP-qq9oKzb6ob1SYit_nSWxoCaAgQAvD_BwE

</details>

---

## Question 329: CLF-C02-ET-Q329
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company that has multiple business units wants to centrally manage and govern its AWS Cloud environments. The company wants to automate the creation of AWS accounts, apply service control policies (SCPs), and simplify billing processes.

Which AWS service or tool should the company use to meet these requirements?

**Choices:**
- A) AWS Organizations
- B) Cost Explorer
- C) AWS Budgets
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html
---
Selected Answer: A
AWS Organizations is a service that allows you to consolidate multiple AWS accounts into an organization that you create and centrally manage. It enables you to automate the creation of AWS accounts, apply Service Control Policies (SCPs) to manage permissions across accounts, and simplify billing by using consolidated billing.

</details>

---

## Question 330: CLF-C02-ET-Q330
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is hosting an application in the AWS Cloud. The company wants to verify that underlying AWS services and general AWS infrastructure are operating normally.

Which combination of AWS services can the company use to gather the required information? (Choose two.)

**Choices:**
- A) AWS Personal Health Dashboard
- B) AWS Systems Manager
- C) AWS Trusted Advisor
- D) AWS Service Health Dashboard
- E) AWS Service Catalog

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
A and D

While these two services may sound similar, the Service Health Dashboard provides the status of AWS services in general, whereas the Personal Health Dashboard gives you a personalized look into the availability and performance of the AWS services that you're actually using.
---
Selected Answer: AD
https://aws.amazon.com/about-aws/whats-new/2016/12/introducing-aws-personal-health-dashboard/
https://docs.aws.amazon.com/health/
---
Selected Answer: AD
AWS Personal Health Dashboard - gives you a personalized view of the status of the Amazon Web Services services that power your applications, enabling you to quickly see when Amazon Web Services is experiencing issues that may impact you.

AWS Health notifies you about service events, planned changes, and account notifications to help you manage and take actions

</details>

---

## Question 331: CLF-C02-ET-Q331
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to migrate a PostgreSQL database from on-premises to Amazon RDS.

Which AWS service or tool should the company use to meet this requirement?

**Choices:**
- A) Cloud Adoption Readiness Tool
- B) AWS Migration Hub
- C) AWS Database Migration Service (AWS DMS)
- D) AWS Application Migration Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Agree with C
---
Selected Answer: C
key - "Database" AWS Database Migration Service

AWS Cloud Readiness - See your responses and scores across the six AWS Cloud Adoption Framework (CAF) perspectives summarized in detail.

AWS Migration Hub provides a central location to collect server and application inventory data for the assessment, planning, and tracking of migrations

AWS Database Migration Service (AWS DMS) is a managed migration and replication service that helps you move your databases and analytics workloads to AWS quickly and securely. 

AWS Application Migration Service (AWS MGN) is the recommended service for migrations to AWS. AWS Application Migration Service simplifies and expedites your migration to AWS by automatically converting your source servers from physical, virtual, or cloud infrastructure to run natively on AWS.

</details>

---

## Question 332: CLF-C02-ET-Q332
**Domain 1:** Cloud Concepts  

**Question:**  
Which cloud concept is demonstrated by using AWS Compute Optimizer?

**Choices:**
- A) Security validation
- B) Rightsizing
- C) Elasticity
- D) Global reach

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Optimizer and rightsizing both have the letter "z" to help remember for the exam
---
Selected Answer: B
B. Rightsizing.

AWS Compute Optimizer analyzes the utilization metrics of your Amazon EC2 instances and provides recommendations for rightsizing them to improve performance and reduce costs. By suggesting the optimal instance types and sizes based on historical usage patterns, Compute Optimizer helps you ensure that your resources are appropriately provisioned to meet your workload requirements without overprovisioning or underprovisioning.
---
Selected Answer: B
B is correct

</details>

---

## Question 333: CLF-C02-ET-Q333
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company hosts a large amount of data in AWS. The company wants to identify if any of the data should be considered sensitive.

Which AWS service will meet the requirement?

**Choices:**
- A) Amazon Inspector
- B) Amazon Macie
- C) AWS Identity and Access Management (IAM)
- D) Amazon CloudWatch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Macie.

Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to automatically discover, classify, and protect sensitive data stored in Amazon S3. It continuously monitors data access activity for anomalies and provides alerts and insights to help you understand and protect your sensitive data.
---
Selected Answer: B
Amazon Macie
Discover and protect your sensitive data at scale
https://aws.amazon.com/macie/
---
B. Amazon Macie

Amazon Macie is specifically designed to help discover, classify, and protect sensitive data stored in AWS. It uses machine learning and pattern matching to automatically identify and classify sensitive data within various AWS services like S3 buckets, helping companies better understand their data and enforce security policies.

</details>

---

## Question 334: CLF-C02-ET-Q334
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user wants to allow applications running on an Amazon EC2 instance to make calls to other AWS services. The access granted must be secure.
Which AWS service or feature should be used?

**Choices:**
- A) Security groups
- B) AWS Firewall Manager
- C) IAM roles
- D) IAM user SSH keys

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (93%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
For allowing applications running on an Amazon EC2 instance to make secure calls to other AWS services, the recommended AWS service or feature is:

C. IAM roles

IAM (Identity and Access Management) roles provide a secure way to grant permissions to AWS services and resources. In this scenario, you can create an IAM role with the necessary permissions for the EC2 instance to access other AWS services. Then, you can associate the IAM role with the EC2 instance.

Option A (Security groups) is used for controlling inbound and outbound traffic to and from an EC2 instance, but it's not directly related to granting permissions to AWS services.
---
Selected Answer: C
C. IAM roles: Are used to grant secure and temporary access to AWS services. In this scenario, where a user wants to allow applications running on an Amazon EC2 instance to make calls to other AWS services, IAM roles should be used. IAM roles provide a secure way to delegate permissions to entities like EC2 instances without the need for long-term credentials.

Option A (Security groups) is used for controlling inbound and outbound traffic to EC2 instances but does not provide secure access to AWS services.

Option B (AWS Firewall Manager) is a service used for managing AWS WAF (Web Application Firewall) rules across accounts and applications, and it is not directly related to granting permissions to EC2 instances.

Option D (IAM user SSH keys) is specifically related to SSH key pairs for IAM users and is not the appropriate solution for granting access to AWS services from EC2 instances.
---
Selected Answer: C
C. IAM roles

IAM (Identity and Access Management) roles provide a secure way to grant permissions to AWS services and resources. In this scenario, you can create an IAM role with the necessary permissions for the EC2 instance to access other AWS services. Then, you can associate the IAM role with the EC2 instance.

</details>

---

## Question 335: CLF-C02-ET-Q335
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a fully managed Windows file server for its Windows-based applications.
Which AWS service will meet this requirement?

**Choices:**
- A) Amazon FSx
- B) Amazon Elastic Kubernetes Service (Amazon EKS)
- C) Amazon Elastic Container Service (Amazon ECS)
- D) Amazon EMR

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon FSx: A fully managed file storage service that is compatible with Windows file servers. It is designed to provide shared file storage for Windows-based applications, making it a suitable choice for the company's requirement of a fully managed Windows file server.

Option B (Amazon Elastic Kubernetes Service - Amazon EKS) and Option C (Amazon Elastic Container Service - Amazon ECS) are container orchestration services, not file storage services.

Option D (Amazon EMR) is Amazon Elastic MapReduce, which is a cloud-based big data platform, and it is not specifically designed for fully managed Windows file servers.
---
Selected Answer: A
Answer is A because:
Service Primary purpose Support for Windows file servers
Amazon FSx Managed file storage Yes
Amazon EKS Managed Kubernetes service No
Amazon ECS Managed container orchestration service No
Amazon EMR Managed Hadoop and Spark service No
---
Selected Answer: A
Answer is A because:
Service Primary purpose Support for Windows file servers
Amazon FSx Managed file storage Yes
Amazon EKS Managed Kubernetes service No
Amazon ECS Managed container orchestration service No
Amazon EMR Managed Hadoop and Spark service No

</details>

---

## Question 336: CLF-C02-ET-Q336
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is an advantage that users experience when they move on-premises workloads to the AWS Cloud?

**Choices:**
- A) Elimination of expenses for running and maintaining data centers
- B) Price discounts that are identical to discounts from hardware providers
- C) Distribution of all operational controls to AWS
- D) Elimination of operational expenses

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `95%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (95%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS removes the need for companies to invest in and maintain physical infrastructure.
---
Selected Answer: A
Option A elimination of expenses for running datacentres
---
Selected Answer: A
expenses are reduce

</details>

---

## Question 337: CLF-C02-ET-Q337
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its NFS on-premises workload to AWS.
Which AWS Storage Gateway type should the company use to meet this requirement?

**Choices:**
- A) Tape Gateway
- B) Volume Gateway
- C) Amazon FSx File Gateway
- D) Amazon S3 File Gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `72%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (72%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
I think this question is a little bit out of scope for this exam, but the AWS S3 File Gateway documentation specifically mentions NFS. You probably could also do C, but I think D is the "Best" answer

A. Tape Gateway: Is used for archiving data to Amazon S3 and Glacier. It is not designed for NFS workloads or migrating on-premises file-based workloads.

B. Volume Gateway: Is used for block storage volumes and might not be the most suitable option for NFS file workloads. It's more focused on block storage solutions.

C. Amazon FSx File Gateway: Provides a file interface to Amazon FSx file systems, which is compatible with Windows file servers. However, it may not be the optimal solution for migrating NFS workloads to AWS.

D. Amazon S3 File Gateway: Supports a file interface into Amazon S3 and allows storing and retrieving objects in Amazon S3 using industry-standard file protocols such as NFS. It is designed for scenarios where you want to integrate on-premises file-based applications with Amazon S3, making it suitable for migrating NFS workloads to AWS.
---
Selected Answer: D
D. Amazon S3 File Gateway: Supports a file interface into Amazon S3 and allows storing and retrieving objects in Amazon S3 using industry-standard file protocols such as NFS. It is designed for scenarios where you want to integrate on-premises file-based applications with Amazon S3, making it suitable for migrating NFS workloads to AWS.
---
Selected Answer: C
If the company is migrating an NFS-based workload (Network File System) from on-premises to AWS, Amazon FSx File Gateway is the best option. It is specifically designed to provide on-premises access to Amazon FSx for Windows File Server or Amazon FSx for Lustre file systems, which can support NFS protocols for file-based workloads.

Amazon FSx File Gateway enables seamless access to file data stored in Amazon FSx file systems via standard file protocols like NFS, which is ideal for companies migrating NFS workloads.

D. Amazon S3 File Gateway
Amazon S3 File Gateway provides access to Amazon S3 via file protocols like NFS and SMB, but it is mainly used for storing files in Amazon S3 and is not optimized for NFS workloads like Amazon FSx File Gateway. It may not provide the same level of performance and features needed for full NFS-based workloads.

</details>

---

## Question 338: CLF-C02-ET-Q338
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to track the activity in its AWS accounts, and needs to know when an API call is made against its AWS resources.
Which AWS tool or service can be used to meet these requirements?

**Choices:**
- A) Amazon CloudWatch
- B) Amazon Inspector
- C) AWS CloudTrail
- D) AWS IAM

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
"CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs, continuously monitors, and retains account activity related to actions across your AWS infrastructure, giving you control over storage, analysis, and remediation actions."

Reference: https://aws.amazon.com/cloudtrail/faqs/
---
CloudWatch is a monitoring service. CloudTrail is a web service that records API activity in your AWS account.
---
Selected Answer: C
A. CloudWatch - primarily for monitoring and managing resources but not API calls directly
B. Amazon Inspector - A security assessment service that helps improve the security and compliance of applications deployed on AWS not for tracking API usage
C. Enables customers to audit API calls in their AWS accounts by capturing and logging those calls. . It provides visibility into user and resource activity 
D. Manages permissions and identities, but does not record or log activity.

</details>

---

## Question 339: CLF-C02-ET-Q339
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to protect its AWS Cloud information, systems, and assets while performing risk assessment and mitigation tasks.
Which pillar of the AWS Well-Architected Framework is supported by these goals?

**Choices:**
- A) Reliability
- B) Security
- C) Operational excellence
- D) Performance efficiency

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Pillars of the AWS Well-Architected Framework:

 Operational Excellence: Focuses on operational practices that enable efficient management and operation of systems. It involves continuous improvement, monitoring, incident response, and evolving procedures over time.

 Security: Focuses on protecting information, systems, and assets. It involves implementing best practices for identity and access management, data protection, and risk assessment and mitigation.

 Reliability: Focuses on the ability of a system to recover from failures and meet customer expectations. It involves implementing best practices for resiliency, fault tolerance, and disaster recovery.

 Performance Efficiency: Focuses on using resources efficiently to maintain good performance. It involves optimizing workloads, selecting the right resources, and monitoring performance.

 Cost Optimization: Focuses on avoiding unnecessary costs and ensuring that resources are used efficiently. It involves optimizing costs, understanding pricing models, and using resources effectively.
---
Selected Answer: B
Security pillar is correct answer
---
Selected Answer: B
he Security pillar of the AWS Well-Architected Framework focuses on protecting AWS Cloud information, systems, and assets. This includes tasks like performing risk assessments, implementing security controls, and mitigating potential threats. It ensures that your workloads are protected against security risks and that data is handled securely.

</details>

---

## Question 340: CLF-C02-ET-Q340
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A user has a stateful workload that will run on Amazon EC2 for the next 3 years.

What is the MOST cost-effective pricing model for this workload?

**Choices:**
- A) On-Demand Instances
- B) Reserved Instances
- C) Dedicated Instances
- D) Spot Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Reserved Instances.

Reserved Instances (RIs) allow you to commit to a specific instance type in a specific AWS region for a term of 1 or 3 years, in exchange for a significant discount compared to On-Demand pricing. Since the workload is expected to run continuously for 3 years, committing to Reserved Instances would provide the most cost savings over the long term.
---
Selected Answer: B
D is wrong, Spot Instances is stateless
---
Selected Answer: B
https://aws.amazon.com/ec2/pricing/reserved-instances/

</details>

---

## Question 341: CLF-C02-ET-Q341
**Domain 2:** Security and Compliance  

**Question:**  
Who enables encryption of data at rest for Amazon Elastic Block Store (Amazon EBS)?

**Choices:**
- A) AWS Support
- B) AWS customers
- C) AWS Key Management Service (AWS KMS)
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `77%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (77%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Not sure, but going for B: While AWS KMS does the encryption on a technical level, the customer needs to initiate the configuration in AWS KMS to do the encryption?! Otherwise, there wouldn't be unencrypted devices. Found this "You can enable encryption automatically on all new EBS volumes and snapshot copies in your AWS account and Region." This "you" is the customer... semantics, I know. Still going for B.

https://docs.aws.amazon.com/kms/latest/developerguide/services-ebs.html
---
Selected Answer: B
The answer is B. The customer has to select AWS KMS. If the customer does not explicit select it then nothing will be encrypted. The question asks "who enables encryption" not what is used to encrypt. Therefore, since the user has to enable the service the answer should be B the user.
---
Selected Answer: B
Open the Amazon EC2 console at
Select the Region from the navigation bar
Select EC2 Dashboard from the navigation pane
Choose Account Attributes, then Data protection and security in the upper-right corner
In the EBS encryption section, choose Manage
Select Enable for Always encrypt new EBS volumes
Choose a default encryption key
Select Update EBS encryption

</details>

---

## Question 342: CLF-C02-ET-Q342
**Domain 3:** Cloud Technology and Services  

**Question:**  
What can a user accomplish using AWS CloudTrail?

**Choices:**
- A) Generate an IAM user credentials report.
- B) Record API calls made to AWS services.
- C) Assess the compliance of AWS resource configurations with policies and guidelines.
- D) Ensure that Amazon EC2 instances are patched with the latest security updates.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Record API calls made to AWS services.
---
Selected Answer: B
B is no doubt
---
B. Record API calls made to AWS services.

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. It records API calls made on your account, including who made the call, the services used, the actions performed, and when they occurred. This information is valuable for security analysis, resource change tracking, and troubleshooting.

</details>

---

## Question 343: CLF-C02-ET-Q343
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to host its workloads on AWS.

Which AWS service requires the company to update and patch the guest operating system?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon S3
- C) Amazon EC2
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches)
https://aws.amazon.com/compliance/shared-responsibility-model/
---
C. Amazon EC2

Amazon EC2 (Elastic Compute Cloud) is the AWS service that provides resizable compute capacity in the cloud. When you use EC2 instances, you have control over the guest operating system, and it is your responsibility to update and patch the operating system.

</details>

---

## Question 344: CLF-C02-ET-Q344
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature will search for and identify AWS resources that are shared externally?

**Choices:**
- A) Amazon OpenSearch Service
- B) AWS Control Tower
- C) AWS IAM Access Analyzer
- D) AWS Fargate

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS IAM Access Analyzer
---
C. AWS IAM Access Analyzer

AWS IAM Access Analyzer is a service that helps you identify and manage access permissions in your AWS environment. It includes the ability to analyze resource policies to check for unintended external sharing of resources. Access Analyzer can identify AWS resources that are shared externally, providing insights into potential security risks and allowing you to adjust access policies accordingly.
---
Selected Answer: C
https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html

</details>

---

## Question 345: CLF-C02-ET-Q345
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is migrating its workloads to the AWS Cloud. The company must retain full control of patch management for the guest operating systems that host its applications.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon EC2
- C) AWS Lambda
- D) Amazon RDS

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches)
https://aws.amazon.com/compliance/shared-responsibility-model/
---
B. Amazon EC2

Amazon EC2 (Elastic Compute Cloud) allows the company to retain full control over the guest operating systems, including patch management. With EC2, you have the flexibility to choose the operating system, configure security settings, and apply patches as needed. This level of control is suitable for scenarios where the company wants to manage the entire software stack, including the operating system.

</details>

---

## Question 346: CLF-C02-ET-Q346
**Domain 3:** Cloud Technology and Services  

**Question:**  
At what support level do users receive access to a support concierge?

**Choices:**
- A) Basic Support
- B) Developer Support
- C) Business Support
- D) Enterprise Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Enterprise Support: Account Assistance by Assigned Support Concierge
---
D. Enterprise Support

Users receive access to a support concierge at the Enterprise Support level. With AWS Enterprise Support, customers have access to a support concierge who can help with case management, provide guidance on best practices, and assist with various AWS-related inquiries. This level of support is designed for organizations with mission-critical workloads and larger-scale AWS implementations.
---
Selected Answer: D
https://aws.amazon.com/premiumsupport/plans/
AWS Enterprise On-Ramp

</details>

---

## Question 347: CLF-C02-ET-Q347
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can a company use to visually design and build serverless applications?

**Choices:**
- A) AWS Lambda
- B) AWS Batch
- C) AWS Application Composer
- D) AWS App Runner

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Application Composer helps you visually compose and configure AWS services into serverless applications backed by infrastructure as code
---
Selected Answer: C
C. AWS Application Composer
---
C isn't even on the exam objectives? How can it be C????

</details>

---

## Question 348: CLF-C02-ET-Q348
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to migrate to AWS and use the same security software it uses on premises. The security software vendor offers its security software as a service on AWS.

Where can the company purchase the security solution?

**Choices:**
- A) AWS Partner Solutions Finder
- B) AWS Support Center
- C) AWS Management Console
- D) AWS Marketplace

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D is correct
---
Selected Answer: D
D. AWS Marketplace - this is where you would purchase third party solutions

</details>

---

## Question 349: CLF-C02-ET-Q349
**Domain 2:** Security and Compliance  

**Question:**  
A company has deployed an Amazon EC2 instance.

Which option is an AWS responsibility under the AWS shared responsibility model?

**Choices:**
- A) Managing and encrypting application data
- B) Installing updates and security patches of guest operating system
- C) Configuration of infrastructure devices
- D) Configuration of security groups on each instance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (88%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C is correct
---
Selected Answer: C
C - Configuration of infrastructure
---
Selected Answer: C
C is correct

</details>

---

## Question 350: CLF-C02-ET-Q350
**Domain 3:** Cloud Technology and Services  

**Question:**  
What is the purpose of having an internet gateway within a VPC?

**Choices:**
- A) To create a VPN connection to the VPC
- B) To allow communication between the VPC and the internet
- C) To impose bandwidth constraints on internet traffic
- D) To load balance traffic from the internet across Amazon EC2 instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. To create a VPN connection to the VPC: VPN connections are typically established using Virtual Private Gateways rather than internet gateways. Internet gateways are not directly involved in VPN connections.

B. To allow communication between the VPC and the internet: The primary purpose of an internet gateway (IGW) within a Virtual Private Cloud (VPC) is to enable communication between resources in the VPC and the internet. It serves as a horizontally scaled, redundant component that allows outbound traffic from resources in the VPC to the internet and vice versa.

C. To impose bandwidth constraints on internet traffic: Internet gateways do not impose bandwidth constraints on internet traffic. 

D. To load balance traffic from the internet across Amazon EC2 instances: Load balancing of internet traffic is typically handled by services like Elastic Load Balancing (ELB) rather than the internet gateway.
---
B is correct.

"An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet."

Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html
---
Selected Answer: B
An internet gateway in a VPC (Virtual Private Cloud) is used to allow bi-directional communication between instances in the VPC and the internet. It is necessary for enabling internet access to and from resources inside the VPC, such as Amazon EC2 instances.

</details>

---

## Question 351: CLF-C02-ET-Q351
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its PostgreSQL database to AWS. The company does not use the database frequently.

Which AWS service or resource will meet these requirements with the LEAST management overhead?

**Choices:**
- A) PostgreSQL on Amazon EC2
- B) Amazon RDS for PostgreSQL
- C) Amazon Aurora PostgreSQL-Compatible Edition
- D) Amazon Aurora Serverless

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (71%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
If cost is not a concern and you want the least management overhead, Amazon Aurora Serverless would be the best option. Amazon Aurora Serverless provides the highest level of automation and scalability as it is a serverless database solution. You don't have to worry about managing database instances, scaling, or maintenance. The database automatically scales up and down to meet your application's requirements, and you only pay for the resources you actually use.

So, the correct answer in this case would be:

D. Amazon Aurora Serverless
---
Selected Answer: D
Amazon Aurora Serverless - automatically starts up, shuts down, and scales capacity up or down based on your application's needs, thus, reducing management overhead.*
Amazon Aurora PostgreSQL-Compatible Edition - a simple and cost-effective to set up, operate, and scale your new and existing PostgreSQL deployments.
Amazon RDS for PostgreSQL - deploy scalable PostgreSQL deployments in minutes with cost-efficient and resizable hardware capacity.
---
Selected Answer: D
Amazon Aurora Serverless is a fully managed database service that automatically adjusts capacity based on the workload. It is specifically designed for use cases where the database is not used frequently or has variable workloads. With Aurora Serverless, you only pay for the database capacity that you use, and it automatically scales up and down as needed. This makes it a great fit for applications with unpredictable or infrequent usage.

</details>

---

## Question 352: CLF-C02-ET-Q352
**Domain 2:** Security and Compliance  

**Question:**  
A company is using Amazon DynamoDB for its application database.

Which tasks are the responsibility of AWS, according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Classify data.
- B) Configure access permissions.
- C) Manage encryption options.
- D) Provide public endpoints to store and retrieve data.
- E) Manage the infrastructure layer and the operating system.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `DE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: DE (100%). Contributor Answer: DE.

Community Rationale & Discussion:
Selected Answer: DE
D. Provide public endpoints to store and retrieve data.
E. Manage the infrastructure layer and the operating system.
---
Selected Answer: DE
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
---
Selected Answer: DE
AWS responsibility “Security of the Cloud” - AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.
https://aws.amazon.com/dynamodb/faqs/

</details>

---

## Question 353: CLF-C02-ET-Q353
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to create a globally accessible ecommerce platform for its customers. The company wants to use a highly available and scalable DNS web service to connect users to the platform.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon EC2
- B) Amazon VPC
- C) Amazon Route 53
- D) Amazon RDS

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon Route 53
---
Selected Answer: C
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service.
https://docs.aws.amazon.com/route53/
---
C. Amazon Route 53

Amazon Route 53 is a scalable and highly available Domain Name System (DNS) web service provided by AWS. It is designed to route end-user requests to endpoints, such as Amazon EC2 instances, AWS Elastic Load Balancers, or other resources. Route 53 provides a reliable and cost-effective way to ensure that users can access your globally distributed ecommerce platform with low-latency and high availability.

</details>

---

## Question 354: CLF-C02-ET-Q354
**Domain 2:** Security and Compliance  

**Question:**  
Which maintenance task is the customer’s responsibility, according to the AWS shared responsibility model?

**Choices:**
- A) Physical connectivity among Availability Zones
- B) Network switch maintenance
- C) Hardware updates and firmware patches
- D) Amazon EC2 updates and security patches

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon EC2 updates and security patches
---
Selected Answer: D
Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches)
https://aws.amazon.com/compliance/shared-responsibility-model/
---
EC2 is solely customer responsibility

</details>

---

## Question 355: CLF-C02-ET-Q355
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to improve its security posture by reviewing user activity through API calls.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS WAF
- B) Amazon Detective
- C) Amazon CloudWatch
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS CloudTrail
---
Selected Answer: D
لانه قال يوزر
---
Selected Answer: D
https://docs.aws.amazon.com/cloudtrail/

</details>

---

## Question 356: CLF-C02-ET-Q356
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is migrating to the AWS Cloud and plans to run experimental workloads for 3 to 6 months on AWS.

Which pricing model will meet these requirements?

**Choices:**
- A) Use Savings Plans for a 3-year term.
- B) Use Dedicated Hosts.
- C) Buy Reserved Instances.
- D) Use On-Demand Instances.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Use On-Demand Instances.

On-Demand Instances provide flexibility and require no upfront commitment. You pay for the compute capacity by the hour or by the second, with no long-term contracts or upfront payments. This model is ideal for short-term workloads, experimental projects, or situations where the workload's duration is uncertain. It allows you to scale up or down as needed without any commitments, making it the most appropriate choice for the company's requirements.
---
Selected Answer: D
I think D is correct, because the company requires short-term but continuous computing resources.

</details>

---

## Question 357: CLF-C02-ET-Q357
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company that has AWS Enterprise Support is launching a new version of a popular product in 2 months. The company expects a large increase in traffic to its website. The website is hosted on Amazon EC2 instances.

Which action should the company take to assess its readiness to scale for this launch?

**Choices:**
- A) Replace the EC2 instances with AWS Lambda functions.
- B) Use AWS Infrastructure Event Management (IEM) support.
- C) Submit a request on AWS Marketplace to monitor the event.
- D) Review the coverage reports in the AWS Cost Management console.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Use AWS Infrastructure Event Management (IEM) support. This is offered to Enterprise Support customers to help plan for big changes
---
Selected Answer: B
B. Use AWS Infrastructure Event Management (IEM) support.

AWS Infrastructure Event Management (IEM) support helps customers prepare for and respond to events that could impact their AWS infrastructure, such as product launches or traffic spikes. It provides proactive guidance, best practices, and recommendations tailored to the company's specific situation and requirements. By leveraging IEM support, the company can ensure that its AWS infrastructure is properly configured, optimized, and ready to handle the anticipated increase in website traffic.
---
Selected Answer: B
https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html

</details>

---

## Question 358: CLF-C02-ET-Q358
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to launch multiple workloads on AWS. Each workload is related to a different business unit. The company wants to separate and track costs for each business unit.

Which solution will meet these requirements with the LEAST operational overhead?

**Choices:**
- A) Use AWS Organizations and create one account for each business unit.
- B) Use a spreadsheet to control the owners and cost of each resource.
- C) Use an Amazon DynamoDB table to record costs for each business unit.
- D) Use the AWS Billing console to assign owners to resources and track costs.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `82%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (82%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A is correct
---
Selected Answer: A
A. Use AWS Organizations and create one account for each business unit. - AWS Organizations allows you to organize all accounts under one master/management account. Then you can easily track costs.
---
Selected Answer: A
A. Use AWS Organizations and create one account for each business unit.

AWS Organizations allows you to centrally manage and govern multiple AWS accounts. By creating separate AWS accounts for each business unit, the company can easily separate and track costs for each unit. AWS provides consolidated billing, which aggregates the charges for all linked accounts in a single bill while still allowing detailed cost reporting at the account level. This approach provides a clean separation of costs for each business unit with minimal operational overhead.

</details>

---

## Question 359: CLF-C02-ET-Q359
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a time-series database service that makes it easier to store and analyze trillions of events each day.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Neptune
- B) Amazon Timestream
- C) Amazon Forecast
- D) Amazon DocumentDB (with MongoDB compatibility)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Timestream
---
Selected Answer: B
https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html
---
Selected Answer: B
https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html

</details>

---

## Question 360: CLF-C02-ET-Q360
**Domain 2:** Security and Compliance  

**Question:**  
Which option is a shared control between AWS and the customer, according to the AWS shared responsibility model?

**Choices:**
- A) Configuration management
- B) Physical and environmental controls
- C) Data integrity authentication
- D) Identity and access management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
remember AWS is responsible for everything of the cloud and the customer is responsible for everything in the cloud so A and D could be correct if this were a two part answer question but A is the best for the real exam.
---
A. Configuration management

In the AWS shared responsibility model, configuration management is a shared control. AWS is responsible for the infrastructure's configuration management, including the configuration of the hardware, software, networking, and facilities that run AWS services.

On the other hand, the customer is responsible for configuration management at the application level, including the security configuration of AWS provided services such as Amazon EC2 instances, Amazon S3 buckets, and Amazon DynamoDB tables.

So, both AWS and the customer have responsibilities when it comes to configuration management, making it a shared control.
---
Selected Answer: A
The answer is A

</details>

---

## Question 361: CLF-C02-ET-Q361
**Domain 1:** Cloud Concepts  

**Question:**  
A company is running a monolithic on-premises application that does not scale and is difficult to maintain. The company has a plan to migrate the application to AWS and divide the application into microservices.
Which best practice of the AWS Well-Architected Framework is the company following with this plan?

**Choices:**
- A) Integrate functional testing as part of AWS deployment.
- B) Use automation to deploy changes.
- C) Deploy the application to multiple locations.
- D) Implement loosely coupled dependencies.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
The Correct answer is D.

Dependencies such as queuing systems, streaming systems, workflows, and load balancers are loosely coupled. Loose coupling helps isolate behavior of a component from other components that depend on it, increasing resiliency and agility.
https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_prevent_interaction_failure_loosely_coupled_system.html
---
Selected Answer: D
breaking a monolithic application into microservices is an example of implementing loose coupling between application components, allowing better scalability and easier maintenance.
---
Selected Answer: D
Implementing Loosely coupled components - Option D

</details>

---

## Question 362: CLF-C02-ET-Q362
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company often does not use all of its current Amazon EC2 capacity to run stateless workloads. The company wants to optimize its EC2 costs.

Which EC2 instance type will meet these requirements?

**Choices:**
- A) Spot Instances
- B) Dedicated Instances
- C) Reserved Instances
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Spot Instances
---
Selected Answer: A
stateless workloads
---
Selected Answer: A
Spot Instances are recommended for stateless, fault-tolerant, flexible applications.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html

</details>

---

## Question 363: CLF-C02-ET-Q363
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to store data in Amazon S3. The company rarely access the data, and the data can be regenerated if necessary. The company wants to store the data in the most cost-effective storage class.

Which S3 storage class will meet this requirement?

**Choices:**
- A) S3 Standard
- B) S3 Intelligent-Tiering
- C) S3 Standard-Infrequent Access (S3 Standard-IA)
- D) S3 One Zone-Infrequent Access (S3 One Zone-IA)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `84%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (84%). Contributor Answer: D.

Community Rationale & Discussion:
D. S3 One Zone-Infrequent Access (S3 One Zone-IA)

For a scenario where data is rarely accessed, and the company can regenerate the data if needed, the most cost-effective storage class would be S3 One Zone-Infrequent Access (S3 One Zone-IA). This storage class stores data in a single availability zone, providing cost savings compared to storage classes that store data redundantly across multiple availability zones.
---
Selected Answer: D
S3 One Zone-IA is ideal for customers who want a lower-cost option for infrequently accessed
---
Selected Answer: D
D. S3 One Zone-Infrequent Access (S3 One Zone-IA) - most cost effective solution that is ideal for data that can be easily recreated and not critical if lost.

</details>

---

## Question 364: CLF-C02-ET-Q364
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has migrated its workloads to AWS. The company wants to adopt AWS at scale and operate more efficiently and securely. Which AWS service or framework should the company use for operational support?

**Choices:**
- A) AWS Support
- B) AWS Cloud Adoption Framework (AWS CAF)
- C) AWS Managed Services (AMS)
- D) AWS Well-Architected Framework

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `81%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (81%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Managed Services (AMS) helps you adopt AWS at scale and operate more efficiently and securely. We leverage standard AWS services and offer operational guidance with specialized automations, skills, and experience that are contextual to your environment and applications
---
Selected Answer: C
The AWS Cloud Adoption Framework (AWS CAF) helps organizations transition to the cloud by providing guidance and best practices across multiple dimensions, including business, people, governance, platform, security, and operations. It is designed specifically for companies that want to adopt AWS at scale and operate more efficiently and securely. AWS CAF enables organizations to build a comprehensive approach for cloud adoption, ensuring the right processes, resources, and practices are in place.
---
Selected Answer: C
C. AWS Managed Services (AMS) - provides ongoing operational support for AWS workloads.

</details>

---

## Question 365: CLF-C02-ET-Q365
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to provision and manage its AWS infrastructure by using the common programming languages Typescript, Python, Java, and .NET.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS CodeBuild
- B) AWS CloudFormation
- C) AWS CLI
- D) AWS Cloud Development Kit (AWS CDK)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Cloud Development Kit (AWS CDK)

AWS CDK is an open-source software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. It supports multiple programming languages, including TypeScript, Python, Java, and .NET, allowing developers to use familiar programming languages to define AWS infrastructure as code.
---
Selected Answer: D
D is the answer
---
Selected Answer: D
It is D of course

</details>

---

## Question 366: CLF-C02-ET-Q366
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which Amazon EC2 pricing model provides the MOST cost savings for an always-up, right-sized database server running for a project that will last 1 year?

**Choices:**
- A) On-Demand Instances
- B) Convertible Reserved Instances
- C) Spot Instances
- D) Standard Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `84%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (84%). Contributor Answer: D.

Community Rationale & Discussion:
Crazy how correct answers are not being provided by this platform which are charging an absolute arm and a leg for this service ;(
---
Selected Answer: D
D. Standard Reserved Instances
---
Selected Answer: D
the system is already right sized so not need to adjust.

</details>

---

## Question 367: CLF-C02-ET-Q367
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a physical tape library to store data backups. The tape library is running out of space. The company needs to extend the tape library's capacity to the AWS Cloud.

Which AWS service should the company use to meet this requirement?

**Choices:**
- A) Amazon Elastic File System (Amazon EFS)
- B) Amazon Elastic Block Store (Amazon EBS)
- C) Amazon S3
- D) AWS Storage Gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Storage Gateway connects an on-premises software appliance with cloud-based storage to provide seamless integration with data security features between your on-premises IT environment and the AWS storage infrastructure. You can use the service to store data in the Amazon Web Services Cloud for scalable and cost-effective storage that helps maintain data security.

AWS Storage Gateway offers file-based File Gateways (Amazon S3 File and Amazon FSx File), volume-based (Cached and Stored), and tape-based storage solutions.
https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html
---
Selected Answer: D
D. AWS Storage Gateway
---
Selected Answer: D
Correct answer D

</details>

---

## Question 368: CLF-C02-ET-Q368
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is using the AWS Free Tier for several AWS services for an application.

What will happen if the Free Tier usage period expires or if the application use exceeds the Free Tier usage limits?

**Choices:**
- A) The company will be charged the standard pay-as-you-go service rates for the usage that exceeds the Free Tier usage.
- B) AWS Support will contact the company to set up standard service charges.
- C) The company will be charged for the services it consumed during the Free Tier period, plus additional charges for service consumption after the Free Tier period.
- D) The company's AWS account will be frozen and can be restarted after a payment plan is established.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. The company will be charged the standard pay-as-you-go service rates for the usage that exceeds the Free Tier usage.
---
Selected Answer: A
A. The company will be charged the standard pay-as-you-go service rates for the usage that exceeds the Free Tier usage.

AWS will start billing the company for the services used beyond the Free Tier limits or after the Free Tier period ends at the standard pay-as-you-go rates. The charges will appear on the company's AWS bill according to the pricing of each respective service.
---
Selected Answer: A
100% voted for A and the platform still marks different answer as corret? Why?

</details>

---

## Question 369: CLF-C02-ET-Q369
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to monitor its workload performance. The company wants to ensure that the cloud services are delivered at a level that meets its business needs.

Which AWS Cloud Adoption Framework (AWS CAF) perspective will meet these requirements?

**Choices:**
- A) Business
- B) Governance
- C) Platform
- D) Operations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (93%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Operations
---
Selected Answer: D
The Operations perspective in the AWS CAF focuses on managing and monitoring the performance and health of cloud resources and services
---
Selected Answer: D
D. Operations

The Operations perspective in AWS CAF focuses on managing and optimizing workloads, ensuring operational excellence, and monitoring performance to meet business requirements. It includes practices related to workload monitoring, performance optimization, incident management, and continuous improvement to ensure that cloud services are delivered effectively and efficiently.

</details>

---

## Question 370: CLF-C02-ET-Q370
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its applications to the AWS Cloud. The company plans to identify and prioritize any business transformation opportunities and evaluate its AWS Cloud readiness.

Which AWS service or tool should the company use to meet these requirements?

**Choices:**
- A) AWS Cloud Adoption Framework (AWS CAF)
- B) AWS Managed Services (AMS)
- C) AWS Well-Architected Framework
- D) AWS Migration Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://aws.amazon.com/cloud-adoption-framework/
---
Selected Answer: A
Use the AWS CAF to identify and prioritize transformation opportunities, evaluate and improve your cloud readiness, and iteratively evolve your transformation roadmap.
https://aws.amazon.com/cloud-adoption-framework/
---
Selected Answer: A
A. The AWS CAF is the most suitable resource. It provides guidance that supports each unit within an organization through the process of understanding how to align cloud strategies to business objectives. It helps organizations develop and execute efficient and effective plans for their cloud adoption journey, identifying and prioritizing opportunities for transformation across the business.

</details>

---

## Question 371: CLF-C02-ET-Q371
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company need an AWS service that provides a clear baseline of what the company runs in its on-premises data centers. The company needs the projected cost to run its on-premises workloads in the AWS Cloud.

What AWS service or tool will meet these requirements?

**Choices:**
- A) AWS Compute Optimizer
- B) AWS Cost Explorer
- C) AWS Systems Manager Agent (SSM Agent)
- D) Migration Evaluator

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Migration Evaluator
---
Selected Answer: D
D. Migration Evaluator is correct.
---
Selected Answer: D
D. Migration Evaluator

</details>

---

## Question 372: CLF-C02-ET-Q372
**Domain 2:** Security and Compliance  

**Question:**  
A company has an AWS account. The company wants to audit its password and access key rotation details for compliance purposes.
Which AWS service or tool will meet this requirement?

**Choices:**
- A) IAM Access Analyzer
- B) AWS Artifact
- C) IAM credential report
- D) AWS Audit Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
The Correct answer is C.

IAM Access Analyzer: Analyzes IAM policies to identify potential issues and excessive permissions, but doesn't specifically focus on password and access key rotation details.

AWS Artifact: Primarily used for managing and tracking infrastructure as code (IaC) configurations, not directly related to credential auditing.

IAM credential report: This built-in IAM feature provides detailed information about the rotation history of user passwords and access keys within the account. It shows dates of last password and access key rotation, along with usernames and key IDs. This aligns perfectly with the requirement of auditing password and access key rotation details for compliance purposes.

AWS Audit Manager: Offers a comprehensive platform for managing and automating audits across various AWS services, but it requires additional setup and configuration compared to the readily available IAM credential report
---
Selected Answer: C
The Correct answer is C.

You can use credential reports to assist in your auditing and compliance efforts. You can use the report to audit the effects of credential lifecycle requirements, such as password and access key updates. 
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html
---
Selected Answer: C
he IAM credential report is an AWS tool that provides detailed information about the status of IAM users' passwords and access keys, including when they were last rotated, whether they are active, and if they are using multi-factor authentication (MFA). This report is ideal for auditing password and access key rotation, which aligns with the company's compliance requirements

</details>

---

## Question 373: CLF-C02-ET-Q373
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company acquired another corporation. The company now has two AWS accounts.

Which AWS service or tool can the company use to consolidate the billing for these two accounts?

**Choices:**
- A) AWS Systems Manager
- B) AWS Organizations
- C) AWS License Manager
- D) Cost Explorer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `96%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (96%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.
---
Selected Answer: B
B. AWS Organizations
---
Selected Answer: B
Another swing and a miss for exam topics B is the correct answer.

</details>

---

## Question 374: CLF-C02-ET-Q374
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to set up its workloads to perform their intended functions and recover quickly from failure.

Which pillar of the AWS Well-Architected Framework aligns with these goals?

**Choices:**
- A) Performance efficiency
- B) Sustainability
- C) Reliability
- D) Security

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `96%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (96%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
https://aws.amazon.com/blogs/apn/the-6-pillars-of-the-aws-well-architected-framework/

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.
---
Selected Answer: D
Reliability
AWS Services • Foundations • Change Management • Failure Management
---
Selected Answer: C
I guess who ever chooses the correct answer for exam topics just picks answers without looking

</details>

---

## Question 375: CLF-C02-ET-Q375
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is a managed AWS service that is used specifically for extract, transform, and load (ETL) data?

**Choices:**
- A) Amazon Athena
- B) AWS Glue
- C) Amazon S3
- D) AWS Snowball Edge

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Glue • Managed extract, transform, and load (ETL) service
---
Selected Answer: B
B. AWS Glue
---
Selected Answer: B
https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html

</details>

---

## Question 376: CLF-C02-ET-Q376
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate petabytes of data from its on-premises data center to AWS. The company does not want to use an internet connection to perform the migration.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS DataSync
- B) Amazon Connect
- C) AWS Snowmobile
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Snowmobile
---
Selected Answer: C
C. AWS Snowmobile
---
Selected Answer: C
https://aws.amazon.com/snowmobile/

</details>

---

## Question 377: CLF-C02-ET-Q377
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to receive alerts to monitor its overall operating costs for its AWS public cloud infrastructure.

Which AWS offering will meet these requirements?

**Choices:**
- A) Amazon EventBridge
- B) Compute Savings Plans
- C) AWS Budgets
- D) Migration Evaluator

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `87%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (87%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Budgets: more advanced – track usage, costs, RI, and get alerts
---
Selected Answer: C
C. AWS Budgets
---
Selected Answer: C
C. AWS Budgets

AWS Budgets is a service that allows you to set custom cost and usage budgets for your AWS resources and receive alerts when your actual costs or usage exceed the thresholds you defined. You can set up budgets based on various dimensions such as service, linked accounts, tags, and more.

By setting up AWS Budgets, the company can define spending thresholds and receive alerts via email or SNS (Simple Notification Service) when their overall operating costs exceed the defined budgets. This allows them to proactively monitor and manage their AWS spending to ensure it stays within desired limits.

</details>

---

## Question 378: CLF-C02-ET-Q378
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
How does the AWS Enterprise Support Concierge team help users?

**Choices:**
- A) Supporting application development
- B) Providing architecture guidance
- C) Answering billing and account inquiries
- D) Answering questions regarding technical support cases

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `85%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (85%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The Enterprise Support Concierge is a group of AWS billing and account experts that specialize in working with enterprise accounts. They help with billing and account inquiries.
---
Selected Answer: C
Concierge Support Team (for billing and account best practices)
---
Selected Answer: C
C. Answering billing and account inquiries

</details>

---

## Question 379: CLF-C02-ET-Q379
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run a simulation for 3 years without interruptions.

Which Amazon EC2 instance purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) Spot Instances
- B) Reserved Instances
- C) Dedicated Hosts
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
It's reserved instances! How on earth could be D. On-demand instances??!!
---
Selected Answer: B
B. Reserved Instances
---
the last answers are not good
Correct answer : B

</details>

---

## Question 380: CLF-C02-ET-Q380
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or resource can provide discounts on some AWS service costs in exchange for a spending commitment?

**Choices:**
- A) Amazon Detective
- B) AWS Pricing Calculator
- C) Savings Plans
- D) Basic Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Savings Plan • Commit a certain $ amount per hour for 1 or 3 years • Easiest way to setup long-term commitments on AWS
---
Selected Answer: C
It's C
---
Selected Answer: C
C. Savings Plans

</details>

---

## Question 381: CLF-C02-ET-Q381
**Domain 1:** Cloud Concepts  

**Question:**  
Which of the following are pillars of the AWS Well-Architected Framework? (Choose two.)

**Choices:**
- A) High availability
- B) Performance efficiency
- C) Cost optimization
- D) Going global in minutes
- E) Continuous development

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `84%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (84%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
BC.

Operational Excellence
Security
Reliability
Performance Efficiency
Cost Optimization
Sustainability
---
Selected Answer: C
Well Architected Framework
6 Pillars
• 1) Operational Excellence
• 2) Security
• 3) Reliability
• 4) Performance Efficiency
• 5) Cost Optimization
• 6) Sustainability

answer BC
---
Selected Answer: C
BC are the correct options

</details>

---

## Question 382: CLF-C02-ET-Q382
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use Amazon EC2 instances to provide a static website to users all over the world. The company needs to minimize latency for the users.

Which solution meets these requirements?

**Choices:**
- A) Use EC2 instances in multiple edge locations.
- B) Use EC2 instances in the same Availability Zone but in different AWS Regions.
- C) Use Amazon CloudFront with the EC2 instances configured as the source.
- D) Use EC2 instances in the same Availability Zone but in different AWS accounts.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (94%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon CloudFront is a content delivery network (CDN) service that accelerates the delivery of your websites, APIs, video content, or other web assets. In this scenario, using Amazon CloudFront is the most suitable option to minimize latency for users all over the world.
---
Selected Answer: C
key word: static website* as in content.
Therefore, it can't be B. as they are just physical locations, situated globally providing low latency, high throughput, but isn't used as a content delivery service.
---
Selected Answer: C
C. Use Amazon CloudFront with the EC2 instances configured as the source.

</details>

---

## Question 383: CLF-C02-ET-Q383
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to receive a notification when a specific AWS cost threshold is reached.
Which AWS services or tools can the company use to meet this requirement? (Choose two.)

**Choices:**
- A) Amazon Simple Queue Service (Amazon SQS)
- B) AWS Budgets
- C) Cost Explorer
- D) Amazon CloudWatch
- E) AWS Cost and Usage Report

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (93%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B. AWS Budgets: AWS Budgets is a service that allows you to set custom cost and usage budgets for your AWS resources. You can configure a budget with a specific threshold and define actions, such as sending notifications, when that threshold is reached.

D. Amazon CloudWatch: Amazon CloudWatch is a monitoring service that can be used to collect and track metrics, logs, and events from various AWS resources. It supports setting up alarms based on cost metrics, so you can create an alarm for a specific cost threshold and configure it to send notifications when the threshold is breached.
---
Selected Answer: BD
B. AWS Budgets: Allows the company to set custom cost and usage budgets that alert them when thresholds are exceeded. They can receive notifications via email or Amazon Simple Notification Service (Amazon SNS) when the budget thresholds are reached.

D. Amazon CloudWatch: Can be used to create custom alarms based on cost metrics. The company can set up alarms to trigger notifications when specific cost thresholds are met or exceeded. CloudWatch Alarms can notify through various channels, including Amazon SNS.

The other options are described as follows:

 A. Amazon Simple Queue Service (Amazon SQS): SQS is a fully managed message queuing service.
 C. Cost Explorer: Cost Explorer is a tool for exploring and analyzing AWS costs but does not provide direct notifications for cost thresholds.
 E. AWS Cost and Usage Report: The Cost and Usage Report provides detailed information about AWS costs but does not offer real-time notifications for cost thresholds.
---
Selected Answer: BD
AWS Budgets allows setting and receiving notifications when specific cost thresholds are met.

</details>

---

## Question 384: CLF-C02-ET-Q384
**Domain 3:** Cloud Technology and Services  

**Question:**  
A team of researchers is going to collect data at remote locations around the world. Many locations do not have internet connectivity. The team needs to capture the data in the field, and transfer it to the AWS Cloud later.

Which AWS service will support these requirements?

**Choices:**
- A) AWS Outposts
- B) AWS Transfer Family
- C) AWS Snow Family
- D) AWS Migration Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (94%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Snow Family
---
Selected Answer: C
snow family in cases where network connectivity is weak or do not exist.
---
Selected Answer: C
C. AWS Snow Family

</details>

---

## Question 385: CLF-C02-ET-Q385
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are benefits that a company receives when it moves an on-premises production workload to AWS? (Choose two.)

**Choices:**
- A) AWS trains the company's staff on the use of all the AWS services.
- B) AWS manages all security in the cloud.
- C) AWS offers free support from technical account managers (TAMs).
- D) AWS offers high availability.
- E) AWS provides economies of scale.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `DE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: DE (100%). Contributor Answer: DE.

Community Rationale & Discussion:
Selected Answer: DE
correct answers are D and E
---
Selected Answer: DE
D. AWS offers high availability.
E. AWS provides economies of scale.
---
Selected Answer: DE
D and E

</details>

---

## Question 386: CLF-C02-ET-Q386
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has decided to adopt Amazon EC2 infrastructure and wants to scale various stateless services for short-term usage.

Which EC2 pricing model is MOST cost-efficient to meet these requirements?

**Choices:**
- A) Spot Instances
- B) On-Demand Instances
- C) Reserved Instances
- D) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Spot Instances
---
Selected Answer: A
Spot Instances
---
Selected Answer: A
Finally a good answer!

</details>

---

## Question 387: CLF-C02-ET-Q387
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are benefits of AWS Trusted Advisor? (Choose two.)

**Choices:**
- A) Access to Amazon Simple Queue Service (Amazon SQS)
- B) Cost optimization recommendations
- C) Hourly refresh of the service limit checks
- D) Security checks
- E) AWS Identity and Access Management (IAM) approval management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B. Cost optimization recommendations
E. Security checks
---
Selected Answer: BD
B & D are correct
---
BD.
https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html

</details>

---

## Question 388: CLF-C02-ET-Q388
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to save costs by archiving data that is no longer frequently accessed by end users.

Which Amazon S3 feature will meet this requirement?

**Choices:**
- A) S3 Versioning
- B) S3 Lifecycle
- C) S3 Object Lock
- D) S3 Inventory

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon S3 Lifecycle policies allow you to define rules to automatically transition objects between storage classes or delete them when they are no longer needed. In the context of cost savings and archiving data that is no longer frequently accessed, using S3 Lifecycle policies is the appropriate solution.
---
Selected Answer: B
Lifecycle
---
Selected Answer: B
best answer B

</details>

---

## Question 389: CLF-C02-ET-Q389
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has an uninterruptible application that runs on Amazon EC2 instances. The application constantly processes a backlog of files in an Amazon Simple Queue Service (Amazon SQS) queue. This usage is expected to continue to grow for years.
What is the MOST cost-effective EC2 instance purchasing model to meet these requirements?

**Choices:**
- A) Spot Instances
- B) On-Demand Instances
- C) Savings Plans
- D) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (71%). Contributor Answer: C.

Community Rationale & Discussion:
How do they expect me to buy their expensive subscription with so many -not even close- wrong answers...
---
Selected Answer: C
Uninterruptible + Years = saving plans or reserved instances
---
Selected Answer: A
The application can continue processing tasks with SQS. Therefore, even if the server goes down and then comes back up, it can retrieve the data to continue processing from SQS. Choosing a spot instance seems to be the right answer because spot instances are cheaper than using a saving plan.

</details>

---

## Question 390: CLF-C02-ET-Q390
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants an AWS service to provide product recommendations based on its customer data.
Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Polly
- B) Amazon Personalize
- C) Amazon Comprehend
- D) Amazon Rekognition

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Answer is B, Amazon Personalize

-Amazon Polly: Deploy high-quality, natural-sounding human voices in dozens of languages.

-Amazon Personalize: Enhance your digital transformation with ML, seamlessly integrating personalized recommendations into websites, applications, email systems,... .

-Amazon Comprehend: Derive and understand valuable insights from text within document.

-Amazon Rekognition : Automate and lower the cost of your image recognition and video analysis with machine learning.
---
Selected Answer: B
-Amazon Personalize: Enhance your digital transformation with ML, seamlessly integrating personalized recommendations into websites, applications, email systems
---
Selected Answer: B
It's B

</details>

---

## Question 391: CLF-C02-ET-Q391
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning its migration to the AWS Cloud. The company is identifying its capability gaps by using the AWS Cloud Adoption Framework (AWS CAF) perspectives.
Which phase of the cloud transformation journey includes these identification activities?

**Choices:**
- A) Envision
- B) Align
- C) Scale
- D) Launch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `83%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (83%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
"Align phase focuses on identifying capability gaps across the six AWS CAF perspectives, identifying cross-organizational dependencies, and surfacing stakeholder concerns and challenges."

Reference: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html
---
Selected Answer: B
B is correct answer
"Identify capability gaps and cross-organizational dependencies"
https://aws.amazon.com/cloud-adoption-framework/
---
Selected Answer: B
In the AWS Cloud Adoption Framework (AWS CAF), the "Align" phase focuses on understanding and addressing capability gaps to ensure that the organization is prepared for cloud adoption. This involves assessing current capabilities, identifying gaps, and planning for the necessary changes to achieve alignment with cloud best practices.

</details>

---

## Question 392: CLF-C02-ET-Q392
**Domain 3:** Cloud Technology and Services  

**Question:**  
A social media company wants to protect its web application from common web exploits such as SQL injections and cross-site scripting.
Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Inspector
- B) AWS WAF
- C) Amazon GuardDuty
- D) Amazon CloudWatch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
"AWS WAF is a web application firewall that helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (count) web requests based on conditions that you define. These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection and cross-site scripting."

References: https://aws.amazon.com/waf/faqs/
---
Selected Answer: B
A. Amazon Inspector - security assessment service that helps improve the security and compliance of applications deployed on AWS but doesn't protect web apps from live exploits.
B. AWS WAF - A web application firewall that allows users to create custom rules to filter and monitor HTTP or HTTPS requests to a web application. It helps protect against web exploits, including SQL injection attacks.
C. Amazon GuardDuty - continuously detects threats and unauthorized behavior but doesn't actively block web exploits.
D. Amazon CloudWatch - Primarily for monitoring and managing resources its not a security tool for blocking attacks.
---
Selected Answer: B
"AWS WAF is a web application firewall that helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (count) web requests based on conditions that you define. These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection and cross-site scripting."

</details>

---

## Question 393: CLF-C02-ET-Q393
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which fully managed AWS service assists with the creation, testing, and management of custom Amazon EC2 images?

**Choices:**
- A) EC2 Image Builder
- B) Amazon Machine Image (AMI)
- C) AWS Launch Wizard
- D) AWS Elastic Beanstalk

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. EC2 Image Builder is a fully managed service that helps you automate the creation, testing, and distribution of custom Amazon EC2 images 
B. Amazon Machine Image (AMI) - is not a service, it's the image used to launch EC2 instances. 
C. AWS Launch Wizard is a tool that helps you easily set up complex applications on AWS—like SQL Server, SAP. Not for building or managing EC2 images.
D. AWS Elastic Beanstalk is a service for deploying and scaling web applications and services. It's not for building EC2 images.
---
Selected Answer: A
A. EC2 Image Builder simplifies the creation, maintenance, validation, sharing, and deployment of Linux or Windows images for use with Amazon EC2 and on-premises."
---
Selected Answer: A
A

Launch Wizard then identifies the right AWS resources, such as EC2 instances and EBS volumes, to deploy and run your application. Launch Wizard provides an estimated cost of deployment, and lets you modify your resources to instantly view an updated cost assessment. Once you approve the AWS resources, Launch Wizard automatically provisions and configures the selected resources to create a fully-functioning, production-ready application. AWS Launch Wizard also creates CloudFormation templates that can serve as a baseline to accelerate subsequent deployments.

AWS Elastic Beanstalk is a service designed to simplify the deployment and management of web applications and services. It allows developers to focus on writing code without worrying about the underlying infrastructure. Elastic Beanstalk handles the details of capacity provisioning, load balancing, scaling, and application health monitoring

</details>

---

## Question 394: CLF-C02-ET-Q394
**Domain 1:** Cloud Concepts  

**Question:**  
Which cloud computing advantage is a company applying when it uses AWS Regions to increase application availability to users in different countries?

**Choices:**
- A) Pay-as-you-go pricing
- B) Capacity forecasting
- C) Economies of scale
- D) Global reach

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
It's D. C is only if we're talking about money.
---
Selected Answer: D
Global reach is the answer
---
Selected Answer: D
https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.

</details>

---

## Question 395: CLF-C02-ET-Q395
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants an AWS service to collect and process 10 TB of data locally and transfer the data to AWS. The company has intermittent connectivity.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Database Migration Service (AWS DMS)
- B) AWS DataSync
- C) AWS Backup
- D) AWS Snowball Edge

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Snowball Edge
---
Selected Answer: D
AWS Snowball Edge is a type of Snowball device with on-board storage and compute power for select AWS capabilities. Snowball Edge can process data locally, run edge-computing workloads, and transfer data to or from the AWS Cloud.

Each Snowball Edge device can transport data at speeds faster than the internet. This transport is done by shipping the data in the devices through a regional carrier. The appliances are rugged, complete with E Ink shipping labels.

Snowball Edge devices have three options for device configurations—Storage Optimized, Compute Optimized, and Compute Optimized with GPU. When this guide refers to Snowball Edge devices, it's referring to all options of the device. When specific information applies only to one or more optional configurations of devices (such as how the Snowball Edge with GPU has an on-board GPU), it is called out specifically.
---
Selected Answer: D
D is the correct answer

</details>

---

## Question 396: CLF-C02-ET-Q396
**Domain 1:** Cloud Concepts  

**Question:**  
Which of the following is an AWS Well-Architected Framework design principle for operational excellence in the AWS Cloud?

**Choices:**
- A) Go global in minutes.
- B) Make frequent, small, reversible changes.
- C) Implement a strong foundation of identity and access management
- D) Stop spending money on hardware infrastructure for data center operations.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.
---
B
Design Principles
There are five design principles for operational excellence in the cloud:

Perform operations as code:
Make frequent, small, reversible changes: 
Refine operations procedures frequently:
Anticipate failure: 
Learn from all operational failures:
---
Selected Answer: B
Operational Excellence
• Includes the ability to run and monitor systems to deliver business value
and to continually improve supporting processes and procedures
• Design Principles
• Perform operations as code - Infrastructure as code
• Make frequent, small, reversible changes - So that in case of any failure, you can
reverse it
• Refine operations procedures frequently - And ensure that team members are
familiar with it

</details>

---

## Question 397: CLF-C02-ET-Q397
**Domain 3:** Cloud Technology and Services  

**Question:**  
What is a benefit of using AWS serverless computing?

**Choices:**
- A) Application deployment and management are not required.
- B) Application security will be fully managed by AWS.
- C) Monitoring and logging are not needed.
- D) Management of infrastructure is offloaded to AWS.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
https://aws.amazon.com/what-is/serverless-computing/#:~:text=serverless%20computing%20requirements%3F-,What%20is%20serverless%20computing%3F,-Serverless%20computing%20is

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.
---
Selected Answer: D
D. Management of infrastructure is offloaded to AWS
---
Selected Answer: D
DDDDDDDDDDDD

</details>

---

## Question 398: CLF-C02-ET-Q398
**Domain 2:** Security and Compliance  

**Question:**  
A developer wants AWS users to access AWS services by using temporary security credentials.

Which AWS service or feature should the developer use to provide these credentials?

**Choices:**
- A) IAM policies
- B) IAM user groups
- C) AWS Security Token Service (AWS STS)
- D) AWS IAM Identity Center (AWS Single Sign-On)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Security Token Service (AWS STS) as a web service that enables you to request temporary, limited-privilege credentials for users.
---
Selected Answer: C
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html
---
Selected Answer: C
AWS provides AWS Security Token Service (AWS STS) as a web service that enables you to request temporary, limited-privilege credentials for users. 
https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html

</details>

---

## Question 399: CLF-C02-ET-Q399
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service or resource provides answers to the most frequently asked security-related questions that AWS receives from its users?

**Choices:**
- A) AWS Artifact
- B) Amazon Connect
- C) AWS Chatbot
- D) AWS Knowledge Center

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (93%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A. AWS Artifact: AWS Artifact provides on-demand access to AWS compliance reports and documents. It includes various compliance-related documents, such as SOC reports, PCI DSS reports, and more. While it offers valuable compliance information, it may not directly address the most frequently asked security-related questions.

B. Amazon Connect: Amazon Connect is a cloud-based contact center service. It is focused on providing customer service solutions and does not specifically provide answers to security-related questions.

C. AWS Chatbot: AWS Chatbot is a service that allows users to receive notifications and interact with AWS resources using chat platforms like Slack and Amazon Chime. While it facilitates communication and notifications, it is not designed to provide answers to frequently asked security-related questions.

D. AWS Knowledge Center: AWS Knowledge Center is a resource that provides answers to the most frequently asked security-related questions that AWS receives from its users. It offers a collection of articles, videos, and other resources to help users address common security queries and challenges.
---
Selected Answer: D
The AWS Knowledge Center provides a repository of frequently asked security-related questions and other common queries that AWS users have. It includes helpful documentation, guides, and answers to commonly encountered issues, including security topics.
---
Selected Answer: D
Knowledge Center provides documentation and answers to specific questions

</details>

---

## Question 400: CLF-C02-ET-Q400
**Domain 2:** Security and Compliance  

**Question:**  
A global company wants to use a managed security service for protection from SQL injection attacks. The service also must provide detailed logging information about access to the company's ecommerce applications.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Network Firewall
- B) Amazon RDS for SQL Server
- C) Amazon GuardDuty
- D) AWS WAF

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Selected Answer: D
---
Selected Answer: D
AWS WAF (Web Application Firewall) is a web application firewall service that helps protect web applications from common web exploits and attacks, including SQL injection attacks. It allows you to define custom rules and conditions to filter and control inbound web traffic, providing protection against SQL injection attacks. Additionally, AWS WAF provides detailed logging information about access to your web applications, including information about requests, IP addresses, and response codes.

https://pupuweb.com/answer-explained-which-aws-managed-security-service-protect-sql-injection-attacks-access-logging-ecommerce-app/
---
Selected Answer: D
With AWS WAF, you can create security rules that control bot traffic and block common attack patterns such as SQL injection or cross-site scripting (XSS).
https://aws.amazon.com/waf/

</details>

---

## Question 401: CLF-C02-ET-Q401
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is migrating its on-premises server to an Amazon EC2 instance. The server must stay active at all times for the next 12 months.

Which EC2 pricing option is the MOST cost-effective for the company's workload?

**Choices:**
- A) On-Demand
- B) Dedicated Hosts
- C) Spot Instances
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Reserved Instances
---
Selected Answer: D
D. Reserved Instances

Reserved Instances offer significant cost savings compared to On-Demand Instances, especially for workloads that are expected to run continuously for a long duration, such as the next 12 months in this scenario. By committing to a 1- or 3-year term with Reserved Instances, the company can benefit from discounted hourly rates compared to On-Demand pricing.
---
Selected Answer: D
Finally a good answer!

</details>

---

## Question 402: CLF-C02-ET-Q402
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following is the customer's responsibility under the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Maintain the configuration of infrastructure devices.
- B) Maintain patching and updates within the hardware infrastructure.
- C) Maintain the configuration of guest operating systems and applications.
- D) Manage decisions involving encryption options.
- E) Maintain infrastructure hardware.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (100%). Contributor Answer: CD.

Community Rationale & Discussion:
Selected Answer: CD
C. Maintain the configuration of guest operating systems and applications. Most Voted
D. Manage decisions involving encryption options.
---
Selected Answer: CD
C. Maintain the configuration of guest operating systems and applications: Customers are responsible for configuring and securing the operating systems and applications running on their instances or virtual machines.

D. Manage decisions involving encryption options: Customers are responsible for making decisions regarding encryption options for their data, including determining which data to encrypt and selecting appropriate encryption mechanisms.
---
Selected Answer: CD
Correct. Answer is CD

</details>

---

## Question 403: CLF-C02-ET-Q403
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to verify if multi-factor authentication (MFA) is enabled for all users within its AWS accounts.

Which AWS service or resource will meet this requirement?

**Choices:**
- A) AWS Cost and Usage Report
- B) IAM credential reports
- C) AWS Artifact
- D) Amazon CloudFront reports

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B IAM credentials report
---
Selected Answer: B
B. IAM credential reports
---
Selected Answer: B
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html
IAM credential reports are delivered in CSV format. "mfa_active" is one of many columns of this report. When a MFA device is enabled for the user, value of this column is TRUE.

</details>

---

## Question 404: CLF-C02-ET-Q404
**Domain 2:** Security and Compliance  

**Question:**  
A company uses AWS security services and tools. The company needs a service to help manage the security alerts and must organize the alerts into a single dashboard.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon GuardDuty
- B) Amazon Inspector
- C) Amazon Macie
- D) AWS Security Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (94%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Correct answer is D
---
Selected Answer: D
D. AWS Security Hub: Centrally view and manage security alerts and automate security checks
---
Selected Answer: D
D. AWS Security Hub

</details>

---

## Question 405: CLF-C02-ET-Q405
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to run its workloads in the AWS Cloud effectively, reduce management overhead, and improve processes.

Which AWS Well-Architected Framework pillar represents these requirements?

**Choices:**
- A) Reliability
- B) Operational excellence
- C) Performance efficiency
- D) Cost optimization

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B.

Keyphrase for operational excellence: Run and monitor systems to deliver business value and to "improve supporting processes and procedures".
---
B
The Operational Excellence pillar includes the ability to support development and run workloads effectively, gain insight into their operations, and to continuously improve supporting processes and procedures to deliver business value.
---
Selected Answer: B
B. Operational excellence

</details>

---

## Question 406: CLF-C02-ET-Q406
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company uses Amazon S3 to store records that can contain personally identifiable information (PII). The company wants a solution that can monitor all S3 buckets for PII and immediately alert staff about vulnerabilities.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon GuardDuty
- B) Amazon Detective
- C) Amazon Macie
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
PII = Sensitive Data. Amazon Macie identifies Sensitive Data.
https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.
---
Selected Answer: C
C.

GuardDuty is more for logs, while Macie is more for PII.
---
Amazon Macie

</details>

---

## Question 407: CLF-C02-ET-Q407
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service allows users to download security and compliance reports about the AWS infrastructure on demand?

**Choices:**
- A) Amazon GuardDuty
- B) AWS Security Hub
- C) AWS Artifact
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C
It is Artifact. most of the answers are wrong after the question No. 255
---
Selected Answer: C
C. AWS Artifact
---
Selected Answer: C
It is Artifact.

</details>

---

## Question 408: CLF-C02-ET-Q408
**Domain 2:** Security and Compliance  

**Question:**  
An external auditor has requested that a company provide a list of all its IAM users, including the status of users' credentials and access keys.

What is the SIMPLEST way to provide this information?

**Choices:**
- A) Create an IAM user account for the auditor, granting the auditor administrator permissions.
- B) Take a screenshot of each user's page in the AWS Management Console, then provide the screenshots to the auditor.
- C) Download the IAM credential report, then provide the report to the auditor.
- D) Download the AWS Trusted Advisor report, then provide the report to the auditor.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Download the IAM credential report, then provide the report to the auditor.
---
The simplest way to provide an external auditor with a list of all IAM users, including the status of users' credentials and access keys, is:

C. Download the IAM credential report, then provide the report to the auditor.

The IAM credential report is a feature within AWS Identity and Access Management (IAM) that provides a way to audit the status of credentials for all IAM users in an AWS account. It includes information about when each user's credentials were last used, the status of multi-factor authentication (MFA), and the status of access keys. This report can be generated and downloaded as a CSV file, making it easy to share with auditors or for compliance purposes.
---
Selected Answer: C
C. Download the IAM credential report, then provide the report to the auditor.

</details>

---

## Question 409: CLF-C02-ET-Q409
**Domain 2:** Security and Compliance  

**Question:**  
Which task can a company perform by using security groups in the AWS Cloud?

**Choices:**
- A) Allow access to an Amazon EC2 instance through only a specific port.
- B) Deny access to malicious IP addresses at a subnet level.
- C) Protect data that is cached by Amazon CloudFront.
- D) Apply a stateless firewall to an Amazon EC2 instance.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
should be A
---
Selected Answer: A
A. Allow access to an Amazon EC2 instance through only a specific port.
---
Selected Answer: A
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
Security groups are stateful. For example, if you send a request from an instance, the response traffic for that request is allowed to reach the instance regardless of the inbound security group rules. Responses to allowed inbound traffic are allowed to leave the instance, regardless of the outbound rules. So "D" is NOT the answer. "A" is the correct answer.

</details>

---

## Question 410: CLF-C02-ET-Q410
**Domain 2:** Security and Compliance  

**Question:**  
Which tasks are customer responsibilities, according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Configure the AWS provided security group firewall.
- B) Classify company assets in the AWS Cloud.
- C) Determine which Availability Zones to use for Amazon S3 buckets.
- D) Patch or upgrade Amazon DynamoDB.
- E) Select Amazon EC2 instances to run AWS Lambda on.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AB`  
**Community Consensus:** `92%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AB (92%). Contributor Answer: AB.

Community Rationale & Discussion:
Selected Answer: AB
A. Configure the AWS provided security group firewall: Customers are responsible for configuring and managing security group firewalls to control inbound and outbound traffic to their AWS resources.

B. Classify company assets in the AWS Cloud: Asset classification is typically a customer responsibility as part of their data governance and security practices.

The other options are not accurate in the context of customer responsibilities:

C. Determine which Availability Zones to use for Amazon S3 buckets: This is more of a design decision and falls under the AWS management responsibilities.

D. Patch or upgrade Amazon DynamoDB: Patching or upgrading services like Amazon DynamoDB is managed by AWS. Customers are not responsible for patching or upgrading the underlying infrastructure or services provided by AWS.

E. Select Amazon EC2 instances to run AWS Lambda on: The selection of underlying infrastructure for serverless services like AWS Lambda is managed by AWS. Customers focus on writing and deploying functions without managing the underlying instances.
---
Selected Answer: AB
A&B. 
Not C: S3 is available across all AZ's and customer does not choose the AZ.
Not D: Dynamo DB patching is "of the cloud", not "in the cloud", hence is AWS responsibility
Not E: AWS Lambda is a serverless service
---
Selected Answer: AB
According to the AWS shared responsibility model, AWS manages the security of the cloud (infrastructure), while customers are responsible for security in the cloud (how they configure and manage their resources).

</details>

---

## Question 411: CLF-C02-ET-Q411
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to run a compute-intensive workload that uses graphics processing units (GPUs).

Which Amazon EC2 instance type should the company use?

**Choices:**
- A) Accelerated computing
- B) Compute optimized
- C) Storage optimized
- D) General purpose

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Instances in the Accelerated Computing category are specifically designed to handle workloads that benefit from hardware acceleration, such as those using GPUs.
---
A. for me was a guess since the other options are too generic
---
Selected Answer: A
https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html#ac_hardware

</details>

---

## Question 412: CLF-C02-ET-Q412
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are features of network ACLs as they are used in the AWS Cloud? (Choose two.)

**Choices:**
- A) They are stateless.
- B) They are stateful.
- C) They evaluate all rules before allowing traffic.
- D) They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic.
- E) They operate at the instance level.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (90%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
A. They are stateless.
D. They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic.
---
Selected Answer: AD
A. They are stateless: Network ACLs do not maintain connection state information. Each packet is evaluated independently based on the rules defined in the ACL.

D. They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic: Network ACLs evaluate rules sequentially from the lowest numbered rule to the highest numbered rule. Once a rule that matches the traffic is found, further rule processing stops.
---
Selected Answer: AD
A, D. Another crap question

</details>

---

## Question 413: CLF-C02-ET-Q413
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which capabilities are in the platform perspective of the AWS Cloud Adoption Framework (AWS CAF)? (Choose two.)

**Choices:**
- A) Performance and capacity management
- B) Data engineering
- C) Continuous integration and continuous delivery (CI/CD)
- D) Infrastructure protection
- E) Change and release management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `76%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (76%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
B. Data engineering: This capability focuses on managing data pipelines, data storage, and data processing workflows to enable efficient data management and analytics in the cloud.

C. Continuous integration and continuous delivery (CI/CD): This capability involves implementing automated processes for building, testing, and deploying software applications in a continuous manner, ensuring faster delivery cycles and improved software quality.

https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/welcome.html
---
Selected Answer: BC
The key is the two for the *platform*
---
Selected Answer: AD
A. Performance and Capacity that falls under the Operations perspective (https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/operations-perspective.html)
D. Infrastructure protection that falls under the security perspective (https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html)

</details>

---

## Question 414: CLF-C02-ET-Q414
**Domain 2:** Security and Compliance  

**Question:**  
According to the AWS shared responsibility model, the customer is responsible for applying the latest security updates and patches for which of the following?

**Choices:**
- A) Amazon DynamoDB
- B) Amazon EC2 instances
- C) Amazon RDS instances
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The customer is responsible for applying the latest security updates and patches to Amazon EC2 instances.
---
Selected Answer: B
S3 and patches? At this point I am rolling on the floor and laughing :D S3 is not even a compute platform!
---
Selected Answer: B
Answer is B.

</details>

---

## Question 415: CLF-C02-ET-Q415
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which Amazon S3 storage class is MOST cost-effective for unknown access patterns?

**Choices:**
- A) S3 Standard
- B) S3 Standard-Infrequent Access (S3 Standard-IA)
- C) S3 One Zone-Infrequent Access (S3 One Zone-IA)
- D) S3 Intelligent-Tiering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. S3 Intelligent-Tiering

S3 Intelligent-Tiering is the most cost-effective option for unknown access patterns. It automatically moves objects between two access tiers (frequent and infrequent access) based on changing access patterns. This helps optimize costs for data with unknown or changing access patterns.
---
D
S3 Intelligent-Tiering is an Amazon S3 storage class that analyzes an AWS user's stored data and automatically moves it between storage tiers based on usage frequency. It is designed to optimize storage costs for data with irregular or unknown access patterns.
---
Selected Answer: D
S3 Intelligent-Tiering: This storage class is designed to optimize costs for data with unknown or changing access patterns. It automatically moves objects between two access tiers (frequent and infrequent access) based on changing access patterns, without any operational overhead. This makes it ideal for data whose access patterns are not predictable.

</details>

---

## Question 416: CLF-C02-ET-Q416
**Domain 2:** Security and Compliance  

**Question:**  
Which options are AWS Cloud Adoption Framework (AWS CAF) security perspective capabilities? (Choose two.)

**Choices:**
- A) Observability
- B) Incident and problem management
- C) Incident response
- D) Infrastructure protection
- E) Availability and continuity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (88%). Contributor Answer: CD.

Community Rationale & Discussion:
Selected Answer: CD
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html
---
Selected Answer: BC
Incident and Problem Management: This capability involves processes and practices for managing security incidents and problems that arise within your cloud environment. It includes detecting, responding to, and resolving security issues to minimize impact.

Incident Response: This capability focuses on the procedures and tools needed to respond to and recover from security incidents. It includes identifying, managing, and mitigating the effects of security breaches or attacks.
---
selected answer : CD 
AWS Cloud Adoption Framework - CAF: Security perspective
・compliance and assurance
・Security Governance
・Security Assurance
・Data Protection
・Application Security
・Threat Detection
・Vulnerability Mgmt
・Identity and Access Mgmt
・Incident response
・Infrastructure protection

</details>

---

## Question 417: CLF-C02-ET-Q417
**Domain 2:** Security and Compliance  

**Question:**  
A company has a managed IAM policy that does not grant the necessary permissions for users to accomplish required tasks.

How can this be resolved?

**Choices:**
- A) Enable AWS Shield Advanced.
- B) Create a custom IAM policy.
- C) Use a third-party web application firewall (WAF) managed rule from the AWS Marketplace.
- D) Use AWS Key Management Service (AWS KMS) to create a customer-managed key.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Create a custom IAM policy.

If the existing managed IAM policy does not provide the necessary permissions, you can create a custom IAM policy tailored to the specific permissions required by the users. This allows you to define and grant the permissions needed for the tasks.
---
Selected Answer: B
B. Create a custom IAM policy.

By creating a custom IAM policy, you can define the specific permissions needed for users to accomplish their required tasks
---
Selected Answer: B
B. Create a custom IAM policy.

Creating a custom IAM policy allows you to define and specify the exact permissions and access controls needed by your users to accomplish their tasks. You can tailor the custom policy to meet your specific requirements and grant the necessary permissions.

</details>

---

## Question 418: CLF-C02-ET-Q418
**Domain 2:** Security and Compliance  

**Question:**  
Who is responsible for managing IAM user access and secret keys according to the AWS shared responsibility model?

**Choices:**
- A) IAM access and secret keys are static, so there is no need to rotate them.
- B) The customer is responsible for rotating keys.
- C) AWS will rotate the keys whenever required.
- D) The AWS Support team will rotate keys when requested by the customer.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The customer is responsible for rotating keys.
---
B 
is the correct answer without any doubt
---
Selected Answer: B
Customer's own responsibility for rotation their keys.

</details>

---

## Question 419: CLF-C02-ET-Q419
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to run a pre-installed third-party firewall on an Amazon EC2 instance.

Which AWS service or feature can provide this solution?

**Choices:**
- A) Network ACLs
- B) Security groups
- C) AWS Marketplace
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
key word: third party*
---
Selected Answer: C
C is the correct answer
---
Selected Answer: C
AWS Marketplace allows you to find, purchase, and deploy a wide range of pre-configured third-party software, including firewall solutions, on your Amazon EC2 instances.

</details>

---

## Question 420: CLF-C02-ET-Q420
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud benefit gives a company the ability to quickly deploy cloud resources to access compute, storage, and database infrastructures in a matter of minutes?

**Choices:**
- A) Elasticity
- B) Cost savings
- C) Agility
- D) Reliability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Agility = quickly deploy
---
Selected Answer: C
Agility in cloud computing refers to the ability to quickly develop, test, and launch applications that the business needs.

</details>

---

## Question 421: CLF-C02-ET-Q421
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a centralized group of users with large file storage requirements that have exceeded the space available on premises. The company wants to extend its file storage capabilities for this group while retaining the performance benefit of sharing content locally.
What is the MOST operationally efficient AWS solution for this scenario?

**Choices:**
- A) Create an Amazon S3 bucket for each user. Mount each bucket by using an S3 file system mounting utility.
- B) Configure and deploy an AWS Storage Gateway file gateway. Connect each user’s workstation to the file gateway.
- C) Move each user’s working environment to Amazon WorkSpaces. Set up an Amazon WorkDocs account for each user.
- D) Deploy an Amazon EC2 instance and attach an Amazon Elastic Block Store (Amazon EBS) Provisioned IOPS volume. Share the EBS volume directly with the users.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `96%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (96%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Storage Gateway is a hybrid storage service
---
B. Configure and deploy an AWS Storage Gateway file gateway. Connect each user’s workstation to the file gateway.

Using an AWS Storage Gateway file gateway allows you to extend your on-premises file storage into the AWS Cloud seamlessly. It provides low-latency access to your data stored in Amazon S3 while maintaining the performance benefits of local access. This solution enables centralized management of storage while still allowing users to access files as if they were stored locally. Additionally, it eliminates the need for managing individual S3 buckets for each user, simplifying administration and scalability.
---
Selected Answer: B
Storage gateway is used for hybrid cloud

</details>

---

## Question 422: CLF-C02-ET-Q422
**Domain 1:** Cloud Concepts  

**Question:**  
Which of the following are pillars of the AWS Well-Architected Framework? (Choose two.)

**Choices:**
- A) Availability
- B) Reliability
- C) Scalability
- D) Responsive design
- E) Operational excellence

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
1. Operational Excellence
2. Security
3. Reliability
4. Performance Efficiency
5. Cost Optimization
---
There are 6 pillars -
1. Operational excellence
2. Security
3. Reliability
4. Performance efficiency
5. Cost optimization
6. Sustainability
---
Selected Answer: BE
The AWS Well-Architected Framework is built on five pillars that help architects build secure, high-performing, resilient, and efficient infrastructure for their applications. The two pillars from the options provided are:

Reliability: Focuses on ensuring a system can recover from failures and meet customer demands without disruption.
Operational excellence: Ensures that workloads are well-managed, continuously improving, and optimized for both operations and efficiency.

</details>

---

## Question 423: CLF-C02-ET-Q423
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following is entirely the responsibility of AWS, according to the AWS shared responsibility model?

**Choices:**
- A) Security awareness and training
- B) Development of an IAM password policy
- C) Patching of the guest operating system
- D) Physical and environmental controls

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Physical Amazon DC
---
D. Physical and environmental controls
---
Selected Answer: D
AWS is responsible for the protection of the physical infrastructure and environment of its data centers. This is a core aspect of the AWS shared responsibility model.

</details>

---

## Question 424: CLF-C02-ET-Q424
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following is a characteristic of the AWS account root user?

**Choices:**
- A) The root user is the only user that can be configured with multi-factor authentication (MFA).
- B) The root user is the only user that can access the AWS Management Console.
- C) The root user is the first sign-in identity that is available when an AWS account is created.
- D) The root user has a password that cannot be changed.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Root user privileges
• Root user = Account Owner (created when the account is created)
• Has complete access to all AWS services and resources
• Lock away your AWS account root user access keys!
---
Selected Answer: C
The root user is the first sign-in identity that is available when an AWS account is created: The root user is the initial identity associated with an AWS account and has full access to all AWS services and resources. It is created when the AWS account is first set up.
---
Selected Answer: C
The root user is the first sign-in identity that is available when an AWS account is created.

</details>

---

## Question 425: CLF-C02-ET-Q425
**Domain 3:** Cloud Technology and Services  

**Question:**  
An Amazon EC2 instance previously used for development is inaccessible and no longer appears in the AWS Management Console.

Which AWS service should be used to determine what action made this EC2 instance inaccessible?

**Choices:**
- A) Amazon CloudWatch Logs
- B) AWS Security Hub
- C) Amazon Inspector
- D) AWS CloudTraiI

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
https://docs.aws.amazon.com/cloudtrail/
---
D. AWS CloudTrail

AWS CloudTrail is the service that records API calls and related events made on your AWS account. If an Amazon EC2 instance is inaccessible or if there are actions taken on the instance, CloudTrail can be used to determine what actions were performed, who performed them, and when they occurred. It provides a detailed history of changes and activity within your AWS environment.

</details>

---

## Question 426: CLF-C02-ET-Q426
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company's application developers need to quickly provision and manage AWS services by using scripts.

Which AWS offering should the developers use to meet these requirements?

**Choices:**
- A) AWS CLI
- B) AWS CodeBuild
- C) AWS Cloud Adoption Framework (AWS CAF)
- D) AWS Systems Manager Session Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://www.agilevision.io/blog/provisioning-of-aws-resources
---
Selected Answer: A
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
---
A: AWS CLI

</details>

---

## Question 427: CLF-C02-ET-Q427
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to migrate unstructured data to AWS. The data needs to be securely moved with inflight encryption and end-to-end data validation.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Application Migration Service
- B) Amazon Elastic File System (Amazon EFS)
- C) AWS DataSync
- D) AWS Migration Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS DataSync
---
Selected Answer: C
https://aws.amazon.com/datasync/#:~:text=replication%20or%20archival.-,How%20it%20works,-Transfer%20data%20between
---
Selected Answer: C
https://aws.amazon.com/datasync/
Securely discover and migrate your data to AWS with end-to-end security, including data encryption and data integrity validation.

</details>

---

## Question 428: CLF-C02-ET-Q428
**Domain 3:** Cloud Technology and Services  

**Question:**  
A development team wants to deploy multiple test environments for an application in a fast, repeatable manner.

Which AWS service should the team use?

**Choices:**
- A) Amazon EC2
- B) AWS CloudFormation
- C) Amazon QuickSight
- D) Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Answer is B: Cloudformation.

https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/testing-phase.html

Provisioning complete environments
While you can create complex test environments containing multiple instances using the AWS APIs, command line tools, or the AWS Management Console, AWS CloudFormation makes it even easier to create a collection of related AWS resources and provision them in an orderly and predictable fashion.

AWS CloudFormation uses templates to create and delete a collection of resources together as a single unit (a stack). A complete test environment running on AWS can be described in a template, which is a text file in JSON or YAML format.
---
Selected Answer: B
the anser is B
---
Selected Answer: B
CloudFormation

</details>

---

## Question 429: CLF-C02-ET-Q429
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to quickly implement a continuous integration/continuous delivery (CI/CD) pipeline.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Config
- B) Amazon Cognito
- C) AWS DataSync
- D) AWS CodeStar

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. AWS CodeStar

Explanation:
AWS CodeStar is a managed service specifically designed to enable quick implementation of a continuous integration/continuous delivery (CI/CD) pipeline. It provides a unified user interface to set up, manage, and collaborate on software development projects.
---
Selected Answer: D
D. AWS CodeStar
---
I got this in exam yesterday

</details>

---

## Question 430: CLF-C02-ET-Q430
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud deployment model uses AWS Outposts as part of the application deployment infrastructure?

**Choices:**
- A) On-premises
- B) Serverless
- C) Cloud-native
- D) Hybrid

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (93%). Contributor Answer: D.

Community Rationale & Discussion:
D (Hybrid) is correct as per ChatGPT
---
Selected Answer: D
D. Hybrid

AWS Outposts brings native AWS services, infrastructure, and operating models to virtually any data center, co-location space, or on-premises facility. It extends AWS infrastructure, services, APIs, and tools to virtually any customer location, allowing for a consistent hybrid experience across on-premises and cloud environments.
---
Selected Answer: D
https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.pdf

</details>

---

## Question 431: CLF-C02-ET-Q431
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is a fully managed graph database service on AWS?

**Choices:**
- A) Amazon Aurora
- B) Amazon FSx
- C) Amazon DynamoDB
- D) Amazon Neptune

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
https://docs.aws.amazon.com/neptune/latest/userguide/intro.html
---
Selected Answer: D
Amazon Neptune is a fully managed graph database service that scales to handle billions of relationships and lets you query them with milliseconds latency, at a low cost for that kind of capacity.
https://docs.aws.amazon.com/neptune/latest/userguide/graph-get-started.html
---
Selected Answer: D
D. amazon neptune is the graph database

</details>

---

## Question 432: CLF-C02-ET-Q432
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service could an administrator use to provide desktop environments for several employees?

**Choices:**
- A) AWS Organizations
- B) AWS Fargate
- C) AWS WAF
- D) AWS WorkSpaces

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html

Important Note: I am noticing that there are incorrect answers for may questions in this question set. I would request administrator of this question set (384 questions) to review the answers for all questions and replace the incorrect answers with correct answers for applicable questions.
---
Selected Answer: D
Amazon WorkSpaces offers an easy way to provide a cloud-based desktop experience to your end users
https://docs.aws.amazon.com/workspaces/
---
D : AWS Workspaces

</details>

---

## Question 433: CLF-C02-ET-Q433
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature is used to send both text and email messages from distributed applications?

**Choices:**
- A) Amazon Simple Notification Service (Amazon SNS)
- B) Amazon Simple Email Service (Amazon SES)
- C) Amazon CloudWatch alerts
- D) Amazon Simple Queue Service (Amazon SQS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `97%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (97%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The answer is A.

Amazon Simple Notification Service (Amazon SNS) sends notifications two ways, A2A and A2P. A2A provides high-throughput, push-based, many-to-many messaging between distributed systems, microservices, and event-driven serverless applications. These applications include Amazon Simple Queue Service (SQS), Amazon Kinesis Data Firehose, AWS Lambda, and other HTTPS endpoints. A2P functionality lets you send messages to your customers with SMS texts, push notifications, and email. 
https://aws.amazon.com/sns/
---
Selected Answer: A
A. Amazon Simple Notification Service (Amazon SNS): A fully managed messaging service that enables the sending of both text (SMS) and email messages from distributed applications. It allows applications to send messages to a variety of endpoints, including email, SMS, HTTP/HTTPS, and more.

B. Amazon Simple Email Service (Amazon SES): Amazon SES is focused on sending email messages, not text (SMS) messages.

C. Amazon CloudWatch alerts: CloudWatch is primarily for monitoring and managing resources, not for sending text or email messages.

D. Amazon Simple Queue Service (Amazon SQS): SQS is used for reliably transmitting messages between components but is not designed for sending text or email messages.
---
Selected Answer: A
Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service that enables applications to send both text messages (SMS) and email notifications to subscribers. It supports multiple communication protocols, including SMS, email, HTTP/HTTPS, and Amazon SQS.

</details>

---

## Question 434: CLF-C02-ET-Q434
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature gives users the ability to capture information about network traffic in a VPC?

**Choices:**
- A) VPC Flow Logs
- B) Amazon Inspector
- C) VPC route tables
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. VPC Flow Logs
---
Selected Answer: A
VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. 
https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html
---
A
is correct answer

</details>

---

## Question 435: CLF-C02-ET-Q435
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is stopped or terminated?

**Choices:**
- A) Amazon Elastic Block Store (Amazon EBS)
- B) Amazon EC2 instance store
- C) Amazon Elastic File System (Amazon EFS)
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
What are Instance Stores?
Instance Store is a storage volume that acts as a physical hard drive.
It provides temporary storage for Amazon EC2 instance.
The data in an instance store persists during the lifetime of its instance.
If an instance reboots, data in the instance store will persist.
When the instance hibernates or terminates, you lose any data in the instance store.
If an instance starts from a stopped state, it might start on another host where the used instance store does not exist.
It is recommended to avoid storing valuable data in the store instance.
Instance Stores are good for temporary files, and data that can be easily recreated.
https://www.w3schools.com/aws/aws_cloudessentials_instancestores.php
---
Selected Answer: B
Letterman B
---
Selected Answer: B
Pretty sure, B

</details>

---

## Question 436: CLF-C02-ET-Q436
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to provide access to Windows file shares in AWS from its on-premises workloads. The company does not want to provision any additional infrastructure or applications in its data center.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon FSx File Gateway
- B) AWS DataSync
- C) Amazon S3
- D) AWS Snow Family

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon FSx File Gateway
Fast, low-latency access on premises to fully managed file shares
Amazon FSx File Gateway optimizes on-premises access to fully managed, highly reliable file shares in Amazon FSx for Windows File Server. Customers with unstructured or file data, whether from SMB-based group shares, or business applications, may require on-premises access to meet low-latency requirements. Amazon FSx File Gateway helps accelerate your file-based storage migration to the cloud to enable faster performance, improved data protection, and reduced cost.
https://aws.amazon.com/storagegateway/file/fsx/
---
Selected Answer: A
https://aws.amazon.com/fsx/windows/

https://aws.amazon.com/blogs/storage/accessing-your-file-workloads-from-on-premises-with-file-gateway/
---
Selected Answer: A
Amazon FSx File Gateway optimizes on-premises access to fully managed, highly reliable file shares in Amazon FSx for Windows File Server. 
https://aws.amazon.com/storagegateway/file/fsx/

</details>

---

## Question 437: CLF-C02-ET-Q437
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants durable storage for static content and infinitely scalable data storage infrastructure at the lowest cost.

Which AWS service should the company choose?

**Choices:**
- A) Amazon Elastic Block Store (Amazon EBS)
- B) Amazon S3
- C) AWS Storage Gateway
- D) Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
S3 is a correct answer
Amazon S3 is object storage built to store and retrieve any amount of data from anywhere. S3 is a simple storage service that offers industry leading durability, availability, performance, security, and virtually unlimited scalability at very low costs.
---
Selected Answer: B
Amazon S3
---
Selected Answer: B
Absolutely B

</details>

---

## Question 438: CLF-C02-ET-Q438
**Domain 3:** Cloud Technology and Services  

**Question:**  
An ecommerce company wants to use Amazon EC2 Auto Scaling to add and remove EC2 instances based on CPU utilization.

Which AWS service or feature can initiate an Amazon EC2 Auto Scaling action to achieve this goal?

**Choices:**
- A) Amazon Simple Queue Service (Amazon SQS)
- B) Amazon Simple Notification Service (Amazon SNS)
- C) AWS Systems Manager
- D) Amazon CloudWatch alarm

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
the anser is D
---
Selected Answer: D
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html
---
Selected Answer: D
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html

</details>

---

## Question 439: CLF-C02-ET-Q439
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to transform its workforce by attracting and developing a digitally fluent high-performance workforce. The company wants to attract a diverse and inclusive workforce with appropriate mix of technical and non-technical skills.

Which AWS Cloud Adoption Framework (AWS CAF) perspective will meet these requirements?

**Choices:**
- A) Business
- B) People
- C) Platform
- D) Operations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
CAF > People > Workforce transformation – To succeed in your cloud transformation, take a proactive approach to talent enablement planning beyond traditional HR to include C-suite leadership, and modernize your approaches to leadership, learning, rewards, inclusion, performance management, career mobility, and hiring.
You will need a diverse and inclusive workforce with the appropriate mix of technical and non-technical skills. Identify gaps in roles and skills across your entire organization and develop a workforce strategy that will improve your organizational cloud capability.
---
Selected Answer: B
Key word: diverse*
---
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/people-perspective.html
please help discussing on 314. Many Thanks.

</details>

---

## Question 440: CLF-C02-ET-Q440
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to move its on-premises databases to managed cloud database services by using a simplified migration process.

Which AWS service or tool can help the company meet this requirement?

**Choices:**
- A) AWS Storage Gateway
- B) AWS Application Migration Service
- C) AWS DataSync
- D) AWS Database Migration Service (AWS DMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
https://aws.amazon.com/dms/
---
D. AWS Database Migration Service (AWS DMS)

AWS Database Migration Service (DMS) is the service designed to help migrate on-premises databases to managed cloud database services in a simplified manner. It supports various database engines and provides a reliable and efficient way to migrate data with minimal downtime.

</details>

---

## Question 441: CLF-C02-ET-Q441
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs a fully managed file server that natively supports Microsoft workloads and file systems. The file server must also support the SMB protocol.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon Elastic File System (Amazon EFS)
- B) Amazon FSx for Lustre
- C) Amazon FSx for Windows File Server
- D) Amazon Elastic Block Store (Amazon EBS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
https://aws.amazon.com/fsx/windows/
---
Selected Answer: C
Provide highly available, high performance storage to your Windows applications with full SMB support.
https://aws.amazon.com/fsx/windows/
---
C. Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is the AWS service that provides a fully managed file server that natively supports Microsoft workloads and file systems. It is built on Windows Server and supports the Server Message Block (SMB) protocol, making it suitable for seamlessly integrating with Microsoft applications and workloads.

</details>

---

## Question 442: CLF-C02-ET-Q442
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has been storing monthly reports in an Amazon S3 bucket. The company exports the report data into comma-separated values (.csv) files. A developer wants to write a simple query that can read all of these files and generate a summary report.

Which AWS service or feature should the developer use to meet these requirements with the LEAST amount of operational overhead?

**Choices:**
- A) Amazon S3 Select
- B) Amazon Athena
- C) Amazon Redshift
- D) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (91%). Contributor Answer: B.

Community Rationale & Discussion:
B. Amazon Athena

Amazon Athena is a serverless query service that allows you to analyze data directly in Amazon S3 using SQL queries. It supports a variety of file formats, including comma-separated values (.csv). With Athena, the developer can write SQL queries to read the .csv files stored in the Amazon S3 bucket and generate the desired summary report without the need to provision or manage infrastructure.
---
this is my last pay to exam-topics, there are A LOT OF wrong responses.
---
Selected Answer: B
B. Amazon Athena

</details>

---

## Question 443: CLF-C02-ET-Q443
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which AWS feature provides a no-cost platform for AWS users to join community groups, ask questions, find answers, and read community-generated articles about best practices?

**Choices:**
- A) AWS Knowledge Center
- B) AWS re:Post
- C) AWS IQ
- D) AWS Enterprise Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS re:Post
---
Selected Answer: B
the answer is B
---
Selected Answer: B
https://repost.aws/

</details>

---

## Question 444: CLF-C02-ET-Q444
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants an automated process to continuously scan its Amazon EC2 instances for software vulnerabilities.
Which AWS service will meet these requirements?

**Choices:**
- A) Amazon GuardDuty
- B) Amazon Inspector
- C) Amazon Detective
- D) Amazon Cognito

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
"Amazon Inspector is an automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2), AWS Lambda functions, and container workloads for software vulnerabilities and unintended network exposure."

Reference: https://aws.amazon.com/inspector/faqs/
---
Selected Answer: B
A. Amazon GuardDuty: A threat detection service that continuously monitors for malicious activity and unauthorized behavior in AWS accounts, doesn’t scan for software vulnerabilities.
B. Amazon Inspector is designed to help assess applications for vulnerabilities and deviations from best practices.
C. A security service that helps users investigate and identify the root cause of potential security issues. Does not perform vulnerability scanning.
D. Amazon Cognito - Manages user authentication and access, not for scanning vulnerabilities.
---
Selected Answer: B
B. Amazon Inspector is an automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2), AWS Lambda functions, and container workloads for software vulnerabilities and unintended network exposure."

</details>

---

## Question 445: CLF-C02-ET-Q445
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to perform data processing once a week that typically takes about 5 hours to complete.
Which AWS service should the company use for this workload?

**Choices:**
- A) AWS Lambda
- B) Amazon EC2
- C) AWS CodeDeploy
- D) AWS Wavelength

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `96%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (96%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The best AWS service for a workload that needs to be processed once a week for about 5 hours is Amazon EC2.

AWS Lambda is a serverless computing service that runs your code without provisioning or managing servers. However, Lambda functions have a maximum execution time of 15 minutes. Therefore, Lambda is not suitable for workloads that need to run for longer than 15 minutes.

Amazon EC2 is a scalable computing service that provides instances with varying capabilities and pricing options. You can choose an EC2 instance that is right for your data processing job and then terminate the instance when the job is complete. This will help you to save money on your AWS bill.
---
If you preparing for AWS Cloud Practitioner CLF-C02 & would like to clear this exam with high score then please visit this series. #aws #cloudpractitioner #ind #ICC #wc2023
https://www.youtube.com/watch?v=4D3ihaeS9uY&list=PLgbuoziNXKY2zd3ujBlKvvDwRdwEm-VLI

https://www.youtube.com/@ExamTricksTips2023
---
Selected Answer: B
B. Amazon EC2 is a scalable computing service that provides instances with varying capabilities and pricing options. You can choose an EC2 instance that is right for your data processing job and then terminate the instance when the job is complete. This will help you to save money on your AWS bill.

</details>

---

## Question 446: CLF-C02-ET-Q446
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature provides log information of the inbound and outbound traffic on network interfaces in a VPC?

**Choices:**
- A) Amazon CloudWatch Logs
- B) AWS CloudTrail
- C) VPC Flow Logs
- D) AWS Identity and Access Management (IAM)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The correct answer is C.

VPC flow logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow logs data can be published to either Amazon CloudWatch Logs or Amazon S3. You can monitor your VPC flow logs to gain operational visibility about your network dependencies and traffic patterns, detect anomalies and prevent data leakage, or troubleshoot network connectivity and configuration issues. 
https://aws.amazon.com/vpc/faqs/#:~:text=VPC%20flow%20logs%20is%20a,network%20interfaces%20in%20your%20VPC.
---
If you preparing for AWS Cloud Practitioner CLF-C02 & would like to clear this exam with high score then please visit this series. #aws #cloudpractitioner #ind #ICC #wc2023
https://www.youtube.com/watch?v=4D3ihaeS9uY&list=PLgbuoziNXKY2zd3ujBlKvvDwRdwEm-VLI

https://www.youtube.com/@ExamTricksTips2023
---
Selected Answer: C
A. Amazon CloudWatch Logs: Stores and analyzes logs (including VPC Flow Logs), but inbound and outbound traffic logs are generated by VPC Flow Logs
B. AWS CloudTrail: Tracks API calls, not network traffic.
C. VPC Flow Logs: capture information about inbound and outbound IP traffic in your VPC.
D. AWS IAM: Manages permissions and access.

</details>

---

## Question 447: CLF-C02-ET-Q447
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to manage deployed IT services and govern its infrastructure as code (IaC) templates.
Which AWS service will meet this requirement?

**Choices:**
- A) AWS Resource Explorer
- B) AWS Service Catalog
- C) AWS Organizations
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (88%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The answer is B.

AWS Service Catalog lets you centrally manage your cloud resources to achieve governance at scale of your infrastructure as code (IaC) templates, written in CloudFormation or Terraform configurations. With AWS Service Catalog, you can meet your compliance requirements while making sure your customers can quickly deploy the cloud resources they need.
https://aws.amazon.com/servicecatalog/
---
Selected Answer: B
enables organizations to centrally manage and distribute approved AWS resources and templates.
---
Selected Answer: B
AWS Service Catalog - This allows us to create , organize, and govern curated IaC templates catalog of AWS Resources that can be sharedd at the permission level so you can quickly provision approvedd cloud resources without needing direct access to the underlying cloud resources

</details>

---

## Question 448: CLF-C02-ET-Q448
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to design a centralized storage system to manage the configuration data and passwords for its critical business applications.
Which AWS service or capability will meet these requirements MOST cost-effectively?

**Choices:**
- A) AWS Systems Manager Parameter Store
- B) AWS Secrets Manager
- C) AWS Config
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `74%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (74%). Contributor Answer: A.

Community Rationale & Discussion:
both are correct but the question here is the MOST cost effective and that is Parameter Store that is free while Secret Manager is $1 per secret
---
Selected Answer: A
both are correct but the question here is the MOST cost effective and that is Parameter Store that is free while Secret Manager is $1 per secret
---
Selected Answer: A
AWS Systems Manager Parameter Store is designed to securely store and manage configuration data, passwords, and other sensitive information like API keys or database credentials. It provides a simple, centralized solution to manage application settings and secrets. It supports versioning, access control, and encryption of sensitive data, making it a secure and cost-effective solution for your use case

</details>

---

## Question 449: CLF-C02-ET-Q449
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user needs programmatic access to AWS resources through the AWS CLI or the AWS API.
Which option will provide the user with the appropriate access?

**Choices:**
- A) Amazon Inspector
- B) Access keys
- C) SSH public keys
- D) AWS Key Management Service (AWS KMS) keys

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The answer is B.

"Access keys are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK)."
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html
---
Selected Answer: B
A. Amazon Inspector: A security assessment service that helps improve the security and compliance of applications deployed on AWS. It is not directly related to providing programmatic access through the AWS CLI or API.

B. Access keys: Consist of an access key ID and a secret access key, and they are used to provide programmatic access to AWS resources through the AWS CLI or API. Access keys are associated with IAM users.

C. SSH public keys: Are used for authenticating users when connecting to instances using SSH (Secure Shell). While SSH public keys provide access to instances, they are not used for programmatic access through the AWS CLI or API.

D. AWS Key Management Service (AWS KMS) keys: Amanaged service that makes it easy for users to create and control encryption keys used to encrypt their data. It is not used for providing programmatic access through the AWS CLI or API.
---
Selected Answer: B
B. Access keys

</details>

---

## Question 450: CLF-C02-ET-Q450
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to search for text in documents that are stored in Amazon S3.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Kendra
- B) Amazon Rekognition
- C) Amazon Polly
- D) Amazon Lex

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
answer is A.

- Amazon Rekognition is a cloud-based image and video analysis service that makes it easy to add advanced computer vision capabilities to your applications.
- Amazon Polly is a machine learning service that converts text to speech.
-Amazon Lex is a service that builds conversational interfaces using voice and text.
---
Selected Answer: A
https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html
---
Selected Answer: A
https://aws.amazon.com/kendra/?p=pm&c=ml&pd=kd&z=4

</details>

---

## Question 451: CLF-C02-ET-Q451
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS services make use of global edge locations? (Choose two.)

**Choices:**
- A) AWS Fargate
- B) Amazon CloudFront
- C) AWS Global Accelerator
- D) AWS Wavelength
- E) Amazon VPC

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
the answer is BC
---
Selected Answer: BC
Amazon CloudFront & AWS Global Accelerator

https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
https://jayendrapatil.com/aws-cloudfront-vs-global-accelerator/
---
Selected Answer: BC
B. Amazon CloudFront
C. AWS Global Accelerator

</details>

---

## Question 452: CLF-C02-ET-Q452
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user needs a relational database but does not have the resources to manage the hardware, resiliency, and replication.

Which AWS service option meets the user's requirements?

**Choices:**
- A) Run MySQL on Amazon Elastic Container Service (Amazon ECS).
- B) Run MySQL on Amazon EC2.
- C) Choose Amazon RDS for MySQL.
- D) Choose Amazon ElastiCache for Redis.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
https://aws.amazon.com/rds/features/?pg=ln&sec=be
---
Selected Answer: C
- Running MySQL on Amazon ECS still needs to manage DB configuration.
- Running MySQL on Amazon EC2 is the same
- ElastiCache for Redis is an in-memory store, irrelevantly
- Amazon RDS is a fully managed cloud database service => Correct
---
C. Choose Amazon RDS for MySQL.

Amazon RDS (Relational Database Service) is a fully managed relational database service that takes care of tasks such as hardware provisioning, database setup, patching, and backups. It provides a managed environment for various database engines, including MySQL. With Amazon RDS for MySQL, users can offload the operational aspects of database management and focus on their application development.

</details>

---

## Question 453: CLF-C02-ET-Q453
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to deploy applications in the AWS Cloud as quickly as possible. The company also needs to minimize the complexity that is related to the management of AWS resources.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS Config
- B) AWS Elastic Beanstalk
- C) Amazon EC2
- D) Amazon Personalize

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
the answer is B
---
Selected Answer: B
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
---
Selected Answer: B
Deploy scalable web applications in minutes without the complexity of provisioning and managing underlying infrastructure.
https://aws.amazon.com/elasticbeanstalk/?trk=29514334-a45b-4894-96c1-cd1eff3a5e50&sc_channel=ps&ef_id=Cj0KCQiAnfmsBhDfARIsAM7MKi1pPCJ9VJze5orCGeZOo9gvY1VflkgqSxKy_KDRJtWhl0lop50eZUsaAluYEALw_wcB:G:s&s_kwcid=AL!4422!3!651510255288!p!!g!!amazon%20beanstalk!19836376744!146491721025&gclid=Cj0KCQiAnfmsBhDfARIsAM7MKi1pPCJ9VJze5orCGeZOo9gvY1VflkgqSxKy_KDRJtWhl0lop50eZUsaAluYEALw_wcB

</details>

---

## Question 454: CLF-C02-ET-Q454
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which mechanism allows developers to access AWS services from application code?

**Choices:**
- A) AWS Software Development Kit
- B) AWS Management Console
- C) AWS CodePipeline
- D) AWS Config

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://docs.aws.amazon.com/panorama/latest/dev/applications-awssdk.html
---
Selected Answer: A
https://aws.amazon.com/what-is/sdk/
---
A. AWS Software Development Kit

The AWS Software Development Kit (SDK) is the mechanism that allows developers to access AWS services from application code. The SDK provides libraries and APIs that developers can use to interact with AWS services programmatically. It supports multiple programming languages, making it easier for developers to integrate AWS services into their applications.

</details>

---

## Question 455: CLF-C02-ET-Q455
**Domain 2:** Security and Compliance  

**Question:**  
A company is migrating to the AWS Cloud. The company wants to understand and identify potential security misconfigurations or unexpected behaviors. The company wants to prioritize any protective controls it might need.

Which AWS Cloud Adoption Framework (AWS CAF) security perspective capability will meet these requirements?

**Choices:**
- A) Identity and access management
- B) Threat detection
- C) Platform engineering
- D) Availability and continuity management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Threat detection – Understand and identify potential security misconfigurations, threats, or unexpected behaviors. 
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html
---
Selected Answer: B
B. Threat Detection.

https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html

Threat detection – Understand and identify potential security misconfigurations, threats, or unexpected behaviors.

</details>

---

## Question 456: CLF-C02-ET-Q456
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to establish a private network connection between AWS and its corporate network.

Which AWS service or feature will meet this requirement?

**Choices:**
- A) Amazon Connect
- B) Amazon Route 53
- C) AWS Direct Connect
- D) VPC peering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
direct connect
---
Selected Answer: C
C, because the connection needs to be private
---
Selected Answer: C
https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

</details>

---

## Question 457: CLF-C02-ET-Q457
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS services or features give users the ability to create a network connection between two VPCs? (Choose two.)

**Choices:**
- A) VPC endpoints
- B) Amazon Route 53
- C) VPC peering
- D) AWS Direct Connect
- E) AWS Transit Gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CE (100%). Contributor Answer: CE.

Community Rationale & Discussion:
Selected Answer: CE
ChatGPT
---
Selected Answer: CE
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html
https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-isolated.html
---
Selected Answer: CE
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html
https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-isolated.html

</details>

---

## Question 458: CLF-C02-ET-Q458
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service converts text to lifelike voices?

**Choices:**
- A) Amazon Transcribe
- B) Amazon Rekognition
- C) Amazon Polly
- D) Amazon Textract

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Answer is C
Amazon Transcribe is a service that uses machine learning to convert audio data to text.
Amazon Polly is a machine learning service that converts text to speech.
Amazon Textract is a machine learning service that can extract text from scanned documents.
Amazon Rekognition is a cloud-based image and video analysis service that makes it easy to add advanced computer vision capabilities to your applications.
---
Selected Answer: C
https://docs.aws.amazon.com/es_es/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/amazon-polly.html
---
Selected Answer: C
https://aws.amazon.com/polly/

</details>

---

## Question 459: CLF-C02-ET-Q459
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use application stacks to run a workload in the AWS Cloud. The company wants to use pre-configured instances.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Lightsail
- B) Amazon Athena
- C) AWS Outposts
- D) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
LightSail gets you started quickly with preconfigured Linux and Windows application stacks and an intuitive management console.
https://aws.amazon.com/free/compute/lightsail/?trk=13b576c7-da6f-4140-99fb-c995644b5b46&sc_channel=ps&ef_id=Cj0KCQiAnfmsBhDfARIsAM7MKi3tzalv_9YtKe_wGWw-C2gG-kay_JhyzyBG_bnDcLKeoyKyg7klfI8aAouNEALw_wcB:G:s&s_kwcid=AL!4422!3!536393441656!p!!g!!lightsail%20cloud!11543056261!112002970709&gclid=Cj0KCQiAnfmsBhDfARIsAM7MKi3tzalv_9YtKe_wGWw-C2gG-kay_JhyzyBG_bnDcLKeoyKyg7klfI8aAouNEALw_wcB
---
A. Amazon Lightsail

Amazon Lightsail is the AWS service that provides pre-configured instances and application stacks designed to simplify the process of deploying and managing applications in the cloud. It is a straightforward way for users to launch instances with pre-configured templates for common use cases, making it easy to get started without the need for extensive AWS expertise.

Therefore, for the specific requirements of using pre-configured instances and application stacks, Amazon Lightsail (Option A) is the most suitable choice.
---
Selected Answer: A
Lightsail is the most suitable choice:

-Pre-configured Instances and Application Stacks: Lightsail offers a wide range of pre-configured instances with popular software stacks already installed and ready to use

</details>

---

## Question 460: CLF-C02-ET-Q460
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company runs thousands of simultaneous simulations using AWS Batch. Each simulation is stateless, is fault tolerant, and runs for up to 3 hours.
Which pricing model enables the company to optimize costs and meet these requirements?

**Choices:**
- A) Reserved Instances
- B) Spot Instances
- C) On-Demand Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
B = Keyword is Fault Tolerant
---
Selected Answer: B
Spot Instances provide significant savings (up to 90% off On-Demand pricing) and are ideal for stateless and fault-tolerant workloads like AWS Batch.
---
Selected Answer: B
The key word is fault tolerant and optimize costs so Spot Instances are the better choice.

</details>

---

## Question 461: CLF-C02-ET-Q461
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which AWS services are supported by Savings Plans? (Choose two.)

**Choices:**
- A) Amazon EC2
- B) Amazon RDS
- C) Amazon SageMaker
- D) Amazon Redshift
- E) Amazon DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (93%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html
three types: EC2 CPU, EC2 Instance and SageMaker
---
Selected Answer: AC
https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-services.html
---
Selected Answer: AE
Amazon RDS, Amazon SageMaker, and Amazon Redshift are not directly covered by Savings Plans, they do have their own cost-saving options and reserved instance pricing models.

</details>

---

## Question 462: CLF-C02-ET-Q462
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool can provide rightsizing recommendations for Amazon EC2 resources at no additional cost?

**Choices:**
- A) AWS Well-Architected Tool
- B) Amazon CloudWatch
- C) AWS Cost Explorer
- D) Amazon S3 analytics

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Am confused on how cist explorer could be the answer.
---
Selected Answer: C
https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html
---
Selected Answer: C
https://aws.amazon.com/aws-cost-management/aws-cost-explorer/

</details>

---

## Question 463: CLF-C02-ET-Q463
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company operates a petabyte-scale data warehouse to analyze its data. The company wants a solution that will not require manual hardware and software management.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon DocumentDB (with MongoDB compatibility)
- B) Amazon Redshift
- C) Amazon Neptune
- D) Amazon ElastiCache

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://docs.aws.amazon.com/redshift/
---
Selected Answer: B
Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools
https://docs.aws.amazon.com/redshift/
---
B. Amazon Redshift

Amazon Redshift is a fully managed, petabyte-scale data warehouse service that allows companies to analyze large volumes of data. It is designed to be scalable, fast, and cost-effective. With Amazon Redshift, there is no need for manual hardware and software management, as AWS takes care of provisioning, configuring, and maintaining the infrastructure.

</details>

---

## Question 464: CLF-C02-ET-Q464
**Domain 3:** Cloud Technology and Services  

**Question:**  
A library wants to automate the classification of electronic books based on the contents of the books.

Which AWS service should the library use to meet this requirement?

**Choices:**
- A) Amazon Redshift
- B) Amazon CloudSearch
- C) Amazon Comprehend
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html
---
Selected Answer: C
https://aws.amazon.com/comprehend/
Differentiate your business by training a model to classify documents and identify terms, with no machine learning experience required.
---
C. Amazon Comprehend

Amazon Comprehend is the AWS service that can be used for natural language processing tasks, including text classification. It can analyze and understand the content of electronic books to automatically classify them based on their contents.

</details>

---

## Question 465: CLF-C02-ET-Q465
**Domain 2:** Security and Compliance  

**Question:**  
Which task is a responsibility of AWS, according to the AWS shared responsibility model?

**Choices:**
- A) Encryption of application data
- B) Authentication of application users
- C) Protection of physical network infrastructure
- D) Configuration of firewalls

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
sure is AWS DC physical network infrastructure is.
---
C. Protection of physical network infrastructure

According to the AWS shared responsibility model:

AWS is responsible for the security of the cloud, which includes protecting the physical infrastructure, hardware, software, and facilities that run AWS services.
---
Selected Answer: C
C is correct

</details>

---

## Question 466: CLF-C02-ET-Q466
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which options are AWS Cloud Adoption Framework (AWS CAF) cloud transformation journey recommendations? (Choose two.)

**Choices:**
- A) Envision phase
- B) Align phase
- C) Assess phase
- D) Mobilize phase
- E) Migrate and modernize phase

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AB`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AB (71%). Contributor Answer: AB.

Community Rationale & Discussion:
Selected Answer: AB
A. Envision phase
B. Align phase
---
Selected Answer: AD
A and D
---
Selected Answer: AB
A & B

https://aws.amazon.com/cloud-adoption-framework/#:~:text=and%20customer%20experience.-,How%20it%20works,-Envision

</details>

---

## Question 467: CLF-C02-ET-Q467
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to generate a list of IAM users. The company also wants to view the status of various credentials that are associated with the users, such as password, access keys, and multi-factor authentication (MFA) devices.

Which AWS service or feature will meet these requirements?

**Choices:**
- A) IAM credential report
- B) AWS IAM Identity Center (AWS Single Sign-On)
- C) AWS Identity and Access Management Access Analyzer
- D) AWS Cost and Usage Report

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html
---
Selected Answer: A
You can generate and download a credential report that lists all users in your account and the status of their various credentials, including passwords, access keys, and MFA devices. 
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html
---
Selected Answer: A
A.

Its a report that lists all your account's users and the status of their various
credentials.

</details>

---

## Question 468: CLF-C02-ET-Q468
**Domain 1:** Cloud Concepts  

**Question:**  
A company is designing its AWS workloads so that components can be updated regularly and so that changes can be made in small, reversible increments.

Which pillar of the AWS Well-Architected Framework does this design support?

**Choices:**
- A) Security
- B) Performance efficiency
- C) Operational excellence
- D) Reliability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Key word designing
---
Selected Answer: C
https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html
---
Selected Answer: C
https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html

</details>

---

## Question 469: CLF-C02-ET-Q469
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to track tags, buckets, and prefixes for its Amazon S3 objects.

Which S3 feature will meet this requirement?

**Choices:**
- A) S3 Inventory report
- B) S3 Lifecycle
- C) S3 Versioning
- D) S3 ACLs

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon S3 Inventory list
An inventory list file contains a list of the objects in the source bucket and metadata for each object.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html

 you can use an S3 Inventory report that lists your stored objects within an S3 bucket or with a specific prefix, and their respective metadata and encryption status. S3 Inventory can be configured to generate reports on a daily or a weekly basis.
https://aws.amazon.com/s3/features/
---
Selected Answer: A
the answer is A
---
Selected Answer: A
https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html

</details>

---

## Question 470: CLF-C02-ET-Q470
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to allow users to authenticate and authorize multiple AWS accounts by using a single set of credentials.

Which AWS service or resource will meet this requirement?

**Choices:**
- A) AWS Organizations
- B) IAM user
- C) AWS IAM Identity Center (AWS Single Sign-On)
- D) AWS Control Tower

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Manage access to a multi-account AWS environment
Your users can use their directory credentials for single sign-on access to multiple AWS accounts. Their personalized web user portal shows their assigned roles in AWS accounts in one place. Users can sign in through the AWS Command Line Interface, AWS SDKs, or AWS Console Mobile Application using their directory credentials for a consistent authentication experience.
https://aws.amazon.com/iam/identity-center/
---
Selected Answer: C
AWS SSO
---
C. AWS IAM Identity Center (AWS Single Sign-On)

AWS Single Sign-On (SSO) enables centralized authentication and authorization across multiple AWS accounts and other business applications. It allows users to sign in once and access resources in various accounts without the need for separate credentials for each account. This helps simplify access management in a multi-account environment.

</details>

---

## Question 471: CLF-C02-ET-Q471
**Domain 1:** Cloud Concepts  

**Question:**  
What does the concept of agility mean in AWS Cloud computing? (Choose two.)

**Choices:**
- A) The speed at which AWS resources are implemented
- B) The speed at which AWS creates new AWS Regions
- C) The ability to experiment quickly
- D) The elimination of wasted capacity
- E) The low cost of entry into cloud computing

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (86%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
A. The speed at which AWS resources are implemented: Agility in AWS refers to the ability to quickly provision and implement resources, allowing users to adapt to changing requirements and scale resources as needed.

C. The ability to experiment quickly: Agility involves the capability to experiment rapidly, enabling users to innovate, test ideas, and iterate quickly in the cloud environment.

The other options are described as follows:

B. The speed at which AWS creates new AWS Regions: The creation of new AWS Regions is not typically within the control of individual AWS customers. AWS decides when and where to create new regions based on business considerations.

D. The elimination of wasted capacity: While efficiency and cost optimization are important aspects of cloud computing, the elimination of wasted capacity is not a direct aspect of the concept of agility.

E. The low cost of entry into cloud computing: While cost considerations are important, the low cost of entry is not a defining aspect of agility. Agility focuses more on speed, flexibility, and the ability to respond quickly to changing demands.
---
Selected Answer: AC
Agility in AWS Cloud computing refers to the ability to quickly provision resources, test new ideas, and adapt to changes with minimal effort and cost.
---
Selected Answer: AC
A. The speed at which AWS resources are implemented
C. The ability to experiment quickly

</details>

---

## Question 472: CLF-C02-ET-Q472
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company created an Amazon EC2 instance. The company wants to control the incoming and outgoing network traffic at the instance level.

Which AWS resource or service will meet this requirement?

**Choices:**
- A) AWS Shield
- B) Security groups
- C) Network Access Analyzer
- D) VPC endpoints

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Control traffic to your AWS resources using security groups
A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
---
Selected Answer: B
Keyword is instance.
---
Selected Answer: B
security groups

</details>

---

## Question 473: CLF-C02-ET-Q473
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use the AWS Cloud to deploy an application globally.

Which architecture deployment model should the company use to meet this requirement?

**Choices:**
- A) Multi-Region
- B) Single-Region
- C) Multi-AZ
- D) Single-AZ

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Global = RegionS = multi-region
AZ = Single region but different datacenters in that region

Answer is A
---
Selected Answer: A
Multi region
---
Selected Answer: A
A, Multi-Region.
Darn, these are bad from about question 250 up....

</details>

---

## Question 474: CLF-C02-ET-Q474
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a web application to interact with various AWS services.

Which AWS service or resource will meet this requirement?

**Choices:**
- A) AWS CloudShell
- B) AWS Marketplace
- C) AWS Management Console
- D) AWS CLI

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `68%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (68%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Difference between C. and D. CLI has a command-line interface, making is less user friendly. Question is asking about a web-based user interface which is simple to use.
---
Selected Answer: C
What’s the AWS CLI?
• A tool that enables you to interact with AWS services using commands in
your command-line shell
---
Selected Answer: D
The AWS CLI allows a web application or script to issue commands and interact programmatically with AWS services. It can perform actions such as creating resources, updating configurations, or fetching data from services.

</details>

---

## Question 475: CLF-C02-ET-Q475
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is migrating its applications from on-premises to the AWS Cloud. The company wants to ensure that the applications are assigned only the minimum permissions that are needed to perform all operations.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Identity and Access Management (IAM)
- B) Amazon CloudWatch
- C) Amazon Macie
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A is the correct answer
---
Selected Answer: A
How it works
With AWS Identity and Access Management (IAM), you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS.
https://aws.amazon.com/iam/
---
Selected Answer: A
Answer is A

</details>

---

## Question 476: CLF-C02-ET-Q476
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which options are AWS Cloud Adoption Framework (AWS CAF) governance perspective capabilities? (Choose two.)

**Choices:**
- A) Identity and access management
- B) Cloud financial management
- C) Application portfolio management
- D) Innovation management
- E) Product management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `89%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (89%). Contributor Answer: BC.

Community Rationale & Discussion:
B & C 
is correct answer
---
Selected Answer: BC
BC.

Governance Perspectives:
Program and Project Management
Benefits Management
Risk Management
Cloud Financial Management
Application Portfolio Management
Data Governance
Data Curation.
---
B & C are correct answers

</details>

---

## Question 477: CLF-C02-ET-Q477
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides a single location to track the progress of application migrations?

**Choices:**
- A) AWS Application Discovery Service
- B) AWS Application Migration Service
- C) AWS Service Catalog
- D) AWS Migration Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Migration Hub is a service that helps you plan, execute, and track migrations to AWS (single place)
---
Selected Answer: D
D is correct
---
Selected Answer: D
https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html

</details>

---

## Question 478: CLF-C02-ET-Q478
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company launched an Amazon EC2 instance with the latest Amazon Linux 2 Amazon Machine Image (AMI).

Which actions can a system administrator take to connect to the EC2 instance? (Choose two.)

**Choices:**
- A) Use Amazon EC2 Instance Connect.
- B) Use a Remote Desktop Protocol (RDP) connection.
- C) Use AWS Batch.
- D) Use AWS Systems Manager Session Manager.
- E) Use Amazon Connect.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
AWS Systems Manager Session Manager: “Administrators who want to grant and revoke access from a single location, and who want to provide one solution to users for Linux, macOS, and Windows Server managed nodes.“
---
Selected Answer: AD
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html
---
Selected Answer: AD
A and D

</details>

---

## Question 479: CLF-C02-ET-Q479
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which architecture concept describes the ability to deploy resources on demand and release resources when they are no longer needed?

**Choices:**
- A) High availability
- B) Decoupled architecture
- C) Resilience
- D) Elasticity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Elasticity is “The ability to acquire resources as you need them and release resources when you no longer need them
---
Selected Answer: D
D is correct
---
Selected Answer: D
Elasticity
The ability to acquire resources as you need them and release resources when you no longer need them. In the cloud, you want to do this automatically.
https://wa.aws.amazon.com/wat.concept.elasticity.en.html

</details>

---

## Question 480: CLF-C02-ET-Q480
**Domain 2:** Security and Compliance  

**Question:**  
Which task requires a user to sign in as the AWS account root user?

**Choices:**
- A) The deletion of IAM users
- B) The deletion of an AWS account
- C) The creation of an organization in AWS Organizations
- D) The deletion of Amazon EC2 instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `87%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (87%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B is correct
---
Selected Answer: B
Tasks that require root user credentials
https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html
---
Selected Answer: B
https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html

</details>

---

## Question 481: CLF-C02-ET-Q481
**Domain 3:** Cloud Technology and Services  

**Question:**  
What does the Amazon S3 Intelligent-Tiering storage class offer?

**Choices:**
- A) Payment flexibility by reserving storage capacity
- B) Long-term retention of data by copying the data to an encrypted Amazon Elastic Block Store (Amazon EBS) volume
- C) Automatic cost savings by moving objects between tiers based on access pattern changes
- D) Secure, durable, and lowest cost storage for data archival

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C is the correct answer
---
Selected Answer: C
Amazon S3 Intelligent-Tiering storage class
Automates storage cost savings by moving data when access patterns change
https://aws.amazon.com/s3/storage-classes/intelligent-tiering/
---
Selected Answer: C
the answer is C

</details>

---

## Question 482: CLF-C02-ET-Q482
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to block SQL injection attacks.
Which AWS service or feature can meet this requirement?

**Choices:**
- A) AWS WAF
- B) AWS Shield
- C) Network ACLs
- D) Security groups

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Confusion will come to choose between WAF or Shield. but all common web attack patterns (XSS, SQL Injection, etc...) dealt by WAF, special cases which can't be handled by WAF - will be handled by Shield primarily DDoS
---
A: AWS WAF allows you to create custom rules to block SQL injection attempts.

 Create a WebACL: Go to AWS WAF dashboard and create a new WebACL.

 Add a Rule: Inside the WebACL, add a new rule.

 SQLi Filter: Choose the rule type to look for SQLi patterns. AWS WAF has built-in SQLi filters.

 Attach Resources: Attach the WebACL to a resource, such as an Application Load Balancer, Amazon CloudFront distribution, or an API Gateway.

 Deploy: Save and deploy the WebACL.
---
Selected Answer: A
WS WAF (Web Application Firewall) helps protect web applications from common web exploits, including SQL injection attacks and cross-site scripting (XSS). You can create rules to block malicious requests before they reach your application.

</details>

---

## Question 483: CLF-C02-ET-Q483
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs Amazon EC2 instances for a workload that can tolerate interruptions.

Which EC2 instance purchasing option meets this requirement with the LARGEST discount compared to On-Demand prices?

**Choices:**
- A) Spot Instances
- B) Convertible Reserved Instances
- C) Standard Reserved Instances
- D) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
since the workload itself can "tolerate interruptions" as per the question, the answer is spot.

Amazon EC2 Spot Instances
Run fault-tolerant workloads for up to 90% off
Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity in the AWS cloud and are available at up to a 90% discount compared to On-Demand prices. You can use Spot Instances for various stateless, fault-tolerant, or flexible applications such as big data, containerized workloads, CI/CD, web servers, high-performance computing (HPC), and test & development workloads. 

https://aws.amazon.com/ec2/spot/
---
Selected Answer: A
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html
---
Selected Answer: A
Keyword is tolerate interruptions

</details>

---

## Question 484: CLF-C02-ET-Q484
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate to the AWS Cloud. The company wants to identify measurable business outcomes that will explain the value of the company's decision to migrate.

Which phase of the cloud transformation journey includes these activities?

**Choices:**
- A) Envision
- B) Align
- C) Scale
- D) Launch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `93%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (93%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Envision
---
Selected Answer: A
AWS Cloud Adoption Framework - CAF: Phases
There're 4 phases: How it works
1. Envision : identify measurable business outcomes and prioritize transformation opportunities in line with your strategic objectives.
2. Align : Identify capability gaps and cross-organizational dependencies.
3. Launch : focus executing cloud migration, deliver pilots in production
4. Scale : optimizing and expanding cloud capabilities / expand pilots and business value
---
Selected Answer: A
Envision
Identify and prioritize transformation opportunities in line with your strategic objectives. Associating your transformation initiatives with key stakeholders and measurable business outcomes will help you demonstrate value as you progress through your transformation journey.
https://aws.amazon.com/cloud-adoption-framework/

</details>

---

## Question 485: CLF-C02-ET-Q485
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or component allows inbound traffic from the internet to access a VPC?

**Choices:**
- A) Internet gateway
- B) NAT gateway
- C) AWS WAF
- D) VPC peering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `95%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (95%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Internet Gateway & NAT Gateways
• Internet Gateways helps our VPC
instances connect with the internet
• Public Subnets have a route to the
internet gateway
---
Selected Answer: A
A. Internet gateway
---
Selected Answer: A
Connect to the internet using an internet gateway
An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. It supports IPv4 and IPv6 traffic. It does not cause availability risks or bandwidth constraints on your network traffic.
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html

</details>

---

## Question 486: CLF-C02-ET-Q486
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can companies use to create infrastructure from code?

**Choices:**
- A) Amazon Elastic Kubernetes Service (Amazon EKS)
- B) AWS Outposts
- C) AWS CodePipeline
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS CloudFormation
Speed up cloud provisioning with infrastructure as code
How it works
AWS CloudFormation lets you model, provision, and manage AWS and third-party resources by treating infrastructure as code.
https://aws.amazon.com/cloudformation/
---
Selected Answer: D
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
---
Selected Answer: D
For AWS cloud development, the built-in choice for infrastructure as code is AWS CloudFormation.
https://www.freecodecamp.org/news/how-to-implement-infrastructure-as-code-with-aws/#:~:text=Infrastructure%20as%20code%20is%20the,as%20code%20is%20AWS%20CloudFormation.

</details>

---

## Question 487: CLF-C02-ET-Q487
**Domain 1:** Cloud Concepts  

**Question:**  
Which guideline is a well-architected design principle for building cloud applications?

**Choices:**
- A) Keep static data closer to compute resources.
- B) Provision resources for peak capacity.
- C) Design for automated recovery from failure.
- D) Use tightly coupled components.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html
---
Selected Answer: C
https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html#:~:text=Automatically%20recover%20from%20failure%3A

"c" is a reliability design principle as per above link.
---
Selected Answer: C
correct answer is C

</details>

---

## Question 488: CLF-C02-ET-Q488
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company needs to move 75 petabytes of data from its on-premises data centers to AWS.

Which AWS service should the company use to meet these requirements MOST cost-effectively?

**Choices:**
- A) AWS Snowball Edge Storage Optimized
- B) AWS Snowmobile
- C) AWS Direct Connect
- D) AWS Storage Gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: A
AWS Snowmobile is a data transfer service designed for moving massive amounts of data (up to 100PB) to AWS
---
Selected Answer: B
https://aws.amazon.com/snowmobile/
---
Selected Answer: B
https://aws.amazon.com/snowmobile/

</details>

---

## Question 489: CLF-C02-ET-Q489
**Domain 1:** Cloud Concepts  

**Question:**  
Which of the following are pillars of the AWS Well-Architected Framework? (Choose two.)

**Choices:**
- A) Resource scalability
- B) Performance efficiency
- C) System elasticity
- D) Agile development
- E) Operational excellence

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
AWS Well-Architected and the Six Pillars:
Operational Excellence Pillar
Security Pillar
Reliability Pillar
Performance Efficiency Pillar
Cost Optimization Pillar
Sustainability Pillar

AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads. Built around six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability—AWS Well-Architected provides a consistent approach for customers and partners to evaluate architectures and implement scalable designs.

https://aws.amazon.com/architecture/well-architected/
---
Selected Answer: BE
https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
---
Selected Answer: BE
BE is the correct answer

</details>

---

## Question 490: CLF-C02-ET-Q490
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to connect its on-premises data center to the AWS Cloud. The company needs a dedicated, low-latency connection with consistent network performance.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Global Accelerator
- B) Amazon CloudFront
- C) AWS Direct Connect
- D) AWS Managed VPN

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Direct Connect=low latency
---
Selected Answer: C
AWS Direct Connect
Create a dedicated network connection to AWS
How it works
The AWS Direct Connect cloud service is the shortest path to your AWS resources. While in transit, your network traffic remains on the AWS global network and never touches the public internet. This reduces the chance of hitting bottlenecks or unexpected increases in latency. When creating a new connection, you can choose a hosted connection provided by an AWS Direct Connect Delivery Partner, or choose a dedicated connection from AWS—and deploy at AWS Direct Connect locations around the globe. With AWS Direct Connect SiteLink, you can send data between AWS Direct Connect locations to create private network connections between the offices and data centers in your global network.
https://aws.amazon.com/directconnect/
---
Selected Answer: C
https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

</details>

---

## Question 491: CLF-C02-ET-Q491
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which design principles should a company apply to AWS Cloud workloads to maximize sustainability and minimize environmental impact? (Choose two.)

**Choices:**
- A) Maximize utilization of Amazon EC2 instances.
- B) Minimize utilization of Amazon EC2 instances.
- C) Minimize usage of managed services.
- D) Force frequent application reinstallations by users.
- E) Reduce the need for users to reinstall applications.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AE (100%). Contributor Answer: AE.

Community Rationale & Discussion:
the first time this website was right in 300 questions
---
Selected Answer: AE
https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/design-principles-for-sustainability-in-the-cloud.html
---
Selected Answer: AE
https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/design-principles-for-sustainability-in-the-cloud.html

</details>

---

## Question 492: CLF-C02-ET-Q492
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
In which ways does the AWS Cloud offer lower total cost of ownership (TCO) of computing resources than on-premises data centers? (Choose two.)

**Choices:**
- A) AWS replaces upfront capital expenditures with pay-as-you-go costs.
- B) AWS is designed for high availability, which eliminates user downtime.
- C) AWS eliminates the need for on-premises IT staff.
- D) AWS uses economies of scale to continually reduce prices.
- E) AWS offers a single pricing model for Amazon EC2 instances.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
https://aws.amazon.com/blogs/publicsector/tco-cost-optimization-best-practices-for-managing-usage/
---
Selected Answer: AD
A and D
---
Selected Answer: AD
https://aws.amazon.com/blogs/publicsector/tco-cost-optimization-best-practices-for-managing-usage/

https://onica.com/blog/migration/aws-total-cost-of-ownership/

</details>

---

## Question 493: CLF-C02-ET-Q493
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service or feature identifies whether an Amazon S3 bucket or an IAM role has been shared with an external entity?

**Choices:**
- A) AWS Service Catalog
- B) AWS Systems Manager
- C) AWS IAM Access Analyzer
- D) AWS Organizations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The answer is C.

IAM Access Analyzer helps identify resources in your organization and accounts that are shared with an external entity.
https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
---
Selected Answer: C
A. AWS Service Catalog: A service that allows organizations to create and manage catalogs of IT services that are approved for use on AWS.

B. AWS Systems Manager: A set of services that enables visibility and control of your infrastructure on AWS. 

C. AWS IAM Access Analyzer: A service that helps identify unintended resource access and resource sharing. It specifically identifies whether an Amazon S3 bucket or an IAM role has been shared with an external entity. It provides insights into resource access policies.

D. AWS Organizations: A service for consolidating multiple AWS accounts into an organization that you create and centrally manage.
---
Selected Answer: C
AWS IAM Access Analyzer helps identify and monitor access policies to determine whether an Amazon S3 bucket, IAM role, or other AWS resources have been shared with external entities (such as another AWS account, a public user, or an unknown third party).

</details>

---

## Question 494: CLF-C02-ET-Q494
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to deploy some of its resources in the AWS Cloud. To meet regulatory requirements, the data must remain local and on premises. There must be low latency between AWS and the company resources.

Which AWS service or feature can be used to meet these requirements?

**Choices:**
- A) AWS Local Zones
- B) Availability Zones
- C) AWS Outposts
- D) AWS Wavelength Zones

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience. Outposts solutions allow you to extend and run native AWS services on premises, and is available in a variety of form factors, from 1U and 2U Outposts servers to 42U Outposts racks, and multiple rack deployments.

With AWS Outposts, you can run some AWS services locally and connect to a broad range of services available in the local AWS Region. Run applications and workloads on premises using familiar AWS services, tools, and APIs. Outposts supports workloads and devices requiring low latency access to on-premises systems, local data processing, data residency, and application migration with local system interdependencies. 
https://aws.amazon.com/outposts/
---
Selected Answer: C
AWS Outposts
---
Selected Answer: C
https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html
https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html

Outposts are created on premise. Local zones are not on premise. Both provide low latency.

</details>

---

## Question 495: CLF-C02-ET-Q495
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following AWS services are serverless? (Choose two.)

**Choices:**
- A) AWS Outposts
- B) Amazon EC2
- C) Amazon Elastic Kubernetes Service (Amazon EKS)
- D) AWS Fargate
- E) AWS Lambda

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `DE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: DE (100%). Contributor Answer: DE.

Community Rationale & Discussion:
This time the page was right again!
---
Selected Answer: DE
https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
---
Selected Answer: DE
https://aws.amazon.com/fargate/
https://aws.amazon.com/lambda/

</details>

---

## Question 496: CLF-C02-ET-Q496
**Domain 3:** Cloud Technology and Services  

**Question:**  
When a user wants to utilize their existing per-socket, per-core, or per-virtual machine software licenses for a Microsoft Windows server running on AWS, which Amazon EC2 instance type is required?

**Choices:**
- A) Spot Instances
- B) Dedicated Instances
- C) Dedicated Hosts
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Dedicated Hosts provide comprehensive Bring Your Own License (BYOL) support. They allow you to use your existing per-socket, per-core, or per-VM software licenses, including Windows Server, SQL Server, SUSE Linux Enterprise Server, Red Hat Enterprise Linux, or other software licenses that are bound to VMs, sockets, or physical cores, subject to your license terms.
https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/dedicated-hosts-overview.html
---
Selected Answer: C
https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/dedicated-hosts-overview.html#:~:text=Dedicated%20Instances.-,Bring%20your%20own%20license,-Dedicated%20Hosts%20allow
---
Selected Answer: C
Dedicated Hosts allow you to use your existing per-socket, per-core, or per-VM software licenses
https://aws.amazon.com/ec2/dedicated-hosts/

</details>

---

## Question 497: CLF-C02-ET-Q497
**Domain 3:** Cloud Technology and Services  

**Question:**  
A solutions architect needs to maintain a fleet of Amazon EC2 instances so that any impaired instances are replaced with new ones.

Which AWS service should the solutions architect use?

**Choices:**
- A) Amazon Elastic Container Service (Amazon ECS)
- B) Amazon GuardDuty
- C) AWS Shield
- D) AWS Auto Scaling

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Answer is D. AWS Auto Scaling
---
Selected Answer: D
1. Improve fault tolerance through automatic detection and replacement of unhealthy instances. 
2. Increase availability with predictive or dynamic scaling policies with the right amount of compute capacity.
3. Optimize workload performance and cost by combining purchase options and instance types.
4. Reduce the complexity of configuration changes and application deployments with instance refresh.
https://aws.amazon.com/ec2/autoscaling/
---
Selected Answer: D
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#:~:text=If%20your%20instance%20is%20part%20of%20an%20Auto%20Scaling%20group%20with%20health%20checks%20enabled%2C%20then%20the%20instance%20is%20replaced%20when%20it%20becomes%20impaired.

</details>

---

## Question 498: CLF-C02-ET-Q498
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides on-premises applications with low-latency access to data that is stored in the AWS Cloud?

**Choices:**
- A) Amazon CloudFront
- B) AWS Storage Gateway
- C) AWS Backup
- D) AWS DataSync

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Storage Gateway gives your applications on-premises and in-cloud access to virtually unlimited cloud storage
---
Selected Answer: B
AWS Storage Gateway
Provide on-premises applications with access to virtually unlimited cloud storage
Storage Gateway types
AWS Storage Gateway gives your applications on-premises and in-cloud access to virtually unlimited cloud storage. You can deploy Storage Gateway as a virtual machine (VM) within your VMware, Hyper-V, or Linux KVM virtual environment, or as an Amazon EC2 instance within your Amazon Virtual Private Cloud (Amazon VPC).
https://aws.amazon.com/storagegateway/
---
Selected Answer: B
https://aws.amazon.com/storagegateway/faqs/
https://lifesciences-resources.awscloud.com/aws-storage-blog/cloud-storage-in-minutes-with-aws-storage-gateway-updated

</details>

---

## Question 499: CLF-C02-ET-Q499
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to deploy containers on AWS. The company wants full control of the compute resources that host the containers. Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Elastic Kubernetes Service (Amazon EKS)
- B) AWS Fargate
- C) Amazon EC2
- D) Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `79%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (79%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon EC2

Amazon EC2 (Elastic Compute Cloud) provides resizable compute capacity and allows you to have full control over the underlying infrastructure. With EC2, you can launch instances and deploy containers on them using container orchestration tools like Docker or Kubernetes while retaining control over the configuration, scaling, and management of the underlying virtual servers. This option provides the flexibility and control needed for managing compute resources directly.
---
Selected Answer: C
Company wants full control of the compute resources that host the containers - it`s an answer
---
Selected Answer: C
For full control over your compute environment, choose to run your containers on Amazon Elastic Compute Cloud (EC2). For container orchestrators, you can choose either Amazon Elastic Container Service (ECS) or Amazon Elastic Kubernetes Service (EKS).

</details>

---

## Question 500: CLF-C02-ET-Q500
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature allows users to create new AWS accounts, group multiple accounts to organize workflows, and apply policies to groups of accounts?

**Choices:**
- A) AWS Identity and Access Management (IAM)
- B) AWS Trusted Advisor
- C) AWS CloudFormation
- D) AWS Organizations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `83%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (83%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Using AWS Organizations, you can programmatically create new AWS accounts and allocate resources, group accounts to organize your workflows, apply policies to accounts or groups for governance, and simplify billing by using a single payment method for all of your accounts.
---
Selected Answer: D
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
AWS Organizations
---
Selected Answer: D
D. AWS Organizations
AWS Organizations helps you centrally govern your environment as you scale your workloads on AWS. Whether you are a growing startup or a large enterprise, Organizations helps you to programmatically create new accounts and allocate resources, simplify billing by setting up a single payment method for all of your accounts, create groups of accounts to organize your workflows, and apply policies to these groups for governance. In addition, AWS Organizations is integrated with other AWS services so you can define central configurations, security mechanisms, and resource sharing across accounts in your organization.

</details>

---

## Question 501: CLF-C02-ET-Q501
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to store and retrieve files in Amazon S3 for its existing on-premises applications by using industry-standard file system protocols.
Which AWS service will meet these requirements?

**Choices:**
- A) AWS DataSync
- B) AWS Snowball Edge
- C) Amazon S3 File Gateway
- D) AWS Transfer Family

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `82%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (82%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. AWS DataSync: is a service for transferring large amounts of data between on-premises storage and Amazon S3, but it is designed for data movement, not for providing real-time file system access
B. AWS Snowball Edge: Device that provids large volumes or edge computing offline data transfer capabilities. Not for access to S3
C. Amazon S3 File Gateway: Allows storing and retrieving files in Amazon S3 using industry-standard file protocols. It acts as a bridge between your on-premesis file-based applications and Amazon S3 object storage
D. AWS Transfer Family: Fully managed support for SFTP, FTPS and FTP. provides fully managed support for file transfers directly into and out of Amazon S3 or Amazon EFS. Supports file transfer protocols, not file system protocols
---
Selected Answer: C
The Amazon S3 File Gateway enables you to store and retrieve objects in Amazon Simple Storage Service (S3) using file protocols such as Network File System (NFS) and Server Message Block (SMB). Objects written through S3 File Gateway can be directly accessed in S3.
---
Selected Answer: C
C. Amazon S3 File Gateway
A S3 File Gateway simplifies file storage in Amazon S3, integrates to existing applications through industry-standard file system protocols, and provides a cost-effective alternative to on-premises storage. It also provides low-latency access to data through transparent local caching. A S3 File Gateway manages data transfer to and from AWS, buffers applications from network congestion, optimizes and streams data in parallel, and manages bandwidth consumption.
https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html

</details>

---

## Question 502: CLF-C02-ET-Q502
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to block SQL injection attacks.
Which AWS service or feature should the company use to meet this requirement?

**Choices:**
- A) AWS WAF
- B) Network ACLs
- C) Security groups
- D) AWS Certificate Manager (ACM)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
SQL ATTACKS- AWS WAF
DDOS- AWS SHEILD
---
Selected Answer: A
A. AWS WAF: web application firewall that allows users to create custom rules to filter and monitor HTTP or HTTPS requests to a web application. It helps protect against common web exploits, including SQL injection attacks
B. Network ACLs: Are used to control traffic at the subnet level. 
C. Security groups: Control inbound and outbound traffic at the network level
D. AWS Certificate Manager (ACM): Manages SSL/TLS certificates or encrypting data in transit.
---
Selected Answer: A
AWS WAF helps protects your website from common attack techniques like SQL injection and Cross-Site Scripting (XSS). In addition, you can create rules that can block or rate-limit traffic from specific user-agents, from specific IP addresses, or that contain particular request headers.

</details>

---

## Question 503: CLF-C02-ET-Q503
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a unified tool to provide a consistent method to interact with AWS services.
Which AWS service or tool will meet this requirement?

**Choices:**
- A) AWS CLI
- B) Amazon Elastic Container Service (Amazon ECS)
- C) AWS Cloud9
- D) AWS Virtual Private Network (AWS VPN)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
"The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts."

Reference: https://aws.amazon.com/cli/
---
Selected Answer: A
A. AWS CLI: tool that provides a way to interact multiple AWS services from the command line.
B. Amazon ECS: A container orchestration service. It manages containerized applications, not for interacting with AWS services
C. AWS Cloud9: A cloud IDE
D. AWS VPN: used to securely connect on-premises networks to AWS, not to interact with or manage AWS services.
---
Selected Answer: A
A. The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts."

</details>

---

## Question 504: CLF-C02-ET-Q504
**Domain 3:** Cloud Technology and Services  

**Question:**  
What does Amazon CloudFront provide?

**Choices:**
- A) Automatic scaling for all resources to power an application from a single unified interface
- B) Secure delivery of data, videos, applications, and APIs to users globally with low latency
- C) Ability to directly manage traffic globally through a variety of routing types, including latency-based routing, geo DNS, geoproximity, and weighted round robin
- D) Automatic distribution of incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and AWS Lambda functions

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon CloudFront
Securely deliver content with low latency and high transfer speeds
How it works
Amazon CloudFront is a content delivery network (CDN) service built for high performance, security, and developer convenience.
https://aws.amazon.com/cloudfront/
---
Selected Answer: B
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
---
Selected Answer: B
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

</details>

---

## Question 505: CLF-C02-ET-Q505
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service supports the deployment and management of applications in the AWS Cloud?

**Choices:**
- A) Amazon CodeGuru
- B) AWS Fargate
- C) AWS CodeCommit
- D) AWS Elastic Beanstalk

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Elastic Beanstalk
---
Selected Answer: D
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
---
Selected Answer: D
AWS Elastic Beanstalk helps you deploy and manage web applications with capacity provisioning, app health monitoring, and more.
https://aws.amazon.com/elasticbeanstalk/

</details>

---

## Question 506: CLF-C02-ET-Q506
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to integrate natural language processing (NLP) into business intelligence (BI) dashboards. The company wants to ask questions and receive answers with relevant visualizations.

Which AWS service or tool will meet these requirements?

**Choices:**
- A) Amazon Macie
- B) Amazon Rekognition
- C) Amazon QuickSight Q
- D) Amazon Lex

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon QuickSight :Serverless machine learning powered business intelligence service to create interactive dashboards
---
Selected Answer: C
https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-get-started.html
---
Selected Answer: C
https://docs.aws.amazon.com/quicksight/latest/user/working-with-quicksight-q.html

</details>

---

## Question 507: CLF-C02-ET-Q507
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which Amazon S3 feature or storage class uses the AWS backbone network and edge locations to reduce latencies from the end user to Amazon S3?

**Choices:**
- A) S3 Cross-Region Replication
- B) S3 Transfer Acceleration
- C) S3 Event Notifications
- D) S3 Standard-Infrequent Access (S3 Standard-IA)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon S3 Transfer Acceleration can Speed up content transfers to and from Amazon S3
---
Selected Answer: B
Amazon S3 Transfer Acceleration can speed up content transfers to and from Amazon S3 by as much as 50-500% for long-distance transfer of larger objects. 
S3TA improves transfer performance by routing traffic through Amazon CloudFront’s globally distributed Edge Locations and over AWS backbone networks, and by using network protocol optimizations. You can turn on S3TA with a few clicks in the S3 console, and test its benefits from your location with a speed comparison tool. With S3TA, you pay only for transfers that are accelerated.
https://aws.amazon.com/s3/transfer-acceleration/
---
Selected Answer: B
https://aws.amazon.com/s3/transfer-acceleration/

</details>

---

## Question 508: CLF-C02-ET-Q508
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides the ability to host a NoSQL database in the AWS Cloud?

**Choices:**
- A) Amazon Aurora
- B) Amazon DynamoDB
- C) Amazon RDS
- D) Amazon Redshift

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon DynamoDB
Serverless, NoSQL, fully managed database with single-digit millisecond performance at any scale
https://aws.amazon.com/dynamodb/
---
Selected Answer: B
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
---
Selected Answer: B
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

</details>

---

## Question 509: CLF-C02-ET-Q509
**Domain 2:** Security and Compliance  

**Question:**  
A cloud practitioner needs to obtain AWS compliance reports before migrating an environment to the AWS Cloud.
How can these reports be generated?

**Choices:**
- A) Contact the AWS Compliance team.
- B) Download the reports from AWS Artifact.
- C) Open a case with AWS Support.
- D) Generate the reports with Amazon Macie.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Artifact is a portal that provides access to various compliance reports, including certifications, attestations, and other relevant documents. You can download these reports directly from AWS Artifact.
---
Selected Answer: B
A. Contact the AWS Compliance team: While it is possible to contact the AWS Compliance team for specific compliance-related inquiries, obtaining standard compliance reports is typically done through self-service options like AWS Artifact. Direct contact may be needed for specific or customized compliance needs.

B. Download the reports from AWS Artifact: A self-service portal that provides on-demand access to AWS compliance reports. Users can download documentation on various compliance programs and certifications, making it a convenient way to obtain compliance reports.

C. Open a case with AWS Support: While AWS Support can assist with various inquiries, opening a case may not be the most efficient way to obtain standard compliance reports. 

D. Generate the reports with Amazon Macie: A service focused on discovering, classifying, and protecting sensitive data.
---
Selected Answer: B
WS Artifact is the centralized compliance portal where AWS customers can access and download AWS compliance reports, certifications, and audit documents. It provides reports related to security, compliance, and regulatory standards such as ISO, SOC, and PCI DSS.

</details>

---

## Question 510: CLF-C02-ET-Q510
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is a relational database compatible with MySQL and PostgreSQL?

**Choices:**
- A) Amazon Redshift
- B) Amazon DynamoDB
- C) Amazon Aurora
- D) Amazon Neptune

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Aurora provides unparalleled high-performance and availability at global scale with full MySQL and PostgreSQL compatibility, at 1/10th the cost of commercial databases. Aurora has 5x the throughput of MySQL and 3x of PostgreSQL. Aurora has broad compliance standards and best-in-class security capabilities. Aurora offers storage resiliency by making data durable across 3 AZs (customers only pay for 1 copy). Aurora has up to 99.99% availability, and customers can access local read performance with Global Database when deployed across AWS Regions. With serverless, Aurora can scale-up to hundreds of thousands of transactions in a fraction of a second. Aurora zero-ETL integration with Amazon Redshift delivers analytics on transactional data in near real-time.

https://aws.amazon.com/rds/aurora/
---
Selected Answer: C
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
---
Selected Answer: C
REDSHIFT IS A DATAWAREHOUSE

</details>

---

## Question 511: CLF-C02-ET-Q511
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which architecture design principle describes the need to isolate failures between dependent components in the AWS Cloud?

**Choices:**
- A) Use a monolithic design.
- B) Design for automation.
- C) Design for single points of failure.
- D) Loosely couple components.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Dependencies such as queuing systems, streaming systems, workflows, and load balancers are loosely coupled. Loose coupling helps isolate behavior of a component from other components that depend on it, increasing resiliency and agility.

https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.html
---
Selected Answer: D
Loosely couple components (microservices) are conceptually small pieces of "monolithic" application created/implemented to isolate failures between dependent components in the AWS Cloud
---
Selected Answer: D
https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html

</details>

---

## Question 512: CLF-C02-ET-Q512
**Domain 1:** Cloud Concepts  

**Question:**  
Which benefit of cloud computing gives a company the ability to deploy applications to users all over the world through a network of AWS Regions, Availability Zones, and edge locations?

**Choices:**
- A) Economy of scale
- B) Global reach
- C) Agility
- D) High availability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Six advantages of cloud computing
Go global in minutes – Easily deploy your application in multiple regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at minimal cost.
https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html
---
Selected Answer: B
don't worry the answer must be B
---
Selected Answer: B
https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html

Go Global in minutes = Global Reach

</details>

---

## Question 513: CLF-C02-ET-Q513
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service makes it easier to monitor and troubleshoot application logs and cloud resources?

**Choices:**
- A) Amazon EC2
- B) AWS Identity and Access Management (IAM)
- C) Amazon CloudWatch
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon CloudWatch helps you analyze logs and, in real time, monitor the metrics of your AWS resources and hosted applications. You can also use the ServiceLens feature to monitor the health of your application or use the Synthetics feature to create canaries that monitor your endpoints and APIs. For more information about using this service to monitor your application, see CloudWatch in this guide.

AWS CloudTrail helps you audit the governance, compliance, and operational risk of your AWS account by recording the actions taken by a user, role, or an AWS service. For more information about using this service to log or monitor events for your application, see CloudTrail in this guide.

https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html
---
Selected Answer: C
https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html
---
Selected Answer: C
https://aws.amazon.com/cloudwatch/features/#:~:text=CloudWatch%20enables%20you%20to%20monitor,building%20applications%20and%20business%20value.

</details>

---

## Question 514: CLF-C02-ET-Q514
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which AWS service uses AWS Compute Optimizer to provide sizing recommendations based on workload metrics?

**Choices:**
- A) Amazon EC2
- B) Amazon RDS
- C) Amazon Lightsail
- D) AWS Step Functions

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Compute Optimizer helps avoid overprovisioning and underprovisioning four types of AWS resources—Amazon Elastic Compute Cloud (EC2) instance types, Amazon Elastic Block Store (EBS) volumes, Amazon Elastic Container Service (ECS) services on AWS Fargate, and AWS Lambda functions—based on your utilization data.

https://aws.amazon.com/compute-optimizer/
---
Answer: A
https://aws.amazon.com/compute-optimizer/
---
Selected Answer: A
https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html#:~:text=Compute%20Optimizer%20generates%20recommendations%20for%20the%20following%20resources%3A

</details>

---

## Question 515: CLF-C02-ET-Q515
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service will help a company plan a migration to AWS by collecting the configuration, usage, and behavior data of on-premises data centers?

**Choices:**
- A) AWS Resource Groups
- B) AWS Application Discovery Service
- C) AWS Service Catalog
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Application Discovery Service helps you plan your migration to the AWS cloud by collecting usage and configuration data about your on-premises servers and databases.

https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html
---
Selected Answer: B
AWS Application Discovery Service

https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html
---
Selected Answer: B
AWS Application Discovery Service helps you plan cloud migration projects by gathering information about your on-premises data centers.

https://aws.amazon.com/application-discovery/

</details>

---

## Question 516: CLF-C02-ET-Q516
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service uses a combination of publishers and subscribers?

**Choices:**
- A) AWS Lambda
- B) Amazon Simple Notification Service (Amazon SNS)
- C) Amazon CloudWatch
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Pub/sub messaging
Amazon Simple Notification Service (SNS) makes it easy for you to build an application using the pub/sub messaging model. You can send messages from your applications to customers or other applications in a scalable and cost-efficient manner.
https://aws.amazon.com/what-is/pub-sub-messaging/#:~:text=to%20connected%20clients-,Pub/sub%20messaging,-Amazon%20Simple%20Notification
---
Selected Answer: B
https://docs.aws.amazon.com/sns/latest/dg/welcome.html
---
Selected Answer: B
https://aws.amazon.com/what-is/pub-sub-messaging/

</details>

---

## Question 517: CLF-C02-ET-Q517
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is in the early stages of planning a migration to AWS. The company wants to obtain the monthly predicted total AWS cost of ownership for future Amazon EC2 instances and associated storage.

Which AWS service or tool should the company use to meet these requirements?

**Choices:**
- A) AWS Pricing Calculator
- B) AWS Compute Optimizer
- C) AWS Trusted Advisor
- D) AWS Application Migration Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Pricing Calculator lets you explore AWS services and create an
estimate for the cost of your use
solution architecture on AWS.
---
Selected Answer: A
it says "in the early stages of planning a migration to AWS", then it must be A. If it was after migration it could be B to rightsize based on the AWS usage history.
---
Selected Answer: A
https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html

</details>

---

## Question 518: CLF-C02-ET-Q518
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool will monitor AWS resources and applications in real time?

**Choices:**
- A) AWS Trusted Advisor
- B) Amazon CloudWatch
- C) AWS CloudTrail
- D) AWS Cost Explorer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon CloudWatch Logs
• CloudWatch Logs can collect log from:
• Elastic Beanstalk: collection of logs from application
• ECS: collection from containers
• AWS Lambda: collection from function logs
• CloudTrail based on filter
• CloudWatch log agents: on EC2 machines or on-premises servers
• Route53: Log DNS queries
• Enables real-time monitoring of logs
---
B. Amazon CloudWatch
---
Selected Answer: B
B is correct.

</details>

---

## Question 519: CLF-C02-ET-Q519
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud Adoption Framework (AWS CAF) capability belongs to the business perspective?

**Choices:**
- A) Program and project management
- B) Data science
- C) Observability
- D) Change and release management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (90%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. Program and project management : Governance perspective
B. Data science : Business perspective
---
Selected Answer: B
Data science – Leverage experimentation, advanced analytics, and machine learning to solve complex business problems. Predictive and prescriptive analytics can help you complete your data monetization strategy by enabling you to improve operational effectiveness and decision-making as well as customer and employee experience.
---
Selected Answer: B
A. Program and project management : Governance perspective
B. Data science : Business perspective

</details>

---

## Question 520: CLF-C02-ET-Q520
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
An ecommerce company has migrated its IT infrastructure from an on-premises data center to the AWS Cloud.
Which cost is the company’s direct responsibility?

**Choices:**
- A) Cost of application software licenses
- B) Cost of the hardware infrastructure on AWS
- C) Cost of power for the AWS servers
- D) Cost of physical security for the AWS data center

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Under the AWS Shared Responsibility Model, AWS manages the hardware, physical security, and infrastructure costs, while customers are responsible for managing their applications, data, and configurations.
---
Selected Answer: A
A. Cost of application software licenses
---
Selected Answer: A
A. Cost of application software licenses

</details>

---

## Question 521: CLF-C02-ET-Q521
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS resource can help a company reduce its costs in exchange for a usage commitment when using Amazon EC2 instances?

**Choices:**
- A) Compute Savings Plans
- B) Auto Scaling group
- C) On-Demand Instance
- D) EC2 instance store

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. Compute Savings
 PlansCompute Savings Plans allow a company to reduce its costs in exchange for a usage commitment over a one- or three-year term. This plan provides the most flexibility and significant savings on Amazon EC2 instances, regardless of instance family, size, operating system, or region.
---
Selected Answer: A
A is correct.
https://aws.amazon.com/savingsplans/faq/

</details>

---

## Question 522: CLF-C02-ET-Q522
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which perspective in the AWS Cloud Adoption Framework (AWS CAF) includes a capability for well-designed data and analytics architecture?

**Choices:**
- A) Security
- B) Governance
- C) Operations
- D) Platform

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
I think architecture is the keyword. Then ,platform is the answer.
---
Selected Answer: D
The keyword "architecture", answer is D
---
Selected Answer: D
D is correct.
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html

</details>

---

## Question 523: CLF-C02-ET-Q523
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which options are AWS Cloud Adoption Framework (AWS CAF) people perspective capabilities? (Choose two.)

**Choices:**
- A) Organizational alignment
- B) Portfolio management
- C) Organization design
- D) Risk management
- E) Modern application development

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
AC correct answers
---
Selected Answer: AC
A and C are correct.
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html

</details>

---

## Question 524: CLF-C02-ET-Q524
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs a bridge between technology and business to help evolve to a culture of continuous growth and learning.

Which perspective in the AWS Cloud Adoption Framework (AWS CAF) serves as this bridge?

**Choices:**
- A) People
- B) Governance
- C) Operations
- D) Security

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
People Perspective serves as a bridge between technology and
business, accelerating the cloud journey to help organizations more
rapidly evolve to a culture of continuous growth, learning, and where
change becomes business-as-normal, with focus on culture,
organizational structure, leadership, and workforce.
---
Selected Answer: A
People perspective - Culture Evolution
---
A is correct.
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html

</details>

---

## Question 525: CLF-C02-ET-Q525
**Domain 2:** Security and Compliance  

**Question:**  
Which option is a responsibility of AWS under the AWS shared responsibility model?

**Choices:**
- A) Application data security
- B) Patch management for applications that run on Amazon EC2 instances
- C) Patch management of the underlying infrastructure for managed services
- D) Application identity and access management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C is correct
---
C is correct.

</details>

---

## Question 526: CLF-C02-ET-Q526
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service or resource can identify and provide reports on IAM resources in one AWS account that is shared with another AWS account?

**Choices:**
- A) IAM credential report
- B) AWS IAM Identity Center (AWS Single Sign-On)
- C) AWS Identity and Access Management Access Analyzer
- D) Amazon Cognito user pool

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C is correct 
AWS IAM Access Analyzer
Here's the resource URL:
https://aws.amazon.com/iam/access-analyzer/
---
Selected Answer: C
C. AWS Identity and Access Management Access Analyzer - It helps identify and analyze resource access policies including those shared with other AWS accounts.

IAM Credential report gives information about user credentials in an AWS account but it does not do cross account sharing.

</details>

---

## Question 527: CLF-C02-ET-Q527
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS Well-Architected Framework pillar focuses on structured and streamlined allocation of computing resources?

**Choices:**
- A) Reliability
- B) Operational excellence
- C) Performance efficiency
- D) Sustainability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C is correct.
https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc
---
C. Performance efficiency

The Performance Efficiency pillar of the AWS Well-Architected Framework focuses on the efficient use of computing resources to meet requirements and the maintenance of that efficiency as demand changes and technologies evolve.

</details>

---

## Question 528: CLF-C02-ET-Q528
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud Adoption Framework (AWS CAF) capabilities belong to the governance perspective? (Choose two.)

**Choices:**
- A) Program and project management
- B) Product management
- C) Portfolio management
- D) Risk management
- E) Event management

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
The correct answers are:

A. Program and project management D. Risk management

These two capabilities fall under the Governance perspective of the AWS Cloud Adoption Framework (AWS CAF), which focuses on ensuring business governance and controls, including managing risks and ensuring compliance.
---
A and D are correct 
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html
---
Selected Answer: AD
A and D are correct.
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html

</details>

---

## Question 529: CLF-C02-ET-Q529
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use AWS Managed Services (AMS) for operational support and wants to understand the scope of AMS.

Which AMS feature will meet these requirements?

**Choices:**
- A) Landing zone and network management
- B) Customer application development
- C) DevSecOps pipeline configuration
- D) Application log monitoring

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (80%). Contributor Answer: A.

Community Rationale & Discussion:
D. Application log monitoring
---
Selected Answer: A
A. Landing zone and network management

AWS Managed Services (AMS) offers landing zone and network management as part of its scope to assist companies in setting up and managing their AWS environment. This includes establishing a secure and well-architected foundation for workloads, setting up network connectivity, managing accounts and users, implementing security controls, and ensuring compliance with best practices and regulatory requirements.
---
Selected Answer: D
AWS Managed Services (AMS) provides operational support for AWS infrastructure and services. This includes managing and monitoring application logs to ensure they are available, secure, and compliant with the company's requirements. Landing zone and network management, customer application development, and DevSecOps pipeline configuration are not typically part of the AMS scope.

</details>

---

## Question 530: CLF-C02-ET-Q530
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its on-premises NoSQL workload to Amazon DynamoDB.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Migration Hub
- B) AWS Database Migration Service (AWS DMS)
- C) Migration Evaluator
- D) AWS Application Migration Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Database Migration Service (AWS DMS)

AWS DMS helps to migrate databases to AWS quickly and securely. It supports various source and target databases, including NoSQL databases like MongoDB, Cassandra, and Couchbase, making it suitable for migrating an on-premises NoSQL workload to Amazon DynamoDB.
---
Given answer is correct

</details>

---

## Question 531: CLF-C02-ET-Q531
**Domain 2:** Security and Compliance  

**Question:**  
A company is setting up AWS Identity and Access Management (IAM) on an AWS account.
Which recommendation complies with IAM security best practices?

**Choices:**
- A) Use the account root user access keys for administrative tasks.
- B) Grant broad permissions so that all company employees can access the resources they need.
- C) Turn on multi-factor authentication (MFA) for added security during the login process.
- D) Avoid rotating credentials to prevent issues in production applications.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Use the account root user access keys for administrative tasks: It is not recommended to use the root user's access keys for day-to-day administrative tasks. The root user has unrestricted access, and using its access keys poses security risks. 

B. Grant broad permissions so that all company employees can access the resources they need: It's advisable to follow the principle of least privilege, granting users only the permissions they need to perform their tasks. 

C. Turn on multi-factor authentication (MFA) for added security during the login process: Enabling multi-factor authentication (MFA) is a security best practice. It adds an extra layer of protection by requiring users to provide a second form of authentication in addition to their password. This helps prevent unauthorized access even if credentials are compromised.

D. Avoid rotating credentials to prevent issues in production applications: Regularly rotating credentials, such as access keys and passwords, enhances security by reducing the window of opportunity for attackers.
---
Selected Answer: C
nabling Multi-Factor Authentication (MFA) is a key IAM security best practice because it adds an extra layer of security by requiring a second form of authentication (such as a one-time code from an authenticator app or a hardware token) in addition to a password.
---
Selected Answer: C
C. Turn on multi-factor authentication (MFA) for added security during the login process.

</details>

---

## Question 532: CLF-C02-ET-Q532
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is in the process of finding correct Amazon EC2 instance types and sizes to meet its performance and capacity requirements. The company wants to find the lowest possible cost.

Which option accurately characterizes the company's actions?

**Choices:**
- A) Auto Scaling
- B) Storage tiering
- C) Rightsizing
- D) Instance scheduling

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Rightsizing

Rightsizing involves finding the most suitable instance types and sizes to match performance and capacity requirements while optimizing costs. This process ensures that resources are neither underutilized nor over-provisioned, helping to minimize expenses while meeting workload demands.
---
Answer is correct

</details>

---

## Question 533: CLF-C02-ET-Q533
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to manage sign-in security for workforce users. The company needs to create workforce users and centrally manage their access across all the company's AWS accounts and applications.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Audit Manager
- B) Amazon Cognito
- C) AWS Security Hub
- D) AWS IAM Identity Center (AWS Single Sign-On)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (90%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS IAM Identity Center (AWS Single Sign-On)
---
would someone help with 392? much appreciation.
---
Selected Answer: D
Cognito = User authentication for Apps
IAM Identity Center = Centralized access management for AWS and Apps
The answer is D) AWS IAM Identity Center

</details>

---

## Question 534: CLF-C02-ET-Q534
**Domain 2:** Security and Compliance  

**Question:**  
A company wants a report that lists the status of multi-factor authentication (MFA) devices that all users in the company's AWS account use.

Which AWS feature or service will meet this requirement?

**Choices:**
- A) AWS Cost and Usage Reports
- B) IAM credential reports
- C) Detailed Billing Reports -
D AWS Cost Explorer reports

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The correct AWS feature or service that meets the requirement of generating a report listing the status of MFA devices for all users in an AWS account is B. IAM credential reports.

</details>

---

## Question 535: CLF-C02-ET-Q535
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to use machine learning capabilities to analyze log data from its Amazon EC2 instances and efficiently conduct security investigations.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Inspector
- B) Amazon QuickSight
- C) Amazon Detective -
D Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Detective is the best service for conducting security investigations using machine learning to analyze log data from Amazon EC2 instances and other AWS resources.
---
Selected Answer: C
Amazon Detective:
1.Investigate and quickly identify the root cause of potential security issues.
2.Automatically collect log data from your AWS resources and uses machine learning to help you visualize and conduct security investigations.
---
Selected Answer: C
Amazon Detective: 
1.Investigate and quickly identify the root cause of potential security issues.
2.Automatically collect log data from your AWS resources and
uses machine learning to help you visualize and
conduct security investigations.

</details>

---

## Question 536: CLF-C02-ET-Q536
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is launching a mobile app in the AWS Cloud. The company wants the app's users to sign in through social media identity providers (IdPs).

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Lambda
- B) Amazon Cognito
- C) AWS Secrets Manager
- D) Amazon CloudFront

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Cognito.

Amazon Cognito is a fully managed identity service that allows you to easily add user sign-up and sign-in to your mobile and web applications. It supports social identity providers (IdPs) such as Facebook, Google, Amazon, and others, allowing users to sign in using their existing social media accounts.
---
Selected Answer: B
B. Amazon Cognito

Amazon Cognito provides authentication, authorization, and user management for web and mobile apps. Users can sign in directly with a user name and password, or through third-party identity providers such as Facebook, Google, and Amazon, as well as through enterprise identity providers via SAML 2.0. Amazon Cognito facilitates the integration of social media identity providers (IdPs), making it a suitable choice for the company's mobile app to allow users to sign in through social media.

</details>

---

## Question 537: CLF-C02-ET-Q537
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which complimentary AWS service or tool creates data-driven business cases for cloud planning?

**Choices:**
- A) Migration Evaluator
- B) AWS Billing Conductor
- C) AWS Billing Console
- D) Amazon Forecast

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Correct
---
A its correct answer The complimentary AWS service that helps create data-driven business cases for cloud planning is AWS Migration Evaluator, formerly known as TSO Logic. AWS Migration Evaluator assists organizations in understanding the cost-benefits of moving to AWS by analyzing their current on-premises IT infrastructure usage and costs. It provides detailed reports and insights, enabling decision-makers to build compelling, data-driven business cases for cloud migration and planning. This tool helps in identifying the most cost-effective AWS services to meet an organization's specific needs, estimating the potential cost savings, and planning the migration strategy effectively.

</details>

---

## Question 538: CLF-C02-ET-Q538
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which cloud concept is demonstrated by using AWS Cost Explorer?

**Choices:**
- A) Rightsizing
- B) Reliability
- C) Resilience
- D) Modernization

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Rightsizing.

One of the key features of AWS Cost Explorer is rightsizing recommendations, which help users identify opportunities to optimize the cost and performance of their AWS resources by matching resource specifications to actual usage requirements.
---
A. Rightsizing

AWS Cost Explorer is a tool that enables you to visualize, understand, and manage your AWS costs and usage over time. This aligns with the concept of rightsizing, which involves optimizing the allocation of cloud resources based on usage and cost. By using AWS Cost Explorer, you can identify underutilized resources and make informed decisions about adjusting resource allocation to reduce costs, which is a key aspect of rightsizing.

</details>

---

## Question 539: CLF-C02-ET-Q539
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to deploy a non-containerized Java-based web application on AWS. The company wants to use a managed service to quickly deploy the application. The company wants the service to automatically provision capacity, load balance, scale, and monitor application health.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Elastic Container Service (Amazon ECS)
- B) AWS Lambda
- C) Amazon Elastic Kubernetes Service (Amazon EKS)
- D) AWS Elastic Beanstalk

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Elastic Beanstalk
---
Selected Answer: D
D. AWS Elastic Beanstalk

AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. You simply upload your code, and AWS Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, and auto-scaling to application health monitoring. It is ideal for non-containerized Java-based web applications, as it abstracts the underlying infrastructure, allowing developers to focus on writing code rather than managing environments

</details>

---

## Question 540: CLF-C02-ET-Q540
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool gives users the ability to connect with AWS and deploy resources programmatically?

**Choices:**
- A) Amazon QuickSight
- B) AWS PrivateLink
- C) AWS Direct Connect
- D) AWS SDKs

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
key word: programmatically*
---
Selected Answer: D
D. AWS SDKs
---
Selected Answer: D
D. AWS SDKs (Software Development Kits)

AWS SDKs provide a set of tools for developers to integrate with and manage AWS services programmatically. These SDKs support multiple programming languages, including Java, Python, .NET, Node.js, PHP, Ruby, and Go, among others, enabling developers to use the language they are most comfortable with to interact with AWS services. Through these SDKs, developers can create, configure, and manage AWS resources directly from their applications.

</details>

---

## Question 541: CLF-C02-ET-Q541
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has deployed a web application to Amazon EC2 instances. The EC2 instances have low usage.

Which AWS service or feature should the company use to rightsize the EC2 instances?

**Choices:**
- A) AWS Config
- B) AWS Cost Anomaly Detection
- C) AWS Budgets
- D) AWS Compute Optimizer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Optimize Amazon EC2 and Amazon RDS instances with customizable rightsizing recommendations tailored to your workload requirements
---
Selected Answer: D
AWS Compute Optimizer enables the efficient usage of AWS compute resources for your workloads.
---
Selected Answer: D
D. AWS Compute Optimizer

</details>

---

## Question 542: CLF-C02-ET-Q542
**Domain 3:** Cloud Technology and Services  

**Question:**  
According to security best practices, how should an Amazon EC2 instance be given access to an Amazon S3 bucket?

**Choices:**
- A) Hard code an IAM user’s secret key and access key directly in the application, and upload the file.
- B) Store the IAM user’s secret key and access key in a text file on the EC2 instance, read the keys, then upload the file.
- C) Have the EC2 instance assume a role to obtain the privileges to upload the file.
- D) Modify the S3 bucket policy so that any service can upload to it at any time.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `89%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (89%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The recommended security best practice for giving an Amazon EC2 instance access to an Amazon S3 bucket is option C: Have the EC2 instance assume a role to obtain the privileges to upload the file. This involves using AWS Identity and Access Management (IAM) roles to grant temporary permissions to the EC2 instance, rather than hard-coding or storing access keys directly in the application or on the instance.

This approach enhances security by minimizing the exposure of long-term credentials and following the principle of least privilege. The EC2 instance assumes a role with specific permissions to interact with the S3 bucket, and AWS automatically rotates temporary credentials for the instance.

Options A and B involve storing IAM user's secret keys on the EC2 instance, which is not recommended due to security risks. Option D, modifying the S3 bucket policy to allow any service to upload to it at any time, is also not recommended as it may lead to security vulnerabilities and compromises the principle of least privilege.
---
Selected Answer: C
AWS Services always assumes roles to gain access to other aws services.
---
Selected Answer: C
c option is valid

</details>

---

## Question 543: CLF-C02-ET-Q543
**Domain 1:** Cloud Concepts  

**Question:**  
Elasticity in the AWS Cloud refers to which of the following? (Choose two.)

**Choices:**
- A) How quickly an Amazon EC2 instance can be restarted
- B) The ability to rightsize resources as demand shifts
- C) The maximum amount of RAM an Amazon EC2 instance can use
- D) The pay-as-you-go billing model
- E) How easily resources can be procured when they are needed

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (94%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
Elasticity is the ability to add and release resources as business needs change. It has nothing to do with pricing.
---
Selected Answer: BE
A. How quickly an Amazon EC2 instance can be restarted: Not directly related to elasticity. Elasticity is more about adjusting resources based on demand rather than the speed of restarting instances.

B. The ability to rightsize resources as demand shifts: Elasticity involves the ability to dynamically adjust the size of resources (e.g., adding or removing instances) based on changing demand.

C. The maximum amount of RAM an Amazon EC2 instance can use: Not directly related to elasticity. Elasticity is more about the ability to scale resources horizontally or vertically, not the specific resource limits.

D. The pay-as-you-go billing model: Pay-as-you-go is related to the pricing model rather than elasticity. 

E. How easily resources can be procured when they are needed: Elasticity involves the ease with which resources can be provisioned or de-provisioned based on changing demand, providing flexibility and scalability.
---
Selected Answer: BE
Elasticity in the AWS Cloud refers to the ability to scale resources up or down dynamically based on demand. This helps optimize cost and performance by ensuring the right amount of resources are available when needed.

</details>

---

## Question 544: CLF-C02-ET-Q544
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to define a central data protection policy that works across AWS services for compute, storage, and database resources.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Batch
- B) AWS Elastic Disaster Recovery
- C) AWS Backup
- D) Amazon FSx

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
backup
---
Selected Answer: C
AWS Backup
• Fully-managed service to centrally manage and automate backups across
AWS services
• On-demand and scheduled backups
• Supports PITR (Point-in-time Recovery)
• Retention Periods, Lifecycle Management, Backup Policies, …
• Cross-Region Backup
• Cross-Account Backup (using AWS Organizations)
---
Selected Answer: C
C. AWS Backup

</details>

---

## Question 545: CLF-C02-ET-Q545
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company needs to categorize and track AWS usage cost based on business categories.

Which AWS service or feature should the company use to meet these requirements?

**Choices:**
- A) Cost allocation tags
- B) AWS Organizations
- C) AWS Security Hub
- D) AWS Cost and Usage Report

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
keyword - categorize = tag
---
Selected Answer: A
A. Cost allocation tags
---
Selected Answer: A
A. Cost allocation tags

Cost allocation tags enable you to categorize and track your AWS costs. When you apply tags to your AWS resources (such as EC2 instances or S3 buckets), AWS generates a Cost and Usage Report that includes usage and costs aggregated by tags. This allows you to allocate costs across your organization's business categories, making it easier to track and manage your AWS spending by project, department, application, or any other business-relevant dimension

</details>

---

## Question 546: CLF-C02-ET-Q546
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can migrate data between AWS storage services?

**Choices:**
- A) AWS DataSync
- B) AWS Direct Connect
- C) AWS Lake Formation
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS DataSync
• Move large amount of data from on-premises to AWS
---
I can not find this concept "AWS DataSync" in the CLF-C02 exam guide ???
---
Selected Answer: A
AWS DataSync works in 3 cases: 1. Transfer data between on premises and AWS; 2. Transfer data between AWS storage services; 3. Transfer data between AWS and other locations. 
https://aws.amazon.com/datasync/

</details>

---

## Question 547: CLF-C02-ET-Q547
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which statements represent the cost-effectiveness of the AWS Cloud? (Choose two.)

**Choices:**
- A) Users can trade fixed expenses for variable expenses.
- B) Users can deploy all over the world in minutes.
- C) AWS offers increased speed and agility.
- D) AWS is responsible for patching the infrastructure.
- E) Users benefit from economies of scale.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AE`  
**Community Consensus:** `83%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AE (83%). Contributor Answer: AE.

Community Rationale & Discussion:
Selected Answer: AE
A. Users can trade fixed expenses for variable expenses.
E. Users benefit from economies of scale.
---
Selected Answer: AE
A&E : cost benefit is the key.
---
Selected Answer: AE
AE, because the D even though is a benefit, the focus of the question is about cost

</details>

---

## Question 548: CLF-C02-ET-Q548
**Domain 1:** Cloud Concepts  

**Question:**  
A company wants to design its cloud architecture so that it can support development innovations, and continuously improve processes and procedures.

This is an example of which pillar of the AWS Well-Architected Framework?

**Choices:**
- A) Security
- B) Performance efficiency
- C) Operational excellence
- D) Reliability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `83%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (83%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
the keywords are : continuously improve processes and procedures"
"support development innovations". so the answer is operational excellence
---
Selected Answer: C
C. Operational excellence
---
Selected Answer: C
C : Operational excellence

</details>

---

## Question 549: CLF-C02-ET-Q549
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to consolidate the billing for multiple AWS accounts. The company needs to use one account to pay on behalf of all the other accounts.

Which AWS service or tool should the company use to meet this requirement?

**Choices:**
- A) AWS Trusted Advisor
- B) AWS Organizations
- C) AWS Budgets
- D) AWS Service Catalog

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Organizations allow you to merge accounts into one consolidated bill.

</details>

---

## Question 550: CLF-C02-ET-Q550
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is moving some of its on-premises IT services to the AWS Cloud. The finance department wants to see the entire bill so it can forecast spending limits.

Which AWS service can the company use to set spending limits and receive notifications if those limits are exceeded?

**Choices:**
- A) AWS Cost and Usage Reports
- B) AWS Budgets
- C) AWS Organizations consolidated billing
- D) Cost Explorer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B: AWS Budgets
---
Selected Answer: B
B. AWS Budgets

AWS Budgets is a service that allows users to set customized budgets that track and monitor their AWS spending. Users can set up alerts to be notified via email or SNS when their budget thresholds are approaching or exceeded. This service would allow the finance department to forecast spending limits and receive notifications if those limits are exceeded as requested.

</details>

---

## Question 551: CLF-C02-ET-Q551
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which AWS Support plans provide access to an AWS technical account manager (TAM)? (Choose two.)

**Choices:**
- A) AWS Basic Support
- B) AWS Developer Support
- C) AWS Business Support
- D) AWS Enterprise On-Ramp Support
- E) AWS Enterprise Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `DE`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: DE (75%). Contributor Answer: DE.

Community Rationale & Discussion:
Selected Answer: DE
https://aws.amazon.com/premiumsupport/plans/
---
Selected Answer: DE
D. AWS Enterprise On-Ramp Support
E. AWS Enterprise Support
---
Selected Answer: CE
C. AWS Business Support
E.AWS Enterprise Support

</details>

---

## Question 552: CLF-C02-ET-Q552
**Domain 3:** Cloud Technology and Services  

**Question:**  
Where can users find examples of AWS Cloud solution designs?

**Choices:**
- A) AWS Marketplace
- B) AWS Service Catalog
- C) AWS Architecture Center
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Architecture Center

Users can find examples of AWS Cloud solution designs in the AWS Architecture Center, which provides a collection of technical resources and best practices for building AWS-based applications.
---
Selected Answer: C
https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all

</details>

---

## Question 553: CLF-C02-ET-Q553
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which task is the responsibility of a company that is using Amazon RDS?

**Choices:**
- A) Provision the underlying infrastructure.
- B) Create IAM policies to control administrative access to the service.
- C) Install the cables to connect the hardware for compute and storage.
- D) Install and patch the RDS operating system.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Create IAM policies to control administrative access to the service.
---
RDS is a serveless service, YOU DON'T MANAGE THE OPERATING SYSTEM, but you control access to you data, so B is the answer
---
Selected Answer: B
RDS is a serveless service

</details>

---

## Question 554: CLF-C02-ET-Q554
**Domain 1:** Cloud Concepts  

**Question:**  
A company needs to evaluate its AWS environment and provide best practice recommendations in five categories: cost, performance, service limits, fault tolerance and security.
Which AWS service can the company use to meet these requirements?

**Choices:**
- A) AWS Shield
- B) AWS WAF
- C) AWS Trusted Advisor
- D) AWS Service Catalog

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. AWS Shield: Protects against DDoS attacks.
B. AWS WAF – Protects web applications from common exploits like SQL injection
C. AWS Trusted Advisor: provides real-time recommendations across five key categories: Cost, Performance, Service limits, Fault tolerance, Security
D. AWS Service Catalog – Manages approved AWS resources for use within an organization.: Manages approved AWS resources for use within an organization.
---
Selected Answer: C
C. AWS Trusted Advisor

Analyze your AWS accounts and provides
recommendation on 5 categories
• Cost optimization
• Performance
• Security
• Fault tolerance
• Service limits
---
who gives reccomendations its trusted advisor always

</details>

---

## Question 555: CLF-C02-ET-Q555
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which perspective in the AWS Cloud Adoption Framework (AWS CAF) includes capabilities for configuration management and patch management?

**Choices:**
- A) Platform
- B) Operations
- C) Security
- D) Governance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS CAF Operations perspective capabilities
• Observability
• Event management (AIOps)
• Incident and problem management
• Change and release management
• Performance and capacity management
• Configuration management
• Patch management
• Availability and continuity management
• Application management

Reference: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/operations-perspective.html
---
Selected Answer: B
AWS CAF Operations perspective capabilities
• Observability
• Event management (AIOps)
• Incident and problem management
• Change and release management
• Performance and capacity management
• Configuration management
• Patch management
• Availability and continuity management
• Application management

Reference: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/operations-perspective.html
---
Selected Answer: B
Opetations is the correct answer.

</details>

---

## Question 556: CLF-C02-ET-Q556
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a compute workload that is steady, predictable, and uninterruptible.
Which Amazon EC2 instance purchasing options meet these requirements MOST cost-effectively? (Choose two.)

**Choices:**
- A) On-Demand Instances
- B) Reserved Instances
- C) Spot Instances
- D) Saving Plans
- E) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B. Reserved Instances: Reserved Instances provide a significant discount compared to On-Demand Instances in exchange for a commitment to a one- or three-year term. Since the workload is steady and predictable, you can forecast your usage and purchase Reserved Instances accordingly, optimizing costs over time.

D. Saving Plans: Similar to Reserved Instances, Savings Plans offer significant discounts on usage in exchange for committing to a specific amount of compute usage (measured in dollars per hour) over a one- or three-year term. Savings Plans provide flexibility across a wider range of instance types and regions compared to Reserved Instances.
---
Yes the answer is BD.
---
Selected Answer: BD
Not dedicated hosts - keywords "MOST cost-effective"

</details>

---

## Question 557: CLF-C02-ET-Q557
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which Amazon EC2 pricing model is the MOST cost efficient for an uninterruptible workload that runs once a year for 24 hours?

**Choices:**
- A) On-Demand Instances
- B) Reserved Instances
- C) Spot Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (90%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Reserved Instances come with a minimum commitment period. The minimum time commitment for a Reserved Instance is typically one year or three years, depending on the type of Reserved Instance you choose.
---
Selected Answer: A
A. On-Demand Instances For an uninterruptible workload that runs once a year just for 24 hours, the most cost-efficient Amazon EC2 pricing model would be On-Demand Instances. On-Demand Instances are ideal for short-term workloads that spike periodically or unpredictable workloads that can’t be interrupted.
---
Selected Answer: A
A is correct and B, C, D are not correct.
"once a year for 24 hours" means that B. Reserved Instances should be excluded.
"uninterruptible" means that C. Spot Instances should be excluded.
"most cost-efficient" means that D. Dedicated Instances should be excluded.

</details>

---

## Question 558: CLF-C02-ET-Q558
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool helps users visualize, understand, and manage spending and usage over time?

**Choices:**
- A) AWS Organizations
- B) AWS Pricing Calculator
- C) AWS Cost Explorer
- D) AWS Service Catalog

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
What helps me is saying "to Explore is to visualize and a Calculator is to estimate."
---
A. AWS Organizations: Manages multiple AWS accounts in an organization, aiding in billing and cost allocation. Not focused on detailed spending visualization.

B. AWS Pricing Calculator: Estimates AWS service costs based on configurations. Lacks detailed historical spending and usage insights.

C. AWS Cost Explorer: Visualizes, understands, and manages AWS spending and usage over time. Provides detailed insights, historical data, and forecasting.

D. AWS Service Catalog: Manages approved IT service catalogs but doesn't focus on detailed cost visualization.
---
Selected Answer: C
cost explorer helps understand

</details>

---

## Question 559: CLF-C02-ET-Q559
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which service enables customers to audit API calls in their AWS accounts?

**Choices:**
- A) AWS CloudTrail
- B) AWS Trusted Advisor
- C) Amazon Inspector
- D) AWS X-Ray

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS CloudTrail: Enables customers to audit API calls in their AWS accounts by capturing and logging those calls. It provides visibility into user and resource activity and can be used for security analysis, compliance checking, and troubleshooting.

B. AWS Trusted Advisor: Provides best practices and recommendations for optimizing AWS resources. While it can offer guidance on security-related matters, it doesn't specifically focus on auditing API calls.

C. Amazon Inspector: Assesses the security vulnerabilities of applications deployed on AWS. It is more focused on security assessments and vulnerability detection rather than auditing API calls.

D. AWS X-Ray: Helps trace requests as they travel through applications, providing insights into application performance. It is not primarily designed for auditing API calls but for understanding and debugging distributed applications.
---
AWS CloudTrail is a service that records all API calls made on your AWS account. It provides a detailed history of events, including who made the call, what actions were performed, and from which IP address the call originated. This audit trail is valuable for security, compliance, troubleshooting, and monitoring purposes, and it helps you maintain visibility into how your AWS resources are being used.
---
Selected Answer: A
AWS CloudTrail enables customers to monitor and log API calls made within their AWS accounts. It provides detailed records of actions taken by users, services, and applications, allowing you to audit activities such as who made a request, which service was called, and what parameters were used. This is essential for compliance and security auditing.

</details>

---

## Question 560: CLF-C02-ET-Q560
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is an advantage that the AWS Cloud provides to users?

**Choices:**
- A) Users eliminate the need to guess about infrastructure capacity requirements.
- B) Users decrease their variable costs by maintaining sole ownership of IT hardware.
- C) Users maintain control of underlying IT infrastructure hardware.
- D) Users maintain control of operating systems for managed services.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Yap A is right answer.
---
Absolutely A
---
answer A is correct

</details>

---

## Question 561: CLF-C02-ET-Q561
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which feature of Amazon RDS provides the ability to automatically create a primary database instance and to synchronously replicate data to an instance in another Availability Zone?

**Choices:**
- A) Read replicas
- B) Blue/green deployment
- C) Multi-AZ deployment
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Key is synchronously as Read replicas are Asynch.
---
Selected Answer: C
Keyword: Automatically create a primary database instance and to synchronously replicate data to an instance in another Availability Zone.

Answer is C. Multi-AZ Deployment
---
Selected Answer: C
The answer is C

</details>

---

## Question 562: CLF-C02-ET-Q562
**Domain 2:** Security and Compliance  

**Question:**  
A company needs to check for IAM access keys that have not been rotated recently.

Which AWS service should the company use to meet this requirement?

**Choices:**
- A) AWS WAF
- B) AWS Shield
- C) Amazon Cognito
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
One of the checks performed by AWS Trusted Advisor is related to IAM Access Key Rotation. It identifies IAM users whose access keys have not been rotated within the recommended time period.
---
Selected Answer: D
Process of elimination:
AWS WAF is used to block SQL injection attacks
AWS Shield is used to protect against DDos attacks
Amazon Cognito is used to implement customer identity into your AWS Application

</details>

---

## Question 563: CLF-C02-ET-Q563
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company runs many Amazon EC2 instances in its VPC. The company wants to use a native AWS security resource to control network traffic between certain EC2 instances.

Which AWS service or feature will meet this requirement?

**Choices:**
- A) Network ACLs
- B) AWS WAF
- C) Amazon GuardDuty
- D) Security groups

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Security groups... keyword is "certain"
---
Selected Answer: D
D, security group is instance level; NACL is subnet level
---
Selected Answer: D
D. Security groups

</details>

---

## Question 564: CLF-C02-ET-Q564
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following can be components of a VPC in the AWS Cloud? (Choose two.)

**Choices:**
- A) Amazon API Gateway
- B) Amazon S3 buckets and objects
- C) AWS Storage Gateway
- D) Internet gateway
- E) Subnet

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `DE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: DE (100%). Contributor Answer: DE.

Community Rationale & Discussion:
Selected Answer: DE
In the AWS Cloud, a Virtual Private Cloud (VPC) can include several components. Here are two key components:

1. **Subnets**: These are segments of a VPC's IP address range where you can place groups of isolated resources¹.
2. **Internet Gateway**: This allows communication between instances in your VPC and the internet².

Source: Conversation with Copilot, 12/11/2024
(1) How Amazon VPC works - Amazon Virtual Private Cloud - docs.aws.amazon.com. https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html.
(2) Amazon VPC FAQs. https://aws.amazon.com/vpc/faqs/.
(3) Amazon Virtual Private Cloud (AWS VPC) Benefits & Components - K21Academy. https://k21academy.com/amazon-web-services/aws-vpc-virtual-private-cloud/.
---
Selected Answer: DE
D. Internet gateway
E. Subnet
---
DE is correct. 

Need discussion on 415 416 419 too. Thanks.

</details>

---

## Question 565: CLF-C02-ET-Q565
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is building a new application on AWS. The company needs the application to remain available if an individual application component fails.

Which design principle should the company use to meet this requirement?

**Choices:**
- A) Disposable resources
- B) Automation
- C) Rightsizing
- D) Loose coupling

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A change or a failure in one component should not cascade to other components
---
Selected Answer: D
D. Loose coupling
---
Loose coupling refers to designing the components of an application so that they are independent of one another. This allows the failure of one component to not affect the others, thus ensuring the application remains available and resilient even if an individual component fails. Loose coupling enables better fault tolerance and flexibility in managing the application.

</details>

---

## Question 566: CLF-C02-ET-Q566
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use a managed service to identify and protect sensitive data that is stored in Amazon S3.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS IAM Access Analyzer
- B) Amazon GuardDuty
- C) Amazon Inspector
- D) Amazon Macie

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon Macie manage sensitive data in S3
---
Selected Answer: D
D. Amazon Macie
---
Amazon Macie is a managed service that uses machine learning to automatically discover, classify, and protect sensitive data in Amazon S3. It is specifically designed to identify personally identifiable information (PII) or other sensitive data, helping organizations to meet compliance requirements and enhance data security.

</details>

---

## Question 567: CLF-C02-ET-Q567
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature can a user configure to limit network access at the subnet level?

**Choices:**
- A) AWS Shield
- B) AWS WAF
- C) Network ACL
- D) Security group

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Network ACL
---
Selected Answer: C
Subnet is the keyword
---
Selected Answer: C
AWS Shield protects from DDos attacks
AWS WAF protects from SQL injections
Security groups are used at the EC2 instance level

</details>

---

## Question 568: CLF-C02-ET-Q568
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service can a company use to manage encryption keys in the cloud?

**Choices:**
- A) AWS License Manager
- B) AWS Certificate Manager (ACM)
- C) AWS CloudHSM
- D) AWS Directory Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
CloudHSM: Hardware encryption, we manage encryption keys
---
Selected Answer: C
It is CloudHSM. The keyword is "encryption keys" as opposed to certificates, which would be AWS Certificate Manager.
---
Selected Answer: C
CloudHSM enables you to generate, store, and manage encryption keys in a dedicated hardware appliance.

</details>

---

## Question 569: CLF-C02-ET-Q569
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to enhance security by launching a third-party ISP intrusion detection system from its AWS account.

Which AWS service or resource should the company use to meet this requirement?

**Choices:**
- A) AWS Security Hub
- B) AWS Marketplace
- C) AWS Quick Starts
- D) AWS Security Center

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `50%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (50%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: D
To enhance security by launching a third-party ISP intrusion detection system from its AWS account, the company should use **AWS Marketplace**. AWS Marketplace offers a variety of third-party IDS/IPS solutions that can be easily deployed and integrated into your AWS environment⁴⁵.

(1) Intrusion Detection and Prevention - aws.amazon.com. https://aws.amazon.com/mp/scenarios/security/ids/.
(2) Discuss Amazon CLF-C01 Exam Topic 4 Question 11 - Pass4Success. https://www.pass4success.com/amazon/discussions/exam-clf-c01-topic-4-question-11-discussion.
(3) AWS re:Invent 2022 - Threat detection and incident response using cloud-native services (SEC309). https://www.youtube.com/watch?v=lx4igENUPVg.
(4) Evaluate Third-Party Resources with AWS Config. https://www.youtube.com/watch?v=XwPVKsvrFXc.
---
Selected Answer: B
B. AWS Marketplace - third party apps
---
Selected Answer: B
It's B, AWS Marketplace. The keyword is third-party.

</details>

---

## Question 570: CLF-C02-ET-Q570
**Domain 2:** Security and Compliance  

**Question:**  
What is a customer responsibility when using AWS Lambda according to the AWS shared responsibility model?

**Choices:**
- A) Managing the code within the Lambda function
- B) Confirming that the hardware is working in the data center
- C) Patching the operating system
- D) Shutting down Lambda functions when they are no longer in use

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Lambda allows developers to run code without provisioning or managing servers. Developers upload their code to Lambda and define the triggers that should invoke the function. The code runs in ephemeral containers, and Lambda takes care of managing the compute resources, allowing for highly scalable and cost-efficient execution of code in response to events.

A. Managing the code within the Lambda function: Customers are responsible for developing, deploying, and managing the code and dependencies within the Lambda function.

B. Confirming that the hardware is working in the data center: AWS manages the hardware infrastructure, and customers do not need to confirm or manage the underlying hardware.

C. Patching the operating system: AWS Lambda abstracts the underlying infrastructure, and customers are not responsible for patching the operating system. AWS takes care of the maintenance.

D. Shutting down Lambda functions when they are no longer in use: While it's good practice to manage resources efficiently, AWS Lambda is designed to automatically scale based on demand, and customers don't need to manually shut down functions.
---
Selected Answer: A
ccording to the AWS Shared Responsibility Model, AWS manages the underlying infrastructure (hardware, network, etc.) while the customer is responsible for the code and the configuration of their application.
---
Selected Answer: A
A. Managing the code within the Lambda function

</details>

---

## Question 571: CLF-C02-ET-Q571
**Domain 1:** Cloud Concepts  

**Question:**  
How does the AWS Cloud help companies build agility into their processes and cloud infrastructure?

**Choices:**
- A) Companies can avoid provisioning too much capacity when they do not know how much capacity is required.
- B) Companies can expand into new geographic regions.
- C) Companies can access a range of technologies to experiment and innovate quickly.
- D) Companies can pay for IT resources only when they use the resources.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Companies can access a range of technologies to experiment and innovate quickly.
---
Selected Answer: C
Gives access to a broad set of tools and services, companies can swiftly try new ideas, develop and test applications, and adopt new technologies without the need for significant upfront investment or the constraints of physical infrastructure. This capability enables faster iteration and innovation, allowing businesses to stay competitive and respond more rapidly to market changes.
---
Selected Answer: C
Agree with b0nb0n101. C seems to be the right pick to build agility into the processes and cloud infrastructure.

</details>

---

## Question 572: CLF-C02-ET-Q572
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or tool gives a company the ability to release application changes in an automated way?

**Choices:**
- A) Amazon AppFlow
- B) AWS CodeDeploy
- C) AWS PrivateLink
- D) Amazon EKS Distro

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS CodeDeploy:
automates code deployments to any instance, including EC2
instances and instances running on premises
---
Selected Answer: B
AWS CodeDeploy
• We want to deploy our application
automatically
---
Selected Answer: B
B. AWS CodeDeploy

</details>

---

## Question 573: CLF-C02-ET-Q573
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud Adoption Framework (AWS CAF) perspective focuses on managing identities and permissions at scale?

**Choices:**
- A) Operations
- B) Platform
- C) Governance
- D) Security

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Security - Identity and Access Management
---
Selected Answer: D
Identity & Access Management -> Security

</details>

---

## Question 574: CLF-C02-ET-Q574
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature allows users to securely store encrypted credentials and retrieve these credentials when required?

**Choices:**
- A) AWS Encryption SDK
- B) AWS Security Hub
- C) AWS Secrets Manager
- D) AWS Artifact

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Secrets Manager
---
C is correct. 

need discussion on 424 428 429. Thanks.
---
Selected Answer: C
The correct answer is C. AWS Secrets Manager. It allows users to securely store and centrally manage secrets such as database credentials, API keys, and other sensitive information. You can use fine-grained AWS Identity and Access Management (IAM) policies to control access to these secrets, and Secrets Manager also supports automatic rotation of secrets to meet security and compliance requirements1. If you need to retrieve a credential from Secrets Manager, you can log into the AWS account, choose Secrets Manager from the Services menu, search for the desired credential, and retrieve its secret value2.

</details>

---

## Question 575: CLF-C02-ET-Q575
**Domain 1:** Cloud Concepts  

**Question:**  
Which pillar of the AWS Well-Architected Framework aligns with the ability to make frequent, small, and reversible changes to AWS Cloud architecture?

**Choices:**
- A) Security
- B) Cost optimization
- C) Operational excellence
- D) Performance efficiency

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Operational excellence
---
C. Operational excellence

</details>

---

## Question 576: CLF-C02-ET-Q576
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service or resource can a company use to deploy AWS WAF rules?

**Choices:**
- A) Amazon EC2
- B) Application Load Balancer
- C) AWS Trusted Advisor
- D) Network Load Balancer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS WAF – Web Application Firewall
• Protects your web applications from common web exploits (Layer 7)
• Layer 7 is HTTP (vs Layer 4 is TCP)
• Deploy on Application Load Balancer, API Gateway, CloudFront
---
Selected Answer: B
WAF is HTTP, level 7; Network load balance is TCP, level 3
---
Selected Answer: B
B. Application Load Balancer- AWS WAF can be deployed to filter HTTP(S) traffic before it reaches your web application.

</details>

---

## Question 577: CLF-C02-ET-Q577
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company hosts its website on Amazon EC2 instances. The company needs to ensure that the website reaches a global audience and provides minimum latency to users.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon Route 53
- B) Amazon CloudFront
- C) Elastic Load Balancing
- D) AWS Lambda

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Why not Amazon Route 53 which does the same to avoid network latency?
---
Selected Answer: B
B. Amazon CloudFront
---
Selected Answer: B
Amazon CloudFront: It’s a content delivery network (CDN) service that distributes content globally through a network of edge locations. CloudFront caches and delivers static and dynamic content (including HTML, images, videos, and APIs) from the nearest edge location to the user, reducing latency significantly. By using CloudFront, the company can serve web content efficiently to users worldwide, improving their experience.

</details>

---

## Question 578: CLF-C02-ET-Q578
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS design principle emphasizes the reduction of interdependencies between components of an application?

**Choices:**
- A) Scalability
- B) Loose coupling
- C) Automation
- D) Caching

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
• Loose Coupling:
• Monolith are applications that do more and more over time, become bigger
• Break it down into smaller, loosely coupled components
• A change or a failure in one component should not cascade to other components
---
Selected Answer: B
B. Loose coupling
---
B. Loose coupling

The principle of loose coupling emphasizes the reduction of interdependencies between components of an application. This allows components to evolve independently and enhances system flexibility and resilience.

</details>

---

## Question 579: CLF-C02-ET-Q579
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to provide one of its employees with access to Amazon RDS. The company also wants to limit the interaction to only the AWS CLI and AWS software development kits (SDKs).

Which combination of actions should the company take to meet these requirements while following the principles of least privilege? (Choose two.)

**Choices:**
- A) Create an IAM user and provide AWS Management Console access only.
- B) Create an IAM user and provide programmatic access only.
- C) Create an IAM role and provide AWS Management Console access only.
- D) Create an IAM policy with administrator access and attach it to the IAM user.
- E) Create an IAM policy with Amazon RDS access and attach it to the IAM user.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
B. Create an IAM user and provide programmatic access only. - allows user to interact with AWS services through CLI or SDKs. 
E. Create an IAM policy with Amazon RDS access and attach it to the IAM user. - user can only interact with RDS and not other AWS resources.
---
Selected Answer: BE
B: Create an IAM user and provider programmatic access only--> This would cover access via AWS CLI or SDK.
E: Create IAM policy with Amazon RDs access --> Would cover just access to RDS ,which is to give only permissions to access required resources that's RDS DB.

</details>

---

## Question 580: CLF-C02-ET-Q580
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is running a reporting web server application on Amazon EC2 instances. The application runs once every week and once again at the end of the month. The EC2 instances can be shut down when they are not in use.

What is the MOST cost-effective billing model for this use case?

**Choices:**
- A) Standard Reserved Instances
- B) Convertible Reserved Instances
- C) On-Demand Capacity Reservations
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (67%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: C
AWS On-Demand Capacity Reservations and On-Demand Instances serve different purposes:
1. On-Demand Capacity Reservations:
 -Purpose: Reserve compute capacity in a specific Availability Zone for any duration.
 -Flexibility: Can be created, modified, or canceled at any time.
 -Use Cases: Ideal for ensuring capacity for business-critical workloads, regulatory requirements, and disaster recovery.
2. On-Demand Instances:
 - Purpose: Provide compute capacity without any upfront commitment.
 - Flexibility: Pay for compute capacity by the hour or second, depending on the instance type.
 - Use Cases: Suitable for applications with unpredictable workloads or short-term requirements(1).
(1) https://aws.amazon.com/compare/the-difference-between-on-demand-instances-and-reserved-instances/.
---
Selected Answer: D
D. On-Demand Instances
---
In this scenario, the application only runs periodically—once every week and at the end of the month. Since the EC2 instances can be shut down when not in use, On-Demand Instances are the most cost-effective option.

On-Demand Instances are ideal for intermittent workloads that do not require long-term or consistent usage commitments, allowing the company to pay only for the compute time they use.

</details>

---

## Question 581: CLF-C02-ET-Q581
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has 5 TB of data stored in Amazon S3. The company plans to occasionally run queries on the data for analysis.
Which AWS service should the company use to run these queries in the MOST cost-effective manner?

**Choices:**
- A) Amazon Redshift
- B) Amazon Athena
- C) Amazon Kinesis
- D) Amazon RDS

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `98%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (98%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Athena
Amazon Athena is a serverless query service that allows you to analyze data directly in Amazon S3 using standard SQL queries. You don't need to set up or manage any infrastructure; you only pay for the queries you run. It is well-suited for ad-hoc and exploratory analysis on data stored in S3 without the need for maintaining a separate database.
Option A (Amazon Redshift) is a fully-managed data warehouse service and is more suitable for complex analytics and large-scale data warehousing scenarios. It might be more cost-effective for frequent and complex analytical workloads.
Option C (Amazon Kinesis) is a service for real-time processing of streaming data and is not designed for running ad-hoc queries on stored data.
Option D (Amazon RDS) is a managed relational database service and is not the most cost-effective choice for running queries directly on data stored in S3.
---
Selected Answer: B
The answer is B.

Amazon Athena is a serverless, interactive analytics service built on open-source frameworks, supporting open-table and file formats. Athena provides a simplified, flexible way to analyze petabytes of data where it lives. Analyze data or build applications from an Amazon Simple Storage Service (S3) data lake and 30 data sources, including on-premises data sources or other cloud systems using SQL or Python. Athena is built on open-source Trino and Presto engines and Apache Spark frameworks, with no provisioning or configuration effort required.
https://aws.amazon.com/athena/
---
Selected Answer: B
Amazon Athena is a serverless query service that allows you to run SQL queries directly on data stored in Amazon S3. You pay only for the amount of data scanned during the query, which makes it a cost-effective solution for occasional querying, especially when dealing with large datasets such as the 5 TB in this case.

</details>

---

## Question 582: CLF-C02-ET-Q582
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to discover, prepare, move, and integrate data from multiple sources for data analytics and machine learning.

Which AWS serverless data integration service should the company use to meet these requirements?

**Choices:**
- A) AWS Glue
- B) AWS Data Exchange
- C) Amazon Athena
- D) Amazon EMR

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Data Exchange is a service that simplifies finding, subscribing to, and using third-party data in the AWS Cloud.
Amazon EMR (Elastic MapReduce) is a managed cluster platform that simplifies running big data frameworks like Apache Hadoop and Apache Spark on AWS.
Amazon Athena is a serverless, interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL.
---
Selected Answer: A
A. AWS Glue
---
AWS Glue -> for ETL service

need discussion on 431 432 433 434 435 437 438 Thanks.

</details>

---

## Question 583: CLF-C02-ET-Q583
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is moving its development and test environments to AWS to increase agility and reduce cost. Because these are not production workloads and the servers are not fully utilized, occasional unavailability is acceptable.

What is the MOST cost-effective Amazon EC2 pricing model that will meet these requirements?

**Choices:**
- A) Reserved Instances
- B) On-Demand Instances
- C) Spot Instances
- D) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Spot Instances due to occasional unavailability being acceptable.
---
C. Spot Instances

</details>

---

## Question 584: CLF-C02-ET-Q584
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company deploys its application on Amazon EC2 instances. The application occasionally experiences sudden increases in demand. The company wants to ensure that its application can respond to changes in demand at the lowest possible cost.

Which AWS service or concept will meet these requirements?

**Choices:**
- A) AWS Auto Scaling
- B) AWS Compute Optimizer
- C) AWS Cost Explorer
- D) AWS Well-Architected Framework

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Auto Scaling - automatically adjusts number of EC2 instances due to demand.

</details>

---

## Question 585: CLF-C02-ET-Q585
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to organize its users so that the company can grant permissions to the users as a group.

Which AWS service or tool can the company use to meet this requirement?

**Choices:**
- A) Security groups
- B) AWS Identity and Access Management (IAM)
- C) Resource groups
- D) AWS Security Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Identity and Access Management (IAM) - allows you to manage users and their permissions

</details>

---

## Question 586: CLF-C02-ET-Q586
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to build an application that uses AWS Lambda to run Python code.

Under the AWS shared responsibility model, which tasks will be the company’s responsibility? (Choose two.)

**Choices:**
- A) Management of the underlying infrastructure.
- B) Management of the operating system.
- C) Writing the business logic code.
- D) Installation of the computer language runtime.
- E) Providing AWS Identity and Access Management (IAM) access to the Lambda service.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CE (100%). Contributor Answer: CE.

Community Rationale & Discussion:
Selected Answer: CE
C. Writing the business logic code.
E. Providing AWS Identity and Access Management (IAM) access to the Lambda service.
---
Selected Answer: CE
This is correct.

</details>

---

## Question 587: CLF-C02-ET-Q587
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to identify who accessed an AWS service and what action was performed for a given time period.

Which AWS service should the company use to meet this requirement?

**Choices:**
- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) AWS Security Hub
- D) Amazon Inspector

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Keyword: Who accessed an AWS service and what action was performed.

AWS CloudTrail:
CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage.

Answer is B.AWS CloudTrail
---
B. AWS CloudTrail

</details>

---

## Question 588: CLF-C02-ET-Q588
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to use a centralized AWS service to enforce compliance with the organizational business standards. The company wants to use an AWS service that can govern and control who can deploy, manage, and decommission AWS resources.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon CloudWatch
- B) AWS Service Catalog
- C) Amazon GuardDuty
- D) AWS Security Hub

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Service Catalog is correct answer.
https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html
---
B. AWS Service Catalog.
---
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. It helps enforce compliance by controlling which services and configurations are available for deployment. Administrators can define and manage these catalogs, ensuring that only compliant and approved resources can be deployed. This service also helps in governing and controlling the lifecycle of these resources, from deployment to decommissioning.

</details>

---

## Question 589: CLF-C02-ET-Q589
**Domain 2:** Security and Compliance  

**Question:**  
What does "security of the cloud” refer to in the AWS shared responsibility model?

**Choices:**
- A) Availability of AWS services such as Amazon EC2
- B) Security of the cloud infrastructure that runs all the AWS services
- C) Implementation of password policies for IAM users
- D) Security of customer environments by using AWS Network Firewall partners

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS responsibility - Security of the Cloud
• Protecting infrastructure (hardware, software, facilities, and networking) that runs
all the AWS services
• Managed services like S3, DynamoDB, RDS, etc.
---
Selected Answer: B
B. Security of the cloud infrastructure that runs all the AWS services
---
Selected Answer: B
Security of the cloud vs security in the cloud (customer).

</details>

---

## Question 590: CLF-C02-ET-Q590
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has an application that produces unstructured data continuously. The company needs to store the data so that the data is durable and easy to query.

Which AWS service can the company use to meet these requirements?

**Choices:**
- A) Amazon RDS
- B) Amazon Aurora
- C) Amazon QuickSight
- D) Amazon DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon DynamoDB
---
Amazon DynamoDB is not specifically designed for unstructured data, but it can handle semi-structured and structured data effectively.
---
Selected Answer: D
Unstructured data = non-relational database. DynamoDB

</details>

---

## Question 591: CLF-C02-ET-Q591
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which options are AWS Cloud Adoption Framework (AWS CAF) perspectives? (Choose two.)

**Choices:**
- A) Cloud fluency
- B) Security
- C) Change acceleration
- D) Architecture
- E) Business

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
B and E are right answers
https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html
---
Selected Answer: BE
B and e
---
B,E - Correct, six Business People Governance Platform Security Operation 

need help with discussion on 440 441 442 444 447 449 Thanks.

</details>

---

## Question 592: CLF-C02-ET-Q592
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which AWS service can be used at no additional cost?

**Choices:**
- A) Amazon SageMaker
- B) AWS Config
- C) AWS Organizations
- D) Amazon CloudWatch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (91%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A. Amazon SageMaker: While Amazon SageMaker has a free tier that includes certain usage limits, it's important to note that certain features and usage beyond the free tier may incur additional costs

B. AWS Config: AWS Config has associated costs based on the number of configuration items recorded and API activity. It is not a service that is provided at no additional cost.

C. AWS Organizations: This service allows you to consolidate multiple AWS accounts into an organization, and it is indeed available at no additional cost. However, costs associated with the resources used in the accounts within the organization are separate.

D. Amazon CloudWatch: While CloudWatch itself is not entirely free, there is a free tier with limited usage. Beyond the free tier, there are associated costs based on the quantity of metrics, dashboards, alarms, and logs stored.
---
Selected Answer: C
The answer is C.

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations is offered at no additional charge. You are charged only for AWS resources that users and roles in your member accounts use. For example, you are charged the standard fees for Amazon EC2 instances that are used by users or roles in your member accounts. 
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
---
Selected Answer: C
AWS Organizations is a service that enables you to manage and consolidate multiple AWS accounts under a single organization. There is no additional cost to use AWS Organizations; you are only charged for the AWS services you use under the organization.

</details>

---

## Question 593: CLF-C02-ET-Q593
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to migrate a company’s on-premises container infrastructure to the AWS Cloud. The company wants to prevent unplanned administration and operation cost and adapt to a serverless architecture.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Connect
- B) AWS Fargate
- C) Amazon Lightsail
- D) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. AWS Fargate -serverless
---
Selected Answer: B
Serverless is the key word.
---
Selected Answer: B
B is correct

</details>

---

## Question 594: CLF-C02-ET-Q594
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants its Amazon EC2 instances to be in different locations but share the same geographic area. The company also wants to use multiple power grids and independent networking connectivity for the EC2 instances.

Which solution meets these requirements?

**Choices:**
- A) Use EC2 instances in multiple edge locations in the same AWS Region.
- B) Use EC2 instances in multiple Availability Zones in the same AWS Region.
- C) Use EC2 instances in multiple Amazon Connect locations in the same AWS Region.
- D) Use EC2 instances in multiple AWS Artifact locations in the same AWS Region.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Use EC2 instances in multiple Availability Zones in the same AWS Region.
---
Selected Answer: B
Keyword: Different locations but share the same geographic area & independent networking connectivity for the EC2 instances. 

Different locations indicates AZ(Availability Zones)
Same geographic area indicates Single AWS Region
Independent networking connectivity indicates each AZ associated with different subnets

Answer is B. Use EC2 instances in multiple Availability Zones in the same AWS Region.
---
Selected Answer: B
B is correct

</details>

---

## Question 595: CLF-C02-ET-Q595
**Domain 3:** Cloud Technology and Services  

**Question:**  
An ecommerce company has deployed a new web application on Amazon EC2 instances. The company wants to distribute incoming HTTP traffic evenly across all running instances.

Which AWS service or resource will meet this requirement?

**Choices:**
- A) Amazon EC2 Auto Scaling
- B) Application Load Balancer
- C) Gateway Load Balancer
- D) Network Load Balancer

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Application Load Balancer
---
Selected Answer: B
Keyword: Distribute incoming HTTP traffic evenly across all running instances.

Application Load Balancer supports Layer 7,it means HTTP protocol
Network Load Balancer supports Layer 4,it means TCP/UDP protocol

Answer is B. Application Load Balancer
---
Selected Answer: B
ALB works at Layer 7, meaning HTTPS. NLB works at Layer 4.

</details>

---

## Question 596: CLF-C02-ET-Q596
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature gives users the ability to connect VPCs and on-premises networks to a central hub?

**Choices:**
- A) Virtual private gateway
- B) AWS Transit Gateway
- C) Internet gateway
- D) Customer gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Transit Gateway • For having transitive peering
between thousands of VPC and
on
-premises, hub-and
-spoke
(star) connection
---
Selected Answer: B
The AWS Transit Gateway is the service that allows users to connect Amazon Virtual Private Clouds (VPCs) and on-premises networks through a central hub. Acting as a virtual router, it simplifies network architecture by reducing the need for numerous point-to-point connections or Transit VPCs
---
Answer is B

</details>

---

## Question 597: CLF-C02-ET-Q597
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run CPU-intensive workload across multiple Amazon EC2 instances.

Which EC2 instance type should the company use to meet this requirement?

**Choices:**
- A) General purpose instances
- B) Compute optimized instances
- C) Memory optimized instances
- D) Storage optimized instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Keyword: Run CPU-intensive workload

If any user wants to run the EC2 workload based on the CPU means, nothing but CPU indicates Core counts of the EC2 server.

In AWS Compute instance family supports the CPU (Core Counts is very high)

Answer is B. Compute optimized instances
---
B. Compute optimized instances

</details>

---

## Question 598: CLF-C02-ET-Q598
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is connecting multiple VPCs and on-premises networks. The company needs to use an AWS service as a cloud router to simplify peering relationships.

Which AWS service can the company use to meet this requirement?

**Choices:**
- A) AWS Direct Connect
- B) AWS Transit Gateway
- C) Amazon Connect
- D) Amazon Route 53

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Transit Gateway is a fully managed service that acts as a cloud router.
---
Selected Answer: B
Keyword: Connecting multiple VPCs and on-premises networks & Simplify peering relationships.

AWS Transit Gateway is the AWS service that allows you to connect multiple VPCs and on-premises networks through a central hub. It simplifies network management by eliminating the need for complex peering relationships.

Answer is B. AWS Transit Gateway
---
Selected Answer: B
AWS Transit Gateway acts as a cloud router to connect multiple Amazon Virtual Private Clouds (VPCs) and on-premises networks. It simplifies the management of network interconnections and allows for scalable peering relationships.
from chat gpt

</details>

---

## Question 599: CLF-C02-ET-Q599
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company stores a large amount of data that auditors access only twice each year.

Which Amazon S3 storage class should the company use to store the data with the LOWEST cost?

**Choices:**
- A) Amazon S3 Outposts
- B) Amazon S3 Glacier Instant Retrieval
- C) Amazon S3 Standard
- D) Amazon S3 Intelligent-Tiering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `65%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (65%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon S3 Glacier Instant Retrieval
• Millisecond retrieval, great for data accessed once a quarter
• Minimum storage duration of 90 days
---
Selected Answer: B
B. Amazon S3 Glacier Instant Retrieval - lowest cost for infrequent access, but fast retrieval

S3 Intelligent-Tiering is the recommended storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period, such as data lakes, data analytics, and new applications.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html#:~:text=The%20S3%20Intelligent-Tiering%20storage%20class%20supports%20all%20Amazon,endpoint%20in%20a%20virtual%20private%20%20cloud%20%28VPC%29
---
Selected Answer: D
Considering that Intelligent-Tiering has been the answer for "cheap" on this website until now, I'm inclined to vote for it.

</details>

---

## Question 600: CLF-C02-ET-Q600
**Domain 2:** Security and Compliance  

**Question:**  
Which action should a company take to improve security in its AWS account?

**Choices:**
- A) Require multi-factor authentication (MFA) for privileged users.
- B) Remove the root user account.
- C) Create an access key for the AWS account root user.
- D) Create an access key for each privileged user.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Require multi-factor authentication (MFA) for privileged users - adds additional layer of security beyond username and password. Privileged users are more likely to be targeted for attacks, and if their password is compromised the malicious actor would still need the second factor.

</details>

---

## Question 601: CLF-C02-ET-Q601
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following are ways to improve security on AWS? (Choose two.)

**Choices:**
- A) Using AWS Artifact
- B) Granting the broadest permissions to all IAM roles
- C) Running application code with AWS Cloud
- D) Enabling multi-factor authentication (MFA) with Amazon Cognito
- E) Using AWS Trusted Advisor security checks

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `DE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: DE (100%). Contributor Answer: DE.

Community Rationale & Discussion:
Selected Answer: DE
D. Enabling multi-factor authentication (MFA) with Amazon Cognito
E. Using AWS Trusted Advisor security checks
---
Selected Answer: DE
The correct answers are:

D. Enabling multi-factor authentication (MFA) with Amazon Cognito
E. Using AWS Trusted Advisor security checks

Explanation:
D. Enabling multi-factor authentication (MFA) with Amazon Cognito

Enhanced Security: Multi-factor authentication (MFA) adds an extra layer of security by requiring users to provide a second form of verification in addition to their password.
User Management: Amazon Cognito allows managing user identities and applying robust security policies, including the use of MFA.

</details>

---

## Question 602: CLF-C02-ET-Q602
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service can a company use to manage encryption keys in the cloud?

**Choices:**
- A) AWS License Manager
- B) AWS Certificate Manager (ACM)
- C) AWS CloudHSM
- D) AWS Directory Service

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
CloudHSM: Hardware encryption, we manage encryption keys
---
Selected Answer: C
C. AWS CloudHSM
---
Selected Answer: C
Hardware Security Module...correct

</details>

---

## Question 603: CLF-C02-ET-Q603
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud Adoption Framework (AWS CAF) capability belongs to the people perspective?

**Choices:**
- A) Data architecture
- B) Event management
- C) Cloud fluency
- D) Strategic partnership

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The answer is C.

Data architecture => Platform
Event management => Operations
Cloud fluency => People
Strategic partnership => Business
https://abhi0751.medium.com/aws-cloud-adoption-framework-aws-caf-a512b89dbcba
---
Selected Answer: C
A. Data architecture: This capability is more related to the data perspective within the AWS Cloud Adoption Framework (CAF). It involves designing and implementing effective data architectures.

B. Event management: This capability is related to the operations perspective within the AWS CAF. It involves managing events, incidents, and responses in the cloud environment.

C. Cloud fluency: This capability belongs to the people perspective within the AWS CAF. It emphasizes the importance of having a workforce that is knowledgeable and skilled in cloud technologies.

D. Strategic partnership: While collaboration and partnerships are important across perspectives, this capability is often associated with the business perspective. It involves forming strategic partnerships to support cloud adoption and business goals.
---
Selected Answer: C
The People perspective focuses on how an organization develops and manages its people during the cloud adoption process. This perspective is aimed at building skills, culture, and cloud fluency across the organization.

</details>

---

## Question 604: CLF-C02-ET-Q604
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to store its files in the AWS Cloud. Users need to be able to download these files directly using a public URL.

Which AWS service or feature will meet this requirement?

**Choices:**
- A) Amazon Redshift
- B) Amazon Elastic Block Store (Amazon EBS)
- C) Amazon Elastic File System (Amazon EFS)
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon S3 - you can make objects publicly available via URL.
---
Amazon S3 (Simple Storage Service) is an object storage service designed for storing and retrieving large amounts of data, including files such as documents, images, videos, backups, and more. With Amazon S3, you can easily store files and configure access permissions to make the files publicly accessible via a direct URL, which perfectly fits the requirement of allowing users to download files directly from a public URL.
---
keyword : url - S3

</details>

---

## Question 605: CLF-C02-ET-Q605
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is using AWS for all its IT infrastructure. The company's developers are allowed to deploy applications on their own. The developers want to deploy their applications without having to provision the infrastructure themselves.

Which AWS service should the developers use to meet these requirements?

**Choices:**
- A) AWS CloudFormation
- B) AWS CodeBuild
- C) AWS Elastic Beanstalk
- D) AWS CodeDeploy

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C is correct. 

need help with discussion on 452 453 454 Thanks.
---
Selected Answer: C
"...AWS Elastic Beanstalk automates the details of capacity provisioning, load balancing, auto scaling, and application deployment, creating an environment that runs a version of your application..."

https://aws.amazon.com/elasticbeanstalk/faqs/

</details>

---

## Question 606: CLF-C02-ET-Q606
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to gain insights from its data and build interactive data visualization dashboards.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon SageMaker
- B) Amazon Rekognition
- C) Amazon QuickSight
- D) Amazon Kinesis

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon QuickSight: Serverless machine learning powered business intelligence service
to create interactive dashboards
---
Selected Answer: C
C. Amazon QuickSight
---
Selected Answer: C
Answer is C

</details>

---

## Question 607: CLF-C02-ET-Q607
**Domain 3:** Cloud Technology and Services  

**Question:**  
A cloud engineer wants to store data in Amazon S3. The engineer will access some of the data yearly and some of the data daily.

Which S3 storage class will meet these requirements MOST cost-effectively?

**Choices:**
- A) S3 Standard
- B) S3 Glacier Deep Archive
- C) S3 One Zone-Infrequent Access (S3 One Zone-IA)
- D) S3 Intelligent-Tiering

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
S3 Intelligent-Tiering: Unknown access patterns
(access some of the data yearly and some of the data daily)
---
Selected Answer: D
D. S3 Intelligent-Tiering
---
C. S3 One Zone-Infrequent Access (S3 One Zone-IA)

</details>

---

## Question 608: CLF-C02-ET-Q608
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following are economic benefits of using the AWS Cloud? (Choose two.)

**Choices:**
- A) Consumption-based pricing
- B) Perpetual licenses
- C) Economies of scale
- D) AWS Enterprise Support at no additional cost
- E) Bring-your-own-hardware model

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
Consumption-based pricing and economies of scale
---
A. Consumption-based pricing
C. Economies of scale:

</details>

---

## Question 609: CLF-C02-ET-Q609
**Domain 2:** Security and Compliance  

**Question:**  
Which option is a shared responsibility between AWS and its customers under the AWS shared responsibility model?

**Choices:**
- A) Configuration of Amazon EC2 instance operating systems
- B) Application file system server-side encryption
- C) Patch management
- D) Security of the physical infrastructure

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Shared Controls 
"AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications."

Reference: https://aws.amazon.com/compliance/shared-responsibility-model/
---
Selected Answer: C
Under the AWS shared responsibility model, patch management is a shared responsibility. AWS is responsible for patching the infrastructure and services they manage, while customers are responsible for patching the operating systems and applications running on their Amazon EC2 instances and other resources.
---
Selected Answer: C
Shared Controls. Examples include:
1. Patch Management
2. Configuration Management
3. Awareness and Training

</details>

---

## Question 610: CLF-C02-ET-Q610
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its on-premises workloads to the AWS Cloud. The company wants to separate workloads for chargeback to different departments.
Which AWS services or features will meet these requirements? (Choose two.)

**Choices:**
- A) Placement groups
- B) Consolidated billing
- C) Edge locations
- D) AWS Config
- E) Multiple AWS accounts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
B. Consolidated Billing

Consolidated billing is a feature of AWS Organizations that allows you to combine billing for multiple AWS accounts. With consolidated billing, each department can have its own AWS account for tracking and managing its resources separately, while the company enjoys the convenience of a single payment method for all these accounts. This setup makes it easier to track costs and implement chargeback mechanisms.
E. Multiple AWS Accounts

Creating multiple AWS accounts, one for each department, is an effective way to segregate resources, manage permissions, and track costs separately. This approach enhances security by limiting the scope of access and impact of changes, and it simplifies the process of attributing costs to the right department. Combined with consolidated billing, it provides both organizational flexibility and centralized financial control.
---
Selected Answer: BE
B. Consolidated billing:

AWS Consolidated Billing allows organizations to manage multiple AWS accounts under a single AWS Organization. It simplifies the billing process by consolidating usage and billing into one bill while still tracking costs for each account. This enables chargeback to specific departments based on their resource usage.
E. Multiple AWS accounts:

Using multiple AWS accounts helps isolate workloads for different departments or teams. This makes it easier to allocate costs directly to specific accounts, enabling precise chargeback.
Other Options:
---
Selected Answer: BE
B. Consolidated billing
E. Multiple AWS accounts

</details>

---

## Question 611: CLF-C02-ET-Q611
**Domain 2:** Security and Compliance  

**Question:**  
Which task is a responsibility of AWS, according to the AWS shared responsibility model?

**Choices:**
- A) Enable client-side encryption for objects that are stored in Amazon S3.
- B) Configure IAM security policies to comply with the principle of least privilege.
- C) Patch the guest operating system on an Amazon EC2 instance.
- D) Apply updates to the Nitro Hypervisor.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Given the options:

A. Enabling client-side encryption for objects that are stored in Amazon S3 is a customer responsibility. This involves managing encryption keys and configuring encryption settings.

B. Configuring IAM (Identity and Access Management) security policies to comply with the principle of least privilege is a customer responsibility. It involves managing access and permissions for AWS resources.

C. Patching the guest operating system on an Amazon EC2 instance is a customer responsibility. It involves maintaining the security of the operating system running on the EC2 instance.

D. Applying updates to the Nitro Hypervisor is an AWS responsibility. The Nitro Hypervisor is a component of the underlying infrastructure managed by AWS.

Therefore, the correct answer is:

D. Apply updates to the Nitro Hypervisor.
---
Selected Answer: D
100% D
---
D. Applying updates to the Nitro Hypervisor is an AWS responsibility. The Nitro Hypervisor is a component of the underlying infrastructure managed by AWS.

</details>

---

## Question 612: CLF-C02-ET-Q612
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is a benefit of using AWS for cloud computing?

**Choices:**
- A) Trade variable expense for fixed expense
- B) Pay-as-you-go pricing
- C) Decreased speed and agility
- D) Spending money running and maintaining data centers

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `87%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (87%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Trade fixed expense for variable expense and not vice versa, so option B
---
Selected Answer: B
Obviously B, pay-as-you-go pricing. It is the same in every cloud platform e.g. Azure, GCP, AWS. 
Come on, we pay for this site here and they make so obvious mistakes... :(
---
Selected Answer: B
B. Pay-as-you-go pricing

</details>

---

## Question 613: CLF-C02-ET-Q613
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is an AWS Cloud Adoption Framework (AWS CAF) business perspective capability?

**Choices:**
- A) Culture evolution
- B) Event management
- C) Data monetization
- D) Platform architecture

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (88%). Contributor Answer: C.

Community Rationale & Discussion:
A. Culture evolution == People
B. Event management == Operations
C. Data monetization == Business
D. Platform architecture == Platform
---
Selected Answer: C
Data monetization
---
Selected Answer: C
C. Data monetization
• Data monetization – Leverage data to obtain measurable business benefit. Cloud facilitates the collection, storage, and analysis of vast amounts of data. To obtain measurable business benefits, develop a comprehensive and long-term data monetization strategy that’s aligned with your strategic intent. Identify opportunities for leveraging data and analytics to improve operations, customer and employee experience, and decision-making, as well as to enable new business models.

</details>

---

## Question 614: CLF-C02-ET-Q614
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user is moving a workload from a local data center to an architecture that is distributed between the local data center and the AWS Cloud.

Which type of migration is this?

**Choices:**
- A) On-premises to cloud native
- B) Hybrid to cloud native
- C) On-premises to hybrid
- D) Cloud native to hybrid

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (86%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. On-premises to hybrid
---
C is correct

need help with discussion on 456~466. Thanks.
---
Selected Answer: C
C is correct

</details>

---

## Question 615: CLF-C02-ET-Q615
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company needs to store infrequently used data for data archives and long-term backups.

Which AWS service or storage class will meet these requirements MOST cost-effectively?

**Choices:**
- A) Amazon FSx for Lustre
- B) Amazon Elastic Block Store (Amazon EBS)
- C) Amazon Elastic File System (Amazon EFS)
- D) Amazon S3 Glacier Flexible Retrieval

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon S3 Glacier Flexible Retrieval
---
Selected Answer: D
Keyword: infrequently used data for data archives and long-term backups.

Data Archives and long term backup supports by Amazon S3 Glacier only.

Answer: D. Amazon S3 Glacier Flexible Retrieval

</details>

---

## Question 616: CLF-C02-ET-Q616
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides users with AWS issued reports, certifications, accreditations, and third-party attestations?

**Choices:**
- A) AWS Artifact
- B) AWS Trusted Advisor
- C) AWS Health Dashboard
- D) AWS Config

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Artifact: Provides on demand downloads of AWS security and compliance
documents (PCI, ISO, etc
---
Selected Answer: A
Artifact: Get access to compliance reports such as PCI, ISO, etc…
---
Selected Answer: A
A. AWS Artifact

</details>

---

## Question 617: CLF-C02-ET-Q617
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to create and publish interactive business intelligence dashboards. The dashboards require insights that are powered by machine learning.

Which AWS service or tool will meet these requirements?

**Choices:**
- A) AWS Glue Studio
- B) Amazon QuickSight
- C) Amazon Redshift
- D) Amazon Athena

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon QuickSight: Serverless machine learning powered business intelligence service to create interactive dashboards.
---
Selected Answer: B
B. Amazon QuickSight

</details>

---

## Question 618: CLF-C02-ET-Q618
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use AWS. The company has stringent requirements about low-latency access to on-premises systems and data residency.

Which AWS service should the company use to design a solution that meets these requirements?

**Choices:**
- A) AWS Wavelength
- B) AWS Transit Gateway
- C) AWS Ground Station
- D) AWS Outposts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Outposts
• Benefits:
• Low-latency access to on-premises systems
• Local data processing
• Data residency
• Easier migration from on-premises to the cloud
• Fully managed service
---
Selected Answer: D
D. AWS Outposts
---
D is correct. 

need help with discussion on 460 ~ 466. Thanks.

</details>

---

## Question 619: CLF-C02-ET-Q619
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company wants to make an upfront commitment for continued use of its production Amazon EC2 instances in exchange for a reduced overall cost.
Which pricing options meet these requirements with the LOWEST cost? (Choose two.)

**Choices:**
- A) Spot Instances
- B) On-Demand Instances
- C) Reserved Instances
- D) Savings Plans
- E) Dedicated Hosts

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (90%). Contributor Answer: CD.

Community Rationale & Discussion:
Selected Answer: CD
We can rule out Spot instances since this is a production environment.
So the right answers are:
C. Reserved Instances: Reserved Instances provide a significant discount (up to 75%) compared to On-Demand pricing in exchange for a one-time upfront payment and/or a lower hourly rate. The more you commit, the greater the discount.

D. Savings Plans: Savings Plans offer flexible pricing and savings on your AWS usage, with discounts of up to 72% compared to On-Demand pricing. With Savings Plans, you commit to a certain amount of usage (measured in dollars per hour) for a one- or three-year term, and receive a lower rate for that usage.
---
Selected Answer: CD
A. Spot Instances: These are spare EC2 instances available at lower prices, but they are not suitable for making upfront commitments as they are subject to termination if the capacity is needed by the system.

B. On-Demand Instances: On-Demand Instances are pay-as-you-go without upfront commitments, making them flexible but not the most cost-effective for long-term commitments.

C. Reserved Instances: Reserved Instances allow upfront commitments for a specific instance type in a particular region, offering significant cost savings compared to On-Demand Instances. They provide a lower overall cost in exchange for the commitment.

D. Savings Plans: Savings Plans provide significant cost savings in exchange for a commitment to a consistent amount of compute usage (measured in $/hr) for a 1 or 3-year period. They offer flexibility and cost savings similar to Reserved Instances.

E. Dedicated Hosts: Dedicated Hosts provide physical servers dedicated to your use. While they offer visibility and control over the placement of instances, they do not necessarily result in the lowest cost and are not based on the concept of upfront commitments for cost reduction.
---
Selected Answer: CD
Both Reserved Instances and Savings Plans allow you to make an upfront commitment for the use of EC2 instances, which results in significant cost savings compared to On-Demand Instances. However, Savings Plans tend to be more flexible than Reserved Instances, offering savings across a broader set of EC2 instance types, regions, and services.

</details>

---

## Question 620: CLF-C02-ET-Q620
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company runs an on-premises contact center for customers. The company needs to migrate to a cloud-based solution that can deliver artificial intelligence features to improve user experience.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Wavelength
- B) AWS IAM Identity Center (AWS Single Sign-On)
- C) AWS Direct Connect
- D) Amazon Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon Connect is a cloud-based customer contact center service offered by Amazon Web Services (AWS), enabling businesses to manage customer interactions through voice, chat, and email, all within a single platform
---
Selected Answer: D
Amazon Connect integrates easily with AI and machine learning features to enhance the user experience.
---
Selected Answer: D
D. Amazon Connect
Amazon Connect is a cloud-based contact center service that enables companies to provide better customer service at a lower cost. It includes built-in artificial intelligence features, such as speech recognition and sentiment analysis, to enhance the user experience. 
(D. Amazon Connect

Amazon Connect is a cloud-based contact center service that enables companies to provide better customer service at a lower cost. It includes built-in artificial intelligence features, such as speech recognition and sentiment analysis, to enhance the user experience.

</details>

---

## Question 621: CLF-C02-ET-Q621
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs the ability to acquire resources when the resources are needed. The company also needs the ability to release the resources when the resources are no longer needed.

Which AWS concept represents the company's goals?

**Choices:**
- A) Scalability
- B) Sustainability
- C) Elasticity
- D) Operational excellence

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Elasticity: The ability to acquire resources as you need them and release resources when you no longer need them. In the cloud, you want to do this automatically.
---
Selected Answer: C
C. Elasticity

</details>

---

## Question 622: CLF-C02-ET-Q622
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use Amazon EC2 instances for a stable production workload that will run for 1 year.

Which instance purchasing option meets these requirements MOST cost-effectively?

**Choices:**
- A) Dedicated Hosts
- B) Reserved Instances
- C) On-Demand Instances
- D) Spot Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Reserved Instances
Reduce your Amazon EC2 costs by making a
commitment to a consistent instance configuration, including instance
type and Region, for a term of 1 or 3 years.
---
Selected Answer: B
B. Reserved Instances

</details>

---

## Question 623: CLF-C02-ET-Q623
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to log in securely to Linux Amazon EC2 instances.

How can the company accomplish this goal?

**Choices:**
- A) Use SSH keys.
- B) Use a VPN.
- C) Use end-to-end encryption.
- D) Use Amazon Route 53.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Use SSH keys. Most secure method.
---
A. SSH keys enable the initiation of remote connectivity

</details>

---

## Question 624: CLF-C02-ET-Q624
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use a serverless compute service for an application.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Lambda
- B) AWS CloudFormation
- C) AWS Elastic Beanstalk
- D) Elastic Load Balancing

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Lambda - serverless computer service
---
Selected Answer: A
Keyword: Serverless Compute Service 

In AWS Compute categories AWS Lambda is a serverless services.

Answer is A. AWS Lambda

</details>

---

## Question 625: CLF-C02-ET-Q625
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants a solution that will automatically adjust the number of Amazon EC2 instances that are being used based on the current load.

Which AWS offering will meet these requirements?

**Choices:**
- A) Dedicated Hosts
- B) Placement groups
- C) Auto Scaling groups
- D) Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Auto Scaling groups
---
key term: automatically*

</details>

---

## Question 626: CLF-C02-ET-Q626
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is building AWS architecture to deliver real-time data feeds from an on-premises data center into an application that runs on AWS. The company needs a consistent network connection with minimal latency.

What should the company use to connect the application and the data center to meet these requirements?

**Choices:**
- A) AWS Direct Connect
- B) Public internet
- C) AWS VPN
- D) Amazon Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Direct Connect: Private dedicated connection between on premises and AWS
---
Selected Answer: A
A. AWS Direct Connect

</details>

---

## Question 627: CLF-C02-ET-Q627
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company plans to migrate its custom marketing application and order-processing application to AWS. The company needs to deploy the applications on different types of instances with various configurations of CPU, memory, storage, and networking capacity.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS Lambda
- B) Amazon Cognito
- C) Amazon Athena
- D) Amazon EC2

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon EC2
---
D is correct. 

please help discussion on 468 ~ 471. Thanks.
---
Selected Answer: D
The correct answer should be D.Amazon EC2.
Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL.
https://docs.aws.amazon.com/athena/latest/ug/what-is.html

</details>

---

## Question 628: CLF-C02-ET-Q628
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to monitor and block malicious HTTP and HTTPS requests that its Amazon CloudFront distributions receive.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon GuardDuty
- B) Amazon Inspector
- C) AWS WAF
- D) Amazon Detective

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
HTTP HTTPS deals with web so AWS WAF ez :)
---
Selected Answer: C
C. AWS WAF
---
C. AWS WAF - An AWS WAF rule defines how to inspect HTTP(S) web requests and the action to take on a request when it matches the inspection criteria. You define rules only in the context of a rule group or web ACL.

</details>

---

## Question 629: CLF-C02-ET-Q629
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS services can host PostgreSQL databases? (Choose two.)

**Choices:**
- A) Amazon S3
- B) Amazon Aurora
- C) Amazon EC2
- D) Amazon OpenSearch Service
- E) Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
• PostgreSQL and MySQL are both supported as Aurora DB
---
Selected Answer: BC
B. Amazon Aurora
C. Amazon EC2
---
"Amazon EC2 (Elastic Compute Cloud) provides scalable computing power in the cloud, making it an excellent platform for hosting databases like PostgreSQL. While managed services like Amazon RDS or Aurora offer convenience, setting up PostgreSQL on EC2 gives you complete control over your database configuration."

</details>

---

## Question 630: CLF-C02-ET-Q630
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate its on-premises relational databases to the AWS Cloud. The company wants to use infrastructure as close to its current geographical location as possible.
Which AWS service or resource should the company use to select its Amazon RDS deployment area?

**Choices:**
- A) Amazon Connect
- B) AWS Wavelength
- C) AWS Regions
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Connect: Customer service cloud contact center
AWS Wavelength: 5G devices
AWS Direct Connect: Dedicated network connection bypass public network
---
Selected Answer: C
WS Regions allow you to select the best region for your use case based on geographical location and regulatory requirements.
---
Selected Answer: C
C. AWS Regions: AWS Regions are geographical locations where AWS data centers (Availability Zones) are situated. When deploying Amazon RDS, you can choose the AWS Region that is geographically closest to your current location to reduce latency and improve performance.

</details>

---

## Question 631: CLF-C02-ET-Q631
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can generate information that can be used by external auditors?

**Choices:**
- A) Amazon Cognito
- B) Amazon FSx
- C) AWS Config
- D) Amazon Inspector

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
AWS Config: AWS service is used to track, record, and audit configuration changes made to AWS resources
---
Selected Answer: C
AWS Config
• Helps with auditing and recording compliance of your AWS resources
• Helps record configurations and changes over time
---
Selected Answer: C
C. AWS Config - provides detailed inventory

</details>

---

## Question 632: CLF-C02-ET-Q632
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature requires an internet service provider (ISP) and a colocation facility to be implemented?

**Choices:**
- A) AWS VPN
- B) Amazon Connect
- C) AWS Direct Connect
- D) Internet gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
"AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable."

</details>

---

## Question 633: CLF-C02-ET-Q633
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants its Amazon EC2 instances to operate in a highly available environment, even if there is a natural disaster in a particular geographic area.

Which solution achieves this goal?

**Choices:**
- A) Use EC2 instances in multiple AWS Regions.
- B) Use EC2 instances in multiple edge locations.
- C) Use EC2 instances in the same Availability Zone but in different AWS Regions.
- D) Use Amazon CloudFront with the EC2 instances configured as the source.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Use EC2 instances in multiple AWS Regions. - This is the best option to ensure high availability if there is a natural disaster in one geographical area.
---
A is correct. 

please help with discussion on 473~476
---
A is Correct. Question: 147

</details>

---

## Question 634: CLF-C02-ET-Q634
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service allows for file sharing between multiple Amazon EC2 instances?

**Choices:**
- A) AWS Direct Connect
- B) AWS Snowball Edge
- C) AWS Backup
- D) Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon Elastic File System (EFS) provides file storage that can be accessed concurrently from multiple Amazon EC2 instances.
---
Selected Answer: D
Keyword: File sharing between multiple Amazon EC2 instances.

If the multiple EC2 machines want to file sharing with multiple machines by using EFS(NFS)via we can do it.

Answer is D. Amazon Elastic File System(EFS)

</details>

---

## Question 635: CLF-C02-ET-Q635
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to manage multiple logins across AWS accounts within the same organization in AWS Organizations.

Which AWS service should the company use to meet this requirement?

**Choices:**
- A) Amazon VPC
- B) Amazon GuardDuty
- C) Amazon Cognito
- D) AWS IAM Identity Center

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
d is correct
---
d is correct

</details>

---

## Question 636: CLF-C02-ET-Q636
**Domain 2:** Security and Compliance  

**Question:**  
A company uses Amazon WorkSpaces.

Which task is the responsibility of AWS, according to the AWS shared responsibility model?

**Choices:**
- A) Set up multi-factor authentication (MFA) for each WorkSpaces user account.
- B) Ensure the environmental safety and security of the AWS infrastructure that hosts WorkSpaces.
- C) Provide security for WorkSpaces user accounts through AWS Identity and Access Management (IAM).
- D) Configure AWS CloudTrail to log API calls and user activity.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Ensure the environmental safety and security of the AWS infrastructure that hosts WorkSpaces.

</details>

---

## Question 637: CLF-C02-ET-Q637
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is migrating its public website to AWS. The company wants to host the domain name for the website on AWS.

Which AWS service should the company use to meet this requirement?

**Choices:**
- A) AWS Lambda
- B) Amazon Route 53
- C) Amazon CloudFront
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon Route 53
---
Selected Answer: B
Keyword: Domain Name for the website 
Route53:
Amazon Route 53 is a highly available and scalable cloud domain name system (DNS) service. Enables to customize DNS routing policies to reduce latency.

In AWS Route53 is a service to use Domain Name Service and DNS routing policies including health checks of webservers.

Answer: B. Amazon Route 53

</details>

---

## Question 638: CLF-C02-ET-Q638
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company uses a third-party identity provider (IdP). The company wants to provide its employees with access to AWS accounts and services without requiring another set of login credentials.

Which AWS service will meet this requirement?

**Choices:**
- A) AWS Directory Service
- B) Amazon Cognito
- C) AWS IAM Identity Center
- D) AWS Resource Access Manager (AWS RAM)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `76%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (76%). Contributor Answer: C.

Community Rationale & Discussion:
B. Amazon Cognito

Amazon Cognito allows you to add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. With Cognito, you can integrate with your existing third-party identity provider (IdP) through industry-standard protocols such as OpenID Connect (OIDC) and SAML 2.0.
---
Selected Answer: C
C. AWS IAM Identity Center - provides federated access, single sign on, and centralized management
---
The key is "...WITHOUT requiring another set of login credentials."

please help with discussion on 478~480. Thanks.

</details>

---

## Question 639: CLF-C02-ET-Q639
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which combination of AWS services can be used to move a commercial relational database to an Amazon-managed open-source database? (Choose two.)

**Choices:**
- A) AWS Database Migration Service (AWS DMS)
- B) AWS software development kits (SDKs)
- C) AWS Schema Conversion Tool
- D) AWS Systems Manager
- E) Amazon EMR

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
A. AWS Database Migration Service (AWS DMS) - facilitates migration of databases 
C. AWS Schema Conversion Tool - helps convert the schema from a source commercial database to a compatible schema on target open-source database

</details>

---

## Question 640: CLF-C02-ET-Q640
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service gives users on-demand, self-service access to AWS compliance control reports?

**Choices:**
- A) AWS Config
- B) Amazon GuardDuty
- C) AWS Trusted Advisor
- D) AWS Artifact

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Artifact provides access to compliance reports and AWS security on demand
---
Selected Answer: D
D. AWS Artifact

</details>

---

## Question 641: CLF-C02-ET-Q641
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is exploring the use of the AWS Cloud, and needs to create a cost estimate for a project before the infrastructure is provisioned.
Which AWS service or feature can be used to estimate costs before deployment?

**Choices:**
- A) AWS Free Tier
- B) AWS Pricing Calculator
- C) AWS Billing and Cost Management
- D) AWS Cost and Usage Report

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. AWS Free Tier: The AWS Free Tier provides limited free access to a range of AWS services for 12 months after signing up for an AWS account. It is not specifically designed for creating detailed cost estimates for a project.

B. AWS Pricing Calculator: The AWS Pricing Calculator is a tool that allows users to estimate the cost of using AWS services based on their projected usage. It provides a detailed breakdown of costs for different services and configurations.

C. AWS Billing and Cost Management: AWS Billing and Cost Management provides tools for monitoring, analyzing, and controlling costs. While it helps manage costs, it is not primarily a tool for creating cost estimates before deployment.

D. AWS Cost and Usage Report: The AWS Cost and Usage Report provides comprehensive data about your AWS costs. It is useful for analyzing historical costs but may not be as suitable for creating upfront cost estimates before infrastructure deployment.
---
Selected Answer: B
WS Pricing Calculator is a tool that allows users to estimate costs for their AWS infrastructure before deployment. It helps in building a detailed estimate based on specific services, configurations, and usage patterns. This service is especially useful for understanding potential costs of an AWS project based on its architecture and resource needs.
---
Selected Answer: B
B. AWS Pricing Calculator

</details>

---

## Question 642: CLF-C02-ET-Q642
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company runs a legacy workload in an on-premises data center. The company wants to migrate the workload to AWS. The company does not want to make any changes to the workload.

Which migration strategy should the company use?

**Choices:**
- A) Repurchase
- B) Replatform
- C) Rehost
- D) Refactor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Rehosting (lift and shift) is the process of migrating your on-premises application to the cloud without modifying it
---
Selected Answer: C
C. Rehost - migrating, but not making any changes
---
Rehosting, also known as "lift and shift," is the migration strategy where you move an existing workload from on-premises to AWS without making any changes to the application itself. This strategy is the most suitable when the company does not want to modify the workload but needs to move it to the cloud for reasons such as scalability, cost savings, or resource optimization.

</details>

---

## Question 643: CLF-C02-ET-Q643
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate applications to the AWS Cloud. During a system audit, the company finds that its content management system (CMS) application is incompatible with cloud environments.

Which migration strategies will help the company to migrate the CMS application with the LEAST effort? (Choose two.)

**Choices:**
- A) Retire
- B) Rehost
- C) Repurchase
- D) Replatform
- E) Refactor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `43%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (43%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
It's not (E) Refactor, requiring significant development effort and increased migration timelines. 

I don't think (A) Retire is an option only because the question states which strategies will help the company migrate the CMS application with the LEAST effort. Choosing to Retire will not help them migrate.

This leaves us with Rehost, Repurchase, and Replatform. Based on the following and a process of elimination, my choices would be B and C.

B) Rehost - Benefits: Rapid migration, minimal code changes, reduced risk. May not fully leverage cloud-native features, potential for suboptimal cost and performance.

C) Repurchase - Benefits: Rapid migration, reduced maintenance burden, potential for cost savings. Limited customization, potential for data migration challenges.

D) Replatform - Benefits: Balance of speed and optimization, leverage cloud benefits. Requires careful planning, potential for increased complexity.
---
Selected Answer: BD
The two migration strategies that will help the company migrate the CMS application with the LEAST effort are:
B. Rehost
D. Replatform

Explanation:
Rehost (Lift-and-Shift):
This strategy involves moving the application to the cloud with minimal or no changes. 

Replatform (Lift-Tinker-and-Shift):
This strategy involves making minor optimizations to the application to make it compatible with the cloud environment.

Why not the other options?
A. Retire: This means decommissioning the application, which is not applicable here since the company wants to migrate the CMS.
C. Repurchase: This involves switching to a different product (e.g., a SaaS CMS). While it may reduce effort in some cases, it is not necessarily the least effort if the company wants to retain its existing CMS.
E. Refactor: This involves re-architecting the application to be cloud-native, which requires significant effort and is not the least effort option.
---
Selected Answer: BC
Repurchase “drop and shop”
• Moving to a different product while moving to the Cloud
• Often you move to a SaaS platform
• Expensive in the short term, but quick to deploy
• Example: CRM to Salesforce.com, HR to Workday, CMS to Drupal

</details>

---

## Question 644: CLF-C02-ET-Q644
**Domain 2:** Security and Compliance  

**Question:**  
Which of the following are AWS best practice recommendations for the use of AWS Identity and Access Management (IAM)? (Choose two.)

**Choices:**
- A) Use the AWS account root user for daily access.
- B) Use access keys and secret access keys on Amazon EC2.
- C) Rotate credentials on a regular basis.
- D) Create a shared set of access keys for system administrators.
- E) Configure multi-factor authentication (MFA).

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CE (100%). Contributor Answer: CE.

Community Rationale & Discussion:
Selected Answer: CE
C. Rotate credentials on a regular basis.
E. Configure multi-factor authentication (MFA).

</details>

---

## Question 645: CLF-C02-ET-Q645
**Domain 2:** Security and Compliance  

**Question:**  
Which option is AWS responsible for under the AWS shared responsibility model?

**Choices:**
- A) Network and firewall configuration
- B) Client-side data encryption
- C) Management of user permissions
- D) Hardware and infrastructure

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Answer is D
---
Selected Answer: D
D is correct

</details>

---

## Question 646: CLF-C02-ET-Q646
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run a graph query that provides credit card users’ names, addresses, and transactions. The company wants the graph to show if the names, addresses, and transactions indicates possible fraud.

Which AWS database service will meet these requirements?

**Choices:**
- A) Amazon DocumentDB (with MongoDB compatibility)
- B) Amazon Timestream
- C) Amazon DynamoDB
- D) Amazon Neptune

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon Neptune is Fully Managed NoSQL graph database that can store, map and query relationships between data sets.
---
Selected Answer: D
D. Amazon Neptune - this is a fully managed graph database service
---
Answer is D Amazon Neptune : Build/Run apps that work with highly connected data sets like fraud detection ,knowledge graph and recommendation engine

</details>

---

## Question 647: CLF-C02-ET-Q647
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides machine learning capability to detect and analyze content in images and videos?

**Choices:**
- A) Amazon Connect
- B) Amazon Lightsail
- C) Amazon Personalize
- D) Amazon Rekognition

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Recognition: image and video analysis, face detection, labeling, celebrity
recognition.
---
Selected Answer: D
Amazon Rekognition
• Find objects, people, text, scenes in images and videos using ML
---
Selected Answer: D
D. Amazon Rekognition

</details>

---

## Question 648: CLF-C02-ET-Q648
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants its AWS usage to be more sustainable. The company wants to track, measure, review, and forecast polluting emissions that result from its AWS applications.

Which AWS service or tool can the company use to meet these requirements?

**Choices:**
- A) AWS Health Dashboard
- B) AWS customer carbon footprint tool
- C) AWS Support Center
- D) Amazon QuickSight

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Customer carbon footprint tool to view estimates of the carbon emissions associated with your AWS products and services.
---
Dawg this isn't even on the exam objectives
---
Selected Answer: B
https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/

</details>

---

## Question 649: CLF-C02-ET-Q649
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service gives users the ability to deploy highly repeatable infrastructure configurations?

**Choices:**
- A) AWS CloudFormation
- B) AWS CodeDeploy
- C) AWS CodeBuild
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS CloudFormation is a service that allows you to model and manage your AWS resources using infrastructure-as-code (IaC) templates, enabling automated and predictable infrastructure provisioning and management
---
Selected Answer: A
A. AWS CloudFormation
---
highly repeatable infrastructure = CloudFormation templates

</details>

---

## Question 650: CLF-C02-ET-Q650
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to provide customer service by using voice calls and web chat features.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) Amazon Aurora
- B) Amazon Connect
- C) Amazon WorkSpaces
- D) AWS Organizations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon Connect:
• Receive calls, create contact flows, cloud-based virtual contact center
---
Selected Answer: B
B. Amazon Connect - fully managed cloud contact center service
---
B. Amazon Connect

Amazon Connect is a cloud-based contact center service that offers capabilities for voice calls, chat, and other customer interactions, making it suitable for customer service operations.

</details>

---

## Question 651: CLF-C02-ET-Q651
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is designed to help users handle large amounts of data in a data warehouse environment?

**Choices:**
- A) Amazon RDS
- B) Amazon DynamoDB
- C) Amazon Redshift
- D) Amazon Aurora

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Redshift is OLAP online analytical processing (analytics and data warehousing)
---
Selected Answer: C
C. Amazon Redshift - data warehouse
---
Answer C : Redshift 
Fully-managed data warehouse service and is more suitable for complex analytics and large-scale data warehousing scenarios.

</details>

---

## Question 652: CLF-C02-ET-Q652
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is building an application that needs to deliver images and videos globally with minimal latency.
Which approach can the company use to accomplish this in a cost effective manner?

**Choices:**
- A) Deliver the content through Amazon CloudFront.
- B) Store the content on Amazon S3 and enable S3 cross-region replication.
- C) Implement a VPN across multiple AWS Regions.
- D) Deliver the content through AWS PrivateLink.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Deliver the content through Amazon CloudFront: Amazon CloudFront is a content delivery network (CDN) service that accelerates the delivery of static and dynamic content, including images and videos, to users globally. It helps minimize latency by caching content at edge locations worldwide.

B. Store the content on Amazon S3 and enable S3 cross-region replication: While Amazon S3 provides durable and scalable storage for objects, enabling cross-region replication in S3 is primarily for data redundancy and disaster recovery, not for minimizing latency globally.

C. Implement a VPN across multiple AWS Regions: Virtual Private Network (VPN) connections are used for secure communication between networks.

D. Deliver the content through AWS PrivateLink: AWS PrivateLink enables private connectivity between VPCs (Virtual Private Clouds) and services.
---
Selected Answer: A
Amazon CloudFront is a Content Delivery Network (CDN) service that distributes content globally with low latency by caching content in edge locations closer to users. CloudFront automatically delivers content such as images, videos, and other web assets quickly and efficiently, minimizing latency for users around the world. This makes it a cost-effective solution for delivering content globally with minimal latency.
---
Selected Answer: A
option A - Deliver it through Cloudfront

</details>

---

## Question 653: CLF-C02-ET-Q653
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is building a web application using AWS.

Which AWS service will help prevent network layer DDoS attacks against the web application?

**Choices:**
- A) AWS WAF
- B) AWS Firewall Manager
- C) Amazon GuardDuty
- D) AWS Shield

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
AWS Shield to protect from DDoS attacks
---
Selected Answer: D
D. AWS Shield - helps prevent DDoS attacks
---
"AWS WAF is a web application firewall service that helps protect your web apps from common exploits that could affect app availability, compromise security, or consume excessive resources. AWS Shield provides expanded DDoS attack protection for your AWS resources."

</details>

---

## Question 654: CLF-C02-ET-Q654
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS compute service gives users the ability to securely and reliably run containers at scale?

**Choices:**
- A) Amazon Elastic Container Service (Amazon ECS)
- B) Amazon Aurora
- C) Amazon Athena
- D) Amazon Polly

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications

</details>

---

## Question 655: CLF-C02-ET-Q655
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS tool or feature acts as a VPC firewall at the subnet level?

**Choices:**
- A) Security group
- B) Network ACL
- C) Traffic Mirroring
- D) Internet gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
NACL (Network ACL)
• A firewall which controls traffic from and to
subnet
• Can have ALLOW and DENY rules
• Are attached at the Subnet level
• Rules only include IP addresses
---
Selected Answer: B
B. Network ACL - "subnet" is key here. Network Access Control Lists "ACLs" are stateless and operate at the subnet level. They evaluate both incoming and outgoing traffic.

</details>

---

## Question 656: CLF-C02-ET-Q656
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company runs an application on AWS that performs batch jobs. The application is fault-tolerant and can handle interruptions. The company wants to optimize the cost to run the application.

Which AWS offering will meet these requirements?

**Choices:**
- A) Amazon Macie
- B) Amazon Neptune
- C) Amazon EC2 Spot Instances
- D) Amazon EC2 On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon EC2 Spot Instances - spot instances are the best for getting the most bang for your buck if your applications are fault tolerant and can handle interruptions.

</details>

---

## Question 657: CLF-C02-ET-Q657
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service can be used to send alerts when a specific Amazon CloudWatch alarm is invoked?

**Choices:**
- A) AWS CloudTrail
- B) Amazon Simple Notification Service (Amazon SNS)
- C) Amazon Simple Queue Service (Amazon SQS)
- D) Amazon EventBridge

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
CloudWatch:
• Metrics: monitor the performance of AWS services and billing metrics
• Alarms: automate notification, perform EC2 action, notify to SNS based on metric
• Logs: collect log files from EC2 instances, servers, Lambda functions…
• Events (or EventBridge): react to events in AWS, or trigger a rule on a schedule
---
Selected Answer: B
B. Amazon Simple Notification Service (Amazon SNS) - allows you to send notifications, emails, and alerts to various endpoints. You can configure the triggered CloudWatch alarm to send a notification to the SNS topic, which then forwards the alert to the relevant recipients.

</details>

---

## Question 658: CLF-C02-ET-Q658
**Domain 3:** Cloud Technology and Services  

**Question:**  
A cloud practitioner wants to use a highly available and scalable DNS service for its AWS workload.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Route 53
- B) Amazon Lightsail
- C) AWS Amplify Hosting
- D) Amazon S3

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon Route 53 - when you see DNS and AWS, think Route 53!

</details>

---

## Question 659: CLF-C02-ET-Q659
**Domain 2:** Security and Compliance  

**Question:**  
According to the AWS shared responsibility model, which task is the customer's responsibility?

**Choices:**
- A) Maintaining the infrastructure needed to run AWS Lambda
- B) Updating the operating system of Amazon DynamoDB instances
- C) Maintaining Amazon S3 infrastructure
- D) Updating the guest operating system on Amazon EC2 instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Updating the guest operating system on Amazon EC2 instances
---
D is the correct answer
---
Selected Answer: D
D is Correct Answer

</details>

---

## Question 660: CLF-C02-ET-Q660
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is learning about its responsibilities that are related to the management of Amazon EC2 instances.

Which tasks for EC2 instances are the company’s responsibility, according to the AWS shared responsibility model? (Choose two.)

**Choices:**
- A) Install and patch the machine hypervisor.
- B) Patch the guest operating system.
- C) Encrypt data at rest on associated storage.
- D) Install the physical hardware and cabling.
- E) Provide physical security for the EC2 instances.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (100%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
Sounds about right
---
Selected Answer: BC
B. Patch the guest operating system.
C. Encrypt data at rest on associated storage.

</details>

---

## Question 661: CLF-C02-ET-Q661
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company runs MySQL database workloads on self-managed servers in an on-premises data center. The company wants to migrate the database workloads to an AWS managed service.

Which migration strategy should the company use?

**Choices:**
- A) Rehost
- B) Repurchase
- C) Refactor
- D) Replatform

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Replatform “lift and reshape”
• Example: migrate your database to RDS
• Example: migrate your application to Elastic Beanstalk
• Not changing the core architecture, but leverage some Cloud optimizations
• Save time and money by moving to a fully managed service or Serverless
---
Selected Answer: D
D. Replatform - a few adjustments will have to be made, so replatforming is the right answer vs rehosting.
---
D is correct. 

please help with discussion on 500 503 ~ 511. Thanks.

</details>

---

## Question 662: CLF-C02-ET-Q662
**Domain 2:** Security and Compliance  

**Question:**  
Which option is a customer responsibility when using Amazon DynamoDB under the AWS Shared Responsibility Model?

**Choices:**
- A) Physical security of DynamoDB
- B) Patching of DynamoDB
- C) Access to DynamoDB tables
- D) Encryption of data at rest in DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (88%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
based on docs, AWS DynamoDB is automatically encrypted your data as default (but RDS you must turn on this feature by your self)
ref: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html
ref: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.Determining
---
Under the AWS Shared Responsibility Model, the customer's responsibilities when using Amazon DynamoDB include:

C. Access to DynamoDB tables

The customer is responsible for managing and controlling access to their DynamoDB tables. This includes defining appropriate permissions, user access control, and authentication mechanisms to ensure that only authorized users or services can access the tables.

The other options are not customer responsibilities:

D. Encryption of data at rest in DynamoDB: AWS provides encryption of data at rest as a built-in feature for DynamoDB. The customer can enable encryption for their tables, but AWS handles the actual implementation and management of the encryption process.

Therefore, the correct customer responsibility is C. Access to DynamoDB tables.
---
Selected Answer: C
Maintaining access to Dynamo DB tables

</details>

---

## Question 663: CLF-C02-ET-Q663
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which option is a benefit of the economies of scale based on the advantages of cloud computing?

**Choices:**
- A) The ability to trade variable expense for fixed expense
- B) Increased speed and agility
- C) Lower variable costs over fixed costs
- D) Increased operational costs across data centers

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (91%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Economies of scale refer to the cost advantages that a business can achieve by increasing its scale of production or operations. In other words, as a company produces more units of a good or service, its average cost of production per unit decreases. This cost reduction occurs because fixed costs are spread over a larger number of units, leading to increased operational efficiency and cost efficiency.

A. The ability to trade variable expense for fixed expense: Cloud computing, in general, provides the advantage of paying for resources on a variable (pay-as-you-go) basis rather than a fixed, upfront expense.

B. Increased speed and agility: While increased speed and agility are benefits of cloud computing, they are not specifically related to the economies of scale. 

C. Lower variable costs over fixed costs: This is a key benefit of economies of scale. With cloud computing, as usage increases, the cost per unit of resources tends to decrease due to the efficiency gained from large-scale operations.

D. Increased operational costs across data centers: Increased operational costs across data centers would be contrary to the benefits of economies of scale.
---
Selected Answer: C
C. Lower variable costs over fixed costs
---
C , economies scale speaks for itself

</details>

---

## Question 664: CLF-C02-ET-Q664
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
A company is assessing its AWS Business Support plan to determine if the plan still meets the company’s needs. The company is considering switching to AWS Enterprise Support.
Which additional benefit will the company receive with AWS Enterprise Support?

**Choices:**
- A) A full set of AWS Trusted Advisor checks
- B) Phone, email, and chat access to cloud support engineers 24 hours a day, 7 days a week
- C) A designated technical account manager (TAM) to assist in monitoring and optimization
- D) A consultative review and architecture guidance for the company’s applications

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `56%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (56%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: D
D is the correct answer. Everyone that is selecting C is not reading the full answer for C correctly. It says that the TAM is for monitoring and optimization. However, if you go to the AWS page that lists the differences between the plans (https://aws.amazon.com/premiumsupport/plans/), you'll see that the TAM is actually for Architectural and Operational guidance, NOT monitoring and optimization.

Here's the text from that page: "Designated Technical Account Manager (TAM) to provide consultative architectural and operational guidance delivered in the context of your applications and use-cases to help you achieve the greatest value from AWS"
---
Selected Answer: D
It comes down to C and D because the additional benefit is going to be a TAM. Im going to go with D though, because it defines what a TAM does. A designated TAM provides consultative architectural and operational guidance tailored to your applications and use cases.
---
Selected Answer: C
A designated technical account manager (TAM) to assist in monitoring and optimization

</details>

---

## Question 665: CLF-C02-ET-Q665
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which pricing model will interrupt a running Amazon EC2 instance if capacity becomes temporarily unavailable?

**Choices:**
- A) On-Demand Instances
- B) Standard Reserved Instances
- C) Spot Instances
- D) Convertible Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Spot Instances
---
Selected Answer: C
C. Spot Instances is correct
---
Spot instance

</details>

---

## Question 666: CLF-C02-ET-Q666
**Domain 2:** Security and Compliance  

**Question:**  
Which options are AWS Cloud Adoption Framework (AWS CAF) security perspective capabilities? (Choose two.)

**Choices:**
- A) Observability
- B) Incident and problem management
- C) Incident response
- D) Infrastructure protection
- E) Availability and continuity

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (100%). Contributor Answer: CD.

Community Rationale & Discussion:
Selected Answer: CD
C. Incident response
D. Infrastructure protection
---
The Key words is response and Infrastructure
---
Selected Answer: CD
C. Incident response
D. Infrastructure protection

</details>

---

## Question 667: CLF-C02-ET-Q667
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to run its workload on Amazon EC2 instances for more than 1 year. This workload will run continuously.

Which option offers a discounted hourly rate compared to the hourly rate of On-Demand Instances?

**Choices:**
- A) AWS Graviton processor
- B) Dedicated Hosts
- C) EC2 Instance Savings Plans
- D) Amazon EC2 Auto Scaling instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. EC2 Instance Savings Plans
---
Selected Answer: C
C. EC2 Instance Savings Plans
---
Selected Answer: C
C - Savings plan

</details>

---

## Question 668: CLF-C02-ET-Q668
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which characteristic of the AWS Cloud helps users eliminate underutilized CPU capacity?

**Choices:**
- A) Agility
- B) Elasticity
- C) Reliability
- D) Durability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A. Agility refers to the ability to rapidly develop, test, and launch software applications
B. Elasticity allows users to scale computing resources up or down automatically, according to actual needs
C. Reliability ensures that computing resources are available when needed
D. Durability concerns the protection and longevity of data
---
Selected Answer: B
The characteristic of the AWS Cloud that helps users eliminate underutilized CPU capacity is elasticity. Elasticity allows users to scale their computing resources up or down based on their needs, which helps to eliminate underutilized CPU capacity.
---
Selected Answer: B
Technically would be Optimization but thats not an answer choice here

</details>

---

## Question 669: CLF-C02-ET-Q669
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate a monolithic application to AWS. The company wants to modernize the application by splitting it into microservices. The company will deploy the microservices on AWS.

Which migration strategy should the company use?

**Choices:**
- A) Rehost
- B) Repurchase
- C) Replatform
- D) Refactor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Refactor—modifying applications to better support the cloud environment.
---
Selected Answer: D
D. Refactor - the application is being redesigned and modernized.
---
Refactoring (also known as re-architecting) is the process of significantly modifying an application’s architecture to improve its functionality, scalability, or maintainability

</details>

---

## Question 670: CLF-C02-ET-Q670
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to implement detailed tracking of its cloud costs by department and project.

Which AWS feature or service should the company use?

**Choices:**
- A) Consolidated billing
- B) Cost allocation tags
- C) AWS Marketplace
- D) AWS Budgets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Cost allocation tags
---
Selected Answer: B
key words detailed tracking by department and project.
---
Answer is B: 
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html

</details>

---

## Question 671: CLF-C02-ET-Q671
**Domain 3:** Cloud Technology and Services  

**Question:**  
A user wants to invoke an AWS Lambda function when an Amazon EC2 instance enters the “stopping” state.

Which AWS service is appropriate for this use case?

**Choices:**
- A) Amazon EventBridge
- B) AWS Config
- C) Amazon Simple Notification Service (Amazon SNS)
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon EventBridge - allows you to set up event-driven workflows based on state changes of resources
---
EventBridge is for event-driven cases
---
A is correct

please help with discussion on 503 ~ 511

</details>

---

## Question 672: CLF-C02-ET-Q672
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has a MariaDB database on premises. The company wants to move the data to the AWS Cloud.

Which AWS service will host this database with the LEAST amount of operational overhead?

**Choices:**
- A) Amazon RDS
- B) Amazon Neptune
- C) Amazon S3
- D) Amazon DynamoDB

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon RDS- supports MariaDB and can be migrated with minimal changes. RDS takes care of most management tasks such as software patching, failover, and scaling.
---
Selected Answer: A
Amazon RDS Is a service that enables you to run a relational Database in the AWS cloud 
It is a managed service that automates tasks as HW provisioning, DB setup, patching and backups

</details>

---

## Question 673: CLF-C02-ET-Q673
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service or feature supports governance, compliance, and risk auditing of AWS accounts?

**Choices:**
- A) Multi-factor authentication (MFA)
- B) AWS Lambda
- C) Amazon Simple Notification Service (Amazon SNS)
- D) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS CloudTrail
---
'AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.'

</details>

---

## Question 674: CLF-C02-ET-Q674
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS Cloud design principle is a company using when the company implements AWS CloudTrail?

**Choices:**
- A) Activate traceability.
- B) Use serverless compute architectures.
- C) Perform operations as code.
- D) Go global in minutes.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Activate traceability.
---
A. Activate traceability

</details>

---

## Question 675: CLF-C02-ET-Q675
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs a threat detection service that will continuously monitor its AWS accounts, workloads, and Amazon S3 buckets for malicious activity and unauthorized behavior.

Which AWS service meets these requirements?

**Choices:**
- A) AWS Shield
- B) AWS Firewall Manager
- C) Amazon GuardDuty
- D) Amazon Inspector

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon GuardDuty
---
Selected Answer: C
Answer is C
---
Selected Answer: C
C. Amazon GuardDuty

Amazon GuardDuty is a threat detection service that continuously monitors your AWS environment for malicious activity and unauthorized behavior, providing actionable security findings to help you protect your AWS resources.

</details>

---

## Question 676: CLF-C02-ET-Q676
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is planning to migrate to the AWS Cloud. The company is conducting organizational transformation and wants to become more responsive to customer inquiries and feedback.

Which task should the company perform to meet these requirements, according to the AWS Cloud Adoption Framework (AWS CAF)?

**Choices:**
- A) Realign teams to focus on products and value streams.
- B) Create new value propositions with new products and services.
- C) Use a new data and analytics platform to create actionable insights.
- D) Migrate and modernize legacy infrastructure.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Realign teams to focus on products and value streams.
---
According to the AWS Cloud Adoption Framework (AWS CAF), an organization undergoing cloud migration should focus on optimizing people, processes, and technology to enhance customer responsiveness. The People Perspective of the AWS CAF emphasizes that aligning teams to focus on products and value streams is essential for increasing agility, reducing time-to-market, and improving customer responsiveness. By organizing teams around customer-focused products or services, the company can respond more effectively to customer inquiries and feedback.
---
Answer is A.
Organization - Reimagine how your business and technology teams create customer value and meet your strategic intent. Organizing your teams around products and value streams while leveraging agile methods to rapidly iterate and evolve will help you become more responsive and customer centric.

</details>

---

## Question 677: CLF-C02-ET-Q677
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to rightsize its Amazon EC2 instances.

Which configuration change will meet this requirement with the LEAST operational overhead?

**Choices:**
- A) Add EC2 instances in another Availability Zone.
- B) Change the size and type of the EC2 instances based on utilization.
- C) Convert the payment method from On-Demand to Savings Plans.
- D) Reprovision the EC2 instances with a larger instance type.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Change the size and type of the EC2 instances based on utilization.
---
B. Change the size and type of the EC2 instances based on utilization.

</details>

---

## Question 678: CLF-C02-ET-Q678
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service supports user sign-up functionality and authentication to mobile and web applications?

**Choices:**
- A) Amazon Cognito
- B) AWS Config
- C) Amazon GuardDuty
- D) AWS Systems Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon Cognito - service that provides user sign-up, sign-in, and access control for web and mobile apps.
---
Keyword is Sign-In Web and Mobile Apps

AWS Congnito — Quick and Easy User Sign-Up, Sign-In, and Access Control to Your Web and Mobile Apps.

Answer is Amazon Cognito

</details>

---

## Question 679: CLF-C02-ET-Q679
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which of the following is a software development framework that a company can use to define cloud resources as code and provision the resources through AWS CloudFormation?

**Choices:**
- A) AWS CLI
- B) AWS Developer Center
- C) AWS Cloud Development Kit (AWS CDK)
- D) AWS CodeStar

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C. AWS Cloud Development Kit (AWS CDK)

AWS CDK is a software development framework that enables developers to define infrastructure as code (IaC) using familiar programming languages like TypeScript, Python, Java, C#, and more. With AWS CDK, you can define cloud resources, their relationships, and provisioning logic in your preferred programming language. AWS CDK also generates CloudFormation templates based on your code, making it easier to manage and deploy infrastructure resources in AWS.
---
Selected Answer: C
A. AWS CLI (Command Line Interface): A command-line tool that allows users to interact with AWS services using commands. While it is a useful tool for managing AWS resources, it is not specifically designed for defining cloud resources as code or provisioning resources through AWS CloudFormation.

B. AWS Developer Center: There is no specific service or tool named "AWS Developer Center" in the AWS ecosystem. It might refer to general resources or documentation for developers.

C. AWS Cloud Development Kit (AWS CDK): A software development framework for defining cloud infrastructure as code (IaC) and provisioning resources using familiar programming languages. It allows developers to use programming languages such as Python, TypeScript, or Java to define AWS infrastructure, making it easier to manage and provision resources.

D. AWS CodeStar: A fully managed service for quickly developing, building, and deploying applications on AWS. While it includes features for continuous integration and deployment, it is not primarily focused on defining cloud resources as code using a framework like AWS CloudFormation.
---
Selected Answer: C
The AWS Cloud Development Kit (AWS CDK) is a software development framework that allows developers to define cloud resources using familiar programming languages (such as Python, JavaScript, TypeScript, Java, and C#). With AWS CDK, developers can define infrastructure in code, and then use AWS CloudFormation to provision and manage those resources

</details>

---

## Question 680: CLF-C02-ET-Q680
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which benefit of the AWS Cloud helps companies achieve lower usage costs because of the aggregate usage of all AWS users?

**Choices:**
- A) No need to guess capacity
- B) Ability to go global in minutes
- C) Economies of scale
- D) Increased speed and agility

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Economies of scale
---
Economies of scale is a key benefit of the AWS Cloud that allows companies to achieve lower costs due to the vast aggregate usage across all AWS customers. AWS can buy and operate infrastructure at a massive scale, which reduces per-unit costs and allows AWS to pass these savings on to customers. This leads to lower prices for cloud services compared to what individual companies might pay for their own infrastructure.

</details>

---

## Question 681: CLF-C02-ET-Q681
**Domain 2:** Security and Compliance  

**Question:**  
Which task is the responsibility of the customer, according to the AWS shared responsibility model?

**Choices:**
- A) Patch the Amazon DynamoDB operating system.
- B) Secure Amazon CloudFront edge locations by allowing physical access according to the principle of least privilege.
- C) Protect the hardware that runs AWS services.
- D) Use AWS Identity and Access Management (IAM) according to the principle of least privilege.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D is correct answer
---
Selected Answer: D
D. Use AWS Identity and Access Management (IAM) according to the principle of least privilege. 

All other answers are the responsibilities of AWS.

</details>

---

## Question 682: CLF-C02-ET-Q682
**Domain 2:** Security and Compliance  

**Question:**  
A company wants to manage its cloud resources by using infrastructure as code (IaC) templates. The company needs to meet compliance requirements.

Which AWS service should the company use to meet these requirements?

**Choices:**
- A) AWS Artifact
- B) AWS Resource Explorer
- C) AWS License Manager
- D) AWS Service Catalog

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS Service Catalog
---
AWS Service Catalog allows organizations to create, manage, and distribute approved collections of cloud resources, referred to as products. It helps organizations enforce compliance requirements by ensuring that only compliant, pre-approved infrastructure templates (e.g., AWS CloudFormation templates) are available for deployment. By using AWS Service Catalog, the company can standardize resource provisioning and enforce consistent configurations that align with its compliance requirements.
---
Selected Answer: D
Answer is D:

https://aws.amazon.com/servicecatalog/
AWS Service Catalog lets you centrally manage your cloud resources to achieve governance at scale of your infrastructure as code (IaC) templates, written in CloudFormation or Terraform configurations. With AWS Service Catalog, you can meet your compliance requirements while making sure your customers can quickly deploy the cloud resources they need.

</details>

---

## Question 683: CLF-C02-ET-Q683
**Domain 3:** Cloud Technology and Services  

**Question:**  
A systems administrator wants to monitor the CPU utilization of a company's Amazon EC2 instances.

Which AWS service can provide this information?

**Choices:**
- A) AWS Config
- B) AWS Trusted Advisor
- C) AWS CloudTrail
- D) Amazon CloudWatch

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon CloudWatch coz is real time monitor.
---
Selected Answer: D
D. Amazon CloudWatch
---
Cloudwatch is correct. 

Please help with discussion on 514 ~ 519. Thanks.

</details>

---

## Question 684: CLF-C02-ET-Q684
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to migrate all of its on-premises infrastructure to the AWS Cloud. Before migration, the company wants estimate of costs for running its as-is infrastructure.

Which AWS service or principle should the company use to meet this requirement?

**Choices:**
- A) AWS Pricing Calculator
- B) AWS Well-Architected Framework
- C) AWS shared responsibility model
- D) AWS Cloud Adoption Framework (AWS CAF)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Pricing Calculator - tool to estimate costs of running workloads on AWS based on the company's current infrastructure.

</details>

---

## Question 685: CLF-C02-ET-Q685
**Domain 3:** Cloud Technology and Services  

**Question:**  
An independent software vendor wants to deliver and share its custom Amazon Machine Images (AMIs) to prospective customers.

Which AWS service will meet these requirements?

**Choices:**
- A) AWS Marketplace
- B) AWS Data Exchange
- C) Amazon EC2
- D) AWS Organizations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. AWS Marketplace - place for independent vendors to sell and distribute their software products, such as custom AMIs.
---
Selected Answer: A
By default AMI is given by AWS,If suppose you want any other OS or Third party OS means,you can go to AWS market place and purchase and use
---
Selected Answer: A
deliver is a Keyword

</details>

---

## Question 686: CLF-C02-ET-Q686
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which component must be attached to a VPC to enable inbound internet access?

**Choices:**
- A) NAT gateway
- B) VPC endpoint
- C) VPN connection
- D) Internet gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Internet gateway
---
Selected Answer: D
internet getaway ==> in
NAT-gateway ==> out

</details>

---

## Question 687: CLF-C02-ET-Q687
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service supports a company's ability to treat infrastructure as code?

**Choices:**
- A) AWS CodeDeploy
- B) AWS Elastic Beanstalk
- C) Amazon API Gateway
- D) AWS CloudFormation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. AWS CloudFormation

</details>

---

## Question 688: CLF-C02-ET-Q688
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is building an application that will receive millions of database queries each second. The company needs the data store for the application to scale to meet these needs.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon DynamoDB
- B) AWS Cloud9
- C) Amazon ElastiCache for Memcached
- D) Amazon Neptune

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon DynamoDB
---
Amazon DynamoDB is a fully managed, serverless, key-value and document database designed to handle high-performance workloads and scale to meet millions of requests per second. It automatically scales to accommodate large numbers of queries and offers features like DynamoDB Accelerator (DAX) to further enhance read performance, making it an excellent choice for applications that require high throughput and low latency.
---
A. DynamoDB offers a fast persistent key–value datastore with built-in support for replication, autoscaling, encryption at rest, and on-demand backup among other features.

</details>

---

## Question 689: CLF-C02-ET-Q689
**Domain 3:** Cloud Technology and Services  

**Question:**  
An AWS user wants to proactively detect when an instance or account might be compromised or if there are threats from attacks.

Which AWS service should the user choose?

**Choices:**
- A) Amazon GuardDuty
- B) AWS WAF
- C) AWS Shield
- D) Amazon Inspector

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon GuardDuty - threat detection service that continuously monitors your AWS environment.
---
key word: threats*

</details>

---

## Question 690: CLF-C02-ET-Q690
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company is developing an application that uses multiple AWS services. The application needs to use temporary, limited-privilege credentials for authentication with other AWS APIs.
Which AWS service or feature should the company use to meet these authentication requirements?

**Choices:**
- A) Amazon API Gateway
- B) IAM users
- C) AWS Security Token Service (AWS STS)
- D) IAM instance profiles

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon API Gateway: While API Gateway is used for creating, publishing, maintaining, monitoring, and securing APIs, it doesn't directly provide temporary credentials for authentication.

 IAM Users: IAM users are long-term credentials associated with specific users or applications. They are not designed for temporary access and are not suitable for the described use case.

 AWS Security Token Service (AWS STS): AWS STS is the correct choice for providing temporary, limited-privilege credentials. It enables you to request temporary credentials with a specific set of permissions (via roles), which can be used to authenticate with other AWS services. This is commonly used for scenarios where you need to grant temporary access to resources without exposing long-term credentials.

 IAM Instance Profiles: IAM instance profiles are used for providing AWS Identity and Access Management (IAM) roles to EC2 instances. While they are related to IAM roles, they are specific to EC2 instances and may not be the most suitable option for non-EC2 services in this scenario. AWS STS is a more generic and flexible solution for temporary credential requirements.
---
Selected Answer: C
AWS Security Token Service (AWS STS) is a service that enables the creation of temporary, limited-privilege credentials for AWS resources. It is used for scenarios where you need to authenticate API requests with temporary credentials that are valid for a specific duration and are assigned limited permissions.
---
Selected Answer: C
AWS Security Token Service (AWS STS): AWS STS is the correct choice for providing temporary, limited-privilege credentials. It enables you to request temporary credentials with a specific set of permissions (via roles), which can be used to authenticate with other AWS services. This is commonly used for scenarios where you need to grant temporary access to resources without exposing long-term credentials.

</details>

---

## Question 691: CLF-C02-ET-Q691
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which AWS Support plan provides the full set of AWS Trusted Advisor checks at the LOWEST cost?

**Choices:**
- A) AWS Developer Support
- B) AWS Business Support
- C) AWS Enterprise On-Ramp Support
- D) AWS Enterprise Support

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `90%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (90%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
https://www.scaler.com/topics/aws/aws-support-plans/
---
Selected Answer: B
AWS Business Support - Access to full set of Trusted Advisor checks
---
Selected Answer: B
B. AWS Business Support - Developer Support does not provide full set of Trusted Advisor checks

</details>

---

## Question 692: CLF-C02-ET-Q692
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company's application is running on Amazon EC2 instances. The company is planning a partial migration to a serverless architecture in the next year and wants to pay for resources up front.

Which AWS purchasing option will optimize the company's costs?

**Choices:**
- A) Convertible Reserved Instances
- B) Spot Instances
- C) EC2 Instance Savings Plans
- D) Compute Savings Plan

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `59%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (59%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
For a company that is planning a partial migration to a serverless architecture in the next year and wants to pay for resources up front to optimize costs, the best AWS purchasing option is:
D. Compute Savings Plan

The other options are less suitable for this scenario:
A. Convertible Reserved Instances are a billing discount applied to specific EC2 instances and do not provide flexibility for serverless workloads.
B. Spot Instances are suitable for fault-tolerant and flexible workloads but do not offer the ability to pay upfront for a commitment period.
C. EC2 Instance Savings Plans provide discounts on EC2 instances only and do not extend to serverless services like Lambda or Fargate.
By choosing a Compute Savings Plan and paying upfront, the company can optimize costs for their current EC2 usage and seamlessly transition to serverless services as their migration progresses, without losing the committed savings. This flexibility aligns well with their planned partial migration to a serverless architecture.
---
Selected Answer: A
Convertible Reserved Instances (RIs) allow customers to purchase EC2 capacity at a discounted rate compared to On-Demand pricing while providing the flexibility to change instance families, operating systems, or tenancies during the term of the reservation.
This flexibility makes it ideal for a company that plans to migrate partially to serverless architecture, as it can adjust its RIs to match changing requirements over time.
The upfront payment option can further optimize costs.

Compute Savings Plans provide discounts on compute services, offering the flexibility to switch between EC2, AWS Lambda, and Fargate. However, they are better suited for fully serverless or containerized migrations rather than for managing upfront costs or EC2-focused workloads in a transitional phase.
---
Selected Answer: D
D. Compute Savings Plan - most flexible

</details>

---

## Question 693: CLF-C02-ET-Q693
**Domain 3:** Cloud Technology and Services  

**Question:**  
A retail company is building a new mobile app. The company is evaluating whether to build the app at an on-premises data center or in the AWS Cloud.

Which of the following are benefits of building this app in the AWS Cloud? (Choose two.)

**Choices:**
- A) A large, upfront capital expense and low variable expenses
- B) Increased speed for trying out new projects
- C) Complete control over the physical security of the infrastructure
- D) Flexibility to scale up in minutes as the application becomes popular
- E) Ability to pick the specific data centers that will host the application servers

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B and D are correct.
---
why its B ? and not D&E?
---
Selected Answer: BD
agree B&D

</details>

---

## Question 694: CLF-C02-ET-Q694
**Domain 2:** Security and Compliance  

**Question:**  
A company must archive its documents by using a write-once, read-many (WORM) model to meet legal and compliance obligations.

Which feature of Amazon S3 can the company use to meet this requirement?

**Choices:**
- A) S3 Versioning
- B) S3 bucket policy
- C) S3 Glacier Vault Lock
- D) S3 multi-factor authentication (MFA) delete

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
S3 Glacier Vault Lock allows you to enforce compliance controls on your archived data in Glacier, ensuring data is stored in a "write once, read many" (WORM) manner, meaning it cannot be modified or deleted within a predefined period
---
Selected Answer: C
C. S3 Glacier Vault Lock
---
Selected Answer: C
S3 Glacier Vault Lock provides the ability to lock your Glacier vaults to enforce WORM protection. Once a vault is locked with a retention policy, data cannot be modified or deleted for the specified retention period, ensuring compliance with regulatory requirements for write-once, read-many storage. This feature is specifically designed to meet compliance and regulatory requirements for immutable data storage.

</details>

---

## Question 695: CLF-C02-ET-Q695
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company has batch workloads that need to run for short periods of time on Amazon EC2. The workloads can handle interruptions and can start again from where they ended.

What is the MOST cost-effective EC2 instance purchasing option to meet these requirements?

**Choices:**
- A) Reserved Instances
- B) Spot Instances
- C) Dedicated Instances
- D) On-Demand Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Spot Instances - most cost effective and can handle interruptions
---
Selected Answer: B
B. Spot Instances
---
Selected Answer: B
in my opinion B is correct

</details>

---

## Question 696: CLF-C02-ET-Q696
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to deploy a PostgreSQL database into Amazon RDS. The database must be highly available and fault tolerant.

Which AWS solution should the company use to meet these requirements?

**Choices:**
- A) Amazon RDS with a single Availability Zone
- B) Amazon RDS snapshots
- C) Amazon RDS with multiple Availability Zones
- D) AWS Database Migration Service (AWS DMS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon RDS with multiple Availability Zones - highly available = multiple AZs
---
Selected Answer: C
Key Word: High available and fault tolerance

RDS configured with Multiple Availability zones (Multi-AZ),If one AZ is fail or not accessible user can access from another AZ RDS database. It is one of the best practice to high availability of RDS.

Answer is C. Amazon RDS with Multiple Availability Zones
---
key words: highly available*

</details>

---

## Question 697: CLF-C02-ET-Q697
**Domain 3:** Cloud Technology and Services  

**Question:**  
What is the MOST secure way to store passwords on AWS?

**Choices:**
- A) Store passwords in an Amazon S3 bucket.
- B) Store passwords as AWS CloudFormation parameters.
- C) Store passwords in AWS Storage Gateway.
- D) Store passwords in AWS Secrets Manager.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Store passwords in AWS Secrets Manager.
---
D. Secrets Manager helps you manage access to your applications, services, and IT resource by centrally storing and managing credentials, API keys, and other secrets.

</details>

---

## Question 698: CLF-C02-ET-Q698
**Domain 1:** Cloud Concepts  

**Question:**  
Which statements accurately describe the relationships among components of AWS global infrastructure? (Choose two.)

**Choices:**
- A) There are more AWS Regions than Availability Zones.
- B) There are more edge locations than AWS Regions.
- C) An edge location is an Availability Zone.
- D) There are more AWS Regions than edge locations.
- E) There are more Availability Zones than AWS Regions.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
B & E are correct
---
B. There are more edge locations than AWS Regions.

E. There are more Availability Zones than AWS Regions.

</details>

---

## Question 699: CLF-C02-ET-Q699
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service provides DNS resolution?

**Choices:**
- A) Amazon CloudFront
- B) Amazon VPC
- C) Amazon Route 53
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon Route 53 - DNS = Route 53

</details>

---

## Question 700: CLF-C02-ET-Q700
**Domain 1:** Cloud Concepts  

**Question:**  
A company needs to host an application in a specific geographic area to comply with regulations.

Which feature of the AWS global infrastructure will help the company meet this requirement?

**Choices:**
- A) Scalability
- B) Global footprint
- C) Availability
- D) Performance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Global footprint
---
Selected Answer: B
B. Global footprint

The AWS global footprint consists of multiple regions and availability zones around the world, allowing customers to choose specific geographic locations for their data and applications. This helps companies comply with regulatory requirements that mandate data residency in particular regions.
---
Global footprint, known as Global Reach previously

please help with discussion on 530 ~ 540. Thanks.

</details>

---

## Question 701: CLF-C02-ET-Q701
**Domain 2:** Security and Compliance  

**Question:**  
Which AWS service is a cloud security posture management (CSPM) service that aggregates alerts from various AWS services and partner products in a standardized format?

**Choices:**
- A) AWS Security Hub
- B) AWS Trusted Advisor
- C) Amazon EventBridge
- D) Amazon GuardDuty

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
AWS Security Hub: A cloud security posture management (CSPM) service that aggregates and prioritizes security findings from various AWS services and integrated partner products. It provides a centralized view of security alerts and compliance status, helping users to identify and remediate security issues.

 AWS Trusted Advisor: Provides recommendations for optimizing AWS resources for cost savings, performance, security, and fault tolerance. While it offers security-related checks, it is not specifically a CSPM service.

 Amazon EventBridge: An event bus service that enables event-driven architectures. It is not focused on CSPM or security alert aggregation.

 Amazon GuardDuty: A threat detection service that continuously monitors for malicious activity and unauthorized behavior in AWS accounts. It generates findings related to security threats, but is not a CSPM service for aggregating alerts in a standardized format.
---
Selected Answer: A
"AWS Security Hub is a cloud security posture management (CSPM) service that performs automated, continuous security best practice checks against your AWS resources to help you identify misconfigurations, and aggregates your security alerts (i.e. findings) in a standardized format so that you can more easily enrich, investigate, and remediate them."

Reference: https://aws.amazon.com/security-hub/features/?nc=sn&loc=2
---
Selected Answer: A
AWS Security Hub is a cloud security posture management (CSPM) service that provides a comprehensive view of your security state in AWS. It aggregates, organizes, and prioritizes security alerts and findings from various AWS services (like Amazon GuardDuty, Amazon Inspector, and AWS IAM Access Analyzer) and third-party partner products. These alerts are standardized in a common format, which helps in managing and responding to security issues more effectively

</details>

---

## Question 702: CLF-C02-ET-Q702
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
An ecommerce company plans to move its data center workload to the AWS Cloud to support highly dynamic usage patterns.

Which benefits make the AWS Cloud cost-effective for the migration of this type of workload? (Choose two.)

**Choices:**
- A) Reliability
- B) Security
- C) Elasticity
- D) Pay-as-you-go resource
- E) High availability

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `CD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: CD (100%). Contributor Answer: CD.

Community Rationale & Discussion:
Selected Answer: CD
C. Elasticity - allows company to scale resources up and down, supporting their highly dynamic usage patterns 
D. Pay-as-you-go resource - makes it cost-effective
---
C. Elasticity and D. Pay-as-you-go resource are the key benefits that make the AWS Cloud cost-effective for handling dynamic usage patterns.

</details>

---

## Question 703: CLF-C02-ET-Q703
**Domain 3:** Cloud Technology and Services  

**Question:**  
When designing AWS workloads to be operational even when there are component failures, what is an AWS best practice?

**Choices:**
- A) Perform quarterly disaster recovery tests.
- B) Place the main component on the us-east-1 Region.
- C) Design for automatic failover to healthy resources.
- D) Design workloads to fit on a single Amazon EC2 instance.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Design for automatic failover to healthy resources. - key aspect for fault tolerant systems

</details>

---

## Question 704: CLF-C02-ET-Q704
**Domain 4:** Billing, Pricing, and Support  

**Question:**  
Which of the following can the AWS Pricing Calculator do?

**Choices:**
- A) Project monthly AWS costs.
- B) Calculate historical AWS costs.
- C) Provide in-depth information about AWS pricing strategies.
- D) Provide users with access to their monthly bills.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Project monthly AWS costs. - this is what the pricing calculator does

</details>

---

## Question 705: CLF-C02-ET-Q705
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS solution gives companies the ability to use protocols such as NFS to store and retrieve objects in Amazon S3?

**Choices:**
- A) Amazon FSx for Lustre
- B) AWS Storage Gateway volume gateway
- C) AWS Storage Gateway file gateway
- D) Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (80%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. AWS Storage Gateway file gateway
---
Selected Answer: C
While Amazon FSx for Lustre supports NFS and can integrate with Amazon S3 for high-performance workloads (such as caching data from S3), it is primarily intended for use cases requiring high-performance computing (HPC) and parallel data processing. Its purpose is to optimize compute-heavy tasks by providing a fast file system that can process large-scale data, not to serve as a storage gateway solution for seamlessly storing and retrieving data from S3 via NFS.

The correct answer was C. AWS Storage Gateway file gateway, because AWS Storage Gateway file gateway is specifically designed to allow companies to use NFS (or SMB) protocols to store and retrieve data directly in S3. It acts as a bridge between on-premises environments and Amazon S3, enabling easy integration for businesses that want to store their files as objects in S3.
---
Selected Answer: A
Amazon FSx for Lustre is a managed file system that provides a high-performance file system optimized for compute-intensive workloads. It supports the Network File System (NFS) protocol and can be linked to Amazon S3. When you create an Amazon FSx for Lustre file system, you can link it to an S3 bucket, enabling you to access objects in S3 using the NFS protocol.
AWS Storage Gateway file gateway might seem like a good candidate due to its support for NFS, but it’s important to note that Amazon FSx for Lustre provides a more integrated and performant solution for linking file systems with S3, particularly for use cases requiring high-performance compute.

</details>

---

## Question 706: CLF-C02-ET-Q706
**Domain 2:** Security and Compliance  

**Question:**  
A user has been granted permission to change their own IAM user password.

Which AWS services can the user use to change the password? (Choose two.)

**Choices:**
- A) AWS Command Line Interface (AWS CLI)
- B) AWS Key Management Sen/ice (AWS KMS)
- C) AWS Management Console
- D) AWS Resource Access Manager (AWS RAM)
- E) AWS Secrets Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
A & C are correct
---
Keyword- change their own IAM user password.

In AWS user wants to change their password by using IAM -Identity and Access Management services only.

This IAM service is only able to access through AWS Management Console and AWS Command Line Interface only.

Answer is-:A- AWS Command Line Interface
 C- AWS Management Console

</details>

---

## Question 707: CLF-C02-ET-Q707
**Domain 2:** Security and Compliance  

**Question:**  
Which task is the customer's responsibility, according to the AWS shared responsibility model?

**Choices:**
- A) Patch a guest operating system that is deployed on an Amazon EC2 instance.
- B) Control physical access to an AWS data center.
- C) Control access to AWS underlying hardware.
- D) Patch a host operating system that is deployed on Amazon S3.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Patch a guest operating system that is deployed on an Amazon EC2 instance.

All other choices are the responsibility of AWS.

</details>

---

## Question 708: CLF-C02-ET-Q708
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service or feature provides a firewall at the subnet level within a VPC?

**Choices:**
- A) Security group
- B) Network ACL
- C) Elastic network interface
- D) AWS WAF

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Network ACL = subnet level

</details>

---

## Question 709: CLF-C02-ET-Q709
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company wants to use automated video analysis to identify employees that are accessing its offices.

Which AWS service will meet this requirement?

**Choices:**
- A) Amazon Rekognition
- B) Amazon Polly
- C) Amazon Cognito
- D) AWS Lambda

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Amazon Rekognition = image and video analysis
---
Selected Answer: A
Answer is A
---
Selected Answer: A
Amazon Rekognition is a cloud-based image and video analysis service that makes it easy to add advanced computer vision capabilities to your applications. The service is powered by proven deep learning technology and it requires no machine learning expertise to use. Amazon Rekognition includes a simple, easy-to-use API that can quickly analyze any image or video file that’s stored in Amazon S3.

You can add features that detect objects, text, unsafe content, analyze images/videos, and compare faces to your application using Rekognition's APIs. With Amazon Rekognition's face recognition APIs, you can detect, analyze, and compare faces for a wide variety of use cases, including user verification, cataloging, people counting, and public safety.

https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html

</details>

---

## Question 710: CLF-C02-ET-Q710
**Domain 3:** Cloud Technology and Services  

**Question:**  
A company needs to host a web server on Amazon EC2 instances for at least 1 year. The web server cannot tolerate interruption.

Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?

**Choices:**
- A) On-Demand Instances
- B) Partial Upfront Reserved Instances
- C) Spot Instances
- D) No Upfront Reserved Instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Partial Upfront Reserved Instances - with this you commit to a one year term (paying a portion of the cost upfront) and do not pay as much hourly as you would with On-Demand Instances.

</details>

---

## Question 711: CLF-C02-ET-Q711
**Domain 2:** Security and Compliance  

**Question:**  
Which guidelines are best practices for using AWS Identity and Access Management (IAM)? (Choose two.)

**Choices:**
- A) Share access keys.
- B) Create individual IAM users.
- C) Use inline policies instead of customer managed policies.
- D) Grant maximum privileges to IAM users.
- E) Use groups to assign permissions to IAM users.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BE`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BE (100%). Contributor Answer: BE.

Community Rationale & Discussion:
Selected Answer: BE
B. Create individual IAM users.
E. Use groups to assign permissions to IAM users.

</details>

---

## Question 712: CLF-C02-ET-Q712
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which AWS service is always provided at no charge?

**Choices:**
- A) Amazon S3
- B) AWS Identity and Access Management (IAM)
- C) Elastic Load Balancers
- D) AWS WAF

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (94%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
"IAM is a feature of your AWS account and is offered at no additional charge."

Reference: https://aws.amazon.com/iam/getting-started/?nc=sn&loc=3
---
Selected Answer: A
AWS Identity and Access Management (IAM) is a service provided at no additional charge. IAM allows you to manage access to AWS resources securely by creating and managing users, groups, roles, and policies. You can use IAM to control who has access to what resources within your AWS account. There are no charges for creating or using IAM resources, such as users, roles, and permissions.
---
Selected Answer: B
B. AWS Identity and Access Management (IAM)

</details>

---

## Question 713: CLF-C02-ET-Q713
**Domain 3:** Cloud Technology and Services  

**Question:**  
Which advantage of cloud computing allows users to scale resources up and down based on the amount of load that an application supports?

**Choices:**
- A) Go global in minutes
- B) Stop guessing capacity
- C) Benefit from massive economies of scale
- D) Trade fixed expense for variable expense

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
The phrase “Stop guessing capacity” is often used in the context of cloud computing. It highlights one of the key benefits of cloud services: the ability to scale resources up or down based on actual demand, rather than having to predict and invest in infrastructure capacity ahead of time. This approach helps avoid the costs associated with over-provisioning (buying more capacity than needed) or under-provisioning (not having enough capacity to meet demand).
---
Selected Answer: B
B. Stop guessing capacity

</details>

---

## Question 714: CLF-C02-ET-Q714
**Domain 2:** Security and Compliance  

**Question:**  
A company is requesting Payment Card Industry (PCI) reports that validate the operating effectiveness of AWS security controls.

How should the company obtain these reports?

**Choices:**
- A) Contact AWS Support.
- B) Download reports from AWS Artifact.
- C) Download reports from AWS Security Hub.
- D) Contact an AWS technical account manager (TAM).

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Download reports from AWS Artifact.
---
AWS Artifact is correct. 

Please help with discussion on 542 ~ 544 549. Thanks.
---
Selected Answer: B
AWS Artifact offers on-demand access to ASW's compliance and security documentation.

</details>

---

## Question 715: CLF-C02-ET-Q715
**Domain 3:** Cloud Technology and Services  

**Question:**  
An ecommerce company wants to distribute traffic between the Amazon EC2 instances that host its website.

Which AWS service or resource will meet these requirements?

**Choices:**
- A) Application Load Balancer
- B) AWS WAF
- C) AWS CloudHSM
- D) AWS Direct Connect

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Application Load Balancer
---
A. A load balancer serves as the single point of contact for clients. The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases the availability of your application. You add one or more listeners to your load balancer.

</details>

---

## Question 716: CLF-C02-ET-Q716
**Domain 1:** Cloud Concepts  

**Question:**  
Which AWS services or features form the AWS Cloud global infrastructure? (Choose two.)

**Choices:**
- A) Availability Zones
- B) Amazon ElastiCache
- C) AWS Regions
- D) Amazon S3
- E) Amazon VPC

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: AC
Availability Zones and Regions form the global infrastructure.

</details>

---

## Question 717: CLF-C02-ET-Q717
**Domain 2:** Security and Compliance  

**Question:**  
According to the AWS shared responsibility model, which of the following are AWS responsibilities? (Choose two.)

**Choices:**
- A) Network infrastructure and virtualization of infrastructure
- B) Security of application data
- C) Guest operating systems
- D) Physical security of hardware
- E) Credentials and policies

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
A & D are the responsibilities of AWS.
---
Selected Answer: AD
A and D look like correct answers.

</details>

---

## Question 718: CLF-C02-ET-Q718
**Domain 2:** Security and Compliance  

**Question:**  
A company uses Amazon Aurora as its database service. The company wants to encrypt its databases and database backups.

Which party manages the encryption of the database clusters and database snapshots, according to the AWS shared responsibility model?

**Choices:**
- A) AWS
- B) The company
- C) AWS Marketplace partners
- D) Third-party partners

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: A
I think its a,Amazon Aurora is a managed database service
---
Selected Answer: B
In the AWS Shared Responsibility Model, you, the customer, are responsible for database encryption. While AWS provides the infrastructure and underlying security of the cloud, you are responsible for securing your data, applications, and access within the AWS environment, which includes encryption.
---
Selected Answer: B
B. The company

</details>

---
