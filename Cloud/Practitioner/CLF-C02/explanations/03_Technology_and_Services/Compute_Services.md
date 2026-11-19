# AWS Compute Services — Map of Content (MOC)

> **Domain:** 03_Services / Compute  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], SAA-C03, DVA-C02

---

## 💡 The Real-World Analogy (ELI5)

> **Modes of Transportation:**
> - **Amazon EC2 (IaaS):** Buying a personal car. You choose the exact engine size, seat fabric, and transmission. You are 100% responsible for changing the oil, replacing the tires, and pumping gas (patching the OS and configuring firewall ports).
> - **AWS Elastic Beanstalk (PaaS):** Leasing a car with a full maintenance contract. You just bring your luggage (code), turn the ignition key, and drive. The leasing company handles oil changes and engine tuning.
> - **AWS Lambda (Serverless FaaS):** Hailing an Uber or taxi. You don't buy a car, pay for gas, or park it. The car appears instantly when you need a ride, drives you for 5 minutes, and disappears. You pay strictly for the exact minutes and miles traveled. When not riding, you pay literally bash.00.
> - **Amazon ECS & EKS (Containers):** Standard shipping containers. Whether you transport electronics, furniture, or food, the standardized container fits on any cargo ship, freight train, or flatbed truck.

---

## 1. Architectural Taxonomy of AWS Compute

AWS compute services span four distinct operational models, ranging from direct virtual server control to serverless function execution:

```mermaid
flowchart TD
    Compute["AWS Compute Portfolio"]
    
    subgraph IaaS["1. Virtual Machines (IaaS)"]
        EC2["Amazon EC2 (Virtual Servers, Full OS control)"]
        Outposts["AWS Outposts (On-Premises Hardware Rack)"]
    end
    
    subgraph Containers["2. Container Orchestration (CaaS)"]
        ECS["Amazon ECS (AWS-native Docker orchestrator)"]
        EKS["Amazon EKS (Managed Kubernetes)"]
        Fargate["AWS Fargate (Serverless compute engine for ECS/EKS)"]
        ECR["Amazon ECR (Docker Container Registry)"]
    end
    
    subgraph Serverless["3. Serverless Execution (FaaS)"]
        Lambda["AWS Lambda (Event-driven, pay-per-millisecond)"]
    end
    
    subgraph PaaS["4. Platform as a Service (PaaS)"]
        Beanstalk["AWS Elastic Beanstalk (Code to app deployment)"]
    end
    
    Compute --> IaaS
    Compute --> Containers
    Compute --> Serverless
    Compute --> PaaS
```

---

## 2. Decision Tree: Choosing the Right Compute Service

```mermaid
flowchart LR
    Start{"Application Type?"}
    Start -->|Monolithic / Legacy OS / Custom Kernel| EC2["Amazon_EC2"]
    Start -->|Containerized Microservices| Cont{"Container Orchestrator?"}
    Cont -->|Kubernetes standard| EKS["Amazon_EKS"]
    Cont -->|Simpler AWS-native Docker| ECS["Amazon_ECS"]
    
    ECS --> LaunchType{"Infrastructure Management?"}
    EKS --> LaunchType
    LaunchType -->|Manage EC2 instances| EC2Worker["EC2 Launch Type"]
    LaunchType -->|Serverless / No server management| Fargate["AWS_Fargate"]
    
    Start -->|Event-driven / Short tasks < 15 min| Lambda["AWS_Lambda"]
    Start -->|Standard Web App / Fast deploy| Beanstalk["AWS_Elastic_Beanstalk"]
```

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[Amazon_EC2]]** | Elastic Compute Cloud | Instances, AMIs, Pricing Models (On-Demand, Spot, Reserved), EBS. |
| **[[AWS_Lambda]]** | Serverless Compute Engine | Event-driven, 15-minute max execution, 0 to 10k auto-scale, pay per ms. |
| **[[Amazon_ECS]]** | Elastic Container Service | AWS-native Docker container orchestration, Task Definitions, Services. |
| **[[Amazon_EKS]]** | Elastic Kubernetes Service | Managed upstream Kubernetes clusters, Pods, control plane HA. |
| **[[AWS_Fargate]]** | Serverless Container Compute | Run containers without managing EC2 instances, per-vCPU/GB pricing. |
| **[[Amazon_ECR]]** | Elastic Container Registry | Managed private/public Docker registries, vulnerability scanning. |
| **[[AWS_Outposts]]** | Hybrid On-Premises Compute | Physical AWS racks deployed directly into customer data centers. |
| **[[Containers_ECS_EKS_Fargate]]** | Container Comparison Guide | Comprehensive architectural distinction matrix for containers. |
---

