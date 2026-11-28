# Domain 1: Fundamentals of AI and ML (`20%` of Scored Content)

> **Official Blueprint:** AWS Certified AI Practitioner (`AIF-C01`) Exam Guide v1.2 (Oct 29, 2026)  
> **Scored Questions (~50 scored total):** ~10 scored questions (~13 in a 65-question full mock)

---

## Task Statement 1.1: Explain basic AI concepts and terminologies
- **Core Terms:** AI, ML, Deep Learning, Neural Networks, Computer Vision, Natural Language Processing (`NLP`), Model, Algorithm, Training vs. Inferencing, Bias, Fairness, Fit (`Overfitting` / `Underfitting`), Large Language Model (`LLM`), Generative AI (`GenAI`), **Agentic AI**.
- **Hierarchy & Distinctions:** Similarities and differences between `AI`, `ML`, `GenAI`, `Deep Learning`, and `Agentic AI`.
- **Inferencing Types:** `Real-Time`, `Batch`, `Asynchronous`, and `Serverless` inference (latency, payload size, traffic pattern tradeoffs).
- **Data Types:** Labeled vs. Unlabeled; Tabular, Time-Series, Image, Text; Structured vs. Unstructured.
- **Learning Paradigms:** `Supervised` (Classification, Regression), `Unsupervised` (Clustering, Dimensionality Reduction, Anomaly Detection), and `Reinforcement Learning` (Agent, Environment, Policy, Rewards/Penalties).

## Task Statement 1.2: Identify practical use cases for AI
- **High-Value AI Applications:** Assisting human decision-making, scalability, automation (Computer Vision, NLP, Speech Recognition, Recommendations, Fraud Detection, Forecasting, Knowledge Bases, Agentic AI).
- **When AI/ML Is NOT Appropriate:** Cost-benefit unfavorable, deterministic exact outcome required instead of probabilistic prediction (e.g., fixed accounting/tax rules), or insufficient/poor-quality data.
- **AWS Managed AI/ML Services:** `Amazon SageMaker AI`, `Amazon Transcribe`, `Amazon Translate`, `Amazon Comprehend`, `Amazon Lex`, `Amazon Polly`, `Amazon Rekognition`, `Amazon Textract`, `Amazon Personalize`.
- **Traditional ML vs. Foundation Models (`FMs`):** Choose traditional ML (e.g., XGBoost, linear regression) for structured tabular data, strict regulatory explainability, or low compute cost; choose FMs for unstructured text/multimodal generation and broad reasoning.

## Task Statement 1.3: Describe the AI/ML development lifecycle
- **Pipeline Stages:** Problem Framing → Data Collection & Preparation → Feature Engineering → Model Training & Tuning → Evaluation → Deployment → Monitoring & Retraining.
- **Model Sources & Production Hosting:** Open-source pre-trained models vs. custom trained models; Managed API services (`Amazon Bedrock`) vs. self-hosted APIs (`SageMaker AI`, `ECS`/`EKS`).
- **AWS Pipeline Services (v1.2):** `Amazon Bedrock`, **`Amazon Quick`**, **`Kiro`**, `Amazon SageMaker AI` (`Data Wrangler`, `Ground Truth`, `Pipelines`, `Model Monitor`, `Model Registry`).
- **MLOps Fundamentals:** Experimentation tracking, repeatable pipelines, scalable systems, managing technical debt, production readiness, drift monitoring, automated retraining.
- **Evaluation & Business Metrics:** Model metrics (`Accuracy`, `Precision`, `Recall`, `F1 Score`, `AUC-ROC`, `RMSE`, `MAE`) vs. Business metrics (`Cost per user`, `Development costs`, `Customer feedback`, `ROI`).
