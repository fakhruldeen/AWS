# 🏆 AWS Certified AI Practitioner (`AIF-C01`) — Top 300 Most Frequent & High-Yield Exam Questions

> **Blueprint Alignment:** Official Exam Guide v1.2 (October 29, 2026)  
> **Selection Methodology:** Ranked by multi-source cross-consensus frequency across verified community pools + v1.2 official blueprint updates, balanced proportionally to exam domain weights (`D1: 20%`, `D2: 24%`, `D3: 28%`, `D4: 14%`, `D5: 14%`).

---

## Domain 1: Fundamentals of AI and ML (20% — 60 Questions)

### Q1.01 (`AIF-U0001`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company has built an image classification model to predict plant diseases from photos of plant leaves. The company wants to evaluate how many images the model classified correctly.Which evaluation metric should the company use to measure the model ' s performance?

- A) R-squared score
- B) Accuracy
- C) Root mean squared error (RMSE)
- D) Learning rate

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Accuracy is the most appropriate metric to measure the performance of an image classification model. It indicates the percentage of correctly classified images out of the total number of images. In the context of classifying plant diseases from images, accuracy will help the company determine how well the model is performing by showing how many images were correctly classified.Option B (Correct): " Accuracy " : This is the correct answer because accuracy measures the proportion of correct predictions made by the model, which is suitable for evaluating the performance of a classification model.Option A: " R-squared score " is incorrect as it is used for regression analysis, not classification tasks.Option C: " Root mean squared error (RMSE) " is incorrect because it is also used for regression tasks to measure prediction errors, not for classification accuracy.Option D: " Learning rate " is incorrect as it is a hyperparameter for training, not a performance metric.AWS AI Practitioner References:Evaluating Machine Learning Models on AWS: AWS documentation emphasizes the use of appropriate metrics, like accuracy, for classification tasks.

</details>

### Q1.02 (`AIF-U0004`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company wants to build an ML model to detect abnormal patterns in sensor data. The company does not have labeled data for training. Which ML method will meet these requirements?

- A) Linear regression
- B) Classification
- C) Decision tree
- D) Autoencoders

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** The correct answer is D because autoencoders are an unsupervised machine learning method commonly used for anomaly detection when labeled data is not available.From AWS documentation:" Autoencoders learn to compress and reconstruct input data. During anomaly detection, they learn normal patterns in data. Data points that the model cannot accurately reconstruct are flagged as anomalies. "This approach is ideal when there is no labeled data and when patterns must be learned based on normal behavior alone — a common situation in IoT sensor data environments.Explanation of other options:A. Linear regression requires labeled data and is used for predicting continuous values.B. Classification requires labeled data to assign inputs into categories.C. Decision trees are supervised learning models and also require labeled datasets.Referenced AWS AI/ML Documents and Study Guides:AWS Machine Learning Specialty Guide – Unsupervised Learning TechniquesAmazon SageMaker Examples – Anomaly Detection Using Autoencoders

</details>

### Q1.03 (`AIF-U0006`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> A food service company wants to develop an ML model to help decrease daily food waste and increase sales revenue. The company needs to continuously improve the model ' s accuracy.Which solution meets these requirements?

- A) Use Amazon SageMaker AI and iterate with the most recent data.
- B) Use Amazon Personalize and iterate with historical data.
- C) Use Amazon CloudWatch to analyze customer orders.
- D) Use Amazon Rekognition to optimize the model.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon SageMaker is AWS’s fully managed ML service that supports retraining and deploying models with new, recent data for continuous improvement. This directly meets the requirement to iterate and continuously improve model accuracy.A is correct:" Amazon SageMaker enables teams to retrain models using the most recent data, ensuring ongoing improvement in model accuracy. "(Reference: Amazon SageMaker Overview)B (Amazon Personalize) is for recommendations, not general ML or waste reduction.C (CloudWatch) is for monitoring, not ML training or deployment.D (Rekognition) is for image/video analysis.

</details>

### Q1.04 (`AIF-U0003`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company wants to build a lead prioritization application for its employees to contact potential customers. The application must give employees the ability to view and adjust the weights assigned to different variables in the model based on domain knowledge and expertise.Which ML model type meets these requirements?

- A) Logistic regression model
- B) Deep learning model built on principal components
- C) K-nearest neighbors (k-NN) model
- D) Neural network

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** A logistic regression model is a simple, interpretable machine learning model that allows users to adjust the weights of different variables based on domain knowledge and expertise. Since logistic regression is based on a linear relationship between the input features and the predicted outcome, each feature has a corresponding weight (coefficient) that can be easily viewed and adjusted. This makes it a suitable choice for a lead prioritization application where domain experts need the ability to modify the model based on their knowledge.

</details>

### Q1.05 (`AIF-U0007`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> Sentiment analysis is a subset of which broader field of AI?

- A) Computer vision
- B) Robotics
- C) Natural language processing (NLP)
- D) Time series forecasting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Sentiment analysis is the task of determining the emotional tone or intent behind a body of text (positive, negative, neutral).This falls under Natural Language Processing (NLP) because it deals with understanding and processing human language.Computer vision relates to images, robotics to autonomous machines, and time series forecasting to predicting values from sequential data.???? Reference:AWS ML Glossary – NLP

</details>

### Q1.06 (`AIF-U0005`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company wants to develop an educational game where users answer questions such as the following: "A jar contains six red, four green, and three yellow marbles. What is the probability of choosing a green marble from the jar?" Which solution meets these requirements with the LEAST operational overhead?

- A) Use supervised learning to create a regression model that will predict probability.
- B) Use reinforcement learning to train a model to return the probability.
- C) Use code that will calculate probability by using simple rules and computations.
- D) Use unsupervised learning to create a model that will estimate probability density.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Calculating probability in this scenario involves straightforward arithmetic, making it most efficient to use simple rules and computations. This approach requires the least operational overhead compared to using complex ML models, which are unnecessary for such basic tasks.

</details>

### Q1.07 (`AIF-U0002`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company is using domain-specific models. The company wants to avoid creating new models from the beginning. The company instead wants to adapt pre-trained models to create models for new, related tasks. Which ML strategy meets these requirements?

- A) Increase the number of epochs.
- B) Use transfer learning.
- C) Decrease the number of epochs.
- D) Use unsupervised learning.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Transfer learning allows the company to adapt pre-trained models for new, related tasks, saving time and resources compared to training models from scratch. The other options do not address the goal of reusing existing models.

</details>

### Q1.08 (`AIF-U0018`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company wants to display the total sales for its top-selling products across various retail locations in the past 12 months.Which AWS solution should the company use to automate the generation of graphs?

- A) Amazon Q in Amazon EC2
- B) Amazon Q Developer
- C) Amazon Q in Amazon QuickSight
- D) Amazon Q in AWS Chatbot

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon QuickSight is a fully managed business intelligence (BI) service that allows users to create and publish interactive dashboards that include visualizations like graphs, charts, and tables. " Amazon Q " is the natural language query feature within Amazon QuickSight. It enables users to ask questions about their data in natural language and receive visual responses such as graphs.Option C (Correct): " Amazon Q in Amazon QuickSight " : This is the correct answer because Amazon QuickSight Q is specifically designed to allow users to explore their data through natural language queries, and it can automatically generate graphs to display sales data and other metrics. This makes it an ideal choice for the company to automate the generation of graphs showing total sales for its top-selling products across various retail locations.Option A, B, and D: These options are incorrect:A. Amazon Q in Amazon EC2: Amazon EC2 is a compute service that provides virtual servers, but it is not directly related to generating graphs or providing natural language querying features.B. Amazon Q Developer: This is not an existing AWS service or feature.D. Amazon Q in AWS Chatbot: AWS Chatbot is a service that integrates with Amazon Chime and Slack for monitoring and managing AWS resources, but it is not used for generating graphs based on sales data.AWS AI Practitioner References:Amazon QuickSight Q is designed to provide insights from data by using natural language queries, making it a powerful tool for generating automated graphs and visualizations directly from queried data.Business Intelligence (BI) on AWS: AWS services such as Amazon QuickSight provide business intelligence capabilities, including automated reporting and visualization features, which are ideal for companies seeking to visualize data like sales trends over time.

</details>

### Q1.09 (`AIF-U0023`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A manufacturing company wants to create product descriptions in multiple languages.Which AWS service will automate this task?

- A) Amazon Translate
- B) Amazon Transcribe
- C) Amazon Kendra
- D) Amazon Polly

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_speech_transcribe_polly`  
**Explanation:** The manufacturing company needs to create product descriptions in multiple languages, which requires automated language translation. Amazon Translate is a fully managed service that uses machine learning to provide high-quality translation between languages, making it the ideal solution for this task.Exact Extract from AWS AI Documents:From the Amazon Translate Developer Guide:" Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable language translation. It can be used to automatically translate text, such as product descriptions, into multiple languages to reach a global audience. "(Source: Amazon Translate Developer Guide, Introduction to Amazon Translate)Detailed Explanation:Option A: Amazon TranslateThis is the correct answer. Amazon Translate automates the translation of text into multiple languages, directly addressing the company’s need to create product descriptions in different languages.Option B: Amazon TranscribeAmazon Transcribe converts speech to text, which is unrelated to translating text into multiple languages. This option is incorrect.Option C: Amazon KendraAmazon Kendra is an intelligent search service that uses machine learning to provide answers from documents, not for translating text. This option is irrelevant.Option D: Amazon PollyAmazon Polly is a text-to-speech service that generates spoken audio from text, not for translating text into other languages. This option does not meet the requirements.

</details>

### Q1.10 (`AIF-U0025`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> An ecommerce company wants to improve search engine recommendations by customizing the results for each user of the company ' s ecommerce platform. Which AWS service meets these requirements?

- A) Amazon Personalize
- B) Amazon Kendra
- C) Amazon Rekognition
- D) Amazon Transcribe

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** The ecommerce company wants to improve search engine recommendations by customizing results for each user. Amazon Personalize is a machine learning service that enables personalized recommendations, tailoring search results or product suggestions based on individual user behavior and preferences, making it the best fit for this requirement.Exact Extract from AWS AI Documents:From the Amazon Personalize Developer Guide:" Amazon Personalize enables developers to build applications with personalized recommendations, such as customized search results or product suggestions, by analyzing user behavior and preferences to deliver tailored experiences. "(Source: Amazon Personalize Developer Guide, Introduction to Amazon Personalize)Detailed Explanation:Option A: Amazon PersonalizeThis is the correct answer. Amazon Personalize specializes in creating personalized recommendations, ideal for customizing search results for each user on an ecommerce platform.Option B: Amazon KendraAmazon Kendra is an intelligent search service for enterprise data, focusing on retrieving relevant documents or answers, not on personalizing search results for individual users.Option C: Amazon RekognitionAmazon Rekognition is for image and video analysis, such as object detection or facial recognition, and is unrelated to search engine recommendations.Option D: Amazon TranscribeAmazon Transcribe converts speech to text, which is not relevant for improving search engine recommendations.

</details>

### Q1.11 (`AIF-U0012`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> A company is training ML models on datasets. The datasets contain some classes that have more examples than other classes. The company wants to measure how well the model balances detecting and labeling the classes. Which metric should the company use?

- A) Accuracy
- B) Recall
- C) Precision
- D) F1 score

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The F1 score is the harmonic mean of precision and recall, making it the most appropriate metric for imbalanced datasets because it penalises models that perform well on one measure but poorly on the other, ensuring the model genuinely balances both detecting all instances of a class and labeling them correctly across all classes. Accuracy measures the overall percentage of correct predictions but is misleading on imbalanced datasets because a model that always predicts the majority class can achieve high accuracy while completely failing to detect minority classes. Recall measures how well the model detects all actual instances of each class, capturing the ability to find true positives, but it ignores the rate of false positives and so does not reflect how well the model balances detection and correct labeling simultaneously. Precision measures how often a positive prediction is actually correct but ignores false negatives, meaning a model that makes very few predictions can achieve high precision while missing most of the actual instances in underrepresented classes.

</details>

### Q1.12 (`AIF-U0008`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company has built a chatbot that can respond to natural language questions with images. The company wants to ensure that the chatbot does not return inappropriate or unwanted images.Which solution will meet these requirements?

- A) Implement moderation APIs.
- B) Retrain the model with a general public dataset.
- C) Perform model validation.
- D) Automate user feedback integration.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Moderation APIs, such as Amazon Rekognition’s Content Moderation API, can help filter and block inappropriate or unwanted images from being returned by a chatbot. These APIs are specifically designed to detect and manage undesirable content in images.Option A (Correct): " Implement moderation APIs " : This is the correct answer because moderation APIs are designed to identify and filter inappropriate content, ensuring the chatbot does not return unwanted images.Option B: " Retrain the model with a general public dataset " is incorrect because retraining does not directly prevent inappropriate content from being returned.Option C: " Perform model validation " is incorrect as it ensures model correctness, not content moderation.Option D: " Automate user feedback integration " is incorrect because user feedback does not prevent inappropriate images in real-time.AWS AI Practitioner References:AWS Content Moderation Services: AWS provides moderation APIs for filtering unwanted content from applications.

</details>

### Q1.13 (`AIF-U0024`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> An AI practitioner has a database of animal photos. The AI practitioner wants to automatically identify and categorize the animals in the photos without manual human effort.Which strategy meets these requirements?

- A) Object detection
- B) Anomaly detection
- C) Named entity recognition
- D) Inpainting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Object detection is the correct strategy for automatically identifying and categorizing animals in photos.Object Detection:A computer vision technique that identifies and locates objects within an image and assigns them to predefined categories.Ideal for tasks such as identifying animals in photos, where the goal is to detect specific objects (animals) and categorize them accordingly.Why Option A is Correct:Automatic Identification: Object detection models can automatically identify different types of animals in the images without manual intervention.Categorization Capability: Assigns labels to detected objects, fulfilling the requirement for categorizing animals.Why Other Options are Incorrect:B. Anomaly detection: Identifies outliers or unusual patterns, not specific objects in images.C. Named entity recognition: Used in NLP to identify entities in text, not for image processing.D. Inpainting: Used for filling in missing parts of images, not for detecting or categorizing objects.

</details>

### Q1.14 (`AIF-U0013`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company manually reviews all submitted resumes in PDF format. As the company grows, the company expects the volume of resumes to exceed the company ' s review capacity. The company needs an automated system to convert the PDF resumes into plain text format for additional processing.Which AWS service meets this requirement?

- A) Amazon Textract
- B) Amazon Personalize
- C) Amazon Lex
- D) Amazon Transcribe

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon Textract is a service that automatically extracts text and data from scanned documents, including PDFs. It is the best choice for converting resumes from PDF format to plain text for further processing.Amazon Textract:Extracts text, forms, and tables from scanned documents accurately.Ideal for automating the process of converting PDF resumes into plain text format.Why Option A is Correct:Automation of Text Extraction: Textract is designed to handle large volumes of documents and convert them into machine-readable text, perfect for the company ' s need.Scalability and Efficiency: Supports scalability to handle a growing volume of resumes as the company expands.Why Other Options are Incorrect:B. Amazon Personalize: Used for creating personalized recommendations, not for text extraction.C. Amazon Lex: A service for building conversational interfaces, not for processing documents.D. Amazon Transcribe: Used for converting speech to text, not for extracting text from documents.

</details>

### Q1.15 (`AIF-U0014`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company needs to collect a large dataset to train an AI assistant in a specific content area. Which dataset will meet this requirement?

- A) Diverse conversations that use relevant terminology
- B) Time series data of general purpose historical sales
- C) Sentiment analysis of news articles
- D) Unique product IDs and corresponding user IDs

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Diverse conversations that use relevant terminology provide the contextual, domain-specific language an AI assistant needs to learn how to understand and respond accurately within the targeted content area, making this the appropriate training dataset. Time series data of general purpose historical sales is structured numerical data suited to forecasting trends over time, not to training a conversational assistant in a specialized subject. Sentiment analysis of news articles produces classifications of positive or negative tone rather than the conversational examples needed to teach an assistant how to interact. Unique product IDs and corresponding user IDs are identifiers used for tasks such as recommendation systems, and contain no linguistic or contextual content from which an assistant could learn to converse.

</details>

### Q1.16 (`AIF-U0021`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> A financial company is developing a fraud detection system that flags potential fraud cases in credit card transactions. Employees will evaluate the flagged fraud cases. The company wants to minimize the amount of time the employees spend reviewing flagged fraud cases that are not actually fraudulent.Which evaluation metric meets these requirements?

- A) Recall
- B) Accuracy
- C) Precision
- D) Lift chart

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Precision is the metric that measures the proportion of true positives (actual frauds) among all flagged positives (flagged frauds). High precision ensures that most of the flagged cases are truly fraudulent, minimizing the number of false positives employees must review.C is correct:" Precision is the ratio of true positives to all predicted positives, and it answers: ‘Of all the cases flagged as fraud, how many were actually fraud?’ High precision means fewer non-fraudulent cases are sent for manual review. "(Reference: AWS ML Concepts – Precision and Recall, AWS Certified AI Practitioner Study Guide)A (Recall) measures how many actual frauds are caught, but does not minimize false positives.B (Accuracy) can be misleading in imbalanced datasets (like fraud detection).

</details>

### Q1.17 (`AIF-U0022`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A manufacturing company uses AI to inspect products and find any damages or defects. Which type of AI application is the company using?

- A) Recommendation system
- B) Natural language processing (NLP)
- C) Computer vision
- D) Image processing

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Computer Vision is the field of AI that enables machines to interpret and analyze visual information from images and videos, making it the technology behind automated inspection systems that detect product damage or defects on a production line. A recommendation system analyzes user behavior and preferences to suggest relevant products or content, which is unrelated to visual defect detection. Natural Language Processing (NLP) focuses on understanding and generating human language in text or speech, not on analyzing images. Image processing refers to low-level manipulation of images such as resizing, filtering, or enhancing them; while it can be part of a vision pipeline, it does not involve the AI-driven interpretation and classification required for defect detection.

</details>

### Q1.18 (`AIF-U0026`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> Which AWS services can be used for document analysis and information extraction?

- A) Amazon Textract
- B) Amazon Comprehend
- C) Amazon Polly
- D) Amazon Translate
- E) Amazon Transcribe

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, B`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon Textract extracts text and structured data such as forms and tables directly from documents and images using optical character recognition, making it the primary service for the document analysis layer. Amazon Comprehend then applies natural language processing to extracted text to identify entities, key phrases, sentiment, and other insights, enabling information extraction from the content of documents. Amazon Polly converts text to synthesised speech, Amazon Translate performs language translation between languages, and Amazon Transcribe converts spoken audio into text transcripts. None of these services are designed for document analysis or information extraction.

</details>

### Q1.19 (`AIF-U0027`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> Which of the following is an example of Unsupervised Learning?

- A) Training a model to identify animals in photographs
- B) Producing human-like text in response to a written prompt
- C) Grouping data points into clusters based on how similar they are
- D) Predicting a house's selling price from features such as its size and location

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Grouping data points into clusters by similarity is a classic example of Unsupervised Learning, where the algorithm finds structure and natural groupings in the data on its own, without any labeled examples to guide it. Training a model to identify animals in photographs is Supervised Learning, since it learns from images already labeled with the correct animal. Predicting a house's selling price from its features is also Supervised Learning, specifically regression, because it is trained on examples with known prices. Producing human-like text from a prompt is Generative AI, which creates new content rather than discovering groupings in unlabeled data.

</details>

### Q1.20 (`AIF-U0010`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company is building an application that needs to generate synthetic data that is based on existing data. Which type of model can the company use to meet this requirement?

- A) Generative adversarial network (GAN)
- B) XGBoost
- C) Residual neural network
- D) WaveNet

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:domain_1_core_concept`  
**Explanation:** GANs are specifically designed for generating synthetic data. They consist of two neural networks: a generator and a discriminator. The generator creates synthetic data that resembles the real data, and the discriminator tries to distinguish between real and generated data. This process enables GANs to generate realistic synthetic data, making them ideal for use cases where synthetic data is needed based on existing data.

</details>

### Q1.21 (`AIF-U0020`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A digital devices company wants to predict customer demand for memory hardware. The company does not have coding experience or knowledge of ML algorithms and needs to develop a data-driven predictive model. The company needs to perform analysis on internal data and external data. Which solution will meet these requirements?

- A) Store the data in Amazon S3. Create ML models and demand forecast predictions by using Amazon SageMaker built-in algorithms that use the data from Amazon S3.
- B) Import the data into Amazon SageMaker Data Wrangler. Create ML models and demand forecast predictions by using SageMaker built-in algorithms.
- C) Import the data into Amazon SageMaker Data Wrangler. Build ML models and demand forecast predictions by using an Amazon Personalize Trending-Now recipe.
- D) Import the data into Amazon SageMaker Canvas. Build ML models and demand forecast predictions by selecting the values in the data from SageMaker Canvas.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** Amazon SageMaker Canvas is a no-code tool that allows users to build ML models and make predictions without requiring programming knowledge. It is ideal for users with no coding experience, providing an easy interface for importing data and generating predictive models. The other options require more technical expertise or are not designed for no-code model building.

</details>

### Q1.22 (`AIF-U0017`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company wants to build and deploy ML models on AWS without writing any code.Which AWS service or feature meets these requirements?

- A) Amazon SageMaker Canvas
- B) Amazon Rekognition
- C) AWS DeepRacer
- D) Amazon Comprehend

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon SageMaker Canvas is a visual, no-code tool for building and deploying ML models. According to the official SageMaker Canvas documentation:“SageMaker Canvas provides a visual point-and-click interface that allows business analysts to generate accurate ML predictions without writing any code.”

</details>

### Q1.23 (`AIF-U0009`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company has developed an ML model for image classification. The company wants to deploy the model to production so that a web application can use the model. The company needs to implement a solution to host the model and serve predictions without managing any of the underlying infrastructure. Which solution will meet these requirements?

- A) Use Amazon SageMaker Serverless Inference to deploy the model.
- B) Use Amazon CloudFront to deploy the model.
- C) Use Amazon API Gateway to host the model and serve predictions.
- D) Use AWS Batch to host the model and serve predictions.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Amazon SageMaker Serverless Inference allows the company to deploy the ML model without managing any underlying infrastructure, making it suitable for hosting the model and serving predictions. The other options do not directly provide serverless model deployment capabilities.

</details>

### Q1.24 (`AIF-U0029`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> Which strategy evaluates the accuracy of a foundation model (FM) that is used in image classification tasks?

- A) Calculate the total cost of resources used by the model.
- B) Measure the model's accuracy against a predefined benchmark dataset.
- C) Count the number of layers in the neural network.
- D) Assess the color accuracy of images processed by the model.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Evaluating a foundation model's accuracy by measuring its performance against a predefined benchmark dataset is the standard approach for assessing accuracy in image classification tasks. The other options do not provide an appropriate measure of classification accuracy.

</details>

### Q1.25 (`AIF-U0015`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> A company that uses multiple ML models wants to identify changes in original model quality so that the company can resolve any issues. Which AWS service or feature meets these requirements?

- A) Amazon SageMaker JumpStart
- B) Amazon SageMaker HyperPod
- C) Amazon SageMaker Data Wrangler
- D) Amazon SageMaker Model Monitor

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** SageMaker Model Monitor continuously measures data and prediction quality in production, detects deviations from your model’s baseline (such as data drift or accuracy degradation), and alerts you so you can investigate and resolve issues promptly.

</details>

### Q1.26 (`AIF-U0019`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company wants to use an ML model to analyze customer reviews on social media. The model must determine if each review has a neutral, positive, or negative sentiment.

- A) Open-ended generation
- B) Text summarization
- C) Machine translation
- D) Classification

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Classification is the evaluation strategy that assigns input data (such as customer reviews) to predefined categories - in this case, neutral, positive, or negative sentiment. This approach is standard for sentiment analysis tasks.

</details>

### Q1.27 (`AIF-U0011`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> A company is developing an ML model to predict customer churn. Which evaluation metric will assess the model's performance on a binary classification task such as predicting chum?

- A) F1 score
- B) Mean squared error (MSE)
- C) R-squared
- D) Time used to train the model

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** For binary classification tasks like churn prediction, the F1 score balances precision and recall into a single metric, making it ideal for evaluating how well the model identifies churners without over- or under-predicting.

</details>

### Q1.28 (`AIF-U0016`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company wants to assess internet quality in remote areas of the world. The company needs to collect internet speed data and store the data in Amazon RDS. The company will analyze internet speed variation throughout each day. The company wants to create an AI model to predict potential internet disruptions.Which type of data should the company collect for this task?

- A) Tabular data
- B) Text data
- C) Time series data
- D) Audio data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_1_core_concept`  
**Explanation:** Time series data consists of measurements (such as internet speed) collected over time, which is essential for analyzing variations throughout the day and for building predictive models of potential internet disruptions.

</details>

### Q1.29 (`AIF-U0028`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> Which option is an example of unsupervised learning?

- A) Clustering data points into groups based on their similarity
- B) Training a model to recognize images of animals
- C) Predicting the price of a house based on the house's features
- D) Generating human-like text based on a given prompt

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Grouping customers based on purchase history is an example of unsupervised learning, where the model discovers patterns or clusters in the data without using labeled outputs.

</details>

### Q1.30 (`AIF-U0057`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> What is overfitting in machine learning?

- A) When a model uses too little training data
- B) When a model performs well on training data but poorly on new data
- C) When a model takes too long to train
- D) When a model performs poorly on both training and test data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** **Correct answer: When a model performs well on training data but poorly on test data** Overfitting occurs when a machine learning model learns the training data too well, including its noise and outliers. As a result, the model performs exceptionally well on the training data it has seen before, but it fails to generalize to new, unseen data (the test data). This poor generalization is the hallmark of overfitting. The model has essentially memorized the training data instead of learning the underlying patterns. Techniques to combat overfitting include using more data, feature selection, regularization, and cross-validation. **Incorrect:** **A. When a model has too few parameters** - This describes underfitting, not overfitting. A model with too few parameters is unable to capture the underlying complexity of the data, leading to poor performance on both training and test sets. **B. When a model generalizes well to new data** - This is the opposite of overfitting. A model that generalizes well performs well on both training and test data, indicating it has learned the underlying patterns without memorizing the noise. **C. When a model underperforms on both training and test data** - This describes underfitting, not overfitting. Underfitting means the model is too simple to capture the underlying patterns in the data, resulting in poor performance on both training and test sets.

</details>

### Q1.31 (`AIF-U0056`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> What does AUC stand for in the context of model performance metrics?

- A) Average User Cost
- B) Area Under the Curve
- C) Automated Universal Calculation
- D) Augmented Use Case

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** AUC stands for Area Under the Curve (specifically, the ROC curve). The study guide mentions AUC as one of the model performance metrics. AUC (Area Under the Curve) is a performance metric that measures the area under the ROC (Receiver Operating Characteristic) curve. It indicates how well a model can distinguish between classes, with values ranging from 0 to 1, where: - 1.0 represents perfect classification - 0.5 represents random chance - < 0.5 represents worse than random basically you are maximizing the area under the curve. if its a flat line at 0.5, you are doing no better than random guessing.

</details>

### Q1.32 (`AIF-U0045`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> An AI practitioner wants to predict the classification of flowers based on petal length, petal width, sepal length, and sepal width. Which algorithm meets these requirements?

- A) K-nearest neighbors (k-NN)
- B) K-mean
- C) Autoregressive Integrated Moving Average (ARIMA)
- D) Linear regression

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** K-nearest neighbors (k-NN) is a supervised learning algorithm used for classification tasks. It works by classifying a data point based on how its features (such as petal length, petal width, sepal length, and sepal width in this case) are similar to the data points in the training set. For this problem, where the task is to classify flowers based on their features, k-NN is an appropriate choice. k-NN is simple and effective for classification problems where the decision boundary is not necessarily linear, as it looks at the closest neighbors to make predictions.

</details>

### Q1.33 (`AIF-U0055`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> What does an F1 score measure in the context of foundation model (FM) performance?

- A) Model precision and recall
- B) Model speed in generating responses
- C) Financial cost of operating the model
- D) Energy efficiency of the model’s computations

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The F1 score is a metric used to evaluate the performance of a classification model by considering both precision (the proportion of correctly predicted positive cases out of all predicted positives) and recall (the proportion of correctly predicted positive cases out of all actual positives). It is the harmonic mean of precision and recall, ensuring a balance between them, especially when dealing with imbalanced datasets.

</details>

### Q1.34 (`AIF-U0040`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A documentary filmmaker wants to reach more viewers. The filmmaker wants to automatically add subtitles and voice-overs in multiple languages to their films. Which combination of steps will meet these requirements? (Choose two.)

- A) Use Amazon Transcribe and Amazon Translate to generate subtitles in other languages.
- B) Use Amazon Textract and Amazon Translate to generate subtitles in other languages.
- C) Use Amazon Polly to generate voice-overs in other languages.
- D) Use Amazon Translate to generate voice-overs in other languages.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_speech_transcribe_polly`  
**Explanation:** Use Amazon Transcribe and Amazon Translate to generate subtitles in other languages: Amazon Transcribe converts spoken dialogue to text (subtitles), and Amazon Translate can then translate these subtitles into multiple languages. Use Amazon Polly to generate voice-overs in other languages: Amazon Polly converts translated text into lifelike speech, enabling the creation of multilingual voice-overs.

</details>

### Q1.35 (`AIF-U0037`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company wants to find groups for its customers based on the customers’ demographics and buying patterns. Which algorithm should the company use to meet this requirement?

- A) K-nearest neighbors (k-NN)
- B) K-means
- C) Decision tree
- D) Support vector machine

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** K-means is a clustering algorithm used in unsupervised learning to group data points into clusters based on their similarities. It is well-suited for finding patterns in customer demographics and buying behavior. The algorithm identifies groups (clusters) of customers with similar characteristics, which can then be used for targeted marketing, personalized recommendations, or segmentation.

</details>

### Q1.36 (`AIF-U0035`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company needs to train an ML model to classify images of different types of animals. The company has a large dataset of labeled images and will not label more data. Which type of learning should the company use to train the model?

- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Active learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** In supervised learning, the model is trained using a labeled dataset, where each image (input) has a corresponding label (the type of animal, in this case). Since the company already has a large dataset of labeled images, supervised learning is the most appropriate approach. The model learns to classify the images based on the features and labels in the training data.

</details>

### Q1.37 (`AIF-U0043`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A medical company wants to develop an AI application that can access structured patient records, extract relevant information, and generate concise summaries. Which solution will meet these requirements?

- A) Use Amazon Comprehend Medical to extract relevant medical entities and relationships. Apply rulebased logic to structure and format summaries.
- B) Use Amazon Personalize to analyze patient engagement patterns. Integrate the output with a general
- C) Use Amazon Textract to convert scanned documents into digital text. Design a keyword extraction
- D) Implement Amazon Kendra to provide a searchable index for medical records. Use a template-based

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_textract_ocr`  
**Explanation:** Amazon Comprehend Medical is specifically designed to extract structured medical information (such as medication, condition, test results) from unstructured text. By applying rule-based logic afterward, relevant data can be formatted into concise summaries, meeting both the extraction and summarization needs.

</details>

### Q1.38 (`AIF-U0030`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company has terabytes of data in a database that the company can use for business analysis. The company wants to build an AI-based application that can build a SQL query from input text that employees provide. The employees have minimal experience with technology. Which solution meets these requirements?

- A) Generative pre-trained transformers (GPT)
- B) Residual neural network
- C) Support vector machine
- D) WaveNet

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** GPT models are well-suited for converting natural language input into structured queries like SQL, making them ideal for building an AI-based application that translates employee-provided text into SQL queries. The other options are not designed for natural language understanding and query generation tasks.

</details>

### Q1.39 (`AIF-U0032`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company is developing a new model to predict the prices of specific items. The model performed well on the training dataset. When the company deployed the model to production, the model's performance decreased significantly. What should the company do to mitigate this problem?

- A) Reduce the volume of data that is used in training.
- B) Add hyperparameters to the model.
- C) Increase the volume of data that is used in training.
- D) Increase the model training time.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** Increasing the volume of data used in training helps the model generalize better to new, unseen data, reducing overfitting and improving performance in production. The other options either do not address the issue of model generalization or are unlikely to effectively solve the problem.

</details>

### Q1.40 (`AIF-U0031`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company is building a customer service chatbot. The company wants the chatbot to improve its responses by learning from past interactions and online resources. Which AI learning strategy provides this self-improvement capability?

