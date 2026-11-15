# Master Architecture Blueprint: Shared Responsibility Model Shift

> **Category:** Security, Governance & Compliance  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#security` `#shared-responsibility`

```mermaid
flowchart TD
    subgraph IaaS ["Infrastructure as a Service (IaaS): Amazon EC2"]
        direction TB
        I_Cust["CUSTOMER:
- Customer Data & Encryption
- IAM Identity, MFA, Credentials
- OS Patching & Updates
- Antivirus & Host Firewalls
- Network Routing & Security Groups
- Application Code & Middleware"]
        I_AWS["AWS:
- Physical Data Center Facilities
- Power, HVAC & Biometric Security
- Hardware Server Racking & Decommissioning
- Hypervisor & Virtualization Layer"]
        I_Cust ---|Boundary of Responsibility| I_AWS
    end

    subgraph PaaS ["Platform as a Service (PaaS / Managed): Amazon RDS"]
        direction TB
        P_Cust["CUSTOMER:
- Customer Data & Schema Design
- Database Engine Configuration Parameters
- IAM Authentication & Network Access
- User Permissions & Data Encryption"]
        P_AWS["AWS:
- Physical Infrastructure & Hypervisor
- Operating System Installation & Patching
- Database Engine Patching & Minor Upgrades
- Automated Daily Backups & Point-in-Time Recovery
- Multi-AZ Storage Synchronous Replication"]
        P_Cust ---|Boundary of Responsibility| P_AWS
    end

    subgraph Serverless ["Serverless / Abstracted: AWS Lambda & Amazon S3"]
        direction TB
        S_Cust["CUSTOMER:
- Customer Data & Storage Policies
- Application Code & Function Logic
- IAM Execution Roles & Resource Policies
- Client-Side / Server-Side Encryption Settings"]
        S_AWS["AWS:
- Server Provisioning & Capacity Autoscaling
- Operating System & Execution Runtime (Python/Node/Java)
- High Availability across 3+ AZs Automatically
- Hardware Maintenance & Storage Disk Degaussing"]
        S_Cust ---|Boundary of Responsibility| S_AWS
    end
```

### Golden Rules:
1. **Customer Data:** Always 100% the customer responsibility across all services.
2. **Identity & Access Management:** Always 100% the customer responsibility.
3. **Physical Security OF the Cloud:** Always 100% AWS responsibility.
