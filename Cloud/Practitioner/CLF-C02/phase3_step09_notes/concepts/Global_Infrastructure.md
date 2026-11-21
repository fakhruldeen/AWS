# AWS Global Infrastructure

> **Knowledge Area:** Cloud Concepts (Domain 1) & Cloud Technology (Domain 3)  
> **Relevant Certifications:** [CLF-C02](../../phase0_step01_syllabus/CLF-C02_Master_Blueprint.md), SAA-C03, AIF-C01  
> **Tags:** `#aws/concepts` `#aws/infrastructure` `#clf-c02`

---

## 1. Overview of AWS Global Infrastructure

AWS operates a purpose-built, high-availability global cloud infrastructure consisting of geographically dispersed **Regions**, isolated **Availability Zones (AZs)**, an ultra-fast private global network backbone, and a distributed footprint of **Edge Locations**, **Local Zones**, and **Wavelength Zones**.

```mermaid
graph TD
    subgraph GlobalFootprint ["AWS Global Network Backbone"]
        direction TB
        
        subgraph RegionA ["AWS Region (e.g., us-east-1)"]
            AZ1["Availability Zone A\n(Isolated Data Centers)"]
            AZ2["Availability Zone B\n(Isolated Data Centers)"]
            AZ3["Availability Zone C\n(Isolated Data Centers)"]
            AZ1 <-->|Ultra-low latency fiber| AZ2
            AZ2 <-->|Ultra-low latency fiber| AZ3
            AZ1 <-->|Ultra-low latency fiber| AZ3
        end
        
        subgraph EdgeLayer ["Global Edge Network (600+ PoPs)"]
            EL1["Edge Location (PoP)"]
            EL2["Edge Location (PoP)"]
            REC["Regional Edge Cache"]
        end
        
        subgraph LowLatencyExtensions ["Low-Latency Edge Extensions"]
            LZ["AWS Local Zones\n(Urban Metro Centers)"]
            WZ["AWS Wavelength Zones\n(5G Telco Carrier Edge)"]
            OP["AWS Outposts\n(Customer On-Premises Racks)"]
        end
        
        RegionA <====|Private High-Speed Global Backbone|====> EdgeLayer
        RegionA <====|Private High-Speed Global Backbone|====> LowLatencyExtensions
    end
```

---

## 2. AWS Regions

An **AWS Region** is a physical geographical area in the world where AWS clusters multiple, physically separated Availability Zones.

### Key Characteristics:
* **Independence:** Every AWS Region is completely independent and isolated from other regions. A failure in one region does not affect another.
* **Minimum 3 AZs:** Every modern AWS Region contains at least **three** discrete Availability Zones (some have 6, like `us-east-1`).
* **Data Sovereignty:** Data stored in a specific Region **never leaves that Region** unless the customer explicitly configures cross-region replication.

### 4 Pillars of Region Selection (High-Yield Exam Focus):
When deciding which AWS Region to deploy workloads in, organizations evaluate 4 factors:

| Factor | Description | Example Scenario |
|---|---|---|
| **1. Compliance & Data Sovereignty** | Legal and regulatory requirements governing where data can physically reside. | GDPR in Europe requires customer data to reside within the EU; government regulations in Australia require data to stay in Sydney. |
| **2. Proximity & Latency** | Minimizing network round-trip time for the primary user base. | Deploy in `eu-west-1` (Ireland) for Western European users; deploy in `ap-southeast-1` (Singapore) for Southeast Asia. |
| **3. Service Availability** | Not all AWS services or new features are available in every region on launch day. | Amazon Bedrock or specialized GPU instance families might only be available in select tier-1 regions initially. |
| **4. Cost & Pricing** | Prices for compute, storage, and data transfer vary between regions due to local power, real estate, and tax costs. | `us-east-1` (N. Virginia) is generally cheaper than `sa-east-1` (São Paulo, Brazil). |

> [!TIP]
> **Exam Tip:** If a question asks for the **most critical** factor in region selection for a healthcare or financial firm, **Compliance and Legal Regulations (Data Sovereignty)** always trumps cost or latency!

---

## 3. Availability Zones (AZs)

An **Availability Zone (AZ)** consists of one or more discrete physical data centers, each with redundant power, networking, and connectivity, housed in separate facilities.

```mermaid
flowchart LR
    subgraph AZ_Interior ["Internal Architecture of an AZ"]
        DC1["Data Center 1"]
        DC2["Data Center 2"]
        DC3["Data Center 3"]
        DC1 ---|Private Dark Fiber| DC2
        DC2 ---|Private Dark Fiber| DC3
    end
```

