---
marp: true
theme: default
paginate: true
header: "AWS Cloud Practitioner (CLF-C02) - Student Training"
footer: "© AWS Cloud Training Course | Module 3: Networking, Security & Identity"
style: |
  section {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    padding: 40px;
    background-color: #fafafa;
  }
  h1 {
    color: #232f3e;
  }
  h2 {
    color: #ff9900;
  }
  .highlight {
    background-color: #fff3cd;
    padding: 2px 6px;
    border-radius: 4px;
  }
---

# AWS Certified Cloud Practitioner
## Module 3: Networking, Security & Identity Management
**Domains 2 & 3: Security, Compliance & Cloud Technology**

*Instructor Delivery Deck & Student Lecture Notes*

---

# Amazon VPC: Virtual Private Cloud

Amazon VPC is your **logically isolated private virtual network in the AWS Cloud**.

### Key VPC Building Blocks:
- **CIDR Blocks:** Define IPv4 IP address ranges (e.g., `10.0.0.0/16`).
- **Subnets:** Segments of IP ranges tied to specific Availability Zones:
  - **Public Subnet:** Route table has route to an **Internet Gateway (IGW)**.
  - **Private Subnet:** No direct route to IGW; shielded from public internet.
- **NAT Gateway (Network Address Translation):**
  - Resides in a **Public Subnet**.
  - Allows instances in Private Subnets to make **outbound connections to the internet** (for software updates) while **blocking inbound connections**.

---

# Security Groups vs. Network ACLs (NACLs)

```
Internet ──> [ Network ACL (Subnet) ] ──> [ Security Group (Instance) ] ──> EC2
```

| Dimension | Security Groups (SG) | Network ACLs (NACL) |
| :--- | :--- | :--- |
| **Operating Level** | **Instance Level** (Virtual NIC). | **Subnet Level** (Applies to all instances in subnet). |
| **Supported Rules** | **ALLOW rules only** (cannot block an IP). | **ALLOW and DENY rules**. |
| **State Nature** | **Stateful:** Return traffic is automatically allowed regardless of outbound rules. | **Stateless:** Inbound and outbound traffic must be explicitly allowed. |
| **Rule Processing** | Evaluates **all rules** before granting access. | Evaluates in **numerical order** (lowest number first). |
| **Default State** | All inbound blocked; all outbound allowed. | Default NACL allows all inbound and outbound. |

---

# Global Routing & Edge Networking

### Amazon Route 53 (Authoritative Cloud DNS)
- Translates domain names (`example.com`) into IP addresses.
- **Alias Records:** Specialized AWS records mapped to the **Zone Apex** (`example.com`) pointing to ELBs, CloudFront, or S3 with zero query cost.
- **Routing Policies:** Simple, Weighted, Latency, Failover (Active-Passive), Geolocation, Geoproximity, Multi-Value.

### Amazon CloudFront (Content Delivery Network - CDN)
- Globally distributed network of **Edge Locations**.
- Caches static and dynamic web content closer to users for ultra-low latency.
- Protects origins using **Origin Access Control (OAC)** and SSL/TLS termination.

---

# AWS Identity and Access Management (IAM)

IAM securely manages access to AWS services and resources.

```
       [ IAM Root User ] ──> Complete Administrative Control (Secure with MFA!)
              │
              ├── [ IAM Groups ] (e.g. Developers, Admins)
              │         │
              │         └── [ IAM Users ] (Individual identities: Alice, Bob)
              │
              └── [ IAM Roles ] (Temporary credentials assumed by EC2 / Lambda)
```

- **Principle of Least Privilege:** Grant only the minimum permissions necessary.
- **IAM Policies (JSON):** Documents defining permissions (`Effect: Allow/Deny`, `Action`, `Resource`, `Condition`).
- **IAM Roles:** Grant temporary security credentials using **AWS STS**; no long-term access keys stored on servers.

---

# Shared Responsibility Model: Who Owns What?

```
               ┌────────────────────────────────────────────────────────┐
               │              Customer: Security IN the Cloud           │
               │  Customer Data, IAM & Access, OS & Network/Firewall    │
               │  Platform & App Management, Client/Server Encryption   │
               └────────────────────────────────────────────────────────┘
               ┌────────────────────────────────────────────────────────┐
               │                 AWS: Security OF the Cloud             │
               │  Physical Data Centers, Hardware & Hypervisors         │
               │  Global Networking Infrastructure, Managed Services    │
               └────────────────────────────────────────────────────────┘
```

- **Infrastructure as a Service (EC2):** Customer patches guest OS, configures firewalls, and updates software.
- **Platform / Managed Services (RDS, S3):** AWS patches OS and database software; customer manages data, encryption, and bucket policies.
- **Serverless (Lambda):** AWS manages servers, runtime environment, and scaling; customer manages code and execution IAM roles.

---

# AWS Security & Compliance Services

| Service | Primary Responsibility |
| :--- | :--- |
| **AWS WAF** | **Web Application Firewall:** Filters Layer 7 traffic (SQL injection, XSS). |
| **AWS Shield** | **DDoS Protection:** Standard (Free Layer 3/4) vs. Advanced (Managed mitigation, cost protection). |
| **AWS KMS** | **Key Management Service:** Create and control cryptographic encryption keys (AES-256). |
| **AWS Secrets Manager** | Securely stores and **automatically rotates database credentials** (RDS, Aurora). |
| **Amazon GuardDuty** | Intelligent threat detection analyzing CloudTrail, VPC Flow Logs, and DNS queries. |
| **Amazon Inspector** | Automated vulnerability assessments for EC2, Lambda, and ECR container images. |
| **Amazon Macie** | Uses Machine Learning to discover and protect **Sensitive Personal Data (PII)** in S3. |
| **AWS Artifact** | Portal providing on-demand access to **AWS compliance reports** (SOC, PCI-DSS, ISO). |

---

# Summary & Key Takeaways

1. **Security Groups vs. NACLs:**
   - Security Groups = Stateful, instance level, ALLOW rules only.
   - NACLs = Stateless, subnet level, supports explicit DENY rules.
2. **Route 53 Alias Records:** Allows mapping the Zone Apex (`example.com`) to AWS resources.
3. **IAM Least Privilege:** Always attach policies to Groups or Roles, never hardcode root keys.
4. **Shared Responsibility:** AWS protects the cloud hardware; you protect your data, access policies, and configurations.
5. **Secrets Manager:** The only service that provides automated database password rotation out of the box.
