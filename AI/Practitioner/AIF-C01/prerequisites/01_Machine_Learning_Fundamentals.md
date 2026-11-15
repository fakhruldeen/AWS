# 01. Machine Learning Fundamentals Prerequisite

## 1. The Three Primary Paradigms of Machine Learning
1. **Supervised Learning:** Training data includes features (inputs) and ground-truth target labels (outputs).
   - *Classification:* Predicting discrete categories (e.g., fraud vs. legitimate transaction, spam vs. not spam).
   - *Regression:* Predicting continuous numerical values (e.g., house prices, customer lifetime value).
2. **Unsupervised Learning:** Data has no target labels; algorithms discover hidden patterns and groupings.
   - *Clustering:* Customer segmentation (e.g., K-Means in Amazon SageMaker).
   - *Dimensionality Reduction:* Compressing features (e.g., PCA).
3. **Reinforcement Learning (RL):** An agent interacts with an environment, learning an optimal policy via actions, states, and trial-and-error reward signals (e.g., AWS DeepRacer).

## 2. Model Evaluation Metrics
- **Classification:** Accuracy, Precision (avoiding false positives), Recall (avoiding false negatives), and F1-Score (harmonic mean of Precision & Recall).
- **Regression:** Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and $R^2$ score.
- **Overfitting vs. Underfitting:**
  - *Overfitting:* Model memorizes training noise and fails to generalize to test data (High Variance). Solved with regularization, dropout, more data.
  - *Underfitting:* Model is too simplistic to capture underlying relationships (High Bias). Solved by increasing model complexity or feature engineering.
