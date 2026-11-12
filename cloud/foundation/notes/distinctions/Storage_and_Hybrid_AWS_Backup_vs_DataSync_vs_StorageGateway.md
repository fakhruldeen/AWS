# Exam Distinction Cheat Sheet: AWS Backup vs. AWS DataSync vs. AWS Storage Gateway

> **Core Topic:** Storage, Backup Automation & Hybrid Cloud  
> **Target Exam:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Source Origin:** Classroom - Manara Course Revision Notes & Official AWS Documentation

---

## The "X vs. Y vs. Z" Comparison Matrix

| Exam Dimension | AWS Backup | AWS DataSync | AWS Storage Gateway |
| :--- | :--- | :--- | :--- |
| **Primary Architectural Role** | **Centralized Backup Automation:** Fully managed, policy-based backup service to automate data protection across AWS services and hybrid workloads. | **High-Speed Online Data Transfer:** Accelerated online data migration and scheduled sync service between storage systems. | **Seamless Hybrid Storage Bridge:** Hybrid cloud storage appliance presenting standard storage protocols (NFS, SMB, iSCSI) to local on-premises applications. |
| **Supported Services / Protocols** | Amazon DynamoDB, RDS, EBS, EFS, S3, Aurora, DocumentDB, Neptune, Timestream, Storage Gateway, VMware Cloud. | NFS, SMB, HDFS, Object Storage (S3-compatible) <-> Amazon S3, Amazon EFS, Amazon FSx. | Local NFS/SMB shares (File Gateway), iSCSI block disks (Volume Gateway), iSCSI Virtual Tape Library (Tape Gateway). |
| **Operational Workflow** | Centralized backup policies, automated retention schedules, lifecycle rules (transitioning backups to cold storage), cross-Region and cross-account backup replication. | One-time massive data migration or automated recurring synchronization tasks running over network links (up to 10x faster than rsync). | Continuous, bidirectional local caching; hot working data stays on-premises, cold data tiers automatically to Amazon S3. |
| **Application Impact** | Zero impact; managed service that snapshots and backs up resources in the background. | Batch sync job; runs independently of application workflows. | **Zero application changes:** Legacy on-premises apps connect directly to standard local storage shares. |

---

## 🎯 Exam Trigger Scenarios & Keywords

### Scenario 1:
> *"A company needs a centralized solution to automate backup policies, enforce retention periods, and replicate backups across AWS Regions for Amazon DynamoDB, Amazon RDS, Amazon EFS, and Amazon EBS from a single console. Which service should they choose?"*  
> **Correct Answer:** **AWS Backup** (centralized, policy-driven backup automation across multiple AWS services).

### Scenario 2:
> *"An enterprise needs to transfer 50 TB of research data from an on-premises NAS over the internet to Amazon S3 as fast as possible, with automated integrity verification and bandwidth throttling. Which service should they choose?"*  
> **Correct Answer:** **AWS DataSync** (high-speed, automated online data transfer service up to 10x faster than rsync).

### Scenario 3:
> *"A hospital wants to eliminate physical tape backup hardware and offsite storage costs while continuing to use its existing on-premises backup software without any configuration changes. Which service should they choose?"*  
> **Correct Answer:** **AWS Storage Gateway (Tape Gateway)** (replaces physical tapes with virtual tapes stored in Amazon S3 Glacier).

---

## 💡 Quick Memory Hook
- **AWS Backup** = **Protect It** (Automated centralized snapshot & retention schedules across AWS services).
- **AWS DataSync** = **Move It** (High-speed bulk file transfer over network).
- **Storage Gateway** = **Bridge It** (NFS/SMB/iSCSI local access backed by cloud storage).
