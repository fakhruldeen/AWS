# Master Architecture Blueprint: Disaster Recovery Strategies Spectrum

> **Category:** Business Continuity & Disaster Recovery  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#disaster-recovery` `#rpo-rto`

```mermaid
flowchart LR
    subgraph Strategy1 ["1. Backup and Restore"]
        S1_Desc["Lowest Cost
Highest RPO / RTO (Hours to Days)
Cold backups in S3 / AWS Backup"]
    end

    subgraph Strategy2 ["2. Pilot Light"]
        S2_Desc["Core data synced continuously (RDS)
Compute servers remain OFF / AMIs ready
RPO: Minutes | RTO: Tens of Minutes"]
    end

    subgraph Strategy3 ["3. Warm Standby"]
        S3_Desc["Scaled-down, live minimal environment running 24/7
Instantly scales up on disaster
RPO: Seconds | RTO: Minutes"]
    end

    subgraph Strategy4 ["4. Multi-Region Active-Active"]
        S4_Desc["Highest Cost & Complexity
Zero Downtime (Near-Zero RPO / RTO)
Traffic split dynamically via Route 53"]
    end

    Strategy1 ===>|"Increasing Cost & Complexity"| Strategy2
    Strategy2 ===>|"Decreasing Downtime (Faster RTO / RPO)"| Strategy3
    Strategy3 ===> Strategy4
```

### Definitions:
- **Recovery Point Objective (RPO):** Maximum acceptable data loss measured in time (e.g., losing 1 hour of database transactions).
- **Recovery Time Objective (RTO):** Maximum acceptable system downtime before application is back online.
