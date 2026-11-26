# AWS Certified Cloud Practitioner (CLF-C02) Full-Length Mock Exam

> **Exam Format:** 65 Multiple-Choice & Multiple-Response Questions  
> **Time Limit:** 90 Minutes  
> **Passing Score:** 700 / 1000 (~72% or 47/65 Correct Answers)  
> **Domain Distribution:**
> - Domain 1: Cloud Concepts (24% ~ 16 Questions)
> - Domain 2: Security and Compliance (30% ~ 20 Questions)
> - Domain 3: Cloud Technology and Services (34% ~ 22 Questions)
> - Domain 4: Billing, Pricing, and Support (12% ~ 7 Questions)

---

## 📝 Practice Exam Simulation

### Question 1 (Domain 1: Cloud Concepts)
A retail company experiences significant traffic spikes during holiday seasons but minimal traffic during the rest of the year. Which benefit of the AWS Cloud BEST addresses this business need?

- [ ] **A)** High availability across multiple data centers
- [ ] **B)** Elasticity to scale resources up and down based on demand
- [ ] **C)** Access to a broad set of global compliance certifications
- [ ] **D)** Ability to deploy applications in multiple programming languages

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Elasticity is the ability to automatically scale computing resources up when demand increases and scale them back down when demand decreases. This is ideal for the retail company because they only pay for the resources they actually use during peak holiday traffic, rather than provisioning for peak capacity year-round. High availability (A) ensures uptime but does not address variable demand. Compliance certifications (C) address regulatory needs, not scaling. Multi-language support (D) is a development concern, not a scaling benefit.
</details>

### Question 2 (Domain 2: Security and Compliance)
Under the AWS Shared Responsibility Model, which of the following is the CUSTOMER'S responsibility?

- [ ] **A)** Physical security of AWS data centers
- [ ] **B)** Patching the hypervisor on EC2 host servers
- [ ] **C)** Configuring security groups and network access control lists
- [ ] **D)** Maintaining the global network infrastructure between AWS Regions

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Under the Shared Responsibility Model, the customer is responsible for "security IN the cloud," which includes configuring security groups and NACLs to control network access to their resources. AWS is responsible for "security OF the cloud," which includes physical data center security (A), hypervisor patching (B), and maintaining the global network infrastructure (D).
</details>

### Question 3 (Domain 3: Cloud Technology and Services)
A startup wants to run a web application on AWS without managing the underlying servers, operating system patches, or capacity planning. They want to simply upload their code and have AWS handle everything else. Which service best fits this requirement?

- [ ] **A)** AWS Elastic Beanstalk
- [ ] **B)** Amazon EC2
- [ ] **C)** Amazon Lightsail
- [ ] **D)** AWS Outposts

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) that allows developers to upload their application code and automatically handles deployment, capacity provisioning, load balancing, auto-scaling, and health monitoring. Amazon EC2 requires you to manage instances, patching, and scaling yourself. Amazon Lightsail is a simplified virtual server offering but still requires some server management. AWS Outposts extends AWS infrastructure to on-premises locations, which is unrelated to this use case.
</details>

### Question 4 (Domain 2: Security and Compliance)
A company is running a web application on Amazon EC2. Under the Shared Responsibility Model, who is responsible for patching the guest operating system on the EC2 instances?

- [ ] **A)** AWS, because they manage the underlying infrastructure
- [ ] **B)** The customer, because they control the guest operating system
- [ ] **C)** It is a shared responsibility between AWS and the customer
- [ ] **D)** The EC2 service automatically handles all OS patching

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** When using Amazon EC2, the customer is responsible for managing the guest operating system, including installing patches and updates. AWS manages the underlying host infrastructure and hypervisor, but the guest OS is the customer's responsibility. This is not a shared responsibility (C) — it falls squarely on the customer. EC2 does not automatically patch guest operating systems (D), though AWS Systems Manager Patch Manager can help automate this process.
</details>

### Question 5 (Domain 3: Cloud Technology and Services)
Which AWS service allows you to run code in response to events (such as an S3 upload or an API Gateway request) without provisioning or managing servers?

- [ ] **A)** Amazon EC2
- [ ] **B)** AWS Lambda
- [ ] **C)** Amazon ECS
- [ ] **D)** AWS Elastic Beanstalk

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources. You pay only for the compute time consumed — there is no charge when your code is not running. Amazon EC2 requires you to provision and manage virtual servers. Amazon ECS is a container orchestration service that still requires infrastructure decisions. AWS Elastic Beanstalk is a PaaS that provisions EC2 instances behind the scenes.
</details>

### Question 6 (Domain 1: Cloud Concepts)
A startup wants to launch a new application but cannot afford the upfront cost of purchasing physical servers. How does AWS Cloud computing help solve this problem?

- [ ] **A)** AWS provides free servers for startups under 50 employees
- [ ] **B)** AWS allows the company to trade upfront capital expense for variable operational expense
- [ ] **C)** AWS guarantees lower total cost of ownership than any on-premises solution
- [ ] **D)** AWS eliminates the need for any IT staff at the company

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** One of the key financial advantages of cloud computing is trading capital expense (CapEx) for operational expense (OpEx). Instead of making large upfront investments in physical hardware, the startup pays only for the resources it consumes on a pay-as-you-go basis. AWS does not provide free servers based on company size (A). While cloud can reduce TCO, AWS does not guarantee it will always be lower (C). Companies still need IT staff to manage their cloud resources (D).
</details>

### Question 7 (Domain 4: Billing, Pricing, and Support)
A company wants to reduce costs on EC2 instances that run a stable, predictable production workload 24/7. Which purchasing option would provide the GREATEST cost savings?

- [ ] **A)** On-Demand Instances
- [ ] **B)** Spot Instances
- [ ] **C)** Reserved Instances or Savings Plans with a 3-year commitment
- [ ] **D)** Dedicated Hosts with no commitment

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** For stable, predictable workloads that run 24/7, Reserved Instances or Savings Plans with a 3-year term offer the greatest discounts — up to 72% compared to On-Demand pricing. On-Demand (A) provides flexibility but no discount. Spot Instances (B) offer deep discounts but can be interrupted with little notice, making them unsuitable for production workloads requiring constant availability. Dedicated Hosts without a commitment (D) are among the most expensive options.
</details>

### Question 8 (Domain 3: Cloud Technology and Services)
A media company needs to run Docker containers at scale but does not want to manage the underlying EC2 instances or cluster infrastructure. Which combination of AWS services should they use?

- [ ] **A)** Amazon ECS with AWS Fargate
- [ ] **B)** Amazon EC2 with Docker installed manually
- [ ] **C)** AWS Lambda with container images
- [ ] **D)** Amazon Lightsail with Docker containers

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** Amazon ECS (Elastic Container Service) with AWS Fargate is the correct answer. Fargate is a serverless compute engine for containers that removes the need to manage EC2 instances — you define your container requirements and Fargate handles the rest. Installing Docker manually on EC2 requires managing infrastructure. AWS Lambda with container images has a 15-minute execution limit and 10 GB image size limit, making it unsuitable for long-running container workloads. Lightsail has limited container capabilities and is designed for simpler workloads.
</details>

### Question 9 (Domain 2: Security and Compliance)
How does the Shared Responsibility Model change when a company uses AWS Lambda instead of Amazon EC2?

