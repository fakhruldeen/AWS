# AWS Cloud Adoption Framework (AWS CAF) & Migration Strategies

> **Knowledge Area:** Cloud Concepts (Domain 1.3) & Migration (Domain 3.8)  
> **Relevant Certifications:** [CLF-C02](../../01_Syllabus/CLF-C02_Master_Blueprint.md), SAA-C03  
> **Tags:** `#aws/concepts` `#aws/migration` `#clf-c02`

---

## 1. Overview of AWS CAF 3.0

The **AWS Cloud Adoption Framework (AWS CAF)** provides actionable guidance that helps organizations digitally transform and accelerate their cloud adoption journey.

The framework organizes guidance into **6 Perspectives**, split equally between **Business Capabilities** and **Technical Capabilities**:

```mermaid
graph TD
    subgraph CAF ["AWS Cloud Adoption Framework (6 Perspectives)"]
        subgraph BusinessFocus ["Business Capabilities"]
            B1["1. Business Perspective"]
            B2["2. People Perspective"]
            B3["3. Governance Perspective"]
        end
        
        subgraph TechnicalFocus ["Technical Capabilities"]
            T1["4. Platform Perspective"]
            T2["5. Security Perspective"]
            T3["6. Operations Perspective"]
        end
    end
```

---

## 2. The 6 Perspectives Breakdown

### Business Capabilities (Focus on Business Strategy & Alignment):

1. **Business Perspective:**
   * *Target Stakeholders:* Business managers, finance managers, strategy leaders.
   * *Core Focus:* Ensures that cloud investments align with business outcomes, return on investment (ROI), revenue generation, and business model innovation.
2. **People Perspective:**
   * *Target Stakeholders:* Human resources, training leaders, organizational change managers.
   * *Core Focus:* Prepares the workforce for cloud adoption, bridging skills gaps through training, organizational change management, and building high-performing cross-functional teams.
3. **Governance Perspective:**
   * *Target Stakeholders:* CIO, program managers, project managers, enterprise architects.
   * *Core Focus:* Orchestrates cloud initiatives, manages cloud portfolio priorities, measures cloud value, and ensures program alignment with organizational goals.

---

### Technical Capabilities (Focus on Implementation & Architecture):

4. **Platform Perspective:**
   * *Target Stakeholders:* CTO, technology leaders, solutions architects, developers.
   * *Core Focus:* Designing, implementing, and optimizing cloud architecture, landing zones, migration strategies, and modern cloud application development.
5. **Security Perspective:**
   * *Target Stakeholders:* CISO, security officers, compliance and risk managers.
   * *Core Focus:* Ensures the organization meets security, identity, data privacy, and compliance requirements in the cloud without slowing down innovation.
6. **Operations Perspective:**
   * *Target Stakeholders:* Operations managers, Site Reliability Engineers (SREs), IT support leads.
   * *Core Focus:* Operating, monitoring, automating, and maintaining cloud workloads according to agreed service-level agreements (SLAs).

---

## 2.5 The Four Phases of AWS CAF (`Envision → Align → Launch → Scale`)

AWS CAF 3.0 structures every organization's cloud transformation journey into **four sequential phases**:

```mermaid
flowchart LR
    P1["1. Envision<br/>Align cloud to business outcomes"] --> P2["2. Align<br/>Identify capability gaps across 6 Perspectives"]
    P2 --> P3["3. Launch<br/>Deliver production pilot initiatives"]
    P3 --> P4["4. Scale<br/>Expand pilots enterprise-wide"]
```

| Phase | Core Objective | Key Activities & Exam Clues |
| :--- | :--- | :--- |
| **1. Envision** | **Demonstrate how cloud accelerates business outcomes** | Identify high-impact transformation opportunities, link them to the **4 Business Outcomes** (*Reduced Business Risk, Improved ESG, Increased Revenue, Increased Operational Efficiency*), and secure executive sponsorship. |
| **2. Align** | **Identify capability gaps across all 6 Perspectives** | Assess readiness across Business, People, Governance, Platform, Security, and Operations; resolve cross-organizational dependencies and build an actionable roadmap. |
| **3. Launch** | **Deliver pilot initiatives in production** | Deploy initial production pilot workloads to demonstrate incremental business value quickly, learn from real-world feedback, and refine processes before mass migration. |
| **4. Scale** | **Expand production pilots to enterprise scale** | Replicate validated patterns across the organization, automate landing zones and governance, and realize full business value at scale. |

---

## 3. The 7 Rs of Cloud Migration

When migrating existing on-premises workloads to AWS, organizations classify each application into one of the **7 Migration Strategies ("7 Rs")**:

