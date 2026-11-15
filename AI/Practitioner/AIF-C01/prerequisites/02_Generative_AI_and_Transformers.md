# 02. Generative AI & Transformer Foundations Prerequisite

## 1. What is Generative AI?
Traditional machine learning analyzes data to classify or predict. **Generative AI (GenAI)** uses deep learning **Foundation Models (FMs)** trained on vast multi-modal datasets to create novel text, code, images, audio, and synthetic data.

## 2. Tokens & Context Windows
- **Tokens:** The basic unit of text processed by Large Language Models (LLMs). Approximately 1 token $\approx$ 0.75 English words (or 100 tokens $\approx$ 75 words).
- **Context Window:** The maximum number of tokens an LLM can receive as prompt input plus generate as response in a single inference call (e.g., Claude 3.5 Sonnet supports 200,000 tokens).

## 3. High-Dimensional Vector Embeddings & Vector Databases
- Text chunks are passed through an embedding model (e.g., Amazon Titan Text Embeddings) to produce dense numerical vectors (e.g., a 1,536-dimensional array of floating-point numbers).
- Semantically similar concepts cluster close together in vector space measured by **Cosine Similarity**.
- Stored in vector databases (e.g., **Amazon OpenSearch Serverless**, **Amazon Aurora pgvector**) to power **Retrieval-Augmented Generation (RAG)** in Amazon Bedrock Knowledge Bases.

## 4. Inference Parameters
- **Temperature (0.0 to 1.0):** Controls randomness. Low temperature (0.0 - 0.2) produces deterministic, factual output. High temperature (0.8 - 1.0) produces creative, diverse output.
- **Top-P (Nucleus Sampling):** Restricts token choices to the cumulative probability mass $P$ (e.g., 0.9 = only top 90% most probable next tokens).
