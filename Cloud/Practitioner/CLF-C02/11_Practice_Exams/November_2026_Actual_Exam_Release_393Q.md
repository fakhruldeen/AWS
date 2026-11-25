# AWS Certified Cloud Practitioner (CLF-C02) — November 2026 Authentic Practice Suite (393 Questions)

> **Exam Code:** `CLF-C02`  
> **Curriculum Release:** November 2026 Candidate Practice & Revision Pool  
> **Total Questions:** 393 Verified Exam Practice Questions  
> **Interactive Terminal Revision:** `python3 scripts/aws_revision_runner.py --cert CLF --release-2026`  
> **Interactive Timed 65-Question Mock:** `python3 scripts/aws_revision_runner.py --cert CLF --release-2026 --mock`  

---

## 📊 Executive Structure & Priority Breakdown

| Priority Tier | Question Count | Exam Impact | Core Focus |
| :--- | :---: | :---: | :--- |
| **Tier 1: Guaranteed Core Traps** | **224 Questions** | **~57.0%** | Shared Responsibility, IAM Least Privilege, S3 Lifecycle Tiers, EC2 Pricing, Security Quartet, Budgets |
| **Tier 2: Core Architecture** | **107 Questions** | **~27.2%** | Lambda, ECS/Fargate, RDS/Aurora, DynamoDB, VPC, Security Groups vs NACLs, Well-Architected 6 Pillars |
| **Tier 3: Specialized Disambiguation** | **62 Questions** | **~15.8%** | Support Plans, Snow Family migration, AI/ML managed services, CloudTrail vs CloudWatch auditing |

---

### Question 1
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q001`

A company is building an application that needs to deliver images and videos globally with
minimal latency.
Which approach can the company use to accomplish this in a cost effective manner?

- **A)** Deliver the content through Amazon CloudFront.
- **B)** Store the content on Amazon S3 and enable S3 cross-region replication.
- **C)** Implement a VPN across multiple AWS Regions.
- **D)** Deliver the content through AWS PrivateLink.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers
data, videos, applications, and APIs to customers globally with low latency, high transfer
speeds, all within a developer-friendly environment. It works seamlessly with services
including AWS Shield for DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon
EC2 as origins for your applications, and Lambda@Edge to run custom code closer to
customers' users and to customize the user experience. By using CloudFront, you can
cache your content at the edge locations that are closest to your end users, reducing the
network latency and improving the performance of your application. CloudFront also offers
a pay-as-you-go pricing model, so you only pay for the data transfer and requests that you
use.

</details>

---

### Question 2
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q002`

Which AWS compute service gives users the ability to securely and reliably run containers
at scale?

- **A)** Amazon Elastic Container Service (Amazon ECS)
- **B)** Amazon Aurora
- **C)** Amazon Athena
- **D)** Amazon Polly

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast container
management service that allows you to run, stop, and manage Docker containers on a
cluster of Amazon EC2 instances or a serverless environment powered by AWS Fargate. It
provides secure, reliable, and scalable operations for containers, allowing users to deploy
containers in a highly secure and reliable manner. Amazon Aurora is a relational database
service, Amazon Athena is an interactive query service, and Amazon Polly is a text-tospeech service. Therefore, the correct answer is Amazon ECS.
Reference:
AWS Documentation on Amazon ECS

</details>

---

### Question 3
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q003`

A company is running workloads for multiple departments within a single VPC. The
company needs to be able to bill each department for its resource usage.
Which action should the company take to accomplish this goal with the LEAST operational
overhead?

- **A)** Add a department tag to each resource and configure cost allocation tags.
- **B)** Move each department resource to its own VPC.
- **C)** Move each department resource to its own AWS account.
- **D)** Use AWS Organizations to get a billing report for each department.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Adding a department tag to each resource and configuring cost allocation tags is an action
that can help you accomplish the goal of billing each department for its resource usage
with the least operational overhead. Tags are simple labels consisting of a key and an
optional value that you can assign to AWS resources. You can use tags to organize your
resources and track your AWS costs on a detailed level. Cost allocation tags enable you to
track your AWS costs on a detailed level. After you activate cost allocation tags, AWS uses
the cost allocation tags to organize your resource costs on your cost allocation report, to
make it easier for you to categorize and track your AWS costs2. Moving each department
resource to its own VPC or its own AWS account is an action that can help you isolate and
control the resources for each department, but it would incur more operational overhead
than using tags. Using AWS Organizations to get a billing report for each department is an
ac

</details>

---

### Question 4
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q004`

What is AWS responsible for according to the AWS shared responsibility model? (Select
TWO.)

- **A)** Client-side data encryption
- **B)** Amazon EC2 guest operating systems
- **C)** The compute infrastructure  D. Availability Zones
- **E)** Customer data

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CD`

According to theAWS Shared Responsibility Model, AWS is responsible for thesecurity of
the cloud, while customers are responsible for thesecurity in the cloud. AWS
responsibilities include protecting the physical infrastructure that supports AWS services,
such as data centers, hardware, networking, and global infrastructure.
Specifically, AWS is responsible forthe compute infrastructure, which includes servers,
storage devices, networking equipment, and virtualization layers. AWS is also responsible
forAvailability Zones, ensuring they are physically separate, fault-isolated, and highly
available.
Client-side data encryption, Amazon EC2 guest operating systems, and customer data are
explicitly defined ascustomer responsibilities. Customers must manage operating system
patching, encryption methods, access controls, and data protection within their AWS
environments.
AWS documentation consistently emphasizes that customers retain ownership and control
of their data, while AWS ensures the

</details>

---

### Question 5
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q005`

A company wants to design a reliable web application that is hosted on Amazon EC2.
Which approach will achieve this goal?

- **A)** Launch large EC2 instances in the same Availability Zone.
- **B)** Spread EC2 instances across more than one security group.
- **C)** Spread EC2 instances across more than one Availability Zone.
- **D)** Use an Amazon Machine Image (AMI) from AWS Marketplace.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The approach that will achieve the goal of designing a reliable web application that is
hosted on Amazon EC2 is to spread EC2 instances across more than one Availability
Zone. An Availability Zone is a physically isolated location within an AWS Region that has
its own power, cooling, and network connectivity. By spreading EC2 instances across
multiple Availability Zones, users can increase the fault tolerance and availability of their
web applications, as well as reduce latency for end users2. Launching large EC2 instances
in the same Availability Zone, spreading EC2 instances across more than one security
group, or using an Amazon Machine Image (AMI) from AWS Marketplace are not sufficient
to ensure reliability, as they do not provide redundancy or resilience in case of an outage in
one Availability Zone.

</details>

---

### Question 6
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q006`

Which AWS service should a cloud practitioner use to receive real-time guidance for
provisioning resources, based on AWS best practices related to security, cost optimization,
and service limits?

- **A)** AWS Trusted Advisor
- **B)** AWS Config
- **C)** AWS Security Hub
- **D)** AWS Systems Manager

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Trusted Advisor is the AWS service that provides real-time guidance for provisioning
resources, based on AWS best practices related to security, cost optimization, and service
limits. AWS Trusted Advisor inspects the user's AWS environment and provides
recommendations for improving performance, security, and reliability, reducing costs, and
following best practices. AWS Trusted Advisor also alerts the user when they are
approaching or exceeding their service limits, and helps them request limit increases3.

</details>

---

### Question 7
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q007`

Which AWS service or feature is an example of a relational database management
system?

- **A)** Amazon Athena
- **B)** Amazon Redshift
- **C)** Amazon S3 Select
- **D)** Amazon Kinesis Data Streams

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud.
You can start with just a few hundred gigabytes of data and scale to a petabyte or more.
This enables you to use your data to acquire new insights for your business and
customers. Amazon Redshift is a relational database management system (RDBMS), so it
is compatible with other RDBMS applications. You can use standard SQL to query the
data.

</details>

---

### Question 8
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q008`

Which of the following is a benefit of operating in the AWS Cloud?

- **A)** The ability to migrate on-premises network devices to the AWS Cloud
- **B)** The ability to expand compute, storage, and memory when needed
- **C)** The ability to host custom hardware in the AWS Cloud
- **D)** The ability to customize the underlying hypervisor layer for Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

One of the benefits of operating in the AWS Cloud is the ability to expand compute,
storage, and memory when needed, which enables users to scale their applications and
resources up or down based on demand. This also helps users optimize their costs and
performance. The ability to migrate on-premises network devices to the AWS Cloud, the

ability to host custom hardware in the AWS Cloud, and the ability to customize the
underlying hypervisor layer for Amazon EC2 are not benefits of operating in the AWS
Cloud, as they are either not possible or not recommended by AWS .

</details>

---

### Question 9
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q009`

Which AWS service or feature allows a user to establish a dedicated network connection
between a company's on-premises data center and the AWS Cloud?

- **A)** AWS Direct Connect
- **B)** VPC peering
- **C)** AWS VPN
- **D)** Amazon Route 53

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Direct Connect is an AWS service that allows users to establish a dedicated network
connection between their on-premises data center and the AWS Cloud. This connection
bypasses the public internet and provides more predictable network performance, reduced
bandwidth costs, and increased security. Users can choose from different port speeds and
connection types, and use AWS Direct Connect to access AWS services in any AWS
Region globally. Users can also use AWS Direct Connect in conjunction with AWS VPN to
create a hybrid network architecture that combines the benefits of both private and public
connectivity. Reference: AWS Direct Connect, [AWS Cloud Practitioner Essentials: Module
3 - Compute in the Cloud]

</details>

---

### Question 10
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q010`

Which AWS service can generate information that can be used by external auditors?

- **A)** Amazon Cognito
- **B)** Amazon FSx
- **C)** AWS Config
- **D)** Amazon Inspector

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Config enables users to assess, audit, and evaluate the configurations of AWS
resources. It provides information that can be used by external auditors to ensure
compliance with various regulatory requirements by tracking changes and maintaining
configuration history. Amazon Cognito, FSx, and Inspector do not provide detailed
configuration tracking for audit purposes.

</details>

---

### Question 11
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q011`

A user needs the ability to access as many resources as are needed. The user also needs
the ability to scale up and scale down with only a few minutes of notice.
Which benefit of the AWS Cloud describes these abilities?

- **A)** Reliability
- **B)** Pay-as-you-go pricing  C. Elasticity
- **D)** Economy of scale

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 12
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q012`

A company has an application that runs periodically in an on-premises environment. The
application runs for a few hours most days, but runs for 8 hours a day for a week at the
end of each month.
Which AWS service or feature should be used to host the application in the AWS Cloud?

- **A)** Amazon EC2 Standard Reserved Instances
- **B)** Amazon EC2 On-Demand Instances
- **C)** AWS Wavelength
- **D)** Application Load Balancer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon EC2 On-Demand Instances are instances that let you pay for compute capacity
by the hour or second (minimum of 60 seconds) with no long-term commitments. This
frees you from the costs and complexities of planning, purchasing, and maintaining
hardware and transforms what are commonly large fixed costs into much smaller variable
costs. On-Demand Instances are suitable for applications with short-term, irregular, or
unpredictable workloads that cannot be interrupted, such as periodic applications that run
for a few hours most days, but run for 8 hours a day for a week at the end of each month2.
Amazon EC2 Standard Reserved Instances are instances that provide you with a
significant discount (up to 75%) compared to On-Demand Instance pricing. In exchange,
you select a term and make an upfront payment to reserve a certain amount of compute
capacity for that term. Reserved Instances are suitable for applications with steady state or
predictable usage that require reserved

</details>

---

### Question 13
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q013`

A company wants its Amazon EC2 instances to share the same geographic area but use
multiple independent underlying power sources.
Which solution achieves this goal?

- **A)** Use EC2 instances in a single Availability Zone.  B. Use EC2 instances in multiple AWS Regions.
- **C)** Use EC2 instances in multiple Availability Zones in the same AWS Region.
- **D)** Use EC2 instances in the same edge location and the same AWS Region.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The solution that achieves the goal of having Amazon EC2 instances share the same
geographic area but use multiple independent underlying power sources is to use EC2
instances in multiple Availability Zones in the same AWS Region. An Availability Zone is a
physically isolated location within an AWS Region that has its own power, cooling, and
network connectivity. An AWS Region is a geographical area that consists of two or more
Availability Zones. By using multiple Availability Zones, users can increase the fault
tolerance and resilience of their applications, as well as reduce latency for end users3.
Using EC2 instances in a single Availability Zone, multiple AWS Regions, or the same
edge location and the same AWS Region would not meet the requirement of having
multiple independent power sources.

</details>

---

### Question 14
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q014`

A social media company wants to protect its web application from common web exploits
such as SQL injections and cross-site scripting. Which AWS service will meet these
requirements?

- **A)** Amazon Inspector
- **B)** AWS WAF
- **C)** Amazon GuardDuty
- **D)** Amazon CloudWatch

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS WAF is a web application firewall service that helps protect web applications from
common web exploits that could affect availability, compromise security, or consume
excessive resources. AWS WAF gives you control over which traffic to allow or block to
your web applications by definingcustomizable web security rules. You can use AWS WAF
to create rules that block common attack patterns, such as SQL injection or cross-site
scripting, and rules that filter out specific traffic patterns you define1. AWS WAF also
integrates with other AWS services, such as Amazon CloudFront, Amazon API Gateway,
AWS AppSync, and AWS Load Balancer, to provide a comprehensive defense against
web attacks2. Therefore, AWS WAF meets the requirements of the social media company,
compared to the other options.
The other options are not suitable for the social media company's requirements, because:
Amazon Inspector is an automated security assessment service that helps improve the
security and compliance of ap

</details>

---

### Question 15
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q015`

A company wants to securely access an Amazon S3 bucket from an Amazon EC2
instance without accessing the internet.
What should the company use to accomplish this goal?

- **A)** VPN connection
- **B)** Internet gateway
- **C)** VPC endpoint
- **D)** NAT gateway

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

A VPC endpoint enables private connections between an Amazon VPC and AWS services,
like Amazon S3, without requiring internet access. This allows secure access to S3 from
an EC2 instance within the same VPC, reducing latency and improving security. VPN
connections and NAT gateways do not eliminate internet traffic, and an internet gateway
would expose the VPC to the public internet.

</details>

---

### Question 16
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q016`

A company is considering a move to the AWS Cloud. The company wants to be able to
scale its compute resources as needed to accommodate changing loads.
Which benefit of the AWS Cloud does this scenario describe?

- **A)** Elasticity
- **B)** Cost savings
- **C)** Agility  D. Global deployment in minutes

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 17
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q017`

A company has an online shopping website and wants to store customers' credit card dat
a. The company must meet Payment Card Industry (PCI) standards.
Which service can the company use to access AWS compliance documentation?

- **A)** Amazon Cloud Directory
- **B)** AWS Artifact
- **C)** AWS Trusted Advisor
- **D)** Amazon Inspector

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The correct answer is B because AWS Artifact is a service that provides access to AWS
compliance documentation, such as audit reports, security certifications, and agreements.
AWS Artifact allows customers to download, review, and accept the documents that are
relevant to their use of AWS services. The other options are incorrect because they are not
services that provide access to AWS compliance documentation. Amazon Cloud Directory
is a service that enables customers to create flexible cloud-native directories for organizing
hierarchies of data. AWS Trusted Advisor is a service that provides real-time guidance to
help customers follow AWS best practices for security, performance, cost optimization, and
fault tolerance. Amazon Inspector is a service that helps customers find security
vulnerabilities and deviations from best practices in their Amazon EC2 instances.
Reference: [AWS Artifact FAQs]

</details>

---

### Question 18
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q018`

A company is hosting a web application in a Docker container on Amazon EC2.
AWS is responsible for which of the following tasks?

- **A)** Scaling the web application and services developed with Docker
- **B)** Provisioning or scheduling containers to run on clusters and maintain their availability
- **C)** Performing hardware maintenance in the AWS facilities that run the AWS Cloud
- **D)** Managing the guest operating system, including updates and security patches

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS is responsible for performing hardware maintenance in the AWS facilities that run the
AWS Cloud. This is part of the shared responsibility model, where AWS is responsible for
the security of the cloud, and the customer is responsible for security in the cloud. AWS is
also responsible for the global infrastructure that runs all of the services offered in the AWS
Cloud, including the hardware, software, networking, and facilities that run AWS Cloud
services3. The customer is responsible for the guest operating system, including updates
and security patches, as well as the web application and services developed with Docker4.

</details>

---

### Question 19
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q019`

A company needs to organize its resources and track AWS costs on a detailed level. The
company needs to categorize costs by business department, environment, and application.
Which solution will meet these requirements'?

- **A)** Access the AWS Cost Management console to organize resources set an AWS budget, and receive notifications of unintentional usage.
- **B)** Use tags to organize the resources. Activate cost allocation tags to track AWS costs on a detailed level.
- **C)** Create Amazon CloudWatch dashboards to visually organize and track costs individually.
- **D)** Access the AWS Billing and Cost Management dashboard to organize and track resource consumption on a detailed level.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS recommends using tags to organize resources effectively and to activate cost
allocation tags to enable detailed tracking of costs by categories such as department,
environment, and application. This approach provides the granularity needed for tracking
and managing AWS costs accurately. AWS Cost Management and Billing tools provide
insights but do not inherently categorize costs without tags.

</details>

---

### Question 20
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q020`

A user needs a relational database but does not have the resources to manage the
hardware, resiliency, and replication.
Which AWS service option meets the user's requirements'?

- **A)** Run MySQL on Amazon Elastic Container Service (Amazon ECS)
- **B)** Run MySQL on Amazon EC2
- **C)** Choose Amazon RDS for MySQL
- **D)** Choose Amazon ElastiCache for Redis

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon RDS for MySQL is a fully managed, open-source cloud database service that
allows you to easily operate and scale your relational database of choice, including
MySQL. With Amazon RDS for MySQL, you don't have to worry about the hardware,
resiliency, and replication of your database, as Amazon RDS handles these tasks for you.
Amazon RDS for MySQL also provides features such as automated backups, multi-AZ

deployments, read replicas, encryption, monitoring, and more. Amazon RDS for MySQL is
compatible with the MySQL Community Edition versions 5.7 and 8.0, which means that
you can use the same code, applications, andtools that you already use with MySQL4567.
Reference: 4: Hosted MySQL - Amazon RDS for MySQL - AWS, 5: Amazon RDS for
MySQL - Amazon Relational Database Service, 6: Amazon RDS for MySQL -

云科

技, 7: Managed SQL Database - Amazon Relational Database Service (RDS) - AWS

</details>

---

### Question 21
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q021`

Which AWS service uses edge locations to cache content?

- **A)** Amazon Kinesis
- **B)** Amazon Simple Queue Service (Amazon SQS)
- **C)** Amazon CloudFront
- **D)** Amazon Route 53

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon CloudFront is a content delivery network (CDN) that uses edge locations to cache
content closer to users, reducing latency and improving performance. It supports the
delivery of web content, such as videos and images, by caching copies at edge locations
around the world. Amazon Kinesis, SQS, and Route 53 do not utilize edge locations for
content caching.

</details>

---

### Question 22
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q022`

Which of the following are the customer's responsibilities under the AWS shared
responsibility model?(Select TWO.)

- **A)** Maintain the configuration of infrastructure devices.
- **B)** Maintain patching and updates within the hardware infrastructure.
- **C)** Maintain the configuration of guest operating systems and applications.
- **D)** Manage decisions involving encryption options.
- **E)** Maintain infrastructure hardware.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C, D`

Customers are responsible for configuring and maintaining guest operating systems and
applications on services where the customer controls those components, such as Amazon
EC2. This includes security settings, software updates, application configuration, and guest
operating system patching. Customers are also responsible for managing their data,
including choosing and configuring appropriate encryption options. Therefore, options C
and D are correct. AWS is responsible for maintaining the configuration of its underlying
infrastructure devices, patching and updating the physical and foundational infrastructure,
and maintaining the servers, storage devices, networking equipment, and facilities that
operate AWS services. These AWS responsibilities are collectively described as
securityofthe cloud. Customer responsibilities vary according to the service selected. For
highly abstracted services such as Amazon S3, AWS also manages the operating system
and platform, while the cu

</details>

---

### Question 23
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q023`

A company is operating several factories where it builds products. The company needs the
ability to process data, store data, and run applications with local system
interdependencies that require low latency.
Which AWS service should the company use to meet these requirements?

- **A)** AWS loT Greengrass
- **B)** AWS Lambda
- **C)** AWS Outposts
- **D)** AWS Snowball Edge

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Outposts is a service that provides fully managed AWS infrastructure and services
on premises. It allows users to run applications that require low latency and local data
processing, while seamlessly connecting to the AWS Cloud for a consistent hybrid
experience. AWS IoT Greengrass is a service that provides local compute, messaging,
data caching, sync, and ML inference capabilities for connected devices. AWS Lambda is
a service that allows users to run code without provisioning or managing servers. AWS
Snowball Edge is a device that provides a petabyte-scale data transport and edge
computing solution.

</details>

---

### Question 24
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q024`

A company has created a VPC that has public subnets and private subnets.
According to the AWS shared responsibility model, which task is the company's
responsibility?

- **A)** Securing the physical routers in AWS data centers
- **B)** Maintaining the network infrastructure between AWS Regions
- **C)** Configuring route tables to direct traffic to an internet gateway
- **D)** Encrypting traffic between Availability Zones

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The customer is responsible for configuring the logical networking resources inside its
Amazon VPC. This includes creating and associating route tables and defining routes that
determine where subnet traffic is directed. A subnet is considered public when its
associated route table contains a route to an internet gateway and the relevant resources
have suitable public addressing and security configuration. Therefore, configuring a route
table to direct internet-bound traffic to an internet gateway is the company's responsibility,
making option C correct. AWS is responsible for the physical routers, backbone networks,
data centers, and networking infrastructure that provide communication within and

between AWS Regions. Customers do not maintain or physically secure that equipment.
AWS also provides infrastructure-level protection for traffic across its global network, while
customers remain responsible for application-level encryption where required by their
security pol

</details>

---

### Question 25
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q025`

Which activity can companies complete by using AWS Organizations?

- **A)** Troubleshoot the performance of applications.
- **B)** Manage service control policies (SCPs).
- **C)** Migrate applications to microservices.
- **D)** Monitor the performance of applications.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Managing service control policies (SCPs) is an activity that companies can complete by
using AWS Organizations. AWS Organizations is a service that enables the user to
consolidate multiple AWS accounts into an organization that can be managed as a single
unit. AWS Organizations allows the user to create groups of accounts and apply policies to
them, such as service control policies (SCPs) that specify the services and actions that
users and roles can access in the accounts. AWS Organizations also enables the user to
use consolidated billing, which combines the usage and charges from all the accounts in
the organization into a single bill3.

</details>

---

### Question 26
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q026`

A company is building a mobile app to provide shopping recommendations to its
customers. The company wants to use a graph database as part of the shopping
recommendation engine.
Which AWS database service should the company choose?

- **A)** Amazon DynamoDB
- **B)** Amazon Aurora
- **C)** Amazon Neptune
- **D)** Amazon DocumentDB (with MongoDB compatibility)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Neptune is a service that provides a fully managed graph database that supports
property graphs and RDF graphs. It can be used to build applications that work with highly
connected datasets, such as shopping recommendations, social networks, fraud detection,
and knowledge graphs2. Amazon DynamoDB is a service that provides a fully managed
NoSQL database that delivers fast and consistent performance at any scale. Amazon
Aurora is a service that provides a fully managed relational database that is compatible

with MySQL and PostgreSQL. Amazon DocumentDB (with MongoDB compatibility) is a
service that provides a fully managed document database that is compatible with
MongoDB.

</details>

---

### Question 27
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q027`

A company is migrating to the AWS Cloud and plans to run experimental workloads for 3 to
6 months on AWS. Which pricing model will meet these requirements?

- **A)** Use Savings Plans for a 3-year term.
- **B)** Use Dedicated Hosts.
- **C)** Buy Reserved Instances.
- **D)** Use On-Demand Instances.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

On-Demand Instances are the most flexible and cost-effective pricing model for short-term,
experimental, or unpredictable workloads on AWS. On-Demand Instances let you pay only
for the resources you use, without any long-term commitments or upfront fees. You can
easily start and stop instances as needed, and scale up or down depending on your
demand.
Savings Plans, Reserved Instances, and Dedicated Hosts are all pricing models that
require a commitment for a certain amount of usage or capacity for a one- or three-year
term. These pricing models offer lower prices than On-Demand Instances, but they are not
suitable for workloads that only run for 3 to 6 months or have variable usage patterns.
Savings Plans and Reserved Instances also offer flexibility to change instance types,
sizes, or regions within the same family or pool, while Dedicated Hosts are physical
servers that can only run specific instance types.

</details>

---

### Question 28
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q028`

A company's IT administrator needs to configure the AWS CLI for programmatic access to
AWS services for the company's employees. Which combination of credential components
must the IT administrator use to meet this requirement? (Select TWO.)

- **A)** A public key
- **B)** A private key
- **C)** An IAM role
- **D)** A secret access key
- **E)** An access key ID

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `DE`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 29
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q029`

A company has a client that uses an Amazon RDS database. The client requests
Information about operating system-level upgrades on the AWS resources that host the
RDS database. The company employs a third-party provider to monitor the RDS database.

Who is responsible for upgrading the operating systems for Amazon RDS under the AWS
shared responsibility model?

- **A)** The client
- **B)** The company
- **C)** AWS
- **D)** The third-party provider

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Under the AWS shared responsibility model, AWS is responsible for managing the
underlying infrastructure, including operating system-level updates on managed services
like Amazon RDS. Customers are responsible for managing the database instance and
configurations, but AWS handles OS updates for the infrastructure supporting RDS.

</details>

---

### Question 30
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q030`

What does "security of the cloud" refer to in the AWS shared responsibility model?

- **A)** Availability of AWS services such as Amazon EC2
- **B)** Security of the cloud infrastructure that runs all the AWS services
- **C)** Implementation of password policies for IAM users
- **D)** Security of customer environments by using AWS Network Firewall partners

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Security of the cloud refers to the security of the cloud infrastructure that runs all the AWS
services. This includes the hardware, software, networking, and facilities that AWS
operates and manages. AWS is responsible for protecting the security of the cloud as part
of the AWS shared responsibility model. Availability of AWS services such as Amazon EC2
refers to the ability of the services to be up and running and to meet the expected
performance. Availability is part of the reliability pillar of the AWS Well-Architected
Framework and is a shared responsibility between AWS and the customer .
Implementation of password policies for IAM users refers to the security of the customer
data and applications in the cloud. This includes the configuration and management of IAM
user permissions, encryption keys, security group rules, network ACLs, and other aspects
of access management. The customer is responsible for protecting the security in the
cloud as part of the AWS shared responsibility

</details>

---

### Question 31
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q031`

A company has set up a VPC on AWS. The company needs a dedicated connection
between the VPC and the company's on-premises network.
Which action should the company take to meet this requirement?

A. Establish a VPN connection between the VPC and the company's on-premises network.

- **B)** Establish an AWS Direct Connect connection between the VPC and the company's onpremises network.
- **C)** Attach an internet gateway to the VPC. Use the AWS public endpoints for connectivity.
- **D)** Configure Amazon Connect to provide connectivity between the VPC and the company's on-premises network.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Establishing an AWS Direct Connect connection between the VPC and the company's onpremises network is the action that the company should take to meet the requirement of
having a dedicated connection between the VPC and the company's on-premises network.
AWS Direct Connect is a service that lets you establish a dedicated network connection
between your network and one of the AWS Direct Connect locations. Using AWS Direct
Connect, you can create a private connection between AWS and your datacenter, office, or
colocation environment, which can reduce your network costs, increase bandwidth
throughput, and provide a more consistent network experience than internet-based
connections. Establishing a VPN connection between the VPC and the company's onpremises network is an action that the company can take to create a secure and encrypted
connection between the VPC and the company's on-premises network, but it is not a
dedicated connection, as it uses the public internet as the transport mechan

</details>

---

### Question 32
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q032`

A company runs Amazon EC2 instances in a research lab. The instances run for 3 hours
each week and cannot be interrupted.

- **A)** Convertible Reserved Instances  B. Compute Savings Plan
- **C)** Spot Instances
- **D)** On-Demand Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 33
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q033`

A company has deployed a web application to Amazon EC2 instances. The EC2 instances
have low usage. Which AWS service or feature should lite company use in rightsized the
FC? instances?

- **A)** AWS Config
- **B)** AWS Cost Anomaly Detection
- **C)** AWS Budgets
- **D)** AWS Compute Optimizer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Understanding AWS Compute Optimizer: AWS Compute Optimizer is a service that
analyzes the configuration and utilization metrics of your AWS resources. It provides
recommendations to help you select the optimal configurations for your workloads.
Why AWS Compute Optimizer for Rightsizing:
Resource Recommendations: It provides specific recommendations to rightsize your EC2
instances by suggesting instance types that match your actual usage patterns.
Cost Efficiency: By optimizing instance sizes, you can reduce costs associated with overprovisioned resources.
Performance Improvement: Ensures that you are using instances that provide the required
performance without over-allocating resources.
How to Implement AWS Compute Optimizer:
Enable AWS Compute Optimizer: In the AWS Management Console, navigate to AWS
Compute Optimizer and enable it for your account.
Review Recommendations: After a period of monitoring, review the recommendations
provided for your EC2 instances.
Implement Changes: Fol

</details>

---

### Question 34
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q034`

A company needs to store data across multiple Availability Zones in an AWS Region. The
data will not be accessed regularly but must be immediately retrievable.
Which Amazon Elastic File System (Amazon EFS) storage class meets these
requirements MOST cost effectively?

- **A)** EFS Standard
- **B)** EFS Standard-Infrequent Access(EFS Standard-IA)
- **C)** EFS One Zone  D. EFS One Zone-Infrequent Access (EFS One Zone-IA)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

EFS Standard-Infrequent Access (EFS Standard-IA) is the storage class that meets the
requirements of storing data across multiple Availability Zones in an AWS Region, that will
not be accessed regularly but must be immediately retrievable, most cost-effectively. EFS
Standard-IA is designed for files that are accessed less frequently, but still require the
same high performance, low latency, and high availability as EFS Standard. EFS
Standard-IA has a lower storage cost than EFS Standard, but charges a small additional
fee for each access. EFS One Zone and EFS One Zone-IA store data in a single
Availability Zone, which reduces the availability and durability compared to EFS Standard
and EFS Standard-IA.

</details>

---

### Question 35
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q035`

A company wants to centrally manage security policies and billing services within a multiaccount AWS environment. Which AWS service should the company use to meet these
requirements?

- **A)** AWS Identity and Access Management (IAM)
- **B)** AWS Organizations
- **C)** AWS Resource Access Manager (AWS RAM)
- **D)** AWS Config

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Organizations is a service that helps you centrally manage and govern your
environment as you grow and scale your AWS resources. You can use AWS
Organizations to create groups of accounts and apply policies to them. You can also use
AWS Organizations to consolidate billing for multiple accounts. Therefore, the correct
answer is B. You can learn more about AWS Organizations and its features .

</details>

---

### Question 36
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q036`

A company is undergoing a security audit. The audit includes security validation and
compliance validation of the AWS infrastructure and services that the company uses. The
auditor needs to locate compliance-related information and must download AWS security
and compliance documents. These documents include the System and Organization
Control (SOC) reports.

- **A)** AWS Abuse team
- **B)** AWS Support
- **C)** AWS Config
- **D)** AWS Artifact

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 37
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q037`

Which of the following is an AWS Well-Architected Framework design principle for
operational excellence in the AWS Cloud?

- **A)** Go global in minutes
- **B)** Make frequent, small, reversible changes
- **C)** Implement a strong foundation of identity and access management
- **D)** Stop spending money on hardware infrastructure for data center operations

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Making frequent, small, reversible changes is one of the design principles for operational
excellence in the AWS Cloud, as defined by the AWS Well-Architected Framework. This
principle means that you should design your workloads to allow for rapid and safe
changes, such as deploying updates, rolling back failures, and experimenting with new
features. By making small and reversible changes, you can reduce the risk of errors,
minimize the impact of failures, and increase the speed of recovery2. Reference: 2: AWS
Documentation - AWS Well-Architected Framework - Operational Excellence Pillar

</details>

---

### Question 38
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q038`

What is a benefit of using AWS serverless computing?

- **A)** Application deployment and management are not required
- **B)** Application security will be fully managed by AWS
- **C)** Monitoring and logging are not needed
- **D)** Management of infrastructure is offloaded to AWS

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS serverless computing is a way of building and running applications without thinking
about servers. AWS manages the infrastructure for you, so you don't have to provision,
scale, patch, or monitor servers. You only pay for the compute time you consume, and you
can focus on your application logic instead of managing servers12. Reference: Serverless
Computing - Amazon Web Services, AWS Serverless Computing, Benefits, Architecture
and Use-cases - XenonStack

</details>

---

### Question 39
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q039`

Which services can be used to deploy applications on AWS? (Select TWO.)

- **A)** AWS Elastic Beanstalk
- **B)** AWS Config
- **C)** AWS OpsWorksQ D. AWS Application Discovery Service
- **D)** Amazon Kinesis

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

The services that can be used to deploy applications on AWS are:
AWS Elastic Beanstalk. This is a service that simplifies the deployment and management
of web applications on AWS. Users can upload their application code and Elastic
Beanstalk automatically handles the provisioning, scaling, load balancing, monitoring, and
health checking of the resources needed to run the application. Users can also retain full

control and access to the underlying resources and customize their configuration settings.
Elastic Beanstalk supports multiple platforms, such as Java, .NET, PHP, Node.js, Python,
Ruby, Go, and Docker. [AWS Elastic Beanstalk Overview] AWS Certified Cloud
Practitioner - aws.amazon.com AWS OpsWorks. This is a service that provides
configuration management and automation for AWS resources. Users can define the
application architecture and the configuration of each resource using Chef or Puppet,
which are popular open-source automation platforms. OpsWorks then automatically
creates

</details>

---

### Question 40
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q040`

Which AWS service should be used when a company needs to provide its remote
employees with virtual desktops?

- **A)** Amazon Identity and Access Management (IAM)
- **B)** AWS Directory Service
- **C)** AWS IAM Identity Center (AWS Single Sign-On)
- **D)** Amazon Workspaces

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The AWS service that should be used when a company needs to provide its remote
employees with virtual desktops is Amazon WorkSpaces. Amazon WorkSpaces is a fully
managed, secure desktop-as-a-service (DaaS) solution that runs on AWS. Amazon
WorkSpaces allows users to provision cloud-based virtual desktops and provide their end
users access to the documents, applications, and resources they need from any supported
device, including Windows and Mac computers, Chromebooks, iPads, Fire tablets, and
Android tablets4. Amazon Identity and Access Management (IAM), AWS Directory Service,
and AWS IAM Identity Center (AWS Single Sign-On) are other AWS services related to
identity and access management, but they do not provide virtual desktops.

</details>

---

### Question 41
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q041`

A company is planning to migrate a monolithic application to AWS. The company wants to
modernize the application by splitting it into microservices. The company will deploy the
microservices on AWS.
Which migration strategy should the company use?

- **A)** Rehost
- **B)** Repurchase
- **C)** Replatform
- **D)** Refactor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Refactoring involves re-architecting and modifying an application to take advantage of
cloud-native features. In this case, the company wants to modernize a monolithic
application by breaking it into microservices. This process aligns with the Refactor
strategy, which is aimed at modernizing and re-architecting applications. Rehost,
Repurchase, and Replatform do not involve the level of re-architecting needed to move
from a monolithic to a microservices architecture.

</details>

---

### Question 42
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q042`

Which AWS services or features can control VPC traffic? (Select TWO.)

- **A)** Security groups
- **B)** AWS Direct Connect
- **C)** Amazon GuardDuty
- **D)** Network ACLs
- **E)** Amazon Connect

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AD`

The AWS services or features that can control VPC traffic are security groups and network
ACLs. Security groups are stateful firewalls that control the inbound and outbound traffic at
the instance level. You can assign one or more security groups to each instance in a VPC,
and specify the rules that allow or deny traffic based on the protocol, port, and source or
destination. Network ACLs are stateless firewalls that control the inbound and outbound
traffic at the subnet level. You can associate one network ACL with each subnet in a VPC,
and specify the rules that allow or deny traffic based on the protocol, port, and source or
destination. AWS Direct Connect, Amazon GuardDuty, and Amazon Connect are not
services or features that can control VPC traffic. AWS Direct Connect is a service that
establishes a dedicated network connection between your premises and AWS. Amazon
GuardDuty is a service that monitors your AWS account and workloads for malicious or
unauthorized activity. Amazon Co

</details>

---

### Question 43
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q043`

A development team wants to deploy multiple test environments for an application in a fast
repeatable manner.
Which AWS service should the team use?

- **A)** Amazon EC2
- **B)** AWS CloudFormation
- **C)** Amazon QuickSight
- **D)** Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS CloudFormation is a service that allows you to model and provision your AWS
resources using templates. You can define your infrastructure as code and automate the
creation and update of your resources. AWS CloudFormation also supports nested stacks,

change sets, and rollback features to help you manage complex and dynamic
environments34. Reference:
AWS CloudFormation
AWS Certified Cloud Practitioner Exam Guide

</details>

---

### Question 44
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q044`

A company is configuring its AWS Cloud environment. The company's administrators need
to group users together and apply permissions to the group.
Which AWS service or feature can the company use to meet these requirements?

- **A)** AWS Organizations
- **B)** Resource groups
- **C)** Resource tagging
- **D)** AWS Identity and Access Management (IAM)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The AWS service or feature that the company can use to group users together and apply
permissions to the group is AWS Identity and Access Management (IAM). AWS IAM is a
service that enables users to create and manage users, groups, roles, and permissions for
AWS services and resources. Users can use IAM groups to organize multiple users that
have similar access requirements, and attach policies to the groups that define the
permissions for the users in the group. This simplifies the management and administration
of user access

</details>

---

### Question 45
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q045`

Which AWS service or tool can a company use to set up consolidated billing?

- **A)** AWS Billing and Cost Management console
- **B)** AWS Organizations
- **C)** AWS Cost and Usage Report
- **D)** AWS Systems Manager

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Organizations Overview:
AWS Organizations allows a company to manage multiple AWS accounts under a single
organization.
Through the feature of consolidated billing, a company can receive a single bill for all
linked accounts.
Key Features of Consolidated Billing in AWS Organizations:
Aggregates usage across accounts to take advantage of volume pricing discounts.
Provides detailed cost reports for individual linked accounts.
Simplifies payment processing by centralizing billing.
Why Other Options Are Incorrect:
A . AWS Billing and Cost Management console:Used for managing budgets and payments
but does not set up consolidated billing.

C . AWS Cost and Usage Report:Provides detailed cost and usage reports but does not
set up consolidated billing.
D . AWS Systems Manager:Focuses on operational management, not billing.
Reference:
AWS Organizations Documentation

</details>

---

### Question 46
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q046`

A company has an application that uses AWS services. During scaling events, the
company wants to keep application usage within AWS service quotas.
Which AWS services or tools can report on the quotas so that the company can improve
the reliability of the application? (Select TWO.)

- **A)** Service Quotas console
- **B)** AWS Trusted Advisor
- **C)** AWS Systems Manager
- **D)** AWS Shield
- **E)** AWS Cost Explorer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AB`

The correct answers are A and B because Service Quotas console and AWS Trusted
Advisor are AWS services or tools that can report on the quotas so that the company can
improve the reliability of the application. Service Quotas console is an AWS tool that
enables users to view and manage their quotas for AWS services from a central location.
Users can use Service Quotas console to request quota increases, track quota usage, and
set up alarms for approaching quota limits. AWS Trusted Advisor is an AWS service that
provides real-time guidance to help users follow AWS best practices for security,
performance, cost optimization, and fault tolerance. One of the categories of checks that
AWS Trusted Advisor performs is service limits, which monitors the usage of each AWS
service and alerts users when they are close to reaching the default limit. The other
options are incorrect because they are not AWS services or tools that can report on the
quotas so that the company can improve the reliabili

</details>

---

### Question 47
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q047`

A company wants to migrate its on-premises data warehouse to AWS. The information in
the data warehouse is used to populate analytics dashboards.
Which AWS service should the company use for the data warehouse?

- **A)** Amazon ElastiCache
- **B)** Amazon Aurora
- **C)** Amazon RDS
- **D)** Amazon Redshift

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The AWS service that the company should use for the data warehouse is Amazon
Redshift. Amazon Redshift is a fully managed, petabyte-scale data warehouse service that
is optimized for analytical queries. It can integrate with various data sources and business
intelligence tools to provide fast and cost-effective insights. Amazon Redshift also offers
high availability, scalability, security, and compliance features. [Amazon Redshift
Overview]

</details>

---

### Question 48
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q048`

Which benefit is always free of charge with AWS, regardless of a user's AWS Support
plan?

- **A)** AWS Developer Support
- **B)** AWS Developer Forums
- **C)** Programmatic case management
- **D)** AWS technical account manager (TAM)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

TheAWS Developer Forumsare always free to use, regardless of the user's AWS Support
plan. They provide a platform for users to ask questions, share knowledge, and collaborate
with the AWS community.
A . AWS Developer Support: Incorrect, as it is a paid support plan option.
C . Programmatic case management: Incorrect, as this feature is available only with certain
AWS Support plans (Business and Enterprise).
D . AWS Technical Account Manager (TAM): Incorrect, as a TAM is provided only under
the AWS Enterprise Support plan, which is a paid support option.
AWS Cloud Reference:
AWS Support Plans

</details>

---

### Question 49
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q049`

A company migrated its core application onto multiple workloads in the AWS Cloud. The
company wants to improve the application's reliability.

Which cloud design principle should the company implement to achieve this goal?

- **A)** Maximize utilization.
- **B)** Decouple the components.
- **C)** Rightsize the resources.
- **D)** Adopt a consumption model.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Decoupling the components of an application means reducing the dependencies and
interactions between them, which can improve the application's reliability, scalability, and
performance. Decoupling can be achieved by using services such as Amazon Simple
Queue Service (Amazon SQS), Amazon Simple Notification Service (Amazon SNS), and
AWS Lambda1

</details>

---

### Question 50
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q050`

Which task can a user complete by using AWS Identity and Access Management (IAM)?

- **A)** Validate JSON syntax from an application configuration file.
- **B)** Grant permissions to applications that run on Amazon EC2 instances.
- **C)** Filter traffic to or from an Amazon EC2 instance.
- **D)** Analyze logs from an Amazon API Gateway call.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 51
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q051`

A company is using Amazon RDS.
Which task is the company's responsibility, according to the AWS shared responsibility
model?

- **A)** Apply encryption options for the database.
- **B)** Manage the underlying server hardware on which Amazon RDS runs.
- **C)** Apply patches to the underlying operating system.
- **D)** Apply minor patches to the database.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The customer is responsible for selecting and configuring the encryption options used for
its Amazon RDS database. When creating an encrypted DB instance, the customer
enables encryption and can select an AWS managed KMS key or an eligible customer
managed KMS key. The customer must also manage permissions and policies for
customer managed keys. Therefore, option A is correct. Amazon RDS is a managed
database service, so AWS manages the underlying server hardware and the operating
system used to run standard RDS DB instances. RDS also manages routine database
software patching, including applicable minor-version maintenance according to the
configured maintenance and upgrade settings. The exact division can differ for specialized
products such as RDS Custom or engines enrolled in Extended Support, but the
foundational-level question refers to standard Amazon RDS. AWS protects and maintains
the managed infrastructure, while customers remain responsible for their data, data

</details>

---

### Question 52
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q052`

An ecommerce company has been monitoring usage of its online store that is hosted on a
fleet of Amazon EC2 instances. Surges in traffic occur every weekend day at the same
time and last for approximately 4 hours.

- **A)** Amazon EC2 Auto Scaling
- **B)** AWS Lambda
- **C)** Amazon EventBridge
- **D)** Elastic Load Balancing (ELB)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 53
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q053`

Which options are perspectives that include foundational capabilities of the AWS Cloud
Adoption Framework (AWS CAF)? (Select TWO.)

- **A)** Sustainability
- **B)** Security
- **C)** Operations
- **D)** Performance efficiency
- **E)** Reliability

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 54
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q054`

Which AWS service or feature can be used to create a private connection between an onpremises workload and an AWS Cloud workload?

- **A)** Amazon Route 53
- **B)** Amazon Macie
- **C)** AWS Direct Connect
- **D)** AWS PrivaleLink

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Direct Connect is a service that establishes a dedicated network connection between
your on-premises network and one or more AWS Regions. AWS Direct Connect can be
used to create a private connection between an on-premises workload and an AWS Cloud
workload, bypassing the public internet and reducing network costs, latency, and
bandwidth issues. AWS Direct Connect can also provide increased security and reliability
for your hybrid cloud applications and data transfers. Reference:
AWS Direct Connect
What is AWS Direct Connect?
AWS Direct Connect User Guide

</details>

---

### Question 55
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q055`

Which of the following promotes AWS Cloud architectural best practices for designing and
operating reliable, secure, efficient, and cost-effective systems?

- **A)** AWS Serverless Application Model framework
- **B)** AWS Business Support
- **C)** Principle of least privilege
- **D)** AWS Well-Architected Framework

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Well-Architected Framework promotes AWS Cloud architectural best practices for
designing and operating reliable, secure, efficient, and cost-effective systems. AWS WellArchitected Framework is a set of guidelines and best practices that help the user to
evaluate and improve the architecture of their applications and workloads on AWS. AWS
Well-Architected Framework consists of five pillars: operational excellence, security,
reliability, performance efficiency, and cost optimization. Each pillar provides a set of
design principles, questions, and best practices that help the user to achieve the desired
outcomes for their systems.

</details>

---

### Question 56
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q056`

Which AWS service or tool helps companies measure the environmental impact of their
AWS usage?

- **A)** AWS customer carbon footprint tool
- **B)** AWS Compute Optimizer
- **C)** Sustainability pillar
- **D)** OS-Climate (Open Source Climate Data Commons)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS customer carbon footprint tool is an AWS service or tool that helps companies
measure the environmental impact of their AWS usage. It allows users to estimate the
carbon emissions associated with their AWS resources and services, such as EC2, S3,
and Lambda. It also provides recommendations and best practices to reduce the carbon
footprint and improve the sustainability of their AWS workloads4. AWS Compute Optimizer
is an AWS service that helps users optimize the performance and cost of their EC2
instances and Auto Scaling groups. It provides recommendations for optimal instance
types, sizes, and configurations based on the workload characteristics and utilization
metrics. It does not help users measure the environmental impact of their AWS usage.
Sustainability pillar is a concept that refers to the ability of a system to operate in an
environmentally friendly and socially responsible manner. It is not an AWS service or tool
that helps users measure the environmental impact of the

</details>

---

### Question 57
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q057`

Which AWS service or feature offers security for a VPC by acting as a firewall to control
traffic in and out of subnets?

- **A)** AWS Security Hub
- **B)** Security groups
- **C)** Network ACL
- **D)** AWSWAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

A network access control list (network ACL) is a feature that acts as a firewall for
controlling traffic in and out of one or more subnets in a virtual private cloud (VPC).
Network ACLs can be configured with rules that allow or deny traffic based on the source
and destination IP addresses, ports, and protocols1. AWS Security Hub is a service that
provides a comprehensive view of the security posture of AWS accounts and resources2.
Security groups are features that act as firewalls for controlling traffic at the instance
level3. AWS WAF is a web application firewall that helps protect web applications from
common web exploits4.

</details>

---

### Question 58
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q058`

A developer needs to use a standardized template to create copies of a company's AWS
architecture for development test, and production environments. Which AWS service
should the developer use to meet this requirement?

- **A)** AWS Cloud Map
- **B)** AWS Cloud Formation
- **C)** Amazon CloudFront
- **D)** AWS CloudTrail

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS CloudFormation allows developers to create, manage, and deploy AWS resources
using templates, ensuring a standardized and repeatable infrastructure setup. It's ideal for
setting up development, test, and production environments consistently. AWS Cloud Map,
CloudFront, and CloudTrail do not provide templated infrastructure management
capabilities.

</details>

---

### Question 59
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q059`

An ecommerce company has deployed a new web application on Amazon EC2 Instances.
The company wants to distribute incoming HTTP traffic evenly across all running
instances.
Which AWS service or resource will meet this requirement?

- **A)** Amazon EC2 Auto Scaling
- **B)** Application Load Balancer
- **C)** Gateway Load Balancer
- **D)** Network Load Balancer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AnApplication Load Balancer (ALB)is the best choice for distributing incoming
HTTP/HTTPS traffic evenly across multiple Amazon EC2 instances. It operates at
theapplication layer (Layer 7 of the OSI model) and is specifically designed to handle
HTTP and HTTPS traffic, which is ideal for web applications.
Here is why the ALB is the correct choice:
Layer 7 Load Balancing: The ALB works at the application layer and provides advanced
routing capabilities based on content. It can inspect the incoming HTTP requests and
make decisions on how to route traffic to various backend targets, which include Amazon
EC2 instances, containers, or Lambda functions. This is particularly useful for web
applications where you need to make routing decisions based on HTTP headers, paths, or
query strings.
HTTP and HTTPS Support: The ALB natively supports HTTP and HTTPS protocols,
making it the ideal load balancer for web-based applications. It can efficiently manage and
route these types of traffic and handle

</details>

---

### Question 60
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q060`

A company wants to provision and manage its AWS infrastructure by using the common
programming languages TypeScript, Python, Java, and .NET. Which h AWS service will
meet this requirement?

- **A)** AWS CodeBuild
- **B)** AWS CloudFormation
- **C)** AWSCLI
- **D)** AWS Cloud Development Kit (AWS CDK)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Cloud Development Kit (AWS CDK) is an open source software development
framework that allows you to model and provision your cloud infrastructure using familiar
programming languages such as TypeScript, Python, Java, and .NET. AWS CDK enables
you to use the expressive power of your favorite language to define your cloud resources,
such as compute, storage, network, and application services. AWS CDK also provides a
library of high-level constructs that represent AWS services and best practices. AWS CDK

uses AWS CloudFormation in the background to deploy your resources in a safe and
repeatable manner12. Reference:
AWS Cloud Development Kit (CDK) - TypeScript and Python are Now Generally Available
AWS Cloud Development Kit (AWS CDK) - Introduction to DevOps on AWS

</details>

---

### Question 61
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q061`

A company needs to invoke an AWS Step Functions workflow each time an Amazon EC2
instance state changes to RUNNING.
Which AWS service can the company use to meet this requirement?

- **A)** Amazon SageMaker
- **B)** Amazon Connect
- **C)** Amazon EventBridge
- **D)** AWS Fargate

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon EventBridge Overview:
EventBridge is a serverless event bus that enables applications to react to changes in
AWS resources.
It supports routing events such as EC2 state changes to various targets, including AWS
Step Functions.
How EventBridge Meets the Requirement:
EventBridge can capture the EC2 instance state change event and trigger the execution of
a Step Functions workflow.
The integration is seamless and supports workflows triggered by multiple event sources.
Why Other Options Are Incorrect:
A . Amazon SageMaker:Used for building, training, and deploying machine learning
models; not related to event triggers.
B . Amazon Connect:A cloud-based contact center service; unrelated to event triggers.
D . AWS Fargate:A compute engine for containers; does not manage events or invoke
workflows.
Reference:
Amazon EventBridge Documentation

</details>

---

### Question 62
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q062`

A company wants to run its application on Amazon EC2 instances. The company needs to
keep the application on-premises to meet a compliance requirement. Which AWS offering
will meet these requirements?

- **A)** Dedicated Instances
- **B)** Amazon CloudFront
- **C)** AWS Fargate
- **D)** AWS Outposts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Outposts is an AWS offering that brings AWS infrastructure and services to a
customer's on-premises location. It allows companies to run AWS services locally while
meeting any regulatory or compliance requirements to keep data or applications onpremises. Dedicated Instances are EC2 instances that run on hardware dedicated to a
single customer but are still within AWS data centers. Amazon CloudFront is a CDN
service, and AWS Fargate is a serverless compute engine for containers, neither of which
meets the requirement for running an application on-premises.
Reference:
AWS Outposts

</details>

---

### Question 63
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q063`

A company is running a key-value NoSQL workload on Amazon EC2 instances. The
company needs the workload to have scalability, failover protection, and backup
capabilities.
What is the MOST operationally efficient way to meet these requirements?

- **A)** Migrate the database to a relational database.
- **B)** Run an identical copy of the database in a second Availability Zone.
- **C)** Add additional EC2 instances to the database cluster.
- **D)** Migrate the database to Amazon DynamoDB.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 64
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q064`

Which of the following is an architectural design principle of the AWS Well-Architected
Framework?

- **A)** Loosely couple components
- **B)** Build monolithic systems
- **C)** Scale vertically, not horizontally
- **D)** Use third-party software

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 65
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q065`

A company needs to set a maximum spending limit on AWS services each month. The
company also needs to set up alerts for when the company reaches its spending limit.
Which AWS service or tool should the company use to meet these requirements?

- **A)** Cost Explorer
- **B)** AWS Trusted Advisor
- **C)** Service Quotas
- **D)** AWS Budgets

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Budgets is a service that helps you plan your service usage, service costs, and
instance reservations, and track how close your plan is to your budgeted amount. You can
set custom budgets that alert you when you exceed (or are forecasted to exceed) your
budgeted thresholds. You can also use AWS Budgets to set a maximum spending limit on
AWS services each month and set up alerts for when you reach your spending limit. Cost
Explorer is a service that enables you to visualize, understand, and manage your AWS
costs and usage over time. You can use Cost Explorer to view charts and graphs that
show how your costs are trending, identify areas that need further inquiry, and see the
impact of your cost management actions. However, Cost Explorer does not allow you to
set a maximum spending limit or alerts for your AWS services. AWS Trusted Advisor is a
service that provides you real time guidance to help you provision your resources following
AWS best practices, including security and perfor

</details>

---

### Question 66
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q066`

A cloud engineer wants to store data in Amazon S3. The engineer will access some of the
data yearly and some of the data dally.
Which S3 storage class will meet these requirements MOST cost-effectively?

- **A)** S3 Standard
- **B)** S3 Glacier Deep Archive
- **C)** S3 One Zone-Infrequent Access (S3 One Zone-IA)
- **D)** S3 Intelligent-Tiering

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

S3 Intelligent-Tiering is cost-effective for data with unpredictable access patterns. It
automatically moves data between two access tiers (frequent and infrequent) based on
access patterns, which is suitable for data accessed daily or infrequently. S3 Glacier Deep
Archive is for archival data accessed infrequently, and S3 One Zone-IA is for infrequent

access data stored in a single availability zone, which may not be ideal for data accessed
daily.

</details>

---

### Question 67
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q067`

A company has deployed an application in the AWS Cloud. The company wants to ensure
that the application is highly resilient.
Which component of AWS infrastructure can the company use to meet this requirement?

- **A)** Content delivery network (CDN)
- **B)** Edge locations
- **C)** Wavelength Zones
- **D)** Availability Zones

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Availability Zones are components of AWS infrastructure that can help the company
ensure that the application is highly resilient. Availability Zones are multiple, isolated
locations within each AWS Region. Each Availability Zone has independent power,
cooling, and physical security, and is connected to the other Availability Zones in the same
Region via low-latency, high-throughput, and highly redundant networking. Availability
Zones allow you to operate production applications and databases that are more highly
available, fault tolerant, and scalable than would be possible from a single data center.

</details>

---

### Question 68
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q068`

A company is looking for a managed machine learning (ML) service that can recommend
products based on a customer's previous behaviors.
Which AWS service meets this requirement?

- **A)** Amazon Personalize
- **B)** Amazon SageMaker
- **C)** Amazon Pinpoint
- **D)** Amazon Comprehend

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The AWS service that meets the requirement of providing a managed machine learning
(ML) service that can recommend products based on a customer's previous behaviors is
Amazon Personalize. Amazon Personalize is a fully managed service that enables
developers to create personalized recommendations for customers using their own data.
Amazon Personalize can automatically process and examine the data, identify what is
meaningful, select the right algorithms, and train and optimize a personalized
recommendation model2. Amazon SageMaker, Amazon Pinpoint, and Amazon
Comprehend are other AWS services related to machine learning, but they do not provide
the specific functionality of product recommendation.

</details>

---

### Question 69
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q069`

A company needs a graph database service that is scalable and highly available.

Which AWS service meets these requirements?

- **A)** Amazon Aurora
- **B)** Amazon Redshift
- **C)** Amazon DynamoDB
- **D)** Amazon Neptune

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The AWS service that meets the requirements of providing a graph database service that
is scalable and highly available is Amazon Neptune. Amazon Neptune is a fast, reliable,
and fully managed graph database service that supports property graph and RDF graph
models. Amazon Neptune is designed to store billions of relationships and query the graph
with milliseconds latency. Amazon Neptune also offers high availability and durability by
replicating six copies of the data across three Availability Zones and continuously backing
up the data to Amazon S35. Amazon Aurora, Amazon Redshift, and Amazon DynamoDB
are other AWS services that provide relational or non-relational database solutions, but
they do not support graph database models.

</details>

---

### Question 70
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q070`

A company wants to use Amazon EC2 instances. The company can commit to specific
usage and pricing terms for one year.
Which AWS purchasing option will meet these requirements MOST cost-effectively?

- **A)** Dedicated Hosts
- **B)** Reserved Instances
- **C)** Spot Instances
- **D)** On-Demand Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon EC2 Reserved Instances provide a billing discount in exchange for a one-year or
three-year commitment to specified EC2 usage attributes and payment terms. Because the
company can commit for one year and expects specific usage, Reserved Instances are the
most cost-effective choice among the listed options. A Reserved Instance is not a separate
physical instance; its billing benefit is applied to qualifying running EC2 instances that
match the reservation's attributes. Dedicated Hosts provide an entire physical host for one
customer and are appropriate for host-level compliance or licensing requirements, but
those requirements are not stated here. Spot Instances can provide larger discounts by
using spare EC2 capacity, but AWS can interrupt them, and the question describes a
predictable committed workload rather than an interruption-tolerant workload. On-Demand
Instances require no long-term commitment and are appropriate for short-term, irregular, or
unpredictable workloads, but

</details>

---

### Question 71
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q071`

A company wants high levels of detection and near-real-time (NRT) mitigation against
large and sophisticated distributed denial of service (DDoS) attacks on applications
running on AWS.
Which AWS service should the company use?

- **A)** Amazon GuardDuty
- **B)** Amazon Inspector
- **C)** AWS Shield Advanced
- **D)** Amazon Macie

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Shield Advanced is a service that provides high levels of detection and near-real-time
(NRT) mitigation against large and sophisticated distributed denial of service (DDoS)
attacks on applications running on AWS. AWS Shield Advanced also provides you with
24x7 access to the AWS DDoS Response Team (DRT) and protection against DDoS
attacks of any size or duration1. Amazon GuardDuty is a service that provides threat
detection for your AWS accounts and workloads, but it does not offer DDoS protection3.
Amazon Inspector is a service that helps you improve the security and compliance of your
applications deployed on AWS by automatically assessing them for vulnerabilities and
deviations from best practices. Amazon Macie is a service that uses machine learning and
pattern matching to discover and protect your sensitive data in AWS.

</details>

---

### Question 72
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q072`

Which aspect of security is the customer's responsibility, according to the AWS shared
responsibility model?

- **A)** Patch and configuration management
- **B)** Service and communications protection or zone security
- **C)** Physical and environmental controls
- **D)** Awareness and training

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

According to the AWS shared responsibility model, AWS is responsible for the security of
the cloud, while the customer is responsible for the security in the cloud. This means that
AWS provides the physical and environmental controls, the service and communications
protection, and the awareness and training for its employees, while the customer provides
the patch and configuration management, the identity and access management, the data
encryption, and the firewall configuration for its resources3.

</details>

---

### Question 73
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q073`

A company wants to use the AWS Cloud to deploy an application globally.
Which architecture deployment model should the company use to meet this requirement?

- **A)** Multi-Region
- **B)** Single-Region  C. Multi-AZ
- **D)** Single-AZ

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The architecture deployment model that the company should use to meet this requirement
is A) Multi-Region.
A multi-region deployment model is a cloud computing architecture that distributes an
application and its data across multiple geographic regions. A multi-region deployment
model enables a company to achieve global reach, high availability, disaster recovery, and
performance optimization. By deploying an application in multiple regions, a company can
serve customers from the nearest region, reduce latency, increase redundancy, and
comply with data sovereignty regulations12.
A single-region deployment model is a cloud computing architecture that runs an
application and its data within a single geographic region. A single-region deployment
model is simpler and cheaper than a multi-region deployment model, but it has limited
scalability, availability, and performance. A single-region deployment model may not be
suitable for a company that wants to deploy an application globally, as i

</details>

---

### Question 74
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q074`

Which AWS service converts text to lifelike voices?

- **A)** Amazon Transcribe
- **B)** Amazon Rekognition
- **C)** Amazon Polly
- **D)** Amazon Textract

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Polly is a service that turns text into lifelike speech, allowing you to create
applications that talk, and build entirely new categories of speech-enabled products. Polly's
Text-to-Speech (TTS) service uses advanced deep learning technologies to synthesize
natural sounding human speech1. Amazon Polly supports dozens of languages and a wide
range of natural-sounding voices. You can customize and control the speech output by
using lexicons and SSML tags. You can also store and redistribute the speech output in
standard audio formats like MP3 and OGG2.
Amazon Transcribe is a service that converts speech to text, enabling you to create text
transcripts from audio or video files. It can recognize multiple speakers, different
languages, accents, dialects, and background noises. It can also add punctuation and
formatting to the transcripts. Amazon Transcribe is useful for applications such as
subtitling, captioning, transcription, and voice search.
Amazon Rekognition is a service that

</details>

---

### Question 75
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q075`

A company needs to identify unused access that has been granted to users in its AWS
accounts.
Which AWS service or feature will provide this information?

- **A)** AWS CloudTrail
- **B)** AWS IAM Access Analyzer
- **C)** AWS IAM Identity Center
- **D)** AWS Trusted Advisor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS IAM Access Analyzer can identify and report unused access granted to IAM users
and roles. When an unused-access analyzer is created, it reviews access activity and
generates findings for conditions such as unused roles, unused IAM user access keys,
unused console passwords, and permissions for services or actions that have not been
used during the configured analysis period. This allows organizations to remove
unnecessary permissions and move toward least-privilege access. Therefore, option B is
correct. AWS CloudTrail records account and API activity, and its data can support
investigations, but it does not by itself produce the specialized unused-access findings
described in the question. IAM Identity Center centrally manages workforce access to
multiple AWS accounts and applications but is not the analysis service for identifying
unused IAM permissions. AWS Trusted Advisor provides best-practice checks across
categories such as cost, performance, resilience, security, and servic

</details>

---

### Question 76
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q076`

Which of the following are advantages of the AWS Cloud? (Select TWO.)

- **A)** Trade variable expenses for capital expenses
- **B)** High economies of scale
- **C)** Launch globally in minutes
- **D)** Focus on managing hardware infrastructure
- **E)** Overprovision to ensure capacity

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B, C`

The correct answers are B and C because they are advantages of the AWS Cloud. High
economies of scale means that AWS can achieve lower variable costs than customers can
get on their own. Launch globally in minutes means that AWS has a global infrastructure
that allows customers to deploy their applications and data across multiple regions and
availability zones. The other options are incorrect because they are not advantages of the
AWS Cloud. Trade variable expenses for capital expenses means that customers have to
invest heavily in data centers and servers before they know how they will use them. Focus
on managing hardware infrastructure means that customers have to spend time and
money on maintaining and upgrading their physical resources. Overprovision to ensure
capacity means that customers have to pay for more resources than they actually need to
avoid performance issues. Reference: What is Cloud Computing?

</details>

---

### Question 77
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q077`

Which AWS service provides a scalable data warehouse solution?

- **A)** Amazon Redshift
- **B)** Amazon DynamoDB
- **C)** Amazon S3
- **D)** Amazon Kinesis Data Streams

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 78
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q078`

Which of the following is entirely the responsibility of AWS, according to the AWS shared
responsibility model?

- **A)** Security awareness and training
- **B)** Development of an IAM password policy
- **C)** Patching of the guest operating system
- **D)** Physical and environmental controls

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Physical and environmental controls are entirely the responsibility of AWS, according to
the AWS shared responsibility model. The AWS shared responsibility model defines the
division of responsibilities between AWS and the customer for security and compliance.
AWS is responsible for the security of the cloud, which includes the physical and
environmental controls of the AWS global infrastructure, such as power, cooling, fire
suppression, and physical access. The customer is responsible for the security in the
cloud, which includes the configuration and management of the AWS resources and
applications. For more information, see [AWS Shared Responsibility Model] and [AWS
Cloud Security].

</details>

---

### Question 79
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q079`

A company website is experiencing DDoS attacks.
Which AWS service can help protect the company website against these attacks?

- **A)** AWS Resource Access Manager
- **B)** AWS Amplify
- **C)** AWS Shield
- **D)** Amazon GuardDuty

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Shield is a managed DDoS protection service that safeguards applications running
on AWS from distributed denial of service (DDoS) attacks. DDoS attacks are malicious
attempts to disrupt the normal functioning of a website or application by overwhelming it

with a large volume of traffic from multiple sources. AWS Shield provides two tiers of
protection: Standard and Advanced. AWS Shield Standard is automatically enabled for all
AWS customers at no additional cost. It protects your AWS resources, such as Amazon
CloudFront, AWS Global Accelerator, and Amazon Route 53, from the most common and
frequently occurring network and transport layer DDoS attacks. AWS Shield Advanced is
an optional paid service that provides additional protection for your AWS resources and
applications, such as Amazon Elastic Compute Cloud (Amazon EC2), Elastic Load
Balancing (ELB), Amazon Simple Storage Service (Amazon S3), Amazon Relational
Database Service (Amazon RDS), and AWS Elastic Beanstalk. AWSShield

</details>

---

### Question 80
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q080`

Which options are AWS Cloud Adoption Framework (AWS CAF) cloud transformation
journey recommendations? (Select TWO.)

- **A)** Envision phase
- **B)** Align phase
- **C)** Assess phase
- **D)** Mobilize phase
- **E)** Migrate and modernize phase

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 81
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q081`

A company wants to integrate natural language processing (NLP) into business
intelligence (Bl) dashboards. The company wants to ask questions and receive answers
with relevant visualizations.
Which AWS service or tool will meet these requirements?

- **A)** Amazon Macie
- **B)** Amazon Rekognition
- **C)** Amazon QuickSight Q
- **D)** Amazon Lex

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon QuickSight Q is a natural language query feature that lets you ask questions
about your data using everyday language and get answers in seconds. You can type
questions such as "What are the total sales by region?" or "How did marketing campaign A
perform?" and get answers in the form of relevant visualizations, such as charts or tables.
You can also use Q to drill down into details, filter data, or perform calculations. Q uses
machine learning to understand your data and your intent, and provides suggestions and
feedback to help you refine your questions.

</details>

---

### Question 82
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q082`

A user wants to allow applications running on an Amazon EC2 instance to make calls to
other AWS services. The access granted must be secure. Which AWS service or feature
should be used?

- **A)** Security groups
- **B)** AWS Firewall Manager
- **C)** IAM roles
- **D)** IAM user SSH keys

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

IAM roles are a secure way to grant permissions to applications running on an Amazon
EC2 instance to make calls to other AWS services. IAM roles are entities that have specific
permissions policies attached to them. You can create an IAM role and associate it with an
EC2 instance when you launch it or later. The applications on the instance can then use
the temporary credentials provided by the role to access AWS resources that the role
allows. This way, you do not have tostore any long-term credentials or access keys on the
instance, which reduces the risk of compromise or misuse12.
The other options are not correct, because:

Security groups are virtual firewalls that control the inbound and outbound traffic for your
EC2 instances. Security groups do not grant permissions to access other AWS services,
but rather filter the network traffic based on rules that you define3.
AWS Firewall Manager is a service that helps you centrally configure and manage firewall
rules across your accoun

</details>

---

### Question 83
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q083`

Which AWS service is a highly available and scalable DNS web service?

- **A)** Amazon VPC
- **B)** Amazon CloudFront
- **C)** Amazon Route 53
- **D)** Amazon Connect

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Route 53 is a highly available and scalable DNS web service. It is designed to
give developers and businesses an extremely reliable and cost-effective way to route end
users to Internet applications by translating domain names into the numeric IP addresses
that computers use to connect to each other2. Amazon Route 53 also offers other features
such as health checks, traffic management, domain name registration, and DNSSEC3.

</details>

---

### Question 84
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q084`

Which tasks are customer responsibilities, according to the AWS shared responsibility
model? (Select TWO.)

- **A)** Configure the AWS provided security group firewall.
- **B)** Classify company assets in the AWS Cloud.
- **C)** Determine which Availability Zones to use for Amazon S3 buckets.
- **D)** Patch or upgrade Amazon DynamoDB.
- **E)** Select Amazon EC2 instances to run AWS Lambda on. F. AWS Config

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AB`

According to the AWS shared responsibility model, the customer is responsible for security
in the cloud, which includes the tasks of configuring the AWS provided security group
firewall and classifying company assets in the AWS Cloud. A security group is a virtual
firewall that controls the inbound and outbound traffic for one or more EC2 instances. The
customer must configure the security group rules to allow or deny traffic based on protocol,
port, or source and destination IP address2 Classifying company assets in the AWS Cloud
means identifying the types, categories, and sensitivity levels of the data and resources
that the customer stores and processes on AWS. The customer must also determine the
applicable compliance requirements and regulations that apply to their assets, and
implement the appropriate security controls and measures to protect them

</details>

---

### Question 85
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q085`

Which Amazon S3 storage class is the MOST cost-effective for long-term storage?

- **A)** S3 Glacier Deep Archive
- **B)** S3 Standard
- **C)** S3 Standard-Infrequent Access (S3 Standard-IA)
- **D)** S3 One Zone-Infrequent Access (S3 One Zone-IA)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon S3 Glacier Deep Archive is the lowest-cost storage class in the cloud. It is
designed for long-term data archiving that is rarely accessed. It offers a retrieval time of 12
hours and a durability of 99.999999999% (11 9's). It is ideal for data that must be retained
for 7 years or longer to meet regulatory compliance requirements.

</details>

---

### Question 86
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q086`

Which AWS service provides a single location to track the progress of application
migrations?

- **A)** AWS Application Discovery Service
- **B)** AWS Application Migration Service
- **C)** AWS Service Catalog
- **D)** AWS Migration Hub

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Migration Hub is a service that provides a single location to track the progress of
application migrations across multiple AWS and partner solutions. It allows you to choose
the AWS and partner migration tools that best fit your needs, while providing visibility into
the status of migrations across your portfolio of applications1. AWS Migration Hub
supports migration status updates from the following tools: AWS Application Migration
Service, AWS Database Migration Service, CloudEndure Migration, Server Migration
Service, and Migrate for Compute Engine1.
The other options are not correct for the following reasons:
AWS Application Discovery Service is a service that helps you plan your migration projects
by automatically identifying servers, applications, and dependencies in your on-premises

data centers2. It does not track the progress of application migrations, but rather provides
information to help you plan and scope your migrations.
AWS Application Migration Service is a servi

</details>

---

### Question 87
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q087`

A company processes personally identifiable information (Pll) and must keep data in the
country where it was generated. The company wants to use Amazon EC2 instances for
these workloads.
Which AWS service will meet these requirements?

- **A)** AWS Outposts
- **B)** AWS Storage Gateway
- **C)** AWS DataSync
- **D)** AWS OpsWorks

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Outposts is an AWS service that extends AWS infrastructure, services, APIs, and
tools to virtually any datacenter, co-location space, or on-premises facility. AWS Outposts
enables you to run Amazon EC2 instances and other AWS services locally, while
maintaining a consistent and seamless connection to the AWS Cloud. AWS Outposts is
ideal for workloads that require low latency, local data processing, or data residency. By
using AWS Outposts, the company can process personally identifiable information (PII)
and keep data in the country where it was generated, while leveraging the benefits of AWS

</details>

---

### Question 88
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q088`

A company wants to migrate its applications to the AWS Cloud. The company plans to
identity and prioritize any business transformation opportunities and evaluate its AWS
Cloud readiness. Which AWS service or tool should the company use to meet these
requirements?

- **A)** AWS Cloud Adoption Framework (AWS CAF)
- **B)** AWS Managed Services (AMS)  C. AWS Well-Architected Framework
- **D)** AWS Migration Hub

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Cloud Adoption Framework (AWS CAF) is a set of best practices, tools, and
guidance that helps organizations get started with cloud technologies. AWS CAF helps
organizations identify and prioritize transformation opportunities, evaluate and improve
their cloud readiness, and iteratively evolve their transformation roadmap. AWS CAF
groups its capabilities in six perspectives: Business, People, Governance, Platform,
Security, and Operations. Each perspective comprises a set of capabilities that functionally
related stakeholders own or manage in the cloud transformation journey1 AWS Managed
Services (AMS) is a service that operates AWS infrastructure on behalf of customers,
providing a secure AWS Landing Zone, features that help meet various compliance
program requirements, a proven enterprise operating model, on-going cost optimization,
and day-to-day infrastructure management. AMS does not help customers identify and
prioritize business transformation opportunities or e

</details>

---

### Question 89
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q089`

A company runs thousands of simultaneous simulations using AWS Batch. Each
simulation is stateless, is fault tolerant, and runs for up to 3 hours.
Which pricing model enables the company to optimize costs and meet these
requirements?

- **A)** Reserved Instances
- **B)** Spot Instances
- **C)** On-Demand Instances
- **D)** Dedicated Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The correct answer is B because Spot Instances enable the company to optimize costs
and meet the requirements. Spot Instances are spare EC2 instances that are available at
up to 90% discount compared to On-Demand prices. Spot Instances are suitable for
stateless, fault-tolerant, and flexible applications that can run for any duration. The other

options are incorrect because they do not enable the company to optimize costs and meet
the requirements. Reserved Instances are EC2 instances that are reserved for a specific
period of time (one or three years) in exchange for a lower hourly rate. Reserved Instances
are suitable for steady-state or predictable workloads that run for a long duration. OnDemand Instances are EC2 instances that are launched and billed at a fixed hourly rate.
On-Demand Instances are suitable for short-term, irregular, or unpredictable workloads
that cannot be interrupted. Dedicated Instances are EC2 instances that run on hardware
that is dedicated to a single cust

</details>

---

### Question 90
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q090`

A cloud engineer wants to know the percentage of the allocated compute units that are in
use for a specific Amazon EC2 instance.
Which AWS service can provide this information?

- **A)** AWS CloudTrail
- **B)** AWS Config
- **C)** Amazon CloudWatch
- **D)** AWS Artifact

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon CloudWatch is a monitoring and observability service built for DevOps engineers,
developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you
with data and actionable insights to monitor your applications, respond to system-wide
performance changes, optimize resource utilization, and get a unified view of operational
health. CloudWatch collects monitoring and operational data in the form of logs, metrics,
and events, providing you with a unified view of AWS resources, applications, and services
that run on AWS and on-premises servers

</details>

---

### Question 91
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q091`

A company has multiple AWS accounts that include compute workloads that cannot be
interrupted. The company wants to obtain billing discounts that are based on the
company's use of AWS services.
Which AWS feature or purchasing option will meet these requirements?

- **A)** Resource tagging
- **B)** Consolidated billing
- **C)** Pay-as-you-go pricing
- **D)** Spot Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Consolidated billing is an AWS feature that allows users to combine the usage and costs of
multiple AWS accounts into a single bill. This enables users to obtain billing discounts that
are based on the company's use of AWS services, such as volume pricing tiers, Reserved

Instance discounts, and Savings Plans discounts5. Resource tagging is an AWS feature
that allows users to assign metadata to AWS resources, such as EC2 instances, S3
buckets, and Lambda functions. This enables users to organize, track, and manage their
AWS resources, such as filtering, grouping, and reporting. Pay-as-you-go pricing is an
AWS pricing model that allows users to pay only for the resources and services they use,
without any upfront or long-term commitments. This enables users to lower their costs by
scaling up or down as needed, and avoiding over-provisioning or under-utilization. Spot
Instances are spare EC2 instances that are available at up to 90% discount compared to
On-Demand prices. They are suitab

</details>

---

### Question 92
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q092`

A company has an on-premises application. The application has processing times of less
than 5 minutes and is invoked only a few times each day. The company wants to move the
application to the AWS Cloud.
Which AWS service will support this application MOST cost-effectively?

- **A)** Amazon Elastic Container Service (Amazon ECS)
- **B)** AWS Lambda
- **C)** Amazon Elastic Kubernetes Service (Amazon EKS)
- **D)** Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Lambda is a serverless compute service that is ideal for applications with shortrunning processes and low-frequency invocation, as it only charges for the compute time
consumed. Since the application is invoked only a few times a day and runs for less than 5
minutes, Lambda is the most cost-effective option. ECS, EKS, and EC2 are better suited
for more persistent workloads and would be more costly in this use case.

</details>

---

### Question 93
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q093`

A company moves its infrastructure from on premises to the AWS Cloud. The company
can now provision additional Amazon EC2 instances whenever the instances are required.

With this ability, the company can launch new marketing campaigns in 3 days instead of 3
weeks.
Which benefit of the AWS Cloud does this scenario demonstrate?

- **A)** Cost savings
- **B)** Improved operational resilience
- **C)** Increased business agility
- **D)** Enhanced security

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Increased business agility is the benefit of the AWS Cloud that this scenario demonstrates.
Business agility refers to the ability of a company to adapt to changing customer needs,
market conditions, and competitive pressures. Moving to the AWS Cloud enables business
agility by providing faster access to resources, lower upfront costs, and greater scalability
and flexibility. By using the AWS Cloud, the company can launch new marketing
campaigns in 3 days instead of 3 weeks, which shows that it can respond to customer
feedback more quickly and efficiently. For more information, see Benefits of Cloud
Computing and [Business Agility].

</details>

---

### Question 94
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q094`

A company wants to automatically add and remove Amazon EC2 instances. The company
wants the EC2 instances to adjust to varying workloads dynamically.
Which service or feature will meet these requirements?

- **A)** Amazon DynamoDB
- **B)** Amazon EC2 Spot Instances
- **C)** AWS Snow Family
- **D)** Amazon EC2 Auto Scaling

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon EC2 Auto Scaling is a service that helps you maintain application availability and
allows you to automatically add or remove EC2 instances according to definable
conditions. You can create collections of EC2 instances, called Auto Scaling groups, and
specify the minimum and maximum number of instances in each group. You can also
define scaling policies that adjust the number of instances based on the demand on your
application. Amazon EC2 Auto Scaling helps you improve the performance, reliability, and
cost-efficiency of your EC2 workloads123. Reference: 1: VDI Desktops - Amazon
WorkSpaces Family - AWS, 2: What is Amazon EC2 Auto Scaling? - Amazon EC2 Auto
Scaling, 3: Discover Amazon EC2 Auto Scaling Unit | Salesforce Trailhead

</details>

---

### Question 95
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q095`

A company has an AWS Business Support plan. The company needs to gain access to the
AWS DDoS Response Team (DRT) to help mitigate DDoS events.
Which AWS service or resource must the company use to meet these requirements?

- **A)** AWS Shield Standard  B. AWS Enterprise Support
- **C)** AWS WAF
- **D)** AWS Shield Advanced

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Shield Advanced provides enhanced protection against DDoS attacks and includes
access to the AWS DDoS Response Team (DRT) to help mitigate complex DDoS events.
AWS Shield Standard offers basic DDoS protection, which is included with AWS services,
but does not provide access to the DRT. AWS WAF is a web application firewall, and AWS
Enterprise Support is a premium support plan but does not specifically provide DDoS
mitigation services or access to the DRT.

</details>

---

### Question 96
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q096`

Which task can a company perform by using security groups in the AWS Cloud?

- **A)** Allow access to an Amazon EC2 instance through only a specific port.
- **B)** Deny access to malicious IP addresses at a subnet level.
- **C)** Protect data that is cached by Amazon CloudFront.
- **D)** Apply a stateless firewall to an Amazon EC2 instance.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Security groups are virtual firewalls that control the inbound and outbound traffic for
Amazon EC2 instances. They can be used to allow access to an Amazon EC2 instance
through only a specific port, such as port 22 for SSH or port 80 for HTTP. Security groups
cannot deny access to malicious IP addresses at a subnet level, as they only allow or deny
traffic based on the rules defined by the customer. To block malicious IP addresses,
customers can use network ACLs, which are stateless firewalls that can be applied to
subnets. Security groups cannot protect data that is cached by Amazon CloudFront, as
they only apply to EC2 instances. To protect data that is cached by Amazon CloudFront,
customers can use encryption, signed URLs, or signed cookies. Security groups are not
stateless firewalls, as they track the state of the traffic and automatically allow the
response traffic to flow back to the source. Stateless firewalls do not track the state of the
traffic and require rules for both inb

</details>

---

### Question 97
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q097`

A company is building a serverless architecture that connects application data from
multiple data sources. The company needs a solution that does not require additional
code.
Which AWS service meets these requirements?

- **A)** AWS Lambda
- **B)** Amazon Simple Queue Service (Amazon SQS)
- **C)** Amazon CloudWatch
- **D)** Amazon EventBridge

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon EventBridge is the service that meets the requirements of building a serverless
architecture that connects application data from multiple data sources without requiring
additional code. Amazon EventBridge is a serverless event bus service that allows you to
easily connect your applications with data from AWS services, SaaS applications, and your
own applications. You can use Amazon EventBridge to create rules that match events and
route them to targets such as AWS Lambda functions, Amazon SNS topics, Amazon SQS
queues, or other AWS services. Amazon EventBridge handles the event ingestion,
delivery, security, authorization, and error handling for you34

</details>

---

### Question 98
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q098`

A company runs its workloads on premises. The company wants to compare the cost of
running its workloads on premises with the cost of running the workloads on AWS.
Which AWS service will meet this requirement?

- **A)** AWS Cost Explorer
- **B)** AWS Budgets
- **C)** AWS Pricing Calculator
- **D)** AWS Trusted Advisor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

According to AWS official documentation, theAWS Pricing Calculatoris designed to
estimate and compare the cost of running workloads on AWS versus on-premises
environments. This service allows customers to model their existing infrastructure,
including compute, storage, and data transfer requirements, and then estimate AWS costs
before migrating. AWS Pricing Calculator supports detailed cost breakdowns for individual
services and helps organizations make informed financial decisions during cloud adoption
planning.
AWS Cost Explorer and AWS Budgets are used onlyafter workloads are already running
on AWSto analyze and manage existing AWS costs. AWS Trusted Advisor provides bestpractice recommendations related to cost optimization, security, fault tolerance, and
performance, but it does not perform cost comparisons with on-premises environments.
AWS documentation explicitly states that the AWS Pricing Calculator is intended forpremigration cost estimation and comparison, maki

</details>

---

### Question 99
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q099`

A company uses Amazon RDS to host its application database.
According to the AWS shared responsibility model, which task is AWS responsible for
when securing this database?

- **A)** Implementing application-level security controls
- **B)** Operating and managing the underlying database infrastructure
- **C)** Encrypting data before storing the data in the database
- **D)** Configuring database user permissions and access controls

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 100
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q100`

A company has teams that have different job roles and responsibilities. The company's
employees often change teams. The company needs to manage permissions for the
employees so that the permissions are appropriate for the job responsibilities.
Which IAM resource should the company use to meet this requirement with the LEAST
operational overhead?

- **A)** IAM user groups
- **B)** IAM roles
- **C)** IAM instance profiles
- **D)** IAM policies for individual users

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

IAM roles are a way of granting temporary permissions to entities that need to access
AWS resources, such as users, applications, or services. IAM roles allow customers to
assign permissions to entities without having to create or manage IAM users or credentials
for them. IAM roles can be assumed by different entities depending on the trust policy
attached to the role. For example, IAM roles can be assumed by IAM users in the same or
different AWS accounts, AWS services such as EC2 or Lambda, or external identities such
as federated users or web identities. IAM roles can also be switched by IAM users to
temporarily change their permissions. IAM roles are recommended for managing
permissions for employees who often change teams, because they allow customers to
define permissions based on job roles and responsibilities, and easily assign or revoke
them as needed. IAM roles also reduce the operational overhead of creating, updating, or
deleting IAM users or credentials for e

</details>

---

### Question 101
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q101`

Which AWS services allow users to monitor and retain records of account activities that
include governance, compliance, and auditing?
(Select TWO.)

- **A)** Amazon CloudWatch
- **B)** AWS CloudTrail
- **C)** Amazon GuardDuty
- **D)** AWS Shield
- **E)** AWS WAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AB`

Amazon CloudWatch and AWS CloudTrail are the AWS services that allow users to
monitor and retain records of account activities that include governance, compliance, and
auditing. Amazon CloudWatch is a service that collects and tracks metrics, collects and
monitors log files, and sets alarms. AWS CloudTrail is a service that enables governance,
compliance, operational auditing, and risk auditing of your AWS account. Amazon

GuardDuty, AWS Shield, and AWS WAF are AWS services that provide security and
protection for AWS resources, but they do not monitor and retain records of account
activities. These concepts are explained in the AWS Cloud Practitioner Essentials course3.

</details>

---

### Question 102
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q102`

A company needs help managing multiple AWS linked accounts that are reported on a
consolidated bill.
Which AWS Support plan includes an AWS concierge whom the company can ask for
assistance?

- **A)** AWS Developer Support
- **B)** AWS Enterprise Support
- **C)** AWS Business Support
- **D)** AWS Basic Support

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Enterprise Support is the AWS Support plan that includes an AWS concierge whom
the company can ask for assistance. According to the AWS Support Plans page, AWS
Enterprise Support provides "a dedicated Technical Account Manager (TAM) who provides
advocacy and guidance to help plan and build solutions using best practices, coordinate
access to subject matter experts, and proactively keep your AWS environment
operationally healthy."2 AWS Business Support, AWS Developer Support, and AWS Basic
Support do not include a TAM or a concierge service.

</details>

---

### Question 103
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q103`

A company needs to migrate a PostgreSQL database from on-premises to Amazon RDS.
Which AWS service or tool should the company use to meet this requirement?

- **A)** Cloud Adoption Readiness Tool
- **B)** AWS Migration Hub
- **C)** AWS Database Migration Service (AWS DMS)
- **D)** AWS Application Migration Service

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Database Migration Service (AWS DMS) is a managed and automated service that
helps you migrate your databases from your on-premises or cloud environment to AWS,
either as a one-time migration or as a continuous replication. AWS DMS supports
migration between 20-plus database and analytics engines, such as PostgreSQL, Oracle,
MySQL, SQL Server, MongoDB, Amazon Aurora, Amazon RDS, Amazon Redshift, and
Amazon S3. AWS DMS also provides schema conversion and validation tools, as well as
monitoring and security features. AWS DMS is a cost-effective and reliable solution for
database migration, as you only pay for the compute resources and additional log storage
used during the migration process, and you can minimize the downtime and data loss with
Multi-AZ and ongoing replication12 To migrate a PostgreSQL database from on-premises
to Amazon RDS using AWS DMS, you need to perform the following steps:

Create an AWS DMS replication instance in the same AWS Region as your target Amazon
RDS

</details>

---

### Question 104
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q104`

A company wants to know more about the benefits offered by cloud computing. The
company wants to understand the operational advantage of agility.
How does AWS provide agility for users?

- **A)** A pay-as-you-go model for many services and resources
- **B)** The ability to provision and deprovision resources quickly with minimal effort
- **C)** The ability the ensure high availability by deploying workloads to multiple regions.
- **D)** The ability to transfer infrastructure management to the AWS Cloud

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 105
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q105`

Which of the following is an advantage of AWS Cloud computing?

- **A)** Trade security for elasticity.
- **B)** Trade operational excellence for agility.
- **C)** Trade fixed expenses for variable expenses.
- **D)** Trade elasticity for performance.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because AWS Cloud computing allows customers to trade fixed
expenses for variable expenses. This means that customers only pay for the resources
they use, and can scale up or down as needed. The other options are incorrect because
they are not advantages of AWS Cloud computing. Trade security for elasticity means that
customers have to compromise on the protection of their data and applications in order to
adjust their capacity quickly. Trade operational excellence for agility means that customers
have to sacrifice the quality and reliability of their operations in order to respond to
changing needs faster. Trade elasticity for performance means that customers have to limit
their ability to scale up or down in order to achieve higher speed and efficiency. Reference:
What is Cloud Computing?

</details>

---

### Question 106
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q106`

What is the MOST secure way to store passwords on AWS?

- **A)** Store passwords in an Amazon S3 bucket.
- **B)** Store passwords as AWS CloudFormation parameters
- **C)** Store passwords in AWS Storage Gateway.
- **D)** Store passwords in AWS Secrets Manager.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Secrets Manageris the most secure way to store and manage sensitive information,
such as passwords, database credentials, and API keys. Secrets Manager allows you to:
Securely store and rotate secrets.
Automatically manage secret rotation without disrupting applications.
Integrate with AWS services and third-party applications to retrieve secrets securely.
Why other options are not suitable:

A . Store passwords in an Amazon S3 bucket: Although S3 is secure, it is not designed for
secret management. It lacks built-in secret rotation and fine-grained access control for
sensitive data.
B . Store passwords as AWS CloudFormation parameters: CloudFormation is used for
managing infrastructure as code, not for securely storing passwords.
C . Store passwords in AWS Storage Gateway: A service for hybrid storage integration, not
suitable for storing secrets or passwords.
Reference:
AWS Secrets Manager Documentation

</details>

---

### Question 107
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q107`

Which task requires the use of AWS account root user credentials?

- **A)** The deletion of IAM users
- **B)** The change to a different AWS Support plan
- **C)** The creation of an organization in AWS Organizations
- **D)** The deletion of Amazon EC2 instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The creation of an organization in AWS Organizations requires the use of AWS account
root user credentials. The AWS account root user is the email address that was used to
create the AWS account. The root user has complete access to all AWS services and
resources in the account, and can perform sensitive tasks such as changing the account
settings, closing the account, or creating an organization. The root user credentials should
be used sparingly and securely, and only for tasks that cannot be performed by IAM users
or roles4

</details>

---

### Question 108
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q108`

A company wants to migrate its on-premises application data to AWS. The company needs
to maintain low-latency access to frequently used data.
Which AWS service will meet these requirements?

- **A)** AWS Database Migration Service (AWS DMS)
- **B)** AWS Application Migration Service
- **C)** AWS Storage Gateway Volume Gateway  D. AWS Direct Connect

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Storage Gateway Volume Gateway, specifically its cached-volume configuration,
meets the stated hybrid-storage requirements. With cached volumes, the primary data is
stored in Amazon S3 while frequently accessed data is retained locally in the gateway's
cache. On-premises application servers access the volumes through the iSCSI protocol,
and the local cache provides low-latency access to the active working set. This design
allows the company to move or extend storage into AWS without requiring every frequently
used block to be retrieved across the network for each access. Therefore, option C is
correct. AWS Database Migration Service migrates and replicates database data, but the
question describes application storage data and persistent low-latency access rather than
a database-engine migration. AWS Application Migration Service moves servers and
applications to AWS and is not a hybrid block-storage caching service. AWS Direct
Connect provides a dedicated network connection between

</details>

---

### Question 109
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q109`

Which AWS service or feature can a company use to create a private, secured, and
scalable network environment in the AWS Cloud?

- **A)** Amazon Elastic Container Service (Amazon ECS)
- **B)** Amazon S3
- **C)** Amazon VPC
- **D)** Route tables

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 110
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q110`

A company wants to log in securely to Linux Amazon EC2 instances.
How can the company accomplish this goal?

- **A)** Use SSH keys.
- **B)** Use a VPN.
- **C)** Use end-to-end encryption.
- **D)** Use Amazon Route 53.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

SSH keys provide secure login for Linux-based Amazon EC2 instances by establishing a
secure connection over SSH (Secure Shell), protecting login credentials from interception.
VPNs and encryption enhance security in other contexts, but SSH keys are the standard
approach for accessing Linux EC2 instances. Amazon Route 53 is unrelated to EC2
instance access.

</details>

---

### Question 111
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q111`

A company wants to migrate its server-based applications to the AWS Cloud. The
company wants to determine the total cost of ownership for its compute resources that will
be hosted on the AWS Cloud.
Which combination of AWS services or tools will meet these requirements?

- **A)** AWS Pricing Calculator
- **B)** Migration Evaluator
- **C)** AWS Support Center
- **D)** AWS Application Discovery Service
- **E)** AWS Database Migration Service (AWS DMS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AD`

AWS Pricing Calculator and AWS Application Discovery Service are the best combination
of AWS services or tools to meet the requirements of determining the total cost of
ownership for compute resources that will be hosted on the AWS Cloud. AWS Pricing
Calculator is a tool that enables you to estimate the cost of using AWS services based on
your usage scenarios and requirements. You can use AWS Pricing Calculator to compare
the costs of running your applications on-premises or on AWS, and to optimize your AWS
spending. AWS Application Discovery Service is a service that helps you plan your
migration to the AWS Cloud by collecting and analyzing information about your onpremises servers, applications, and dependencies. You can use AWS Application
Discovery Service to identify the inventory of your on-premises infrastructure, group
servers by applications, and estimate the performance and resource utilization of your
applications45

</details>

---

### Question 112
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q112`

A company wants to build graph queries for real-time fraud pattern detection.
Which AWS service will meet this requirement?

- **A)** Amazon Neptune
- **B)** Amazon DynamoDB
- **C)** Amazon Timestream
- **D)** Amazon Forecast

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon Neptuneis a fully managed graph database service optimized for storing and
querying highly connected data. It supports popular graph models such as Property Graph
and W3C's RDF, making it ideal for building graph queries for real-time fraud pattern
detection and other applications that require complex relationships and data traversal.
B . Amazon DynamoDB: Incorrect, as it is a NoSQL database service that is not optimized
for graph queries.
C . Amazon Timestream: Incorrect, as it is a time-series database service designed for
storing and analyzing time-series data, not graph data.

D . Amazon Forecast: Incorrect, as it is a fully managed service that provides time-series
forecasting capabilities, not for graph queries.
AWS Cloud Reference:
Amazon Neptune

</details>

---

### Question 113
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q113`

A company is launching a mobile app. The company wants customers to be able to use
the app without upgrading their mobile devices.
Which pillar of the AWS Well-Architected Framework does this goal represent?

- **A)** Security
- **B)** Reliability
- **C)** Cost optimization
- **D)** Sustainability

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Cost optimization is one of the five pillars of the AWS Well-Architected Framework. It
focuses on avoiding unnecessary costs, understanding and controlling where money is
being spent, selecting the most appropriate and right number of resource types, analyzing
spend over time, and scaling to meet business needs without overspending.

</details>

---

### Question 114
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q114`

Amazon Elastic File System (Amazon EFS) and Amazon FSx offer which type of storage?

- **A)** File storage
- **B)** Object storage
- **C)** Block storage
- **D)** Instance store

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon Elastic File System (Amazon EFS) and Amazon FSx offer file storage. File
storage is a type of storage that organizes data into files and folders, and allows multiple
users or applications to access and share the same files over a network. Amazon EFS is a
fully managed, scalable, and elastic file system that supports the Network File System
(NFS) protocol and can be used with Amazon EC2 instances and AWS Lambda functions.
Amazon FSx is a fully managed service that provides two file system options: Amazon FSx
for Windows File Server, which supports the Server Message Block (SMB) protocol and is
compatible with Microsoft Windows applications; and Amazon FSx for Lustre, which is a
high-performance file system that is optimized for compute-intensive workloads

</details>

---

### Question 115
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q115`

Which option is a perspective that includes foundational capabilities of the AWS Cloud
Adoption Framework (AWS CAF)?

- **A)** Sustainability
- **B)** Operations  C. Performance efficiency
- **D)** Reliability

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 116
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q116`

A company wants to migrate its high-performance computing (HPC) application to Amazon
EC2 instances. The application has multiple components. The application must have fault
tolerance and must have the ability to fail over automatically.
Which AWS infrastructure solution will meet these requirements with the LEAST latency
between components?

- **A)** Multiple AWS Regions
- **B)** Multiple edge locations
- **C)** Multiple Availability Zones
- **D)** Regional edge caches

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Using EC2 instances in multiple Availability Zones is an AWS infrastructure solution that
meets the requirements of migrating a high performance computing (HPC) application to
AWS with fault tolerance and failover capabilities, and with the least latency between
components. An Availability Zone is a physically isolated location within an AWS Region
that has its own power, cooling, and network connectivity. EC2 instances within the same
Region can communicate with each other using low-latency private IP addresses. By using
EC2 instances in multiple Availability Zones, the company can achieve fault tolerance and
failover for their HPC application, because they can distribute the workload and data
across different locations that are independent of each other. If one Availability Zone
becomes unavailable or impaired, the company can redirect the traffic and data to another
Availability Zone without affecting the performance and availability of the application5

</details>

---

### Question 117
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q117`

What can a user accomplish using AWS CloudTrail?

- **A)** Generate an IAM user credentials report.
- **B)** Record API calls made to AWS services.
- **C)** Assess the compliance of AWS resource configurations with policies and guidelines.
- **D)** Ensure that Amazon EC2 instances are patched with the latest security updates.A company uses Amazon Workspaces.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS CloudTrail is an AWS service that enables users to accomplish the task of recording
API calls made to AWS services. AWS CloudTrail is a service that tracks user activity and
API usage across the AWS account. AWS CloudTrail records the details of every API call
made to AWS services, such as the identity of the caller, the time of the call, the source IP
address of the caller, the parameters and responses of the call, and more. Users can use
AWS CloudTrail to audit, monitor, and troubleshoot their AWS resources and actions. The
other options are incorrect because they are not tasks that users can accomplish using
AWS CloudTrail. Generating an IAM user credentials report is a task that users can
accomplish using IAM, which is an AWS service that enables users to manage access and
permissions to AWS resources and services. Assessing the compliance of AWS resource
configurations with policies and guidelines is a task that users can accomplish using AWS
Config, which is an AWS service th

</details>

---

### Question 118
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q118`

A company wants to use an AWS networking solution to connect multiple VPCs.
Which AWS service will meet this requirement?

- **A)** AWS Direct Connect
- **B)** AWS Config
- **C)** AWS Transit Gateway
- **D)** Amazon GuardDuty

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 119
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q119`

A company is migrating its applications from on-premises to the AWS Cloud. The company
wants to ensure that the applications are assigned only the minimum permissions that are
needed to perform all operations.
Which AWS service will meet these requirements'?

A. AWS Identity and Access Management (IAM)

- **B)** Amazon CloudWatch
- **C)** Amazon Macie
- **D)** Amazon GuardDuty

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Identity and Access Management (IAM) is a service that helps you securely control
access to AWS resources for your users. You use IAM to control who can use your AWS
resources (authentication) and what resources they can use and in what ways
(authorization). IAM also enables you to follow the principle of least privilege, which means
granting only the permissions that are necessary to perform a task1. Reference: AWS
Identity and Access Management (IAM) - AWS Documentation

</details>

---

### Question 120
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q120`

A company is running a monolithic on-premises application that does not scale and is
difficult to maintain. The company has a plan to migrate the application to AWS and divide
the application into microservices.
Which best practice of the AWS Well-Architected Framework is the company following with
this plan?

- **A)** Integrate functional testing as part of AWS deployment.
- **B)** Use automation to deploy changes.
- **C)** Deploy the application to multiple locations.
- **D)** Implement loosely coupled dependencies.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The company is following the best practice of implementing loosely coupled dependencies
by migrating the application to AWS and dividing the application into microservices.
Loosely coupled dependencies are a design principle of the AWS Well-Architected
Framework that helps to reduce the interdependencies between components and improve
the scalability, reliability, and performance of the system. By breaking down the monolithic
application into smaller, independent, and modular services, the company can reduce the
complexity and maintenance costs, increase the agility and flexibility, and enable faster
and more frequent deployments. AWS CloudFormation is an AWS service that provides
the ability to manage infrastructure as code. Infrastructure as code is a process of defining
and provisioning AWS resources using code or templates, rather than manual actions or
scripts. AWS CloudFormation allows users to create and update stacks of AWS resources
based on predefined templates

</details>

---

### Question 121
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q121`

Which of the following is a fully managed graph database service on AWS?

- **A)** Amazon Aurora
- **B)** Amazon FSx
- **C)** Amazon DynamoDB
- **D)** Amazon Neptune

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon Neptune is a fully managed graph database service on AWS. A graph database is
a type of database that stores and queries data as a network of nodes and edges,
representing entities and relationships. Graph databases are useful for applications that
deal with highly connected data, such as social networks, recommendation engines, fraud
detection, and knowledge graphs45. Amazon Neptune is a fast, reliable, and scalable
graph database service that supports two popular graph models: property graphs and
RDF. Amazon Neptune also supports two open standards for querying graphs: Apache
TinkerPop Gremlin and SPARQL. Amazon Neptune handles the heavy lifting of managing
the database, such as provisioning, patching, backup, recovery, encryption, and
replication456. Reference: 4: Managed Graph Database - Amazon Neptune - AWS, 5:
Amazon Neptune - A Fully Managed Graph Database Service, 6: Working with AWS
Neptune. Neptune is a fully-managed graph ... - Medium

</details>

---

### Question 122
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q122`

Which AWS service will help protect applications running on AWS from DDoS attacks?

- **A)** Amazon GuardDuty
- **B)** AWS WAF
- **C)** AWS Shield
- **D)** Amazon Inspector

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that
safeguards applications running on AWS. AWS Shield provides always-on detection and
automatic inline mitigations that minimize application downtime and latency, so there is no
need to engage AWS Support to benefit from DDoS protection3.

</details>

---

### Question 123
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q123`

Which AWS service provides automated backups of data by default?

- **A)** Amazon S3
- **B)** Amazon Elastic File System (Amazon EFS)
- **C)** Amazon Aurora
- **D)** Amazon ElastiCache (Memcached)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 124
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q124`

A retail company has recently migrated its website to AWS. The company wants to ensure
that it is protected from SQL injection attacks. The website uses an Application Load
Balancer to distribute traffic to multiple Amazon EC2 instances.
Which AWS service or feature can be used to create a custom rule that blocks SQL
injection attacks?

- **A)** Security groups
- **B)** AWS WAF
- **C)** Network ACLs
- **D)** AWS Shield

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS WAF is a web application firewall that helps protect your web applications or APIs
against common web exploits that may affect availability, compromise security, or
consume excessive resources. AWS WAF gives you control over how traffic reaches your
applications by enabling you to create security rules that block common attack patterns,
such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns
you define2. You can use AWS WAF to create a custom rule that blocks SQL injection
attacks on your website.

</details>

---

### Question 125
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q125`

A company has a large number of Linux Amazon EC2 instances across several Availability
Zones in an AWS Region. Applications that run on the EC2 instances need access to a
common set of files.
Which AWS service or device should the company use to meet this requirement?

- **A)** AWS Backup
- **B)** Amazon Elastic File System (Amazon EFS)
- **C)** Amazon Elastic Block Store (Amazon EBS)
- **D)** AWS Snowball Edge Storage Optimized

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Elastic File System (Amazon EFS) is a service that provides a scalable and
elastic file system for Linux-based workloads. It can be mounted on multiple Amazon EC2
instances across different Availability Zones within a region, allowing applications to

access a common set of files1. AWS Backup is a service that provides a centralized and
automated way to back up data across AWS services. Amazon Elastic Block Store
(Amazon EBS) is a service that provides persistent block storage volumes for Amazon
EC2 instances. AWS Snowball Edge Storage Optimized is a device that provides a
petabyte-scale data transport and edge computing solution.

</details>

---

### Question 126
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q126`

A company needs to implement identity management for a fleet of mobile apps that are
running in the AWS Cloud.
Which AWS service will meet this requirement?

- **A)** Amazon Cognito
- **B)** AWS Security Hub
- **C)** AWS Shield
- **D)** AWS WAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon Cognito is a service that provides identity management for mobile and web
applications, allowing users to sign up, sign in, and access AWS resources with different
identity providers. AWS Security Hub is a service that provides a comprehensive view of
the security posture of AWS accounts and resources. AWS Shield is a service that
provides protection against distributed denial of service (DDoS) attacks. AWS WAF is a
web application firewall that helps protect web applications from common web exploits.

</details>

---

### Question 127
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q127`

A company wants to rightsize its Amazon EC2 instances.
Which configuration change will meet this requirement with the LEAST operational
overhead?

- **A)** Add EC2 instances in another Availability Zone.
- **B)** Change the size and type of the EC2 instances based on utilization.
- **C)** Convert the payment method from On-Demand to Savings Plans.
- **D)** Reprovision the EC2 instances with a larger instance type.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Rightsizing involves adjusting instance types based on actual utilization to optimize costs
and performance. Changing the size and type of EC2 instances according to utilization
data achieves this with minimal operational overhead. Adding instances or changing
payment methods does not directly address instance resizing, and reprovisioning with
larger instances may not be optimal based on actual usage.

</details>

---

### Question 128
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q128`

At what support level do users receive access to a support concierge?

- **A)** Basic Support
- **B)** Developer Support  C. Business Support
- **D)** Enterprise Support

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Users receive access to a support concierge at the Enterprise Support level. A support
concierge is a team of AWS billing and account experts that specialize in working with
enterprise accounts. They can help users with billing and account inquiries, cost
optimization, FinOps support, cost analysis, and prioritized answers to billing questions.
The support concierge is included as part of the Enterprise Support plan, which also
provides access to a Technical Account Manager (TAM), Infrastructure Event
Management, AWS Trusted Advisor, and 24/7 technical support. Reference: AWS Support
Plan Comparison, AWS Enterprise Support Plan, AWS Support Concierge

</details>

---

### Question 129
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q129`

A company needs a firewall that will control network connections to and from a single
Amazon EC2 instance. This firewall will not control network connections to and from other
instances that are in the same subnet.
Which AWS service or feature can the company use to meet these requirements?

- **A)** Network ACL
- **B)** AWS WAF
- **C)** Route table
- **D)** Security group

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

ASecurity Groupacts as a virtual firewall for your Amazon EC2 instances to control inbound
and outbound traffic. It provides granular control over network connections to and from a
specific EC2 instance or set of instances. Unlike Network ACLs, which operate at the
subnet level, Security Groups operate at the instance level, allowing control over network
traffic for individual instances.
A . Network ACL: Incorrect, as it controls traffic at the subnet level and not for individual
instances.
B . AWS WAF: Incorrect, as AWS WAF is a web application firewall that helps protect web
applications from common web exploits but is not designed for controlling instance-level
traffic.
C . Route table: Incorrect, as route tables are used for network routing within a VPC and
do not act as firewalls.
AWS Cloud Reference:
AWS Security Groups

</details>

---

### Question 130
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q130`

A company needs to identify who accessed an AWS service and what action was
performed for a given time period.
Which AWS service should the company use to meet this requirement?

A. Amazon CloudWatch

- **B)** AWS CloudTrail
- **C)** AWS Security Hub
- **D)** Amazon Inspector

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS CloudTrail is a service that enables governance, compliance, operational auditing,
and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor,
and retain account activity related to actions across your AWS infrastructure. You can use
CloudTrail to identify who accessed an AWS service and what action was performed for a
given time period. Amazon CloudWatch, AWS Security Hub, and Amazon Inspector are
AWS services that provide different types of monitoring and security capabilities.

</details>

---

### Question 131
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q131`

Which service enables customers to audit API calls in their AWS accounts'?

- **A)** AWS CloudTrail
- **B)** AWS Trusted Advisor
- **C)** Amazon Inspector
- **D)** AWS X-Ray

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS CloudTrail is a service that provides a record of actions taken by a user, role, or an
AWS service in your AWS account. CloudTrail captures all API calls for AWS services as
events, including calls from the AWS Management Console, AWS SDKs, command line
tools, and higher-level AWS services. You can use CloudTrail to monitor, audit, and
troubleshoot your AWS account activity34. AWS Trusted Advisor is a service that provides
best practices recommendations for cost optimization, performance, security, and fault
tolerance in your AWS account5. Amazon Inspector is a service that helps you improve the
security and compliance of your applications deployed on AWS by automatically assessing
them for vulnerabilities and deviations from best practices6. AWS X-Ray is a service that
helps you analyze and debug your applications by collecting data about the requests that
your application serves, and providing tools to view, filter, and gain insights into that data7.
Reference: Logging AWS Audit

</details>

---

### Question 132
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q132`

A company wants to migrate critical on-premises production systems to Amazon EC2
instances. The production instances will be used for at least 3 years. The company wants
a pricing option that will minimize cost.
Which solution will meet these requirements?

- **A)** On-Demand Instances  B. Reserved Instances
- **C)** Spot Instances
- **D)** AWS Free Tier

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Reserved Instances (RIs)offer a significant discount (up to 75%) compared to On-Demand
pricing in exchange for committing to use AWS for a period of 1 or 3 years. This pricing
model is ideal for applications with predictable usage patterns or long-term commitments,
such as critical production systems that will be running for at least 3 years.
A . On-Demand Instances: Incorrect, as they provide flexibility without commitment but are
more expensive over the long term.
C . Spot Instances: Incorrect, as they offer the lowest cost for non-critical, interruptible
workloads but are not suitable for critical production systems due to their potential for
sudden termination.
D . AWS Free Tier: Incorrect, as it provides limited free usage for certain AWS services for
a short period (typically one year) and is not intended for long-term production workloads.
AWS Cloud Reference:
Amazon EC2 Reserved Instances

</details>

---

### Question 133
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q133`

A company needs to run a workload for several batch image rendering applications. It is
acceptable for the workload to experience downtime.
Which Amazon EC2 pricing model would be MOST cost-effective in this situation?

- **A)** On-Demand Instances
- **B)** Reserved Instances
- **C)** Dedicated Instances
- **D)** Spot Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon EC2 Spot Instances are instances that use spare EC2 capacity that is available at
up to a 90% discount compared to On-Demand prices. You can use Spot Instances for
various stateless, fault-tolerant, or flexible applications such as big data, containerized
workloads, high-performance computing (HPC), and test & development workloads. Spot
Instances are ideal for workloads that can be interrupted, such as batch image rendering
applications1. On-Demand Instances are instances that let you pay for compute capacity
by the hour or second (minimum of 60 seconds) with no long-term commitments. This
frees you from the costs and complexities of planning, purchasing, and maintaining
hardware and transforms what are commonly large fixed costs into much smaller variable
costs2. Reserved Instances are instances that provide you with a significant discount (up
to 75%) compared to On-Demand Instance pricing. In exchange, you select a term and
make an upfront payment to reserve a certain amount

</details>

---

### Question 134
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q134`

What is a benefit of moving to the AWS Cloud in terms of improving time to market?

- **A)** Decreased deployment speed
- **B)** Increased application security
- **C)** Increased business agility
- **D)** Increased backup capabilities

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Increased business agility is a benefit of moving to the AWS Cloud in terms of improving
time to market. Business agility refers to the ability of a company to adapt to changing
customer needs, market conditions, and competitive pressures. Moving to the AWS Cloud
enables business agility by providing faster access to resources, lower upfront costs, and
greater scalability and flexibility. By using the AWS Cloud, companies can launch new
products and services, experiment with new ideas, and respond to customer feedback
more quickly and efficiently. For more information, see [Benefits of Cloud Computing] and
[Business Agility].

</details>

---

### Question 135
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q135`

A company needs to use dashboards and charts to analyze insights from business data.
Which AWS service will provide the dashboards and charts for these insights?

- **A)** Amazon Macie
- **B)** Amazon Aurora
- **C)** Amazon QuickSight
- **D)** AWS CloudTrail

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because Amazon QuickSight is an AWS service that will provide
the dashboards and charts for the insights from business data. Amazon QuickSight is a
fully managed, scalable, and serverless business intelligence service that enables users to
create and share interactive dashboards and charts. Amazon QuickSight can connect to
various data sources, such as Amazon S3, Amazon RDS, Amazon Redshift, and more.
Amazon QuickSight also provides users with machine learning insights, such as anomaly
detection, forecasting, and natural language narratives. The other options are incorrect
because they are not AWS services that will provide the dashboards and charts for the
insights from business data. Amazon Macie is an AWS service that helps users discover,
classify, and protect sensitive data stored in Amazon S3. Amazon Aurora is an AWS
service that provides a relational database that is compatible with MySQL and
PostgreSQL. AWS CloudTrail is an AWS service that enables users

</details>

---

### Question 136
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q136`

Which options are benefits of using third-party software from AWS Marketplace? (Select
TWO.)

- **A)** Users do not need to conduct security testing on the software.
- **B)** The software's data encryption is managed by a third-party vendor.
- **C)** Users do not need to upgrade to newer software versions.
- **D)** Users can launch preconfigured software in only a few steps.
- **E)** The software has been evaluated by vendors to ensure that it will run on AWS.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D, E`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 137
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q137`

A company wants to automatically patch its Windows instances that are deployed on
Amazon EC2.
Which AWS service will meet these requirements?

- **A)** AWS Systems Manager
- **B)** AWS Organizations
- **C)** AWS Control Tower
- **D)** Elastic Load Balancing (ELB)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Systems Manager offers the capability to automate patching for Amazon EC2
instances, including Windows instances, through Patch Manager. It can automate patching
tasks, schedule updates, and apply patches based on specified baselines. AWS
Organizations and Control Tower focus on account management and governance, while
Elastic Load Balancing (ELB) is unrelated to patch management.

</details>

---

### Question 138
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q138`

A company hosts its website on Amazon EC2 instances. The company needs to ensure
that the website reaches a global audience and provides minimum latency to users.
Which AWS service should the company use to meet these requirements?

- **A)** Amazon Route 53
- **B)** Amazon CloudFront
- **C)** Elastic Load Balancing  D. AWS Lambda

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon CloudFrontis a content delivery network (CDN) that helps deliver your website
content globally with low latency by caching copies of your website content at edge
locations around the world. This helps ensure that users receive content from the edge
location closest to them, thereby reducing latency and improving user experience.
A . Amazon Route 53: Incorrect, as it is a DNS web service that routes users to the
appropriate endpoint, but it does not cache content or reduce latency.
C . Elastic Load Balancing: Incorrect, as it distributes incoming application or network
traffic across multiple targets, but does not cache content globally.
D . AWS Lambda: Incorrect, as it is a serverless compute service, not intended for content
delivery.
AWS Cloud Reference:
Amazon CloudFront

</details>

---

### Question 139
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q139`

A company needs Amazon EC2 instances for a workload that can tolerate interruptions.
Which EC2 instance purchasing option meets this requirement with the LARGEST
discount compared to On-Demand prices?

- **A)** Spot Instances
- **B)** Convertible Reserved Instances
- **C)** Standard Reserved Instances
- **D)** Dedicated Hosts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Spot Instances are spare Amazon EC2 instances that are available at up to 90% discount
compared to On-Demand prices. They are suitable for workloads that can tolerate
interruptions, such as batch processing, data analysis, and testing. Spot Instances are
allocated based on the current supply and demand, and can be reclaimed by AWS with a
two-minute notice when the demand exceeds the supply5. Convertible Reserved Instances
are a type of Reserved Instances that provide a significant discount (up to 54%) compared
to On-Demand prices and a capacity reservation for Amazon EC2 instances. They are
available in 1-year or 3-year terms and allow users to change the instance family, size,
operating system, or tenancy during the term. Standard Reserved Instances are another
type of Reserved Instances that provide a larger discount (up to 75%) compared to OnDemand prices and a capacity reservation for Amazon EC2 instances. They are available
in 1-year or 3-year terms and do not allow users to chang

</details>

---

### Question 140
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q140`

A company wants to optimize its cloud costs. The company discovers that many of its
cloud resources have more capacity than necessary for current workloads.
Which strategy can the company use to optimize costs?

- **A)** Load balancing
- **B)** Vertical scaling
- **C)** Rightsizing
- **D)** Horizontal scaling

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 141
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q141`

A company has a compute workload that is steady, predictable, and uninterruptible.
Which Amazon EC2 instance purchasing options meet these requirements MOST costeffectively? (Select TWO.)

- **A)** On-Demand Instances
- **B)** Reserved Instances
- **C)** Spot Instances
- **D)** Saving Plans
- **E)** Dedicated Hosts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `BD`

Reserved Instances and Savings Plans are the most cost-effective purchasing options for
a compute workload that is steady, predictable, and uninterruptible. Reserved Instances
provide a significant discount compared to On-Demand Instances, and Savings Plans offer
flexible and consistent savings on EC2 usage. Both options require a commitment to a
consistent amount of usage, in USD per hour, for a term of 1 or 3 years. On-Demand
Instances are suitable for short-term, irregular, or unpredictable workloads, but they are
more expensive than Reserved Instances or Savings Plans. Spot Instances are the
cheapest option, but they are not suitable for uninterruptible workloads, as they can be
reclaimed by AWS at any time. Dedicated Hosts and Dedicated Instances are designed for
compliance and licensing requirements, not for cost optimization. They are more expensive
than the other options, as they run on single-tenant hardware. Reference: Instance
purchasing options, Amazon EC2 Pricing, 4 Ways t

</details>

---

### Question 142
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q142`

Which AWS service gives users on-demand, sell-service access to AWS compliance
control reports?

- **A)** AWS Config
- **B)** Amazon GuardDuty
- **C)** AWS Trusted Advisor
- **D)** AWS Artifact

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Artifact provides on-demand access to AWS compliance reports and security
documentation. It is a self- service portal where customers can download documents like
SOC reports, ISO certifications, and other compliance-related materials necessary for
meeting regulatory requirements. AWS Config and Trusted Advisor offer security
assessments and compliance monitoring, but they do not provide direct access to
compliance reports.

</details>

---

### Question 143
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q143`

Which of the following is a benefit of decoupling an AWS Cloud architecture?

- **A)** Reduced latency
- **B)** Ability to upgrade components independently
- **C)** Decreased costs
- **D)** Fewer components to manage

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

A benefit of decoupling an AWS Cloud architecture is the ability to upgrade components
independently. Decoupling is a way of designing systems to reduce interdependencies and
minimize the impact of changes. Decoupling allows components to interact with each other
through well-defined interfaces, rather than direct references. This reduces the risk of
failures and errors propagating across the system, and enables greater scalability,
availability, and maintainability. By decoupling an AWS Cloud architecture, the user can
upgrade or modify one component without affecting the other components5.

</details>

---

### Question 144
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q144`

A company needs to run its existing custom, nonproduction workloads in the AWS Cloud
quickly and cost-effectively.
The workloads can recover from interruptions easily.
Which pricing model should the company use?

- **A)** Reserved Instances
- **B)** On-Demand Instances
- **C)** Spot Instances
- **D)** Dedicated Hosts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because Spot Instances are the pricing model that enables the
company to run its existing custom, nonproduction workloads in the AWS Cloud quickly
and cost-effectively. Spot Instances are spare Amazon EC2 instances that are available at
up to 90% discount compared to On-Demand prices. Spot Instances are suitable for
stateless, fault-tolerant, and flexible workloads that can recover from interruptions easily.
The other options are incorrect because they are not the pricing model that enables the
company to run its existing custom, nonproduction workloads in the AWS Cloud quickly
and cost-effectively. Reserved Instances are Amazon EC2 instances that are reserved for
a specific period of time (one or three years) in exchange for a lower hourly rate. Reserved

Instances are suitable for steady-state or predictable workloads that run for a long
duration. On-Demand Instances are Amazon EC2 instances that are launched and billed at
a fixed hourly rate. On-Demand Insta

</details>

---

### Question 145
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q145`

An IT engineer needs to access AWS services from an on-premises application.
Which credentials or keys does the application need for authentication?

- **A)** AWS account user name and password
- **B)** IAM access key and secret
- **C)** Amazon EC2 key pairs
- **D)** AWS Key Management Service (AWS KMS) keys

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

IAM access keys are long-term credentials that consist of an access key ID and a secret
access key. You use access keys to sign programmatic requests that you make to AWS. If
you need to access AWS services from an on-premises application, you can use IAM
access keys to authenticate your requests. AWS account user name and password are
used to sign in to the AWS Management Console. Amazon EC2 key pairs are used to
connect to your EC2 instances using SSH. AWS Key Management Service (AWS KMS)
keys are used to encrypt and decrypt your data using the AWS Encryption SDK or the
AWS CLI.

</details>

---

### Question 146
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q146`

Which task is the shared responsibility of the customer and AWS under the AWS shared
responsibility model?

- **A)** Managing guest operating systems
- **B)** Installing hardware infrastructure
- **C)** Managing security
- **D)** Protecting the physical infrastructure that runs all services

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 147
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q147`

Which AWS service is designed to help users handle large amounts of data in a data
warehouse environment?

- **A)** Amazon RDS
- **B)** Amazon DynamoDB
- **C)** Amazon Redshift
- **D)** Amazon Aurora

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Redshiftis a fully managed data warehouse service that enables users to analyze
large amounts of data quickly and cost-effectively. It is designed specifically for online
analytical processing (OLAP) and is optimized for complex queries against large datasets.
Amazon Redshift uses columnar storage, data compression, and massively parallel
processing (MPP) to handle petabyte-scale data warehouse environments.
A . Amazon RDS: Incorrect, as it is a managed relational database service for online
transaction processing (OLTP) workloads, not specifically designed for data warehousing.
B . Amazon DynamoDB: Incorrect, as it is a NoSQL database service for fast and flexible
data storage, not a data warehouse.
D . Amazon Aurora: Incorrect, as it is a MySQL- and PostgreSQL-compatible relational
database designed for high performance and availability for OLTP workloads, not data
warehousing.
AWS Cloud Reference:
Amazon Redshift

</details>

---

### Question 148
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q148`

Which of the following services can be used to block network traffic to an instance? (Select
TWO.)

- **A)** Security groups
- **B)** Amazon Virtual Private Cloud (Amazon VPC) flow logs
- **C)** Network ACLs
- **D)** Amazon CloudWatch
- **E)** AWS CloudTrail

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

Security groups and network ACLs are two AWS services that can be used to block
network traffic to an instance. Security groups are virtual firewalls that control the inbound
and outbound traffic for your instances at the instance level. You can specify which
protocols, ports, and source or destination IP addresses are allowed or denied for each
instance. Security groups are stateful, which means that they automatically allow return
traffic for any allowed inbound or outbound traffic123. Network ACLs are virtual firewalls
that control the inbound and outbound traffic for your subnets at the subnet level. You can
create rules to allow or deny traffic based on protocols, ports, and source or destination IP
addresses. Network ACLs are stateless, which means that you have to explicitly allow
return traffic for any allowed inbound or outbound traffic456. Reference: 1: Security groups
for your VPC - Amazon Virtual Private Cloud, 2: Security Groups for Your VPC - Amazon
Elastic Compute Cloud,

</details>

---

### Question 149
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q149`

Which database engine is compatible with Amazon RDS?

- **A)** Apache Cassandra
- **B)** MongoDB
- **C)** Neo4j
- **D)** PostgreSQL

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon RDS supports six database engines: Amazon Aurora, MySQL, MariaDB,
PostgreSQL, Oracle, and SQL Server. Apache Cassandra, MongoDB, and Neo4j are not
compatible with Amazon RDS. Therefore, the correct answer is D. You can learn more
about Amazon RDS and its supported database engines

</details>

---

### Question 150
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q150`

A company wants to migrate its database to a managed AWS service that is compatible
with PostgreSQL.
Which AWS services will meet these requirements? (Select TWO)

- **A)** Amazon Athena
- **B)** Amazon RDS
- **C)** Amazon EC2
- **D)** Amazon DynamoDB
- **E)** Amazon Aurora

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `BE`

Amazon RDS and Amazon Aurora are both managed AWS services that support the
PostgreSQL database engine. Amazon RDS makes it easier to set up, operate, and scale
PostgreSQL deployments on the cloud, while Amazon Aurora is a cloud-native database
engine that is compatible with PostgreSQL and offers higher performance and availability.
Amazon Athena is a serverless query service that does not support PostgreSQL, but can
analyze data in Amazon S3 using standard SQL. Amazon EC2 is a compute service that
allows users to launch virtual machines, but does not provide any database management
features. Amazon DynamoDB is a NoSQL database service that is not compatible with
PostgreSQL, but offers fast and consistent performance at any scale. Reference: Hosted
PostgreSQL - Amazon RDS for PostgreSQL - AWS, Amazon RDS for PostgreSQL Amazon Relational Database Service, AWS PostgreSQL: Managed or Self-Managed? NetApp, AWS Announces Amazon Aurora Supports PostgreSQL 12 - InfoQ, Amazon
Aurora vs Postgre

</details>

---

### Question 151
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q151`

A company is requesting Payment Card Industry (PCI) reports that validate the operating
effectiveness of AWS security controls.
How should the company obtain these reports?

- **A)** Contact AWS Support  B. Download reports from AWS Artifact.
- **C)** Download reports from AWS Security Hub.
- **D)** Contact an AWS technical account manager (TAM).

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Artifact is a service provided by AWS that offers on-demand access to AWS
compliance reports, including the Payment Card Industry (PCI) reports. It is the primary
tool for retrieving compliance reports such as Service Organization Control (SOC) reports,
ISO certifications, and Payment Card Industry Data Security Standard (PCI DSS) reports.
To obtain these reports:
The company should log into the AWS Management Console and navigate to AWS
Artifact.
From there, they can select and download the necessary compliance reports.
Why other options are not suitable:
A . Contact AWS Support: AWS Support is not needed to obtain these reports; they are
readily available through AWS Artifact.
C . Download reports from AWS Security Hub: AWS Security Hub is a service that
provides a comprehensive view of security alerts and compliance status, but it does not
host or provide compliance reports like PCI DSS.
D . Contact an AWS technical account manager (TAM): While a TAM may assist in

</details>

---

### Question 152
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q152`

Which benefits does a company gain when the company moves from on-premises IT
architecture to the AWS Cloud? (Select TWO.)

- **A)** Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and procurement
- **B)** Elimination of the need for trained IT staff
- **C)** Automatic security configuration of all applications that are migrated to the cloud
- **D)** Elimination of the need for disaster recovery planning  E. Faster deployment of new features and applications

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AE`

When a company moves from on-premises IT architecture to the AWS Cloud, it gains
several benefits:
A . Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and
procurement: In an on-premises environment, companies must maintain their own
hardware, which involves procuring servers, configuring them, managing capacity, and
troubleshooting hardware failures. Moving to the AWS Cloud eliminates or greatly reduces
these tasks since AWS is responsible for the underlying infrastructure.
E . Faster deployment of new features and applications: AWS provides scalable resources
and automation tools that allow companies to deploy applications faster. Services like
AWS Elastic Beanstalk, AWS CloudFormation, and AWS Lambda help streamline the
deployment process, enabling quicker time-to-market for new features and applications.
Why other options are not suitable:
B . Elimination of the need for trained IT staff: While the cloud reduces certain operational
burdens, it does not e

</details>

---

### Question 153
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q153`

A company is creating a web application that requires a relational database to store
customer data. Which AWS service should the company use to host the database?

- **A)** Amazon Redshift
- **B)** Amazon Aurora
- **C)** Amazon ElastiCache
- **D)** Amazon DynamoDB

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 154
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q154`

A company wants to create a globally accessible ecommerce platform for its customers.
The company wants to use a highly available and scalable DNS web service to connect
users to the platform.
Which AWS service will meet these requirements?

- **A)** Amazon EC2  B. Amazon VPC
- **C)** Amazon Route 53
- **D)** Amazon RDS

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web
service that can route internet traffic to the company's ecommerce platform1. Route 53 can
also register domain names, check the health of resources, and provide global DNS
features2. Route 53 can connect users to the platform by translating human-readable
names like www.example.com into the numeric IP addresses that computers use to
communicate with each other2. Reference: 1: Amazon Route 53 | DNS Service | AWS; 2:
What is Amazon Route 53? - Amazon Route 53

</details>

---

### Question 155
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q155`

Which of the following actions are controlled with AWS Identity and Access Management
(IAM)? (Select TWO.)

- **A)** Control access to AWS service APIs and to other specific resources.
- **B)** Provide intelligent threat detection and continuous monitoring.
- **C)** Protect the AWS environment using multi-factor authentication (MFA).
- **D)** Grant users access to AWS data centers.
- **E)** Provide firewall protection for applications from common web attacks.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

AWS Identity and Access Management (IAM) is a service that enables you to manage
access to AWS services and resources securely. You can use IAM to perform the following
actions:
Control access to AWS service APIs and to other specific resources: You can create
users, groups, roles, and policies that define who can access which AWS resources and
how. You can also use IAM to grant temporary access to users or applications that need to
perform certain tasks on your behalf3 Protect the AWS environment using multi-factor
authentication (MFA): You can enable MFA for your IAM users and root user to add an
extra layer of security to your AWS account. MFA requires users to provide a unique
authentication code from an approved device or SMS text message, in addition to their
user name and password, when they sign in to AWS4

</details>

---

### Question 156
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q156`

A company wants to reduce the time its employees spend on database maintenance tasks.
Which option presents a benefit of using Amazon RDS?

- **A)** Provides better query performance than self-managed databases
- **B)** Supports more database engines than self-managed databases
- **C)** Automatically handles database backups and software patching
- **D)** Provides automatic horizontal scaling for read and write workloads

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Relational Database Service reduces database administration work by managing
common operational tasks. AWS documentation states that Amazon RDS manages
activities including database backups, software patching, automatic failure detection, and
recovery. Customers can configure settings such as backup retention periods and
maintenance windows, while RDS performs the underlying managed operations.
Therefore, option C is correct. Amazon RDS does not automatically guarantee better query
performance than a self-managed database. Query performance depends on database
design, indexing, SQL queries, instance sizing, data distribution, and workload
characteristics, and customers remain responsible for query tuning. RDS also supports a
defined set of database engines rather than necessarily supporting more engines than any
self-managed environment. Automatic horizontal scaling for both read and write workloads
is not a general feature of every RDS engine or configuration. S

</details>

---

### Question 157
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q157`

A company uses AWS for its web application. The company wants to minimize latency and
perform compute operations for the application as close to end users as possible.
Which AWS service or infrastructure component will provide this functionality?

- **A)** AWS Regions
- **B)** Availability Zones
- **C)** Edge locations
- **D)** AWS Direct Connect

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Edge locations are sites that Amazon CloudFront uses to cache copies of your content for
faster delivery to users at any location. You can use Amazon CloudFront to deliver your
entire website, including dynamic, static, streaming, and interactive content using a global
network of edge locations. Requests for your content are automatically routed to the
nearest edge location, so content is delivered with the best possible performance3. Edge
locations can also host AWS Lambda functions to perform compute operations for your
web application as close to end users as possible4.

</details>

---

### Question 158
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q158`

Which AWS service provides this functionality?

- **A)** AWS IAM Identity Center (AWS Single Sign-On)
- **B)** AWS Systems Manager
- **C)** AWS Config
- **D)** AWS Control Tower

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Control Tower is a service that provides an easy way to set up and govern a secure,
multi-account AWS environment. It automates the creation of accounts, organizational
units, policies, and best practices based on the AWS Well-Architected Framework. AWS
IAM Identity Center (AWS Single Sign-On) is a service that enables users to centrally
manage access to multiple AWS accounts and business applications using a single signon experience. AWS Systems Manager is a service that provides operational management
for AWS resources and applications. AWS Config is a service that enables users to
assess, audit, and evaluate the configurations of AWS resources.

</details>

---

### Question 159
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q159`

A company wants to migrate its applications from its on-premises data center to a VPC in
the AWS Cloud. These applications will need to access on-premises resources. Which
actions will meet these requirements? (Select TWO.)

- **A)** Use AWS Service Catalog to identify a list of on-premises resources that can be migrated.
- **B)** Use an Amazon CloudFront distribution and configure it to accelerate content delivery close to the on-premises resources
- **C)** Set up an AWS Direct Connect connection between the on-premises data center and AWS.
- **D)** Create a VPN connection between an on-premises device and a virtual private gateway in the VPC.
- **E)** Use Amazon CloudFront to restrict access to static web content provided through the on-premises web servers.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CD`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 160
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q160`

A company is developing a web application that uses containers. The company needs a
repository to store and control access to container images.

- **A)** Amazon Elastic Kubernetes Service (Amazon EKS)
- **B)** Amazon Elastic Container Registry (Amazon ECR)
- **C)** Amazon Elastic Container Service (Amazon ECS)
- **D)** Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 161
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q161`

How does the AWS Enterprise Support Concierge team help users?

- **A)** Supporting application development
- **B)** Providing architecture guidance
- **C)** Answering billing and account inquiries
- **D)** Answering questions regarding technical support cases

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS Enterprise Support Concierge team is a group of billing and account experts who
specialize in working with enterprise customers. They can help customers with questions
about billing, account management, cost optimization, and other non-technical issues.
They can also assist customers with navigating and optimizing their AWS environment,
such as setting up consolidated billing, applying for service limit increases, or requesting
refunds.
Reference:
AWS Support Plan Comparison
AWS Enterprise Support Plan
Answer Explained: Which AWS Support plan provides access to AWS Concierge Support
team for account assistance?

</details>

---

### Question 162
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q162`

A company must archive Amazon S3 data that the company's business units no longer
need to access.
Which S3 storage class will meet this requirement MOST cost-effectively?

- **A)** S3 Glacier Instant Retrieval
- **B)** S3 Glacier Flexible Retrieval
- **C)** S3 Glacier Deep Archive
- **D)** S3 One Zone-Infrequent Access (S3 One Zone-IA)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

S3 Glacier Deep Archive is Amazon S3's lowest-cost storage class and supports long-term
retention and digital preservation for data that may be accessed once or twice in a year. It
is designed for customers - particularly those in highly-regulated industries, such as the
Financial Services, Healthcare, and Public Sectors - that retain data sets for 7-10 years or
longer to meet regulatory compliance requirements. Customers can store large amounts of
data at a very low cost, and reliably access it with a wait time of 12 hours3.

</details>

---

### Question 163
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q163`

What does the concept of agility mean in AWS Cloud computing? (Select TWO.)

- **A)** The speed at which AWS resources are implemented
- **B)** The speed at which AWS creates new AWS Regions
- **C)** The ability to experiment quickly
- **D)** The elimination of wasted capacity
- **E)** The low cost of entry into cloud computing

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

Agility in AWS Cloud computing means the ability to rapidly provision and deprovision
AWS resources as needed, and the ability to experiment quickly with new ideas and
solutions. Agility helps businesses to respond to changing customer demands, market
opportunities, and competitive threats, and to innovate faster and cheaper. Agility also
reduces the risk of failure, as businesses can test and validate their assumptions before

committing to large-scale deployments. Some of the benefits of agility in AWS Cloud
computing are:
The speed at which AWS resources are implemented: AWS provides a variety of services
and tools that allow you to create, configure, and launch AWS resources in minutes, using
the AWS Management Console, the AWS Command Line Interface (AWS CLI), the AWS
Software Development Kits (AWS SDKs), or the AWS CloudFormation templates. You can
also use the AWS Cloud Development Kit (AWS CDK) to define your AWS resources as
code using familiar programming languages, and synt

</details>

---

### Question 164
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q164`

A company needs to run code in response to an event notification that occurs when
objects are uploaded to an Amazon S3 bucket.
Which AWS service will integrate directly with the event notification?

- **A)** AWS Lambda
- **B)** Amazon EC2
- **C)** Amazon Elastic Container Registry (Amazon ECR)
- **D)** AWS Elastic Beanstalk

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Lambda is a service that lets you run code without provisioning or managing servers.
You can use Lambda to process event notifications from Amazon S3 when objects are
uploaded or deleted. Lambda integrates directly with the event notification and invokes
your code automatically. Therefore, the correct answer is A.

</details>

---

### Question 165
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q165`

Which actions are best practices for an AWS account root user? (Select TWO.)

- **A)** Share root user credentials with team members.
- **B)** Create multiple root users for the account, separated by environment.
- **C)** Enable multi-factor authentication (MFA) on the root user.
- **D)** Create an IAM user with administrator privileges for daily administrative tasks, instead of using the root user.
- **E)** Use programmatic access instead of the root user and password.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CD`

The AWS account root user is the identity that has complete access to all AWS services
and resources in the account. It is accessed by signing in with the email address and
password that were used to create the account1. The root user should be protected and
used only for a few account and service management tasks that require it1. Therefore, the
following actions are best practices for an AWS account root user:
Enable multi-factor authentication (MFA) on the root user. MFA is a security feature that
requires users to provide two or more pieces of information to authenticate themselves,
such as a password and a code from a device. MFA adds an extra layer of protection for
the root user credentials, which can access sensitive information and perform critical
operations in the account2.
Create an IAM user with administrator privileges for daily administrative tasks, instead of
using the root user. IAM is a service that helps customers manage access to AWS
resources for users and groups.

</details>

---

### Question 166
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q166`

Which AWS service or feature enables users to encrypt data at rest in Amazon S3?

- **A)** IAM policies
- **B)** Server-side encryption
- **C)** Amazon GuardDuty
- **D)** Client-side encryption

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Server-side encryption is an encryption option that Amazon S3 provides to encrypt data at
rest in Amazon S3. With server-side encryption, Amazon S3 encrypts an object before
saving it to disk in its data centers and decrypts it when you download the objects. You
have three server-side encryption options to choose from: SSE-S3, SSE-C, and SSE-KMS.
SSE-S3 uses keys that are managed by Amazon S3. SSE-C allows you to manage your
own encryption keys. SSE-KMS uses keys that are managed by AWS Key Management
Service (AWS KMS)5.

</details>

---

### Question 167
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q167`

According to security best practices, how should an Amazon EC2 instance be given
access to an Amazon S3 bucket?

- **A)** Hard code an IAM user's secret key and access key directly in the application, and upload the file.
- **B)** Store the IAM user's secret key and access key in a text file on the EC2 instance, read the keys, then upload the file.
- **C)** Have the EC2 instance assume a role to obtain the privileges to upload the file.
- **D)** Modify the S3 bucket policy so that any service can upload to it at any time.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

According to security best practices, the best way to give an Amazon EC2 instance access
to an Amazon S3 bucket is to have the EC2 instance assume a role to obtain the privileges
to upload the file. A role is an AWS Identity and Access Management (IAM) entity that
defines a set of permissions for making AWS service requests. You can use roles to
delegate access to users, applications, or services that don't normally have access to your
AWS resources. For example, you can create a role that allows EC2 instances to access
S3 buckets, and then attach the role to the EC2 instance. This way, the EC2 instance can
assume the role and obtain temporary security credentials to access the S3 bucket. This
method is more secure and scalable than storing or hardcoding IAM user credentials on
the EC2 instance, as it avoids the risk of exposing or compromising the credentials. It also
allows you to manage the permissions centrally and dynamically, and to audit the access
using AWS CloudTrail. For more

</details>

---

### Question 168
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q168`

Which maintenance task is the customer's responsibility, according to the AWS shared
responsibility model?

- **A)** Physical connectivity among Availability Zones
- **B)** Network switch maintenance
- **C)** Hardware updates and firmware patches
- **D)** Amazon EC2 updates and security patches

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

According to the AWS shared responsibility model, customers are responsible for
managing their data, applications, operating systems, security groups, and other aspects
of their AWS environment. This includes installing updates and security patches of the
guest operating system and any application software or utilities installed by the customer
on the instances. AWS is responsible for protecting the infrastructure that runs all of the
services offered in the AWS Cloud, such as data centers, hardware, software, networking,
and facilities. This includes the physical connectivity among Availability Zones, the network
switch maintenance, and the hardware updates and firmware patches. Therefore, option D
is the correct answer, and options A, B, and C are AWS responsibilities, not customer
responsibilities. Reference: : AWS Well-Architected Framework - Elasticity; : Reactive
Systems on AWS - Elastic

</details>

---

### Question 169
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q169`

Which AWS service can provide users with instant access to their desktop applications
from anywhere?

- **A)** Amazon AppStream 2.0
- **B)** Amazon Lightsail
- **C)** AWS Resource Access Manager (AWS RAM)
- **D)** AWS Client VPN

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon AppStream 2.0 is the former exam name for the service currently documented as
Amazon WorkSpaces Applications. It is a fully managed application-streaming service that
allows organizations to centrally host desktop applications and stream them to users.
Users can access applications through supported clients or an HTML5-capable web
browser without installing the complete application locally. This provides the instant,
location-independent application access described in the question, making option A
correct. Amazon Lightsail is a simplified service for virtual private servers, containers,
databases, networking, and web application hosting. AWS Resource Access Manager
allows supported AWS resources to be shared across accounts or within AWS
Organizations. AWS Client VPN provides managed remote network connectivity to AWS
and connected networks, but it does not host and stream desktop applications by itself.
WorkSpaces Applications can maintain centrally managed application images,

</details>

---

### Question 170
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q170`

A company that has multiple business units wants to centrally manage and govern its AWS
Cloud environments. The company wants to automate the creation of AWS accounts,
apply service control policies (SCPs), and simplify billing processes.
Which AWS service or tool should the company use to meet these requirements?

- **A)** AWS Organizations
- **B)** Cost Explorer
- **C)** AWS Budgets
- **D)** AWS Trusted Advisor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Organizations is an AWS service that enables you to centrally manage and govern
your AWS Cloud environments across multiple business units. AWS Organizations allows
you to create an organization that consists of AWS accounts that you create or invite to
join. You can group your accounts into organizational units (OUs) and apply service control
policies (SCPs) to them. SCPs are a type of policy that specify the maximum permissions
for the accounts in your organization, and can help you enforce compliance and security
requirements. AWS Organizations also simplifies billing processes by enabling you to
consolidate and pay for all member accounts with a single payment method. You can also
use AWS Organizations to automate the creation of AWS accounts by using APIs or AWS
CloudFormation templates. Reference: What is AWS Organizations?, Policy-Based
Management - AWS Organizations

</details>

---

### Question 171
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q171`

Which of the following is a cost efficiency principle related to the AWS Cloud?

- **A)** Right-size services based on capacity requirements.
- **B)** Use the Billing Dashboard to access information about monthly bills.
- **C)** Use AWS Organizations to combine the expenses of multiple accounts into a single bill.
- **D)** Tag all AWS resources.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

One of the cost efficiency principles related to the AWS Cloud is to right-size services
based on capacity requirements. This means choosing the most appropriate type and size
of AWS resources to meet the performance and scalability needs of the applications, while
avoiding over-provisioning or under-provisioning. By right-sizing services, users can
optimize the costs and benefits of using the AWS Cloud1

</details>

---

### Question 172
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q172`

A company is reviewing the design of an application that will be migrated from on premises
to a single Amazon EC2 instance.
What should the company do to make the application highly available?

- **A)** Provision additional EC2 instances in other Availability Zones.
- **B)** Configure an Application Load Balancer (ALB). Assign the EC2 instance as the ALB's target.
- **C)** Use an Amazon Machine Image (AMI) to create the EC2 instance.
- **D)** Provision the application by using an EC2 Spot Instance.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Provisioning additional EC2 instances in other Availability Zones is a way to make the
application highly available, as it reduces the impact of failures and increases fault
tolerance. Configuring an Application Load Balancer and assigning the EC2 instance as
the ALB's target is a way to distribute traffic among multiple instances, but it does not
make the application highly available if there is only one instance. Using an Amazon
Machine Image to create the EC2 instance is a way to launch a virtual server with a
preconfigured operating system and software, but it does not make the application highly
available by itself. Provisioning the application by using an EC2 Spot Instance is a way to
use spare EC2 capacity at up to 90% off the On-Demand price, but it does not make the
application highly available, as Spot Instances can be interrupted by EC2 with a twominute notification.

</details>

---

### Question 173
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q173`

When a user wants to utilize their existing per-socket, per-core, or per-virtual machine
software licenses for a Microsoft Windows server running on AWS, which Amazon EC2
instance type is required?

- **A)** Spot Instances
- **B)** Dedicated Instances
- **C)** Dedicated Hosts
- **D)** Reserved Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because Dedicated Hosts are Amazon EC2 instances that are
required when a user wants to utilize their existing per-socket, per-core, or per-virtual
machine software licenses for a Microsoft Windows server running on AWS. Dedicated
Hosts are physical servers that are dedicated to a single customer. Dedicated Hosts allow
customers to use their existing server-bound software licenses, such as Windows Server,
SQL Server, and SUSE Linux Enterprise Server, subject to their license terms. The other
options are incorrect because they are not Amazon EC2 instances that are required when
a user wants to utilize their existing per-socket, per-core, or per-virtual machine software
licenses for a Microsoft Windows server running on AWS. Spot Instances are spare
Amazon EC2 instances that are available at up to 90% discount compared to On-Demand
prices. Spot Instances are suitable for stateless, fault-tolerant, and flexible workloads that

can recover from interr

</details>

---

### Question 174
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q174`

Which of the following is a managed AWS service that is used specifically for extract,
transform, and load (ETL) data?

- **A)** Amazon Athena
- **B)** AWS Glue
- **C)** Amazon S3
- **D)** AWS Snowball Edge

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Glue is a serverless data integration service that makes it easy to discover, prepare,
move, and integrate data from multiple sources for analytics, machine learning, and
application development. You can use various data integration engines, such as ETL, ELT,
batch, and streaming, and manage your data in a centralized data catalog. AWS Glue is
designed specifically for extract, transform, and load (ETL) data, whereas the other options
are not.

</details>

---

### Question 175
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q175`

A company wants to push VPC Flow Logs to an Amazon S3 bucket.
A company wants to optimize long-term compute costs of AWS Lambda functions and
Amazon EC2 instances.
Which AWS purchasing option should the company choose to meet these requirements?

- **A)** Dedicated Hosts
- **B)** Compute Savings Plans
- **C)** Reserved Instances
- **D)** Spot Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Compute Savings Plans are a flexible and cost-effective way to optimize long-term
compute costs of AWS Lambda functions and Amazon EC2 instances. With Compute
Savings Plans, customers can commit to a consistent amount of compute usage
(measured in $/hour) for a 1-year or 3-year term and receive a discount of up to 66%
compared to On-Demand prices3. Dedicated Hosts are physical servers with EC2 instance
capacity fully dedicated to the customer's use. They are suitable for customers who have
specific server-bound software licenses or compliance requirements4. Reserved Instances

are a pricing model that provides a significant discount (up to 75%) compared to OnDemand pricing and a capacity reservation for EC2 instances. They are available in 1-year
or 3-year terms and different payment options5. Spot Instances are spare EC2 instances
that are available at up to 90% discount compared to On-Demand prices. They are suitable
for customers who have flexible start and end times,

</details>

---

### Question 176
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q176`

Which design principles support the reliability pillar of the AWS Well-Architected
Framework? (Select TWO.)

- **A)** Perform operations as code.
- **B)** Enable traceability.
- **C)** Automatically scale to meet demand.
- **D)** Deploy resources globally to improve response time.
- **E)** Automatically recover from failure.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CE`

The design principles that support the reliability pillar of the AWS Well-Architected
Framework are: automatically scale to meet demand, and automatically recover from
failure. These principles help users design systems that can handle changes in load, avoid
disruptions, and resume normal operations quickly. Automatically scaling to meet demand
means adjusting the capacity of the system based on the current and anticipated workload,
using services such as AWS Auto Scaling, Amazon EC2, and AWS Lambda. Automatically
recovering from failure means detecting and resolving issues, using services such as
Amazon CloudWatch, AWS CloudFormation, and AWS CloudTrail

</details>

---

### Question 177
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q177`

A company is in the process of finding correct Amazon EC2 instance types and sizes to
meet its performance and capacity requirements. The company wants to find the lowest
possible cost.
Which option accurately characterizes the company's actions?

- **A)** Auto Scaling
- **B)** Rightsizing
- **C)** Storage tiering
- **D)** Instance scheduling

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 178
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q178`

A company needs to reserve a certain amount of Amazon EC2 compute resources in a
specific Availability Zone within an AWS Region. Which purchasing option should the
company use to meet this requirement?

- **A)** Compute Savings Plans  B. EC2 Instance Savings Plans
- **C)** Zonal Reserved Instances
- **D)** Regional Reserved Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 179
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q179`

Which AWS service can run a managed PostgreSQL database that provides online
transaction processing (OLTP)?

- **A)** Amazon DynamoDB
- **B)** Amazon Athena
- **C)** Amazon RDS
- **D)** Amazon EMR

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon RDS is a fully managed relational database service that supports several
database engines, including PostgreSQL. Amazon RDS can run a managed PostgreSQL
database that provides online transaction processing (OLTP), which is a type of database
workload that handles frequent read and write operations on small amounts of data.
Amazon RDS for PostgreSQL offers high performance, availability, scalability, security,
and compatibility with the PostgreSQL community edition. Amazon RDS also provides
automated backups, point-in-time recovery, encryption, monitoring, and maintenance for
PostgreSQL databases. Reference:
Hosted PostgreSQL - Amazon RDS for PostgreSQL
OLTP Database, MySQL And PostgreSQL Managed Database - Amazon Aurora
PostgreSQL options on AWS: Self- managed, managed, and serverless

</details>

---

### Question 180
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q180`

A user wants to invoke an AWS Lambda function when an Amazon EC2 instance enters
the "stopping" state.
Which AWS service is appropriate for this use case?

- **A)** Amazon EventBridge
- **B)** AWS Config
- **C)** Amazon Simple Notification Service (Amazon SNS)
- **D)** AWS CloudFormation

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon EventBridge (formerly CloudWatch Events) allows users to respond to changes in
the state of AWS resources. It can be configured to invoke an AWS Lambda function when
an EC2 instance enters the "stopping" state, providing a serverless way to automate
responses to changes in EC2 instance states. AWS Config, SNS, and CloudFormation do
not provide direct triggering for specific instance state changes.

</details>

---

### Question 181
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q181`

Which AWS service or tool does AWS Control Tower use to create resources?

- **A)** AWS CloudFormation
- **B)** AWS Trusted Advisor
- **C)** AWS Directory Service
- **D)** AWS Cost Explorer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Control Tower uses AWS CloudFormation to create resources in your landing zone.
AWS CloudFormation is a service that helps you model and set up your AWS resources
using templates. AWS Control Tower supports creating
AWS::ControlTower::EnabledControl resources in AWS CloudFormation. Therefore, the
correct answer is A. You can learn more about AWS Control Tower and AWS
CloudFormation

</details>

---

### Question 182
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q182`

A company needs to evaluate its AWS environment and provide best practice
recommendations in five categories: cost, performance, service limits, fault tolerance, and
security. Which AWS service can the company use to meet these requirements?

- **A)** AWS Shield
- **B)** AWS WAF
- **C)** AWS Trusted Advisor
- **D)** AWS Service Catalog

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Trusted Advisor is the service that can meet these requirements. AWS Trusted
Advisor is a service that helps you optimize your AWS environment by providing
recommendations based on AWS best practices. Trusted Advisor continuously evaluates
your AWS resources and services across five categories: cost optimization, performance,
service limits, fault tolerance, and security. You can view the recommendations on the
Trusted Advisor console or access them programmatically using the Trusted Advisor API.
You can also set up notifications and alerts for any changes in the status of your checks.
Trusted Advisor can help you improve your AWS environment by reducing costs,
enhancing performance, increasing security, and ensuring reliability12. The other services
are not designed to provide best practice recommendations in five categories. AWS Shield

is a service that protects your AWS resources from distributed denial-of-service (DDoS)
attacks. AWS WAF is a service that helps you protect you

</details>

---

### Question 183
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q183`

A company wants to develop a shopping application that records customer orders. The
application needs to use an AWS managed database service to store data.
Which AWS service should the company use to meet these requirements?

- **A)** Amazon RDS
- **B)** Amazon Redshift
- **C)** Amazon ElastiCache
- **D)** Amazon Neptune

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

A is correct because Amazon RDS is the AWS service that provides a managed relational
database service that supports various database engines, such as MySQL, PostgreSQL,
Oracle, and SQL Server. B is incorrect because Amazon Redshift is the AWS service that
provides a managed data warehouse service that is optimized for analytical queries. C is
incorrect because Amazon ElastiCache is the AWS service that provides a managed inmemory data store service that supports Redis and Memcached. D is incorrect because
Amazon Neptune is the AWS service that provides a managed graph database service
that supports property graph and RDF models.

</details>

---

### Question 184
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q184`

In which of the following AWS services should database credentials be stored for
maximum security?

- **A)** AWS Identity and Access Management (IAM)
- **B)** AWS Secrets Manager
- **C)** Amazon S3
- **D)** AWS Key Management Service (AWS KMS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Secrets Manager is the AWS service where database credentials should be stored
for maximum security. AWS Secrets Manager helps to protect the secrets, such as
database credentials, passwords, API keys, and tokens, that are used to access
applications, services, and resources. AWS Secrets Manager enables secure storage,
encryption, rotation, and retrieval of the secrets. AWS Secrets Manager also integrates
with other AWS services, such as AWS Identity and Access Management (IAM), AWS Key
Management Service (AWS KMS), and AWS Lambda. For more information, see [What is
AWS Secrets Manager?] and [Getting Started with AWS Secrets Manager].

</details>

---

### Question 185
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q185`

A company plans to migrate its custom marketing application and order-processing
application to AWS. The company needs to deploy the applications on different types of
instances with various configurations of CPU, memory, storage, and networking capacity.
Which AWS service should the company use to meet these requirements?

- **A)** AWS Lambda
- **B)** Amazon Cognito
- **C)** Amazon Athena
- **D)** Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 186
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q186`

A company needs to block SOL injection attacks.
Which AWS service or feature provides this functionality?

- **A)** AWS WAF
- **B)** Network ACLs
- **C)** Security groups
- **D)** AWS Trusted Advisor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS WAF is a web application firewall that helps protect applications from SQL injection
attacks and other common web exploits. By defining rules to block, allow, or monitor
specific types of requests, AWS WAF provides an effective defense against SQL injection.
Network ACLs and Security Groups provide network- level security but do not inspect web
traffic for specific attack patterns like SQL injection.

</details>

---

### Question 187
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q187`

A company needs to search for text in documents that are stored in Amazon S3.
Which AWS service will meet these requirements?

- **A)** Amazon Kendra
- **B)** Amazon Rekognition
- **C)** Amazon Polly
- **D)** Amazon Lex

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon Kendra is a highly accurate and easy to use intelligent search service powered by
machine learning. It enables users to easily find the content they are looking for, even
when it is scattered across multiple locations and content repositories within their
organization. Amazon Kendra supports natural language queries, and can search for text
in documents stored in Amazon S3, as well as other sources such as SharePoint,
OneDrive, Salesforce, ServiceNow, and more1.
Amazon Rekognition is a computer vision service that makes it easy to add image and
video analysis to applications. It can detect objects, faces, text, scenes, activities, and
emotions in images and videos. However, it is not designed for searching for text in
documents stored in Amazon S32.
Amazon Polly is a text-to-speech service that turns text into lifelike speech. It can create
audio versions of books, articles, podcasts, and more. However, it is not designed for
searching for text in documents stored

</details>

---

### Question 188
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q188`

A company's gaming application has been gaining popularity. There has been high
demand for the gaming application in countries where the company does not currently
deploy the application.
Which advantage of the AWS Cloud can help the company to deploy the application to
more countries around the world?

- **A)** Increase speed and agility
- **B)** Go global in minutes
- **C)** Trade fixed expense for variable expense
- **D)** Benefit from massive economies of scale

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The AWS Cloud's global infrastructure enables rapid deployment across multiple
geographic regions, allowing companies to extend applications to new markets quickly.
This capability to "go global in minutes" is especially valuable for businesses looking to
reach customers in new countries without building data centers. Other options, like speed
and agility, are advantages but do not specifically address global deployment.

</details>

---

### Question 189
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q189`

A company wants to migrate a company's on-premises container Infrastructure to the AWS
Cloud. The company wants to prevent unplanned administration and operation cost and
adapt to a serverless architecture.
Which AWS service will meet these requirements?

- **A)** Amazon Connect
- **B)** AWS Fargate
- **C)** Amazon Lightsail
- **D)** Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Fargateis a serverless compute engine for containers that allows users to run
containers without having to manage the underlying infrastructure. Fargate eliminates the
need for managing servers and reduces operational overhead, providing a fully managed,
serverless approach to containerized applications. It helps avoid unplanned administration
and operational costs and is ideal for companies migrating from on-premises container
infrastructure.
Why other options are not suitable:
A . Amazon Connect: A service for cloud-based contact centers, not for container
management.
C . Amazon Lightsail: Simplifies virtual private server (VPS) management but is not
serverless or specialized for containers.
D . Amazon EC2: Provides virtual servers but requires more manual administration and is
not serverless.
Reference:
AWS Fargate Documentation

</details>

---

### Question 190
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q190`

Which AWS service provides storage-optimized and compute-optimized device
configurations?

- **A)** AWS Snowcone
- **B)** AWS Storage Gateway
- **C)** AWS Snowball Edge
- **D)** AWS DataSync

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Snowball Edge offers configurations that are either storage-optimized or computeoptimized, providing flexibility for different data migration and processing needs. It supports
local processing and data transfer to AWS, catering to scenarios that require heavy
storage or compute resources. AWS Snowcone and DataSync do not offer these
optimizations, and Storage Gateway focuses on hybrid cloud storage.

</details>

---

### Question 191
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q191`

Which guidelines are best practices for using AWS Identity and Access Management
(1AM)? (Select TWO.)

- **A)** Share access keys.
- **B)** Create individual 1AM users.
- **C)** Use inline policies instead of customer managed policies.
- **D)** Grant maximum privileges to 1AM users.
- **E)** Use groups to assign permissions to 1AM users.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `BE`

Best practices for using AWS Identity and Access Management (IAM) include:
B . Create individual IAM users: Each user should have their own IAM credentials to
ensure accountability, control, and traceability. Sharing credentials can lead to security
risks and difficulty in auditing.
E . Use groups to assign permissions to IAM users: Assigning permissions through IAM
groups simplifies permission management. You can assign the necessary permissions to
the group, and then add or remove users from the group as needed, rather than managing
permissions for each user individually.
Why other options are not suitable:
A . Share access keys: Sharing access keys is a security risk and violates AWS security
best practices. Each user should have their own credentials.
C . Use inline policies instead of customer-managed policies: Customer-managed policies
are preferred over inline policies because they offer better control, reusability, and
versioning.
D . Grant maximum privileges to IAM users: Gran

</details>

---

### Question 192
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q192`

A company is planning to migrate its application to the AWS Cloud.
Which AWS tool or set of resources should the company use to analyze and asses its
readiness for migration?

- **A)** AWS Cloud Adoption Framework (AWS CAF)
- **B)** AWS Pricing Calculator
- **C)** AWS Well-Architected Framework  D. AWS Budgets

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Cloud Adoption Framework (AWS CAF) is a tool that helps organizations understand
how cloud adoption transforms the way they work, and it provides structure to identify and
address gaps in skills and processes. Applying the AWS CAF in your organization results
in an actionable plan that helps you prepare the cloud environment, enable your staff with
new skills, and migrate your applications. AWS Pricing Calculator is a tool that helps you
estimate the cost of AWS services for your use cases and compare the cost of different
AWS service configurations. AWS Well-Architected Framework is a tool that helps you
review and improve your cloud-based architectures and better understand the business
impact of your design decisions. AWS Budgets is a tool that helps you plan your service
usage, service costs, and instance reservations, and track how close your plan is to your
budgeted amount.

</details>

---

### Question 193
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q193`

Which actions are the responsibility of AWS. according to the AWS shared responsibility
model? (Select TWO.)

- **A)** Securing the virtualization layer
- **B)** Patching the operating system on Amazon RDS instances
- **C)** Patching the operating system on Amazon EC2 instances
- **D)** Configuring security groups and network ACLs
- **E)** Enforcing a strict password policy for 1AM users

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AB`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 194
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q194`

A company recently migrated to the AWS Cloud. The company needs to determine
whether its newly imported Amazon EC2 instances are the appropriate size and type.
Which AWS services can provide this information to the company? {Select TWO.)

- **A)** AWS Auto Scaling
- **B)** AWS Control Tower
- **C)** AWS Trusted Advisor
- **D)** AWS Compute Optimizer
- **E)** Amazon Forecast

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CD`

AWS Trusted Advisor and AWS Compute Optimizer are the AWS services that can provide
information to the company about whether its newly imported Amazon EC2 instances are
the appropriate size and type. AWS Trusted Advisor is an online tool that provides best
practices recommendations in five categories: cost optimization, performance, security,
fault tolerance, and service limits. AWS Trusted Advisor can help users identify
underutilized or idle EC2 instances, and suggest ways to reduce costs and improve
performance. AWS Compute Optimizer is a service that analyzes the configuration and

utilization metrics of EC2 instances and delivers recommendations for optimal instance
types, sizes, and configurations. AWS Compute Optimizer helps users improve
performance, reduce costs, and eliminate underutilized resources

</details>

---

### Question 195
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q195`

A company is building an application that will receive millions of database queries each
second. The company needs the data store for the application to scale to meet these
needs.
Which AWS service will meet this requirement?

- **A)** Amazon DynamoDB
- **B)** AWS Cloud9
- **C)** Amazon ElastiCache for Memcached
- **D)** Amazon Neptune

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon DynamoDB is the AWS service that will meet the requirement of building an
application that will receive millions of database queries each second. Amazon DynamoDB
is a fully managed NoSQL database service that provides fast and consistent performance,
scalability, and durability. Amazon DynamoDB can handle any level of request traffic and
automatically scale up or down the capacity based on the demand. Amazon DynamoDB
also supports in-memory caching with Amazon DynamoDB Accelerator (DAX) to improve
the response time and reduce the cost. For more information, see What is Amazon
DynamoDB? and Amazon DynamoDB Features.

</details>

---

### Question 196
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q196`

An application runs on multiple Amazon EC2 instances that access a shared file system
simultaneously.
Which AWS storage service should be used?

- **A)** Amazon EBS
- **B)** Amazon EFS
- **C)** Amazon S3
- **D)** AWS Artifact

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Elastic File System (Amazon EFS) is the AWS storage service that should be
used for an application that runs on multiple Amazon EC2 instances that access a shared
file system simultaneously. Amazon EFS is a fully managed service that provides a
scalable, elastic, and highly available file system for Linux-based workloads. Amazon EFS
supports the Network File System version 4 (NFSv4) protocol and allows multiple EC2
instances to read and write data to the same file system concurrently. Amazon EFS also
integrates with other AWS services, such as AWS Backup, AWS CloudFormation, and
AWS CloudTrail. For more information, see What is Amazon Elastic File System? and
[Amazon EFS Use Cases].

</details>

---

### Question 197
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q197`

Which AWS service or feature provides information about governance monitoring and risk
auditing of AWS accounts?

- **A)** AWS Trusted Advisor
- **B)** AWS CloudTrail
- **C)** Amazon CloudWatch
- **D)** VPC Flow Logs

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 198
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q198`

What is an Availability Zone?

- **A)** A location where users can deploy compute, storage, database, and other select AWS services where no AWS Region currently exists
- **B)** One or more discrete data centers with redundant power, networking, and connectivity
- **C)** One or more clusters of servers where new workloads can be deployed
- **D)** A fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to users globally

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

An Availability Zone is one or more discrete data centers with redundant power,
networking, and connectivity. Availability Zones are part of the AWS global infrastructure,
which consists of AWS Regions, Availability Zones, and edge locations. Availability Zones
are physically separate locations within an AWS Region that are engineered to be isolated
from failures and connected by low-latency, high-throughput, and highly redundant
networking. Each Availability Zone contains one or more data centers that house the
servers and storage devices that run AWS services. Availability Zones enable users to
design and operate fault-tolerant and high-availability applications on AWS. AWS Global
InfrastructureAWS Certified Cloud Practitioner - aws.amazon.com

</details>

---

### Question 199
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q199`

A company deploys its application to multiple AWS Regions and configures automatic
failover between those Regions.

Which cloud concept does this architecture represent?

- **A)** Security
- **B)** Reliability
- **C)** Scalability
- **D)** Cost optimization

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Reliability is the cloud concept that this architecture represents. Reliability is the ability of a
system to recover from infrastructure or service disruptions, dynamically acquire computing
resources to meet demand, and mitigate disruptions such as misconfigurations or transient
network issues. Deploying an application to multiple AWS Regions and configuring
automatic failover between those Regions enhances the reliability of the application by
reducing the impact of regional failures and increasing the availability of the application4

</details>

---

### Question 200
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q200`

A company wants to query its server logs to gain insights about its customers'
experiences.
Which AWS service will store this data MOST cost-effectively?

- **A)** Amazon Aurora
- **B)** Amazon Elastic File System (Amazon EFS)
- **C)** Amazon Elastic Block Store (Amazon EBS)
- **D)** Amazon S3

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon S3 is an AWS service that provides scalable, durable, and cost-effective object
storage in the cloud. Amazon S3 can store any amount and type of data, such as server
logs, and offers various storage classes with different performance and pricing
characteristics. Amazon S3 is the most cost-effective option for storing server logs, as it
offers low-cost storage classes, such as S3 Standard-Infrequent Access (S3 Standard-IA)
and S3 Intelligent-Tiering, that are suitable for infrequently accessed or changing access
patterns data. Amazon S3 also integrates with other AWS services, such as Amazon
Athena and Amazon OpenSearch Service, that can query the server logs directly from S3
without requiring any additional data loading or transformation. Reference: Amazon S3,
Amazon S3 Storage Classes, Querying Data in Amazon S3

</details>

---

### Question 201
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q201`

A company needs to track the activity in its AWS accounts, and needs to know when an
API call is made against its AWS resources. Which AWS tool or service can be used to
meet these requirements?

- **A)** Amazon CloudWatch
- **B)** Amazon Inspector
- **C)** AWS CloudTrail
- **D)** AWS IAM

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS CloudTrail is the service that can be used to meet these requirements. AWS
CloudTrail is a service that records AWS API calls for your account and delivers log files to
you. The recorded information includes the identity of the API caller, the time of the API
call, the source IP address of the API caller, the request parameters, and the response
elements returned by the AWS service1. You can use CloudTrail to track the activity in
your AWS accounts, such as who made an API call, when it was made, and what
resources were affected. You can also use CloudTrail to monitor the compliance, security,
and governance of your AWS environment2. The other services are not designed to track
the activity and API calls in your AWS accounts. Amazon CloudWatch is a service that
monitors and collects metrics, logs, and events from your AWS resources and applications.
You can use CloudWatch to set alarms, visualize data, and automate actions based on
predefined thresholds or rules3. Amazon Inspector

</details>

---

### Question 202
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q202`

Which AWS service is always provided at no charge?

- **A)** Amazon S3
- **B)** AWS Identity and Access Management (IAM)
- **C)** Elastic Load Balancers
- **D)** AWS WAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Identity and Access Management (IAM) is a web service that helps you securely
control access to AWS resources. You can use IAM to create and manage AWS users and
groups, and use permissions to allow and deny their access to AWS resources. IAM is
always provided at nocharge12. Reference: 1: AWS Identity and Access Management
(IAM) - Amazon Web Services (AWS), 2: Which aws service is always provided at no
charge? - Brainly.in

</details>

---

### Question 203
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q203`

Which of the following is a fully managed MySQL-compatible database?

- **A)** Amazon S3
- **B)** Amazon DynamoDB
- **C)** Amazon Redshift
- **D)** Amazon Aurora

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon Aurora is a fully managed MySQL-compatible database that combines the
performance and availability of traditional enterprise databases with the simplicity and costeffectiveness of open-source databases. Amazon Aurora is part of the Amazon Relational
Database Service (Amazon RDS) family, which means it inherits the benefits of a fully
managed service, such as automated backups, patches, scaling, monitoring, and security.
Amazon Aurora also offers up to five times the throughput of standard MySQL, as well as
high availability, durability, and fault tolerance with up to 15 read replicas, cross-Region
replication, and self-healing storage. Amazon Aurora is compatible with the latest versions
of MySQL, as well as PostgreSQL, and supports various features and integrations that
enhance its functionality and usability123 Amazon Aurora, Amazon RDS, AWS - Amazon
Aurora Overview

</details>

---

### Question 204
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q204`

Which AWS Support plan provides customers with access to an AWS technical account
manager (TAM)?

- **A)** AWS Basic Support
- **B)** AWS Developer Support
- **C)** AWS Business Support
- **D)** AWS Enterprise Support

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The correct answer is D because AWS Enterprise Support is the support plan that provides
customers with access to an AWS technical account manager (TAM). AWS Enterprise
Support is the highest level of support plan offered by AWS, and it provides customers with
the most comprehensive and personalized support experience. An AWS TAM is a
dedicated technical resource who works closely with customers to understand their
business and technical needs, provide proactive guidance, and coordinate support across
AWS teams. The other options are incorrect because they are not support plans that
provide customers with access to an AWS TAM. AWS Basic Support is the default and
free support plan that provides customers with access to online documentation, forums,
and account information. AWS Developer Support is the lowest level of paid support plan
that provides customers with access to technical support during business hours, general
guidance, and best practice recommendations. AWS Bu

</details>

---

### Question 205
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q205`

Which AWS service is deployed to VPCs and provides protection from common network
threats?

- **A)** AWSShield  B. AWSWAF
- **C)** AWS Network Firewall
- **D)** AWS FirewallManager

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Network Firewall is a managed service that makes it easy to deploy essential
network protections for all of your Amazon Virtual Private Clouds (VPCs). The service can
be set up with just a few clicks from the AWS console or using APIs. AWS Network
Firewall automatically scales with your network traffic, so you don't have to worry about
deploying and managing any infrastructure. AWS Network Firewall provides protection
from common network threats such as SQL injection, cross-site scripting, and DDoS
attacks1.

</details>

---

### Question 206
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q206`

Which tasks are the responsibility of AWS, according to the AWS shared responsibility
model? (Select TWO.)

- **A)** Patch AWS network devices.
- **B)** Set user password rules.
- **C)** Provide physical security for compute resources.
- **D)** Configure security groups.
- **E)** Patch the operating system of an Amazon EC2 instance.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A, C`

The correct answers are A and C because patching AWS network devices and providing
physical security for compute resources are tasks that are the responsibility of AWS,
according to the AWS shared responsibility model. The AWS shared responsibility model
is a framework that defines the division of responsibilities between AWS and the customer
for security and compliance. AWS is responsible for the security of the cloud, which
includes the global infrastructure, such as the regions, availability zones, and edge
locations; the hardware, software, networking, and facilities that run the AWS services; and
the virtualization layer that separates the customer instances and storage. The customer is
responsible for the security in the cloud, which includes the customer data, the guest
operating systems, the applications, the identity and access management, the firewall
configuration, and the encryption. The other options are incorrect because they are tasks
that are the responsib

</details>

---

### Question 207
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q207`

A software engineer wants to launch a virtual machine (VM) and MySQL database on
AWS.
Which AWS service will meet these requirements with the LEAST operational effort?

A. Amazon Elastic Container Service (Amazon ECS)

- **B)** AWS Elastic Beanstalk
- **C)** Amazon Lightsail
- **D)** Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Elastic Beanstalk is a service that enables you to quickly deploy and manage
applications in the AWS Cloud without worrying about the infrastructure that runs those
applications. You simply upload your application, and Elastic Beanstalk automatically
handles the details of capacity provisioning, load balancing, scaling, and application health
monitoring. Elastic Beanstalk supports several platform configurations for Java, .NET,
PHP, Node.js, Python, Ruby, Go, and Docker web applications that can run on familiar
servers such as Apache, Nginx, Passenger, and IIS. You can also use Elastic Beanstalk to
launch a virtual machine (VM) and MySQL database on AWS with the least operational
effort. Amazon Elastic Container Service (Amazon ECS) is a fully managed container
orchestration service that enables you to easily run, scale, and secure Docker
containerized applications on AWS. However, it requires more operational effort than
Elastic Beanstalk, as you need to define your application ar

</details>

---

### Question 208
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q208`

Which benefit of the AWS Cloud helps companies achieve lower usage costs because of
the aggregate usage of all AWS users?

- **A)** No need to guess capacity
- **B)** Ability to go global in minutes
- **C)** Economies of scale
- **D)** Increased speed and agility

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The benefit of the AWS Cloud that helps companies achieve lower usage costs because of
the aggregate usage of all AWS users is economies of scale. Economies of scale means
that AWS can achieve lower costs and higher efficiency by operating at a massive scale
and passing the savings to the customers. AWS leverages the aggregate usage of all AWS
users to negotiate better prices with hardware vendors, optimize power consumption, and

improve operational processes. As a result, AWS can offer lower and more flexible pricing
options to the customers, such as pay-as-you-go, reserved, and spot pricing models. No
need to guess capacity, ability to go global in minutes, and increased speed and agility are
other benefits of the AWS Cloud, but they are not directly related to the aggregate usage of
all AWS users. No need to guess capacity means that AWS customers can avoid the risk
of over-provisioning or under-provisioning resources, and scale up or down as needed.
Ability to go global in minute

</details>

---

### Question 209
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q209`

Which action is a security best practice for access to sensitive data that is stored in an
Amazon S3 bucket?

- **A)** Enable S3 Cross-Region Replication (CRR) on the S3 bucket.
- **B)** Use IAM roles for applications that require access to the S3 bucket.
- **C)** Configure AWS WAF to prevent unauthorized access to the S3 bucket.
- **D)** Configure Amazon GuardDuty to prevent unauthorized access to the S3 bucket.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Understanding IAM Roles: IAM (Identity and Access Management) roles in AWS are
designed to delegate access permissions without sharing long-term security credentials.
This means applications and services can use temporary security credentials, which
enhances security.
Why IAM Roles are Best Practice:
Least Privilege Principle: By using IAM roles, you can ensure that applications only have
the minimum permissions they need to function, reducing the risk of unauthorized access.
Temporary Credentials: Roles provide temporary security credentials, which reduce the
risk if they are compromised compared to long-term access keys.
Automated Rotation: Temporary credentials automatically expire and are rotated, which
means you don't have to manage the rotation manually.
How to Implement IAM Roles:
Create an IAM Role: In the AWS Management Console, navigate to IAM, and create a new
role. Choose the type of trusted entity (e.g., EC2, Lambda).
Attach Policies: Attach the necessary policies to the r

</details>

---

### Question 210
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q210`

A company is using a central data platform to manage multiple types of data for its
customers. The company wants to use AWS services to discover, transform, and visualize
the data.
Which combination of AWS services should the company use to meet these requirements?
(Select TWO.)

- **A)** AWS Glue
- **B)** Amazon Elastic File System (Amazon EFS)
- **C)** Amazon Redshift
- **D)** Amazon QuickSight
- **E)** Amazon Quantum Ledger Database (Amazon QLDB)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy
to prepare and load data for analytics. AWS Glue can discover data sources, transform
data, and make it available for analysis by using data catalogs and workflows. Amazon
Redshift is a fully managed, petabyte-scale data warehouse service in the cloud that
enables customers to analyze data using standard SQL and existing business intelligence
tools. Amazon Redshift can also integrate with other AWS services to visualize and
transform data. Amazon Elastic File System (Amazon EFS) provides a simple, scalable,
fully managed elastic NFS file system for use with AWS Cloud services and on-premises
resources. Amazon QuickSight is a fast, cloud-powered business intelligence service that
makes it easy to deliver insights to everyone in an organization. Amazon Quantum Ledger
Database (Amazon QLDB) is a fully managed ledger database that provides a transparent,
immutable, and cryptographically verifiable tra

</details>

---

### Question 211
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q211`

A company stores 5 TB of data in Amazon S3. The company plans to occasionally run
queries on the data for analysis.
Which AWS service should the company use to run these queries MOST cost-effectively?

- **A)** Amazon Kinesis Data Streams
- **B)** Amazon Athena
- **C)** Amazon RDS
- **D)** Amazon Redshift

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 212
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q212`

Which AWS service or feature captures information about the network traffic to and from
an Amazon EC2 instance?

- **A)** VPC Reachability Analyzer
- **B)** Amazon Athena
- **C)** VPC Flow Logs
- **D)** AWS X-Ray

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 213
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q213`

Which cloud computing advantage is a company applying when it uses AWS Regions to
increase application availability to users in different countries?

- **A)** Pay-as-you-go pricing
- **B)** Capacity forecasting
- **C)** Economies of scale
- **D)** Global reach

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Global reach is a cloud computing advantage that a company can apply when it uses AWS
Regions to increase application availability to users in different countries. Global reach

refers to the ability to deploy applications and services in multiple geographic locations
around the world, and to serve customers with low latency and high performance. AWS
has the largest and most reliable global infrastructure of any cloud provider, with 25
Regions and 81 Availability Zones across the Americas, Europe, Asia Pacific, Africa, and
the Middle East123. By using AWS Regions, a company can choose the best location for
its application based on customer proximity, compliance requirements, and disaster
recovery strategies23. Reference: 1: AWS Global Infrastructure - Amazon Web Services
(AWS), 2: Regions and Availability Zones - Amazon Elastic Compute Cloud, 3: AWS
Infrastructure: Regions and Availability Zones Explained

</details>

---

### Question 214
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q214`

Which action should a company take to improve security in its AWS account?

- **A)** Require multi-factor authentication (MFA) for privileged users.
- **B)** Remove the root user account.
- **C)** Create an access key for the AWS account root user.
- **D)** Create an access key for each privileged user.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Enforcing multi-factor authentication (MFA) for privileged users enhances account security
by requiring a second form of authentication. It reduces the risk of unauthorized access,
even if credentials are compromised. Removing the root account is not possible, and
creating access keys for the root account or privileged users can increase security risks
rather than reduce them.

</details>

---

### Question 215
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q215`

Which AWS Cloud design principle is a company using when the company implements
AWS CloudTrail?

- **A)** Activate traceability.
- **B)** Use serverless compute architectures.
- **C)** Perform operations as code.
- **D)** Go global in minutes.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

By implementingAWS CloudTrail, a company is adhering to the AWS Cloud design
principle ofactivating traceability. AWS CloudTrail provides detailed logs of all API calls
made in an AWS account, which helps monitor, troubleshoot, and detect unusual activity,
thereby improving security and compliance. This supports the principle of "activating
traceability" by enabling continuous monitoring and auditing of all actions and changes
within the AWS environment.
B . Use serverless compute architectures: Incorrect, as this principle encourages the use
of managed services that handle infrastructure, such as AWS Lambda, and is not directly
related to CloudTrail.

C . Perform operations as code: Incorrect, as this principle emphasizes the use of code
and automation for infrastructure management.
D . Go global in minutes: Incorrect, as this principle relates to the global deployment of
applications and services.
AWS Cloud Reference:
AWS Well-Architected Framework
AWS CloudTrail

</details>

---

### Question 216
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q216`

A company wants to add a conversational chatbot to its website.
Which AWS service can the company use to meet this requirement?

- **A)** Amazon Textract
- **B)** Amazon Lex
- **C)** AWS Glue
- **D)** Amazon Rekognition

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Lexis a service for building conversational interfaces into any application using
voice and text. It provides the tools necessary to create, test, and publish intelligent
chatbots that can be integrated with web applications to provide a conversational
experience.
A . Amazon Textract: Incorrect, as it is a service for extracting text and data from
documents, not for creating chatbots.
C . AWS Glue: Incorrect, as it is a data integration service used for preparing and
transforming data.
D . Amazon Rekognition: Incorrect, as it is an image and video analysis service.
AWS Cloud Reference:
Amazon Lex

</details>

---

### Question 217
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q217`

A company wants to manage its cloud resources by using infrastructure as code (laC)
template.....
Which AWS service should the company use to meet these requirements?

- **A)** AWS Artifact
- **B)** AWS Resource Explorer
- **C)** AWS License Manager
- **D)** AWS Service Catalog

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Service Catalog enables companies to create, manage, and distribute catalogs of
approved infrastructure as code (IaC) templates and software configurations. This service
supports infrastructure automation by allowing users to deploy resources using predefined
templates, which align with the company's policies and best practices. It helps in managing

cloud resources at scale by utilizing IaC principles, enabling consistent deployments, and
enforcing governance across AWS resources. AWS Service Catalog is an excellent choice
for organizations implementing IaC.

</details>

---

### Question 218
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q218`

A company migrated its systems to the AWS Cloud. The systems are rightsized, and a
security review did not reveal any issues. The company must ensure that additional
developments, integrations, changes, and system usage growth do not jeopardize this
optimized AWS infrastructure.
Which AWS service should the company use to report ongoing optimization and security?

- **A)** AWS Trusted Advisor
- **B)** AWS Health Dashboard
- **C)** Amazon Connect
- **D)** AWS Systems Manager

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Trusted Advisoris a service that provides real-time guidance to help you provision
your resources following AWS best practices. It offers checks in five categories: cost
optimization, performance, security, fault tolerance, and service limits. By continuously
monitoring the AWS environment, AWS Trusted Advisor helps ensure that additional
developments, integrations, changes, and growth do not jeopardize the optimized
infrastructure by providing ongoing optimization and security recommendations.
B . AWS Health Dashboard: Incorrect, as it provides personalized view of service health
and status updates but does not offer continuous optimization and security advice.
C . Amazon Connect: Incorrect, as it is a contact center service, not related to
infrastructure optimization or security.
D . AWS Systems Manager: Incorrect, as it provides operational insights and management
for AWS resources but is not specifically focused on ongoing optimization and security
checks.
AWS Cloud Reference:

</details>

---

### Question 219
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q219`

Which option presents a benefit of using managed services?

- **A)** Eliminate the need to manage underlying infrastructure
- **B)** Provide better performance than self-managed infrastructure
- **C)** Provide unlimited storage capacity
- **D)** Support more applications than self-managed infrastructure

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

A primary benefit of an AWS managed service is that AWS takes responsibility for more of
the underlying infrastructure and routine operational work. Depending on the service, AWS
can handle activities such as hardware provisioning, infrastructure maintenance, service

software patching, availability mechanisms, and scaling of the managed platform. This
allows customers to concentrate more heavily on application logic, data, business
requirements, and customer-facing improvements instead of performing undifferentiated
infrastructure administration. Therefore, option A is the supported general benefit. A
managed service does not automatically guarantee better performance than every possible
self-managed implementation; performance depends on architecture, configuration,
workload characteristics, and selected capacity. Managed services also do not provide
unlimited storage. Each service has supported capacities, quotas, technical limits, and
pricing considerations, even when it can scale

</details>

---

### Question 220
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q220`

Which AWS service or tool inspects a user's AWS environment and makes
recommendations for cost savings and system performance improvements?

- **A)** Cost Explorer
- **B)** Amazon Inspector
- **C)** AWS Trusted Advisor
- **D)** AWS Budgets

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 221
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q221`

A developer needs to build an application for a retail company. The application must
provide real-time product recommendations that are based on machine learning.
Which AWS service should the developer use to meet this requirement?

- **A)** AWS Health Dashboard
- **B)** Amazon Personalize
- **C)** Amazon Forecast
- **D)** Amazon Transcribe

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Personalize is a fully managed machine learning service that customers can use
to generate personalized recommendations for their users. It can also generate user
segments based on the users' affinity for certain items or item metadata. Amazon
Personalize uses the customers' data to train and deploy custom recommendation models
that can be integrated into their applications. Therefore, the correct answer is B. You can
learn more about Amazon Personalize and its use case.

</details>

---

### Question 222
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q222`

Which top-level key performance indicator (KPI) is available in AWS rightsizing
recommendations of Cost Optimization?

- **A)** Container modernization opportunities
- **B)** Estimated monthly saving
- **C)** Reserved instances savings
- **D)** Compute savings recommendations

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Understanding Cost Optimization Recommendations: In AWS, cost optimization involves
identifying ways to reduce costs while maintaining or improving performance and capacity.
Top-Level KPI - Estimated Monthly Saving:
Definition: This KPI provides an estimate of how much you can save per month by
following the recommended actions.
Importance: It helps you quantify the potential cost savings from rightsizing, purchasing
reserved instances, or optimizing resource usage.
Decision-Making: Provides a clear financial benefit to justify changes in your resource
configurations.
How to Use Estimated Monthly Saving:
Access Recommendations: Navigate to the AWS Cost Management Console to view
rightsizing recommendations.
Review Savings Estimates: Look at the estimated monthly savings for each
recommendation to understand the potential financial impact.
Implement Recommendations: Prioritize actions based on the savings estimates to
maximize cost reduction.
AWS Cost Management
AWS Rightsizing Recommen

</details>

---

### Question 223
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q223`

A company wants to avoid unnecessary charges and run workloads at the lowest price
point. Which pillar of the AWS Well-Architected Framework includes these goals?

- **A)** Reliability
- **B)** Sustainability
- **C)** Security
- **D)** Cost optimization

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 224
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q224`

Which AWS service or tool provides a visualization of historical AWS spending patterns
and projections of future AWS costs?

- **A)** AWS Cos! and Usage Report
- **B)** AWS Budgets
- **C)** Cost Explorer  D. Amazon CloudWatch

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Cost Explorer provides a visualization of historical AWS spending patterns and
allows users to project future costs based on past usage. It offers advanced filtering and
grouping features, enabling users to analyze costs and usage at a granular level. The
AWS Cost and Usage Report provides detailed AWS cost and usage data but does not
offer visualization or future cost projections. AWS Budgets is used for setting custom cost
and usage budgets and receiving alerts. Amazon CloudWatch is for monitoring AWS
resources and applications, not for cost management.

</details>

---

### Question 225
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q225`

Which AWS service or feature is used to Troubleshoot network connectivity issues
between Amazon EC2 instances?

- **A)** AWS Certificate Manager (ACM)
- **B)** Internet gateway
- **C)** VPC Flow Logs
- **D)** AWS CloudHSM

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

VPC Flow Logs is the AWS service or feature that is used to troubleshoot network
connectivity issues between Amazon EC2 instances. VPC Flow Logs is a feature that
enables users to capture information about the IP traffic going to and from network
interfaces in their VPC. VPC Flow Logs can help users monitor and diagnose networkrelated issues, such as traffic not reaching an instance, or an instance not responding to
requests. VPC Flow Logs can be published to Amazon CloudWatch Logs, Amazon S3, or
Amazon Kinesis Data Firehose for analysis and storage.

</details>

---

### Question 226
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q226`

Which AWS services can a company use to achieve a loosely coupled architecture?
(Select TWO.)

- **A)** Amazon Workspaces
- **B)** Amazon Simple Queue Service (Amazon SQS)
- **C)** Amazon Connect
- **D)** AWS Trusted Advisor
- **E)** AWS Step Functions

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B, E`

Amazon Simple Queue Service (Amazon SQS) and AWS Step Functions are AWS
services that can be used to achieve a loosely coupled architecture. Amazon SQS is a fully
managed message queuing service that enables you to decouple and scale microservices,
distributed systems, and serverless applications. AWS Step Functions lets you coordinate
multiple AWS services into serverless workflows so you can build and update apps quickly.
Using Step Functions, you can design and run workflows that stitch together services such

as AWS Lambda and Amazon SNS into feature-rich applications. Reference: Amazon
SQS, AWS Step Functions

</details>

---

### Question 227
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q227`

An ecommerce company wants to use Amazon EC2 Auto Scaling to add and remove EC2
instances based on CPU utilization.
Which AWS service or feature can initiate an Amazon EC2 Auto Scaling action to achieve
this goal?

- **A)** Amazon Simple Queue Service (Amazon SQS)
- **B)** Amazon Simple Notification Service (Amazon SNS)
- **C)** AWS Systems Manager
- **D)** Amazon CloudWatch alarm

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon CloudWatch alarm is an AWS service or feature that can initiate an Amazon EC2
Auto Scaling action based on CPU utilization. Amazon CloudWatch is a monitoring and
observability service that collects and tracks metrics, logs, events, and alarms for your
AWS resources and applications. Amazon CloudWatch alarms are actions that you can
configure to send notifications or automatically make changes to the resources you are
monitoring based on rules that you define67.
Amazon EC2 Auto Scaling is a service that helps you maintain application availability and
allows you to automatically add or remove EC2 instances according to definable
conditions. You can create dynamic scaling policies that track a specific CloudWatch
metric, such as CPU utilization, and define what action to take when the associated
CloudWatch alarm is in ALARM. When the policy is in effect, Amazon EC2 Auto Scaling
adjusts the group's desired capacity up or down when the threshold of an alarm is
breached89. Reference:

</details>

---

### Question 228
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q228`

Which of the following is a software development framework that a company can use to
define cloud resources as code and provision the resources through AWS
CloudFormation?

- **A)** AWS CLI
- **B)** AWS Developer Center
- **C)** AWS Cloud Development Kit (AWS CDK)
- **D)** AWS CodeStar

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Cloud Development Kit (AWS CDK) is a software development framework that allows
you to define cloud resources as code using familiar programming languages, such as
TypeScript, Python, Java, .NET, and Go (in Developer Preview). You can use AWS CDK
to model your application resources using high-level constructs that provide sensible
defaults and best practices, or use low-level constructs that provide full access to the
underlying AWS CloudFormation resources. AWS CDK synthesizes your code into AWS
CloudFormation templates that you can deploy using the AWS CDK CLI or the AWS
Management Console. AWS CDK also integrates with other AWS services, such as AWS
CodeCommit, AWS CodeBuild, AWS CodePipeline, AWS Lambda, Amazon EC2, Amazon
S3, and more, to help you automate your development and deployment processes. AWS
CDK is an open-source framework that you can extend and contribute to. Reference:
Cloud Development Framework - AWS Cloud Development Kit - AWS, AWS Cloud
Development Kit Docume

</details>

---

### Question 229
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q229`

What can a cloud practitioner use to retrieve AWS security and compliance documents and
submit them as evidence to an auditor or regulator?

- **A)** AWS Certificate Manager
- **B)** AWS Systems Manager
- **C)** AWS Artifact
- **D)** Amazon Inspector

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Artifact is a service that provides on-demand access to AWS security and
compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI)
reports, and Service Organization Control (SOC) reports. You can download these
documents and submit them as evidence to your auditors or regulators to demonstrate the
security and compliance of the AWS infrastructure and services that you use. AWS Artifact
also allows you to review, accept, and manage AWS agreements, such as the Business
Associate Addendum (BAA) for customers who are subject to the Health Insurance
Portability and Accountability Act (HIPAA). Reference: AWS Artifact, What is AWS Artifact?

</details>

---

### Question 230
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q230`

Which AWS service uses a combination of publishers and subscribers?

- **A)** AWS Lambda
- **B)** Amazon Simple Notification Service (Amazon SNS)
- **C)** Amazon CloudWatch
- **D)** AWS CloudFormation

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Simple Notification Service (Amazon SNS) is a service that provides fully
managed pub/sub messaging. Pub/sub messaging is a pattern that uses a combination of
publishers and subscribers. Publishers are entities that produce messages and send them
to topics. Subscribers are entities that receive messages from topics. Topics are logical
access points that act as communication channels between publishers and subscribers.
Amazon SNS enables applications to decouple, scale, and coordinate the delivery of
messages to multiple endpoints, such as email, SMS, mobile push notifications, Lambda
functions, SQS queues, and HTTP/S endpoints. Amazon SNS OverviewAWS Certified
Cloud Practitioner - aws.amazon.com

</details>

---

### Question 231
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q231`

A company wants to minimize network latency between its Amazon EC2 instances. The
EC2 instances do not need to be highly available.
Which solution meets these requirements?

- **A)** Use EC2 instances in a single Availability Zone.
- **B)** Use Amazon CloudFront as the database for the EC2 instances.
- **C)** Use EC2 instances in the same edge location and the same Availability Zone.
- **D)** Use EC2 instances in the same edge location and the same AWS Region.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Using EC2 instances in a single Availability Zone is a solution that meets the requirements
of minimizing network latency between the EC2 instances and not needing high
availability. An Availability Zone is a physically isolated location within an AWS Region that
has its own power, cooling, and network connectivity. EC2 instances within the same
Availability Zone can communicate with each other using low-latency private IP addresses.
However, EC2 instances in a single Availability Zone are not highly available, because
they are vulnerable to failures or disruptions that affect the Availability Zone

</details>

---

### Question 232
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q232`

A user has been granted permission to change their own IAM user password.
Which AWS services can the user use to change the password? (Select TWO.)

- **A)** AWS Command Line Interface (AWS CLI)
- **B)** AWS Key Management Service (AWS KMS)
- **C)** AWS Management Console
- **D)** AWS Resource Access Manager (AWS RAM)
- **E)** AWS Secrets Manager

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 233
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q233`

What is a customer responsibility when using AWS Lambda according to the AWS shared
responsibility model?

- **A)** Managing the code within the Lambda function
- **B)** Confirming that the hardware is working in the data center
- **C)** Patching the operating system
- **D)** Shutting down Lambda functions when they are no longer in use

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

According to the AWS shared responsibility model, AWS is responsible for the security of
the cloud, while customers are responsible for the security in the cloud. This means that
AWS is responsible for the physical servers, networking, and operating system that run
Lambda functions, while customers are responsible for the security of their code and AWS
IAM to the Lambda service and within their function1. Customers need to manage the code
within the Lambda function, such as writing, testing, debugging, deploying, and updating
the code, as well as ensuring that the code does not contain any vulnerabilities or
malicious code that could compromise the security or performance of the function23.
Reference: 2: AWS Lambda - Amazon Web Services (AWS), 3: AWS Lambda
Documentation, 1: Amazon CLF-C02: What is customer responsibility under AWS ... PUPUWEB

</details>

---

### Question 234
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q234`

Which AWS service helps developers use loose coupling and reliable messaging between
microservices?

- **A)** Elastic Load Balancing
- **B)** Amazon Simple Notification Service (Amazon SNS)  C. Amazon CloudFront
- **D)** Amazon Simple Queue Service (Amazon SQS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon Simple Queue Service (Amazon SQS) is a service that provides fully managed
message queues for asynchronous communication between microservices. It helps
developers use loose coupling and reliable messaging by allowing them to send, store,
and receive messages between distributed components without losing them or requiring
each component to be always available1. Elastic Load Balancing is a service that
distributes incoming traffic across multiple targets, such as Amazon EC2 instances,
containers, and IP addresses. Amazon Simple Notification Service (Amazon SNS) is a
service that provides fully managed pub/sub messaging for event-driven and push-based
communication between microservices. Amazon CloudFront is a service that provides a
fast and secure content delivery network (CDN) for web applications.

</details>

---

### Question 235
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q235`

Which AWS service or feature offers HTTP attack protection to users running public-facing
web applications?

- **A)** Security groups
- **B)** Network ACLs
- **C)** AWS Shield Standard
- **D)** AWS WAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS WAF is the AWS service or feature that offers HTTP attack protection to users
running public-facing web applications. AWS WAF is a web application firewall that helps
users protect their web applications from common web exploits, such as SQL injection,
cross-site scripting, and bot attacks. Users can create custom rules to define the web
traffic that they want to allow, block, or count. Users can also use AWS Managed Rules,
which are pre-configured rules that are curated and maintained by AWS or AWS
Marketplace Sellers. AWS WAF can be integrated with other AWS services, such as
Amazon CloudFront, Amazon API Gateway, and Application Load Balancer, to provide
comprehensive security for web applications. [AWS WAF Overview] AWS Certified Cloud
Practitioner - aws.amazon.com

</details>

---

### Question 236
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q236`

Which AWS service enables companies to deploy an application dose to end users?

- **A)** Amazon CloudFront
- **B)** AWS Auto Scaling
- **C)** AWS AppSync
- **D)** Amazon Route S3

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers
data, videos, applications, and APIs to customers globally with low latency, high transfer
speeds, all within a developer-friendly environment. CloudFront enables companies to
deploy an application close to end users by caching the application's content at edge
locations that are geographically closer to the users. This reduces the network latency and
improves the user experience. CloudFront also integrates with other AWS services, such
as Amazon S3, Amazon EC2, AWS Lambda, AWS Shield, and AWS WAF, to provide a
secure and scalable solution for delivering applications12. Reference:
What Is Amazon CloudFront? - Amazon CloudFront
Amazon CloudFront Features - Amazon CloudFront

</details>

---

### Question 237
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q237`

A company wants to establish a schedule for rotating database user credentials.
Which AWS service will support this requirement with the LEAST amount of operational
overhead?

- **A)** AWS Systems Manager
- **B)** AWS Secrets Manager
- **C)** AWS License Manager
- **D)** AWS Managed Services

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Secrets Manager is a service that helps you protect access to your applications,
services, and IT resources. This service enables you to easily rotate, manage, and retrieve
database credentials, API keys, and other secrets throughout their lifecycle. Users and
applications retrieve secrets with a call to Secrets Manager APIs, eliminating the need to
hardcode sensitive information in plain text. Secrets Manager offers secret rotation with
built-in integration for Amazon RDS, Amazon Redshift, Amazon DocumentDB, and other
AWS services1. You can also extend Secrets Manager to rotate other types of secrets,
such as credentials for Oracle, SQL Server, or MongoDB databases, by using custom
AWS Lambda functions2. Secrets Manager enables you to control access to secrets using
fine-grained permissions and audit secret rotation centrally for resources in the AWS
Cloud, third-party services, and on-premises3. Therefore, AWS Secrets Manager supports
the requirement of rotating dat

</details>

---

### Question 238
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q238`

A company needs to migrate all of its development teams to a cloud-based integrated
development environment (IDE).
Which AWS service should the company use?

A. AWS CodeBuild

- **B)** AWS Cloud9
- **C)** AWS OpsWorks
- **D)** AWS Cloud Development Kit (AWS CDK)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The correct answer is B because AWS Cloud9 is an AWS service that enables users to run
their existing custom, nonproduction workloads in the AWS Cloud quickly and costeffectively. AWS Cloud9 is a cloud-based integrated development environment (IDE) that
allows users to write, run, and debug code from a web browser. AWS Cloud9 supports
multiple programming languages, such as Python, Java, Node.js, and more. AWS Cloud9
also provides users with a terminal that can access AWS services and resources, such as
Amazon EC2 instances, AWS Lambda functions, and AWS CloudFormation stacks. The
other options are incorrect because they are not AWS services that enable users to run
their existing custom, nonproduction workloads in the AWS Cloud quickly and costeffectively. AWS CodeBuild is an AWS service that enables users to compile, test, and
package their code for deployment. AWS OpsWorks is an AWS service that enables users
to configure and manage their applications using Chef or Puppet. AWS Cloud

</details>

---

### Question 239
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q239`

A company wants to create a chatbot and integrate the chatbot with its current web
application.
Which AWS service will meet these requirements?

- **A)** AmazonKendra
- **B)** Amazon Lex
- **C)** AmazonTextract
- **D)** AmazonPolly

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The AWS service that will meet the requirements of the company that wants to create a
chatbot and integrate the chatbot with its current web application is Amazon Lex. Amazon
Lex is a service that helps customers build conversational interfaces using voice and text.
The company can use Amazon Lex to create a chatbot that can understand natural
language and respond to user requests, using the same deep learning technologies that
power Amazon Alexa. Amazon Lex also provides easy integration with other AWS
services, such as Amazon Comprehend, Amazon Polly, and AWS Lambda, as well as
popular platforms, such as Facebook Messenger, Slack, and Twilio. Amazon Lex helps
customers create engaging and interactive chatbots for their web applications. Amazon
Kendra, Amazon Textract, and Amazon Polly are not the best services to use for this
purpose. Amazon Kendra is a service that helps customers provide accurate and natural

answers to natural language queries using machine learning

</details>

---

### Question 240
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q240`

A company wants to store its files in the AWS Cloud. Users need to be able to download
these files directly using a public URL.
Which AWS service or feature will meet this requirement?

- **A)** Amazon Redshift
- **B)** Amazon Elastic Block Store (Amazon EBS)
- **C)** Amazon Elastic File System (Amazon EFS)
- **D)** Amazon S3

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 241
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q241`

Which benefit does AWS offer exclusively to users who have an AWS Enterprise Support
plan?

- **A)** Access to a technical project manager
- **B)** Access to a technical account manager (TAM)
- **C)** Access to a cloud support engineer
- **D)** Access to a solutions architectA company wants to automatically set up and govern a multi-account AWS environment.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Enterprise Support plan is the highest level of support that AWS offers to its
customers. One of the exclusive benefits of this plan is the access to a technical account
manager (TAM), who is adedicated point of contact for guidance, advocacy, and support2.
A technical project manager, a cloud support engineer, and a solutions architect are not
exclusive benefits of the AWS Enterprise Support plan, as they are also available to
customers with lower-tier support plans or through other AWS services or programs345.

</details>

---

### Question 242
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q242`

Which credential allows programmatic access to AWS resources for use from the AWS CLI
or the AWS API?

- **A)** User name and password
- **B)** Access keys
- **C)** SSH public keys
- **D)** AWS Key Management Service (AWS KMS) keys

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Access keys are long-term credentials that consist of an access key ID and a secret
access key. You use access keys to sign programmatic requests that you make to AWS
using the AWS CLI or AWS API1. User name and password are credentials that you use to
sign in to the AWS Management Console or the AWS Management Console mobile app2.
SSH public keys are credentials that you use to authenticate with EC2 instances that are
launched from certain Linux AMIs3. AWS Key Management Service (AWS KMS) keys are
customer master keys (CMKs) that you use to encrypt and decrypt your data and to control
access to your data across AWS services and in your applications4.

</details>

---

### Question 243
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q243`

Under the AWS shared responsibility model, which of the following is a responsibility of the
customer?

- **A)** Shred disk drives before they leave a data center.
- **B)** Prevent customers from gathering packets or collecting traffic at the hypervisor level.
- **C)** Patch the guest operating system with the latest security patches.
- **D)** Maintain security systems that provide physical monitoring of data centers.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Under the AWS shared responsibility model, AWS is responsible for the security "of" the
cloud, which includes the physical infrastructure, networking, and hypervisor layer. The
customer, however, is responsible for security "in" the cloud, which includes managing the
security of their data, patching and maintaining their guest operating system and
applications, and managing identity and access. The responsibilities of shredding disk
drives, preventing packet capture at the hypervisor level, and physical monitoring are
handled by AWS as part of its responsibility for security "of" the cloud.

</details>

---

### Question 244
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q244`

Which AWS service helps users plan and track their server and application inventory
migration data to AWS?

- **A)** Amazon CloudWatch
- **B)** AWS DataSync
- **C)** AWS Migration Hub
- **D)** AWS Application Migration Service

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Migration Hub assists users in planning and tracking the progress of their server and
application migrations. It centralizes migration tracking across various AWS services,
providing visibility into application inventory and migration status. While AWS Application
Migration Service also assists with migrations, Migration Hub is specifically designed for
tracking migration data comprehensively.

</details>

---

### Question 245
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q245`

Which AWS Support plan provides the full set of AWS Trusted Advisor checks at the
LOWEST cost?

- **A)** AWS Developer Support
- **B)** AWS Business Support
- **C)** AWS Enterprise On-Ramp Support
- **D)** AWS Enterprise Support

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The AWS Support plan that provides the full set of AWS Trusted Advisor checks at the
lowest cost is the AWS Business Support plan. The AWS Business Support plan includes
access to the complete set of Trusted Advisor checks, which cover areas such as cost
optimization, security, performance, fault tolerance, and service limits. This plan is
specifically designed to support production workloads and includes 24/7 access to cloud
support engineers, response times for impaired systems, and other enhanced technical
support features.
AWS Developer Support, while more affordable, only provides limited Trusted Advisor
checks, specifically around Service Limits and basic Security checks. Full access to all
Trusted Advisor checks is only available with Business Support and higher-tier plans, such
as Enterprise On-Ramp and Enterprise Support

</details>

---

### Question 246
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q246`

Which AWS service can identify when an Amazon EC2 instance was terminated?

- **A)** AWS Identity and Access Management (IAM)
- **B)** AWS CloudTrail
- **C)** AWS Compute Optimizer
- **D)** Amazon EventBridge

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS CloudTrail is the AWS service that can identify when an Amazon EC2 instance was
terminated. AWS CloudTrail is a service that records API calls and events for AWS
accounts and resources. AWS CloudTrail can capture the TerminateInstances event,
which is triggered when an EC2 instance is terminated by a user or an AWS service. The
event contains information such as the instance ID, the user identity, the source IP
address, the time, and the reason for the termination12. Customers can use the CloudTrail
console, the AWS CLI, or the AWS SDKs to view and search for the TerminateInstances
events in their event history or in their S3 buckets where they store their CloudTrail logs13.

</details>

---

### Question 247
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q247`

Which tasks are the responsibility of AWS according to the AWS shared responsibility
model? (Select TWO.)

- **A)** Configure AWS Identity and Access Management (IAM).
- **B)** Configure security groups on Amazon EC2 instances.
- **C)** Secure the access of physical AWS facilities.
- **D)** Patch applications that run on Amazon EC2 instances.
- **E)** Perform infrastructure patching and maintenance.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CE`

The tasks that are the responsibility of AWS according to the AWS shared responsibility
model are securing the access of physical AWS facilities and performing infrastructure
patching and maintenance. The AWS shared responsibility model defines the division of
responsibilities between AWS and the customer for security and compliance. AWS is
responsible for the security of the cloud, which includes the physical security of the
hardware, software, networking, and facilities that run the AWS services. AWS is also
responsible for the maintenance and patching of the infrastructure that supports the AWS
services. The customer is responsible for the security in the cloud, which includes the
configuration and management of the AWS resources and applications that they use.
Configuring AWS Identity and Access Management (IAM), configuring security groups on
Amazon EC2 instances, and patching applications that run on Amazon EC2 instances are
tasks that are the responsibility of the customer, not

</details>

---

### Question 248
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q248`

Which AWS service or tool provides users with a graphical interface that they can use to
manage AWS services?

- **A)** AWS Copilot
- **B)** AWS CLI
- **C)** AWS Management Console
- **D)** AWS software development kits (SDKs)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS Management Console provides a web-based graphical user interface (GUI) that
allows users to manage AWS services. It is user-friendly and accessible, enabling users to
control and configure resources without needing to interact with AWS through code or
command-line interfaces. AWS CLI and SDKs are command-line and programming tools,
respectively, and do not offer a graphical interface.

</details>

---

### Question 249
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q249`

Which design principle aligns with the performance efficiency pillar of the AWS WellArchitected Framework?

- **A)** Measure the cost of workloads
- **B)** Enable traceability
- **C)** Use serverless architectures
- **D)** Scale vertically

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 250
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q250`

Which AWS services or features can a company use to connect the network of its onpremises data center to AWS? (Select TWO.)

- **A)** AWS VPN
- **B)** AWS Directory Service
- **C)** AWS Data Pipeline
- **D)** AWS Direct Connect
- **E)** AWS CloudHSM

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AD`

AWS VPN and AWS Direct Connect are two services that enable customers to connect
their on-premises data center network to the AWS Cloud. AWS VPN establishes a secure
and encrypted connection over the public internet, while AWS Direct Connect establishes a
dedicated and private connection through a partner network. You can learn more about
AWS VPN from [this webpage] or [this digital course]. You can learn more about AWS
Direct Connect from [this webpage] or [this digital course].

</details>

---

### Question 251
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q251`

What is the total amount of storage offered by Amazon S3?

- **A)** WOMB  B. 5 GB
- **C)** 5 TB
- **D)** Unlimited

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon S3 offers unlimited storage for any amount of data. You can store as many
objects as you want, and each object can be as large as 5 terabytes. You pay only for the
storage space that you actually use, and there are no minimum commitments or upfront
fees. Amazon S3 also provides high durability, availability, scalability, and security for your
data.

</details>

---

### Question 252
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q252`

Which AWS service is a fully managed service for machine learning?

- **A)** Amazon Athena
- **B)** Amazon SageMaker
- **C)** Amazon Kinesis
- **D)** AWS Lambda

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 253
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q253`

Which AWS feature or resource is a deployable Amazon EC2 instance template that is
prepackaged with software and security requirements?

- **A)** Amazon Elastic Block Store (Amazon EBS) volume
- **B)** AWS CloudFormation template
- **C)** Amazon Elastic Block Store (Amazon EBS) snapshot
- **D)** Amazon Machine Image (AMI)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

An Amazon Machine Image (AMI) is a deployable Amazon EC2 instance template that is
prepackaged with software and security requirements. It provides the information required
to launch an instance, which is a virtual server in the cloud. You can use an AMI to launch
as many instances as you need. You can also create your own custom AMIs or use AMIs
shared by other AWS users1.

</details>

---

### Question 254
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q254`

A company that has an AWS Enterprise Support plan needs to protect its applications from
DDoS attacks. The company requires access to the AWS DDoS Response Team (DRT)
24 hours a day. 7 days a week.
Which AWS service will meet these requirements?

- **A)** AWS Firewall Manager
- **B)** AWS Shield Standard
- **C)** AWS Shield Advanced
- **D)** AWS WAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 255
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q255`

Which pillar of the AWS Well-Architected Framework focuses on the ability to run
workloads effectively, gain insight into operations, and continuously improve supporting
processes and procedures?

- **A)** Cost optimization
- **B)** Reliability
- **C)** Operational excellence
- **D)** Performance efficiency

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS Well-Architected Framework is a set of best practices and guidelines for
designing and operating systems in the cloud. The framework consists of five pillars:
operational excellence, security, reliability, performance efficiency, and cost optimization.
The operational excellence pillar focuses on the ability to run workloads effectively, gain
insight into operations, and continuously improve supporting processes and procedures.
Therefore, the correct answer is C. You can learn more about the AWS Well-Architected
Framework and its pillars.

</details>

---

### Question 256
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q256`

A company needs to list all users in an account. The company must report on the status of
specific account details. The account details include passwords, access keys, and multifactor authentication (MFA) devices.
Which AWS service or tool will meet these requirements?

- **A)** AWS Shield
- **B)** AWS Trusted Advisor
- **C)** Amazon Inspector
- **D)** IAM credential report

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

An IAM credential report is designed for account-level auditing of IAM user credentials.
AWS states that the report lists all IAM users in an AWS account and shows the status of
their credentials, including passwords, access keys, and multi-factor authentication
devices. It can also contain information such as whether a password is enabled, when
credentials were created or last used, whether access keys are active, and whether an
MFA device is enabled. This directly satisfies both requirements in the question: listing
users and reporting specific credential details. AWS Shield protects applications against
distributed denial-of-service attacks and does not produce user credential inventories.
AWS Trusted Advisor evaluates an AWS environment against best-practice checks, but it
is not the tool for downloading a complete per-user credential-status report. Amazon
Inspector scans workloads such as Amazon EC2 instances, container images, and
Lambda functions for software vulnerabilities and

</details>

---

### Question 257
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q257`

A company is using Amazon DynamoDB.
Which task is the company's responsibility, according to the AWS shared responsibility
model?

- **A)** Patch the operating system
- **B)** Provision hosts
- **C)** Manage database access permissions.
- **D)** Secure the operating system

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

According to the AWS shared responsibility model, AWS is responsible for the security of
the cloud, while customers are responsible for the security in the cloud. This means that
AWS is responsible for the physical servers, networking, and operating system that run
DynamoDB, while customers are responsible for the security of their data and access to
the database. Customers need to manage database access permissions, such as creating
and managing AWS Identity and Access Management (IAM) policies and roles, and using
encryption and key management options to protect their data123. Reference: 1: Shared
Responsibility Model - Amazon Web Services (AWS), 2: Security in Amazon DynamoDB Amazon DynamoDB, 3: AWS Shared Responsibility Model - Introduction to DevOps ...

</details>

---

### Question 258
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q258`

Where can users find examples of AWS Cloud solution designs?

- **A)** AWS Marketplace
- **B)** AWS Service Catalog
- **C)** AWS Architecture Center
- **D)** AWS Trusted Advisor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS Architecture Center provides examples, best practices, and architectural
blueprints for various AWS Cloud solutions. It includes whitepapers, reference
architectures, and detailed diagrams to help users design secure, scalable, and reliable

applications on AWS. Other services like AWS Marketplace, Service Catalog, and Trusted
Advisor do not offer solution design examples.

</details>

---

### Question 259
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q259`

A company migrated its on-premises data to AWS by using AWS Storage Gateway
Volume Gateway. The company needs the ability to restore data to a time in the past in
case of data corruption or accidental deletion.
Which Volume Gateway capability meets this requirement?

- **A)** Automated snapshots stored as Amazon EBS snapshots
- **B)** Real-time replication to multiple AWS Regions
- **C)** Continuous data mirroring to Amazon S3 Glacier Flexible Retrieval
- **D)** Automated lifecycle policies to archive snapshots to Amazon S3 Glacier Flexible Retrieval

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Storage Gateway Volume Gateway supports point-in-time backups by creating
snapshots of gateway volumes. AWS stores these backups as Amazon EBS snapshots,
and snapshots can be created manually or according to a schedule. Because each
snapshot represents the volume at a particular point in time, the company can restore a
previous snapshot when data is corrupted or accidentally deleted. AWS documentation
specifically states that Storage Gateway volume backups can be stored as Amazon EBS
snapshots and subsequently restored to a Storage Gateway volume or an Amazon EBS
volume. Real-time multi-Region replication is not the described Volume Gateway recovery
mechanism, and Glacier Flexible Retrieval lifecycle or continuous mirroring options do not
provide the stated native point-in-time volume recovery capability. Therefore, automated
snapshots stored as Amazon EBS snapshots is correct.

</details>

---

### Question 260
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q260`

Which of the following describes an AWS Region?

- **A)** A specific location within a geographic area that provides high availability
- **B)** A set of data centers spanning multiple countries
- **C)** A global picture of a user's cloud computing environment
- **D)** A collection of databases that can be accessed from a specific geographic area only

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

An AWS Region is a specific location within a geographic area that provides high
availability. An AWS Region consists of two or more Availability Zones, which are isolated
locations within the same Region. Each Availability Zone has independent power, cooling,
and physical security, and is connected to the other Availability Zones in the same Region
by low-latency, high-throughput, and highly redundant networking. AWS services are
available in multiple Regions around the world, allowing the user to choose where to run
their applications and store their data1.

</details>

---

### Question 261
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q261`

A company purchased Amazon EC2 Standard Reserved Instances (Rls) for a workload in
the AWS Cloud. The company needs to move part of the workload to an instance family
that does not match the instance family of these Standard RIs.
How can the company take advantage of the Standard RIs that it no longer needs?

- **A)** Contact the AWS Support team, and ask the team to sell the Standard RIs.
- **B)** Sell the Standard RIs on the Amazon EC2 Reserved Instance Marketplace.
- **C)** Sell the Standard RIs as a third-party seller on the AWS Marketplace.
- **D)** Convert the Standard RIs to Savings Plans.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The Amazon EC2 Reserved Instance Marketplace allows customers to sell unused
Standard Reserved Instances to other AWS users. This enables companies to recoup
some of the costs if they no longer need certain RIs. Standard RIs cannot be converted to
Savings Plans, and AWS Support does not facilitate the resale of RIs directly.

</details>

---

### Question 262
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q262`

Which AWS Cloud benefit is shown by an architecture's ability to withstand failures with
minimal downtime?

- **A)** Agility
- **B)** Elasticity
- **C)** Scalability
- **D)** High availability

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 263
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q263`

Which AWS service is a key-value database that provides sub-millisecond latency on a
large scale?

- **A)** Amazon DynamoDB
- **B)** Amazon Aurora
- **C)** Amazon DocumentDB (with MongoDB compatibility)
- **D)** Amazon Neptune

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The correct answer is A because Amazon DynamoDB is a key-value database that
provides sub-millisecond latency on a large scale. Amazon DynamoDB is a fully managed,
serverless, and scalable NoSQL database service that supports both key-value and
document data models. The other options are incorrect because they are not key-value
databases. Amazon Aurora is a relational database that is compatible with MySQL and
PostgreSQL. Amazon DocumentDB (with MongoDB compatibility) is a document database
that is compatible with MongoDB. Amazon Neptune is a graph database that supports
property graph and RDF models. Reference: Amazon DynamoDB FAQs

</details>

---

### Question 264
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q264`

A company hosts an application on an Amazon EC2 instance. The EC2 instance needs to
access several AWS resources, including Amazon S3 and Amazon DynamoDB.
What is the MOST operationally efficient solution to delegate permissions?

- **A)** Create an IAM role with the required permissions. Attach the role to the EC2 instance.
- **B)** Create an IAM user and use its access key and secret access key in the application.
- **C)** Create an IAM user and use its access key and secret access key to create a CLI profile in the EC2 instance.
- **D)** Create an IAM role with the required permissions. Attach the role to the administrativeIAM user.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Creating an IAM role with the required permissions and attaching the role to the EC2
instance is the most operationally efficient solution to delegate permissions. An IAM role is
an entity that defines a set of permissions for making AWS service requests. An IAM role
can be assumed by an EC2 instance to access other AWS resources, such as Amazon S3
and Amazon DynamoDB, without having to store any credentials on the instance. This
solution is more secure and scalable than using IAM users and their access keys. For
more information, see [IAM Roles for Amazon EC2] and [Using an IAM Role to Grant
Permissions to Applications Running on Amazon EC2 Instances].

</details>

---

### Question 265
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q265`

Which benefit does Amazon Rekognition provide?

- **A)** The ability to place watermarks on images
- **B)** The ability to detect objects that appear in pictures  C. The ability to resize millions of images automatically
- **D)** The ability to bid on object detection jobs

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Rekognition is a service that provides deep learning-based image and video
analysis. One of the benefits of Amazon Rekognition is the ability to detect objects that
appear in pictures, such as faces, landmarks, animals, text, and scenes. This can enable
applications to perform tasks such as face recognition, face verification, face comparison,
face search, celebrity recognition, emotion detection, age range estimation, gender
identification, facial analysis, facial expression recognition, and more. Amazon Rekognition
OverviewAWS Certified Cloud Practitioner - aws.amazon.com

</details>

---

### Question 266
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q266`

A company wants a customized assessment of its current on-premises environment. The
company wants to understand its projected running costs in the AWS Cloud.
Which AWS service or tool will meet these requirements?

- **A)** AWS Trusted Advisor
- **B)** Amazon Inspector
- **C)** AWS Control Tower
- **D)** Migration Evaluator

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Migration Evaluator is an AWS service that provides a customized assessment of your
current on-premises environment and helps you build a data-driven business case for
migration to AWS. Migration Evaluator collects and analyzes data from your on-premises
servers, such as CPU, memory, disk, network, and utilization metrics, and compares them
with the most cost-effective AWS alternatives. Migration Evaluator also helps you
understand your existing software licenses and running costs, and provides
recommendations for Bring Your Own License (BYOL) and License Included (LI) options in
AWS. Migration Evaluator generates a detailed report that shows your projected running
costs in the AWS Cloud, along with potential savings and benefits. You can use this report
to support your decision-making and planning for cloud migration. Reference: Cloud
Business Case & Migration Plan - Amazon Migration Evaluator - AWS, Getting started with
Migration Evaluator

</details>

---

### Question 267
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q267`

An independent software vendor wants to deliver and share its custom Amazon Machine
images (AMIs) to prospective customers.
Which AWS service will meet these requirements?

- **A)** AWS Marketplace
- **B)** AWS Data Exchange
- **C)** Amazon EC2
- **D)** AWS Organizations

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Marketplaceis an online store where independent software vendors (ISVs) can list
and sell their software products, including custom Amazon Machine Images (AMIs). It
allows vendors to share, distribute, and monetize their AMIs with a broad audience of AWS
customers.
B . AWS Data Exchange: Incorrect, as it is a service for finding, subscribing to, and using
third-party data in the cloud, not for delivering custom AMIs.
C . Amazon EC2: Incorrect, as it is the service for running instances, but it does not
provide a marketplace for distributing AMIs.
D . AWS Organizations: Incorrect, as it is a service for managing multiple AWS accounts,
not for distributing software products like AMIs.
AWS Cloud Reference:
AWS Marketplace

</details>

---

### Question 268
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q268`

A company plans to migrate its on-premises workload to AWS. Before the migration, the
company needs to estimate its future AWS service costs.
Which AWS service or tool should the company use to meet this requirement?

- **A)** AWS Trusted Advisor
- **B)** AWS Budgets
- **C)** AWS Pricing Calculator
- **D)** AWS Cost Explorer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Pricing Calculator is the AWS service or tool that the company should use to
estimate its future AWS service costs before the migration. AWS Pricing Calculator is a
web-based tool that allows the company to create cost estimates for various AWS services
and scenarios. AWS Pricing Calculator helps the company to compare the costs of running
the workload on premises versus on AWS, and to optimize the costs by choosing the best
options for the workload. AWS Pricing Calculator also provides a detailed breakdown of
the cost components and a downloadable report. For more information, see [AWS Pricing
Calculator] and [Getting Started with AWS Pricing Calculator].

</details>

---

### Question 269
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q269`

A network engineer needs to build a hybrid cloud architecture connecting on-premises
networks to the AWS Cloud using AWS Direct Connect. The company has a few VPCs in a
single AWS Region and expects to increase the number of VPCs to hundreds over time.
Which AWS service or feature should the engineer use to simplify and scale this
connectivity as the VPCs increase in number?

- **A)** VPC endpoints
- **B)** AWS Transit Gateway
- **C)** Amazon Route 53  D. AWS Secrets Manager

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Transit Gateway is a network transit hub that you can use to interconnect your VPCs
and on-premises networks through a central gateway. AWS Transit Gateway simplifies and
scales the connectivity between your on-premises networks and AWS, as you only need to
create and manage a single connection from the central gateway to each on-premises
network, rather than individual connections to each VPC. You can also use AWS Transit
Gateway to connect to other AWS services, such as Amazon S3, Amazon DynamoDB,
and AWS PrivateLink12. AWS Transit Gateway supports thousands of VPCs per gateway,
and enables you to peer Transit Gateways across AWS Regions3.
The other options are not AWS services or features that can simplify and scale the
connectivity between on-premises networks and hundreds of VPCs using AWS Direct
Connect. VPC endpoints enable private connectivity between your VPCs and supported
AWS services, but do not support on-premises networks4. Amazon Route 53 is a DNS
service that helps

</details>

---

### Question 270
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q270`

Which AWS service or feature is available only to users who have an AWS Enterprise
Support plan?

- **A)** AWS Trusted Advisor
- **B)** AWS Support case
- **C)** AWS Concierge Support team
- **D)** Amazon Connect

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Among the listed options, the AWS Concierge Support team is the intended answer for this
exam question. Traditional AWS certification materials associate Support Concierge with
AWS Enterprise Support and describe it as assistance for billing and account-related
matters. Current AWS documentation has modernized the support-plan presentation and
emphasizes that Enterprise Support provides concierge-like service, a designated
Technical Account Manager, rapid technical response, and expert guidance. The option
therefore reflects legacy but recognizable Enterprise Support terminology. AWS Trusted
Advisor is not exclusive to Enterprise Support: all customers can access core checks,
while broader check availability depends on the support plan. An AWS Support case is
also not exclusive to Enterprise Support. Account and billing cases are available to all
customers, and technical case access is included with qualifying paid support plans.
Amazon Connect is an AWS customer-experience and contact

</details>

---

### Question 271
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q271`

An auditor is preparing for an annual security audit. The auditor requests certification
details for a company's AWS hosted resources across multiple Availability Zones in the useast-1 Region.
How should the company respond to the auditor's request?

- **A)** Open an AWS Support ticket to request that the AWS technical account manager (TAM) respond and help the auditor.
- **B)** Open an AWS Support ticket to request that the auditor receive approval to conduct an onsite assessment of the AWS data centers in which the company operates.
- **C)** Explain to the auditor that AWS does not need to be audited because the company's application is hosted in multiple Availability Zones.
- **D)** Use AWS Artifact to download the applicable report for AWS security controls. Provide the report to the auditor.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Artifact is your go-to, central resource for compliance-related information that matters
to you. It provides on-demand access to AWS' security and compliance reports and select
online agreements. Reports available in AWS Artifact include our Service Organization
Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from
accreditation bodies across geographies and compliance verticals that validate the
implementation and operating effectiveness of AWS security controls. Agreements
available in AWS Artifact include the Business Associate Addendum (BAA) and the
Nondisclosure Agreement (NDA). You can use AWS Artifact to download the applicable
report for AWS security controls and provide it to the auditor.

</details>

---

### Question 272
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q272`

Which AWS service or tool can be used to consolidate payments for a company with
multiple AWS accounts?

- **A)** AWS Cost and Usage Report
- **B)** AWS Organizations  C. Cost Explorer
- **D)** AWS Budgets

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Organizations is an account management service that enables you to consolidate
multiple AWS accounts into an organization that you create and centrally manage. AWS
Organizations includes consolidated billing and account management capabilities that
enable you to better meet the budgetary, security, and compliance needs of your
business1.

</details>

---

### Question 273
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q273`

A company wants to define a central data protection policy that works across AWS
services for compute, storage, and database resources.
Which AWS service will meet this requirement?

- **A)** AWS Batch
- **B)** AWS Elastic Disaster Recovery
- **C)** AWS Backup
- **D)** Amazon FSx

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS service that will meet this requirement is C. AWS Backup.
AWS Backup is a service that allows you to define a central data protection policy that
works across AWS services for compute, storage, and database resources. You can use
AWS Backup to create backup plans that specify the frequency, retention, and lifecycle of
your backups, and apply them to your AWS resources using tags or resource IDs. AWS
Backup supports various AWS services, such as Amazon EC2, Amazon EBS, Amazon
RDS, Amazon DynamoDB, Amazon EFS, Amazon FSx, and AWS Storage Gateway12.
AWS Batch is a service that allows you to run batch computing workloads on AWS. AWS
Batch does not provide a central data protection policy, but rather enables you to optimize
the allocation and utilization of your compute resources3.
AWS Elastic Disaster Recovery is a service that allows you to prepare for and recover from
disasters using AWS. AWS Elastic Disaster Recovery does not provide a central data
protection polic

</details>

---

### Question 274
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q274`

A company is building a new application on AWS. The company needs the application to
remain available if an individual application component fails.
Which design principle should the company use to meet this requirement?

- **A)** Disposable resources
- **B)** Automation
- **C)** Rightsizing
- **D)** Loose coupling

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Loose coupling is a design principle that involves reducing dependencies between
application components so that they can operate independently. This approach ensures
that the failure of one component does not affect the availability of the others, thereby
improving the application's fault tolerance and resilience. Disposable resources,
automation, and rightsizing are valuable principles in cloud architecture, but they do not
directly address the requirement of remaining available despite the failure of an individual
component like loose coupling does.
Reference:
AWS Well-Architected Framework - Design Principles

</details>

---

### Question 275
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q275`

A company wants to use an AWS networking solution that can act as a centralized
gateway between multiple VPCs and on-premises networks. Which AWS service or feature
will meet this requirement?

- **A)** Gateway VPC endpoint
- **B)** AWS Direct Connect
- **C)** AWS Transit Gateway
- **D)** AWS PrivateLink

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Transit Gateway serves as a central hub that enables connectivity between multiple
VPCs and on- premises networks. It simplifies network architecture and management by
acting as a centralized gateway for traffic flowing between all connected networks. Other
options, such as Gateway VPC Endpoints and AWS PrivateLink, do not provide the
centralized, scalable connectivity that Transit Gateway offers across multiple VPCs and
on-premises environments.

</details>

---

### Question 276
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q276`

Which of the following is a recommended design principle of the AWS Well-Architected
Framework?

- **A)** Reduce downtime by making infrastructure changes infrequently and in large increments.  B. Invest the time to configure infrastructure manually.
- **C)** Learn to improve from operational failures.
- **D)** Use monolithic application design for centralization.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because learning to improve from operational failures is a
recommended design principle of the AWS Well-Architected Framework. The AWS WellArchitected Framework is a set of best practices and guidelines for designing and
operating reliable, secure, efficient, and cost-effective systems in the cloud. The AWS
Well-Architected Framework consists of five pillars: operational excellence, security,
reliability, performance efficiency, and cost optimization. Each pillar has a set of design
principles that describe the characteristics of a well-architected system. Learning to
improve from operational failures is a design principle of the operational excellence pillar,
which focuses on running and monitoring systems to deliver business value and
continually improve supporting processes and procedures. The other options are incorrect
because they are not recommended design principles of the AWS Well-Architected
Framework. Reducing downtime by making infrastr

</details>

---

### Question 277
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q277`

A company is designing a web application that will run on Amazon EC2 instances.
Which AWS services and features will improve availability and reduce the impact of
failures for this application?
(Select TWO.)

- **A)** Amazon EC2 Auto Scaling for the EC2 instances
- **B)** VPC subnet ACLs to check the health of a service
- **C)** Resources that are distributed across multiple Availability Zones
- **D)** Configuration of AWS Server Migration Service (AWS SMS) to move the EC2 instances to a different AWS Region
- **E)** Resources that are distributed across multiple AWS points of presence

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

The correct answers are A and C because Amazon EC2 Auto Scaling and resources that
are distributed across multiple Availability Zones are AWS services and features that will

improve availability and reduce the impact of failures for the web application. Amazon EC2
Auto Scaling is a service that enables users to automatically adjust the number of Amazon
EC2 instances in response to changes in demand or performance. Amazon EC2 Auto
Scaling helps users to maintain optimal availability and performance of their applications
by adding or removing instances as needed. Resources that are distributed across multiple
Availability Zones are AWS features that enable users to increase the fault tolerance and
resilience of their applications. Availability Zones are isolated locations within an AWS
Region that have independent power, cooling, and networking. Users can launch their
resources, such as Amazon EC2 instances, in multiple Availability Zones to protect their
applications from the failure

</details>

---

### Question 278
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q278`

Which pillar of the AWS Well-Architected Framework focuses on the ability to recover
automatically from service Interruptions?

- **A)** Security
- **B)** Performance efficiency
- **C)** Operational excellence
- **D)** Reliability

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

TheReliabilitypillar of the AWS Well-Architected Framework focuses on the ability of a
system to recover from failures and disruptions, dynamically acquire computing resources
to meet demand, and mitigate disruptions such as misconfigurations or network issues.
This includes the ability to automatically recover from service interruptions and implement
mechanisms that anticipate, respond to, and prevent failures.
A . Security: Incorrect, as it focuses on protecting information, systems, and assets while
delivering business value.

B . Performance efficiency: Incorrect, as it focuses on using IT and computing resources
efficiently.
C . Operational excellence: Incorrect, as it focuses on operations in the cloud, including
monitoring and managing systems.
AWS Cloud Reference:
AWS Well-Architected Framework - Reliability Pillar

</details>

---

### Question 279
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q279`

A company needs to host a web server on Amazon EC2 instances for at least 1 year. The
web server cannot tolerate interruption.
Which EC2 instance purchasing option will meet these requirements MOST costeffectively?

- **A)** On-Demand Instances
- **B)** Partial Upfront Reserved Instances
- **C)** Spot Instances
- **D)** No Upfront Reserved Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The most cost-effective EC2 instance purchasing option for the company that needs to
host a web server on Amazon EC2 instances for at least 1 year and cannot tolerate
interruption is Partial Upfront Reserved Instances. Reserved Instances are a pricing model
that offer significant discounts compared to On-Demand Instances in exchange for a
commitment to use a specific amount of compute capacity for a fixed period of time (1 or 3
years). Partial Upfront Reserved Instances require customers to pay a portion of the total
cost upfront, and the remaining cost in monthly installments over the term. This option
offers a lower effective hourly rate than No Upfront Reserved Instances, which require no
upfront payment but have higher monthly payments. On-Demand Instances and Spot
Instances are not the best options for the company. On-Demand Instances are a pricing
model that offer the most flexibility and no long-term commitment, but have the highest
hourly rate. Spot Instances are a pricing mode

</details>

---

### Question 280
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q280`

A developer needs to maintain a development environment infrastructure and a production
environment infrastructure in a repeatable fashion Which AWS service should the
developer use to meet these requirements?

- **A)** AWS Ground Station
- **B)** AWS Shield
- **C)** AWS loT Device Defender
- **D)** AWS CloudFormation

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS CloudFormation is a service that allows developers to model and provision their AWS
infrastructure in a repeatable and declarative way, using code and templates. AWS
CloudFormation enables developers to define the resources they need for their
development and production environments, such as compute, storage, network, and
application services, and automate their creation and configuration. AWS CloudFormation
also provides features such as change sets, nested stacks, and rollback triggers to help
developers manage and update their infrastructure safely and efficiently12. Reference:
AWS CloudFormation
What is AWS CloudFormation?

</details>

---

### Question 281
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q281`

A company needs to manage multiple logins across AWS accounts within the same
organization in AWS Organizations.
Which AWS service should the company use to meet this requirement?

- **A)** Amazon VPC
- **B)** Amazon GuardDuty
- **C)** Amazon Cognito
- **D)** AWS IAM Identity Center

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS IAM Identity Center (formerly AWS Single Sign-On) provides centralized
management of user access to multiple AWS accounts within an organization in AWS
Organizations. It allows users to log in once and gain access to all assigned accounts
without managing separate logins for each account. Amazon Cognito is generally used for
application-level user management and authentication, not for managing access across
AWS accounts.

</details>

---

### Question 282
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q282`

Which capabilities are part of the Operations perspective of the AWS Cloud Adoption
Framework (AWS CAF)?(Select TWO.)

- **A)** Observability
- **B)** Data governance
- **C)** Platform architecture
- **D)** Portfolio management
- **E)** Configuration management

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A, E`

Comprehensive and Detailed Explanation From AWS Cloud Documentation:
The AWS Cloud Adoption Framework Operations perspective focuses on delivering cloud
services at an agreed level and improving workload reliability through effective operations.
AWS lists observability as an Operations capability because teams need metrics, logs,
traces, endpoint monitoring, and alerts to understand workload health and identify
problems. AWS also lists configuration management as an Operations capability because

organizations need an accurate record of workloads, relationships, settings, and
configuration changes, and must control configuration drift. Therefore, options A and E are
correct. The other choices belong to different AWS CAF perspectives. Data governance is
a Governance perspective capability concerned with authority, ownership, standards,
quality, and control over organizational data. Platform architecture is a Platform
perspective capability that establishes architectural g

</details>

---

### Question 283
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q283`

Which tasks are the responsibility of the customer, according to the AWS shared
responsibility model? (Select TWO.)

- **A)** Patch the Amazon RDS operating system.
- **B)** Upgrade the firmware of the network infrastructure.
- **C)** Manage data encryption.
- **D)** Maintain physical access control in an AWS Region.
- **E)** Grant least privilege access to IAM users.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CE`

According to the AWS shared responsibility model, the customer is responsible for security
in the cloud, which includes the tasks of managing data encryption and granting least
privilege access to IAM users. Data encryption is the process of transforming data into an
unreadable format that can only be accessed with a key or a password. The customer
must decide whether to encrypt their data at rest (when it is stored on AWS) or in transit
(when it is moving between AWS and the customer or between AWS services). The
customer must also choose the encryption method, algorithm, and key management
solution that best suit their needs. AWS provides various services and features that
support data encryption, such as AWS Key Management Service (AWS KMS), AWS
Certificate Manager (ACM), and AWS Encryption SDK5 IAM users are entities that
represent the people or applications that interact with AWS resources and services. The
customer must grant the IAM users the minimum permissions that they need t

</details>

---

### Question 284
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q284`

An AWS user wants to proactively detect when an instance or account might be
compromised or if there are threats from attacks.
Which AWS service should the user choose?

A. Amazon GuardDuty

- **B)** AWS WAF
- **C)** AWS Shield
- **D)** Amazon Inspector

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon GuardDutyis a threat detection service that continuously monitors AWS accounts
and workloads for malicious activity and unauthorized behavior to help protect your AWS
resources. It uses machine learning, anomaly detection, and integrated threat intelligence
to detect when an instance or account might be compromised or if there are threats from
attacks.
B . AWS WAF: Incorrect, as it is a web application firewall that protects against common
web exploits but does not provide comprehensive threat detection.
C . AWS Shield: Incorrect, as it provides protection against DDoS attacks but does not
detect compromises within AWS accounts.
D . Amazon Inspector: Incorrect, as it is a service that helps improve the security and
compliance of applications deployed on AWS by assessing for vulnerabilities, not for threat
detection.
AWS Cloud Reference:
Amazon GuardDuty

</details>

---

### Question 285
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q285`

A company wants to improve its security and audit posture by limiting Amazon EC2
inbound access.
According to the AWS shared responsibility model, which task is the responsibility of the
customer?

- **A)** Protect the global infrastructure that runs all of the services offered in the AWS Cloud.
- **B)** Configure logical access controls for resources, and protect account credentials.
- **C)** Configure the security used by managed services.
- **D)** Patch and back up Amazon Aurora.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

According to the AWS shared responsibility model, the customer is responsible for
configuring logical access controls for resources, and protecting account credentials. This
includes managing IAM user permissions, security group rules, network ACLs, encryption
keys, and other aspects of access management1. AWS is responsible for protecting the
global infrastructure that runs all of the services offered in the AWS Cloud, such as the
hardware, software, networking, and facilities. AWS is also responsible for configuring the
security used by managed services, such as Amazon RDS, Amazon DynamoDB, and
Amazon Aurora2.

</details>

---

### Question 286
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q286`

Which of the following are AWS Cloud design principles? (Select TWO.)

A. Pay for compute resources in advance.

- **B)** Make data-driven decisions to determine cloud architectural design.
- **C)** Emphasize manual processes to allow for changes.
- **D)** Test systems at production scale.
- **E)** Refine operational procedures infrequently.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B, D`

The correct answers are B and D because making data-driven decisions to determine
cloud architectural design and testing systems at production scale are AWS Cloud design
principles. Making data-driven decisions to determine cloud architectural design means
that users should collect and analyze data from their AWS resources and applications to
optimize their performance, availability, security, and cost. Testing systems at production
scale means that users should simulate real-world scenarios and load conditions to
validate the functionality, reliability, and scalability of their systems. The other options are
incorrect because they are not AWS Cloud design principles. Paying for compute
resources in advance means that users have to invest heavily in data centers and servers
before they know how they will use them. This is not a cloud design principle, but rather a
traditional IT model. Emphasizing manual processes to allow for changes means that
users have to rely on huma

</details>

---

### Question 287
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q287`

A company wants an AWS service to provide product recommendations based on its
customer data.
Which AWS service will meet this requirement?

- **A)** Amazon Polly
- **B)** Amazon Personalize
- **C)** Amazon Comprehend
- **D)** Amazon Rekognition

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Personalize is an AWS service that helps developers quickly build and deploy a
custom recommendation engine with real-time personalization and user segmentation1. It
uses machine learning (ML) to analyze customer data and provide relevant
recommendations based on their preferences, behavior, and context.Amazon Personalize
can be used for various use cases such as optimizing recommendations, targeting
customers more accurately, maximizing the value of unstructured text, and promoting
items using business rules1.
The other options are not suitable for providing product recommendations based on
customer data. Amazon Polly is a service that converts text into lifelike speech. Amazon
Comprehend is a service that uses natural language processing (NLP) toextract insights
from text and documents. Amazon Rekognition is a service that uses computer vision (CV)
to analyze images and videos for faces, objects, scenes, and activities.
1: Cloud Products - Amazon Web Services (AWS)
2: Recommen

</details>

---

### Question 288
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q288`

A company is considering using AWS Lambda to host its workloads.
Which option presents the cost benefit of using Lambda?

- **A)** Pay a fixed hourly rate for each Lambda function deployed
- **B)** Pay only for resources used
- **C)** Pay a monthly flat rate
- **D)** Pay only for the entire server instance

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 289
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q289`

A company is using Amazon EC2 instances.
Which tasks are the company's responsibility, according to the AWS shared responsibility
model? (Select TWO.)

- **A)** Manage the underlying hypervisor.
- **B)** Provide physical security for the underlying hardware of the EC2 instances.
- **C)** Patch the guest operating system.
- **D)** Configure a security group on deployed EC2 instances.
- **E)** Maintain the network infrastructure.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C, D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 290
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q290`

Which AWS service can a company use to manage encryption keys in the cloud?

- **A)** AWS License Manager
- **B)** AWS Certificate Manager (ACM)
- **C)** AWS CloudHSM
- **D)** AWS Directory Service

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS CloudHSM provides cloud-based hardware security modules that securely generate,
store, and use cryptographic keys. Customers have control over the HSM users and keys
in their CloudHSM clusters and can use supported interfaces and libraries to perform
cryptographic operations and manage key material. Therefore, option C is correct among
the supplied choices. AWS License Manager helps organizations track and manage
software licenses and licensing rules. AWS Certificate Manager provisions, manages, and
deploys public and private TLS certificates, but it is not the general-purpose customercontrolled encryption-key management service described here. AWS Directory Service
provides managed directory capabilities such as Microsoft Active Directory integration and
is unrelated to cryptographic key storage. In many normal AWS architectures, AWS Key
Management Service would be the primary managed service used to create and control
encryption keys; however, AWS KMS is not include

</details>

---

### Question 291
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q291`

Which group shares responsibility with AWS for security and compliance of AWS accounts
and resources?

- **A)** Third-party vendors
- **B)** Customers
- **C)** Reseller partners
- **D)** Internet providers

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Customers share responsibility with AWS for security and compliance of AWS accounts
and resources. This is part of the AWS shared responsibility model, which defines the
division of responsibilities between AWS and the customer for security and compliance.
AWS is responsible for the security of the cloud, which includes the physical and
environmental controls of the AWS global infrastructure, such as power, cooling, fire
suppression, and physical access. The customer is responsible for the security in the
cloud, which includes the configuration and management of the AWS resources and

applications, such as identity and access management, encryption, firewall, and backup.
For more information, see AWS Shared Responsibility Model and AWS Cloud Security.

</details>

---

### Question 292
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q292`

Which AWS service should a cloud engineer use to view API calls to AWS services?

- **A)** Amazon CloudWatch
- **B)** AWS CloudTrail
- **C)** AWS Config
- **D)** AWS Artifact

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The correct answer is B because AWS CloudTrail is an AWS service that a cloud engineer
can use to view API calls to AWS services. AWS CloudTrail is a service that enables
customers to track user activity and API usage across their AWS account. AWS CloudTrail
records the details of every API call made to AWS services, such as the identity of the
caller, the time of the call, the source IP address of the caller, the parameters and
responses of the call, and more. Customers can use AWS CloudTrail to audit, monitor, and
troubleshoot their AWS resources and actions. The other options are incorrect because
they are not AWS services that a cloud engineer can use to view API calls to AWS
services. Amazon CloudWatch is an AWS service that enables customers to collect,
analyze, and visualize metrics, logs, and events from their AWS resources and
applications. AWS Config is an AWS service that enables customers to assess, audit, and
evaluate the configurations of their AWS resources

</details>

---

### Question 293
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q293`

A company suspects that its AWS resources are being used for illegal activities.
Which AWS group or team should the company notify?

- **A)** AWS Abuse team
- **B)** AWS Support team
- **C)** AWS technical account managers
- **D)** AWS Professional Services team

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Abuse team is the AWS group or team that the company should notify if it suspects
that its AWS resources are being used for illegal activities. AWS Abuse team is a
dedicated team that handles reports of abuse, such as spam, phishing, malware, denial-ofservice attacks, and unauthorized access, involving AWS resources. The company can
contact the AWS Abuse team by filling out the [Report Abuse of AWS Resources form] or
sending an email to abuse@amazonaws.com. The company should provide as much
information as possible, such as the source and destination IP addresses, timestamps, log

files, and screenshots, to help the AWS Abuse team investigate and take appropriate
actions. For more information, see [Reporting Abuse] and [AWS Acceptable Use Policy].

</details>

---

### Question 294
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q294`

A company needs an automated vulnerability management service that continually scans
AWS workloads for software vulnerabilities.
Which AWS service will meet these requirements?

- **A)** Amazon GuardDuty
- **B)** Amazon Inspector
- **C)** AWS Security Hub
- **D)** AWS Shield

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The correct answer is B. Amazon Inspector.
Amazon Inspector is an automated vulnerability management service that continually
scans AWS workloads for software vulnerabilities and unintended network exposure.
Amazon Inspector automatically discovers workloads, such as Amazon EC2 instances,
containers, and Lambda functions, and scans them for software vulnerabilities and
unintended network exposure12.
Amazon GuardDuty is a threat detection service that monitors your AWS accounts and
workloads for malicious or unauthorized activity. Amazon GuardDuty does not scan for
software vulnerabilities, but rather analyzes AWS CloudTrail, Amazon VPC Flow Logs, and
DNS logs to detect threats such as compromised credentials, backdoors, or crypto
mining3.
AWS Security Hub is a security and compliance service that aggregates and prioritizes
security findings from multiple AWS services and partner solutions. AWS Security Hub
does not scan for software vulnerabilities, but rather provides a comprehensive

</details>

---

### Question 295
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q295`

A systems administrator created a new 1AM user for a developer and assigned the user an
access key instead of a user name and password. What is the access key used for?

- **A)** To access the AWS account as the AWS account root user  B. To access the AWS account through the AWS Management Console
- **C)** To access the AWS account through a CLI
- **D)** To access all of a company's AWS accounts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

An access key is a pair of long-term credentials that consists of an access key ID and a
secret access key. An access key is used to sign programmatic requests to the AWS CLI
or AWS API (directly or using the AWS SDK). An access key allows a user to access the
AWS account through a CLI, which is a tool that enables users to interact with AWS
services using commands in a terminal or a script12.
The other options are not correct, because:
To access the AWS account as the AWS account root user, a user needs the email
address and password associated with the account. The root user has complete access to
all AWS resources and services in the account. However, it is not recommended to use the
root user for everyday tasks3.
To access the AWS account through the AWS Management Console, a user needs a user
name and password. The console is a web-based interface that allows users to manage
their AWS resources and services using a graphical user interface4.
To access all of a compan

</details>

---

### Question 296
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q296`

A company wants to verify if multi-factor authentication (MFA) is enabled for all users
within its AWS accounts.
Which AWS service or resource will meet this requirement?

- **A)** AWS Cost and Usage Report
- **B)** IAM credential reports
- **C)** AWS Artifact
- **D)** Amazon CloudFront reports

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The AWS service or resource that will meet the requirement of verifying if multi-factor
authentication (MFA) is enabled for all users within its AWS accounts is IAM credential
reports. IAM credential reports are downloadable reports that list all the users in an AWS
account and the status of their various credentials, including passwords, access keys, and
MFA devices. Users can use IAM credential reports to audit the security status of their
AWS accounts and identify any issues or risks4. AWS Cost and Usage Report, AWS

Artifact, and Amazon CloudFront reports are other AWS services or resources that provide
different types of information, such as billing, compliance, and content delivery, but they do
not show the MFA status of the users.

</details>

---

### Question 297
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q297`

A company needs to centralize its operational data. The company also needs to automate
tasks across all of its Amazon EC2 instances.
Which AWS service can the company use to meet these requirements?

- **A)** AWS Trusted Advisor
- **B)** AWS Systems Manager
- **C)** AWS CodeDeploy
- **D)** AWS Elastic Beanstalk

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Systems Manager is a service that enables users to centralize and automate the
management of their AWS resources. It provides a unified user interface to view
operational data, such as inventory, patch compliance, and performance metrics. It also
allows users to automate common and repetitive tasks, such as patching, backup, and
configuration management, across all of their Amazon EC2 instances1. AWS Trusted
Advisor is a service that provides best practices and recommendations to optimize the
performance, security, and cost of AWS resources2. AWS CodeDeploy is a service that
automates the deployment of code and applications to Amazon EC2 instances or other
compute services3. AWS Elastic Beanstalk is a service that simplifies the deployment and
management of web applications using popular platforms, such as Java, PHP, and
Node.js4.

</details>

---

### Question 298
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q298`

Which AWS feature can a company use to track and categorize expenditures at a detailed
level?

- **A)** AWS cost allocation tags
- **B)** Consolidated billing for AWS Organizations
- **C)** AWS Budgets
- **D)** AWS Marketplace

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Comprehensive and Detailed Explanation From AWS Cloud Documentation:
AWS cost allocation tags are the feature designed to organize resources and attribute their
costs at a detailed level. A tag is a key-value label applied either by the customer or by
AWS. After an eligible cost allocation tag is activated in the Billing and Cost Management
console, AWS can use that tag in cost-management data and reports, allowing charges to
be grouped by values such as application, project, department, environment, or cost
center. This makes option A the direct match for both "track" and "categorize
expenditures." Consolidated billing combines billing and usage across accounts in AWS

Organizations, but it is not itself a resource-labeling mechanism. AWS Budgets compares
cost or usage against thresholds and can generate alerts or actions; it does not provide the
requested detailed categorization method. AWS Marketplace is a catalog and procurement
channel for third-party and AWS software, data, and

</details>

---

### Question 299
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q299`

A new AWS user who has little cloud experience wants to build an application by using
AWS services. The user wants to learn how to implement specific AWS services from
other customer examples. The user also wants to ask questions to AWS experts.
Which AWS service or resource will meet these requirements?

- **A)** AWS Online Tech Talks
- **B)** AWS documentation
- **C)** AWS Marketplace
- **D)** AWS Health Dashboard

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Online Tech Talks are online presentations that cover a broad range of topics at
varying technical levels and provide a live Q&A session with AWS experts. They are a
great resource for new AWS users who want to learn how to implement specific AWS
services from other customer examples and ask questions to AWS experts. AWS
documentation, AWS Marketplace, and AWS Health Dashboard do not offer the same
level of interactivity and guidance as AWS Online Tech Talks. Source: AWS Online Tech
Talks

</details>

---

### Question 300
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q300`

A company has a website on AWS. The company wants to deliver the website to a
worldwide audience and provide low-latency response times for global users.
Which AWS service will meet these requirements?

- **A)** AWS CloudFormation
- **B)** Amazon CloudFront
- **C)** Amazon ElastiCache
- **D)** Amazon DynamoDB

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon CloudFront is AWS's global content delivery network (CDN). It delivers static and
dynamic web content through a worldwide network of edge locations. When a user
requests content, CloudFront routes the request to an appropriate edge location, typically
one that provides the lowest latency, and serves cached content close to the user
whenever possible. This architecture reduces network delay and improves performance for
geographically distributed audiences. AWS CloudFormation provisions infrastructure from
templates; it does not distribute website content. Amazon ElastiCache accelerates

application access to frequently used data but is not a global CDN. Amazon DynamoDB is
a managed NoSQL database service. Therefore, for worldwide website delivery with lowlatency response times, Amazon CloudFront is the appropriate AWS service.

</details>

---

### Question 301
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q301`

Which of the following AWS services are serverless? (Select TWO.)

- **A)** Amazon Elastic Kubernetes Service (Amazon EKS)
- **B)** AWS Outposts
- **C)** AWS Fargate
- **D)** AWS Lambda
- **E)** Amazon EC2

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CD`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 302
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q302`

A company wants to use a serverless compute service for an application. Which AWS
service will meet this requirement?

- **A)** AWS Lambda
- **B)** AWS Cloud Formation
- **C)** AWS Elastic Beanstalk
- **D)** Elastic Load Balancing

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Lambdais a serverless compute service that allows users to run code in response to
events without provisioning or managing servers. It automatically scales the application by
running code only when needed, and users are charged only for the compute time
consumed. This service is ideal for applications that require event-driven compute
functions.
B . AWS CloudFormation: Incorrect, as it is an infrastructure-as-code service that helps
users automate the deployment of AWS resources, not a serverless compute service.
C . AWS Elastic Beanstalk: Incorrect, as it is a Platform-as-a-Service (PaaS) that still
involves managing servers, even though it abstracts much of the infrastructure
management.

D . Elastic Load Balancing: Incorrect, as it is a service for distributing incoming application
or network traffic across multiple targets, not a serverless compute service.
AWS Cloud Reference:
AWS Lambda

</details>

---

### Question 303
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q303`

Which AWS service or feature is used to send both text and email messages from
distributed applications?

- **A)** Amazon Simple Notification Service (Amazon SNS)
- **B)** Amazon Simple Email Service (Amazon SES)
- **C)** Amazon CloudWatch alerts
- **D)** Amazon Simple Queue Service (Amazon SQS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Amazon Simple Notification Service (Amazon SNS) is the AWS service or feature that is
used to send both text and email messages from distributed applications. Amazon SNS is
a fully managed pub/sub messaging service that enables the user to send messages to
multiple subscribers or endpoints, such as email addresses, phone numbers, HTTP
endpoints, AWS Lambda functions, and more. Amazon SNS can be used to send
notifications, alerts, confirmations, and reminders from applications to users or other
applications4.

</details>

---

### Question 304
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q304`

Which AWS service or feature gives users the ability to connect VPCs and on-premises
networks to a central hub?

- **A)** Virtual private gateway
- **B)** AWS Transit Gateway
- **C)** Internet gateway
- **D)** Customer gateway

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Transit Gatewayis a network transit hub that customers can use to connect their
Amazon VPCs and on-premises networks to a central hub. This service simplifies network
management and reduces operational overhead by enabling a single gateway for
managing multiple network connections. It facilitates seamless integration and routing
between VPCs and on-premises networks.
A . Virtual private gateway: Incorrect, as it is used to connect a single VPC to an onpremises network through a VPN connection.
C . Internet gateway: Incorrect, as it provides internet access for instances in a VPC but
does not connect multiple networks.
D . Customer gateway: Incorrect, as it represents the on-premises device or software
application that connects to AWS, but it does not provide a central hub.
AWS Cloud Reference:

AWS Transit Gateway

</details>

---

### Question 305
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q305`

A company has a physical tape library to store data backups. The tape library is running
out of space. The company needs to extend the tape library's capacity to the AWS Cloud.
Which AWS service should the company use to meet this requirement?

- **A)** Amazon Elastic File System (Amazon EFS)
- **B)** Amazon Elastic Block Store (Amazon EBS)
- **C)** Amazon S3
- **D)** AWS Storage Gateway

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Storage Gateway is a hybrid cloud storage service that provides on-premises access
to virtually unlimited cloud storage. You can use AWS Storage Gateway to simplify storage
management and reduce costs for key hybrid cloud storage use cases. One of these use
cases is tape-based backup, which allows you to store data backups on virtual tapes in the
AWS Cloud. You can use the Tape Gateway feature of AWS Storage Gateway to extend
your existing physical tape library to the AWS Cloud. Tape Gateway provides a virtual tape
infrastructure that scales seamlessly with your backup needs and eliminates the
operational burden of provisioning, scaling, and maintaining a physical tape
infrastructure123. Reference: 1: Cloud Storage Appliances, Hybrid Device - AWS Storage
Gateway - AWS, 2: AWS Storage Gateway Documentation, 3: AWS Storage Gateway
Features | Amazon Web Services

</details>

---

### Question 306
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q306`

Which cloud concept is demonstrated by using AWS Cost Explorer?

- **A)** Reliability
- **B)** Modernization
- **C)** Rightsizing
- **D)** Resilience

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 307
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q307`

A company is deploying a Multi-AZ Amazon RDS database. The company wants to
understand which failover tasks AWS will handle automatically.
According to the AWS shared responsibility model, which task is AWS responsible for?

- **A)** Configuring the application to reconnect to the database after a failover event
- **B)** Automatically promoting the standby instance to the primary database during a failure
- **C)** Enabling Multi-AZ deployment for the RDS database instance
- **D)** Monitoring the database and application performance after a failover event

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Comprehensive and Detailed Explanation From AWS Cloud Documentation:

For an Amazon RDS Multi-AZ DB instance deployment, Amazon RDS provides the
managed high-availability and failover mechanism. If a qualifying planned or unplanned
outage affects the primary DB instance, RDS automatically switches to the standby replica
in another Availability Zone. This automatic promotion or failover is performed by AWS as
part of the managed RDS service, so option B is correct. The customer must first choose
and enable a Multi-AZ deployment; AWS does not decide to enable that architecture on
the customer's behalf, which eliminates option C. The application must also be designed to
recover connections after failover, normally by reconnecting through the unchanged DB
endpoint after DNS updates propagate, which eliminates option A. Monitoring application
behavior, business transactions, latency, and post-failover performance also remains part
of the customer's operational responsibility, even though A

</details>

---

### Question 308
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q308`

Which task is a responsibility of AWS, according to the AWS shared responsibility model?

- **A)** Maintain the physical hardware of the infrastructure.
- **B)** Configure security groups for Amazon EC2 instances.
- **C)** Manage encryption options for data that is stored on AWS.
- **D)** Configure identity and access management for applications.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 309
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q309`

A company is running and managing its own Docker environment on Amazon EC2
instances. The company wants an alternative to help manage cluster size, scheduling, and
environment maintenance.
Which AWS service meets these requirements?

- **A)** AWS Lambda
- **B)** Amazon RDS
- **C)** AWS Fargate
- **D)** Amazon Athena

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Fargate is a serverless compute engine for containers that works with both Amazon
Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service
(Amazon EKS). AWS Fargate allows you to run containers without having to manage
servers or clusters of Amazon EC2 instances. With AWS Fargate, you only pay for the
compute resources you use to run your containers, and you don't need to worry about
scaling, patching, securing, or maintaining the underlying infrastructure. AWS Fargate
simplifies the deployment and management of containerized applications, and enables you

to focus on building and running your applications instead of managing the infrastructure.
Reference: AWS Fargate, What is AWS Fargate?

</details>

---

### Question 310
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q310`

A company wants to monitor its workload performance. The company wants to ensure that
the cloud services are delivered at a level that meets its business needs.
Which AWS Cloud Adoption Framework (AWS CAF) perspective will meet these
requirements?

- **A)** Business
- **B)** Governance
- **C)** Platform
- **D)** Operations

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

The Operations perspective helps you monitor and manage your cloud workloads to
ensure that they are delivered at a level that meets your business needs. Common
stakeholders include chief operations officer (COO), cloud director, cloud operations
manager, and cloud operations engineers1. The Operations perspective covers
capabilities such as workload health monitoring, incident management, change
management, release management, configuration management, and disaster recovery2.
The Business perspective helps ensure that your cloud investments accelerate your digital
transformation ambitions and business outcomes. Common stakeholders include chief
executive officer (CEO), chief financial officer (CFO), chief information officer (CIO), and
chief technology officer (CTO). The Business perspective covers capabilities such as
business case development, value realization, portfolio management, and stakeholder
management3.
The Governance perspective helps you orchestrate your cloud initiatives

</details>

---

### Question 311
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q311`

A company uses Amazon EC2 instances to run its application. The application needs to be
available and running continuously for three or more years. What type of EC2 instance
should the company purchase for a discount on the EC2 pricing?

- **A)** Reserved Instances
- **B)** On-Demand Instances
- **C)** Spot Instances
- **D)** EC2 Fleet

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 312
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q312`

Which of the following are advantages of moving to the AWS Cloud? (Select TWO.)

- **A)** The ability to turn over the responsibility for all security to AWS.
- **B)** The ability to use the pay-as-you-go model.
- **C)** The ability to have full control over the physical infrastructure.
- **D)** No longer having to guess what capacity will be required.
- **E)** No longer worrying about users access controls.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B, D`

The advantages of moving to the AWS Cloud are the ability to use the pay-as-you-go
model and no longer having to guess what capacity will be required. The pay-as-you-go
model allows the user to pay only for the resources they use, without any upfront or longterm commitments. This reduces the cost and risk of over-provisioning or underprovisioning resources. No longer having to guess what capacity will be required means
that the user can scale their resources up or down according to the demand, without
wasting money on idle resources or losing customers due to insufficient capacity4.

</details>

---

### Question 313
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q313`

A company wants to control the protection of its AWS resources. The company wants to
block SQL injection attacks and cross-site scripting.
Which AWS service or feature meets these requirements?

- **A)** Security groups
- **B)** Amazon GuardDuty
- **C)** AWSWAF
- **D)** AWS Shield

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 314
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q314`

A company wants to migrate its on-premises NoSQL workload to Amazon DynamoDB.
Which AWS service will meet this requirement?

A. Migration Evaluator

- **B)** AWS Migration Hub
- **C)** AWS Application Migration Service
- **D)** AWS Database Migration Service (AWS DMS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 315
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q315`

A company wants to store data with high availability, encrypt the data at rest, and have
direct access to the data over the internet.
Which AWS service will meet these requirements MOST cost-effectively?

- **A)** Amazon Elastic Block Store (AmazonEBS)
- **B)** Amazon S3
- **C)** Amazon Elastic File System (Amazon EFS)
- **D)** AWS Storage Gateway

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed
elastic NFS file system for use with AWS Cloud services and on-premises resources. It is
built to scale on demand to petabytes without disrupting applications, growing and
shrinking automatically as you add and remove files, eliminating the need to provision and
manage capacity to accommodate growth. Amazon EFS offers two storage classes: the
Standard storage class, and the Infrequent Access storage class (EFS IA). EFS IA
provides price/performance that is cost-optimized for files not accessed every day.
Amazon EFS encrypts data at rest and in transit, and supports direct access over the
internet4.

</details>

---

### Question 316
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q316`

A company wants to migrate its on_premises workloads to the AWS Cloud. The company
wants to separate workloads for chargeback to different departments.
Which AWS services or features will meet these requirements? (Select TWO.)

- **A)** Placement groups
- **B)** Consolidated billing
- **C)** Edge locations
- **D)** AWS Config
- **E)** Multiple AWS accounts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `BE`

Consolidated billing is a feature of AWS Organizations that enables customers to
consolidate billing and payment for multiple AWS accounts. With consolidated billing,
customers can group multiple AWS accounts under one payer account, making it easier to
manage billing and track costs across multiple accounts. Consolidated billing also offers
benefits such as volume discounts, Reserved Instance discounts, and Savings Plans
discounts. Consolidated billing is offered at no additional cost.

Multiple AWS accounts is a feature of AWS Organizations that enables customers to
create and manage multiple AWS accounts from a central location. With multiple AWS
accounts, customers can isolate workloads for different departments, projects, or
environments, and apply granular access controls and policies to each account. Multiple
AWS accounts also helps customers improve security, compliance, and governance of
their AWS resources56. Reference: 5: Consolidated billing for AWS Organizations - AWS
Bil

</details>

---

### Question 317
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q317`

How can an AWS user conduct security assessments of Amazon EC2 instances, NAT
gateways, and Elastic Load Balancers in a way that is approved by AWS?

- **A)** Flood a target with requests.
- **B)** Use Amazon Inspector.
- **C)** Perform penetration testing.
- **D)** Use the AWS Service Health Dashboard.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Inspector is an automated security assessment service that helps improve the
security and compliance of applications deployed on AWS. Amazon Inspector
automatically assesses applications for exposure, vulnerabilities, and deviations from best
practices. After performing an assessment, Amazon Inspector produces a detailed list of
security findings prioritized by level of severity2.

</details>

---

### Question 318
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q318`

company wants to protect its AWS Cloud information, systems, and assets while
performing risk assessment and mitigation tasks.
Which pillar of the AWS Well-Architected Framework is supported by these goals?

- **A)** Reliability
- **B)** Security
- **C)** Operational excellence
- **D)** Performance efficiency

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The pillar of the AWS Well-Architected Framework that is supported by the goals of
protecting AWS Cloud information, systems, and assets while performing risk assessment
and mitigation tasks is security. Security is the ability to protect information, systems, and
assets while delivering business value through risk assessments and mitigation strategies.
The security pillar covers topics such as identity and access management, data protection,
infrastructure protection, detective controls, incident response, and compliance

</details>

---

### Question 319
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q319`

A company runs an uninterruptible Amazon EC2 workload on AWS 24 hours a day. 7 days
a week. The company will require the same instance family and instance type to run the
workload for the next 12 months.
Which combination of purchasing options should the company choose to MOST optimize
costs? (Select TWO.)

- **A)** Standard Reserved Instance
- **B)** Convertible Reserved Instance
- **C)** Compute Savings Plan
- **D)** Spot Instance
- **E)** All Upfront payment

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AE`

For workloads running 24/7 for a year, Standard Reserved Instances provide a significant
discount compared to On-Demand pricing. Choosing the "All Upfront" payment option
maximizes the cost savings as AWS offers the highest discount for upfront payments.
Convertible Reserved Instances provide flexibility to change the instance type but usually
at a slightly higher cost than Standard Reserved Instances. Compute Savings Plans offer
cost savings, but in this scenario, the best optimization would be a combination of
Standard Reserved Instances with All Upfront payment. Spot Instances are not suitable
due to their interruptible nature.
Reference:
AWS EC2 Reserved Instances
AWS Savings Plans

</details>

---

### Question 320
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q320`

An auditor needs to find out whether a specific AWS service is compliant with specific
compliance frameworks.
Which AWS service will provide this information?

- **A)** AWS Artifact
- **B)** AWS Trusted Advisor
- **C)** Amazon GuardDuty
- **D)** AWS Certificate Manager (ACM)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Artifact is the service that will provide the information about whether a specific AWS
service is compliant with specific compliance frameworks. AWS Artifact is a self-service
portal that allows you to access, review, and download AWS security and compliance
reports and agreements. You can use AWS Artifact to verify the compliance status of AWS
services across various regions and compliance programs, such as ISO, PCI, SOC,
FedRAMP, HIPAA, and more12

</details>

---

### Question 321
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q321`

A company needs to block SQL injection attacks.
Which AWS service or feature can meet this requirement?

- **A)** AWS WAF
- **B)** AWS Shield
- **C)** Network ACLs
- **D)** Security groups

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS WAF is a web application firewall that helps protect web applications from common
web exploits, such as SQL injection attacks. It allows customers to create custom rules
that block malicious requests. AWS Shield is a managed service that protects against
distributed denial of service (DDoS) attacks, not SQL injection attacks. Network ACLs and
security groups are network-level security features that filter traffic based on IP addresses
and ports, not web requests or SQL queries. Reference: [AWS WAF], [AWS Shield],
[Network ACLs], [Security groups]

</details>

---

### Question 322
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q322`

Which AWS service requires the customer to patch the guest operating system?

- **A)** AWS Lambda
- **B)** Amazon OpenSearch Service
- **C)** Amazon EC2
- **D)** Amazon ElastiCache

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS service that requires the customer to patch the guest operating system is
Amazon EC2. Amazon EC2 is a service that provides scalable compute capacity in the
cloud, and allows customers to launch and run virtual servers, called instances, with a
variety of operating systems, configurations, and specifications. The customer is
responsible for patching and updating the guest operating system and any applications
that run on the EC2 instances, as part of the security in the cloud. AWS Lambda, Amazon
OpenSearch Service, and Amazon ElastiCache are not services that require the customer
to patch the guest operating system. AWS Lambda is a serverless compute service that
allows customers to run code without provisioning or managing servers. Amazon
OpenSearch Service is a fully managed service that makes it easy to deploy, operate, and
scale OpenSearch clusters in the AWS Cloud. Amazon ElastiCache is a fully managed

service that provides in-memory data store and cache solutions, such

</details>

---

### Question 323
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q323`

Which benefit of cloud computing gives a company the ability to deploy applications to
users all over the world through a network of AWS Regions, Availability Zones, and edge
locations?

- **A)** Global reach
- **B)** Economy of scale
- **C)** Agility
- **D)** High availability

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 324
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q324`

Which AWS service can provide a dedicated network connection with consistent low
latency from on premises to the AWS Cloud?

- **A)** Amazon VPC
- **B)** Amazon Kinesis Data Streams
- **C)** AWS Direct Connect
- **D)** Amazon OpenSearch Service

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Direct Connect is a service that provides a dedicated network connection from on
premises to the AWS Cloud. It can reduce network costs, increase bandwidth throughput,
and provide a more consistent network experience than internet-based connections. It can
also provide low latency for applications that require real-time data transfer4. Amazon VPC
is a service that provides a logically isolated section of the AWS Cloud where users can
launch AWS resources in a virtual network that they define. Amazon Kinesis Data Streams
is a service that provides a scalable and durable stream of data records for real-time data
processing. Amazon OpenSearch Service is a service that provides a fully managed,
scalable, and secure search and analytics solution that is compatible with Elasticsearch.

</details>

---

### Question 325
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q325`

Which of the following are general AWS Cloud design principles described in the AWS
Well-Architected Framework?

- **A)** Consolidate key components into monolithic architectures.
- **B)** Test systems at production scale.
- **C)** Provision more capacity than a workload is expected to need.
- **D)** Drive architecture design based on data collected about the workload behavior and requirements.
- **E)** Make AWS Cloud architectural decisions static, one-time events.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `BD`

These are two of the general AWS Cloud design principles described in the AWS WellArchitected Framework. Testing systems at production scale means using tools such as
AWS CloudFormation, AWS CodeDeploy, and AWS X-Ray to simulate real-world
scenarios and measure the performance, scalability, and availability of the system. Driving
architecture design based on data means using tools such as Amazon CloudWatch, AWS
CloudTrail, and AWS Config to collect and analyze metrics, logs, and events about the
system and use the insights to optimize the system's design and operation. You can learn
more about the AWS Well-Architected Framework from this whitepaper or [this digital
course].

</details>

---

### Question 326
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q326`

Which AWS service provides on-premises applications with low-latency access to data that
is stored in the AWS Cloud?

- **A)** Amazon CloudFront
- **B)** AWS Storage Gateway
- **C)** AWS Backup
- **D)** AWS DataSync

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Storage Gateway provides on-premises applications with low-latency access to data
stored in AWS by caching frequently accessed data locally. It seamlessly integrates onpremises environments with cloud storage, enabling hybrid storage solutions. AWS
DataSync is for data transfer, CloudFront is a content delivery network, and AWS Backup
is for backup management, not low-latency access.

</details>

---

### Question 327
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q327`

A company wants a time-series database service that makes it easier to store and analyze
trillions of events each day.
Which AWS service will meet this requirement?

- **A)** Amazon Neptune
- **B)** Amazon Timestream
- **C)** Amazon Forecast
- **D)** Amazon DocumentDB (with MongoDB compatibility)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Timestream is a fast, scalable, and serverless time-series database service for
IoT and other operational applications that makes it easy to store and analyze trillions of
events per day up to 1,000 times faster and at as little as 1/10th thecost of relational
databases1. Amazon Timestream saves you time and cost in managing the lifecycle of
time series data, and its purpose-built query engine lets you access and analyze recent
and historical data together with a single query1. Amazon Timestream has built-in time
series analytics functions, helping you identify trends and patterns in near real time1.

The other options are not suitable for storing and analyzing trillions of events per day.
Amazon Neptune is a graph database service that supports highly connected data sets.
Amazon Forecast is a machine learning service that generates accurate forecasts based
on historical data. Amazon DocumentDB (with MongoDB compatibility) is a document
database service that supports MongoDB wo

</details>

---

### Question 328
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q328`

Which of the following are advantages of moving to the AWS Cloud? (Select TWO.)

- **A)** Users can implement all AWS services in seconds.
- **B)** AWS assumes all responsibility for the security of infrastructure and applications.
- **C)** Users experience increased speed and agility.
- **D)** Users benefit from massive economies of scale.
- **E)** Users can move hardware from their data center to the AWS Cloud.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `CD`

Moving to the AWS Cloud offers several advantages, including increased speed and
agility, which allows users to experiment, innovate, and iterate faster by using the global
AWS infrastructure. Additionally, AWS offers massive economies of scale due to its large
customer base, leading to lower pay-as-you-go prices. AWS does not assume all
responsibilities for the security of infrastructure and applications; it follows a shared
responsibility model. Also, not all AWS services can be implemented in seconds, and
physical hardware cannot be moved from a user's data center to the AWS Cloud.
Reference:
AWS Cloud Benefits

</details>

---

### Question 329
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q329`

Which AWS solution gives companies the ability to use protocols such as NFS to store and
retrieve objects in Amazon S3?

- **A)** Amazon FSx for Lustre
- **B)** AWS Storage Gateway volume gateway
- **C)** AWS Storage Gateway file gateway
- **D)** Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Storage Gateway file gateway allows companies to use protocols such as NFS and
SMB to store and retrieve objects in Amazon S3. File gateway provides a seamless
integration between on-premises applications and Amazon S3, and enables low-latency
access to data through local caching. File gateway also supports encryption, compression,
and lifecycle management of the objects in Amazon S3. For more information, see What is
AWS Storage Gateway? and File Gateway.

</details>

---

### Question 330
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q330`

A company has all of its servers in the us-east-1 Region. The company is considering the
deployment of additional servers different Region.
Which AWS tool should the company use to find pricing information for other Regions?

- **A)** Cost Explorer
- **B)** AWS Budgets
- **C)** AWS Purchase Order Management
- **D)** AWS Pricing Calculator

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Pricing Calculator lets customers explore AWS services, and create an estimate for
the cost of their use cases on AWS. AWS Pricing Calculator can also compare the costs of
different AWS Regions and configurations. Cost Explorer is a tool that enables customers
to visualize, understand, and manage their AWS costs and usage over time. AWS Budgets
gives customers the ability to set custom budgets that alert them when their costs or usage
exceed (or are forecasted to exceed) their budgeted amount. AWS Purchase Order
Management is a feature that allows customers to pay for their AWS invoices using
purchase orders.

</details>

---

### Question 331
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q331`

Which AWS design principle emphasizes the reduction of interdependencies between
components of an application?

- **A)** Caching
- **B)** Automation
- **C)** Scalability
- **D)** Loose coupling

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 332
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q332`

A company is considering migration to the AWS Cloud. The company wants a fully
managed service or feature that can transfer streaming data from multiple sources to an
Amazon S3 bucket.
Which AWS service or feature should the company use to meet these requirements?

- **A)** AWS DataSync  B. Amazon Kinesis Data Firehose
- **C)** S3 Select
- **D)** AWS Transfer Family

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Kinesis Data Firehose is a fully managed service that delivers real-time streaming
data to destinations such as Amazon S3, Amazon Redshift, Amazon Elasticsearch
Service, and Splunk. You can use Amazon Kinesis Data Firehose to capture, transform,
and load streaming data from multiple sources, such as web applications, mobile devices,
IoT sensors, and social media.

</details>

---

### Question 333
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q333`

What is a benefit of using an Elastic Load Balancing (ELB) load balancer with applications
running in the AWS Cloud?

- **A)** An ELB will automatically scale resources to meet capacity needs.
- **B)** An ELB can balance traffic across multiple compute resources.
- **C)** An ELB can span multiple AWS Regions.
- **D)** An ELB can balance traffic between multiple internet gateways.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Elastic Load Balancing (ELB) distributes incoming traffic across multiple targets, such as
EC2 instances, containers, and IP addresses, ensuring better application availability and
fault tolerance. While ELB scales to meet traffic demands, it does not inherently scale
compute resources themselves, span multiple regions, or balance traffic between internet
gateways.

</details>

---

### Question 334
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q334`

A company is planning to move data backups to the AWS Cloud. The company needs to
replace on-premises storage with storage that is cloud-based but locally cached.
Which AWS service meets these requirements?

- **A)** AWS Storage Gateway
- **B)** AWS Snowcone
- **C)** AWS Backup
- **D)** Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Storage Gatewayis a hybrid cloud storage service that provides on-premises access
to virtually unlimited cloud storage. TheFile Gatewayconfiguration allows for on-premises
applications to store data in Amazon S3 using NFS and SMB protocols, while keeping
frequently accessed data cached locally. This meets the company's requirement for cloudbased storage that is locally cached.
B . AWS Snowcone: Incorrect, as it is a portable edge computing and storage device, not a
storage service that provides local caching for cloud storage.

C . AWS Backup: Incorrect, as it is a centralized backup service to automate data
protection across AWS services but does not provide local caching.
D . Amazon Elastic File System (Amazon EFS): Incorrect, as it provides scalable file
storage for use with Amazon EC2 but does not offer local caching for on-premises storage
needs.
AWS Cloud Reference:
AWS Storage Gateway

</details>

---

### Question 335
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q335`

Which design principles should a company apply to AWS Cloud workloads to maximize
sustainability and minimize environmental impact? (Select TWO.)

- **A)** Maximize utilization of Amazon EC2 instances.
- **B)** Minimize utilization of Amazon EC2 instances.
- **C)** Minimize usage of managed services.
- **D)** Force frequent application reinstallations by users.
- **E)** Reduce the need for users to reinstall applications.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AE`

To maximize sustainability and minimize environmental impact, a company should apply
the following design principles to AWS Cloud workloads: maximize utilization of Amazon
EC2 instances and reduce the need for users to reinstall applications. Maximizing
utilization of Amazon EC2 instances means that the company can optimize the
performance and efficiency of their compute resources, and avoid wasting energy and
money on idle or underutilized instances. The company can use features such as Amazon
EC2 Auto Scaling, Amazon EC2 Spot Instances, and AWS Compute Optimizer to
automatically adjust the number and type of instances based on demand, cost, and
performance. Reducing the need for users to reinstall applications means that the
company can minimize the amount of data and bandwidth required to deliver their
applications to users, and avoid unnecessary downloads and updates that consume
energy and resources. The company can use services such as Amazon CloudFront, AWS
AppStream 2.0, and AW

</details>

---

### Question 336
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q336`

A large company has a workload that requires hardware to remain on premises. The
company wants to use the same management and control plane services that it currently
uses on AWS.
Which AWS service should the company use to meet these requirements?

- **A)** AWS Device Farm
- **B)** AWS Fargate
- **C)** AWS Outposts
- **D)** AWS Ground Station

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because AWS Outposts is an AWS service that enables the
company to meet the requirements. AWS Outposts is a fully managed service that extends
AWS infrastructure, services, APIs, and tools to virtually any datacenter, co-location space,
or on-premises facility. AWS Outposts allows customers to run their workloads on the
same hardware and software that AWS uses in its cloud, while maintaining local access
and control. The other options are incorrect because they are not AWS services that
enable the company to meet the requirements. AWS Device Farm is an AWS service that
enables customers to test their mobile and web applications on real devices in the AWS
Cloud. AWS Fargate is an AWS service that enables customers to run containers without
having to manage servers or clusters. AWS Ground Station is an AWS service that
enables customers to communicate with satellites and downlink data from orbit. Reference:
AWS Outposts FAQs

</details>

---

### Question 337
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q337`

A company wants durable storage for static content and infinitely scalable data storage
infrastructure at the lowest cost.
Which AWS service should the company choose?

- **A)** Amazon Elastic Block Store (Amazon EBS)
- **B)** Amazon S3
- **C)** AWS Storage Gateway
- **D)** Amazon Elastic File System (Amazon EFS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon S3 is a service that provides durable storage for static content and infinitely
scalable data storage infrastructure at the lowest cost. Amazon S3 is an object storage
service that allows you to store and retrieve any amount of data from anywhere on the
internet. Amazon S3 offers industry-leading scalability, availability, and performance, as
well as 99.999999999% (11 9s) of durability and multi-AZ resilience. Amazon S3 also
provides various storage classes that offer different levels of performance and cost
optimization, such as S3 Standard, S3 Intelligent-Tiering, S3 Standard-Infrequent Access
(S3 Standard-IA), S3 One Zone-Infrequent Access (S3 One Zone-IA), and S3 Glacier456.

Amazon S3 is ideal for storing static content, such as images, videos, documents, and web
pages, as well as building data lakes, backup and archive solutions, big data analytics, and
machine learning applications456. Reference: 4: Cloud Storage on AWS, 5: Object
Storage - Amazon Simple Storage Service

</details>

---

### Question 338
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q338`

Which perspective of the AWS Cloud Adoption Framework (AWS CAF) encourages the
development of well- architected, cloud-focused applications?

- **A)** Platform
- **B)** Operations
- **C)** Governance
- **D)** Security

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 339
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q339`

Which duties are the responsibility of a company that is using AWS Lambda? (Select
TWO.)

- **A)** Security inside of code
- **B)** Selection of CPU resources
- **C)** Patching of operating system
- **D)** Writing and updating of code
- **E)** Security of underlying infrastructure

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A, D`

The duties that are the responsibility of a company that is using AWS Lambda are security
inside of code and writing and updating of code. AWS Lambda is a serverless compute
service that allows you to run code without provisioning or managing servers, scaling, or
patching. AWS Lambda takes care of the security of the underlying infrastructure, such as
the operating system, the network, and the firewall. However, the company is still
responsible for the security of the code itself, such as encrypting sensitive data, validating
input, and handling errors. The company is also responsible for writing and updating the
code that defines the Lambda function, and choosing the runtime environment, such as
Node.js, Python, or Java. AWS Lambda does not require the selection of CPU resources,
as it automatically allocates them based on the memory configuration34

</details>

---

### Question 340
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q340`

A company is using Amazon RDS.
A company is launching a critical business application in an AWS Region.
How can the company increase resilience for this application?

- **A)** Deploy a copy of the application in another AWS account.
- **B)** Deploy the application by using multiple VPCs.
- **C)** Deploy the application by using multiple subnets.  D. Deploy the application by using multiple Availability Zones.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Deploying the application by using multiple Availability Zones is the best way to increase
resilience for the application. According to the Amazon RDS User Guide, "Amazon RDS
provides high availability and failover support for DB instances using Multi-AZ
deployments. In a Multi-AZ deployment, Amazon RDS automatically provisions and
maintains a synchronous standby replica in a different Availability Zone. The primary DB
instance is synchronously replicated across Availability Zones to a standby replica to
provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system
backups."4 Deploying a copy of the application in another AWS account, using multiple
VPCs, or using multiple subnets do not provide the same level of resilience as using
multiple Availability Zones.

</details>

---

### Question 341
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q341`

A company has 5 TB of data stored in Amazon S3. The company plans to occasionally run
queries on the data for analysis.
Which AWS service should the company use to run these queries in the MOST costeffective manner?

- **A)** Amazon Redshift
- **B)** Amazon Athena
- **C)** Amazon Kinesis
- **D)** Amazon RDS

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Athena is a serverless, interactive analytics service that allows users to run SQL
queries on data stored in Amazon S3. It is ideal for occasional queries on large datasets,
as it does not require any server provisioning, configuration, or management. Users only
pay for the queries they run, based on the amount of data scanned. Amazon Athena
supports various data formats, such as CSV, JSON, Parquet, ORC, and Avro, and
integrates with AWS Glue Data Catalog to create and manage schemas. Amazon Athena
also supports querying data from other sources, such as on-premises or other cloud
systems, using data connectors1.
Amazon Redshift is a fully managed data warehouse service that allows users to run
complex analytical queries on petabyte-scale data. However, it requires users to provision
and maintain clusters of nodes, and pay for the storage and compute capacity they use.
Amazon Redshift is more suitable for frequent and consistent queries on structured or
semi-structured data2.
Ama

</details>

---

### Question 342
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q342`

A company wants an automated process to continuously scan its Amazon EC2 instances
for software vulnerabilities.
Which AWS service will meet these requirements?

- **A)** Amazon GuardDuty
- **B)** Amazon Inspector
- **C)** Amazon Detective
- **D)** Amazon Cognito

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon Inspector is the AWS service that can be used to perform vulnerability scans on
AWS EC2 instances for software vulnerabilities automatically in a periodic fashion.
Amazon Inspector automatically discovers EC2 instances and scans them for software
vulnerabilities and unintended network exposure. Amazon Inspector uses AWS Systems
Manager (SSM) and the SSM Agent to collect information about the software application
inventory of the EC2 instances. This data is then scanned by Amazon Inspector for
software vulnerabilities12. Amazon Inspector also integrates with other AWS services,
such as Amazon EventBridge and AWS Security Hub, to automate discovery, expedite
vulnerability routing, and shorten mean time to remediate (MTTR) vulnerabilities2.

</details>

---

### Question 343
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q343`

For which AWS service is the customer responsible for maintaining the underlying
operating system?

- **A)** Amazon DynamoDB
- **B)** Amazon S3
- **C)** Amazon EC2
- **D)** AWS Lambda

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon EC2 is a service that provides resizable compute capacity in the cloud. Users can
launch and manage virtual servers, known as instances, that run on the AWS
infrastructure. Users are responsible for maintaining the underlying operating system of the

instances, as well as any applications or software that run on them. Amazon DynamoDB is
a service that provides a fully managed NoSQL database that delivers fast and consistent
performance at any scale. Users do not need to manage the underlying operating system
or the database software. Amazon S3 is a service that provides scalable and durable
object storage in the cloud. Users do not need to manage the underlying operating system
or the storage infrastructure. AWS Lambda is a service that allows users to run code
without provisioning or managing servers. Users only need to upload their code and
configure the triggers and parameters. AWS Lambda takes care of the underlying
operating system and the execution environment.

</details>

---

### Question 344
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q344`

A company wants to securely store Amazon RDS database credentials and automatically
rotate user passwords periodically.
Which AWS service or capability will meet these requirements?

- **A)** Amazon S3
- **B)** AWS Systems Manager Parameter Store
- **C)** AWS Secrets Manager
- **D)** AWS CloudTrail

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Secrets Manager is a service that helps you protect access to your applications,
services, and IT resources. This service enables you to easily rotate, manage, and retrieve
database credentials, API keys, and other secrets throughout their lifecycle1. Amazon S3
is a storage service that does not offer automatic rotation of credentials. AWS Systems
Manager Parameter Store is a service that provides secure, hierarchical storage for
configuration data management and secrets management2, but it does not offer automatic
rotation of credentials. AWS CloudTrail is a service that enables governance, compliance,
operational auditing, and risk auditing of your AWS account3, but it does not store or rotate
credentials.

</details>

---

### Question 345
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q345`

A company manages factory machines in real time. The company wants to use AWS
technology to deploy its monitoring applications as close to the factory machines as
possible.
Which AWS solution will meet these requirements with the LEAST latency?

- **A)** AWS Outposts
- **B)** Amazon EC2
- **C)** AWS App Runner
- **D)** AWS Batch

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Outposts is a fully managed service that extends AWS infrastructure, AWS services,
APIs, and tools to virtually any datacenter, co-location space, or on-premises facility for a

truly consistent hybrid experience. AWS Outposts enables you to run AWS services in your
on-premises data center1.

</details>

---

### Question 346
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q346`

Which AWS service provides access to AWS security and compliance reports for audits?

- **A)** Amazon Inspector
- **B)** Amazon GuardDuty
- **C)** AWS Artifact
- **D)** Amazon Detective

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 347
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q347`

Which AWS service or feature should a company use between two microservices to
ensure that messages are sent and received in exact order?

- **A)** Amazon Simple Email Service (Amazon SES)
- **B)** Amazon S3 Event Notifications
- **C)** Amazon Simple Queue Service (Amazon SQS) FIFO queues
- **D)** Amazon Simple Notification Service (Amazon SNS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 348
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q348`

Which AWS services are supported by Savings Plans? (Select TWO.)

- **A)** Amazon EC2
- **B)** Amazon RDS
- **C)** Amazon SageMaker
- **D)** Amazon Redshift
- **E)** Amazon DynamoDB

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AC`

The AWS services that are supported by Savings Plans are:
Amazon EC2: Amazon EC2 is a service that provides scalable computing capacity in the
AWS cloud. You can use Amazon EC2 to launch virtual servers, configure security and

networking, and manage storage. Amazon EC2 is eligible for both Compute Savings Plans
and EC2 Instance Savings Plans12.
Amazon SageMaker: Amazon SageMaker is a service that helps you build and deploy
machine learning models. You can use Amazon SageMaker to access Jupyter notebooks,
use common machine learning algorithms, train and tune models, and deploy them to a
hosted environment. Amazon SageMaker is eligible for SageMaker Savings Plans13.
The other options are not supported by Savings Plans. Amazon RDS, Amazon Redshift,
and Amazon DynamoDB are database services that are eligible for Reserved Instances,
but not Savings Plans4.

</details>

---

### Question 349
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q349`

A developer wants to use an Amazon S3 bucket to store application logs that contain
sensitive data.
Which AWS service or feature should the developer use to restrict read and write access
to the S3 bucket?

- **A)** Security groups
- **B)** Amazon CloudWatch
- **C)** AWS CloudTrail
- **D)** ACLs

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

ACLs are an AWS service or feature that the developer can use to restrict read and write
access to the S3 bucket. ACLs are access control lists that grant basic permissions to
other AWS accounts or predefined groups. They can be used to grant read or write access
to an S3 bucket or an object3. Security groups are virtual firewalls that control the inbound
and outbound traffic for Amazon EC2 instances. They are not a service or feature that can
be used to restrict access to an S3 bucket. Amazon CloudWatch is a service that provides
monitoring and observability for AWS resources and applications. It can be used to collect
and analyze metrics, logs, events, and alarms. It is not a service or feature that can be
used to restrict access to an S3 bucket. AWS CloudTrail is a service that provides
governance, compliance, and audit for AWS accounts and resources. It can be used to
track and record the API calls and user activity in AWS. It is not a service or feature that
can be u

</details>

---

### Question 350
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q350`

Which advantage of cloud computing allows users to scale resources up and down based
on the amount of load that an application supports?

- **A)** Go global in minutes
- **B)** Stop guessing capacity
- **C)** Benefit from massive economies of scale
- **D)** Trade fixed expense for variable expense

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The ability to scale resources up and down based on application load is tied to the
advantage of "Stop guessing capacity." This feature allows users to scale resources
automatically to match the demand, thereby avoiding over-provisioning or underprovisioning of resources. "Go global in minutes," "Benefit from massive economies of
scale," and "Trade fixed expense for variable expense" are other advantages of cloud
computing, but they do not specifically address scaling resources up and down based on
load.

</details>

---

### Question 351
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q351`

A company is planning to migrate to the AWS Cloud. The company is conducting
organizational transformation and wants to become more responsive to customer inquiries
and feedback.
Which tasks should the company perform to meet these requirements, according to the
AWS Cloud Adoption Framework (AWS CAF)? (Select TWO.)

- **A)** Realign teams to focus on products and value streams.
- **B)** Create new value propositions with new products and services.
- **C)** Use agile methods to rapidly iterate and evolve.
- **D)** Use a new data and analytics platform to create actionable insights.
- **E)** Migrate and modernize legacy infrastructure.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `E`

Realigning teams to focus on products and value streams, and using agile methods to
rapidly iterate and evolve are tasks that the company should perform to meet the
requirements of becoming more responsive to customer inquiries and feedback, according
to the AWS Cloud Adoption Framework (AWS CAF). AWS CAF organizes guidance into
six areas of focus, called perspectives: business, people, governance, platform, security,
and operations. Each perspective is divided into capabilities, which describe the skills and
processes to execute the transition effectively. The people perspective helps you prepare
your organization for cloud adoption, and includes capabilities such as organizational
change management, staff skills and readiness, and organizational alignment. The
business perspective helps you align IT strategy with business strategy, and includes
capabilities such as business case development, value proposition, and product
ownership. Creating new value propositions with new products a

</details>

---

### Question 352
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q352`

A company wants to host an application on Amazon EC2 instances. The company needs
to bring its own license for its operating systems. To meet governance and compliance
requirements, the application needs software licensing at the physical server level.
Which EC2 instance purchasing option will meet these requirements?

- **A)** On-Demand Instances
- **B)** Reserved Instances
- **C)** Dedicated Hosts
- **D)** Spot Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 353
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q353`

Which of the following is an advantage that users experience when they move on-premises
workloads to the AWS Cloud?

- **A)** Elimination of expenses for running and maintaining data centers
- **B)** Price discounts that are identical to discounts from hardware providers
- **C)** Distribution of all operational controls to AWS
- **D)** Elimination of operational expenses

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The advantage that users experience when they move on-premises workloads to the AWS
Cloud is: elimination of expenses for running and maintaining data centers. By moving onpremises workloads to the AWS Cloud, users can reduce or eliminate the costs associated
with owning and operating physical servers, storage, network equipment, and facilities.
These costs include hardware purchase, maintenance, repair, power, cooling, security,
and staff. Users can also benefit from the pay-as-you-go pricing model of AWS, which
allows them to pay only for the resources they use, and scale up or down as needed.

</details>

---

### Question 354
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q354`

A company is designing an identity access management solution for an application. The
company wants users to be able to use their social media, email, or online shopping
accounts to access the application.
Which AWS service provides this functionality?

- **A)** AWS IAM Identity Center (AWS Single Sign-On)
- **B)** AWS Config
- **C)** Amazon Cognito
- **D)** AWS Identity and Access Management (IAM)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The correct answer is C because Amazon Cognito provides identity federation and user
authentication for web and mobile applications. Amazon Cognito allows users to sign in
with their social media, email, or online shopping accounts. The other options are incorrect
because they do not provide identity federation or user authentication. AWS IAM Identity
Center (AWS Single Sign-On) is a service that enables users to access multiple AWS
accounts and applications with a single sign-on experience. AWS Config is a service that
enables users to assess, audit, and evaluate the configurations of their AWS resources.
AWS Identity and Access Management (IAM) is a service that enables users to manage
access to AWS resources using users, groups, roles, and policies. Reference: Amazon
Cognito FAQs

</details>

---

### Question 355
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q355`

To assist companies with Payment Card Industry Data Security Standard (PCI DSS)
compliance in the cloud. AWS provides:

- **A)** physical inspections of data centers by appointment.
- **B)** required PCI compliance certifications for any application running on AWS.
- **C)** an AWS Attestation of Compliance (AOC) report for specific AWS services.
- **D)** professional PCI compliance services.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS provides an Attestation of Compliance (AOC) report for specific AWS services to
assist companies in achieving Payment Card Industry Data Security Standard (PCI DSS)
compliance in the cloud. This report demonstrates that AWS services meet the necessary
PCI DSS requirements. AWS does not offer physical inspections of data centers by
appointment, nor does it provide certifications for any application running on AWS.
Additionally, AWS does not provide professional PCI compliance services; companies
must manage their PCI compliance in their environment.

</details>

---

### Question 356
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q356`

A company is learning about its responsibilities that are related to the management of
Amazon EC2 instances.
Which tasks for EC2 instances are the company's responsibility, according to the AWS
shared responsibility model? (Select TWO.)

- **A)** Install and patch the machine hypervisor.
- **B)** Patch the guest operating system.
- **C)** Encrypt data at rest on associated storage.
- **D)** Install the physical hardware and cabling.
- **E)** Provide physical security for the EC2 instances.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `BC`

Under the AWS Shared Responsibility Model, AWS manages the security of the cloud,
while customers manage security in the cloud. For EC2 instances, it is the customer's
responsibility to manage the guest operating system, including patching and encrypting

data stored on attached storage volumes. AWS is responsible for the underlying
infrastructure, including physical security and hypervisor maintenance.

</details>

---

### Question 357
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q357`

Which AWS service can a company use to build conversational chatbots for customer
service?

- **A)** Amazon Lex
- **B)** Amazon Polly
- **C)** Amazon Comprehend
- **D)** AWS Amplify

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 358
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q358`

Which AWS database service provides in-memory data storage?

- **A)** Amazon DynamoDB
- **B)** Amazon ElastiCache
- **C)** Amazon RDS
- **D)** Amazon Timestream

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

The correct answer is B because Amazon ElastiCache is a service that provides inmemory data storage. Amazon ElastiCache is a fully managed, scalable, and highperformance service that supports two popular open-source in-memory engines: Redis and
Memcached. Amazon ElastiCache allows users to store and retrieve data from fast, lowlatency, and high-throughput in-memory systems. Users can use Amazon ElastiCache to
improve the performance of their applications by caching frequently accessed data,
reducing database load, and enabling real-time data processing. The other options are
incorrect because they are not services that provide in-memory data storage. Amazon
DynamoDB is a service that provides key-value and document data storage. Amazon RDS
is a service that provides relational data storage. Amazon Timestream is a service that
provides time series data storage. Reference: Amazon ElastiCache FAQs

</details>

---

### Question 359
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q359`

A company has developed a distributed application that recovers gracefully from
interruptions. The application periodically processes large volumes of data by using
multiple Amazon EC2 instances. The application is sometimes idle for months.
Which EC2 instance purchasing option is MOST cost-effective for this use case?

- **A)** Reserved Instances
- **B)** Spot Instances
- **C)** Dedicated Instances
- **D)** On-Demand Instances

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Spot Instances are instances that use spare EC2 capacity that is available for up to 90%
off the On-Demand price. Because Spot Instances can be interrupted by EC2 with two
minutes of notification when EC2 needs the capacity back, you can use them for
applications that have flexible start and end times, or that can withstand interruptions5.
This option is most cost-effective for the use case described in the question. Reserved
Instances are instances that you purchase for a one-year or three-year term, and pay a
lower hourly rate compared to On-Demand Instances. This option is suitable for
applications that have steady state or predictable usage. Dedicated Instances are
instances that run on hardware that's dedicated to a single customer within an Amazon
VPC. This option is suitable for applications that have stringent regulatory or compliance
requirements. On-Demand Instances are instances that you pay for by the second, with no
long-term commitments or upfront payments

</details>

---

### Question 360
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q360`

Which AWS tool or feature acts as a VPC firewall at the subnet level?

- **A)** Security group
- **B)** Network ACL
- **C)** Traffic Mirroring
- **D)** Internet gateway

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Network ACLs (NACLs) are subnet-level firewalls in AWS, controlling inbound and
outbound traffic for VPC subnets. They provide an additional layer of security by allowing
or denying traffic based on IP protocol, source and destination IP, and port. Security
groups operate at the instance level, while Traffic Mirroring and Internet Gateways do not
function as firewalls at the subnet level.

</details>

---

### Question 361
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q361`

A company wants to migrate its PostgreSQL database to AWS. The company does not
use the database frequently.
Which AWS service or resource will meet these requirements with the LEAST
management overhead?

- **A)** PostgreSQL on Amazon EC2
- **B)** Amazon RDS for PostgreSQL
- **C)** Amazon Aurora PostgreSQL-Compatible Edition
- **D)** Amazon Aurora Serverless

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Amazon Aurora Serverless is an on-demand, auto-scaling configuration for Amazon
Aurora PostgreSQL-Compatible Edition. It is a fully managed service that automatically
scales up and down based on the application's actual needs. Amazon Aurora Serverless is
suitable for applications that have infrequent, intermittent, or unpredictable database

workloads, and that do not require the full power and range of options provided by
provisioned Aurora clusters. Amazon Aurora Serverless eliminates the need to provision
and manage database instances, and reduces the management overhead associated with
database administration tasks such as scaling, patching, backup, and recovery. Reference:
Amazon Aurora Serverless, Choosing between Aurora Serverless and provisioned Aurora
DB clusters, [AWS Cloud Practitioner Essentials: Module 4 - Databases in the Cloud]

</details>

---

### Question 362
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q362`

Which of the following is an advantage that the AWS Cloud provides to users?

- **A)** Users eliminate the need to guess about infrastructure capacity requirements.
- **B)** Users decrease their variable costs by maintaining sole ownership of IT hardware.
- **C)** Users maintain control of underlying IT infrastructure hardware.
- **D)** Users maintain control of operating systems for managed services.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

One of the primary advantages of the AWS Cloud is the ability to provision resources on
demand. Users no longer need to over-provision or guess the capacity needed for
infrastructure, which helps optimize costs and improve agility. AWS handles infrastructure
scaling dynamically based on the actual usage. Options B, C, and D are incorrect as users
do not maintain sole ownership of IT hardware or control of underlying infrastructure, and
while they do maintain some control over the operating system in some cases, it is not an
advantage specific to the cloud.

</details>

---

### Question 363
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q363`

A company has multiple AWS accounts. The company needs to receive a consolidated bill
from AWS and must centrally manage security and compliance. Which AWS service or
feature should the company use to meet these requirements?

- **A)** AWS Cost and Usage Report
- **B)** AWS Organizations
- **C)** AWS Config
- **D)** AWS Security Hub

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Organizations enables consolidated billing across multiple AWS accounts and allows
for centralized management of security and compliance policies. It provides account
grouping and centralized payment management, making it the optimal choice for a
company requiring consolidated billing and centralized governance. AWS Cost and Usage
Report only provides billing information, and AWS Config and Security Hub offer
monitoring and security insights but do not handle billing consolidation.

</details>

---

### Question 364
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q364`

A company plans to use an Amazon Snowball Edge device la transfer files to the AWS
Cloud.
Which activities related in a Snowball device are available to the company at no cost?

- **A)** Use of the Snowball Edge appliance for a 10-day period
- **B)** The transfer of data out of Amazon S3 and 10 the Snowball Edge appliance
- **C)** The transfer of data from the Snowball Edge appliance into Amazon S3
- **D)** Daily use of the Snowball Edge appliance after 10 days

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

Understanding Amazon Snowball Edge: Amazon Snowball Edge is a data migration and
edge computing device that helps in transferring large amounts of data to and from AWS.
No-Cost Activities:
Transfer into S3: AWS does not charge for transferring data from the Snowball Edge
device into Amazon S3. This is part of the service to facilitate easy data migration into the
AWS cloud.
Other Costs: The use of the Snowball Edge appliance for up to 10 days is included in the
service fee. However, any usage beyond the 10-day period may incur additional costs.
How to Utilize Snowball Edge:
Order the Device: Use the AWS Management Console to order a Snowball Edge device.
Load Data: Transfer your data onto the Snowball Edge appliance.
Ship Back: Ship the device back to AWS, where the data will be uploaded to Amazon S3 at
no additional cost.
Amazon Snowball Edge Pricing
Amazon Snowball Edge Documentation

</details>

---

### Question 365
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q365`

An ecommerce company wants to design a highly available application that will be hosted
on multiple Amazon EC2 instances.
How should the company deploy the EC2 instances to meet these requirements?

- **A)** Across multiple edge locations
- **B)** Across multiple VPCs
- **C)** Across multiple Availability Zones
- **D)** Across multiple AWS accounts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The company should deploy the EC2 instances across multiple Availability Zones to design
a highly available application. Availability Zones are isolated locations within an AWS
Region that are engineered to be fault-tolerant and operate independently of each other.
By deploying the EC2 instances across multiple Availability Zones, the company can
ensure that their application can withstand the failure of an entire Availability Zone and
continue to operate with minimal disruption. Deploying the EC2 instances across multiple
edge locations, VPCs, or AWS accounts will not provide the same level of availability and
fault tolerance as Availability Zones. Edge locations are part of the Amazon CloudFront
service, which is a content delivery network (CDN) that caches and serves web content to
users. VPCs are virtual networks that isolate the AWS resources within an AWS Region.
AWS accounts are the primary units of ownership and access control for AWS
resources12

</details>

---

### Question 366
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q366`

Which AWS service can be used at no additional cost?

- **A)** Amazon SageMaker
- **B)** AWS Config
- **C)** AWS Organizations
- **D)** Amazon CloudWatch

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Organizationsis a no-cost service that helps you centrally manage and govern your
environment as you grow and scale your AWS resources. With AWS Organizations, you
can create new AWS accounts, invite existing accounts to join your organization, and apply
policies to groups of accounts for governance. While some features within AWS services
incur additional costs, using AWS Organizations itself does not add any direct costs.
A . Amazon SageMaker: Incorrect, as it is a fully managed service for building, training,
and deploying machine learning models, and it is not free.
B . AWS Config: Incorrect, as while it offers some free-tier usage, it generally incurs
charges for recording and evaluating configuration changes.
D . Amazon CloudWatch: Incorrect, as certain CloudWatch metrics, custom metrics, and
alarms have associated costs beyond the free tier.
AWS Cloud Reference:
AWS Organizations

</details>

---

### Question 367
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q367`

What is the LEAST expensive AWS Support plan that provides the full set of AWS Trusted
Advisor best practice checks for cost optimization?

- **A)** AWS Enterprise Support
- **B)** AWS Business Support
- **C)** AWS Developer Support
- **D)** AWS Basic Support

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS Business Support is the least expensive AWS Support plan that provides the full set
of AWS Trusted Advisor best practice checks for cost optimization. AWS Trusted Advisor
is a service that provides best practices and recommendations for cost optimization,
performance, security, and fault tolerance. AWS Business Support also provides other
benefits, such as 24/7 technical support, unlimited cases, and faster response times. AWS
Enterprise Support is the most expensive AWS Support plan that provides the same
benefits as AWS Business Support, plus additional benefits, such as a technical account
manager and enterprise concierge support. AWS Developer Support and AWS Basic
Support are cheaper AWS Support plans that provide only a limited set of AWS Trusted
Advisor best practice checks for cost optimization .

</details>

---

### Question 368
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q368`

A developer who has no AWS Cloud experience wants to use AWS technology to build a
web application.
Which AWS service should the developer use to start building the application?

- **A)** Amazon SageMaker
- **B)** AWS Lambda
- **C)** Amazon Lightsail
- **D)** Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon Lightsail is an easy-to-use cloud platform that offers everything you need to build
an application or website, plus a cost-effective, monthly plan1. It is designed for developers
who have little or no prior cloud experience and want to launch and manage applications
on AWS with minimal complexity2. Amazon SageMaker is a service for building, training,
and deploying machine learning models3. AWS Lambda is a service that lets you run code
without provisioning or managing servers4. Amazon Elastic Container Service (Amazon
ECS) is a fully managed container orchestration service.

</details>

---

### Question 369
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q369`

A company is planning a migration to the AWS Cloud and wants to examine the costs that
are associated with different workloads.
Which AWS tool will meet these requirements?

- **A)** AWS Budgets
- **B)** AWS Cost Explorer
- **C)** AWS Pricing Calculator
- **D)** AWS Cost and Usage Report

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

The AWS tool that will meet the requirements of the company that is planning a migration
to the AWS Cloud and wants to examine the costs that are associated with different
workloads is AWS Pricing Calculator. AWS Pricing Calculator is a tool that helps

customers estimate the cost of using AWS services based on their requirements and
preferences. The company can use AWS Pricing Calculator to compare the costs of
different AWS services and configurations, such as Amazon EC2, Amazon S3, Amazon
RDS, and more. AWS Pricing Calculator also provides detailed breakdowns of the cost
components, such as compute, storage, network, and data transfer. AWS Pricing
Calculator helps customers plan and optimize their cloud budget and migration strategy.
AWS Budgets, AWS Cost Explorer, and AWS Cost and Usage Report are not the best
tools to use for this purpose. AWS Budgets is a tool that helps customers monitor and
manage their AWS spending and usage against predefined budget limits and thresholds.
AW

</details>

---

### Question 370
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q370`

Which AWS service or tool should a company use to forecast AWS spending?

- **A)** Amazon DevPay
- **B)** AWS Organizations
- **C)** AWS Trusted Advisor
- **D)** Cost Explorer

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

Cost Explorer is an AWS service or tool that can be used to forecast AWS spending. It
allows users to analyze their AWS costs and usage using interactive graphs and tables. It
also provides features such as filtering, grouping, and forecasting to help users plan their
future spending. Amazon DevPay is an AWS service that allows developers to sell
applications that are built on AWS services. It handles the billing and metering for the
customers of the applications and collects payments from them. It is not a tool for
forecasting AWS spending. AWS Organizations is an AWS service that allows users to
centrally manage and govern their AWS accounts. It provides features such as creating
groups of accounts, applying policies, and automating account creation. It is not a tool for
forecasting AWS spending. AWS Trusted Advisor is an AWS service that provides best
practices and recommendations to optimize the performance, security, and cost of AWS
resources. It can help users ident

</details>

---

### Question 371
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q371`

Which task is the responsibility of the customer, according to the AWS shared
responsibility model?

- **A)** Patch the Amazon DynamoDB operating system.  B. Secure Amazon CloudFront edge locations by allowing physical access according to the principle of least privilege.
- **C)** Protect the hardware that runs AWS services.
- **D)** Use AWS Identity and Access Management (1AM) according to the principle of least privilege.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

According to theAWS Shared Responsibility Model, AWS is responsible for the security
"of" the cloud (such as protecting the infrastructure, including hardware, software,
networking, and facilities that run AWS Cloud services). In contrast, customers are
responsible for security "in" the cloud. This includes configuring and using AWS services
securely.
D . Use AWS Identity and Access Management (IAM) according to the principle of least
privilegeis a customer's responsibility. Customers must manage their credentials, control
access to resources, and ensure that IAM policies follow the principle of least privilege,
which means granting only the permissions necessary to perform a task.
Why other options are not suitable:
A . Patch the Amazon DynamoDB operating system: AWS is responsible for managing and
patching the infrastructure for managed services like DynamoDB.
B . Secure Amazon CloudFront edge locations by allowing physical access according to
the principle of least privilege: AWS ha

</details>

---

### Question 372
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q372`

A company provides a software as a service (SaaS) application. The company has a new
customer that is based in a different country.
The new customer's data needs to be hosted in that country.
Which AWS service or infrastructure component should the company use to meet this
requirement?

- **A)** AWS Shield
- **B)** Amazon S3 Object Lock
- **C)** AWS Regions
- **D)** Placement groups

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

AWS Regions are geographic areas around the world where AWS has clusters of data
centers. Each AWS Region consists of multiple, isolated, and physically separate AZ's
within a geographic area. By hosting the customer's data in a specific AWS Region, the
company can meet the requirement of hosting the data in the customer's country. AWS
Shield is a service that provides always-on detection and automatic inline mitigations that

minimize application downtime and latency, so there is no need to engage AWS Support to
benefit from DDoS protection. Amazon S3 Object Lock is a feature that allows you to store
objects using a write-once-read-many (WORM) model. You can use it to prevent an object
from being deleted or overwritten for a fixed amount of time or indefinitely. Placement
groups are logical grouping of instances within a single Availability Zone. Placement
groups enable applications to participate in a low-latency, 10 Gbps network. None of these
services or infrastructu

</details>

---

### Question 373
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q373`

A company plans to migrate to the AWS Cloud. The company wants to use the AWS Cloud
Adoption Framework (AWS CAF) to define and track business outcomes as part of its
cloud transformation journey.
Which AWS CAF governance perspective capability will meet these requirements?

- **A)** Benefits management
- **B)** Risk management
- **C)** Application portfolio management
- **D)** Cloud financial management

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

The correct answer is A. Benefits management.
Benefits management is the AWS CAF governance perspective capability that helps you
define and track business outcomes as part of your cloud transformation journey.Benefits
management helps you align your cloud initiatives with your business objectives, measure
the value and impact of your cloud investments, and communicate the benefits of cloud
adoption to your stakeholders12.
Risk management is the AWS CAF governance perspective capability that helps you
identify and mitigate the potential risks associated with cloud adoption, such as security,
compliance, legal, and operational risks12.
Application portfolio management is the AWS CAF governance perspective capability that
helps you assess and optimize your existing application portfolio for cloud migration or
modernization.Application portfolio management helps you categorize your applications
based on their business value and technical fit, prioritize them for cloud adoption, and
select

</details>

---

### Question 374
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q374`

According to the AWS shared responsibility model, which of the following are AWS
responsibilities? (Select TWO.)

- **A)** Network infrastructure and virtualization of infrastructure
- **B)** Security of application data
- **C)** Guest operating systems
- **D)** Physical security of hardware
- **E)** Credentials and policies

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `AD`

The correct answers are A and D because network infrastructure and virtualization of
infrastructure and physical security of hardware are AWS responsibilities according to the
AWS shared responsibility model. The AWS shared responsibility model is a framework
that defines the division of responsibilities between AWS and the customer for security and
compliance. AWS is responsible for the security of the cloud, which includes the global
infrastructure, such as the regions, availability zones, and edge locations; the hardware,
software, networking, and facilities that run the AWS services; and the virtualization layer
that separates the customer instances and storage. The customer is responsible for the
security in the cloud, which includes the customer data, the guest operating systems, the
applications, the identity and access management, the firewall configuration, and the
encryption. The other options are incorrect because they are not AWS responsibilities
according to the AWS shared

</details>

---

### Question 375
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q375`

Which AWS service is a cloud security posture management (CSPM) service that
aggregates alerts from various AWS services and partner products in a standardized
format?

- **A)** AWS Security Hub
- **B)** AWS Trusted Advisor
- **C)** Amazon EventBndge
- **D)** Amazon GuardDuty

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Security Hub is a cloud security posture management (CSPM) service that performs
security best practice checks, aggregates alerts, and enables automated remediation.
Security Hub collects findings from the security services enabled across your AWS
accounts, such as intrusion detection findings from Amazon GuardDuty, vulnerability scans
from Amazon Inspector, and sensitive data identification findings from Amazon Macie.
Security Hub also collects findings from partner security products using a standardized
AWS Security Finding Format, eliminating the need for time-consuming data parsing and
normalization efforts. Customers can designate an administrator account that can access

all findings across their accounts. Reference: AWS Security Hub Overview, AWS Security
Hub FAQs

</details>

---

### Question 376
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q376`

A manufacturing company has a critical application that runs at a remote site that has a
slow internet connection. The company wants to migrate the workload to AWS. The
application is sensitive to latency and interruptions in connectivity. The company wants a
solution that can host this application with minimum latency.
Which AWS service or feature should the company use to meet these requirements?

- **A)** Availability Zones
- **B)** AWS Local Zones
- **C)** AWS Wavelength
- **D)** AWS Outposts

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Outposts is a service that offers fully managed and configurable compute and
storage racks built with AWS-designed hardware that allow you to run your workloads on
premises and seamlessly connect to AWS services in the cloud. AWS Outposts is ideal for
workloads that require low latency, local data processing, or local data storage. With AWS
Outposts, you can use the same AWS APIs, tools, and infrastructure across on premises
and the cloud to deliver a truly consistent hybrid experience5. Availability Zones are
isolated locations within each AWS Region that are engineered to be fault-tolerant and
provide high availability. AWS Local Zones are extensions of AWS Regions that are placed
closer to large population, industry, and IT centers where no AWS Region exists today.
AWS Wavelength is a service that enables developers to build applications that deliver
ultra-low latency to mobile devices and users by deploying AWS compute and storage at
the edge of the 5G network. None of these se

</details>

---

### Question 377
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q377`

A company notices suspicious network activity against an application that is running on a
fleet of Amazon EC2 instances. The suspicious activity is coming from a single IP address.
Which AWS service should the company use to block access from this IP address?

A. AWS Shield

- **B)** AWS Config
- **C)** Amazon GuardDuty
- **D)** AWS WAF

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS WAF Overview:
AWS Web Application Firewall (WAF) allows users to create rules to block or allow traffic
based on IP addresses, request patterns, and other conditions.
It is ideal for blocking traffic from a specific IP address.
Why AWS WAF Meets the Requirement:
The company can create a WAF rule to block traffic from the malicious IP address.
WAF integrates with services like Amazon CloudFront, Application Load Balancer, and API
Gateway.
Why Other Options Are Incorrect:
A . AWS Shield:Protects against DDoS attacks but does not allow custom IP blocking.
B . AWS Config:Monitors resource configurations but does not block IPs.
C . Amazon GuardDuty:Detects threats but does not block traffic directly.
Reference:
AWS WAF Documentation

</details>

---

### Question 378
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q378`

A company is moving to the AWS Cloud to reduce operational overhead for its application
infrastructure.
Which IT operation will the company still be responsible for after the migration to AWS?

- **A)** Security patching of AWS Elastic Beanstalk
- **B)** Backups of data that is stored in Amazon Aurora
- **C)** Termination of Amazon EC2 instances that are managed by AWS Auto Scaling
- **D)** Configuration of IAM access controls

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Elastic Beanstalk, Amazon Aurora, and AWS Auto Scaling are managed services
that reduce the operational overhead for the customers. AWS is responsible for security
patching, backups, and termination of these services. However, the customers are still
responsible for configuring IAM access controls to manage the permissions and policies for
their AWS resources. This is part of the AWS shared responsibility model, which defines
the security and compliance responsibilities of AWS and the customers. You can learn
more about the AWS shared responsibility model from this whitepaper or this digital
course.

</details>

---

### Question 379
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q379`

A company plans to perform a one-time migration of a large dataset with millions of files
from its on- premises data center to the AWS Cloud.

Which AWS service should the company use for the migration?

- **A)** AWS Database Migration Service (AWS DMS)
- **B)** AWS DataSync
- **C)** AWS Migration Hub
- **D)** AWS Application Migration Service

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS DataSync is designed for large-scale data transfers, especially involving large
datasets with millions of files from on-premises to AWS. It provides fast and efficient
transfer capabilities, and supports a one-time migration. AWS DMS is specific to
databases, while Migration Hub is for tracking migrations, and Application Migration
Service is for continuous replication rather than one-time file migrations.

</details>

---

### Question 380
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q380`

Which tasks are responsibilities of AWS, according to the AWS shared responsibility
model?(Select TWO.)

- **A)** Encrypt client-side data and authenticate data integrity.
- **B)** Manage customer data.
- **C)** Perform identity and access management.
- **D)** Provide physical security for Availability Zones.
- **E)** Patch the operating system of Amazon S3.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `DE`

AWS is responsible for the physical security of the facilities and infrastructure that make up
AWS Regions and Availability Zones. AWS also operates the infrastructure, operating
system, and service platform for abstracted managed services such as Amazon S3.
Consequently, AWS is responsible for patching the underlying operating system and
platform that run S3. Options D and E are therefore correct. Customers are responsible for
managing and protecting their data, including deciding whether client-side encryption is
needed and implementing appropriate encryption and integrity controls. Customers also
use AWS Identity and Access Management tools to define their users, roles, policies, and
permissions. Although AWS operates the IAM service itself, the customer is responsible for
configuring identities and access to the customer's resources. The phrase "manage
customer data" is also a customer responsibility because AWS does not determine the
customer's data classification, retention, perm

</details>

---

### Question 381
> **Domain:** `Domain 4: Billing, Pricing, and Support (12%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q381`

Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is
stopped or terminated?

- **A)** Amazon Elastic Block Store (Amazon EBS)  B. Amazon EC2 instance store
- **C)** Amazon Elastic File System (Amazon EFS)
- **D)** Amazon S3

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

Amazon EC2 instance store provides temporary block-level storage for your EC2 instance.
This storage is located on disks that are physically attached to the host computer. Instance
store is ideal for temporary storage of information that changes frequently, such as buffers,
caches, scratch data, and other temporary content. It can also be used to store temporary
data that you replicate across a fleet of instances, such as a load-balanced pool of web
servers. An instance store consists of one or more instance store volumes exposed as
block devices. The size of an instance store as well as the number of devices available
varies by instance type and instance size. The virtual devices for instance store volumes
are ephemeral[0-23]. Instance types that support one instance store volume have
ephemeral0. Instance types that support two or more instance store volumes have
ephemeral0, ephemeral1, and so on. Instance store pricing Instance store volumes are
included as part of the instance's usa

</details>

---

### Question 382
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q382`

A company needs a fully managed file server that natively supports Microsoft workloads
and file systems The file server must also support the SMB protocol.
Which AWS service should the company use to meet these requirements?

- **A)** Amazon Elastic File System (Amazon EFS)
- **B)** Amazon FSx for Lustre
- **C)** Amazon FSx for Windows File Server
- **D)** Amazon Elastic Block Store (Amazon EBS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon FSx for Windows File Server is a fully managed file server that supports Microsoft
workloads and file systems, including the SMB protocol. It provides features such as user
quotas, end-user file restore, and Microsoft Active Directory integration. Amazon EFS is a
fully managed file system that supports the NFS protocol, not SMB. Amazon FSx for Lustre

is a fully managed file system that supports high-performance computing workloads, not
Microsoft workloads. Amazon EBS is a block storage service that does not provide a file
system or SMB support. Reference: Amazon FSx for Windows File Server, Amazon FSx
for Lustre, Amazon EFS, Amazon EBS

</details>

---

### Question 383
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q383`

Which AWS service could an administrator use to provide desktop environments for
several employees?

- **A)** AWS Organizations
- **B)** AWS Fargate
- **C)** AWS WAF
- **D)** AWS Workspaces

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

AWS Workspaces is a service that provides fully managed, secure, and reliable virtual
desktops for your employees. You can access your personal Windows environment on
various devices, such as Android, iOS, Fire, Mac, PC, Chromebook, and Linux. You can
choose from different bundles of CPU, memory, storage, and software options to suit your
needs. You can also integrate AWS Workspaces with your existing Active Directory, VPN,
and security policies. AWS Workspaces helps you reduce the cost and complexity of
managing your desktop infrastructure, while enhancing the productivity and security of your
remote workers456. Reference: 4: Amazon WorkSpaces Client Download, 5: VDI
Desktops - Amazon WorkSpaces Family - AWS, 6: Amazon WorkSpaces

</details>

---

### Question 384
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q384`

A company stores data in an Amazon S3 bucket.
Which task is the responsibility of AWS?

- **A)** Configure an S3 Lifecycle policy.
- **B)** Activate S3 Versioning.
- **C)** Configure S3 bucket policies.
- **D)** Protect the infrastructure that supports S3 storage.

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `D`

According to theAWS Shared Responsibility Model, AWS is responsible for protecting the
infrastructure that runs all of the services offered in the AWS Cloud, including Amazon S3.
This infrastructure includes hardware, software, networking, and facilities that run AWS
services.
A . Configure an S3 Lifecycle policy: Incorrect, as configuring S3 Lifecycle policies to
manage object lifecycle (e.g., transitioning objects to different storage classes or deleting
them after a certain period) is the customer's responsibility.
B . Activate S3 Versioning: Incorrect, as enabling S3 Versioning is a customer
responsibility for managing data protection.

C . Configure S3 bucket policies: Incorrect, as setting and managing S3 bucket policies to
control access is the customer's responsibility.
AWS Cloud Reference:
AWS Shared Responsibility Model
Amazon S3

</details>

---

### Question 385
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q385`

Which AWS service offers object storage?

- **A)** Amazon RDS
- **B)** Amazon Elastic File System (Amazon EFS)
- **C)** Amazon S3
- **D)** Amazon DynamoDB

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Amazon S3 is the AWS service that offers object storage. Object storage is a technology
that stores and manages data in an unstructured format called objects. Each object
consists of the data, metadata, and a unique identifier. Object storage is ideal for storing
large amounts of unstructured data, such as photos, videos, email, web pages, sensor
data, and audio files1. Amazon S3 provides industry-leading scalability, data availability,
security, and performance for object storage2.
Amazon RDS is the AWS service that offers relational database storage. Relational
database storage is a technology that stores and manages data in a structured format
called tables. Each table consists of rows and columns that define the attributes and
values of the dat a. Relational database storage is ideal for storing structured or semistructured data, such as customer records, inventory, transactions, and analytics3.
Amazon Elastic File System (Amazon EFS) is the AWS service that offers file storage. Fi

</details>

---

### Question 386
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q386`

A company needs to host a highly available application in the AWS Cloud. The application
runs infrequently for short periods of time.

Which AWS service will meet these requirements with the LEAST amount of operational
overhead?

- **A)** Amazon EC2
- **B)** AWS Fargate
- **C)** AWS Lambda
- **D)** Amazon Aurora

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 387
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q387`

Which AWS service or resource provides answers to the most frequently asked securityrelated questions that AWS receives from its users'?

- **A)** AWS Artifact
- **B)** Amazon Connect
- **C)** AWS Chatbot
- **D)** AWS Knowledge Center

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `A`

AWS Artifact is your go-to, central resource for compliance-related information that matters
to you. It provides on-demand access to AWS's security and compliance reports and select
online agreements. Reports available in AWS Artifact include our Service Organization

Control (SOC) reports, Payment Card Industry (PCI) attestation of compliance, and
certifications from accreditation bodies across geographies and compliance verticals that
validate the implementation and operating effectiveness of AWS security controls.
Agreements available in AWS Artifact include the Business Associate Addendum (BAA)
and the Nondisclosure Agreement (NDA). AWS Artifact helps you answer the most
frequently asked security and compliance questions that AWS receives from its users.
Reference: Compliance FAQ, Compliance Solutions Guide

</details>

---

### Question 388
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q388`

A company is planning to migrate applications to the AWS Cloud. During a system audit,
the company finds that its content management system (CMS) application is incompatible
with cloud environments.
Which migration strategies will help the company to migrate the CMS application with the
LEAST effort? (Select TWO.)

- **A)** Retire
- **B)** Rehost
- **C)** Repurchase
- **D)** Replatform
- **E)** Refactor

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B, C`

Rehosting ("lift and shift") is a migration strategy where applications are moved to the
cloud with minimal changes, making it the least effort-intensive method for applications
incompatible with the cloud. Repurchasing involves moving to a different product, often a
SaaS solution, which can also minimize migration effort by avoiding the need for
application-level changes. Retiring, replatforming, and refactoring require significant effort
either in terms of analyzing and shutting down the application, making changes to the
underlying platform, or redesigning the application architecture, respectively.
Reference:
AWS Migration Strategies

</details>

---

### Question 389
> **Domain:** `Domain 3: Cloud Technology and Services (34%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q389`

A company wants a unified tool to provide a consistent method to interact with AWS
services.
Which AWS service or tool will meet this requirement?

- **A)** AWS VPN
- **B)** Amazon Connect
- **C)** AWS CLI
- **D)** Amazon Elastic Container Service (Amazon ECS)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

Verified authentic candidate practice response from the November 2026 revision pool.

</details>

---

### Question 390
> **Domain:** `Domain 1: Cloud Concepts (24%)` | **Priority:** `🔶 Tier 3: Specialized Disambiguation` | **ID:** `ACTUAL-2026-Q390`

A company wants its AWS usage to be more sustainable. The company wants to track,
measure, review, and forecast polluting emissions that result from its AWS applications.
Which AWS service or tool can the company use to meet these requirements?

- **A)** AWS Health Dashboard
- **B)** AWS customer carbon footprint tool
- **C)** AWS Support Center
- **D)** Amazon QuickSight

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B`

AWS customer carbon footprint tool is a tool that helps customers measure and manage
their carbon emissions from their AWS usage. It provides data on the carbon intensity,
energy consumption, and estimated emissions of AWS services across regions and time
periods. It also enables customers to review and forecast their emissions, and compare
them with industry benchmarks. AWS Health Dashboard is a service that provides
personalized information about the health and performance of AWS services and
resources. AWS Support Center is a service that provides access to AWS support
resources, such as cases, forums, and documentation. Amazon QuickSight is a service
that provides business intelligence and analytics for AWS data sources.

</details>

---

### Question 391
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q391`

Which AWS service or feature provides log information of the inbound and outbound traffic
on network interfaces in a VPC?

- **A)** Amazon CloudWatch Logs
- **B)** AWS CloudTrail
- **C)** VPC Flow Logs
- **D)** AWS Identity and Access Management (IAM)

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `C`

VPC Flow Logs is a feature that enables you to capture information about the IP traffic
going to and from network interfaces in your VPC. Flow log data can be published to the
following locations: Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data
Firehose. You can use VPC Flow Logs to monitor network traffic, diagnose security issues,
troubleshoot connectivity problems, and perform network forensics1. Reference:
Logging IP traffic using VPC Flow Logs - Amazon Virtual Private Cloud

</details>

---

### Question 392
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `🔷 Tier 2: Core Architecture & Services` | **ID:** `ACTUAL-2026-Q392`

Which perspective in the AWS Cloud Adoption Framework (AWS CAF) includes a
capability for well-designed data and analytics architecture?

- **A)** Security
- **B)** Governance
- **C)** Operations
- **D)** Platform

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

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

### Question 393
> **Domain:** `Domain 2: Security and Compliance (30%)` | **Priority:** `⭐ Tier 1: Guaranteed Core Exam Traps` | **ID:** `ACTUAL-2026-Q393`

In which situations should a company create an 1AM user instead of an 1AM role? (Select
TWO.)

- **A)** When an application that runs on Amazon EC2 instances requires access to other AWS services
- **B)** When the company creates AWS access credentials for individuals  C. When the company creates an application that runs on a mobile phone that makes requests to AWS
- **D)** When the company needs to add users to 1AM groups
- **E)** When users are authenticated in the corporate network and want to be able to use AWS without having to sign in a second time

<details>
<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>

**Correct Answer:** `B, D`

AnIAM useris created when the company needs to provide unique credentials (username
and password) to individuals who need access to the AWS Management Console or
programmatic access (using access keys) to AWS services.
B . When the company creates AWS access credentials for individuals: Correct, as an IAM
user is created to provide credentials for specific individuals.
D . When the company needs to add users to IAM groups: Correct, as IAM users can be
added to groups to apply permissions and policies at a group level.
A . When an application that runs on Amazon EC2 instances requires access to other
AWS services: Incorrect, as an IAM role is more appropriate for applications running on
EC2 to assume temporary credentials.
C . When the company creates an application that runs on a mobile phone that makes
requests to AWS: Incorrect, as using Cognito or a role with temporary credentials is more
suitable.
E . When users are authenticated in the corporate network and want to b

</details>

---