## 7. Post-Topic Question Simulation & Retention Check

Test your understanding of AWS Compute Services with these 5 exam-style questions:

## 🎯 Exam Traps & 'Clue-to-Answer' Trigger Words

| Exam Question Clue Keyword | Correct Compute Option | Key Constraint |
| :--- | :--- | :--- |
| *'Event-driven, pay per millisecond, zero server management'* | **AWS Lambda** | Max execution timeout is **15 minutes**. |
| *'Run containers without provisioning or managing EC2 virtual servers'* | **AWS Fargate** | Serverless container compute engine for ECS and EKS. |
| *'Fault-tolerant batch jobs, non-critical workloads, up to 90% discount'* | **EC2 Spot Instances** | Can be interrupted with a **2-minute notice**. |
| *'Dedicated physical server for per-socket software licensing (BYOL)'* | **EC2 Dedicated Hosts** | Provides socket and core visibility for regulatory compliance. |
| *'Deploy web application code without managing underlying infrastructure'* | **AWS Elastic Beanstalk** | PaaS service; handles provisioning, load balancing, auto scaling. |

---

### Question 1
**Which EC2 pricing option offers up to a 90% discount on on-demand rates by allowing workloads to run on spare, unused EC2 capacity with the caveat that instances can be terminated with a 2-minute notice?**
- A) Dedicated Hosts
- B) Reserved Instances
- C) Spot Instances
- D) Savings Plans

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C) Spot Instances**  
- **Why it's correct:** Spot Instances take advantage of unused EC2 capacity at steep discounts (up to 90%). They are ideal for fault-tolerant, stateless batch jobs, big data analysis, and containerized microservices that can tolerate unexpected interruptions.
</details>

### Question 2
**A developer wants to run a lightweight Python data transformation script in response to new files landing in an Amazon S3 bucket. The script runs for 30 seconds twice a day. Which compute option is most cost-effective?**
- A) Amazon EC2 On-Demand Instance
- B) AWS Lambda
- C) Amazon ECS with dedicated EC2 worker nodes
- D) AWS Elastic Beanstalk

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS Lambda**  
- **Why it's correct:** AWS Lambda is serverless event-driven compute. You pay strictly for execution time measured in 1-millisecond increments. When idle, costs are literally $0.00.
</details>

### Question 3
**Which container management service runs Docker containers on AWS without requiring the customer to provision, configure, or scale the underlying EC2 virtual machine instances?**
- A) Amazon EC2 Auto Scaling
- B) AWS Fargate
- C) Amazon Elastic Container Registry (ECR)
- D) AWS Outposts

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) AWS Fargate**  
- **Why it's correct:** AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS, abstracting away the server layer entirely.
</details>

### Question 4
**A company has an enterprise software license that is bound to specific physical CPU sockets and cores. Which Amazon EC2 tenancy option is required to satisfy this licensing restriction?**
- A) Spot Instances
- B) Dedicated Hosts
- C) Default Multi-Tenant Instances
- D) Dedicated Instances

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Dedicated Hosts**  
- **Why it's correct:** An EC2 Dedicated Host gives the customer full physical visibility and socket-level control over a dedicated physical server, satisfying Bring Your Own License (BYOL) socket-bound requirements.
</details>

### Question 5
**What is the maximum execution time limit for a single AWS Lambda function invocation?**
- A) 1 minute
- B) 5 minutes
- C) 15 minutes
- D) Unlimited

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C) 15 minutes**  
- **Why it's correct:** AWS Lambda has a hard technical limit of 15 minutes (900 seconds) per function invocation. Workloads running longer should use AWS Fargate, EC2, or AWS Batch.
</details>