```mermaid
graph TD
    App[On-Premises Application]
    
    App -->|No code change / Lift & Shift| Rehost["1. Rehost (Lift-and-Shift)\nAWS Application Migration Service (MGN)"]
    App -->|Minor optimization / Cloud tweaks| Replatform["2. Replatform (Lift, Tinker & Shift)\nMove to Managed RDS or Containers"]
    App -->|Complete rewrite for cloud-native| Refactor["3. Refactor / Rearchitect\nServerless Lambda, Microservices"]
    App -->|Switch to SaaS or commercial product| Repurchase["4. Repurchase (Drop and Shop)\nMove to SaaS CRM / Marketplace"]
    App -->|Do nothing / Keep on-prem for now| Retain["5. Retain (Revisit later)\nKeep due to strict compliance / legacy"]
    App -->|Decommission / Shut down| Retire["6. Retire\nNo longer needed / Unused apps"]
    App -->|Move VMs without changing hypervisor| Relocate["7. Relocate (Hypervisor level)\nVMware Cloud on AWS"]
```

| Strategy | Alias | Description | Effort | Speed | Typical Tools |
|---|---|---|---|---|---|
| **Rehost** | Lift-and-Shift | Move applications without changing any code or architecture. | Low | Fastest | **AWS Application Migration Service (MGN)** |
| **Replatform** | Lift, Tinker & Shift | Make minor optimizations without altering core code (e.g., migrating an on-prem DB to Amazon RDS). | Medium | Fast | AWS DMS, AWS Elastic Beanstalk |
| **Refactor** | Rearchitect | Re-imagine application architecture from scratch to be cloud-native (serverless, microservices). | High | Slowest | AWS Lambda, Amazon ECS/EKS, DynamoDB |
| **Repurchase** | Drop and Shop | Discard custom application and switch to a SaaS solution or commercial package. | Low-Med | Fast | AWS Marketplace |
| **Retain** | Keep as-is | Leave legacy application on-premises because migration is not yet feasible or cost-effective. | None | N/A | Hybrid VPN / Direct Connect |
| **Retire** | Decommission | Identify and shut down applications that are no longer actively used by the business. | Low | Fast | AWS Application Discovery Service |
| **Relocate** | Hypervisor Shift | Move existing VMware or containerized workloads directly to AWS without converting VM formats. | Low | Fast | VMware Cloud on AWS |

---

## 4. Key AWS Migration Services Portfolio

```mermaid
flowchart LR
    subgraph Discovery ["1. Discovery & Planning"]
        ADS["AWS Application Discovery Service"]
        ME["Migration Evaluator"]
        MH["AWS Migration Hub"]
    end

    subgraph DataTransfer ["2. Bulk Data Movement"]
        Snow["AWS Snow Family (Peta/Exabyte)"]
        Sync["AWS DataSync (Automated Online)"]
    end

    subgraph Execution ["3. Server & DB Migration"]
        MGN["AWS Application Migration Service (MGN)"]
        DMS["AWS Database Migration Service (DMS)"]
        SCT["AWS Schema Conversion Tool (SCT)"]
    end

    Discovery --> DataTransfer
    Discovery --> Execution
```

1. **AWS Migration Hub:** A single unified dashboard to track the progress of migrations across multiple AWS and partner solutions (MGN, DMS).
2. **AWS Application Discovery Service:** Plans migration projects by automatically discovering on-premises server specifications, CPU/RAM utilization, and network dependency mappings. (Offers *Agentless Collector* for VMware and *Discovery Agent* for physical servers).
3. **AWS Application Migration Service (AWS MGN):** The primary AWS service for **Rehosting (lift-and-shift)** servers to AWS with minimal downtime and continuous block-level data replication.
4. **AWS Database Migration Service (AWS DMS):** Migrates relational databases, data warehouses, and NoSQL databases to AWS. Keeps source database **fully operational and online** during migration. Supports homogeneous (MySQL -> MySQL) and heterogeneous (Oracle -> PostgreSQL) migrations.
5. **AWS Schema Conversion Tool (AWS SCT):** Automatically converts source database schemas, stored procedures, and triggers from commercial engines (Oracle, SQL Server) to open-source targets (Aurora, PostgreSQL, MySQL).
6. **AWS Snow Family:** Physical, ruggedized hardware appliances to transport massive data volumes offline:
   - *AWS Snowcone:* Portable, lightweight (8 TB).
   - *AWS Snowball Edge:* Storage & compute-optimized (80 TB to 210 TB).
   - *AWS Snowmobile:* 45-foot ruggedized shipping container truck for exabyte-scale migrations (up to 100 PB per truck).

---

## 5. Exam Tip Matrix

| Exam Scenario | Correct Service / Strategy |
|---|---|
| *"Wants to move 200 on-premises Windows and Linux servers to AWS with minimal configuration change"* | **Rehost** using **AWS Application Migration Service (MGN)** |
| *"Migrating Oracle to Amazon Aurora while keeping the production database running without downtime"* | **AWS Database Migration Service (DMS)** + **AWS Schema Conversion Tool (SCT)** |
| *"Company needs to transfer 500 TB of data to S3 from a remote location with limited 10 Mbps internet bandwidth"* | **AWS Snowball Edge** (physical offline transfer) |
| *"Which CAF perspective focuses on bridging staff cloud skill gaps and change management?"* | **People Perspective** |
| *"Which CAF perspective focuses on ROI, business model innovation, and financial justification?"* | **Business Perspective** |
| *"Single pane of glass to monitor migration progress across servers and databases"* | **AWS Migration Hub** |
