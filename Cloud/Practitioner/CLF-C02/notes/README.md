# 📝 AWS Certified Cloud Practitioner (CLF-C02) High-Yield Study Notes & Cheat Sheets

> **Module:** Rapid Study Notes, Distinction Tables & Exam Cheat Sheets  
> **Course:** AWS Certified Cloud Practitioner (`CLF-C02`)  
> **Exam Version Alignment:** Official v1.2 (2026 Edition)  
> **Target Audience:** Students, engineers, and exam candidates in their final sprint review.

---

## 🗺️ Master Notes & Distinction Index

### 1. Rapid Review Cheatsheet (The Final Sprint Guide)
* **[Rapid_Review_Cheatsheet.md](./Rapid_Review_Cheatsheet.md)** — Comprehensive single-page revision guide covering the 6 Advantages of Cloud Computing, CAF 3.0 (6 Perspectives), 7 Rs Migration Strategies, 5-Layer Defense-in-Depth, EC2 Pricing Decision Tree, S3 Storage Classes, and Support Plans.

---

### 2. High-Yield "X vs. Y" Distinction Tables (`distinctions/`)
Side-by-side comparison matrices designed to eliminate confusion on the most frequently failed exam questions:

| Distinction Guide | Services / Concepts Compared | Core Exam Discriminator |
| :--- | :--- | :--- |
| **[AWS_Support_Plans_Comparison_Matrix.md](./distinctions/AWS_Support_Plans_Comparison_Matrix.md)** | Basic vs Developer vs Business vs Enterprise On-Ramp vs Enterprise | Response times, TAM allocation, Architecture guidance, Concierge support. |
| **[Disaster_Recovery_Strategies_Comparison.md](./distinctions/Disaster_Recovery_Strategies_Comparison.md)** | Backup & Restore vs Pilot Light vs Warm Standby vs Multi-Site Active/Active | RTO / RPO tradeoffs and cost profiles. |
| **[Monitoring_Governance_Trio.md](./distinctions/Monitoring_Governance_Trio_CloudWatch_vs_CloudTrail_vs_Config.md)** | CloudWatch vs CloudTrail vs AWS Config | Metrics/Logs vs API Auditing vs Compliance & Configuration history. |
| **[Security_Services_Four_Guardians.md](./distinctions/Security_Services_Four_Guardians_Shield_WAF_GuardDuty_Inspector_Macie.md)** | AWS Shield vs WAF vs GuardDuty vs Inspector vs Macie | DDoS vs L7 Web Attacks vs Threat Detection vs Vulnerability Scans vs S3 PII. |
| **[KMS_vs_CloudHSM_vs_SecretsManager.md](./distinctions/KMS_vs_CloudHSM_vs_SecretsManager_vs_ParameterStore.md)** | KMS vs CloudHSM vs Secrets Manager vs Parameter Store | Multi-tenant vs Dedicated FIPS 140-2 Level 3 vs Auto-Rotation vs Hierarchical config. |
| **[Hybrid_Networking_Comparison.md](./distinctions/Hybrid_Networking_DirectConnect_vs_SiteToSiteVPN_vs_TransitGateway.md)** | Direct Connect vs Site-to-Site VPN vs Transit Gateway | Dedicated physical line vs Encrypted internet tunnel vs Multi-VPC hub. |
| **[VPC_Endpoints_Gateway_vs_Interface.md](./distinctions/VPC_Endpoints_Gateway_vs_Interface_vs_PrivateLink.md)** | Gateway Endpoints (S3/DynamoDB) vs Interface Endpoints (PrivateLink) | Route table target (Free) vs ENI with private IP ($/hr). |
| **[Storage_and_Hybrid_Comparison.md](./distinctions/Storage_and_Hybrid_AWS_Backup_vs_DataSync_vs_StorageGateway.md)** | AWS Backup vs DataSync vs Storage Gateway | Centralized backup policy vs Online data migration vs Hybrid cache. |
| **[AWS_Health_Dashboard_Comparison.md](./distinctions/AWS_Health_Dashboard_Global_vs_Account.md)** | Global Service Health vs Account-Specific Health | Public service outages vs Personal impacted resources. |
| **[Developer_and_Mobile_Comparison.md](./distinctions/Developer_and_Mobile_Amplify_vs_DeviceFarm_vs_AppSync.md)** | AWS Amplify vs Device Farm vs AppSync | Full-stack app framework vs Real mobile device testing vs GraphQL APIs. |

---

## 🎯 How to Use These Notes for Revision

1. **Sprint Review:** Read [Rapid_Review_Cheatsheet.md](./Rapid_Review_Cheatsheet.md) 24–48 hours before the exam.
2. **Targeted Disambiguation:** Whenever you hesitate between two similar AWS services, review the corresponding matrix in `distinctions/`.
3. **Question Practice:** Drill with the [Master Unique Revision Banks](../../../../Documents/Obsidian%20Vault/Brain/AWS/Questions_Bank/Unique_Revision_Banks/Cloud_Practitioner_CLF-C02/README.md) and sit the timed [65-Question Mock Exam](../revision_questions/CLF_C02_Full_Length_Mock_Revision_Exam.md).