- [ ] **A)** There is no change — the customer has the same responsibilities regardless of service
- [ ] **B)** AWS takes on more responsibility because Lambda is a managed service, so the customer no longer manages the OS or runtime
- [ ] **C)** The customer takes on more responsibility with Lambda because serverless requires more security configuration
- [ ] **D)** AWS is responsible for all security aspects when using Lambda, including application code security

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** With managed and serverless services like AWS Lambda, the shared responsibility model shifts more responsibility to AWS. The customer no longer manages the operating system, runtime, or server patching — AWS handles all of that. The customer remains responsible for their function code, data, and IAM permissions. The responsibilities do change by service type (A is wrong). The customer has fewer infrastructure responsibilities with Lambda (C is wrong). AWS is not responsible for the customer's application code security (D is wrong).
</details>

### Question 10 (Domain 1: Cloud Concepts)
A company needs to deploy its application to serve customers in Asia, Europe, and North America with low latency. Which advantage of AWS Cloud computing makes this possible without building physical data centers in each region?

- [ ] **A)** Economies of scale
- [ ] **B)** Increased speed and agility
- [ ] **C)** Global infrastructure with Regions and Availability Zones
- [ ] **D)** Managed database services

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS operates a global infrastructure consisting of Regions and Availability Zones around the world. This allows the company to deploy its application close to customers in Asia, Europe, and North America without building or managing physical data centers. Economies of scale (A) relates to cost advantages, not global deployment. Speed and agility (B) refers to how quickly you can provision resources, not geographic reach. Managed databases (D) is a specific service category, not a global deployment benefit.
</details>

### Question 11 (Domain 3: Cloud Technology and Services)
Which AWS service is a container orchestration platform that supports Kubernetes and allows you to run, scale, and manage containerized applications?

- [ ] **A)** Amazon ECS
- [ ] **B)** Amazon EKS
- [ ] **C)** AWS Fargate
- [ ] **D)** AWS App Runner

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EKS (Elastic Kubernetes Service) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install and maintain your own Kubernetes control plane. Amazon ECS is AWS's own container orchestration service but does not use Kubernetes. AWS Fargate is a serverless compute engine used with ECS or EKS — it is not an orchestration platform itself. AWS App Runner is a fully managed service for deploying containerized web apps but does not provide Kubernetes compatibility.
</details>

### Question 12 (Domain 2: Security and Compliance)
Which of the following is AWS's responsibility under the Shared Responsibility Model?

- [ ] **A)** Encrypting customer data stored in Amazon S3
- [ ] **B)** Managing IAM user permissions and access policies
- [ ] **C)** Decommissioning and destroying storage hardware that reaches end of life
- [ ] **D)** Configuring VPC routing tables and subnet configurations

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS is responsible for the physical infrastructure, which includes the secure decommissioning and destruction of storage hardware when it reaches end of life. AWS follows industry-standard practices (e.g., DoD 5220.22-M, NIST 800-88) to ensure data cannot be recovered from decommissioned hardware. Encrypting S3 data (A), managing IAM policies (B), and configuring VPC networking (D) are all customer responsibilities.
</details>

### Question 13 (Domain 3: Cloud Technology and Services)
A small business owner with limited cloud experience wants to quickly launch a simple WordPress website with a predictable monthly cost. Which AWS service is designed for this use case?

- [ ] **A)** Amazon EC2 with Auto Scaling
- [ ] **B)** Amazon Lightsail
- [ ] **C)** AWS Lambda
- [ ] **D)** Amazon EKS

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon Lightsail is specifically designed for simple workloads, quick deployments, and users with limited cloud experience. It offers virtual servers, storage, databases, and networking with predictable monthly pricing and a simplified management console. EC2 with Auto Scaling is more complex and does not offer a bundled, predictable monthly price. AWS Lambda is serverless and not suitable for hosting traditional WordPress sites. Amazon EKS is a Kubernetes platform far too complex for a simple WordPress site.
</details>

### Question 14 (Domain 4: Billing, Pricing, and Support)
Which Amazon EC2 pricing model provides the largest discount (up to 90% off On-Demand prices) but allows AWS to interrupt the instance with a two-minute warning?

- [ ] **A)** Reserved Instances
- [ ] **B)** On-Demand Instances
- [ ] **C)** Spot Instances
- [ ] **D)** Dedicated Hosts

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity at up to 90% off On-Demand prices. The trade-off is that AWS can reclaim (interrupt) Spot Instances with a two-minute notification when it needs the capacity back. Reserved Instances offer up to 72% savings with a 1- or 3-year commitment but are not interruptible. On-Demand Instances have no discount and no commitment. Dedicated Hosts provide a physical server dedicated to your use but are the most expensive option.
</details>

### Question 15 (Domain 1: Cloud Concepts)
Which scenario BEST demonstrates the agility benefit of cloud computing?

- [ ] **A)** A company reduces its monthly IT spending by 15%
- [ ] **B)** A development team provisions new test environments in minutes instead of weeks
- [ ] **C)** An application automatically recovers from a server failure
- [ ] **D)** A company achieves SOC 2 compliance for its workloads

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Agility in cloud computing refers to the ability to quickly provision and deploy IT resources. When a development team can spin up new test environments in minutes rather than waiting weeks for hardware procurement and setup, that demonstrates agility. Cost reduction (A) relates to cost optimization. Automatic recovery (C) demonstrates reliability and fault tolerance. Achieving compliance (D) relates to security and governance, not agility.
</details>

### Question 16 (Domain 2: Security and Compliance)
A company uses Amazon RDS for its database. Under the Shared Responsibility Model, which task is AWS responsible for?

- [ ] **A)** Creating and managing database user accounts and permissions
- [ ] **B)** Patching the underlying database engine software
- [ ] **C)** Encrypting sensitive columns within database tables
- [ ] **D)** Designing the database schema and optimizing queries

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon RDS is a managed database service, so AWS is responsible for patching the underlying database engine software during customer-specified maintenance windows. However, the customer is responsible for managing database user accounts (A), encrypting specific data columns (C), and designing schemas and queries (D). This illustrates how managed services shift more infrastructure responsibility to AWS while data and application-level responsibilities remain with the customer.
</details>

### Question 17 (Domain 3: Cloud Technology and Services)
An e-commerce company experiences traffic spikes during holiday sales events. They want their application to automatically add EC2 instances when demand increases and remove them when demand decreases. Which AWS feature provides this capability?

- [ ] **A)** Elastic Load Balancing
- [ ] **B)** Amazon EC2 Auto Scaling
- [ ] **C)** AWS CloudFormation
- [ ] **D)** Amazon CloudFront

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EC2 Auto Scaling automatically adjusts the number of EC2 instances based on demand conditions you define (such as CPU utilization or request count). It scales out (adds instances) during spikes and scales in (removes instances) when demand drops, optimizing both performance and cost. Elastic Load Balancing distributes traffic across instances but does not add or remove them. AWS CloudFormation is an infrastructure-as-code tool for provisioning resources, not for dynamic scaling. Amazon CloudFront is a CDN for caching content at edge locations.
</details>

### Question 18 (Domain 4: Billing, Pricing, and Support)
A company runs a batch image processing job every night that can be stopped and restarted without any issues. The job typically takes 3-4 hours to complete. Which EC2 pricing model would be the most cost-effective?

