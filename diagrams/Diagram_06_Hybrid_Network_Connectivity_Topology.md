# Master Architecture Blueprint: Hybrid Enterprise Networking Topology

> **Category:** Networking, Transit Gateway & Direct Connect  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#networking` `#direct-connect` `#vpn`

```mermaid
flowchart LR
    subgraph OnPremise ["Corporate Headquarters / On-Premises Data Center"]
        Router["Customer Gateway (CGW)
Border Router (BGP ASN 65000)"]
    end

    subgraph PublicInternet ["Public Internet"]
        VPN["AWS Site-to-Site VPN
(Dual IPsec Tunnels, Encrypted, Setup in Minutes)"]
    end

    subgraph Colocation ["Direct Connect Colocation Facility"]
        DXLocation["AWS Direct Connect Location
(Dedicated Physical Fiber Cross-Connect)"]
    end

    subgraph Hub ["Regional Network Hub"]
        TGW["AWS Transit Gateway (TGW)
(Cloud Router Interconnecting 100s of VPCs & On-Prem)"]
    end

    subgraph CloudVPCs ["AWS VPC Infrastructure"]
        VPC_Prod["Production VPC (10.1.0.0/16)"]
        VPC_Dev["Development VPC (10.2.0.0/16)"]
        VPC_Shared["Shared Services VPC (10.3.0.0/16)"]
    end

    Router -->|"IPsec over Internet"| VPN
    VPN --> TGW
    Router ===|"Physical Fiber Link (1G - 100G)"| DXLocation
    DXLocation ===|"Transit VIF"| TGW

    TGW <--> VPC_Prod
    TGW <--> VPC_Dev
    TGW <--> VPC_Shared
```

### High-Yield Comparison:
- **Site-to-Site VPN:** Fast setup, encrypted over public internet, bandwidth capped at 1.25 Gbps per tunnel, variable internet latency.
- **Direct Connect:** Weeks to provision physical cross-connect, dedicated private fiber bypassing public internet, ultra-consistent sub-millisecond latency, discounted data egress.
- **Transit Gateway:** Hub-and-spoke router eliminating complex point-to-point VPC peering meshes.
