# Lecture 02: Compute Services, Virtualization, Containers & Serverless

> **Course Track:** AWS Certified Cloud Practitioner (`CLF-C02`)  
> **Target Exam Domain:** Domain 3: Cloud Technology & Services (34% of Exam Blueprint)  
> **Estimated Delivery Duration:** 90 Minutes  
> **Associated Slide Deck:** `slides/Module_02_Compute_Storage_and_Databases_Slides.md`  
> **Target Hands-On Labs:** `labs/lab_03_ec2_compute_bootstrap.md` & `labs/lab_05_serverless_lambda_apigateway.md`  
> **Student Explanations:** `explanations/03_Technology_and_Services/Compute_Services.md`

---

## 📚 Prescribed Textbook Reading & Literature Grounding

Before delivering or attending this lecture, review the assigned chapters:
* **Tom Taulli (*O'Reilly 2026, 1st Ed.*):**
  * Chapter 9: *AWS Compute, Containers, and Serverless* (pp. 133–158)
    * Amazon EC2 instances, Graviton custom silicon, pricing options (On-Demand, Spot, Savings Plans, RIs, Dedicated).
    * Container orchestration: Amazon ECS vs Amazon EKS vs AWS Fargate.
    * Serverless architecture: AWS Lambda event sources, execution limits, and pricing.
* **Rajesh Daswani (*Packt 2026, 2nd Ed.*):**
  * Chapter 8: *AWS Compute Services: EC2, Lightsail, ECS, EKS, and Lambda* (pp. 157–184)
    * Virtualization layers, instance metadata, User Data bootstrapping, container lifecycles.
* **Gaurav H Kankaria (*Orange Education 2026, 2nd Ed.*):**
  * Chapter 5: *AWS Core Services – Part I (Compute)* (pp. 47–68)
    * Step-by-step EC2 provisioning, instance states, and serverless compute models.

---

## ⏱️ Detailed 90-Minute Delivery Schedule & Pacing

```
00:00 - 00:15 | Review Lecture 01 & The Compute Spectrum (IaaS vs PaaS vs CaaS vs FaaS)
00:15 - 00:40 | Amazon EC2 Deep-Dive: Instance Families, Graviton, User Data & Tenancy
00:40 - 00:55 | EC2 Purchasing Options: On-Demand, Savings Plans, RIs, Spot & Dedicated Hosts
00:55 - 01:15 | Containers in the Cloud: Docker, Amazon ECR, Amazon ECS, Amazon EKS & AWS Fargate
01:15 - 01:25 | Serverless Compute: AWS Lambda Mechanics, Triggers & 15-Minute Technical Limit
01:25 - 01:30 | Socratic Q&A & Transition to Lab 03 (EC2 Web Server Bootstrap)
```

---

## 🗣️ Instructor Delivery Talking Points & Storytelling

### 1. The Compute Continuum Analogy: Car Ownership to Public Transit
* **Amazon EC2 (IaaS):** Buying a personal sports car. You pick the engine and transmission. You must change the oil, rotate tires, and patch the engine (install OS security updates).
* **AWS Elastic Beanstalk (PaaS):** Leasing a fully serviced vehicle. You just bring your luggage (source code) and drive. AWS handles provisioning, load balancing, and scaling automatically.
* **AWS Fargate (Containers):** Riding in a standardized container taxi. You don't manage the chassis or tires, but you control what software packages are placed inside the container.
* **AWS Lambda (FaaS):** Hailing an on-demand electric scooter or Uber. You pay strictly for the exact seconds the wheels are spinning. When you reach your destination, the vehicle vanishes. Idle cost = \$0.00.

---

### 2. Amazon EC2 Instance Families (Memory Anchor Tricks)
Teach students this mental anchor to easily recognize instance families in exam scenarios:
* **G - General Purpose (`t3`, `m6i`, `m7g`):** Balanced compute, memory, and networking. Ideal for web servers, dev environments, small databases.
* **C - Compute Optimized (`c6i`, `c7g`):** High-performance CPUs. Ideal for batch processing, media transcoding, scientific modeling, gaming dedicated servers.
* **M - Memory Optimized (`r6i`, `r7g`, `x2gd`):** High RAM-to-CPU ratio. Ideal for high-performance in-memory relational databases, real-time big data processing (Spark/SAP HANA).
* **S - Storage Optimized (`i3en`, `d3`, `h1`):** Direct-attached NVMe storage. High sequential read/write IOPS. Ideal for distributed file systems, data warehouses, Elasticsearch.
* **A - Accelerated Computing (`p4`, `g5`):** Hardware GPU coprocessors. Machine learning training, AI inference, 3D graphics rendering.
* **AWS Graviton Processors:** ARM-based custom silicon engineered by AWS delivering up to **40% better price-performance** over comparable x86 processors.

---

### 3. Whiteboard Matrix: EC2 Pricing Options Decision Tree

Draw this high-yield matrix on the classroom board:

```
┌────────────────────┬─────────────────┬───────────────────┬──────────────────────────────────────────┐
│ Pricing Option     │ Commitment      │ Discount vs OD    │ Ideal Use Case                           │
├────────────────────┼─────────────────┼───────────────────┼──────────────────────────────────────────┤
│ On-Demand          │ None (sec/hr)   │ Baseline (0%)     │ Unpredictable, short-term, dev/test      │
│ Savings Plans      │ 1 or 3 Years    │ Up to 72%         │ Steady-state compute across EC2/Lambda   │
│ Reserved Instances │ 1 or 3 Years    │ Up to 72%         │ Steady-state predictable EC2 / RDS loads │
│ Spot Instances     │ None (Spare)    │ Up to 90%         │ Batch, fault-tolerant (2-min notice)     │
│ Dedicated Hosts    │ On-Demand/1-3yr │ Varies            │ Compliance, socket-bound BYOL licenses   │
│ Dedicated Instance │ Per instance    │ Surcharge         │ Hardware isolation for single tenant     │
└────────────────────┴─────────────────┴───────────────────┴──────────────────────────────────────────┘
```

* **Exam Trap Highlights:**
  * *Trap 1: Spot Instances interruption.* Emphasize: AWS gives a **2-minute warning** before reclaiming a Spot instance. Never use Spot for stateful databases or critical e-commerce checkout systems!
  * *Trap 2: Dedicated Host vs Dedicated Instance.* Dedicated Host gives socket-level physical control to satisfy commercial software licenses (Windows Server, Oracle). Dedicated Instance only guarantees single-tenant hardware isolation without socket visibility.

---

### 4. Containers & Serverless Architecture
* **Amazon ECR:** Private, secure Docker container image registry.
* **Amazon ECS vs. Amazon EKS:**
  * *ECS:* AWS-native container orchestrator. Simpler, deeply integrated with AWS IAM and CloudWatch.
  * *EKS:* Managed Kubernetes. Use when an enterprise already has existing Kubernetes YAML manifests or requires multi-cloud portability.
* **AWS Fargate:** Serverless compute engine for both ECS and EKS. Eliminates EC2 worker node management.
* **AWS Lambda Rules to Remember:**
  * Pay per invocation and execution duration (rounded to nearest 1 ms).
  * **Hard Limit:** Maximum execution duration is **15 minutes (900 seconds)**.
  * Maximum memory allocation: 10,240 MB (10 GB).
  * Workloads requiring > 15 minutes of compute belong on AWS Fargate, EC2, or AWS Batch.

---

## ❓ Socratic Classroom Check Questions

1. *"A company processes satellite imagery overnight. If a job fails halfway through, the worker can simply restart from the last processed tile without business impact. Which purchasing model saves the most money?"*
   * **Expected Answer:** **EC2 Spot Instances** (saves up to 90%).
2. *"A database administrator needs to run an in-memory Redis cluster requiring 256 GB of RAM. Which EC2 instance family should they deploy?"*
   * **Expected Answer:** **Memory Optimized (`R` or `X` family)**.
3. *"A developer writes a Python script that runs once every 24 hours to resize images uploaded to S3. The script takes 45 seconds to execute. What is the most cost-effective compute choice?"*
   * **Expected Answer:** **AWS Lambda**. Zero server maintenance, zero idle costs, sub-second billing.

---


---

## 🎯 Authentic Exam Practice & Case Scenarios
> High-yield scenario questions from the authentic candidate practice pool reinforcing the core competencies of this lecture.

### Scenario Practice 1: CLF-C02-ET-Q124
**Question:**  
A company wants a cost-effective option when running its applications in an Amazon EC2 instance for short time periods. The applications can be interrupted.

Which EC2 instance type will meet these requirements?

**Options:**
- A) Spot Instances
- B) On-Demand Instances
- C) Reserved Instances
- D) Dedicated Instances

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `A`  
**Peer Consensus:** `100%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
A. Spot Instances

</details>

### Scenario Practice 2: CLF-C02-ET-Q156
**Question:**  
A company has data lakes designed for high performance computing (HPC) workloads.

Which Amazon EC2 instance type should the company use to meet these requirements?

**Options:**
- A) General purpose instances
- B) Compute optimized instances
- C) Memory optimized instances
- D) Storage optimized instances

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `B`  
**Peer Consensus:** `67%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
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

### Scenario Practice 3: CLF-C02-ET-Q184
**Question:**  
Which type of workload should a company run on Amazon EC2 Spot Instances?

**Options:**
- A) A steady-state workload that requires a particular EC2 instance configuration for a long period of time
- B) A workload that can be interrupted and can control costs
- C) A steady-state workload that does not require a long-term commitment
- D) A workload that cannot be interrupted and can control costs

<details>
<summary><b>View Verified Answer & Solution Analysis</b></summary>

**Correct Answer:** `B`  
**Peer Consensus:** `100%` agreement.  

**Architectural Breakdown & Distractor Analysis:**  
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

## 🚀 Post-Lecture Student Transition
* Direct students to review [Compute_Services.md](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Compute_Services.md).
* Transition to hands-on practice: [Lab 03: EC2 Compute & Bootstrap](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/07_Hands_On_Labs/lab_03_ec2_compute_bootstrap.md) and [Lab 05: Serverless Lambda & API Gateway](file:///home/mohamed/Desktop/Work/aws/Cloud/Practitioner/CLF-C02/07_Hands_On_Labs/lab_05_serverless_lambda_apigateway.md).
