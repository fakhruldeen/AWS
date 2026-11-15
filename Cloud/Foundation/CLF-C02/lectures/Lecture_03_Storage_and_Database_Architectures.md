# Lecture 03: Storage & Database Architectures

## ⏱️ Timing & Delivery Strategy
- **Duration:** 120 Minutes
- **Lecture Slide Deck:** `slides/Module_02_Compute_Storage_and_Databases_Slides.md` (Part 2)
- **Hands-On Transition:** `labs/lab_07_s3_storage_lifecycle.md` & `labs/lab_09_rds_database_ha.md`

## 🎯 Learning Objectives
1. Categorize storage types: Amazon S3 (Object), Amazon EBS (Block), and Amazon EFS (Shared File).
2. Master S3 Storage Classes (Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive).
3. Contrast Relational (Amazon RDS, Aurora) vs. NoSQL (Amazon DynamoDB) architectures.
4. Understand Multi-AZ synchronous replication vs. asynchronous Read Replicas.

## 🗣️ Instructor Talking Points & Common Traps
- **Trap 1: Multi-AZ vs. Read Replicas:** Students constantly confuse these on the exam!
  - *Multi-AZ:* For **High Availability & Disaster Recovery**. Synchronous replication. Standby instance cannot accept read traffic. Automated failover.
  - *Read Replicas:* For **Read Performance Scalability**. Asynchronous replication. Accepts read-only queries. Does NOT provide automatic failover unless manually promoted.
- **Trap 2: EBS Multi-Attach vs. EFS:** EBS `io2` supports Multi-Attach for clustered enterprise databases (like Oracle RAC) within a *single AZ*. For generic Linux multi-instance file sharing across *multiple AZs*, always choose **Amazon EFS**.
