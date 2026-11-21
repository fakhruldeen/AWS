# Diagram 06: Model Customization Spectrum (Prompt to Pre-Training)

> **Architecture Blueprint:** `Diagram_06_Model_Customization_Spectrum_Prompt_to_Pretraining.md`  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Domain Alignment:** Domain 3 (Applications of Foundation Models)

---

## 🏛️ Architectural Blueprint

```mermaid
flowchart LR
    subgraph Spectrum["The Model Customization Continuum"]
        direction LR
        P1["1. Prompt Engineering\n- Zero / Few-Shot\n- No training data\n- Cost: $ (Lowest)\n- Time: Minutes"] --> P2["2. Retrieval Augmented Generation\n- Dynamic grounding on S3 docs\n- Vector search (OpenSearch)\n- Cost: $$\n- Time: Hours / Days"]
        P2 --> P3["3. Fine-Tuning (PEFT / LoRA)\n- Adjusts adapter weights (<1%)\n- Domain tone & JSON output\n- Cost: $$$\n- Time: Days"]
        P3 --> P4["4. Continued Pre-Training\n- Unlabeled domain corpora\n- Expands vocabulary & knowledge\n- Cost: $$$$\n- Time: Weeks"]
        P4 --> P5["5. Full Pre-Training from Scratch\n- Billions of tokens on Trainium\n- Novel base foundation model\n- Cost: $$$$$\n- Time: Months"]
    end
```

---

## 🔍 Core Architectural Highlights

| Customization Strategy | Model Weights Altered? | Primary Data Requirement | AWS Implementation | Best Used For |
|---|---|---|---|---|
| **Prompt Engineering** | No (0%) | Context examples | Bedrock Prompt Management | General reasoning, format adherence, Q&A |
| **RAG** | No (0%) | Unstructured text documents | Bedrock Knowledge Bases | Private enterprise data grounding |
| **Fine-Tuning (LoRA)** | Adapter weights only (<1%) | Labeled $(Prompt, Completion)$ pairs | Bedrock Custom Models | Custom tone, industry jargon, strict schema output |
| **Continued Pre-Training** | All weights modified incrementally | Large unlabeled text corpus | Bedrock Custom Models / SageMaker | Novel terminology, non-English language adaptation |
| **Full Pre-Training** | All weights initialized randomly | Trillions of diverse tokens | AWS Trainium / EC2 UltraClusters | Creating proprietary foundation models |