- [ ] **A)** On-Demand Instances
- [ ] **B)** Spot Instances
- [ ] **C)** Reserved Instances (1-year, All Upfront)
- [ ] **D)** Dedicated Instances

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Spot Instances are ideal for workloads that are fault-tolerant and can handle interruptions — batch processing jobs that can be stopped and restarted are a classic Spot use case. Spot pricing offers up to 90% savings over On-Demand. On-Demand would work but costs significantly more. Reserved Instances require a 1- or 3-year commitment, which is overkill for a nightly batch job. Dedicated Instances are the most expensive and are used for regulatory or licensing requirements, not cost savings.
</details>

### Question 19 (Domain 1: Cloud Concepts)
A company currently maintains its own data centers and wants to understand the total cost implications of cloud migration. Which factors should they consider when comparing on-premises costs to AWS Cloud costs?

- [ ] **A)** Only the monthly AWS service charges
- [ ] **B)** Hardware, power, cooling, staff salaries, and facility costs for on-premises versus pay-as-you-go cloud costs
- [ ] **C)** Only the cost of EC2 instances needed to replace physical servers
- [ ] **D)** The cost of purchasing AWS data center equipment

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** A true total cost of ownership (TCO) comparison must include all on-premises costs: hardware procurement, power, cooling, physical security, facility maintenance, and IT staff salaries. These are compared against the pay-as-you-go model of AWS where many of those costs are eliminated or reduced. Looking at only monthly service charges (A) or only EC2 costs (C) gives an incomplete picture. Customers do not purchase AWS data center equipment (D) — AWS owns and manages all infrastructure.
</details>

### Question 20 (Domain 2: Security and Compliance)
A company has 50 developers who need access to AWS resources. Instead of creating individual policies for each developer, what is the BEST practice for managing their permissions?

- [ ] **A)** Share a single IAM user account among all developers
- [ ] **B)** Create an IAM group for developers and attach the appropriate policy to the group
- [ ] **C)** Give each developer root account credentials
- [ ] **D)** Create 50 individual IAM policies, one for each developer

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** IAM groups are the recommended way to manage permissions for multiple users with similar access needs. By creating a "Developers" group and attaching the appropriate policy to the group, all members automatically inherit those permissions. Sharing credentials (A) violates security best practices and makes auditing impossible. Using root credentials (C) is extremely dangerous and violates the principle of least privilege. Individual policies (D) create unnecessary management overhead.
</details>

### Question 21 (Domain 3: Cloud Technology and Services)
Which of the following statements about AWS Lambda is correct?

- [ ] **A)** Lambda functions can run indefinitely with no time limit
- [ ] **B)** Lambda automatically scales by running code in response to each trigger event
- [ ] **C)** Lambda requires you to pre-provision the number of concurrent executions
- [ ] **D)** Lambda functions must be written exclusively in Python

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Lambda automatically scales by running your code in response to each trigger — each event invocation is handled independently, and Lambda can run thousands of instances of your function concurrently. A standard Lambda function invocation can run for at most 15 minutes (the default timeout is 3 seconds), and even Lambda's longer-running options have fixed limits, so functions cannot run indefinitely. You do not need to pre-provision concurrency (though you can optionally set reserved concurrency). Lambda supports multiple languages including Python, Node.js, Java, Go, .NET, Ruby, and custom runtimes.
</details>

### Question 22 (Domain 2: Security and Compliance)
An application running on an EC2 instance needs to read objects from an S3 bucket. What is the MOST secure way to grant this access?

- [ ] **A)** Store AWS access keys in the application code on the EC2 instance
- [ ] **B)** Store AWS access keys in an environment variable on the EC2 instance
- [ ] **C)** Attach an IAM role with the appropriate S3 permissions to the EC2 instance
- [ ] **D)** Make the S3 bucket public so any application can read from it

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** IAM roles are the most secure way to grant AWS service permissions to EC2 instances. When you attach a role to an EC2 instance, temporary security credentials are automatically provided and rotated. Storing access keys in code (A) or environment variables (B) is insecure because keys can be accidentally exposed and do not rotate automatically. Making the S3 bucket public (D) exposes data to the entire internet.
</details>

### Question 23 (Domain 3: Cloud Technology and Services)
Which EC2 instance family is optimized for memory-intensive applications such as in-memory databases, real-time big data analytics, and high-performance caching?

- [ ] **A)** C-family (Compute Optimized)
- [ ] **B)** R-family (Memory Optimized)
- [ ] **C)** T-family (General Purpose)
- [ ] **D)** P-family (Accelerated Computing)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** R-family instances (Memory Optimized) are designed for workloads that process large data sets in memory, such as in-memory databases (Redis, Memcached), real-time processing of large unstructured data, and Apache Spark-based analytics. C-family instances (Compute Optimized) are for compute-bound tasks like batch processing and scientific modeling. T-family instances (General Purpose) provide a balance of compute, memory, and networking. P-family instances (Accelerated Computing) use GPUs for machine learning and graphics-intensive applications.
</details>

### Question 24 (Domain 1: Cloud Concepts)
A company currently pays $500,000 upfront every three years to refresh its server hardware. After migrating to AWS, it expects to pay $15,000 per month for equivalent compute resources. Which cloud economic principle does this transition represent?

- [ ] **A)** Benefit from massive economies of scale
- [ ] **B)** Stop guessing capacity
- [ ] **C)** Trade fixed expense for variable expense
- [ ] **D)** Increase speed and agility

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Moving from a large upfront capital expenditure ($500,000 every three years) to a monthly operational expenditure ($15,000/month) is a classic example of trading fixed expense for variable expense. This shifts spending from CapEx to OpEx and allows the company to pay only for what it uses. Economies of scale (A) refers to AWS passing along volume discounts. Stop guessing capacity (B) addresses right-sizing. Speed and agility (D) addresses provisioning speed.
</details>

### Question 25 (Domain 4: Billing, Pricing, and Support)
A company has a steady-state production database running 24/7 on Amazon EC2. The workload is predictable and will continue for at least 3 years. Which pricing option provides the greatest cost savings?

- [ ] **A)** On-Demand Instances
- [ ] **B)** Spot Instances
- [ ] **C)** Reserved Instances (3-year, All Upfront)
- [ ] **D)** Savings Plans (1-year, No Upfront)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Reserved Instances with a 3-year term and All Upfront payment provide the deepest discount (up to 72% off On-Demand). For a predictable, steady-state workload running 24/7 for at least 3 years, this is the most cost-effective option. Spot Instances are not appropriate because databases cannot tolerate interruptions. On-Demand provides no discount. A 1-year Savings Plan with No Upfront offers a smaller discount than a 3-year Reserved Instance with All Upfront.
</details>

### Question 26 (Domain 3: Cloud Technology and Services)
An application uses Amazon EC2 Auto Scaling with a minimum of 2 instances, a desired capacity of 4, and a maximum of 8. During a sudden traffic surge, CPU utilization spikes to 95% across all instances. What will Auto Scaling do?

