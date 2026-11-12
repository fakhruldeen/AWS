# Distinction Cheat Sheet: Hybrid Connectivity (Direct Connect vs. Site-to-Site VPN vs. Transit Gateway)

> **Role:** Rapid distinction matrix for enterprise hybrid networking scenarios.  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#exam-prep` `#networking` `#hybrid` `#distinction`

---

## 🎯 Architecture Diagram

```mermaid
flowchart TD
    subgraph CorporateHQ ["Corporate Data Center / On-Premises HQ"]
        Router["Customer Gateway (CGW)"]
    end

    subgraph AWSConnectivity ["AWS Edge & Ingestion"]
        DXLocation["AWS Direct Connect Location\n(Dedicated Physical Fiber Link)"]
        VGW["Virtual Private Gateway (VGW)\n(IPsec VPN over Public Internet)"]
        TGW["AWS Transit Gateway\n(Central Hub connecting multiple VPCs & On-Prem)"]
    end

    subgraph CloudVPCs ["AWS Cloud VPCs"]
        VPC1["VPC A (Production)"]
        VPC2["VPC B (Staging)"]
        VPC3["VPC C (Shared Services)"]
    end

    Router -->|Physical Private 1Gbps / 10Gbps / 100Gbps| DXLocation --> TGW
    Router -->|Encrypted IPsec Tunnel (Public Internet)| VGW --> TGW

    TGW --> VPC1
    TGW --> VPC2
    TGW --> VPC3
```

---

## 🔍 Detailed Comparison Table

| Dimension | AWS Site-to-Site VPN | AWS Direct Connect (DX) | AWS Transit Gateway (TGW) |
|:---|:---|:---|:---|
| **Underlying Connection** | IPsec tunnels running over the **public internet** | **Dedicated private physical fiber cable** bypassing the internet | **Central hub router** inside AWS |
| **Setup Time** | **Minutes** | **Weeks to Months** (Requires telco provider cross-connect) | **Minutes** |
| **Bandwidth & Throughput** | Up to 1.25 Gbps per tunnel (limited by internet path) | High bandwidth: **1 Gbps, 10 Gbps, or 100 Gbps** dedicated | Up to 50 Gbps per VPC attachment |
| **Network Consistency & Latency** | Variable latency & jitter (dependent on internet routing) | **Predictable, low latency** and consistent performance | Hub routing performance |
| **Encryption** | **Encrypted by default** in transit using IPsec (AES-256) | **Not encrypted by default** (Can add MACsec or run VPN over DX) | Encrypted within AWS backbone |
| **Cost Structure** | Low hourly connection fee (\$0.05/hr) + data egress | High monthly port fee + significantly **discounted data egress rates** | Hourly fee per attachment + data processing fee |
| **Primary Role** | Quick setup, low cost, backup connection | Mission-critical, high data volume, strict regulatory isolation | Hub-and-spoke interconnect for 100s of VPCs and on-premises networks |

---

## ⚡ High-Yield Exam Clues

* **"Needs a dedicated, private physical connection between on-prem data center and AWS that does NOT traverse the public internet with consistent network performance":**
  👉 **AWS Direct Connect (DX)**
* **"Needs a fast, inexpensive, encrypted connection over the public internet to connect branch offices to an AWS VPC within hours":**
  👉 **AWS Site-to-Site VPN**
* **"Interconnect hundreds of VPCs and multiple on-premises corporate offices in a hub-and-spoke topology without complex peering mesh":**
  👉 **AWS Transit Gateway**
* **"Most cost-effective backup / failover strategy for an existing AWS Direct Connect link":**
  👉 **AWS Site-to-Site VPN** (as backup)
