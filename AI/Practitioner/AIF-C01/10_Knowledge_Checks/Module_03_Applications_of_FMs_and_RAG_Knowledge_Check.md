# Module 03 Knowledge Check: Applications of Foundation Models & RAG

> **Domain:** Domain 3: Applications of Foundation Models (28% Weight)  
> **Questions:** 10 Diagnostic Questions with Answers & Rationales

---

### Questions

1. **A bank wants an AI application to answer employee questions about internal HR policy documents stored in S3 without retraining the underlying model. Which architecture should be deployed?**
   - A) Continued Pre-training
   - B) Full Fine-Tuning
   - C) Retrieval-Augmented Generation (RAG) with Bedrock Knowledge Bases
   - D) SageMaker JumpStart Endpoints with LoRA

2. **Which vector database option in AWS provides a fully managed, serverless vector search index for Bedrock Knowledge Bases without managing cluster infrastructure?**
   - A) Amazon OpenSearch Serverless
   - B) Amazon Redshift Serverless
   - C) Amazon DynamoDB Accelerator (DAX)
   - D) Amazon ElastiCache for Memcached

3. **What is the primary benefit of enabling Prompt Caching in Amazon Bedrock for repetitive multi-turn enterprise conversations?**
   - A) It increases model parameter count dynamically
   - B) It caches static portions of prompts, reducing latency by up to 80% and token costs by up to 50%
   - C) It converts text prompts into audio files automatically
   - D) It enables cross-account billing consolidation

4. **Which prompt engineering strategy involves providing 2 to 5 structured input and output examples in the prompt to teach the model a specific format or tone?**
   - A) Zero-Shot Prompting
   - B) Few-Shot Prompting (In-Context Learning)
   - C) Chain-of-Thought Prompting
   - D) Directional Stimulus Prompting

5. **Which model customization technique freezes pre-trained foundation model weights and injects lightweight trainable adapter matrices into transformer layers?**
   - A) Full Parameter Fine-Tuning
   - B) Low-Rank Adaptation (LoRA / PEFT)
   - C) Knowledge Distillation
   - D) Quantization-Aware Training

6. **Which evaluation metric measures $n$-gram recall between model-generated summaries and reference human summaries?**
   - A) BLEU
   - B) ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
   - C) Perplexity
   - D) Mean Absolute Percentage Error (MAPE)

7. **In Amazon Bedrock Agents, which component allows the agent to execute actions against enterprise backend systems using AWS Lambda and OpenAPI schemas?**
   - A) Knowledge Bases
   - B) Action Groups
   - C) Guardrails
   - D) Model Evaluation Jobs

8. **What modern evaluation methodology uses a high-capability frontier model (such as Amazon Nova Pro) to automatically score the outputs of smaller models based on predefined rubrics?**
   - A) A/B Split Testing
   - B) LLM-as-a-Judge
   - C) Linear Regression Validation
   - D) K-Fold Cross-Validation

9. **When should an organization transition from On-Demand token pricing to Provisioned Throughput in Amazon Bedrock?**
   - A) When running infrequent, ad-hoc exploratory testing in the playground
   - B) When high-volume steady-state traffic requires predictable pricing and guaranteed low-latency throughput SLAs
   - C) When only using open-source models
   - D) When prompt lengths are under 100 tokens

10. **What is "Catastrophic Forgetting" in the context of foundation model fine-tuning?**
    - A) A GPU memory overflow during backpropagation
    - B) When a model loses its general reasoning and broad conversational capabilities after aggressive fine-tuning on a narrow task
    - C) When an S3 bucket lifecycle rule deletes training data
    - D) When the context window exceeds 128,000 tokens

---

### Answer Key & Explanations

| Q# | Answer | Key Concept Reference | Detailed Explanation |
|:---:|:---:|:--- |:--- |
| **1** | **C** | RAG Architecture | RAG grounds foundation models on private S3 data dynamically without altering base model weights. |
| **2** | **A** | OpenSearch Serverless | Amazon OpenSearch Serverless vector collections provide automated, zero-admin vector indexing for Bedrock Knowledge Bases. |
| **3** | **B** | Prompt Caching | Caching large system prompts or reference documents avoids re-processing identical tokens, saving time and money. |
| **4** | **B** | Few-Shot Prompting | Few-shot prompting guides the model via in-context demonstrations without updating internal parameters. |
| **5** | **B** | PEFT / LoRA | LoRA trains low-rank adapter matrices (<1% of parameters), preserving base model knowledge and slashing compute costs. |
| **6** | **B** | ROUGE Metric | ROUGE measures $n$-gram recall (ROUGE-1, ROUGE-2, ROUGE-L) and is standard for evaluating text summarization. BLEU measures precision for translation. |
| **7** | **B** | Action Groups | Action Groups connect the reasoning loop of a Bedrock Agent to real-world AWS Lambda executions. |
| **8** | **B** | LLM-as-a-Judge | LLM-as-a-judge leverages advanced models to evaluate factual accuracy, coherence, and safety against scoring criteria. |
| **9** | **B** | Provisioned Throughput | Provisioned Throughput commits Model Units (MU) to provide dedicated, non-throttled capacity for mission-critical production loads. |
| **10** | **B** | Catastrophic Forgetting | When fine-tuning overwrites too many base weights, the model "forgets" its broader foundational intelligence. |
