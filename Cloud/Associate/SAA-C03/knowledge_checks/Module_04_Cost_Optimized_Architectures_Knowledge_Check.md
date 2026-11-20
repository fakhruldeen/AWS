# Module 04: Designing Cost-Optimized Architectures — Knowledge Check

> **Track:** AWS Certified Solutions Architect - Associate (SAA-C03)  
> **Module:** Module 4: FinOps, Storage Lifecycle & Compute Economics  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 4 materials and completing the high-yield decision notes. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
A compliance law mandates that digital financial audit logs must be retained for 10 years. Records are accessed fewer than once a year, and retrieval delays of 12 to 48 hours are acceptable. Which S3 storage class provides the lowest storage cost?

- **A.** Amazon S3 Standard
- **B.** Amazon S3 Standard-IA
- **C.** Amazon S3 Glacier Flexible Archive
- **D.** Amazon S3 Glacier Deep Archive

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **D**

**Explanation:**
- **Amazon S3 Glacier Deep Archive** is S3's lowest-cost storage class (~$0.00099/GB/month), roughly 23x cheaper than S3 Standard and 4x cheaper than Glacier Flexible Archive, designed for data accessed once or twice a year with retrieval times of 12-48 hours.
</details>

---

### Question 2
An S3 bucket stores petabytes of data with unpredictable and fluctuating access patterns. The company wants to automatically save costs on infrequently accessed data while avoiding per-GB data retrieval fees. Which storage class should be used?

- **A.** Amazon S3 Intelligent-Tiering
- **B.** Amazon S3 Standard-IA
- **C.** Amazon S3 One Zone-IA
- **D.** Amazon S3 Glacier Instant Retrieval

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon S3 Intelligent-Tiering** automatically moves objects between frequent, infrequent, and archive access tiers based on changing access patterns. Crucially, it charges **zero retrieval fees**, preventing unexpected cost spikes when dormant data is accessed.
</details>

---

### Question 3
A fleet of 40 EC2 instances in a private subnet transfers 80 TB of data monthly to Amazon S3 through a NAT Gateway, incurring thousands of dollars in NAT Gateway data processing fees ($0.045/GB). How can the architect completely eliminate these processing fees?

- **A.** Deploy an Interface VPC Endpoint for Amazon S3
- **B.** Deploy a Gateway VPC Endpoint for Amazon S3 and update the private route table
- **C.** Assign Elastic IPs to the EC2 instances
- **D.** Replace the NAT Gateway with an EC2 NAT instance

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Gateway VPC Endpoints** for Amazon S3 are provided at **no charge** (zero hourly and zero data processing fees). Directing S3 traffic through the Gateway Endpoint bypasses the NAT Gateway completely, saving $0.045/GB on all S3 data transfers.
</details>

---

### Question 4
A company processes stateless batch rendering jobs that can be interrupted and resumed without data corruption. The management requires up to 90% savings compared to On-Demand prices. Which purchasing option should be selected?

- **A.** On-Demand Instances
- **B.** EC2 Spot Instances
- **C.** Standard Reserved Instances
- **D.** Dedicated Hosts

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **Amazon EC2 Spot Instances** take advantage of spare EC2 capacity at steep discounts of up to 90% off On-Demand rates, ideal for fault-tolerant, flexible batch workloads.
</details>

---

### Question 5
An enterprise runs steady-state workloads across EC2 instances, AWS Fargate containers, and AWS Lambda functions across multiple regions, and plans to switch instance types from x86 to Graviton. Which commitment discount model offers maximum flexibility across compute types, instance families, and regions?

- **A.** Compute Savings Plans
- **B.** EC2 Instance Savings Plans
- **C.** Standard Reserved Instances
- **D.** Convertible Reserved Instances

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Compute Savings Plans** provide up to 66% savings and apply automatically to eligible compute usage regardless of instance family (C5 vs C7g), instance size, OS, tenancy, region, or compute type (EC2, Fargate, Lambda).
- **EC2 Instance Savings Plans** provide higher discounts (up to 72%) but are locked to a specific instance family in a specific region.
</details>

---

### Question 6
A development team runs 25 relational staging database instances on PostgreSQL that are only used during business hours (40 hours/week) and idle at night and on weekends. Which database option scales capacity down to 0.5 ACU during idle off-hours to drastically reduce costs?

- **A.** Amazon Aurora Serverless v2
- **B.** Amazon RDS for PostgreSQL Multi-AZ
- **C.** Amazon DynamoDB with Provisioned Capacity
- **D.** Amazon Redshift Dense Compute

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon Aurora Serverless v2** dynamically scales compute capacity up and down in fractions of a second based on load, scaling down to as low as 0.5 ACU during idle periods, dramatically cutting costs for development and intermittent workloads.
</details>

---

### Question 7
A company has millions of 10 KB log files uploaded daily. An engineer creates an S3 Lifecycle rule to transition all objects to S3 Standard-IA after 30 days. Why might this increase monthly storage costs?

- **A.** S3 Standard-IA has a minimum billable object size of 128 KB.
- **B.** S3 Standard-IA charges an hourly encryption fee.
- **C.** S3 Standard-IA deletes objects under 1 MB.
- **D.** S3 Standard-IA only supports video files.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **S3 Standard-IA** and Glacier storage classes enforce a **minimum billable object size of 128 KB**. Transitioning a 10 KB object results in being billed for 128 KB of storage (a 12.8x increase in billable storage volume), plus per-request transition fees.
</details>

---

### Question 8
Which AWS service uses machine learning on historical CloudWatch metrics to provide automated right-sizing recommendations for over-provisioned EC2 instances, EBS volumes, and Lambda functions?

- **A.** AWS Cost Explorer
- **B.** AWS Compute Optimizer
- **C.** AWS Trusted Advisor
- **D.** AWS Pricing Calculator

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**

**Explanation:**
- **AWS Compute Optimizer** uses machine learning to evaluate historical resource utilization metrics to recommend optimal AWS resources for workloads, helping eliminate over-provisioning and lower costs by up to 25%.
</details>

---

### Question 9
A company wants to host a public company website consisting entirely of static HTML, CSS, client-side JS, and images, receiving 50,000 visitors per month with high availability and lowest possible cost (<$1/month). Which architecture should be deployed?

- **A.** Amazon S3 Static Website Hosting behind Amazon CloudFront with Origin Access Control (OAC)
- **B.** Auto Scaling group of EC2 instances behind an Application Load Balancer
- **C.** Single large EC2 instance with Elastic IP
- **D.** AWS Elastic Beanstalk Docker container

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Amazon S3 static website hosting with Amazon CloudFront** is completely serverless. CloudFront caches assets at edge locations worldwide while S3 provides 11 9s durability. With no running virtual machines or load balancer base hourly fees, costs are typically pennies per month.
</details>

---

### Question 10
An organization with 30 member accounts wants to combine usage across accounts to qualify for tiered S3 volume discounts and receive a single consolidated bill. Which feature should be used?

- **A.** AWS Organizations Consolidated Billing
- **B.** AWS Control Tower Guardrails
- **C.** AWS Budgets
- **D.** AWS Systems Manager

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
- **Consolidated Billing** in AWS Organizations aggregates usage across all member accounts, allowing the organization to reach higher volume discount tiers (e.g., S3 tiered storage rates where price per GB drops above 50 TB) as if it were a single account, with a single consolidated invoice.
</details>
