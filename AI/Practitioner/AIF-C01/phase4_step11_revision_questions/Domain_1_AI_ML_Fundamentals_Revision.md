# Domain 1 Revision Questions: Fundamentals of AI and ML

> **Domain:** Domain 1: Fundamentals of AI and Machine Learning (20% Exam Weight)  
> **Question Count:** 15 Comprehensive Scenario-Based Questions  
> **Format:** Multiple Choice & Multiple Response with Detailed Explanations

---

### Question 1
A retail company wants to forecast daily unit sales for 5,000 grocery items over the next quarter using historical sales logs, promotions, and local weather data. Which machine learning paradigm and AWS service is best suited for this task?
- [ ] A) Unsupervised Clustering with Amazon Rekognition
- [ ] B) Time-Series Regression with Amazon Forecast / SageMaker Canvas
- [ ] C) Binary Classification with Amazon Comprehend
- [ ] D) Reinforcement Learning with AWS DeepRacer
> **Correct Answer:** B  
> **Rationale:** Forecasting future continuous numeric units over time is a time-series regression task. Amazon Forecast and SageMaker Canvas provide automated algorithms for multi-variable time-series forecasting.

---

### Question 2
A machine learning engineer evaluates a customer credit default model. The model scores 99% accuracy on the training dataset, but drops to 61% accuracy on the test dataset. Which condition is the model experiencing, and what is an appropriate remedy?
- [ ] A) High Bias (Underfitting); decrease regularization and add more layers.
- [ ] B) High Variance (Overfitting); apply regularization (L1/L2), prune decision trees, and add more training data.
- [ ] C) Data poisoning; delete all negative labels.
- [ ] D) Cold-start latency; provision auto-scaling endpoints.
> **Correct Answer:** B  
> **Rationale:** High training accuracy paired with poor test generalization is the classic definition of overfitting (high variance). Remediation includes regularization, dropout, pruning, and collecting more data.

---

### Question 3
A hospital builds an AI model to detect malignant tumors from CT scans. The Chief Medical Officer insists that missing an actual tumor (False Negative) has catastrophic consequences, while a False Positive can be safely ruled out via follow-up biopsy. Which metric should the data science team optimize?
- [ ] A) Precision
- [ ] B) Recall (Sensitivity)
- [ ] C) Specificity
- [ ] D) Accuracy
> **Correct Answer:** B  
> **Rationale:** Recall equals $TP / (TP + FN)$. Maximizing Recall directly minimizes False Negatives, ensuring that positive disease cases are not missed.

---

### Question 4
An insurance firm needs to extract tabular expense line items and key-value fields from thousands of scanned PDF accident claim forms. Which AWS service accomplishes this without requiring the customer to train an ML model from scratch?
- [ ] A) Amazon Rekognition
- [ ] B) Amazon Textract
- [ ] C) Amazon Polly
- [ ] D) Amazon Transcribe
> **Correct Answer:** B  
> **Rationale:** Amazon Textract uses pre-trained computer vision and OCR models to extract structured forms, key-value pairs, and tables from scanned documents and PDFs.

---

### Question 5
A marketing manager wants to segment the company's customer base into distinct demographic and purchasing behavior groups. The customer database contains no predefined labels or purchase tags. Which technique should be applied?
- [ ] A) Supervised Binary Classification
- [ ] B) Unsupervised Clustering (e.g., K-Means)
- [ ] C) Supervised Polynomial Regression
- [ ] D) Reinforcement Learning with Policy Gradients
> **Correct Answer:** B  
> **Rationale:** Unsupervised learning algorithms like K-Means cluster data points based on geometric similarity without requiring ground-truth target labels.

---

### Question 6
Which tool in Amazon SageMaker Studio provides a visual data flow interface with hundreds of pre-built transforms to clean data, impute missing values, and balance datasets without coding?
- [ ] A) SageMaker Data Wrangler
- [ ] B) SageMaker Feature Store
- [ ] C) SageMaker Edge Manager
- [ ] D) SageMaker Model Monitor
> **Correct Answer:** A  
> **Rationale:** SageMaker Data Wrangler simplifies the process of data preparation and feature engineering from a single visual interface.

---

### Question 7
A telecommunications provider has an imbalanced dataset where only 2% of customers cancel their subscriptions (churn). If a simple model predicts that no customer will ever churn, what will the model's accuracy be, and why is accuracy a misleading metric here?
- [ ] A) Accuracy will be 50%; accuracy is misleading because it ignores regression loss.
- [ ] B) Accuracy will be 98%; accuracy is misleading because the model fails to identify any actual churners.
- [ ] C) Accuracy will be 2%; accuracy is misleading because it overweights minority classes.
- [ ] D) Accuracy will be 0%; accuracy cannot be calculated on binary datasets.
> **Correct Answer:** B  
> **Rationale:** On imbalanced datasets, a naive model predicting the majority class achieves high accuracy (98%) while providing zero predictive utility. The $F_1$-score or AUC-ROC should be used instead.

