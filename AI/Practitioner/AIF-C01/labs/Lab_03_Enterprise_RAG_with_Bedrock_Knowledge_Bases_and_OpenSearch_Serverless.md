# Lab 03: Enterprise RAG with Bedrock Knowledge Bases & OpenSearch Serverless

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 3: Applications of Foundation Models  
> **Estimated Duration:** 60 minutes  
> **Cost / Free Tier:** S3 minimal storage + Bedrock Knowledge Base queries ($<\$0.25$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Upload corporate policy documents to an encrypted **Amazon S3** bucket.
2. Provision an **Amazon OpenSearch Serverless** vector search collection.
3. Configure an **Amazon Bedrock Knowledge Base** with **Titan Text Embeddings v2**.
4. Sync and chunk unstructured text data automatically.
5. Query the knowledge base and verify response grounding and source citations.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Create the Document Ingestion Bucket in S3
1. In the **AWS Management Console**, navigate to **Amazon S3** > **Create bucket**.
2. **Bucket name:** `aif-rag-knowledge-docs-[your-unique-suffix]`
3. Keep default private settings (Block all public access enabled).
4. Click **Create bucket**.
5. Upload 2 sample text/PDF files (e.g., `remote_work_policy.txt` and `travel_expense_policy.txt`).

![S3 Document Bucket Overview](images/lab03_step01_s3_document_bucket.png)

### Step 2: Configure OpenSearch Serverless Vector Collection
1. Navigate to **Amazon OpenSearch Service** > **Serverless collections**.
2. Click **Create collection**:
   * Name: `aif-kb-vector-collection`
   * Type: **Vector search**
3. In Encryption settings, select **AWS owned key**.
4. In Network settings, allow access via Public or private endpoints.
5. In Data access policy, grant `aoss:*` to the current IAM principal. Click **Submit**.

![OpenSearch Serverless Collection](images/lab03_step02_aoss_vector_collection.png)

### Step 3: Create and Sync the Bedrock Knowledge Base
1. Navigate to **Amazon Bedrock** > **Knowledge bases** > **Create knowledge base**.
2. **Knowledge base details:**
   * Name: `CorporatePoliciesKB`
   * IAM Role: Allow Bedrock to create a new service role.
3. **Data source:**
   * Point to the S3 bucket created in Step 1.
   * Chunking: Choose **Default chunking** (300 tokens, 20% overlap).
4. **Embeddings Model:**
   * Select **Titan Text Embeddings v2**.
5. **Vector Database:**
   * Choose **Quick create a new vector store** (or select the OpenSearch Serverless collection from Step 2).
6. Click **Create knowledge base**.
7. Once created, click the orange **Sync** button in the Data sources table and wait until the status changes to **Available**.

![Knowledge Base Data Source Sync](images/lab03_step03_kb_data_source_sync.png)

### Step 4: Test Grounded Retrieval with Citations
1. In the Knowledge Base overview, locate the **Test knowledge base** pane on the right side.
2. Select foundation model: **Amazon Nova Pro** (or **Anthropic Claude 3.5 Sonnet**).
3. In the chat box, ask a question based on your uploaded document:
   ```text
   What is the maximum daily meal allowance for business travel?
   ```
4. Click **Run**.
5. Observe the response and click on the generated citation link (e.g., `[1]`). Verify that it displays the exact S3 chunk retrieved from your document.

![Knowledge Base Citations Test](images/lab03_step04_retrieval_citation_test.png)

---

## 💻 AWS CLI v2 Runbook

Query the knowledge base via the AWS CLI:
```bash
aws bedrock-agent-runtime retrieve \
    --knowledge-base-id YOUR_KB_ID \
    --retrieval-query '{"text": "What is the policy for daily meal expenses?"}' \
    --retrieval-configuration '{
        "vectorSearchConfiguration": {
            "numberOfResults": 3
        }
    }'
```

---

## 🧹 Teardown & Clean-up
1. In Amazon Bedrock, delete the Knowledge Base `CorporatePoliciesKB`.
2. In Amazon OpenSearch Service, delete the vector collection `aif-kb-vector-collection`.
3. In Amazon S3, empty and delete the bucket `aif-rag-knowledge-docs-[suffix]`.
