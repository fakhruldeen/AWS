# Lecture 03: Prompt Engineering & RAG Architecture

## ⏱️ Timing & Delivery Strategy
- **Duration:** 120 Minutes
- **Lecture Slide Deck:** `slides/Module_02_Amazon_Bedrock_and_RAG_Slides.md` (Part 1)
- **Hands-On Transition:** `labs/Lab_02_Building_RAG_with_Bedrock_Knowledge_Bases.md`

## 🎯 Learning Objectives
1. Implement core prompt engineering techniques: Zero-shot, Few-shot, System Prompts, Chain-of-Thought (CoT), and ReAct prompting.
2. Architecture of **Amazon Bedrock Knowledge Bases**: Ingesting unstructured PDFs from Amazon S3 $\rightarrow$ chunking & Titan Embeddings $\rightarrow$ OpenSearch Serverless vector indexing $\rightarrow$ context retrieval $\rightarrow$ augmented FM generation.
3. Contrast RAG vs. Fine-Tuning: RAG provides dynamic, real-time proprietary knowledge retrieval without changing model weights; Fine-Tuning updates model weights for specific style or task adaptation.
