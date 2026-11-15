# Diagram 07: Amazon Bedrock Guardrails Multi-Layered Perimeter

> **Architecture Blueprint:** `Diagram_07_Bedrock_Guardrails_Multi_Layered_Perimeter.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 4 (Guidelines for Responsible AI)

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart TD
    UserPrompt["Incoming User Prompt"] --> GuardrailIn["Amazon Bedrock Guardrails (Input Evaluation)"]

    subgraph InspectionPillars["5 Layered Inspection Engines"]
        F1["1. Denied Topics\n(Blocks out-of-scope subjects, e.g. 'legal counsel')"]
        F2["2. Content Filters\n(Hate, Insults, Sexual, Violence - Configurable Thresholds)"]
        F3["3. Sensitive Information Filters\n(PII Regex & Predefined Entities: SSN, Cards, Emails)"]
        F4["4. Word Filters\n(Custom profanity lists & competitor brand blocklists)"]
        F5["5. Contextual Grounding Check\n(Hallucination & Relevance Validation against RAG docs)"]
    end

    GuardrailIn --> InspectionPillars
    
    InspectionPillars -->|"Any Violation Detected"| BlockResponse["Standardized Blocked Response:\n'I cannot fulfill this request per company policy.'"]
    
    InspectionPillars -->|"Passed Input Filters"| FM["Foundation Model Invocation\n(Amazon Nova / Claude)"]
    
    FM --> GuardrailOut["Amazon Bedrock Guardrails (Output Evaluation)"]
    GuardrailOut --> InspectionPillars
    
    InspectionPillars -->|"Passed Output Filters"| CleanOutput["Sanitized, PII-Masked Response Delivered to User"]
```

---

## 🔍 Core Architectural Highlights

1. **Independent Security Layer:** Guardrails operate independently of the underlying foundation model, ensuring consistent safety policies across different models (Nova, Claude, Titan).
2. **PII Masking vs. Blocking:** Sensitive information filters can either redact confidential data (e.g., transforming `4111-XXXX` to `[CREDIT_CARD]`) or terminate the conversation entirely.
3. **Contextual Grounding:** Specifically mitigates hallucinations in RAG architectures by verifying that generated claims are factually grounded in retrieved knowledge base chunks.
