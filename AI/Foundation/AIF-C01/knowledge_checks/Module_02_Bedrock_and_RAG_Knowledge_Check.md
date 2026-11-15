# Module 02 Knowledge Check: Generative AI & Amazon Bedrock

### Questions
1. **What is Amazon Bedrock?**
   - A) A physical server appliance installed in on-premises datacenters
   - B) A fully managed serverless service providing access to leading Foundation Models via an API
   - C) A relational database engine for transactional processing
   - D) A network load balancer operating at Layer 4
2. **What does Retrieval-Augmented Generation (RAG) provide?**
   - A) Permanently retrains the neural network weights of an LLM
   - B) Augments user prompts with retrieved proprietary company data from a vector store at query time
   - C) Translates programming languages between Python and Rust
   - D) Generates synthetic audio waveforms using Amazon Polly
3. **What is an Embedding Vector?**
   - A) A continuous array of numbers capturing the semantic meaning of text in multi-dimensional space
   - B) An IAM role permission boundary JSON document
   - C) A physical fiber-optic connection in AWS Direct Connect
   - D) A container image stored in Amazon ECR
4. **Which prompt engineering technique provides the model with a few solved examples before asking it to solve a new problem?**
   - A) Zero-Shot Prompting
   - B) Few-Shot Prompting
   - C) Chain-of-Thought Prompting
   - D) ReAct Framework
5. **What is the maximum number of tokens a foundation model can process across both input prompt and output response called?**
   - A) Embedding Dimension
   - B) Context Window
   - C) Epoch
   - D) Learning Rate

---

### Answer Key & Explanations
| Q# | Answer | Key Concept Reference |
| :---: | :---: | :--- |
| **1** | **B** | Amazon Bedrock is a serverless API service offering leading FMs from Anthropic, Meta, Amazon, etc. |
| **2** | **B** | RAG retrieves external data dynamically to ground model answers without updating model weights. |
| **3** | **A** | Vector embeddings represent semantic concepts as points in high-dimensional vector space. |
| **4** | **B** | Few-Shot prompting includes exemplar input-output demonstrations to guide model behavior. |
| **5** | **B** | Context Window is the token capacity constraint for prompt inputs plus completion outputs. |
