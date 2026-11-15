# AWS Compute Services — Map of Content (MOC)

> **Domain:** 03_Services / Compute  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], SAA-C03, DVA-C02

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
