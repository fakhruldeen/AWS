# Domain 2: Fundamentals of GenAI (`24%` of Scored Content)

> **Official Blueprint:** AWS Certified AI Practitioner (`AIF-C01`) Exam Guide v1.2 (Oct 29, 2026)  
> **Scored Questions (~50 scored total):** ~12 scored questions (~16 in a 65-question full mock)

---

## Task Statement 2.1: Explain the basic concepts of generative AI (GenAI)
- **Foundational Mechanics:** `Tokens`, `Chunking`, `Embeddings`, `Vectors`, `Prompt Engineering`, Transformer-based `LLMs`, Foundation Models (`FMs`), Multi-modal models, Diffusion models.
- **Use Cases:** Text/image/video/audio generation, summarization, AI assistants, translation, code generation, customer service agents, semantic search, recommendation engines.
- **FM Lifecycle:** Data selection → Model selection → Pre-training → Fine-tuning → Evaluation → Deployment → Continuous feedback.
- **Token-Based Pricing:** Input vs. output token pricing, context window length impact on latency and inference cost.
- **Context Engineering (v1.2):** Designing and dynamically managing the entire runtime context window (system prompts, RAG context, memory, tool schemas/outputs).
- **Agentic AI Concepts (v1.2):** Multi-agent system patterns, **Model Context Protocol (`MCP`)** for connecting agents to external tools/systems, multi-agent communication patterns, memory management (short-term & long-term), tool usage, and workflow orchestration.

## Task Statement 2.2: Understand the capabilities and limitations of GenAI for solving business problems
- **Advantages:** Adaptability across tasks, responsiveness, conversational interfaces, rapid content/code generation.
- **Disadvantages / Limitations:** `Hallucinations`, low `interpretability` (black-box), `inaccuracy`, `nondeterminism`, knowledge cutoffs.
- **Model Selection Factors:** Model type/modality, performance requirements, capabilities, constraints, compliance, cost, latency, and model complexity.
- **Business Value & Metrics:** Cross-domain performance, `ROI`, operational efficiency, conversion rate, average revenue per user (`ARPU`), accuracy, customer lifetime value (`CLV`).

## Task Statement 2.3: Describe AWS infrastructure and technologies for building GenAI applications
- **Core AWS GenAI Services (v1.2):** `Amazon Bedrock`, `Amazon Nova`, `Amazon SageMaker AI`, `SageMaker JumpStart`, **`Amazon Quick`**, **`Kiro`**, **`Strands Agents`**, **`Amazon Bedrock AgentCore`**, **`AWS Transform`**.
- **Advantages of AWS GenAI Services:** Accessibility, lower barrier to entry, efficiency, cost-effectiveness, speed to market, alignment with business objectives.
- **Benefits of AWS Infrastructure:** Enterprise security, global compliance, responsible AI tooling, safety, and custom silicon (`AWS Trainium`, `AWS Inferentia`).
- **Cost Tradeoffs:** Responsiveness, availability, redundancy, performance, regional coverage, `On-Demand` token-based pricing vs. `Batch Inference` vs. `Provisioned Throughput` vs. custom fine-tuned model hosting.