- [ ] **A)** Terminate instances to save costs since CPU is too high
- [ ] **B)** Launch additional instances up to the maximum of 8 to handle the load
- [ ] **C)** Do nothing because the desired capacity is already set to 4
- [ ] **D)** Send a notification but take no scaling action

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EC2 Auto Scaling will launch additional instances to handle the increased load, up to the configured maximum of 8. When scaling policies detect that CPU utilization exceeds the target threshold, Auto Scaling performs a scale-out action by adding instances. It will never exceed the maximum capacity you set (8 in this case). Auto Scaling does not terminate instances in response to high load — it does the opposite. It does not simply sit idle when scaling policies are triggered, nor does it only notify without action (though it can send SNS notifications alongside scaling).
</details>

### Question 27 (Domain 2: Security and Compliance)
Which IAM security best practice should be applied to the AWS root user account?

- [ ] **A)** Use the root user for daily administrative tasks
- [ ] **B)** Share root user credentials with the IT team for emergency access
- [ ] **C)** Enable multi-factor authentication (MFA) and avoid using the root user for everyday tasks
- [ ] **D)** Delete the root user account after creating IAM admin users

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS strongly recommends enabling MFA on the root user and avoiding its use for everyday tasks. The root user has unrestricted access to all resources and cannot be limited by IAM policies. Instead, create IAM users with appropriate permissions for daily work. Using root for daily tasks (A) exposes the account to unnecessary risk. Sharing credentials (B) violates security best practices. The root user cannot be deleted (D) — it is the original account identity.
</details>

### Question 28 (Domain 1: Cloud Concepts)
How does AWS achieve lower pay-as-you-go prices for its customers compared to what most individual companies could achieve on their own?

- [ ] **A)** AWS uses older, less expensive hardware
- [ ] **B)** AWS aggregates usage from hundreds of thousands of customers to achieve economies of scale
- [ ] **C)** AWS does not charge for data transfer
- [ ] **D)** AWS receives government subsidies to reduce cloud pricing

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS achieves economies of scale by aggregating demand from hundreds of thousands of customers worldwide. This massive scale allows AWS to purchase hardware, power, and networking at much lower per-unit costs and pass those savings on to customers. AWS uses current-generation hardware, not older equipment (A). AWS does charge for certain data transfers (C). AWS pricing is based on its business model, not government subsidies (D).
</details>

### Question 29 (Domain 3: Cloud Technology and Services)
A development team wants to run a microservice that executes for only 200 milliseconds each time it is called, processes approximately 10 million requests per month, and requires no persistent server. How is this workload billed on AWS Lambda?

- [ ] **A)** By the number of EC2 instances provisioned per hour
- [ ] **B)** By the number of requests and the duration of each function execution
- [ ] **C)** A flat monthly fee based on the programming language used
- [ ] **D)** By the amount of data stored in the Lambda service

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Lambda pricing is based on two factors: the number of requests (invocations) and the duration of each execution (measured in milliseconds), multiplied by the amount of memory allocated to the function. There are no EC2 instances involved — Lambda is serverless. There is no flat monthly fee or per-language pricing. Lambda does not charge for data storage (any persistent storage would use S3 or DynamoDB with their own pricing). Lambda includes a generous free tier of 1 million requests and 400,000 GB-seconds per month.
</details>

### Question 30 (Domain 2: Security and Compliance)
A new IAM user has been created but has not been assigned any policies. What access does this user have to AWS services?

- [ ] **A)** Full read-only access to all AWS services
- [ ] **B)** Full access to the services in the same AWS Region
- [ ] **C)** No access to any AWS services — all permissions are denied by default
- [ ] **D)** Access to only IAM and billing services

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** IAM follows the principle of least privilege by default. A newly created IAM user has no permissions whatsoever — all access is implicitly denied until explicit permissions are granted through IAM policies. This ensures that users only receive the minimum access they need. There is no default read-only access (A), regional access (B), or baseline service access (D).
</details>

### Question 31 (Domain 3: Cloud Technology and Services)
Which of the following describes the relationship between Amazon ECS, Amazon EKS, and AWS Fargate?

- [ ] **A)** ECS and EKS are compute engines; Fargate is an orchestration platform
- [ ] **B)** ECS and EKS are container orchestration services; Fargate is a serverless compute engine that can run containers for either service
- [ ] **C)** Fargate is a container orchestration service; ECS and EKS are different compute engines
- [ ] **D)** All three are independent container orchestration platforms that cannot work together

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon ECS and Amazon EKS are container orchestration services — ECS is AWS's proprietary orchestrator, while EKS is managed Kubernetes. AWS Fargate is a serverless compute engine that can be used as the launch type for both ECS and EKS, removing the need to manage the underlying EC2 instances. Think of Fargate as the "how" (serverless infrastructure) and ECS/EKS as the "what" (orchestration layer). They work together, not independently.
</details>

### Question 32 (Domain 4: Billing, Pricing, and Support)
A company wants to reduce costs by committing to a consistent amount of compute usage (measured in $/hour) for 1 or 3 years, with the flexibility to change instance types, operating systems, and even switch between EC2 and Lambda. Which pricing model offers this flexibility?

- [ ] **A)** EC2 Reserved Instances
- [ ] **B)** Compute Savings Plans
- [ ] **C)** Spot Instances
- [ ] **D)** EC2 Instance Savings Plans

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Compute Savings Plans offer the most flexibility among commitment-based pricing models. You commit to a consistent amount of compute usage (in $/hour) for 1 or 3 years, and in return, you receive discounted pricing. The key advantage is that this discount applies across any EC2 instance family, size, OS, tenancy, or Region, and also applies to AWS Fargate and AWS Lambda usage. EC2 Reserved Instances and EC2 Instance Savings Plans are locked to a specific instance family and Region. Spot Instances are not commitment-based.
</details>

### Question 33 (Domain 1: Cloud Concepts)
A company provisioned 20 large EC2 instances for a new application but monitoring shows only 5 are needed during peak usage. Which cloud economics best practice should the company apply?

- [ ] **A)** Purchase Reserved Instances for all 20 servers to save money
- [ ] **B)** Right-size the deployment by reducing to the appropriate number and size of instances
- [ ] **C)** Move all instances to the largest available instance type for better performance
- [ ] **D)** Migrate the workload back to on-premises data centers

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Right-sizing means matching instance types and quantities to actual workload requirements. Since only 5 instances are needed at peak, the company should reduce from 20 to avoid paying for unused capacity. Purchasing Reserved Instances for all 20 (A) would lock in unnecessary spending. Upsizing instances (C) would increase costs further. Migrating back on-premises (D) does not solve the over-provisioning problem and abandons cloud benefits.
</details>

### Question 34 (Domain 2: Security and Compliance)
A company wants to allow a third-party auditing firm to read its AWS CloudTrail logs without creating IAM users in the company's account. What is the recommended approach?

- [ ] **A)** Share the root account credentials with the auditing firm
- [ ] **B)** Create an IAM role with cross-account access that the auditing firm can assume
- [ ] **C)** Make the CloudTrail S3 bucket publicly accessible
- [ ] **D)** Email the CloudTrail log files directly to the auditors

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** IAM cross-account roles are the recommended way to grant third parties access to your AWS resources. You create a role in your account with the necessary permissions, and the third-party account assumes that role to gain temporary access. Sharing root credentials (A) gives unrestricted access and is extremely dangerous. Making logs public (C) exposes sensitive audit data to anyone. Emailing logs (D) is not scalable, secure, or practical for ongoing access.
</details>