### Key Characteristics:
* **Distance & Separation:** AZs in the same Region are separated by a meaningful physical distance (typically tens of miles) to ensure they are on different flood plains, electrical grids, and seismic fault lines.
* **Low-Latency Interconnect:** Despite physical separation, all AZs in a Region are connected via redundant, private dark-fiber networks with single-digit millisecond latency (<1–2 ms).
* **Fault Isolation:** AZs are engineered as independent failure zones. If a catastrophic event strikes one AZ (e.g., substation power failure), other AZs in that region continue operating unaffected.
* **High Availability (HA) Best Practice:** Deploying an application across at least **two Availability Zones (Multi-AZ)** within a Region protects against local infrastructure failures and delivers high availability.

---

## 4. Edge Locations & Point of Presence (PoP)

An **Edge Location** is a physical site where AWS caches content closer to end-users to reduce latency.

### Services Operating at Edge Locations:
1. **Amazon CloudFront:** Content Delivery Network (CDN) that caches static and dynamic web content, videos, APIs, and software downloads.
2. **Amazon Route 53:** Highly available and scalable cloud DNS web service.
3. **AWS Shield Standard & AWS WAF:** Distributed Denial of Service (DDoS) protection and Web Application Firewall rules executed at the network edge before traffic ever hits customer servers.
4. **AWS Global Accelerator:** Routes traffic through edge entry points onto AWS's congestion-free private global network.

### Difference Between AZs and Edge Locations:
* **Availability Zones:** Where you **run your application workloads** (EC2 instances, RDS databases, VPC subnets).
* **Edge Locations:** Where AWS **caches content and handles DNS/routing/edge security** to speed up global delivery. You cannot launch an EC2 instance in an Edge Location!

---

## 5. Low-Latency Hybrid & Edge Extensions

For workloads that cannot tolerate the latency of a regional data center, AWS provides three specialized extensions:

```mermaid
graph TD
    Workload[Your Workload Requirements]
    
    Workload -->|<10ms to urban population| LZ[AWS Local Zones]
    Workload -->|Mobile 5G ultra-low latency| WZ[AWS Wavelength]
    Workload -->|Strict on-prem physical data residency| OP[AWS Outposts]
```

### 1. AWS Local Zones
* **What it is:** Brings AWS compute, storage, database, and select services closer to large population, industry, and IT centers where no AWS Region currently exists (e.g., Los Angeles, Chicago, Hamburg, Taipei).
* **Ideal for:** Video editing/rendering, real-time gaming, CAD design, local healthcare applications requiring single-digit millisecond latency to local end users.

### 2. AWS Wavelength
* **What it is:** Embeds AWS compute and storage services inside telecommunication carriers' 5G networks (e.g., Verizon, Vodafone, KDDI).
* **Ideal for:** Mobile edge computing, connected vehicles (V2X), smart factories, real-time interactive game streaming on 5G mobile devices.
* **Mechanism:** Traffic from 5G devices reaches Wavelength servers directly without leaving the telecom network, eliminating internet hop latency.

### 3. AWS Outposts
* **What it is:** Physical AWS hardware racks and servers installed directly inside the customer’s on-premises data center or co-location facility.
* **Ideal for:** Workloads requiring local data processing for manufacturing plant floor execution systems (MES), ultra-low latency to existing on-premises mainframes, or strict regulatory local data storage mandates.
* **Unified Control:** Outposts hardware is managed, monitored, and patched by AWS using the exact same AWS APIs, tools, and console used in the cloud.

---

## 6. Exam Review Summary Table

| Infrastructure Component | Scope | Primary Purpose | Resilient Architecture Rule |
|---|---|---|---|
| **Region** | Geographic area (country/state) | Global compliance, local latency, full service catalog. | Replicate across multiple Regions for **Disaster Recovery (DR)**. |
| **Availability Zone (AZ)** | Cluster of data centers within a Region | Fault-isolated compute and data persistence. | Deploy across **Multi-AZ** for **High Availability (HA)**. |
| **Edge Location** | Worldwide Points of Presence (PoPs) | Caching, DNS, DDoS protection at perimeter. | Use CloudFront & Route 53 to protect origin servers. |
| **Local Zone** | Urban metro area extension | Single-digit ms latency to urban centers. | Extend VPC subnets into designated Local Zones. |
| **Wavelength Zone** | 5G telecom carrier network | Ultra-low latency for 5G mobile devices. | Deploy mobile app backends into carrier Wavelength subnets. |
| **Outposts** | Customer on-prem data center | On-premises AWS hardware & data residency. | Managed by AWS; connected back to parent AWS Region. |
