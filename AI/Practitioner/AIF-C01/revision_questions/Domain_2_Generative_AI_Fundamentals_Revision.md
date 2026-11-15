# Domain 2 Revision Questions: Fundamentals of Generative AI

> **Domain:** Domain 2: Fundamentals of Generative AI (24% Exam Weight)  
> **Question Count:** 15 Comprehensive Scenario-Based Questions  
> **Format:** Multiple Choice & Multiple Response with Detailed Explanations

---

### Question 1
What fundamental architectural breakthrough allowed the Transformer architecture to surpass recurrent neural networks (RNNs) in processing speed and context retention?
- [ ] A) Processing text sequentially one token at a time
- [ ] B) Multi-Head Self-Attention mechanisms operating in parallel across the entire sequence
- [ ] C) Eliminating matrix multiplication in dense layers
- [ ] D) Storing all past conversation turns in hard drive cache
> **Correct Answer:** B  
> **Rationale:** Transformers replace sequential recurrence with self-attention, allowing all tokens in a prompt to be processed concurrently across GPU hardware.

---

### Question 2
An engineer is building a high-volume customer intent classification router. The system processes millions of short queries daily and requires sub-second response times with minimal token costs. Which Amazon Nova foundation model is optimal?
- [ ] A) Amazon Nova Premier
- [ ] B) Amazon Nova Pro
- [ ] C) Amazon Nova Lite
- [ ] D) Amazon Nova Micro
> **Correct Answer:** D  
> **Rationale:** Amazon Nova Micro is a text-only foundation model engineered specifically for ultra-low latency (lowest TTFT) and lowest cost per token.

---

### Question 3
A developer notices that an LLM in the Bedrock Chat Playground produces completely different answers when the identical prompt is submitted three times. Which configuration change will force the model to provide deterministic, identical completions?
- [ ] A) Increase Max Generation Length to 4,000 tokens
- [ ] B) Set Temperature to 0.0
- [ ] C) Increase Top-P to 1.0
- [ ] D) Add a stop sequence containing punctuation marks
> **Correct Answer:** B  
> **Rationale:** A Temperature of 0.0 collapses the softmax probability distribution, forcing greedy decoding (selecting the single highest probability token), resulting in deterministic output.

---

### Question 4
What is the core distinction between discriminative AI models and generative AI models?
- [ ] A) Discriminative models generate novel data instances; generative models output class labels.
- [ ] B) Discriminative models calculate $P(Y|X)$ to classify inputs; generative models capture data distributions to synthesize novel data.
- [ ] C) Generative models run only on CPUs; discriminative models run on GPUs.
- [ ] D) Discriminative models require transformers; generative models use only decision trees.
> **Correct Answer:** B  
> **Rationale:** Discriminative models separate data points into classes or predict continuous numbers. Generative models learn the underlying probability distribution to generate new content.

---

### Question 5
What is the role of the Model Context Protocol (MCP) in modern generative AI and agentic systems?
- [ ] A) An encryption algorithm used to secure weights in AWS KMS
- [ ] B) An open, standardized protocol enabling foundation models to discover, inspect, and execute tools and read resources over JSON-RPC
- [ ] C) A compression technique to reduce LLM memory footprints by 90%
- [ ] D) An AWS IAM policy format for managing root account credentials
> **Correct Answer:** B  
> **Rationale:** The Model Context Protocol (MCP) is an open standard that decouples models from tools and data sources, eliminating custom one-off API glue code.

---

### Question 6
An organization wants to create realistic product lifestyle images for an online catalog and require invisible proof-of-authenticity watermarks embedded into every generated image. Which AWS service natively fulfills this requirement?
- [ ] A) Amazon Rekognition
- [ ] B) Amazon Titan Image Generator
- [ ] C) Amazon Nova Micro
- [ ] D) Amazon Polly
> **Correct Answer:** B  
> **Rationale:** Amazon Titan Image Generator synthesizes photorealistic images and automatically embeds invisible, tamper-resistant digital watermarks to support content provenance.

---

### Question 7
In Large Language Models, what does the "Context Window" represent?
- [ ] A) The total number of hours an EC2 GPU instance can run before rebooting
- [ ] B) The maximum number of combined input and output tokens the model can process and retain in a single invocation
- [ ] C) The physical monitor display size of the SageMaker Studio console
- [ ] D) The number of layers in the Transformer encoder
> **Correct Answer:** B  
> **Rationale:** The context window is the finite token capacity (e.g., 32K, 128K, 200K tokens) that an LLM can attend to during a single inference call.

---

