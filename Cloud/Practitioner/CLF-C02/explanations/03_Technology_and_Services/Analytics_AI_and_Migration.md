# AWS Analytics & Big Data — Map of Content (MOC)

> **Domain:** 03_Services / Analytics & Big Data  
> **Parent MOC:** [[AWS_Brain_MOC]]  
> **Certifications:** [[CLF-C02_Master_Blueprint|CLF-C02]], Data Analytics, Solutions Architect

---

## 💡 The Real-World Analogy (ELI5)

> **Big Data & Artificial Intelligence Factory:**
> - **Amazon Athena:** An interactive searchlight. Instead of importing millions of spreadsheets into a database, you shine a light directly at your files in Amazon S3 and run SQL queries immediately on demand.
> - **AWS Glue:** The automated data cleaning assembly line. It crawls messy data files, cataloging and transforming them so data analysts can use them (ETL — Extract, Transform, Load).
> - **Amazon EMR:** A fleet of giant industrial dump trucks running Apache Spark and Hadoop for massive distributed petabyte data processing.
> - **Amazon Bedrock:** An AI vending machine. You don't train massive multi-billion parameter neural networks yourself; you swipe your API card and get instant access to leading foundation models (Claude, Titan, Llama).

---

## 1. Architectural Taxonomy of AWS Analytics

AWS provides an end-to-end analytics stack covering the complete lifecycle: **Ingestion & Streaming**, **Data Lake & Catalogs**, **Data Warehousing**, **Big Data Frameworks**, **Interactive SQL**, **Log Analytics**, and **Business Intelligence**:

```mermaid
flowchart TD
    Analytics["AWS Analytics & Big Data Portfolio"]
    
    subgraph Streaming["1. Real-Time Streaming & Ingestion"]
        Kinesis["Amazon Kinesis (Data Streams, Firehose, Flink, Video)"]
    end
    
    subgraph Lake_ETL["2. Data Lake & Serverless ETL"]
        S3Lake["Amazon S3 (Central Data Lake Storage)"]
        Glue["AWS Glue (Data Catalog, Crawlers, Spark ETL)"]
    end
    
    subgraph Query_Engines["3. Query & Analytics Engines"]
        Athena["Amazon Athena (Serverless interactive SQL on S3)"]
        Redshift["Amazon Redshift (Petabyte MPP columnar data warehouse)"]
        EMR["Amazon EMR (Managed Spark, Hadoop, Presto, Hive clusters)"]
        OpenSearch["Amazon OpenSearch Service (Log search & dashboarding)"]
    end
    
    subgraph BI_Viz["4. Business Intelligence"]
        QuickSight["Amazon QuickSight (Serverless BI, SPICE engine, QuickSight Q)"]
    end
    
    Analytics --> Streaming
    Analytics --> Lake_ETL
    Analytics --> Query_Engines
    Analytics --> BI_Viz
```

---

## 2. Decision Matrix: Selecting Analytics Services

| Scenario / Need | Best AWS Service | Why |
| :--- | :--- | :--- |
| **Ad-hoc SQL queries on S3 files without servers** | **[[Amazon_Athena]]** | Serverless, pay per TB scanned, uses Glue schema. |
| **Complex analytical joins across enterprise historical data** | **[[Amazon_Redshift]]** | Columnar storage, MPP architecture, OLAP engine. |
| **Run Apache Spark, Hadoop, or Hive big data jobs** | **[[Amazon_EMR]]** | Managed distributed cluster nodes; Spot instance integration. |
| **Collect and process real-time clickstreams / IoT** | **[[Amazon_Kinesis]]** | Sub-second latency streaming ingestion; Firehose delivery. |
| **Discover metadata and automate serverless ETL** | **[[AWS_Glue]]** | Glue Data Catalog + automated schema inference crawlers. |
| **Operational log search and interactive heatmaps** | **[[Amazon_OpenSearch_Service]]** | Real-time indexing, full-text search, OpenSearch Dashboards. |
| **Executive financial dashboards with ML insights** | **[[Amazon_QuickSight]]** | In-memory SPICE calculations; natural language queries with Q. |

---

## 3. Atomic Notes in this Domain

