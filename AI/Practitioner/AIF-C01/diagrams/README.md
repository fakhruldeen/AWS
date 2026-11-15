# 📊 AWS Certified AI Practitioner (AIF-C01) Production Architecture Diagrams

> **Module:** Visual Architecture Blueprints  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Exam Version Alignment:** Official v1.2 (October 2026)  
> **Standard:** Standalone production Mermaid diagrams with architectural analysis and exam highlights.

---

## 🗺️ Master Diagrams Index

| # | Blueprint File | Title & Core Subject | Key Services Involved | Domain Alignment |
|---|---|---|---|:---:|
| **01** | **[Diagram_01_Traditional_ML_vs_GenAI_Lifecycle.md](./Diagram_01_Traditional_ML_vs_GenAI_Lifecycle.md)** | **Traditional ML vs. Generative AI Lifecycle**<br>Contrasts traditional predictive data science against the modern generative AI iterative lifecycle. | SageMaker Data Wrangler, Training, Bedrock, JumpStart | Domain 1 & 2 |
| **02** | **[Diagram_02_Transformer_Architecture_and_Tokenization.md](./Diagram_02_Transformer_Architecture_and_Tokenization.md)** | **Transformer Architecture and Tokenization**<br>Visualizes tokenization, positional encoding, multi-head self-attention, and temperature sampling. | Foundation Models, Transformer Decoders | Domain 2 |
| **03** | **[Diagram_03_Amazon_Bedrock_Serverless_Topology_and_Nova_Models.md](./Diagram_03_Amazon_Bedrock_Serverless_Topology_and_Nova_Models.md)** | **Amazon Bedrock Serverless Topology & Nova Models**<br>Serverless endpoint layout, prompt caching, and the Amazon Nova model family tiers. | Amazon Bedrock, Amazon Nova, PrivateLink | Domain 2 & 3 |
| **04** | **[Diagram_04_Enterprise_RAG_Ingestion_and_Retrieval_Flow.md](./Diagram_04_Enterprise_RAG_Ingestion_and_Retrieval_Flow.md)** | **Enterprise RAG Ingestion and Retrieval Flow**<br>End-to-end offline chunking/embedding pipeline and online semantic vector retrieval flow. | Bedrock Knowledge Bases, Titan Embeddings v2, OpenSearch Serverless | Domain 3 |
| **05** | **[Diagram_05_Agentic_AI_Workflow_and_Model_Context_Protocol_MCP.md](./Diagram_05_Agentic_AI_Workflow_and_Model_Context_Protocol_MCP.md)** | **Agentic AI Workflow & Model Context Protocol (MCP)**<br>Autonomous ReAct loops, Action Groups, Lambda execution, and universal MCP tool connectivity. | Bedrock Agents, AgentCore, MCP, Lambda, DynamoDB | Domain 2 & 3 |
| **06** | **[Diagram_06_Model_Customization_Spectrum_Prompt_to_Pretraining.md](./Diagram_06_Model_Customization_Spectrum_Prompt_to_Pretraining.md)** | **Model Customization Spectrum**<br>Trade-offs across Prompt Engineering, RAG, PEFT/LoRA Fine-Tuning, and Full Pre-Training. | Bedrock Custom Models, SageMaker, Trainium | Domain 3 |
| **07** | **[Diagram_07_Bedrock_Guardrails_Multi_Layered_Perimeter.md](./Diagram_07_Bedrock_Guardrails_Multi_Layered_Perimeter.md)** | **Bedrock Guardrails Multi-Layered Perimeter**<br>Five-layered inspection architecture for Denied Topics, Content, PII Masking, Word, and Grounding checks. | Amazon Bedrock Guardrails | Domain 4 |
| **08** | **[Diagram_08_SageMaker_AI_Ecosystem_Canvas_JumpStart_Clarify.md](./Diagram_08_SageMaker_AI_Ecosystem_Canvas_JumpStart_Clarify.md)** | **SageMaker AI Ecosystem**<br>Role-based persona workflows across Canvas (no-code), JumpStart (models), Clarify (bias), and Model Cards. | SageMaker Canvas, JumpStart, Clarify, Model Cards | Domain 1 & 4 |
| **09** | **[Diagram_09_Generative_AI_Security_Scoping_Matrix.md](./Diagram_09_Generative_AI_Security_Scoping_Matrix.md)** | **Generative AI Security Scoping Matrix**<br>Architectural shared responsibility models across Scopes 1, 2, 3, and 4. | Amazon Q, Bedrock, SageMaker, Trainium | Domain 5 |
| **10** | **[Diagram_10_Enterprise_AI_Security_KMS_and_Audit_Loop.md](./Diagram_10_Enterprise_AI_Security_KMS_and_Audit_Loop.md)** | **Enterprise AI Security, KMS, and Audit Loop**<br>Defense-in-depth layout connecting PrivateLink, IAM, KMS envelope encryption, Macie, and CloudTrail. | AWS PrivateLink, IAM, KMS, CloudTrail, Macie | Domain 5 |
