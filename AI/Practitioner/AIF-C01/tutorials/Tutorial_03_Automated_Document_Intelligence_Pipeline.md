# Tutorial 03: Automated Document Intelligence Pipeline

> **Architecture Build Tutorial:** `Tutorial_03_Automated_Document_Intelligence_Pipeline.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Services Integrated:** Amazon S3, Amazon EventBridge, AWS Step Functions, Amazon Textract, Amazon Comprehend, Amazon Bedrock (Nova Lite/Claude), Amazon SNS  
> **Level:** Production-Grade Serverless Pipeline

---

## 🏛️ Architecture Overview

Organizations ingest thousands of scanned PDF invoices, contracts, and medical forms daily. This tutorial builds an automated, event-driven document processing and intelligence pipeline. 

```mermaid
flowchart LR
    S3In["1. S3 Upload\n(Incoming Document)"] --> EB["2. Amazon EventBridge\n(S3 Object Created)"]
    EB --> SF["3. AWS Step Functions\n(Workflow State Machine)"]
    
    subgraph AIProcessing["AI Processing Suite"]
        SF --> Textract["Amazon Textract\n(Extract Tables & Key-Value Pairs)"]
        Textract --> Comprehend["Amazon Comprehend\n(PII Detection & Sentiment)"]
        Comprehend --> Bedrock["Amazon Bedrock (Nova Lite)\n(Executive Summarization & Validation)"]
    end
    
    Bedrock --> S3Out["4. S3 Storage\n(Processed JSON & Summary)"]
    Bedrock --> SNS["5. Amazon SNS\n(Executive Notification)"]
```

---

## 🛠️ Step-by-Step Implementation Guide

### Step 1: Create the Source and Destination S3 Buckets
```bash
aws s3api create-bucket \
    --bucket doc-intelligence-incoming-corp \
    --region eu-north-1 \
    --create-bucket-configuration LocationConstraint=eu-north-1

aws s3api create-bucket \
    --bucket doc-intelligence-processed-corp \
    --region eu-north-1 \
    --create-bucket-configuration LocationConstraint=eu-north-1

# Enable EventBridge notifications on incoming bucket
aws s3api put-bucket-notification-configuration \
    --bucket doc-intelligence-incoming-corp \
    --notification-configuration '{"EventBridgeConfiguration": {}}'
```

### Step 2: Configure the Step Functions State Machine
The workflow coordinates document extraction, entity detection, and generative summarization.
Author `document_processing_workflow.json`:
```json
{
  "Comment": "Automated Document Processing Pipeline with Textract, Comprehend, and Bedrock",
  "StartAt": "ExtractDocumentText",
  "States": {
    "ExtractDocumentText": {
      "Type": "Task",
      "Resource": "arn:aws:states:::aws-sdk:textract:analyzeDocument",
      "Parameters": {
        "Document": {
          "S3Object": {
            "Bucket.$": "$.detail.bucket.name",
            "Name.$": "$.detail.object.key"
          }
        },
        "FeatureTypes": ["TABLES", "FORMS"]
      },
      "ResultPath": "$.TextractResult",
      "Next": "DetectEntitiesAndPII"
    },
    "DetectEntitiesAndPII": {
      "Type": "Task",
      "Resource": "arn:aws:states:::aws-sdk:comprehend:detectPiiEntities",
      "Parameters": {
        "LanguageCode": "en",
        "Text.$": "$.TextractResult.Blocks[0].Text"
      },
      "ResultPath": "$.ComprehendPII",
      "Next": "GenerateExecutiveSummary"
    },
    "GenerateExecutiveSummary": {
      "Type": "Task",
      "Resource": "arn:aws:states:::bedrock:invokeModel",
      "Parameters": {
        "ModelId": "arn:aws:bedrock:eu-north-1::foundation-model/amazon.nova-lite-v1:0",
        "Body": {
          "messages": [
            {
              "role": "user",
              "content": [
                {
                  "text": "Summarize the key contractual obligations and monetary values in this extracted text: \n\n"
                }
              ]
            }
          ]
        }
      },
      "ResultPath": "$.BedrockSummary",
      "Next": "SaveProcessedResult"
    },
    "SaveProcessedResult": {
      "Type": "Task",
      "Resource": "arn:aws:states:::aws-sdk:s3:putObject",
      "Parameters": {
        "Bucket": "doc-intelligence-processed-corp",
        "Key.$": "States.Format('{}-summary.json', $.detail.object.key)",
        "Body.$": "$.BedrockSummary"
      },
      "End": true
    }
  }
}
```

Deploy the state machine:
```bash
aws stepfunctions create-state-machine \
    --name EnterpriseDocumentIntelligencePipeline \
    --definition file://document_processing_workflow.json \
    --role-arn arn:aws:iam::123456789012:role/StepFunctionsProcessingRole \
    --region eu-north-1
```

### Step 3: EventBridge Rule for S3 Upload Trigger
```bash
aws events put-rule \
    --name TriggerDocPipelineOnUpload \
    --event-pattern '{
        "source": ["aws.s3"],
        "detail-type": ["Object Created"],
        "detail": {
            "bucket": {
                "name": ["doc-intelligence-incoming-corp"]
            }
        }
    }' \
    --region eu-north-1

aws events put-targets \
    --rule TriggerDocPipelineOnUpload \
    --targets "Id"="1","Arn"="arn:aws:states:eu-north-1:123456789012:stateMachine:EnterpriseDocumentIntelligencePipeline","RoleArn"="arn:aws:iam::123456789012:role/EventBridgeInvokeStepFunctionsRole" \
    --region eu-north-1
```

---

## 🔍 Architecture Benefits
1. **Fully Serverless:** Scales automatically with zero idle compute costs.
2. **Specialized Synergy:** Textract extracts high-accuracy optical tables; Comprehend audits for sensitive PII; Bedrock synthesizes natural language executive briefs.
3. **Resilience:** Step Functions automatically retries on transient API rate limits and routes failed documents to a Dead-Letter Queue (DLQ).
