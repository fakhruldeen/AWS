# Module 02: ML Model Development — Knowledge Check

> **Track:** AWS Certified Machine Learning Engineer - Associate (MLA-C01)  
> **Module:** Module 2: Model Architecture Selection, PEFT/LoRA, Distributed Training & Tuning  
> **Format:** 10 Rapid Diagnostic Assessment Questions with Explanations

---

## 📌 Instructions
Complete this rapid diagnostic retention check after reviewing Domain 2 materials and completing Lab 04. Commit to an answer for each question before expanding the `<details>` dropdown.

---

### Question 1
An ML engineer is fine-tuning a 7-billion parameter Foundation Model for specialized financial document extraction. Due to budget constraints, the engineer cannot update all 7B parameters. Which technique allows updating only ~0.1% to 1% of total parameters by inserting trainable rank decomposition matrices?

- **A.** Low-Rank Adaptation (LoRA / PEFT)
- **B.** Full Supervised Retraining
- **C.** L1 Lasso Regularization
- **D.** Principal Component Analysis (PCA)

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**LoRA (Low-Rank Adaptation)** freezes the pre-trained model weights W₀ and decomposes the weight update ΔW into two low-rank matrices B × A. This slashes trainable parameters by >99%, avoids catastrophic forgetting, and produces tiny, portable adapter weights.
</details>

---

### Question 2
When training a deep neural network on a massive multi-terabyte image dataset across 16 multi-GPU EC2 `p4de.24xlarge` instances, each GPU holds a full copy of the model weights but processes a distinct slice of the training mini-batch. Gradients are synchronized across GPUs via AllReduce. Which distributed training strategy is this?

- **A.** Distributed Data Parallelism (DDP)
- **B.** Pipeline Model Parallelism
- **C.** Tensor Model Parallelism
- **D.** Single-threaded CPU Batching

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Data Parallelism (DDP)** replicates the entire model across all worker GPUs, partitions the training data across workers, and aggregates gradients across nodes at the end of each backward pass using efficient collective communications (Ring-AllReduce).
</details>

---

### Question 3
In which scenario is **Model Parallelism** (Tensor Parallelism or Pipeline Parallelism) strictly required instead of Data Parallelism?

- **A.** When the model size (parameters, activations, optimizer states) is too large to fit in the VRAM of a single GPU.
- **B.** When the training dataset has fewer than 100 rows.
- **C.** When training a simple decision tree on tabular data.
- **D.** When using serverless CPU endpoints.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
When a model has dozens or hundreds of billions of parameters (e.g., a 70B parameter model requiring >140 GB VRAM just for weights), it cannot fit into a single 80 GB GPU. **Model Parallelism** shards the model layers (Pipeline) or tensor matrices (Tensor) across multiple GPUs.
</details>

---

### Question 4
An ML engineer uses **Amazon SageMaker Automatic Model Tuning (Hyperparameter Optimization - HPO)**. Which search strategy is generally the most efficient for finding optimal hyperparameters in the fewest training jobs?

- **A.** Bayesian Optimization
- **B.** Random Search
- **C.** Grid Search
- **D.** Manual Trial and Error

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Bayesian Optimization** builds a probabilistic surrogate model (Gaussian Process) that treats hyperparameter tuning as a regression problem. It uses previous job evaluation results to intelligently select the next set of hyperparameters most likely to improve the objective metric.
</details>

---

### Question 5
Which metric is specifically designed to evaluate the factual overlap and recall between an LLM's generated summary and human ground-truth reference summaries?

- **A.** ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
- **B.** BLEU (Bilingual Evaluation Understudy)
- **C.** Mean Absolute Error (MAE)
- **D.** Adjusted R-Squared

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**ROUGE** evaluates text summarization by calculating n-gram and longest common subsequence (ROUGE-L) recall against human reference summaries. BLEU is primarily precision-oriented and used for machine translation.
</details>

---

### Question 6
An engineer trains an XGBoost model on Amazon SageMaker. During training, the training loss decreases consistently to near zero, while the validation loss begins increasing sharply after epoch 20. What is happening, and how should it be resolved?

- **A.** Overfitting; resolve by implementing **Early Stopping** (e.g., `early_stopping_rounds = 10`), increasing regularization, or reducing tree depth.
- **B.** Underfitting; resolve by training for 100 more epochs.
- **C.** Concept drift; resolve by upgrading the EC2 instance size.
- **D.** High bias; resolve by removing validation splits.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
When training loss drops while validation loss increases, the model has begun memorizing noise in the training set (**Overfitting**). Early stopping halts training as soon as the validation loss stops improving.
</details>

---

### Question 7
What is the mathematical formulation of the **F1-Score**, and why is it preferred over raw Accuracy for fraud detection models?

- **A.** $F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$; it represents the harmonic mean of precision and recall and is sensitive to class imbalance.
- **B.** F1 = Accuracy × MAE.
- **C.** F1 = True Positives / False Positives.
- **D.** F1 is only used for unsupervised clustering.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
In severely imbalanced datasets (e.g., 0.1% fraud), a model that predicts "Not Fraud" 100% of the time achieves 99.9% accuracy but 0.0 Recall and 0.0 F1. The harmonic mean forces both precision and recall to be high for a strong F1 score.
</details>

---

### Question 8
Which AWS managed service provides an interactive, collaborative workspace in Amazon SageMaker Studio for tracking machine learning experiments, comparing runs, visualizing loss curves, and organizing trials?

- **A.** Amazon SageMaker Experiments
- **B.** AWS CloudTrail
- **C.** Amazon S3 Glacier
- **D.** Amazon QuickSight

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
**Amazon SageMaker Experiments** automatically captures input parameters, configurations, and metric outputs for every training trial, allowing data scientists to organize, search, compare, and rank model training runs.
</details>

---

### Question 9
In Generative AI, what happens when you set the decoding parameter **Temperature to 0.0**?

- **A.** The model executes **Greedy Decoding**, always selecting the token with the highest probability, producing deterministic and repeatable output.
- **B.** The model generates random, nonsensical tokens.
- **C.** The model shuts down to reduce energy consumption.
- **D.** The context window increases by 50%.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
A Temperature of 0.0 eliminates randomness from the softmax probability distribution. The model greedily picks the argmax token, ensuring identical, deterministic responses for the same input prompt.
</details>

---

### Question 10
What is **Catastrophic Forgetting** in the context of foundation model customization?

- **A.** The phenomenon where fine-tuning a pre-trained model on a narrow domain causes it to overwrite and lose its general reasoning and language capabilities.
- **B.** An EC2 instance rebooting unexpectedly during training.
- **C.** Forgetting the root password to the AWS Management Console.
- **D.** Deleting an S3 training bucket.

<details>
<summary><b>Click to View Answer & Explanation</b></summary>

**Correct Answer:** **A**

**Explanation:**
Catastrophic forgetting occurs when a neural network fine-tuned on new task data experiences weight changes that overwrite previously learned general representations. PEFT / LoRA prevents this by freezing the base model weights.
</details>
