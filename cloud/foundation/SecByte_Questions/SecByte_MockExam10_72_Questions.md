# AWS Certified Cloud Practitioner (CLF-C02) - SecByte Mock Exam 10 (72 Questions)

Extracted from [Learn SecByte Mock Exam 10](https://learn.secbyte.org/mock-exams/clf-c02-practice-test-mock-exam-10).

This document contains all **72 practice questions** structured across 18 core AWS CLF-C02 knowledge domains (4 questions per topic), with verified correct answers and detailed option-by-option rationales.

## Quick Table of Contents

- [Question 1](#q-1): `AWS global infrastructure` - A company wants to deploy an application in multiple isolated location... *(Ans: A)*
- [Question 2](#q-2): `AWS global infrastructure` - Which AWS infrastructure component is primarily used by Amazon CloudFr... *(Ans: B)*
- [Question 3](#q-3): `AWS global infrastructure` - A workload must run near users in a city that is far from the nearest ... *(Ans: A)*
- [Question 4](#q-4): `AWS global infrastructure` - Which statements correctly describe AWS Regions? (Select TWO.)... *(Ans: A, B)*
- [Question 5](#q-5): `Cloud computing benefits` - A startup moves its application from self-managed servers to AWS. Whic... *(Ans: A)*
- [Question 6](#q-6): `Cloud computing benefits` - Which cloud benefit allows an organization to replace a large upfront ... *(Ans: A)*
- [Question 7](#q-7): `Cloud computing benefits` - An application experiences unpredictable traffic spikes. Which cloud c... *(Ans: A)*
- [Question 8](#q-8): `Cloud computing benefits` - Which are common benefits of cloud computing? (Select TWO.)... *(Ans: A, B)*
- [Question 9](#q-9): `AWS shared responsibility model` - Under the AWS shared responsibility model, which task is generally the... *(Ans: A)*
- [Question 10](#q-10): `AWS shared responsibility model` - Which security task remains the customer's responsibility when using A... *(Ans: A)*
- [Question 11](#q-11): `AWS shared responsibility model` - A company uses Amazon RDS and wants to understand which task it still ... *(Ans: A)*
- [Question 12](#q-12): `AWS shared responsibility model` - Which responsibilities remain with the customer in AWS? (Select TWO.)... *(Ans: A, B)*
- [Question 13](#q-13): `IAM users, groups, roles, and policies` - What is the recommended way for an application running on Amazon EC2 t... *(Ans: A)*
- [Question 14](#q-14): `IAM users, groups, roles, and policies` - A company wants to grant the same read-only permissions to 40 develope... *(Ans: A)*
- [Question 15](#q-15): `IAM users, groups, roles, and policies` - An administrator must permit a backup service to delete objects only f... *(Ans: A)*
- [Question 16](#q-16): `IAM users, groups, roles, and policies` - Which IAM practices improve account security? (Select TWO.)... *(Ans: A, B)*
- [Question 17](#q-17): `Amazon EC2` - A workload requires a predictable amount of compute capacity continuou... *(Ans: A)*
- [Question 18](#q-18): `Amazon EC2` - A batch processing application can tolerate interruptions and must min... *(Ans: A)*
- [Question 19](#q-19): `Amazon EC2` - Which EC2 feature allows instances to be launched from a predefined te... *(Ans: A)*
- [Question 20](#q-20): `Amazon EC2` - Which statements about EC2 security groups are correct? (Select TWO.)... *(Ans: A, B)*
- [Question 21](#q-21): `AWS Lambda` - A developer needs to run short-lived code whenever a new object is upl... *(Ans: A)*
- [Question 22](#q-22): `AWS Lambda` - A Lambda function must access DynamoDB without storing credentials in ... *(Ans: A)*
- [Question 23](#q-23): `AWS Lambda` - Which factor most directly affects Lambda pricing for a function invoc... *(Ans: A)*
- [Question 24](#q-24): `AWS Lambda` - Which are characteristics of AWS Lambda? (Select TWO.)... *(Ans: A, B)*
- [Question 25](#q-25): `Amazon S3` - A company needs highly durable object storage for user-uploaded images... *(Ans: A)*
- [Question 26](#q-26): `Amazon S3` - Which S3 feature helps prevent accidental deletion or overwriting of o... *(Ans: A)*
- [Question 27](#q-27): `Amazon S3` - A company must ensure that objects uploaded to an S3 bucket are encryp... *(Ans: A)*
- [Question 28](#q-28): `Amazon S3` - Which S3 features can help protect or manage stored objects? (Select T... *(Ans: A, B)*
- [Question 29](#q-29): `Amazon EBS` - An EC2 instance requires persistent block storage that remains availab... *(Ans: A)*
- [Question 30](#q-30): `Amazon EBS` - A database workload requires consistently high IOPS and low-latency bl... *(Ans: A)*
- [Question 31](#q-31): `Amazon EBS` - A company wants to create a point-in-time backup of an EBS volume. Whi... *(Ans: A)*
- [Question 32](#q-32): `Amazon EBS` - Which statements about EBS are correct? (Select TWO.)... *(Ans: A, B)*
- [Question 33](#q-33): `Amazon RDS and DynamoDB` - A company needs a managed relational database with automated backups, ... *(Ans: A)*
- [Question 34](#q-34): `Amazon RDS and DynamoDB` - An application needs a serverless NoSQL database with single-digit mil... *(Ans: A)*
- [Question 35](#q-35): `Amazon RDS and DynamoDB` - A database must remain available if one Availability Zone fails. Which... *(Ans: A)*
- [Question 36](#q-36): `Amazon RDS and DynamoDB` - Which statements correctly compare Amazon RDS and DynamoDB? (Select TW... *(Ans: A, B)*
- [Question 37](#q-37): `Amazon VPC` - A public web application needs isolated networking, public subnets for... *(Ans: A)*
- [Question 38](#q-38): `Amazon VPC` - Instances in a private subnet need outbound internet access for softwa... *(Ans: A)*
- [Question 39](#q-39): `Amazon VPC` - Which VPC component determines where network traffic from a subnet is ... *(Ans: A)*
- [Question 40](#q-40): `Amazon VPC` - Which VPC controls are stateful and stateful-less, respectively?... *(Ans: A)*
- [Question 41](#q-41): `Elastic Load Balancing` - A web application runs on multiple EC2 instances and needs automatic d... *(Ans: A)*
- [Question 42](#q-42): `Elastic Load Balancing` - A company needs to distribute TCP traffic to a fleet of servers while ... *(Ans: A)*
- [Question 43](#q-43): `Elastic Load Balancing` - Which ELB capability helps stop routing traffic to an unhealthy EC2 ta... *(Ans: A)*
- [Question 44](#q-44): `Elastic Load Balancing` - Which statements about Elastic Load Balancing are correct? (Select TWO... *(Ans: A, B)*
- [Question 45](#q-45): `Amazon CloudFront` - A media company wants users worldwide to receive cached video segments... *(Ans: A)*
- [Question 46](#q-46): `Amazon CloudFront` - A company wants CloudFront to retrieve private content from an S3 buck... *(Ans: A)*
- [Question 47](#q-47): `Amazon CloudFront` - Which CloudFront feature allows a distribution to serve different cach... *(Ans: A)*
- [Question 48](#q-48): `Amazon CloudFront` - Which CloudFront capabilities can improve delivery performance or secu... *(Ans: A, B)*
- [Question 49](#q-49): `Amazon Route 53` - Which Route 53 routing policy directs users to the endpoint with the l... *(Ans: A)*
- [Question 50](#q-50): `Amazon Route 53` - A company wants DNS to direct traffic to a primary application endpoin... *(Ans: A)*
- [Question 51](#q-51): `Amazon Route 53` - Which Route 53 function translates a domain name such as app.example.c... *(Ans: A)*
- [Question 52](#q-52): `Amazon Route 53` - Which Route 53 features are available for application traffic manageme... *(Ans: A, B)*
- [Question 53](#q-53): `AWS CloudTrail and Amazon CloudWatch` - A security team needs a record of AWS API calls, including who made th... *(Ans: A)*
- [Question 54](#q-54): `AWS CloudTrail and Amazon CloudWatch` - An operations team wants an alarm when an EC2 instance's CPU utilizati... *(Ans: A)*
- [Question 55](#q-55): `AWS CloudTrail and Amazon CloudWatch` - Which service is best suited for collecting application logs and creat... *(Ans: A)*
- [Question 56](#q-56): `AWS CloudTrail and Amazon CloudWatch` - Which statements correctly distinguish CloudTrail and CloudWatch? (Sel... *(Ans: A, B)*
- [Question 57](#q-57): `AWS pricing models` - A company runs a production workload continuously and wants a discount... *(Ans: A)*
- [Question 58](#q-58): `AWS pricing models` - Which pricing model is most appropriate for a fault-tolerant workload ... *(Ans: A)*
- [Question 59](#q-59): `AWS pricing models` - Which AWS tool can estimate the expected monthly cost of a planned arc... *(Ans: A)*
- [Question 60](#q-60): `AWS pricing models` - Which factors can affect the cost of an AWS workload? (Select TWO.)... *(Ans: A, B)*
- [Question 61](#q-61): `AWS Cost Explorer and AWS Budgets` - A finance team wants to analyze historical AWS spending by service, ac... *(Ans: A)*
- [Question 62](#q-62): `AWS Cost Explorer and AWS Budgets` - A company wants an alert when monthly AWS spending is forecast to exce... *(Ans: A)*
- [Question 63](#q-63): `AWS Cost Explorer and AWS Budgets` - A team needs to determine which tagged application generated a recent ... *(Ans: A)*
- [Question 64](#q-64): `AWS Cost Explorer and AWS Budgets` - Which actions support AWS cost governance? (Select TWO.)... *(Ans: A, B)*
- [Question 65](#q-65): `AWS Support plans` - A company needs architectural guidance and a predictable response targ... *(Ans: A)*
- [Question 66](#q-66): `AWS Support plans` - Which AWS Support feature can help a customer review account security,... *(Ans: A)*
- [Question 67](#q-67): `AWS Support plans` - A developer has a general question about configuring an AWS service an... *(Ans: A)*
- [Question 68](#q-68): `AWS Support plans` - Which AWS Support-related capabilities can help an organization operat... *(Ans: A, B)*
- [Question 69](#q-69): `AWS Well-Architected Framework` - A team wants to improve an application by evaluating operational excel... *(Ans: A)*
- [Question 70](#q-70): `AWS Well-Architected Framework` - A workload has no tested recovery process and depends on one Availabil... *(Ans: A)*
- [Question 71](#q-71): `AWS Well-Architected Framework` - An organization discovers that several oversized instances run at low ... *(Ans: A)*
- [Question 72](#q-72): `AWS Well-Architected Framework` - Which practices align with the AWS Well-Architected Framework? (Select... *(Ans: A, B)*

---

<a id="q-1"></a>

### Question 1

**Topic:** `AWS global infrastructure` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `6b08beaf-249e-4599-8582-740de9e6a8ce`

> **Scenario:**  
> A company wants to deploy an application in multiple isolated locations within the same AWS geographic area to improve availability. Which AWS infrastructure concept should it use?

#### Options
- **A.** Availability Zones **[CORRECT]**
- **B.** Edge locations
- **C.** AWS Regions
- **D.** Local Zones

**Correct Answer:** `A`

> **Summary:** Availability Zones (AZs) are one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region, providing fault isolation within the same geographic area.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Availability Zones (AZs) provide isolated locations within the same AWS Region connected through low-latency links. Deploying across multiple AZs ensures high availability and resilience against data center failures.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Edge locations are points of presence used by Amazon CloudFront to cache content closer to end users, not for deploying multi-tier applications directly.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Regions represent separate geographic locations around the world (e.g., us-east-1, eu-west-1), not multiple isolated locations within the same geographic area.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Local Zones extend AWS infrastructure closer to specific metropolitan areas for single-digit millisecond latency, but do not provide the multi-AZ isolated deployment model within a standard Region.

---

<a id="q-2"></a>

### Question 2

**Topic:** `AWS global infrastructure` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `515b6774-fcdf-4dfa-8e94-d70e011de33f`

> **Scenario:**  
> Which AWS infrastructure component is primarily used by Amazon CloudFront to cache content close to end users?

#### Options
- **A.** Availability Zones
- **B.** Edge locations **[CORRECT]**
- **C.** Dedicated Hosts
- **D.** VPC subnets

**Correct Answer:** `B`

> **Summary:** Amazon CloudFront is a Content Delivery Network (CDN) that delivers data, videos, and APIs to customers globally using a worldwide network of Edge locations.

#### Comprehensive Verification & Explanations

- **Option A:** ❌ **Why it is INCORRECT:**  
  Availability Zones host compute and database workloads within a Region, whereas CloudFront caches web content globally at Edge locations.

- **Option B:** ✅ **Why it is CORRECT:**  
  Edge locations are globally distributed points of presence (PoPs) where Amazon CloudFront caches content to deliver it to viewers with the lowest possible latency.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Dedicated Hosts are physical EC2 servers dedicated entirely to a single customer for licensing and compliance compliance; they do not cache content for CloudFront.

- **Option D:** ❌ **Why it is INCORRECT:**  
  VPC subnets are IP address ranges within an Amazon VPC in a specific Availability Zone and are not the global endpoints used by CloudFront.

---

<a id="q-3"></a>

### Question 3

**Topic:** `AWS global infrastructure` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `9d5e2bb6-7ba0-4f4b-87d4-c1faff40a38d`

> **Scenario:**  
> A workload must run near users in a city that is far from the nearest AWS Region. Which option can reduce latency while remaining connected to the parent Region?

#### Options
- **A.** AWS Local Zones **[CORRECT]**
- **B.** AWS Organizations
- **C.** Security groups
- **D.** AWS Direct Connect gateways

**Correct Answer:** `A`

> **Summary:** AWS Local Zones place compute, storage, database, and select AWS services close to large population and industry centers where no AWS Region currently exists.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Local Zones extend AWS Regions to place resources (such as compute and storage) geographically close to end users in specific metropolitan areas to achieve single-digit millisecond latency.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS Organizations is an account governance and consolidated billing service, not an infrastructure deployment component.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Security groups function as virtual firewalls to control traffic for EC2 instances, not physical or geographical deployment zones.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Direct Connect gateways connect on-premises networks to multiple VPCs across different Regions, but do not provide compute capacity in remote cities.

---

<a id="q-4"></a>

### Question 4

**Topic:** `AWS global infrastructure` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `4eef13fe-925e-4438-b9f5-e3d03af71aa9`

> **Scenario *(Select TWO)*:**  
> Which statements correctly describe AWS Regions? (Select TWO.)

#### Options
- **A.** A Region contains multiple Availability Zones. **[CORRECT]**
- **B.** A Region is a separate geographic area. **[CORRECT]**
- **C.** Every AWS service is available in every Region.
- **D.** Regions are used only for static website hosting.
- **E.** All Regions share one automatically replicated data store.

**Correct Answer:** `A, B`

> **Summary:** An AWS Region is a physical location in the world where AWS has multiple, isolated, and physically separated Availability Zones (AZs).

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Every AWS Region consists of multiple (at least three) isolated and physically separated Availability Zones connected via low-latency, high-throughput private networking.

- **Option B:** ✅ **Why it is CORRECT:**  
  An AWS Region is a completely separate geographic area (such as US East (N. Virginia), Europe (Ireland), or Asia Pacific (Tokyo)) to achieve fault isolation and regulatory compliance.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Not every AWS service is available in every Region; service availability varies depending on customer demand and regional rollout timelines.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Regions host virtually all AWS compute, database, networking, and storage services, not just static website hosting.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Regions are independent and isolated by design; data is not automatically replicated across all Regions unless explicitly configured by the customer.

---

<a id="q-5"></a>

### Question 5

**Topic:** `Cloud computing benefits` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `2b87b7f1-a141-4bee-bf68-9332ac4feaf1`

> **Scenario:**  
> A startup moves its application from self-managed servers to AWS. Which benefit most directly reduces the need to forecast hardware capacity months in advance?

#### Options
- **A.** Elasticity **[CORRECT]**
- **B.** Global reach
- **C.** Encryption by default
- **D.** Physical server ownership

**Correct Answer:** `A`

> **Summary:** Elasticity is the ability to acquire resources as you need them and release them when no longer needed, eliminating the need to forecast capacity months in advance.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Elasticity allows organizations to scale resources up or down dynamically in response to demand, completely removing the requirement to predict hardware capacity months ahead.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Global reach allows applications to be deployed across multiple worldwide locations in minutes, but does not specifically solve capacity forecasting.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Encryption by default is a data security feature, not a cloud capacity management principle.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Physical server ownership is an on-premises model that requires manual forecasting and upfront capital expenditures; cloud computing replaces this model.

---

<a id="q-6"></a>

### Question 6

**Topic:** `Cloud computing benefits` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `737084ee-ea49-4642-8b83-c412d2432d5a`

> **Scenario:**  
> Which cloud benefit allows an organization to replace a large upfront hardware purchase with expenses that generally vary with usage?

#### Options
- **A.** Variable expense **[CORRECT]**
- **B.** Fault isolation
- **C.** Data sovereignty
- **D.** Manual scaling

**Correct Answer:** `A`

> **Summary:** Cloud computing allows businesses to trade fixed capital expense (CapEx) for variable operating expense (OpEx), paying only for the IT resources consumed.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Variable expense allows businesses to replace massive upfront capital expenditures (CapEx) for physical hardware with operational expenses (OpEx) that scale with actual usage.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Fault isolation prevents issues in one component or zone from impacting others, but relates to architectural reliability rather than financial expense.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Data sovereignty refers to compliance with local laws regarding data residency and storage location, not cost models.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Manual scaling requires human intervention to adjust resources and does not inherently define the financial shift to variable cost.

---

<a id="q-7"></a>

### Question 7

**Topic:** `Cloud computing benefits` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `16f3b386-fa8f-4d49-bd1f-de2d17e962d5`

> **Scenario:**  
> An application experiences unpredictable traffic spikes. Which cloud capability allows it to add resources during spikes and remove them afterward?

#### Options
- **A.** Elasticity **[CORRECT]**
- **B.** Durability
- **C.** Data residency
- **D.** Hardware procurement

**Correct Answer:** `A`

> **Summary:** Elasticity allows systems to automatically adapt capacity to match volatile traffic spikes without human intervention.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Elasticity is the cloud capability that automatically provisions additional capacity during traffic spikes and terminates idle capacity when demand subsides, optimizing cost and performance.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Durability measures the probability that stored data will remain intact over time without corruption or loss (e.g., S3 99.999999999% durability).

- **Option C:** ❌ **Why it is INCORRECT:**  
  Data residency refers to the physical or geographic location where customer data resides for compliance and legal reasons.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Hardware procurement is a legacy on-premises process involving purchasing and installing physical servers, which cannot respond to sudden traffic spikes.

---

<a id="q-8"></a>

### Question 8

**Topic:** `Cloud computing benefits` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `cdb9a99b-f7a3-4481-b032-2536bebf1a87`

> **Scenario *(Select TWO)*:**  
> Which are common benefits of cloud computing? (Select TWO.)

#### Options
- **A.** Rapid global deployment **[CORRECT]**
- **B.** Reduced need to manage physical infrastructure **[CORRECT]**
- **C.** Guaranteed zero downtime
- **D.** Elimination of all security responsibilities
- **E.** Unlimited free capacity

**Correct Answer:** `A, B`

> **Summary:** Two fundamental benefits of cloud computing are deploying globally in minutes and shifting the burden of managing physical infrastructure to the cloud provider.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Rapid global deployment allows organizations to deploy applications in multiple AWS Regions around the world with just a few clicks or API calls.

- **Option B:** ✅ **Why it is CORRECT:**  
  Reduced need to manage physical infrastructure eliminates the heavy lifting of racking, stacking, powering, and cooling physical hardware in data centers.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Guaranteed zero downtime is impossible in any IT environment; AWS provides high availability architectures but never guarantees 100% zero downtime.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Under the AWS Shared Responsibility Model, customers remain responsible for security 'in' the cloud (data, IAM, guest OS, network configurations).

- **Option E:** ❌ **Why it is INCORRECT:**  
  Cloud capacity is vast and elastic, but it is not completely unlimited nor is it free; usage incurs metered costs.

---

<a id="q-9"></a>

### Question 9

**Topic:** `AWS shared responsibility model` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `11435e9b-8626-4f3e-9b61-edcd0c178d65`

> **Scenario:**  
> Under the AWS shared responsibility model, which task is generally the customer's responsibility for an Amazon EC2 instance?

#### Options
- **A.** Patching the guest operating system **[CORRECT]**
- **B.** Replacing failed physical disks
- **C.** Securing AWS data centers
- **D.** Maintaining the hypervisor

**Correct Answer:** `A`

> **Summary:** In Infrastructure as a Service (IaaS) like Amazon EC2, customers are responsible for managing the guest operating system, including security updates and patches.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Patching and updating the guest operating system (Linux or Windows) on Amazon EC2 instances is strictly the customer's responsibility under the Shared Responsibility Model.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Replacing failed physical storage drives and hardware components is AWS's responsibility as part of security 'of' the cloud.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Securing physical data centers, facilities, perimeters, and environmental controls is entirely managed by AWS.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Maintaining and patching the virtualization hypervisor layer (such as AWS Nitro) is the responsibility of AWS.

---

<a id="q-10"></a>

### Question 10

**Topic:** `AWS shared responsibility model` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `bbff97a4-1a33-48c7-9f8b-1bfb60b72978`

> **Scenario:**  
> Which security task remains the customer's responsibility when using Amazon S3?

#### Options
- **A.** Configuring bucket policies **[CORRECT]**
- **B.** Maintaining S3 storage hardware
- **C.** Patching the S3 service
- **D.** Guarding AWS facilities

**Correct Answer:** `A`

> **Summary:** For managed object storage like Amazon S3, AWS manages the underlying infrastructure, while customers are responsible for configuring access controls and bucket policies.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Configuring S3 bucket policies, access control lists (ACLs), Block Public Access settings, and IAM permissions is the customer's responsibility to protect their data.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Maintaining physical S3 storage drives, servers, and multi-facility redundancy is AWS's responsibility.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Patching the underlying S3 service software, endpoints, and storage operating systems is managed by AWS.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Guarding physical AWS data center facilities and controlling physical entry is strictly handled by AWS.

---

<a id="q-11"></a>

### Question 11

**Topic:** `AWS shared responsibility model` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `ddab2029-db5c-48cd-a852-132441a36f6e`

> **Scenario:**  
> A company uses Amazon RDS and wants to understand which task it still owns. Which task is customer responsibility?

#### Options
- **A.** Selecting database security groups **[CORRECT]**
- **B.** Replacing failed database servers
- **C.** Applying patches to the managed database engine binaries
- **D.** Operating the underlying hypervisor

**Correct Answer:** `A`

> **Summary:** In Amazon RDS (a managed PaaS), AWS manages the OS and database engine patching, while the customer configures network firewall rules (database security groups) and user permissions.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Configuring database security groups, VPC subnets, and database-level user authentication remains the customer's responsibility.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Replacing failed physical database host servers and hardware is automatically handled by AWS.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Applying routine security patches and maintenance updates to the managed database engine binaries is automated and managed by AWS.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Operating the virtualization hypervisor layer running the RDS database instance is managed by AWS.

---

<a id="q-12"></a>

### Question 12

**Topic:** `AWS shared responsibility model` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `965fb1b5-f0ce-491b-8514-7167cbbb1ec2`

> **Scenario *(Select TWO)*:**  
> Which responsibilities remain with the customer in AWS? (Select TWO.)

#### Options
- **A.** Managing IAM permissions **[CORRECT]**
- **B.** Classifying and protecting application data **[CORRECT]**
- **C.** Securing AWS data center buildings
- **D.** Replacing failed AWS networking hardware
- **E.** Maintaining the AWS hypervisor

**Correct Answer:** `A, B`

> **Summary:** Under the AWS Shared Responsibility Model, the customer is always responsible for IAM access management and data classification/protection.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Managing IAM permissions, user credentials, access keys, and role-based policies is solely the customer's responsibility.

- **Option B:** ✅ **Why it is CORRECT:**  
  Classifying, encrypting, and protecting application data (both at rest and in transit) is the responsibility of the customer.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Securing physical AWS data center buildings and facilities is the sole responsibility of AWS.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Replacing failed physical networking hardware (switches, routers, optical fibers) is managed by AWS.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Maintaining and securing the virtualization hypervisor is the responsibility of AWS.

---

<a id="q-13"></a>

### Question 13

**Topic:** `IAM users, groups, roles, and policies` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `fa2c882b-dedb-4b57-9bbf-ebbe665ae407`

> **Scenario:**  
> What is the recommended way for an application running on Amazon EC2 to obtain temporary permissions to access an S3 bucket?

#### Options
- **A.** Attach an IAM role to the EC2 instance **[CORRECT]**
- **B.** Create a long-term access key in the source code
- **C.** Share the root user credentials
- **D.** Place credentials in a public S3 object

**Correct Answer:** `A`

> **Summary:** Using IAM roles for EC2 instances allows applications to securely obtain temporary, automatically rotated AWS credentials without hardcoding secrets.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Attaching an IAM role (via an EC2 instance profile) provides temporary security credentials that are automatically rotated by AWS STS, eliminating hardcoded keys.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Embedding long-term IAM access keys directly in source code or configuration files is a dangerous security risk and violates AWS security best practices.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Sharing or using AWS account root user credentials for applications is an extreme security risk; root access should never be used for operational tasks.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Placing credentials in a public S3 bucket exposes AWS credentials to the entire internet, resulting in immediate account compromise.

---

<a id="q-14"></a>

### Question 14

**Topic:** `IAM users, groups, roles, and policies` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `52b329a8-39a1-4c11-ae97-685d22852355`

> **Scenario:**  
> A company wants to grant the same read-only permissions to 40 developers. Which IAM feature is most appropriate?

#### Options
- **A.** IAM group **[CORRECT]**
- **B.** IAM access key
- **C.** AWS account root user
- **D.** Security group

**Correct Answer:** `A`

> **Summary:** An IAM group allows administrators to assign permissions to multiple IAM users simultaneously, simplifying credential and permission lifecycle management.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  An IAM group is a collection of IAM users. Attaching a read-only policy to the group automatically grants those permissions to all 40 developer members.

- **Option B:** ❌ **Why it is INCORRECT:**  
  An IAM access key consists of an Access Key ID and Secret Access Key used for programmatic API authentication, not for grouping permission sets.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The AWS account root user possesses unrestricted administrative privileges across all account resources and should never be used for group permissions.

- **Option D:** ❌ **Why it is INCORRECT:**  
  A security group is a network-level virtual firewall for EC2 instances, not an identity and access management construct.

---

<a id="q-15"></a>

### Question 15

**Topic:** `IAM users, groups, roles, and policies` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `d95d6154-c6bd-42a3-900d-b6332b76554e`

> **Scenario:**  
> An administrator must permit a backup service to delete objects only from one S3 bucket. Which IAM policy design best follows least privilege?

#### Options
- **A.** Allow s3:DeleteObject only for the specified bucket ARN **[CORRECT]**
- **B.** Allow s3:* on all resources
- **C.** Allow AdministratorAccess to the service
- **D.** Allow delete access to every bucket in the account

**Correct Answer:** `A`

> **Summary:** The principle of least privilege states that identities should only be granted the exact permissions needed on the exact resources required.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Specifying the `s3:DeleteObject` action scoped specifically to the target bucket ARN adheres strictly to the principle of least privilege.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Granting `s3:*` on all resources grants broad destructive permissions across all S3 buckets in the account, violating least privilege.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Granting full `AdministratorAccess` provides complete control over all AWS services and resources, creating a massive security vulnerability.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Allowing delete access to every bucket in the account creates unacceptable risk of accidental or malicious data loss across unrelated workloads.

---

<a id="q-16"></a>

### Question 16

**Topic:** `IAM users, groups, roles, and policies` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `4bfcba43-be2a-48cd-a64f-f7babb7e45fe`

> **Scenario *(Select TWO)*:**  
> Which IAM practices improve account security? (Select TWO.)

#### Options
- **A.** Enable multi-factor authentication for privileged users **[CORRECT]**
- **B.** Use roles for workloads instead of embedded long-term keys **[CORRECT]**
- **C.** Use the root user for daily administration
- **D.** Grant administrator permissions to every developer
- **E.** Reuse one access key across all applications

**Correct Answer:** `A, B`

> **Summary:** Enabling Multi-Factor Authentication (MFA) and using IAM roles for workloads are two critical AWS Identity and Access Management security best practices.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Enabling MFA requires users to provide a second authentication factor, safeguarding privileged accounts against credential theft or compromise.

- **Option B:** ✅ **Why it is CORRECT:**  
  Using IAM roles grants workloads short-term, temporary credentials, eliminating the need to store static, long-term access keys.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Using the root user for daily administrative tasks is strongly discouraged; AWS recommends locking away root credentials and creating administrative IAM users.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Granting administrator permissions to every developer violates the core security principle of least privilege.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Sharing or reusing a single access key across multiple applications eliminates auditability and expands the blast radius if the key is leaked.

---

<a id="q-17"></a>

### Question 17

**Topic:** `Amazon EC2` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `dbae6b2c-3a46-4fae-a716-2d5422779137`

> **Scenario:**  
> A workload requires a predictable amount of compute capacity continuously for three years. Which EC2 purchasing option can provide a discount in exchange for a commitment?

#### Options
- **A.** Reserved Instances **[CORRECT]**
- **B.** On-Demand Instances
- **C.** Spot Instances
- **D.** Dedicated Hosts without a commitment

**Correct Answer:** `A`

> **Summary:** Reserved Instances (RIs) and Compute Savings Plans provide significant discounts (up to 72%) in exchange for a committed steady-state usage term of 1 or 3 years.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Reserved Instances provide substantial cost savings for predictable, steady-state workloads running continuously over a 1-year or 3-year commitment period.

- **Option B:** ❌ **Why it is INCORRECT:**  
  On-Demand Instances provide maximum flexibility with no commitment, but carry the highest hourly cost for steady, continuous workloads.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Spot Instances can be reclaimed by AWS with a 2-minute warning and are unsuitable for continuous, interruption-sensitive production applications.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Dedicated Hosts without commitments incur high hourly rates and are primarily intended for dedicated hardware licensing requirements, not standard cost reduction.

---

<a id="q-18"></a>

### Question 18

**Topic:** `Amazon EC2` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `34daf697-f4fa-436e-a3f4-d4b4ccd9054d`

> **Scenario:**  
> A batch processing application can tolerate interruptions and must minimize compute cost. Which EC2 option is most suitable?

#### Options
- **A.** Spot Instances **[CORRECT]**
- **B.** Dedicated Hosts
- **C.** On-Demand Instances only
- **D.** Reserved Instances with no workload flexibility

**Correct Answer:** `A`

> **Summary:** Spot Instances allow customers to take advantage of unused EC2 capacity at steep discounts (up to 90% off On-Demand) for workloads that can tolerate interruptions.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Spot Instances offer up to 90% discount compared to On-Demand pricing, making them ideal for fault-tolerant, stateless batch processing jobs.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Dedicated Hosts provide physical server isolation and are the most expensive EC2 hosting option, running counter to cost minimization.

- **Option C:** ❌ **Why it is INCORRECT:**  
  On-Demand Instances charge full standard rates and do not take advantage of spare capacity discounts for interruptible workloads.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Reserved Instances require long-term financial commitments (1 or 3 years) and lack the flexibility of dynamic spot batch capacity.

---

<a id="q-19"></a>

### Question 19

**Topic:** `Amazon EC2` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `a48f7b0d-8f99-44d4-8b4e-ebf7c3493eec`

> **Scenario:**  
> Which EC2 feature allows instances to be launched from a predefined template containing an AMI, instance type, and networking settings?

#### Options
- **A.** Launch template **[CORRECT]**
- **B.** Elastic IP address
- **C.** Placement group
- **D.** Security group

**Correct Answer:** `A`

> **Summary:** An EC2 Launch Template contains the instance configuration parameters (AMI ID, instance type, key pair, security groups, block device mappings, user data) to launch instances.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  A Launch Template specifies instance configuration information, allowing consistent, versioned deployments for manual launches and Auto Scaling groups.

- **Option B:** ❌ **Why it is INCORRECT:**  
  An Elastic IP address is a static, public IPv4 address designed for dynamic cloud computing, not a template for provisioning instances.

- **Option C:** ❌ **Why it is INCORRECT:**  
  A placement group determines how EC2 instances are physically arranged within underlying hardware (cluster, spread, partition) to optimize networking or fault isolation.

- **Option D:** ❌ **Why it is INCORRECT:**  
  A security group controls inbound and outbound network traffic for instances, but does not define instance launch parameters.

---

<a id="q-20"></a>

### Question 20

**Topic:** `Amazon EC2` | **Difficulty:** `Hard` | **Type:** `Multiple`  
**Question ID:** `79081c8c-3f02-4aa9-949a-d2d86977a4d5`

> **Scenario *(Select TWO)*:**  
> Which statements about EC2 security groups are correct? (Select TWO.)

#### Options
- **A.** They act as stateful virtual firewalls. **[CORRECT]**
- **B.** They can control inbound and outbound instance traffic. **[CORRECT]**
- **C.** They support explicit deny rules that override allows.
- **D.** They are attached to an entire AWS Region.
- **E.** They replace the need for IAM permissions.

**Correct Answer:** `A, B`

> **Summary:** Security groups operate at the EC2 instance level as stateful virtual firewalls controlling inbound and outbound network traffic.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Security groups are stateful: if an inbound request is permitted, return outbound traffic is automatically allowed regardless of outbound rules.

- **Option B:** ✅ **Why it is CORRECT:**  
  Security groups can specify distinct rules to evaluate both inbound (ingress) and outbound (egress) network connections at the virtual network interface level.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Security groups only support allow rules; all traffic not explicitly permitted is denied by default, with no explicit 'deny' rule syntax (unlike Network ACLs).

- **Option D:** ❌ **Why it is INCORRECT:**  
  Security groups are associated with specific elastic network interfaces (ENIs) within a VPC, not an entire AWS Region.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Security groups control network layer access (ports and IP protocols) and do not replace IAM identity and access permissions.

---

<a id="q-21"></a>

### Question 21

**Topic:** `AWS Lambda` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `91f9cb17-b3e8-43e3-9a79-949320ce3dfb`

> **Scenario:**  
> A developer needs to run short-lived code whenever a new object is uploaded to an S3 bucket. Which service is best suited?

#### Options
- **A.** AWS Lambda **[CORRECT]**
- **B.** Amazon EC2 Dedicated Host
- **C.** Amazon RDS
- **D.** AWS Direct Connect

**Correct Answer:** `A`

> **Summary:** AWS Lambda is a serverless compute service that runs code in response to events (such as S3 object creation) and automatically manages the underlying compute resources.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Lambda allows developers to run short-lived, event-driven functions automatically triggered by S3 `s3:ObjectCreated:*` events without managing servers.

- **Option B:** ❌ **Why it is INCORRECT:**  
  EC2 Dedicated Hosts require managing physical servers and maintaining continuous operating costs, which is unsuitable for event-driven short-lived code.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon RDS is a managed relational database service, not a serverless compute execution environment.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Direct Connect establishes dedicated private network connections between on-premises data centers and AWS, not code execution.

---

<a id="q-22"></a>

### Question 22

**Topic:** `AWS Lambda` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `7d8fb868-bab3-4ae5-a472-d51178a4e2f9`

> **Scenario:**  
> A Lambda function must access DynamoDB without storing credentials in code. What should be configured?

#### Options
- **A.** An execution role with appropriate DynamoDB permissions **[CORRECT]**
- **B.** A hard-coded root access key
- **C.** A public subnet with no route table
- **D.** An S3 bucket ACL

**Correct Answer:** `A`

> **Summary:** AWS Lambda uses an execution role (an IAM role assumed by the service) to securely grant the function permissions to access other AWS services like Amazon DynamoDB.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Attaching an IAM execution role with DynamoDB read/write permissions allows Lambda to securely assume temporary credentials to interact with DynamoDB.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Hardcoding root access keys in function code is a severe security violation that risks total account takeover.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Placing Lambda in a public subnet without route tables breaks network connectivity and does not grant service authorization.

- **Option D:** ❌ **Why it is INCORRECT:**  
  S3 bucket ACLs manage legacy object storage permissions on S3 buckets and have no effect on DynamoDB database access.

---

<a id="q-23"></a>

### Question 23

**Topic:** `AWS Lambda` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `82b5d5aa-d156-4a67-80f6-11ef9d6f78bd`

> **Scenario:**  
> Which factor most directly affects Lambda pricing for a function invocation?

#### Options
- **A.** Number of requests and execution duration **[CORRECT]**
- **B.** Number of IAM users in the account
- **C.** Number of VPC route tables
- **D.** Amount of data stored in Glacier only

**Correct Answer:** `A`

> **Summary:** AWS Lambda pricing is based on the number of requests (invocations) and the execution duration billed in milliseconds, proportional to allocated memory.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Lambda charges are calculated primarily from the total number of function invocations and the execution duration (measured in milliseconds) based on allocated memory.

- **Option B:** ❌ **Why it is INCORRECT:**  
  The number of IAM users in an AWS account is an identity metric that is completely free of charge and does not influence Lambda billing.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The count of VPC route tables is a network routing configuration that has no direct bearing on Lambda execution fees.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Data stored in Amazon S3 Glacier is billed under S3 archive storage pricing, entirely separate from Lambda compute invocations.

---

<a id="q-24"></a>

### Question 24

**Topic:** `AWS Lambda` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `54121e98-afa8-4841-bb64-d62c3dd42d7f`

> **Scenario *(Select TWO)*:**  
> Which are characteristics of AWS Lambda? (Select TWO.)

#### Options
- **A.** AWS manages the underlying servers. **[CORRECT]**
- **B.** Functions can be invoked by events or direct API calls. **[CORRECT]**
- **C.** Customers must choose and patch an operating system.
- **D.** Functions run indefinitely without execution limits.
- **E.** Every function requires a permanently running EC2 instance.

**Correct Answer:** `A, B`

> **Summary:** AWS Lambda is a fully managed serverless compute service where AWS handles server infrastructure and functions are triggered by events or direct API calls.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS manages all underlying infrastructure, server provisioning, operating system maintenance, capacity scaling, and high availability.

- **Option B:** ✅ **Why it is CORRECT:**  
  Lambda functions can be triggered automatically by events from over 200 AWS services (e.g., S3, DynamoDB, SQS) or invoked directly via API Gateway and SDK calls.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Customers do not manage, select, or patch the underlying operating system in AWS Lambda; it is managed entirely by AWS.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Lambda functions have a hard maximum execution timeout of 15 minutes (900 seconds) and cannot run indefinitely.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Lambda is serverless and executes in temporary, managed micro-containers; it does not require running permanent EC2 instances.

---

<a id="q-25"></a>

### Question 25

**Topic:** `Amazon S3` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `4c67bbe0-e66b-4428-a9d7-ccf4106a5019`

> **Scenario:**  
> A company needs highly durable object storage for user-uploaded images that are accessed frequently. Which S3 storage class is a reasonable default?

#### Options
- **A.** S3 Standard **[CORRECT]**
- **B.** S3 Glacier Deep Archive
- **C.** S3 One Zone-IA
- **D.** S3 Glacier Flexible Retrieval only

**Correct Answer:** `A`

> **Summary:** Amazon S3 Standard offers high durability, high availability, and low latency for frequently accessed data, storing objects redundantly across multiple Availability Zones.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  S3 Standard is designed for 99.999999999% (11 9s) of data durability and high throughput/low latency access across at least three Availability Zones.

- **Option B:** ❌ **Why it is INCORRECT:**  
  S3 Glacier Deep Archive is designed for long-term cold archiving with retrieval times ranging from 12 to 48 hours, making it unsuitable for active image viewing.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 One Zone-IA stores data in only one Availability Zone and lacks multi-AZ redundancy, risking permanent data loss if that AZ suffers a disaster.

- **Option D:** ❌ **Why it is INCORRECT:**  
  S3 Glacier Flexible Retrieval is an archival storage tier with retrieval times of minutes to hours, unsuitable for immediate image retrieval.

---

<a id="q-26"></a>

### Question 26

**Topic:** `Amazon S3` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `51d2b355-17a9-41bf-8a34-4eee7961760f`

> **Scenario:**  
> Which S3 feature helps prevent accidental deletion or overwriting of object versions?

#### Options
- **A.** S3 Versioning **[CORRECT]**
- **B.** S3 Transfer Acceleration only
- **C.** S3 Select
- **D.** S3 Batch Operations only

**Correct Answer:** `A`

> **Summary:** Amazon S3 Versioning preserves, retrieves, and restores every version of every object stored in an S3 bucket, protecting against accidental deletes or overwrites.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  S3 Versioning keeps multiple versions of an object in the same bucket, allowing users to easily recover from unintended overwrites or accidental deletions.

- **Option B:** ❌ **Why it is INCORRECT:**  
  S3 Transfer Acceleration speeds up uploads and downloads over long distances using Amazon CloudFront's globally distributed edge locations.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 Select allows applications to retrieve a subset of data from an object using simple SQL expressions, but does not prevent accidental deletion.

- **Option D:** ❌ **Why it is INCORRECT:**  
  S3 Batch Operations performs large-scale batch actions across billions of S3 objects, but does not provide object version protection.

---

<a id="q-27"></a>

### Question 27

**Topic:** `Amazon S3` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `b63b57cb-db2b-43b6-a6e8-b7a17c6dd90e`

> **Scenario:**  
> A company must ensure that objects uploaded to an S3 bucket are encrypted using customer-controlled keys. Which option best meets this requirement?

#### Options
- **A.** SSE-KMS using a customer-managed AWS KMS key **[CORRECT]**
- **B.** Public-read bucket ACLs
- **C.** S3 Transfer Acceleration
- **D.** An EC2 security group

**Correct Answer:** `A`

> **Summary:** Server-Side Encryption with AWS KMS (SSE-KMS) allows customers to enforce encryption using customer-managed keys (CMKs) with full audit trails via AWS CloudTrail.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  SSE-KMS encrypts objects at rest using AWS Key Management Service keys, providing customer control over key rotation and audit logging of key usage.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Public-read bucket ACLs make object contents publicly accessible to anyone on the internet and provide zero encryption.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 Transfer Acceleration optimizes network transport speed via edge locations, but does not provide cryptographic at-rest storage encryption.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EC2 security groups are network packet filters for virtual servers and cannot manage cryptographic keys or S3 at-rest encryption.

---

<a id="q-28"></a>

### Question 28

**Topic:** `Amazon S3` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `d33ee789-0f56-4714-8ba3-39e29fd64546`

> **Scenario *(Select TWO)*:**  
> Which S3 features can help protect or manage stored objects? (Select TWO.)

#### Options
- **A.** Lifecycle rules **[CORRECT]**
- **B.** Versioning **[CORRECT]**
- **C.** EC2 placement groups
- **D.** RDS read replicas
- **E.** VPC peering

**Correct Answer:** `A, B`

> **Summary:** S3 Lifecycle rules and S3 Versioning are two core Amazon S3 features designed to manage object retention, transitions, and accidental loss prevention.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  S3 Lifecycle rules define automated actions to transition objects to cheaper storage classes (e.g., Standard to Glacier) or expire them after set retention periods.

- **Option B:** ✅ **Why it is CORRECT:**  
  S3 Versioning protects objects against accidental overwrites and deletions by retaining historical versions and inserting delete markers.

- **Option C:** ❌ **Why it is INCORRECT:**  
  EC2 placement groups configure physical instance placement on host hardware to reduce network latency or isolate faults.

- **Option D:** ❌ **Why it is INCORRECT:**  
  RDS read replicas provide read scalability for relational databases and have no function in managing Amazon S3 objects.

- **Option E:** ❌ **Why it is INCORRECT:**  
  VPC peering connects two virtual private clouds to route network traffic between them, unrelated to S3 object management.

---

<a id="q-29"></a>

### Question 29

**Topic:** `Amazon EBS` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `9c2dcf85-a3ac-4721-ae76-796c1874d411`

> **Scenario:**  
> An EC2 instance requires persistent block storage that remains available independently of the instance lifecycle. Which service should be used?

#### Options
- **A.** Amazon EBS **[CORRECT]**
- **B.** Instance store only
- **C.** Amazon CloudFront
- **D.** Amazon Route 53

**Correct Answer:** `A`

> **Summary:** Amazon Elastic Block Store (Amazon EBS) provides durable, persistent block-level storage volumes for use with EC2 instances that persist independently of instance lifecycles.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon EBS provides persistent block storage volumes that retain data even when the attached EC2 instance is stopped or terminated.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Instance store is ephemeral temporary storage physically attached to the host computer; all data is lost when the instance is stopped or terminated.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon CloudFront is a Content Delivery Network for edge caching, not local block storage for operating systems.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon Route 53 is a cloud Domain Name System (DNS) web service, not a storage volume service.

---

<a id="q-30"></a>

### Question 30

**Topic:** `Amazon EBS` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `7bcf2540-8789-42f3-b409-ec9c6a0d1b8d`

> **Scenario:**  
> A database workload requires consistently high IOPS and low-latency block storage. Which EBS volume type is generally most appropriate?

#### Options
- **A.** Provisioned IOPS SSD **[CORRECT]**
- **B.** Cold HDD
- **C.** Throughput Optimized HDD
- **D.** Magnetic standard volume

**Correct Answer:** `A`

> **Summary:** Provisioned IOPS SSD (io2 and io1) volumes are designed for I/O-intensive database workloads requiring consistent, low-latency, high-performance IOPS.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Provisioned IOPS SSD volumes deliver predictable, high-performance IOPS and sub-millisecond latencies for mission-critical transactional databases.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Cold HDD (sc1) is a low-cost magnetic storage tier designed for infrequently accessed sequential workloads, not high-IOPS random databases.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Throughput Optimized HDD (st1) is optimized for high-throughput sequential data streams (like big data and log processing), not low-latency random IOPS.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Magnetic standard volumes are previous-generation low-performance drives unsuitable for enterprise database workloads.

---

<a id="q-31"></a>

### Question 31

**Topic:** `Amazon EBS` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `1bdda4b2-b44e-4ba9-a148-7da6dec6e0e6`

> **Scenario:**  
> A company wants to create a point-in-time backup of an EBS volume. Which capability should it use?

#### Options
- **A.** EBS snapshot **[CORRECT]**
- **B.** Security group rule
- **C.** Elastic IP reassociation
- **D.** EC2 placement group

**Correct Answer:** `A`

> **Summary:** An Amazon EBS snapshot is a point-in-time, incremental backup of an EBS volume stored redundantly in Amazon S3.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  EBS snapshots capture incremental point-in-time block-level backups of an EBS volume, which can be used to restore new volumes at any time.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Security group rules specify inbound and outbound network traffic permissions and cannot perform storage backups.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Elastic IP reassociation moves a static public IP address to a different network interface and has no backup capability.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EC2 placement groups dictate physical instance hardware placement within an AZ and do not back up storage data.

---

<a id="q-32"></a>

### Question 32

**Topic:** `Amazon EBS` | **Difficulty:** `Hard` | **Type:** `Multiple`  
**Question ID:** `9962d629-35f7-4356-8ef7-afd3a74e0c05`

> **Scenario *(Select TWO)*:**  
> Which statements about EBS are correct? (Select TWO.)

#### Options
- **A.** An EBS volume is normally associated with a specific Availability Zone. **[CORRECT]**
- **B.** EBS snapshots can be used to create new volumes. **[CORRECT]**
- **C.** EBS is an object storage service for arbitrary HTTP objects.
- **D.** EBS volumes are automatically accessible from every Region.
- **E.** Deleting an EC2 instance always deletes every attached EBS volume.

**Correct Answer:** `A, B`

> **Summary:** EBS volumes are placed in a specific Availability Zone for high-speed attachment, and EBS snapshots can be used to instantiate new volumes across AZs or Regions.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  An EBS volume is physically bound to a single Availability Zone in which it was created, allowing low-latency attachment to EC2 instances in that same AZ.

- **Option B:** ✅ **Why it is CORRECT:**  
  EBS snapshots stored in Amazon S3 can be used to create identical new EBS volumes in any Availability Zone within the Region or copied across Regions.

- **Option C:** ❌ **Why it is INCORRECT:**  
  EBS is a block storage service for file systems and operating systems; Amazon S3 is the object storage service accessed via HTTP.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EBS volumes cannot be accessed across different AWS Regions directly; an instance can only attach an EBS volume in its own Availability Zone.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Non-root EBS volumes persist by default upon instance termination, and the `DeleteOnTermination` flag can be set to false on root volumes.

---

<a id="q-33"></a>

### Question 33

**Topic:** `Amazon RDS and DynamoDB` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `f0b86133-395a-4966-8521-a56fddd7d3c7`

> **Scenario:**  
> A company needs a managed relational database with automated backups, patching options, and support for multiple database engines. Which service should it choose?

#### Options
- **A.** Amazon RDS **[CORRECT]**
- **B.** Amazon DynamoDB
- **C.** Amazon S3
- **D.** Amazon EBS

**Correct Answer:** `A`

> **Summary:** Amazon Relational Database Service (Amazon RDS) is a managed relational database service supporting engines like PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon RDS automates relational database management tasks, including automated backups, hardware provisioning, database engine patching, and Multi-AZ failover.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon DynamoDB is a serverless key-value and document NoSQL database, not a traditional relational database engine.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon S3 is an object storage service designed for storing unstructured files, not a transactional relational database.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS IAM manages user authentication and authorization across AWS services, not database data storage.

---

<a id="q-34"></a>

### Question 34

**Topic:** `Amazon RDS and DynamoDB` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `92dd23ef-3f70-4f15-8067-54975a996b00`

> **Scenario:**  
> An application needs a serverless NoSQL database with single-digit millisecond performance and automatic scaling. Which service is most suitable?

#### Options
- **A.** Amazon DynamoDB **[CORRECT]**
- **B.** Amazon RDS for PostgreSQL
- **C.** Amazon EBS
- **D.** Amazon Redshift only

**Correct Answer:** `A`

> **Summary:** Amazon DynamoDB is a fully managed, serverless NoSQL database service that provides consistent single-digit millisecond performance at any scale.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon DynamoDB is a serverless, non-relational (NoSQL) database that automatically scales throughput and storage while delivering sub-10ms response times.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon RDS is a managed relational database service that requires instance sizing and relational table schema definitions.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon Redshift is a managed columnar data warehouse optimized for complex OLAP analytics queries, not fast single-digit millisecond NoSQL operations.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon Aurora is a high-performance relational database engine compatible with MySQL and PostgreSQL, not a NoSQL database.

---

<a id="q-35"></a>

### Question 35

**Topic:** `Amazon RDS and DynamoDB` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `b2be8e8d-4ce1-4d68-a9e5-c1f38d6c959b`

> **Scenario:**  
> A database must remain available if one Availability Zone fails. Which Amazon RDS capability is designed for this requirement?

#### Options
- **A.** Multi-AZ deployment **[CORRECT]**
- **B.** Read-only IAM user
- **C.** S3 lifecycle policy
- **D.** DynamoDB partition key only

**Correct Answer:** `A`

> **Summary:** Amazon RDS Multi-AZ deployments provision and maintain a synchronous standby replica in a different Availability Zone to provide high availability and automated failover.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  RDS Multi-AZ deployments synchronously replicate data to a standby instance in a different Availability Zone, providing automated failover without data loss if the primary AZ fails.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Read replicas asynchronously replicate data to handle read-heavy queries, but standard read replicas require manual promotion during failover.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Single-AZ deployments host the database in a single data center; if that AZ experiences an outage, the database becomes unavailable.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EC2 placement groups configure host hardware proximity within a single AZ and do not provide cross-AZ database failover.

---

<a id="q-36"></a>

### Question 36

**Topic:** `Amazon RDS and DynamoDB` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `c53df76c-88f2-4960-b176-70d42a8b9d77`

> **Scenario *(Select TWO)*:**  
> Which statements correctly compare Amazon RDS and DynamoDB? (Select TWO.)

#### Options
- **A.** RDS is a managed relational database service. **[CORRECT]**
- **B.** DynamoDB is a managed NoSQL database service. **[CORRECT]**
- **C.** RDS stores data only as S3 objects.
- **D.** DynamoDB requires customers to manage database servers.
- **E.** Neither service supports automated scaling under any configuration.

**Correct Answer:** `A, B`

> **Summary:** Amazon RDS provides managed relational databases (SQL), whereas Amazon DynamoDB provides a fully managed, serverless non-relational database (NoSQL).

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon RDS provides managed relational database engines (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server) with structured SQL schemas.

- **Option B:** ✅ **Why it is CORRECT:**  
  Amazon DynamoDB provides a managed, serverless NoSQL key-value and document database designed for high scalability and flexible schemas.

- **Option C:** ❌ **Why it is INCORRECT:**  
  RDS stores structured table data on persistent block storage (EBS/optimized storage volumes), not as individual S3 objects.

- **Option D:** ❌ **Why it is INCORRECT:**  
  DynamoDB is fully serverless; customers never configure, provision, patch, or manage underlying operating systems or database servers.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Both RDS (via storage autoscaling and Aurora auto-scaling) and DynamoDB (via auto-scaling and on-demand capacity mode) support automated scaling.

---

<a id="q-37"></a>

### Question 37

**Topic:** `Amazon VPC` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `e4d4ea5d-c733-46b8-9d88-82a5ff6cd77c`

> **Scenario:**  
> A public web application needs isolated networking, public subnets for load balancers, and private subnets for application servers. Which AWS service provides this logical network boundary?

#### Options
- **A.** Amazon VPC **[CORRECT]**
- **B.** Amazon CloudFront
- **C.** AWS IAM
- **D.** Amazon S3

**Correct Answer:** `A`

> **Summary:** Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined with complete network isolation.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon VPC allows customers to provision a logically isolated section of the AWS Cloud, creating subnets, routing tables, and network gateways.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS Artifact is a portal providing access to AWS compliance reports and agreements, not a networking service.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Organizations manages multi-account governance and billing, not virtual network IP topology.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon CloudFront is a global content delivery network, not an isolated private virtual network.

---

<a id="q-38"></a>

### Question 38

**Topic:** `Amazon VPC` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `c7574a6c-74c0-4449-a1e4-de23c5f5258e`

> **Scenario:**  
> Instances in a private subnet need outbound internet access for software updates but must not accept unsolicited inbound internet connections. Which component is appropriate?

#### Options
- **A.** NAT gateway in a public subnet **[CORRECT]**
- **B.** Internet gateway directly on the private subnet
- **C.** Public IP on every private instance
- **D.** VPC peering connection to an unrelated VPC

**Correct Answer:** `A`

> **Summary:** A NAT gateway enables instances in a private subnet to connect to the internet or other AWS services, while preventing the internet from initiating an inbound connection.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  A NAT gateway deployed in a public subnet allows private subnet instances to initiate outbound connections for patches and updates while blocking inbound internet traffic.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Assigning public IP addresses directly to private instances exposes them directly to inbound internet traffic, violating private network isolation.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Placing private instances in a public subnet removes their private security posture and exposes them to the public internet.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Attaching an internet gateway directly to a private subnet turns it into a public subnet, eliminating network isolation.

---

<a id="q-39"></a>

### Question 39

**Topic:** `Amazon VPC` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `39e4808b-cd72-4f6c-b257-9b38ff19bc1f`

> **Scenario:**  
> Which VPC component determines where network traffic from a subnet is sent?

#### Options
- **A.** Route table **[CORRECT]**
- **B.** IAM policy
- **C.** EBS snapshot
- **D.** CloudFront distribution

**Correct Answer:** `A`

> **Summary:** A route table contains a set of rules (called routes) that determine where network traffic from your subnet or gateway is directed.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  A route table specifies IP destination CIDR blocks and target gateways (e.g., local, igw-xxx, nat-xxx) to control network packet routing.

- **Option B:** ❌ **Why it is INCORRECT:**  
  An IAM policy grants or denies identity access permissions to AWS API actions, but does not route IP packets.

- **Option C:** ❌ **Why it is INCORRECT:**  
  An EC2 security group controls firewall filtering at the network interface layer, but does not route traffic across subnets.

- **Option D:** ❌ **Why it is INCORRECT:**  
  An S3 bucket policy manages access permissions to S3 storage resources, not VPC packet routing.

---

<a id="q-40"></a>

### Question 40

**Topic:** `Amazon VPC` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `d9df8600-f001-4a95-823c-ad7dd6524498`

> **Scenario:**  
> Which VPC controls are stateful and stateful-less, respectively?

#### Options
- **A.** Security groups are stateful; network ACLs are stateless. **[CORRECT]**
- **B.** Network ACLs are stateful; security groups are stateless.
- **C.** Both are stateless.
- **D.** Both are stateful and apply only to IAM users.

**Correct Answer:** `A`

> **Summary:** Security groups are stateful virtual firewalls that automatically allow response traffic, while Network Access Control Lists (NACLs) are stateless subnet-level firewalls.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Security groups are stateful (inbound allowed traffic automatically allows return outbound traffic), whereas Network ACLs are stateless (both inbound and outbound rules must be explicitly configured).

- **Option B:** ❌ **Why it is INCORRECT:**  
  Reversing the definitions is incorrect; Network ACLs are stateless, and security groups are stateful.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Both are not stateless; security groups track connection state at the ENI level.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Neither security groups nor NACLs apply to IAM users; they operate on network packets at the instance and subnet layers.

---

<a id="q-41"></a>

### Question 41

**Topic:** `Elastic Load Balancing` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `6a23f106-3fc9-4519-996f-3d50de6ac608`

> **Scenario:**  
> A web application runs on multiple EC2 instances and needs automatic distribution of incoming HTTP traffic. Which service should be used?

#### Options
- **A.** Application Load Balancer **[CORRECT]**
- **B.** NAT gateway
- **C.** AWS Transit Gateway
- **D.** Amazon EBS

**Correct Answer:** `A`

> **Summary:** Application Load Balancer (ALB) operates at Layer 7 (HTTP/HTTPS) and routes traffic based on URL paths, host headers, and HTTP request attributes across EC2 targets.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Application Load Balancer operates at the application layer (Layer 7) and provides advanced content-based routing (e.g., path/host routing) for HTTP and HTTPS workloads.

- **Option B:** ❌ **Why it is INCORRECT:**  
  A NAT gateway translates private IPv4 addresses to a public address for outbound internet egress, not load balancing.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Transit Gateway acts as a central cloud router connecting hundreds of VPCs and on-premises networks, not an HTTP application load balancer.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon EBS is a persistent block storage service, not a network traffic distribution service.

---

<a id="q-42"></a>

### Question 42

**Topic:** `Elastic Load Balancing` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `e29a2a3d-f66a-44a3-8b6d-4c7e6ff31c0a`

> **Scenario:**  
> A company needs to distribute TCP traffic to a fleet of servers while preserving very high throughput and low latency. Which load balancer is most appropriate?

#### Options
- **A.** Network Load Balancer **[CORRECT]**
- **B.** Application Load Balancer
- **C.** Gateway Load Balancer only for HTTP routing
- **D.** CloudFront origin access control

**Correct Answer:** `A`

> **Summary:** Network Load Balancer (NLB) operates at Layer 4 (Transport layer) and is capable of handling millions of requests per second with ultra-low latency while preserving client IP addresses.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Network Load Balancer (NLB) operates at Layer 4 (TCP/UDP/TLS) and provides ultra-low latency, handling volatile traffic patterns and massive throughput.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Application Load Balancer operates at Layer 7 and inspects application-layer HTTP protocols, which incurs slightly higher latency than Layer 4 NLB.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Gateway Load Balancers deploy and scale third-party virtual network appliances (like firewalls and IDS/IPS), not standard TCP application server fleets.

- **Option D:** ❌ **Why it is INCORRECT:**  
  CloudFront origin access control (OAC) secures access between CloudFront distributions and S3 origins, not TCP server load balancing.

---

<a id="q-43"></a>

### Question 43

**Topic:** `Elastic Load Balancing` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `cd1374d5-98ef-4697-bac2-55ccc0317223`

> **Scenario:**  
> Which ELB capability helps stop routing traffic to an unhealthy EC2 target?

#### Options
- **A.** Health checks **[CORRECT]**
- **B.** IAM groups
- **C.** S3 versioning
- **D.** EBS encryption

**Correct Answer:** `A`

> **Summary:** Elastic Load Balancing continuously performs health checks on target instances to automatically detect degraded targets and reroute traffic only to healthy instances.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  ELB health checks regularly ping target instances using configured protocols/paths; if an instance fails consecutive checks, ELB immediately ceases routing requests to it.

- **Option B:** ❌ **Why it is INCORRECT:**  
  IAM groups manage user identity authorizations and have no visibility into the operational health of EC2 compute targets.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 versioning manages object revision history in S3 buckets and does not interact with load balancer target routing.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EBS encryption protects data at rest on virtual disks and cannot evaluate EC2 application responsiveness.

---

<a id="q-44"></a>

### Question 44

**Topic:** `Elastic Load Balancing` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `15f846ff-3c95-494c-a8c3-3b5b8c3231c7`

> **Scenario *(Select TWO)*:**  
> Which statements about Elastic Load Balancing are correct? (Select TWO.)

#### Options
- **A.** It can distribute traffic across multiple Availability Zones. **[CORRECT]**
- **B.** It can integrate with Auto Scaling groups. **[CORRECT]**
- **C.** It replaces all application authentication controls.
- **D.** It provides persistent block storage to targets.
- **E.** It automatically makes every backend application stateless.

**Correct Answer:** `A, B`

> **Summary:** Elastic Load Balancing distributes incoming application traffic across targets in multiple Availability Zones and integrates seamlessly with EC2 Auto Scaling.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  ELB can balance incoming application traffic across targets deployed in multiple Availability Zones, enhancing fault tolerance and resiliency.

- **Option B:** ✅ **Why it is CORRECT:**  
  ELB automatically registers and deregisters instances managed by EC2 Auto Scaling groups as the fleet expands or contracts based on demand.

- **Option C:** ❌ **Why it is INCORRECT:**  
  ELB does not replace application authentication or authorization controls; application logic or IAM/Cognito is still required.

- **Option D:** ❌ **Why it is INCORRECT:**  
  ELB is a network routing and balancing service; it does not provide persistent storage to compute targets.

- **Option E:** ❌ **Why it is INCORRECT:**  
  ELB does not alter backend application state; developers must architect applications to be stateless or use external session stores.

---

<a id="q-45"></a>

### Question 45

**Topic:** `Amazon CloudFront` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `91b0c174-bc09-450a-b11a-8e96abbf309a`

> **Scenario:**  
> A media company wants users worldwide to receive cached video segments from locations close to them. Which service should it use?

#### Options
- **A.** Amazon CloudFront **[CORRECT]**
- **B.** Amazon EBS
- **C.** AWS IAM
- **D.** Amazon RDS

**Correct Answer:** `A`

> **Summary:** Amazon CloudFront is a fast Content Delivery Network (CDN) service that securely delivers data, videos, applications, and APIs to users globally with low latency.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon CloudFront caches static and dynamic web content at Edge locations worldwide, drastically reducing latency for viewers globally.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon EBS provides block storage for EC2 instances within a single AZ and cannot cache content globally.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS IAM manages identities and access permissions, not global media content delivery.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon RDS provides relational database management, not edge caching for streaming media.

---

<a id="q-46"></a>

### Question 46

**Topic:** `Amazon CloudFront` | **Difficulty:** `Hard` | **Type:** `Single`  
**Question ID:** `adf57f01-4b21-4356-a308-1cd478e3fc08`

> **Scenario:**  
> A company wants CloudFront to retrieve private content from an S3 bucket without making the bucket public. Which approach is appropriate?

#### Options
- **A.** Use CloudFront origin access control and restrict the bucket policy **[CORRECT]**
- **B.** Enable public read access for all S3 objects
- **C.** Place the S3 bucket in a private subnet
- **D.** Attach an EC2 security group to the bucket

**Correct Answer:** `A`

> **Summary:** CloudFront Origin Access Control (OAC) allows you to restrict access to an Amazon S3 origin so that users can only access files through the CloudFront distribution.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Configuring Origin Access Control (OAC) and restricting the S3 bucket policy ensures that S3 content is only accessible via authorized CloudFront URLs, keeping the bucket private.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Enabling public read access exposes the S3 bucket objects directly to anyone on the internet, defeating private content security.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 buckets do not reside inside VPC subnets; they are regional public service endpoints.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EC2 security groups apply to virtual network interfaces, not to Amazon S3 bucket resources.

---

<a id="q-47"></a>

### Question 47

**Topic:** `Amazon CloudFront` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `86c83eac-46a0-4de4-88ef-091ea54644e8`

> **Scenario:**  
> Which CloudFront feature allows a distribution to serve different cached content based on a viewer's country?

#### Options
- **A.** Geographic restriction **[CORRECT]**
- **B.** EBS snapshot
- **C.** IAM permission boundary
- **D.** RDS Multi-AZ

**Correct Answer:** `A`

> **Summary:** CloudFront Geographic Restriction (geo-blocking) allows you to prevent users in specific geographic locations from accessing content that you're distributing.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Geographic restriction allows administrators to whitelist or blacklist specific countries, preventing unauthorized geographic regions from accessing copyrighted or regulated content.

- **Option B:** ❌ **Why it is INCORRECT:**  
  An EBS snapshot is an incremental backup of a block storage volume and has no CDN distribution capabilities.

- **Option C:** ❌ **Why it is INCORRECT:**  
  An IAM permission boundary sets the maximum permissions an identity can receive, but does not control web viewer geography.

- **Option D:** ❌ **Why it is INCORRECT:**  
  RDS Multi-AZ manages database replication across data centers, completely unrelated to content delivery networks.

---

<a id="q-48"></a>

### Question 48

**Topic:** `Amazon CloudFront` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `c1c2b7e8-feb2-4663-b8f4-7dc338c2b167`

> **Scenario *(Select TWO)*:**  
> Which CloudFront capabilities can improve delivery performance or security? (Select TWO.)

#### Options
- **A.** Caching content at edge locations **[CORRECT]**
- **B.** Integrating with AWS WAF **[CORRECT]**
- **C.** Replacing the need for TLS certificates
- **D.** Providing relational database transactions
- **E.** Eliminating the need for an origin in every design

**Correct Answer:** `A, B`

> **Summary:** Amazon CloudFront improves delivery performance by caching at edge locations and improves security through native integration with AWS WAF.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Caching content closer to end users at edge locations reduces network transit hops and dramatically lowers latency for static and media assets.

- **Option B:** ✅ **Why it is CORRECT:**  
  CloudFront integrates directly with AWS WAF (Web Application Firewall) to block malicious SQL injection, cross-site scripting, and DDoS attacks at the edge.

- **Option C:** ❌ **Why it is INCORRECT:**  
  CloudFront does not replace TLS certificates; it requires custom or ACM-generated TLS certificates for custom HTTPS domain delivery.

- **Option D:** ❌ **Why it is INCORRECT:**  
  CloudFront is an edge CDN service and does not execute or manage relational database transactions.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Every CloudFront distribution requires at least one designated origin (such as an S3 bucket or HTTP web server) to fetch non-cached content.

---

<a id="q-49"></a>

### Question 49

**Topic:** `Amazon Route 53` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `9fed9e89-39de-4e89-9009-08fc170833cc`

> **Scenario:**  
> Which Route 53 routing policy directs users to the endpoint with the lowest network latency among configured AWS Regions?

#### Options
- **A.** Latency-based routing **[CORRECT]**
- **B.** Simple routing
- **C.** Weighted routing
- **D.** Failover routing only

**Correct Answer:** `A`

> **Summary:** Amazon Route 53 latency-based routing routes user traffic to the AWS Region that provides the lowest network latency to the user.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Latency-based routing directs user DNS queries to the AWS Region that provides the fastest network response times based on worldwide latency measurements.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Simple routing performs standard DNS lookups for a single resource or random multiple IP addresses without latency optimization.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Weighted routing distributes traffic across multiple endpoints based on assigned percentage proportions (e.g., 80% to v1, 20% to v2).

- **Option D:** ❌ **Why it is INCORRECT:**  
  Failover routing directs traffic to a primary resource and flips to a standby resource only when the primary fails health checks.

---

<a id="q-50"></a>

### Question 50

**Topic:** `Amazon Route 53` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `55d159c3-4171-41c0-b624-311d23cf0ddb`

> **Scenario:**  
> A company wants DNS to direct traffic to a primary application endpoint and automatically use a secondary endpoint if the primary is unhealthy. Which Route 53 policy should it use?

#### Options
- **A.** Failover routing **[CORRECT]**
- **B.** Geolocation routing
- **C.** Weighted routing
- **D.** Multivalue answer routing without health checks

**Correct Answer:** `A`

> **Summary:** Amazon Route 53 failover routing policy allows you to configure active-passive failover by directing traffic to a healthy primary resource and switching to secondary if unhealthy.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Failover routing automatically monitors the health of the primary endpoint and diverts DNS requests to a secondary disaster recovery site when the primary fails.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Geolocation routing routes traffic based on the geographic location of the DNS query requester (e.g., by country or continent), not endpoint operational health.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Weighted routing distributes traffic according to assigned weight ratios and is primarily used for testing or gradual canary rollouts.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Multivalue answer routing returns multiple randomly selected healthy IP addresses, not an active-passive failover design.

---

<a id="q-51"></a>

### Question 51

**Topic:** `Amazon Route 53` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `2325e45a-70f1-4a3f-944c-30312bc3a7e5`

> **Scenario:**  
> Which Route 53 function translates a domain name such as app.example.com into an IP address or AWS resource endpoint?

#### Options
- **A.** DNS resolution **[CORRECT]**
- **B.** Block storage provisioning
- **C.** Identity federation
- **D.** Container image scanning

**Correct Answer:** `A`

> **Summary:** Domain Name System (DNS) resolution is the core process of converting human-readable domain names (like example.com) into machine-readable IP addresses.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Route 53 performs authoritative and recursive DNS resolution, mapping domain names (such as app.example.com) to target IP addresses or AWS resource endpoints.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Block storage provisioning is handled by Amazon EBS, not a DNS routing system.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Identity federation connects corporate identities (like SAML or Active Directory) to AWS IAM, not domain name translation.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Container image scanning is performed by Amazon ECR or Amazon Inspector, not Route 53.

---

<a id="q-52"></a>

### Question 52

**Topic:** `Amazon Route 53` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `7e92d1d5-1cf3-4b53-ac31-ddd275829dc7`

> **Scenario *(Select TWO)*:**  
> Which Route 53 features are available for application traffic management? (Select TWO.)

#### Options
- **A.** Health checks **[CORRECT]**
- **B.** Weighted routing **[CORRECT]**
- **C.** EBS volume encryption
- **D.** IAM policy simulation as DNS routing
- **E.** Automatic relational schema migration

**Correct Answer:** `A, B`

> **Summary:** Amazon Route 53 provides sophisticated traffic management features, including automated endpoint health checks and weighted routing policies.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Route 53 health checks continuously monitor web application endpoints and automatically trigger DNS failover when servers become unreachable.

- **Option B:** ✅ **Why it is CORRECT:**  
  Weighted routing allows administrators to specify relative weight ratios to divide traffic across multiple resources for A/B testing and canary deployments.

- **Option C:** ❌ **Why it is INCORRECT:**  
  EBS volume encryption is a storage feature managed by AWS KMS and EBS, entirely separate from DNS traffic routing.

- **Option D:** ❌ **Why it is INCORRECT:**  
  IAM policy simulation evaluates identity permissions and cannot serve as a DNS routing policy.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Database schema migration is performed by AWS Database Migration Service (DMS), not Route 53.

---

<a id="q-53"></a>

### Question 53

**Topic:** `AWS CloudTrail and Amazon CloudWatch` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `b53b8dd1-afb2-4273-818a-65fa75bc90f4`

> **Scenario:**  
> A security team needs a record of AWS API calls, including who made the call and which resource was affected. Which service should it use?

#### Options
- **A.** AWS CloudTrail **[CORRECT]**
- **B.** Amazon CloudWatch
- **C.** Amazon Route 53
- **D.** AWS Budgets

**Correct Answer:** `A`

> **Summary:** AWS CloudTrail records AWS API calls for your account and delivers log files containing event history, caller identity, request parameters, and response elements.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS CloudTrail audits and logs every API activity and management event across AWS services, detailing who made the request, when, and from what IP address.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon CloudWatch monitors operational performance metrics and application logs, but does not capture raw AWS API management audit trails.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon Route 53 is a cloud DNS service, not an API audit log repository.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Budgets tracks financial spending thresholds and alerts on cost, not identity API interactions.

---

<a id="q-54"></a>

### Question 54

**Topic:** `AWS CloudTrail and Amazon CloudWatch` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `0fd0cf41-f0f2-42ec-afd4-de31ccc1946b`

> **Scenario:**  
> An operations team wants an alarm when an EC2 instance's CPU utilization exceeds a threshold for several minutes. Which service should provide the alarm?

#### Options
- **A.** Amazon CloudWatch **[CORRECT]**
- **B.** AWS CloudTrail
- **C.** Amazon S3 Glacier
- **D.** IAM Access Analyzer

**Correct Answer:** `A`

> **Summary:** Amazon CloudWatch monitors metrics like CPU utilization and allows you to configure CloudWatch Alarms to send notifications or initiate automated actions.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon CloudWatch collects system performance metrics (such as `CPUUtilization`) and triggers alarms when thresholds are breached, sending SNS notifications.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS CloudTrail records API calls for governance and compliance, but does not monitor real-time operating metrics like CPU percentage.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon S3 Glacier is an archival object storage service, not an infrastructure monitoring tool.

- **Option D:** ❌ **Why it is INCORRECT:**  
  IAM Access Analyzer analyzes resource-based policies to identify unintended public or cross-account access, not compute metrics.

---

<a id="q-55"></a>

### Question 55

**Topic:** `AWS CloudTrail and Amazon CloudWatch` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `c6daac40-86f6-4d6f-b34b-3c4d8fc6dee7`

> **Scenario:**  
> Which service is best suited for collecting application logs and creating metric filters from those logs?

#### Options
- **A.** Amazon CloudWatch Logs **[CORRECT]**
- **B.** AWS CloudTrail Lake only
- **C.** Amazon Route 53
- **D.** AWS Pricing Calculator

**Correct Answer:** `A`

> **Summary:** Amazon CloudWatch Logs enables you to centralize and store application and system logs, query them with CloudWatch Logs Insights, and build metric filters.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Amazon CloudWatch Logs centralizes log ingestion from EC2, Lambda, and containers, enabling searching, monitoring, and metric filter generation.

- **Option B:** ❌ **Why it is INCORRECT:**  
  CloudTrail Lake is an immutable managed audit query store for CloudTrail API events, not general application error logs.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon Route 53 manages DNS traffic and records, not application log ingestion.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Pricing Calculator generates cost estimates for planned AWS architectures, not operational log analytics.

---

<a id="q-56"></a>

### Question 56

**Topic:** `AWS CloudTrail and Amazon CloudWatch` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `43cd270d-b1ca-4cee-bab9-f6c1862c5923`

> **Scenario *(Select TWO)*:**  
> Which statements correctly distinguish CloudTrail and CloudWatch? (Select TWO.)

#### Options
- **A.** CloudTrail records API activity for auditing. **[CORRECT]**
- **B.** CloudWatch monitors metrics, logs, and operational events. **[CORRECT]**
- **C.** CloudTrail primarily measures CPU utilization.
- **D.** CloudWatch is only an IAM credential store.
- **E.** Neither service supports notifications or automation integrations.

**Correct Answer:** `A, B`

> **Summary:** AWS CloudTrail tracks 'who did what' (API governance and auditing), while Amazon CloudWatch tracks 'how systems are performing' (metrics, logs, and alarms).

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  CloudTrail records administrative and data API activities across your account to provide audit trails for security compliance and troubleshooting.

- **Option B:** ✅ **Why it is CORRECT:**  
  CloudWatch collects operational metrics, monitors system logs, and provides visual dashboards and automated alarms for system health.

- **Option C:** ❌ **Why it is INCORRECT:**  
  CPU utilization is a performance metric gathered by CloudWatch, not CloudTrail.

- **Option D:** ❌ **Why it is INCORRECT:**  
  CloudWatch is a full observability platform, not an IAM credential storage mechanism.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Both services integrate extensively with automation, including Amazon SNS alerts and EventBridge event-driven workflows.

---

<a id="q-57"></a>

### Question 57

**Topic:** `AWS pricing models` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `07c67aab-bf7d-4cc0-b9be-a33fdb6b9cef`

> **Scenario:**  
> A company runs a production workload continuously and wants a discount in exchange for a one-year or three-year compute usage commitment. Which pricing option should it evaluate?

#### Options
- **A.** Savings Plans **[CORRECT]**
- **B.** On-Demand pricing only
- **C.** Spot pricing without interruption tolerance
- **D.** Free Tier only

**Correct Answer:** `A`

> **Summary:** AWS Savings Plans offer significant savings (up to 72%) over On-Demand pricing in exchange for a commitment to a consistent amount of compute usage ($/hour) for 1 or 3 years.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Savings Plans provide substantial discounts on EC2, Fargate, and Lambda usage in exchange for committing to a consistent hourly compute spend for a 1- or 3-year term.

- **Option B:** ❌ **Why it is INCORRECT:**  
  On-Demand pricing offers zero commitment and maximum flexibility, but costs the highest standard hourly rate.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Spot pricing does not provide term discount commitments and is subject to interruption, making it inappropriate for non-interruptible continuous production.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Free Tier provides temporary or introductory limits for new accounts and cannot support continuous production workloads at scale.

---

<a id="q-58"></a>

### Question 58

**Topic:** `AWS pricing models` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `bc03cc78-43ae-40d4-bd99-262a52f6bd77`

> **Scenario:**  
> Which pricing model is most appropriate for a fault-tolerant workload that can be interrupted and restarted?

#### Options
- **A.** Spot pricing **[CORRECT]**
- **B.** Dedicated Host pricing only
- **C.** On-Demand pricing with no interruptions allowed
- **D.** Data transfer pricing

**Correct Answer:** `A`

> **Summary:** Spot Instances leverage spare EC2 capacity at discounts of up to 90% off On-Demand rates, making them the most cost-effective choice for fault-tolerant, interruptible jobs.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Spot pricing delivers the lowest cost on AWS for flexible workloads that can gracefully withstand unexpected capacity reclamation.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Dedicated Host pricing is the most expensive hosting tier, designed for compliance or BYOL requirements rather than cost reduction.

- **Option C:** ❌ **Why it is INCORRECT:**  
  On-Demand pricing ensures instances cannot be reclaimed by AWS, but charges full standard rates.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Data transfer pricing covers bandwidth in and out of AWS, not compute capacity execution models.

---

<a id="q-59"></a>

### Question 59

**Topic:** `AWS pricing models` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `ec4ac980-16ff-4cbc-98dc-c087a5c79c14`

> **Scenario:**  
> Which AWS tool can estimate the expected monthly cost of a planned architecture before resources are deployed?

#### Options
- **A.** AWS Pricing Calculator **[CORRECT]**
- **B.** AWS CloudTrail
- **C.** Amazon Inspector
- **D.** AWS Artifact

**Correct Answer:** `A`

> **Summary:** AWS Pricing Calculator is a web-based planning tool that allows you to model proposed architectural solutions and estimate monthly AWS costs before deploying.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Pricing Calculator allows users to model architectural use cases and calculate estimated monthly costs based on projected resource usage.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS CloudTrail audits API calls and management events in existing accounts, but cannot model future cost estimates.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon Inspector is an automated vulnerability management service that scans workloads for software flaws, not financial modeling.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Artifact provides on-demand downloads of compliance certifications and SOC reports, not cost estimations.

---

<a id="q-60"></a>

### Question 60

**Topic:** `AWS pricing models` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `541f0cd2-fb41-4f39-997d-6ae1afa2b08e`

> **Scenario *(Select TWO)*:**  
> Which factors can affect the cost of an AWS workload? (Select TWO.)

#### Options
- **A.** Data transfer volume and direction **[CORRECT]**
- **B.** AWS Region selected **[CORRECT]**
- **C.** Number of IAM groups alone
- **D.** Whether an S3 bucket has a memorable name
- **E.** The color of an EC2 console tag

**Correct Answer:** `A, B`

> **Summary:** AWS workload costs vary significantly depending on the volume and direction of data transfer (outbound data transfer incurs charges) and the selected AWS Region.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Data transfer volume and direction heavily affect costs: inbound data transfer is generally free, whereas outbound data transfer to the internet or across Regions incurs charges.

- **Option B:** ✅ **Why it is CORRECT:**  
  AWS Region selection impacts pricing because physical infrastructure, taxes, and operational expenses vary geographically across different AWS Regions.

- **Option C:** ❌ **Why it is INCORRECT:**  
  IAM groups, users, and roles are identity features provided at zero additional charge.

- **Option D:** ❌ **Why it is INCORRECT:**  
  S3 bucket naming has no impact on billing; S3 charges are based on storage tiers, request counts, and data transfer volume.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Console tag colors or metadata formatting do not carry any billing fee.

---

<a id="q-61"></a>

### Question 61

**Topic:** `AWS Cost Explorer and AWS Budgets` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `d9f5a486-be58-4e42-a2cb-706849a5ec29`

> **Scenario:**  
> A finance team wants to analyze historical AWS spending by service, account, and tag and identify usage trends. Which tool is most appropriate?

#### Options
- **A.** AWS Cost Explorer **[CORRECT]**
- **B.** AWS CloudFormation only
- **C.** Amazon CloudFront
- **D.** IAM Policy Simulator

**Correct Answer:** `A`

> **Summary:** AWS Cost Explorer provides interactive visual charts and tools to view, analyze, and forecast historical AWS spending by service, account, and tag.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Cost Explorer enables finance and engineering teams to visualize and dissect spending patterns over time, filter by dimensions, and forecast future costs.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS CloudFormation is an Infrastructure as Code (IaC) deployment tool, not a financial analytics reporting dashboard.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Amazon CloudFront is a Content Delivery Network for caching web assets, not a billing analysis interface.

- **Option D:** ❌ **Why it is INCORRECT:**  
  IAM Policy Simulator tests and evaluates identity permissions, not account financial expenditures.

---

<a id="q-62"></a>

### Question 62

**Topic:** `AWS Cost Explorer and AWS Budgets` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `40416f8a-e819-423a-bda9-5d59f5466f71`

> **Scenario:**  
> A company wants an alert when monthly AWS spending is forecast to exceed a defined amount. Which service should it configure?

#### Options
- **A.** AWS Budgets **[CORRECT]**
- **B.** Amazon Inspector
- **C.** AWS CloudTrail
- **D.** Amazon Route 53

**Correct Answer:** `A`

> **Summary:** AWS Budgets gives you the ability to set custom cost and usage budgets and receive automated alerts when actual or forecasted spending exceeds your thresholds.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Budgets allows organizations to configure custom financial targets and receive automated SNS or email notifications when forecasted spending exceeds thresholds.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon Inspector evaluates operating systems and container images for software vulnerabilities, not financial spending limits.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS CloudTrail tracks management API call history, not monetary cost thresholds.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Amazon Route 53 handles domain registration and DNS routing, not billing alerts.

---

<a id="q-63"></a>

### Question 63

**Topic:** `AWS Cost Explorer and AWS Budgets` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `b4658cd3-91a9-43cd-ac1e-33fb675001bd`

> **Scenario:**  
> A team needs to determine which tagged application generated a recent increase in AWS charges. Which Cost Explorer capability is most useful?

#### Options
- **A.** Filtering and grouping by cost allocation tags **[CORRECT]**
- **B.** Creating an IAM role for every invoice line
- **C.** Enabling an internet gateway
- **D.** Changing the account root password

**Correct Answer:** `A`

> **Summary:** Cost allocation tags allow organizations to categorize and track AWS costs on a detailed level by labeling resources with key-value pairs (e.g., Environment=Prod, App=Billing).

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Activating and filtering by user-defined cost allocation tags allows finance teams to break down AWS monthly bills by specific project, cost center, or application.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Creating IAM roles does not provide financial categorization or line-item billing breakdown.

- **Option C:** ❌ **Why it is INCORRECT:**  
  An internet gateway provides internet routing for VPC public subnets and has no financial attribution functionality.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Changing account root passwords is a security measure that has no impact on billing reports.

---

<a id="q-64"></a>

### Question 64

**Topic:** `AWS Cost Explorer and AWS Budgets` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `4b92bc2a-aea8-4f31-94d3-bffe231dad91`

> **Scenario *(Select TWO)*:**  
> Which actions support AWS cost governance? (Select TWO.)

#### Options
- **A.** Create budgets with notification thresholds **[CORRECT]**
- **B.** Review usage trends with Cost Explorer **[CORRECT]**
- **C.** Disable all monitoring to reduce visibility costs
- **D.** Give every user unrestricted spending authority
- **E.** Ignore resource tags because billing data cannot be grouped

**Correct Answer:** `A, B`

> **Summary:** Effective AWS cost governance requires tracking budgets with notification thresholds and continuously reviewing consumption trends with Cost Explorer.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Setting up AWS Budgets with notification thresholds ensures early warning before unexpected cost overruns occur.

- **Option B:** ✅ **Why it is CORRECT:**  
  Regularly reviewing usage trends and anomalous spikes using AWS Cost Explorer enables proactive right-sizing and architecture optimization.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Disabling monitoring blinds the organization to resource consumption and cost anomalies, leading to massive accidental spending.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Granting unrestricted spending authority invites runaway cloud costs and completely undermines financial governance.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Ignoring resource tags makes it impossible to allocate expenses to specific teams, business units, or applications.

---

<a id="q-65"></a>

### Question 65

**Topic:** `AWS Support plans` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `db17bc5d-e2cb-485d-ab8d-f72a977860ac`

> **Scenario:**  
> A company needs architectural guidance and a predictable response target for business-critical AWS workloads. Which AWS Support plan should it evaluate first?

#### Options
- **A.** Business Support **[CORRECT]**
- **B.** Basic Support only
- **C.** No support plan
- **D.** AWS Free Tier

**Correct Answer:** `A`

> **Summary:** AWS Business Support provides 24/7 phone, chat, and web access to Cloud Support Engineers with response times under 1 hour for production system down issues.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Business Support provides 24/7 access to Cloud Support Engineers, architectural guidance, and a <1 hour response SLA for production outages.

- **Option B:** ❌ **Why it is INCORRECT:**  
  AWS Basic Support is free for all customers but only covers billing and account questions with no technical case management or response SLAs.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Operating with no support plan leaves production workloads vulnerable with no technical escalation path during critical outages.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Free Tier is a temporary usage quota, not an enterprise customer support plan.

---

<a id="q-66"></a>

### Question 66

**Topic:** `AWS Support plans` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `a6ff2ca6-f34c-4b3f-a362-c15c6cc36703`

> **Scenario:**  
> Which AWS Support feature can help a customer review account security, service limits, and operational optimization opportunities?

#### Options
- **A.** AWS Trusted Advisor **[CORRECT]**
- **B.** Amazon Route 53
- **C.** S3 Transfer Acceleration
- **D.** EC2 instance store

**Correct Answer:** `A`

> **Summary:** AWS Trusted Advisor inspects your AWS environment and provides real-time recommendations across five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Quotas.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Trusted Advisor evaluates your AWS environment against best practices, identifying idle resources, security vulnerabilities, quota limits, and optimization opportunities.

- **Option B:** ❌ **Why it is INCORRECT:**  
  Amazon Route 53 is a cloud DNS service, not an automated architecture review tool.

- **Option C:** ❌ **Why it is INCORRECT:**  
  S3 Transfer Acceleration speeds up data transfers over long distances using edge locations, unrelated to account configuration reviews.

- **Option D:** ❌ **Why it is INCORRECT:**  
  EC2 instance store provides ephemeral block storage and does not perform security or cost auditing.

---

<a id="q-67"></a>

### Question 67

**Topic:** `AWS Support plans` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `e0da2682-21b3-467d-9bac-5d8718b4d921`

> **Scenario:**  
> A developer has a general question about configuring an AWS service and wants to use community discussions and documentation before opening a support case. Which resource is appropriate?

#### Options
- **A.** AWS re:Post and AWS documentation **[CORRECT]**
- **B.** An EBS snapshot
- **C.** A VPC network ACL
- **D.** An S3 lifecycle rule

**Correct Answer:** `A`

> **Summary:** AWS Documentation and AWS re:Post (a community-driven knowledge sharing forum) provide comprehensive, free technical guidance and configuration examples.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS re:Post provides a vetted community Q&A forum, and AWS official documentation provides detailed configuration guides, architecture references, and API tutorials.

- **Option B:** ❌ **Why it is INCORRECT:**  
  An EBS snapshot is a block storage volume backup and cannot provide technical documentation.

- **Option C:** ❌ **Why it is INCORRECT:**  
  A VPC network ACL is a network firewall and cannot answer configuration questions.

- **Option D:** ❌ **Why it is INCORRECT:**  
  An S3 lifecycle rule manages storage class transitions, not technical developer support.

---

<a id="q-68"></a>

### Question 68

**Topic:** `AWS Support plans` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `e6a5e833-3e0d-4f94-abcf-c5e099f97048`

> **Scenario *(Select TWO)*:**  
> Which AWS Support-related capabilities can help an organization operate workloads more effectively? (Select TWO.)

#### Options
- **A.** Trusted Advisor recommendations **[CORRECT]**
- **B.** Technical support case management **[CORRECT]**
- **C.** Automatic elimination of all application defects
- **D.** Guaranteed unlimited architecture design by AWS
- **E.** Replacement of customer IAM administration

**Correct Answer:** `A, B`

> **Summary:** Key AWS Support capabilities include automated Trusted Advisor architectural guidance and 24/7 technical support case management with SLA-backed response times.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  AWS Trusted Advisor automatically inspects AWS environments to provide actionable recommendations for security, cost optimization, fault tolerance, and quotas.

- **Option B:** ✅ **Why it is CORRECT:**  
  Technical support case management allows teams to submit tickets and engage directly with AWS Cloud Support Engineers via chat, phone, and email.

- **Option C:** ❌ **Why it is INCORRECT:**  
  AWS Support does not eliminate defects in customer application code; debugging application source code remains the customer's responsibility.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Support does not offer unlimited custom architecture design for customers; design assistance is advisory.

- **Option E:** ❌ **Why it is INCORRECT:**  
  AWS Support never replaces customer IAM administration; access control remains strictly the customer's responsibility.

---

<a id="q-69"></a>

### Question 69

**Topic:** `AWS Well-Architected Framework` | **Difficulty:** `Easy` | **Type:** `Single`  
**Question ID:** `b7a3b0f2-d233-4aed-a54e-fc4538ff6b30`

> **Scenario:**  
> A team wants to improve an application by evaluating operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. Which AWS framework should it use?

#### Options
- **A.** AWS Well-Architected Framework **[CORRECT]**
- **B.** AWS Cloud Adoption Framework only
- **C.** AWS Shared Responsibility Model only
- **D.** AWS Pricing Calculator

**Correct Answer:** `A`

> **Summary:** The AWS Well-Architected Framework provides architectural best practices across six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  The AWS Well-Architected Framework helps cloud architects build secure, high-performing, resilient, and efficient infrastructure based on 6 core pillars.

- **Option B:** ❌ **Why it is INCORRECT:**  
  The AWS Cloud Adoption Framework (CAF) organizes cloud transformation into 6 organizational perspectives (Business, People, Governance, Platform, Security, Operations), not technical architecture reviews.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The Shared Responsibility Model defines security demarcation between AWS and the customer, but does not provide an architectural design evaluation framework.

- **Option D:** ❌ **Why it is INCORRECT:**  
  AWS Pricing Calculator generates financial cost projections, not architectural maturity evaluations.

---

<a id="q-70"></a>

### Question 70

**Topic:** `AWS Well-Architected Framework` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `b91c75b5-c723-4da2-a31f-443539e7a97b`

> **Scenario:**  
> A workload has no tested recovery process and depends on one Availability Zone. Which Well-Architected pillar is most directly affected?

#### Options
- **A.** Reliability **[CORRECT]**
- **B.** Cost optimization
- **C.** Sustainability only
- **D.** Performance efficiency only

**Correct Answer:** `A`

> **Summary:** The Reliability pillar of the AWS Well-Architected Framework focuses on the ability of a workload to perform its intended function correctly and consistently, including automatic recovery from failures.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  The Reliability pillar focuses on designing systems to recover automatically from failures, testing recovery procedures, and distributing workloads across multiple Availability Zones.

- **Option B:** ❌ **Why it is INCORRECT:**  
  The Cost Optimization pillar focuses on avoiding unnecessary expenditure, right-sizing resources, and analyzing spending.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The Sustainability pillar focuses on minimizing the environmental and carbon impact of running cloud workloads.

- **Option D:** ❌ **Why it is INCORRECT:**  
  The Performance Efficiency pillar focuses on using compute and storage resources efficiently to meet system requirements.

---

<a id="q-71"></a>

### Question 71

**Topic:** `AWS Well-Architected Framework` | **Difficulty:** `Medium` | **Type:** `Single`  
**Question ID:** `de531f3b-4516-404b-bfda-8f655a737be1`

> **Scenario:**  
> An organization discovers that several oversized instances run at low utilization. Which Well-Architected pillar should guide the remediation?

#### Options
- **A.** Cost optimization **[CORRECT]**
- **B.** Security
- **C.** Operational excellence only
- **D.** Reliability only

**Correct Answer:** `A`

> **Summary:** The Cost Optimization pillar emphasizes right-sizing compute instances and adopting appropriate pricing models to avoid paying for unneeded capacity.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  The Cost Optimization pillar guides organizations in right-sizing oversized instances running at low utilization and stopping idle resources to eliminate unnecessary expense.

- **Option B:** ❌ **Why it is INCORRECT:**  
  The Security pillar focuses on protecting data, systems, and assets through least privilege, encryption, and continuous monitoring.

- **Option C:** ❌ **Why it is INCORRECT:**  
  The Operational Excellence pillar focuses on running workloads effectively, automating changes, and learning from operational events.

- **Option D:** ❌ **Why it is INCORRECT:**  
  The Reliability pillar focuses on high availability, fault tolerance, and automated recovery from infrastructure failures.

---

<a id="q-72"></a>

### Question 72

**Topic:** `AWS Well-Architected Framework` | **Difficulty:** `Medium` | **Type:** `Multiple`  
**Question ID:** `a93152b1-e4c7-48c3-a450-af8abce53e9a`

> **Scenario *(Select TWO)*:**  
> Which practices align with the AWS Well-Architected Framework? (Select TWO.)

#### Options
- **A.** Automate deployments and operational responses where appropriate **[CORRECT]**
- **B.** Design for failure and regularly test recovery **[CORRECT]**
- **C.** Use the largest instance type by default
- **D.** Treat security as a one-time launch activity
- **E.** Avoid monitoring to reduce operational complexity

**Correct Answer:** `A, B`

> **Summary:** Core Well-Architected Framework design principles include automating operational responses and designing systems to anticipate failure and regularly test recovery.

#### Comprehensive Verification & Explanations

- **Option A:** ✅ **Why it is CORRECT:**  
  Automating deployments and operational responses where appropriate aligns with the Operational Excellence pillar to minimize human error and ensure repeatable consistency.

- **Option B:** ✅ **Why it is CORRECT:**  
  Designing for failure and regularly testing recovery procedures aligns directly with the Reliability pillar to ensure business continuity.

- **Option C:** ❌ **Why it is INCORRECT:**  
  Using the largest instance type by default violates the Cost Optimization pillar; workloads should be right-sized based on empirical metrics.

- **Option D:** ❌ **Why it is INCORRECT:**  
  Treating security as a one-time launch activity violates the Security pillar; security must be continuous and integrated into every stage of the lifecycle.

- **Option E:** ❌ **Why it is INCORRECT:**  
  Avoiding monitoring completely undermines Operational Excellence and Reliability; comprehensive telemetry is mandatory for operational visibility.

---

