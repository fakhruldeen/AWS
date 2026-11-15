# Module 01 Knowledge Check: Cloud Foundations

Test your retention of Module 01 concepts. Review each question before checking the answer key at the bottom.

### Questions
1. **What is an AWS Region?**
   - A) A single physical data center building
   - B) A physical geographical location containing at least three isolated Availability Zones
   - C) A global network of edge locations for caching content
   - D) A software-defined virtual private network
2. **Which cloud advantage refers to provisioning only the exact compute power needed and automatically matching fluctuations in demand?**
   - A) High Availability
   - B) Elasticity
   - C) Fault Tolerance
   - D) Global Reach
3. **What is an Availability Zone (AZ)?**
   - A) One or more discrete data centers with redundant power, networking, and connectivity
   - B) A group of countries sharing the same currency
   - C) A server rack inside an on-premises data center
   - D) An edge cache server in a metropolitan city
4. **Which cloud deployment model combines on-premises infrastructure with AWS cloud services?**
   - A) Public Cloud
   - B) Private Cloud
   - C) Hybrid Cloud
   - D) Community Cloud
5. **Which perspective of the AWS Cloud Adoption Framework (CAF) aligns cloud investments with business strategy and measurable ROI?**
   - A) Business Perspective
   - B) Platform Perspective
   - C) People Perspective
   - D) Security Perspective
6. **Which of the following represents an Operational Expenditure (OpEx)?**
   - A) Purchasing 50 physical blade servers
   - B) Paying a monthly bill for EC2 compute hours consumed
   - C) Building a raised-floor HVAC server room
   - D) Purchasing a 5-year hardware maintenance contract upfront
7. **What is the primary function of an AWS Edge Location?**
   - A) Running heavy relational database workloads
   - B) Caching static and dynamic content closer to end-users via Amazon CloudFront
   - C) Hosting on-premises Active Directory domains
   - D) Providing long-term tape archive storage
8. **What disaster recovery strategy involves running a minimal, scaled-down version of core systems in the cloud that can rapidly scale up if disaster strikes?**
   - A) Backup and Restore
   - B) Pilot Light
   - C) Warm Standby
   - D) Multi-Site Active/Active
9. **How many Availability Zones are included in a standard AWS Region at minimum?**
   - A) 1
   - B) 2
   - C) 3
   - D) 5
10. **Which Well-Architected Framework pillar focuses on the ability of a workload to withstand component failures and dynamically acquire computing resources?**
    - A) Security
    - B) Reliability
    - C) Cost Optimization
    - D) Sustainability

---

### Answer Key & Explanations
| Q# | Answer | Key Concept Reference |
| :---: | :---: | :--- |
| **1** | **B** | AWS Regions are physical geographical locations consisting of at least 3 AZs. |
| **2** | **B** | Elasticity is the ability to acquire resources as demand spikes and release them as demand drops. |
| **3** | **A** | An AZ consists of one or more discrete data centers with independent power and networking. |
| **4** | **C** | Hybrid cloud links on-premises environments with AWS cloud resources. |
| **5** | **A** | The Business perspective of CAF aligns cloud investments with business strategy and KPIs. |
| **6** | **B** | Monthly pay-as-you-go cloud compute is classified as OpEx under standard accounting. |
| **7** | **B** | Edge locations cache content via Amazon CloudFront to deliver lowest latency to end-users. |
| **8** | **B** | Pilot Light runs core components (e.g. database replication) with compute scaled down until needed. |
| **9** | **C** | Every AWS Region contains a minimum of 3 physical Availability Zones. |
| **10** | **B** | Reliability focuses on self-healing recovery, fault tolerance, and multi-AZ resilience. |
