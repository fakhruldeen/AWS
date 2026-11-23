# Domain 3 Revision Questions: Applications of Foundation Models

> **Domain:** Domain 3: Applications of Foundation Models (28% Exam Weight)  
> **Question Count:** 15 Comprehensive Scenario-Based Questions  
> **Format:** Multiple Choice & Multiple Response with Detailed Explanations

---

### Question 1
An enterprise customer support portal needs to answer customer inquiries based on private PDF warranty documents stored in Amazon S3. The company has strict requirements: the model must cite source pages, provide grounded answers, and require zero training code. Which architecture meets all requirements?
- [ ] A) Fine-tune an open-weights model using SageMaker JumpStart
- [ ] B) Deploy Amazon Bedrock Knowledge Bases connected to S3 and OpenSearch Serverless
- [ ] C) Pre-train an Amazon Nova model from scratch on AWS Trainium
- [ ] D) Embed documents into Amazon DynamoDB and use full table scans
> **Correct Answer:** B  
> **Rationale:** Amazon Bedrock Knowledge Bases automates Retrieval-Augmented Generation (RAG). It chunks and embeds S3 documents into vector collections and provides responses with exact citations.

---

### Question 2
A developer writes a prompt that includes 3 input-output examples demonstrating how to convert unstructured medical notes into strict JSON payloads. What prompt engineering strategy is being applied?
- [ ] A) Zero-Shot Prompting
- [ ] B) Few-Shot Prompting (In-Context Learning)
- [ ] C) Directional Stimulus Prompting
- [ ] D) Parameter-Efficient Fine-Tuning
> **Correct Answer:** B  
> **Rationale:** Providing multiple input-output demonstrations within the prompt is known as Few-Shot Prompting or In-Context Learning.

---

### Question 3
An application uses a 20,000-token enterprise system instruction and product catalog in every customer chat turn. Invocations suffer from high latency and significant token costs. Which feature in Amazon Bedrock should be enabled to optimize performance?
- [ ] A) Cross-Region Replication
- [ ] B) Prompt Caching
- [ ] C) Model Distillation
- [ ] D) Auto-scaling Endpoints
> **Correct Answer:** B  
> **Rationale:** Bedrock Prompt Caching caches static prompt preambles in GPU memory, cutting latency by up to 80% and input token costs by up to 50% for repeated queries.

---

### Question 4
An AI architect wants to fine-tune an LLM to follow a specific medical clinical report format. The architect wants to avoid the risk of "Catastrophic Forgetting" and minimize GPU training compute costs. Which customization technique is optimal?
- [ ] A) Full Parameter Fine-Tuning
- [ ] B) Parameter-Efficient Fine-Tuning (PEFT) using Low-Rank Adaptation (LoRA)
- [ ] C) Pre-training from scratch on an EC2 UltraCluster
- [ ] D) Unsupervised K-Means Clustering
> **Correct Answer:** B  
> **Rationale:** LoRA freezes the original pre-trained foundation weights and trains small adapter matrices ($<1\%$ of parameters), preventing catastrophic forgetting and minimizing compute hours.

---

### Question 5
Which evaluation metric is standard for assessing automated text summarization models by calculating $n$-gram recall against reference gold-standard summaries?
- [ ] A) BLEU
- [ ] B) ROUGE
- [ ] C) Perplexity
- [ ] D) RMSE
> **Correct Answer:** B  
> **Rationale:** ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures $n$-gram recall (ROUGE-1, ROUGE-2, ROUGE-L) and is the gold standard for summarization evaluation.

---

### Question 6
An engineering team is building an autonomous Bedrock Agent to book hotel reservations. What component connects the agent's reasoning engine to backend databases and executes business logic via AWS Lambda?
- [ ] A) Prompt Cache
- [ ] B) Action Group
- [ ] C) Guardrail Filter
- [ ] D) Bedrock Playground
> **Correct Answer:** B  
> **Rationale:** Action Groups define the actions an agent can take, tying OpenAPI 3.0 REST specifications to AWS Lambda functions that execute business logic.

---

### Question 7
In Retrieval-Augmented Generation (RAG), what is the difference between fixed-size chunking and hierarchical (parent-child) chunking?
- [ ] A) Fixed-size chunking splits text into static token intervals; hierarchical chunking indexes small child chunks for vector search but retrieves larger parent chunks for LLM context.
- [ ] B) Fixed-size chunking requires GPUs; hierarchical chunking runs on CPUs.
- [ ] C) Fixed-size chunking deletes stop words; hierarchical chunking translates documents to German.
- [ ] D) Hierarchical chunking alters the underlying model weights.
> **Correct Answer:** A  
> **Rationale:** Hierarchical chunking optimizes search accuracy: small child chunks provide precise embedding matches, while the larger parent chunk provides the LLM with sufficient surrounding narrative context.

---

