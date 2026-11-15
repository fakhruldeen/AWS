# Lab 11: Applied Document Intelligence with Amazon Textract, Comprehend & Bedrock

> **Course:** AWS Certified AI Practitioner (`AIF-C01`) Track  
> **Module:** Domain 1 & Domain 3: Multi-Service AI Applied Workloads  
> **Estimated Duration:** 45 minutes  
> **Cost / Free Tier:** Minimal pay-per-page / pay-per-token usage ($<\$0.10$)  
> **AWS Region:** `eu-north-1` (Stockholm) or `us-east-1` (N. Virginia)

---

## 🎯 Lab Objectives
By the end of this lab, you will be able to:
1. Extract structured forms and tabular data from invoices using **Amazon Textract**.
2. Perform Named Entity Recognition (NER) and PII detection with **Amazon Comprehend**.
3. Generate natural language executive summaries with **Amazon Bedrock (Nova Lite)**.
4. Execute document analysis using the AWS CLI v2.

---

## 🛠️ Step-by-Step Console Walkthrough

### Step 1: Extract Form Data and Tables with Amazon Textract
1. In the **AWS Management Console**, navigate to **Amazon Textract**.
2. In the left navigation menu, click **Analyze Document**.
3. Upload a sample invoice or receipt image (JPG/PNG or PDF).
4. Review the extracted tabs:
   * **Raw Text:** Extracted line-by-line optical character recognition.
   * **Forms:** Key-value pairs (e.g., `Invoice Number: INV-9041`, `Due Date: 2026-12-01`).
   * **Tables:** Structured grid containing line items, quantities, unit prices, and subtotals.

![Textract Form Extraction](images/lab11_step01_textract_form_extraction.png)

### Step 2: Detect PII and Named Entities with Amazon Comprehend
1. Navigate to **Amazon Comprehend** > **Real-time analysis**.
2. In the input box, paste the text extracted from Step 1.
3. Click **Analyze**.
4. Review the detection tabs:
   * **Entities:** Classifies words into `ORGANIZATION`, `PERSON`, `LOCATION`, `DATE`, `QUANTITY`.
   * **PII:** Detects confidential data such as bank account numbers, physical addresses, or tax IDs with confidence scores $>0.98$.
   * **Sentiment:** Classifies document sentiment (Neutral, Positive, Negative).

![Comprehend PII Detection](images/lab11_step02_comprehend_pii_detection.png)

### Step 3: Synthesize Executive Summary with Amazon Bedrock
1. Navigate to **Amazon Bedrock** > **Playgrounds** > **Chat**.
2. Select model **Amazon Nova Lite** (or **Anthropic Claude 3 Haiku**).
3. Paste the extracted invoice data and prompt:
   ```text
   Review this invoice data extracted via Textract:
   [PASTE EXTRACTED TEXT]
   
   Generate a brief executive bulleted summary highlighting:
   1. Total amount owed and payment terms.
   2. Identified vendor name and billing address.
   3. Flag any discrepancies or unusual line items.
   ```
4. Click **Run**. Observe how the foundation model converts fragmented OCR text into actionable business intelligence.

![Bedrock Summarization Output](images/lab11_step03_bedrock_summarization_output.png)

---

## 💻 AWS CLI v2 Runbook

Analyze a document directly via the AWS CLI:
```bash
aws textract analyze-document \
    --document '{"S3Object":{"Bucket":"your-doc-bucket","Name":"sample_invoice.pdf"}}' \
    --feature-types '["TABLES","FORMS"]'
```

---

## 🧹 Teardown & Clean-up
* Real-time console analyses in Textract, Comprehend, and Bedrock do not retain persistent state.
* Delete any temporary S3 test documents if created.
