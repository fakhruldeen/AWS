# Diagram 01: Traditional Machine Learning vs. Generative AI Lifecycle

> **Architecture Blueprint:** `Diagram_01_Traditional_ML_vs_GenAI_Lifecycle.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 1 & Domain 2

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart TD
    subgraph TraditionalML["Traditional Predictive ML Lifecycle"]
        direction TB
        T1["1. Frame Problem\n(Classification / Regression)"] --> T2["2. Collect Labeled Data\n(S3 / Redshift / RDS)"]
        T2 --> T3["3. Feature Engineering\n(SageMaker Data Wrangler)"]
        T3 --> T4["4. Model Training & Tuning\n(SageMaker Training / HPO)"]
        T4 --> T5["5. Evaluation & Validation\n(Confusion Matrix, RMSE, AUC-ROC)"]
        T5 --> T6["6. Real-Time / Batch Hosting\n(SageMaker Endpoints)"]
        T6 --> T7["7. Monitor Data Drift\n(SageMaker Model Monitor)"]
        T7 -.->|"Retrain Trigger"| T2
    end

    subgraph GenAILifecycle["Generative AI Application Lifecycle"]
        direction TB
        G1["1. Frame Task & Modality\n(Text, Image, Multimodal)"] --> G2["2. Select Foundation Model\n(Bedrock Catalog / JumpStart)"]
        G2 --> G3["3. Prompt Engineering & Context\n(Zero/Few-Shot, System Prompts)"]
        G3 --> G4{"Is Base FM Accurate\n& Domain-Aware?"}
        
        G4 -- "Needs Real-Time / Private Data" --> G5["4A. Implement RAG\n(Bedrock Knowledge Bases)"]
        G4 -- "Needs Style / Domain Nomenclature" --> G6["4B. Parameter-Efficient Fine-Tuning\n(Bedrock Custom Models / LoRA)"]
        G4 -- "Yes (Task Solved)" --> G7["5. Multi-Layer Guardrails\n(Amazon Bedrock Guardrails)"]
        
        G5 --> G7
        G6 --> G7
        G7 --> G8["6. Deploy & Evaluate\n(Bedrock Model Evaluation / LLM-as-a-Judge)"]
        G8 --> G9["7. Enterprise Audit & Observability\n(CloudTrail, CloudWatch, Macie)"]
    end

    TraditionalML ~~~ GenAILifecycle
```

---

## 🔍 Core Architectural Highlights

1. **Data Dependency:** Traditional ML requires thousands of curated, task-specific ground-truth labeled examples. Generative AI leverages massive pre-trained Foundation Models with zero-to-few task-specific examples.
2. **Feature Engineering vs Prompt Engineering:** In classical ML, humans explicitly craft mathematical features (one-hot encoding, PCA). In GenAI, practitioners engineer textual context, schemas, and system directives.
3. **Adaptation Mechanisms:** While traditional ML requires complete retraining to adjust to new tasks, GenAI adapts via prompt engineering, RAG, or PEFT/LoRA without altering base transformer architectures.