- A) Supervised learning with a manually curated dataset of good responses and bad responses
- B) Reinforcement learning with rewards for positive customer feedback
- C) Unsupervised learning to find clusters of similar customer inquiries
- D) Supervised learning with a continuously updated FAQ database

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Reinforcement learning allows the chatbot to learn from interactions by receiving rewards for positive customer feedback, which helps the model self-improve over time. The other options do not directly provide a mechanism for continuous self-improvement based on interactions.

</details>

### Q1.41 (`AIF-U0033`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company is developing an ML application. The application must automatically group similar customers and products based on their characteristics. Which ML strategy should the company use to meet these requirements?

- A) Unsupervised learning
- B) Supervised learning
- C) Reinforcement learning
- D) Semi-supervised learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Unsupervised learning is used to automatically group or cluster similar customers and products based on their characteristics without the need for labeled data. This strategy fits scenarios where the goal is to discover patterns or groupings in the data.

</details>

### Q1.42 (`AIF-U0041`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> A financial company has deployed an ML model to predict customer churn. The model has been running in production for 1 week. The company wants to evaluate how accurately the model predicts churn compared to actual customer behavior. Which metric meets these requirements?

- A) Root mean squared error (RMSE)
- B) Return on investment (ROI)
- C) F1 score
- D) Bilingual Evaluation Understudy (BLEU) score

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The F1 score combines precision (how many predicted churners actually churned) and recall (how many actual churners were correctly identified) into a single metric, making it ideal for measuring your model’s accuracy on the binary churn‐ prediction task.

</details>

### Q1.43 (`AIF-U0048`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> An ecommerce company wants to group customers based on their purchase history and preferences to personalize the user experience of the company's application. Which ML technique should the company use?

- A) Classification
- B) Clustering
- C) Regression
- D) Content generation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Clustering is an unsupervised learning technique that automatically groups data points - in this case, customers with similar purchase histories and preferences - into segments without needing predefined labels, enabling personalized experiences.

</details>

### Q1.44 (`AIF-U0062`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> Which of the following is NOT a typical business metric for evaluating ML models?

- A) Cost per user
- B) Development costs
- C) Customer feedback
- D) F1 score

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** F1 score is a **model performance metric**, not a business metric. Typical business metrics include Cost per user, Development costs, and Customer feedback, which relate to real-world impact rather than prediction quality.

</details>

### Q1.45 (`AIF-U0038`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A company wants to identify groups for its customers based on the customers’ demographics and buying patterns. Which algorithm should the company use to meet this requirement?

- A) K-nearest neighbors (k-NN)
- B) K-means
- C) Decision tree
- D) Support vector machine

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** K-means is a clustering algorithm commonly used to identify and group customers based on shared characteristics such as demographics and buying patterns, making it suitable for customer segmentation tasks.

</details>

### Q1.46 (`AIF-U0059`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> What is the purpose of vector embeddings in a large language model (LLM)?

- A) Splitting text into manageable pieces of data
- B) Grouping a set of characters to be treated as a single unit
- C) Providing the ability to mathematically compare texts
- D) Providing the count of every word in the input

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Embeddings convert text into high-dimensional vectors that capture semantic relationships, allowing you to compute distances or similarities between pieces of text for tasks like retrieval or clustering.

</details>

### Q1.47 (`AIF-U0046`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> An AI practitioner who has minimal ML knowledge wants to predict employee attrition without writing code. Which Amazon SageMaker feature meets this requirement?

- A) SageMaker Canvas
- B) SageMaker Clarify
- C) SageMaker Model Monitor
- D) SageMaker Data Wrangler

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** SageMaker Canvas provides a no-code visual interface that allows users with minimal ML knowledge to build, train, and deploy models for predictions, such as employee attrition, without writing any code.

</details>

### Q1.48 (`AIF-U0034`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A company is using an Amazon Nova Canvas model to generate images. The model generates images successfully. The company needs to prevent the model from including specific items in the generated images. Which solution will meet this requirement?

- A) Use a higher temperature value.
- B) Use a more detailed prompt.
- C) Use a negative prompt.
- D) Use another foundation model (FM).

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** A negative prompt is used to specify items or characteristics that you want the image generation model to avoid including in the output, ensuring that specific items are excluded from generated images.

</details>

### Q1.49 (`AIF-U0042`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A financial company wants to flag all credit card activity as possibly fraudulent or non-fraudulent based on transaction data. Which type of ML model meets these requirements?

- A) Regression
- B) Diffusion
- C) Binary classification
- D) Multi-class classification

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Binary classification models are designed to distinguish between two classes - fraudulent versus nonfraudulent transactions - making them the appropriate choice for this use case.

</details>

### Q1.50 (`AIF-U0047`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> An animation company wants to provide subtitles for its content. Which AWS service meets this requirement?

- A) Amazon Comprehend
- B) Amazon Polly
- C) Amazon Transcribe
- D) Amazon Translate

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_speech_transcribe_polly`  
**Explanation:** Amazon Transcribe converts spoken audio into accurate, time-stamped text transcripts, making it the ideal service for generating subtitles from your animation audio tracks.

</details>

### Q1.51 (`AIF-U0044`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> A news agency publishes articles in English. The agency wants to make articles available in other languages. Which solution meets these requirements?

- A) Add Amazon Transcribe to the company’s website.
- B) Use the Amazon Translate real-time translation feature.
- C) Add Amazon Personalize to the company’s website.
- D) Use the Amazon Textract real-time document processing feature.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon Translate provides real-time translation of text, making it suitable for automatically translating articles from English into other languages for publication.

</details>

### Q1.52 (`AIF-U0061`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> Which AWS service is best suited for natural language processing tasks?

- A) Amazon SageMaker
- B) Amazon Comprehend
- C) Amazon Polly
- D) Amazon Transcribe

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_speech_transcribe_polly`  
**Explanation:** Amazon Comprehend is specifically designed for natural language processing tasks. The study guide lists various AWS managed AI/ML services and their capabilities.

</details>

### Q1.53 (`AIF-U0063`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> Which type of learning is most appropriate when you have a large dataset of labeled examples?

- A) Unsupervised learning
- B) Reinforcement learning
- C) Supervised learning
- D) Semi-supervised learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Supervised learning is most appropriate when you have labeled data. The study guide describes supervised learning as one of the types of machine learning.

</details>

### Q1.54 (`AIF-U0039`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> A customer service team is developing an application to analyze customer feedback and automatically classify the feedback into different categories. The categories include product quality, customer service, and delivery experience. Which AI concept does this scenario present?

- A) Computer vision
- B) Natural language processing (NLP)
- C) Recommendation systems
- D) Fraud detection

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Automatically analyzing and classifying free-text feedback into thematic categories is a core NLP task (text classification).

</details>

### Q1.55 (`AIF-U0060`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> Which AWS service is best suited for converting text to speech?

- A) Amazon Comprehend
- B) Amazon Translate
- C) Amazon Transcribe
- D) Amazon Polly

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:aws_managed_ai_speech_transcribe_polly`  
**Explanation:** Amazon Polly is a text-to-speech service that converts written text into spoken audio.

</details>

### Q1.56 (`AIF-U0356`) — 1.2 Practical AI Use Cases & AWS Managed AI Services
> Which algorithm is best suited for large datasets with many features?

- A) Gradient Boosting
- B) Naive Bayes
- C) Random Forest
- D) K-means

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** **Correct answer: Gradient Boosting** Gradient Boosting algorithms, such as XGBoost, LightGBM, and CatBoost, are well-suited for large datasets with many features due to their ability to handle complex relationships and high dimensionality. These algorithms work by sequentially building an ensemble of weak learners (typically decision trees), where each new tree corrects the errors of the previous ones. This iterative process allows Gradient Boosting to capture intricate patterns in the data and achieve high accuracy. Furthermore, these implementations often include regularization techniques and efficient handling of missing values, making them robust for large, feature-rich datasets. They are designed for speed and performance, and are often preferred in machine learning competitions and real-world applications with large datasets. **Incorrect:** **B. Naive Bayes** - Naive Bayes is a simple and fast algorithm, but it assumes that features are independent of each other, which is often not the case in real-world datasets. This assumption can lead to poor performance, especially when dealing with many features that are correlated. While Naive Bayes can handle large datasets, its accuracy may suffer compared to more sophisticated algorithms like Gradient Boosting. **C. Random Forest** - Random Forest is an ensemble learning method that combines multiple decision trees. While it can handle large datasets and many features, it may not be as efficient as Gradient Boosting, especially when the number of features is very high. Random Forests can also be prone to overfitting if not properly tuned, and the individual trees can be computationally expensive to train on very large datasets. Gradient Boosting often provides better performance due to its sequential, error-correcting approach. **D. K-means** - K-means is a clustering algorithm used for unsupervised learning. It aims to partition data points into K clusters based on their proximity to cluster centroids. K-means is not designed for classification or regression tasks, and it does not directly address the problem of handling many features. While K-means can be applied to large datasets, it is not the best choice for predictive modeling with many features, where algorithms like Gradient Boosting are more appropriate.

</details>

### Q1.57 (`AIF-U0345`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> What is the role of the activation function in a neural network?

- A) To normalize the input data
- B) To reduce the number of parameters
- C) To introduce non-linearity into the model
- D) To decrease the learning rate

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** **Correct answer: To introduce non-linearity into the model** Activation functions are a crucial component of neural networks because they introduce non-linearity. Without activation functions, a neural network would simply be a linear regression model, regardless of its depth (number of layers). Linear models can only learn linear relationships between inputs and outputs. Real-world data is rarely linear; it often contains complex, non-linear relationships. Activation functions allow neural networks to learn these complex patterns by transforming the linear output of a neuron into a non-linear output. Common activation functions include ReLU (Rectified Linear Unit), sigmoid, and tanh. The choice of activation function can significantly impact the performance of the neural network. **Incorrect:** **A. To normalize the input data** - While normalizing input data is a common preprocessing step to improve model training, it is not the role of the activation function. Normalization typically involves scaling the input features to a specific range (e.g., 0 to 1) or standardizing them to have a mean of 0 and a standard deviation of 1. This is done before the data is fed into the neural network, independently of the activation functions. **B. To reduce the number of parameters** - Activation functions do not directly reduce the number of parameters in a neural network. The number of parameters is determined by the network's architecture (number of layers and neurons per layer). Techniques like regularization or pruning are used to reduce the number of parameters and prevent overfitting, but these are distinct from the role of activation functions. **D. To decrease the learning rate** - The learning rate is a hyperparameter that controls the step size during the optimization process (e.g., gradient descent). It determines how much the model's weights are adjusted in response to the error calculated during training. Activation functions do not directly control or decrease the learning rate. Learning rate scheduling techniques (e.g., reducing the learning rate over time) are used to adjust the learning rate during training, but these are separate from the function of activation functions.

</details>

### Q1.58 (`AIF-U0331`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> What is the primary purpose of normalization in data preprocessing?

- A) To split the data into training and test sets
- B) To increase the number of features
- C) To ensure all features contribute equally to the model
- D) To remove outliers from the data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** **Correct answer: To ensure all features contribute equally to the model** Normalization is a data preprocessing technique used to scale numerical features to a standard range of values. This is crucial because features with larger values can disproportionately influence machine learning models, leading to biased results. By normalizing the data, all features are brought to a similar scale (e.g., between 0 and 1), ensuring that each feature contributes more equally to the model's learning process. This helps to improve the model's accuracy, stability, and convergence speed. Common normalization techniques include Min-Max scaling and Z-score standardization. Without normalization, models might incorrectly prioritize features with larger magnitudes, hindering their ability to learn underlying patterns effectively. **Incorrect:** **A. To split the data into training and test sets** - Splitting data into training and test sets is a crucial step in model evaluation and preventing overfitting, but it is distinct from normalization. Splitting involves dividing the dataset into subsets for training the model and evaluating its performance on unseen data. Normalization is applied to the numerical features within these sets, but it doesn't perform the splitting itself. **B. To increase the number of features** - Feature engineering, not normalization, is the process of creating new features from existing ones. Normalization focuses on scaling the existing numerical features, not increasing their number. Increasing the number of features can be useful in some cases, but it's a separate data preprocessing step. **D. To remove outliers from the data** - While normalization can reduce the impact of outliers to some extent by scaling the data, its primary purpose is not outlier removal. Outlier removal is a separate data cleaning task that involves identifying and handling extreme values in the dataset, often using techniques like trimming or winsorizing. Normalization might be applied after outlier treatment.

</details>

### Q1.59 (`AIF-U0304`) — 1.1 Basic AI/ML Concepts, Data Types & Learning Paradigms
> What is a common use of decision trees in machine learning?

- A) Data normalization
- B) Regression and classification
- C) Clustering data points
- D) Dimensionality reduction

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** **Correct answer: Regression and classification** Decision trees are a supervised learning algorithm used for both regression and classification tasks. In classification, the tree predicts the class to which a data point belongs. In regression, the tree predicts a continuous numerical value. The tree structure consists of nodes representing features, branches representing decision rules, and leaves representing the predicted outcome. The algorithm learns these rules from labeled training data to make predictions on new, unseen data. Decision trees are popular due to their interpretability and ease of visualization. **Incorrect:** **A. Data normalization** - Data normalization is a preprocessing technique used to scale numerical features to a standard range. While important for many machine learning algorithms, it is not a primary use of decision trees themselves. Decision trees can handle data without normalization, although normalization may improve performance in some cases when used in conjunction with other algorithms in an ensemble. **C. Clustering data points** - Clustering is an unsupervised learning technique used to group similar data points together. Decision trees, on the other hand, are a supervised learning algorithm that requires labeled data for training. Clustering algorithms like K-means or hierarchical clustering are used for grouping data points, not decision trees. **D. Dimensionality reduction** - Dimensionality reduction techniques, such as Principal Component Analysis (PCA), are used to reduce the number of features in a dataset while preserving important information. While decision trees can implicitly perform feature selection by choosing the most relevant features for splitting, their primary purpose is not dimensionality reduction. Other methods are more directly suited for this task.

</details>

### Q1.60 (`AIF-U0334`) — 1.3 AI/ML Development Lifecycle, MLOps & ML Metrics
> What is the purpose of a confusion matrix in classification?

- A) To measure the accuracy of regression models
- B) To perform dimensionality reduction
- C) To evaluate the performance of a classification model
- D) To visualize data distributions

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** **Correct answer: To evaluate the performance of a classification model** A confusion matrix is a table that summarizes the performance of a classification model. It visualizes the counts of true positive, true negative, false positive, and false negative predictions. This allows for a detailed analysis of the model's accuracy, precision, recall, and F1-score, which are essential metrics for understanding how well the model is performing on different classes. It helps identify where the model is making mistakes and provides insights for improving its performance. For example, if a model has a high false negative rate for a particular class, it indicates that the model is frequently misclassifying instances of that class as belonging to other classes. **Incorrect:** **A. To measure the accuracy of regression models** - Confusion matrices are specifically used for evaluating classification models, not regression models. Regression models predict continuous values, and their performance is typically evaluated using metrics like Mean Squared Error (MSE) or R-squared. **B. To perform dimensionality reduction** - Dimensionality reduction techniques, such as Principal Component Analysis (PCA) or t-distributed Stochastic Neighbor Embedding (t-SNE), are used to reduce the number of features in a dataset while preserving its essential information. Confusion matrices are not related to dimensionality reduction. **D. To visualize data distributions** - Histograms, box plots, and scatter plots are commonly used to visualize data distributions. While a confusion matrix presents data in a visual format, its primary purpose is to evaluate the performance of a classification model, not to visualize the underlying data distributions.

</details>

## Domain 2: Fundamentals of Generative AI (24% — 72 Questions)

### Q2.01 (`AIF-U0568`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which concept describes systematically designing, curating, and dynamically managing everything inside a Foundation Model's context window—including system instructions, retrieved RAG chunks, conversation memory, and tool outputs—within token budgets?

- A) Hyperparameter tuning
- B) Context engineering
- C) Quantization
- D) Transfer learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_context_engineering`  
**Explanation:** Context engineering goes beyond static prompt phrasing by managing the full runtime context payload (instructions, RAG retrieval, short/long-term memory, and tool outputs) to maximize FM accuracy and control token cost.

</details>

### Q2.02 (`AIF-U0525`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A media company needs a single AWS-native family of foundation models in Amazon Bedrock that supports fast low-cost text tasks, multimodal image/video understanding, and image/video generation. Which model family should they evaluate?

- A) Amazon Nova
- B) Amazon Lex
- C) Amazon Polly
- D) AWS Lake Formation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon Nova is AWS's generation of foundation models in Amazon Bedrock spanning ultra-fast text (Nova Micro), multimodal understanding (Nova Lite, Nova Pro), and creative media generation (Nova Canvas, Nova Reel).

</details>

### Q2.03 (`AIF-U0531`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A software engineering team wants an agentic AI IDE from AWS that uses spec-driven development to guide work from requirements and design specifications through automated task execution and verification. Which AWS developer tool should they use?

- A) Amazon Rekognition
- B) Kiro
- C) AWS Artifact
- D) Amazon Polly

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:dev_tools_kiro_pipeline`  
**Explanation:** Kiro is AWS's agentic AI IDE designed for spec-driven development, turning requirements into structured design specs, implementation tasks, and verified code across the AI/ML and software lifecycle.

</details>

### Q2.04 (`AIF-U0543`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Business analysts want a unified AWS analytics and AI workspace to ask natural-language questions across corporate dashboards, documents, and business workflows without writing code or building custom Foundation Model pipelines. Which AWS service fits best?

- A) Amazon Quick
- B) Amazon SageMaker Ground Truth
- C) AWS PrivateLink
- D) Amazon EKS

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** Amazon Quick (in-scope under Analytics and GenAI applications in AIF-C01 v1.2) provides AI-powered natural-language BI, research, and enterprise workflow automation for business users.

</details>

### Q2.05 (`AIF-U0559`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is the primary role of the Model Context Protocol (MCP) in an agentic AI architecture?

- A) Encrypting training datasets stored in Amazon S3 buckets
- B) Providing a standardized protocol for connecting AI agents and models to external tools, APIs, and data sources
- C) Measuring n-gram overlap in automated text summarization
- D) Reducing model weights from FP32 to INT8 precision

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_agentic_ai_mcp`  
**Explanation:** Model Context Protocol (MCP) is an open standard that standardizes how AI agents and foundation models discover and connect to external tools, enterprise APIs, and data repositories.

</details>

### Q2.06 (`AIF-U0541`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> An enterprise wants to accelerate large-scale modernization of legacy .NET, Java, and mainframe workloads using specialized AWS agentic AI capabilities. Which in-scope AWS service is designed for this purpose?

- A) Amazon Comprehend
- B) AWS Transform
- C) Amazon Translate
- D) Amazon Neptune

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** AWS Transform is AWS's agentic AI service built specifically to automate enterprise modernization and migration of legacy workloads (such as .NET, Java, VMware, and Mainframe).

</details>

### Q2.07 (`AIF-U0516`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A developer team wants an open-source, model-driven Python SDK from AWS to build multi-agent AI workflows with native Model Context Protocol (MCP) tool support in minimal code. Which tool meets this requirement?

- A) AWS Glue DataBrew
- B) Strands Agents
- C) Amazon Macie
- D) AWS Cost Explorer

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_agentic_ai_mcp`  
**Explanation:** Strands Agents is AWS's open-source, model-driven SDK for building single- and multi-agent AI applications using native FM reasoning loops and MCP tool integrations.

</details>

### Q2.08 (`AIF-U0440`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to use language models to create an application for inference on edge devices. The inference must have the lowest latency possible.Which solution will meet these requirements?

- A) Deploy optimized small language models (SLMs) on edge devices.
- B) Deploy optimized large language models (LLMs) on edge devices.
- C) Incorporate a centralized small language model (SLM) API for asynchronous communication with edge devices.
- D) Incorporate a centralized large language model (LLM) API for asynchronous communication with edge devices.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** To achieve the lowest latency possible for inference on edge devices, deploying optimized small language models (SLMs) is the most effective solution. SLMs require fewer resources and havefaster inference times, making them ideal for deployment on edge devices where processing power and memory are limited.Option A (Correct): " Deploy optimized small language models (SLMs) on edge devices " : This is the correct answer because SLMs provide fast inference with low latency, which is crucial for edge deployments.Option B: " Deploy optimized large language models (LLMs) on edge devices " is incorrect because LLMs are resource-intensive and may not perform well on edge devices due to their size and computational demands.Option C: " Incorporate a centralized small language model (SLM) API for asynchronous communication with edge devices " is incorrect because it introduces network latency due to the need for communication with a centralized server.Option D: " Incorporate a centralized large language model (LLM) API for asynchronous communication with edge devices " is incorrect for the same reason, with even greater latency due to the larger model size.AWS AI Practitioner References:Optimizing AI Models for Edge Devices on AWS: AWS recommends using small, optimized models for edge deployments to ensure minimal latency and efficient performance.

</details>

### Q2.09 (`AIF-U0439`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to use generative AI to increase developer productivity and software development. The company wants to use Amazon Q Developer.What can Amazon Q Developer do to help the company meet these requirements?

- A) Create software snippets, reference tracking, and open-source license tracking.
- B) Run an application without provisioning or managing servers.
- C) Enable voice commands for coding and providing natural language search.
- D) Convert audio files to text documents by using ML models.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_speech_transcribe_polly`  
**Explanation:** Amazon Q Developer is a tool designed to assist developers in increasing productivity by generating code snippets, managing reference tracking, and handling open-source license tracking. These features help developers by automating parts of the software development process.Option A (Correct): " Create software snippets, reference tracking, and open-source license tracking " : This is the correct answer because these are key features that help developers streamline and automate tasks, thus improving productivity.Option B: " Run an application without provisioning or managing servers " is incorrect as it refers to AWS Lambda or AWS Fargate, not Amazon Q Developer.Option C: " Enable voice commands for coding and providing natural language search " is incorrect because this is not a function of Amazon Q Developer.Option D: " Convert audio files to text documents by using ML models " is incorrect as this refers to Amazon Transcribe, not Amazon Q Developer.AWS AI Practitioner References:Amazon Q Developer Features: AWS documentation outlines how Amazon Q Developer supports developers by offering features that reduce manual effort and improve efficiency.

</details>

### Q2.10 (`AIF-U0441`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> What is a hallucination in the context of generative AI?

- A) An error in the training data
- B) When a model generates plausible-sounding but factually incorrect content
- C) A visual artifact or distortion that appears in generated images
- D) A hardware malfunction during inference that corrupts the GPU memory output

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_limitations_hallucination_nondeterminism`  
**Explanation:** AI hallucination occurs when a generative model produces outputs that sound confident and plausible but are factually incorrect, fabricated, or not supported by the training data. This is a fundamental challenge with large language models. Mitigation strategies include RAG (grounding responses in real data), guardrails, human review, and temperature tuning. Exam tip: RAG is the primary AWS-recommended technique for reducing hallucinations by grounding responses in verified knowledge sources.

</details>

### Q2.11 (`AIF-U0469`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which term describes the numerical representations of real-world objects and concepts that AI and natural language processing (NLP) models use to improve understanding of textual information?

- A) Embeddings
- B) Tokens
- C) Models
- D) Binaries

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Embeddings are numerical representations of objects (such as words, sentences, or documents) that capture the objects ' semantic meanings in a form that AI and NLP models can easily understand. These representations help models improve their understanding of textual information by representing concepts in a continuous vector space.Option A (Correct): " Embeddings " : This is the correct term, as embeddings provide a way for models to learn relationships between different objects in their input space, improving their understanding and processing capabilities.Option B: " Tokens " are pieces of text used in processing, but they do not capture semantic meanings like embeddings do.Option C: " Models " are the algorithms that use embeddings and other inputs, not the representations themselves.Option D: " Binaries " refer to data represented in binary form, which is unrelated to the concept of embeddings.AWS AI Practitioner References:Understanding Embeddings in AI and NLP: AWS provides resources and tools, like Amazon SageMaker, that utilize embeddings to represent data in formats suitable for machine learning models.

</details>

### Q2.12 (`AIF-U0444`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A company is developing an editorial assistant application that uses generative AI. During the pilot phase, usage is low and application performance is not a concern. The company cannot predict application usage after the application is fully deployed and wants to minimize application costs.Which solution will meet these requirements?

- A) Use GPU-powered Amazon EC2 instances.
- B) Use Amazon Bedrock with Provisioned Throughput.
- C) Use Amazon Bedrock with On-Demand Throughput.
- D) Use Amazon SageMaker JumpStart.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** The correct answer is C because Amazon Bedrock with On-Demand Throughput is designed for variable or unpredictable workloads. It allows you to pay only for what you use, which is ideal for early-stage or pilot-phase generative AI applications.From AWS documentation:" On-Demand Throughput in Amazon Bedrock provides flexibility and cost-efficiency for unpredictable or low-volume generative AI applications. You are charged based on the number of input/output tokens processed, with no need to provision dedicated capacity. "Explanation of other options:A. Using GPU-powered EC2 instances requires managing infrastructure and is generally more expensive, especially for inconsistent usage.B. Provisioned Throughput is best suited for predictable, high-volume production workloads where guaranteed throughput is needed.D. SageMaker JumpStart is for training and deploying ML models, not for efficient inference of foundation models.Referenced AWS AI/ML Documents and Study Guides:Amazon Bedrock Pricing and Throughput ModelsAWS Generative AI Best Practices – Cost OptimizationAWS ML Specialty Guide – Bedrock Deployment Models

</details>

### Q2.13 (`AIF-U0471`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which type of AI model makes numeric predictions?

- A) Diffusion
- B) Regression
- C) Transformer
- D) Multi-modal

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** The correct answer is regression. In machine learning, regression models are designed to predict continuous numerical values based on input features. Common use cases include predicting house prices, sales forecasting, temperature trends, or medical risk scores. According to AWS SageMaker documentation, regression tasks fall under supervised learning where the output is a real-valued number rather than a class label. For instance, linear regression is one of the most commonly used models for predicting a single continuous output. By contrast, diffusion models are typically used in generative image tasks, transformers are architectures (not specific to numeric output), and multi-modal models process various data types like text, images, and audio. Only regression models are purpose-built for making precise numeric predictions, which aligns with AWS best practices when the output is a quantity, not a category.Referenced AWS AI/ML Documents and Study Guides:AWS Machine Learning Specialty Guide – Regression ModelsAmazon SageMaker Built-in Algorithms – Linear Learner (Regression and Classification)

</details>

### Q2.14 (`AIF-U0464`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is the main difference between batch inferencing and real-time inferencing?

- A) Batch inferencing is always more accurate
- B) Real-time inferencing can only be done on small datasets
- C) Batch inferencing processes multiple inputs at once, while real-time inferencing processes individual inputs as they arrive
- D) Real-time inferencing is always faster than batch inferencing

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Batch inferencing collects multiple inputs and processes them together in a single job, making it well suited for non-time-sensitive workloads where throughput and efficiency are the priority. Real-time inferencing processes each input individually as it arrives and returns a prediction immediately, making it suitable for applications that require instant responses such as fraud detection or content moderation. Batch inferencing is not always more accurate than real-time inferencing because accuracy is a property of the model and its training data, not of the inferencing method used to serve predictions. Real-time inferencing is not limited to small datasets as it processes individual inputs on demand regardless of the overall size of the data being served. Real-time inferencing is not always faster than batch inferencing because while it offers lower latency per individual request, batch inferencing can achieve higher overall throughput by processing many inputs simultaneously.

</details>

### Q2.15 (`AIF-U0451`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A company wants to learn about generative AI applications in an experimental environment.Which solution will meet this requirement MOST cost-effectively?

- A) Amazon Q Developer
- B) Amazon SageMaker JumpStart
- C) Amazon Bedrock PartyRock
- D) Amazon Q Business

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** The correct answer is Amazon Bedrock PartyRock, a playground for building and experimenting with generative AI apps in a low-cost, no-code environment. PartyRock is designed for innovation and learning. It enables users to try out prompts, LLM apps, and templates using Amazon Bedrock under a free-tier friendly setup. According to AWS, PartyRock abstracts infrastructure and allows rapid prototyping using models from Bedrock providers. This makes it ideal for early experimentation, especially for non-developers or those not ready to invest in full production pipelines. In contrast, Amazon Q Developer is for software engineering tasks, SageMaker JumpStart focuses on deploying ML models, and Q Business targets enterprise knowledge workers. None of those are as cost-effective and experimental-focused as PartyRock.Referenced AWS AI/ML Documents and Study Guides:Amazon Bedrock Documentation – PartyRock OverviewAWS Generative AI Learning Path – Getting Started Tools

</details>

### Q2.16 (`AIF-U0442`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company acquires International Organization for Standardization (ISO) accreditation to manage AI risks and to use AI responsibly. What does this accreditation reflect about the company?

- A) All members of the company are ISO certified.
- B) All AI systems that the company uses are ISO certified.
- C) All AI application team members are ISO certified.
- D) The company's development framework is ISO certified.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** ISO accreditation certifies that the company's development framework, processes, and controls for managing AI meet the requirements of the relevant ISO standard, reflecting that the organization has demonstrated responsible and risk-aware AI governance practices at a structural level. All members of the company being ISO certified is incorrect because organizational accreditation does not automatically certify every individual employee; personal ISO certification is a separate process that individuals undertake independently. All AI systems being ISO certified is incorrect because the accreditation applies to the framework and processes used to develop and govern AI, not to the individual systems or models produced within it. All AI application team members being ISO certified is incorrect for the same reason, as individual employees require separate certification and are not automatically certified by the organization achieving accreditation.

</details>

### Q2.17 (`AIF-U0466`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which option is a benefit of using Infrastructure as Code (IaC) in Machine Learning Operations (MLOps)?

- A) IaC eliminates the need for hyperparameter tuning
- B) IaC always provisions powerful compute instances, contributing to the training of more accurate models
- C) IaC streamlines the deployment of scalable and consistent ML workloads in cloud environments
- D) IaC minimizes overall expenses by deploying only low-cost instances

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** IaC allows infrastructure to be defined, versioned, and automated in code, enabling repeatable and consistent provisioning of ML environments across development, testing, and production stages, which directly supports the MLOps principles of scalable systems and repeatable processes. Hyperparameter tuning is a model optimization activity that adjusts parameters such as learning rate and batch size during training to improve model performance; it is entirely separate from infrastructure provisioning, so IaC cannot eliminate it. IaC does not inherently provision powerful or low-cost instances, as it simply provisions whatever resources are defined in the configuration code; the choice of instance type and cost profile is determined by the engineer writing the template, not by IaC itself.

</details>

### Q2.18 (`AIF-U0457`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A pharmaceutical company wants to analyze user reviews of new medications and provide a concise overview for each medication. Which solution meets these requirements?

- A) Create a time-series forecasting model to analyze the medication reviews by using Amazon Personalize.
- B) Create medication review summaries by using Amazon Bedrock large language models (LLMs).
- C) Create a classification model that categorizes medications into different groups by using Amazon SageMaker.
- D) Create medication review summaries by using Amazon Rekognition.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Amazon Bedrock provides access to a variety of large language models (LLMs), which are well-suited for tasks such as text summarization. By using LLMs, the pharmaceutical company can automatically generate concise and coherent summaries of user reviews for each medication. These models are designed to understand and process large amounts of text, making them ideal for summarizing user reviews in a clear and efficient manner. Amazon Bedrock allows the company to utilize LLMs that can generate summaries, which is exactly what is needed in this case.

</details>

### Q2.19 (`AIF-U0463`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is the difference between discriminative and generative AI models?

- A) Discriminative models are faster than generative models
- B) Discriminative models are more accurate than generative models
- C) Discriminative models classify or predict, while generative models create new content
- D) Discriminative models need more data than generative models

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** Discriminative models learn to classify inputs or predict outcomes, whereas generative models learn to create new content similar to their training data; this is the core distinction between the two. Claims that discriminative models are inherently faster, more accurate, or need more data are not the defining difference and are not generally true; the real distinction is what each type of model produces.

</details>

### Q2.20 (`AIF-U0446`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A company uses Amazon Bedrock to implement a generative AI assistant on a website. The AI assistant helps customers with product recommendations and purchasing decisions. The company wants to measure the direct impact of the AI assistant on sales performance.

- A) The conversion rate of customers who purchase products after AI assistant interactions
- B) The number of customer interactions with the AI assistant
- C) Sentiment analysis scores from customer feedback after AI assistant interactions
- D) Natural language understanding accuracy rates

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The most direct business KPI for sales performance is conversion rate (percentage of users who purchase after AI assistant interaction).Number of interactions (B) shows engagement, not sales impact.Sentiment analysis (C) shows customer satisfaction but not revenue impact.NLU accuracy (D) is a technical metric, not a business outcome.???? Reference:AWS Generative AI Use Cases – Measuring Business Value

</details>

### Q2.21 (`AIF-U0461`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is a foundation model in generative AI?

- A) A model that can only generate text
- B) A model designed specifically for image generation
- C) A large, pre-trained model that can be adapted for many tasks
- D) A model that requires no training data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** A foundation model is a large model pre-trained on vast amounts of data that can be adapted or fine-tuned for many downstream tasks such as text generation, summarization, and question answering. A foundation model is not limited to text and is not built only for image generation, and it is trained on large amounts of data, so the claim that it needs no training data is incorrect.

</details>

### Q2.22 (`AIF-U0450`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to keep its foundation model (FM) relevant by using the most recent data. The company wants to implement a model training strategy that includes regular updates to the FM.Which solution meets these requirements?

- A) Batch learning
- B) Continuous pre-training
- C) Static training
- D) Latent training

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** Continuous pre-training keeps a foundation model “always learning” by periodically (or even continuously) ingesting the latest data and updating its weights. This approach ensures the model stays current without having to start training from scratch every time new data arrives, unlike static or strictly batch-oriented methods.

</details>

### Q2.23 (`AIF-U0465`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> Which of the following is a potential disadvantage of generative AI solutions?

- A) Adaptability
- B) Responsiveness
- C) Inaccuracy
- D) Simplicity

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Inaccuracy is a known disadvantage of generative AI, which can produce incorrect, biased, or fabricated information that requires validation and human oversight. Adaptability and responsiveness are advantages of generative AI, and simplicity is not a disadvantage. None of these represents a drawback of generative AI solutions.

</details>

### Q2.24 (`AIF-U0445`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A company uses a foundation model (FM) from Amazon Bedrock for an AI search tool. The company wants to fine-tune the model to be more accurate by using the company's data. Which strategy will successfully fine-tune the model?

- A) Provide labeled data with the prompt field and the completion field.
- B) Prepare the training dataset by creating a .txt file that contains multiple lines in .csv format.
- C) Purchase Provisioned Throughput for Amazon Bedrock.
- D) Train the model on journals and textbooks.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Fine-tuning a foundation model involves training it with labeled data that contains both input prompts and corresponding expected completions to adjust the model’s behavior to fit the company’s needs. The other options are not directly related to the fine-tuning process using specific labeled data.

</details>

### Q2.25 (`AIF-U0447`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company uses Amazon SageMaker for its ML pipeline in a production environment. The company has large input data sizes up to 1 GB and processing times up to 1 hour. The company needs near real-time latency. Which SageMaker inference option meets these requirements?

- A) Real-time inference
- B) Serverless inference
- C) Asynchronous inference
- D) Batch transform

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_inference_modes`  
**Explanation:** Asynchronous inference is suitable for handling large input data and long processing times while still providing responses without blocking other requests. It allows for near real-time latency, whereas the other options are less suitable given the input size and processing time constraints.

