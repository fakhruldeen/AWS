# Module 01 Knowledge Check: Fundamentals of AI and ML

> **Domain:** Domain 1: Fundamentals of AI and Machine Learning (20% Weight)  
> **Questions:** 10 Diagnostic Questions with Answers & Rationales

---

### Questions

1. **Which machine learning paradigm is used to predict continuous numerical values, such as future sales revenue?**
   - A) Binary Classification
   - B) Regression
   - C) Clustering
   - D) Dimensionality Reduction

2. **What occurs when a model performs exceptionally well on training data but poorly on unseen test data?**
   - A) Underfitting (High Bias)
   - B) Overfitting (High Variance)
   - C) Data leakage
   - D) Cold-start latency

3. **Which SageMaker capability allows business analysts to build ML models using a visual drag-and-drop interface without writing Python code?**
   - A) SageMaker Canvas
   - B) SageMaker JumpStart
   - C) SageMaker Clarify
   - D) SageMaker Model Cards

4. **Which AWS service automatically converts spoken audio into written text?**
   - A) Amazon Polly
   - B) Amazon Transcribe
   - C) Amazon Comprehend
   - D) Amazon Rekognition

5. **Which evaluation metric is most critical when evaluating a cancer diagnostic model where missing a positive case is life-threatening?**
   - A) Precision
   - B) Recall (Sensitivity)
   - C) Specificity
   - D) Accuracy

6. **A company needs to extract structured form key-value pairs and tabular data from scanned PDF invoices without manual labeling. Which service is optimal?**
   - A) Amazon Rekognition
   - B) Amazon Textract
   - C) Amazon Comprehend
   - D) Amazon Translate

7. **In a customer segmentation project, a data scientist wants to group customers into clusters based on purchasing behavior without predefined labels. Which learning paradigm applies?**
   - A) Supervised Learning
   - B) Unsupervised Learning
   - C) Semi-Supervised Learning
   - D) Reinforcement Learning

8. **Which SageMaker feature provides a visual data preparation tool with over 300 built-in transformations to handle missing data and outliers?**
   - A) SageMaker Studio Lab
   - B) SageMaker Data Wrangler
   - C) SageMaker Feature Store
   - D) SageMaker Edge Manager

9. **In the Confusion Matrix, what does a "False Positive" (Type I Error) represent?**
   - A) An actual positive instance correctly predicted as positive
   - B) An actual negative instance incorrectly predicted as positive
   - C) An actual positive instance incorrectly predicted as negative
   - D) An actual negative instance correctly predicted as negative

10. **Which metric is the harmonic mean of Precision and Recall, providing a balanced evaluation on imbalanced datasets?**
    - A) AUC-ROC
    - B) F1-Score
    - C) Mean Squared Error (MSE)
    - D) R-squared (R²)

---

### Answer Key & Explanations

| Q# | Answer | Key Concept Reference | Detailed Explanation |
|:---:|:---:|:--- |:--- |
| **1** | **B** | Regression | Regression models output continuous quantitative values (sales, temperature, prices). Classification predicts discrete categories. |
| **2** | **B** | Overfitting | Overfitting occurs when a model memorizes noise in the training set and fails to generalize to out-of-sample data. |
| **3** | **A** | SageMaker Canvas | SageMaker Canvas is AWS's no-code visual AutoML workspace designed for business analysts. |
| **4** | **B** | Amazon Transcribe | Amazon Transcribe converts speech audio streams or recordings into text. Polly converts text to speech. |
| **5** | **B** | Recall (Sensitivity) | Recall measures $TP / (TP + FN)$. Maximizing recall minimizes False Negatives (missed diagnoses). |
| **6** | **B** | Amazon Textract | Textract goes beyond basic OCR by extracting structured forms and tables from documents. |
| **7** | **B** | Unsupervised Learning | Unsupervised clustering groups unlabelled data instances based on geometric proximity without ground truth targets. |
| **8** | **B** | SageMaker Data Wrangler | Data Wrangler provides a visual point-and-click interface for cleaning, transforming, and analyzing tabular/image data. |
| **9** | **B** | Type I Error | A False Positive occurs when the model predicts positive, but the actual true ground state is negative (e.g., flagging valid email as spam). |
| **10** | **B** | F1-Score | The F1-score balances Precision and Recall: $2 \times (\text{Precision} \times \text{Recall}) / (\text{Precision} + \text{Recall})$. |
