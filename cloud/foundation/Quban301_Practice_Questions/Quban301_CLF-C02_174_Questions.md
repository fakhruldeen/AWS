# AWS Certified Cloud Practitioner (CLF-C02) - Master Question Bank (174 Questions)

Source: [Quban301/Certification-Practice](https://github.com/Quban301/Certification-Practice)

Complete bank combining Practice Exam 1 and Final Exam papers.

Total Questions: **174**

## 📑 Quick Table of Contents

- [Question 1](#q-1): `Module 5 · Compute, Storage & Databases` - An EC2 instance is named m5.large. What does the letter 'm' indicate?... *(Ans: B)*
- [Question 2](#q-2): `Module 5 · Compute, Storage & Databases` - A workload does sustained, consistently heavy CPU processing (media tr... *(Ans: B)*
- [Question 3](#q-3): `Module 5 · Compute, Storage & Databases` - An in-memory database such as Redis or SAP HANA needs a large amount o... *(Ans: C)*
- [Question 4](#q-4): `Module 5 · Compute, Storage & Databases` - A small web app is mostly idle but occasionally spikes. Which EC2 fami... *(Ans: A)*
- [Question 5](#q-5): `Module 5 · Compute, Storage & Databases` - How do burstable (T family) instances handle CPU above their baseline?... *(Ans: B)*
- [Question 6](#q-6): `Module 5 · Compute, Storage & Databases` - Which storage option provides the highest IOPS and lowest latency but ... *(Ans: B)*
- [Question 7](#q-7): `Module 5 · Compute, Storage & Databases` - A single EC2 instance needs a persistent boot volume that survives reb... *(Ans: B)*
- [Question 8](#q-8): `Module 5 · Compute, Storage & Databases` - Thousands of EC2 instances across multiple Availability Zones must rea... *(Ans: C)*
- [Question 9](#q-9): `Module 5 · Compute, Storage & Databases` - Which statement about Amazon S3 durability is correct?... *(Ans: B)*
- [Question 10](#q-10): `Module 5 · Compute, Storage & Databases` - Data is temporary, already replicated elsewhere, and needs the absolut... *(Ans: A)*
- [Question 11](#q-11): `Module 5 · Compute, Storage & Databases` - Which S3 storage class automatically moves objects between access tier... *(Ans: B)*
- [Question 12](#q-12): `Module 5 · Compute, Storage & Databases` - Archived data is rarely accessed (e.g. quarterly) but must still be re... *(Ans: B)*
- [Question 13](#q-13): `Module 5 · Compute, Storage & Databases` - Which S3 storage class is the cheapest and is designed for 7–10+ year ... *(Ans: C)*
- [Question 14](#q-14): `Module 5 · Compute, Storage & Databases` - What do S3 Lifecycle policies let you do without writing any applicati... *(Ans: B)*
- [Question 15](#q-15): `Module 5 · Compute, Storage & Databases` - Which AWS database service is a relational engine supporting MySQL, Po... *(Ans: B)*
- [Question 16](#q-16): `Module 5 · Compute, Storage & Databases` - A workload needs massive, key-based throughput with single-digit-milli... *(Ans: C)*
- [Question 17](#q-17): `Module 5 · Compute, Storage & Databases` - Analysts need to run complex analytical queries across years of histor... *(Ans: B)*
- [Question 18](#q-18): `Module 5 · Compute, Storage & Databases` - You want to reduce load on a relational database by serving repeated r... *(Ans: B)*
- [Question 19](#q-19): `Module 5 · Compute, Storage & Databases` - Which is an advantage of Amazon Aurora over standard Amazon RDS?... *(Ans: B)*
- [Question 20](#q-20): `Module 5 · Compute, Storage & Databases` - Aurora stores how many copies of your data, and across how many Availa... *(Ans: B)*
- [Question 21](#q-21): `Module 5 · Compute, Storage & Databases` - A dev/test database has intermittent, spiky traffic and you want the m... *(Ans: A)*
- [Question 22](#q-22): `Module 5 · Compute, Storage & Databases` - Which Auto Scaling policy works like a thermostat — you set a metric t... *(Ans: B)*
- [Question 23](#q-23): `Module 5 · Compute, Storage & Databases` - You know traffic peaks every weekday at 9 a.m. and want to raise capac... *(Ans: C)*
- [Question 24](#q-24): `Module 5 · Compute, Storage & Databases` - What is the canonical AWS answer for elastic, self-healing, highly ava... *(Ans: B)*
- [Question 25](#q-25): `Module 6 · Integration & DevOps` - What problem does Amazon SQS primarily solve?... *(Ans: B)*
- [Question 26](#q-26): `Module 6 · Integration & DevOps` - A banking workload must process messages exactly once and in strict or... *(Ans: B)*
- [Question 27](#q-27): `Module 6 · Integration & DevOps` - A Standard SQS queue offers which delivery and ordering guarantees?... *(Ans: B)*
- [Question 28](#q-28): `Module 6 · Integration & DevOps` - A malformed 'poison pill' message keeps failing and blocking an SQS qu... *(Ans: B)*
- [Question 29](#q-29): `Module 6 · Integration & DevOps` - What is the SQS visibility timeout?... *(Ans: B)*
- [Question 30](#q-30): `Module 6 · Integration & DevOps` - One 'order placed' event must be delivered simultaneously to a fulfilm... *(Ans: B)*
- [Question 31](#q-31): `Module 6 · Integration & DevOps` - You need to route events to different targets based on the content of ... *(Ans: C)*
- [Question 32](#q-32): `Module 6 · Integration & DevOps` - Which messaging service is pull-based (consumers retrieve messages) ra... *(Ans: B)*
- [Question 33](#q-33): `Module 6 · Integration & DevOps` - In an AWS CI/CD pipeline, which service compiles code, runs tests and ... *(Ans: B)*
- [Question 34](#q-34): `Module 6 · Integration & DevOps` - Which service automates deployments to EC2, Lambda or ECS using in-pla... *(Ans: C)*
- [Question 35](#q-35): `Module 6 · Integration & DevOps` - Which service orchestrates the overall CI/CD workflow (Source → Build ... *(Ans: C)*
- [Question 36](#q-36): `Module 6 · Integration & DevOps` - Which AWS-native, declarative Infrastructure-as-Code service uses JSON... *(Ans: C)*
- [Question 37](#q-37): `Module 6 · Integration & DevOps` - A team wants to define infrastructure using real programming languages... *(Ans: B)*
- [Question 38](#q-38): `Module 6 · Integration & DevOps` - Which IaC tool is third-party, cloud-agnostic, uses HCL, and maintains... *(Ans: C)*
- [Question 39](#q-39): `Module 6 · Integration & DevOps` - Which CloudWatch feature scans centralised logs for a pattern (e.g. 'E... *(Ans: B)*
- [Question 40](#q-40): `Module 6 · Integration & DevOps` - What is the CloudWatch automation chain that lets a system react to pr... *(Ans: B)*
- [Question 41](#q-41): `Module 6 · Integration & DevOps` - You must give administrators shell access to EC2 instances without ope... *(Ans: B)*
- [Question 42](#q-42): `Module 6 · Integration & DevOps` - Which Systems Manager capability provides secure, hierarchical storage... *(Ans: B)*
- [Question 43](#q-43): `Module 6 · Integration & DevOps` - Which Systems Manager capability automates OS/application patching aga... *(Ans: C)*
- [Question 44](#q-44): `Module 6 · Integration & DevOps` - A multi-step workflow needs sequencing, automatic retries with backoff... *(Ans: B)*
- [Question 45](#q-45): `Module 6 · Integration & DevOps` - Which scenario is best served by a single plain Lambda function rather... *(Ans: B)*
- [Question 46](#q-46): `Module 7 · AI/ML, Analytics & Migration` - Which AWS AI service analyses images and video for objects, faces, sce... *(Ans: B)*
- [Question 47](#q-47): `Module 7 · AI/ML, Analytics & Migration` - You need to extract text, forms and tables (key-value pairs) from scan... *(Ans: B)*
- [Question 48](#q-48): `Module 7 · AI/ML, Analytics & Migration` - Which service performs NLP tasks such as sentiment analysis, entity an... *(Ans: A)*
- [Question 49](#q-49): `Module 7 · AI/ML, Analytics & Migration` - Which service converts written text into lifelike speech (text-to-spee... *(Ans: B)*
- [Question 50](#q-50): `Module 7 · AI/ML, Analytics & Migration` - Which service produces speech-to-text transcripts with timestamps and ... *(Ans: B)*
- [Question 51](#q-51): `Module 7 · AI/ML, Analytics & Migration` - Which service is used to build the conversation flow of a voice/text c... *(Ans: A)*
- [Question 52](#q-52): `Module 7 · AI/ML, Analytics & Migration` - Which service gives real-time product recommendations on an e-commerce... *(Ans: B)*
- [Question 53](#q-53): `Module 7 · AI/ML, Analytics & Migration` - A company wants to detect fraud patterns unique to its own historical ... *(Ans: B)*
- [Question 54](#q-54): `Module 7 · AI/ML, Analytics & Migration` - In SageMaker, what do you pay for during model training?... *(Ans: B)*
- [Question 55](#q-55): `Module 7 · AI/ML, Analytics & Migration` - A team with no data scientists wants to build a custom model from tabu... *(Ans: A)*
- [Question 56](#q-56): `Module 7 · AI/ML, Analytics & Migration` - A custom, low-latency application must process each streaming record a... *(Ans: B)*
- [Question 57](#q-57): `Module 7 · AI/ML, Analytics & Migration` - You need a fully managed 'fire-and-forget' pipeline to load streaming ... *(Ans: B)*
- [Question 58](#q-58): `Module 7 · AI/ML, Analytics & Migration` - In a data lake, which service crawls raw S3 data to populate a catalog... *(Ans: B)*
- [Question 59](#q-59): `Module 7 · AI/ML, Analytics & Migration` - Which service runs serverless standard SQL directly against data in S3... *(Ans: B)*
- [Question 60](#q-60): `Module 7 · AI/ML, Analytics & Migration` - Which service provides no-code BI dashboards and reports for business ... *(Ans: B)*
- [Question 61](#q-61): `Module 7 · AI/ML, Analytics & Migration` - Analytics differ mainly by where the data lives. Which fits 'data stay... *(Ans: B)*
- [Question 62](#q-62): `Module 7 · AI/ML, Analytics & Migration` - A large-scale big-data job needs specific open-source frameworks (Spar... *(Ans: B)*
- [Question 63](#q-63): `Module 7 · AI/ML, Analytics & Migration` - Which migration service performs a lift-and-shift 'rehost' by continuo... *(Ans: B)*
- [Question 64](#q-64): `Module 7 · AI/ML, Analytics & Migration` - Which service migrates databases with a full load plus Change Data Cap... *(Ans: B)*
- [Question 65](#q-65): `Module 7 · AI/ML, Analytics & Migration` - You are moving from Oracle to PostgreSQL (a heterogeneous migration). ... *(Ans: A)*
- [Question 66](#q-66): `Module 7 · AI/ML, Analytics & Migration` - A petabyte-scale dataset must reach AWS but the network would take wee... *(Ans: B)*
- [Question 67](#q-67): `Module 7 · AI/ML, Analytics & Migration` - Which service provides automated, online transfer between on-prem NFS/... *(Ans: A)*
- [Question 68](#q-68): `Module 8 · Billing, Pricing & Support` - Which AWS Support plan is free and included with every account?... *(Ans: A)*
- [Question 69](#q-69): `Module 8 · Billing, Pricing & Support` - At which support plan do the FULL set of Trusted Advisor checks (all f... *(Ans: C)*
- [Question 70](#q-70): `Module 8 · Billing, Pricing & Support` - A mission-critical workload needs a dedicated Technical Account Manage... *(Ans: C)*
- [Question 71](#q-71): `Module 8 · Billing, Pricing & Support` - A small team needs business-hours email guidance from Cloud Support As... *(Ans: B)*
- [Question 72](#q-72): `Module 8 · Billing, Pricing & Support` - Which AWS tool is used to VISUALISE and investigate spend and usage ov... *(Ans: B)*
- [Question 73](#q-73): `Module 8 · Billing, Pricing & Support` - Which tool lets you set a cost or usage threshold and get alerted (or ... *(Ans: B)*
- [Question 74](#q-74): `Module 8 · Billing, Pricing & Support` - Which feature uses machine learning to automatically flag unusual spen... *(Ans: A)*
- [Question 75](#q-75): `Module 8 · Billing, Pricing & Support` - Which compute pricing model offers the deepest discount (up to ~90%) b... *(Ans: D)*
- [Question 76](#q-76): `Module 8 · Billing, Pricing & Support` - A steady workload needs discounts that stay flexible across instance f... *(Ans: B)*
- [Question 77](#q-77): `Module 8 · Billing, Pricing & Support` - Which pricing model is the flexible baseline with no commitment and th... *(Ans: A)*
- [Question 78](#q-78): `Module 8 · Billing, Pricing & Support` - Reserved Instances require what kind of commitment?... *(Ans: B)*
- [Question 79](#q-79): `Module 8 · Billing, Pricing & Support` - Which free tool (no AWS account needed) lets you build a cost estimate... *(Ans: B)*
- [Question 80](#q-80): `Module 8 · Billing, Pricing & Support` - A parent company wants ONE invoice covering all its subsidiary account... *(Ans: B)*
- [Question 81](#q-81): `Module 8 · Billing, Pricing & Support` - Under consolidated billing, how do Reserved Instance and Savings Plans... *(Ans: B)*
- [Question 82](#q-82): `Module 8 · Billing, Pricing & Support` - Activating which feature lets you break down spend by team or project ... *(Ans: A)*
- [Question 83](#q-83): `Module 8 · Billing, Pricing & Support` - Which Trusted Advisor category flags idle/underutilised EC2 instances ... *(Ans: C)*
- [Question 84](#q-84): `Module 8 · Billing, Pricing & Support` - Which Trusted Advisor category checks open security-group ports, root-... *(Ans: A)*
- [Question 85](#q-85): `Module 8 · Billing, Pricing & Support` - Which of these are the five Trusted Advisor check categories? (Choose ... *(Ans: A)*
- [Question 86](#q-86): `Module 8 · Billing, Pricing & Support` - When several answers technically work on CLF-C02, which framework is t... *(Ans: B)*
- [Question 87](#q-87): `Module 8 · Billing, Pricing & Support` - On the exam, qualifying phrases like 'LEAST operational overhead' or '... *(Ans: B)*
- [Question 88](#q-88): `Domain 1 · Cloud Concepts (24%)` - Which is a core financial benefit of cloud computing over a traditiona... *(Ans: A)*
- [Question 89](#q-89): `Domain 1 · Cloud Concepts (24%)` - 'Elasticity' in the AWS Cloud refers to:... *(Ans: B)*
- [Question 90](#q-90): `Domain 1 · Cloud Concepts (24%)` - Which benefit describes AWS's ability to deploy to new geographic Regi... *(Ans: A)*
- [Question 91](#q-91): `Domain 1 · Cloud Concepts (24%)` - How many pillars does the AWS Well-Architected Framework have, and whi... *(Ans: A)*
- [Question 92](#q-92): `Domain 1 · Cloud Concepts (24%)` - Which Well-Architected pillar focuses on running and monitoring system... *(Ans: A)*
- [Question 93](#q-93): `Domain 1 · Cloud Concepts (24%)` - A company runs part of its workload on-premises and part in AWS, conne... *(Ans: C)*
- [Question 94](#q-94): `Domain 1 · Cloud Concepts (24%)` - What is an AWS Availability Zone?... *(Ans: B)*
- [Question 95](#q-95): `Domain 1 · Cloud Concepts (24%)` - To build a highly available architecture, across what should you distr... *(Ans: A)*
- [Question 96](#q-96): `Domain 1 · Cloud Concepts (24%)` - What is the primary purpose of AWS edge locations / Amazon CloudFront?... *(Ans: B)*
- [Question 97](#q-97): `Domain 1 · Cloud Concepts (24%)` - The AWS Cloud Adoption Framework (CAF) is used to:... *(Ans: B)*
- [Question 98](#q-98): `Domain 1 · Cloud Concepts (24%)` - Which is an example of increased agility in the cloud?... *(Ans: B)*
- [Question 99](#q-99): `Domain 1 · Cloud Concepts (24%)` - 'Economies of scale' as an AWS benefit means:... *(Ans: B)*
- [Question 100](#q-100): `Domain 1 · Cloud Concepts (24%)` - Under the AWS shared responsibility model, which describes the split a... *(Ans: C)*
- [Question 101](#q-101): `Domain 1 · Cloud Concepts (24%)` - Which cloud characteristic lets you provision and release computing re... *(Ans: A)*
- [Question 102](#q-102): `Domain 1 · Cloud Concepts (24%)` - A start-up wants to avoid large up-front spending on servers it may no... *(Ans: A)*
- [Question 103](#q-103): `Domain 1 · Cloud Concepts (24%)` - Which Well-Architected pillar is specifically about using energy effic... *(Ans: A)*
- [Question 104](#q-104): `Domain 1 · Cloud Concepts (24%)` - Which statement about AWS Regions is correct?... *(Ans: B)*
- [Question 105](#q-105): `Domain 1 · Cloud Concepts (24%)` - Which is a valid reason to choose a particular AWS Region for a worklo... *(Ans: A)*
- [Question 106](#q-106): `Domain 1 · Cloud Concepts (24%)` - Reliability, as a Well-Architected pillar, primarily ensures a workloa... *(Ans: B)*
- [Question 107](#q-107): `Domain 1 · Cloud Concepts (24%)` - Which is an example of loose coupling improving reliability in a cloud... *(Ans: B)*
- [Question 108](#q-108): `Domain 2 · Security & Compliance (30%)` - Under the shared responsibility model, which task is ALWAYS the custom... *(Ans: C)*
- [Question 109](#q-109): `Domain 2 · Security & Compliance (30%)` - For Amazon EC2 (IaaS), who is responsible for patching the guest opera... *(Ans: B)*
- [Question 110](#q-110): `Domain 2 · Security & Compliance (30%)` - What is the recommended way to grant an application running on EC2 acc... *(Ans: B)*
- [Question 111](#q-111): `Domain 2 · Security & Compliance (30%)` - Which is an AWS security best practice for the root user of an account... *(Ans: B)*
- [Question 112](#q-112): `Domain 2 · Security & Compliance (30%)` - What does the principle of least privilege mean in IAM?... *(Ans: B)*
- [Question 113](#q-113): `Domain 2 · Security & Compliance (30%)` - Which IAM entity is best for granting temporary permissions that can b... *(Ans: B)*
- [Question 114](#q-114): `Domain 2 · Security & Compliance (30%)` - Which AWS service protects web applications against common exploits su... *(Ans: A)*
- [Question 115](#q-115): `Domain 2 · Security & Compliance (30%)` - Which AWS service provides managed DDoS protection?... *(Ans: A)*
- [Question 116](#q-116): `Domain 2 · Security & Compliance (30%)` - Which service is an intelligent threat-detection service that continuo... *(Ans: A)*
- [Question 117](#q-117): `Domain 2 · Security & Compliance (30%)` - Which service uses machine learning to discover and protect sensitive ... *(Ans: A)*
- [Question 118](#q-118): `Domain 2 · Security & Compliance (30%)` - Which service performs automated vulnerability assessments of EC2 inst... *(Ans: A)*
- [Question 119](#q-119): `Domain 2 · Security & Compliance (30%)` - Which service creates and manages cryptographic keys and integrates wi... *(Ans: A)*
- [Question 120](#q-120): `Domain 2 · Security & Compliance (30%)` - Which service securely stores database credentials and API keys and ca... *(Ans: A)*
- [Question 121](#q-121): `Domain 2 · Security & Compliance (30%)` - Which service records API calls and account activity for auditing and ... *(Ans: B)*
- [Question 122](#q-122): `Domain 2 · Security & Compliance (30%)` - Which service continuously records resource configurations and evaluat... *(Ans: A)*
- [Question 123](#q-123): `Domain 2 · Security & Compliance (30%)` - Where can you download AWS compliance reports such as SOC and ISO cert... *(Ans: A)*
- [Question 124](#q-124): `Domain 2 · Security & Compliance (30%)` - An organisation wants to centrally restrict which services member acco... *(Ans: A)*
- [Question 125](#q-125): `Domain 2 · Security & Compliance (30%)` - By default, how is data in a new Amazon S3 bucket exposed to the publi... *(Ans: B)*
- [Question 126](#q-126): `Domain 2 · Security & Compliance (30%)` - Which pair correctly maps a control to what it protects?... *(Ans: A)*
- [Question 127](#q-127): `Domain 2 · Security & Compliance (30%)` - Which security service acts as a single dashboard aggregating and prio... *(Ans: A)*
- [Question 128](#q-128): `Domain 2 · Security & Compliance (30%)` - Which network control acts as a stateful virtual firewall at the insta... *(Ans: A)*
- [Question 129](#q-129): `Domain 2 · Security & Compliance (30%)` - To require a second factor beyond a password when signing in, a user s... *(Ans: A)*
- [Question 130](#q-130): `Domain 2 · Security & Compliance (30%)` - An IAM policy is best described as:... *(Ans: A)*
- [Question 131](#q-131): `Domain 2 · Security & Compliance (30%)` - Which is the correct way to give three new developers the same set of ... *(Ans: A)*
- [Question 132](#q-132): `Domain 2 · Security & Compliance (30%)` - Which statement about AWS-managed encryption at rest is correct by def... *(Ans: B)*
- [Question 133](#q-133): `Domain 3 · Cloud Technology & Services (34%)` - Which AWS service provides resizable virtual servers in the cloud?... *(Ans: A)*
- [Question 134](#q-134): `Domain 3 · Cloud Technology & Services (34%)` - Which compute service runs your code without provisioning or managing ... *(Ans: B)*
- [Question 135](#q-135): `Domain 3 · Cloud Technology & Services (34%)` - A team wants to run Docker containers without managing the underlying ... *(Ans: A)*
- [Question 136](#q-136): `Domain 3 · Cloud Technology & Services (34%)` - Which service is object storage for virtually unlimited data, accessed... *(Ans: B)*
- [Question 137](#q-137): `Domain 3 · Cloud Technology & Services (34%)` - Which service is a managed relational database supporting engines like... *(Ans: B)*
- [Question 138](#q-138): `Domain 3 · Cloud Technology & Services (34%)` - Which service is a fully managed NoSQL key-value database with single-... *(Ans: B)*
- [Question 139](#q-139): `Domain 3 · Cloud Technology & Services (34%)` - Which service is a content delivery network (CDN) that caches content ... *(Ans: A)*
- [Question 140](#q-140): `Domain 3 · Cloud Technology & Services (34%)` - Which service is a scalable Domain Name System (DNS) web service?... *(Ans: A)*
- [Question 141](#q-141): `Domain 3 · Cloud Technology & Services (34%)` - What is an Amazon VPC?... *(Ans: A)*
- [Question 142](#q-142): `Domain 3 · Cloud Technology & Services (34%)` - Which service provides a dedicated, private physical network connectio... *(Ans: A)*
- [Question 143](#q-143): `Domain 3 · Cloud Technology & Services (34%)` - Which service distributes incoming application traffic across multiple... *(Ans: A)*
- [Question 144](#q-144): `Domain 3 · Cloud Technology & Services (34%)` - Which service automatically adjusts the number of EC2 instances to mat... *(Ans: A)*
- [Question 145](#q-145): `Domain 3 · Cloud Technology & Services (34%)` - A workload needs a message queue to decouple components so consumers p... *(Ans: A)*
- [Question 146](#q-146): `Domain 3 · Cloud Technology & Services (34%)` - Which service delivers one published message to many subscribers (pub/... *(Ans: A)*
- [Question 147](#q-147): `Domain 3 · Cloud Technology & Services (34%)` - Which service lets you provision your entire infrastructure from JSON/... *(Ans: A)*
- [Question 148](#q-148): `Domain 3 · Cloud Technology & Services (34%)` - Which service collects metrics, logs and alarms to monitor AWS resourc... *(Ans: A)*
- [Question 149](#q-149): `Domain 3 · Cloud Technology & Services (34%)` - A developer wants a simple, low-cost way to run a small website or app... *(Ans: A)*
- [Question 150](#q-150): `Domain 3 · Cloud Technology & Services (34%)` - Which service lets you deploy and manage a web application without dea... *(Ans: A)*
- [Question 151](#q-151): `Domain 3 · Cloud Technology & Services (34%)` - Which service runs serverless SQL queries directly against data stored... *(Ans: A)*
- [Question 152](#q-152): `Domain 3 · Cloud Technology & Services (34%)` - Which service is a petabyte-scale data warehouse for complex analytica... *(Ans: A)*
- [Question 153](#q-153): `Domain 3 · Cloud Technology & Services (34%)` - A shared file system that many EC2 instances can mount simultaneously ... *(Ans: A)*
- [Question 154](#q-154): `Domain 3 · Cloud Technology & Services (34%)` - Which service ingests and processes real-time streaming data such as c... *(Ans: A)*
- [Question 155](#q-155): `Domain 3 · Cloud Technology & Services (34%)` - Which pre-built AI service extracts text and data from scanned documen... *(Ans: A)*
- [Question 156](#q-156): `Domain 3 · Cloud Technology & Services (34%)` - Which fully managed platform is used to build, train and deploy custom... *(Ans: A)*
- [Question 157](#q-157): `Domain 3 · Cloud Technology & Services (34%)` - Which physical device transfers very large datasets to AWS when the ne... *(Ans: A)*
- [Question 158](#q-158): `Domain 3 · Cloud Technology & Services (34%)` - Which service enables interactive, no-code BI dashboards for business ... *(Ans: A)*
- [Question 159](#q-159): `Domain 3 · Cloud Technology & Services (34%)` - Which storage option provides persistent block storage for a single EC... *(Ans: A)*
- [Question 160](#q-160): `Domain 3 · Cloud Technology & Services (34%)` - Which service orchestrates multi-step, serverless workflows as visual ... *(Ans: A)*
- [Question 161](#q-161): `Domain 3 · Cloud Technology & Services (34%)` - Which service provides managed publish/subscribe messaging AND which p... *(Ans: A)*
- [Question 162](#q-162): `Domain 3 · Cloud Technology & Services (34%)` - A gaming company needs global users to reach the nearest healthy appli... *(Ans: A)*
- [Question 163](#q-163): `Domain 4 · Billing, Pricing & Support (12%)` - Which pricing model gives the biggest discount but can be interrupted ... *(Ans: A)*
- [Question 164](#q-164): `Domain 4 · Billing, Pricing & Support (12%)` - Which support plan is required to get the FULL set of Trusted Advisor ... *(Ans: A)*
- [Question 165](#q-165): `Domain 4 · Billing, Pricing & Support (12%)` - Which tool lets you set a spending threshold and receive an alert when... *(Ans: A)*
- [Question 166](#q-166): `Domain 4 · Billing, Pricing & Support (12%)` - Which capability lets a company receive a single consolidated bill for... *(Ans: A)*
- [Question 167](#q-167): `Domain 4 · Billing, Pricing & Support (12%)` - A dedicated Technical Account Manager (TAM) is included with which AWS... *(Ans: A)*
- [Question 168](#q-168): `Domain 4 · Billing, Pricing & Support (12%)` - Which free tool estimates the cost of a proposed AWS architecture befo... *(Ans: A)*
- [Question 169](#q-169): `Domain 4 · Billing, Pricing & Support (12%)` - Which service helps you visualise, understand and investigate your pas... *(Ans: A)*
- [Question 170](#q-170): `Domain 4 · Billing, Pricing & Support (12%)` - A steady, long-running workload wants savings while staying flexible a... *(Ans: A)*
- [Question 171](#q-171): `Domain 4 · Billing, Pricing & Support (12%)` - Under the AWS Free Tier, which category is NOT one of its three types?... *(Ans: A)*
- [Question 172](#q-172): `Domain 4 · Billing, Pricing & Support (12%)` - Which Trusted Advisor category checks whether you are approaching AWS ... *(Ans: A)*
- [Question 173](#q-173): `Domain 4 · Billing, Pricing & Support (12%)` - Which support plan offers a response time target of under 1 hour for p... *(Ans: A)*
- [Question 174](#q-174): `Domain 4 · Billing, Pricing & Support (12%)` - Which statement about On-Demand pricing is correct?... *(Ans: A)*

---

<a id="q-1"></a>

### Question 1

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-001`

> **Scenario:**  
> An EC2 instance is named m5.large. What does the letter 'm' indicate?

#### Options
- **A.** The generation
- **B.** The instance family **[CORRECT]**
- **C.** The size
- **D.** The Region

**Correct Answer:** `B`

#### Explanation & Rationale

In m5.large, 'm' is the family (general purpose), '5' is the generation, and 'large' is the size.

---

<a id="q-2"></a>

### Question 2

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-002`

> **Scenario:**  
> A workload does sustained, consistently heavy CPU processing (media transcoding). Which EC2 instance family fits best?

#### Options
- **A.** T family (burstable)
- **B.** C family (compute optimised) **[CORRECT]**
- **C.** R family (memory optimised)
- **D.** I family (storage optimised)

**Correct Answer:** `B`

#### Explanation & Rationale

Sustained high CPU maps to the Compute-optimised C family; the T family is for bursty, mostly-idle workloads.

---

<a id="q-3"></a>

### Question 3

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-003`

> **Scenario:**  
> An in-memory database such as Redis or SAP HANA needs a large amount of RAM per vCPU. Which instance family is designed for this?

#### Options
- **A.** General purpose (M)
- **B.** Compute optimised (C)
- **C.** Memory optimised (R, X, z1d) **[CORRECT]**
- **D.** Accelerated (P, G)

**Correct Answer:** `C`

#### Explanation & Rationale

Memory-optimised families (R, X, z1d) offer a high memory-to-CPU ratio for large caches and in-memory databases.

---

<a id="q-4"></a>

### Question 4

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-004`

> **Scenario:**  
> A small web app is mostly idle but occasionally spikes. Which EC2 family is the most cost-effective match?

#### Options
- **A.** T family (burstable) **[CORRECT]**
- **B.** C family
- **C.** R family
- **D.** P family

**Correct Answer:** `A`

#### Explanation & Rationale

T-family burstable instances earn CPU credits while idle and spend them to burst — ideal for unpredictable spikes with low average utilisation.

---

<a id="q-5"></a>

### Question 5

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-005`

> **Scenario:**  
> How do burstable (T family) instances handle CPU above their baseline?

#### Options
- **A.** They throttle to zero
- **B.** They earn CPU credits while idle and spend them to burst **[CORRECT]**
- **C.** They automatically switch to a C instance
- **D.** They add more vCPUs permanently

**Correct Answer:** `B`

#### Explanation & Rationale

T instances accumulate CPU credits during idle periods and consume them to burst above baseline.

---

<a id="q-6"></a>

### Question 6

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-006`

> **Scenario:**  
> Which storage option provides the highest IOPS and lowest latency but loses its data when the instance stops or is terminated?

#### Options
- **A.** Amazon EBS
- **B.** Instance store **[CORRECT]**
- **C.** Amazon EFS
- **D.** Amazon S3

**Correct Answer:** `B`

#### Explanation & Rationale

Instance store is local NVMe on the host — fastest, but ephemeral: data is lost on stop/terminate (it survives a reboot).

---

<a id="q-7"></a>

### Question 7

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-007`

> **Scenario:**  
> A single EC2 instance needs a persistent boot volume that survives reboots and can be snapshotted. Which service is appropriate?

#### Options
- **A.** Instance store
- **B.** Amazon EBS **[CORRECT]**
- **C.** Amazon EFS
- **D.** Amazon S3

**Correct Answer:** `B`

#### Explanation & Rationale

EBS is network-attached block storage that persists independently of the instance and snapshots to S3.

---

<a id="q-8"></a>

### Question 8

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-008`

> **Scenario:**  
> Thousands of EC2 instances across multiple Availability Zones must read and write the same POSIX file system simultaneously. Which service fits?

#### Options
- **A.** Amazon EBS
- **B.** Instance store
- **C.** Amazon EFS **[CORRECT]**
- **D.** Amazon S3

**Correct Answer:** `C`

#### Explanation & Rationale

EFS is a managed shared file system mounted by many instances across AZs, scaling capacity automatically.

---

<a id="q-9"></a>

### Question 9

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-009`

> **Scenario:**  
> Which statement about Amazon S3 durability is correct?

#### Options
- **A.** It offers 99% durability in a single AZ
- **B.** It offers 11 nines of durability across multiple AZs **[CORRECT]**
- **C.** Durability depends on the instance type
- **D.** Objects are stored on a single disk

**Correct Answer:** `B`

#### Explanation & Rationale

S3 provides eleven 9s (99.999999999%) of durability by replicating objects across multiple AZs.

---

<a id="q-10"></a>

### Question 10

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-010`

> **Scenario:**  
> Data is temporary, already replicated elsewhere, and needs the absolute fastest I/O. Which storage type is the engineer's choice?

#### Options
- **A.** Instance store **[CORRECT]**
- **B.** EBS gp3
- **C.** EFS
- **D.** S3 Standard

**Correct Answer:** `A`

#### Explanation & Rationale

When data is disposable/replicated and needs maximum I/O, instance store is chosen despite being ephemeral.

---

<a id="q-11"></a>

### Question 11

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-011`

> **Scenario:**  
> Which S3 storage class automatically moves objects between access tiers as usage changes, with no operational effort?

#### Options
- **A.** S3 Standard
- **B.** S3 Intelligent-Tiering **[CORRECT]**
- **C.** S3 One Zone-IA
- **D.** S3 Glacier Deep Archive

**Correct Answer:** `B`

#### Explanation & Rationale

S3 Intelligent-Tiering auto-moves objects between tiers based on changing access patterns — ideal for unknown/changing patterns.

---

<a id="q-12"></a>

### Question 12

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-012`

> **Scenario:**  
> Archived data is rarely accessed (e.g. quarterly) but must still be retrievable in milliseconds when needed. Which class fits?

#### Options
- **A.** S3 Standard-IA
- **B.** S3 Glacier Instant Retrieval **[CORRECT]**
- **C.** S3 Glacier Flexible Retrieval
- **D.** S3 Glacier Deep Archive

**Correct Answer:** `B`

#### Explanation & Rationale

'Instantly/immediately' + 'rarely accessed' points to Glacier Instant Retrieval, which keeps millisecond retrieval.

---

<a id="q-13"></a>

### Question 13

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-013`

> **Scenario:**  
> Which S3 storage class is the cheapest and is designed for 7–10+ year compliance data with retrieval times up to 12 hours?

#### Options
- **A.** S3 Standard-IA
- **B.** S3 Glacier Flexible Retrieval
- **C.** S3 Glacier Deep Archive **[CORRECT]**
- **D.** S3 Intelligent-Tiering

**Correct Answer:** `C`

#### Explanation & Rationale

Glacier Deep Archive is the lowest-cost class, with retrieval up to ~12 hours — for long-term compliance archives.

---

<a id="q-14"></a>

### Question 14

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-014`

> **Scenario:**  
> What do S3 Lifecycle policies let you do without writing any application code?

#### Options
- **A.** Encrypt objects with customer keys
- **B.** Transition and expire objects automatically by age **[CORRECT]**
- **C.** Replicate a bucket to another account
- **D.** Serve objects through a CDN

**Correct Answer:** `B`

#### Explanation & Rationale

Lifecycle rules configured on a bucket/prefix transition objects between classes and expire them based on age — no code.

---

<a id="q-15"></a>

### Question 15

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-015`

> **Scenario:**  
> Which AWS database service is a relational engine supporting MySQL, PostgreSQL, MariaDB, SQL Server and Oracle?

#### Options
- **A.** Amazon DynamoDB
- **B.** Amazon RDS **[CORRECT]**
- **C.** Amazon Redshift
- **D.** Amazon ElastiCache

**Correct Answer:** `B`

#### Explanation & Rationale

Amazon RDS is the managed relational service supporting those five engines.

---

<a id="q-16"></a>

### Question 16

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-016`

> **Scenario:**  
> A workload needs massive, key-based throughput with single-digit-millisecond latency and virtually unlimited scale. Which database fits?

#### Options
- **A.** Amazon RDS
- **B.** Amazon Aurora
- **C.** Amazon DynamoDB **[CORRECT]**
- **D.** Amazon Redshift

**Correct Answer:** `C`

#### Explanation & Rationale

DynamoDB is a serverless NoSQL key-value/document store delivering single-digit-ms latency at any scale.

---

<a id="q-17"></a>

### Question 17

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-017`

> **Scenario:**  
> Analysts need to run complex analytical queries across years of historical data. Which purpose-built service is designed for this (OLAP)?

#### Options
- **A.** Amazon DynamoDB
- **B.** Amazon Redshift **[CORRECT]**
- **C.** Amazon ElastiCache
- **D.** Amazon RDS

**Correct Answer:** `B`

#### Explanation & Rationale

Redshift is a columnar data-warehouse (OLAP) service for complex analytics over large historical datasets.

---

<a id="q-18"></a>

### Question 18

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-018`

> **Scenario:**  
> You want to reduce load on a relational database by serving repeated reads from a sub-millisecond in-memory layer. Which service?

#### Options
- **A.** Amazon Redshift
- **B.** Amazon ElastiCache **[CORRECT]**
- **C.** Amazon Aurora
- **D.** Amazon S3

**Correct Answer:** `B`

#### Explanation & Rationale

ElastiCache (Redis/Memcached) provides a sub-millisecond caching layer that shields the primary database from repeated reads.

---

<a id="q-19"></a>

### Question 19

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-019`

> **Scenario:**  
> Which is an advantage of Amazon Aurora over standard Amazon RDS?

#### Options
- **A.** It supports Oracle and SQL Server
- **B.** Up to 15 read replicas with lower replication lag **[CORRECT]**
- **C.** It is the cheapest option for all workloads
- **D.** It requires no storage at all

**Correct Answer:** `B`

#### Explanation & Rationale

Aurora supports up to 15 read replicas (RDS: 5) with single-digit-ms replication lag and faster failover.

---

<a id="q-20"></a>

### Question 20

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-020`

> **Scenario:**  
> Aurora stores how many copies of your data, and across how many Availability Zones?

#### Options
- **A.** 3 copies across 2 AZs
- **B.** 6 copies across 3 AZs **[CORRECT]**
- **C.** 2 copies across 1 AZ
- **D.** 10 copies across 5 AZs

**Correct Answer:** `B`

#### Explanation & Rationale

Aurora's shared distributed storage layer keeps 6 copies of data across 3 Availability Zones.

---

<a id="q-21"></a>

### Question 21

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-021`

> **Scenario:**  
> A dev/test database has intermittent, spiky traffic and you want the most cost-effective option that scales capacity automatically. Which fits?

#### Options
- **A.** Aurora Serverless v2 **[CORRECT]**
- **B.** A large Redshift cluster
- **C.** Provisioned RDS with max instance size
- **D.** Instance store on EC2

**Correct Answer:** `A`

#### Explanation & Rationale

Aurora Serverless v2 scales capacity in fine-grained steps for intermittent/spiky loads — 'intermittent traffic, most cost-effective'.

---

<a id="q-22"></a>

### Question 22

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-022`

> **Scenario:**  
> Which Auto Scaling policy works like a thermostat — you set a metric target (e.g. 'keep average CPU at 50%') and the group holds it?

#### Options
- **A.** Step scaling
- **B.** Target tracking **[CORRECT]**
- **C.** Scheduled scaling
- **D.** Manual scaling

**Correct Answer:** `B`

#### Explanation & Rationale

Target tracking maintains a chosen metric at a target value; it is the most common ASG policy.

---

<a id="q-23"></a>

### Question 23

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-023`

> **Scenario:**  
> You know traffic peaks every weekday at 9 a.m. and want to raise capacity just before that time. Which scaling policy is best?

#### Options
- **A.** Target tracking
- **B.** Step scaling
- **C.** Scheduled scaling **[CORRECT]**
- **D.** Spot scaling

**Correct Answer:** `C`

#### Explanation & Rationale

Scheduled scaling changes capacity at known times, ahead of predictable peaks.

---

<a id="q-24"></a>

### Question 24

**Set:** `Practice Exam 1` | **Domain:** `Module 5 · Compute, Storage & Databases` | **ID:** `aws-practice-1-024`

> **Scenario:**  
> What is the canonical AWS answer for elastic, self-healing, highly available compute across multiple AZs?

#### Options
- **A.** A single large EC2 instance
- **B.** An Auto Scaling Group behind an Elastic Load Balancer **[CORRECT]**
- **C.** Instance store volumes
- **D.** A Redshift cluster

**Correct Answer:** `B`

#### Explanation & Rationale

ASG + Elastic Load Balancer across AZs gives elastic, self-healing, highly available compute.

---

<a id="q-25"></a>

### Question 25

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-025`

> **Scenario:**  
> What problem does Amazon SQS primarily solve?

#### Options
- **A.** It encrypts data at rest
- **B.** It decouples producers from consumers so a slow/failed consumer doesn't drag the producer down **[CORRECT]**
- **C.** It provides a relational database
- **D.** It runs container images

**Correct Answer:** `B`

#### Explanation & Rationale

SQS breaks tight coupling: producers send and move on; consumers process at their own pace; messages wait safely.

---

<a id="q-26"></a>

### Question 26

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-026`

> **Scenario:**  
> A banking workload must process messages exactly once and in strict order within a group. Which SQS queue type is required?

#### Options
- **A.** Standard queue
- **B.** FIFO queue **[CORRECT]**
- **C.** Dead-letter queue
- **D.** Priority queue

**Correct Answer:** `B`

#### Explanation & Rationale

FIFO queues give exactly-once processing and strict first-in-first-out ordering within a message group.

---

<a id="q-27"></a>

### Question 27

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-027`

> **Scenario:**  
> A Standard SQS queue offers which delivery and ordering guarantees?

#### Options
- **A.** Exactly-once, strict ordering
- **B.** At-least-once delivery, best-effort ordering **[CORRECT]**
- **C.** At-most-once, no duplicates
- **D.** Exactly-once, no ordering

**Correct Answer:** `B`

#### Explanation & Rationale

Standard queues provide at-least-once delivery with best-effort ordering and near-unlimited throughput — make processing idempotent.

---

<a id="q-28"></a>

### Question 28

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-028`

> **Scenario:**  
> A malformed 'poison pill' message keeps failing and blocking an SQS queue. What should you configure?

#### Options
- **A.** A larger visibility timeout only
- **B.** A dead-letter queue (DLQ) **[CORRECT]**
- **C.** A FIFO queue
- **D.** An SNS topic

**Correct Answer:** `B`

#### Explanation & Rationale

A DLQ receives messages that fail a defined number of times, moving them aside so healthy messages keep flowing.

---

<a id="q-29"></a>

### Question 29

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-029`

> **Scenario:**  
> What is the SQS visibility timeout?

#### Options
- **A.** The time a queue can hold a message before deletion
- **B.** The period a retrieved message is hidden from other consumers until deleted or it reappears **[CORRECT]**
- **C.** The maximum message size
- **D.** The delay before a message is first delivered

**Correct Answer:** `B`

#### Explanation & Rationale

When a consumer retrieves a message SQS hides it for a set period; if not deleted in time it reappears — enabling at-least-once delivery.

---

<a id="q-30"></a>

### Question 30

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-030`

> **Scenario:**  
> One 'order placed' event must be delivered simultaneously to a fulfilment queue, an analytics queue and an email Lambda, with the publisher unaware of them. Which service fits?

#### Options
- **A.** Amazon SQS
- **B.** Amazon SNS **[CORRECT]**
- **C.** AWS Step Functions
- **D.** Amazon RDS

**Correct Answer:** `B`

#### Explanation & Rationale

SNS is push-based pub/sub fan-out: one message to a topic is delivered to every subscriber.

---

<a id="q-31"></a>

### Question 31

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-031`

> **Scenario:**  
> You need to route events to different targets based on the content of the event payload (e.g. status = FAILED vs COMPLETED). Which service is designed for this?

#### Options
- **A.** Amazon SQS
- **B.** Amazon SNS
- **C.** Amazon EventBridge **[CORRECT]**
- **D.** Amazon EFS

**Correct Answer:** `C`

#### Explanation & Rationale

EventBridge does content-based routing on an event bus, plus scheduled (cron-like) rules and many AWS integrations.

---

<a id="q-32"></a>

### Question 32

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-032`

> **Scenario:**  
> Which messaging service is pull-based (consumers retrieve messages) rather than push-based?

#### Options
- **A.** Amazon SNS
- **B.** Amazon SQS **[CORRECT]**
- **C.** Amazon EventBridge
- **D.** Amazon Polly

**Correct Answer:** `B`

#### Explanation & Rationale

SQS is point-to-point and pull-based; SNS and EventBridge are push-based.

---

<a id="q-33"></a>

### Question 33

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-033`

> **Scenario:**  
> In an AWS CI/CD pipeline, which service compiles code, runs tests and produces deployable artifacts in temporary build environments?

#### Options
- **A.** CodeCommit
- **B.** CodeBuild **[CORRECT]**
- **C.** CodeDeploy
- **D.** CodePipeline

**Correct Answer:** `B`

#### Explanation & Rationale

CodeBuild builds/compiles/tests and outputs artifacts in auto-scaling, temporary environments — no build server to maintain.

---

<a id="q-34"></a>

### Question 34

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-034`

> **Scenario:**  
> Which service automates deployments to EC2, Lambda or ECS using in-place, blue/green and canary strategies?

#### Options
- **A.** CodeCommit
- **B.** CodeBuild
- **C.** CodeDeploy **[CORRECT]**
- **D.** CloudFormation

**Correct Answer:** `C`

#### Explanation & Rationale

CodeDeploy handles the deployment stage with in-place, blue/green and canary strategies.

---

<a id="q-35"></a>

### Question 35

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-035`

> **Scenario:**  
> Which service orchestrates the overall CI/CD workflow (Source → Build → Test → Deploy) and can add manual approval gates?

#### Options
- **A.** CodeBuild
- **B.** CodeDeploy
- **C.** CodePipeline **[CORRECT]**
- **D.** CodeCommit

**Correct Answer:** `C`

#### Explanation & Rationale

CodePipeline defines the stages, invokes the other tools in order, and adds approval gates.

---

<a id="q-36"></a>

### Question 36

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-036`

> **Scenario:**  
> Which AWS-native, declarative Infrastructure-as-Code service uses JSON/YAML templates and offers drift detection?

#### Options
- **A.** AWS CDK
- **B.** Terraform
- **C.** AWS CloudFormation **[CORRECT]**
- **D.** AWS CodeBuild

**Correct Answer:** `C`

#### Explanation & Rationale

CloudFormation is the AWS-native declarative IaC service; drift detection flags manual changes that diverge from the template.

---

<a id="q-37"></a>

### Question 37

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-037`

> **Scenario:**  
> A team wants to define infrastructure using real programming languages like Python or TypeScript, with loops and reusable constructs. Which tool fits?

#### Options
- **A.** AWS CloudFormation
- **B.** AWS CDK **[CORRECT]**
- **C.** AWS Budgets
- **D.** Amazon Athena

**Correct Answer:** `B`

#### Explanation & Rationale

The AWS CDK lets you define infra in real languages; it synthesises into a CloudFormation template under the hood.

---

<a id="q-38"></a>

### Question 38

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-038`

> **Scenario:**  
> Which IaC tool is third-party, cloud-agnostic, uses HCL, and maintains its own state file separate from AWS?

#### Options
- **A.** CloudFormation
- **B.** AWS CDK
- **C.** Terraform **[CORRECT]**
- **D.** CodeDeploy

**Correct Answer:** `C`

#### Explanation & Rationale

HashiCorp Terraform uses HCL, works across clouds via providers, and keeps its own state file — best for multi-cloud consistency.

---

<a id="q-39"></a>

### Question 39

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-039`

> **Scenario:**  
> Which CloudWatch feature scans centralised logs for a pattern (e.g. 'ERROR') and turns matches into a metric that can trigger an alarm?

#### Options
- **A.** A dashboard
- **B.** A metric filter **[CORRECT]**
- **C.** A canary
- **D.** A budget

**Correct Answer:** `B`

#### Explanation & Rationale

A CloudWatch Logs metric filter matches a log pattern and produces a metric that alarms can watch.

---

<a id="q-40"></a>

### Question 40

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-040`

> **Scenario:**  
> What is the CloudWatch automation chain that lets a system react to problems without a human?

#### Options
- **A.** Log → dashboard → email
- **B.** Metric → alarm → SNS / Auto Scaling / Lambda **[CORRECT]**
- **C.** Budget → anomaly → report
- **D.** Metric → snapshot → archive

**Correct Answer:** `B`

#### Explanation & Rationale

A metric feeds an alarm which triggers SNS, Auto Scaling, or an EventBridge/Lambda action — automated reaction.

---

<a id="q-41"></a>

### Question 41

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-041`

> **Scenario:**  
> You must give administrators shell access to EC2 instances without opening port 22/3389 or managing SSH keys. Which Systems Manager capability fits?

#### Options
- **A.** Parameter Store
- **B.** Session Manager **[CORRECT]**
- **C.** Patch Manager
- **D.** EventBridge

**Correct Answer:** `B`

#### Explanation & Rationale

SSM Session Manager provides shell access via IAM with no open inbound ports or key pairs — a frequently tested fact.

---

<a id="q-42"></a>

### Question 42

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-042`

> **Scenario:**  
> Which Systems Manager capability provides secure, hierarchical storage for configuration values and secrets (encrypted with KMS) retrieved at runtime?

#### Options
- **A.** Session Manager
- **B.** Parameter Store **[CORRECT]**
- **C.** Patch Manager
- **D.** Step Functions

**Correct Answer:** `B`

#### Explanation & Rationale

SSM Parameter Store holds connection strings, API keys and flags, KMS-encrypted, so credentials aren't hard-coded.

---

<a id="q-43"></a>

### Question 43

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-043`

> **Scenario:**  
> Which Systems Manager capability automates OS/application patching against defined baselines and maintenance windows?

#### Options
- **A.** Parameter Store
- **B.** Session Manager
- **C.** Patch Manager **[CORRECT]**
- **D.** CloudFormation

**Correct Answer:** `C`

#### Explanation & Rationale

SSM Patch Manager automates patching against baselines/maintenance windows — the customer's guest-OS patching duty.

---

<a id="q-44"></a>

### Question 44

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-044`

> **Scenario:**  
> A multi-step workflow needs sequencing, automatic retries with backoff, conditional branching, human-approval steps and a visual view of progress. Which service fits?

#### Options
- **A.** Plain AWS Lambda
- **B.** AWS Step Functions **[CORRECT]**
- **C.** Amazon SQS
- **D.** Amazon SNS

**Correct Answer:** `B`

#### Explanation & Rationale

Step Functions defines a state machine (Amazon States Language) with built-in sequencing, retries, branching and a visual graph.

---

<a id="q-45"></a>

### Question 45

**Set:** `Practice Exam 1` | **Domain:** `Module 6 · Integration & DevOps` | **ID:** `aws-practice-1-045`

> **Scenario:**  
> Which scenario is best served by a single plain Lambda function rather than Step Functions?

#### Options
- **A.** A multi-step order-fulfilment process with approvals
- **B.** A single function reacting to a single event **[CORRECT]**
- **C.** A workflow needing visual progress tracking
- **D.** A long-running process exceeding Lambda's duration limit

**Correct Answer:** `B`

#### Explanation & Rationale

A single function reacting to a single event is plain Lambda; multi-step orchestrated workflows call for Step Functions.

---

<a id="q-46"></a>

### Question 46

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-046`

> **Scenario:**  
> Which AWS AI service analyses images and video for objects, faces, scenes and content moderation?

#### Options
- **A.** Amazon Textract
- **B.** Amazon Rekognition **[CORRECT]**
- **C.** Amazon Comprehend
- **D.** Amazon Polly

**Correct Answer:** `B`

#### Explanation & Rationale

Rekognition handles general image/video content analysis, including content moderation.

---

<a id="q-47"></a>

### Question 47

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-047`

> **Scenario:**  
> You need to extract text, forms and tables (key-value pairs) from scanned or handwritten documents. Which service fits best?

#### Options
- **A.** Amazon Rekognition
- **B.** Amazon Textract **[CORRECT]**
- **C.** Amazon Translate
- **D.** Amazon Lex

**Correct Answer:** `B`

#### Explanation & Rationale

Textract extracts text, forms and tables from documents — the classic distractor against Rekognition (general images).

---

<a id="q-48"></a>

### Question 48

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-048`

> **Scenario:**  
> Which service performs NLP tasks such as sentiment analysis, entity and key-phrase extraction — e.g. classifying support tickets by tone?

#### Options
- **A.** Amazon Comprehend **[CORRECT]**
- **B.** Amazon Polly
- **C.** Amazon Transcribe
- **D.** Amazon Forecast

**Correct Answer:** `A`

#### Explanation & Rationale

Comprehend is the NLP service for sentiment, entities, key phrases and language detection.

---

<a id="q-49"></a>

### Question 49

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-049`

> **Scenario:**  
> Which service converts written text into lifelike speech (text-to-speech)?

#### Options
- **A.** Amazon Transcribe
- **B.** Amazon Polly **[CORRECT]**
- **C.** Amazon Lex
- **D.** Amazon Comprehend

**Correct Answer:** `B`

#### Explanation & Rationale

Polly is text-to-speech; Transcribe is the reverse (speech-to-text).

---

<a id="q-50"></a>

### Question 50

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-050`

> **Scenario:**  
> Which service produces speech-to-text transcripts with timestamps and speaker identification (e.g. searchable call transcripts)?

#### Options
- **A.** Amazon Polly
- **B.** Amazon Transcribe **[CORRECT]**
- **C.** Amazon Translate
- **D.** Amazon Textract

**Correct Answer:** `B`

#### Explanation & Rationale

Transcribe converts audio to text with timestamps and speaker ID.

---

<a id="q-51"></a>

### Question 51

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-051`

> **Scenario:**  
> Which service is used to build the conversation flow of a voice/text chatbot?

#### Options
- **A.** Amazon Lex **[CORRECT]**
- **B.** Amazon Polly
- **C.** Amazon Comprehend
- **D.** Amazon Personalize

**Correct Answer:** `A`

#### Explanation & Rationale

Lex builds conversational chatbots (the conversation flow); add Translate and Polly for multilingual voice.

---

<a id="q-52"></a>

### Question 52

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-052`

> **Scenario:**  
> Which service gives real-time product recommendations on an e-commerce site?

#### Options
- **A.** Amazon Forecast
- **B.** Amazon Personalize **[CORRECT]**
- **C.** Amazon Comprehend
- **D.** Amazon Rekognition

**Correct Answer:** `B`

#### Explanation & Rationale

Personalize provides real-time recommendations; Forecast does time-series prediction.

---

<a id="q-53"></a>

### Question 53

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-053`

> **Scenario:**  
> A company wants to detect fraud patterns unique to its own historical transaction data. Which choice does the wording signal?

#### Options
- **A.** A pre-built AI service
- **B.** A custom SageMaker model **[CORRECT]**
- **C.** AWS Marketplace generic model
- **D.** Amazon Polly

**Correct Answer:** `B`

#### Explanation & Rationale

'Our own historical data / patterns specific to us' signals a custom model built with SageMaker, not a pre-built service.

---

<a id="q-54"></a>

### Question 54

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-054`

> **Scenario:**  
> In SageMaker, what do you pay for during model training?

#### Options
- **A.** A fixed monthly platform fee
- **B.** Only the training time (infrastructure is provisioned then torn down) **[CORRECT]**
- **C.** Per prediction request
- **D.** Nothing — training is free

**Correct Answer:** `B`

#### Explanation & Rationale

SageMaker provisions compute for training, then tears it down; you pay only for training duration.

---

<a id="q-55"></a>

### Question 55

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-055`

> **Scenario:**  
> A team with no data scientists wants to build a custom model from tabular data with minimal configuration. Which SageMaker features help?

#### Options
- **A.** Autopilot and Canvas **[CORRECT]**
- **B.** Data Wrangler only
- **C.** Ground Truth only
- **D.** Neptune

**Correct Answer:** `A`

#### Explanation & Rationale

SageMaker Autopilot and Canvas automatically build and tune models from tabular data with minimal ML expertise.

---

<a id="q-56"></a>

### Question 56

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-056`

> **Scenario:**  
> A custom, low-latency application must process each streaming record as it arrives, with multiple independent consumers. Which service fits?

#### Options
- **A.** Kinesis Data Firehose
- **B.** Kinesis Data Streams **[CORRECT]**
- **C.** Amazon S3
- **D.** AWS Glue

**Correct Answer:** `B`

#### Explanation & Rationale

Kinesis Data Streams uses shards and lets multiple consumers read the same stream within seconds for custom real-time apps.

---

<a id="q-57"></a>

### Question 57

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-057`

> **Scenario:**  
> You need a fully managed 'fire-and-forget' pipeline to load streaming data into S3 or Redshift with no shard management. Which service fits?

#### Options
- **A.** Kinesis Data Streams
- **B.** Kinesis Data Firehose **[CORRECT]**
- **C.** Amazon EMR
- **D.** Amazon Athena

**Correct Answer:** `B`

#### Explanation & Rationale

Firehose is a managed delivery pipeline into S3/Redshift/OpenSearch with optional Lambda transformation and no shards.

---

<a id="q-58"></a>

### Question 58

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-058`

> **Scenario:**  
> In a data lake, which service crawls raw S3 data to populate a catalog of schemas and can run serverless ETL jobs?

#### Options
- **A.** Amazon Athena
- **B.** AWS Glue **[CORRECT]**
- **C.** Amazon QuickSight
- **D.** Amazon Redshift

**Correct Answer:** `B`

#### Explanation & Rationale

Glue provides the Data Catalog (metadata) and serverless Spark ETL jobs; the data itself stays in S3.

---

<a id="q-59"></a>

### Question 59

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-059`

> **Scenario:**  
> Which service runs serverless standard SQL directly against data in S3, priced per query by data scanned?

#### Options
- **A.** Amazon Redshift
- **B.** Amazon Athena **[CORRECT]**
- **C.** Amazon EMR
- **D.** AWS Glue

**Correct Answer:** `B`

#### Explanation & Rationale

Athena queries S3 in place using the Glue Catalog, priced per data scanned — ideal for ad-hoc analysis.

---

<a id="q-60"></a>

### Question 60

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-060`

> **Scenario:**  
> Which service provides no-code BI dashboards and reports for business users, connecting to Athena, Redshift, RDS and S3?

#### Options
- **A.** AWS Glue
- **B.** Amazon QuickSight **[CORRECT]**
- **C.** Amazon Kinesis
- **D.** Amazon Comprehend

**Correct Answer:** `B`

#### Explanation & Rationale

QuickSight is the BI/dashboarding service for business users.

---

<a id="q-61"></a>

### Question 61

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-061`

> **Scenario:**  
> Analytics differ mainly by where the data lives. Which fits 'data stays in S3, queried occasionally, pay per scan'?

#### Options
- **A.** Redshift
- **B.** Athena **[CORRECT]**
- **C.** EMR
- **D.** DynamoDB

**Correct Answer:** `B`

#### Explanation & Rationale

Athena: data in S3, occasional/ad-hoc queries, per-scan pricing. Redshift = loaded warehouse; EMR = cluster frameworks.

---

<a id="q-62"></a>

### Question 62

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-062`

> **Scenario:**  
> A large-scale big-data job needs specific open-source frameworks (Spark, Hive, Presto) and cluster-level control. Which service fits?

#### Options
- **A.** Amazon Athena
- **B.** Amazon EMR **[CORRECT]**
- **C.** Amazon QuickSight
- **D.** Amazon RDS

**Correct Answer:** `B`

#### Explanation & Rationale

EMR runs Spark/Hadoop/Hive/Presto on clusters you control — for large custom big-data jobs.

---

<a id="q-63"></a>

### Question 63

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-063`

> **Scenario:**  
> Which migration service performs a lift-and-shift 'rehost' by continuously replicating source server disks to AWS for a minimal-downtime cutover to EC2?

#### Options
- **A.** Database Migration Service (DMS)
- **B.** Application Migration Service (MGN) **[CORRECT]**
- **C.** Schema Conversion Tool (SCT)
- **D.** DataSync

**Correct Answer:** `B`

#### Explanation & Rationale

MGN continuously replicates whole servers (physical/virtual/other-cloud) for a minimal-downtime rehost to EC2.

---

<a id="q-64"></a>

### Question 64

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-064`

> **Scenario:**  
> Which service migrates databases with a full load plus Change Data Capture, keeping the target in sync until cutover?

#### Options
- **A.** Application Migration Service (MGN)
- **B.** Database Migration Service (DMS) **[CORRECT]**
- **C.** Transfer Family
- **D.** Snowball

**Correct Answer:** `B`

#### Explanation & Rationale

DMS does a full load then CDC to keep the target synced with the live source until cutover; supports homogeneous and heterogeneous moves.

---

<a id="q-65"></a>

### Question 65

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-065`

> **Scenario:**  
> You are moving from Oracle to PostgreSQL (a heterogeneous migration). Which tool converts tables, views and stored procedures to the target engine's syntax?

#### Options
- **A.** Schema Conversion Tool (SCT) **[CORRECT]**
- **B.** DataSync
- **C.** MGN
- **D.** QuickSight

**Correct Answer:** `A`

#### Explanation & Rationale

The Schema Conversion Tool partners with DMS on heterogeneous moves, converting schema/code and flagging manual work.

---

<a id="q-66"></a>

### Question 66

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-066`

> **Scenario:**  
> A petabyte-scale dataset must reach AWS but the network would take weeks. Which option is appropriate?

#### Options
- **A.** DataSync over the internet
- **B.** A Snow Family physical device **[CORRECT]**
- **C.** Transfer Family (SFTP)
- **D.** Kinesis Firehose

**Correct Answer:** `B`

#### Explanation & Rationale

When network transfer would take too long, ship a Snow Family device; DataSync is for transfers the network can finish in time.

---

<a id="q-67"></a>

### Question 67

**Set:** `Practice Exam 1` | **Domain:** `Module 7 · AI/ML, Analytics & Migration` | **ID:** `aws-practice-1-067`

> **Scenario:**  
> Which service provides automated, online transfer between on-prem NFS/SMB and S3, EFS or FSx with scheduling and integrity checks?

#### Options
- **A.** AWS DataSync **[CORRECT]**
- **B.** AWS Snowmobile
- **C.** AWS Transfer Family
- **D.** AWS DMS

**Correct Answer:** `A`

#### Explanation & Rationale

DataSync automates online file transfer between on-prem storage and AWS with built-in scheduling and validation.

---

<a id="q-68"></a>

### Question 68

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-068`

> **Scenario:**  
> Which AWS Support plan is free and included with every account?

#### Options
- **A.** Basic **[CORRECT]**
- **B.** Developer
- **C.** Business
- **D.** Enterprise

**Correct Answer:** `A`

#### Explanation & Rationale

The Basic plan is free: account/billing support, core Trusted Advisor checks, docs and forums.

---

<a id="q-69"></a>

### Question 69

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-069`

> **Scenario:**  
> At which support plan do the FULL set of Trusted Advisor checks (all five categories) first become available?

#### Options
- **A.** Basic
- **B.** Developer
- **C.** Business **[CORRECT]**
- **D.** Enterprise

**Correct Answer:** `C`

#### Explanation & Rationale

Full Trusted Advisor checks start at the Business plan; Basic/Developer get only core checks.

---

<a id="q-70"></a>

### Question 70

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-070`

> **Scenario:**  
> A mission-critical workload needs a dedicated Technical Account Manager (TAM) and Infrastructure Event Management. Which plan is required?

#### Options
- **A.** Developer
- **B.** Business
- **C.** Enterprise **[CORRECT]**
- **D.** Basic

**Correct Answer:** `C`

#### Explanation & Rationale

A dedicated TAM and Infrastructure Event Management are Enterprise-only.

---

<a id="q-71"></a>

### Question 71

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-071`

> **Scenario:**  
> A small team needs business-hours email guidance from Cloud Support Associates for non-production work. Which plan is the cheapest fit?

#### Options
- **A.** Basic
- **B.** Developer **[CORRECT]**
- **C.** Business
- **D.** Enterprise

**Correct Answer:** `B`

#### Explanation & Rationale

The Developer plan (from $29/mo) gives business-hours email access for small teams and non-production work.

---

<a id="q-72"></a>

### Question 72

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-072`

> **Scenario:**  
> Which AWS tool is used to VISUALISE and investigate spend and usage over time, filtering by service, account, Region or tag?

#### Options
- **A.** AWS Budgets
- **B.** AWS Cost Explorer **[CORRECT]**
- **C.** AWS Pricing Calculator
- **D.** Trusted Advisor

**Correct Answer:** `B`

#### Explanation & Rationale

Cost Explorer analyses and visualises spend/usage over time and can forecast future costs.

---

<a id="q-73"></a>

### Question 73

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-073`

> **Scenario:**  
> Which tool lets you set a cost or usage threshold and get alerted (or trigger an action) when it is breached or forecast to be?

#### Options
- **A.** Cost Explorer
- **B.** AWS Budgets **[CORRECT]**
- **C.** Pricing Calculator
- **D.** CloudTrail

**Correct Answer:** `B`

#### Explanation & Rationale

AWS Budgets sets thresholds and notifies via SNS/email, and can trigger automated actions on breach.

---

<a id="q-74"></a>

### Question 74

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-074`

> **Scenario:**  
> Which feature uses machine learning to automatically flag unusual spending without you setting manual thresholds?

#### Options
- **A.** Cost Anomaly Detection **[CORRECT]**
- **B.** AWS Budgets
- **C.** Trusted Advisor
- **D.** Consolidated billing

**Correct Answer:** `A`

#### Explanation & Rationale

Cost Anomaly Detection (part of Cost Explorer) uses ML to flag unusual spend automatically.

---

<a id="q-75"></a>

### Question 75

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-075`

> **Scenario:**  
> Which compute pricing model offers the deepest discount (up to ~90%) but can be reclaimed with a two-minute warning?

#### Options
- **A.** On-Demand
- **B.** Reserved Instances
- **C.** Savings Plans
- **D.** Spot Instances **[CORRECT]**

**Correct Answer:** `D`

#### Explanation & Rationale

Spot Instances use spare capacity at up to 90% off but can be reclaimed — only for interruption-tolerant work.

---

<a id="q-76"></a>

### Question 76

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-076`

> **Scenario:**  
> A steady workload needs discounts that stay flexible across instance family, size, Region, and even Fargate and Lambda. Which model fits best?

#### Options
- **A.** Standard Reserved Instances
- **B.** Compute Savings Plans **[CORRECT]**
- **C.** Spot Instances
- **D.** On-Demand

**Correct Answer:** `B`

#### Explanation & Rationale

Compute Savings Plans commit to $/hour of compute and apply across families, sizes, Regions, EC2, Fargate and Lambda.

---

<a id="q-77"></a>

### Question 77

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-077`

> **Scenario:**  
> Which pricing model is the flexible baseline with no commitment and the highest unit price, used as the yardstick for measuring savings?

#### Options
- **A.** On-Demand **[CORRECT]**
- **B.** Reserved Instances
- **C.** Savings Plans
- **D.** Spot

**Correct Answer:** `A`

#### Explanation & Rationale

On-Demand has no commitment and the highest unit price; all savings are measured against it.

---

<a id="q-78"></a>

### Question 78

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-078`

> **Scenario:**  
> Reserved Instances require what kind of commitment?

#### Options
- **A.** No commitment, pay per second
- **B.** A 1- or 3-year commitment to instance attributes **[CORRECT]**
- **C.** A two-minute reclaimable lease
- **D.** A per-request fee

**Correct Answer:** `B`

#### Explanation & Rationale

RIs commit for 1 or 3 years to family/size/Region (Standard) or with in-family flexibility (Convertible).

---

<a id="q-79"></a>

### Question 79

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-079`

> **Scenario:**  
> Which free tool (no AWS account needed) lets you build a cost estimate for a proposed architecture before you deploy it?

#### Options
- **A.** Cost Explorer
- **B.** AWS Pricing Calculator **[CORRECT]**
- **C.** AWS Budgets
- **D.** Trusted Advisor

**Correct Answer:** `B`

#### Explanation & Rationale

The AWS Pricing Calculator builds estimates for planned architectures and is free with no account required.

---

<a id="q-80"></a>

### Question 80

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-080`

> **Scenario:**  
> A parent company wants ONE invoice covering all its subsidiary accounts, with shared discounts and volume tiers. Which capability provides this?

#### Options
- **A.** AWS Budgets
- **B.** AWS Organizations consolidated billing **[CORRECT]**
- **C.** Cost Explorer
- **D.** Trusted Advisor

**Correct Answer:** `B`

#### Explanation & Rationale

Consolidated billing rolls all member accounts into one bill, aggregates volume pricing, and shares RI/Savings Plans discounts.

---

<a id="q-81"></a>

### Question 81

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-081`

> **Scenario:**  
> Under consolidated billing, how do Reserved Instance and Savings Plans discounts behave across linked accounts?

#### Options
- **A.** They apply only to the buying account
- **B.** They automatically apply to matching usage in any linked account (unless sharing is disabled) **[CORRECT]**
- **C.** They must be re-purchased per account
- **D.** They expire monthly

**Correct Answer:** `B`

#### Explanation & Rationale

Commitments bought in one account apply to matching usage in any other account, unless sharing is switched off.

---

<a id="q-82"></a>

### Question 82

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-082`

> **Scenario:**  
> Activating which feature lets you break down spend by team or project (e.g. CostCentre: Marketing) in Cost Explorer and billing reports?

#### Options
- **A.** Cost Allocation Tags **[CORRECT]**
- **B.** Service Control Policies
- **C.** Metric filters
- **D.** Savings Plans

**Correct Answer:** `A`

#### Explanation & Rationale

Cost Allocation Tags let you attribute spend to teams/projects for chargeback or showback.

---

<a id="q-83"></a>

### Question 83

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-083`

> **Scenario:**  
> Which Trusted Advisor category flags idle/underutilised EC2 instances and unattached EBS volumes?

#### Options
- **A.** Security
- **B.** Performance
- **C.** Cost Optimisation **[CORRECT]**
- **D.** Fault Tolerance

**Correct Answer:** `C`

#### Explanation & Rationale

Cost Optimisation checks surface idle resources and RI/Savings Plans opportunities.

---

<a id="q-84"></a>

### Question 84

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-084`

> **Scenario:**  
> Which Trusted Advisor category checks open security-group ports, root-account MFA and S3 bucket permissions?

#### Options
- **A.** Security **[CORRECT]**
- **B.** Performance
- **C.** Service Limits
- **D.** Fault Tolerance

**Correct Answer:** `A`

#### Explanation & Rationale

The Security category checks open ports, root MFA/IAM configuration and S3 permissions.

---

<a id="q-85"></a>

### Question 85

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-085`

> **Scenario:**  
> Which of these are the five Trusted Advisor check categories? (Choose the complete set.)

#### Options
- **A.** Cost, Performance, Security, Fault Tolerance, Service Limits **[CORRECT]**
- **B.** Cost, Speed, Encryption, Backup, Networking
- **C.** Compute, Storage, Database, Network, Billing
- **D.** Availability, Latency, Cost, Identity, Logging

**Correct Answer:** `A`

#### Explanation & Rationale

Trusted Advisor covers Cost Optimisation, Performance, Security, Fault Tolerance and Service Limits.

---

<a id="q-86"></a>

### Question 86

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-086`

> **Scenario:**  
> When several answers technically work on CLF-C02, which framework is the intended tiebreaker for the 'most correct' answer?

#### Options
- **A.** The Cloud Adoption Framework
- **B.** The Well-Architected Framework **[CORRECT]**
- **C.** The Shared Responsibility Model
- **D.** The MoSCoW method

**Correct Answer:** `B`

#### Explanation & Rationale

The Well-Architected Framework is the tiebreaker: prefer the answer reflecting best practice (e.g. Parameter Store over hard-coded creds).

---

<a id="q-87"></a>

### Question 87

**Set:** `Practice Exam 1` | **Domain:** `Module 8 · Billing, Pricing & Support` | **ID:** `aws-practice-1-087`

> **Scenario:**  
> On the exam, qualifying phrases like 'LEAST operational overhead' or 'MOST cost-effective' should be treated as:

#### Options
- **A.** Filler to ignore
- **B.** The selection criterion that decides among otherwise valid options **[CORRECT]**
- **C.** A hint the question is unscored
- **D.** A sign to pick the cheapest service always

**Correct Answer:** `B`

#### Explanation & Rationale

These qualifiers are the actual selection criteria; CLF-C02 rewards the managed/serverless, least-effort option.

---

<a id="q-88"></a>

### Question 88

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-001`

> **Scenario:**  
> Which is a core financial benefit of cloud computing over a traditional data centre?

#### Options
- **A.** Trading capital expense for variable operating expense **[CORRECT]**
- **B.** Guaranteed zero cost
- **C.** Removing the need for any security
- **D.** Owning all physical hardware

**Correct Answer:** `A`

#### Explanation & Rationale

The cloud lets you trade large up-front capital expense (CapEx) for pay-as-you-go variable expense (OpEx).

---

<a id="q-89"></a>

### Question 89

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-002`

> **Scenario:**  
> 'Elasticity' in the AWS Cloud refers to:

#### Options
- **A.** Data being encrypted in transit
- **B.** Resources scaling out and in automatically to match demand **[CORRECT]**
- **C.** A fixed pool of servers
- **D.** A discount pricing model

**Correct Answer:** `B`

#### Explanation & Rationale

Elasticity is the ability to acquire resources as you need them and release them when you don't — scaling with demand.

---

<a id="q-90"></a>

### Question 90

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-003`

> **Scenario:**  
> Which benefit describes AWS's ability to deploy to new geographic Regions quickly to serve users worldwide?

#### Options
- **A.** Going global in minutes **[CORRECT]**
- **B.** Economies of scale
- **C.** Trading CapEx for OpEx
- **D.** Increasing speed and agility

**Correct Answer:** `A`

#### Explanation & Rationale

'Go global in minutes' is the benefit of deploying an application in multiple Regions around the world with a few clicks.

---

<a id="q-91"></a>

### Question 91

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-004`

> **Scenario:**  
> How many pillars does the AWS Well-Architected Framework have, and which is NOT one of them?

#### Options
- **A.** Six pillars; 'Marketing' is not one **[CORRECT]**
- **B.** Six pillars; 'Sustainability' is not one
- **C.** Four pillars; 'Security' is not one
- **D.** Three pillars; 'Cost' is not one

**Correct Answer:** `A`

#### Explanation & Rationale

The Well-Architected Framework has six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimisation and Sustainability. Marketing is not a pillar.

---

<a id="q-92"></a>

### Question 92

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-005`

> **Scenario:**  
> Which Well-Architected pillar focuses on running and monitoring systems and continually improving processes?

#### Options
- **A.** Operational Excellence **[CORRECT]**
- **B.** Reliability
- **C.** Cost Optimisation
- **D.** Security

**Correct Answer:** `A`

#### Explanation & Rationale

Operational Excellence covers running, monitoring and continuously improving systems and processes.

---

<a id="q-93"></a>

### Question 93

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-006`

> **Scenario:**  
> A company runs part of its workload on-premises and part in AWS, connected together. This deployment model is called:

#### Options
- **A.** Public cloud
- **B.** Private cloud
- **C.** Hybrid cloud **[CORRECT]**
- **D.** Multi-cloud

**Correct Answer:** `C`

#### Explanation & Rationale

A hybrid deployment connects on-premises infrastructure with cloud resources.

---

<a id="q-94"></a>

### Question 94

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-007`

> **Scenario:**  
> What is an AWS Availability Zone?

#### Options
- **A.** A single edge/CDN location
- **B.** One or more discrete data centres with redundant power and networking within a Region **[CORRECT]**
- **C.** A billing boundary
- **D.** A type of EC2 instance

**Correct Answer:** `B`

#### Explanation & Rationale

An AZ is one or more discrete data centres with redundant power, networking and connectivity inside a Region.

---

<a id="q-95"></a>

### Question 95

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-008`

> **Scenario:**  
> To build a highly available architecture, across what should you distribute your resources within a Region?

#### Options
- **A.** Multiple Availability Zones **[CORRECT]**
- **B.** A single AZ with bigger instances
- **C.** Multiple AWS accounts only
- **D.** Multiple edge locations

**Correct Answer:** `A`

#### Explanation & Rationale

Spreading resources across multiple AZs protects against the failure of any single data centre.

---

<a id="q-96"></a>

### Question 96

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-009`

> **Scenario:**  
> What is the primary purpose of AWS edge locations / Amazon CloudFront?

#### Options
- **A.** Store relational databases
- **B.** Cache and deliver content closer to users to reduce latency **[CORRECT]**
- **C.** Run large batch analytics
- **D.** Manage IAM users

**Correct Answer:** `B`

#### Explanation & Rationale

Edge locations serve the CloudFront CDN, caching content near users to lower latency.

---

<a id="q-97"></a>

### Question 97

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-010`

> **Scenario:**  
> The AWS Cloud Adoption Framework (CAF) is used to:

#### Options
- **A.** Encrypt data at rest
- **B.** Organise guidance for planning an organisation's cloud adoption journey **[CORRECT]**
- **C.** Bill customers monthly
- **D.** Replace IAM

**Correct Answer:** `B`

#### Explanation & Rationale

The AWS CAF organises guidance across perspectives (Business, People, Governance, Platform, Security, Operations) to plan cloud adoption.

---

<a id="q-98"></a>

### Question 98

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-011`

> **Scenario:**  
> Which is an example of increased agility in the cloud?

#### Options
- **A.** Signing a 5-year hardware lease
- **B.** Spinning up test environments in minutes and tearing them down after **[CORRECT]**
- **C.** Buying servers months in advance
- **D.** Owning a data centre

**Correct Answer:** `B`

#### Explanation & Rationale

Agility means provisioning resources on demand in minutes, enabling faster experimentation.

---

<a id="q-99"></a>

### Question 99

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-012`

> **Scenario:**  
> 'Economies of scale' as an AWS benefit means:

#### Options
- **A.** You pay more as you grow
- **B.** Aggregated usage from many customers yields lower pay-as-you-go prices **[CORRECT]**
- **C.** You must reserve capacity for a year
- **D.** Prices are fixed regardless of usage

**Correct Answer:** `B`

#### Explanation & Rationale

AWS aggregates usage across many customers, achieving higher economies of scale and passing lower prices on.

---

<a id="q-100"></a>

### Question 100

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-013`

> **Scenario:**  
> Under the AWS shared responsibility model, which describes the split at a high level?

#### Options
- **A.** AWS secures everything
- **B.** The customer secures everything
- **C.** AWS is responsible for security OF the cloud; the customer for security IN the cloud **[CORRECT]**
- **D.** There is no security responsibility

**Correct Answer:** `C`

#### Explanation & Rationale

AWS secures the underlying cloud infrastructure; the customer secures what they put in the cloud (data, config, access).

---

<a id="q-101"></a>

### Question 101

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-014`

> **Scenario:**  
> Which cloud characteristic lets you provision and release computing resources with minimal human interaction?

#### Options
- **A.** On-demand self-service **[CORRECT]**
- **B.** Vendor lock-in
- **C.** Manual procurement
- **D.** Fixed capacity

**Correct Answer:** `A`

#### Explanation & Rationale

On-demand self-service means users can provision resources automatically without manual provider intervention.

---

<a id="q-102"></a>

### Question 102

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-015`

> **Scenario:**  
> A start-up wants to avoid large up-front spending on servers it may not need. Which cloud advantage addresses this directly?

#### Options
- **A.** Pay-as-you-go / variable expense **[CORRECT]**
- **B.** Vendor lock-in
- **C.** Longer procurement cycles
- **D.** Guaranteed uptime of 100%

**Correct Answer:** `A`

#### Explanation & Rationale

Pay-as-you-go lets you pay only for what you consume, avoiding large up-front investments.

---

<a id="q-103"></a>

### Question 103

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-016`

> **Scenario:**  
> Which Well-Architected pillar is specifically about using energy efficiently and reducing environmental impact?

#### Options
- **A.** Sustainability **[CORRECT]**
- **B.** Reliability
- **C.** Security
- **D.** Performance Efficiency

**Correct Answer:** `A`

#### Explanation & Rationale

Sustainability, added as the sixth pillar, focuses on minimising the environmental impact of running cloud workloads.

---

<a id="q-104"></a>

### Question 104

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-017`

> **Scenario:**  
> Which statement about AWS Regions is correct?

#### Options
- **A.** A Region is a single data centre
- **B.** Each Region is a separate geographic area containing multiple Availability Zones **[CORRECT]**
- **C.** Regions share the same power source
- **D.** You cannot choose your Region

**Correct Answer:** `B`

#### Explanation & Rationale

A Region is a physical geographic area that contains multiple, isolated Availability Zones.

---

<a id="q-105"></a>

### Question 105

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-018`

> **Scenario:**  
> Which is a valid reason to choose a particular AWS Region for a workload? (Choose the best answer.)

#### Options
- **A.** Data-residency/compliance requirements and proximity to users **[CORRECT]**
- **B.** The Region with the most colours in its name
- **C.** A Region always has one AZ
- **D.** Regions have identical service availability and price everywhere

**Correct Answer:** `A`

#### Explanation & Rationale

Region choice is driven by compliance/data residency, latency to users, service availability and price.

---

<a id="q-106"></a>

### Question 106

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-019`

> **Scenario:**  
> Reliability, as a Well-Architected pillar, primarily ensures a workload can:

#### Options
- **A.** Cost the least possible
- **B.** Recover from failures and meet demand **[CORRECT]**
- **C.** Use the newest instance types
- **D.** Avoid all encryption

**Correct Answer:** `B`

#### Explanation & Rationale

Reliability is about a workload performing its function correctly and recovering quickly from failures.

---

<a id="q-107"></a>

### Question 107

**Set:** `Final Exam` | **Domain:** `Domain 1 · Cloud Concepts (24%)` | **ID:** `aws-final-020`

> **Scenario:**  
> Which is an example of loose coupling improving reliability in a cloud architecture?

#### Options
- **A.** Calling a downstream service directly and waiting
- **B.** Placing an SQS queue between producer and consumer **[CORRECT]**
- **C.** Hard-coding IP addresses
- **D.** Running everything on one server

**Correct Answer:** `B`

#### Explanation & Rationale

Decoupling components (e.g. via a queue) prevents a failure in one component from cascading — a reliability best practice.

---

<a id="q-108"></a>

### Question 108

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-021`

> **Scenario:**  
> Under the shared responsibility model, which task is ALWAYS the customer's responsibility?

#### Options
- **A.** Securing the physical data centres
- **B.** Maintaining the hypervisor
- **C.** Managing customer data and IAM access configuration **[CORRECT]**
- **D.** Patching the AWS global network hardware

**Correct Answer:** `C`

#### Explanation & Rationale

Customers are always responsible for their data, identities and access management configuration ('security in the cloud').

---

<a id="q-109"></a>

### Question 109

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-022`

> **Scenario:**  
> For Amazon EC2 (IaaS), who is responsible for patching the guest operating system?

#### Options
- **A.** AWS
- **B.** The customer **[CORRECT]**
- **C.** No one
- **D.** The AWS Support team

**Correct Answer:** `B`

#### Explanation & Rationale

For EC2, patching the guest OS and applications is the customer's responsibility; AWS patches the underlying infrastructure.

---

<a id="q-110"></a>

### Question 110

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-023`

> **Scenario:**  
> What is the recommended way to grant an application running on EC2 access to an S3 bucket?

#### Options
- **A.** Embed an IAM user's access keys in the code
- **B.** Attach an IAM role to the EC2 instance **[CORRECT]**
- **C.** Use the root account credentials
- **D.** Make the bucket public

**Correct Answer:** `B`

#### Explanation & Rationale

Attach an IAM role to the instance so temporary credentials are provided automatically — no long-lived keys in code.

---

<a id="q-111"></a>

### Question 111

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-024`

> **Scenario:**  
> Which is an AWS security best practice for the root user of an account?

#### Options
- **A.** Use it for all daily tasks
- **B.** Enable MFA on it and avoid using it for everyday work **[CORRECT]**
- **C.** Share its password with the team
- **D.** Delete it entirely

**Correct Answer:** `B`

#### Explanation & Rationale

Protect the root user with MFA, lock away its credentials, and use IAM users/roles for daily work.

---

<a id="q-112"></a>

### Question 112

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-025`

> **Scenario:**  
> What does the principle of least privilege mean in IAM?

#### Options
- **A.** Grant every user administrator access
- **B.** Grant only the permissions required to perform a task **[CORRECT]**
- **C.** Never grant any permissions
- **D.** Give all permissions then remove some later

**Correct Answer:** `B`

#### Explanation & Rationale

Least privilege means granting only the minimum permissions necessary for the job.

---

<a id="q-113"></a>

### Question 113

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-026`

> **Scenario:**  
> Which IAM entity is best for granting temporary permissions that can be assumed by users, applications or AWS services?

#### Options
- **A.** An IAM user with long-term keys
- **B.** An IAM role **[CORRECT]**
- **C.** The root user
- **D.** A security group

**Correct Answer:** `B`

#### Explanation & Rationale

IAM roles provide temporary credentials and can be assumed by users, services or federated identities — no long-term keys.

---

<a id="q-114"></a>

### Question 114

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-027`

> **Scenario:**  
> Which AWS service protects web applications against common exploits such as SQL injection and cross-site scripting (OWASP Top 10)?

#### Options
- **A.** AWS WAF **[CORRECT]**
- **B.** Amazon GuardDuty
- **C.** AWS KMS
- **D.** Amazon Macie

**Correct Answer:** `A`

#### Explanation & Rationale

AWS WAF (Web Application Firewall) filters and blocks common web exploits like SQL injection and XSS.

---

<a id="q-115"></a>

### Question 115

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-028`

> **Scenario:**  
> Which AWS service provides managed DDoS protection?

#### Options
- **A.** AWS Shield **[CORRECT]**
- **B.** Amazon Inspector
- **C.** AWS Config
- **D.** Amazon Macie

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Shield provides managed protection against Distributed Denial of Service attacks (Standard is automatic; Advanced is paid).

---

<a id="q-116"></a>

### Question 116

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-029`

> **Scenario:**  
> Which service is an intelligent threat-detection service that continuously monitors for malicious activity using logs (e.g. VPC Flow Logs, CloudTrail, DNS)?

#### Options
- **A.** Amazon GuardDuty **[CORRECT]**
- **B.** AWS WAF
- **C.** AWS Artifact
- **D.** Amazon Macie

**Correct Answer:** `A`

#### Explanation & Rationale

GuardDuty is a threat-detection service that analyses account and network activity to flag malicious behaviour.

---

<a id="q-117"></a>

### Question 117

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-030`

> **Scenario:**  
> Which service uses machine learning to discover and protect sensitive data such as PII stored in Amazon S3?

#### Options
- **A.** Amazon Macie **[CORRECT]**
- **B.** Amazon Inspector
- **C.** AWS Shield
- **D.** AWS KMS

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Macie uses ML to discover, classify and protect sensitive data (e.g. PII) in S3.

---

<a id="q-118"></a>

### Question 118

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-031`

> **Scenario:**  
> Which service performs automated vulnerability assessments of EC2 instances and container images?

#### Options
- **A.** Amazon Inspector **[CORRECT]**
- **B.** Amazon Macie
- **C.** AWS Artifact
- **D.** AWS Shield

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Inspector automatically scans workloads (EC2, ECR images, Lambda) for software vulnerabilities and network exposure.

---

<a id="q-119"></a>

### Question 119

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-032`

> **Scenario:**  
> Which service creates and manages cryptographic keys and integrates with many AWS services for encryption?

#### Options
- **A.** AWS Key Management Service (KMS) **[CORRECT]**
- **B.** AWS CloudTrail
- **C.** Amazon GuardDuty
- **D.** AWS Config

**Correct Answer:** `A`

#### Explanation & Rationale

AWS KMS creates and controls encryption keys and integrates with services to encrypt data.

---

<a id="q-120"></a>

### Question 120

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-033`

> **Scenario:**  
> Which service securely stores database credentials and API keys and can automatically rotate them?

#### Options
- **A.** AWS Secrets Manager **[CORRECT]**
- **B.** Amazon S3
- **C.** AWS CloudTrail
- **D.** Amazon Inspector

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Secrets Manager stores secrets like DB credentials and can rotate them automatically.

---

<a id="q-121"></a>

### Question 121

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-034`

> **Scenario:**  
> Which service records API calls and account activity for auditing and governance ('who did what, and when')?

#### Options
- **A.** Amazon CloudWatch
- **B.** AWS CloudTrail **[CORRECT]**
- **C.** AWS Config
- **D.** Amazon Macie

**Correct Answer:** `B`

#### Explanation & Rationale

CloudTrail logs API activity across the account for auditing; CloudWatch is for performance metrics/monitoring.

---

<a id="q-122"></a>

### Question 122

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-035`

> **Scenario:**  
> Which service continuously records resource configurations and evaluates them against desired rules (configuration compliance)?

#### Options
- **A.** AWS Config **[CORRECT]**
- **B.** AWS CloudTrail
- **C.** Amazon Inspector
- **D.** AWS Shield

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Config tracks resource configuration over time and evaluates compliance against rules.

---

<a id="q-123"></a>

### Question 123

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-036`

> **Scenario:**  
> Where can you download AWS compliance reports such as SOC and ISO certifications on demand?

#### Options
- **A.** AWS Artifact **[CORRECT]**
- **B.** AWS Config
- **C.** Amazon Macie
- **D.** AWS Trusted Advisor

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Artifact is the self-service portal for on-demand access to AWS compliance reports and agreements.

---

<a id="q-124"></a>

### Question 124

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-037`

> **Scenario:**  
> An organisation wants to centrally restrict which services member accounts can use, regardless of their IAM permissions. Which feature is used?

#### Options
- **A.** Service Control Policies (SCPs) in AWS Organizations **[CORRECT]**
- **B.** IAM password policy
- **C.** Security groups
- **D.** Amazon Macie

**Correct Answer:** `A`

#### Explanation & Rationale

SCPs in AWS Organizations set permission guardrails that cap what member accounts can do, even for admins.

---

<a id="q-125"></a>

### Question 125

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-038`

> **Scenario:**  
> By default, how is data in a new Amazon S3 bucket exposed to the public internet?

#### Options
- **A.** It is public to everyone
- **B.** It is private by default; access must be explicitly granted **[CORRECT]**
- **C.** It is shared with all AWS accounts
- **D.** It is deleted after 24 hours

**Correct Answer:** `B`

#### Explanation & Rationale

S3 buckets and objects are private by default; you must explicitly grant access.

---

<a id="q-126"></a>

### Question 126

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-039`

> **Scenario:**  
> Which pair correctly maps a control to what it protects?

#### Options
- **A.** TLS/HTTPS → data in transit; server-side encryption → data at rest **[CORRECT]**
- **B.** TLS → data at rest; hashing → availability
- **C.** KMS → DDoS; Shield → encryption
- **D.** WAF → encryption; Macie → DDoS

**Correct Answer:** `A`

#### Explanation & Rationale

TLS/HTTPS protects data in transit; server-side/at-rest encryption protects stored data.

---

<a id="q-127"></a>

### Question 127

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-040`

> **Scenario:**  
> Which security service acts as a single dashboard aggregating and prioritising security findings from GuardDuty, Inspector, Macie and more?

#### Options
- **A.** AWS Security Hub **[CORRECT]**
- **B.** AWS Artifact
- **C.** AWS Config
- **D.** Amazon CloudFront

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Security Hub aggregates, organises and prioritises security findings across multiple AWS security services.

---

<a id="q-128"></a>

### Question 128

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-041`

> **Scenario:**  
> Which network control acts as a stateful virtual firewall at the instance level, controlling inbound and outbound traffic?

#### Options
- **A.** Security group **[CORRECT]**
- **B.** Network ACL only
- **C.** S3 bucket policy
- **D.** IAM policy

**Correct Answer:** `A`

#### Explanation & Rationale

Security groups are stateful instance-level firewalls; return traffic is automatically allowed. NACLs are stateless at the subnet level.

---

<a id="q-129"></a>

### Question 129

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-042`

> **Scenario:**  
> To require a second factor beyond a password when signing in, a user should enable:

#### Options
- **A.** Multi-Factor Authentication (MFA) **[CORRECT]**
- **B.** A stronger password only
- **C.** A larger instance
- **D.** Public bucket access

**Correct Answer:** `A`

#### Explanation & Rationale

MFA adds a second authentication factor (e.g. an authenticator app or hardware key) on top of the password.

---

<a id="q-130"></a>

### Question 130

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-043`

> **Scenario:**  
> An IAM policy is best described as:

#### Options
- **A.** A JSON document that defines permissions (allow/deny) for actions on resources **[CORRECT]**
- **B.** A physical firewall appliance
- **C.** A billing report
- **D.** An encryption key

**Correct Answer:** `A`

#### Explanation & Rationale

IAM policies are JSON documents specifying which actions are allowed or denied on which resources.

---

<a id="q-131"></a>

### Question 131

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-044`

> **Scenario:**  
> Which is the correct way to give three new developers the same set of permissions efficiently?

#### Options
- **A.** Create an IAM group with a policy and add the users to it **[CORRECT]**
- **B.** Give each the root credentials
- **C.** Create one shared IAM user
- **D.** Make an S3 bucket public

**Correct Answer:** `A`

#### Explanation & Rationale

Attach the policy to an IAM group and add users to the group — permissions are managed centrally.

---

<a id="q-132"></a>

### Question 132

**Set:** `Final Exam` | **Domain:** `Domain 2 · Security & Compliance (30%)` | **ID:** `aws-final-045`

> **Scenario:**  
> Which statement about AWS-managed encryption at rest is correct by default for many services?

#### Options
- **A.** Data is never encrypted
- **B.** AWS can use AWS-managed keys to encrypt data, with the option to use customer-managed keys in KMS **[CORRECT]**
- **C.** Only the customer can encrypt anything
- **D.** Encryption requires the Enterprise support plan

**Correct Answer:** `B`

#### Explanation & Rationale

Many services offer encryption at rest with AWS-managed keys by default, and customer-managed KMS keys as an option.

---

<a id="q-133"></a>

### Question 133

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-046`

> **Scenario:**  
> Which AWS service provides resizable virtual servers in the cloud?

#### Options
- **A.** Amazon EC2 **[CORRECT]**
- **B.** Amazon S3
- **C.** Amazon RDS
- **D.** AWS Lambda

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon EC2 provides resizable virtual machine (compute) capacity.

---

<a id="q-134"></a>

### Question 134

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-047`

> **Scenario:**  
> Which compute service runs your code without provisioning or managing servers, billing per request and duration?

#### Options
- **A.** Amazon EC2
- **B.** AWS Lambda **[CORRECT]**
- **C.** Amazon Lightsail
- **D.** AWS Batch

**Correct Answer:** `B`

#### Explanation & Rationale

AWS Lambda is serverless — you run code without managing servers and pay only for execution time.

---

<a id="q-135"></a>

### Question 135

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-048`

> **Scenario:**  
> A team wants to run Docker containers without managing the underlying servers. Which option fits best?

#### Options
- **A.** AWS Fargate **[CORRECT]**
- **B.** Amazon EC2 with manual setup
- **C.** Amazon S3
- **D.** Amazon Redshift

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Fargate is a serverless compute engine for containers (with ECS/EKS) — no server management.

---

<a id="q-136"></a>

### Question 136

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-049`

> **Scenario:**  
> Which service is object storage for virtually unlimited data, accessed over HTTP(S) with 11 nines of durability?

#### Options
- **A.** Amazon EBS
- **B.** Amazon S3 **[CORRECT]**
- **C.** Amazon EFS
- **D.** Instance store

**Correct Answer:** `B`

#### Explanation & Rationale

Amazon S3 is object storage accessed via API with 11-nines durability and effectively unlimited capacity.

---

<a id="q-137"></a>

### Question 137

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-050`

> **Scenario:**  
> Which service is a managed relational database supporting engines like MySQL and PostgreSQL?

#### Options
- **A.** Amazon DynamoDB
- **B.** Amazon RDS **[CORRECT]**
- **C.** Amazon Redshift
- **D.** Amazon ElastiCache

**Correct Answer:** `B`

#### Explanation & Rationale

Amazon RDS is the managed relational database service.

---

<a id="q-138"></a>

### Question 138

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-051`

> **Scenario:**  
> Which service is a fully managed NoSQL key-value database with single-digit-millisecond latency at any scale?

#### Options
- **A.** Amazon RDS
- **B.** Amazon DynamoDB **[CORRECT]**
- **C.** Amazon Aurora
- **D.** Amazon Redshift

**Correct Answer:** `B`

#### Explanation & Rationale

DynamoDB is serverless NoSQL delivering consistent single-digit-ms performance at scale.

---

<a id="q-139"></a>

### Question 139

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-052`

> **Scenario:**  
> Which service is a content delivery network (CDN) that caches content at edge locations?

#### Options
- **A.** Amazon CloudFront **[CORRECT]**
- **B.** Amazon Route 53
- **C.** AWS Direct Connect
- **D.** Amazon VPC

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon CloudFront is the CDN that delivers content from edge locations near users.

---

<a id="q-140"></a>

### Question 140

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-053`

> **Scenario:**  
> Which service is a scalable Domain Name System (DNS) web service?

#### Options
- **A.** Amazon Route 53 **[CORRECT]**
- **B.** Amazon CloudFront
- **C.** AWS Direct Connect
- **D.** AWS Global Accelerator

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Route 53 is AWS's managed, scalable DNS and domain registration service.

---

<a id="q-141"></a>

### Question 141

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-054`

> **Scenario:**  
> What is an Amazon VPC?

#### Options
- **A.** A logically isolated virtual network in the AWS Cloud that you control **[CORRECT]**
- **B.** A relational database
- **C.** A CDN edge location
- **D.** A billing tool

**Correct Answer:** `A`

#### Explanation & Rationale

A Virtual Private Cloud is your own logically isolated network within AWS where you launch resources.

---

<a id="q-142"></a>

### Question 142

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-055`

> **Scenario:**  
> Which service provides a dedicated, private physical network connection between on-premises and AWS?

#### Options
- **A.** AWS Direct Connect **[CORRECT]**
- **B.** Amazon CloudFront
- **C.** AWS Site-to-Site VPN over the internet
- **D.** Amazon Route 53

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Direct Connect establishes a dedicated private connection from on-premises to AWS, bypassing the public internet.

---

<a id="q-143"></a>

### Question 143

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-056`

> **Scenario:**  
> Which service distributes incoming application traffic across multiple targets such as EC2 instances?

#### Options
- **A.** Elastic Load Balancing (ELB) **[CORRECT]**
- **B.** Amazon S3
- **C.** AWS Lambda
- **D.** Amazon Athena

**Correct Answer:** `A`

#### Explanation & Rationale

Elastic Load Balancing spreads traffic across targets in one or more AZs for availability and scale.

---

<a id="q-144"></a>

### Question 144

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-057`

> **Scenario:**  
> Which service automatically adjusts the number of EC2 instances to match demand?

#### Options
- **A.** EC2 Auto Scaling **[CORRECT]**
- **B.** Amazon S3
- **C.** Amazon RDS
- **D.** AWS CloudTrail

**Correct Answer:** `A`

#### Explanation & Rationale

EC2 Auto Scaling adds/removes instances based on demand, keeping capacity between min/max/desired.

---

<a id="q-145"></a>

### Question 145

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-058`

> **Scenario:**  
> A workload needs a message queue to decouple components so consumers process at their own pace. Which service fits?

#### Options
- **A.** Amazon SQS **[CORRECT]**
- **B.** Amazon CloudFront
- **C.** AWS Config
- **D.** Amazon EC2

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon SQS is a managed message queue used to decouple and buffer between components.

---

<a id="q-146"></a>

### Question 146

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-059`

> **Scenario:**  
> Which service delivers one published message to many subscribers (pub/sub fan-out)?

#### Options
- **A.** Amazon SNS **[CORRECT]**
- **B.** Amazon SQS
- **C.** AWS Lambda
- **D.** Amazon EBS

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon SNS is the push-based publish/subscribe service delivering a message to all topic subscribers.

---

<a id="q-147"></a>

### Question 147

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-060`

> **Scenario:**  
> Which service lets you provision your entire infrastructure from JSON/YAML templates (Infrastructure as Code)?

#### Options
- **A.** AWS CloudFormation **[CORRECT]**
- **B.** Amazon QuickSight
- **C.** Amazon Comprehend
- **D.** AWS Artifact

**Correct Answer:** `A`

#### Explanation & Rationale

AWS CloudFormation provisions and manages infrastructure declaratively from templates.

---

<a id="q-148"></a>

### Question 148

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-061`

> **Scenario:**  
> Which service collects metrics, logs and alarms to monitor AWS resources and applications?

#### Options
- **A.** Amazon CloudWatch **[CORRECT]**
- **B.** AWS CloudTrail
- **C.** AWS Config
- **D.** Amazon Macie

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon CloudWatch is the monitoring and observability service (metrics, logs, alarms, dashboards).

---

<a id="q-149"></a>

### Question 149

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-062`

> **Scenario:**  
> A developer wants a simple, low-cost way to run a small website or app with predictable monthly pricing and preconfigured stacks. Which service fits?

#### Options
- **A.** Amazon Lightsail **[CORRECT]**
- **B.** Amazon EC2 with full manual configuration
- **C.** Amazon Redshift
- **D.** AWS Batch

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Lightsail offers easy, low-cost virtual servers with bundled resources and predictable pricing for simple workloads.

---

<a id="q-150"></a>

### Question 150

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-063`

> **Scenario:**  
> Which service lets you deploy and manage a web application without dealing with the underlying infrastructure, by just uploading code?

#### Options
- **A.** AWS Elastic Beanstalk **[CORRECT]**
- **B.** Amazon EC2
- **C.** Amazon VPC
- **D.** AWS Direct Connect

**Correct Answer:** `A`

#### Explanation & Rationale

Elastic Beanstalk handles capacity provisioning, load balancing and scaling for uploaded application code (PaaS).

---

<a id="q-151"></a>

### Question 151

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-064`

> **Scenario:**  
> Which service runs serverless SQL queries directly against data stored in Amazon S3?

#### Options
- **A.** Amazon Athena **[CORRECT]**
- **B.** Amazon Redshift
- **C.** Amazon RDS
- **D.** Amazon EMR

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Athena queries S3 data in place using standard SQL, priced per data scanned.

---

<a id="q-152"></a>

### Question 152

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-065`

> **Scenario:**  
> Which service is a petabyte-scale data warehouse for complex analytical (OLAP) queries?

#### Options
- **A.** Amazon Redshift **[CORRECT]**
- **B.** Amazon DynamoDB
- **C.** Amazon ElastiCache
- **D.** Amazon S3

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Redshift is the columnar data-warehouse service for large-scale analytics.

---

<a id="q-153"></a>

### Question 153

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-066`

> **Scenario:**  
> A shared file system that many EC2 instances can mount simultaneously across AZs is provided by:

#### Options
- **A.** Amazon EFS **[CORRECT]**
- **B.** Amazon S3
- **C.** Amazon EBS
- **D.** Instance store

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon EFS is the managed elastic file system mountable by many instances across AZs.

---

<a id="q-154"></a>

### Question 154

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-067`

> **Scenario:**  
> Which service ingests and processes real-time streaming data such as clickstreams and IoT telemetry?

#### Options
- **A.** Amazon Kinesis **[CORRECT]**
- **B.** Amazon Athena
- **C.** Amazon QuickSight
- **D.** AWS Snowball

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Kinesis ingests and processes streaming data in real time.

---

<a id="q-155"></a>

### Question 155

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-068`

> **Scenario:**  
> Which pre-built AI service extracts text and data from scanned documents?

#### Options
- **A.** Amazon Textract **[CORRECT]**
- **B.** Amazon Rekognition
- **C.** Amazon Polly
- **D.** Amazon Lex

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon Textract extracts text, forms and tables from documents; Rekognition analyses images/video.

---

<a id="q-156"></a>

### Question 156

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-069`

> **Scenario:**  
> Which fully managed platform is used to build, train and deploy custom machine-learning models?

#### Options
- **A.** Amazon SageMaker **[CORRECT]**
- **B.** Amazon Comprehend
- **C.** Amazon Personalize
- **D.** Amazon Transcribe

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon SageMaker is the managed platform for building, training and deploying custom ML models.

---

<a id="q-157"></a>

### Question 157

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-070`

> **Scenario:**  
> Which physical device transfers very large datasets to AWS when the network would take too long?

#### Options
- **A.** AWS Snowball **[CORRECT]**
- **B.** AWS Direct Connect
- **C.** Amazon CloudFront
- **D.** AWS Lambda

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Snowball (Snow Family) ships physical storage devices for large offline data transfer.

---

<a id="q-158"></a>

### Question 158

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-071`

> **Scenario:**  
> Which service enables interactive, no-code BI dashboards for business users?

#### Options
- **A.** Amazon QuickSight **[CORRECT]**
- **B.** AWS Glue
- **C.** Amazon Kinesis
- **D.** Amazon Inspector

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon QuickSight is the managed business-intelligence dashboarding service.

---

<a id="q-159"></a>

### Question 159

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-072`

> **Scenario:**  
> Which storage option provides persistent block storage for a single EC2 instance (like a virtual hard disk)?

#### Options
- **A.** Amazon EBS **[CORRECT]**
- **B.** Amazon S3
- **C.** Amazon EFS
- **D.** Amazon CloudFront

**Correct Answer:** `A`

#### Explanation & Rationale

Amazon EBS provides persistent block volumes attached to a single instance.

---

<a id="q-160"></a>

### Question 160

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-073`

> **Scenario:**  
> Which service orchestrates multi-step, serverless workflows as visual state machines with built-in retries?

#### Options
- **A.** AWS Step Functions **[CORRECT]**
- **B.** Amazon SNS
- **C.** Amazon EC2
- **D.** AWS Config

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Step Functions coordinates multi-step workflows with sequencing, retries and a visual view.

---

<a id="q-161"></a>

### Question 161

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-074`

> **Scenario:**  
> Which service provides managed publish/subscribe messaging AND which provides content-based event routing? (Match the pair.)

#### Options
- **A.** SNS = pub/sub; EventBridge = content-based routing **[CORRECT]**
- **B.** SQS = pub/sub; SNS = routing
- **C.** EventBridge = pub/sub; SQS = routing
- **D.** Kinesis = pub/sub; SNS = routing

**Correct Answer:** `A`

#### Explanation & Rationale

SNS is pub/sub fan-out; EventBridge routes events based on their content and supports schedules.

---

<a id="q-162"></a>

### Question 162

**Set:** `Final Exam` | **Domain:** `Domain 3 · Cloud Technology & Services (34%)` | **ID:** `aws-final-075`

> **Scenario:**  
> A gaming company needs global users to reach the nearest healthy application endpoint with improved performance over the AWS network. Which service fits?

#### Options
- **A.** AWS Global Accelerator **[CORRECT]**
- **B.** Amazon Macie
- **C.** AWS Config
- **D.** Amazon RDS

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Global Accelerator routes user traffic over the AWS global network to the nearest healthy endpoint, improving performance.

---

<a id="q-163"></a>

### Question 163

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-076`

> **Scenario:**  
> Which pricing model gives the biggest discount but can be interrupted with a two-minute warning?

#### Options
- **A.** Spot Instances **[CORRECT]**
- **B.** On-Demand
- **C.** Reserved Instances
- **D.** Dedicated Hosts

**Correct Answer:** `A`

#### Explanation & Rationale

Spot Instances offer up to ~90% off spare capacity but can be reclaimed — for interruption-tolerant workloads.

---

<a id="q-164"></a>

### Question 164

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-077`

> **Scenario:**  
> Which support plan is required to get the FULL set of Trusted Advisor checks?

#### Options
- **A.** Business (or Enterprise) **[CORRECT]**
- **B.** Basic
- **C.** Developer
- **D.** Only Enterprise

**Correct Answer:** `A`

#### Explanation & Rationale

Full Trusted Advisor checks begin at the Business plan; Basic/Developer get only core checks.

---

<a id="q-165"></a>

### Question 165

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-078`

> **Scenario:**  
> Which tool lets you set a spending threshold and receive an alert when costs exceed (or are forecast to exceed) it?

#### Options
- **A.** AWS Budgets **[CORRECT]**
- **B.** AWS Cost Explorer
- **C.** AWS Pricing Calculator
- **D.** AWS Trusted Advisor

**Correct Answer:** `A`

#### Explanation & Rationale

AWS Budgets sets custom cost/usage thresholds and alerts (or triggers actions) on breach.

---

<a id="q-166"></a>

### Question 166

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-079`

> **Scenario:**  
> Which capability lets a company receive a single consolidated bill for many AWS accounts and share volume discounts?

#### Options
- **A.** AWS Organizations consolidated billing **[CORRECT]**
- **B.** AWS Budgets
- **C.** AWS Cost Explorer
- **D.** AWS Support

**Correct Answer:** `A`

#### Explanation & Rationale

Consolidated billing in AWS Organizations combines accounts into one bill and aggregates volume/commitment discounts.

---

<a id="q-167"></a>

### Question 167

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-080`

> **Scenario:**  
> A dedicated Technical Account Manager (TAM) is included with which AWS Support plan?

#### Options
- **A.** Enterprise **[CORRECT]**
- **B.** Business
- **C.** Developer
- **D.** Basic

**Correct Answer:** `A`

#### Explanation & Rationale

A dedicated TAM is an Enterprise-plan benefit.

---

<a id="q-168"></a>

### Question 168

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-081`

> **Scenario:**  
> Which free tool estimates the cost of a proposed AWS architecture before deployment (no account required)?

#### Options
- **A.** AWS Pricing Calculator **[CORRECT]**
- **B.** AWS Cost Explorer
- **C.** AWS Budgets
- **D.** Amazon CloudWatch

**Correct Answer:** `A`

#### Explanation & Rationale

The AWS Pricing Calculator builds pre-deployment cost estimates and needs no AWS account.

---

<a id="q-169"></a>

### Question 169

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-082`

> **Scenario:**  
> Which service helps you visualise, understand and investigate your past and current AWS spend with filtering and forecasting?

#### Options
- **A.** AWS Cost Explorer **[CORRECT]**
- **B.** AWS Budgets
- **C.** AWS Artifact
- **D.** AWS Config

**Correct Answer:** `A`

#### Explanation & Rationale

Cost Explorer visualises and analyses spend/usage over time and forecasts future costs.

---

<a id="q-170"></a>

### Question 170

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-083`

> **Scenario:**  
> A steady, long-running workload wants savings while staying flexible across instance families and Regions. Which model fits best?

#### Options
- **A.** Compute Savings Plans **[CORRECT]**
- **B.** Spot Instances
- **C.** On-Demand
- **D.** Dedicated Hosts

**Correct Answer:** `A`

#### Explanation & Rationale

Compute Savings Plans commit to $/hour of usage and apply flexibly across families, sizes, Regions, and to Fargate/Lambda.

---

<a id="q-171"></a>

### Question 171

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-084`

> **Scenario:**  
> Under the AWS Free Tier, which category is NOT one of its three types?

#### Options
- **A.** Interruptible **[CORRECT]**
- **B.** Always Free
- **C.** 12 Months Free
- **D.** Trials

**Correct Answer:** `A`

#### Explanation & Rationale

The Free Tier types are Always Free, 12 Months Free, and short-term Trials. 'Interruptible' is not a Free Tier type.

---

<a id="q-172"></a>

### Question 172

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-085`

> **Scenario:**  
> Which Trusted Advisor category checks whether you are approaching AWS account quotas (e.g. number of VPCs)?

#### Options
- **A.** Service Limits **[CORRECT]**
- **B.** Cost Optimisation
- **C.** Security
- **D.** Performance

**Correct Answer:** `A`

#### Explanation & Rationale

The Service Limits category warns when usage approaches account quotas.

---

<a id="q-173"></a>

### Question 173

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-086`

> **Scenario:**  
> Which support plan offers a response time target of under 1 hour for production-system-down cases?

#### Options
- **A.** Business **[CORRECT]**
- **B.** Developer
- **C.** Basic
- **D.** Free tier only

**Correct Answer:** `A`

#### Explanation & Rationale

The Business plan targets under 1 hour for production-down issues; Enterprise targets under 15 minutes for business-critical.

---

<a id="q-174"></a>

### Question 174

**Set:** `Final Exam` | **Domain:** `Domain 4 · Billing, Pricing & Support (12%)` | **ID:** `aws-final-087`

> **Scenario:**  
> Which statement about On-Demand pricing is correct?

#### Options
- **A.** It requires no long-term commitment and bills per second/hour **[CORRECT]**
- **B.** It requires a 3-year commitment
- **C.** It is always the cheapest option
- **D.** It cannot be interrupted only because it is reserved

**Correct Answer:** `A`

#### Explanation & Rationale

On-Demand has no commitment and bills per second/hour — maximum flexibility at the highest unit price.

---

