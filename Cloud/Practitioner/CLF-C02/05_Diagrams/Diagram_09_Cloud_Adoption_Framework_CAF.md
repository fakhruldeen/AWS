# Master Architecture Blueprint: AWS Cloud Adoption Framework & Migration

> **Category:** Cloud Adoption & Migration Strategy  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#caf` `#migration` `#7rs`

```mermaid
flowchart TD
    subgraph CAF ["AWS Cloud Adoption Framework (CAF 3.0) - 6 Perspectives"]
        subgraph BizFocus ["Business Capabilities"]
            P_Biz["1. Business Perspective (Strategy, ROI, Business Outcomes)"]
            P_People["2. People Perspective (Training, Skills Gap, Change Management)"]
            P_Gov["3. Governance Perspective (Portfolio Management, Value Tracking)"]
        end

        subgraph TechFocus ["Technical Capabilities"]
            P_Plat["4. Platform Perspective (Architecture, Landing Zones, Cloud-Native)"]
            P_Sec["5. Security Perspective (Compliance, Identity, Data Protection)"]
            P_Ops["6. Operations Perspective (SRE, Monitoring, Operating SLAs)"]
        end
    end

    subgraph Phases ["The Four Phases of AWS CAF Transformation Journey"]
        Ph1["1. Envision<br/>Align Cloud to Business Outcomes"] --> Ph2["2. Align<br/>Identify Capability Gaps across 6 Perspectives"]
        Ph2 --> Ph3["3. Launch<br/>Deliver Production Pilot Workloads"]
        Ph3 --> Ph4["4. Scale<br/>Expand Pilots Enterprise-Wide"]
    end

    subgraph SevenRs ["The 7 Migration Strategies (7 Rs)"]
        R1["1. Rehost (Lift-and-Shift -> AWS MGN)"]
        R2["2. Replatform (Lift, Tinker & Shift -> Managed RDS)"]
        R3["3. Refactor / Rearchitect (Serverless & Microservices)"]
        R4["4. Repurchase (Drop & Shop -> SaaS / Marketplace)"]
        R5["5. Retain (Keep on-premises for now)"]
        R6["6. Retire (Decommission unused apps)"]
        R7["7. Relocate (Hypervisor shift -> VMware Cloud on AWS)"]
    end

    CAF -.->|Executed Through| Phases
    Phases -.->|Guides Application Strategy| SevenRs
```