### Question 35 (Domain 3: Cloud Technology and Services)
A company has a web application behind an Elastic Load Balancer. During peak hours, some EC2 instances become unhealthy. What happens when the load balancer detects an unhealthy instance?

- [ ] **A)** The load balancer terminates the unhealthy instance and launches a replacement
- [ ] **B)** The load balancer stops sending traffic to the unhealthy instance and routes requests to healthy instances
- [ ] **C)** The load balancer shuts down entirely until all instances are healthy
- [ ] **D)** The load balancer sends an alert but continues routing traffic to the unhealthy instance

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Elastic Load Balancing performs health checks on registered targets. When it detects an unhealthy instance, it stops routing new requests to that instance and distributes traffic only among the remaining healthy instances. The load balancer does not terminate instances — that is the responsibility of EC2 Auto Scaling (if configured). The load balancer never shuts itself down due to unhealthy targets. It does not continue routing traffic to instances it has marked as unhealthy.
</details>

### Question 36 (Domain 4: Billing, Pricing, and Support)
A company needs to run a legacy Windows application that requires a specific software license tied to physical server hardware. Which EC2 pricing option allows them to use their own server-bound software licenses?

- [ ] **A)** Spot Instances
- [ ] **B)** On-Demand Instances
- [ ] **C)** Dedicated Hosts
- [ ] **D)** Reserved Instances

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** EC2 Dedicated Hosts provide a physical server fully dedicated to your use. This is important for software licenses that are tied to specific physical hardware (per-socket, per-core, or per-VM licensing models) such as Windows Server, SQL Server, or Oracle Database. Spot Instances, On-Demand Instances, and standard Reserved Instances all run on shared physical infrastructure, which does not satisfy hardware-bound license requirements. Dedicated Hosts give you visibility into the physical server, including sockets and cores.
</details>

### Question 37 (Domain 1: Cloud Concepts)
Which statement BEST describes the difference between capital expenditure (CapEx) and operational expenditure (OpEx) in the context of cloud computing?

- [ ] **A)** CapEx is a one-time expense for physical infrastructure; OpEx is an ongoing expense for services consumed
- [ ] **B)** CapEx is always more expensive than OpEx
- [ ] **C)** OpEx requires long-term contracts while CapEx does not
- [ ] **D)** CapEx refers to cloud costs while OpEx refers to on-premises costs

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** Capital expenditure (CapEx) involves upfront spending on physical assets like servers, data centers, and networking equipment. Operational expenditure (OpEx) involves paying for services as you consume them, like monthly cloud bills. Cloud computing shifts spending from CapEx to OpEx. CapEx is not always more expensive than OpEx (B) — it depends on the scenario. OpEx in the cloud often avoids long-term contracts (C). The definitions are reversed in option D — CapEx is typically associated with on-premises, and OpEx with cloud.
</details>

### Question 38 (Domain 2: Security and Compliance)
An IAM policy contains the following statement: {"Effect": "Deny", "Action": "s3:DeleteObject", "Resource": "*"}. Another policy attached to the same user contains: {"Effect": "Allow", "Action": "s3:*", "Resource": "*"}. What is the result when the user tries to delete an S3 object?

- [ ] **A)** The action is allowed because the Allow policy grants full S3 access
- [ ] **B)** The action is denied because an explicit Deny always overrides an Allow
- [ ] **C)** The action outcome depends on which policy was attached first
- [ ] **D)** The action is allowed because the wildcard (*) in the Allow policy takes precedence

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** In IAM policy evaluation, an explicit Deny always takes precedence over any Allow, regardless of how many policies grant access. This is a fundamental IAM rule. The Deny on s3:DeleteObject will block that specific action even though another policy allows all S3 actions. Policy attachment order (C) does not matter. Wildcards (D) do not override explicit Deny statements. This is a critical security mechanism that prevents accidental over-permissioning.
</details>

### Question 39 (Domain 3: Cloud Technology and Services)
A company needs to store millions of user-uploaded images that must be accessible from anywhere via a URL. The data should be highly durable and available. Which AWS storage service is best suited for this use case?

- [ ] **A)** Amazon EBS
- [ ] **B)** Amazon S3
- [ ] **C)** Amazon EFS
- [ ] **D)** AWS Storage Gateway

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon S3 (Simple Storage Service) is an object storage service designed for storing and retrieving any amount of data from anywhere on the internet. It provides 99.999999999% (11 nines) of durability and makes objects accessible via unique URLs. Amazon EBS is block storage attached to a single EC2 instance and cannot be accessed via URL. Amazon EFS is a network file system for EC2 instances, not designed for public URL access. AWS Storage Gateway is a hybrid storage service for connecting on-premises environments to cloud storage.
</details>

### Question 40 (Domain 2: Security and Compliance)
A company is experiencing a Distributed Denial of Service (DDoS) attack on its web application hosted on AWS. Which AWS service provides automatic DDoS protection at no additional cost?

- [ ] **A)** AWS WAF
- [ ] **B)** Amazon GuardDuty
- [ ] **C)** AWS Shield Standard
- [ ] **D)** AWS Shield Advanced

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS Shield Standard is automatically enabled for all AWS customers at no additional cost. It provides protection against the most common and frequently occurring DDoS attacks (Layer 3 and Layer 4). AWS WAF (A) is a web application firewall that filters HTTP/HTTPS traffic but is not free and is not specifically a DDoS service. Amazon GuardDuty (B) is a threat detection service for monitoring malicious activity, not DDoS mitigation. AWS Shield Advanced (D) provides enhanced DDoS protection but requires an additional paid subscription.
</details>

### Question 41 (Domain 3: Cloud Technology and Services)
A company stores compliance documents in Amazon S3 that are accessed frequently for the first 30 days, then rarely accessed afterward but must be retained for 7 years. Which S3 feature can automatically move objects to a cheaper storage class over time?

- [ ] **A)** S3 Versioning
- [ ] **B)** S3 Lifecycle Policies
- [ ] **C)** S3 Cross-Region Replication
- [ ] **D)** S3 Object Lock

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** S3 Lifecycle Policies allow you to define rules that automatically transition objects between storage classes based on age. For example, you could move objects to S3 Standard-IA after 30 days and to S3 Glacier after 90 days, optimizing costs over time. S3 Versioning keeps multiple versions of an object but does not change storage classes. S3 Cross-Region Replication copies objects to another Region for disaster recovery. S3 Object Lock prevents objects from being deleted or overwritten (for compliance), but does not manage storage class transitions.
</details>

### Question 42 (Domain 1: Cloud Concepts)
A solutions architect is designing an application that must continue operating even if an entire AWS data center experiences a failure. Which cloud design principle should they apply?

- [ ] **A)** Design for single-region deployment to reduce latency
- [ ] **B)** Design for failure by distributing workloads across multiple Availability Zones
- [ ] **C)** Design for cost optimization by using a single Availability Zone
- [ ] **D)** Design for simplicity by running everything on one large instance

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Designing for failure is a core cloud principle. By distributing workloads across multiple Availability Zones (AZs), the application can survive the failure of an entire data center because each AZ is a physically separate facility with independent power, networking, and cooling. A single-region deployment (A) does not protect against AZ failures. Using a single AZ (C) is the opposite of what is needed. Running on one large instance (D) creates a single point of failure.
</details>

