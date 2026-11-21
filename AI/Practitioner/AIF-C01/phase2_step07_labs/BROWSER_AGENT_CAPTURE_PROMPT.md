# Browser-Based Agent Console Screenshot Capture Runbook & Prompt

> **Role:** Automated AWS Management Console Visual Documentation Agent  
> **Target:** AWS Certified AI Practitioner (`AIF-C01`) 12 Student Labs  
> **Output Destination:** `/home/mohamed/Desktop/Work/aws/AI/Practitioner/AIF-C01/phase2_step07_labs/images/`  
> **Image Naming Standard:** `lab{XX}_step{YY}_{action_description}.png`  

---

## 🎯 Master Prompt for the Browser Agent

```markdown
You are an expert technical screenshot capture agent operating an automated browser.
Your sole responsibility is to navigate the live AWS Management Console, execute visual setup steps for the 12 AWS Certified AI Practitioner (AIF-C01) labs, capture pristine, high-resolution screenshots, and save them with strict sequential numbering.

### Capture Rules & Standards:
1. Viewport Resolution: 1920x1080 (Full HD, 100% DPI zoom, clean UI layout).
2. Theme: AWS Light Mode (standard accessibility and publication contrast).
3. Focus & Highlighting: The active element, button, modal dialog, or configuration panel must be visible and centered.
4. Privacy & Masking: Automatically blur or omit Account IDs, IAM access keys, or personal email addresses.
5. Directory & File Naming:
   - Save all files directly to: `AI/Practitioner/AIF-C01/phase2_step07_labs/images/`
   - File format: PNG
   - Strict naming convention: `lab{XX}_step{YY}_{action_name}.png` (e.g., `lab01_step01_model_access.png`).
```

---

## 📋 Screenshot Capture Manifest for All 12 Labs

### Lab 01: Amazon Bedrock Model Access & Playgrounds
- `lab01_step01_model_access_catalog.png`: Bedrock Console > Model access overview showing "Access granted" statuses.
- `lab01_step02_chat_playground_setup.png`: Chat Playground with Amazon Nova / Claude selected and configuration panel visible.
- `lab01_step03_temperature_comparison.png`: Side-by-side prompt output comparing Temperature 0.0 vs 1.0.
- `lab01_step04_prompt_caching_panel.png`: Bedrock Prompt Management with caching indicator enabled.

### Lab 02: Multi-Modal Generation with Amazon Nova & Titan Image
- `lab02_step01_image_playground_canvas.png`: Amazon Titan Image Generator playground with aspect ratio and quality settings.
- `lab02_step02_inpainting_mask_selection.png`: Drawing an inpainting mask over an object in the playground canvas.
- `lab02_step03_multimodal_nova_analysis.png`: Nova Lite / Pro processing a combined input of an uploaded chart and natural language prompt.

### Lab 03: Enterprise RAG with Bedrock Knowledge Bases
- `lab03_step01_s3_document_bucket.png`: S3 bucket overview displaying uploaded corporate policy documents.
- `lab03_step02_aoss_vector_collection.png`: OpenSearch Serverless collection configuration showing vector search type.
- `lab03_step03_kb_data_source_sync.png`: Bedrock Knowledge Base console showing successful data sync status.
- `lab03_step04_retrieval_citation_test.png`: Knowledge Base testing panel showing retrieved response with inline S3 citations.

### Lab 04: Autonomous AI Agents with Bedrock AgentCore & MCP
- `lab04_step01_agent_configuration_screen.png`: Bedrock Agent builder with instructions and Nova Pro model selection.
- `lab04_step02_action_group_openapi_schema.png`: Action Group modal showing Lambda function attachment and OpenAPI JSON schema.
- `lab04_step03_mcp_tool_configuration.png`: External tool integration interface demonstrating Model Context Protocol server connection.
- `lab04_step04_agent_reasoning_trace.png`: Agent test chat window showing expanded "Show Trace" view with intermediate thoughts and tool inputs.

