# Module 02 Knowledge Check: Fundamentals of Generative AI & Nova

> **Domain:** Domain 2: Fundamentals of Generative AI (24% Weight)  
> **Questions:** 10 Diagnostic Questions with Answers & Rationales

---

### Questions

1. **What fundamental mechanism in the Transformer architecture allows models to process all words in a sentence simultaneously and capture long-range contextual relationships?**
   - A) Recurrent hidden states
   - B) Multi-Head Self-Attention
   - C) Causal Convolution
   - D) Gradient clipping

2. **Which model within the Amazon Nova foundation model family is engineered specifically for text-to-text processing with the lowest latency and lowest cost?**
   - A) Amazon Nova Premier
   - B) Amazon Nova Pro
   - C) Amazon Nova Lite
   - D) Amazon Nova Micro

3. **What happens to the output of a foundation model when the Temperature parameter is lowered to 0.0?**
   - A) The output becomes maximum randomness and creative
   - B) The output becomes completely deterministic and repeatable
   - C) The context window capacity doubles
   - D) The model generates images instead of text

4. **Which sampling parameter restricts token selection to the smallest cumulative probability mass exceeding threshold $P$?**
   - A) Top-K
   - B) Top-P (Nucleus Sampling)
   - C) Stop Sequence
   - D) Max Generation Length

5. **An AI engineer wants to integrate an autonomous agent with external local developer tools and cloud services using a single universal standard. Which open protocol should be utilized?**
   - A) OpenAPI 2.0
   - B) Model Context Protocol (MCP)
   - C) SOAP XML
   - D) GraphQL Federation

6. **What is the approximate rule of thumb for token estimation in English text for typical Large Language Models?**
   - A) 1 token = 10 words
   - B) 1 token ≈ 0.75 words (or 1,000 tokens ≈ 750 words)
   - C) 1 token = 1 sentence
   - D) 1 token = 1 character

7. **Which Amazon foundation model family provides native high-fidelity image generation, inpainting, and invisible digital watermarking?**
   - A) Amazon Nova Micro
   - B) Amazon Titan Image Generator
   - C) Amazon Polly Neural
   - D) Amazon Rekognition Custom Labels

8. **In the Transformer decoder, what is the role of Positional Encodings?**
   - A) To compress embeddings into lower dimensions
   - B) To restore sequential word order information since self-attention processes all tokens in parallel
   - C) To mask future tokens during training
   - D) To prevent overfitting on small datasets

9. **What term describes a failure mode where a Foundation Model generates syntactically convincing, authoritative statements that are factually inaccurate or ungrounded?**
   - A) Overfitting
   - B) Hallucination
   - C) Model drift
   - D) Quantization loss

10. **Which Amazon Nova model is designed for multimodal processing of text, images, and video frames at a frontier level of complex reasoning and agentic planning?**
    - A) Amazon Nova Micro
    - B) Amazon Nova Lite
    - C) Amazon Nova Pro
    - D) Amazon Titan Text Express

---

### Answer Key & Explanations

| Q# | Answer | Key Concept Reference | Detailed Explanation |
|:---:|:---:|:--- |:--- |
| **1** | **B** | Self-Attention Mechanism | Multi-head self-attention computes pairwise token weights across the entire sequence concurrently, replacing recurrent loops. |
| **2** | **D** | Amazon Nova Micro | Nova Micro is text-only, delivering sub-second TTFT and lowest token pricing for fast routing and summarization. |
| **3** | **B** | Temperature 0.0 | Lowering temperature concentrates probability around the argmax token, producing greedy, deterministic responses. |
| **4** | **B** | Top-P (Nucleus Sampling) | Top-P sums probabilities dynamically until $P$ is reached, cutting off the long tail of low-probability words. |
| **5** | **B** | Model Context Protocol (MCP) | MCP is the open standardized protocol for models to discover and execute tools and read resources over JSON-RPC. |
| **6** | **B** | Token Sizing | In English, 1,000 tokens represent approximately 750 words (or 1 token ≈ 0.75 words). |
| **7** | **B** | Titan Image Generator | Titan Image Generator produces high-resolution images and embeds tamper-resistant invisible watermarks. |
| **8** | **B** | Positional Encodings | Self-attention has no innate awareness of sequential order; positional encodings inject word sequence geometry into embeddings. |
| **9** | **B** | Hallucination | Hallucination occurs when an LLM generates fabricated or non-factual information with high linguistic confidence. |
| **10** | **C** | Amazon Nova Pro | Nova Pro is Amazon's frontier multimodal model for software coding, complex math, and autonomous agent orchestration. |