</details>

### Q2.26 (`AIF-U0462`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is a token in the context of generative AI?

- A) A security feature
- B) A type of neural network
- C) A unit of text processed by the model
- D) A model evaluation metric

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** A token is the basic unit of text, such as a word or sub-word, that a model processes and generates, which is what the term refers to. A token is not a security feature, not a type of neural network, and not a model evaluation metric; those describe unrelated concepts.

</details>

### Q2.27 (`AIF-U0455`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A financial institution is using Amazon Bedrock to develop an AI application. The application is hosted in a VPC. To meet regulatory compliance standards, the VPC is not allowed access to any internet traffic. Which AWS service or feature will meet these requirements?

- A) AWS PrivateLink
- B) Amazon Macie
- C) Amazon CloudFront
- D) Internet gateway

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** AWS PrivateLink allows secure, private connectivity between VPCs and AWS services without needing internet access, making it suitable for meeting regulatory compliance standards. The other options either do not provide private connectivity or require internet access.

</details>

### Q2.28 (`AIF-U0448`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to build a generative AI application by using Amazon Bedrock and needs to choose a foundation model (FM). The company wants to know how much information can fit into one prompt. Which consideration will inform the company's decision?

- A) Temperature
- B) Context window
- C) Batch size
- D) Model size

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** The context window determines how much information can fit into a single prompt. It specifies the number of tokens the foundation model can process at once, affecting the length of input that can be provided. The other options do not directly relate to prompt size.

</details>

### Q2.29 (`AIF-U0467`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which option is a use case for generative AI models?

- A) Improving network security by using intrusion detection systems
- B) Creating photorealistic images from text descriptions for digital marketing
- C) Enhancing database performance by using optimized indexing
- D) Analyzing financial data to forecast stock market trends

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** Generative AI models are used to create new content, such as photorealistic images from text descriptions, which is useful for digital marketing. The other options involve tasks better suited for analytical or detection systems rather than generative models.

</details>

### Q2.30 (`AIF-U0454`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A financial company is using ML to help with some of the company's tasks. Which option is a use of generative AI models?

- A) Summarizing customer complaints
- B) Classifying customers based on product usage
- C) Segmenting customers based on type of investments
- D) Forecasting revenue for certain products

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** Generative AI models are designed to generate new content such as text, images, or audio. Summarizing customer complaints involves generating concise versions of longer texts, which is a task well-suited for generative AI models like large language models.

</details>

### Q2.31 (`AIF-U0452`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to make a chatbot to help customers. The chatbot will help solve technical problems without human intervention. The company chose a foundation model (FM) for the chatbot. The chatbot needs to produce responses that adhere to company tone. Which solution meets these requirements?

- A) Set a low limit on the number of tokens the FM can produce.
- B) Use batch inferencing to process detailed responses.
- C) Experiment and refine the prompt until the FM produces the desired responses.
- D) Define a higher number for the temperature parameter.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Experimenting and refining the prompt allows you to guide the FM to produce responses that align with the company's desired tone. This approach helps to shape the behavior of the chatbot. The other options do not directly ensure adherence to company tone.

</details>

### Q2.32 (`AIF-U0443`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company is building a contact center application and wants to gain insights from customer conversations. The company wants to analyze and extract key information from the audio of the customer calls. Which solution meets these requirements?

- A) Build a conversational chatbot by using Amazon Lex.
- B) Transcribe call recordings by using Amazon Transcribe.
- C) Extract information from call recordings by using Amazon SageMaker Model Monitor.
- D) Create classification labels by using Amazon Comprehend.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon Transcribe converts audio recordings into text, which allows for further analysis and extraction of key information from customer conversations. The other options do not directly handle audio transcription or extraction of information from audio.

</details>

### Q2.33 (`AIF-U0456`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A law firm wants to build an AI application by using large language models (LLMs). The application will read legal documents and extract key points from the documents. Which solution meets these requirements?

- A) Build an automatic named entity recognition system.
- B) Create a recommendation engine.
- C) Develop a summarization chatbot.
- D) Develop a multi-language translation system.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** A summarization chatbot can effectively read legal documents and generate concise versions that highlight key points. This directly addresses the requirement of extracting essential information, unlike the other options, which focus on different tasks.

</details>

### Q2.34 (`AIF-U0458`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A security company is using Amazon Bedrock to run foundation models (FMs). The company wants to ensure that only authorized users invoke the models. The company needs to identify any unauthorized access attempts to set appropriate AWS Identity and Access Management (IAM) policies and roles for future iterations of the FMs. Which AWS service should the company use to identify unauthorized users that are trying to access Amazon Bedrock?

- A) AWS Audit Manager
- B) AWS CloudTrail
- C) Amazon Fraud Detector
- D) AWS Trusted Advisor

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** AWS CloudTrail records API activity and provides a log of access attempts, which helps identify unauthorized users trying to access Amazon Bedrock. The other services are not specifically used for tracking unauthorized access attempts in this context.

</details>

### Q2.35 (`AIF-U0453`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to use AI to protect its application from threats. The AI solution needs to check if an IP address is from a suspicious source. Which solution meets these requirements?

- A) Build a speech recognition system.
- B) Create a natural language processing (NLP) named entity recognition system.
- C) Develop an anomaly detection system.
- D) Create a fraud forecasting system.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** An anomaly detection system can identify suspicious behavior, such as IP addresses that deviate from expected patterns, which helps in protecting the application from threats. The other options are not designed for detecting suspicious IP addresses.

</details>

### Q2.36 (`AIF-U0468`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which technique breaks a complex task into smaller subtasks that are sent sequentially to a large language model (LLM)?

- A) One-shot prompting
- B) Prompt chaining
- C) Tree of thoughts
- D) Retrieval Augmented Generation (RAG)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Prompt chaining involves breaking a complex task into smaller, manageable subtasks and passing them sequentially to a large language model. Each step builds upon the previous one, enabling more structured reasoning and improved task execution.

</details>

### Q2.37 (`AIF-U0460`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> In which stage of the generative AI model lifecycle are tests performed to examine the model's accuracy?

- A) Deployment
- B) Data selection
- C) Fine-tuning
- D) Evaluation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The evaluation stage is when you run tests and benchmarks, such as accuracy, precision, and other performance metrics, to measure how well the generative AI model performs on hold-out or validation data before moving on to deployment.

</details>

### Q2.38 (`AIF-U0459`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> An AI practitioner is using a large language model (LLM) to create content for marketing campaigns. The generated content sounds plausible and factual but is incorrect. Which problem is the LLM having?

- A) Data leakage
- B) Hallucination
- C) Overfitting
- D) Underfitting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** Hallucination occurs when a large language model generates content that appears plausible and factual but is incorrect or fabricated. This is a common issue with LLMs. The other options do not describe this particular behavior.

</details>

### Q2.39 (`AIF-U0449`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A company wants to classify human genes into 20 categories based on gene characteristics. The company needs an ML algorithm to document how the inner mechanism of the model affects the output. Which ML algorithm meets these requirements?

- A) Decision trees
- B) Linear regression
- C) Logistic regression
- D) Neural networks

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Decision trees provide clear transparency into how the model makes decisions, allowing easy documentation of how the inner mechanism influences the output. The other options do not offer this level of interpretability.

</details>

### Q2.40 (`AIF-U0470`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which term refers to the Instructions given to foundation models (FMs) so that the FMs provide a more accurate response to a question?

- A) Prompt
- B) Direction
- C) Dialog
- D) Translation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** A prompt is the input instruction or query you provide to a foundation model to guide its response, ensuring the model understands the task and delivers a more accurate answer.

</details>

### Q2.41 (`AIF-U0556`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is the primary difference between AI and ML?

- A) AI is a subset of ML
- B) ML is a subset of AI
- C) They are completely unrelated fields
- D) AI and ML are the same thing

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** ML is a subset of AI. The study guide mentions that understanding the similarities and differences between AI, ML, and deep learning is important. The main difference is that Artificial Intelligence (AI) is the broad concept of machines mimicking human intelligence, while Machine Learning (ML) is a subset of AI that specifically enables systems to learn from data and improve without explicit programming, acting as a core tool within the larger AI field. Think of AI as the whole universe of smart systems, and ML as one powerful way (using algorithms to find patterns) to build those systems, alongside other AI approaches like expert systems or rule-based logi

</details>

### Q2.42 (`AIF-U0506`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to create an ML model to predict customer satisfaction. The company needs fully automated model tuning. IT meets these requirements? Which AWS service

- A) Amazon Personalize
- B) Amazon SageMaker
- C) Amazon Athena
- D) Amazon Comprehend

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon SageMaker provides a fully managed environment for building, training, and deploying machine learning models, including automatic model tuning. Specifically, SageMaker includes a feature called Automatic Model Tuning (or Hyperparameter Optimization), which automates the process of finding the best hyperparameters for your machine learning model. This is essential when you want to optimize the model’s performance without manual intervention. Amazon SageMaker allows you to automate the training process and hyperparameter tuning, which aligns perfectly with the company's need for fully automated model tuning.

</details>

### Q2.43 (`AIF-U0479`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company has developed an ML model to predict real estate sale prices. The company wants to deploy the model to make predictions without managing servers or infrastructure. Which solution meets these requirements?

- A) Deploy the model on an Amazon EC2 instance.
- B) Deploy the model on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster.
- C) Deploy the model by using Amazon CloudFront with an Amazon S3 integration.
- D) Deploy the model by using an Amazon SageMaker endpoint.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** Amazon SageMaker provides a fully managed service for deploying machine learning models at scale without needing to manage servers or infrastructure. When you deploy a model using Amazon SageMaker endpoints, it handles all the infrastructure, scaling, and maintenance aspects. This allows the company to focus solely on making predictions and integrating the model into their application, without worrying about managing servers or clusters. Amazon SageMaker simplifies the deployment of ML models by providing scalable, secure, and serverless endpoints, which are ideal for serving predictions in real-time.

</details>

### Q2.44 (`AIF-U0579`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which strategy will determine if a foundation model (FM) effectively meets business objectives?

- A) Evaluate the model's performance on benchmark datasets.
- B) Analyze the model's architecture and hyperparameters.
- C) Assess the model's alignment with specific use cases.
- D) Measure the computational resources required for model deployment.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** To determine if a foundation model (FM) effectively meets business objectives, the key is to assess how well the model aligns with the specific use cases or business goals it is intended to address. This involves evaluating whether the model can provide meaningful and accurate outputs relevant to the business’s needs, ensuring that it solves the real-world problems the company aims to tackle. Aligning with specific use cases ensures that the model’s capabilities are tailored to the tasks at hand, such as improving customer support, enhancing decision-making, or automating certain processes.

</details>

### Q2.45 (`AIF-U0486`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A company is building a mobile app for users who have a visual impairment. The app must be able to hear what users say and provide voice responses. Which solution will meet these requirements?

- A) Use a deep learning neural network to perform speech recognition.
- B) Build ML models to search for patterns in numeric data.
- C) Use generative AI summarization to generate human-like text.
- D) Build custom models for image classification and recognition.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** To meet the requirements of enabling the app to "hear what users say and provide voice responses," the solution must include speech recognition and text-to-speech capabilities. Using a deep learning neural network for speech recognition allows the app to convert spoken words into text. Once the input is understood, text-to-speech systems can provide voice responses back to users. This approach is fundamental in applications that assist users with visual impairments by enabling interaction through spoken language.

</details>

### Q2.46 (`AIF-U0514`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A company’s large language model (LLM) is experiencing hallucinations. How can the company decrease hallucinations?

- A) Set up Agents for Amazon Bedrock to supervise the model training.
- B) Use data pre-processing and remove any data that causes hallucinations.
- C) Decrease the temperature inference parameter for the model.
- D) Use a foundation model (FM) that is trained to not hallucinate.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_inference_parameters_temp_top_p`  
**Explanation:** In the context of large language models (LLMs), the temperature inference parameter controls the randomness of the model's output. Lowering the temperature reduces randomness and makes the model's responses more deterministic and focused on the most likely predictions. By decreasing the temperature, the likelihood of hallucinations (when the model generates incorrect or nonsensical information) is reduced, as the model relies more on high-probability outputs rather than exploring less likely possibilities.

</details>

### Q2.47 (`AIF-U0520`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A global financial company has developed an ML application to analyze stock market data and provide stock market trends. The company wants to continuously monitor the application development phases and to ensure that company policies and industry regulations are followed. Which AWS services will help the company assess compliance requirements? (Choose 2)

- A) AWS Audit Manager
- B) AWS Config
- C) Amazon Inspector
- D) Amazon CloudWatch
- E) AWS CloudTrail

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, B`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** AWS Audit Manager helps organizations continuously assess and audit compliance with industry regulations and internal policies by automating evidence collection and generating audit reports. This is essential for ensuring that the ML application meets regulatory requirements. AWS Config enables continuous monitoring and compliance checks by tracking configuration changes in AWS resources. It helps the company ensure that infrastructure settings align with security policies and industry standards.

</details>

### Q2.48 (`AIF-U0577`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which prompting attack directly exposes the configured behavior of a large language model (LLM)?

- A) Prompted persona switches
- B) Exploiting friendliness and trust
- C) Ignoring the prompt template
- D) Extracting the prompt template

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** "Extracting the prompt template" is a type of prompting attack that involves directly exposing the configured behavior or the underlying system prompt of a large language model (LLM). This attack can reveal sensitive details about how the model operates, including its internal instructions or restrictions, which are typically not intended to be disclosed to the user. Such an exposure can compromise the security and reliability of the LLM by making it vulnerable to further exploitation or misuse.

</details>

### Q2.49 (`AIF-U0496`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company needs to monitor the performance of its ML systems by using a highly scalable AWS service. Which AWS service meets these requirements?

- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) AWS Trusted Advisor
- D) AWS Config

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** Amazon CloudWatch is a highly scalable AWS service designed for monitoring and observability. It provides real-time monitoring of system metrics, including performance data for ML systems, such as resource utilization (CPU, memory, etc.), model inference latency, request counts, and errors. CloudWatch enables users to set up alarms, visualize metrics, and automate actions based on performance thresholds, making it ideal for monitoring the performance of ML systems.

</details>

### Q2.50 (`AIF-U0507`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A company wants to deploy a conversational chatbot to answer customer questions. The chatbot is based on a fine-tuned Amazon SageMaker JumpStart model. The application must comply with multiple regulatory frameworks. Which capabilities can the company show compliance for? (Choose 2)

- A) Auto scaling inference endpoints
- B) Threat detection
- C) Data protection
- D) Cost optimization
- E) Loosely coupled microservices

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B, C`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Threat detection: Ensuring security measures are in place to detect threats is important for compliance with regulatory frameworks. Data protection: Proper data handling and protection measures are key compliance aspects, especially in applications dealing with sensitive customer information. The other options (auto scaling, cost optimization, and loosely coupled microservices) are more related to performance and architecture rather than regulatory compliance.

</details>

### Q2.51 (`AIF-U0553`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is the primary advantage of using Amazon Aurora with pgvector for AI applications?

- A) It provides serverless computing capabilities
- B) It enables vector similarity search within a relational database
- C) It automatically generates AI models
- D) It provides pre-trained language models

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Amazon Aurora with pgvector enables vector similarity search operations within a relational database, allowing organizations to: - Store embeddings alongside structured data - Perform vector similarity searches using SQL - Maintain ACID compliance while working with vector data - Scale vector operations efficiently **Task Reference**: Referenced in Task Statement 3.1 as one of the AWS services that help store embeddings within databases.

</details>

### Q2.52 (`AIF-U0491`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company is testing the security of a foundation model (FM). During testing, the company wants to get around the safety features and make harmful content. Which security technique is this an example of?

- A) Fuzzing training data to find vulnerabilities
- B) Denial of service (DoS)
- C) Penetration testing with authorization
- D) Jailbreak

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:prompt_management_and_risks`  
**Explanation:** "Jailbreaking" refers to attempts to bypass or disable the built-in safety features and restrictions of a system, in this case, a foundation model (FM). This technique involves trying to circumvent the safeguards that prevent the model from generating harmful or unsafe content. Jailbreaking is often performed to exploit vulnerabilities in a model’s filtering or safety protocols, making it a direct attempt to undermine its protections.

</details>

### Q2.53 (`AIF-U0526`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A media company wants to analyze viewer behavior and demographics to recommend personalized content. The company wants to deploy a customized ML model in its production environment. The company also wants to observe if the model quality drifts over time. Which AWS service or feature meets these requirements?

- A) Amazon Rekognition
- B) Amazon SageMaker Clarify
- C) Amazon Comprehend
- D) Amazon SageMaker Model Monitor

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon SageMaker Model Monitor continuously tracks deployed ML models in production to detect data drift, model drift, and quality degradation over time. This is essential for ensuring that the recommendation model remains accurate as viewer behavior and demographics change. Model Monitor helps detect anomalies and provides alerts when model performance deviates from expected trends, allowing the company to take corrective action.

</details>

### Q2.54 (`AIF-U0499`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company notices that its foundation model (FM) generates images that are unrelated to the prompts. The company wants to modify the prompt techniques to decrease unrelated images. Which solution meets these requirements?

- A) Use zero-shot prompts.
- B) Use negative prompts.
- C) Use positive prompts.
- D) Use ambiguous prompts.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** Negative prompts are used to explicitly instruct the model about what to avoid or not generate. By providing the model with specific guidance on what is not desired (e.g., by including terms or concepts that should not appear in the image), the model can better focus on generating relevant and related content. This technique can help reduce unrelated or irrelevant images by constraining the model's creative generation process.

</details>

### Q2.55 (`AIF-U0536`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> An AI practitioner trained a custom model on Amazon Bedrock by using a training dataset that contains confidential data. The AI practitioner wants to ensure that the custom model does not generate inference responses based on confidential data. How should the AI practitioner prevent responses based on confidential data?

- A) Delete the custom model. Remove the confidential data from the training dataset. Retrain the custom
- B) Mask the confidential data in the inference responses by using dynamic data masking.
- C) Encrypt the confidential data in the inference responses by using Amazon SageMaker.
- D) Encrypt the confidential data in the custom model by using AWS Key Management Service (AWS KMS).

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** To ensure that the custom model does not generate responses based on confidential data, the best approach is to retrain the model without including the confidential data. This prevents the model from learning patterns associated with that sensitive information, thereby avoiding its use in inference. The other options do not address the root cause of the issue—removing confidential data from the training process.

</details>

### Q2.56 (`AIF-U0570`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which features make Amazon Kendra most valuable for enterprise search applications? (Choose 2)

- A) Natural language understanding
- B) Website hosting capabilities
- C) Semantic search functionality
- D) Email server functionality
- E) Network monitoring

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** Amazon Kendra provides advanced search capabilities through: - Natural language understanding that interprets user intent - Semantic search that understands context and meaning - Integration with enterprise data sources - Learning from user interactions and feedback **Task Reference**: This service is mentioned in Task Statement 1.2 under AWS managed AI services, particularly for intelligent search applications.

</details>

### Q2.57 (`AIF-U0512`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A company wants to use Amazon Bedrock. The company needs to review which security aspects the company is responsible for when using Amazon Bedrock. Which security aspect will the company be responsible for?

- A) Patching and updating the versions of Amazon Bedrock
- B) Protecting the infrastructure that hosts Amazon Bedrock
- C) Securing the company's data in transit and at rest
- D) Provisioning Amazon Bedrock within the company network

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** According to the AWS Shared Responsibility Model, AWS manages the security of the cloud, including the infrastructure and services like Amazon Bedrock. Customers are responsible for security in the cloud, which encompasses protecting their data, managing access controls, and configuring security settings for their applications. Reference: https://aws.amazon.com/compliance/shared-responsibility-model/?nc1=h_ls

</details>

### Q2.58 (`AIF-U0576`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> Which parameters are commonly used for controlling the output diversity in generative AI models? (Choose 2)

- A) Top-k sampling
- B) Model size
- C) Top-p (nucleus) sampling
- D) Training dataset size
- E) Hardware configuration

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:fm_inference_parameters_temp_top_p`  
**Explanation:** Top-k and Top-p sampling are key parameters for controlling output generation: - Top-k limits token selection to the k most likely next tokens - Top-p (nucleus) sampling selects from tokens that sum to probability p Both help balance between diversity and quality of generated content. **Task Reference**: These concepts relate to Task Statement 3.1 regarding inference parameters' effects on model responses.

</details>

### Q2.59 (`AIF-U0513`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> A company wants to use large language models (LLMs) to produce code from natural language code comments. Which LLM feature meets these requirements?

- A) Text summarization
- B) Text generation
- C) Text completion
- D) Text classification

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Text generation is the feature of large language models (LLMs) that enables them to produce text based on a given prompt or input. In this scenario, the input would be natural language code comments, and the LLM would generate code based on those comments. This process involves understanding the context of the comment and generating corresponding code, which is the core functionality of text generation.

</details>

### Q2.60 (`AIF-U0495`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A company needs to build its own large language model (LLM) based on only the company's private data. The company is concerned about the environmental effect of the training process. Which Amazon EC2 instance type has the LEAST environmental effect when training LLMs?

- A) Amazon EC2 C series
- B) Amazon EC2 G series
- C) Amazon EC2 P series
- D) Amazon EC2 Trn series

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:rai_principles_and_sustainability`  
**Explanation:** Amazon EC2 Trn series instances (powered by AWS Trainium chips) are designed to provide efficient and environmentally friendly training of large machine learning models. They are optimized for energy efficiency, which reduces the environmental impact of the training process. The other instance types are not specifically optimized for minimizing environmental effects during training.

</details>

### Q2.61 (`AIF-U0530`) — 2.3 AWS GenAI Infrastructure, Services & Cost Tradeoffs
> A social media company wants to prevent users from posting discriminatory content on the company's application. The company wants to use Amazon Bedrock as part of the solution. How can the company use Amazon Bedrock to meet these requirements?

- A) Give users the ability to interact based on user preferences.
- B) Block interactions related to predefined topics.
- C) Restrict user conversations to predefined topics.
- D) Provide a variety of responses to select from for user engagement.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Amazon Bedrock’s built-in content moderation lets you define categories or keywords (e.g., hate speech, discriminatory language) and automatically block or filter any user inputs or outputs that fall under those topics. By configuring Bedrock’s safety filters with your predefined “disallowed” categories, the application will prevent discriminatory content from ever being posted.

</details>

### Q2.62 (`AIF-U0529`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A retail store wants to predict the demand for a specific product for the next few weeks by using the Amazon SageMaker DeepAR forecasting algorithm. Which type of data will meet this requirement?

- A) Text data
- B) Image data
- C) Time series data
- D) Binary data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_2_core_concept`  
**Explanation:** The Amazon SageMaker DeepAR forecasting algorithm is specifically designed for forecasting scalar (onedimensional) time series data using recurrent neural networks (RNNs). It excels when trained on datasets containing hundreds of related time series, enabling it to learn patterns across multiple series and provide accurate forecasts. Reference:

</details>

### Q2.63 (`AIF-U0548`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> How does top-p (nucleus) sampling differ from traditional temperature-based sampling?

- A) It samples from the smallest possible token set
- B) It selectively samples from tokens that sum to probability p
- C) It always produces deterministic output
- D) It only works with specific model architectures

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_inference_parameters_temp_top_p`  
**Explanation:** Top-p (nucleus) sampling: - Dynamically selects tokens based on cumulative probability - More adaptive than fixed temperature or top-k approaches - Balances quality and diversity - Helps prevent unlikely token combinations **Task Reference**: This relates to Task Statement 3.1 regarding inference parameters and their effects on model outputs.

</details>

### Q2.64 (`AIF-U0477`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company has developed a generative AI model for customer segmentation. The model has been deployed in the company's production environment for a long time. The company recently noticed some inconsistency in the model's responses. The company wants to evaluate model bias and drift. Which AWS service or feature meets these requirements?

- A) Amazon SageMaker Model Monitor
- B) Amazon SageMaker Clarify
- C) Amazon SageMaker Model Cards
- D) Amazon SageMaker Feature Store

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** SageMaker Model Monitor continuously collects inference and ground-truth data to automatically detect data drift, concept drift, and bias shifts in production models. By configuring baseline metrics and thresholds, the company can track inconsistencies in responses over time and receive alerts whenever bias or drift exceed acceptable limits.

</details>

### Q2.65 (`AIF-U0474`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company has a foundation model (FM) that was customized by using Amazon Bedrock to answer customer queries about products. The company wants to validate the model's responses to new types of queries. The company needs to upload a new dataset that Amazon Bedrock can use for validation. Which AWS service meets these requirements?

- A) Amazon S3
- B) Amazon Elastic Block Store (Amazon EBS)
- C) Amazon Elastic File System (Amazon EFS)
- D) AWS Snowcone

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon S3 is the most suitable AWS service for uploading and storing datasets used for validation purposes. It is highly scalable and integrated with Amazon Bedrock, allowing easy access to data for model validation. The other options do not provide the same level of integration or suitability for managing datasets in this context.

</details>

### Q2.66 (`AIF-U0504`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company wants to create a new solution by using AWS Glue. The company has minimal programming experience with AWS Glue. Which AWS service can help the company use AWS Glue?

- A) Amazon Q Developer
- B) AWS Config
- C) Amazon Personalize
- D) Amazon Comprehend

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon Q Developer is a tool designed to help users with minimal programming experience to work with AWS Glue. It provides a graphical user interface and simplifies the creation of data transformation and extraction workflows, allowing users to perform tasks like querying and working with data without needing deep coding skills.

</details>

### Q2.67 (`AIF-U0560`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> What is the purpose of Amazon SageMaker Model Monitor?

- A) To train models faster
- B) To detect data drift and model performance degradation
- C) To serve models for inference
- D) To create training datasets

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** Amazon SageMaker Model Monitor continuously monitors deployed machine learning models in production. It detects data drift, model drift, bias drift, and feature distribution changes. This helps ensure that model performance remains reliable over time and alerts teams when retraining or investigation is needed.

</details>

### Q2.68 (`AIF-U0522`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A healthcare company wants to analyze patient data. The data was gathered over the previous year to detect patterns in disease outbreaks. The company needs to create a trend analysis report for each month to present to public health officials. The company must provide insights into patient data from the most recent month of the current year. Which inference method will meet these requirements MOST cost-effectively?

- A) Real-time inference
- B) Batch transform
- C) Serverless inference
- D) Asynchronous inference

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_inference_modes`  
**Explanation:** Batch transform is the most cost-effective inference method for analyzing large amounts of data collected over a period (such as monthly patient data). It allows you to process and generate reports on all historical data in batches, rather than incurring the higher costs of real-time or serverless inference.

</details>

### Q2.69 (`AIF-U0498`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company needs to use Amazon SageMaker for model training and inference. The company must comply with regulatory requirements to run SageMaker jobs in an isolated environment without internet access. Which solution will meet these requirements?

- A) Run SageMaker training and inference by using SageMaker Experiments.
- B) Run SageMaker training and inference by using network isolation.
- C) Encrypt the data at rest by using encryption for SageMaker geospatial capabilities.
- D) Associate appropriate AWS Identity and Access Management (IAM) roles with the SageMaker jobs.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** Network isolation in Amazon SageMaker allows you to run training and inference jobs in an environment that does not have access to the internet. This helps ensure that the data and the model do not inadvertently access external resources, meeting regulatory compliance requirements for isolated environments.

</details>

### Q2.70 (`AIF-U0487`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A company is building an ML model to analyze archived data. The company must perform inference on large datasets that are multiple GBs in size. The company does not need to access the model predictions immediately. Which Amazon SageMaker inference option will meet these requirements?

- A) Batch transform
- B) Real-time inference
- C) Serverless inference
- D) Asynchronous inference

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_inference_modes`  
**Explanation:** Batch transform is ideal for processing large datasets that do not require real-time predictions. It allows the company to perform inference on multiple GBs of data efficiently without needing immediate results. The other options are more suitable for scenarios requiring real-time or near real-time access.

</details>

### Q2.71 (`AIF-U0538`) — 2.2 GenAI Capabilities, Limitations & Business Value Metrics
> An ecommerce company is using a chatbot to automate the customer order submission process. The chatbot is powered by AI and is available to customers directly from the company's website 24 hours a day, 7 days a week. Which option is an AI system input vulnerability that the company needs to resolve before the chatbot is made available?

- A) Data leakage
- B) Prompt injection
- C) Large language model (LLM) hallucinations
- D) Concept drift

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Prompt injection is an input-level attack where a user crafts malicious input to override or manipulate the chatbot’s instructions or behavior. Addressing this vulnerability by sanitizing and constraining user prompts ensures the chatbot won’t execute unintended or harmful instructions when it goes live.

</details>

### Q2.72 (`AIF-U0515`) — 2.1 Foundational GenAI, Context Engineering & Agentic AI/MCP
> A design company is using a foundation model (FM) on Amazon Bedrock to generate images for various projects. The company wants to have control over how detailed or abstract each generated image appears Which model parameter should the company modify?

- A) Model checkpoint
- B) Batch size
- C) Generation step
- D) Token length

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** The “generation step” parameter controls how detailed or abstract an image appears during generation. By adjusting the number of generation steps, you can influence the level of refinement and detail in the output more steps yield more detailed images, while fewer steps result in more abstract images.

</details>

## Domain 3: Applications of Foundation Models (28% — 84 Questions)

### Q3.01 (`AIF-U1089`) — 3.4 FM & AI Application Performance Evaluation
> An organization wants to evaluate open-ended responses generated by a customer-support LLM for helpfulness, correctness, and tone at scale without hiring a large team of human reviewers for every test run. Which automated evaluation approach is best suited for this?