### Question 43 (Domain 4: Billing, Pricing, and Support)
A startup expects unpredictable traffic spikes for a new mobile app. The company does not want to commit to a long-term contract. Which EC2 pricing model is MOST appropriate?

- [ ] **A)** On-Demand Instances
- [ ] **B)** Reserved Instances
- [ ] **C)** Dedicated Hosts
- [ ] **D)** Spot Instances

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** On-Demand Instances let you pay by the second (or hour) with no upfront commitment or long-term contract. This is ideal for unpredictable workloads. Reserved Instances require a 1- or 3-year commitment. Spot Instances can be interrupted with short notice, making them risky for user-facing apps. Dedicated Hosts are for compliance-driven workloads and are the most expensive option.
</details>

### Question 44 (Domain 3: Cloud Technology and Services)
Which Amazon S3 storage class is designed for data with unpredictable access patterns and automatically moves objects between frequent and infrequent access tiers to optimize costs?

- [ ] **A)** S3 Standard
- [ ] **B)** S3 Standard-Infrequent Access
- [ ] **C)** S3 Intelligent-Tiering
- [ ] **D)** S3 Glacier Flexible Retrieval

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** S3 Intelligent-Tiering automatically moves objects between a frequent access tier and an infrequent access tier based on changing access patterns. It charges a small monthly monitoring fee per object but has no retrieval fees and no minimum storage duration. S3 Standard is designed for frequently accessed data but does not automatically tier. S3 Standard-IA is for infrequently accessed data and charges retrieval fees. S3 Glacier Flexible Retrieval is for archival data with retrieval times of minutes to hours.
</details>

### Question 45 (Domain 2: Security and Compliance)
A security team wants to automatically detect unusual API activity, cryptocurrency mining, and potentially compromised EC2 instances in their AWS account. Which service should they enable?

- [ ] **A)** Amazon Inspector
- [ ] **B)** Amazon GuardDuty
- [ ] **C)** AWS Config
- [ ] **D)** AWS CloudTrail

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon GuardDuty is an intelligent threat detection service that continuously monitors for malicious activity and unauthorized behavior. It analyzes CloudTrail event logs, VPC Flow Logs, and DNS logs to detect threats like unusual API calls, cryptocurrency mining, and compromised instances. Amazon Inspector (A) assesses EC2 instances for vulnerabilities and deviations from best practices, not threat detection. AWS Config (C) tracks resource configuration changes. AWS CloudTrail (D) logs API activity but does not analyze it for threats.
</details>

### Question 46 (Domain 1: Cloud Concepts)
Which cloud architecture principle recommends replacing a single large server with multiple smaller servers to handle a workload?

- [ ] **A)** Implement elasticity
- [ ] **B)** Think parallel — scale horizontally instead of vertically
- [ ] **C)** Automate everything
- [ ] **D)** Use serverless architectures

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Horizontal scaling (scaling out) means adding more smaller servers instead of making one server bigger (vertical scaling or scaling up). This approach, often called "thinking parallel," improves fault tolerance and allows for more granular scaling. Elasticity (A) refers to automatic scaling but does not specifically address horizontal vs. vertical. Automation (C) is about reducing manual processes. Serverless (D) is a specific architecture pattern, not a scaling principle.
</details>

### Question 47 (Domain 3: Cloud Technology and Services)
An application running on Amazon EC2 needs a high-performance block storage volume that persists independently of the instance lifecycle. Which service provides this?

- [ ] **A)** Amazon S3
- [ ] **B)** Amazon EBS
- [ ] **C)** Instance Store
- [ ] **D)** Amazon S3 Glacier

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon EBS (Elastic Block Store) provides persistent block storage volumes for EC2 instances. EBS volumes persist independently of the instance lifecycle — if you stop or terminate an instance, the EBS volume and its data can be retained. Amazon S3 is object storage, not block storage. Instance Store provides temporary block storage that is physically attached to the host machine — data is lost when the instance is stopped or terminated. S3 Glacier is an archival storage service, not block storage.
</details>

### Question 48 (Domain 2: Security and Compliance)
A company needs to protect its web application from common exploits such as SQL injection and cross-site scripting (XSS) attacks. Which AWS service should they use?

- [ ] **A)** AWS Shield Standard
- [ ] **B)** Amazon GuardDuty
- [ ] **C)** AWS WAF (Web Application Firewall)
- [ ] **D)** Amazon Macie

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** AWS WAF is designed to protect web applications from common web exploits like SQL injection, cross-site scripting (XSS), and other OWASP Top 10 vulnerabilities. It lets you create rules to filter HTTP/HTTPS traffic based on conditions you define. AWS Shield Standard (A) protects against DDoS attacks, not application-layer exploits. GuardDuty (B) detects threats but does not filter web traffic. Amazon Macie (D) discovers and protects sensitive data in S3, not web application traffic.
</details>

### Question 49 (Domain 3: Cloud Technology and Services)
A research organization must migrate a large data set to Amazon S3, but the available network would take too long. Which AWS offering can transport the data on a shipped device?

- [ ] **A)** AWS Direct Connect
- [ ] **B)** AWS Snowball Edge
- [ ] **C)** S3 Transfer Acceleration
- [ ] **D)** AWS DataSync

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Snowball Edge is a Snow Family device that AWS ships to the customer for offline data transfer and later ingestion into AWS storage. Since November 7, 2025, Snowball Edge is available only to existing customers; AWS points new customers to AWS DataSync for online transfers, AWS Data Transfer Terminal for secure physical transfers, or AWS Partner solutions. Direct Connect, S3 Transfer Acceleration, and DataSync move data over network connections and therefore do not remove the stated bandwidth constraint.
</details>

### Question 50 (Domain 1: Cloud Concepts)
A company wants to ensure its cloud infrastructure can be consistently and repeatedly deployed without manual configuration errors. Which cloud design principle addresses this need?

- [ ] **A)** Stop guessing capacity
- [ ] **B)** Test at production scale
- [ ] **C)** Use infrastructure as code (IaC) to automate deployments
- [ ] **D)** Go global in minutes

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Infrastructure as code (IaC) enables consistent, repeatable deployments by defining infrastructure in machine-readable templates (such as AWS CloudFormation or Terraform). This eliminates manual configuration errors and makes infrastructure version-controllable. Stop guessing capacity (A) addresses right-sizing. Testing at production scale (B) addresses testing methodology. Going global in minutes (D) addresses geographic expansion, not configuration consistency.
</details>

### Question 51 (Domain 2: Security and Compliance)
A company stores sensitive customer data, including personally identifiable information (PII) and financial records, in Amazon S3. Which AWS service can automatically discover and classify this sensitive data?

- [ ] **A)** Amazon GuardDuty
- [ ] **B)** Amazon Macie
- [ ] **C)** AWS Shield
- [ ] **D)** Amazon Inspector

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon Macie is a data security service that uses machine learning and pattern matching to discover and protect sensitive data stored in Amazon S3. It can automatically identify PII, financial data, and other sensitive information and alert you to potential data exposure. GuardDuty (A) detects threats but does not classify data. AWS Shield (C) protects against DDoS attacks. Amazon Inspector (D) assesses infrastructure for vulnerabilities, not data classification.
</details>