### Lab 05: Responsible AI with Amazon Bedrock Guardrails
- `lab05_step01_guardrail_builder_overview.png`: Guardrails console showing the 5 policy tabs.
- `lab05_step02_denied_topics_configuration.png`: Configuring the "Financial Advice" denied topic with sample phrases.
- `lab05_step03_pii_masking_policy.png`: Sensitive information filter showing SSN set to BLOCK and Email set to ANONYMIZE.
- `lab05_step04_guardrail_blocking_test.png`: Testing playground triggering the canned rejection response.

### Lab 06: No-Code Predictive ML with Amazon SageMaker Canvas
- `lab06_step01_canvas_import_dataset.png`: SageMaker Canvas dataset library with imported tabular CSV.
- `lab06_step02_canvas_target_selection.png`: Canvas model builder selecting target column and displaying automated feature correlations.
- `lab06_step03_canvas_model_metrics.png`: Model evaluation tab displaying Accuracy, F1-Score, and Confusion Matrix.
- `lab06_step04_canvas_single_prediction.png`: Single prediction tab modifying slider inputs to generate real-time prediction probabilities.

### Lab 07: Data Prep with SageMaker Data Wrangler
- `lab07_step01_data_flow_canvas.png`: Data Wrangler interactive data flow graph connecting S3 to transformation blocks.
- `lab07_step02_missing_value_imputation.png`: Configuring missing value imputation transform.
- `lab07_step03_one_hot_encoding_step.png`: Configuring categorical encoding for nominal variables.
- `lab07_step04_export_pipeline_destination.png`: Export screen targeting SageMaker Feature Store or S3.

### Lab 08: Foundation Model Deployment with SageMaker JumpStart
- `lab08_step01_jumpstart_model_hub.png`: Browsing the SageMaker JumpStart catalog (Llama, Mistral, Falcon).
- `lab08_step02_jumpstart_deploy_parameters.png`: Deployment configuration screen showing instance type and endpoint name.
- `lab08_step03_jumpstart_endpoint_in_service.png`: SageMaker Endpoints list showing status "InService".
- `lab08_step04_endpoint_teardown_dialog.png`: Confirmation modal deleting the JumpStart endpoint to avoid idle GPU charges.

### Lab 09: Bias Detection & Explainability with SageMaker Clarify
- `lab09_step01_clarify_analysis_config.png`: Clarify configuration selecting demographic facet (Gender/Age) and target label.
- `lab09_step02_pre_training_bias_metrics.png`: Clarify report visual displaying Class Imbalance (CI) and DPL values.
- `lab09_step03_post_training_disparate_impact.png`: Report section showing Disparate Impact (DI) chart.
- `lab09_step04_shap_feature_importance_plot.png`: Global SHAP feature attribution bar chart ranking top predictive features.

### Lab 10: Model Governance with SageMaker Model Cards
- `lab10_step01_model_card_creator.png`: Creating a new model card with business overview and intended use tabs.
- `lab10_step02_model_card_evaluation_metrics.png`: Embedding Clarify bias scores and test set accuracy into the card.
- `lab10_step03_model_card_risk_rating.png`: Setting risk rating and compliance sign-off ownership.
- `lab10_step04_model_registry_approval_gate.png`: SageMaker Model Registry showing transition from "PendingManualApproval" to "Approved".

### Lab 11: Document Intelligence with Textract, Comprehend & Bedrock
- `lab11_step01_textract_form_extraction.png`: Textract console showing extracted key-value pairs and structured tables from a PDF receipt.
- `lab11_step02_comprehend_pii_detection.png`: Comprehend console displaying detected PII entities with confidence scores.
- `lab11_step03_bedrock_summarization_output.png`: Bedrock playground showing executive summary of the extracted document text.

### Lab 12: Generative AI FinOps: Token Pricing & Throughput
- `lab12_step01_cost_explorer_bedrock_filter.png`: AWS Cost Explorer filtered by Service "Amazon Bedrock" and usage types.
- `lab12_step02_service_quotas_bedrock.png`: AWS Service Quotas console showing TPM (Tokens Per Minute) and RPM limits.
- `lab12_step03_provisioned_throughput_modal.png`: Bedrock console configuring Model Units (MU) and commitment terms (1-month vs 6-month).
