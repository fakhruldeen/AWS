# Diagram 04: Enterprise RAG Ingestion and Retrieval Flow

> **Architecture Blueprint:** `Diagram_04_Enterprise_RAG_Ingestion_and_Retrieval_Flow.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 3 (Applications of Foundation Models)

---

## 🏛️ Architectural Blueprint

```mermaid
sequenceDiagram
    autonumber
    actor User as User / Client
    participant App as Application / API
    participant Bedrock as Amazon Bedrock Runtime
    participant VectorDB as Vector Store (OpenSearch Serverless)
    participant EmbedModel as Titan Embeddings v2
    participant FM as Foundation Model (Nova / Claude)

    Note over User, VectorDB: Phase 1: Ingestion Pipeline (Offline Sync)
    rect rgb(240, 248, 255)
        Note right of VectorDB: S3 Documents -> Chunked -> Embedded -> Stored in Vector Index
    end

    Note over User, FM: Phase 2: Online Query & Augmented Generation
    User->>App: Submits question: "What is our company travel reimbursement policy?"
    App->>Bedrock: Invokes Bedrock RetrieveAndGenerate API
    Bedrock->>EmbedModel: Generate dense vector embedding for user query
    EmbedModel-->>Bedrock: Returns 1536-dimensional query vector
    Bedrock->>VectorDB: Execute k-NN Semantic Vector Search (Top-K = 5)
    VectorDB-->>Bedrock: Returns relevant document chunks with metadata & citations
    Bedrock->>Bedrock: Synthesize Augmented Prompt (System Directive + Context Chunks + Query)
    Bedrock->>FM: Invoke Model with Grounded Prompt
    FM-->>Bedrock: Generates factual response grounded strictly in context
    Bedrock-->>App: Returns final answer with inline source citations
    App-->>User: Displays verified answer to employee
```

---

## 🔍 Core Architectural Highlights

1. **Dual-Phase Architecture:** Decouples heavy document ingestion (asynchronous parsing, chunking, and embedding) from low-latency online inference.
2. **Deterministic Grounding:** The LLM is constrained to respond using only retrieved snippets, mitigating hallucinations.
3. **Traceability:** Bedrock Knowledge Bases automatically appends S3 document citations (bucket, object, and page numbers) for auditable compliance.
