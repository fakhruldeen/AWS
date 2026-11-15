# Diagram 10: Enterprise AI Security, KMS, and Audit Loop

> **Architecture Blueprint:** `Diagram_10_Enterprise_AI_Security_KMS_and_Audit_Loop.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 5 (Security, Compliance, and Governance)

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart TD
    subgraph EnterprisePerimeter["Enterprise Private VPC"]
        ClientApp["Corporate Application"]
        VPCE["VPC Interface Endpoint\n(AWS PrivateLink)"]
        ClientApp --> VPCE
    end

    subgraph SecurityControls["Cryptographic & Access Controls"]
        IAMPolicy["AWS IAM Least Privilege\n(bedrock:InvokeModel with Resource Tagging)"]
        KMS["AWS KMS Customer-Managed Keys (CMK)\n(Enforces Envelope Encryption)"]
    end

    subgraph BedrockPlatform["Amazon Bedrock Secure Environment"]
        BedrockAPI["Amazon Bedrock Runtime"]
        CustomWeights["Encrypted Custom Model Weights"]
        RAGIndex["OpenSearch Serverless Vector Index"]
        
        BedrockAPI <--> CustomWeights
        BedrockAPI <--> RAGIndex
    end

    subgraph GovernanceLoop["Audit & Observability Loop"]
        CloudTrail["AWS CloudTrail\n(Logs Management & Data API Events)"]
        CloudWatch["Amazon CloudWatch\n(Model Latency, Token Usage, Invocation Errors)"]
        Macie["Amazon Macie\n(Scans S3 for Sensitive PII & Compliance Leaks)"]
        SIEM["Security Operations / SIEM\n(Audit Alarms & Compliance Reporting)"]
    end

    VPCE --> IAMPolicy
    IAMPolicy --> BedrockAPI
    KMS --> CustomWeights & RAGIndex
    BedrockAPI --> CloudTrail & CloudWatch
    Macie --> SIEM
    CloudTrail --> SIEM
    CloudWatch --> SIEM
```

---

## 🔍 Core Architectural Highlights

1. **Defense-in-Depth:** Combines network isolation (PrivateLink), access management (IAM SigV4), and cryptographic boundaries (KMS CMKs).
2. **Comprehensive Telemetry:** CloudTrail records every API call (who invoked what model at what timestamp), while CloudWatch tracks operational metrics (latency, token consumption, and errors).
3. **Proactive Sensitive Data Discovery:** Amazon Macie continuously monitors training and RAG data buckets in S3, alerting security operations before sensitive PII is exposed to generative pipelines.
