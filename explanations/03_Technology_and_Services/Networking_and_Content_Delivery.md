# AWS Networking & Content Delivery — Map of Content (MOC)

> **Domain:** 03_Services / Networking & Content Delivery  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], SAA-C03, Advanced Networking

---

## 1. Architectural Taxonomy of AWS Networking

AWS networking services provide the foundational connectivity, isolation, traffic routing, edge acceleration, and hybrid bridges for all cloud workloads:

```mermaid
flowchart TD
    Net["AWS Networking & Content Delivery"]
    
    subgraph VPC_Core["1. VPC Core & Traffic Distribution"]
        VPC["Amazon VPC (Subnets, IGW, NAT GW, Route Tables, NACLs, SGs)"]
        ELB["Elastic Load Balancing / ELB (ALB, NLB, GWLB)"]
        TGW["AWS Transit Gateway (Hub-and-spoke multi-VPC router)"]
    end
    
    subgraph Edge_DNS["2. Edge Routing & Content Delivery"]
        R53["Amazon Route 53 (Global DNS, Health Checks, Routing Policies)"]
        CF["Amazon CloudFront (Edge CDN Caching & DDoS Shield)"]
        GA["AWS Global Accelerator (Anycast Static IPs & TCP/UDP optimization)"]
    end
    
    subgraph Hybrid["3. Hybrid Connectivity (On-Prem to AWS)"]
        VPN["AWS Site-to-Site VPN (IPsec encrypted tunnels over Internet)"]
        DX["AWS Direct Connect (Dedicated physical private fiber link)"]
        ClientVPN["AWS Client VPN (OpenVPN remote worker desktop client)"]
    end
    
    Net --> VPC_Core
    Net --> Edge_DNS
    Net --> Hybrid
```

---

## 2. Decision Tree: Global Edge Acceleration & Routing

```mermaid
flowchart LR
    Start{"Global Traffic Need?"}
    Start -->|"Domain Name Registration & DNS Resolution"| R53["Amazon Route 53"]
    
    Start -->|"Cache HTTP content (Images, Videos, Web Pages)"| CF["Amazon CloudFront"]
    
    Start -->|"Optimize non-HTTP TCP/UDP (Gaming, VoIP) or Need Static Anycast IPs"| GA["AWS Global Accelerator"]
    
    Start -->|"Connect Corporate HQ to AWS"| HybridChoice{"Connection Nature?"}
    HybridChoice -->|"Fast setup, low cost, encrypted over Internet"| VPN["AWS Site-to-Site VPN"]
    HybridChoice -->|"Dedicated physical fiber, consistent throughput, private"| DX["AWS Direct Connect"]
```

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[Amazon_VPC]]** | Virtual Private Cloud | Subnets, Internet Gateway, NAT Gateway, Security Groups vs. NACLs. |
| **[[AWS_Elastic_Load_Balancing_ELB]]** | Elastic Load Balancing | ALB (Layer 7 HTTP), NLB (Layer 4 static IP/ultra-low latency), GWLB. |
| **[[Amazon_Route53]]** | Highly Available DNS Service | Latency, Geolocation, Failover, Weighted, Multivalue, Alias Records. |
| **[[Amazon_CloudFront]]** | Content Delivery Network (CDN) | Edge Locations, Caching, Origin Access Control (OAC), DDoS protection. |
| **[[AWS_Global_Accelerator]]** | Global Traffic Accelerator | Anycast static IPs, AWS global fiber backbone, 60% latency reduction. |
| **[[AWS_Transit_Gateway]]** | Centralized Cloud Router | Hub-and-spoke topology, eliminates complex VPC peering meshes. |
| **[[AWS_Site_to_Site_VPN]]** | IPsec VPN Connection | Fast, secure encrypted tunnel over the public internet. |
| **[[AWS_Direct_Connect]]** | Dedicated Private Connection | Bypasses public internet entirely; consistent throughput, lower data egress costs. |
| **[[AWS_Client_VPN]]** | Managed Remote Access VPN | Secure OpenVPN client for remote employees accessing VPC resources. |
