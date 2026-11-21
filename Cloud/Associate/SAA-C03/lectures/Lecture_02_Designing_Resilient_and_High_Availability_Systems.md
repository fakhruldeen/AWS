# Lecture 02: Designing Resilient & High-Availability Systems

> **Course Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Domain 2: Design Resilient Architectures (26% Exam Weighting)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Decouple synchronous monolithic architectures into resilient, asynchronous microservices using SQS, SNS, and EventBridge.
2. Differentiate between SQS Standard and SQS FIFO queues, configuring message deduplication, visibility timeouts, and dead-letter queues (DLQs).
3. Architect highly available multi-AZ compute tiers with Application Load Balancers and Auto Scaling lifecycle hooks.
4. Compare relational high availability in Amazon RDS Multi-AZ versus Amazon Aurora Global Database.
5. Formulate disaster recovery (DR) architectures across the 4 primary tiers: Backup & Restore, Pilot Light, Warm Standby, and Multi-Site Active-Active.

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:00] 1. The Law of Cloud Resilience: "Everything Fails All the Time"
[01:00 - 02:30] 2. Decoupled Messaging Patterns: SQS Standard vs. FIFO, Fan-Out & EventBridge
[02:30 - 04:00] 3. High Availability Compute: ALB, NLB, Auto Scaling Lifecycle Hooks & Target Tracking
[04:00 - 05:00] 4. Database Resilience: RDS Multi-AZ vs. Aurora Multi-AZ & Global Database
[05:00 - 05:45] 5. Disaster Recovery Strategies: Evaluating RTO, RPO & Architecture Tiers
[05:45 - 06:00] 6. Exam Traps & Scenario Walkthroughs
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. Asynchronous Decoupling & Queue Topologies (Whiteboard Prompt)
- *Whiteboard Diagram:* Draw Web Tier $
ightarrow$ SQS Queue $
ightarrow$ EC2 Worker Fleet.
- **Why Decouple?** Without a queue, a traffic surge knocks over the backend database. With SQS, the queue absorbs the shock wave; workers pull messages at their own rate.
- **SQS Standard vs. FIFO:**
  - **Standard:** Nearly unlimited throughput, at-least-once delivery (occasional duplicate messages), best-effort ordering.
  - **FIFO:** Exactly-once processing, preserves chronological order, max 300 msg/sec (or 3,000 msg/sec with batching). Requires `.fifo` suffix, `MessageGroupId`, and `MessageDeduplicationId`.
- **The Fan-Out Architecture:** When one event must reach multiple independent services, publish to an **Amazon SNS Topic**, which pushes copies to multiple subscribed **Amazon SQS Queues**.

### 2. Load Balancers: ALB vs. NLB
- **Application Load Balancer (ALB):** Layer 7 (HTTP/HTTPS/gRPC). Features: path-based routing (`/api`), host-based routing (`app.example.com`), redirect HTTP to HTTPS, user authentication (OIDC/Cognito), inserts client IP into `X-Forwarded-For` header. Dynamic IP addresses!
- **Network Load Balancer (NLB):** Layer 4 (TCP/UDP/TLS). Extreme performance: millions of requests per second with microsecond latencies. Provides **static IP addresses** (one per AZ) or Elastic IPs. Preserves client IP directly in the packet header for instance targets.

### 3. Database High Availability: RDS Multi-AZ vs. Aurora
- **RDS Multi-AZ:** Synchronous physical replication to a passive standby in a second AZ. Standby cannot handle read traffic! Automated failover in under 60 seconds.
- **Amazon Aurora:** 6 copies of data replicated across 3 AZs. Storage volume auto-scales up to 128 TiB. Up to 15 Read Replicas sharing the same underlying storage volume with milliseconds replication lag. Any replica can be promoted to primary during failover in under 30 seconds.
- **Aurora Global Database:** Cross-region storage replication with RPO < 1s and RTO < 1m.

### 4. Disaster Recovery (DR) Spectrum
| DR Strategy | Cost | RTO (Recovery Time Objective) | RPO (Recovery Point Objective) | Key Infrastructure |
|---|---|---|---|---|
| **Backup & Restore** | $\$$ (Lowest) | Hours to 24h | Hours to 24h | S3, AWS Backup, AMIs |
| **Pilot Light** | $\$ \$$ | Tens of minutes | Minutes | Replicating DB running; compute launched via IaC on failover |
| **Warm Standby** | $\$ \$ \$$ | Minutes | Seconds to Minutes | Scaled-down running copy of all tiers 24/7 |
| **Multi-Site Active-Active** | $\$ \$ \$ \$$ (Highest) | Real-time (near zero) | Near zero | Multi-region full capacity, Route 53, Aurora Global / DynamoDB Global |

---

## 🚨 SAA-C03 Exam Traps & Anti-Patterns

1. **Attempting to Read from an RDS Standby:** An RDS Multi-AZ standby replica is strictly for failover and cannot accept read queries! If the exam asks to offload read reporting, the answer is **RDS Read Replicas**, not Multi-AZ standby.
2. **Dropping Connections During ASG Scale-In:** If EC2 instances abruptly terminate and drop active HTTP requests, the fix is enabling **Deregistration Delay** (Connection Draining) on the ALB target group, paired with an ASG **Lifecycle Hook**.
3. **Scaling Worker Fleets on CPU:** If an EC2 fleet processes messages from SQS, scaling on CPU is a trap. The correct Well-Architected metric is the custom metric **Backlog per Instance** (`ApproximateNumberOfMessagesVisible / Number of Instances`).

---

## 🔬 Hands-on Lab & Homework Alignment
- **Hands-on Lab:** Guide students through [Lab 02: HA & Scalable Web Tier (ALB + ASG)](../phase2_step07_labs/lab_02_ha_scalable_web_tier_asg_alb.md), [Lab 03: Aurora Fault-Tolerant Database](../phase2_step07_labs/lab_03_aurora_fault_tolerant_relational_database.md), and [Lab 04: Decoupled Microservices (SQS + SNS)](../phase2_step07_labs/lab_04_decoupled_asynchronous_microservices_sqs_sns.md).
- **Knowledge Check:** Assign [Module 02 Knowledge Check](../phase4_step10_knowledge_checks/Module_02_Resilient_Architectures_Knowledge_Check.md).
- **Revision Questions:** Direct students to practice [Domain 2 Revision Questions](../phase4_step11_revision_questions/Domain_2_Design_Resilient_Architectures_Revision_Questions.md).
