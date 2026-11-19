# Lab 03: Enterprise RAG with Amazon Bedrock Knowledge Bases & OpenSearch Serverless

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Exam Domain Alignment:** Domain 3 (Applications of Foundation Models) & Domain 2 (Fundamentals of Generative AI)  
> **Estimated Duration:** 60 minutes  
> **Cost Profile:** Low pay-per-use (<$0.25 for testing); ⚠️ **Must delete OpenSearch Serverless collection post-lab to avoid idle OCU charges!**  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Overview & Exam Objectives

Retrieval-Augmented Generation (RAG) is the most heavily tested architectural pattern on the AIF-C01 exam. It enables foundation models to answer queries using private, proprietary, dynamic company documents **without retraining or fine-tuning model weights**, completely eliminating hallucinations by anchoring responses in verifiable citations.

By completing this guided lab, you will master:
1. **The Complete Enterprise RAG Pipeline:** Document storage in Amazon S3, automated text chunking, dense vector embedding generation, vector indexing, and grounded inference.
2. **Chunking Strategy Trade-offs:** The operational differences between **Default (Fixed-Size)**, **Hierarchical (Parent-Child)**, **Semantic**, and **No Chunking**.
3. **Vector Database Architecture:** How **Amazon OpenSearch Serverless (Vector Engine)** manages security policies (Encryption, Network, Data Access) and indexes high-dimensional vectors using **HNSW**.
4. **Hybrid Search & Semantic Reranking:** Combining dense semantic vector distance with sparse lexical keyword matching (**BM25**).
5. **API Distinction:** The precise behavioral difference between the `Retrieve` API and the `RetrieveAndGenerate` API.

---

## 🏗️ Architectural Topology

```mermaid
flowchart TD
    User["Student / Query Client"]
    
    subgraph DataIngestion ["1. Data Ingestion & Indexing Pipeline (Sync)"]
        S3["Amazon S3 Bucket\n(Raw PDFs, Docs, Policies)"]
        Chunker["Document Chunker\n(Default / Hierarchical / Semantic)"]
        EmbeddingModel["Amazon Titan Text Embeddings v2\n(Generates 1,024-dim Vector Arrays)"]
        VectorDB[("Amazon OpenSearch Serverless\nVector Search Collection\n(HNSW Index)")]
        
        S3 -->|Raw Text| Chunker
        Chunker -->|Text Chunks| EmbeddingModel
        EmbeddingModel -->|Vector + Text Chunks| VectorDB
    end
    
    subgraph QueryRuntime ["2. Grounded Inference Runtime"]
        UserQuery["User Query: 'What is the daily meal allowance?'"]
        BedrockKB["Amazon Bedrock Knowledge Base Engine"]
        LLM["Foundation Model (Amazon Nova Pro / Claude 3.5)"]
        FinalAnswer["Cited Grounded Response\n('Per Section 4.2: $75/day [1]')"]
        
        UserQuery --> BedrockKB
        BedrockKB -->|Vector Lookup (k-NN / BM25)| VectorDB
        VectorDB -->|Top-K Context Chunks| BedrockKB
        BedrockKB -->|Prompt + Context Chunks| LLM
        LLM --> FinalAnswer
    end
```

---

## 🛠️ Guided Step-by-Step Console Walkthrough

### Step 1: Create the Document Storage S3 Bucket
1. In the **AWS Management Console**, navigate to **Amazon S3** > **Create bucket**.
2. **Bucket name:** `aif-rag-knowledge-docs-[your-unique-suffix]`
3. **AWS Region:** Select `Europe (Stockholm) eu-north-1` (or `us-east-1`).
4. **Block Public Access:** Ensure **Block *all* public access** remains **checked**.
5. **Encryption:** Keep **Server-side encryption with Amazon S3 managed keys (SSE-S3)**.
6. Click **Create bucket**.

---

### Step 2: Author and Upload Sample Corporate Knowledge Documents
Create two sample policy documents on your local machine to test retrieval grounding:

#### Document 1: `travel_expense_policy.txt`
```text
ACME CORP GLOBAL TRAVEL & EXPENSE POLICY (REVISED 2026)

Section 1: Daily Meal Allowance
Employees traveling on official company business are eligible for a maximum daily meal per diem of $85 USD in Tier-1 cities (New York, London, Tokyo, Zurich) and $65 USD in all other standard locations. Alcohol is strictly non-reimbursable under corporate funds.

Section 2: Lodging Standards
Standard hotel bookings must not exceed $250 USD per night inclusive of local occupancy taxes, unless approved in writing by a Vice President. Bookings must be executed through the internal corporate travel portal at least 14 days in advance.

Section 3: Ground Transportation
Rideshare services (Uber, Lyft) are fully reimbursable for transit to and from airports and client offices. Premium luxury tiers (Uber Black) are not reimbursable.
```