### Question 52 (Domain 3: Cloud Technology and Services)
A media production company needs a shared file system that multiple Linux-based EC2 instances can access simultaneously with standard NFS protocol. Which AWS storage service should they use?

- [ ] **A)** Amazon EBS
- [ ] **B)** Amazon S3
- [ ] **C)** Amazon EFS
- [ ] **D)** Amazon FSx for Windows File Server

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon EFS (Elastic File System) is a fully managed, elastic NFS file system that can be mounted simultaneously by thousands of EC2 instances across multiple Availability Zones. It uses the standard NFSv4 protocol and is designed for Linux workloads. Amazon EBS volumes can only be attached to a single EC2 instance at a time (with the exception of Multi-Attach for io1/io2 volumes). Amazon S3 is object storage and does not support NFS mounting. Amazon FSx for Windows File Server uses the SMB protocol and is designed for Windows workloads, not Linux/NFS.
</details>

### Question 53 (Domain 1: Cloud Concepts)
Which cloud deployment model uses a combination of on-premises infrastructure and AWS Cloud resources, connected via a secure network?

- [ ] **A)** Public cloud
- [ ] **B)** Private cloud
- [ ] **C)** Hybrid cloud
- [ ] **D)** Multi-cloud

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** A hybrid cloud deployment connects on-premises infrastructure (or a private cloud) with public cloud resources like AWS. This is typically done using a VPN or AWS Direct Connect to create a secure network bridge between environments. A public cloud (A) is fully hosted by a cloud provider with no on-premises component. A private cloud (B) is dedicated infrastructure for a single organization. Multi-cloud (D) refers to using multiple public cloud providers, not combining on-premises with cloud.
</details>

### Question 54 (Domain 2: Security and Compliance)
A security engineer needs to run automated vulnerability assessments on EC2 instances to identify unpatched software and unintended network exposure. Which AWS service should they use?

- [ ] **A)** AWS Trusted Advisor
- [ ] **B)** Amazon Inspector
- [ ] **C)** AWS Security Hub
- [ ] **D)** Amazon Detective

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon Inspector is an automated vulnerability management service that continually scans EC2 instances (and container images and Lambda functions) for software vulnerabilities and unintended network exposure. It provides detailed findings with remediation guidance. AWS Trusted Advisor (A) provides broad best-practice recommendations but is not a vulnerability scanner. AWS Security Hub (C) aggregates security findings from multiple services but does not perform scans itself. Amazon Detective (D) investigates and analyzes security findings, not scan for vulnerabilities.
</details>

### Question 55 (Domain 3: Cloud Technology and Services)
Which Amazon S3 storage class provides the lowest cost for data archival with a retrieval time of 12 hours or more?

- [ ] **A)** S3 Glacier Flexible Retrieval
- [ ] **B)** S3 Glacier Deep Archive
- [ ] **C)** S3 Standard-Infrequent Access
- [ ] **D)** S3 One Zone-Infrequent Access

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** S3 Glacier Deep Archive is the lowest-cost S3 storage class, designed for long-term data archival where retrieval times of 12 hours are acceptable. It is ideal for data that is accessed once or twice a year, such as compliance archives and digital preservation. S3 Glacier Flexible Retrieval is cheaper than standard classes but more expensive than Deep Archive, with retrieval times from minutes to hours. S3 Standard-IA and S3 One Zone-IA are designed for infrequently accessed data but provide millisecond access and cost more than either Glacier class.
</details>

### Question 56 (Domain 2: Security and Compliance)
A company wants a centralized dashboard that aggregates security findings from Amazon GuardDuty, Amazon Inspector, Amazon Macie, and third-party tools. Which AWS service provides this capability?

- [ ] **A)** AWS CloudTrail
- [ ] **B)** AWS Security Hub
- [ ] **C)** Amazon CloudWatch
- [ ] **D)** AWS Config

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Security Hub provides a comprehensive view of your security posture across AWS accounts. (AWS now calls these findings-aggregation and best-practice-check features AWS Security Hub CSPM; the newer AWS Security Hub correlates GuardDuty, Inspector, Macie, and Security Hub CSPM signals. The online CLF-C02 in-scope list still says AWS Security Hub.) It aggregates, organizes, and prioritizes security findings from multiple AWS services (GuardDuty, Inspector, Macie, Firewall Manager) and third-party tools in a single dashboard. CloudTrail (A) logs API calls. CloudWatch (C) monitors metrics and logs for operational purposes. AWS Config (D) tracks resource configurations but does not aggregate security findings from multiple services.
</details>

### Question 57 (Domain 3: Cloud Technology and Services)
A company uses Windows-based file shares for their enterprise applications and wants to migrate to a fully managed AWS solution that supports the SMB protocol and Active Directory integration. Which service should they choose?

- [ ] **A)** Amazon EFS
- [ ] **B)** Amazon FSx for Windows File Server
- [ ] **C)** Amazon S3
- [ ] **D)** AWS Storage Gateway (File Gateway)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Amazon FSx for Windows File Server is a fully managed Windows file system built on Windows Server. It supports the SMB protocol, NTFS, Active Directory (AD) integration, and Distributed File System (DFS) — making it the natural migration path for Windows file shares. Amazon EFS supports the NFS protocol only (Linux workloads). Amazon S3 is object storage that does not support SMB. AWS Storage Gateway (File Gateway) provides a hybrid solution but acts as a cache in front of S3, not a native Windows file server.
</details>

### Question 58 (Domain 1: Cloud Concepts)
A company wants to move its existing on-premises applications to AWS as quickly as possible without making any code changes. Which migration strategy (one of the 6 Rs) should they use?

- [ ] **A)** Refactor — re-architect the application for cloud-native features
- [ ] **B)** Rehost — lift and shift the application to AWS without modifications
- [ ] **C)** Repurchase — replace the application with a SaaS alternative
- [ ] **D)** Retire — decommission the application entirely

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Rehosting (lift and shift) involves moving an application to AWS without making any changes to the application code or architecture. This is the fastest migration approach. Refactoring (A) requires re-architecting the application, which takes significant time and effort. Repurchasing (C) replaces the application with a different product. Retiring (D) means shutting down the application, not migrating it.
</details>

### Question 59 (Domain 3: Cloud Technology and Services)
An architect needs to create a point-in-time backup of an Amazon EBS volume that can be used to restore data or create new volumes in the same or different Availability Zone. What should they use?

- [ ] **A)** EBS Snapshots
- [ ] **B)** Amazon S3 Versioning
- [ ] **C)** AWS Backup
- [ ] **D)** Amazon Machine Images (AMI)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** EBS Snapshots are incremental backups of EBS volumes stored in Amazon S3 (managed by AWS). You can use snapshots to restore an existing volume or create new EBS volumes in any Availability Zone within the same Region (or copy them to other Regions). S3 Versioning manages versions of S3 objects, not EBS volumes. AWS Backup is a centralized backup service that can manage EBS snapshots but the fundamental mechanism is still EBS Snapshots. AMIs contain the instance configuration and root volume snapshot but are for launching entire instances, not just restoring individual data volumes.
</details>

