# AWS Certified Cloud Practitioner (CLF-C02) - Domain 4: Billing, Pricing, and Support Revision Questions

> **Weight:** 12% of Scored Content  
> **Questions Count:** 20 Curated Exam-Style Practice Questions  
> **Target Certification:** AWS Certified Cloud Practitioner (`CLF-C02`)  

---

## 📝 Practice Questions

### Question 1 (Category: aws-billing-pricing-support)
A company wants to reduce costs on EC2 instances that run a stable, predictable production workload 24/7. Which purchasing option would provide the GREATEST cost savings?

- [ ] {'label': 'A', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Spot Instances', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Reserved Instances or Savings Plans with a 3-year commitment', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Dedicated Hosts with no commitment', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** For stable, predictable workloads that run 24/7, Reserved Instances or Savings Plans with a 3-year term offer the greatest discounts — up to 72% compared to On-Demand pricing. On-Demand (A) provides flexibility but no discount. Spot Instances (B) offer deep discounts but can be interrupted with little notice, making them unsuitable for production workloads requiring constant availability. Dedicated Hosts without a commitment (D) are among the most expensive options.
</details>

### Question 2 (Category: aws-billing-pricing-support)
Which Amazon EC2 pricing model provides the largest discount (up to 90% off On-Demand prices) but allows AWS to interrupt the instance with a two-minute warning?

- [ ] {'label': 'A', 'text': 'Reserved Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Spot Instances', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Dedicated Hosts', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity at up to 90% off On-Demand prices. The trade-off is that AWS can reclaim (interrupt) Spot Instances with a two-minute notification when it needs the capacity back. Reserved Instances offer up to 72% savings with a 1- or 3-year commitment but are not interruptible. On-Demand Instances have no discount and no commitment. Dedicated Hosts provide a physical server dedicated to your use but are the most expensive option.
</details>

### Question 3 (Category: aws-billing-pricing-support)
A company runs a batch image processing job every night that can be stopped and restarted without any issues. The job typically takes 3-4 hours to complete. Which EC2 pricing model would be the most cost-effective?

- [ ] {'label': 'A', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Spot Instances', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Reserved Instances (1-year, All Upfront)', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Dedicated Instances', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Spot Instances are ideal for workloads that are fault-tolerant and can handle interruptions — batch processing jobs that can be stopped and restarted are a classic Spot use case. Spot pricing offers up to 90% savings over On-Demand. On-Demand would work but costs significantly more. Reserved Instances require a 1- or 3-year commitment, which is overkill for a nightly batch job. Dedicated Instances are the most expensive and are used for regulatory or licensing requirements, not cost savings.
</details>

### Question 4 (Category: aws-billing-pricing-support)
A company has a steady-state production database running 24/7 on Amazon EC2. The workload is predictable and will continue for at least 3 years. Which pricing option provides the greatest cost savings?

- [ ] {'label': 'A', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Spot Instances', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Reserved Instances (3-year, All Upfront)', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Savings Plans (1-year, No Upfront)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Reserved Instances with a 3-year term and All Upfront payment provide the deepest discount (up to 72% off On-Demand). For a predictable, steady-state workload running 24/7 for at least 3 years, this is the most cost-effective option. Spot Instances are not appropriate because databases cannot tolerate interruptions. On-Demand provides no discount. A 1-year Savings Plan with No Upfront offers a smaller discount than a 3-year Reserved Instance with All Upfront.
</details>

### Question 5 (Category: aws-billing-pricing-support)
A company wants to reduce costs by committing to a consistent amount of compute usage (measured in $/hour) for 1 or 3 years, with the flexibility to change instance types, operating systems, and even switch between EC2 and Lambda. Which pricing model offers this flexibility?

- [ ] {'label': 'A', 'text': 'EC2 Reserved Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Compute Savings Plans', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Spot Instances', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'EC2 Instance Savings Plans', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Compute Savings Plans offer the most flexibility among commitment-based pricing models. You commit to a consistent amount of compute usage (in $/hour) for 1 or 3 years, and in return, you receive discounted pricing. The key advantage is that this discount applies across any EC2 instance family, size, OS, tenancy, or Region, and also applies to AWS Fargate and AWS Lambda usage. EC2 Reserved Instances and EC2 Instance Savings Plans are locked to a specific instance family and Region. Spot Instances are not commitment-based.
</details>

### Question 6 (Category: aws-billing-pricing-support)
A company needs to run a legacy Windows application that requires a specific software license tied to physical server hardware. Which EC2 pricing option allows them to use their own server-bound software licenses?

- [ ] {'label': 'A', 'text': 'Spot Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Dedicated Hosts', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Reserved Instances', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** EC2 Dedicated Hosts provide a physical server fully dedicated to your use. This is important for software licenses that are tied to specific physical hardware (per-socket, per-core, or per-VM licensing models) such as Windows Server, SQL Server, or Oracle Database. Spot Instances, On-Demand Instances, and standard Reserved Instances all run on shared physical infrastructure, which does not satisfy hardware-bound license requirements. Dedicated Hosts give you visibility into the physical server, including sockets and cores.
</details>

### Question 7 (Category: aws-billing-pricing-support)
A startup expects unpredictable traffic spikes for a new mobile app. The company does not want to commit to a long-term contract. Which EC2 pricing model is MOST appropriate?

- [ ] {'label': 'A', 'text': 'On-Demand Instances', 'is_correct': True}
- [ ] {'label': 'B', 'text': 'Reserved Instances', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Dedicated Hosts', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Spot Instances', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**  

- **Detailed Explanation:** On-Demand Instances let you pay by the second (or hour) with no upfront commitment or long-term contract. This is ideal for unpredictable workloads. Reserved Instances require a 1- or 3-year commitment. Spot Instances can be interrupted with short notice, making them risky for user-facing apps. Dedicated Hosts are for compliance-driven workloads and are the most expensive option.
</details>

### Question 8 (Category: aws-billing-pricing-support)
A company has a stable, predictable database workload that will run continuously for the next three years. Which pricing option will provide the GREATEST cost savings?

- [ ] {'label': 'A', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Spot Instances', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Reserved Instances with All Upfront payment for 3 years', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Reserved Instances with No Upfront payment for 1 year', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Reserved Instances with a 3-year term and All Upfront payment offer the highest discount (up to 72% off On-Demand). The longer the commitment and the more you pay upfront, the greater the discount. 1-year No Upfront still saves money but less than 3-year All Upfront. Spot Instances are interruptible, so they are unsuitable for a database. On-Demand is the most expensive option for sustained workloads.
</details>

### Question 9 (Category: aws-billing-pricing-support)
A data analytics team needs to run a large batch processing job that can tolerate interruptions. Which EC2 pricing model offers the DEEPEST discount?

- [ ] {'label': 'A', 'text': 'On-Demand Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Savings Plans', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'Spot Instances', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'Reserved Instances', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** Spot Instances offer up to 90% discount compared to On-Demand pricing, making them the cheapest option. However, AWS can reclaim them with a 2-minute warning when it needs the capacity back. This makes them ideal for fault-tolerant, interruptible workloads like batch processing, data analysis, and CI/CD pipelines. Savings Plans and Reserved Instances offer up to 72% savings but require commitments.
</details>

### Question 10 (Category: aws-billing-pricing-support)
Which pricing model provides flexible pricing across EC2, Lambda, and Fargate in exchange for a commitment to a consistent amount of compute usage (measured in $/hour) for 1 or 3 years?

- [ ] {'label': 'A', 'text': 'Reserved Instances', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Compute Savings Plans', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Spot Instances', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'On-Demand Instances', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Compute Savings Plans offer up to 66% savings and apply automatically to EC2, Lambda, and Fargate usage regardless of instance family, size, OS, tenancy, or Region. You commit to a consistent amount of compute usage ($/hr) for 1 or 3 years. Reserved Instances are locked to a specific instance type in a specific Region. Spot Instances have no commitment but can be interrupted. On-Demand has no discount.
</details>

### Question 11 (Category: aws-billing-pricing-support)
A company wants to visualize its AWS spending over the past 12 months and forecast future costs. Which tool should they use?

- [ ] {'label': 'A', 'text': 'AWS Budgets', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Cost Explorer', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Pricing Calculator', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Cost and Usage Report (CUR)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Cost Explorer provides an interactive interface to visualize, understand, and manage AWS costs and usage over time. By default it can show up to the last 13 months of historical data and forecast costs for the next 18 months. AWS Budgets is for setting spending thresholds and alerts. The Pricing Calculator estimates costs for new architectures. CUR provides the most granular raw billing data but is not a visualization tool.
</details>

### Question 12 (Category: aws-billing-pricing-support)
A finance team wants to receive an email alert whenever their monthly AWS spending is projected to exceed $10,000. Which service should they configure?

- [ ] {'label': 'A', 'text': 'AWS Cost Explorer', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Budgets', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Trusted Advisor', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Cost Anomaly Detection', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Budgets lets you set custom cost and usage budgets with configurable alert thresholds. When actual or forecasted spend exceeds your defined threshold, Budgets sends notifications via email or SNS. Cost Explorer visualizes past spending but does not send alerts. Trusted Advisor provides best-practice recommendations. Cost Anomaly Detection uses ML to detect unusual spending patterns but is not designed for fixed-threshold budget alerts.
</details>

### Question 13 (Category: aws-billing-pricing-support)
Which AWS tool provides the MOST detailed and granular billing data, which can be delivered to an S3 bucket for analysis with Athena or Quick Sight?

- [ ] {'label': 'A', 'text': 'AWS Budgets', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Cost Explorer', 'is_correct': False}
- [ ] {'label': 'C', 'text': 'AWS Cost and Usage Report (CUR)', 'is_correct': True}
- [ ] {'label': 'D', 'text': 'AWS Billing Dashboard', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **C**  

- **Detailed Explanation:** The AWS Cost and Usage Report (CUR) is the most comprehensive billing dataset available. It can be delivered to an S3 bucket and includes hourly or daily line items for every service, resource tags, and pricing details. It integrates with Athena, Redshift, and Amazon Quick Sight for advanced analysis. Cost Explorer provides visualizations but not raw data. Budgets is for alerting. The Billing Dashboard shows a high-level summary.
</details>

### Question 14 (Category: aws-billing-pricing-support)
A solutions architect wants to estimate the monthly cost of a proposed AWS architecture before deploying it. Which tool should they use?

- [ ] {'label': 'A', 'text': 'AWS Cost Explorer', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Pricing Calculator', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Cost and Usage Report', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Budgets', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** The AWS Pricing Calculator is a free web-based planning tool that lets you estimate the cost of AWS services for your specific use case before you deploy anything. You configure services, regions, and usage amounts to get a monthly estimate. Cost Explorer analyzes historical spending. CUR reports on actual usage. Budgets tracks spending against thresholds. None of these estimate costs for architectures that do not exist yet.
</details>

### Question 15 (Category: aws-billing-pricing-support)
A company notices an unexpected spike in its AWS bill. Which service uses machine learning to automatically detect unusual spending patterns and alert the team?

- [ ] {'label': 'A', 'text': 'AWS Budgets', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Cost Anomaly Detection', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon Inspector', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Trusted Advisor', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Cost Anomaly Detection uses machine learning models to continuously monitor spending patterns and automatically detect anomalous (unusual) costs. It can send alerts via SNS or email when anomalies are found. AWS Budgets alerts on fixed thresholds, not anomalies. Amazon Inspector is a security vulnerability scanning service. Trusted Advisor provides general best-practice checks, not ML-based anomaly detection.
</details>

### Question 16 (Category: aws-billing-pricing-support)
A corporation has 15 AWS accounts across different business units. They want a single bill and the ability to share volume pricing discounts. Which feature should they use?

- [ ] {'label': 'A', 'text': 'AWS Cost Explorer', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Consolidated billing with AWS Organizations', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'AWS Budgets', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Multiple linked credit cards', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Consolidated billing is a feature of AWS Organizations that combines usage from all member accounts into a single bill paid by the management account. This aggregation can qualify for volume pricing discounts (e.g., S3 or EC2 tiered pricing) because usage is pooled. Cost Explorer visualizes costs but does not combine billing. Budgets sets alerts. You cannot share discounts by linking multiple credit cards.
</details>

### Question 17 (Category: aws-billing-pricing-support)
Which benefit does consolidated billing in AWS Organizations provide?

- [ ] {'label': 'A', 'text': 'Automatic provisioning of resources across accounts', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Combined usage across accounts for potential volume discounts', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Free AWS Support upgrades for all member accounts', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Automatic security compliance for all member accounts', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** The primary benefit of consolidated billing is that it aggregates usage across all member accounts, potentially qualifying for tiered pricing discounts on services like S3, EC2, and data transfer. It does not provision resources, upgrade support plans, or enforce security compliance. Those are handled by other AWS Organizations features like Service Control Policies (SCPs) or separate support subscriptions.
</details>

### Question 18 (Category: aws-billing-pricing-support)
Which AWS Support plan is automatically included at no additional cost for ALL AWS accounts?

- [ ] {'label': 'A', 'text': 'Business Support+', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Basic Support', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Enterprise Support', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Unified Operations', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Basic Support is included with AWS accounts and provides account and billing assistance, service-health information, documentation, community resources, and core Trusted Advisor guidance. Premium technical-support plans such as Business Support+, Enterprise Support, and Unified Operations are paid offerings.
</details>

### Question 19 (Category: aws-billing-pricing-support)
A company wants to purchase and deploy a pre-configured third-party firewall appliance that runs on AWS. Where should they look?

- [ ] {'label': 'A', 'text': 'AWS Partner Network (APN)', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'AWS Marketplace', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Amazon AppStream 2.0', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'AWS Service Catalog', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** AWS Marketplace is a digital catalog of thousands of software listings from independent software vendors (ISVs). Customers can find, buy, and deploy software that runs on AWS, including security appliances, databases, machine learning models, and more. APN is a partner program for consulting and technology partners, not a purchasing catalog. Amazon AppStream 2.0 (now Amazon WorkSpaces Applications) is an application streaming service. Service Catalog lets organizations create and manage approved IT services.
</details>

### Question 20 (Category: aws-billing-pricing-support)
A CTO is building a business case to migrate from on-premises to AWS and needs to compare the total cost of running infrastructure on-premises versus in the cloud. Which concept does this represent?

- [ ] {'label': 'A', 'text': 'Return on Investment (ROI)', 'is_correct': False}
- [ ] {'label': 'B', 'text': 'Total Cost of Ownership (TCO)', 'is_correct': True}
- [ ] {'label': 'C', 'text': 'Capital Expenditure (CapEx)', 'is_correct': False}
- [ ] {'label': 'D', 'text': 'Operational Expenditure (OpEx)', 'is_correct': False}

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B**  

- **Detailed Explanation:** Total Cost of Ownership (TCO) is a financial estimate that compares the full cost of owning and operating on-premises infrastructure (servers, power, cooling, staff, facility) against the cost of cloud services. ROI measures return on an investment. CapEx is upfront spending on physical assets. OpEx is ongoing operational spending. While cloud migration often shifts CapEx to OpEx, TCO is the concept that captures the full comparison.
</details>

---

## 🔑 Quick Answer Key Summary

- 1. **C**
- 2. **C**
- 3. **B**
- 4. **C**
- 5. **B**
- 6. **C**
- 7. **A**
- 8. **C**
- 9. **C**
- 10. **B**
- 11. **B**
- 12. **B**
- 13. **C**
- 14. **B**
- 15. **B**
- 16. **B**
- 17. **B**
- 18. **B**
- 19. **B**
- 20. **B**
