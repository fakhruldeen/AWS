# Lab 14: Financial Governance (AWS Budgets, Cost Explorer & Rightsizing)

> **Focus:** Cloud Financial Management (FinOps), Cost Allocation Tags, AWS Cost Explorer, AWS Budgets, AWS Pricing Calculator, and AWS Compute Optimizer  
> **Region:** Global (Billing & Cost Management)  
> **Course Domain:** Domain 4: Billing, Pricing & Support  
> **Associated Vault Notes:** [[AWS_Budgets]], [[AWS_Cost_Explorer]], [[AWS_Pricing_Calculator]], [[AWS_Compute_Optimizer]]  

---

## 🧭 Prerequisite Concept Refresher: Cloud Financial Management (FinOps)

### 1. CapEx (Capital Expenditure) vs. OpEx (Operational Expenditure)
- **Traditional On-Premises (CapEx):** Requires heavy upfront financial investments in physical servers, data center cooling, real estate, and networking gear before writing a single line of application code. You are locked into fixed capacity for 3–5 years regardless of business performance.
- **AWS Cloud (OpEx):** Replaces fixed upfront capital expense with variable, pay-as-you-go operational expenses. You pay only for the compute cycles and storage gigabytes actually consumed, adapting dynamically to business demand with zero depreciation risks.

### 2. The 3 Primary Drivers of AWS Cost
Every AWS invoice is primarily derived from three resource dimensions:
1. **Compute:** Billed by time (seconds or hours) and instance size/family.
2. **Storage:** Billed by gigabytes (GB/month) and storage class tier.
3. **Data Transfer:** **Inbound data transfer is 100% FREE** across all services. Outbound data transfer to the public internet (egress) is billed per gigabyte beyond the first 100 GB/month.

### 3. Cost Allocation Tags (The Activation Rule)
Applying tags (e.g., `Environment=Production`, `CostCenter=1042`) to EC2 instances or S3 buckets does **NOT** automatically make them appear in billing reports! An administrator must **explicitly activate user-defined tags in the Billing and Cost Management console**. Once activated, AWS tracks and organizes costs against those tags going forward.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Activate Cost Allocation Tags
1. In the AWS Management Console, open the account dropdown in the top right and select **Billing and Cost Management** (or navigate to `https://console.aws.amazon.com/costmanagement/`).
2. In the left navigation pane under **Cost organization**, click **Cost allocation tags**.
3. Select the **User-defined cost allocation tags** tab:
   - Search for tags you created (e.g., `Environment`, `Project`, `Department`).
   - Select the checkbox next to each tag.
   - Click **Activate**. (Tags take up to 24 hours to appear in Cost Explorer).

> [!NOTE]
> *Billing Console Permissions:* Accessing Cost Allocation Tags and billing dashboards requires Root credentials or an IAM role explicitly granted Billing and Cost Management permissions (`aws-portal:*` or fine-grained `ce:*` / `budgets:*`).

---

### Step 2: Analyze Historical Spend in AWS Cost Explorer
1. In the Billing Console left navigation pane, click **Cost Explorer**.
2. Click **Cost and usage** (or **Launch Cost Explorer**).
3. In the graphical chart view:
   - Set **Date range:** `Last 6 months`.
   - Set **Granularity:** `Monthly`.
   - Set **Group by:** `Service` (or `Linked account`, `Region`, `Tag`).
4. Hover over the bar segments to inspect the exact dollar amounts incurred by individual services (e.g., EC2-Instances, S3, RDS).

---

### Step 3: Generate a Predictive Cost Forecast
1. In AWS Cost Explorer, click the **Forecast** toggle above the chart.
2. Set the forecasting horizon: `Next 3 months`.
3. Cost Explorer applies machine learning time-series regression against your past spending run-rate, producing an estimated spending trajectory with 80% confidence prediction intervals.

---

### Step 4: Configure an AWS Budget with Threshold Alerts
1. In the left navigation pane under **Cost management**, click **Budgets**.
2. Click the orange **Create budget** button.
3. Select **Cost budget (recommended)** -> Click **Next**:
   - **Budget name:** `Monthly-Cloud-Practitioner-Budget`.
   - **Period:** `Monthly`.
   - **Budget effective date:** `Recurring budget`.
   - **Budgeting method:** `Fixed`.
   - **Enter budgeted amount ($):** `20.00`.
4. Under **Configure alerts**:
   - **Alert 1 (Actual Spend):** Trigger when actual spend is **Greater than 80%** ($16.00). Enter notification email: `aws@fakhr.me`.
   - **Alert 2 (Forecasted Spend):** Trigger when forecasted spend is **Greater than 100%** ($20.00). This provides early warning on Day 5 if your end-of-month run rate will exceed budget!
5. Click through to **Create budget**.

---

### Step 5: Model Solutions with the AWS Pricing Calculator
The AWS Pricing Calculator (`https://calculator.aws`) lets you estimate architecture costs **before launching resources**:
1. Open a browser tab and navigate to [https://calculator.aws](https://calculator.aws).
2. Click **Create estimate**.
3. Add services to model a standard 3-tier web architecture:
   - **Amazon EC2:** 2 x `t3.micro` instances in `eu-north-1`.
   - **Application Load Balancer:** 1 ALB processing 50 GB/month.
   - **Amazon RDS:** PostgreSQL `db.t3.micro` Single-AZ with 20 GB GP3 storage.
   - **Amazon S3:** 50 GB Standard storage with 1,000 PUT and 10,000 GET requests.
4. Review the generated **Estimate Summary Card**: inspect the total upfront cost ($0) and estimated monthly total (typically ~$30–$40/month).
5. Click **Share** to generate a permanent shareable URL or export the estimate as a CSV/PDF report.

---

### Step 6: Review Machine Learning Rightsizing in Compute Optimizer
1. Navigate to the **AWS Compute Optimizer Console**.
2. If opening for the first time, click **Opt in** (it takes up to 24–48 hours to analyze historical metrics).
3. In the dashboard, inspect the findings:
   - **Under-provisioned:** Identifies instances experiencing CPU/RAM bottlenecks.
   - **Over-provisioned:** Identifies oversized instances wasting budget.
   - **Optimized:** Instances perfectly sized for their workload.
4. Click on an overprovisioned EC2 instance to view Compute Optimizer's exact target recommendation (e.g., recommending a migration from `m5.large` down to `t4g.medium` for a 45% monthly cost reduction).

---

## 💻 AWS CLI Verification Commands

```bash
# 1. Query current month-to-date unblended costs grouped by service
aws ce get-cost-and-usage \
  --time-period Start=$(date +%Y-%m-01),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE \
  --region us-east-1 \
  --profile aws-notes

# 2. Inspect active budgets
aws budgets describe-budgets \
  --account-id $(aws sts get-caller-identity --query "Account" --output text --profile aws-notes) \
  --region us-east-1 \
  --profile aws-notes
```

---

## 🧹 Free Tier Cleanup & Cost Safeguard
1. In the **AWS Budgets Console**, select `Monthly-Cloud-Practitioner-Budget` -> Click **Actions** -> **Delete**.
2. If any stray resources from previous labs remain active, use the AWS Console Resource Groups or Billing Cost by Service view to locate and terminate them immediately.