- A) BLEU score only
- B) LLM-as-a-judge
- C) Confusion matrix
- D) Mean Absolute Error (MAE)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_evaluation_metrics_rouge_bleu_bertscore`  
**Explanation:** LLM-as-a-judge uses a strong evaluator foundation model (supported in Amazon Bedrock Model Evaluation) to score open-ended outputs on nuanced criteria like correctness, faithfulness, and helpfulness at scale.

</details>

### Q3.02 (`AIF-U1060`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company uses a large, highly accurate Foundation Model in Amazon Bedrock for customer ticket classification, but inference latency and per-token costs are too high at production volume. They want a smaller, faster, cheaper model that preserves similar accuracy for this specific task. Which customization technique should they use?

- A) Pre-training a new foundation model from scratch
- B) Model distillation
- C) Increasing the temperature parameter to 1.0
- D) Switching to Amazon S3 Glacier

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_customization_spectrum_and_distillation`  
**Explanation:** Model distillation transfers task-specific knowledge from a large, high-performing Teacher model into a smaller, faster, lower-cost Student model, significantly reducing latency and inference cost.

</details>

### Q3.03 (`AIF-U1081`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A team maintains dozens of prompts across development, staging, and production environments in Amazon Bedrock and needs centralized versioning, testing, and rollback of prompt templates. Which feature should they use?

- A) Amazon Bedrock Prompt Management
- B) AWS CloudTrail
- C) Amazon SageMaker Clarify
- D) AWS Data Exchange

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon Bedrock Prompt Management enables teams to create, version, test, compare, and deploy reusable prompt templates across environments without hardcoding prompts into application code.

</details>

### Q3.04 (`AIF-U1082`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> An AI application sends a 20,000-token static company policy document and system instructions in every API request to Amazon Bedrock, changing only the short user question at the end. Which feature reduces both input token costs and latency without changing the model?

- A) Continued pre-training
- B) Prompt caching
- C) Top-K sampling
- D) Batch transform

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_inference_modes`  
**Explanation:** Prompt caching caches repeated static prompt prefixes (such as long system instructions or reference documents) across requests, reducing input token costs and time-to-first-token latency.

</details>

### Q3.05 (`AIF-U1100`) — 3.4 FM & AI Application Performance Evaluation
> Which automated metric uses contextual embeddings from a pre-trained transformer to measure semantic similarity between generated text and a reference text, rather than relying only on exact surface n-gram matches?

- A) ROUGE-1
- B) BLEU
- C) BERTScore
- D) RMSE

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_evaluation_metrics_rouge_bleu_bertscore`  
**Explanation:** BERTScore computes semantic similarity using contextual embeddings, capturing paraphrases and meaning even when exact words differ, whereas ROUGE and BLEU rely on exact n-gram overlap.

</details>

### Q3.06 (`AIF-U1012`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which feature of Amazon OpenSearch Service gives companies the ability to build vector database applications?

- A) Integration with Amazon S3 for object storage
- B) Support for geospatial indexing and queries
- C) Scalable index management and nearest neighbor search capability
- D) Ability to perform real-time analysis on streaming data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Amazon OpenSearch Service (formerly Amazon Elasticsearch Service) has introduced capabilities to support vector search, which allows companies to build vector database applications. This is particularly useful in machine learning, where vector representations (embeddings) of data are often used to capture semantic meaning.Scalable index management and nearest neighbor search capability are the core features enabling vector database functionalities in OpenSearch. The service allows users to index high-dimensional vectors and perform efficient nearest neighbor searches, which are crucial for tasks such as recommendation systems, anomaly detection, and semantic search.Here is why option C is the correct answer:Scalable Index Management: OpenSearch Service supports scalable indexing of vector data. This means you can index a large volume of high-dimensional vectors and manage these indexes in a cost-effective and performance-optimized way. The service leverages underlying AWS infrastructure to ensure that indexing scales seamlessly with data size.Nearest Neighbor Search Capability: OpenSearch Service ' s nearest neighbor search capability allows for fast and efficient searches over vector data. This is essential for applications like product recommendation engines, where the system needs to quickly find the most similar items based on a user ' s query or behavior.AWS AI Practitioner References:According to AWS documentation, OpenSearch Service ' s support for nearest neighbor search using vector embeddings is a key feature for companies building machine learning applications that require similarity search.The service uses Approximate Nearest Neighbors (ANN) algorithms to speed up searches over large datasets, ensuring high performance even with large-scale vector data.The other options do not directly relate to building vector database applications:A. Integration with Amazon S3 for object storage is about storing data objects, not vector-based searching or indexing.B. Support for geospatial indexing and queries is related to location-based data, not vectors used in machine learning.D. Ability to perform real-time analysis on streaming data relates to analyzing incoming data streams, which is different from the vector search capabilities.

</details>

### Q3.07 (`AIF-U1005`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company has petabytes of unlabeled customer data to use for an advertisement campaign. The company wants to classify its customers into tiers to advertise and promote the company ' s products.Which methodology should the company use to meet these requirements?

- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Reinforcement learning from human feedback (RLHF)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Unsupervised learning is the correct methodology for classifying customers into tiers when the data is unlabeled, as it does not require predefined labels or outputs.Unsupervised Learning:This type of machine learning is used when the data has no labels or pre-defined categories. The goal is to identify patterns, clusters, or associations within the data.In this case, the company has petabytes of unlabeled customer data and needs to classify customers into different tiers. Unsupervised learning techniques like clustering (e.g., K-Means, Hierarchical Clustering) can group similar customers based on various attributes without any prior knowledge or labels.Why Option B is Correct:Handling Unlabeled Data: Unsupervised learning is specifically designed to work with unlabeled data, making it ideal for the company’s need to classify customer data.Customer Segmentation: Techniques in unsupervised learning can be used to find natural groupings within customer data, such as identifying high-value vs. low-value customers or segmenting based on purchasing behavior.Why Other Options are Incorrect:A. Supervised learning: Requires labeled data with input-output pairs to train the model, which is not suitable since the company ' s data is unlabeled.C. Reinforcement learning: Focuses on training an agent to make decisions by maximizing some notion of cumulative reward, which does not align with the company ' s need for customer classification.D. Reinforcement learning from human feedback (RLHF): Similar to reinforcement learning but involves human feedback to refine the model’s behavior; it is also not appropriate for classifying unlabeled customer data.

</details>

### Q3.08 (`AIF-U1006`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is building a solution to generate images for protective eyewear. The solution must have high accuracy and must minimize the risk of incorrect annotations.Which solution will meet these requirements?

- A) Human-in-the-loop validation by using Amazon SageMaker Ground Truth Plus
- B) Data augmentation by using an Amazon Bedrock knowledge base
- C) Image recognition by using Amazon Rekognition
- D) Data summarization by using Amazon QuickSight

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Amazon SageMaker Ground Truth Plus is a managed data labeling service that includes human-in-the-loop (HITL) validation. This solution ensures high accuracy by involving human reviewers to validate the annotations and reduce the risk of incorrect annotations.Amazon SageMaker Ground Truth Plus:It allows for the creation of high-quality training datasets with human oversight, which minimizes errors in labeling and increases accuracy.Human-in-the-loop workflows help verify the correctness of annotations, ensuring that generated images for protective eyewear meet high-quality standards.Why Option A is Correct:High Accuracy: Human-in-the-loop validation provides the ability to catch and correct errors in annotations, ensuring high-quality data.Minimized Risk of Incorrect Annotations: Human review adds a layer of quality assurance, which is especially important in use cases like generating precise images for protective eyewear.Why Other Options are Incorrect:B. Amazon Bedrock: Does not offer a knowledge base for data augmentation; it focuses on running foundation models.C. Amazon Rekognition: Provides image recognition and analysis, not a solution for minimizing annotation errors.D. Amazon QuickSight: A data visualization tool, not relevant to image annotation or generation tasks.Thus, A is the correct answer for generating high-accuracy images with minimized annotation risks.

</details>

### Q3.09 (`AIF-U1009`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company wants to use a large language model (LLM) on Amazon Bedrock for sentiment analysis. The company wants to classify the sentiment of text passages as positive or negative.Which prompt engineering strategy meets these requirements?

- A) Provide examples of text passages with corresponding positive or negative labels in the prompt followed by the new text passage to be classified.
- B) Provide a detailed explanation of sentiment analysis and how LLMs work in the prompt.
- C) Provide the new text passage to be classified without any additional context or examples.
- D) Provide the new text passage with a few examples of unrelated tasks, such as text summarization or question answering.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Providing examples of text passages with corresponding positive or negative labels in the prompt followed by the new text passage to be classified is the correct prompt engineering strategy for using a large language model (LLM) on Amazon Bedrock for sentiment analysis.Example-Driven Prompts:This strategy, known as few-shot learning, involves giving the model examples of input-output pairs (e.g., text passages with their sentiment labels) to help it understand the task context.It allows the model to learn from these examples and apply the learned pattern to classify new text passages correctly.Why Option A is Correct:Guides the Model: Providing labeled examples teaches the model how to perform sentiment analysis effectively, increasing accuracy.Contextual Relevance: Aligns the model ' s responses to the specific task of classifying sentiment.Why Other Options are Incorrect:B. Detailed explanation of sentiment analysis: Unnecessary for the model ' s operation; it requires examples, not explanations.C. New text passage without context: Provides no guidance or learning context for the model.D. Unrelated task examples: Would confuse the model and lead to inaccurate results.

</details>

### Q3.10 (`AIF-U1010`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> An AI practitioner has built a deep learning model to classify the types of materials in images. The AI practitioner now wants to measure the model performance.Which metric will help the AI practitioner evaluate the performance of the model?

- A) Confusion matrix
- B) Correlation matrix
- C) R2 score
- D) Mean squared error (MSE)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** A confusion matrix is the correct metric for evaluating the performance of a classification model, such as the deep learning model built to classify types of materials in images.Confusion Matrix:It is a table used to describe the performance of a classification model by comparing the actual and predicted classifications.Provides detailed insights into the model’s performance, including true positives, true negatives, false positives, and false negatives.Why Option A is Correct:Performance Measurement: Helps measure various performance metrics like accuracy, precision, recall, and F1-score, which are critical for evaluating a classification model.Comprehensive Evaluation: Allows for a thorough analysis of where the model is making errors and the types of errors being made.Why Other Options are Incorrect:B. Correlation matrix: Used to identify relationships between variables, not for evaluating classification performance.C. R2 score: Used for regression models, not classification.D. Mean squared error (MSE): Also a metric for regression, measuring the average of the squares of the errors.

</details>

### Q3.11 (`AIF-U1008`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is using a pre-trained large language model (LLM) to build a chatbot for product recommendations. The company needs the LLM outputs to be short and written in a specific language.Which solution will align the LLM response quality with the company ' s expectations?

- A) Adjust the prompt.
- B) Choose an LLM of a different size.
- C) Increase the temperature.
- D) Increase the Top K value.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Adjusting the prompt is the correct solution to align the LLM outputs with the company ' s expectations for short, specific language responses.Adjust the Prompt:Modifying the prompt can guide the LLM to produce outputs that are shorter and tailored to the desired language.A well-crafted prompt can provide specific instructions to the model, such as " Answer in a short sentence in Spanish. "Why Option A is Correct:Control Over Output: Adjusting the prompt allows for direct control over the style, length, and language of the LLM outputs.Flexibility: Prompt engineering is a flexible approach to refining the model’s behavior without modifying the model itself.Why Other Options are Incorrect:B. Choose an LLM of a different size: The model size does not directly impact the response length or language.C. Increase the temperature: Increases randomness in responses but does not ensure brevity or specific language.D. Increase the Top K value: Affects diversity in model output but does not align directly with response length or language specificity.

</details>

### Q3.12 (`AIF-U1013`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which metric measures the runtime efficiency of operating AI models?

- A) Customer satisfaction score (CSAT)
- B) Training time for each epoch
- C) Average response time
- D) Number of training instances

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** The average response time is the correct metric for measuring the runtime efficiency of operating AI models.Average Response Time:Refers to the time taken by the model to generate an output after receiving an input. It is a key metric for evaluating the performance and efficiency of AI models in production.A lower average response time indicates a more efficient model that can handle queries quickly.Why Option C is Correct:Measures Runtime Efficiency: Directly indicates how fast the model processes inputs and delivers outputs, which is critical for real-time applications.Performance Indicator: Helps identify potential bottlenecks and optimize model performance.Why Other Options are Incorrect:A. Customer satisfaction score (CSAT): Measures customer satisfaction, not model runtime efficiency.B. Training time for each epoch: Measures training efficiency, not runtime efficiency during model operation.D. Number of training instances: Refers to data used during training, not operational efficiency.

</details>

### Q3.13 (`AIF-U1014`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which statement presents an advantage of using Retrieval Augmented Generation (RAG) for natural language processing (NLP) tasks?

- A) RAG can use external knowledge sources to generate more accurate and informative responses
- B) RAG is designed to improve the speed of language model training
- C) RAG is primarily used for speech recognition tasks
- D) RAG is a technique for data augmentation in computer vision tasks

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Retrieval-Augmented Generation (RAG) integrates external knowledge sources (databases, vector stores, document repositories) with LLMs, enabling them to generate contextually accurate and up-to-date responses without retraining.B is incorrect: RAG does not speed up training; it improves inference results.C is incorrect: speech recognition is not an RAG use case.D is incorrect: computer vision augmentation is unrelated to RAG.???? Reference:AWS Documentation – Knowledge Bases for RAG in Amazon Bedrock

</details>

### Q3.14 (`AIF-U1007`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is building an AI application to summarize books of varying lengths. During testing, the application fails to summarize some books. Why does the application fail to summarize some books?

- A) The temperature is set too high.
- B) The selected model does not support fine-tuning.
- C) The Top P value is too high.
- D) The input tokens exceed the model ' s context size.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Foundation models have a context window (max tokens), which limits the size of the input text (prompt + instructions).If the input (e.g., a very long book) exceeds this limit, the model cannot process it, causing failure.Temperature (A) and Top P (C) control randomness, not input size.Fine-tuning (B) is irrelevant to input truncation failures.???? Reference:AWS Documentation – Amazon Bedrock Model Parameters (context size limits)

</details>

### Q3.15 (`AIF-U1011`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> An AI practitioner wants to use a foundation model (FM) to design a search application. The search application must handle queries that have text and images. Which type of FM should the AI practitioner use to power the search application?

- A) Multi-modal embedding model
- B) Text embedding model
- C) Multi-modal generation model
- D) Image generation model

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** A multi-modal embedding model can handle both text and image queries by embedding them into a shared space, enabling the search application to process and relate different data types. The other options are not suitable for handling both text and image inputs effectively.

</details>

### Q3.16 (`AIF-U1026`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> An AI practitioner needs to improve the accuracy of a natural language generation model. The model uses rapidly changing inventory data.Which technique will improve the model ' s accuracy?

- A) Transfer learning
- B) Federated learning
- C) Retrieval Augmented Generation (RAG)
- D) One-shot prompting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** The requirement is to improve the accuracy of a natural language generation (NLG) model that relies on rapidly changing inventory data. Let’s evaluate the options:A. Transfer learning: This involves pre-training a model on a large dataset and fine-tuning it for a specific task. While effective for general model improvement, it does not specifically address the challenge of incorporating rapidly changing inventory data into the model’s responses.B. Federated learning: This technique trains models across decentralized devices while keeping data localized, primarily for privacy purposes. It is not designed to handle rapidly changing data or improve NLG model accuracy in this context.C. Retrieval Augmented Generation (RAG): RAG combines a language model with a retrieval mechanism that fetches relevant, up-to-date information (e.g., inventory data) from an external source during inference. This is ideal for scenarios with dynamic data, as it ensures the model’s responses are grounded in the latest information, improving accuracy.D. One-shot prompting: This involves providing a single example to guide the model’s output. While useful for specific tasks, it does not scale well for rapidly changing data or ensure consistent accuracy with dynamic inventory updates.Exact Extract Reference: According to AWS documentation on generative AI techniques, “Retrieval Augmented Generation (RAG) enhances large language models by retrieving relevant documents or data at inference time, enabling the model to generate accurate and contextually relevant responses, especially for dynamic or frequently updated datasets.” (Source: AWS Generative AI Glossary, https://aws.amazon.com/what-is/retrieval-augmented-generation/). This directly addresses the need for accuracy with rapidly changing inventory data. RAG is the most suitable technique for this scenario, as it allows the model to access and incorporate the latest inventory data, making C the correct answer.

</details>

### Q3.17 (`AIF-U1023`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company wants to enhance response quality for a large language model (LLM) for complex problem-solving tasks. The tasks require detailed reasoning and a step-by-step explanation process.Which prompt engineering technique meets these requirements?

- A) Few-shot prompting
- B) Zero-shot prompting
- C) Directional stimulus prompting
- D) Chain-of-thought prompting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** The company wants to enhance the response quality of an LLM for complex problem-solving tasks requiring detailed reasoning and step-by-step explanations. Chain-of-thought prompting encourages the LLM to break down the problem into intermediate steps, providing a clear reasoning process before arriving at the final answer, which is ideal for this requirement.Exact Extract from AWS AI Documents:From the AWS Bedrock User Guide:" Chain-of-thought prompting improves the reasoning capabilities of large language models by encouraging them to break down complex tasks into intermediate steps, providing a step-by-step explanation that leads to the final answer. This technique is particularly effective for problem-solving tasks requiring detailed reasoning. "(Source: AWS Bedrock User Guide, Prompt Engineering Techniques)Detailed Explanation:Option A: Few-shot promptingFew-shot prompting provides a few examples to guide the LLM but does not explicitly encourage step-by-step reasoning or detailed explanations.Option B: Zero-shot promptingZero-shot prompting relies on the LLM’s pre-trained knowledge without examples, making it less effective for complex tasks requiring detailed reasoning.Option C: Directional stimulus promptingDirectional stimulus prompting is not a standard technique in AWS documentation, likely a distractor, and does not address step-by-step reasoning.Option D: Chain-of-thought promptingThis is the correct answer. Chain-of-thought prompting enhances response quality for complex tasks by guiding the LLM to reason step-by-step, providing detailed explanations.

</details>

### Q3.18 (`AIF-U1016`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is developing an ML model to predict heart disease risk. The model uses patient data, such as age, cholesterol, blood pressure, smoking status, and exercise habits. The dataset includes a target value that indicates whether a patient has heart disease.Which ML technique will meet these requirements?

- A) Unsupervised learning
- B) Supervised learning
- C) Reinforcement learning
- D) Semi-supervised learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** This scenario describes a classic supervised learning problem. Supervised learning involves training a model on a labeled dataset where the correct output (also called the target variable or ground truth) is already known. In this case, the company has a dataset containing features such as age, cholesterol, and exercise habits, and a label indicating whether a patient has heart disease or not. This matches the definition of a binary classification task, which is a type of supervised learning. According to the AWS Machine Learning Specialty Study Guide, supervised learning is most effective when labels are available for all training examples, and the goal is to map input variables to a known output. This method enables the model to learn patterns and predict the presence or absence of heart disease. By contrast, unsupervised learning is used when labels are not available, and reinforcement learning involves agents learning via rewards and punishments, which is not applicable here. Semi-supervised learning is used when only some data is labeled.Referenced AWS AI/ML Documents and Study Guides:AWS Certified Machine Learning Specialty Guide – Supervised vs. Unsupervised LearningAmazon SageMaker Documentation – Classification Models

</details>

### Q3.19 (`AIF-U1024`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company wants to use a pre-trained generative AI model to generate content for its marketing campaigns. The company needs to ensure that the generated content aligns with the company ' s brand voice and messaging requirements.Which solution meets these requirements?

- A) Optimize the model ' s architecture and hyperparameters to improve the model ' s overall performance.
- B) Increase the model ' s complexity by adding more layers to the model ' s architecture.
- C) Create effective prompts that provide clear instructions and context to guide the model ' s generation.
- D) Select a large, diverse dataset to pre-train a new generative model.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:rai_sagemaker_clarify_bias_shap`  
**Explanation:** Creating effective prompts is the best solution to ensure that the content generated by a pre-trained generative AI model aligns with the company ' s brand voice and messaging requirements.Effective Prompt Engineering:Involves crafting prompts that clearly outline the desired tone, style, and content guidelines for the model.By providing explicit instructions in the prompts, the company can guide the AI to generate content that matches the brand’s voice and messaging.Why Option C is Correct:Guides Model Output: Ensures the generated content adheres to specific brand guidelines by shaping the model ' s response through the prompt.Flexible and Cost-effective: Does not require retraining or modifying the model, which is more resource-efficient.Why Other Options are Incorrect:A. Optimize the model ' s architecture and hyperparameters: Improves model performance but does not specifically address alignment with brand voice.B. Increase model complexity: Adding more layers may not directly help with content alignment.D. Pre-training a new model: Is a costly and time-consuming process that is unnecessary if the goal is content alignment.

</details>

### Q3.20 (`AIF-U1019`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company is using few-shot prompting on a base model that is hosted on Amazon Bedrock. The model currently uses 10 examples in the prompt. The model is invoked once daily and is performing well. The company wants to lower the monthly cost.Which solution will meet these requirements?

- A) Customize the model by using fine-tuning.
- B) Decrease the number of tokens in the prompt.
- C) Increase the number of tokens in the prompt.
- D) Use Provisioned Throughput.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Decreasing the number of tokens in the prompt reduces the cost associated with using an LLM model on Amazon Bedrock, as costs are often based on the number of tokens processed by the model.Token Reduction Strategy:By decreasing the number of tokens (words or characters) in each prompt, the company reduces the computational load and, therefore, the cost associated with invoking the model.Since the model is performing well with few-shot prompting, reducing token usage without sacrificing performance can lower monthly costs.Why Option B is Correct:Cost Efficiency: Directly reduces the number of tokens processed, lowering costs without requiring additional adjustments.Maintaining Performance: If the model is already performing well, a reduction in tokens should not significantly impact its performance.Why Other Options are Incorrect:A. Fine-tuning: Can be costly and time-consuming and is not needed if the current model is already performing well.C. Increase the number of tokens: Would increase costs, not lower them.D. Use Provisioned Throughput: Is unrelated to token costs and applies more to read/write capacity in databases.

</details>

### Q3.21 (`AIF-U1031`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which of the following are considered business metrics for AI model evaluation?

- A) Precision score
- B) Customer satisfaction score
- C) Mean Average Precision
- D) Time-to-value
- E) Root Mean Square Error

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B, D`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Customer satisfaction score measures how well an AI solution meets end user needs and directly reflects the value delivered to the business, while time-to-value measures how quickly the AI solution begins delivering measurable business outcomes, making both examples of business metrics used to assess whether an AI model is meeting organizational objectives. Precision score is a technical model performance metric that measures the proportion of positive predictions that are actually correct (true positives divided by all positive predictions), not a business outcome measure. Mean Average Precision is a technical evaluation metric used in information retrieval and object detection tasks to quantify how well a model ranks relevant results, measuring accuracy across ranked outputs rather than business value. Root Mean Square Error is a regression metric that measures the average magnitude of prediction errors by taking the square root of the mean of squared differences between predicted and actual values, again a technical performance measure rather than an indicator of business impact.

</details>

### Q3.22 (`AIF-U1018`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is making a chatbot. The chatbot uses Amazon Lex and Amazon OpenSearch Service. The chatbot uses the company ' s private data to answer questions. The company needs to convert the data into a vector representation before storing the data in a database.Which model type should the company use?

- A) Text completion model
- B) Instruction following model
- C) Text embeddings model
- D) Image generation model

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** The correct answer is Text embeddings model, which transforms input text into dense vector representations. These vectors preserve semantic meaning and are ideal for similarity search, retrieval-augmented generation (RAG), and semantic search use cases, especially with Amazon OpenSearch Service. According to AWS Bedrock documentation, embeddings models are specifically designed to map text into a numerical space where related concepts are placed closer together. This allows efficient querying and ranking of documents based on the user’s question. This step is critical in chatbots using private knowledge bases. Text completion and instruction-following models focus on generating or following tasks, not producing embeddings. Image generation models are irrelevant here. Therefore, using a text embeddings model ensures that the chatbot retrieves contextually relevant results from stored vectors.Referenced AWS AI/ML Documents and Study Guides:Amazon Bedrock Developer Guide – Text Embeddings ModelsAWS ML Specialty Guide – Semantic Search and Vector Databases

</details>

### Q3.23 (`AIF-U1030`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> Which ML technique uses training data that is labeled with the correct output values?

- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Transfer learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Supervised learning trains models on datasets where each input example is paired with a known correct output label, allowing the model to learn the mapping between inputs and targets and make predictions on new unseen data. Unsupervised learning works with entirely unlabeled data and discovers hidden patterns or groupings without any known output values to learn from. Reinforcement learning does not use labeled training data at all, instead training an agent to take actions in an environment by rewarding desirable outcomes and penalising undesirable ones. Transfer learning is a technique where a model pre-trained on one task is adapted for a different task, which is about reusing existing model knowledge rather than describing how training data is structured.

</details>

### Q3.24 (`AIF-U1032`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which of the following is NOT a type of machine learning?

- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Diagnostic learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Diagnostic learning is not a recognized type of machine learning and does not appear in the AI/ML literature or the AWS exam guide, making it the option that does not belong among the established ML learning paradigms. Supervised learning, unsupervised learning, and reinforcement learning are the three primary types of machine learning. Supervised learning trains models on labeled datasets where each input is paired with a known correct output. Unsupervised learning discovers hidden patterns in unlabeled data without any predefined output values to learn from. Reinforcement learning trains an agent to make sequential decisions by rewarding desirable behaviors and penalising undesirable ones.

</details>

### Q3.25 (`AIF-U1017`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is implementing intelligent agents to provide conversational search experiences for its customers. The company needs a database service that will support storage and queries of embeddings from a generative AI model as vectors in the database. Which AWS service will meet these requirements?

- A) Amazon Athena
- B) Amazon Aurora PostgreSQL
- C) Amazon Redshift
- D) Amazon EMR

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Amazon Aurora PostgreSQL is a relational database service that supports a wide range of applications, including those that require vector-based operations. Specifically, Aurora PostgreSQL can be extended with vector search capabilities using extensions like pgvector. This extension allows you to store, index, and query vector embeddings from generative AI models, making it well-suited for the company's needs to store and query embeddings as vectors. pgvector is an extension for PostgreSQL that provides efficient similarity search for vector data, which is ideal for storing and querying embeddings.

</details>

### Q3.26 (`AIF-U1033`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which statement correctly describes embeddings in generative AI?

- A) Embeddings search data to find the most helpful information for answering natural-language questions
- B) Embeddings lower hardware requirements by using a less precise data type for weights and activations
- C) Embeddings represent data as high-dimensional vectors that capture semantic relationships
- D) Embeddings store and retrieve data for generative AI applications

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Embeddings map inputs such as words or documents into high-dimensional vectors where semantic similarity corresponds to closeness in the vector space, letting models reason about meaning and relationships. Searching data to find helpful information describes retrieval, as in RAG. Reducing hardware needs with a less precise data type describes quantization. Storing and retrieving data describes a database or vector store, not embeddings themselves.

</details>

### Q3.27 (`AIF-U1015`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A bank is building a chatbot to answer customer questions about opening a bank account. The chatbot will use public bank documents to generate responses. The company will use Amazon Bedrock and prompt engineering to improve the chatbot ' s responses.Which prompt engineering technique meets these requirements?

- A) Complexity-based prompting
- B) Zero-shot prompting
- C) Few-shot prompting
- D) Directional stimulus prompting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** Directional stimulus prompting guides the foundation model to produce outputs aligned with business context. It’s particularly effective for aligning responses with public documents and improving coherence. From Bedrock Prompt Engineering Techniques documentation:“Directional stimulus prompting provides structured prompts to steer the model output towards desired formats or behaviors using specific linguistic cues.”

</details>

### Q3.28 (`AIF-U1029`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which AWS service is designed specifically for developing generative AI applications?

- A) Amazon EC2
- B) Amazon Bedrock
- C) Amazon S3
- D) Amazon RDS

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon Bedrock is purpose-built for generative AI, providing access to foundation models and tools to build and scale generative AI applications. Amazon EC2 provides general compute, Amazon S3 provides object storage, and Amazon RDS provides managed relational databases; none is specifically designed for developing generative AI applications.

</details>

### Q3.29 (`AIF-U1021`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company needs to choose a model from Amazon Bedrock to use internally. The company must identify a model that generates responses in a style that the company's employees prefer. What should the company do to meet these requirements?

- A) Evaluate the models by using built-in prompt datasets.
- B) Evaluate the models by using a human workforce and custom prompt datasets.
- C) Use public model leaderboards to identify the model.
- D) Use the model InvocationLatency runtime metrics in Amazon CloudWatch when trying models.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Evaluating models using a human workforce and custom prompt datasets ensures that the model generates responses in the style that aligns with the company’s preferences. The other options either do not provide direct feedback on style preferences or are not specific enough for determining suitability based on employee preferences.

</details>

### Q3.30 (`AIF-U1022`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company wants to assess the costs that are associated with using a large language model (LLM) to generate inferences. The company wants to use Amazon Bedrock to build generative AI applications. Which factor will drive the inference costs?

- A) Number of tokens consumed
- B) Temperature value
- C) Amount of data used to train the LLM
- D) Total training time

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Inference costs for large language models are typically driven by the number of tokens processed during input and output, as each token incurs computational resources. The other factors (temperature value, training data, and training time) do not directly impact inference costs.

</details>

### Q3.31 (`AIF-U1025`) — 3.4 FM & AI Application Performance Evaluation
> A research group wants to test different generative AI models to create research papers. The research group has defined a prompt and needs a method to assess the models' output. The research group wants to use a team of scientists to perform the output assessments. Which solution will meet these requirements?

- A) Use automatic evaluation on Amazon Personalize.
- B) Use content moderation on Amazon Rekognition.
- C) Use model evaluation on Amazon Bedrock.
- D) Use sentiment analysis on Amazon Comprehend.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon Bedrock provides model evaluation capabilities, allowing a team of scientists to manually assess and compare the outputs of different generative AI models based on defined prompts and criteria. This meets the requirement for human-in-the-loop model output evaluation.

</details>

### Q3.32 (`AIF-U1027`) — 3.4 FM & AI Application Performance Evaluation
> An education company is building a chatbot whose target audience is teenagers. The company is training a custom large language model (LLM). The company wants the chatbot to speak in the target audience’s language style by using creative spelling and shortened words. Which metric will assess the LLM’s performance?

