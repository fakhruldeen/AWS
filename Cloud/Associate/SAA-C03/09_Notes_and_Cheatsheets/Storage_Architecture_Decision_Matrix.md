# Storage Architecture Decision Matrix (SAA-C03)

> **Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Topic:** Storage Architecture (Block vs Object vs File vs Hybrid)

---

## 🧭 Executive Decision Framework

```mermaid
flowchart TD
    Req{"What is the Storage Requirement?"}

    Req -->|Key-Value Objects, Static Web, Data Lake, Backups| S3["Amazon S3<br/>• Unlimited object storage<br/>• Up to 5 TB per object<br/>• S3 Intelligent-Tiering, Glacier"]
    Req -->|Single EC2 Instance Boot / High-IOPS Block Storage| EBS["Amazon EBS<br/>• AZ-locked block storage<br/>• gp3 (general) / io2 Block Express (mission-critical)"]
    Req -->|Multi-AZ Concurrent Shared File Access (Linux NFS)| EFS["Amazon EFS<br/>• POSIX-compliant Linux file system<br/>• Multi-AZ concurrent mounting<br/>• Burstable / Elastic throughput"]
    Req -->|High-Performance Windows SMB / HPC Lustre| FSx["Amazon FSx Family<br/>• FSx for Windows (SMB/Active Directory)<br/>• FSx for Lustre (Sub-ms HPC / ML training)"]
```

---

## 📊 Comprehensive Storage Comparison Matrix

| Storage Service | Storage Type | Access Protocol | Scope / Boundary | Max Throughput / IOPS | Concurrent Access | Typical SAA-C03 Use Case |
|---|---|---|---|---|---|---|
| **Amazon S3** | Object | HTTPS REST API | Global namespace (Regional data) | 3,500 PUT / 5,500 GET per prefix | Unlimited via API | Unstructured assets, backups, static websites, data lake storage. |
| **Amazon EBS** | Block | Block volume bus | Single AZ (attached to 1 instance) | Up to 256,000 IOPS (`io2`) | 1 instance (Multi-Attach on `io2` max 16) | EC2 root boot disks, transactional relational databases (PostgreSQL/SQL Server). |
| **Amazon EFS** | File | NFSv4.0 / NFSv4.1 | Regional (Multi-AZ) | 10+ GB/s, 500k+ IOPS (Elastic) | 1,000s of EC2/ECS/Lambda concurrent | Shared WordPress uploads, CI/CD home directories, microservices shared state. |
| **FSx for Windows** | File | SMBv2 / SMBv3 | Single-AZ or Multi-AZ | 12 GB/s, 400k IOPS | Windows / Linux enterprise clients | Microsoft Active Directory enterprise shares, SQL Server Failover Clustering. |
| **FSx for Lustre** | File | POSIX Lustre | Single-AZ / Multi-AZ | 1,000+ GB/s, Millions IOPS | HPC compute nodes / GPUs | Machine learning training datasets, seismic processing, genomic analysis. |

---

## ⚡ High-Yield Exam Traps & Distinctions

1. **EBS Multi-Attach:** Available ONLY on Provisioned IOPS (`io1`/`io2`) within the **same Availability Zone**. Does NOT support cross-AZ attachment. Requires a cluster-aware file system (like GFS2) to prevent data corruption.
2. **EFS vs EBS Multi-AZ:** EBS is strictly confined to a single Availability Zone. If an AZ goes down, the EBS volume is inaccessible until the AZ recovers (unless restored from an S3 snapshot). EFS is **inherently Multi-AZ** and survives AZ outages seamlessly.
3. **S3 Intelligent-Tiering:** Automatically moves objects between frequent, infrequent, and archive access tiers based on access patterns with **zero retrieval fees and zero operational overhead**. Recommended when access patterns are unpredictable or unknown.
4. **S3 Object Lock (WORM):** Write Once, Read Many. Prevents deletion or modification of S3 objects for a fixed retention period. Required for SEC Rule 17a-4 and FINRA compliance.
   - *Governance Mode:* Users with specific IAM permissions (`s3:BypassGovernanceRetention`) can delete objects.
   - *Compliance Mode:* **No one** (including the AWS root account) can delete or alter the object until the retention period expires.
