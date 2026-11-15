# AWS Storage Services — Map of Content (MOC)

> **Domain:** 03_Services / Storage  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], SAA-C03, SysOps

---

## 1. Architectural Taxonomy of AWS Storage

AWS divides storage services across three fundamental paradigms—**Object Storage**, **Block Storage**, and **File Storage**—alongside hybrid and data transfer appliances:

```mermaid
flowchart TD
    Storage["AWS Storage Portfolio"]
    
    subgraph Object["1. Object Storage (Any volume, HTTP/REST)"]
        S3["Amazon S3 (Standard, IA, Glacier, 11 9s durability)"]
    end
    
    subgraph Block["2. Block Storage (Dedicated low-latency disks)"]
        EBS["Amazon EBS (Persistent virtual drive for single EC2)"]
        InstanceStore["Instance Store (Ephemeral, physical host NVMe SSD)"]
    end
    
    subgraph File["3. File Storage (Shared hierarchical POSIX / SMB)"]
        EFS["Amazon EFS (Elastic Linux NFSv4, multi-instance)"]
        FSx["Amazon FSx (Windows File Server, Lustre, NetApp, OpenZFS)"]
    end
    
    subgraph Hybrid_Data["4. Hybrid & Data Movement"]
        StorageGW["AWS Storage Gateway (File, Volume, Tape Gateways)"]
        DataSync["AWS DataSync (High-speed online transfer agent)"]
        Snow["AWS Snow Family (Snowcone, Snowball, Snowmobile)"]
    end
    
    Storage --> Object
    Storage --> Block
    Storage --> File
    Storage --> Hybrid_Data
```

---

## 2. Decision Tree: Choosing the Right Storage Service

```mermaid
flowchart LR
    Start{"Storage Type Needed?"}
    
    Start -->|"Web images, videos, backups, big data lake"| S3["Amazon S3"]
    
    Start -->|"EC2 Boot disk / Transactional OS drive"| BlockChoice{"Persistence Needed?"}
    BlockChoice -->|"Yes, survives instance stop"| EBS["Amazon EBS"]
    BlockChoice -->|"No, ultra-fast temporary cache"| InstStore["Amazon EC2 Instance Store"]
    
    Start -->|"Shared file system across 100+ servers"| FileChoice{"OS / Protocol?"}
    FileChoice -->|"Linux (NFS)"| EFS["Amazon EFS"]
    FileChoice -->|"Windows (SMB) / High Perf Lustre"| FSx["Amazon FSx"]
    
    Start -->|"Migrate petabytes from On-Prem"| NetSpeed{"Network Bandwidth?"}
    NetSpeed -->|"High speed network link (>10 Gbps)"| DataSync["AWS DataSync"]
    NetSpeed -->|"Slow / Limited network link (<1 Gbps)"| Snow["AWS Snow Family"]
```

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[Amazon_S3]]** | Simple Storage Service | Buckets, Storage Classes, Lifecycle Rules, Versioning, S3 Object Lock. |
| **[[Amazon_EBS]]** | Elastic Block Store | `gp3`, `io2`, `st1`, `sc1`, Snapshots, Multi-Attach, single AZ. |
| **[[Amazon_EC2_Instance_Store]]** | Ephemeral Host Storage | Maximum IOPS/performance, data lost on instance stop/termination. |
| **[[Amazon_EFS]]** | Elastic File System | Managed Linux NFS, multi-AZ, scales automatically, concurrent mount. |
| **[[Amazon_FSx]]** | Specialized File Systems | FSx for Windows File Server (SMB), FSx for Lustre (HPC/ML). |
| **[[AWS_Storage_Gateway]]** | Hybrid Storage Bridge | S3 File Gateway, Volume Gateway (Stored/Cached), Tape Gateway. |
| **[[AWS_DataSync]]** | Automated Data Transfer | 10x faster online transfer between on-prem storage and S3/EFS/FSx. |
| **[[AWS_Snow_Family]]** | Physical Data Migration Devices | Snowcone (8 TB), Snowball Edge (80 TB), Snowmobile (up to 100 PB). |
| **[[Block_and_File_Storage_EBS_EFS]]** | Comparison Guide | Detailed architectural breakdown comparing EBS vs. EFS. |