#### Document 2: `remote_work_security_policy.txt`
```text
ACME CORP REMOTE WORK CYBERSECURITY MANDATE

Section 1: Mandatory Hardware
All remote employees must exclusively conduct company business on corporate-issued laptops equipped with full-disk BitLocker/FileVault encryption. Under no circumstances may personal desktop computers or tablets access the internal codebase or production customer databases.

Section 2: Network Access & VPN
Remote access to AWS VPC internal staging and production environments requires multi-factor authentication (MFA) via AWS IAM Identity Center and an active encrypted tunnel through AWS Client VPN. Public Wi-Fi networks in coffee shops or hotels must never be used without an active corporate VPN connection.
```

1. Navigate into your new S3 bucket `aif-rag-knowledge-docs-[your-unique-suffix]`.
2. Click **Upload** > Click **Add files** > Select both `.txt` files.
3. Click the orange **Upload** button.

---

### Step 3: Create the Amazon Bedrock Knowledge Base
Amazon Bedrock provides an automated wizard that provisions the vector store, creates IAM roles, configures chunking, and syncs your S3 data.

1. In the AWS Management Console, navigate to **Amazon Bedrock**.
2. In the left-hand navigation pane under **Builder tools**, select **Knowledge bases**.
3. Click the orange **Create knowledge base** button.
4. **Step 1: Provide knowledge base details:**
   - **Knowledge base name:** `AcmeCorporatePolicyKB`
   - **Description:** `Knowledge base containing corporate travel, expense, and remote work security policies.`
   - **IAM Permissions:** Select **Create and use a new service role** *(Bedrock will automatically configure an IAM role with `bedrock.amazonaws.com` trust and S3 read permissions)*.
   - Click **Next**.

5. **Step 2: Set up data source:**
   - **Data source name:** `AcmeS3PolicyDocs`
   - **S3 URI:** Click **Browse S3**, select your bucket `aif-rag-knowledge-docs-[your-unique-suffix]`, and click **Choose**.
   - Expand **Advanced settings** > **Chunking strategy**:
     - *Default chunking:* Chunks text to a maximum of 300 tokens with 20% overlap.
     - *Fixed-size chunking:* Manually specify chunk size and overlap percentage.
     - *Hierarchical chunking:* Splits into parent chunks (1,500 tokens) and child chunks (300 tokens) for high-precision retrieval with broad context.
     - *Semantic chunking:* Splits text based on natural thematic shifts using semantic sentence similarity.
     - Select **Default chunking** for this lab.
   - Click **Next**.

6. **Step 3: Select embeddings model and configure vector store:**
   - **Embeddings model:** Select **Titan Text Embeddings v2** (1,024 vector dimensions).
   - **Vector database:** Select **Quick create a new vector store - Recommended**.
     > [!NOTE]
     > **Under the Hood:** Bedrock automatically provisions an **Amazon OpenSearch Serverless** vector search collection (`bedrock-knowledge-base-...`), creates an HNSW index, configures the vector field mappings, and generates the required encryption, network, and data access security policies without manual intervention!
   - Click **Next**.

7. **Step 4: Review and create:**
   - Review your configuration and click **Create knowledge base**.
   - The provisioning process takes approximately 2–3 minutes as OpenSearch Serverless initializes.

---

### Step 4: Synchronize (Ingest) Data into the Vector Index
Creating the Knowledge Base defines the pipeline, but you must trigger an explicit **Sync** to chunk the files and generate vector embeddings.

1. Once the Knowledge Base status displays **Available**, locate the **Data source** table at the bottom.
2. Select `AcmeS3PolicyDocs` and click the orange **Sync** button.
3. Observe the sync status change from *In progress* to **Available**.
4. **What happened during Sync:**
   - Bedrock pulled the text files from S3.
   - It split the documents into 300-token chunks with 20% overlap.
   - It invoked `Titan Text Embeddings v2` to convert every text chunk into a 1,024-dimensional floating-point vector.
   - It wrote the vectors and raw chunk text into the OpenSearch Serverless vector collection.

---

### Step 5: Test Grounded Retrieval & Source Citations
1. In the Knowledge Base console, locate the **Test knowledge base** panel on the right side of the screen.
2. Under **Select model**, choose **Amazon Nova Pro** (or **Anthropic Claude 3.5 Sonnet**) and click **Apply**.
3. In the chat box, enter the following query:
   ```text
   Can I use an Uber to get from my hotel to the client office, and what is my meal budget in London?
   ```
4. Click **Run**.
5. **Inspect the Grounded Answer:**
   - The model responds: *"Yes, rideshare services like Uber are fully reimbursable for transit to client offices. For London (a Tier-1 city), your daily meal per diem is $85 USD [1]."*
