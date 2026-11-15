# AWS Billing & Cost Management — Map of Content (MOC)

> **Domain:** 03_Services / Billing & Cost Management  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], Cloud Operations, Solutions Architect

---

## 1. Architectural Taxonomy of AWS Billing & FinOps

AWS billing and cost management tools guide organizations through the full lifecycle of cloud financial governance—from initial architectural estimation through proactive alerting, visual analysis, machine learning optimization, and executive reporting:

```mermaid
flowchart TD
    FinOps["AWS Billing & Cost Management"]
    
    subgraph PreDeploy["1. Pre-Deployment Planning"]
        Calc["AWS Pricing Calculator (calculator.aws: Estimate before launching)"]
    end
    
    subgraph Proactive["2. Proactive Alerting & Governance"]
        Budgets["AWS Budgets (Alert on actual/forecasted spend + auto actions)"]
        Anom["AWS Cost Anomaly Detection (ML-powered spend spikes)"]
    end
    
    subgraph Analytics["3. Analytics & Reporting"]
        CE["AWS Cost Explorer (12-mo historical visual trends + 12-mo forecast)"]
        CUR["AWS CUR (Raw line-item CSV/Parquet in S3 queried via Athena)"]
    end
    
    subgraph Optimization["4. Resource Optimization"]
        Optimizer["AWS Compute Optimizer (ML rightsizing: EC2, EBS, Lambda)"]
    end
    
    subgraph Commercial["5. Support & Procurement"]
        Support["AWS Support Plans (Basic, Developer, Business, Enterprise)"]
        Marketplace["AWS Marketplace (Curated catalog for 3rd-party software/AMIs)"]
    end
    
    FinOps --> PreDeploy
    FinOps --> Proactive
    FinOps --> Analytics
    FinOps --> Optimization
    FinOps --> Commercial
```

---

## 2. High-Yield Tool Comparison (CLF-C02 Cheat Sheet)

```mermaid
flowchart LR
    Plan["Planning: AWS_Pricing_Calculator"] --> Launch["Resources Provisioned"]
    Launch --> Alert["Alerting: AWS_Budgets"]
    Launch --> Analyze["Visual Trends: AWS_Cost_Explorer"]
    Launch --> DeepDive["Raw Line-Items: AWS_Cost_and_Usage_Report_CUR"]
    Launch --> Rightsize["ML Rightsizing: AWS_Compute_Optimizer"]
```

| Tool | When to Use | Key Differentiator |
| :--- | :--- | :--- |
| **[[AWS_Pricing_Calculator]]** | **Before** launching resources. | Estimate expected monthly bill; no AWS account required (`calculator.aws`). |
| **[[AWS_Budgets]]** | **During** the billing cycle. | Set hard thresholds; alert via email/SNS; execute automated shutdown actions. |
| **[[AWS_Cost_Explorer]]** | **Monthly/Weekly** reviews. | Interactive visual charts; group by tag/service; 12-month historical + 12-month forecast. |
| **[[AWS_Cost_and_Usage_Report_CUR]]** | **Enterprise FinOps**. | Most granular raw line-item dataset; delivered to S3; queried using SQL via Athena. |
| **[[AWS_Compute_Optimizer]]** | **Optimization** sprints. | ML analysis of CloudWatch metrics to recommend downsizing or upsizing instances. |
| **[[AWS_Support_Plans]]** | **Operational planning**. | SLA response times (< 15 min for Enterprise); TAM assignment; 24/7 phone access. |
| **[[AWS_Marketplace]]** | **Software procurement**. | Buy 3rd-party software and AMIs; consolidated billing onto regular AWS invoice. |

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[AWS_Budgets]]** | Cost & Usage Budgets | Actual vs. Forecasted thresholds, auto-stop EC2 actions, SNS alerts. |
| **[[AWS_Cost_Explorer]]** | Historical Analytics & Forecasting | Visual graphs, breakdown by tag/service, Savings Plans recommendations. |
| **[[AWS_Cost_and_Usage_Report_CUR]]** | Raw Line-Item Data | Ultimate billing granularity, S3 delivery, Amazon Athena SQL integration. |
| **[[AWS_Pricing_Calculator]]** | Pre-Deployment Estimator | Estimate architectures before building, shareable links, CSV export. |
| **[[AWS_Compute_Optimizer]]** | ML Resource Rightsizing | Identify over-provisioned and under-provisioned EC2, EBS, Lambda, Fargate. |
| **[[AWS_Support_Plans]]** | Support Tier Comparison | Basic, Developer, Business, Enterprise; TAM, Concierge, response SLAs. |
| **[[AWS_Marketplace]]** | Digital Software Catalog | 3rd-party AMIs and SaaS, consolidated monthly billing, Private Marketplace. |