### Question 8
What is the "LLM-as-a-Judge" methodology, and what is a primary advantage of this approach in model evaluation?
- [ ] A) A human courtroom deciding copyright disputes
- [ ] B) Using a high-capability frontier foundation model to automatically evaluate smaller model outputs against defined scoring rubrics, enabling scalable automated assessment
- [ ] C) A compiler flag that halts training when loss increases
- [ ] D) A hardware chip that verifies cryptographic signatures
> **Correct Answer:** B  
> **Rationale:** LLM-as-a-judge leverages frontier models (e.g., Nova Pro, Claude 3.5) to evaluate complex qualitative criteria (helpfulness, tone, grounding) automatically at scale.

---

### Question 9
A production generative AI application experiences unpredictable traffic surges, resulting in `ThrottlingException (HTTP 429)` errors during peak business hours. What configuration guarantees dedicated capacity and consistent throughput?
- [ ] A) Purchase Amazon Bedrock Provisioned Throughput (Model Units)
- [ ] B) Enable AWS Shield Standard
- [ ] C) Switch to Amazon Nova Micro exclusively
- [ ] D) Increase temperature to 1.0
> **Correct Answer:** A  
> **Rationale:** Provisioned Throughput allocates dedicated Model Units (MUs) for foundation models in Bedrock, guaranteeing throughput SLAs and eliminating on-demand rate-limit throttling.

---

### Question 10 (Multiple Response)
Which TWO embedding models and vector database pairings are natively supported by Amazon Bedrock Knowledge Bases? (Select TWO.)
- [ ] A) Amazon Titan Text Embeddings v2 with Amazon OpenSearch Serverless
- [ ] B) Cohere Embed English with Amazon Aurora PostgreSQL (pgvector)
- [ ] C) Amazon Polly Neural with Amazon Simple Queue Service (SQS)
- [ ] D) Amazon Rekognition with Amazon Glacier Deep Archive
- [ ] E) AWS Trainium with Amazon CloudFront
> **Correct Answers:** A, B  
> **Rationale:** Bedrock Knowledge Bases supports Titan and Cohere embedding models integrated with vector stores including OpenSearch Serverless, Aurora pgvector, Pinecone, and Redis Enterprise.

---

### Question 11
What is a Prompt Injection attack in Generative AI?
- [ ] A) Overheating of GPU server instances
- [ ] B) An adversarial attack where a user inputs malicious text designed to override the system prompt and hijack the model's behavior
- [ ] C) Injecting SQL statements into an Amazon RDS database
- [ ] D) Exceeding the maximum token limit of an S3 bucket
> **Correct Answer:** B  
> **Rationale:** Prompt injection occurs when untrusted user input tricks the foundation model into ignoring developer instructions and executing unauthorized actions.

---

### Question 12
When evaluating machine translation models, which metric calculates $n$-gram precision against reference translations?
- [ ] A) ROUGE
- [ ] B) BLEU (Bilingual Evaluation Understudy)
- [ ] C) F1-Score
- [ ] D) Mean Squared Error
> **Correct Answer:** B  
> **Rationale:** BLEU measures the precision of $n$-grams in the generated translation against human reference texts.

---

### Question 13
An organization wants to teach a foundation model an entirely new specialized non-English language that is missing from its pre-training corpus. Which customization method is required?
- [ ] A) Few-Shot Prompting
- [ ] B) Continued Pre-Training with domain text corpora
- [ ] C) Reducing the context window to 512 tokens
- [ ] D) Increasing Top-K to 500
> **Correct Answer:** B  
> **Rationale:** Introducing a completely new vocabulary and syntax requires feeding large unlabeled text corpora through Continued Pre-Training to modify the model's foundational weights.

---

### Question 14
In the Amazon Bedrock Converse API, what is the role of the `system` parameter block?
- [ ] A) It contains the user's password
- [ ] B) It specifies foundational instructions, persona, and behavioral boundaries that govern the entire conversation
- [ ] C) It tells the AWS hypervisor which physical CPU core to allocate
- [ ] D) It formats output exclusively as binary hex
> **Correct Answer:** B  
> **Rationale:** The system prompt sets the operational persona, role, rules, and constraints for the foundation model throughout the conversational session.

---

### Question 15
What is the primary difference between RAG and Fine-Tuning regarding operational data currency?
- [ ] A) Fine-tuning updates immediately when S3 documents change; RAG requires a 2-day training run.
- [ ] B) RAG reflects data changes instantly as soon as documents are synced in the vector index; fine-tuning requires retraining to incorporate new information.
- [ ] C) Neither RAG nor fine-tuning can incorporate new data.
- [ ] D) RAG alters model weights; fine-tuning does not.
> **Correct Answer:** B  
> **Rationale:** RAG decouples knowledge retrieval from model weights: syncing a document in the vector store immediately updates the model's factual knowledge base without retraining.
