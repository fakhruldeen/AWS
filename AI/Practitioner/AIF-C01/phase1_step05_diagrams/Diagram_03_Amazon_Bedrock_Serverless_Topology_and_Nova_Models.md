# Diagram 03: Amazon Bedrock Serverless Topology and Nova Models

> **Architecture Blueprint:** `Diagram_03_Amazon_Bedrock_Serverless_Topology_and_Nova_Models.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 2 & Domain 3

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart TD
    subgraph ClientLayer["Enterprise Clients & Frontends"]
        App["Web / Mobile Applications"]
        CLI["AWS CLI / SDK (boto3)"]
        Agents["Autonomous Agents / MCP Clients"]
    end

    subgraph SecurityPerimeter["AWS Security & Network Boundary"]
        VPCE["VPC Interface Endpoint\n(AWS PrivateLink)"]
        IAMAuth["AWS IAM SigV4 Authentication\n(Least-Privilege Roles)"]
    end

    subgraph BedrockPlatform["Amazon Bedrock Fully Managed Platform"]
        API["Bedrock Runtime API\n(InvokeModel / ConverseStream)"]
        Guard["Amazon Bedrock Guardrails\n(PII Masking, Content & Word Filters)"]
        PromptCache["Prompt Caching Layer\n(Sub-second response for cached context)"]
        
        API --> Guard
        Guard --> PromptCache
    end

    subgraph FoundationModels["Unified Foundation Model Catalog"]
        subgraph NovaFamily["Amazon Nova Family"]
            NMicro["Nova Micro\n(Text-to-text, ultra-low latency)"]
            NLite["Nova Lite\n(Multimodal, cost-optimized)"]
            NPro["Nova Pro\n(Multimodal, frontier reasoning)"]
            NPremier["Nova Premier\n(Frontier intelligence scale)"]
        end
        
        subgraph PartnerModels["Partner & Open Models"]
            Claude["Anthropic Claude 3.5 Sonnet"]
            Llama["Meta Llama 3"]
            Mistral["Mistral Large"]
            TitanImg["Titan Image Generator G1/v2"]
        end
    end

    ClientLayer --> VPCE
    VPCE --> IAMAuth
    IAMAuth --> API
    PromptCache --> NovaFamily
    PromptCache --> PartnerModels
```

---

## 🔍 Core Architectural Highlights

1. **Serverless Abstraction:** No EC2 instances, cluster auto-scaling, or GPU drivers to manage; developers call uniform REST APIs.
2. **PrivateLink Integration:** Client requests never traverse the public internet when routed through private VPC endpoints.
3. **Nova Family Tiers:** Spans from lightweight sub-second processing (Nova Micro) to multimodal frontier intelligence (Nova Pro/Premier).
