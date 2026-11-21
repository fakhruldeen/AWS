# 🔬 AWS Certified AI Practitioner (AIF-C01) Guided Student Labs

> **Module:** Self-Contained Guided Hands-On Student Labs  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Exam Version Alignment:** Official v1.2 (October 2026)  
> **Master Safety Guide & Emergency Teardown Runbook:** [LAB_SAFETY_AND_VERIFICATION_GUIDE.md](./LAB_SAFETY_AND_VERIFICATION_GUIDE.md)  
> **Format:** 100% Written Guided Walkthroughs with Mermaid Architectures, Step-by-Step Console Options, AWS CLI v2 Runbooks, and Exam Scenario Matrices (No reliance on screenshots).

---

## 🎯 Hands-On Philosophy & Exam Alignment Standards

Every lab in this curriculum is engineered to directly prepare students for official exam scenarios:
1. **100% Text-Guided Self-Sufficiency:** Every UI button, dropdown value, configuration parameter, and input prompt is detailed explicitly in text—allowing students to complete labs smoothly without external media dependencies.
2. **Dedicated Exam Scenario Matrices:** Every lab features an **Exam Practice: Scenarios & Traps** section directly connecting configuration options to real exam distractor choices.
3. **AWS CLI v2 Equivalents:** Production commands provided with expected JSON responses for programmatic terminal mastery.
4. **Mandatory Cost Safeguards & Teardowns:** Clear, step-by-step deletion runbooks to prevent unexpected cloud charges.


---

## 🗺️ Master Labs Index

| Lab | Title & Focus | Key AWS Services & Technologies | Estimated Time | Cost Profile |
|:---:|---|---|:---:|:---:|
| **[01](./Lab_01_Amazon_Bedrock_Model_Access_Playgrounds_and_Prompt_Engineering.md)** | **Bedrock Model Access, Playgrounds & Prompting**<br>Request model access, configure temperature/top-p, test CoT & few-shot prompts, configure prompt caching. | Bedrock, Amazon Nova, Claude, Titan | 45 min | $<\$0.10$ |
| **[02](./Lab_02_Multi_Modal_Generation_with_Amazon_Nova_and_Titan_Image.md)** | **Multimodal Generation with Nova & Titan Image**<br>Synthesize 8k imagery, perform inpainting/outpainting with masks, and analyze charts with multimodal Nova. | Titan Image Generator, Amazon Nova Lite/Pro | 45 min | $<\$0.15$ |
| **[03](./Lab_03_Enterprise_RAG_with_Bedrock_Knowledge_Bases_and_OpenSearch_Serverless.md)** | **Enterprise RAG with Bedrock Knowledge Bases**<br>Upload policy docs to S3, provision OpenSearch Serverless vector index, sync Titan Embeddings v2, test citations. | Bedrock Knowledge Bases, S3, OpenSearch Serverless | 60 min | $<\$0.25$ |
| **[04](./Lab_04_Autonomous_AI_Agents_with_Bedrock_AgentCore_Action_Groups_and_MCP.md)** | **Autonomous AI Agents with AgentCore & MCP**<br>Build an IT ops agent with ReAct reasoning, attach Lambda action groups with OpenAPI schemas, and connect MCP tools. | Bedrock Agents, AgentCore, Lambda, DynamoDB, MCP | 60 min | Free Tier |
| **[05](./Lab_05_Responsible_AI_and_PII_Masking_with_Amazon_Bedrock_Guardrails.md)** | **Responsible AI & PII Masking with Guardrails**<br>Configure denied topics, toxicity filters, PII regex masking, and contextual grounding hallucination checks. | Amazon Bedrock Guardrails, Nova Pro | 45 min | $<\$0.05$ |
| **[06](./Lab_06_No_Code_Predictive_ML_with_Amazon_SageMaker_Canvas.md)** | **No-Code Predictive ML with SageMaker Canvas**<br>Import tabular churn data, configure automated feature correlation, run Quick/Standard builds, and inspect confusion matrix. | SageMaker Canvas, S3 | 45 min | Free Tier |
| **[07](./Lab_07_Data_Preparation_and_Feature_Engineering_with_SageMaker_Data_Wrangler.md)** | **Data Prep & Feature Engineering with Data Wrangler**<br>Visual data flow, missing value median imputation, one-hot categorical encoding, and export to Feature Store/S3. | SageMaker Data Wrangler, Studio | 45 min | Free Tier |
| **[08](./Lab_08_Pre_Trained_Foundation_Model_Deployment_with_SageMaker_JumpStart.md)** | **Foundation Model Deployment with SageMaker JumpStart**<br>Deploy an open-weights foundation model to a dedicated GPU real-time endpoint, test inference, and tear down immediately. | SageMaker JumpStart, Real-Time Endpoints | 45 min | $\sim\$0.40$ |
| **[09](./Lab_09_Model_Fairness_Bias_Detection_and_SHAP_Explainability_with_SageMaker_Clarify.md)** | **Model Fairness, Bias Detection & SHAP with Clarify**<br>Audit pre-training Class Imbalance (CI), DPL, post-training Disparate Impact (DI), and compute local/global SHAP values. | SageMaker Clarify, Processing Jobs | 45 min | $<\$0.15$ |
| **[10](./Lab_10_Model_Governance_Lineage_Tracking_and_Auditing_with_SageMaker_Model_Cards.md)** | **Model Governance & Auditing with Model Cards**<br>Document intended use, risk ratings, Clarify metrics, and enforce approval transitions in Model Registry. | SageMaker Model Cards, Model Registry | 45 min | Free Tier |
| **[11](./Lab_11_Applied_Document_Intelligence_with_Amazon_Textract_Comprehend_and_Bedrock.md)** | **Document Intelligence with Textract, Comprehend & Bedrock**<br>Extract forms/tables from receipts with Textract, audit PII with Comprehend, and synthesize executive summaries with Bedrock. | Textract, Comprehend, Bedrock | 45 min | $<\$0.10$ |
| **[12](./Lab_12_Generative_AI_FinOps_Token_Pricing_Quotas_and_Provisioned_Throughput.md)** | **Generative AI FinOps: Pricing, Quotas & Throughput**<br>Analyze token spend in Cost Explorer, inspect TPM/RPM rate limits in Service Quotas, and model Provisioned Throughput commitments. | AWS Cost Explorer, Service Quotas, Bedrock | 45 min | Free Tier |