- A) F1 score
- B) BERTScore
- C) Recall-Oriented Understudy for Gisting Evaluation (ROUGE)
- D) Bilingual Evaluation Understudy (BLEU) score

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:fm_evaluation_metrics_rouge_bleu_bertscore`  
**Explanation:** BLEU evaluates surface-level n-gram overlap between the LLM’s outputs and reference examples—in this case, targets written in creative spelling and shorthand, making it well suited to measure how closely the model’s style matches the teenager-oriented language.

</details>

### Q3.33 (`AIF-U1028`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> What is the benefit of fine-tuning a foundation model (FM)?

- A) Fine-tuning reduces the FM's size and complexity and enables slower inference.
- B) Fine-tuning uses specific training data to retrain the FM from scratch to adapt to a specific use case.
- C) Fine-tuning keeps the FM's knowledge up to date by pre-training the FM on more recent data.
- D) Fine-tuning improves the performance of the FM on a specific task by further training the FM on new labeled data.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** By updating the model’s weights with task-relevant examples, fine-tuning sharpens its understanding of domain-specific language and objectives, yielding higher accuracy and relevance on that particular task.

</details>

### Q3.34 (`AIF-U1034`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> Which technique involves training AI models on labeled datasets to adapt the models to specific industry terminology and requirements?

- A) Data augmentation
- B) Fine-tuning
- C) Model quantization
- D) Continuous pre-training

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Fine-tuning takes a pre-trained model and continues training it on a labeled, domain-specific dataset so the model learns industry terminology and task nuances directly from that specialized data.

</details>

### Q3.35 (`AIF-U1020`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company is using supervised learning to train an AI model on a small labeled dataset that is specific to a target task. Which step of the foundation model (FM) lifecycle does this describe?

- A) Fine-tuning
- B) Data selection
- C) Pre-training
- D) Evaluation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Fine-tuning is the process of training a pre-existing foundation model on a smaller, labeled dataset that is specific to a target task, allowing the model to adapt to the company's requirements.

</details>

### Q3.36 (`AIF-U1064`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company wants to develop an AI application to help its employees check open customer claims, identify details for a specific claim, and access documents for a claim. Which solution meets these requirements?

- A) Use Agents for Amazon Bedrock with Amazon Fraud Detector to build the application.
- B) Use Agents for Amazon Bedrock with Amazon Bedrock knowledge bases to build the application.
- C) Use Amazon Personalize with Amazon Bedrock knowledge bases to build the application.
- D) Use Amazon SageMaker to build the application by training a new ML model.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon Bedrock is a service that allows you to build AI-powered applications using foundation models (FMs) without managing infrastructure. Agents for Amazon Bedrock allows you to create intelligent agents that can help users interact with data and perform tasks such as checking open customer claims, identifying claim details, and accessing relevant documents. By using Amazon Bedrock knowledge bases, the AI agent can access relevant information (e.g., details about claims, documents, or customer data) in real time, and provide precise, context-driven answers based on the claim-related data stored in the knowledge base. Agents for Amazon Bedrock can help automate interactions by understanding and responding to natural language queries, making it a good fit for this use case. Amazon Bedrock knowledge bases enable the system to access stored information, documents, and details for specific claims efficiently.

</details>

### Q3.37 (`AIF-U1096`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> What is the primary purpose of Amazon Q for Business?

- A) To train custom ML models
- B) To provide AI-powered business intelligence and assistance
- C) To store large datasets
- D) To monitor infrastructure

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Amazon Q for Business is an enterprise-grade, generative AI-powered assistant specifically designed for business use. It integrates with enterprise systems, applications, and data repositories to provide contextual assistance to employees. Key capabilities include: answering questions about company data and policies, generating content like emails and documents based on internal knowledge, providing summaries of documents and meetings, troubleshooting issues and offering solutions, assisting with software development tasks, all while respecting company security policies and access controls. Unlike general AI assistants, Q for Business is specifically trained on your organization's internal information and maintains privacy and security requirements, making it different from both standard ML training tools (A) and basic data storage (C) or monitoring (D) solutions.

</details>

### Q3.38 (`AIF-U1043`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company has fine-tuned a large language model (LLM) to answer questions for a help desk. The company wants to determine if the fine-tuning has enhanced the model's accuracy. Which metric should the company use for the evaluation?

- A) Precision
- B) Time to first token
- C) F1 score
- D) Word error rate

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The F1 score is a metric that combines precision and recall into a single value, providing a balance between the two. It is particularly useful in evaluating models where there is an uneven class distribution, as it considers both false positives and false negatives. The F1 score is calculated as the harmonic mean of precision and recall: This metric ranges from 0 to 1, with 1 indicating perfect precision and recall. In the context of evaluating a fine-tuned large language model (LLM) for a help desk application, the F1 score is appropriate because it assesses the model's ability to provide accurate and relevant responses, balancing the trade-off between precision (correctness of responses) and recall (completeness of relevant responses). Reference:

</details>

### Q3.39 (`AIF-U1106`) — 3.4 FM & AI Application Performance Evaluation
> Which metrics are commonly used to evaluate generative AI model performance? (Choose 2)

- A) BLEU score for translation quality
- B) CPU utilization
- C) ROUGE score for summarization quality
- D) Network latency
- E) Storage capacity

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:fm_evaluation_metrics_rouge_bleu_bertscore`  
**Explanation:** BLEU (Bilingual Evaluation Understudy) score (A) is the standard metric for evaluating machine translation quality. It measures the precision of n-grams (word sequences) in machine translations compared to reference human translations, with scores ranging from 0 to 1 (higher is better). ROUGE (Recall-Oriented Understudy for Gisting Evaluation) (C) evaluates summarization quality by measuring the overlap between generated summaries and reference summaries, focusing on recall (how much of the reference appears in the generated summary). In AWS, you can implement these metrics in custom evaluation tests within Amazon Bedrock Model Evaluation or SageMaker. Options B, D, and E are system performance metrics unrelated to output quality.

</details>

### Q3.40 (`AIF-U1071`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company wants to use a large language model (LLM) to generate concise, feature-specific descriptions for the company’s products. Which prompt engineering technique meets these requirements?

- A) Create one prompt that covers all products. Edit the responses to make the responses more specific, concise, and tailored to each product.
- B) Create prompts for each product category that highlight the key features. Include the desired output format and length for each prompt response.
- C) Include a diverse range of product features in each prompt to generate creative and unique descriptions.
- D) Provide detailed, product-specific prompts to ensure precise and customized descriptions.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_inference_parameters_temp_top_p`  
**Explanation:** To generate concise, feature-specific descriptions for each product, the company should create prompts tailored to specific product categories. By highlighting the key features of each product category in the prompt, the model can focus on generating descriptions that are relevant and aligned with the unique attributes of each product. Additionally, specifying the desired output format and length ensures that the responses meet the company's requirements for conciseness and clarity. Tailored prompts help ensure the model generates relevant and accurate descriptions by focusing on the most important features of each product category. Desired output format and length ensure the responses are consistent and concise, as required.

</details>

### Q3.41 (`AIF-U1053`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is introducing a mobile app that helps users learn foreign languages. The app makes text more coherent by calling a large language model (LLM). The company collected a diverse dataset of text and supplemented the dataset with examples of more readable versions. The company wants the LLM output to resemble the provided examples. Which metric should the company use to assess whether the LLM meets these requirements?

- A) Value of the loss function
- B) Semantic robustness
- C) Recall-Oriented Understudy for Gisting Evaluation (ROUGE) score
- D) Latency of the text generation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** ROUGE is a set of metrics that evaluates the quality of summaries by comparing the overlap of n-grams, word sequences, and word pairs between the model output and reference examples. Since the company is working on a language model that improves the coherence of text and wants the output to resemble the provided examples (which are more readable versions of the original text), ROUGE is the most appropriate metric. It assesses how closely the generated text matches the reference text in terms of content and readability. ROUGE score is commonly used to evaluate the performance of models in tasks like summarization, where the goal is to ensure the generated text aligns closely with human-provided examples.

</details>

### Q3.42 (`AIF-U1035`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A bank has fine-tuned a large language model (LLM) to expedite the loan approval process. During an external audit of the model, the company discovered that the model was approving loans at a faster pace for a specific demographic than for other demographics. How should the bank fix this issue MOST cost-effectively?

- A) Include more diverse training data. Fine-tune the model again by using the new data.
- B) Use Retrieval Augmented Generation (RAG) with the fine-tuned model.
- C) Use AWS Trusted Advisor checks to eliminate bias.
- D) Pre-train a new LLM with more diverse training data.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** The issue described is a case of bias in the model’s decision-making process, where the model is showing a preference for a specific demographic. The most cost-effective way to address this is to include more diverse training data that better represents all demographics. By fine-tuning the model with this more diverse data, you can help ensure that the model treats all demographic groups fairly and does not exhibit biased behavior. Fine-tuning the model with updated data ensures that the model learns from a more representative sample, improving fairness in its predictions without needing to completely retrain the model from scratch.

</details>

### Q3.43 (`AIF-U1077`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A publishing company built a Retrieval Augmented Generation (RAG) based solution to give its users the ability to interact with published content. New content is published daily. The company wants to provide a near real-time experience to users. Which steps in the RAG pipeline should the company implement by using offline batch processing to meet these requirements? (Choose two.)

- A) Generation of content embeddings
- B) Generation of embeddings for user queries
- C) Creation of the search index
- D) Retrieval of relevant content

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Generation of content embeddings New or updated documents can be converted to vector representations in periodic batches (e.g., hourly, nightly). Because a document’s embedding remains fixed until the document itself changes, this step does not have to run for every user query, making it ideal for offline processing. Creation of the search index After new embeddings are produced, the vector (or hybrid) index can be rebuilt or incrementally updated in batch mode. Index construction is computationally intensive but happens infrequently relative to user requests, so running it offline avoids adding latency to real-time interactions.

</details>

### Q3.44 (`AIF-U1037`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company deployed an AI/ML solution to help customer service agents respond to frequently asked questions. The questions can change over time. The company wants to give customer service agents the ability to ask questions and receive automatically generated answers to common customer questions. Which strategy will meet these requirements MOST cost-effectively?

- A) Fine-tune the model regularly.
- B) Train the model by using context data.
- C) Pre-train and benchmark the model by using context data.
- D) Use Retrieval Augmented Generation (RAG) with prompt engineering techniques.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Retrieval Augmented Generation (RAG) is a cost-effective approach that enhances AI-generated responses by retrieving relevant information from external knowledge sources. Instead of fine-tuning or re-training a model, RAG dynamically pulls the most recent and relevant data at query time. This is particularly useful in scenarios where questions change over time, ensuring that the AI/ML solution provides accurate and up-todate responses without requiring expensive and time-consuming model retraining. Prompt engineering techniques further optimize how the model processes and generates responses, improving accuracy and relevance.

</details>

### Q3.45 (`AIF-U1051`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is developing an ML model to predict customer churn. The model performs well on the training dataset but does not accurately predict churn for new data. Which solution will resolve this issue?

- A) Decrease the regularization parameter to increase model complexity.
- B) Increase the regularization parameter to decrease model complexity.
- C) Add more features to the input data.
- D) Train the model for more epochs.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** The issue described is a common case of overfitting, where the model performs well on the training data but fails to generalize to new, unseen data. This suggests that the model is too complex and has learned to memorize the training data rather than identifying generalizable patterns. Increasing the regularization parameter helps to reduce model complexity by penalizing large weights, thereby encouraging simpler models that are less likely to overfit. This will improve the model's ability to generalize to new data, potentially improving performance on unseen customer data.

</details>

### Q3.46 (`AIF-U1042`) — 3.4 FM & AI Application Performance Evaluation
> A company has developed a generative text summarization model by using Amazon Bedrock. The company will use Amazon Bedrock automatic model evaluation capabilities. Which metric should the company use to evaluate the accuracy of the model?

- A) Area Under the ROC Curve (AUC) score
- B) F1 score
- C) BERTScore
- D) Real world knowledge (RWK) score

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** BERTScore is a metric specifically designed for evaluating the quality of text generated by models, particularly in tasks like text summarization and machine translation. It uses contextual embeddings from a pre-trained BERT model to compare generated text with reference text at the word level, making it wellsuited for evaluating the accuracy of generative text summarization models. BERTScore assesses the semantic similarity between the generated text and the reference text, providing a more nuanced evaluation compared to traditional methods that focus on exact matches.

</details>

### Q3.47 (`AIF-U1068`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company wants to implement a large language model (LLM) based chatbot to provide customer service agents with real-time contextual responses to customers' inquiries. The company will use the company's policies as the knowledge base. Which solution will meet these requirements MOST cost-effectively?

- A) Retrain the LLM on the company policy data.
- B) Fine-tune the LLM on the company policy data.
- C) Implement Retrieval Augmented Generation (RAG) for in-context responses.
- D) Use pre-training and data augmentation on the company policy data.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Retrieval Augmented Generation (RAG) integrates external data sources with LLMs to produce accurate and contextually relevant outputs without the need for extensive retraining. By connecting the chatbot to the company's policy documents, RAG enables the model to retrieve pertinent information in real-time, ensuring responses are both accurate and up-to-date. This approach is cost-effective as it leverages existing data without the computational expenses associated with retraining or fine-tuning large models. Reference:

</details>

### Q3.48 (`AIF-U1083`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> An AI practitioner is developing a prompt for an Amazon Titan model. The model is hosted on Amazon Bedrock. The AI practitioner is using the model to solve numerical reasoning challenges. The AI practitioner adds the following phrase to the end of the prompt: “Ask the model to show its work by explaining its reasoning step by step.” Which prompt engineering technique is the AI practitioner using?

- A) Chain-of-thought prompting
- B) Prompt injection
- C) Few-shot prompting
- D) Prompt templating

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Chain-of-thought prompting is a technique in prompt engineering where the AI model is encouraged to break down its reasoning process step by step to solve a problem, such as numerical reasoning challenges. By explicitly instructing the model to "show its work by explaining its reasoning step by step," the practitioner ensures the model provides a logical sequence of intermediate steps leading to the solution. This improves the accuracy and transparency of the model's outputs, particularly for complex reasoning tasks.

</details>

### Q3.49 (`AIF-U1093`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> What is few-shot prompting?

- A) Training a model with limited data
- B) Including a small number of examples in the prompt to guide the response
- C) Using short prompts to save tokens
- D) Running inference with minimal compute resources by limiting output tokens

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** Few-shot prompting is a technique where you include a few examples of the desired input-output format directly in the prompt. This helps the model understand the expected response pattern without any training or fine-tuning. For example, showing 3 examples of sentiment classification before asking the model to classify a new text. Zero-shot uses no examples, one-shot uses one example. Exam tip: Few-shot prompting works well for consistent formatting, classification, and structured output generation.

</details>

### Q3.50 (`AIF-U1079`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A social media company wants to use a large language model (LLM) to summarize messages. The company has chosen a few LLMs that are available on Amazon SageMaker JumpStart. The company wants to compare the generated output toxicity of these models. Which strategy gives the company the ability to evaluate the LLMs with the LEAST operational overhead?

- A) Crowd-sourced evaluation
- B) Automatic model evaluation
- C) Model evaluation with human workers
- D) Reinforcement learning from human feedback (RLHF)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Automatic model evaluation is the strategy that allows the company to evaluate the LLMs with the least operational overhead. This method leverages automated tools and processes to assess the toxicity or quality of the generated output without the need for manual intervention or crowd-sourced input. By using pre-built evaluation metrics or toxicity detection models, the company can quickly and efficiently evaluate multiple models without the complexity and time required for human evaluations.

</details>

### Q3.51 (`AIF-U1085`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> An ecommerce company is using a generative AI chatbot to respond to customer inquiries. The company wants to measure the financial effect of the chatbot on the company’s operations. Which metric should the company use?

- A) Number of customer inquiries handled
- B) Cost of training AI models
- C) Cost for each customer conversation
- D) Average handled time (AHT)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** To measure the financial effect of a generative AI chatbot on the company's operations, the cost for each customer conversation is the most relevant metric. It directly quantifies the operational expense associated with using the chatbot to handle customer inquiries. By analyzing this metric, the company can evaluate how much it spends per conversation and compare it to the cost of alternative methods (e.g., human agents), providing insight into the chatbot's financial efficiency and ROI.

</details>

### Q3.52 (`AIF-U1074`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company’s employees provide product descriptions and recommendations to customers when customers call the customer service center. These recommendations are based on where the customers are located. The company wants to use foundation models (FMs) to automate this process. Which AWS service meets these requirements?

- A) Amazon Macie
- B) Amazon Transcribe
- C) Amazon Bedrock
- D) Amazon Textract

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_textract_ocr`  
**Explanation:** Amazon Bedrock enables companies to use foundation models (FMs) to build and automate tasks like generating product descriptions and recommendations. It allows the integration of pre-trained FMs into applications without managing infrastructure, making it an ideal choice for automating customer service tasks. With Amazon Bedrock, the company can leverage FMs to generate tailored recommendations based on customer locations, enabling dynamic and efficient customer interactions.

</details>

### Q3.53 (`AIF-U1056`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company is using a large language model (LLM) on Amazon Bedrock to build a chatbot. The chatbot processes customer support requests. To resolve a request, the customer and the chatbot must interact a few times. Which solution gives the LLM the ability to use content from previous customer messages?

- A) Turn on model invocation logging to collect messages.
- B) Add messages to the model prompt.
- C) Use Amazon Personalize to save conversation history.
- D) Use Provisioned Throughput for the LLM.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** To give a large language model (LLM) the ability to use content from previous customer messages in a conversation, the previous messages must be included in the model prompt. This technique is known as prompt engineering and allows the LLM to retain context by incorporating a history of the interaction within the prompt. By appending prior exchanges to the prompt, the model can generate contextually relevant and coherent responses throughout the multi-turn conversation.

</details>

### Q3.54 (`AIF-U1075`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A grocery store wants to create a chatbot to help customers find products in the store. The chatbot must check the inventory in real time and provide the product location in the store. Which prompt engineering technique should the store use to build the chatbot?

- A) Zero-shot prompting
- B) Few-shot prompting
- C) Least-to-most prompting
- D) Reasoning and acting (ReAct) prompting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** ReAct prompting interleaves the model’s chain-of-thought reasoning with explicit “actions” (such as calling your real-time inventory API), then uses the API response to inform its final answer. By structuring your prompts to have the LLM think, choose the “CheckInventory” action with the product name, receive the live location data, and then respond to the user, you seamlessly integrate real-time lookups and precise product locations into the chatbot’s replies.

</details>

### Q3.55 (`AIF-U1059`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is using Retrieval Augmented Generation (RAG) with Amazon Bedrock and Stable Diffusion to generate product images based on text descriptions. The results are often random and lack specific details. The company wants to increase the specificity of the generated images. Which solution meets these requirements?

- A) Increase the number of generation steps.
- B) Use the MASK_IMAGE_BLACK mask source option.
- C) Increase the classifier-free guidance (CFG) scale.
- D) Increase the prompt strength.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** In Stable Diffusion, the classifier-free guidance (CFG) scale parameter controls how closely the generated image adheres to the provided text prompt. By increasing the CFG scale, the model places more emphasis on the prompt, leading to images that more accurately reflect the specified details. However, it's important to balance this setting, as excessively high values can result in less diverse and potentially lowerquality images.

</details>

### Q3.56 (`AIF-U1095`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> What is the difference between zero-shot, one-shot, and few-shot learning in generative AI?

- A) They refer to different model architectures
- B) They refer to the number of examples provided in the prompt
- C) They refer to different training datasets
- D) They refer to different inference speeds

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** These terms describe how many examples are included in the prompt: - Zero-shot learning: No examples are provided, only instructions. - One-shot learning: One example is provided to guide the model. - Few-shot learning: A small number of examples (typically 2–5) are provided to establish a pattern for the model to follow. These techniques help influence output behavior without retraining the model.

</details>

### Q3.57 (`AIF-U1110`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> Which statements about model latent space are correct? (Choose 2)

- A) It represents the model's internal understanding of relationships
- B) It is only used for image processing
- C) It enables semantic similarities between different inputs
- D) It requires human supervision to maintain
- E) It must be stored in a specific database type

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:fm_training_finetuning_rlhf`  
**Explanation:** Model latent space: - Represents the model's internal understanding and organization of concepts - Enables computation of semantic similarities between different inputs - Facilitates transfer learning and generalization - Supports various types of data representations **Task Reference**: This concept is referenced in Task Statement 3.2 under concepts of prompt engineering and model architecture.

</details>

### Q3.58 (`AIF-U1086`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> An ecommerce company wants to build a solution to determine customer sentiments based on written customer reviews of products. Which AWS services meet these requirements? (Choose 2)

- A) Amazon Lex
- B) Amazon Comprehend
- C) Amazon Polly
- D) Amazon Bedrock
- E) Amazon Rekognition

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B, D`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon Comprehend: This service is specifically designed for natural language processing (NLP) tasks, including sentiment analysis, making it ideal for analyzing customer reviews. Amazon Bedrock: Bedrock can be used to leverage foundation models, which can also be employed for sentiment analysis tasks. The other options are not suitable for sentiment analysis of written customer reviews.

</details>

### Q3.59 (`AIF-U1080`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A software company builds tools for customers. The company wants to use AI to increase software development productivity. Which solution will meet these requirements?

- A) Use a binary classification model to generate code reviews.
- B) Install code recommendation software in the company's developer tools.
- C) Install a code forecasting tool to predict potential code issues.
- D) Use a natural language processing (NLP) tool to generate code.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Natural language processing (NLP) tools can be used to generate code from high-level descriptions or suggestions, which can greatly enhance software development productivity. By leveraging NLP models, developers can automate repetitive coding tasks, generate code snippets, or even complete blocks of code based on natural language inputs. This can speed up development and reduce errors.

</details>

### Q3.60 (`AIF-U1091`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> What are the primary use cases for storing embeddings in a vector database like Amazon OpenSearch Service? (Choose 2)

- A) Semantic search implementation
- B) Website content management
- C) Similarity-based recommendations
- D) Email routing
- E) Network traffic analysis

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Vector databases are essential for: - Implementing semantic search by finding similar vectors - Building recommendation systems based on content similarity - Supporting RAG (Retrieval Augmented Generation) - Enabling efficient nearest neighbor search at scale **Task Reference**: This aligns with Task Statement 3.1 regarding vector database applications and RAG implementations.

</details>

### Q3.61 (`AIF-U1105`) — 3.4 FM & AI Application Performance Evaluation
> Which metric is used to evaluate the performance of foundation models (FMs) for text summarization tasks?

- A) F1 score
- B) Bilingual Evaluation Understudy (BLEU) score
- C) Accuracy
- D) Mean squared error (MSE)

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Text summarization quality is most commonly assessed using ROUGE metrics, which report recall, precision, and an F1-score that balances the two. The ROUGE-F1 (often simply called the F1 score in this context) measures how well the model’s summary overlaps with reference summaries, making it the standard choice for evaluating foundation models on summarization tasks.

</details>

### Q3.62 (`AIF-U1046`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company is building a chatbot to improve user experience. The company is using a large language model (LLM) from Amazon Bedrock for intent detection. The company wants to use few-shot learning to improve intent detection accuracy. Which additional data does the company need to meet these requirements?

- A) Pairs of chatbot responses and correct user intents
- B) Pairs of user messages and correct chatbot responses
- C) Pairs of user messages and correct user intents
- D) Pairs of user intents and correct chatbot responses

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Few-shot learning involves providing the model with a few examples to help it understand how to perform the task. For intent detection, the company needs pairs of user messages and the correct user intents, which will help the LLM improve its accuracy in detecting user intents. The other options do not provide the necessary pairing for improving intent detection.

</details>

### Q3.63 (`AIF-U1039`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company has a generative AI application that uses a pre-trained foundation model (FM) on Amazon Bedrock. The company wants the FM to include more context by using company information. Which solution meets these requirements MOST cost-effectively?

- A) Use Amazon Bedrock Knowledge Bases.
- B) Choose a different FM on Amazon Bedrock.
- C) Use Amazon Bedrock Agents.
- D) Deploy a custom model on Amazon Bedrock.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Amazon Bedrock Knowledge Bases let you index and retrieve your company’s documents at inference time, injecting relevant context into the pre-trained FM’s prompts without the cost or complexity of re-training or fine-tuning a custom model. This retrieval-augmented approach delivers up-to-date, domain-specific information in responses while keeping costs low.

</details>

### Q3.64 (`AIF-U1102`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which capabilities of Amazon OpenSearch Service are most relevant for AI/ML workloads? (Choose 2)

- A) Vector similarity search with k-NN
- B) Website hosting
- C) Vector database functionality
- D) Email processing
- E) Log analysis

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Amazon OpenSearch Service provides essential capabilities for AI/ML workloads through: - Vector similarity search (k-NN) for efficient similarity-based queries - Vector database functionality for storing and querying embeddings **Task Reference**: This is covered in Task Statement 3.1 regarding services for storing embeddings within vector databases.

</details>

### Q3.65 (`AIF-U1070`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A company wants to improve the accuracy of the responses from a generative AI application. The application uses a foundation model (FM) on Amazon Bedrock. Which solution meets these requirements MOST cost-effectively?

- A) Fine-tune the FM.
- B) Retrain the FM.
- C) Train a new FM.
- D) Use prompt engineering.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Using prompt engineering is the most cost-effective way to improve the accuracy of responses from a generative AI application without retraining or fine-tuning the foundation model (FM). Prompt engineering involves carefully designing the input prompts to guide the model toward producing better responses, improving relevance and accuracy.

</details>

### Q3.66 (`AIF-U1104`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> Which features of Amazon Aurora with pgvector are most important for AI applications? (Choose 2)

- A) Vector similarity search capabilities
- B) Traditional SQL operations
- C) Integration with structured data
- D) Web hosting features
- E) Email processing

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Key features include: - Vector similarity search for finding related content - Ability to combine traditional structured data with vector operations - SQL interface for vector operations - Scalable vector storage and querying **Task Reference**: This relates to Task Statement 3.1 regarding storage and querying of embeddings in databases.

</details>

### Q3.67 (`AIF-U1065`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company wants to fine-tune a foundation model (FM) by using AWS services. The company needs to ensure that its data stays private, safe, and secure in the source AWS Region where the data is stored. Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

- A) Host the model on premises by using AWS Outposts.
- B) Use the Amazon Bedrock API.
- C) Use AWS PrivateLink and a VPC.
- D) Host the Amazon Bedrock API on premises.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** Use the Amazon Bedrock API: You’ll call Bedrock’s managed fine-tuning endpoints directly in your AWS Region, so your data never leaves that region. Use AWS PrivateLink and a VPC: Front Bedrock API traffic through a VPC endpoint via PrivateLink to keep all network traffic on the AWS backbone and within your account’s private network.

</details>

### Q3.68 (`AIF-U1073`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company wants to use large language models (LLMs) with Amazon Bedrock to develop a chat interface for the company's product manuals. The manuals are stored as PDF files. Which solution meets these requirements MOST cost-effectively?

- A) Use prompt engineering to add one PDF file as context to the user prompt when the prompt is submitted to Amazon Bedrock.
- B) Use prompt engineering to add all the PDF files as context to the user prompt when the prompt is submitted to Amazon Bedrock.
- C) Use all the PDF documents to fine-tune a model with Amazon Bedrock. Use the fine-tuned model to process user prompts.
- D) Upload PDF documents to an Amazon Bedrock knowledge base. Use the knowledge base to provide context when users submit prompts to Amazon Bedrock

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Using an Amazon Bedrock knowledge base allows the model to efficiently access relevant information from the PDF manuals when needed, reducing the cost compared to continuously fine-tuning a model or providing all PDFs as context in each prompt. This approach ensures that only necessary context is provided, making it cost-effective.

</details>

### Q3.69 (`AIF-U1054`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company is introducing a new feature for its application. The feature will refine the style of output messages. The company will fine-tune a large language model (LLM) on Amazon Bedrock to implement the feature. Which type of data does the company need to meet these requirements?

- A) Samples of only input messages
- B) Samples of only output messages
- C) Samples of pairs of input and output messages
- D) Separate samples of input and output messages

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Fine-tuning a large language model to refine the style of output messages requires training data consisting of paired input and output messages. These pairs allow the model to learn the relationship between the input provided and the desired styled output, ensuring the fine-tuned model produces responses with the intended style.

</details>

### Q3.70 (`AIF-U1076`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A large retailer receives thousands of customer support inquiries about products every day. The customer support inquiries need to be processed quickly. The company wants to implement Agents for Amazon Bedrock. What are the key benefits of using Amazon Bedrock agents that could help this retailer?

- A) Generation of custom foundation models (FMs) to predict customer needs
- B) Automation of repetitive tasks and orchestration of complex workflows
- C) Automatically calling multiple foundation models (FMs) and consolidating the results
- D) Selecting the foundation model (FM) based on predefined criteria and metrics

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon Bedrock agents help automate repetitive tasks and orchestrate complex workflows, which is ideal for handling thousands of customer support inquiries efficiently. This helps reduce response times and improves productivity. The other options do not directly address automation and orchestration of tasks for customer support.

</details>

### Q3.71 (`AIF-U1058`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is using an Amazon Titan foundation model (FM) in Amazon Bedrock. The company needs to supplement the model by using relevant data from the company's private data sources. Which solution will meet this requirement?

- A) Use a different FM.
- B) Choose a lower temperature value.
- C) Create an Amazon Bedrock knowledge base.
- D) Enable model invocation logging.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Creating an Amazon Bedrock knowledge base allows the company to supplement the foundation model with relevant data from their private data sources. This ensures that the model has access to the additional, context-specific information needed. The other options do not directly address supplementing the model with private data.

</details>

### Q3.72 (`AIF-U1087`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> An education provider is building a question and answer application that uses a generative AI model to explain complex concepts. The education provider wants to automatically change the style of the model response depending on who is asking the question. The education provider will give the model the age range of the user who has asked the question. Which solution meets these requirements with the LEAST implementation effort?

- A) Fine-tune the model by using additional training data that is representative of the various age ranges
- B) Add a role description to the prompt context that instructs the model of the age range that the response
- C) Use chain-of-thought reasoning to deduce the correct style and complexity for a response suitable for
- D) Summarize the response text depending on the age of the user so that younger users receive shorter

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** Adding a role description to the prompt is the simplest and most effective way to adjust the model's response style based on the user's age range. It requires minimal implementation effort and effectively tailors the output. The other options involve more complex processes, such as fine-tuning or additional reasoning steps.

</details>

### Q3.73 (`AIF-U1040`) — 3.4 FM & AI Application Performance Evaluation
> A company has built a solution by using generative AI. The solution uses large language models (LLMs) to translate training manuals from English into other languages. The company wants to evaluate the accuracy of the solution by examining the text generated for the manuals. Which model evaluation strategy meets these requirements?

- A) Bilingual Evaluation Understudy (BLEU)
- B) Root mean squared error (RMSE)
- C) Recall-Oriented Understudy for Gisting Evaluation (ROUGE)
- D) F1 score

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** The BLEU (Bilingual Evaluation Understudy) score is a common metric used to evaluate the accuracy of machine translation by comparing the generated translation with reference translations. It is specifically designed for translation tasks, whereas the other metrics are not suitable for evaluating translation quality.

</details>

### Q3.74 (`AIF-U1078`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> A research company implemented a chatbot by using a foundation model (FM) from Amazon Bedrock. The chatbot searches for answers to questions from a large database of research papers. After multiple prompt engineering attempts, the company notices that the FM is performing poorly because of the complex scientific terms in the research papers. How can the company improve the performance of the chatbot?

- A) Use few-shot prompting to define how the FM can answer the questions.
- B) Use domain adaptation fine-tuning to adapt the FM to complex scientific terms.
- C) Change the FM inference parameters.
- D) Clean the research paper data to remove complex scientific terms.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Domain adaptation fine-tuning allows the FM to better understand the complex scientific terms by training it with domain-specific data, improving its performance on such specialized content. The other options are either insufficient or not directly related to handling complex terminology effectively.

</details>

### Q3.75 (`AIF-U1109`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> Which scenario describes a potential risk and limitation of prompt engineering in the context of a generative AI model?

- A) Prompt engineering does not ensure that the model always produces consistent and deterministic outputs, eliminating the need for validation.
- B) Prompt engineering could expose the model to vulnerabilities such as prompt injection attacks.
- C) Properly designed prompts reduce but do not eliminate the risk of data poisoning or model hijacking.
- D) Prompt engineering does not ensure that the model will consistently generate highly reliable outputs when working with real-world data.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_inference_parameters_temp_top_p`  
**Explanation:** A key risk in prompt engineering is prompt injection, where attackers manipulate input prompts to alter a model's behavior or produce unintended outputs. This vulnerability arises from the model's sensitivity to input structure and content, making it a critical limitation in secure prompt design.

</details>

### Q3.76 (`AIF-U1045`) — 3.4 FM & AI Application Performance Evaluation
> A company has set up a translation tool to help its customer service team handle issues from customers around the world. The company wants to evaluate the performance of the translation tool. The company sets up a parallel data process that compares the responses from the tool to responses from actual humans. Both sets of responses are generated on the same set of documents. Which strategy should the company use to evaluate the translation tool?

- A) Use the Bilingual Evaluation Understudy (BLEU) score to estimate the absolute translation quality of the two methods.
- B) Use the Bilingual Evaluation Understudy (BLEU) score to estimate the relative translation quality of the two methods.
- C) Use the BERTScore to estimate the absolute translation quality of the two methods.
- D) Use the BERTScore to estimate the relative translation quality of the two methods.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_evaluation_metrics_rouge_bleu_bertscore`  
**Explanation:** BLEU measures n-gram overlap between a candidate translation and one or more reference translations. When you apply it to both the tool’s outputs and the human outputs on the same source documents, you get comparable scores that let you directly assess which approach yields better translations.

</details>

### Q3.77 (`AIF-U1061`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company wants to build an AI assistant to provide responses to user queries. The AI assistant must evaluate specific data sources, query external APIs, generate response options, and compare and prioritize response options. Which Amazon Bedrock feature or resource will meet these requirements?

- A) Prompt Management
- B) Response streaming
- C) Knowledge Bases
- D) Agents

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon Bedrock Agents enable AI assistants to interact with specific data sources, query external APIs, generate and compare response options, and prioritize results, making them the ideal feature for building advanced, task-oriented chatbots with decision-making and orchestration capabilities.

</details>

### Q3.78 (`AIF-U1041`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company has created a custom model by fine-tuning an existing large language model (LLM) from Amazon Bedrock. The company wants to deploy the model to production and use the model to handle a steady rate of requests each minute. Which solution meets these requirements MOST cost-effectively?