### Question 8
Which model in the Amazon Nova family provides a balanced multimodal architecture capable of processing text, images, and video frames at high throughput and cost-optimized economics?
- [ ] A) Amazon Nova Micro
- [ ] B) Amazon Nova Lite
- [ ] C) Amazon Nova Premier
- [ ] D) Amazon Titan Text Embeddings
> **Correct Answer:** B  
> **Rationale:** Amazon Nova Lite is a cost-effective, high-speed multimodal foundation model designed for document understanding, visual search, and video analysis.

---

### Question 9
What are dense vector embeddings, and what mathematical operation is commonly used to measure their semantic similarity?
- [ ] A) Sparse binary strings; measured via Hamming distance
- [ ] B) High-dimensional continuous numerical vectors; measured via Cosine Similarity or Euclidean Distance
- [ ] C) Compressed image pixels; measured via Mean Absolute Error
- [ ] D) Plaintext ASCII characters; measured via Levenshtein distance
> **Correct Answer:** B  
> **Rationale:** Vector embeddings represent semantic concepts in high-dimensional continuous geometric space. Proximity (similarity) is evaluated using Cosine Similarity or Dot Product.

---

### Question 10 (Multiple Response)
Which TWO statements correctly describe the ReAct (Reason + Act) prompting framework used by autonomous agents? (Select TWO.)
- [ ] A) The agent executes a continuous loop: Thought $\rightarrow$ Action $\rightarrow$ Observation $\rightarrow$ Thought
- [ ] B) The agent updates the foundational weights of the underlying model during every interaction
- [ ] C) The agent decomposes complex goals into intermediate reasoning steps and tool invocations
- [ ] D) The agent disables temperature and forces greedy token decoding
- [ ] E) The agent stores all user passwords in plaintext
> **Correct Answers:** A, C  
> **Rationale:** ReAct interleaves reasoning ("Thought") with real-world tool execution ("Action") and feedback analysis ("Observation") to solve complex multi-hop tasks.

---

### Question 11
What is Top-P (Nucleus Sampling), and how does reducing it affect LLM text generation?
- [ ] A) It sets the absolute maximum token length; reducing it causes early truncation.
- [ ] B) It selects the top $K$ tokens; reducing it increases vocabulary diversity.
- [ ] C) It restricts sampling to the smallest pool of tokens whose cumulative probability exceeds $P$; reducing it removes unlikely or unusual words.
- [ ] D) It adds random Gaussian noise to the attention weights.
> **Correct Answer:** C  
> **Rationale:** Nucleus sampling (Top-P) dynamically adjusts the candidate token pool based on cumulative probability mass, preventing bizarre or out-of-context token generation.

---

### Question 12
A legal assistant application is asked to cite precedent cases. The model invents plausible-sounding court citations and case numbers that do not exist. What is this phenomenon called?
- [ ] A) Prompt Injection
- [ ] B) Hallucination
- [ ] C) Data Poisoning
- [ ] D) Over-fitting
> **Correct Answer:** B  
> **Rationale:** Hallucination occurs when an LLM generates fluent, confident text that is factually ungrounded or fabricated.

---

### Question 13
Why are Positional Encodings necessary in the Transformer architecture?
- [ ] A) Because Transformers process all tokens in parallel and lack an inherent mechanism to represent word sequence order
- [ ] B) To prevent unauthorized cross-region data transfers
- [ ] C) To compress token vectors from 1536 dimensions down to 128 dimensions
- [ ] D) To encrypt prompt payloads before sending to Bedrock
> **Correct Answer:** A  
> **Rationale:** Without positional encodings, the sentence "Dog bites man" and "Man bites dog" would appear identical to the multi-head self-attention mechanism.

---

### Question 14
Which Amazon Nova foundation model represents the frontier capability tier for advanced reasoning, complex code generation, and multi-step autonomous agent workflows?
- [ ] A) Amazon Nova Micro
- [ ] B) Amazon Nova Lite
- [ ] C) Amazon Nova Pro
- [ ] D) Amazon Titan Text Lite
> **Correct Answer:** C  
> **Rationale:** Amazon Nova Pro is Amazon's highest-capability multimodal reasoning model in the Nova family, ideal for complex software engineering and agentic orchestration.

---

### Question 15
What is the primary function of a Stop Sequence in an LLM inference request?
- [ ] A) It shuts down the EC2 GPU instance immediately
- [ ] B) It specifies a character sequence that, upon generation, halts further token output
- [ ] C) It blocks prompt injection attacks
- [ ] D) It flushes the Amazon OpenSearch vector cache
> **Correct Answer:** B  
> **Rationale:** Stop sequences signal the model's inference engine to stop generating tokens immediately when a specified string (e.g., `"\n\n"` or `"User:"`) is emitted.
