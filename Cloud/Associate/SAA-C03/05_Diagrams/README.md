# 📐 SAA-C03 Production Architecture Blueprints (Mermaid)

> **Module:** Standalone Architectural Diagrams & Blueprints  
> **Target Certification:** AWS Certified Solutions Architect - Associate (`SAA-C03`)  

---

## 🗺️ Master Blueprints Index

1. **Multi-Tier Resilient VPC Architecture:** Public, Application, and Database subnets across 2 Availability Zones.
2. **High-Availability Web Tier:** ALB with dynamic Auto Scaling Groups and target health checks.
3. **Fault-Tolerant Aurora Topology:** Primary Writer instance with synchronous cross-AZ replicas and auto-failover.
4. **Decoupled Asynchronous Microservices:** API Gateway -> SQS Queue -> Worker Lambda -> DynamoDB with DLQ fanout.
5. **Hybrid Connectivity Blueprint:** Direct Connect Gateway and Transit Gateway hub-and-spoke interconnecting multiple VPCs.
