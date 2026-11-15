# Domain 1: Cloud Concepts Revision Questions (24% Exam Weight)

### Question 1
A startup company needs to launch a new web application globally with unpredictable traffic. They want to avoid large upfront capital expenditures and pay only for compute resources consumed. Which cloud advantage best describes this benefit?
- [ ] A) High Availability
- [ ] B) Trading fixed capital expense for variable expense
- [ ] C) Increasing speed and agility
- [ ] D) Benefiting from massive economies of scale
> **Correct Answer:** B  
> **Rationale:** Trading fixed capital expenditure (CapEx) for variable operational expenditure (OpEx) allows companies to pay solely for the capacity consumed rather than investing upfront in physical servers.

---

### Question 2
Under the AWS Cloud Adoption Framework (AWS CAF 3.0), which perspective focuses on identifying the skills gaps in the current workforce and developing modern cloud engineering training curricula?
- [ ] A) Business Perspective
- [ ] B) Governance Perspective
- [ ] C) People Perspective
- [ ] D) Operations Perspective
> **Correct Answer:** C  
> **Rationale:** The People perspective focuses on culture, organizational structure, cloud leadership, skills development, and closing workforce competence gaps.

---

### Question 3
An architectural design mandates that if an entire physical data center loses power due to a flood, application traffic must instantly continue processing without human intervention. Which design principle does this implement?
- [ ] A) Deploying across multiple AWS Accounts
- [ ] B) Deploying across multiple Availability Zones in a Region
- [ ] C) Scaling vertically to a larger instance type
- [ ] D) Storing static files in EBS rather than S3
> **Correct Answer:** B  
> **Rationale:** Availability Zones within an AWS Region are physically separated by meaningful distance and equipped with isolated redundant power, cooling, and networking.

---

### Question 4
Which disaster recovery strategy incurs the lowest ongoing infrastructure cost while accepting an RTO (Recovery Time Objective) and RPO (Recovery Point Objective) measured in hours to days?
- [ ] A) Multi-Site Active/Active
- [ ] B) Warm Standby
- [ ] C) Pilot Light
- [ ] D) Backup and Restore
> **Correct Answer:** D  
> **Rationale:** Backup and Restore is the most cost-effective DR strategy because no active compute runs in the recovery region during normal operations; data is backed up to S3 and restored only after a disaster.

---

### Question 5
Which pillar of the AWS Well-Architected Framework emphasizes the ability to support development and run workloads effectively, gain insight into their operations, and continuously improve supporting processes?
- [ ] A) Operational Excellence
- [ ] B) Reliability
- [ ] C) Performance Efficiency
- [ ] D) Sustainability
> **Correct Answer:** A  
> **Rationale:** Operational Excellence focuses on running and monitoring systems, responding to events, and defining standards to manage daily operations through code.
