# Master Architecture Blueprint: Resilient 3-Tier Enterprise Web Application

> **Category:** High Availability, Fault Tolerance & Scalability  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02) / SAA-C03  
> **Tags:** `#diagram` `#vpc` `#ha` `#three-tier`

```mermaid
flowchart TD
    User["End-User Client (Web Browser)"] --> Route53["Amazon Route 53
(Global DNS with Health Checks)"]
    Route53 --> CF["Amazon CloudFront
(Global CDN Edge Caching + AWS WAF Layer 7)"]
    
    subgraph VPC ["Amazon VPC (10.0.0.0/16 in Region us-east-1)"]
        IGW["Internet Gateway (IGW)"]
        CF --> IGW

        subgraph PublicSubnets ["Public Subnets (Web Ingress Tier)"]
            ALB["Application Load Balancer (ALB)
(Multi-AZ Public Listener)"]
            NAT1["NAT Gateway (AZ 1A)"]
            NAT2["NAT Gateway (AZ 1B)"]
        end
        IGW --> ALB

        subgraph PrivateAppSubnets ["Private Subnets (Application Compute Tier)"]
            subgraph ASG ["EC2 Auto Scaling Group"]
                EC2_A["EC2 Web Instance (AZ 1A)"]
                EC2_B["EC2 Web Instance (AZ 1B)"]
            end
        end
        ALB -->|Port 80/443| EC2_A
        ALB -->|Port 80/443| EC2_B
        EC2_A -.->|Outbound Updates| NAT1 --> IGW
        EC2_B -.->|Outbound Updates| NAT2 --> IGW

        subgraph PrivateDataSubnets ["Isolated Database Subnets (Data Tier)"]
            subgraph RDS ["Amazon RDS Aurora Multi-AZ"]
                PrimaryDB["Aurora Primary Writer (AZ 1A)"]
                ReplicaDB["Aurora Read Replica / Standby (AZ 1B)"]
                PrimaryDB <==|Synchronous Block Replication|==> ReplicaDB
            end
            Cache["Amazon ElastiCache Redis
(In-Memory Session & Query Cache)"]
        end
        EC2_A --> PrimaryDB
        EC2_B --> PrimaryDB
        EC2_A <--> Cache
        EC2_B <--> Cache
    end
```

### Architectural Highlights:
- **No Direct Internet Access to Servers:** EC2 instances sit in private subnets; only the ALB has a public IP.
- **Multi-AZ Redundancy:** If Availability Zone 1A experiences an outage, ALB routes 100% of traffic to AZ 1B, and Aurora automatically promotes the standby replica to primary writer in under 30 seconds.
- **In-Memory Caching:** ElastiCache offloads frequent read queries from Aurora, dropping read latency to sub-millisecond speeds.