- A) Deploy the model by using an Amazon EC2 compute optimized instance.
- B) Use the model with on-demand throughput on Amazon Bedrock.
- C) Store the model in Amazon S3 and host the model by using AWS Lambda.
- D) Purchase Provisioned Throughput for the model on Amazon Bedrock.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:genai_pricing_on_demand_vs_provisioned`  
**Explanation:** Provisioned Throughput is priced lower per request when you have a predictable, steady volume of calls. By committing to a fixed throughput level, you secure the necessary capacity at a reduced unit cost compared to on-demand, making it the most cost-effective choice for steady-minute usage.

</details>

### Q3.79 (`AIF-U1084`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> An airline company wants to build a conversational AI assistant to answer customer questions about flight schedules, booking, and payments. The company wants to use large language models (LLMs) and a knowledge base to create a text-based chatbot interface. Which solution will meet these requirements with the LEAST development effort?

- A) Train models on Amazon SageMaker Autopilot.
- B) Develop a Retrieval Augmented Generation (RAG) agent by using Amazon Bedrock.
- C) Create a Python application by using Amazon Q Developer.
- D) Fine-tune models on Amazon SageMaker Jumpstart.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Amazon Bedrock allows quick integration of large language models with a knowledge base using RAG architecture, enabling accurate and dynamic responses based on up-to-date information. This approach requires minimal development effort while leveraging powerful generative capabilities.

</details>

### Q3.80 (`AIF-U1048`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company is building an ML model. The company collected new data and analyzed the data by creating a correlation matrix, calculating statistics, and visualizing the data. Which stage of the ML pipeline is the company currently in?

- A) Data pre-processing
- B) Feature engineering
- C) Exploratory data analysis
- D) Hyperparameter tuning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_training_finetuning_rlhf`  
**Explanation:** The company is currently in the exploratory data analysis (EDA) stage, which involves summarizing data through statistics, visualizations, and correlation matrices to understand the dataset before moving on to modeling. The other options are subsequent steps in the ML pipeline.

</details>

### Q3.81 (`AIF-U1047`) — 3.1 FM Design Considerations, RAG, Vector DBs & Agents
> A company is building a large language model (LLM) question answering chatbot. The company wants to decrease the number of actions call center employees need to take to respond to customer questions. Which business objective should the company use to evaluate the effect of the LLM chatbot?

- A) Website engagement rate
- B) Average call duration
- C) Corporate social responsibility
- D) Regulatory compliance

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Reducing the average call duration directly indicates how effectively the LLM chatbot is helping call center employees answer customer questions, thus reducing the number of actions needed. The other options are not directly related to the performance of a call center chatbot.

</details>

### Q3.82 (`AIF-U1108`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> Which option is a benefit of ongoing pre-training when fine-tuning a foundation model (FM)?

- A) Helps decrease the model's complexity
- B) Improves model performance over time
- C) Decreases the training time requirement
- D) Optimizes model inference time

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** Ongoing pre-training helps enhance a foundation model's performance by continuously updating it with new data, thereby improving its ability to generalize and perform well on different tasks. The other options do not directly relate to the benefits of ongoing pre-training.

</details>

### Q3.83 (`AIF-U1066`) — 3.3 FM Training, Fine-Tuning, Continued Pre-Training & RLHF
> A company wants to fine-tune a foundation model (FM) to answer questions for a specific domain. The company wants to use instruction-based fine-tuning. How should the company prepare the training data?

- A) Gather company internal documents and industry-specific materials. Merge the documents and
- B) Collect external company reviews from various online sources. Manually label each review as either
- C) Create pairs of questions and answers that specifically address topics related to the company's industry
- D) Create few-shot prompts to instruct the model to answer only domain knowledge.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** Instruction-based fine-tuning requires a dataset of instruction–response examples. By curating question– answer pairs focused on the company’s domain, you teach the model exactly how to interpret domainspecific queries and generate the correct responses during inference.

</details>

### Q3.84 (`AIF-U1094`) — 3.2 Prompt Engineering Techniques, Risks & Prompt Management
> What is prompt engineering in the context of generative AI?

- A) A method of hardware optimization
- B) A technique for designing the physical structure of AI models
- C) The process of crafting effective input prompts to guide model outputs
- D) A way to reduce energy consumption in AI systems

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_3_core_concept`  
**Explanation:** Prompt engineering is the practice of carefully designing and refining input instructions (prompts) to guide a generative model toward producing accurate, relevant, and structured outputs. It can involve adding context, constraints, examples, or formatting instructions.

</details>

## Domain 4: Guidelines for Responsible AI (14% — 42 Questions)

### Q4.01 (`AIF-U1605`) — 4.2 Transparent & Explainable AI Models
> A financial institution is deploying an AI loan-eligibility assistant and wants to follow human-centered design principles for explainable AI. Which practice best supports this objective?

- A) Hiding all model confidence scores and decision factors from users
- B) Providing transparent explanations of AI decisions alongside clear user-feedback mechanisms
- C) Maximizing model parameter count regardless of interpretability
- D) Disabling audit logging to reduce storage overhead

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:rai_transparency_model_cards`  
**Explanation:** Human-centered design for explainable AI emphasizes clear AI decision transparency (why a recommendation was made) and user-feedback mechanisms so humans can understand, contest, and improve system behavior.

</details>

### Q4.02 (`AIF-U1572`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company built a deep learning model for object detection and deployed the model to production.Which AI process occurs when the model analyzes a new image to identify objects?

- A) Training
- B) Inference
- C) Model deployment
- D) Bias correction

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Inference is the correct answer because it is the AI process that occurs when a deployed model analyzes new data (such as an image) to make predictions or identify objects.Inference:In the context of machine learning, inference is the process of using a trained model to make predictions on new, unseen data.When the deep learning model is deployed to production and receives a new image for analysis, it uses the learned patterns from the training phase to identify objects in the image. This is known as inference.Why Option B is Correct:Inference Process: Involves applying the trained model to real-world data (the new image) to identify objects.Deployment Context: The model has already been trained, and the deployment to production indicates it is being used for inference.Why Other Options are Incorrect:A. Training: Refers to the process of teaching the model using historical data, not making predictions on new data.C. Model deployment: Refers to the process of making a trained model available for use in production.D. Bias correction: Is a process to adjust a model to minimize bias, not for analyzing new images.

</details>

### Q4.03 (`AIF-U1575`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A financial company is developing a generative AI application for loan approval decisions. The company needs the application output to be responsible and fair.Which solution meets these requirements?

- A) Review the training data to check for biases. Include data from all demographics in the training data.
- B) Use a deep learning model with many hidden layers.
- C) Keep the model ' s decision-making process a secret to protect proprietary algorithms.
- D) Continuously monitor the model’s performance on a static test dataset.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:rai_sagemaker_clarify_bias_shap`  
**Explanation:** The correct answer is A because ensuring responsibility and fairness in ML begins with bias detection in the training data. Including a balanced representation of all demographics ensures the model learns fairly across different groups, which is critical in regulated industries like finance.From AWS documentation:" A key principle of responsible AI is building models that do not propagate or amplify bias. Fairness begins with training data. Reviewing and augmenting data for representation is essential. "Explanation of other options:B. The number of hidden layers doesn’t inherently improve fairness or responsibility.C. Keeping decisions opaque violates explainability principles in responsible AI.D. A static dataset can become outdated and may not reflect real-world shifts, which limits fairness assessment over time.Referenced AWS AI/ML Documents and Study Guides:Amazon SageMaker Clarify Documentation – Bias Detection and ExplainabilityAWS Responsible AI GuidelinesAWS ML Specialty Study Guide – Fairness and Governance

</details>

### Q4.04 (`AIF-U1574`) — 4.2 Transparent & Explainable AI Models
> A company wants to build an ML model by using Amazon SageMaker. The company needs to share and manage variables for model development across multiple teams.Which SageMaker feature meets these requirements?

- A) Amazon SageMaker Feature Store
- B) Amazon SageMaker Data Wrangler
- C) Amazon SageMaker Clarify
- D) Amazon SageMaker Model Cards

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:rai_sagemaker_clarify_bias_shap`  
**Explanation:** Amazon SageMaker Feature Store is the correct solution for sharing and managing variables (features) across multiple teams during model development.Amazon SageMaker Feature Store:A fully managed repository for storing, sharing, and managing machine learning features across different teams and models.It enables collaboration and reuse of features, ensuring consistent data usage and reducing redundancy.Why Option A is Correct:Centralized Feature Management: Provides a central repository for managing features, making it easier to share them across teams.Collaboration and Reusability: Improves efficiency by allowing teams to reuse existing features instead of creating them from scratch.Why Other Options are Incorrect:B. SageMaker Data Wrangler: Helps with data preparation and analysis but does not provide a centralized feature store.C. SageMaker Clarify: Used for bias detection and explainability, not for managing variables across teams.D. SageMaker Model Cards: Provide model documentation, not feature management.

</details>

### Q4.05 (`AIF-U1573`) — 4.2 Transparent & Explainable AI Models
> A company makes forecasts each quarter to decide how to optimize operations to meet expected demand. The company uses ML models to make these forecasts. An AI practitioner is writing a report about the trained ML models to provide transparency and explainability to company stakeholders. What should the AI practitioner include in the report to meet the transparency and explainability requirements?

- A) Code for model training
- B) Partial dependence plots (PDPs)
- C) Sample data for training
- D) Model convergence tables

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:domain_4_core_concept`  
**Explanation:** Partial Dependence Plots (PDPs) are a powerful tool for understanding and explaining how the features in a machine learning model impact predictions. They are often used to meet transparency and explainability requirements for stakeholders. Let's go over why this is the correct choice, along with why the other options are less suitable: Partial Dependence Plots (PDPs) Purpose: PDPs show the relationship between a feature (or multiple features) and the model's predicted output, which helps to explain the effect of each feature on the model’s predictions. Explainability: By visualizing how each feature influences the prediction, stakeholders can better understand how the model works and why it makes certain predictions. This level of interpretability is essential for gaining trust from non-technical stakeholders. Transparency: PDPs improve transparency by providing an intuitive way to analyze and present the effects of individual features.

</details>

### Q4.06 (`AIF-U1576`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A student at a university is copying content from generative AI to write essays.Which challenge of responsible generative AI does this scenario represent?

- A) Toxicity
- B) Hallucinations
- C) Plagiarism
- D) Privacy

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_limitations_hallucination_nondeterminism`  
**Explanation:** The scenario where a student copies content from generative AI to write essays represents the challenge of plagiarism in responsible AI use.Plagiarism:Occurs when someone uses content generated by AI (or any source) without proper attribution, claiming it as their own.This is a key challenge with generative AI models, which can produce human-like text that might be misused for academic or other purposes.Why Option C is Correct:Represents Unauthorized Use: Copying content directly from AI without attribution is a clear case of plagiarism.Ethical Concern: Highlights the ethical considerations around using AI-generated content responsibly.Why Other Options are Incorrect:A. Toxicity: Refers to harmful or offensive content generation, not content copying.B. Hallucinations: When AI generates incorrect or nonsensical information, not plagiarism.D. Privacy: Involves the misuse or exposure of personal information, not copying content.

</details>

### Q4.07 (`AIF-U1585`) — 4.2 Transparent & Explainable AI Models
> A medical company is customizing a foundation model (FM) for diagnostic purposes. The company needs the model to be transparent and explainable to meet regulatory requirements.Which solution will meet these requirements?

- A) Configure security and compliance by using Amazon Inspector.
- B) Generate simple metrics, reports, and examples by using Amazon SageMaker Clarify.
- C) Encrypt and secure training data by using Amazon Macie.
- D) Gather more data. Use Amazon Rekognition to add custom labels to the data.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:rai_transparency_model_cards`  
**Explanation:** Amazon SageMaker Clarify provides transparency and explainability for machine learning models by generating metrics, reports, and examples that help to understand model predictions. For a medical company that needs a foundation model to be transparent and explainable to meet regulatory requirements, SageMaker Clarify is the most suitable solution.Amazon SageMaker Clarify:It helps in identifying potential bias in the data and model, and also explains model behavior by generating feature attributions, providing insights into which features are most influential in the model ' s predictions.These capabilities are critical in medical applications where regulatory compliance often mandates transparency and explainability to ensure that decisions made by the model can be trusted and audited.Why Option B is Correct:Transparency and Explainability: SageMaker Clarify is explicitly designed to provide insights into machine learning models ' decision-making processes, helping meet regulatory requirements by explaining why a model made a particular prediction.Compliance with Regulations: The tool is suitable for use in sensitive domains, such as healthcare, where there is a need for explainable AI.Why Other Options are Incorrect:A. Amazon Inspector: Focuses on security assessments, not on explainability or model transparency.C. Amazon Macie: Provides data security by identifying and protecting sensitive data, but does not help in making models explainable.D. Amazon Rekognition: Used for image and video analysis, not relevant to making models explainable.Thus, B is the correct answer for meeting transparency and explainability requirements for the foundation model

</details>

### Q4.08 (`AIF-U1589`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> An ecommerce company is deploying a chatbot. The chatbot will give users the ability to ask questions about the company ' s products and receive details on users ' orders. The company must implement safeguards for the chatbot to filter harmful content from the input prompts and chatbot responses.Which AWS feature or resource meets these requirements?

- A) Amazon Bedrock Guardrails
- B) Amazon Bedrock Agents
- C) Amazon Bedrock inference APIs
- D) Amazon Bedrock custom models

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:rai_bedrock_guardrails`  
**Explanation:** The ecommerce company is deploying a chatbot that needs safeguards to filter harmful content from input prompts and responses. Amazon Bedrock Guardrails provide mechanisms to ensure responsible AI usage by filtering harmful content, such as hate speech, violence, or misinformation, making it the appropriate feature for this requirement.Exact Extract from AWS AI Documents:From the AWS Bedrock User Guide:" Amazon Bedrock Guardrails enable developers to implement safeguards for generative AI applications, such as chatbots, by filtering harmful content in input prompts and model responses. Guardrails include content filters, word filters, and denied topics to ensure safe and responsible outputs. "(Source: AWS Bedrock User Guide, Guardrails for Responsible AI)Detailed Explanation:Option A: Amazon Bedrock GuardrailsThis is the correct answer. Amazon Bedrock Guardrails are specifically designed to filter harmful content from chatbot inputs and responses, ensuring safe interactions for users.Option B: Amazon Bedrock AgentsAmazon Bedrock Agents are used to automate tasks and integrate with external tools, not to filter harmful content. This option does not meet the requirement.Option C: Amazon Bedrock inference APIsAmazon Bedrock inference APIs allow users to invoke foundation models for generating responses, but they do not provide built-in content filtering mechanisms.Option D: Amazon Bedrock custom modelsCustom models on Amazon Bedrock allow users to fine-tune models, but they do not inherently include safeguards for filtering harmful content unless explicitly implemented.

</details>

### Q4.09 (`AIF-U1581`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company is using large language models (LLMs) to develop online tutoring applications. The company needs to apply configurable safeguards to the LLMs. These safeguards must ensure that the LLMs follow standard safety rules when creating applications.Which solution will meet these requirements with the LEAST effort?

- A) Amazon Bedrock playgrounds
- B) Amazon SageMaker Clarify
- C) Amazon Bedrock Guardrails
- D) Amazon SageMaker JumpStart

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** The correct answer is C because Amazon Bedrock Guardrails provides out-of-the-box configurable safety mechanisms to control the behavior of LLMs in generative AI applications. Guardrails can be configured with denylists, content filters, sensitive topics, and tone enforcement, all without retraining the model.From AWS documentation:" Amazon Bedrock Guardrails allows developers to define safety and responsible AI policies directly in the model inference layer, making it easy to prevent harmful, biased, or unsafe outputs with minimal configuration. "Explanation of other options:A. Bedrock playgrounds are interactive environments for testing prompts and models but do not provide production-grade safety enforcement.B. SageMaker Clarify focuses on bias detection and explainability for supervised ML models — it does not directly apply guardrails to LLM outputs.D. SageMaker JumpStart is for model fine-tuning and deployment, not for enforcing safety policies on LLM responses.Referenced AWS AI/ML Documents and Study Guides:Amazon Bedrock Documentation – Guardrails OverviewAWS Responsible AI WhitepaperAWS Certified ML Specialty Study Guide – Safety in Generative AI

</details>

### Q4.10 (`AIF-U1587`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> An AI practitioner is building a model to generate images of humans in various professions. The AI practitioner discovered that the input data is biased and that specific attributes affect the image generation and create bias in the model.Which technique will solve the problem?

- A) Data augmentation for imbalanced classes
- B) Model monitoring for class distribution
- C) Retrieval Augmented Generation (RAG)
- D) Watermark detection for images

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Data augmentation for imbalanced classes is the correct technique to address bias in input data affecting image generation.Data Augmentation for Imbalanced Classes:Involves generating new data samples by modifying existing ones, such as flipping, rotating, or cropping images, to balance the representation of different classes.Helps mitigate bias by ensuring that the training data is more representative of diverse characteristics and scenarios.Why Option A is Correct:Balances Data Distribution: Addresses class imbalance by augmenting underrepresented classes, which reduces bias in the model.Improves Model Fairness: Ensures that the model is exposed to a more diverse set of training examples, promoting fairness in image generation.Why Other Options are Incorrect:B. Model monitoring for class distribution: Helps identify bias but does not actively correct it.C. Retrieval Augmented Generation (RAG): Involves combining retrieval and generation but is unrelated to mitigating bias in image generation.D. Watermark detection for images: Detects watermarks in images, not a technique for addressing bias.

</details>

### Q4.11 (`AIF-U1590`) — 4.2 Transparent & Explainable AI Models
> Which functionality does Amazon SageMaker Clarify provide?

- A) Integrates a Retrieval Augmented Generation (RAG) workflow
- B) Monitors the quality of ML models in production
- C) Documents critical details about ML models
- D) Identifies potential bias during data preparation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** Exploratory data analysis (EDA) involves understanding the data by visualizing it, calculating statistics, and creating correlation matrices. This stage helps identify patterns, relationships, and anomalies in the data, which can guide further steps in the ML pipeline.Option C (Correct): " Exploratory data analysis " : This is the correct answer as the tasks described (correlation matrix, calculating statistics, visualizing data) are all part of the EDA process.Option A: " Data pre-processing " is incorrect because it involves cleaning and transforming data, not initial analysis.Option B: " Feature engineering " is incorrect because it involves creating new features from raw data, not analyzing the data ' s existing structure.Option D: " Hyperparameter tuning " is incorrect because it refers to optimizing model parameters, not analyzing the data.AWS AI Practitioner References:Stages of the Machine Learning Pipeline: AWS outlines EDA as the initial phase of understanding and exploring data before moving to more specific preprocessing, feature engineering, and model training stages.

</details>

### Q4.12 (`AIF-U1579`) — 4.2 Transparent & Explainable AI Models
> A company is developing an ML model to make loan approvals. The company must implement a solution to detect bias in the model. The company must also be able to explain the model ' s predictions.Which solution will meet these requirements?

- A) Amazon SageMaker Clarify
- B) Amazon SageMaker Data Wrangler
- C) Amazon SageMaker Model Cards
- D) AWS AI Service Cards

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:rai_sagemaker_clarify_bias_shap`  
**Explanation:** Amazon SageMaker Clarify is a tool that helps detect bias in machine learning models and provides explainability for model predictions. It allows users to understand the factors influencing a model's predictions and assess whether the model is fair across different demographic groups. This is exactly what the company needs for detecting bias and explaining model decisions, especially for high-stakes applications like loan approvals. Bias detection: SageMaker Clarify can analyze the training data and the model's predictions to identify and mitigate bias. Explainability: It provides features for explaining the predictions made by the model, which helps users understand the reasons behind the model's decisions.

</details>

### Q4.13 (`AIF-U1583`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company wants to identify harmful language in the comments section of social media posts by using an ML model. The company will not use labeled data to train the model. Which strategy should the company use to identify harmful language?

- A) Use Amazon Rekognition moderation.
- B) Use Amazon Comprehend toxicity detection.
- C) Use Amazon SageMaker AI built-in algorithms to train the model.
- D) Use Amazon Polly to monitor comments.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Amazon Comprehend toxicity detection is a managed NLP service that can analyze text for harmful or toxic language using pre-trained models—no need for labeled data or custom training.B is correct: Comprehend’s toxicity detection API is designed for this use case, works out-of-the-box, and requires no data labeling or model training.A (Rekognition) is for image and video content moderation.C would require labeled data for training.D (Polly) is for text-to-speech, not content moderation.“Amazon Comprehend can detect toxicity in text with pre-trained models, requiring no labeled training data.”(Reference: Amazon Comprehend Toxicity Detection, AWS AI Practitioner Official Guide)

</details>

### Q4.14 (`AIF-U1592`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> Which technique can a company use to lower bias and toxicity in generative AI applications during the post-processing ML lifecycle?

- A) Human-in-the-loop
- B) Data augmentation
- C) Feature engineering
- D) Adversarial training

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:fm_business_alignment_metrics`  
**Explanation:** A: Incorrect. Does not fulfill the core requirement: Identify post-processing techniques that reduce bias and toxicity in generative AI applications. | B: Incorrect. Does not fulfill the core requirement: Identify post-processing techniques that reduce bias and toxicity in generative AI applications. | C: Incorrect. Does not fulfill the core requirement: Identify post-processing techniques that reduce bias and toxicity in generative AI applications. | D: Incorrect. Does not fulfill the core requirement: Identify post-processing techniques that reduce bias and toxicity in generative AI applications.

</details>

### Q4.15 (`AIF-U1584`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A loan company is building a generative AI-based solution to offer new applicants discounts based on specific business criteria. The company wants to build and use an AI model responsibly to minimize bias that could negatively affect some customers. Which actions should the company take to meet these requirements? (Select TWO.)

- A) Detect imbalances or disparities in the data.
- B) Ensure that the model runs frequently.
- C) Evaluate the model's behavior so that the company can provide transparency to stakeholders.
- D) Use the Recall-Oriented Understudy for Gisting Evaluation (ROUGE) technique to ensure that the model is 100% accurate.
- E) Ensure that the model's inference time is within the accepted limits.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Detect imbalances or disparities in the data: Identifying and addressing data imbalances helps minimize biases that could negatively affect customers. Evaluate the model's behavior so that the company can provide transparency to stakeholders: Evaluating the model and ensuring transparency is important for responsible AI usage, as it helps stakeholders understand how decisions are made. The other options are either not directly related to minimizing bias or do not address responsible AI development.

</details>

### Q4.16 (`AIF-U1586`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> An AI practitioner has trained a model on a training dataset. The model performs well on the training data. However, the model does not perform well on evaluation data. What is the MOST likely cause of this issue?

- A) The model is underfit.
- B) The model requires prompt engineering.
- C) The model is biased.
- D) The model is overfit.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** When a model performs well on training data but poorly on evaluation/test data, it indicates overfitting.Overfitting: The model memorizes the training data patterns instead of generalizing.Underfitting (A) means the model performs poorly on both training and test data.Bias (C) refers to systemic errors in predictions, not this training/test mismatch.Prompt engineering (B) applies to generative AI, not general ML training models.???? Reference:AWS ML Glossary – Overfitting and Underfitting

</details>

### Q4.17 (`AIF-U1578`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company has installed a security camera. The company uses an ML model to evaluate the security camera footage for potential thefts. The company has discovered that the model disproportionately flags people who are members of a specific ethnic group. Which type of bias is affecting the model output?

- A) Measurement bias
- B) Sampling bias
- C) Observer bias
- D) Confirmation bias

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:domain_4_core_concept`  
**Explanation:** Sampling bias occurs when the training data is not representative of the overall population, leading to disproportionate flagging of specific groups. In this case, the model may have been trained on biased data that did not adequately represent all ethnic groups, resulting in skewed predictions. The other types of bias do not directly apply to the selection of training data or its representativeness.

</details>

### Q4.18 (`AIF-U1582`) — 4.2 Transparent & Explainable AI Models
> A company wants to collaborate with several research institutes to develop an AI model. The company needs standardized documentation of model version tracking and a record of model development.Which solution meets these requirements?

- A) Track the model changes by using Git.
- B) Track the model changes by using Amazon Fraud Detector.
- C) Track the model changes by using Amazon SageMaker Model Cards.
- D) Track the model changes by using Amazon Comprehend.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon SageMaker Model Cards provide a standardized way to document and track model information, including versions and performance. According to AWS documentation:“SageMaker Model Cards provide a single source of truth for model information including intended use, training details, evaluation metrics, and ethical considerations to support governance and collaboration.”

</details>

### Q4.19 (`AIF-U1591`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> Which prompting technique can protect against prompt injection attacks?

- A) Adversarial prompting
- B) Zero-shot prompting
- C) Least-to-most prompting
- D) Chain-of-thought prompting

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:prompt_engineering_techniques`  
**Explanation:** Adversarial prompting is a technique used to defend against prompt injection attacks by crafting inputs that are specifically designed to identify and neutralize malicious prompts. This approach involves generating prompts that can detect and mitigate adversarial inputs, thereby enhancing the robustness of language models against such attacks.

</details>

### Q4.20 (`AIF-U1577`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A bank is fine-tuning a large language model (LLM) on Amazon Bedrock to assist customers with questions about their loans. The bank wants to ensure that the model does not reveal any private customer data. Which solution meets these requirements?

- A) Use Amazon Bedrock Guardrails.
- B) Remove personally identifiable information (PII) from the customer data before fine-tuning the LLM.
- C) Increase the Top-K parameter of the LLM.
- D) Store customer data in Amazon S3. Encrypt the data before fine-tuning the LLM.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:rai_bedrock_guardrails`  
**Explanation:** Preprocessing your fine-tuning dataset to strip out names, account numbers, and other PII prevents the model from ever ingesting - or later regurgitating - private customer information. This data sanitization step is the most reliable way to guarantee that sensitive details aren’t embedded into the model.

</details>

### Q4.21 (`AIF-U1580`) — 4.2 Transparent & Explainable AI Models
> A company is using Amazon SageMaker to deploy a model that identifies if social media posts contain certain topics. The company needs to show how different input features influence model behavior.

- A) SageMaker Canvas
- B) SageMaker Clarify
- C) SageMaker Feature Store
- D) SageMaker Ground Truth

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** SageMaker Clarify provides model explainability, bias detection, and helps visualize how input features affect predictions.Canvas is for low-code ML building.Feature Store is for storing and managing ML features.Ground Truth is for data labeling.???? Reference:AWS Documentation – Amazon SageMaker Clarify

</details>

### Q4.22 (`AIF-U1588`) — 4.2 Transparent & Explainable AI Models
> An AI practitioner is building an ML model. The AI practitioner wants to provide model transparency and explainability to stakeholders. Which solution will meet these requirements?

- A) Present the model Shapley values.
- B) Provide the model accuracy measure.
- C) Provide the model confusion matrix.
- D) Provide a secure model inference endpoint.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_metrics_confusion_matrix`  
**Explanation:** Presenting the model Shapley values provides transparency and explainability by showing how each feature contributes to individual predictions, helping stakeholders understand the reasoning behind the model’s outputs.

</details>

### Q4.23 (`AIF-U1616`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> Which component of Amazon Bedrock Studio can help secure the content that AI systems generate?

- A) Access controls
- B) Function calling
- C) Guardrails
- D) Knowledge bases

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon Bedrock Studio provides tools to build and manage generative AI applications, and the company needs a component to secure the content generated by AI systems. Guardrails in Amazon Bedrock are designed to ensure safe and responsible AI outputs by filtering harmful or inappropriate content, making them the key component for securing generated content.Exact Extract from AWS AI Documents:From the AWS Bedrock User Guide:" Guardrails in Amazon Bedrock provide mechanisms to secure the content generated by AI systems by filtering out harmful or inappropriate outputs, such as hate speech, violence, or misinformation, ensuring responsible AI usage. "(Source: AWS Bedrock User Guide, Guardrails for Responsible AI)Detailed Explanation:Option A: Access controlsAccess controls manage who can use or interact with the AI system but do not directly secure the content generated by the system.Option B: Function callingFunction calling enables AI models to interact with external tools or APIs, but it is not related to securing generated content.Option C: GuardrailsThis is the correct answer. Guardrails in Amazon Bedrock secure generated content by filtering out harmful or inappropriate material, ensuring safe outputs.Option D: Knowledge basesKnowledge bases provide data for AI models to generate responses but do not inherently secure the content that is generated.

</details>

### Q4.24 (`AIF-U1604`) — 4.2 Transparent & Explainable AI Models
> A financial institution is building an AI solution to make loan approval decisions by using a foundation model (FM). For security and audit purposes, the company needs the AI solution's decisions to be explainable. Which factor relates to the explainability of the AI solution's decisions?

- A) Model complexity
- B) Training time
- C) Number of hyperparameters
- D) Deployment time

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Model complexity plays a significant role in the explainability of an AI solution. Simpler models tend to be more explainable because it is easier to understand how they make decisions. For example, linear regression or decision trees are generally easier to interpret compared to more complex models like deep neural networks. In contrast, highly complex models, such as deep learning models, may provide very accurate results but are often considered "black boxes," meaning their decision-making process is not easily interpretable. This lack of transparency makes it difficult to explain their decisions in a way that satisfies regulatory requirements or customer understanding.

</details>

### Q4.25 (`AIF-U1598`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company is developing a mobile ML app that uses a phone's camera to diagnose and treat insect bites. The company wants to train an image classification model by using a diverse dataset of insect bite photos from different genders, ethnicities, and geographic locations around the world. Which principle of responsible AI does the company demonstrate in this scenario?

- A) Fairness
- B) Explainability
- C) Governance
- D) Transparency

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** The company is actively seeking to ensure that the image classification model is trained on a diverse dataset that includes insect bite photos from various genders, ethnicities, and geographic locations. This reflects the fairness principle of responsible AI, which emphasizes creating models that make unbiased decisions across all demographic groups. By including a diverse range of data, the company is aiming to prevent biases that could lead to inaccurate diagnoses or treatments for certain groups of people. Fairness ensures that AI systems do not discriminate based on race, gender, geography, or other characteristics.

</details>

### Q4.26 (`AIF-U1613`) — 4.2 Transparent & Explainable AI Models
> An ML research team develops custom ML models. The model artifacts are shared with other teams for integration into products and services. The ML team retains the model training code and data. The ML team wants to build a mechanism that the ML team can use to audit models. Which solution should the ML team use when publishing the custom ML models?

- A) Create documents with the relevant information. Store the documents in Amazon S3.
- B) Use AWS AI Service Cards for transparency and understanding models.
- C) Create Amazon SageMaker Model Cards with intended uses and training and inference details.
- D) Create model training scripts. Commit the model training scripts to a Git repository.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:rai_transparency_model_cards`  
**Explanation:** Amazon SageMaker Model Cards are designed to document the essential details about machine learning models, including their intended uses, training datasets, training parameters, evaluation metrics, and inference environment. This provides a centralized mechanism to store and audit the metadata of the models, which is ideal for the ML team's need to share and audit models effectively. T Key benefits of Amazon Model Cards: SageMaker Standardized documentation of models' characteristics and intended use cases. for auditing purposes. Transparency and traceability Integration with other AWS services for lifecycle management.

</details>

### Q4.27 (`AIF-U1611`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> An accounting firm wants to implement a large language model (LLM) to automate document processing. The firm must proceed responsibly to avoid potential harms. What should the firm do when developing and deploying the LLM? (Choose 2)

- A) Include fairness metrics for model evaluation.
- B) Adjust the temperature parameter of the model.
- C) Modify the training data to mitigate bias.
- D) Avoid overfitting on the training data.
- E) Apply prompt engineering techniques.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, C`  
**Point Tested:** `point:ml_fit_overfitting_underfitting`  
**Explanation:** Include fairness metrics for model evaluation: Fairness metrics help ensure that the LLM is unbiased and treats all cases equitably, which is essential for responsible AI use. Modify the training data to mitigate bias: Adjusting the training data helps reduce any inherent bias that might exist, contributing to a more fair and responsible LLM. The other options are related to general model optimization but do not directly address responsible AI practices regarding potential harms like bias and fairness.

</details>

### Q4.28 (`AIF-U1593`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company built an AI-powered resume screening system. The company used a large dataset to train the model. The dataset contained resumes that were not representative of all demographics. Which core dimension of responsible AI does this scenario present?

- A) Fairness
- B) Explainability
- C) Privacy and security
- D) Transparency

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:rai_principles_and_sustainability`  
**Explanation:** The scenario describes a dataset that is not representative of all demographics, which can lead to biased model predictions. This directly relates to fairness, a core dimension of responsible AI that ensures AI systems make unbiased and equitable decisions across different demographic groups. Addressing fairness involves techniques such as balanced dataset curation, bias detection, and mitigation strategies to ensure that the AI system does not discriminate against any group.

</details>

### Q4.29 (`AIF-U1614`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> Which Amazon Bedrock features help with content filtering and safety? (Choose 2)

- A) Guardrails for content filtering
- B) Model customization options
- C) Prompt management capabilities
- D) Watermark detection for AI-generated content
- E) Knowledge base integration

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, D`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Guardrails filter harmful, inappropriate, or unwanted content in both inputs and outputs, ensuring that AI-generated responses align with ethical and safety standards. Watermark detection helps identify AI-generated content, which is crucial for maintaining transparency and accountability. By detecting watermarks, organizations can prevent misuse of AI-generated content, such as plagiarism or the spread of misinformation, thereby enhancing trust and safety in AI deployments.