---

### Question 8
Which AWS AI service converts written text into lifelike natural speech across dozens of languages and diverse neural voices?
- [ ] A) Amazon Transcribe
- [ ] B) Amazon Polly
- [ ] C) Amazon Comprehend
- [ ] D) Amazon Translate
> **Correct Answer:** B  
> **Rationale:** Amazon Polly is a Text-to-Speech (TTS) service. Amazon Transcribe converts speech to text.

---

### Question 9
In the Machine Learning lifecycle, what is the key distinction between a model parameter and a hyperparameter?
- [ ] A) Parameters are configured manually before training; hyperparameters are learned from data.
- [ ] B) Parameters are internal variables learned by the algorithm during training; hyperparameters are external configuration settings specified prior to training.
- [ ] C) Parameters are used only in regression; hyperparameters are used only in classification.
- [ ] D) Parameters are stored in Amazon S3; hyperparameters are stored in AWS KMS.
> **Correct Answer:** B  
> **Rationale:** Parameters (such as neural network weights and bias terms) are optimized automatically during training. Hyperparameters (such as learning rate and batch size) are set by the engineer before training starts.

---

### Question 10
A call center records customer audio calls and wants to analyze customer sentiment and detect brand mentions. Which combination of AWS AI services provides an automated end-to-end pipeline?
- [ ] A) Amazon Rekognition followed by Amazon Polly
- [ ] B) Amazon Transcribe to convert speech to text, followed by Amazon Comprehend to analyze sentiment and entities
- [ ] C) Amazon Textract followed by Amazon Translate
- [ ] D) AWS DeepRacer followed by Amazon Kendra
> **Correct Answer:** B  
> **Rationale:** Amazon Transcribe converts call audio into text transcripts, and Amazon Comprehend extracts sentiment, key phrases, and brand entities from the transcripts.

---

### Question 11 (Multiple Response)
A data science team is preparing a tabular dataset for an XGBoost model. Which TWO feature engineering transformations are standard practice for handling categorical and numerical features? (Select TWO.)
- [ ] A) One-Hot Encoding for categorical nominal features with low cardinality
- [ ] B) Standardizing / Z-score normalization for numeric variables with vastly different scales
- [ ] C) Converting all numbers into raw audio waveforms
- [ ] D) Training a diffusion model to generate synthetic tabular labels
- [ ] E) Disabling validation splits during cross-validation
> **Correct Answers:** A, B  
> **Rationale:** One-Hot Encoding converts categorical variables into binary columns. Numeric feature scaling prevents features with large magnitudes from dominating gradient descent.

---

### Question 12
Which metric measures the proportion of predicted positive cases that were actually correct, making it critical for spam filters where legitimate emails must not be discarded?
- [ ] A) Precision
- [ ] B) Recall
- [ ] C) Mean Squared Error
- [ ] D) $R^2$
> **Correct Answer:** A  
> **Rationale:** $\text{Precision} = TP / (TP + FP)$. High precision minimizes False Positives (e.g., misclassifying an important email as spam).

---

### Question 13
What is the primary function of the Amazon SageMaker Feature Store?
- [ ] A) An online marketplace where third-party vendors sell trained models
- [ ] B) A centralized, secure repository to store, share, and discover curated ML features for training and low-latency inference
- [ ] C) A GPU cluster manager for PyTorch distributed training
- [ ] D) A billing management tool for tracking EC2 spot instances
> **Correct Answer:** B  
> **Rationale:** SageMaker Feature Store is a purpose-built repository where teams can ingest, discover, and reuse curated features across both batch training and real-time inference workloads.

---

### Question 14
A financial fraud model produces a Confusion Matrix with: $TP = 80$, $FP = 20$, $FN = 10$, $TN = 890$. What is the Precision of this model?
- [ ] A) 80% ($80 / 100$)
- [ ] B) 88.8% ($80 / 90$)
- [ ] C) 90% ($890 / 988$)
- [ ] D) 97% ($970 / 1000$)
> **Correct Answer:** A  
> **Rationale:** $\text{Precision} = TP / (TP + FP) = 80 / (80 + 20) = 80 / 100 = 0.80$ (80%).

---

### Question 15
Which machine learning paradigm involves an agent learning an optimal policy by interacting with an environment through states, actions, and scalar rewards?
- [ ] A) Supervised Learning
- [ ] B) Unsupervised Learning
- [ ] C) Reinforcement Learning
- [ ] D) Semi-Supervised Learning
> **Correct Answer:** C  
> **Rationale:** Reinforcement learning is centered around an agent exploring an environment to maximize cumulative reward through a learned policy.