| Atomic Note | Description | Key Focus / Keywords |
| :--- | :--- | :--- |
| **[[Amazon_Athena]]** | Serverless SQL Engine | Query S3 directly, pay per TB scanned, Parquet/ORC optimization. |
| **[[Amazon_EMR]]** | Managed Big Data Platform | Apache Spark, Hadoop, Hive, Presto, Master/Core/Task nodes. |
| **[[Amazon_Redshift]]** | Cloud Data Warehouse | OLAP, columnar storage, MPP, Redshift Spectrum, Serverless. |
| **[[Amazon_Kinesis]]** | Real-Time Streaming Data | Kinesis Data Streams (real-time) vs. Data Firehose (near real-time). |
| **[[AWS_Glue]]** | Serverless ETL & Metadata | Glue Data Catalog, Crawlers, Glue Studio, schema-on-read. |
| **[[Amazon_OpenSearch_Service]]** | Search & Log Analytics | OpenSearch / Elasticsearch, log indexing, OpenSearch Dashboards. |
| **[[Amazon_QuickSight]]** | Cloud Business Intelligence | SPICE engine, pay-per-session pricing, QuickSight Q natural language. |
---

## 7. Post-Topic Question Simulation & Retention Check

Test your understanding of Analytics, AI & Migration with these 5 exam-style questions:

## 🎯 Exam Traps & 'Clue-to-Answer' Trigger Words

| Exam Question Clue Keyword | Correct Service | Exam Trap Tip |
| :--- | :--- | :--- |
| *'Serverless interactive query service analyzing data directly in S3 with standard SQL'* | **Amazon Athena** | Pay only for bytes scanned by queries; no servers to manage. |
| *'Serverless Extract, Transform, and Load (ETL) and centralized Data Catalog'* | **AWS Glue** | Discovers data schema automatically via Glue Crawlers. |
| *'Serverless business intelligence (BI) dashboard and interactive data visualization'* | **Amazon QuickSight** | Pay-per-session pricing; ML-powered insights. |
| *'Real-time streaming data ingestion and processing at massive scale'* | **Amazon Kinesis** | Kinesis Data Streams / Data Firehose. |
| *'Build, train, and deploy custom machine learning models end-to-end'* | **Amazon SageMaker** | Comprehensive ML platform for data scientists. |
| *'Access leading foundation models via an API without managing infrastructure'* | **Amazon Bedrock** | Serverless Generative AI service. |
| *'Migrate on-premises physical, virtual, or cloud servers to AWS with minimal downtime'* | **AWS Application Migration Service (MGN)** | Continuous block-level data replication. |
| *'Migrate relational and NoSQL databases to AWS with zero downtime'* | **AWS Database Migration Service (DMS)** | Source database remains fully operational during migration. |

---

### Question 1
**Which serverless interactive query service allows analyzing data directly in Amazon S3 using standard SQL without needing to load or manage database infrastructure?**
- A) Amazon Redshift
- B) Amazon Athena
- C) Amazon EMR
- D) AWS Glue

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Amazon Athena**  
- **Why it's correct:** Amazon Athena is an interactive serverless query service that runs standard ANSI SQL queries directly against files (CSV, JSON, Parquet) stored in S3, charging strictly per TB of data scanned.
</details>

### Question 2
**Which AWS service provides choice of leading foundation models (Claude, Llama, Titan) via a single unified API without managing any underlying GPU infrastructure?**
- A) Amazon SageMaker Studio
- B) Amazon Bedrock
- C) Amazon Comprehend
- D) AWS Deep Learning AMIs

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Amazon Bedrock**  
- **Why it's correct:** Amazon Bedrock is the premier serverless foundation model service on AWS, providing API access to frontier generative AI models with built-in RAG (Knowledge Bases), Agents, and Guardrails.
</details>

### Question 3
**Which pre-trained AI service should an application use to detect sentiment, extract key phrases, and identify named entities in customer feedback emails without requiring custom machine learning models?**
- A) Amazon Rekognition
- B) Amazon Comprehend
- C) Amazon Transcribe
- D) Amazon Polly

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Amazon Comprehend**  
- **Why it's correct:** Amazon Comprehend is a pre-trained Natural Language Processing (NLP) service that automatically analyzes text to extract sentiment, entities, and language.
</details>

### Question 4
**Which migration strategy (from the 6 Rs) involves moving physical or virtual servers to AWS without any code or architectural changes ("Lift and Shift")?**
- A) Replatforming
- B) Rehosting
- C) Refactoring
- D) Repurchasing

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **B) Rehosting**  
- **Why it's correct:** Rehosting (Lift and Shift) moves applications directly to EC2 with zero code modifications, often automated using AWS Application Migration Service (AWS MGN).
</details>

### Question 5
**Which service provides a centralized collaborative hub to track migration progress across discovery, planning, server replication, and database migration?**
- A) AWS Migration Hub
- B) AWS Application Discovery Service
- C) AWS DMS
- D) AWS DataSync

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A) AWS Migration Hub**  
- **Why it's correct:** AWS Migration Hub provides a single location to track the progress of application migrations across AWS and partner tools (MGN, DMS).
</details>
