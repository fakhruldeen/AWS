# AWS Certified AI Practitioner (`AIF-C01`) Hands-On Lab Safety & Verification Guide

> **Target Repository:** `AI/Practitioner/AIF-C01/07_Hands_On_Labs/`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Student Hands-On Curriculum  
> **Primary Assigned Region:** `eu-north-1` (Stockholm) / `us-east-1` (for select Bedrock preview models)  
> **Cost Guarantee:** **100% Free-Tier & Low-Cost Guardrails** when observing the teardown protocols herein.

---

## 🧭 Executive Overview

This master guide establishes the operational and cost-safety standards for all 12 hands-on labs in the `AIF-C01` curriculum. It equips students and instructors with:
1. **The Master AI Lab Catalog:** Detailed matrix of all 12 labs, estimated time, services used, and Free-Tier classification.
2. **The AI Cost Trap Radar:** Critical warnings on billable services (e.g., SageMaker Endpoints, OpenSearch Serverless OCUs, Canvas sessions) that could generate unexpected charges if left unmanaged.
3. **Universal Pre-Flight Environment Checks:** CLI diagnostic scripts to verify AI service access, credentials, and quotas.
4. **Universal Emergency Teardown Runbook:** Automated bash scripts to instantly delete active endpoints, vector collections, and agent resources.

---

## 📊 Master AI Lab Catalog & Cost Safety Matrix

| Lab # | Lab Title | Domain | Est. Time | AWS Services Covered | Free-Tier Status | Cost Risk Level & Action |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **01** | [Bedrock Model Access & Playgrounds](./Lab_01_Amazon_Bedrock_Model_Access_Playgrounds_and_Prompt_Engineering.md) | Domain 2 | 20 min | Amazon Bedrock, Titan, Claude, Temperature, Top-P | Pay-per-token | **Zero/Negligible Risk:** Testing prompts in playground costs pennies ($0.01–$0.05). |
| **02** | [Multimodal Generation with Nova & Titan Image](./Lab_02_Multi_Modal_Generation_with_Amazon_Nova_and_Titan_Image.md) | Domain 2 | 20 min | Amazon Nova (Lite/Pro), Amazon Titan Image Generator | Pay-per-token/image | **Low Risk:** Generating 5–10 sample images costs < $0.08 total. |
| **03** | [Enterprise RAG with Bedrock Knowledge Bases](./Lab_03_Enterprise_RAG_with_Bedrock_Knowledge_Bases_and_OpenSearch_Serverless.md) | Domain 3 | 30 min | Bedrock Knowledge Bases, OpenSearch Serverless, S3 | ⚠️ Conditional | **HIGH RISK TRAP:** OpenSearch Serverless has a 2 OCU minimum (~$0.48/hr = ~$350/mo). **Delete vector collection immediately after testing!** |
| **04** | [Autonomous AI Agents & Action Groups](./Lab_04_Autonomous_AI_Agents_with_Bedrock_AgentCore_Action_Groups_and_MCP.md) | Domain 3 | 30 min | Bedrock Agents, Action Groups, Lambda, OpenAPI, MCP | 100% Free Tier | **Zero Risk:** Lambda is free; Bedrock token usage is fractions of a cent. |
| **05** | [Responsible AI & Guardrails](./Lab_05_Responsible_AI_and_PII_Masking_with_Amazon_Bedrock_Guardrails.md) | Domain 4 | 25 min | Amazon Bedrock Guardrails, PII Masking, Denied Topics | Pay-per-call | **Zero Risk:** Guardrail text policy evaluation costs ~$0.00075 per call. |
| **06** | [No-Code Predictive ML with SageMaker Canvas](./Lab_06_No_Code_Predictive_ML_with_Amazon_SageMaker_Canvas.md) | Domain 1 | 25 min | SageMaker Canvas (AutoML, 2-month Free Tier) | Free Tier (2 mos) | **Medium Risk:** Canvas charges for active workspace instance hours. **Always log out of Canvas and terminate workspace session!** |
| **07** | [Data Prep with SageMaker Data Wrangler](./Lab_07_Data_Preparation_and_Feature_Engineering_with_SageMaker_Data_Wrangler.md) | Domain 1 | 20 min | SageMaker Data Wrangler, S3, Data Ingestion | Free Tier (25 hrs) | **Low Risk:** Included in SageMaker Studio Free Tier. Stop processing job when done. |
| **08** | [Model Deployment with SageMaker JumpStart](./Lab_08_Pre_Trained_Foundation_Model_Deployment_with_SageMaker_JumpStart.md) | Domain 3 | 30 min | SageMaker JumpStart, Real-Time Endpoints | ⚠️ Conditional | **CRITICAL RISK TRAP:** Real-time endpoints incur hourly GPU/CPU fees ($1.50–$5.00/hr). **Delete the endpoint immediately after invoking test!** |
| **09** | [Model Fairness & SHAP with Clarify](./Lab_09_Model_Fairness_Bias_Detection_and_SHAP_Explainability_with_SageMaker_Clarify.md) | Domain 4 | 25 min | SageMaker Clarify, SHAP Values, Bias Detection | Free Tier (Studio) | **Low Risk:** Short processing job takes 3–5 minutes. Clean up output S3 prefix. |
| **10** | [Governance Lineage with Model Cards](./Lab_10_Model_Governance_Lineage_Tracking_and_Auditing_with_SageMaker_Model_Cards.md) | Domain 4 | 20 min | SageMaker Model Cards, Model Dashboard | 100% Free Always | **Zero Risk:** Model Cards are metadata documents stored at zero compute fee. |
| **11** | [Document Intelligence with Textract & Bedrock](./Lab_11_Applied_Document_Intelligence_with_Amazon_Textract_Comprehend_and_Bedrock.md) | Domain 3 | 25 min | Amazon Textract, Comprehend, Bedrock RAG | Free Tier (1,000 pgs) | **Zero Risk:** Textract 1,000 pages free/month for first 3 months. |
| **12** | [Generative AI FinOps & Token Pricing](./Lab_12_Generative_AI_FinOps_Token_Pricing_Quotas_and_Provisioned_Throughput.md) | Domain 5 | 20 min | AWS Budgets, CloudWatch Alarms, Service Quotas | 100% Free Always | **Zero Risk:** Configures alerts and spend limits. Keep active indefinitely! |