</details>

### Q4.30 (`AIF-U1608`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A large retail bank wants to develop an ML system to help the risk management team decide on loan allocations for different demographics. What must the bank do to develop an unbiased ML model?

- A) Reduce the size of the training dataset.
- B) Ensure that the ML model predictions are consistent with historical results.
- C) Create a different ML model for each demographic group.
- D) Measure class imbalance on the training dataset. Adapt the training process accordingly.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:rai_sagemaker_clarify_bias_shap`  
**Explanation:** In machine learning, class imbalance occurs when certain classes are underrepresented in the training dataset, leading to biased model predictions. To develop an unbiased model, it's crucial to assess the class distribution and adjust the training process to address any imbalances. This can be achieved through techniques such as oversampling the minority class, undersampling the majority class, or applying class weights to ensure the model treats all classes equitably.

</details>

### Q4.31 (`AIF-U1618`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> Which option is a characteristic of AI governance frameworks for building trust and deploying humancentered AI technologies?

- A) Expanding initiatives across business units to create long-term business value
- B) Ensuring alignment with business standards, revenue goals, and stakeholder expectations
- C) Overcoming challenges to drive business transformation and growth
- D) Developing policies and guidelines for data, transparency, responsible AI, and compliance

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:rai_principles_and_sustainability`  
**Explanation:** AI governance frameworks focus on building trust and ensuring the responsible deployment of AI technologies. They establish clear policies and guidelines to address critical aspects such as data management, transparency, ethical considerations, responsible AI practices, and regulatory compliance. These frameworks help organizations mitigate risks, promote fairness, and foster public trust in AI systems, making them essential for creating human-centered AI technologies.

</details>

### Q4.32 (`AIF-U1606`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A financial services company must ensure that its generative AI-powered chatbot provides factual responses for regulatory compliance. Which solution prevents the underlying foundation model (FM) from hallucinating?

- A) Use AWS Config to query compliance metadata by using natural language.
- B) Configure Amazon Bedrock Guardrails to evaluate user inputs and model responses.
- C) Use Amazon Fraud Detector to detect potentially fraudulent online activities.
- D) Use AWS Audit Manager to prepare IT audit and compliance reports.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** Amazon Bedrock Guardrails allows you to define rules and policies that evaluate and constrain both user inputs and model responses. By configuring guardrails, you can prevent the generative AI model from producing hallucinated or non-factual outputs, ensuring the chatbot adheres to compliance requirements and provides factual responses. This directly addresses the need to control hallucinations in generative AI systems for regulatory compliance.

</details>

### Q4.33 (`AIF-U1601`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company uses Amazon Bedrock for its generative AI application. The company wants to use Amazon Bedrock Guardrails to detect and filter harmful user inputs and model-generated outputs. Which content categories can the guardrails filter? (Choose two.)

- A) Hate
- B) Politics
- C) Violence
- D) Gambling

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:rai_bedrock_guardrails`  
**Explanation:** Amazon Bedrock Guardrails provide configurable content filters to detect and block harmful content in generative AI applications. Specifically, they include filters for categories such as Hate and Violence, among others. These filters can be applied to both user inputs and model-generated outputs to ensure that the AI application adheres to responsible AI practices and organizational policies.

</details>

### Q4.34 (`AIF-U1609`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A medical company wants to modernize its onsite information processing application. The company wants to use generative AI to respond to medical questions from patients. Which AWS service should the company use to ensure responsible AI for the application?

- A) Guardrails for Amazon Bedrock
- B) Amazon Inspector
- C) Amazon Rekognition
- D) AWS Trusted Advisor

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** Guardrails for Amazon Bedrock let you define and enforce safety, compliance, and bias controls on generative AI workloads. By embedding these guardrails into your application, you can ensure that patientfacing responses meet medical accuracy, privacy, and regulatory requirements without having to build custom monitoring or filtering pipelines yourself.

</details>

### Q4.35 (`AIF-U1597`) — 4.2 Transparent & Explainable AI Models
> A company is deploying AI/ML models by using AWS services. The company wants to offer transparency into the models’ decision-making processes and provide explanations for the model outputs. Which AWS service or feature meets these requirements?

- A) Amazon SageMaker Model Cards
- B) Amazon Rekognition
- C) Amazon Comprehend
- D) Amazon Lex

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_comprehend_nlp`  
**Explanation:** Amazon SageMaker Model Cards help provide transparency into AI/ML models by documenting key details such as model purpose, training data, performance metrics, and limitations. This documentation enables organizations to explain model outputs and decision-making processes, ensuring accountability and compliance with responsible AI principles.

</details>

### Q4.36 (`AIF-U1602`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company wants to build an interactive application for children that generates new stories based on classic stories. The company wants to use Amazon Bedrock and needs to ensure that the results and topics are appropriate for children. Which AWS service or feature will meet these requirements?

- A) Amazon Rekognition
- B) Amazon Bedrock playgrounds
- C) Guardrails for Amazon Bedrock
- D) Agents for Amazon Bedrock

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Guardrails for Amazon Bedrock can help ensure that the output generated by Amazon Bedrock is appropriate for children. Guardrails are used to apply content moderation, guidelines, and ensure safety by filtering potentially harmful or inappropriate content, which is essential when building an interactive application for children.

</details>

### Q4.37 (`AIF-U1610`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A social media company wants to use a large language model (LLM) for content moderation. The company wants to evaluate the LLM outputs for bias and potential discrimination against specific groups or individuals. Which data source should the company use to evaluate the LLM outputs with the LEAST administrative effort?

- A) User-generated content
- B) Moderation logs
- C) Content moderation guidelines
- D) Benchmark datasets

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Benchmark datasets are standardized datasets specifically designed for evaluating models for bias and fairness, allowing for efficient assessment with minimal administrative effort. The other options would require more manual processing and might not provide a consistent basis for evaluating bias and discrimination.

</details>

### Q4.38 (`AIF-U1617`) — 4.2 Transparent & Explainable AI Models
> Which option is a benefit of using Amazon SageMaker Model Cards to document AI models?

- A) Providing a visually appealing summary of a model’s capabilities.
- B) Standardizing information about a model’s purpose, performance, and limitations.
- C) Reducing the overall computational requirements of a model.
- D) Physically storing models for archival purposes.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:rai_transparency_model_cards`  
**Explanation:** Amazon SageMaker Model Cards provide a structured way to document key details about AI models, including their intended use, performance metrics, and limitations. This helps organizations maintain transparency, compliance, and governance in AI model development, making it easier to track and manage models over time.

</details>

### Q4.39 (`AIF-U1615`) — 4.2 Transparent & Explainable AI Models
> Which AWS feature records details about ML instance data for governance and reporting?

- A) Amazon SageMaker Model Cards
- B) Amazon SageMaker Debugger
- C) Amazon SageMaker Model Monitor
- D) Amazon SageMaker JumpStart

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:mlops_sagemaker_lifecycle`  
**Explanation:** Amazon SageMaker Model Cards record key details about machine learning models, including intended use, training data, evaluation metrics, and compliance information. They support governance and reporting by providing a standardized way to document model information throughout its lifecycle.

</details>

### Q4.40 (`AIF-U1603`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A financial company is using AI systems to obtain customer credit scores as part of the loan application process. The company wants to expand to a new market in a different geographic area. The company must ensure that it can operate in that geographic area. Which compliance laws should the company review?

- A) Local health data protection laws
- B) Local payment card data protection laws
- C) Local education privacy laws
- D) Local algorithm accountability laws

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:rai_principles_and_sustainability`  
**Explanation:** When deploying AI systems that affect individuals, such as credit scoring, companies must comply with local algorithm accountability laws. These laws regulate the fairness, transparency, and impact of automated decision-making, ensuring ethical use of AI in new geographic regions.

</details>

### Q4.41 (`AIF-U1595`) — 4.1 Responsible AI Principles, Bias Detection & Guardrails
> A company is building a new generative AI chatbot. The chatbot uses an Amazon Bedrock foundation model (FM) to generate responses. During testing, the company notices that the chatbot is prone to prompt injection attacks. What can the company do to secure the chatbot with the LEAST implementation effort?

- A) Fine-tune the FM to avoid harmful responses.
- B) Use Amazon Bedrock Guardrails content filters and denied topics.
- C) Change the FM to a more secure FM.
- D) Use chain-of-thought prompting to produce secure responses.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:rai_bedrock_guardrails`  
**Explanation:** Using Amazon Bedrock Guardrails' content filters and denied topics is the quickest and least effort solution to mitigate prompt injection attacks. These guardrails can be configured without model retraining, helping to automatically filter or block unsafe prompts and responses.

</details>

### Q4.42 (`AIF-U1594`) — 4.2 Transparent & Explainable AI Models
> A company has developed an ML model to approve or reject loan applications. The model's decision-making process must be transparent and explainable to comply with regulatory requirements. The company must document the decision-making process for audit purposes. Which solution will meet these requirements?

- A) Amazon Textract
- B) Amazon SageMaker Model Card
- C) AWS Cloud Formation
- D) Amazon Comprehend

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:rai_transparency_model_cards`  
**Explanation:** Amazon SageMaker Model Card enables you to document a model’s decision-making process, including transparency and explainability details, which helps meet regulatory and audit requirements for AI-driven decisions such as loan approvals.

</details>

## Domain 5: Security, Compliance, and Governance for AI Solutions (14% — 42 Questions)

### Q5.01 (`AIF-U1861`) — 5.1 Securing AI Systems, Data Protection & Grounding
> An enterprise deploys autonomous AI agents in production using Amazon Bedrock AgentCore. Security architects require strict enforcement so that agents only invoke approved external APIs with user-delegated credentials and deterministic allow/deny tool policies. Which two Amazon Bedrock AgentCore capabilities directly address these requirements? (Choose TWO.)

- A) Amazon Bedrock AgentCore Identity
- B) Policy in AgentCore
- C) Amazon S3 Glacier Deep Archive
- D) AWS Budgets
- E) Amazon Polly

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, B`  
**Point Tested:** `point:sec_agentcore_identity_and_policy`  
**Explanation:** Amazon Bedrock AgentCore Identity manages secure OAuth/IAM delegation and scoped credentials for agents, while Policy in AgentCore enforces deterministic allow/forbid policies on agent tool calls before execution.

</details>

### Q5.02 (`AIF-U1860`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A healthcare company wants to detect and mitigate hallucinations in an Amazon Bedrock RAG application before responses reach clinicians. Which combination of techniques directly improves output accuracy and grounding?

- A) Increasing temperature and removing system prompts
- B) RAG grounding, Bedrock Guardrails contextual grounding checks, and output validation with source citations
- C) Disabling encryption at rest to speed up vector retrieval
- D) Switching from supervised learning to k-means clustering

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:ml_tasks_regression_classification_clustering`  
**Explanation:** Grounding responses in verified RAG sources, applying Bedrock Guardrails contextual grounding checks, and enforcing output validation with source citations directly detect and reduce hallucinations.

</details>

### Q5.03 (`AIF-U1842`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company wants to upload customer service email messages to Amazon S3 to develop a business analysis application. The messages sometimes contain sensitive data. The company wants to receive an alert every time sensitive information is found.Which solution fully automates the sensitive information detection process with the LEAST development effort?

- A) Configure Amazon Macie to detect sensitive information in the documents that are uploaded to Amazon S3.
- B) Use Amazon SageMaker endpoints to deploy a large language model (LLM) to redact sensitive data.
- C) Develop multiple regex patterns to detect sensitive data. Expose the regex patterns on an Amazon SageMaker notebook.
- D) Ask the customers to avoid sharing sensitive information in their email messages.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** The verified answer is A. Configure Amazon Macie to detect sensitive information in the documents that are uploaded to Amazon S3. The data is stored in Amazon S3, and the company wants automated sensitive information detection with the least development effort. AWS documentation states that Amazon Macie can automate discovery, logging, and reporting of sensitive data in an Amazon S3 data estate. Macie can use automated sensitive data discovery or sensitive data discovery jobs, and it can analyze S3 objects using AWS-managed data identifiers, custom data identifiers, or both.This fits the requirement better than a custom ML or regex-based approach because Macie is purpose-built for discovering sensitive data in S3. AWS states that managed data identifiers can detect many types of sensitive data, including personally identifiable information, financial information, and credentials. Macie also produces sensitive data findings and discovery results, which can be monitored and processed by other AWS services.Option B is incorrect because deploying an LLM on SageMaker would require model selection, deployment, prompt design, testing, security controls, and possibly custom redaction logic. That is not the least development effort.Option C is incorrect because manually developing regex patterns is brittle and maintenance-heavy. It also requires custom development and does not fully automate sensitive information detection across many data types.Option D is incorrect because asking customers not to share sensitive data is not a technical control and cannot guarantee detection or alerting.Because the documents are in Amazon S3 and sensitive data detection must be automated, Amazon Macie is the correct solution.

</details>

### Q5.04 (`AIF-U1844`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> An AI company periodically evaluates its systems and processes with the help of independent software vendors (ISVs). The company needs to receive email message notifications when an ISV ' s compliance reports become available.Which AWS service meets this requirement?

- A) AWS Audit Manager
- B) AWS Artifact
- C) AWS Trusted Advisor
- D) AWS Data Exchange

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** The correct answer is AWS Artifact, which is a central resource for accessing AWS compliance documentation, audit reports, and certifications from both AWS and third-party providers, including ISVs. According to AWS documentation, Artifact supports notifications for newly available reports. Customers can subscribe to notification emails when specific compliance documents or updates are published. This feature is ideal for regulated industries or companies needing third-party verification of compliance and security postures. Artifact provides access to reports such as SOC 2, ISO, PCI, and more, and is commonly used for audit preparation and vendor risk management. In contrast, AWS Audit Manager helps create internal audit frameworks but is not focused on third-party report distribution. AWS Data Exchange is for marketplace data sharing, and Trusted Advisor provides performance and cost optimization recommendations, not compliance document alerts. Thus, AWS Artifact is the purpose-built service that meets this requirement.Referenced AWS AI/ML Documents and Study Guides:AWS Artifact Documentation – Compliance Reports and SubscriptionsAWS Security and Compliance Whitepaper – Using Artifact for Third-Party Assurance

</details>

### Q5.05 (`AIF-U1843`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A company wants to use a large language model (LLM) to develop a conversational agent. The company needs to prevent the LLM from being manipulated with common prompt engineering techniques to perform undesirable actions or expose sensitive information.Which action will reduce these risks?

- A) Create a prompt template that teaches the LLM to detect attack patterns.
- B) Increase the temperature parameter on invocation requests to the LLM.
- C) Avoid using LLMs that are not listed in Amazon SageMaker.
- D) Decrease the number of input tokens on invocations of the LLM.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Creating a prompt template that teaches the LLM to detect attack patterns is the most effective way to reduce the risk of the model being manipulated through prompt engineering.Prompt Templates for Security:A well-designed prompt template can guide the LLM to recognize and respond appropriately to potential manipulation attempts.This strategy helps prevent the model from performing undesirable actions or exposing sensitive information by embedding security awareness directly into the prompts.Why Option A is Correct:Teaches Model Security Awareness: Equips the LLM to handle potentially harmful inputs by recognizing suspicious patterns.Reduces Manipulation Risk: Helps mitigate risks associated with prompt engineering attacks by proactively preparing the LLM.Why Other Options are Incorrect:B. Increase the temperature parameter: This increases randomness in responses, potentially making the LLM more unpredictable and less secure.C. Avoid LLMs not listed in SageMaker: Does not directly address the risk of prompt manipulation.D. Decrease the number of input tokens: Does not mitigate risks related to prompt manipulation.

</details>

### Q5.06 (`AIF-U1841`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company wants to create a chatbot by using a foundation model (FM) on Amazon Bedrock. The FM needs to access encrypted data that is stored in an Amazon S3 bucket. The data is encrypted with Amazon S3 managed keys (SSE-S3). The FM encounters a failure when attempting to access the S3 bucket data. Which solution will meet these requirements?

- A) Ensure that the role that Amazon Bedrock assumes has permission to decrypt data with the correct encryption key.
- B) Set the access permissions for the S3 buckets to allow public access to enable access over the internet.
- C) Use prompt engineering techniques to tell the model to look for information in Amazon S3.
- D) Ensure that the S3 data does not contain sensitive information.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** The foundation model needs the appropriate permissions to decrypt the encrypted data in the S3 bucket. Ensuring that the role used by Amazon Bedrock has permission to access and decrypt the data will resolve the access failure. The other options are not suitable for addressing the encryption and permission issue.

</details>

### Q5.07 (`AIF-U1855`) — 5.1 Securing AI Systems, Data Protection & Grounding
> Which option describes embeddings in the context of AI?

- A) A method for compressing large datasets
- B) An encryption method for securing sensitive data
- C) A method for visualizing high-dimensional data
- D) A numerical method for data representation in a reduced dimensionality space

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** Embeddings in AI refer to numerical representations of data (e.g., text, images) in a lower-dimensional space, capturing semantic or contextual relationships. They are widely used in NLP and other AI tasks to represent complex data in a format that models can process efficiently.Exact Extract from AWS AI Documents:From the AWS AI Practitioner Learning Path:" Embeddings are numerical representations of data in a reduced dimensionality space. In natural language processing, for example, word or sentence embeddings capture semantic relationships, enabling models to process text efficiently for tasks like classification or similarity search. "(Source: AWS AI Practitioner Learning Path, Module on AI Concepts)Detailed Explanation:Option A: A method for compressing large datasetsWhile embeddings reduce dimensionality, their primary purpose is not data compression but rather to represent data in a way that preserves meaningful relationships. This option is incorrect.Option B: An encryption method for securing sensitive dataEmbeddings are not related to encryption or data security. They are used for data representation, making this option incorrect.Option C: A method for visualizing high-dimensional dataWhile embeddings can sometimes be used in visualization (e.g., t-SNE), their primary role is data representation for model processing, not visualization. This option is misleading.Option D: A numerical method for data representation in a reduced dimensionality spaceThis is the correct answer. Embeddings transform complex data into lower-dimensional numerical vectors, preserving semantic or contextual information for use in AI models.

</details>

### Q5.08 (`AIF-U1849`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A financial company has offices in different countries worldwide. The company requires that all API calls between generative AI applications and foundation models (FMs) must not travel across the public internet.Which AWS service should the company use?

- A) AWS PrivateLink
- B) Amazon Q
- C) Amazon CloudFront
- D) AWS CloudTrail

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** The verified answer is A. AWS PrivateLink. The requirement is that API calls between generative AI applications and foundation models must not travel across the public internet. AWS documentation states that AWS PrivateLink can create a private connection between a VPC and Amazon Bedrock. With this configuration, applications can access Amazon Bedrock as if it were inside the VPC, without requiring an internet gateway, NAT device, VPN connection, or Direct Connect connection. AWS also states that instances in the VPC do not need public IP addresses to access Amazon Bedrock. This exactly satisfies the requirement for private API communication to foundation models.Amazon Q is incorrect because Amazon Q is a generative AI assistant service for business, developer, and data use cases. It is not the network service used to privately route API calls between applications and FMs.Amazon CloudFront is incorrect because CloudFront is a content delivery network. It caches and delivers content through edge locations, but it is not the correct service for private VPC-to-AWS-service connectivity that avoids the public internet.AWS CloudTrail is incorrect because CloudTrail records account activity and API events for governance, audit, and security analysis. It helps track what happened, but it does not provide private network connectivity.The key phrase is “must not travel across the public internet.” In AWS architecture, that requirement points to private connectivity using VPC endpoints powered by AWS PrivateLink. Therefore, the correct service is AWS PrivateLink.

</details>

### Q5.09 (`AIF-U1848`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company wants to develop a large language model (LLM) application by using Amazon Bedrock and customer data that is uploaded to Amazon S3. The company ' s security policy states that each team can access data for only the team ' s own customers.Which solution will meet these requirements?

- A) Create an Amazon Bedrock custom service role for each team that has access to only the team ' s customer data.
- B) Create a custom service role that has Amazon S3 access. Ask teams to specify the customer name on each Amazon Bedrock request.
- C) Redact personal data in Amazon S3. Update the S3 bucket policy to allow team access to customer data.
- D) Create one Amazon Bedrock role that has full Amazon S3 access. Create IAM roles for each team that have access to only each team ' s customer folders.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** To comply with the company ' s security policy, which restricts each team to access data for only their own customers, creating an Amazon Bedrock custom service role for each team is the correct solution.Custom Service Role Per Team:A custom service role for each team ensures that the access control is granular, allowing only specific teams to access their own customer data in Amazon S3.This setup aligns with the principle of least privilege, ensuring teams can only interact with data they are authorized to access.Why Option A is Correct:Access Control: Allows precise access permissions for each team ' s data.Security Compliance: Directly meets the company ' s security policy requirements by ensuring data segregation.Why Other Options are Incorrect:B. Custom service role with customer name specification: This approach is impractical as it relies on manual input, which is prone to errors and does not inherently enforce data access controls.C. Redacting personal data and updating S3 bucket policy: Redaction does not solve the requirement for team-specific access, and updating bucket policies is less granular than creating roles.D. One Bedrock role with full S3 access and IAM roles for teams: This setup does not meet the least privilege principle, as having a single role with full access is contrary to the company ' s security policy.Thus, A is the correct answer to meet the company ' s security requirements.

</details>

### Q5.10 (`AIF-U1852`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A medical company deployed a disease detection model on Amazon Bedrock. To comply with privacy policies, the company wants to prevent the model from including personal patient information in its responses. The company also wants to receive notification when policy violations occur.Which solution meets these requirements?

- A) Use Amazon Macie to scan the model ' s output for sensitive data and set up alerts for potential violations.
- B) Configure AWS CloudTrail to monitor the model ' s responses and create alerts for any detected personal information.
- C) Use Guardrails for Amazon Bedrock to filter content. Set up Amazon CloudWatch alarms for notification of policy violations.
- D) Implement Amazon SageMaker Model Monitor to detect data drift and receive alerts when model quality degrades.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:aws_managed_ai_rekognition_cv`  
**Explanation:** Guardrails for Amazon Bedrock provide mechanisms to filter and control the content generated by models to comply with privacy and policy requirements. Using guardrails ensures that sensitive or personal information is not included in the model ' s responses. Additionally, integrating Amazon CloudWatch alarms allows for real-time notification when a policy violation occurs.Option C (Correct): " Use Guardrails for Amazon Bedrock to filter content. Set up Amazon CloudWatch alarms for notification of policy violations " : This is the correct answer because it directly addresses both the prevention of policy violations and the requirement to receive notifications when such violations occur.Option A: " Use Amazon Macie to scan the model ' s output for sensitive data " is incorrect because Amazon Macie is designed to monitor data in S3, not to filter real-time model outputs.Option B: " Configure AWS CloudTrail to monitor the model ' s responses " is incorrect because CloudTrail tracks API activity and is not suited for content moderation.Option D: " Implement Amazon SageMaker Model Monitor to detect data drift " is incorrect because data drift detection does not address content moderation or privacy compliance.AWS AI Practitioner References:Guardrails in Amazon Bedrock: AWS provides guardrails to ensure AI models comply with content policies, and using CloudWatch for alerting integrates monitoring capabilities.

</details>

### Q5.11 (`AIF-U1853`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How can companies use large language models (LLMs) securely on Amazon Bedrock?

- A) Design clear and specific prompts. Configure AWS Identity and Access Management (IAM) roles and policies by using least privilege access.
- B) Enable AWS Audit Manager for automatic model evaluation jobs.
- C) Enable Amazon Bedrock automatic model evaluation jobs.
- D) Use Amazon CloudWatch Logs to make models explainable and to monitor for bias.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** To securely use large language models (LLMs) on Amazon Bedrock, companies should design clear and specific prompts to avoid unintended outputs and ensure proper configuration of AWS Identity and Access Management (IAM) roles and policies with the principle of least privilege. This approach limits access to sensitive resources and minimizes the potential impact of security incidents.Option A (Correct): " Design clear and specific prompts. Configure AWS Identity and Access Management (IAM) roles and policies by using least privilege access " : This is the correct answer as it directly addresses both security practices in prompt design and access management.Option B: " Enable AWS Audit Manager for automatic model evaluation jobs " is incorrect because Audit Manager is for compliance and auditing, not directly related to secure LLM usage.Option C: " Enable Amazon Bedrock automatic model evaluation jobs " is incorrect because Bedrock does not provide automatic model evaluation jobs specifically for security purposes.Option D: " Use Amazon CloudWatch Logs to make models explainable and to monitor for bias " is incorrect because CloudWatch Logs are used for monitoring and not directly for making models explainable or secure.AWS AI Practitioner References:Secure AI Practices on AWS: AWS recommends configuring IAM roles and using least privilege access to ensure secure usage of AI models.

</details>

### Q5.12 (`AIF-U1854`) — 5.1 Securing AI Systems, Data Protection & Grounding
> Which AWS service makes foundation models (FMs) available to help users build and scale generative AI applications?

- A) Amazon Q Developer
- B) Amazon Bedrock
- C) Amazon Kendra
- D) Amazon Comprehend

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** The correct answer is Amazon Bedrock, AWS’s fully managed service for building and scaling generative AI applications using foundation models (FMs). Bedrock gives developers access to models from leading providers such as Anthropic (Claude), Meta (Llama), Mistral, Cohere, and Amazon Titan. Users can invoke these models via API without managing infrastructure or model training. According to AWS documentation, Bedrock supports tasks such as text generation, summarization, question answering, image generation, and RAG workflows with minimal setup. It supports both on-demand and provisioned throughput modes and integrates with features like Guardrails, Knowledge Bases, and Agents for secure, enterprise-grade applications. Amazon Q Developer is a generative AI tool for developers, but it doesn’t host or scale models. Amazon Kendra is an intelligent search engine, and Amazon Comprehend is used for NLP tasks like entity extraction—not foundation model access.Referenced AWS AI/ML Documents and Study Guides:Amazon Bedrock Developer Guide – Foundation Models and Use CasesAWS Certified ML Specialty Guide – Generative AI on AWS

</details>

### Q5.13 (`AIF-U1845`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company is using Amazon SageMaker Studio notebooks to build and train ML models. The company stores the data in an Amazon S3 bucket. The company needs to manage the flow of data from Amazon S3 to SageMaker Studio notebooks.Which solution will meet this requirement?

- A) Use Amazon Inspector to monitor SageMaker Studio.
- B) Use Amazon Macie to monitor SageMaker Studio.
- C) Configure SageMaker to use a VPC with an S3 endpoint.
- D) Configure SageMaker to use S3 Glacier Deep Archive.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** To manage the flow of data from Amazon S3 to SageMaker Studio notebooks securely, using a VPC with an S3 endpoint is the best solution.Amazon SageMaker and S3 Integration:Configuring SageMaker to use a Virtual Private Cloud (VPC) with an S3 endpoint allows the data flow between Amazon S3 and SageMaker Studio notebooks to occur over a private network.This setup ensures that traffic between SageMaker and S3 does not traverse the public internet, enhancing security and performance.Why Option C is Correct:Secure Data Transfer: Ensures secure, private connectivity between SageMaker and S3, reducing exposure to potential security risks.Direct Access to S3: Using an S3 endpoint in a VPC allows direct access to data in S3 without leaving the AWS network.Why Other Options are Incorrect:A. Amazon Inspector: Focuses on identifying security vulnerabilities, not managing data flow.B. Amazon Macie: Monitors for sensitive data but does not manage data flow between S3 and SageMaker.D. S3 Glacier Deep Archive: Is a storage class for archiving data, not for managing active data flow.

</details>

### Q5.14 (`AIF-U1847`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A company needs to log all requests made to its Amazon Bedrock API. The company must retain the logs securely for 5 years at the lowest possible cost.Which combination of AWS service and storage class meets these requirements? (Select TWO.)

- A) AWS CloudTrail
- B) Amazon CloudWatch
- C) AWS Audit Manager
- D) Amazon S3 Intelligent-Tiering
- E) Amazon S3 Standard

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A, D`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** AWS CloudTrail is the AWS service designed for logging and monitoring API calls made to AWS services, including Amazon Bedrock. CloudTrail records detailed information about the API requests, including the identity of the requester, the time of the request, and the source IP address. This service is ideal for logging all requests made to the Amazon Bedrock API and meets the logging requirement. Amazon S3 Intelligent-Tiering is a storage class designed for storing data that has unpredictable access patterns. It automatically moves data between two access tiers (frequent and infrequent) based on usage, which helps reduce costs while ensuring data is still available when needed. For retaining logs securely over 5 years at the lowest possible cost, this storage class provides an efficient way to handle long-term storage requirements without incurring unnecessary costs.

</details>

### Q5.15 (`AIF-U1851`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A hospital is developing an AI system to assist doctors in diagnosing diseases based on patient records and medical images. To comply with regulations, the sensitive patient data must not leave the country the data is located in. Which data governance strategy will ensure compliance and protect patient privacy?

- A) Data residency
- B) Data quality
- C) Data discoverability
- D) Data enrichment

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:sec_data_lineage_and_grounding`  
**Explanation:** Data residency refers to the practice of ensuring that data is stored and processed within a specific geographical location to comply with regulations or policies. In this scenario, where sensitive patient data must not leave the country it originates from, implementing a data residency strategy ensures compliance with legal and regulatory requirements while protecting patient privacy. This approach is crucial for organizations like hospitals operating under strict data governance frameworks such as HIPAA or GDPR.

</details>

### Q5.16 (`AIF-U1846`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A company is using the Generative AI Security Scoping Matrix to assess security responsibilities for its solutions. The company has identified four different solution scopes based on the matrix. Which solution scope gives the company the MOST ownership of security responsibilities?

- A) Using a third-party enterprise application that has embedded generative AI features.
- B) Building an application by using an existing third-party generative AI foundation model (FM).
- C) Refining an existing third-party generative AI foundation model (FM) by fine-tuning the model by using data specific to the business.
- D) Building and training a generative AI model from scratch by using specific data that a customer owns.

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:fm_training_finetuning_rlhf`  
**Explanation:** Building and training a generative AI model from scratch gives the company the most ownership of security responsibilities, as it involves full control over data, training, deployment, and security measures. The other options involve varying levels of dependency on third-party tools and services, which reduces the company's ownership of security.

</details>

### Q5.17 (`AIF-U1850`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A financial company uses AWS to host its generative AI models. The company must generate reports to show adherence to international regulations for handling sensitive customer data.

- A) Amazon Macie
- B) AWS Artifact
- C) AWS Secrets Manager
- D) AWS Config

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** AWS Artifact provides on-demand access to AWS’s compliance reports and certifications (for example, ISO, SOC, GDPR), enabling the company to demonstrate its generative AI workloads and data handling practices adhere to international regulatory requirements.

</details>

### Q5.18 (`AIF-U1856`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A company is using Amazon Bedrock to process vendor invoices. The company needs to obtain compliance documentation for submission to regulatory authorities.Which AWS service meets these requirements?

- A) AWS Config
- B) Amazon Bedrock
- C) Amazon SageMaker AI
- D) AWS Artifact

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** The verified answer is D. AWS Artifact. The company needs compliance documentation for submission to regulatory authorities. AWS Artifact is the AWS service designed for this exact requirement. AWS describes AWS Artifact as a self-service portal that provides on-demand access to AWS security and compliance reports and agreements. AWS also states that customers can use AWS Artifact to access AWS and independent software vendor security and compliance reports, download compliance reports, and manage compliance agreements. This directly matches the need to obtain documentation for auditors or regulators.AWS compliance guidance also explains that AWS supports many security standards and compliance certifications, and AWS reports such as SOC reports help customers and auditors understand AWS controls established to support operations and compliance. AWS Artifact is the mechanism customers use to retrieve many of these compliance documents. Therefore, if the company is using Amazon Bedrock and needs compliance documentation related to AWS services, AWS Artifact is the appropriate service.AWS Config is incorrect because it records, evaluates, and audits AWS resource configurations. It can help assess whether resources comply with internal rules, but it is not the service for obtaining AWS compliance reports for submission to regulators. Amazon Bedrock is incorrect because Bedrock is the generative AI service being used to process invoices; it does not serve as the compliance report portal. Amazon SageMaker AI is incorrect because SageMaker AI is used to build, train, deploy, and manage machine learning models. It is not the AWS service for downloading AWS compliance documentation.The question is not asking how to process invoices securely or how to configure Bedrock controls. It is asking where to obtain formal compliance documentation. The correct AWS service is AWS Artifact.

</details>

### Q5.19 (`AIF-U1857`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company is using custom models in Amazon Bedrock for a generative AI application. The company wants to use a company managed encryption key to encrypt the model artifacts that the model customization jobs create. Which AWS service meets these requirements?

- A) AWS Key Management Service (AWS KMS)
- B) Amazon Inspector
- C) Amazon Macie
- D) AWS Secrets Manager

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** AWS Key Management Service (AWS KMS) is a fully managed service that allows you to create and control encryption keys used to encrypt your data. It is ideal for scenarios like this, where a company wants to use a custom, company-managed encryption key to protect model artifacts. AWS KMS allows you to securely manage keys for encrypting and decrypting data, and it integrates with various AWS services, including Amazon Bedrock. AWS KMS provides centralized key management, and it is designed for use cases that involve encrypting both data and artifacts, such as model customization jobs.

</details>

### Q5.20 (`AIF-U1863`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> Which phase of the ML lifecycle determines compliance and regulatory requirements?

- A) Feature engineering
- B) Model training
- C) Data collection
- D) Business goal identification

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:domain_5_core_concept`  
**Explanation:** The data collection phase of the ML lifecycle is the most relevant for determining compliance and regulatory requirements. During this phase, organizations must ensure that the data being collected and used for training the model complies with legal and regulatory standards, such as data privacy laws (e.g., GDPR, HIPAA), industry-specific regulations, and ethical considerations. The organization must also verify that they have the proper consent to use the data and that the data does not contain any biases or violate any regulations.

