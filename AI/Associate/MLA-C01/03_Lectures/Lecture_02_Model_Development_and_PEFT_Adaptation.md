# Lecture 02: ML Model Development, Distributed Training & PEFT

> **Course Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Domain 2: ML Model and Foundation Model (FM) Development (26%)  
> **Instructor Delivery Plan & Talking Points**  
> **Target Duration:** 60 minutes

---

## 🎯 Learning Objectives

By the end of this lecture, candidates will be able to:
1. Select the right machine learning algorithm on Amazon SageMaker based on data type and business goal.
2. Formulate and execute Parameter-Efficient Fine-Tuning (PEFT / LoRA) for Large Language Models.
3. Understand distributed training architectures (Distributed Data Parallelism vs. Model Parallelism).
4. Configure Bayesian Hyperparameter Optimization (HPO) and evaluate models across classification, regression, and GenAI metrics.

---

## ⏱️ Lecture Timeline & Delivery Outline

```
[00:00 - 01:15] 1. SageMaker Built-in Algorithms (XGBoost, Linear Learner, DeepAR, RCF)
[01:15 - 02:45] 2. Foundation Model Adaptation Spectrum: Prompt vs. RAG vs. Fine-Tuning
[02:45 - 04:15] 3. Mathematics & Mechanics of PEFT / LoRA (Low-Rank Decomposition)
[04:15 - 05:15] 4. Distributed Training at Scale (Data Parallelism vs. Model Parallelism)
[05:15 - 06:00] 5. Metric Evaluation (Precision/Recall, AUC, ROUGE, BLEU, BERTScore)
```

---

## 🗣️ Instructor Talking Points & Whiteboard Guidance

### 1. The Algorithm Selection Procedure
- **Tabular Classification & Regression:** **XGBoost** is the undisputed workhorse for tabular structured data.
- **Time-Series Forecasting:** **DeepAR** handles multiple related time-series with neural networks; **Amazon Forecast** for fully managed auto-ML forecasting.
- **Anomaly Detection:** **Random Cut Forest (RCF)** for unsupervised anomaly detection in streaming time-series.
- **Topic Modeling & Document Grouping:** **LDA (Latent Dirichlet Allocation)** or **NTM (Neural Topic Model)**.

### 2. The Customization Spectrum & LoRA Mechanics
- *Whiteboard Equation:*

  $$
  W = W_0 + \Delta W = W_0 + B \times A
  $$

- **Explain LoRA:**
  - W₀ is the multi-gigabyte frozen foundation model weights.
  - $A$ (Gaussian init) and $B$ (Zero init) are low-rank matrices where rank $r$ is tiny (r=8 or r=16).
  - Trainable parameters drop from 7,000,000,000 to ~7,000,000 (99.9% reduction!).
  - **Catastrophic Forgetting:** Explain why freezing W₀ completely protects the base model's general common-sense and grammar knowledge.

### 3. Distributed Training: DDP vs. Model Parallelism
- **Data Parallelism (DDP):**
  - Model fits on 1 GPU.
  - Replicate model across $N$ GPUs.
  - Split training data. Synchronize gradients via Ring-AllReduce.
- **Model Parallelism:**
  - Model DOES NOT fit on 1 GPU (e.g., Llama 70B requiring 140 GB VRAM).
  - Must shard layers across GPUs (Pipeline Parallelism) or shard matrix multiplication across GPUs (Tensor Parallelism).

---

## 💻 Classroom Live Demo Walkthrough (5 Minutes)

1. Show a SageMaker Training Job configuration in the console.
2. Demonstrate how Managed Spot Training with S3 checkpointing cuts training costs by up to 70%:
   ```python
   estimator = Estimator(
       image_uri=xgboost_image,
       instance_type="ml.m5.2xlarge",
       use_spot_instances=True,
       max_wait=3600,
       checkpoint_s3_uri="s3://my-bucket/checkpoints/"
   )
   ```

---

## 🎯 High-Yield Exam Traps for this Lecture

1. **Trap:** Fine-tuning an LLM to add daily stock prices or real-time news.  
   *Correction:* Use **RAG** (Bedrock Knowledge Bases). Fine-tuning is for tone, style, and formatting, not daily dynamic facts.
2. **Trap:** Forgetting S3 checkpointing when enabling Managed Spot Training.  
   *Correction:* Without checkpointing, an EC2 Spot interruption will cause the training job to restart from epoch 0.