---

## 🚨 The AI Cost Trap Radar: Top 4 Critical Pitfalls

Students working in AI and Generative AI must pay special attention to these 4 services:

1. **The SageMaker Real-Time Endpoint Trap (Lab 08):**
   * *Problem:* Deploying a foundation model from SageMaker JumpStart provisions an active real-time EC2 instance (e.g. `ml.g5.2xlarge` or `ml.m5.2xlarge`). Even when idle and processing zero inference queries, AWS bills by the second (~$1.50 to $5.00/hour = ~$1,100 to $3,600/month!).
   * *Remedy:* As soon as you test the sample prompt, run:  
     `aws sagemaker delete-endpoint --endpoint-name <endpoint-name>`
2. **The OpenSearch Serverless OCU Minimum Trap (Lab 03):**
   * *Problem:* When creating a Bedrock Knowledge Base with an automated OpenSearch Serverless vector store, AWS allocates a minimum of 2 OpenSearch Compute Units (OCUs) for search and ingestion. At ~$0.24/OCU/hour, this costs ~$0.48/hour (~$350/month) even with zero documents stored!
   * *Remedy:* Always delete the OpenSearch Serverless collection immediately after finishing the RAG demonstration.
3. **The SageMaker Canvas Idle Workspace Trap (Lab 06):**
   * *Problem:* Closing your browser tab does NOT terminate a SageMaker Canvas workspace session. The background instance stays running and consumes monthly quota hours.
   * *Remedy:* Always click the **Log Out** button inside the Canvas UI and confirm workspace termination.
4. **Bedrock Provisioned Throughput:**
   * *Problem:* Provisioned Throughput allows dedicated capacity for foundation models on a 1-month or 6-month commitment, costing thousands of dollars per model unit.
   * *Remedy:* **NEVER** purchase Provisioned Throughput for exam studies. Always select **On-Demand Pay-As-You-Go** token pricing!

---

## 🛠️ Universal Pre-Flight AI Environment Check

Run this diagnostic script in **AWS CloudShell** before starting any AI lab:

```bash
#!/usr/bin/env bash
# Pre-Flight Diagnostic Check for AIF-C01 Student Labs
set -euo pipefail

echo "=== AWS AIF-C01 Pre-Flight AI Environment Check ==="

# 1. Verify Caller Identity
CALLER_JSON=$(aws sts get-caller-identity --output json)
echo "Identity OK: $(echo "$CALLER_JSON" | grep -o '"Arn": "[^"]*' | cut -d'"' -f4)"

# 2. Check for Active Billable SageMaker Endpoints
echo -n "2. Scanning for Active SageMaker Endpoints... "
SM_ENDPOINTS=$(aws sagemaker list-endpoints --status-equals InService --query "Endpoints[*].EndpointName" --output text 2>/dev/null || echo "")
if [ -n "$SM_ENDPOINTS" ]; then
  echo "⚠️ WARNING: Active SageMaker endpoint(s) detected: $SM_ENDPOINTS (High hourly charge!)"
else
  echo "OK (0 active SageMaker endpoints)"
fi

# 3. Check for Active OpenSearch Serverless Collections
echo -n "3. Scanning for Active OpenSearch Serverless Collections... "
AOSS_COLLECTIONS=$(aws opensearchserverless list-collections --query "collectionSummaries[*].name" --output text 2>/dev/null || echo "")
if [ -n "$AOSS_COLLECTIONS" ]; then
  echo "⚠️ WARNING: Active OpenSearch Serverless collection(s) detected: $AOSS_COLLECTIONS (~$0.48/hr!)"
else
  echo "OK (0 OpenSearch Serverless collections)"
fi

# 4. Check Bedrock Foundation Model Access
echo -n "4. Testing Amazon Bedrock Model Access... "
TITAN_CHECK=$(aws bedrock list-foundation-models --by-provider "Amazon" --query "length(modelSummaries)" --output text 2>/dev/null || echo "0")
if [ "$TITAN_CHECK" -gt 0 ]; then
  echo "OK ($TITAN_CHECK Amazon foundation models available)"
else
  echo "⚠️ Check Bedrock Model Access in AWS Console -> Model Access tab."
fi

echo "=== AI Pre-Flight Check Complete. You are ready to start! ==="
```

---

## 🧹 Universal Emergency AI Teardown Runbook

Run this script in **AWS CloudShell** to instantly delete any running SageMaker endpoints or OpenSearch Serverless collections:

```bash
#!/usr/bin/env bash
# Universal Emergency Teardown Runbook for AIF-C01 Labs
set -eo pipefail

echo "🚨 STARTING UNIVERSAL AI RESOURCE TEARDOWN..."

# 1. Delete all Active SageMaker Endpoints
echo "1. Scanning and deleting SageMaker Endpoints..."
ENDPOINTS=$(aws sagemaker list-endpoints --query "Endpoints[*].EndpointName" --output text 2>/dev/null || echo "")
for ep in $ENDPOINTS; do
  echo "   Deleting SageMaker Endpoint: $ep"
  aws sagemaker delete-endpoint --endpoint-name "$ep"
done

# 2. Delete Endpoint Configurations & Models
echo "2. Deleting SageMaker Endpoint Configurations..."
CONFIGS=$(aws sagemaker list-endpoint-configs --query "EndpointConfigs[*].EndpointConfigName" --output text 2>/dev/null || echo "")
for cfg in $CONFIGS; do
  echo "   Deleting Endpoint Config: $cfg"
  aws sagemaker delete-endpoint-config --endpoint-config-name "$cfg"
done

# 3. Delete OpenSearch Serverless Collections
echo "3. Scanning and deleting OpenSearch Serverless Collections..."
AOSS_IDS=$(aws opensearchserverless list-collections --query "collectionSummaries[*].id" --output text 2>/dev/null || echo "")
for cid in $AOSS_IDS; do
  echo "   Deleting OpenSearch Serverless Collection: $cid"
  aws opensearchserverless delete-collection --id "$cid"
done

# 4. Delete Bedrock Agents & Knowledge Bases
echo "4. Scanning for test Bedrock Agents..."
AGENT_IDS=$(aws bedrock-agent list-agents --query "agentSummaries[?contains(agentName, 'student') || contains(agentName, 'test')].agentId" --output text 2>/dev/null || echo "")
for ag in $AGENT_IDS; do
  echo "   Deleting Bedrock Agent: $ag"
  aws bedrock-agent delete-agent --agent-id "$ag" --skip-resource-in-use-check || true
done

echo "✅ UNIVERSAL AI TEARDOWN COMPLETE! All billable AI endpoints removed."
```