</details>

### Q5.21 (`AIF-U1862`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> Which ML technique ensures data compliance and privacy when training AI models on AWS?

- A) Reinforcement learning
- B) Transfer learning
- C) Federated learning
- D) Unsupervised learning

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:ml_paradigms_supervised_unsupervised_rl`  
**Explanation:** Federated learning lets you train a global model across multiple data holders (for example, different AWS accounts or edge devices) without moving raw data to a central location. Each participant trains locally on its own private dataset and only shares model updates, preserving data privacy and ensuring compliance.

</details>

### Q5.22 (`AIF-U1859`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company wants to set up private access to Amazon Bedrock APIs from the company’s AWS account. The company also wants to protect its data from internet exposure. Which solution meets these requirements?

- A) Use Amazon CloudFront to restrict access to the company’s private content.
- B) Use AWS Glue to set up data encryption across the company’s data catalog.
- C) Use AWS Lake Formation to manage centralized data governance and cross-account data sharing.
- D) Use AWS PrivateLink to configure a private connection between the company’s VPC and Amazon

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** AWS PrivateLink enables private connectivity between your VPC and Amazon Bedrock APIs without exposing data to the public internet, ensuring that all API calls and data transfers remain secure and private within your AWS account.

</details>

### Q5.23 (`AIF-U1858`) — 5.1 Securing AI Systems, Data Protection & Grounding
> A company uses a third-party model on Amazon Bedrock to analyze confidential documents. The company is concerned about data privacy. Which statement describes how Amazon Bedrock protects data privacy?

- A) User inputs and model outputs are anonymized and shared with third-party model providers.
- B) User inputs and model outputs are not shared with any third-party model providers.
- C) User inputs are kept confidential, but model outputs are shared with third-party model providers.
- D) User inputs and model outputs are redacted before the inputs and outputs are shared with third-party

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** Amazon Bedrock processes your data entirely within AWS’s secure environment and does not forward your inputs or the generated outputs back to the model vendor, ensuring that your confidential documents remain private.

</details>

### Q5.24 (`AIF-U1983`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> How does AWS Identity and Access Management (IAM) support compliance in AI solutions?

- A) By deploying models
- B) By enforcing access policies and permissions
- C) By increasing storage capacity
- D) By monitoring API activity

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** **Correct answer: By enforcing access policies and permissions** AWS Identity and Access Management (IAM) is a fundamental service for security and compliance on AWS. In the context of AI solutions, IAM enables you to control who (identities) can access what (resources) and how (permissions). By defining granular access policies, you can ensure that only authorized personnel can access sensitive AI models, datasets, and infrastructure. This helps meet compliance requirements related to data privacy, security, and governance. For example, you can restrict access to training data containing personally identifiable information (PII) to only authorized data scientists and engineers. IAM policies can also enforce the principle of least privilege, granting users only the minimum permissions necessary to perform their tasks, further reducing the risk of unauthorized access or data breaches. This is crucial for maintaining compliance with regulations like GDPR or HIPAA when dealing with sensitive data in AI applications. **Incorrect:** **A. By deploying models** - IAM does not directly deploy AI models. Model deployment is typically handled by services like Amazon SageMaker, AWS Lambda, or Amazon ECS. While IAM is used to control access to these services and the deployed models, it's not responsible for the deployment process itself. **C. By increasing storage capacity** - IAM does not manage storage capacity. Storage capacity is managed by services like Amazon S3, Amazon EBS, or Amazon EFS. IAM controls access to these storage services, but it does not directly increase or manage their capacity. **D. By monitoring API activity** - While IAM integrates with AWS CloudTrail, which monitors API activity, IAM itself doesn't perform the monitoring. CloudTrail records API calls made to AWS services, and IAM policies control which API calls users are authorized to make. The monitoring is done by CloudTrail, and IAM provides the access control framework that determines what activity is permitted and therefore potentially logged.

</details>

### Q5.25 (`AIF-U1974`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How does Amazon Bedrock ensure data privacy during foundation model tuning?

- A) By creating a private copy of the foundation model
- B) By disabling data encryption
- C) By using public datasets
- D) By using internet traffic for data transfer

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** **Correct answer: By creating a private copy of the foundation model** Amazon Bedrock ensures data privacy during foundation model tuning by creating a private copy of the foundation model. When you fine-tune a foundation model (FM) on Amazon Bedrock, the service creates a dedicated, isolated copy of the model specifically for your use. Your training data is used to adjust the parameters of this private copy, and the original FM remains untouched. This approach prevents your training data from being mixed with the data of other users and ensures that your fine-tuned model is only accessible to you. This isolation is a key security feature, addressing concerns about data leakage and maintaining the confidentiality of your proprietary information. This aligns with security best practices for AI/ML, where data isolation is crucial for protecting sensitive information. **Incorrect:** **B. By disabling data encryption** - Disabling data encryption would severely compromise data privacy and security, which is the opposite of what Amazon Bedrock aims to achieve. Encryption is a fundamental security measure to protect data at rest and in transit. **C. By using public datasets** - While public datasets can be used with Amazon Bedrock, relying solely on them does not guarantee data privacy during fine-tuning. The privacy concern arises from the data used to fine-tune the model, regardless of whether it's public or private. Using only public datasets doesn't address the need to keep your fine-tuning process and the resulting model isolated. **D. By using internet traffic for data transfer** - Using internet traffic for data transfer, without proper security measures, would increase the risk of data breaches and compromise data privacy. Amazon Bedrock uses secure channels for data transfer, and the method of transfer is not the primary mechanism for ensuring data privacy during model tuning. The creation of a private model copy is the key factor.

</details>

### Q5.26 (`AIF-U1976`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How does Amazon Bedrock ensure the privacy of data used for customizing foundation models?

- A) By encrypting data at rest and in transit
- B) By applying strict IAM policies
- C) By creating private, customized copies of the base model
- D) By using dedicated hardware

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** **Correct answer: By creating private, customized copies of the base model** Amazon Bedrock ensures data privacy during foundation model customization by creating private, customized copies of the base model. When you customize a model with your data, Bedrock doesn't modify the original base model. Instead, it creates a new, private version of the model that is only accessible to you. This ensures that your data is not used to train or influence the original base model, and that other users cannot access your customized model or the data used to create it. This isolation is a key aspect of Bedrock's security and privacy design. **Incorrect:** **A. By encrypting data at rest and in transit** - While encryption at rest and in transit is a standard security practice employed by AWS, including Amazon Bedrock, it is not the primary mechanism for ensuring data privacy during model customization. Encryption protects the data from unauthorized access, but it doesn't prevent the data from being used to train the base model. The creation of private model copies is the key differentiator for privacy. **B. By applying strict IAM policies** - IAM (Identity and Access Management) policies are crucial for controlling access to AWS resources, including Amazon Bedrock and the data used for customization. However, IAM policies alone do not guarantee that your data will not be used to train the original base model or that other users cannot access your customized model. IAM controls access, but the creation of private model copies provides the data isolation needed for privacy. **D. By using dedicated hardware** - While dedicated hardware can provide enhanced security and isolation, Amazon Bedrock does not rely on dedicated hardware as the primary mechanism for ensuring data privacy during model customization. The creation of private, customized copies of the base model is the core privacy feature, regardless of the underlying hardware.

</details>

### Q5.27 (`AIF-U2022`) — 5.1 Securing AI Systems, Data Protection & Grounding
> Which AWS service can help with the secure integration of Bedrock into an enterprise system?

- A) Amazon CloudFront
- B) AWS Lambda
- C) Amazon S3
- D) AWS IAM Identity Center

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** **Correct answer: AWS IAM Identity Center** AWS IAM Identity Center (successor to AWS Single Sign-On) is the AWS service that enables you to securely manage access to AWS accounts and applications, including Bedrock. It allows you to centrally manage identities and permissions, providing single sign-on access to Bedrock and other AWS services. This ensures that only authorized users and applications can interact with Bedrock, adhering to enterprise security policies and compliance requirements. IAM Identity Center facilitates secure integration by providing a centralized point for authentication and authorization, simplifying user management and enhancing security posture. **Incorrect:** **A. Amazon CloudFront** - Amazon CloudFront is a content delivery network (CDN) service. While it can be used to deliver content generated by Bedrock, it doesn't directly address the secure integration of Bedrock into an enterprise system in terms of authentication and authorization. Its primary function is content caching and delivery, not identity and access management. **B. AWS Lambda** - AWS Lambda is a serverless compute service. While Lambda functions can be used to interact with Bedrock, Lambda itself doesn't provide the necessary mechanisms for secure user authentication, authorization, and centralized identity management required for secure enterprise integration. Lambda functions would need to be integrated with an identity provider. **C. Amazon S3** - Amazon S3 is an object storage service. While S3 can be used to store data used by or generated by Bedrock, it doesn't provide the identity and access management capabilities needed for secure enterprise integration. S3 access control mechanisms are useful for securing the data itself, but not for managing user access to Bedrock's APIs and services.

</details>

### Q5.28 (`AIF-U1982`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How does AWS address privacy concerns in AI?

- A) By limiting data collection
- B) By implementing data encryption and access controls
- C) By avoiding compliance with regulations
- D) By ignoring user data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** **Correct answer: By implementing data encryption and access controls** AWS addresses privacy concerns in AI by implementing robust data encryption and access controls. Encryption protects data both in transit and at rest, making it unreadable to unauthorized parties. Access controls, such as Identity and Access Management (IAM) policies, limit who can access and modify data and AI models. These measures help ensure that sensitive data used in AI applications remains private and secure, aligning with compliance requirements and best practices for data governance. AWS services like Key Management Service (KMS) and CloudHSM facilitate encryption key management, while IAM enables fine-grained access control policies. **Incorrect:** **A. By limiting data collection** - While minimizing data collection can be a privacy-enhancing technique, it's not the primary way AWS addresses privacy concerns in AI. AWS focuses on providing tools and services to manage and protect the data that is collected, regardless of the volume. Limiting data collection is a separate consideration related to data minimization principles. **C. By avoiding compliance with regulations** - AWS does not avoid compliance with regulations. In fact, AWS prioritizes compliance with various global and regional regulations, such as GDPR, HIPAA, and FedRAMP. AWS provides services and features that help customers meet their compliance obligations when using AI services. **D. By ignoring user data** - Ignoring user data would be a direct violation of privacy principles and regulations. AWS provides tools and services to help customers manage and protect user data, not ignore it. AWS is committed to data privacy and security.

</details>

### Q5.29 (`AIF-U2015`) — 5.1 Securing AI Systems, Data Protection & Grounding
> What is the role of AWS CloudTrail in AI governance?

- A) To deploy machine learning models
- B) To manage encryption keys
- C) To monitor API activity and provide audit logs
- D) To store training data

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** **Correct answer: To monitor API activity and provide audit logs** AWS CloudTrail plays a crucial role in AI governance by providing visibility into API activity within your AWS environment. Specifically, it logs actions taken by users, roles, and AWS services. This includes API calls made to AWS AI services like Amazon SageMaker, Amazon Rekognition, Amazon Comprehend, and others. These logs are essential for auditing, security monitoring, and compliance purposes. By analyzing CloudTrail logs, organizations can track who accessed AI resources, what actions they performed, and when these actions occurred. This information is vital for identifying potential security breaches, ensuring compliance with regulatory requirements, and maintaining accountability in AI deployments. CloudTrail helps organizations adhere to responsible AI practices by providing a clear audit trail of AI-related activities. **Incorrect:** **A. To deploy machine learning models** - AWS CloudTrail is not used for deploying machine learning models. Model deployment is typically handled by services like Amazon SageMaker, which provides tools and infrastructure for deploying and managing ML models. **B. To manage encryption keys** - While CloudTrail can log API calls related to AWS Key Management Service (KMS), which is used for managing encryption keys, its primary role is not key management itself. KMS is the service dedicated to creating, storing, and controlling encryption keys. **D. To store training data** - AWS CloudTrail does not store training data. Services like Amazon S3, Amazon EFS, or Amazon FSx are typically used for storing the large datasets required for training machine learning models.

</details>

### Q5.30 (`AIF-U2014`) — 5.1 Securing AI Systems, Data Protection & Grounding
> What is the role of Amazon VPC in securing AI applications?

- A) To manage encryption keys
- B) To create a private network environment
- C) To provide compute resources
- D) To deploy machine learning models

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** **Correct answer: To create a private network environment** Amazon Virtual Private Cloud (VPC) plays a crucial role in securing AI applications by enabling you to launch AWS resources, including those used for AI/ML, into a logically isolated virtual network that you define. This isolation allows you to control network access to your AI applications and data, enhancing security. You can define your own IP address ranges, create subnets, configure route tables, and set up network gateways. By controlling the network environment, you can restrict access to your AI models, training data, and other sensitive resources, preventing unauthorized access and potential data breaches. This is a fundamental security best practice for AI solutions on AWS. **Incorrect:** **A. To manage encryption keys** - While AWS Key Management Service (KMS) is used for managing encryption keys, Amazon VPC itself does not directly manage encryption keys. VPC provides the network isolation where KMS-encrypted resources can reside and be accessed securely. **C. To provide compute resources** - Compute resources, such as Amazon EC2 instances or AWS SageMaker notebooks, are launched within an Amazon VPC. The VPC provides the network environment for these resources, but it does not directly provide the compute resources themselves. **D. To deploy machine learning models** - While you can deploy machine learning models within an Amazon VPC for secure access, the VPC itself does not handle the deployment process. Services like AWS SageMaker are used for deploying and hosting machine learning models, and these can be configured to operate within a VPC.

</details>

### Q5.31 (`AIF-U1970`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> How can administrators control the behavior of Amazon Q Business?

- A) By setting up IP restrictions
- B) By configuring guardrails and keywords
- C) By disabling the service for certain users
- D) By setting up separate networks

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `B`  
**Point Tested:** `point:domain_5_core_concept`  
**Explanation:** **Correct answer: By configuring guardrails and keywords** Administrators can control the behavior of Amazon Q Business primarily through configuring guardrails and keywords. Guardrails allow administrators to define acceptable use policies and prevent Q Business from generating responses that violate these policies. Keywords can be used to block specific terms or topics, ensuring that Q Business avoids sensitive or inappropriate content. This approach provides granular control over the AI's output and helps maintain compliance with organizational standards and ethical guidelines. **Incorrect:** **A. By setting up IP restrictions** - IP restrictions are typically used for controlling network access and are not directly related to controlling the behavior or content generated by Amazon Q Business. While IP restrictions can limit who can access the service, they do not influence the AI's responses or prevent specific types of content from being generated. **C. By disabling the service for certain users** - Disabling the service for certain users controls access but does not control the behavior of the service itself. While this prevents those users from interacting with Q Business, it doesn't address the content or responses generated when the service is active for other users. **D. By setting up separate networks** - Setting up separate networks isolates network traffic but does not directly influence the behavior or content generated by Amazon Q Business. Network segmentation is a security measure but does not provide the granular control over the AI's output that guardrails and keywords offer.

</details>

### Q5.32 (`AIF-U1984`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How does Managed Spot Training reduce costs in SageMaker?

- A) By providing data encryption
- B) By increasing model complexity
- C) By using EC2 Spot Instances
- D) By extending training duration

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_pricing_on_demand_vs_provisioned`  
**Explanation:** **Correct answer: By using EC2 Spot Instances** Managed Spot Training in SageMaker leverages EC2 Spot Instances to reduce costs. EC2 Spot Instances are spare compute capacity available in the AWS cloud at discounted prices compared to On-Demand instances. SageMaker can automatically manage the process of requesting Spot Instances for training jobs, handling interruptions, and resuming training from checkpoints, allowing you to take advantage of the cost savings without the operational overhead of managing Spot Instances directly. This is a cost optimization strategy, as Spot Instances can offer significant discounts (up to 90%) compared to On-Demand pricing. **Incorrect:** **A. By providing data encryption** - While SageMaker provides data encryption features (both at rest and in transit), data encryption is primarily a security measure and not directly related to the cost reduction achieved by Managed Spot Training. Encryption protects data confidentiality and integrity, but it doesn't inherently lower the cost of compute resources. **B. By increasing model complexity** - Increasing model complexity generally increases computational requirements and, therefore, costs. Managed Spot Training aims to reduce costs for a given model complexity, not by increasing it. **D. By extending training duration** - Extending training duration would typically increase costs, not reduce them. Managed Spot Training aims to reduce the cost per unit of training time by using cheaper compute resources (Spot Instances), even if the training takes slightly longer due to potential interruptions and restarts.

</details>

### Q5.33 (`AIF-U1972`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> How can you enhance prompt robustness against attacks?

- A) By implementing dynamic and context-aware templates
- B) By using static templates
- C) By ignoring security
- D) By reducing token usage

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** **Correct answer: By implementing dynamic and context-aware templates** Dynamic and context-aware templates enhance prompt robustness by adapting the prompt based on the specific input and context. This makes it more difficult for attackers to craft adversarial inputs that exploit vulnerabilities in the prompt. By incorporating context, the AI model can better understand the user's intent and filter out malicious or irrelevant information. This approach helps mitigate prompt injection attacks, where attackers try to manipulate the model's behavior by injecting malicious instructions into the prompt. Dynamic templates can also include validation checks and sanitization steps to further protect against attacks. This aligns with responsible AI practices by ensuring the AI system is secure and reliable. **Incorrect:** **B. By using static templates** - Static templates are vulnerable to prompt injection attacks because they do not adapt to the input. Attackers can easily craft inputs that exploit the fixed structure of the prompt to manipulate the model's behavior. **C. By ignoring security** - Ignoring security is the opposite of enhancing prompt robustness. It leaves the AI system vulnerable to various attacks, including prompt injection, data poisoning, and model evasion. **D. By reducing token usage** - Reducing token usage might improve efficiency but does not directly address prompt robustness against attacks. While shorter prompts can sometimes be less vulnerable, this is not a reliable security measure. Attackers can still craft malicious inputs within a limited number of tokens.

</details>

### Q5.34 (`AIF-U2021`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> Which AWS service can be used to record actions taken by Amazon Q Business?

- A) Amazon S3
- B) AWS CodeBuild
- C) AWS CloudTrail
- D) AWS CloudFormation

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:fm_rag_knowledge_bases`  
**Explanation:** **Correct answer: AWS CloudTrail** AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail logs API calls made to AWS services, including Amazon Q Business. By enabling CloudTrail, you can record actions taken by users and services within your AWS environment, providing a detailed audit trail for security analysis, resource change tracking, and troubleshooting. This is crucial for maintaining compliance and understanding the usage patterns of Amazon Q Business within your organization. **Incorrect:** **A. Amazon S3** - Amazon S3 is an object storage service for storing and retrieving data. While Amazon Q Business might store data in S3, S3 itself does not record the actions taken *by* Amazon Q Business. S3 provides its own logging mechanisms, but these logs are focused on access to S3 buckets and objects, not the actions of other AWS services. **B. AWS CodeBuild** - AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. It is not designed for auditing or recording actions taken by services like Amazon Q Business. **D. AWS CloudFormation** - AWS CloudFormation is a service that allows you to model and provision AWS resources using code. While you might use CloudFormation to deploy and configure Amazon Q Business, it does not record the actions taken by Amazon Q Business after it has been deployed. CloudFormation is focused on infrastructure as code and deployment automation, not runtime auditing.

</details>

### Q5.35 (`AIF-U1980`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How does Amazon CloudWatch support governance in AI solutions?

- A) By increasing data storage capacity
- B) By storing encryption keys
- C) By tracking usage metrics and providing logs
- D) By managing user authentication

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** **Correct answer: By tracking usage metrics and providing logs** Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS, hybrid, and on-premises applications and infrastructure resources. In the context of AI solutions, CloudWatch supports governance by enabling the tracking of usage metrics (e.g., how often a model is used, resource consumption) and providing logs (e.g., errors, performance data). This information is crucial for auditing, compliance, and identifying potential issues related to AI model performance, security, and responsible AI practices. By monitoring these metrics and logs, organizations can ensure that their AI solutions are used appropriately, comply with relevant regulations, and adhere to established governance policies. **Incorrect:** **A. By increasing data storage capacity** - While data storage is essential for AI solutions, CloudWatch's primary function is monitoring and observability, not increasing data storage capacity. Services like Amazon S3 or Amazon EBS are responsible for data storage. **B. By storing encryption keys** - Encryption keys are managed by services like AWS Key Management Service (KMS), not CloudWatch. CloudWatch focuses on monitoring and logging, not key management. **D. By managing user authentication** - User authentication is typically handled by services like AWS Identity and Access Management (IAM) or AWS Cognito. CloudWatch does not directly manage user authentication; it monitors the usage and performance of services, including those related to authentication.

</details>

### Q5.36 (`AIF-U1981`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> How does Amazon Rekognition help in security and surveillance?

- A) By providing personalized recommendations
- B) By translating surveillance footage
- C) By converting text to speech
- D) By analyzing images and videos for security threats

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** **Correct answer: By analyzing images and videos for security threats** Amazon Rekognition is a service that provides image and video analysis. In the context of security and surveillance, it can be used to detect objects, people, and activities that might indicate a security threat. For example, it can identify unauthorized personnel entering a restricted area, detect suspicious objects left unattended, or recognize known offenders. Rekognition can also be integrated with other AWS services like Amazon CloudWatch to trigger alerts based on detected events, enhancing security monitoring and response capabilities. This proactive threat detection makes it a valuable tool for enhancing security and surveillance systems. **Incorrect:** **A. By providing personalized recommendations** - Personalized recommendations are more commonly associated with services like Amazon Personalize, which analyzes user behavior to suggest relevant products or content. Rekognition focuses on image and video analysis, not personalized recommendations. **B. By translating surveillance footage** - Translation of surveillance footage would typically involve services like Amazon Translate, which converts text from one language to another. Rekognition analyzes the content of images and videos, but it doesn't perform language translation. **C. By converting text to speech** - Text-to-speech conversion is a feature of services like Amazon Polly, which transforms written text into spoken words. Rekognition's primary function is image and video analysis, not text-to-speech conversion.

</details>

### Q5.37 (`AIF-U1973`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How can you prevent prompt injection attacks in Amazon Bedrock?

- A) By using static tokens
- B) By increasing token count
- C) By implementing dynamic tokenization and validation
- D) By ignoring user inputs

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_tokens_embeddings_transformers`  
**Explanation:** **Correct answer: By implementing dynamic tokenization and validation** Prompt injection attacks occur when malicious user input manipulates the behavior of a large language model (LLM). Dynamic tokenization and validation are crucial for mitigating these attacks. Dynamic tokenization involves breaking down the input into tokens in a way that is sensitive to context and potential injection attempts. Validation then checks these tokens against expected patterns and security policies. This approach helps to identify and neutralize malicious instructions embedded within user prompts, preventing the LLM from executing unintended commands or revealing sensitive information. This is a key security consideration when deploying LLMs via Amazon Bedrock. **Incorrect:** **A. By using static tokens** - Static tokens, such as API keys, are used for authentication and authorization, not for preventing prompt injection. They do not analyze or validate the content of user inputs and therefore offer no protection against malicious prompts. **B. By increasing token count** - Increasing the token count simply allows for longer inputs. It does not address the underlying vulnerability of prompt injection. In fact, longer inputs might provide more opportunities for attackers to inject malicious code. **D. By ignoring user inputs** - Ignoring user inputs would render the LLM useless, as it would not be able to respond to any queries. This is not a practical or effective security measure. The goal is to safely process user inputs, not to avoid them entirely.

</details>

### Q5.38 (`AIF-U1975`) — 5.1 Securing AI Systems, Data Protection & Grounding
> How does Amazon Bedrock ensure security for AI-generated content?

- A) By ignoring security measures
- B) By using static IP addresses
- C) By implementing guardrails and encryption
- D) By limiting user access

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `C`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** **Correct answer: By implementing guardrails and encryption** Amazon Bedrock provides security for AI-generated content through several mechanisms, including guardrails and encryption. Guardrails allow you to implement policies that filter and monitor the input and output of foundation models, helping to prevent the generation of harmful or inappropriate content. Encryption ensures that data is protected both in transit and at rest, safeguarding the confidentiality of the data used to generate AI content. These security measures are crucial for responsible AI development and deployment, addressing potential risks associated with AI-generated content. **Incorrect:** **A. By ignoring security measures** - This is incorrect because Amazon Bedrock prioritizes security and offers various features to protect AI-generated content and user data. Ignoring security measures would be a significant risk and is not aligned with AWS's security best practices. **B. By using static IP addresses** - While static IP addresses can be part of a broader security strategy, they are not the primary method by which Amazon Bedrock ensures the security of AI-generated content. Security measures like guardrails and encryption are more directly relevant to content security. **D. By limiting user access** - Limiting user access is a valid security practice, but it's not the sole or primary method for securing AI-generated content in Amazon Bedrock. While access control is important, guardrails and encryption are more directly focused on the content itself.

</details>

### Q5.39 (`AIF-U2017`) — 5.1 Securing AI Systems, Data Protection & Grounding
> What service does AWS provide to manage encryption keys for AI solutions?

- A) AWS KMS
- B) AWS IAM
- C) Amazon S3
- D) Amazon VPC

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:sec_ai_iam_kms_privatelink_macie`  
**Explanation:** **Correct answer: AWS KMS** AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. This is crucial for AI solutions, as they often handle sensitive data that needs to be protected both at rest and in transit. KMS allows you to centrally manage keys, define usage policies, and integrate with other AWS services, ensuring that your AI applications meet security and compliance requirements. Using KMS is a best practice for securing AI workloads on AWS. **Incorrect:** **B. AWS IAM** - AWS Identity and Access Management (IAM) controls access to AWS services and resources. While IAM is essential for securing your AWS environment and AI solutions by managing user permissions and roles, it does not directly manage encryption keys. IAM focuses on authentication and authorization, not key management. **C. Amazon S3** - Amazon Simple Storage Service (S3) is an object storage service. While S3 can store data used in AI solutions, and supports encryption at rest using KMS or S3-managed keys, S3 itself is not a key management service. KMS is the dedicated service for managing encryption keys. **D. Amazon VPC** - Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. VPC provides network-level security and isolation, but it does not manage encryption keys for AI solutions. Its focus is on network configuration and security.

</details>

### Q5.40 (`AIF-U1994`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> What AWS service helps monitor and log AI solution activities for audit purposes?

- A) Amazon Rekognition
- B) Amazon S3
- C) Amazon Lex
- D) AWS CloudTrail

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `D`  
**Point Tested:** `point:aws_managed_ai_translate_lex_personalize`  
**Explanation:** **Correct answer: AWS CloudTrail** AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. CloudTrail logs API calls made to AWS services, including AI services, providing a history of account activity. This is crucial for monitoring and logging AI solution activities for audit purposes, allowing you to track who did what, when, and from where. This information is essential for security analysis, resource change tracking, and compliance auditing related to your AI solutions. **Incorrect:** **A. Amazon Rekognition** - Amazon Rekognition is an AI service for image and video analysis. While it provides insights into the content of media, it doesn't directly monitor and log activities for audit purposes in the way CloudTrail does. Rekognition's primary function is object and facial recognition, not activity logging. **B. Amazon S3** - Amazon S3 (Simple Storage Service) is an object storage service. While it can store logs generated by other services, including CloudTrail logs, S3 itself doesn't provide the monitoring and logging functionality for AI solution activities. It's a storage destination, not an auditing tool. **C. Amazon Lex** - Amazon Lex is a service for building conversational interfaces using voice and text. While Lex interactions can be logged, Lex itself doesn't provide comprehensive monitoring and logging of all AI solution activities for audit purposes. Its focus is on chatbot functionality, not auditing.

</details>

### Q5.41 (`AIF-U1978`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> How does Amazon Bedrock help in preventing potential misuse of AI models?

- A) By implementing automated abuse detection mechanisms
- B) By disabling logging
- C) By using static API keys
- D) By increasing model complexity

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:genai_bedrock_nova_jumpstart`  
**Explanation:** **Correct answer: By implementing automated abuse detection mechanisms** Amazon Bedrock includes features designed to detect and prevent the misuse of AI models. These automated abuse detection mechanisms can identify harmful or inappropriate inputs and outputs, helping to ensure responsible use of the models. This aligns with the principles of responsible AI, which emphasizes safety and ethical considerations in AI development and deployment. Bedrock's guardrails feature allows you to set up controls to filter harmful content and protect against misuse. **Incorrect:** **B. By disabling logging** - Disabling logging would hinder the ability to monitor and detect misuse. Logging is crucial for auditing and identifying potential abuse patterns. Disabling it would make it harder to ensure responsible AI usage and compliance. **C. By using static API keys** - Using static API keys does not directly prevent the misuse of AI models. While API keys are essential for authentication and authorization, they do not address the content or behavior of the model itself. Static API keys, if compromised, can even increase the risk of misuse. **D. By increasing model complexity** - Increasing model complexity does not inherently prevent misuse. In fact, more complex models can sometimes be harder to control and understand, potentially increasing the risk of unintended or harmful outputs. The focus should be on implementing safety mechanisms and monitoring, not simply increasing complexity.

</details>

### Q5.42 (`AIF-U1921`) — 5.2 AI Governance, Compliance & Scoping Frameworks
> A compliance team wants a single AWS service that continuously evaluates whether their S3 buckets and EC2 security groups remain compliant with an internal encryption-at-rest and open-port policy, flags any resource that drifts out of compliance, and lets them see what the resource's settings looked like six months ago. Which AWS service should they configure to meet this requirement?

- A) AWS Config with custom rules and configuration history
- B) AWS Artifact with downloaded compliance reports
- C) Amazon Inspector with vulnerability scan findings
- D) AWS Trusted Advisor with cost optimization checks

<details><summary><b>View Answer & Rationale</b></summary>

**Correct Answer:** `A`  
**Point Tested:** `point:gov_compliance_cloudtrail_config_artifact_inspector`  
**Explanation:** A: AWS Config with custom rules and configuration history. AWS Config rules continuously evaluate resource settings such as encryption status and security group ports against defined conditions and flag noncompliant resources, while its configuration history lets the team view settings from months earlier. This combination of continuous rule evaluation plus historical lookback matches every part of the requirement. | B: AWS Artifact with downloaded compliance reports. AWS Artifact provides static, pre-generated compliance documents about AWS's own infrastructure rather than continuously evaluating a customer's individual S3 buckets or security groups. It offers no mechanism for tracking a customer resource's configuration history. | C: Amazon Inspector with vulnerability scan findings. Amazon Inspector focuses on scanning compute resources and container images for software vulnerabilities and network reachability issues, not on evaluating encryption settings against a custom internal policy or storing configuration history. Its findings are vulnerability-oriented rather than configuration-drift-oriented. | D: AWS Trusted Advisor with cost optimization checks. Trusted Advisor offers point-in-time best-practice recommendations across several categories but does not continuously evaluate custom internal policies or retain a historical record of a resource's past configuration. It lacks the customizable rule and history features the scenario requires.

</details>