6. **Inspect the Footnote Citation:**
   - Click on the footnote citation pill (e.g. `[1]`).
   - A drawer opens showing the **exact chunk text** retrieved from S3, the URI (`s3://.../travel_expense_policy.txt`), and the metadata.
7. **Negative Test (Preventing Hallucinations):**
   - In the chat box, ask:
     ```text
     What is the corporate policy regarding pet care reimbursements when traveling?
     ```
   - **Observation:** The model inspects the retrieved context, finds zero mention of pet care, and responds: *"Based on the provided documents, there is no corporate policy or provision regarding pet care reimbursements."*  
   - This demonstrates how **RAG prevents hallucinations** by constraining the model to authoritative source documents.

---

## 💻 Programmatic RAG Execution via AWS CLI v2

### Mode A: `retrieve` API (Vector Search Only - Returns Raw Chunks)
Use this when your custom application wants to handle prompt injection or reranking itself:

```bash
aws bedrock-agent-runtime retrieve \
  --knowledge-base-id "YOUR_KB_ID" \
  --retrieval-query '{"text": "What are the rules for public Wi-Fi networks?"}' \
  --retrieval-configuration '{
    "vectorSearchConfiguration": {
      "numberOfResults": 2
    }
  }' \
  --region eu-north-1 \
  --output json
```

#### Expected JSON Output Structure:
```json
{
    "retrievalResults": [
        {
            "content": {
                "text": "Public Wi-Fi networks in coffee shops or hotels must never be used without an active corporate VPN connection."
            },
            "location": {
                "type": "S3",
                "s3Location": {
                    "uri": "s3://aif-rag-knowledge-docs-xxxx/remote_work_security_policy.txt"
                }
            },
            "score": 0.8842
        }
    ]
}
```

### Mode B: `retrieve-and-generate` API (End-to-End Managed RAG)
Use this when you want Bedrock to retrieve the chunks, prompt the LLM, and return the synthesized cited answer in a single call:

```bash
aws bedrock-agent-runtime retrieve-and-generate \
  --input '{"text": "What is the maximum hotel rate allowed per night?"}' \
  --retrieve-and-generate-configuration '{
    "type": "KNOWLEDGE_BASE",
    "knowledgeBaseConfiguration": {
      "knowledgeBaseId": "YOUR_KB_ID",
      "modelArn": "arn:aws:bedrock:eu-north-1::foundation-model/amazon.nova-pro-v1:0"
    }
  }' \
  --region eu-north-1 \
  --output json
```

---

## 🎯 Exam Practice: Scenarios & Traps

| Exam Scenario | Correct Recommendation | Why Distractors Fail |
|---|---|---|
| *"An enterprise needs its internal chatbot to answer questions from HR documents that change daily, ensuring answers link back to the exact source PDF."* | **Amazon Bedrock Knowledge Bases (RAG)** | Fine-Tuning does not provide source citations, requires continuous retraining as policies change, and frequently hallucinates outdated facts. |
| *"A developer needs to combine dense semantic vector search with keyword matching (e.g. searching exact product model serial numbers) in a RAG pipeline."* | **Configure Hybrid Search (Dense Vectors + BM25 Lexical Matching)** | Standard vector search alone struggles with exact alphanumeric serial numbers or acronyms; Hybrid Search merges semantic meaning with exact keyword indexing. |
| *"When creating an OpenSearch Serverless collection manually for Bedrock Knowledge Bases, which three security policies are mandatory?"* | **Encryption Policy, Network Policy, and Data Access Policy** | Missing any of these three prevents Bedrock from creating indices or querying vectors. |
| *"An application requires extracting high-precision 200-token chunks for vector distance comparison, but needs to feed the entire 1,500-token surrounding section to the LLM for context."* | **Hierarchical Chunking (Parent-Child)** | Fixed-size chunking either makes chunks too large for accurate vector search or too small for comprehensive LLM context. |

---

## 🧹 Cost Safeguard & Cleanup (MANDATORY!)

> [!WARNING]
> **OpenSearch Serverless OCU Charges:** OpenSearch Serverless collections provision OpenSearch Compute Units (OCUs). If left running, an idle collection can incur charges of approximately \$0.24 per OCU-hour. **You must delete the knowledge base and vector collection immediately after testing!**

1. **Delete the Knowledge Base:**
   - In **Amazon Bedrock** > **Knowledge bases** > Select `AcmeCorporatePolicyKB` > Click **Delete**.
2. **Delete the OpenSearch Serverless Collection:**
   - Navigate to **Amazon OpenSearch Service** > **Serverless collections**.
   - Select the collection created for the knowledge base (`bedrock-knowledge-base-...`).
   - Click **Delete** and confirm deletion.
3. **Delete the S3 Bucket:**
   - Navigate to **Amazon S3** > Select `aif-rag-knowledge-docs-[your-unique-suffix]` > Click **Empty** > Confirm.
   - Click **Delete** to permanently remove the bucket.