### Question 60 (Domain 2: Security and Compliance)
After Amazon GuardDuty generates a finding about suspicious activity, a security analyst needs to investigate the root cause by analyzing related events, network flows, and user activity over time. Which AWS service is designed for this investigation workflow?

- [ ] **A)** Amazon Macie
- [ ] **B)** AWS CloudTrail
- [ ] **C)** Amazon Detective
- [ ] **D)** AWS Config

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon Detective makes it easy to analyze, investigate, and identify the root cause of security findings. It automatically collects and processes data from AWS CloudTrail, VPC Flow Logs, and GuardDuty findings to build a unified interactive view for investigation. While CloudTrail (B) provides raw API logs, it does not provide the analysis and visualization capabilities that Detective offers. Macie (A) focuses on data discovery in S3. AWS Config (D) tracks configuration changes.
</details>

### Question 61 (Domain 1: Cloud Concepts)
A company decides to move its on-premises Microsoft Exchange email servers to Microsoft 365 in the cloud. Which migration strategy does this represent?

- [ ] **A)** Rehost
- [ ] **B)** Replatform
- [ ] **C)** Repurchase
- [ ] **D)** Refactor

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Repurchasing (also called "drop and shop") involves replacing an existing application with a cloud-based alternative, typically a SaaS product. Moving from self-managed Exchange servers to Microsoft 365 is a classic repurchase example — the company is buying a new product rather than migrating the existing one. Rehosting (A) would mean running Exchange on AWS EC2. Replatforming (B) would involve minor optimizations while keeping the same product. Refactoring (D) would mean re-architecting the email system for cloud-native features.
</details>

### Question 62 (Domain 3: Cloud Technology and Services)
A hospital needs to maintain on-premises access to medical imaging files for low-latency access while also backing up the data to Amazon S3 for durability and compliance. Which AWS service bridges this hybrid storage requirement?

- [ ] **A)** AWS Snowball
- [ ] **B)** AWS Storage Gateway
- [ ] **C)** Amazon EFS
- [ ] **D)** AWS Direct Connect

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Storage Gateway is a hybrid cloud storage service that provides on-premises applications with seamless access to virtually unlimited cloud storage. It caches frequently accessed data on-premises for low-latency access while storing the full data set in Amazon S3. This is ideal for hybrid environments where you need local performance and cloud durability. AWS Snowball is for offline data transfer, not ongoing hybrid access. Amazon EFS is a cloud-native file system, not a hybrid bridge. AWS Direct Connect provides a dedicated network connection but does not manage storage caching.
</details>

### Question 63 (Domain 2: Security and Compliance)
A healthcare company needs to verify that AWS services it uses are compliant with HIPAA before storing protected health information (PHI). Where can the company find documentation of AWS compliance certifications and reports?

- [ ] **A)** AWS Trusted Advisor
- [ ] **B)** AWS Artifact
- [ ] **C)** AWS Config
- [ ] **D)** AWS CloudTrail

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports, certifications, and agreements. This includes SOC reports, PCI DSS attestations, HIPAA-related documentation, and other compliance artifacts. Trusted Advisor (A) provides best practice recommendations but not compliance reports. AWS Config (C) evaluates resource configurations. CloudTrail (D) logs API activity.
</details>

### Question 64 (Domain 1: Cloud Concepts)
A company migrates its on-premises MySQL database to Amazon Aurora without changing the application code but gains performance improvements from the managed service. Which migration strategy is this?

- [ ] **A)** Rehost
- [ ] **B)** Replatform
- [ ] **C)** Refactor
- [ ] **D)** Retain

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Replatforming (lift, tinker, and shift) involves making a few cloud optimizations during migration without changing the core architecture. Migrating MySQL to Amazon Aurora is a classic replatform example — the database engine is MySQL-compatible, so the application code does not change, but the company benefits from Aurora's managed features and performance improvements. Rehosting (A) would mean running the same MySQL on EC2 with no changes. Refactoring (C) would mean completely re-architecting the data layer. Retaining (D) means keeping the workload on-premises.
</details>

### Question 65 (Domain 2: Security and Compliance)
A large enterprise with multiple AWS accounts wants to enforce security policies centrally, such as preventing any account from disabling CloudTrail logging. Which AWS feature should they use?

- [ ] **A)** IAM policies attached to each account's admin user
- [ ] **B)** Service Control Policies (SCPs) in AWS Organizations
- [ ] **C)** Amazon GuardDuty across all accounts
- [ ] **D)** AWS Config rules in each account

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Service Control Policies (SCPs) in AWS Organizations allow you to centrally enforce permission guardrails across all accounts in the organization. SCPs can restrict actions even for account administrators, such as preventing the disabling of CloudTrail. Individual IAM policies (A) can be overridden by account admins. GuardDuty (C) detects threats but cannot prevent actions. AWS Config rules (D) can detect non-compliance but cannot prevent actions in real time.
</details>

---

## 🔑 Quick Answer Key Summary

- 1. **B** (Domain 1)
- 2. **C** (Domain 2)
- 3. **A** (Domain 3)
- 4. **B** (Domain 2)
- 5. **B** (Domain 3)
- 6. **B** (Domain 1)
- 7. **C** (Domain 4)
- 8. **A** (Domain 3)
- 9. **B** (Domain 2)
- 10. **C** (Domain 1)
- 11. **B** (Domain 3)
- 12. **C** (Domain 2)
- 13. **B** (Domain 3)
- 14. **C** (Domain 4)
- 15. **B** (Domain 1)
- 16. **B** (Domain 2)
- 17. **B** (Domain 3)
- 18. **B** (Domain 4)
- 19. **B** (Domain 1)
- 20. **B** (Domain 2)
- 21. **B** (Domain 3)
- 22. **C** (Domain 2)
- 23. **B** (Domain 3)
- 24. **C** (Domain 1)
- 25. **C** (Domain 4)
- 26. **B** (Domain 3)
- 27. **C** (Domain 2)
- 28. **B** (Domain 1)
- 29. **B** (Domain 3)
- 30. **C** (Domain 2)
- 31. **B** (Domain 3)
- 32. **B** (Domain 4)
- 33. **B** (Domain 1)
- 34. **B** (Domain 2)
- 35. **B** (Domain 3)
- 36. **C** (Domain 4)
- 37. **A** (Domain 1)
- 38. **B** (Domain 2)
- 39. **B** (Domain 3)
- 40. **C** (Domain 2)
- 41. **B** (Domain 3)
- 42. **B** (Domain 1)
- 43. **A** (Domain 4)
- 44. **C** (Domain 3)
- 45. **B** (Domain 2)
- 46. **B** (Domain 1)
- 47. **B** (Domain 3)
- 48. **C** (Domain 2)
- 49. **B** (Domain 3)
- 50. **C** (Domain 1)
- 51. **B** (Domain 2)
- 52. **C** (Domain 3)
- 53. **C** (Domain 1)
- 54. **B** (Domain 2)
- 55. **B** (Domain 3)
- 56. **B** (Domain 2)
- 57. **B** (Domain 3)
- 58. **B** (Domain 1)
- 59. **A** (Domain 3)
- 60. **C** (Domain 2)
- 61. **C** (Domain 1)
- 62. **B** (Domain 3)
- 63. **B** (Domain 2)
- 64. **B** (Domain 1)
- 65. **B** (Domain 2)
