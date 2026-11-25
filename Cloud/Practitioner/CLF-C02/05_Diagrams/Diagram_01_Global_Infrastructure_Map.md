# Master Architecture Blueprint: AWS Global Infrastructure

> **Category:** Global Architecture & Resilience  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02) / SAA-C03  
> **Tags:** `#diagram` `#global-infra` `#architecture`

```mermaid
flowchart TD
    subgraph GlobalPlane ["AWS Global Network Backbone (Redundant 100GbE Terrestrial & Undersea Fiber)"]
        direction TB
        
        subgraph Region1 ["AWS Region (e.g., us-east-1 N. Virginia)"]
            direction LR
            AZ1["Availability Zone 1A
(Isolated Data Centers)"]
            AZ2["Availability Zone 1B
(Isolated Data Centers)"]
            AZ3["Availability Zone 1C
(Isolated Data Centers)"]
            AZ1 <-->|Low-Latency Ultra-High Speed Fiber sub-1ms| AZ2
            AZ2 <-->|Low-Latency Ultra-High Speed Fiber sub-1ms| AZ3
            AZ1 <-->|Low-Latency Ultra-High Speed Fiber sub-1ms| AZ3
        end

        subgraph EdgeLayer ["Global Edge Network (600+ Points of Presence)"]
            Edge1["Edge Location (CloudFront / Route 53)"]
            Edge2["Edge Location (API Gateway / WAF)"]
            GA["AWS Global Accelerator (Anycast Static IPs)"]
        end

        subgraph SpecializedEdge ["Specialized Low-Latency Edge Tiers"]
            LocalZone["AWS Local Zones
(Sub-10ms latency in major metro cities)"]
            Wavelength["AWS Wavelength Zones
(Embedded in 5G Telco Networks for Mobile/IoT)"]
            Outposts["AWS Outposts
(Fully managed AWS hardware in customer on-premises data centers)"]
        end
    end

    Users["Global End-User Devices"] --> EdgeLayer
    EdgeLayer -->|Private AWS Global Backbone| Region1
    Users --> SpecializedEdge
```

### Key Conceptual Anchors:
- **Region:** Physical geographical area containing 3 or more isolated Availability Zones connected via low-latency private fiber.
- **Availability Zone (AZ):** One or more discrete data centers with redundant power, networking, and cooling; designed for fault domain isolation.
- **Points of Presence (PoPs):** CloudFront Edge Locations and Regional Edge Caches distributed across 90+ cities in 50+ countries.
- **Local Zones:** Extends AWS compute, storage, and database services to large urban centers (e.g., Los Angeles, Chicago) for latency-sensitive workloads.
- **Wavelength:** Deploys AWS hardware inside telecommunications providers’ 5G data centers for ultra-low latency mobile gaming and autonomous vehicles.
- **Outposts:** AWS racks shipped to physical customer data centers for true hybrid consistency.
