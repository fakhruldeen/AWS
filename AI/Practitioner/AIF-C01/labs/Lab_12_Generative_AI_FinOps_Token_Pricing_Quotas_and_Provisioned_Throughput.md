# Lab 12: Generative AI FinOps: Token Pricing, Quotas & Throughput

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 3 & Domain 5: AI Cost Management & Operational Governance  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** AWS Cost Explorer is free for standard usage ($0.00)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Inspect Amazon Bedrock token pricing and calculate On-Demand vs. Provisioned Throughput costs.
2. Filter and analyze Generative AI expenditures using **AWS Cost Explorer**.
3. Inspect and monitor **Service Quotas** for Tokens Per Minute (TPM) and Requests Per Minute (RPM).
4. Model commitment tradeoffs for **Provisioned Throughput** (Model Units - MU).

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Analyze Bedrock Expenditures in AWS Cost Explorer
1. In the **AWS Management Console**, navigate to **AWS Billing and Cost Management** > **Cost Explorer**.
2. Set the date range to **Last 30 days** and granularity to **Daily**.
3. In the right-hand filter bar:
   * Filter by **Service** > Select **Amazon Bedrock**.
   * Group by **Usage type**.
4. Observe the breakdown between:
   * Input token charges (e.g., `EU-Bedrock-Nova-Pro-Input-Tokens`).
   * Output token charges (e.g., `EU-Bedrock-Nova-Pro-Output-Tokens`).
   * Knowledge Base vector search and storage costs.

![Cost Explorer Bedrock Filter](images/lab12_step01_cost_explorer_bedrock_filter.png)

### Step 2: Inspect Service Quotas and Rate Limits
1. Navigate to **Service Quotas** in the console.
2. In the AWS Services list, search for **Amazon Bedrock**.
3. Review key operational limits:
   * **Invocations per minute:** Default RPM limits per model.
   * **Tokens per minute (TPM):** Maximum combined input/output tokens processed per minute.
4. Understand how throttling occurs when TPM/RPM limits are breached (HTTP 429 Too Many Requests), and how to request quota increases for production scaling.

![Service Quotas Bedrock](images/lab12_step02_service_quotas_bedrock.png)

### Step 3: Model Provisioned Throughput for Consistent Latency
1. Navigate to **Amazon Bedrock** > **Assessment & deployment** > **Provisioned throughput**.
2. Click **Purchase Provisioned Throughput**:
   * Select Model: **Amazon Nova Pro** (or **Anthropic Claude 3.5 Sonnet**).
   * Specify **Model Units (MU)**: 1 MU guarantees dedicated capacity and zero throttling during peak hours.
   * Review commitment duration: **No commitment (Hourly)** vs. **1-Month Commitment** vs. **6-Month Commitment** (up to 33% discount).
3. Evaluate when an enterprise should transition from On-Demand (pay-per-token) to Provisioned Throughput:
   * When steady-state token volume exceeds the break-even threshold.
   * When strict SLA guarantees and sub-second deterministic response latencies are mandatory.

![Provisioned Throughput Modal](images/lab12_step03_provisioned_throughput_modal.png)

---

## 🧹 Teardown & Clean-up
* Cost Explorer and Service Quotas are informational services that incur zero infrastructure costs.
* **Important:** Do NOT click purchase on Provisioned Throughput unless required for production, as commitments incur fixed hourly charges.
