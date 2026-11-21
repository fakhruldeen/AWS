# AIF-C01 Authentic Exam Practice Pool & Community Consensus

> **Total Questions:** 149  
> **Source:** Verified Community Consensus & Discussion Pool  
> **Pedagogical Designation:** Professional Exam Practice Suite (Recall Pool)  

---

## Question 1: AIF-C01-ET-Q001
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company makes forecasts each quarter to decide how to optimize operations to meet expected demand. The company uses ML models to make these forecasts.
An AI practitioner is writing a report about the trained ML models to provide transparency and explainability to company stakeholders.
What should the AI practitioner include in the report to meet the transparency and explainability requirements?

**Choices:**
- A) Code for model training
- B) Partial dependence plots (PDPs)
- C) Sample data for training
- D) Model convergence tables

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Partial Dependence Plots (PDPs)

Explanation:
Partial Dependence Plots (PDPs) are useful tools for understanding the relationship between specific features and the model's predictions, making it easier to see how changes in input variables affect the forecast. PDPs are particularly helpful for stakeholders because they visually show the impact of individual features on predictions without requiring a deep understanding of the model's inner workings.
---
Selected Answer: B
B is the answer Thanks to
---
Selected Answer: B
Explicação:Gráficos de dependência parcial (Partial Dependence Plots - PDPs) são usados para mostrar como uma variável de entrada afeta a previsão do modelo, mantendo as outras variáveis constantes.São ferramentas poderosas de explicabilidade e transparência, especialmente para partes interessadas não técnicas. Eles ajudam a visualizar a relação entre características importantes e as previsões do modelo, respondendo perguntas como:
"Se aumentarmos o orçamento em marketing, o que acontece com a demanda prevista?"

</details>

---

## Question 2: AIF-C01-ET-Q002
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to use language models to create an application for inference on edge devices. The inference must have the lowest latency possible.
Which solution will meet these requirements?

**Choices:**
- A) Deploy optimized small language models (SLMs) on edge devices.
- B) Deploy optimized large language models (LLMs) on edge devices.
- C) Incorporate a centralized small language model (SLM) API for asynchronous communication with edge devices.
- D) Incorporate a centralized large language model (LLM) API for asynchronous communication with edge devices.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `92%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (92%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Quando o objetivo é inferência com a menor latência possível, a melhor abordagem é executar o modelo diretamente no dispositivo de borda (edge).
SLMs (Small Language Models) são projetados para serem leves, rápidos e eficientes, o que os torna ideais para: Dispositivos com recursos limitados
Tempo de resposta imediato . Execução offline ou com pouca conectividade
---
Selected Answer: A
Optimized small language models (SLMs) are specifically designed to run efficiently on edge devices with limited resources (such as memory and processing power). Deploying smaller, optimized models directly on the edge devices allows for near-instantaneous inference with minimal latency, as the data doesn't need to travel to a central server for processing.
---
Selected Answer: A
A: Deploy optimized small language models (SLMs) on edge devices.

Explanation:
Deploying optimized small language models (SLMs) on edge devices ensures low latency because the inference happens directly on the device without relying on cloud communication. Small language models are lightweight and designed to run efficiently on devices with limited resources, making them ideal for edge computing.

</details>

---

## Question 3: AIF-C01-ET-Q003
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is developing a mobile ML app that uses a phone's camera to diagnose and treat insect bites. The company wants to train an image classification model by using a diverse dataset of insect bite photos from different genders, ethnicities, and geographic locations around the world.

Which principle of responsible AI does the company demonstrate in this scenario?

**Choices:**
- A) Fairness
- B) Explainability
- C) Governance
- D) Transparency

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
In this scenario, the company is demonstrating the principle of Fairness by ensuring their training data includes a diverse range of demographics, preventing potential biases based on gender, ethnicity, or geographic location, which aligns with the core idea of responsible AI.
---
Selected Answer: A
The correct answer is A. Fairness. Using diverse datasets ensures equal representation and performance across different demographic groups.
---
Selected Answer: A
By using a diverse dataset that includes different genders, ethnicities, and geographic locations, the company is addressing fairness by making sure the model does not discriminate against any particular group.

</details>

---

## Question 4: AIF-C01-ET-Q004
**Domain 4:** Guidelines for Responsible AI  

**Question:**  
A company is developing an ML model to make loan approvals. The company must implement a solution to detect bias in the model. The company must also be able to explain the model's predictions.

Which solution will meet these requirements?

**Choices:**
- A) Amazon SageMaker Clarify
- B) Amazon SageMaker Data Wrangler
- C) Amazon SageMaker Model Cards
- D) AWS AI Service Cards

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The solution that meets the requirements of detecting bias and explaining model predictions in a loan approval scenario is A. Amazon SageMaker Clarify
---
Selected Answer: A
The correct answer is A. SageMaker Clarify provides both bias detection and model explainability features.
---
Selected Answer: A
Amazon SageMaker Clarify provides both bias detection and model explainability features, making it the most suitable choice for detecting bias in a loan approval model and explaining its predictions.

</details>

---

## Question 5: AIF-C01-ET-Q005
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company has developed a generative text summarization model by using Amazon Bedrock. The company will use Amazon Bedrock automatic model evaluation capabilities.

Which metric should the company use to evaluate the accuracy of the model?

**Choices:**
- A) Area Under the ROC Curve (AUC) score
- B) F1 score
- C) BERTScore
- D) Real world knowledge (RWK) score

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
BERTScore: This metric leverages the capabilities of a pre-trained BERT model to assess the semantic similarity between the generated summaries and the reference text, providing a more accurate evaluation of the model's ability to capture the key points of the original text, which is crucial for text summarization.
---
Selected Answer: C
The correct answer is C. BERTScore is specifically designed for evaluating text generation quality.
---
Selected Answer: C
BERTScore is the most appropriate metric for evaluating the accuracy of a generative text summarization model because it compares semantic similarity in a manner that aligns well with the goal of text summarization.

</details>

---

## Question 6: AIF-C01-ET-Q006
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to develop an educational game where users answer questions such as the following: "A jar contains six red, four green, and three yellow marbles. What is the probability of choosing a green marble from the jar?"
Which solution meets these requirements with the LEAST operational overhead?

**Choices:**
- A) Use supervised learning to create a regression model that will predict probability.
- B) Use reinforcement learning to train a model to return the probability.
- C) Use code that will calculate probability by using simple rules and computations.
- D) Use unsupervised learning to create a model that will estimate probability density.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Estimated Costs
Memory: Less than 1 MB for the model.
Computation: A few seconds to minutes on a standard laptop CPU.
Data: A few hundred examples, which can be generated programmatically.
Instead
def calculate_probability(green_marbles, total_marbles):
 return green_marbles / total_marbles

# Example usage
green_marbles = 4
total_marbles = 6 + 4 + 3 # red + green + yellow
probability = calculate_probability(green_marbles, total_marbles)
print(f"Probability of choosing a green marble: {probability:.2f}")

A program is effective and time saving
---
Selected Answer: C
The problem described is a simple probability calculation based on basic combinatorics. The probability of choosing a green marble is simply the ratio of green marbles to total marbles, which can be computed directly without needing a complex machine learning model.
Using a straightforward code implementation to calculate the probability based on the given numbers (6 red, 4 green, and 3 yellow marbles) will be the most efficient and have the least operational overhead. It’s a direct computation using basic arithmetic.
---
Selected Answer: C
no NEED to do do anything fancy. its doable with simple code

</details>

---

## Question 7: AIF-C01-ET-Q007
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is using a large language model (LLM) on Amazon Bedrock to build a chatbot. The chatbot processes customer support requests. To resolve a request, the customer and the chatbot must interact a few times.

Which solution gives the LLM the ability to use content from previous customer messages?

**Choices:**
- A) Turn on model invocation logging to collect messages.
- B) Add messages to the model prompt.
- C) Use Amazon Personalize to save conversation history.
- D) Use Provisioned Throughput for the LLM.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Add previous messages to the model prompt.
---
Selected Answer: B
B is the correct answer. Here's why:

Adding previous messages to the prompt allows the LLM to maintain context across multiple interactions.
---
Selected Answer: B
Add messages to the model prompt.

By including the conversation history in the model's prompt, the LLM can maintain context and reference previous interactions to provide coherent and relevant responses. This approach ensures that the chatbot can understand and respond to the customer's requests based on the entire conversation history.

</details>

---

## Question 8: AIF-C01-ET-Q008
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company’s employees provide product descriptions and recommendations to customers when customers call the customer service center. These recommendations are based on where the customers are located. The company wants to use foundation models (FMs) to automate this process.

Which AWS service meets these requirements?

**Choices:**
- A) Amazon Macie
- B) Amazon Transcribe
- C) Amazon Bedrock
- D) Amazon Textract

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Amazon Bedrock

Amazon Bedrock is a fully managed service that provides access to a variety of foundation models (FMs) from leading AI companies. It allows you to build and scale generative AI applications, such as automating product recommendations and descriptions, by leveraging the capabilities of these models.
---
Selected Answer: C
C. Amazon Bedrock

</details>

---

## Question 9: AIF-C01-ET-Q009
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to upload customer service email messages to Amazon S3 to develop a business analysis application. The messages sometimes contain sensitive data. The company wants to receive an alert every time sensitive information is found.

Which solution fully automates the sensitive information detection process with the LEAST development effort?

**Choices:**
- A) Configure Amazon Macie to detect sensitive information in the documents that are uploaded to Amazon S3.
- B) Use Amazon SageMaker endpoints to deploy a large language model (LLM) to redact sensitive data.
- C) Develop multiple regex patterns to detect sensitive data. Expose the regex patterns on an Amazon SageMaker notebook.
- D) Ask the customers to avoid sharing sensitive information in their email messages.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Macie is a fully managed data security and privacy service that uses machine learning and pattern matching to automatically discover, classify, and protect sensitive data in Amazon S3. It can generate findings and alerts whenever sensitive information, such as personally identifiable information (PII) or financial data, is detected in S3 objects. This solution minimizes development effort and fully automates the process of sensitive data detection and alerting.
---
Selected Answer: A
A is the correct answer. Here's why:

Amazon Macie is specifically designed for automated sensitive data detection in S3.
---
Selected Answer: A
Configure Amazon Macie to detect sensitive information in the documents that are uploaded to Amazon S3.

Amazon Macie is a fully managed data security and privacy service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. It can be configured to monitor Amazon S3 buckets for sensitive information and send alerts when such information is detected. This solution requires minimal development effort and leverages AWS's built-in capabilities for sensitive data detection.

</details>

---

## Question 11: AIF-C01-ET-Q011
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
Which option is a benefit of using Amazon SageMaker Model Cards to document AI models?

**Choices:**
- A) Providing a visually appealing summary of a mode’s capabilities.
- B) Standardizing information about a model’s purpose, performance, and limitations.
- C) Reducing the overall computational requirements of a model.
- D) Physically storing models for archival purposes.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A opção correta é B. Padronizar informações sobre a finalidade, o desempenho e as limitações de um modelo. Os cartões de modelo do Amazon SageMaker são projetados para fornecer documentação padronizada e detalhada sobre os modelos de IA. Eles ajudam a comunicar claramente a finalidade, o desempenho e as limitações de um modelo, promovendo a transparência e o uso ético de IA. Quer saber mais sobre isso?

</details>

---

## Question 12: AIF-C01-ET-Q012
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
What does an F1 score measure in the context of foundation model (FM) performance?

**Choices:**
- A) Model precision and recall
- B) Model speed in generating responses
- C) Financial cost of operating the model
- D) Energy efficiency of the model’s computations

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `U`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: U (100%). Contributor Answer: U.

Community Rationale & Discussion:
Selected Answer: U
A resposta correta é A. Precisão e recall do modelo.

A pontuação F1 é uma métrica estatística usada para avaliar o desempenho de modelos de aprendizado de máquina, especialmente em situações de classificação. Ela representa a harmonia entre precisão (quantos dos exemplos classificados como positivos são realmente positivos) e recall (quantos dos exemplos positivos foram corretamente identificados pelo modelo). É particularmente útil quando há um equilíbrio necessário entre os dois e, muitas vezes, é aplicada em cenários com dados desbalanceados.

</details>

---

## Question 13: AIF-C01-ET-Q013
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company deployed an AI/ML solution to help customer service agents respond to frequently asked questions. The questions can change over time. The company wants to give customer service agents the ability to ask questions and receive automatically generated answers to common customer questions.

Which strategy will meet these requirements MOST cost-effectively?

**Choices:**
- A) Fine-tune the model regularly.
- B) Train the model by using context data.
- C) Pre-train and benchmark the model by using context data.
- D) Use Retrieval Augmented Generation (RAG) with prompt engineering techniques.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
se a Geração Aumentada de Recuperação (RAG) com técnicas de engenharia rápidas.

A abordagem RAG combina modelos de geração de linguagem com um sistema de recuperação de informações. Isso permite que os agentes obtenham respostas geradas automaticamente com base em perguntas e dados atualizados sem precisar ajustar ou treinar o modelo continuamente. É uma solução eficiente, especialmente quando as perguntas dos clientes mudam frequentemente, pois utiliza técnicas para buscar informações de fontes relevantes em tempo real.

</details>

---

## Question 14: AIF-C01-ET-Q014
**Domain 4:** Guidelines for Responsible AI  

**Question:**  
A company built an AI-powered resume screening system. The company used a large dataset to train the model. The dataset contained resumes that were not representative of all demographics.

Which core dimension of responsible AI does this scenario present?

**Choices:**
- A) Fairness
- B) Explainability
- C) Privacy and security
- D) Transparency

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `U`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: U (100%). Contributor Answer: U.

Community Rationale & Discussion:
Selected Answer: U
A dimensão central apresentada nesse cenário é A. Justiça.

O sistema de triagem de currículos enfrenta desafios relacionados à justiça, pois foi treinado com dados que não são representativos de todos os grupos demográficos. Isso pode introduzir vieses no modelo, prejudicando certos grupos enquanto favorece outros. Em sistemas de IA responsáveis, é essencial abordar esses vieses, garantindo que os dados de treinamento sejam equilibrados e inclusivos para promover resultados justos.

</details>

---

## Question 15: AIF-C01-ET-Q015
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
A global financial company has developed an ML application to analyze stock market data and provide stock market trends. The company wants to continuously monitor the application development phases and to ensure that company policies and industry regulations are followed.

Which AWS services will help the company assess compliance requirements? (Choose two.)

**Choices:**
- A) AWS Audit Manager
- B) AWS Config
- C) Amazon Inspector
- D) Amazon CloudWatch
- E) AWS CloudTrail

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
> [!WARNING] Answer Controversy  
> Contributor marked `UB`, but community consensus voted `B` with 100% agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: UB.

Community Rationale & Discussion:
Selected Answer: UB
Os dois serviços da AWS que ajudarão a empresa a avaliar os requisitos de conformidade são:

A. Gerenciador de Auditoria da AWS: Ele auxilia no gerenciamento contínuo de auditorias ao automatizar a coleta de evidências relacionadas à conformidade com as políticas da empresa e regulamentos do setor.

B. Configuração da AWS: Este serviço permite monitorar e avaliar configurações de recursos continuamente para garantir que estejam em conformidade com as políticas e regulamentos definidos.

</details>

---

## Question 16: AIF-C01-ET-Q016
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
Which metric measures the runtime efficiency of operating AI models?

**Choices:**
- A) Customer satisfaction score (CSAT)
- B) Training time for each epoch
- C) Average response time
- D) Number of training instances

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Average response time refers to the time taken by an AI model to produce a result after receiving an input. It is a critical metric for assessing the runtime efficiency of an AI model during inference, particularly in applications where quick responses are essential, such as in real-time applications or interactive systems.
---
Selected Answer: C
O tempo médio de resposta mede a eficiência do tempo de execução de um modelo operacional de IA — ou seja, quanto tempo ele leva para processar uma solicitação e Retornar uma resposta. Isso é crucial em ambientes de produção onde a latência pode impactar a experiência do usuário e a performance do sistema. As outras opções não medem diretamente a eficiência operacional em tempo de execução: A. CSAT (Customer Satisfaction Score) avalia a satisfação do cliente, não o desempenho técnico do modelo.

B. Tempo de treinamento por época mede a eficiência durante o treinamento, e não durante a execução operacional. D. Número de instâncias de treinamento refere-se à infraestrutura usada, mas não mede eficiência diretamente.
---
Selected Answer: C
Average response time measures how quickly the AI model can generate a result after receiving input. This is a key metric for runtime efficiency, as it directly reflects how fast the model operates during inference or real-time usage. Lower response times indicate higher runtime efficiency.

</details>

---

## Question 17: AIF-C01-ET-Q017
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to improve the accuracy of the responses from a generative AI application. The application uses a foundation model (FM) on Amazon Bedrock.

Which solution meets these requirements MOST cost-effectively?

**Choices:**
- A) Fine-tune the FM.
- B) Retrain the FM.
- C) Train a new FM.
- D) Use prompt engineering.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A solução mais econômica é D. Use engenharia rápida.

A técnica de engenharia rápida permite melhorar a precisão das respostas sem a necessidade de ajustar ou treinar novamente o modelo, o que pode ser bastante custoso em termos de tempo e recursos computacionais. A engenharia rápida envolve a criação de prompts mais eficazes e direcionados, otimizando os resultados gerados pelo modelo com investimentos mínimos.

</details>

---

## Question 18: AIF-C01-ET-Q018
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to identify harmful language in the comments section of social media posts by using an ML model. The company will not use labeled data to train the model.

Which strategy should the company use to identify harmful language?

**Choices:**
- A) Use Amazon Rekognition moderation.
- B) Use Amazon Comprehend toxicity detection.
- C) Use Amazon SageMaker built-in algorithms to train the model.
- D) Use Amazon Polly to monitor comments.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A estratégia correta é B. Use a detecção de toxicidade do Amazon Comprehend.

O Amazon Comprehend é um serviço que utiliza processamento de linguagem natural (NLP) para analisar texto e identificar linguagem prejudicial, como comentários tóxicos. Ele permite detectar automaticamente padrões de toxicidade sem depender de dados rotulados para treinamento, tornando-se uma solução eficaz para esse caso de uso.

</details>

---

## Question 19: AIF-C01-ET-Q019
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A media company wants to analyze viewer behavior and demographics to recommend personalized content. The company wants to deploy a customized ML model in its production environment. The company also wants to observe if the model quality drifts over time.

Which AWS service or feature meets these requirements?

**Choices:**
- A) Amazon Rekognition
- B) Amazon SageMaker Clarify
- C) Amazon Comprehend
- D) Amazon SageMaker Model Monitor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A opção correta é D. Monitor de modelos do Amazon SageMaker.

O Amazon SageMaker Model Monitor é ideal para monitorar continuamente o desempenho de modelos de aprendizado de máquina implantados em produção. Ele ajuda a identificar possíveis desvios de qualidade ou mudanças nos padrões dos dados ao longo do tempo, garantindo que o modelo continue funcionando conforme esperado. Esse recurso é essencial para acompanhar mudanças no comportamento e na demografia dos espectadores enquanto recomenda conteúdo personalizado.

</details>

---

## Question 20: AIF-C01-ET-Q020
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is deploying AI/ML models by using AWS services. The company wants to offer transparency into the models’ decision-making processes and provide explanations for the model outputs.

Which AWS service or feature meets these requirements?

**Choices:**
- A) Amazon SageMaker Model Cards
- B) Amazon Rekognition
- C) Amazon Comprehend
- D) Amazon Lex

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `U`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: U (100%). Contributor Answer: U.

Community Rationale & Discussion:
Selected Answer: U
A resposta correta é A. Cartões de modelo do Amazon SageMaker.

Os cartões de modelo do Amazon SageMaker são projetados para promover a transparência e explicabilidade, documentando informações detalhadas sobre a finalidade do modelo, seu desempenho, limitações e processos de tomada de decisão. Eles ajudam a fornecer explicações claras e padronizadas dos resultados do modelo, sendo uma ferramenta ideal para atender a esses requisitos.

</details>

---

## Question 21: AIF-C01-ET-Q021
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A manufacturing company wants to create product descriptions in multiple languages.

Which AWS service will automate this task?

**Choices:**
- A) Amazon Translate
- B) Amazon Transcribe
- C) Amazon Kendra
- D) Amazon Polly

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `U`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: U (100%). Contributor Answer: U.

Community Rationale & Discussion:
Selected Answer: U
A resposta correta é A. Amazon Tradutor.

O Amazon Translate é um serviço que utiliza aprendizado de máquina para realizar traduções automáticas de alta qualidade em vários idiomas. Ele é ideal para gerar descrições de produtos em diferentes idiomas de forma rápida e eficiente, permitindo que a empresa alcance um público global com facilidade.

</details>

---

## Question 23: AIF-C01-ET-Q023
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building a contact center application and wants to gain insights from customer conversations. The company wants to analyze and extract key information from the audio of the customer calls.
Which solution meets these requirements?

**Choices:**
- A) Build a conversational chatbot by using Amazon Lex.
- B) Transcribe call recordings by using Amazon Transcribe.
- C) Extract information from call recordings by using Amazon SageMaker Model Monitor.
- D) Create classification labels by using Amazon Comprehend.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon Transcribe is a service designed to automatically convert audio (such as customer call recordings) into text. Once transcribed, the text can be further processed to extract key insights, such as customer intent, sentiment, and specific information (e.g., product details or requests). This aligns directly with the goal of analyzing and extracting key information from customer conversations.
---
Selected Answer: B
Transcribe support for speech to text - B
---
Selected Answer: B
B: Transcribe call recordings by using Amazon Transcribe.

Explanation:
Amazon Transcribe is designed for converting speech in audio files (such as customer calls) into text. This text can then be analyzed further to extract key information. It is the first step in gaining insights from audio conversations, making it the appropriate solution for the given requirement.

</details>

---

## Question 24: AIF-C01-ET-Q024
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has petabytes of unlabeled customer data to use for an advertisement campaign. The company wants to classify its customers into tiers to advertise and promote the company's products.
Which methodology should the company use to meet these requirements?

**Choices:**
- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Reinforcement learning from human feedback (RLHF)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Because of the large amounts of unlabeled data and need to identify patterns or groupings within that data, Unsupervised learning is best. Clustering techniques can be used to classify customers into different tiers.
---
Selected Answer: B
Unsupervised learning is ideal for scenarios where the data is unlabeled, and the goal is to find patterns or groupings within the data. In this case, the company has petabytes of unlabeled customer data and wants to classify customers into tiers. Unsupervised learning techniques, such as clustering (e.g., k-means or hierarchical clustering), can be used to group customers based on similar behaviors, preferences, or attributes without needing predefined labels.
---
Selected Answer: B
Unsupervised Learning handled the unlabeled datasets

</details>

---

## Question 25: AIF-C01-ET-Q025
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
An AI practitioner wants to use a foundation model (FM) to design a search application. The search application must handle queries that have text and images.
Which type of FM should the AI practitioner use to power the search application?

**Choices:**
- A) Multi-modal embedding model
- B) Text embedding model
- C) Multi-modal generation model
- D) Image generation model

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `94%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (94%). Contributor Answer: A.

Community Rationale & Discussion:
Multi-modal embedding models can process multiple types of input data, such as text and images. This allows the search application to handle queries that involve both text and images effectively.
---
Selected Answer: A
queries that have text and images >>> Multi-modal embedding
---
Selected Answer: A
Multi-modal generation model (generates content) = Focuses on generation, not search

</details>

---

## Question 26: AIF-C01-ET-Q026
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company uses a foundation model (FM) from Amazon Bedrock for an AI search tool. The company wants to fine-tune the model to be more accurate by using the company's data.
Which strategy will successfully fine-tune the model?

**Choices:**
- A) Provide labeled data with the prompt field and the completion field.
- B) Prepare the training dataset by creating a .txt file that contains multiple lines in .csv format.
- C) Purchase Provisioned Throughput for Amazon Bedrock.
- D) Train the model on journals and textbooks.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Provide labeled data with the prompt field and the completion field: Fine-tuning a foundation model (FM) typically involves providing labeled data in the form of prompts (input) and completions (desired output). The model learns from this data to generate more accurate responses tailored to the company’s specific use case. This approach is aligned with how fine-tuning works, where the model adjusts its parameters based on the relationship between inputs (prompts) and outputs (completions).
---
Selected Answer: A
Fine-tuning a foundation model involves providing labeled training data where each example consists of a prompt (the input to the model) and a completion (the desired output). This structure helps the model learn specific patterns or behaviors tailored to the company’s data and use case.
In Amazon Bedrock, fine-tuning relies on a structured dataset that aligns with the model's learning requirements to improve its accuracy for domain-specific tasks.
---
Why is it not C? Finetuning cannot be done without provisioned throughput mode active.

</details>

---

## Question 27: AIF-C01-ET-Q027
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A law firm wants to build an AI application by using large language models (LLMs). The application will read legal documents and extract key points from the documents.
Which solution meets these requirements?

**Choices:**
- A) Build an automatic named entity recognition system.
- B) Create a recommendation engine.
- C) Develop a summarization chatbot.
- D) Develop a multi-language translation system.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `78%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (78%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Extracting legal language and key points is an example of an extract summary
---
Selected Answer: C
The law firm wants to extract key points from legal documents, which aligns with the goal of summarization. A summarization chatbot powered by large language models (LLMs) can read through legal documents and provide concise, accurate summaries that capture the essential points, making it the most appropriate choice.
---
Selected Answer: C
"C" is correct - The primary requirement is to read legal documents and extract key points.
Summarization is the best approach for condensing lengthy legal text into key points while preserving important details.

"A" is incorrect - NER helps identify names, dates, contract numbers. but does not summarize key points from documents.

</details>

---

## Question 28: AIF-C01-ET-Q028
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to use AI to protect its application from threats. The AI solution needs to check if an IP address is from a suspicious source.
Which solution meets these requirements?

**Choices:**
- A) Build a speech recognition system.
- B) Create a natural language processing (NLP) named entity recognition system.
- C) Develop an anomaly detection system.
- D) Create a fraud forecasting system.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
An anomaly detection system is designed to identify unusual patterns or behaviors within data
---
An anomaly detection system can analyze patterns and behaviors, such as IP address access patterns, to detect any deviations from the norm, which could indicate suspicious or malicious activity. An anomaly detection model can flag unusual access attempts, such as those from suspicious IP addresses, making it well-suited for threat detection.

Fraud forecasting (option D) typically focuses on predicting potential fraud patterns rather than real-time anomaly detection, so it would not directly address the need to check IP addresses for suspicious activity.

Thus, option C is the most suitable choice for identifying suspicious IP addresses in this scenario.
---
Selected Answer: C
Develop an anomaly detection system: Anomaly detection is a technique used to identify unusual patterns in data, such as suspicious IP addresses that deviate from normal behavior. By monitoring and analyzing network traffic, an anomaly detection system can flag IP addresses that exhibit abnormal behavior or characteristics that are indicative of potential threats. This is the most appropriate approach for identifying suspicious sources.

</details>

---

## Question 29: AIF-C01-ET-Q029
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
Which feature of Amazon OpenSearch Service gives companies the ability to build vector database applications?

**Choices:**
- A) Integration with Amazon S3 for object storage
- B) Support for geospatial indexing and queries
- C) Scalable index management and nearest neighbor search capability
- D) Ability to perform real-time analysis on streaming data

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Scalable index management and nearest neighbor search capability: Amazon OpenSearch Service provides built-in support for vector search, which allows for efficient nearest neighbor search (such as k-nearest neighbors or k-NN) in large datasets. This is essential for vector databases, which store high-dimensional data (such as embeddings from machine learning models) and support fast similarity search. The scalable index management ensures that these searches can be performed efficiently even with large datasets.
---
Selected Answer: C
Scalable index management and k-NN algorithms which support to build and handle the recommendation systems, semantic search and anomalies detection.
---
Selected Answer: C
C: Scalable index management and nearest neighbor search capability

Explanation:
The Amazon OpenSearch Service supports building vector database applications by enabling nearest neighbor search capability. This feature allows the service to efficiently perform similarity searches, which is crucial for applications that rely on vector embeddings (e.g., recommendation systems, image or text similarity searches). Combined with scalable index management, this makes OpenSearch an excellent choice for vector database applications.

</details>

---

## Question 30: AIF-C01-ET-Q030
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which option is a use case for generative AI models?

**Choices:**
- A) Improving network security by using intrusion detection systems
- B) Creating photorealistic images from text descriptions for digital marketing
- C) Enhancing database performance by using optimized indexing
- D) Analyzing financial data to forecast stock market trends

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `85%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (85%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Generative AI models are designed to generate new content based on input data.

A common use case is generating photorealistic images from text descriptions, often used in digital marketing, content creation, and design.

Models like DALL·E, Stable Diffusion, or MidJourney can create high-quality images based on user prompts.
---
Selected Answer: B
Creating photorealistic images from text descriptions for digital marketing: Generative AI models, such as generative adversarial networks (GANs) and diffusion models, are capable of generating new content (like images, text, and audio) based on input data. In this case, a generative model can create photorealistic images from text descriptions, which is widely used in digital marketing and content creation.
---
Selected Answer: B
Generative AI is used to generate new content, images, video, and audio from existing content or new inputs from various data sources.

</details>

---

## Question 31: AIF-C01-ET-Q031
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to build a generative AI application by using Amazon Bedrock and needs to choose a foundation model (FM). The company wants to know how much information can fit into one prompt.
Which consideration will inform the company's decision?

**Choices:**
- A) Temperature
- B) Context window
- C) Batch size
- D) Model size

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
A company needs to know the maximum input size for a single prompt when choosing a Foundation Model (FM) in Amazon Bedrock.

A. Temperature: This controls the randomness of the output, not the input prompt length. Temperature affects creativity, not input size.
B. Context window: This defines the maximum length of the input prompt the model can process. It directly limits how much information can be included.
C. Batch size: This is the number of prompts processed at once, affecting throughput, not individual prompt length. It's about processing multiple prompts efficiently.
D. Model size: This relates to the model's overall capacity and complexity, not directly to the input prompt length. Size impacts performance, not input limits.
Therefore, B. Context window is the correct answer.
---
Selected Answer: B
Context window: The context window refers to the amount of text (or tokens) that a model can process at once. This is crucial when working with foundation models (FMs) like those available in Amazon Bedrock, as it defines the maximum input size for the prompt. The context window determines how much of the prompt the model can "remember" and use to generate responses. If the prompt exceeds the context window, the model will only process the portion of the prompt that fits within this limit, potentially missing important details.
---
Selected Answer: B
The context-window is the input prompt for the model generation.

</details>

---

## Question 32: AIF-C01-ET-Q032
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to make a chatbot to help customers. The chatbot will help solve technical problems without human intervention.
The company chose a foundation model (FM) for the chatbot. The chatbot needs to produce responses that adhere to company tone.
Which solution meets these requirements?

**Choices:**
- A) Set a low limit on the number of tokens the FM can produce.
- B) Use batch inferencing to process detailed responses.
- C) Experiment and refine the prompt until the FM produces the desired responses.
- D) Define a higher number for the temperature parameter.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Experiment and refine the prompt until the FM produces the desired responses: The behavior and tone of a chatbot powered by a foundation model (FM) are heavily influenced by how the prompt is crafted. By iterating on the prompt and fine-tuning it, you can guide the model to respond in a way that aligns with the company’s tone, whether it's formal, friendly, technical, or casual. This is a common practice in prompt engineering to get the model to generate output that matches specific requirements.
---
Selected Answer: C
Continued pre-taining of the datasets to produce responses to the company's tone.
---
Selected Answer: C
C. Experiment and refine the prompt until the FM produces the desired responses.

Refining the prompt is key to aligning the chatbot's responses with the company's tone and guidelines. Foundation models respond significantly to how prompts are phrased, making prompt engineering a powerful tool for achieving desired behavior.

</details>

---

## Question 33: AIF-C01-ET-Q033
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use a large language model (LLM) on Amazon Bedrock for sentiment analysis. The company wants to classify the sentiment of text passages as positive or negative.

Which prompt engineering strategy meets these requirements?

**Choices:**
- A) Provide examples of text passages with corresponding positive or negative labels in the prompt followed by the new text passage to be classified.
- B) Provide a detailed explanation of sentiment analysis and how LLMs work in the prompt.
- C) Provide the new text passage to be classified without any additional context or examples.
- D) Provide the new text passage with a few examples of unrelated tasks, such as text summarization or question answering.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
This approach is known as few-shot prompting, where you include a few labeled examples to guide the model on how to classify sentiment.
---
Selected Answer: A
Provide examples of text passages with corresponding positive or negative labels in the prompt followed by the new text passage to be classified: This approach uses few-shot learning, where you give the model clear examples of text passages labeled with sentiment (positive or negative). By providing these examples in the prompt, the model is better able to understand the task and generalize it to classify the new text passage correctly. This is a common and effective strategy for tasks like sentiment analysis.
---
Selected Answer: A
Set the proper label with a few examples to the prompts

</details>

---

## Question 34: AIF-C01-ET-Q034
**Domain 3:** Applications of Foundation Models  

**Question:**  
A security company is using Amazon Bedrock to run foundation models (FMs). The company wants to ensure that only authorized users invoke the models. The company needs to identify any unauthorized access attempts to set appropriate AWS Identity and Access Management (IAM) policies and roles for future iterations of the FMs.
Which AWS service should the company use to identify unauthorized users that are trying to access Amazon Bedrock?

**Choices:**
- A) AWS Audit Manager
- B) AWS CloudTrail
- C) Amazon Fraud Detector
- D) AWS Trusted Advisor

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS CloudTrail: CloudTrail records all API requests made to AWS services, including Amazon Bedrock. By using CloudTrail, the security company can track and log all access attempts, including any unauthorized attempts, to access Amazon Bedrock. This helps the company identify and respond to unauthorized access, and also provides detailed logs for setting up appropriate IAM policies and roles.
---
Selected Answer: B
AWS CloudTrail is a service that records all API calls and user activity across AWS services, including Amazon Bedrock.
---
Selected Answer: B
Use AWS CloudTrail to track the API Calls to AWS resources.

</details>

---

## Question 35: AIF-C01-ET-Q035
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has developed an ML model for image classification. The company wants to deploy the model to production so that a web application can use the model.
The company needs to implement a solution to host the model and serve predictions without managing any of the underlying infrastructure.
Which solution will meet these requirements?

**Choices:**
- A) Use Amazon SageMaker Serverless Inference to deploy the model.
- B) Use Amazon CloudFront to deploy the model.
- C) Use Amazon API Gateway to host the model and serve predictions.
- D) Use AWS Batch to host the model and serve predictions.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Use Amazon SageMaker Serverless Inference to deploy the model: Amazon SageMaker Serverless Inference allows you to deploy machine learning models in a fully managed, serverless environment. You don't need to manage the underlying infrastructure (such as EC2 instances) to handle predictions. This is ideal for scenarios like yours, where the model needs to be deployed and used by a web application, and scalability and infrastructure management should be abstracted away.
---
Selected Answer: A
Amazon SageMaker helps to host the model, and serve predictions without managing infrastructure provisioning and configurations.
---
Selected Answer: A
A. Use Amazon SageMaker Serverless Inference to deploy the model.

Amazon SageMaker Serverless Inference is specifically designed for hosting ML models and serving predictions without requiring the management of underlying infrastructure. It automatically provisions compute resources as needed and is ideal for use cases like the one described.

</details>

---

## Question 36: AIF-C01-ET-Q036
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
An AI company periodically evaluates its systems and processes with the help of independent software vendors (ISVs). The company needs to receive email message notifications when an ISV's compliance reports become available.
Which AWS service can the company use to meet this requirement?

**Choices:**
- A) AWS Audit Manager
- B) AWS Artifact
- C) AWS Trusted Advisor
- D) AWS Data Exchange

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (67%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
AWS Artifacts has email notifications that notify you when a report is available.
https://aws.amazon.com/about-aws/whats-new/2023/08/aws-artifact-email-notifications/
---
Selected Answer: B
Portal that provides customers with on-demand access to AWS
compliance documentation and AWS agreements
• Artifact Reports - Allows you to download AWS security and compliance
documents from third-party auditors, like AWS ISO certifications, Payment
Card Industry (PCI), and System and Organization Control (SOC) reports
• Artifact Agreements - Allows you to review, accept, and track the status of
AWS agreements such as the Business Associate Addendum (BAA) or the
Health Insurance Portability and Accountability Act (HIPAA) for an individual
account or in your organization
---
Selected Answer: D
However, AWS Artifact is not designed for receiving notifications about third-party compliance reports from ISVs (Independent Software Vendors). Instead, it focuses on AWS's own compliance documentation, which makes it different from services like AWS Data Exchange that facilitate access to third-party data products and notifications about new data availability.

</details>

---

## Question 37: AIF-C01-ET-Q037
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use a large language model (LLM) to develop a conversational agent. The company needs to prevent the LLM from being manipulated with common prompt engineering techniques to perform undesirable actions or expose sensitive information.
Which action will reduce these risks?

**Choices:**
- A) Create a prompt template that teaches the LLM to detect attack patterns.
- B) Increase the temperature parameter on invocation requests to the LLM.
- C) Avoid using LLMs that are not listed in Amazon SageMaker.
- D) Decrease the number of input tokens on invocations of the LLM.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (88%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Explicação: A criação de cuidadosamente projetados,ados com técnicas de segurança como validação de entrada,agem de conteúdo e detecção padrões de engenharia de prompt (prompt injection), é prática fundamental para reduzir os riscos de manipulação de LLM. Essa abordagem ensina modelo a reconhecer e resistir tentativas maliciosas, como comandos disfarçados exploração de brechas prompt.
---
Selected Answer: A
Create a prompt template that teaches the LLM to detect attack patterns: By creating a prompt template that is specifically designed to identify and mitigate common attack patterns (e.g., prompt injections or malicious requests), you can make the LLM more robust to manipulation. This can help the LLM recognize when it's being manipulated into performing undesirable actions or exposing sensitive data, and take preventive measures accordingly.
---
Selected Answer: A
Ask model to use Prompt template to avoid the various types of prompt injection attacks.

</details>

---

## Question 38: AIF-C01-ET-Q038
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to classify human genes into 20 categories based on gene characteristics. The company needs an ML algorithm to document how the inner mechanism of the model affects the output.
Which ML algorithm meets these requirements?

**Choices:**
- A) Decision trees
- B) Linear regression
- C) Logistic regression
- D) Neural networks

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Decision trees provide a transparent and interpretable model. They allow you to understand how decisions are made by following the path of splits at each node, which directly shows the influence of input features (gene characteristics) on the final output (gene category). This helps document and explain how the model arrives at its classifications, satisfying the requirement for transparency regarding the inner mechanism of the model.
---
Selected Answer: A
A is correct. I firstly thought Logistic regression should be right, but it's for binary classification, and not suitable for the case in this question because there are 20 categories.
---
Selected Answer: A
i believe A is the right one but why logistic regression is not correct

</details>

---

## Question 39: AIF-C01-ET-Q039
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
A company is using the Generative AI Security Scoping Matrix to assess security responsibilities for its solutions. The company has identified four different solution scopes based on the matrix.
Which solution scope gives the company the MOST ownership of security responsibilities?

**Choices:**
- A) Using a third-party enterprise application that has embedded generative AI features.
- B) Building an application by using an existing third-party generative AI foundation model (FM).
- C) Refining an existing third-party generative AI foundation model (FM) by fine-tuning the model by using data specific to the business.
- D) Building and training a generative AI model from scratch by using specific data that a customer owns.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Explicação:
De acordo com a Generative AI Security Scoping Matrix, quanto maior o controle e customização de uma solução, maior é a responsabilidade da empresa pela segurança.

Opção D representa o maior nível de propriedade: ao construir e treinar um modelo do zero, a empresa assume controle total sobre o modelo, os dados, o treinamento, a implantação e a segurança em cada etapa.

As demais opções têm menos responsabilidade direta porque envolvem componentes terceirizados:
---
Selected Answer: D
Building and training a generative AI model from scratch by using specific data that a customer owns: When a company builds and trains a model from scratch using its own or customer-specific data, the company has full control over the entire development process, including data collection, model training, infrastructure management, and deployment. As a result, the company assumes the most responsibility for security in all areas, from data protection to model security and the underlying infrastructure.
---
Selected Answer: D
D: Building and training a generative AI model from scratch by using specific data that a customer owns.

Explanation:
When a company builds and trains a generative AI model from scratch, it assumes the most ownership of security responsibilities, including:

Data security and compliance during training.
Model development and training processes.
Infrastructure and deployment security.
Protecting the model from adversarial attacks.
Ensuring ethical use of the model and safeguarding against bias and misuse.
This approach provides complete control over the entire lifecycle of the AI solution but also places the greatest burden of responsibility on the company.

</details>

---

## Question 40: AIF-C01-ET-Q040
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
An AI practitioner has a database of animal photos. The AI practitioner wants to automatically identify and categorize the animals in the photos without manual human effort.
Which strategy meets these requirements?

**Choices:**
- A) Object detection
- B) Anomaly detection
- C) Named entity recognition
- D) Inpainting

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Object detection: Object detection is a computer vision technique used to automatically identify and locate objects (in this case, animals) within an image. It also categorizes the objects by labeling them. This is exactly what the AI practitioner needs to classify and categorize the animals in the photos without manual effort.
---
Selected Answer: A
Object detection helps to identify and category the object of the image.
---
Selected Answer: A
A: Object detection

Explanation:
Object detection is a computer vision technique that identifies and categorizes objects within an image. In this scenario, it can automatically detect animals in the photos and assign them to categories (e.g., "dog," "cat," "bird"). This approach aligns perfectly with the requirement to identify and categorize animals without manual intervention.

</details>

---

## Question 41: AIF-C01-ET-Q041
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company wants to create an application by using Amazon Bedrock. The company has a limited budget and prefers flexibility without long-term commitment.
Which Amazon Bedrock pricing model meets these requirements?

**Choices:**
- A) On-Demand
- B) Model customization
- C) Provisioned Throughput
- D) Spot Instance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (86%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Explicação:
O modelo de preço sob demanda do Amazon Bedrock permite que a empresa pague apenas pelo que usar, sem necessidade de compromissos de longo prazo ou reservas antecipadas.
Isso oferece: Flexibilidade: Ideal para projetos em fase inicial ou com uso variável.
Custo controlado: Perfeito para orçamentos limitados, pois evita gastos fixos ou comprometimento com capacidade provisionada.
Sem contratos: A empresa pode interromper ou ajustar o uso a qualquer momento.
---
Selected Answer: A
On-Demand: The On-Demand pricing model allows the company to pay for the compute resources or services they use without requiring a long-term commitment. This model is ideal for companies that need flexibility and have variable usage patterns, as they can scale up or down based on their needs while only paying for what they use. This model provides the most flexibility and is cost-effective for companies with limited budgets.
---
Selected Answer: A
On-Demand pricing plan helps to run the application in the temporary mode.

</details>

---

## Question 42: AIF-C01-ET-Q042
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which AWS service or feature can help an AI development team quickly deploy and consume a foundation model (FM) within the team's VPC?

**Choices:**
- A) Amazon Personalize
- B) Amazon SageMaker JumpStart
- C) PartyRock, an Amazon Bedrock Playground
- D) Amazon SageMaker endpoints

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `61%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (61%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Amazon SageMaker JumpStart

Explanation:
 • Amazon SageMaker JumpStart enables AI teams to quickly deploy and consume foundation models (FMs) within their own VPC.
 • It provides pre-trained foundation models from AWS and third-party providers, making it easy to fine-tune and integrate them into applications.
 • VPC Integration: Ensures that models are deployed securely within the team’s AWS environment.
---
Selected Answer: D
Amazon SageMaker endpoints are a managed service feature that allows you to deploy models (including foundation models) for real-time inference. By hosting your model on an endpoint, you can make it accessible within your Virtual Private Cloud (VPC) and integrate it into your applications quickly. This approach provides a secure, scalable, and managed way to deploy and consume models across different teams.
B. Amazon SageMaker JumpStart: Provides quick access to pre-trained models and sample solutions, but you ultimately deploy those models via SageMaker endpoints to consume them in your VPC.
---
Selected Answer: D
Amazon SageMaker endpoints allow AI development teams to deploy and consume foundation models (FMs) within their Amazon VPC for secure, low-latency inference.

</details>

---

## Question 43: AIF-C01-ET-Q043
**Domain 3:** Applications of Foundation Models  

**Question:**  
How can companies use large language models (LLMs) securely on Amazon Bedrock?

**Choices:**
- A) Design clear and specific prompts. Configure AWS Identity and Access Management (IAM) roles and policies by using least privilege access.
- B) Enable AWS Audit Manager for automatic model evaluation jobs.
- C) Enable Amazon Bedrock automatic model evaluation jobs.
- D) Use Amazon CloudWatch Logs to make models explainable and to monitor for bias.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Design clear and specific prompts. Configure AWS Identity and Access Management (IAM) roles and policies by using least privilege access.:
Designing clear and specific prompts helps prevent unintended or manipulative outputs from the large language models (LLMs), ensuring secure and controlled use.
Configuring IAM roles and policies using least privilege access ensures that only authorized users and services can access and invoke the models, limiting potential security risks.
---
Selected Answer: A
Using IAM with least privilege will secure the LLM on the Amazon Bedrock.
---
Selected Answer: A
A. Design clear and specific prompts. Configure AWS Identity and Access Management (IAM) roles and policies by using least privilege access.

This option addresses two key aspects of secure LLM usage on Amazon Bedrock:

Prompt Engineering: Clear and specific prompts reduce the risk of unintended or harmful outputs. Well-defined prompts help guide the model's responses and minimize the potential for bias or misinformation.
IAM Access Control: Implementing strong access controls is crucial to protect sensitive data and prevent unauthorized access to the LLM. By using IAM roles and policies with least privilege access, you can limit permissions to only the necessary actions, reducing the risk of security breaches.

</details>

---

## Question 44: AIF-C01-ET-Q044
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has terabytes of data in a database that the company can use for business analysis. The company wants to build an AI-based application that can build a SQL query from input text that employees provide. The employees have minimal experience with technology.
Which solution meets these requirements?

**Choices:**
- A) Generative pre-trained transformers (GPT)
- B) Residual neural network
- C) Support vector machine
- D) WaveNet

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Generative pre-trained transformers (GPT): GPT models are well-suited for natural language processing tasks, such as generating SQL queries from input text. These models are designed to understand and generate human-like text, which makes them ideal for translating text input into structured outputs like SQL queries. With minimal training, GPT models can be fine-tuned for specific tasks, such as query generation, and can help employees with minimal technical experience by understanding natural language inputs and converting them into SQL queries.
---
Selected Answer: A
GPT helps to produces the NL based responsed based on the input text.
---
Selected Answer: A
The best solution for building an AI-based application that translates natural language (employee input text) into SQL queries is A. Generative pre-trained transformers (GPT).

Here's why:

GPT's strength in natural language processing: GPT models are specifically designed for understanding and generating human language. They excel at tasks like text translation, question answering, and, crucially, code generation from natural language descriptions. This makes them ideal for converting employee input into SQL queries.

</details>

---

## Question 45: AIF-C01-ET-Q045
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company built a deep learning model for object detection and deployed the model to production.
Which AI process occurs when the model analyzes a new image to identify objects?

**Choices:**
- A) Training
- B) Inference
- C) Model deployment
- D) Bias correction

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Explicação:
A inferência é o processo que ocorre após o modelo estar treinado e implantado, quando ele é usado para analisar novos dados (neste caso, uma nova imagem) e gerar previsões ou classificações — como identificar objetos na imagem.

As outras opções se referem a fases diferentes do ciclo de vida da IA:

A. Formação (Treinamento): é o processo de ensinar o modelo usando dados rotulados.

C. Implantação de modelo: é quando o modelo é colocado em produção, mas ainda não está processando dados.

D. Correção de viés: refere-se a técnicas usadas para identificar e mitigar preconceitos nos dados ou no modelo.
---
Selected Answer: B
Inference: Inference is the process in which a trained model analyzes new data (in this case, a new image) to make predictions or classifications. After the model is trained, it is deployed to production, and inference occurs when the model processes new, unseen data to identify objects or make decisions.
---
Selected Answer: B
During the inference phase, model analyses a new image to identify objects.

</details>

---

## Question 46: AIF-C01-ET-Q046
**Domain 4:** Guidelines for Responsible AI  

**Question:**  
An AI practitioner is building a model to generate images of humans in various professions. The AI practitioner discovered that the input data is biased and that specific attributes affect the image generation and create bias in the model.
Which technique will solve the problem?

**Choices:**
- A) Data augmentation for imbalanced classes
- B) Model monitoring for class distribution
- C) Retrieval Augmented Generation (RAG)
- D) Watermark detection for images

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Data augmentation for imbalanced classes: If the input data is biased and leads to undesirable attributes in the generated images (such as certain professions being overrepresented by specific attributes like gender or race), data augmentation can help balance the dataset. Data augmentation involves creating new training samples by applying transformations like cropping, rotating, or altering color schemes to existing data. This can help create a more diverse, balanced dataset and reduce bias by ensuring the model sees a more representative set of examples.
---
Selected Answer: A
Data augmentation for imbalanced classes

Data augmentation techniques can help mitigate bias in image generation models by artificially increasing the diversity of the training data. By applying transformations like rotations, flips, and color jittering to existing images, you can create new, synthetic images that are similar to the original ones. This can help balance the dataset and reduce the impact of biases present in the original data.
---
Selected Answer: A
A. Data augmentation for imbalanced classes is the most effective technique to mitigate bias in the input data by ensuring a more balanced representation of classes and attributes in the training set, leading to fairer and more accurate image generation.

</details>

---

## Question 47: AIF-C01-ET-Q047
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company is implementing the Amazon Titan foundation model (FM) by using Amazon Bedrock. The company needs to supplement the model by using relevant data from the company's private data sources.
Which solution will meet this requirement?

**Choices:**
- A) Use a different FM.
- B) Choose a lower temperature value.
- C) Create an Amazon Bedrock knowledge base.
- D) Enable model invocation logging.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Explicação:
O Amazon Bedrock permite que você complemente um modelo de fundação (Foundation Model – FM), como o Amazon Titan, com dados proprietários da sua empresa sem precisar treinar ou ajustar o modelo.

Isso é feito por meio da criação de uma base de conhecimento, que permite que o modelo:

Busque e consulte dados relevantes em fontes privadas (como documentos, bancos de dados ou repositórios internos).

Ofereça respostas mais precisas e contextualizadas com base nas informações da empresa.Use a técnica conhecida como RAG (Retrieval-Augmented Generation).
---
Selected Answer: C
Create an Amazon Bedrock knowledge base: This solution allows the company to supplement the Amazon Titan foundation model with their own relevant, private data sources. The knowledge base enables the foundation model to access specific, proprietary data during inference, enhancing the model's responses and making it more tailored to the company’s needs. This is especially useful when the model needs to be supplemented with data that is not part of the model’s initial training data.
---
Selected Answer: C
Amazon Bedrock KB support to interact with the company's private data sources.

</details>

---

## Question 48: AIF-C01-ET-Q048
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A medical company is customizing a foundation model (FM) for diagnostic purposes. The company needs the model to be transparent and explainable to meet regulatory requirements.
Which solution will meet these requirements?

**Choices:**
- A) Configure the security and compliance by using Amazon Inspector.
- B) Generate simple metrics, reports, and examples by using Amazon SageMaker Clarify.
- C) Encrypt and secure training data by using Amazon Macie.
- D) Gather more data. Use Amazon Rekognition to add custom labels to the data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon SageMaker Clarify is specifically designed to help make machine learning models more transparent and explainable by generating metrics and reports on model bias, data bias, and feature importance.
---
Selected Answer: B
Generate simple metrics, reports, and examples by using Amazon SageMaker Clarify: Amazon SageMaker Clarify helps provide transparency and explainability to machine learning models by generating metrics, reports, and visual explanations of the model’s predictions. This is crucial for meeting regulatory requirements in domains like healthcare, where understanding how a model arrives at its decisions is essential for validation and trust. SageMaker Clarify also helps identify potential biases in the model, which is important for ensuring fair and responsible use of AI.
---
Selected Answer: B
B. Generate simple metrics, reports, and examples by using Amazon SageMaker Clarify.

Amazon SageMaker Clarify helps in identifying bias and explaining predictions made by machine learning models, which aligns well with the need for transparency and explainability to meet regulatory requirements.

</details>

---

## Question 49: AIF-C01-ET-Q049
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has built an image classification model to predict plant diseases from photos of plant leaves. The company wants to evaluate how many images the model classified correctly.
Which evaluation metric should the company use to measure the model's performance?

**Choices:**
- A) R-squared score
- B) Accuracy
- C) Root mean squared error (RMSE)
- D) Learning rate

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Accuracy is the most straightforward metric, measuring the proportion of correctly predicted instances out of the total instances. It is suitable when the classes are balanced (but can be misleading for imbalanced datasets).
---
Selected Answer: B
A métrica de avaliação mais apropriada para medir quantas imagens o modelo classificou corretamente em um modelo de classificação é:

B. Exatidão

Explicações das opções:
A. Pontuação R-quadrado: usada em modelos de regressão, não em classificação.

B. Exatidão (Accuracy): mede a proporção de previsões corretas em relação ao total de previsões — ideal para classificação.

C. RMSE (Raiz do Erro Quadrático Médio): também usada em regressão, não em problemas de classificação.

D. Taxa de aprendizado: não é uma métrica de avaliação, mas um hiperparâmetro usado durante o treinamento do modelo.

 Resposta correta: B. Exatidão
---
Selected Answer: B
A exatidão (accuracy) é uma métrica apropriada para avaliar o desempenho de um modelo de classificação de imagens. Ela calcula a proporção de imagens que o modelo classificou corretamente em relação ao total de imagens avaliadas.

</details>

---

## Question 50: AIF-C01-ET-Q050
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company wants to deploy a conversational chatbot to answer customer questions. The chatbot is based on a fine-tuned Amazon SageMaker JumpStart model. The application must comply with multiple regulatory frameworks.
Which capabilities can the company show compliance for? (Choose two.)

**Choices:**
- A) Auto scaling inference endpoints
- B) Threat detection
- C) Data protection
- D) Cost optimization
- E) Loosely coupled microservices

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BC`  
**Community Consensus:** `92%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BC (92%). Contributor Answer: BC.

Community Rationale & Discussion:
Selected Answer: BC
B. Threat detection: Regulatory frameworks often require companies to have the ability to detect and respond to threats, ensuring that sensitive data is protected from unauthorized access or misuse. Amazon services like Amazon GuardDuty can help with threat detection, which is an important part of compliance.
C. Data protection: Compliance with regulatory frameworks typically involves ensuring that data is securely stored and processed. Amazon SageMaker provides built-in data protection features such as encryption, and it is essential to comply with privacy regulations like GDPR, HIPAA, etc. This ensures that sensitive data is properly handled.
---
Selected Answer: BC
Threat (Amazon GuardDuty) and Data Protection (Amazon Macie, KMS, Encrypt the data at REST and in-Transit.
---
Selected Answer: BC
Why not the other options?
A: Auto scaling inference endpoints:
Auto-scaling improves performance and cost-efficiency but is not directly related to regulatory compliance.
D: Cost optimization:
Cost optimization is beneficial for managing expenses but is not a compliance requirement.
E: Loosely coupled microservices:
While a good architectural principle, it does not directly address compliance with regulatory frameworks.

</details>

---

## Question 51: AIF-C01-ET-Q051
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is training a foundation model (FM). The company wants to increase the accuracy of the model up to a specific acceptance level.
Which solution will meet these requirements?

**Choices:**
- A) Decrease the batch size.
- B) Increase the epochs.
- C) Decrease the epochs.
- D) Increase the temperature parameter.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Explicação: Durante o treinamento de um modelo de fundação (FM), aumentar o número de épocas significa que o modelo passará mais vezes pelos dados de treinamento, 
o que pode ajudar a melhorar a precisão, especialmente se ele ainda estiver aprendendo padrões importantes. Mais épocas,mais aprendizado, até certo ponto. Porém, é importante monitorar para evitar overfitting . A. Diminua o tamanho do lote: Isso pode afetar a estabilidade do treinamento, mas não garante aumento de precisão. C. Diminua as épocas: Isso reduz o tempo de aprendizado, o que pode diminuir a precisão. D. Aumente o parâmetro de temperatura: Isso afeta o comportamento do modelo na inferência, tornando as respostas mais criativas/aleatórias, mas não melhora a precisão no treinamento.
---
Selected Answer: B
B. Increase the epochs: In deep learning, training a model for more epochs means that the model will go through the dataset more times, which generally leads to better learning and improved accuracy. Increasing the number of epochs allows the model to learn patterns more effectively, helping it reach the desired accuracy level. However, there’s a trade-off, as increasing epochs too much could lead to overfitting.
---
Selected Answer: B
B: Increase the epochs.

Explanation:
Increasing the epochs allows the model to go through the entire training dataset multiple times, improving its learning and optimizing its weights. This can help the model achieve a higher accuracy level, provided it does not lead to overfitting. For a foundation model (FM), increasing epochs is a common approach to refining accuracy to meet specific acceptance levels.

</details>

---

## Question 52: AIF-C01-ET-Q052
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is building a large language model (LLM) question answering chatbot. The company wants to decrease the number of actions call center employees need to take to respond to customer questions.
Which business objective should the company use to evaluate the effect of the LLM chatbot?

**Choices:**
- A) Website engagement rate
- B) Average call duration
- C) Corporate social responsibility
- D) Regulatory compliance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Explicação:
Se o objetivo é reduzir o número de ações dos funcionários do call center, o impacto mais direto e mensurável será na duração média da chamada. Um chatbot LLM bem implementado pode:

Ajudar os atendentes com respostas rápidas e precisas.

Reduzir o tempo necessário para buscar informações.

Aumentar a eficiência no atendimento ao cliente.

Tudo isso contribui para chamadas mais curtas e eficazes, o que é um indicativo claro de ganho de produtividade.
---
Selected Answer: B
B. Average call duration: This metric is a direct measure of how much time call center employees spend responding to customer questions. By implementing an LLM chatbot, the company aims to reduce the number of actions that call center employees need to take, which should lead to a decrease in average call duration. If the chatbot can effectively answer customer questions, employees can resolve issues more quickly or be less involved in the conversation, leading to shorter calls.
---
Selected Answer: B
B: Average call duration

Explanation:
Average call duration is a key metric for evaluating the efficiency of a question-answering chatbot in a call center environment. By reducing the number of actions employees need to take, the chatbot can help streamline customer interactions, resulting in shorter call durations. Monitoring this metric helps the company assess whether the chatbot is achieving its goal of improving call center efficiency.

</details>

---

## Question 53: AIF-C01-ET-Q053
**Domain 4:** Guidelines for Responsible AI  

**Question:**  
Which functionality does Amazon SageMaker Clarify provide?

**Choices:**
- A) Integrates a Retrieval Augmented Generation (RAG) workflow
- B) Monitors the quality of ML models in production
- C) Documents critical details about ML models
- D) Identifies potential bias during data preparation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Amazon SageMaker Clarify provides functionality to detect and identify potential bias in data both before and after training, helping teams uncover imbalances in datasets that might lead to biased model predictions. This is essential for ensuring fairness and compliance, especially in sensitive applications.

Why Not the Other Options?
A. Integrates a Retrieval Augmented Generation (RAG) workflow: RAG workflows are used for combining retrieved documents with model outputs, typically in language models, but this is not a function of SageMaker Clarify.
B. Monitors the quality of ML models in production: Monitoring model quality in production is handled by SageMaker Model Monitor, not SageMaker Clarify.
C. Documents critical details about ML models: This functionality is part of Amazon SageMaker Model Cards, which documents model details for transparency and compliance.
---
Selected Answer: D
Explicação:
O Amazon SageMaker Clarify é uma ferramenta que auxilia na detecção de vieses e na explicabilidade de modelos de machine learning (ML). Ele oferece funcionalidades como:

Detecção de vieses: Ajuda a identificar possíveis vieses nos dados durante a preparação e também nos modelos após o treinamento. 

Explicabilidade de modelos: Fornece insights sobre como os modelos de ML fazem previsões, aumentando a transparência
---
Selected Answer: D
Identifies potential bias during data preparation: This is the core functionality of Amazon SageMaker Clarify. It helps data scientists and AI practitioners detect bias in training data, providing insights into how the data might introduce bi

</details>

---

## Question 54: AIF-C01-ET-Q054
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is developing a new model to predict the prices of specific items. The model performed well on the training dataset. When the company deployed the model to production, the model's performance decreased significantly.
What should the company do to mitigate this problem?

**Choices:**
- A) Reduce the volume of data that is used in training.
- B) Add hyperparameters to the model.
- C) Increase the volume of data that is used in training.
- D) Increase the model training time.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (86%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Increase the volume of data that is used in training: If the model performs well on the training dataset but poorly on production data, it could be due to overfitting or the model not generalizing well. Increasing the volume of data can help the model generalize better to unseen data and improve its robustness, thus improving performance in production.
---
Selected Answer: B
The company should use hyperparameters for model tuning, which involves adjusting parameters such as regularization, learning rates, and dropout rates to enhance the model's ability to generalize well to new data

Explanation: 
Hyperparameter tuning is the most effective solution in this scenario because it allows the company to adjust the settings that control the learning process of the model. By fine-tuning hyperparameters, such as increasing regularization or early stopping or adjusting dropout rates, the model can avoid overfitting to the training data and better generalize to new, unseen data in production. This approach helps improve the model's performance across various data distributions.
---
Selected Answer: C
C: Increase the volume of data that is used in training.

Explanation:
The issue described is likely caused by overfitting, where the model performs well on the training dataset but fails to generalize to unseen data. Increasing the volume of training data can help mitigate overfitting by providing the model with more diverse examples, improving its ability to generalize to new data in production.

</details>

---

## Question 55: AIF-C01-ET-Q055
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
An ecommerce company wants to build a solution to determine customer sentiments based on written customer reviews of products.
Which AWS services meet these requirements? (Choose two.)

**Choices:**
- A) Amazon Lex
- B) Amazon Comprehend
- C) Amazon Polly
- D) Amazon Bedrock
- E) Amazon Rekognition

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `BD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: BD (100%). Contributor Answer: BD.

Community Rationale & Discussion:
Selected Answer: BD
B. Amazon Comprehend: Amazon Comprehend is a fully managed natural language processing (NLP) service that can analyze text and extract insights, including sentiment analysis. This makes it ideal for determining customer sentiment based on written reviews.
D. Amazon Bedrock: Amazon Bedrock provides access to foundation models (FMs) for various tasks, including sentiment analysis, through generative AI. It can be used to analyze customer reviews and understand sentiment.
---
Selected Answer: BD
Amazon Comprehend (insight of the customer reviews) and Amazon Bedrock helps for sentiment analysis.
---
Selected Answer: BD
B. Amazon Comprehend:

 Amazon Comprehend is a fully managed natural language processing (NLP) service that can analyze text and determine sentiment, entities, key phrases, and language. For customer sentiment analysis based on written reviews, Amazon Comprehend provides built-in sentiment analysis that can classify text as positive, negative, or neutral.

D. Amazon Bedrock:

 Amazon Bedrock is a service that provides access to various foundation models (FMs), which can be used to build and deploy AI-driven applications. For advanced natural language processing tasks like sentiment analysis, foundation models can be fine-tuned and applied to specific use cases, such as understanding customer sentiment in reviews. This is a more customizable and advanced option compared to pre-built solutions like Amazon Comprehend.

</details>

---

## Question 56: AIF-C01-ET-Q056
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
An AI practitioner wants to predict the classification of flowers based on petal length, petal width, sepal length, and sepal width.

Which algorithm meets these requirements?

**Choices:**
- A) K-nearest neighbors (k-NN)
- B) K-mean
- C) Autoregressive Integrated Moving Average (ARIMA)
- D) Linear regression

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
k-NN: This is a classification algorithm that predicts the class of a new data point by comparing it to the closest data points in the training set. In this case, the new data point would be a new flower with measured petal and sepal dimensions, and the algorithm would find the flowers in the training set that are most similar to it based on these features.
---
Selected Answer: A
The practitioner wants to classify flowers based on measurements. This indicates a classification problem.

A. K-nearest neighbors (k-NN): This is a classification algorithm that classifies data points based on the majority class among their k-nearest neighbors. It's suitable for this scenario.

B. K-means: This is a clustering algorithm used for unsupervised learning. It groups data points into clusters based on similarity, but it doesn't perform classification with predefined labels.

C. Autoregressive Integrated Moving Average (ARIMA): This is a time series forecasting model used for predicting future values based on past data trends. It's not suitable for classification based on static measurements like flower dimensions.

D. Linear regression: This is a regression algorithm used for predicting continuous values. It's not suitable for classification into discrete categories like flower types.

Therefore, A. K-nearest neighbors (k-NN) is the appropriate algorithm for this classification task
---
Selected Answer: A
The correct answer is A. K-nearest neighbors (k-NN) is a classification algorithm suitable for predicting the classification of flowers based on the provided features.

</details>

---

## Question 57: AIF-C01-ET-Q057
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is using custom models in Amazon Bedrock for a generative AI application. The company wants to use a company managed encryption key to encrypt the model artifacts that the model customization jobs create.

Which AWS service meets these requirements?

**Choices:**
- A) AWS Key Management Service (AWS KMS)
- B) Amazon Inspector
- C) Amazon Macie
- D) AWS Secrets Manager

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Bedrock supports encryption of model artifacts using AWS Key Management Service (AWS KMS). AWS KMS allows you to use a company-managed encryption key (customer-managed key or CMK) to encrypt the model artifacts created during model customization jobs.
---
Selected Answer: A
The company needs to use a company-managed encryption key to encrypt model artifacts. This points directly to key management.

A. AWS Key Management Service (AWS KMS): This is the correct answer. AWS KMS allows you to create and manage encryption keys, including customer-managed keys (CMKs), which give you control over the key lifecycle and usage.

B. Amazon Inspector: Inspector is a vulnerability management service that scans for security vulnerabilities in your AWS resources.

C. Amazon Macie: Macie is a data security and privacy service that uses machine learning to discover and protect sensitive data in AWS.

D. AWS Secrets Manager: Secrets Manager helps you manage secrets such as passwords, API keys, and database credentials. While it can store encrypted secrets, it's not the primary service for managing encryption keys used to protect model artifacts at rest.
---
The company needs to use a company-managed encryption key to encrypt model artifacts. This points directly to key management.

A. AWS Key Management Service (AWS KMS): This is the correct answer. AWS KMS allows you to create and manage encryption keys, including customer-managed keys (CMKs), which give you control over the key lifecycle and usage.

B. Amazon Inspector: Inspector is a vulnerability management service that scans for security vulnerabilities in your AWS resources.

C. Amazon Macie: Macie is a data security and privacy service that uses machine learning to discover and protect sensitive data in AWS.

D. AWS Secrets Manager: Secrets Manager helps you manage secrets such as passwords, API keys, and database credentials. While it can store encrypted secrets, it's not the primary service for managing encryption keys used to protect model artifacts at rest.

</details>

---

## Question 58: AIF-C01-ET-Q058
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use large language models (LLMs) to produce code from natural language code comments.

Which LLM feature meets these requirements?

**Choices:**
- A) Text summarization
- B) Text generation
- C) Text completion
- D) Text classification

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: C
The task described — producing code from natural language comments — involves continuing or completing a prompt (in this case, natural language) with appropriate code. This is best handled by the text completion capability of large language models (LLMs).

You provide a prompt such as:

# This function calculates the factorial of a number\n def factorial(n):

The model completes the rest with actual code.

Text completion is specifically designed for this kind of task, where the model infers the most likely continuation of a given input, which can be natural language or code.
---
Selected Answer: B
Large language models (LLMs) that convert natural language comments into code need the ability to generate new content based on the provided input. This aligns with the text generation feature, where the model produces human-like text, including writing code from natural language descriptions.
---
Selected Answer: B
The correct answer is B. Text generation is the appropriate feature for converting natural language into code.

</details>

---

## Question 59: AIF-C01-ET-Q059
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is introducing a mobile app that helps users learn foreign languages. The app makes text more coherent by calling a large language model (LLM). The company collected a diverse dataset of text and supplemented the dataset with examples of more readable versions. The company wants the LLM output to resemble the provided examples.

Which metric should the company use to assess whether the LLM meets these requirements?

**Choices:**
- A) Value of the loss function
- B) Semantic robustness
- C) Recall-Oriented Understudy for Gisting Evaluation (ROUGE) score
- D) Latency of the text generation

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The ROUGE (Recall-Oriented Understudy for Gisting Evaluation) score is widely used to measure the similarity between generated text and a set of reference texts. Since the company wants the LLM's output to resemble the provided readable examples, ROUGE is the most appropriate metric.

ROUGE compares the LLM-generated text with the human-provided reference texts by evaluating n-gram overlap, precision, recall, and F1 score, making it a great choice for text coherence and readability assessment.
---
Selected Answer: C
The correct answer is C. ROUGE score measures how well generated text matches reference examples.
---
Selected Answer: C
Since the company wants the LLM output to resemble the provided examples in terms of coherence and readability, ROUGE score is the best metric for this evaluation.

</details>

---

## Question 60: AIF-C01-ET-Q060
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company notices that its foundation model (FM) generates images that are unrelated to the prompts. The company wants to modify the prompt techniques to decrease unrelated images.

Which solution meets these requirements?

**Choices:**
- A) Use zero-shot prompts.
- B) Use negative prompts.
- C) Use positive prompts.
- D) Use ambiguous prompts.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Helps exclude unwanted elements, making images more relevant.
---
Selected Answer: B
The correct answer is B. Using negative prompts can help guide the model away from generating unrelated images.
---
Selected Answer: B
By using negative prompts, the company can reduce the generation of unrelated images by specifying what should not be included in the output, leading to more accurate and relevant image generation based on the given prompt.

</details>

---

## Question 61: AIF-C01-ET-Q061
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company wants to use large language models (LLMs) with Amazon Bedrock to develop a chat interface for the company's product manuals. The manuals are stored as PDF files.
Which solution meets these requirements MOST cost-effectively?

**Choices:**
- A) Use prompt engineering to add one PDF file as context to the user prompt when the prompt is submitted to Amazon Bedrock.
- B) Use prompt engineering to add all the PDF files as context to the user prompt when the prompt is submitted to Amazon Bedrock.
- C) Use all the PDF documents to fine-tune a model with Amazon Bedrock. Use the fine-tuned model to process user prompts.
- D) Upload PDF documents to an Amazon Bedrock knowledge base. Use the knowledge base to provide context when users submit prompts to Amazon Bedrock.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Upload PDF documents to an Amazon Bedrock knowledge base. Use the knowledge base to provide context when users submit prompts to Amazon Bedrock: While this could be an efficient solution, it may not be as cost-effective as using prompt engineering with just the necessary context per query. Building and maintaining a knowledge base could incur additional costs, especially if the company only needs a temporary context for each query.
---
Selected Answer: D
Amazon Bedrock Knowledge Base
---
Selected Answer: D
Using a knowledge base allows for efficient retrieval of relevant information from the PDFs without having to include all the content in every prompt.

</details>

---

## Question 62: AIF-C01-ET-Q062
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A social media company wants to use a large language model (LLM) for content moderation. The company wants to evaluate the LLM outputs for bias and potential discrimination against specific groups or individuals.
Which data source should the company use to evaluate the LLM outputs with the LEAST administrative effort?

**Choices:**
- A) User-generated content
- B) Moderation logs
- C) Content moderation guidelines
- D) Benchmark datasets

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
A resposta correta é: D. Conjuntos de dados de referência

Explicação simples:
Esses conjuntos de dados já estão prontos e foram feitos justamente para testar preconceitos e discriminação. Usá-los economiza tempo e trabalho, porque não é preciso montar tudo do zero.
---
Selected Answer: D
Benchmark datasets: Benchmark datasets are specifically designed for evaluating models on specific tasks, including fairness and bias. These datasets typically include a wide range of content and scenarios designed to assess how well the model handles various forms of bias or discrimination. Using these datasets will provide the least administrative effort because they are pre-structured and widely recognized for evaluating model behavior across a variety of contexts.
---
Selected Answer: D
Least administrative effort: Benchmark datasets are pre-existing, curated collections of data specifically designed for evaluating AI models, including LLMs. Using these requires the least administrative effort compared to the other options.

</details>

---

## Question 63: AIF-C01-ET-Q063
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use a pre-trained generative AI model to generate content for its marketing campaigns. The company needs to ensure that the generated content aligns with the company's brand voice and messaging requirements.
Which solution meets these requirements?

**Choices:**
- A) Optimize the model's architecture and hyperparameters to improve the model's overall performance.
- B) Increase the model's complexity by adding more layers to the model's architecture.
- C) Create effective prompts that provide clear instructions and context to guide the model's generation.
- D) Select a large, diverse dataset to pre-train a new generative model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
A alternativa correta é:

C. Crie prompts eficazes que forneçam instruções claras e contexto para orientar a geração do modelo.

Explicação simples:
Se a empresa quer usar um modelo de IA já pronto (pré-treinado) para criar conteúdo de marketing alinhado com a voz da marca, a melhor maneira de garantir isso é com prompts bem feitos.

Um prompt eficaz:

Dá instruções claras sobre o tom, estilo e mensagem que o conteúdo deve seguir.

Pode incluir exemplos de conteúdo anterior, palavras-chave da marca ou diretrizes de comunicação.
---
Selected Answer: C
C. Create effective prompts that provide clear instructions and context to guide the model's generation: This is the best approach for aligning the generated content with the company's specific voice and messaging requirements. By crafting detailed and specific prompts, the company can guide the generative AI model to produce content that aligns with the brand's tone, values, and style. Prompt engineering allows you to control the output without needing to modify the underlying model itself.
---
Selected Answer: C
C. Create effective prompts that provide clear instructions and context to guide the model's generation.

Prompt engineering is a crucial technique to ensure that a pre-trained generative AI model generates content that aligns with the company's brand voice and messaging requirements. By carefully crafting prompts, you can guide the model to produce specific, relevant, and on-brand content.

</details>

---

## Question 64: AIF-C01-ET-Q064
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A loan company is building a generative AI-based solution to offer new applicants discounts based on specific business criteria. The company wants to build and use an AI model responsibly to minimize bias that could negatively affect some customers.
Which actions should the company take to meet these requirements? (Choose two.)

**Choices:**
- A) Detect imbalances or disparities in the data.
- B) Ensure that the model runs frequently.
- C) Evaluate the model's behavior so that the company can provide transparency to stakeholders.
- D) Use the Recall-Oriented Understudy for Gisting Evaluation (ROUGE) technique to ensure that the model is 100% accurate.
- E) Ensure that the model's inference time is within the accepted limits.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (100%). Contributor Answer: AC.

Community Rationale & Discussion:
The correct answers are A and C:

A: Detect imbalances or disparities in the data
C: Evaluate the model's behavior so that the company can provide transparency to stakeholders

Let's analyze why these are correct:

Detect imbalances or disparities in the data (A):

Essential for identifying potential sources of bias in training data
Helps ensure fair representation across different customer groups
Allows for correction of data bias before model training
Critical for responsible AI development in financial services

Evaluate model's behavior for transparency (C):

Enables stakeholder understanding of model decisions
Helps identify potential discriminatory patterns
Supports regulatory compliance
Essential for maintaining accountability
---
Selected Answer: AC
A. Detect imbalances or disparities in the data: Bias often originates from imbalanced or biased data. By detecting and addressing any imbalances or disparities in the data (such as certain groups being overrepresented or underrepresented), the company can ensure that the model treats all applicants fairly, regardless of their background. This helps to minimize potential bias that could negatively affect certain customers.

C. Evaluate the model's behavior so that the company can provide transparency to stakeholders: Evaluating the model’s behavior is crucial for responsible AI usage. By assessing how the model performs across different customer groups, the company can ensure that the model is not inadvertently discriminating or providing unfair treatment. Transparency about the model's decision-making process also builds trust with stakeholders and customers.
---
Selected Answer: AC
A. Detect imbalances or disparities in the data C. Evaluate the model's behavior so that the company can provide transparency to stakeholders

Why:

Detecting imbalances or disparities in the data is crucial because:
It helps identify potential bias in training data before it affects model decisions
It ensures fair treatment across different customer segments
It aligns with responsible AI development practices
Evaluating model behavior for transparency is important because:
It allows stakeholders to understand how decisions are made
It helps demonstrate compliance with fair lending regulations
It enables the company to justify decisions to customers and regulators

below incorrect because:

B (frequent model runs) doesn't address bias or responsible AI
D (ROUGE technique) is for text summarization evaluation, not lending decisions
E (inference time) is about performance, not fairness or responsibility

</details>

---

## Question 65: AIF-C01-ET-Q065
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is using a pre-trained large language model (LLM) to build a chatbot for product recommendations. The company needs the LLM outputs to be short and written in a specific language.
Which solution will align the LLM response quality with the company's expectations?

**Choices:**
- A) Adjust the prompt.
- B) Choose an LLM of a different size.
- C) Increase the temperature.
- D) Increase the Top K value.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
B not correct - The size of LLM may not affect the size of the output.
C not correct - Temperature controls the creativity of the output, not size of the output.
D not correct - Top-K controls number of next possible tokens, not size of the output. 
A is correct - In the prompt itself we can control various attributes of the output like size, language etc.
---
Selected Answer: A
Adjusting the prompt allows you to guide the model to produce responses that are more aligned with your desired output. By modifying the prompt, you can specify the length and language requirements more clearly. For example, you could ask the model to "Provide a short product recommendation in [specific language]." This is the most direct way to control the behavior of the LLM and ensure it meets the company’s needs.
---
Selected Answer: A
A: Adjust the prompt.

Explanation:
The behavior of a large language model (LLM) can be significantly influenced by the prompt it receives. To make the outputs short and written in a specific language, you can adjust the prompt to explicitly instruct the model to produce concise responses and specify the desired language. For example:

"Provide a brief recommendation in Spanish."
"Give a short response in French."
This is the most direct way to align the output with the company’s expectations without requiring modifications to the model or its parameters.

</details>

---

## Question 66: AIF-C01-ET-Q066
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company is using an Amazon Bedrock base model to summarize documents for an internal use case. The company trained a custom model to improve the summarization quality.
Which action must the company take to use the custom model through Amazon Bedrock?

**Choices:**
- A) Purchase Provisioned Throughput for the custom model.
- B) Deploy the custom model in an Amazon SageMaker endpoint for real-time inference.
- C) Register the model with the Amazon SageMaker Model Registry.
- D) Grant access to the custom model in Amazon Bedrock.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `57%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (57%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Initially I was going with D but after reading this article sticking with A
https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html?form=MG0AV3
---
Selected Answer: A
A To customize model you must purchase Provisioned Throughput.
---
Selected Answer: D
When you train a custom model using Amazon Bedrock, especially via fine-tuning a base foundation model (e.g., Anthropic Claude, AI21, etc.), the custom model is managed within Bedrock itself.

To use it in your applications via Bedrock APIs, you must:

Grant access to the fine-tuned (custom) model within Bedrock.

This allows your applications to invoke it using Bedrock's InvokeModel API.

</details>

---

## Question 67: AIF-C01-ET-Q067
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company needs to choose a model from Amazon Bedrock to use internally. The company must identify a model that generates responses in a style that the company's employees prefer.
What should the company do to meet these requirements?

**Choices:**
- A) Evaluate the models by using built-in prompt datasets.
- B) Evaluate the models by using a human workforce and custom prompt datasets.
- C) Use public model leaderboards to identify the model.
- D) Use the model InvocationLatency runtime metrics in Amazon CloudWatch when trying models.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Evaluate the models by using a human workforce and custom prompt datasets: This approach ensures that the evaluation is tailored to the company's specific needs. By using a human workforce to test how the models generate responses and customizing the prompt datasets, the company can assess how well the model aligns with the style that their employees prefer. This is the most effective method for evaluating and selecting a model based on the desired output style.
---
Selected Answer: B
B: Evaluate the models by using a human workforce and custom prompt datasets.

Explanation:
To determine which model generates responses in the style that the company's employees prefer, the company should evaluate the models using custom prompt datasets relevant to their specific use cases. Additionally, involving a human workforce ensures subjective aspects, like tone, style, and alignment with employee preferences, are effectively assessed.
---
Selected Answer: B
Custom prompting is the way.

</details>

---

## Question 68: AIF-C01-ET-Q068
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A student at a university is copying content from generative AI to write essays.
Which challenge of responsible generative AI does this scenario represent?

**Choices:**
- A) Toxicity
- B) Hallucinations
- C) Plagiarism
- D) Privacy

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Plagiarism: This is the correct answer because the student is using generative AI content and copying it as their own work, which is a clear case of plagiarism. The ethical challenge here is the student passing off AI-generated content as their own without proper citation or acknowledgment.
---
Selected Answer: C
Plagiarism is the act of taking someone else's work or ideas and passing them off as one's own. In this case, the student is using AI-generated content without proper attribution, which is a form of plagiarism.
---
Selected Answer: C
The student is plagiarizing.

</details>

---

## Question 69: AIF-C01-ET-Q069
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company needs to build its own large language model (LLM) based on only the company's private data. The company is concerned about the environmental effect of the training process.
Which Amazon EC2 instance type has the LEAST environmental effect when training LLMs?

**Choices:**
- A) Amazon EC2 C series
- B) Amazon EC2 G series
- C) Amazon EC2 P series
- D) Amazon EC2 Trn series

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon EC2 Trn series: These instances are specifically designed for training deep learning models and are optimized for energy efficiency. They use specialized AWS-designed chips (Tranium) that provide a better performance-to-energy ratio, reducing the environmental impact of training large models.
---
Selected Answer: D
D: Amazon EC2 Trn series

Explanation:
The Amazon EC2 Trn series (Trn1 instances) are purpose-built for training machine learning models and are designed to deliver high performance while optimizing energy efficiency. They use AWS Trainium chips, which are specifically engineered for ML training workloads, providing excellent performance per watt and reducing the environmental impact of large-scale training processes.
---
Selected Answer: D
From the documentation of the Sustainability pillar here : https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a3.html

"For machine learning workloads, take advantage of purpose-built hardware that is specific to your workload such as AWS Trainium, AWS Inferentia, and Amazon EC2 DL1. AWS Inferentia instances such as Inf2 instances offer up to 50% better performance per watt over comparable Amazon EC2 instances."

</details>

---

## Question 70: AIF-C01-ET-Q070
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company wants to build an interactive application for children that generates new stories based on classic stories. The company wants to use Amazon Bedrock and needs to ensure that the results and topics are appropriate for children.
Which AWS service or feature will meet these requirements?

**Choices:**
- A) Amazon Rekognition
- B) Amazon Bedrock playgrounds
- C) Guardrails for Amazon Bedrock
- D) Agents for Amazon Bedrock

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Guardrails for Amazon Bedrock: Guardrails are a set of best practices and safety mechanisms that can be applied to ensure content generated by foundation models, like those from Amazon Bedrock, adheres to specific safety and appropriateness guidelines. This includes ensuring that the generated stories are suitable for children and avoid inappropriate content.
---
Selected Answer: C
Guardrails helps to filter the unnecessary content, and release only appropriate results and topics to the children.
---
Selected Answer: C
C is correct

</details>

---

## Question 71: AIF-C01-ET-Q071
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building an application that needs to generate synthetic data that is based on existing data.
Which type of model can the company use to meet this requirement?

**Choices:**
- A) Generative adversarial network (GAN)
- B) XGBoost
- C) Residual neural network
- D) WaveNet

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Generative adversarial network (GAN): GANs are specifically designed for generating synthetic data. They consist of two neural networks: a generator and a discriminator. The generator creates synthetic data that resembles the real data, and the discriminator tries to distinguish between real and generated data. This process enables GANs to generate realistic synthetic data, making them ideal for use cases where synthetic data is needed based on existing data.
---
Selected Answer: A
GANS can do this (A & B can do this task). But, Why can't we use XGBoost to generate the Synthetic data?.
---
Selected Answer: A
100% A - GANs are specifically designed to generate synthetic data that closely resembles real data. This aligns perfectly with the company's requirement.

</details>

---

## Question 72: AIF-C01-ET-Q072
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A digital devices company wants to predict customer demand for memory hardware. The company does not have coding experience or knowledge of ML algorithms and needs to develop a data-driven predictive model. The company needs to perform analysis on internal data and external data.
Which solution will meet these requirements?

**Choices:**
- A) Store the data in Amazon S3. Create ML models and demand forecast predictions by using Amazon SageMaker built-in algorithms that use the data from Amazon S3.
- B) Import the data into Amazon SageMaker Data Wrangler. Create ML models and demand forecast predictions by using SageMaker built-in algorithms.
- C) Import the data into Amazon SageMaker Data Wrangler. Build ML models and demand forecast predictions by using an Amazon Personalize Trending-Now recipe.
- D) Import the data into Amazon SageMaker Canvas. Build ML models and demand forecast predictions by selecting the values in the data from SageMaker Canvas.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
D. Amazon SageMaker Canvas: SageMaker Canvas is a no-code solution designed specifically for users who don't have deep machine learning or coding expertise. It provides an easy-to-use interface to build machine learning models, perform data analysis, and generate predictions (like demand forecasting) without writing any code. Users can simply import their data and interact with the application to select values and generate predictions.
---
Selected Answer: D
Amazon SageMaker Canvas supports to build and run the AI solutions without code.
---
Selected Answer: D
Amazon SageMaker Canvas is a no-code machine learning service that allows users without coding or ML expertise to build predictive models. It enables the company to import data, perform analysis, and build ML models through an easy-to-use graphical interface. This makes it ideal for businesses with limited technical expertise but a need for data-driven predictions.

</details>

---

## Question 73: AIF-C01-ET-Q073
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
A company has installed a security camera. The company uses an ML model to evaluate the security camera footage for potential thefts. The company has discovered that the model disproportionately flags people who are members of a specific ethnic group.
Which type of bias is affecting the model output?

**Choices:**
- A) Measurement bias
- B) Sampling bias
- C) Observer bias
- D) Confirmation bias

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `85%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (85%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Sampling bias occurs when the data used to train the machine learning model is not representative of the entire population or the range of possible scenarios. If the model disproportionately flags people from a specific ethnic group, it suggests that the data used to train the model may have an overrepresentation or underrepresentation of certain ethnic groups, leading to biased predictions.
---
Selected Answer: B
B. Sampling bias occurs when the data used to train the model is not representative of the entire population. In this case, if the training data contains an overrepresentation or underrepresentation of certain ethnic groups, the model may disproportionately flag individuals from specific ethnic groups, leading to biased outcomes.
---
Selected Answer: A
Measurement bias occurs when the data used to train the machine learning model contains inherent biases or inaccuracies, leading to biased outputs or predictions.

In the given scenario, the security camera model is disproportionately flagging people from a specific ethnic group

</details>

---

## Question 74: AIF-C01-ET-Q074
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building a customer service chatbot. The company wants the chatbot to improve its responses by learning from past interactions and online resources.
Which AI learning strategy provides this self-improvement capability?

**Choices:**
- A) Supervised learning with a manually curated dataset of good responses and bad responses
- B) Reinforcement learning with rewards for positive customer feedback
- C) Unsupervised learning to find clusters of similar customer inquiries
- D) Supervised learning with a continuously updated FAQ database

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Reinforcement learning with rewards for positive customer feedback is the strategy that provides self-improvement capability. In reinforcement learning (RL), an agent (in this case, the chatbot) learns by interacting with its environment and receiving feedback (rewards or penalties). The chatbot can improve its performance over time by adjusting its responses based on positive feedback from users. This allows it to "learn" from past interactions and improve autonomously.
---
Selected Answer: B
Reinforcement learning: is the most suitable strategy for a chatbot to continuously improve its responses based on real-time feedback from users. The chatbot can "learn" by receiving positive reinforcement (reward) when it provides a helpful response and negative reinforcement when it doesn't, allowing it to adjust its responses over time to better suit customer needs.
Why other options are not suitable:
A. While this can provide a good initial training set, it wouldn't allow the chatbot to adapt to new situations or customer feedback without manual intervention.
C. This can be helpful in understanding customer patterns but wouldn't directly improve the chatbot's responses without additional training data or feedback mechanisms.
D. While updating the FAQ database can be beneficial, it still requires manual effort and wouldn't enable the chatbot to learn from real-time interactions with customers in the same way that reinforcement learning does.
---
Selected Answer: B
Reinforcement learning: This method allows the chatbot to learn from the outcomes of its actions, essentially receiving "rewards" for positive customer feedback and adjusting its responses accordingly to maximize those rewards in the future.

</details>

---

## Question 75: AIF-C01-ET-Q075
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
An AI practitioner has built a deep learning model to classify the types of materials in images. The AI practitioner now wants to measure the model performance.

Which metric will help the AI practitioner evaluate the performance of the model?

**Choices:**
- A) Confusion matrix
- B) Correlation matrix
- C) R2 score
- D) Mean squared error (MSE)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Confusion matrix is a key metric for evaluating classification models. It provides a summary of the model's predictions, showing the true positive, false positive, true negative, and false negative counts. This allows the AI practitioner to understand how well the model is classifying the different types of materials, and helps in calculating other important metrics like accuracy, precision, recall, and F1-score.
---
Selected Answer: A
The model is performing a classification task (identifying types of materials), and confusion matrices are specifically designed for evaluating classification models.
---
A. Confusion matrix

A confusion matrix is a useful metric for evaluating the performance of a classification model. It provides a summary of prediction results on a classification problem, showing the number of correct and incorrect predictions broken down by each class. This helps the AI practitioner understand how well the model is distinguishing between different types of materials in the images.

</details>

---

## Question 76: AIF-C01-ET-Q076
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company uses Amazon SageMaker for its ML pipeline in a production environment. The company has large input data sizes up to 1 GB and processing times up to 1 hour. The company needs near real-time latency.
Which SageMaker inference option meets these requirements?

**Choices:**
- A) Real-time inference
- B) Serverless inference
- C) Asynchronous inference
- D) Batch transform

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `79%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (79%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Real-Time Inference: Immediate responses for high-traffic, low-latency applications.
>> Asynchronous Inference: Near real-time for large payloads and longer processing.
Batch Transform: Large-scale, offline processing without real-time needs.
Serverless Inference: Low-latency inference for intermittent or unpredictable traffic without managing infrastructure.
---
Selected Answer: A
Asynchronous inference processes requests in the background, returning a response ID and allowing the client to check for results later, while real-time inference delivers redictions with minimal delay, suitable for interactive applications
---
Selected Answer: C
Explicação:A inferência assíncrona do Amazon SageMaker é ideal quando:
Os dados de entrada são grandes (por exemplo, até 1 GB),O tempo de processamento Pode ser longo (até 1 hora por solicitação),E você ainda precisa de respostas com latência razoável, mas não exige resposta instantânea como em APIs síncronas.
Ela permite que você envie a solicitação, continue processando outras tarefas e recupere o resultado quando estiver pronto, o que evita timeouts comuns em inferência síncrona.

</details>

---

## Question 77: AIF-C01-ET-Q077
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has built a chatbot that can respond to natural language questions with images. The company wants to ensure that the chatbot does not return inappropriate or unwanted images.
Which solution will meet these requirements?

**Choices:**
- A) Implement moderation APIs.
- B) Retrain the model with a general public dataset.
- C) Perform model validation.
- D) Automate user feedback integration.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Implement moderation APIs: Moderation APIs can help screen the content generated by the chatbot to ensure that inappropriate or unwanted images are not returned to users. These APIs can identify and filter out offensive, explicit, or harmful content before it's shown to the user. This is the most direct and effective way to ensure content is appropriate.
---
Selected Answer: A
A: Implement moderation APIs.

Explanation:
Moderation APIs are designed to detect and filter inappropriate or unwanted content, such as images, text, or videos. By integrating moderation APIs into the chatbot workflow, the company can screen and block inappropriate images before they are returned to users. This ensures compliance with ethical standards and avoids exposing users to harmful or unwanted content.
---
Selected Answer: A
Amazon Rekognition moderation APIs can help you automatically identify and filter inappropriate content in images and videos, reducing the need for manual human review. This can significantly improve efficiency and reduce costs while maintaining high standards of content moderation. For details, please refer to the following document:
https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html

</details>

---

## Question 78: AIF-C01-ET-Q078
**Domain 3:** Applications of Foundation Models  

**Question:**  
An AI practitioner is using an Amazon Bedrock base model to summarize session chats from the customer service department. The AI practitioner wants to store invocation logs to monitor model input and output data.
Which strategy should the AI practitioner use?

**Choices:**
- A) Configure AWS CloudTrail as the logs destination for the model.
- B) Enable invocation logging in Amazon Bedrock.
- C) Configure AWS Audit Manager as the logs destination for the model.
- D) Configure model invocation logging in Amazon EventBridge.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Enable invocation logging in Amazon Bedrock: Amazon Bedrock provides a built-in option to enable invocation logging. This feature allows you to capture and store detailed logs for model invocations, including input and output data, which helps you monitor and analyze the performance and behavior of the model.
---
Selected Answer: B
B: Enable invocation logging in Amazon Bedrock.

Explanation:
Amazon Bedrock provides the ability to log model invocations, including input and output data, for monitoring and troubleshooting purposes. By enabling invocation logging in Amazon Bedrock, the AI practitioner can store logs securely and use them to analyze model behavior and performance.
---
Selected Answer: B
B - The question mentions using an Amazon Bedrock base model, and invocation logging is a feature specifically designed for Amazon Bedrock.

</details>

---

## Question 79: AIF-C01-ET-Q079
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building an ML model to analyze archived data. The company must perform inference on large datasets that are multiple GBs in size. The company does not need to access the model predictions immediately.
Which Amazon SageMaker inference option will meet these requirements?

**Choices:**
- A) Batch transform
- B) Real-time inference
- C) Serverless inference
- D) Asynchronous inference

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `78%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (78%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Batch transform is ideal for scenarios where you need to perform inference on large datasets, but the predictions are not needed immediately.
---
Selected Answer: A
A. Batch transform: This is the best option for performing inference on large datasets that are stored in bulk and do not require immediate access to predictions. Batch transform allows you to process large amounts of data (such as multiple GBs of archived data) in batches, without the need for real-time responses. You can submit data in large volumes, and SageMaker processes the data and returns the results once the job completes.
---
Selected Answer: A
A. Batch transform ✅

Explanation:
Batch Transform is ideal for processing large datasets in bulk when immediate responses are not needed.
It supports multiple GB-sized datasets and can handle inference without requiring an endpoint to be always active.
Since the company is working with archived data and does not need real-time predictions, batch processing is the most efficient and cost-effective choice.

</details>

---

## Question 80: AIF-C01-ET-Q080
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
Which term describes the numerical representations of real-world objects and concepts that AI and natural language processing (NLP) models use to improve understanding of textual information?

**Choices:**
- A) Embeddings
- B) Tokens
- C) Models
- D) Binaries

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Embeddings: Embeddings are numerical representations of words, phrases, or even entire documents. These representations capture the semantic meaning of the real-world objects and concepts and are used by AI and NLP models to improve their understanding of textual information. They help the model interpret and process language in a more meaningful way.
---
Selected Answer: A
A. Embeddings

Explanation:
Embeddings are numerical representations of real-world objects, words, phrases, or concepts in a continuous vector space. They enable AI and Natural Language Processing (NLP) models to understand and process textual information by capturing the semantic relationships and contextual meanings of words and phrases.
---
Explanation:

 Embeddings are numerical representations of real-world objects, concepts, or textual data. In AI and NLP, embeddings map words, phrases, or even entire documents to a high-dimensional vector space. This allows models to capture semantic relationships and improve understanding of the textual information

</details>

---

## Question 81: AIF-C01-ET-Q081
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A research company implemented a chatbot by using a foundation model (FM) from Amazon Bedrock. The chatbot searches for answers to questions from a large database of research papers.
After multiple prompt engineering attempts, the company notices that the FM is performing poorly because of the complex scientific terms in the research papers.
How can the company improve the performance of the chatbot?

**Choices:**
- A) Use few-shot prompting to define how the FM can answer the questions.
- B) Use domain adaptation fine-tuning to adapt the FM to complex scientific terms.
- C) Change the FM inference parameters.
- D) Clean the research paper data to remove complex scientific terms.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `91%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (91%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Domain adaptation fine-tuning is a method where the foundation model (FM) is fine-tuned on a specific domain's dataset, allowing the model to better understand and handle specialized language or complex terms relevant to that domain. In this case, since the chatbot is struggling with complex scientific terms in the research papers, fine-tuning the model on a corpus of research papers with similar scientific terminology will help it perform better in answering questions related to these terms.
---
Selected Answer: B
B. Use domain adaptation fine-tuning: Domain adaptation fine-tuning involves customizing the foundation model (FM) to perform better in a specific domain (in this case, research papers with complex scientific terms). By fine-tuning the FM on a corpus that includes more examples of the complex terminology and context of the research papers, the model will become better at understanding and generating appropriate responses. This improves its performance with domain-specific language
---
Selected Answer: B
Domain Adaptation fine-tuning helps for industry-specific terminology based solutions.

</details>

---

## Question 82: AIF-C01-ET-Q082
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use a large language model (LLM) on Amazon Bedrock for sentiment analysis. The company needs the LLM to produce more consistent responses to the same input prompt.
Which adjustment to an inference parameter should the company make to meet these requirements?

**Choices:**
- A) Decrease the temperature value.
- B) Increase the temperature value.
- C) Decrease the length of output tokens.
- D) Increase the maximum generation length.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Decrease the temperature value: The temperature parameter controls the randomness of the model’s output. Lower temperatures make the model more deterministic and lead to more consistent and focused responses, while higher temperatures introduce more randomness and variety. For sentiment analysis, where you want consistent outputs for the same input, decreasing the temperature will help achieve more predictable and reliable results.
---
Selected Answer: A
Lowering the temperature value in an LLM controls the randomness of the model's output. A lower temperature (close to 0) makes the model's predictions more deterministic and consistent, leading to similar outputs for identical prompts. This is particularly beneficial in tasks like sentiment analysis, where consistency and reliability in responses are crucial.
---
A. Decrease the temperature value.

Lowering the temperature value reduces the randomness of predictions from a large language model (LLM) and makes the output more deterministic and consistent. This is ideal for producing consistent responses to the same input prompt during sentiment analysis.

</details>

---

## Question 83: AIF-C01-ET-Q083
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to develop a large language model (LLM) application by using Amazon Bedrock and customer data that is uploaded to Amazon S3. The company's security policy states that each team can access data for only the team's own customers.
Which solution will meet these requirements?

**Choices:**
- A) Create an Amazon Bedrock custom service role for each team that has access to only the team's customer data.
- B) Create a custom service role that has Amazon S3 access. Ask teams to specify the customer name on each Amazon Bedrock request.
- C) Redact personal data in Amazon S3. Update the S3 bucket policy to allow team access to customer data.
- D) Create one Amazon Bedrock role that has full Amazon S3 access. Create IAM roles for each team that have access to only each team's customer folders.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (71%). Contributor Answer: A.

Community Rationale & Discussion:
This option ensures that each team has a dedicated service role with permissions specifically tailored to access only their own customer data. This approach aligns with the company's security policy by enforcing strict access controls at the role level, ensuring that teams cannot access data belonging to other teams. By creating separate roles for each team, the solution adheres to the principle of least privilege, which is a fundamental security best practice. This method also simplifies auditing and management of access permissions, as each role's permissions can be reviewed and adjusted independently.
---
Selected Answer: A
A. Create an Amazon Bedrock custom service role for each team that has access to only the team's customer data.: This would require multiple service roles for Amazon Bedrock itself, which could lead to unnecessary complexity and overhead in role management. It's better to use IAM roles to control team-specific data access.
---
Selected Answer: D
By creating a single Bedrock role with full S3 access and then using IAM roles to control access to the customer data folders, the company can meet its requirements for developing the LLM application while also adhering to its security policy.

</details>

---

## Question 84: AIF-C01-ET-Q084
**Domain 3:** Applications of Foundation Models  

**Question:**  
A medical company deployed a disease detection model on Amazon Bedrock. To comply with privacy policies, the company wants to prevent the model from including personal patient information in its responses. The company also wants to receive notification when policy violations occur.
Which solution meets these requirements?

**Choices:**
- A) Use Amazon Macie to scan the model's output for sensitive data and set up alerts for potential violations.
- B) Configure AWS CloudTrail to monitor the model's responses and create alerts for any detected personal information.
- C) Use Guardrails for Amazon Bedrock to filter content. Set up Amazon CloudWatch alarms for notification of policy violations.
- D) Implement Amazon SageMaker Model Monitor to detect data drift and receive alerts when model quality degrades.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Explicação:Guardrails for Amazon Bedrock permite configurar diretrizes que ajudam a impedir que os modelos fundacionais (FMs) incluam informações pessoais ou violem políticas de uso. Isso é feito por meio de filtros e regras de moderação de conteúdo.Amazon CloudWatch pode ser usado para configurar alarmes e notificações quando essas políticas forem violadas, fornecendo a visibilidade necessária em tempo real.
---
Selected Answer: C
C. Use Guardrails for Amazon Bedrock to filter content. Set up Amazon CloudWatch alarms for notification of policy violations.: Guardrails for Amazon Bedrock are designed to enforce compliance and mitigate the risk of inappropriate or sensitive data being generated by foundation models. Guardrails can filter content to prevent sensitive information from being included in model outputs. Amazon CloudWatch alarms can then be configured to notify the company of potential policy violations, making it a comprehensive solution for ensuring privacy and compliance.
---
Selected Answer: C
C: Use Guardrails for Amazon Bedrock to filter content. Set up Amazon CloudWatch alarms for notification of policy violations.

Explanation:
Guardrails for Amazon Bedrock allow you to enforce policies that filter out sensitive or inappropriate content, such as personal patient information, from the model's responses. By configuring these guardrails, you ensure that the model adheres to privacy policies. Additionally, you can set up Amazon CloudWatch alarms to receive notifications when policy violations occur, providing real-time monitoring and alerting.

</details>

---

## Question 85: AIF-C01-ET-Q085
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company manually reviews all submitted resumes in PDF format. As the company grows, the company expects the volume of resumes to exceed the company's review capacity. The company needs an automated system to convert the PDF resumes into plain text format for additional processing.
Which AWS service meets this requirement?

**Choices:**
- A) Amazon Textract
- B) Amazon Personalize
- C) Amazon Lex
- D) Amazon Transcribe

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (67%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Explicação:
Amazon Textract é um serviço da AWS que extrai automaticamente texto, dados e informações estruturadas de documentos digitalizados, como arquivos PDF ou imagens. Ele é ideal para converter currículos em texto simples para análise e processamento adicional.
Por que as outras opções estão incorretas:
B. Amazon Personalize: É usado para criar sistemas de recomendação personalizados, não para extrair texto de documentos.
C. Amazon Lex: É um serviço de criação de chatbots com linguagem natural, não converte PDFs em texto.
D. Amazon Transcribe: É usado para converter fala em texto (por exemplo, de arquivos de áudio), não para processar documentos PDF.
---
Selected Answer: A
A. Amazon Textract: Amazon Textract is a fully managed service that automatically extracts text and data from scanned documents, including PDFs. It uses machine learning to identify the text in the document and converts it into a plain-text format, making it ideal for converting resumes from PDF to text for further processing.
---
Amazon Textract is designed to extract text, handwriting, and structured data (like tables and forms) from documents such as PDFs. It is ideal for automating the conversion of resumes into plain text format for further processing.

</details>

---

## Question 86: AIF-C01-ET-Q086
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
An education provider is building a question and answer application that uses a generative AI model to explain complex concepts. The education provider wants to automatically change the style of the model response depending on who is asking the question. The education provider will give the model the age range of the user who has asked the question.
Which solution meets these requirements with the LEAST implementation effort?

**Choices:**
- A) Fine-tune the model by using additional training data that is representative of the various age ranges that the application will support.
- B) Add a role description to the prompt context that instructs the model of the age range that the response should target.
- C) Use chain-of-thought reasoning to deduce the correct style and complexity for a response suitable for that user.
- D) Summarize the response text depending on the age of the user so that younger users receive shorter responses.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Adding a role description to the prompt is a straightforward approach that requires minimal changes to the existing model infrastructure. This method leverages prompt engineering, which is often easier and faster to implement than fine-tuning or retraining a model.
---
Selected Answer: B
Essa abordagem é simples, eficaz e de baixo esforço de implementação. Modelos de IA generativa, especialmente os baseados em prompt engineering, respondem bem a instruções contextuais.Ao incluir no prompt algo como “Explique este conceito para uma criança de 10 anos” ou “Responda como se estivesse falando com um universitário”, o modelo adapta o estilo e a complexidade da resposta automaticamente
---
Selected Answer: B
B. Add a role description to the prompt context: This approach leverages prompt engineering, where you include specific instructions within the input to guide the model's response style. By adding the age range of the user to the prompt, you can influence the style and complexity of the model’s answer based on that information. This is a highly efficient and low-effort solution that doesn't require fine-tuning the model or complex setups.

</details>

---

## Question 87: AIF-C01-ET-Q087
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is using domain-specific models. The company wants to avoid creating new models from the beginning. The company instead wants to adapt pre-trained models to create models for new, related tasks.
Which ML strategy meets these requirements?

**Choices:**
- A) Increase the number of epochs.
- B) Use transfer learning.
- C) Decrease the number of epochs.
- D) Use unsupervised learning.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Transfer learning allows you to leverage pre-trained models (which have already been trained on large datasets) and adapt them for new, related tasks with minimal additional training. This strategy is highly efficient because it saves time and computational resources compared to training a model from scratch. By fine-tuning the pre-trained model on a smaller dataset specific to the new task, the model can learn task-specific features while maintaining the general knowledge it acquired during its initial training.
---
Selected Answer: B
It is clearly B. The number of epochs is not related to that issue while the (un)supervised learning is used for training a new model, which is totally different from adapting a pre-trained model to create a new model.
---
Selected Answer: B
B: Use transfer learning.

Explanation:
Transfer learning is a machine learning strategy that leverages pre-trained models and adapts them to new but related tasks. This allows the company to avoid building models from scratch, significantly reducing the time and resources required for training. By fine-tuning the pre-trained model on domain-specific data, the company can achieve high performance for the new task without starting from the beginning.

</details>

---

## Question 88: AIF-C01-ET-Q088
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
Which strategy evaluates the accuracy of a foundation model (FM) that is used in image classification tasks?

**Choices:**
- A) Calculate the total cost of resources used by the model.
- B) Measure the model's accuracy against a predefined benchmark dataset.
- C) Count the number of layers in the neural network.
- D) Assess the color accuracy of images processed by the model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Explicação:
Em tarefas de classificação de imagens, a precisão (accuracy) é uma métrica comum que compara as previsões do modelo com os rótulos reais de um conjunto de dados de teste conhecido (conjunto de dados de referência).
Por que as outras opções estão incorretas:
A. Calcule o custo total dos recursos usados pelo modelo: Isso mede eficiência ou custo operacional, não a precisão do modelo.
C. Conte o número de camadas na rede neural: Isso fornece informações sobre a complexidade do modelo, não sua precisão ou desempenho real.
D. Avalie a precisão de cores das imagens processadas pelo modelo: Irrelevante para tarefas de classificação; a precisão de cores não mede se a classificação foi correta.
---
Selected Answer: B
B. Measure the model's accuracy against a predefined benchmark dataset: This is the correct strategy for evaluating the performance of a foundation model (FM) in an image classification task. Accuracy is typically evaluated by comparing the model's predictions to the known labels of a benchmark dataset that is representative of the problem domain. This allows you to quantify how well the model is performing.
---
Selected Answer: B
B. Measure the model's accuracy against a predefined benchmark dataset.

Reasoning:
Accuracy in Image Classification:

The standard way to evaluate the accuracy of a foundation model in image classification tasks is to compare the model's predictions against the ground truth labels in a predefined benchmark dataset. This ensures consistency and reliability in performance evaluation.
Benchmark Dataset:

A benchmark dataset contains labelled images that serve as a standard for evaluating the performance of image classification models. Examples include ImageNet, CIFAR-10, or MNIST, depending on the task and complexity.
Evaluation Metrics:

Metrics such as accuracy, precision, recall, and F1 score are typically calculated using the predictions and ground truth labels in the benchmark dataset.

</details>

---

## Question 89: AIF-C01-ET-Q089
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
An accounting firm wants to implement a large language model (LLM) to automate document processing. The firm must proceed responsibly to avoid potential harms.
What should the firm do when developing and deploying the LLM? (Choose two.)

**Choices:**
- A) Include fairness metrics for model evaluation.
- B) Adjust the temperature parameter of the model.
- C) Modify the training data to mitigate bias.
- D) Avoid overfitting on the training data.
- E) Apply prompt engineering techniques.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AC`  
**Community Consensus:** `71%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AC (71%). Contributor Answer: AC.

Community Rationale & Discussion:
Selected Answer: UC
Explicação:
Desenvolver e implantar LLMs com responsabilidade envolve garantir que o modelo seja justo, ético, e evite causar danos involuntários. As duas práticas mais alinhadas com esse objetivo são:A. Incluir métricas de imparcialidade para avaliação do modelo.Avaliar a imparcialidade (fairness) garante que o modelo não gere resultados discriminatórios ou enviesados, especialmente importante em áreas sensíveis como contabilidade e finanças.
C. Modificar os dados de treinamento para mitigar o viés.O viés muitas vezes está nos dados. Corrigir ou balancear o conjunto de dados pode ajudar a reduzir decisões injustas ou distorcidas do modelo.
---
A. Include fairness metrics for model evaluation.

C. Modify the training data to mitigate bias.
---
Selected Answer: AC
A. Include fairness metrics for model evaluation: Fairness metrics help evaluate whether the model treats all groups fairly and does not introduce harmful bias. When developing an LLM for document processing, it's essential to assess and mitigate any potential biases in the model's outputs to ensure that it operates responsibly and equitably, especially when the model interacts with sensitive data.
C. Modify the training data to mitigate bias: Bias in AI models often originates from biased training data. Modifying the training data to ensure it is representative and free from harmful biases is a crucial step in reducing the risk of the model producing unfair or harmful outcomes. This proactive approach is essential for responsible deployment.

</details>

---

## Question 90: AIF-C01-ET-Q090
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building an ML model. The company collected new data and analyzed the data by creating a correlation matrix, calculating statistics, and visualizing the data.
Which stage of the ML pipeline is the company currently in?

**Choices:**
- A) Data pre-processing
- B) Feature engineering
- C) Exploratory data analysis
- D) Hyperparameter tuning

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Exploratory data analysis (EDA): EDA is the process of analyzing and visualizing the data to understand its characteristics and identify patterns, relationships, and anomalies. The company is performing actions like creating a correlation matrix, calculating statistics, and visualizing the data, all of which are typical activities in EDA.
---
Selected Answer: C
C: Exploratory data analysis

Explanation:
Exploratory Data Analysis (EDA) involves examining and summarizing data to understand its underlying structure, detect patterns, identify relationships (e.g., via a correlation matrix), and highlight any anomalies. The company's activities, such as creating a correlation matrix, calculating statistics, and visualizing the data, are typical tasks performed during EDA.

Why not the other options?
A: Data pre-processing:
Data pre-processing involves cleaning and preparing data for modeling, such as handling missing values, scaling features, or encoding categorical data. While pre-processing may follow EDA, the tasks described in the question focus on analysis rather than preparation.
---
C. Exploratory data analysis

Exploratory Data Analysis (EDA) involves examining and visualizing data to understand its structure, patterns, and relationships. Creating a correlation matrix, calculating statistics, and visualizing data are all typical tasks during the EDA phase, which helps inform later stages such as data preprocessing and feature engineering.

</details>

---

## Question 91: AIF-C01-ET-Q091
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has documents that are missing some words because of a database error. The company wants to build an ML model that can suggest potential words to fill in the missing text.
Which type of model meets this requirement?

**Choices:**
- A) Topic modeling
- B) Clustering models
- C) Prescriptive ML models
- D) BERT-based models

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
BERT (Bidirectional Encoder Representations from Transformers) is a language model designed to understand context in text by considering both the left and right sides of a word. BERT-based models are well-suited for filling in missing words in sentences due to their ability to predict masked words in a given text. This makes them ideal for tasks that require filling in missing information within text data.
---
Selected Answer: D
D. BERT-based models: BERT (Bidirectional Encoder Representations from Transformers) is a pre-trained language model that has been fine-tuned for various natural language processing tasks, including text completion. BERT-based models are particularly effective at predicting missing words or filling in gaps in text because they can understand context in both directions (left and right of the missing word). This makes them ideal for suggesting potential words to fill in missing text.
---
Selected Answer: D
**Answer: D. BERT-based models**

BERT (Bidirectional Encoder Representations from Transformers) uses a **masked language modeling** approach. It learns how to predict missing or “masked” words in a sentence based on the surrounding context. This makes a BERT-based model ideal for suggesting potential words to fill in missing text.

</details>

---

## Question 92: AIF-C01-ET-Q092
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to display the total sales for its top-selling products across various retail locations in the past 12 months.
Which AWS solution should the company use to automate the generation of graphs?

**Choices:**
- A) Amazon Q in Amazon EC2
- B) Amazon Q Developer
- C) Amazon Q in Amazon QuickSight
- D) Amazon Q in AWS Chatbot

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Amazon Q in Amazon QuickSight: Amazon QuickSight is a fully managed business intelligence service that allows users to easily create and publish interactive dashboards and visualizations. Amazon Q is a natural language query feature in QuickSight that allows users to ask questions about their data using conversational queries. It can automatically generate graphs, charts, and dashboards based on the user's natural language input. This solution is best suited for automating the generation of graphs showing total sales for top-selling products.
---
Selected Answer: C
C. Amazon Q in Amazon QuickSight: This is the correct answer. Amazon QuickSight is a cloud-based BI service that allows you to create interactive dashboards and visualizations, including graphs, from various data sources. Integrating with Amazon Q enables natural language querying to generate these visualizations more easily
---
Correct answer is C. Quicksight can generate the visual chart for visualization

</details>

---

## Question 93: AIF-C01-ET-Q093
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is building a chatbot to improve user experience. The company is using a large language model (LLM) from Amazon Bedrock for intent detection. The company wants to use few-shot learning to improve intent detection accuracy.
Which additional data does the company need to meet these requirements?

**Choices:**
- A) Pairs of chatbot responses and correct user intents
- B) Pairs of user messages and correct chatbot responses
- C) Pairs of user messages and correct user intents
- D) Pairs of user intents and correct chatbot responses

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
C. Pairs of user messages and correct user intents: Few-shot learning works by providing the model with a small number of labeled examples to help it learn how to generalize better. In this case, the model needs to be trained with examples that consist of user messages and their corresponding intents. These pairs will help the LLM improve its ability to classify new user messages into the correct intent categories. The model will use these few-shot examples to adjust its response pattern to better detect the user's intent.
---
Selected Answer: C
C. Pairs of user messages and correct user intents
Few-shot learning is a machine learning technique that allows the model to learn from small amounts of data, including labeled examples or "shots." In this case, the company wants to use few-shot learning to improve intent detection accuracy.
To implement few-shot learning for intent detection, the company needs additional data in the form of pairs of user messages and their corresponding correct user intents. This data will serve as the "shooting" examples that the LLM can learn from.
---
Selected Answer: C
C. Pairs of user messages and correct user intents

Explanation:
Few-shot learning involves training a model with a small number of examples (or samples). In this case, the goal is to improve intent detection, which requires a clear understanding of the user's intent based on their message. To fine-tune the large language model (LLM) using few-shot learning, the model needs examples of user messages along with their corresponding correct user intents. These pairs will teach the model how to accurately classify user intents based on input messages.

</details>

---

## Question 94: AIF-C01-ET-Q094
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company is using few-shot prompting on a base model that is hosted on Amazon Bedrock. The model currently uses 10 examples in the prompt. The model is invoked once daily and is performing well. The company wants to lower the monthly cost.
Which solution will meet these requirements?

**Choices:**
- A) Customize the model by using fine-tuning.
- B) Decrease the number of tokens in the prompt.
- C) Increase the number of tokens in the prompt.
- D) Use Provisioned Throughput.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `88%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (88%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Bedrock pricing is based on the number of tokens processed, which includes both input tokens (from the prompt) and output tokens (generated by the model). By decreasing the number of tokens in the prompt, you directly reduce the cost associated with each invocation of the model.
---
Selected Answer: B
B. Decrease the number of tokens in the prompt: In a few-shot learning scenario, the number of tokens used in the prompt contributes directly to the cost, as you're billed based on the number of tokens processed during each invocation. By decreasing the number of tokens in the prompt, the company can reduce the cost per invocation while still maintaining the model's performance. This can be done by reducing the number of examples or making the examples more concise.
---
Selected Answer: D
D. Use Provisioned Throughput

To lower the monthly cost, the company can use Provisioned Throughput (PT) to scale their model's resource utilization. This allows them to pay only for the actual compute time used by the model, rather than paying a fixed monthly fee.

</details>

---

## Question 95: AIF-C01-ET-Q095
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
An AI practitioner is using a large language model (LLM) to create content for marketing campaigns. The generated content sounds plausible and factual but is incorrect.
Which problem is the LLM having?

**Choices:**
- A) Data leakage
- B) Hallucination
- C) Overfitting
- D) Underfitting

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Hallucination: In the context of large language models (LLMs), hallucination refers to when the model generates content that sounds plausible and coherent but is factually incorrect or misleading. This is a common issue with generative models, where they may produce text that seems accurate on the surface but is not grounded in real data or facts.
---
Selected Answer: B
Hallucination is a phenomenon in which an LLM generates text that sounds plausible and factual but is actually incorrect or nonsensical. This occurs when the model is overconfident in its ability to generate coherent text based on patterns it has learned from training data.
---
Selected Answer: B
Hallucination

</details>

---

## Question 96: AIF-C01-ET-Q096
**Domain 3:** Applications of Foundation Models  

**Question:**  
An AI practitioner trained a custom model on Amazon Bedrock by using a training dataset that contains confidential data. The AI practitioner wants to ensure that the custom model does not generate inference responses based on confidential data.
How should the AI practitioner prevent responses based on confidential data?

**Choices:**
- A) Delete the custom model. Remove the confidential data from the training dataset. Retrain the custom model.
- B) Mask the confidential data in the inference responses by using dynamic data masking.
- C) Encrypt the confidential data in the inference responses by using Amazon SageMaker.
- D) Encrypt the confidential data in the custom model by using AWS Key Management Service (AWS KMS).

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `76%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (76%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
If the model was trained with confidential data, there's a risk it might have memorized that information and could generate it in responses. Deleting the model is the first step to prevent this.
---
Selected Answer: A
To ensure that the custom model does not generate inference responses based on confidential data, the best approach is to:

Delete the custom model: If the confidential data was used in training, there's a possibility that the model has memorized this data and might generate it in responses. Removing the model is the first step.
Remove the confidential data from the training dataset: This ensures that confidential information is not included in the model's learning process, mitigating the risk of leakage.
Retrain the custom model: After removing the confidential data, retraining the model with a cleaned dataset ensures that the model does not inadvertently include any sensitive information in its responses.
---
A
A. Delete the custom model. Remove confidential data from dataset. Retrain the model.

This is the correct answer because:

Once a model learns from confidential data, that information becomes embedded in its parameters
The only way to truly prevent it from using that knowledge is to retrain from scratch without the confidential data
Deleting and retraining ensures the model has no access to the sensitive information

</details>

---

## Question 97: AIF-C01-ET-Q097
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company has built a solution by using generative AI. The solution uses large language models (LLMs) to translate training manuals from English into other languages. The company wants to evaluate the accuracy of the solution by examining the text generated for the manuals.
Which model evaluation strategy meets these requirements?

**Choices:**
- A) Bilingual Evaluation Understudy (BLEU)
- B) Root mean squared error (RMSE)
- C) Recall-Oriented Understudy for Gisting Evaluation (ROUGE)
- D) F1 score

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `78%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (78%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Métrica Uso Principal
BLEU ✅ Tradução de texto (Machine Translation)
ROUGE Resumo de texto (Text Summarization)
RMSE Modelos de regressão
F1 Score Classificação
---
Selected Answer: A
BLEU (Bilingual Evaluation Understudy) score is a metric specifically designed for evaluating the quality of machine-generated translations by comparing them to one or more human-produced reference translations. BLEU is particularly useful for measuring the accuracy of translations, which is exactly what the company needs to evaluate in this scenario.
---
Selected Answer: A
A. Bilingual Evaluation Understudy (BLEU): This is the correct answer. BLEU is a common metric for evaluating machine translation quality. It compares the generated text to one or more reference translations and measures the n-gram overlap.

</details>

---

## Question 98: AIF-C01-ET-Q098
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building a solution to generate images for protective eyewear. The solution must have high accuracy and must minimize the risk of incorrect annotations.
Which solution will meet these requirements?

**Choices:**
- A) Human-in-the-loop validation by using Amazon SageMaker Ground Truth Plus
- B) Data augmentation by using an Amazon Bedrock knowledge base
- C) Image recognition by using Amazon Rekognition
- D) Data summarization by using Amazon QuickSight Q

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Human-in-the-loop validation combines the efficiency of machine learning with human expertise to ensure high-quality labeled data. Amazon SageMaker Ground Truth Plus enables you to have human labelers validate and correct model predictions, which reduces errors in annotations and increases the accuracy of the training data. This is particularly useful when you need to generate accurate images or annotations for protective eyewear and want to ensure that the annotations are reliable.
---
Selected Answer: A
Using Amazon SageMaker GroundTruth, human workforce to create label for the datasets which will help to get accuracy for the datasets.
---
Selected Answer: A
A: Human-in-the-loop validation by using Amazon SageMaker Ground Truth Plus

Explanation:
Amazon SageMaker Ground Truth Plus is designed for creating high-quality labeled datasets with human-in-the-loop validation to ensure accuracy. This solution helps minimize the risk of incorrect annotations by involving human reviewers to verify and correct the model's predictions. It is particularly useful for scenarios requiring precision, such as generating images with specific requirements like protective eyewear.

</details>

---

## Question 99: AIF-C01-ET-Q099
**Domain 3:** Applications of Foundation Models  

**Question:**  
A large retailer receives thousands of customer support inquiries about products every day. The customer support inquiries need to be processed and responded to quickly. The company wants to implement Agents for Amazon Bedrock.
What are the key benefits of using Amazon Bedrock agents that could help this retailer?

**Choices:**
- A) Generation of custom foundation models (FMs) to predict customer needs
- B) Automation of repetitive tasks and orchestration of complex workflows
- C) Automatically calling multiple foundation models (FMs) and consolidating the results
- D) Selecting the foundation model (FM) based on predefined criteria and metrics

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Main advantage of using Amazon Bedrock Agent is the automation of repetitive tasks and the orchestration of complex workflows. Customer support inquiries are often patterned and repetitive. By using Amazon Bedrock Agent, you can automate the initial response to such routine inquiries and information gathering. In addition, even in cases where the workflow is somewhat complex and the response required varies depending on the inquiry content, Amazon Bedrock can flexibly respond by combining multiple AI models. This will enable quick and accurate customer support while optimally utilizing human resources. It will lead to efficient processing of large volumes of inquiries, which will lead to improved customer satisfaction.
---
Selected Answer: B
Amazon Bedrock agents are designed to help automate and manage complex workflows, such as orchestrating multiple tasks and interacting with other systems, making them particularly suitable for automating repetitive tasks. In the case of the retailer, this would help in efficiently processing customer support inquiries and responding to them quickly.
---
Selected Answer: B
Amazon Bedrock agents are specifically designed to automate tasks and orchestrate workflows
They can handle repetitive customer support inquiries efficiently
They can break down complex customer requests into smaller steps and execute them in sequence
This directly addresses the retailer's need to process thousands of inquiries quickly

</details>

---

## Question 100: AIF-C01-ET-Q100
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which option is a benefit of ongoing pre-training when fine-tuning a foundation model (FM)?

**Choices:**
- A) Helps decrease the model's complexity
- B) Improves model performance over time
- C) Decreases the training time requirement
- D) Optimizes model inference time

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Ongoing pre-training when fine-tuning a foundation model (FM) allows the model to continue learning and adapting to new data or evolving contexts. As new data becomes available, the model can be pre-trained on this additional data, improving its ability to handle specific tasks, making it more effective and accurate over time.
---
Selected Answer: B
The correct answer is B. Ongoing pre-training improves model performance over time by allowing the model to adapt to new data and tasks.
---
Selected Answer: B
Ongoing pre-training helps the model continuously learn and improve its performance over time. This is the whole point of fine-tuning a foundation model

</details>

---

## Question 101: AIF-C01-ET-Q101
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
What are tokens in the context of generative AI models?

**Choices:**
- A) Tokens are the basic units of input and output that a generative AI model operates on, representing words, subwords, or other linguistic units.
- B) Tokens are the mathematical representations of words or concepts used in generative AI models.
- C) Tokens are the pre-trained weights of a generative AI model that are fine-tuned for specific tasks.
- D) Tokens are the specific prompts or instructions given to a generative AI model to generate output.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A is correct
---
Selected Answer: A
In the context of generative AI models, tokens are the smallest units of text that the model processes. A token could represent an entire word, a subword, or even a single character, depending on how the model is tokenized. Tokens are the basic building blocks for both input and output in natural language processing (NLP) tasks, such as text generation or translation.

</details>

---

## Question 102: AIF-C01-ET-Q102
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to assess the costs that are associated with using a large language model (LLM) to generate inferences. The company wants to use Amazon Bedrock to build generative AI applications.
Which factor will drive the inference costs?

**Choices:**
- A) Number of tokens consumed
- B) Temperature value
- C) Amount of data used to train the LLM
- D) Total training time

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
In the context of using Amazon Bedrock and generative AI models, inference costs are typically driven by the number of tokens consumed during the input and output processing.

Number of tokens consumed refers to how many tokens (words, subwords, characters) the model processes during inference (both input and output). More tokens mean higher processing and hence higher costs.
---
Selected Answer: A
A. Number of tokens consumed. More tokens used = higher cost. 

All other affects training costs, not inference costs. Correct answer is A
---
Selected Answer: A
No. of tokens consumed while processing. Tokens are the basic units of input and output that a generative AI model operates on, representing words, subwords, or other linguistic units.

</details>

---

## Question 103: AIF-C01-ET-Q103
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is using Amazon SageMaker Studio notebooks to build and train ML models. The company stores the data in an Amazon S3 bucket. The company needs to manage the flow of data from Amazon S3 to SageMaker Studio notebooks.
Which solution will meet this requirement?

**Choices:**
- A) Use Amazon Inspector to monitor SageMaker Studio.
- B) Use Amazon Macie to monitor SageMaker Studio.
- C) Configure SageMaker to use a VPC with an S3 endpoint.
- D) Configure SageMaker to use S3 Glacier Deep Archive.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
To manage the flow of data from Amazon S3 to SageMaker Studio notebooks securely and efficiently, configuring SageMaker to use a VPC (Virtual Private Cloud) with an S3 endpoint is the best solution. This setup ensures that data transfer between SageMaker and S3 happens within the AWS network, without going through the public internet, which improves security and performance.

S3 VPC endpoint: An S3 VPC endpoint allows secure, private access to Amazon S3 from resources in your VPC, enabling SageMaker to securely retrieve data stored in S3 buckets without leaving the AWS network. This setup helps manage data flow efficiently.
---
Selected Answer: C
S3 gateway endpoint should be a default in every VPC.
---
Selected Answer: C
Deploy and run the Amazon SageMaker Studio on VPC and Connect to S3 using S3 Gateway endpoint.

</details>

---

## Question 104: AIF-C01-ET-Q104
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company has a foundation model (FM) that was customized by using Amazon Bedrock to answer customer queries about products. The company wants to validate the model's responses to new types of queries. The company needs to upload a new dataset that Amazon Bedrock can use for validation.
Which AWS service meets these requirements?

**Choices:**
- A) Amazon S3
- B) Amazon Elastic Block Store (Amazon EBS)
- C) Amazon Elastic File System (Amazon EFS)
- D) AWS Snowcone

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon S3 (Simple Storage Service) is the ideal solution for storing datasets that will be used by Amazon Bedrock for model validation. It is a scalable, durable, and secure storage service that is commonly used to store large datasets, including those used for machine learning model training, validation, and inference.

In the case of Amazon Bedrock, the company would typically upload the new validation dataset to an S3 bucket, which can then be accessed by Bedrock to validate the model's responses against the new data.
---
Selected Answer: A
Amazon S3 is the best option for storing (Object Storage) the datasets that Amazon Bedrock uses for customer queries.
---
Selected Answer: A
A is correct

</details>

---

## Question 105: AIF-C01-ET-Q105
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which prompting attack directly exposes the configured behavior of a large language model (LLM)?

**Choices:**
- A) Prompted persona switches
- B) Exploiting friendliness and trust
- C) Ignoring the prompt template
- D) Extracting the prompt template

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `83%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (83%). Contributor Answer: D.

Community Rationale & Discussion:
D. Extracting the prompt template
---
Selected Answer: D
Extracting the prompt template refers to a situation where the attacker tries to reveal or access the underlying structure or instructions used to configure the behavior of the large language model (LLM). This type of attack can expose how the model has been trained or how it responds to certain inputs, effectively giving the attacker insight into how the LLM has been directed to generate responses.

This type of attack could potentially lead to misuse, such as causing the model to behave in unintended ways, or even allow an attacker to manipulate the behavior of the model by crafting specific inputs based on the extracted prompt template.
---
Selected Answer: D
D. Extracting the prompt template

</details>

---

## Question 106: AIF-C01-ET-Q106
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company wants to use Amazon Bedrock. The company needs to review which security aspects the company is responsible for when using Amazon Bedrock.

Which security aspect will the company be responsible for?

**Choices:**
- A) Patching and updating the versions of Amazon Bedrock
- B) Protecting the infrastructure that hosts Amazon Bedrock
- C) Securing the company's data in transit and at rest
- D) Provisioning Amazon Bedrock within the company network

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
When using Amazon Bedrock, AWS is responsible for managing and securing the infrastructure that supports the service, including patching and updating the service itself. However, the company still has responsibility for securing its own data, both during transmission (in transit) and when it is stored (at rest). This includes ensuring that sensitive data is protected using encryption, access controls, and other security best practices as part of shared responsibility.
---
Selected Answer: C
Encrypting the company's data In-TRANSIT and At-REST.
---
Selected Answer: C
The correct answer is C. Customers are responsible for securing their own data when using AWS services.

</details>

---

## Question 107: AIF-C01-ET-Q107
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A social media company wants to use a large language model (LLM) to summarize messages. The company has chosen a few LLMs that are available on Amazon SageMaker JumpStart. The company wants to compare the generated output toxicity of these models.

Which strategy gives the company the ability to evaluate the LLMs with the LEAST operational overhead?

**Choices:**
- A) Crowd-sourced evaluation
- B) Automatic model evaluation
- C) Model evaluation with human workers
- D) Reinforcement learning from human feedback (RLHF)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Automatic model evaluation provides a way to assess the generated output of large language models (LLMs) with minimal operational overhead. This can be done by using pre-built toxicity evaluation tools or integrating models that can automatically detect and score toxicity in the generated text. This method saves time and resources compared to manual evaluation or more complex processes.
---
Selected Answer: B
The correct answer is B. Automatic model evaluation requires minimal human intervention, making it operationally lighter than human-based approaches.
---
Selected Answer: B
B. Automatic model evaluation

Explanation:
Using automatic model evaluation is the most efficient and low-overhead approach to evaluate the toxicity of the generated outputs from different LLMs. This strategy involves using automated tools or frameworks designed to assess the toxicity, bias, or other quality metrics of the model outputs, which minimizes operational overhead compared to manual methods.

</details>

---

## Question 108: AIF-C01-ET-Q108
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
A company is testing the security of a foundation model (FM). During testing, the company wants to get around the safety features and make harmful content.

Which security technique is this an example of?

**Choices:**
- A) Fuzzing training data to find vulnerabilities
- B) Denial of service (DoS)
- C) Penetration testing with authorization
- D) Jailbreak

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Jailbreaking refers to bypassing or disabling the security restrictions placed on a system—in this case, a foundation model (FM)—to make the system behave in unintended ways, often to produce harmful or malicious content. In the context of AI, jailbreaking typically involves manipulating the model's behavior or output by exploiting vulnerabilities in its design or safety features.
---
Selected Answer: D
The correct answer is D. A jailbreak is an attempt to bypass an AI model's built-in safety controls.
---
Selected Answer: D
D. Jailbreak

Explanation:
Jailbreaking is a technique used to bypass the safety features and restrictions of a foundation model (FM). The goal is to manipulate the model into generating harmful, inappropriate, or otherwise unintended content, despite the safeguards in place. This is often done to test the robustness of the model's safety mechanisms.

</details>

---

## Question 109: AIF-C01-ET-Q109
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to create a chatbot by using a foundation model (FM) on Amazon Bedrock. The FM needs to access encrypted data that is stored in an Amazon S3 bucket. The data is encrypted with Amazon S3 managed keys (SSE-S3).
The FM encounters a failure when attempting to access the S3 bucket data.
Which solution will meet these requirements?

**Choices:**
- A) Ensure that the role that Amazon Bedrock assumes has permission to decrypt data with the correct encryption key.
- B) Set the access permissions for the S3 buckets to allow public access to enable access over the internet.
- C) Use prompt engineering techniques to tell the model to look for information in Amazon S3.
- D) Ensure that the S3 data does not contain sensitive information.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon S3 managed keys (SSE-S3) encrypt your data using an Amazon-managed key, and to access this encrypted data, the IAM role that the service (in this case, Amazon Bedrock) assumes must have the appropriate permissions to decrypt the data. This includes permissions to read the object from the S3 bucket and decrypt it using the SSE-S3 encryption key.
---
Selected Answer: A
A: Ensure that the role that Amazon Bedrock assumes has permission to decrypt data with the correct encryption key.

Explanation:
When data in an Amazon S3 bucket is encrypted using SSE-S3 (Server-Side Encryption with Amazon S3 managed keys), the IAM role used by the application (in this case, Amazon Bedrock) must have permissions to access and decrypt the data. Assigning the correct permissions to the role ensures that the Foundation Model (FM) can access the encrypted data.
---
Selected Answer: A
>Permissions to decrypt your AWS KMS key for your data sources in Amazon S3
https://docs.aws.amazon.com/ja_jp/bedrock/latest/userguide/encryption-kb.html

</details>

---

## Question 110: AIF-C01-ET-Q110
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company needs to use Amazon SageMaker for model training and inference. The company must comply with regulatory requirements to run SageMaker jobs in an isolated environment without internet access.

Which solution will meet these requirements?

**Choices:**
- A) Run SageMaker training and inference by using SageMaker Experiments.
- B) Run SageMaker training and Inference by using network Isolation.
- C) Encrypt the data at rest by using encryption for SageMaker geospatial capabilities.
- D) Associate appropriate AWS Identity and Access Management (IAM) roles with the SageMaker jobs.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Network isolation allows Amazon SageMaker jobs (including training and inference) to run in a private, isolated environment without internet access, which is often required for compliance with regulatory requirements. This ensures that the SageMaker jobs do not have access to external networks, enhancing data security and privacy.
---
Selected Answer: B
B: Run SageMaker training and inference by using network isolation.

Explanation:
Network isolation in Amazon SageMaker ensures that training and inference jobs run in a fully isolated environment without internet access. When network isolation is enabled:

SageMaker jobs can only access resources within the specified Virtual Private Cloud (VPC).
Outbound internet access is disabled.
Data and models remain secure and compliant with regulatory requirements.
---
Selected Answer: B
The correct answer is B. Network isolation allows SageMaker to run without internet access, meeting regulatory requirements.

</details>

---

## Question 111: AIF-C01-ET-Q111
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use a large language model (LLM) to generate concise, feature-specific descriptions for the company’s products.

Which prompt engineering technique meets these requirements?

**Choices:**
- A) Create one prompt that covers all products. Edit the responses to make the responses more specific, concise, and tailored to each product.
- B) Create prompts for each product category that highlight the key features. Include the desired output format and length for each prompt response.
- C) Include a diverse range of product features in each prompt to generate creative and unique descriptions.
- D) Provide detailed, product-specific prompts to ensure precise and customized descriptions.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `75%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (75%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
This approach ensures that the prompts are tailored to specific product categories, guiding the LLM to generate concise, feature-specific descriptions. Including the desired output format and length further refines the model’s responses, making them consistent and aligned with the company’s requirements.
---
Selected Answer: B
Ensures concise, feature-focused, and structured responses.
---
Selected Answer: D
Option B: Creating prompts for each product category can help highlight key features, but it may still result in more generalized descriptions. This approach might not capture the unique aspects of each individual product as effectively as a detailed, product-specific prompt.

Option D: By providing detailed, product-specific prompts, you ensure that the descriptions are tailored to each product's unique features. This method minimizes the need for further editing and ensures that the output is concise and highly relevant.

In summary, while Option B is useful for generating category-specific descriptions, Option D offers a higher level of precision and customization for individual products.

</details>

---

## Question 112: AIF-C01-ET-Q112
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is developing an ML model to predict customer churn. The model performs well on the training dataset but does not accurately predict churn for new data.

Which solution will resolve this issue?

**Choices:**
- A) Decrease the regularization parameter to increase model complexity.
- B) Increase the regularization parameter to decrease model complexity.
- C) Add more features to the input data.
- D) Train the model for more epochs.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Reduces overfitting, improving generalization to new data.
---
Selected Answer: B
The correct answer is B. Increasing the regularization parameter reduces model complexity and prevents overfitting.
---
Selected Answer: B
The most effective solution to resolve overfitting and improve the model’s performance on new data is B. Increase the regularization parameter. This helps make the model simpler, reducing the likelihood of overfitting and improving its ability to generalize.

</details>

---

## Question 113: AIF-C01-ET-Q113
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to build an ML model by using Amazon SageMaker. The company needs to share and manage variables for model development across multiple teams.
Which SageMaker feature meets these requirements?

**Choices:**
- A) Amazon SageMaker Feature Store
- B) Amazon SageMaker Data Wrangler
- C) Amazon SageMaker Clarify
- D) Amazon SageMaker Model Cards

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Amazon SageMaker Feature Store ensures all teams have access to a centralized store of features, improving consistency and collaboration in ML workflows.
---
Selected Answer: A
Amazon SageMaker Feature Store is designed to store, manage, and share features (variables) for machine learning models across teams. It provides a centralized repository to track and manage features, ensuring consistency in feature usage across various models and teams. This is ideal when you need to collaborate on feature development and reuse them in multiple ML models.
---
Selected Answer: A
Amazon SageMaker Feature Store helps to create, store, share, manage features that are used in ML models.

</details>

---

## Question 114: AIF-C01-ET-Q114
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is implementing intelligent agents to provide conversational search experiences for its customers. The company needs a database service that will support storage and queries of embeddings from a generative AI model as vectors in the database.

Which AWS service will meet these requirements?

**Choices:**
- A) Amazon Athena
- B) Amazon Aurora PostgreSQL
- C) Amazon Redshift
- D) Amazon EMR

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Supports pgvector, a popular extension for storing and querying vector embeddings.
---
Selected Answer: B
The correct answer is B. Amazon Aurora PostgreSQL supports vector data types and can efficiently store and query embeddings.
---
Selected Answer: B
Amazon Aurora PostgreSQL is the best choice for a database service to store and query embeddings from generative AI models, as it supports vector storage and similarity searches through the pgvector extension.

</details>

---

## Question 115: AIF-C01-ET-Q115
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
A financial institution is building an AI solution to make loan approval decisions by using a foundation model (FM). For security and audit purposes, the company needs the AI solution's decisions to be explainable.

Which factor relates to the explainability of the AI solution's decisions?

**Choices:**
- A) Model complexity
- B) Training time
- C) Number of hyperparameters
- D) Deployment time

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
More complex models are harder to interpret; simpler models improve explainability.
---
Selected Answer: A
The correct answer is A. Model complexity directly affects how interpretable and explainable AI decisions are.
---
Selected Answer: A
Model complexity is the most important factor when considering the explainability of the AI solution's decisions, as simpler models with fewer parameters and layers are typically easier to explain and interpret.

</details>

---

## Question 116: AIF-C01-ET-Q116
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
An ML research team develops custom ML models. The model artifacts are shared with other teams for integration into products and services. The ML team retains the model training code and data. The ML team wants to build a mechanism that the ML team can use to audit models.

Which solution should the ML team use when publishing the custom ML models?

**Choices:**
- A) Create documents with the relevant information. Store the documents in Amazon S3.
- B) Use AWS AI Service Cards for transparency and understanding models.
- C) Create Amazon SageMaker Model Cards with intended uses and training and inference details.
- D) Create model training scripts. Commit the model training scripts to a Git repository.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
C.

Create Amazon SageMaker Model Cards with intended uses and training and inference details.
---
Selected Answer: C
Amazon SageMaker Model Cards are designed to provide transparency and detailed information about a model's intended uses, training process, data, and performance. They are specifically designed for auditing models and making them more interpretable, which is exactly what the ML team needs. Model cards help document key details about the model, including how it was trained, its intended use cases, and any potential risks associated with its use. This solution supports effective auditing and provides a comprehensive, structured format for tracking important model information.
---
Selected Answer: C
Amazon SageMaker Model Cards: These provide a standardized way to document important information about ML models, including:
Model purpose and intended use cases
Training data and methodology
Evaluation metrics and results
Ethical considerations and limitations
Bias analysis
Version history This comprehensive documentation facilitates auditing by providing a clear record of how the model was developed, evaluated, and intended to be used. It also promotes transparency and accountability.
B. Use AWS AI Service Cards for transparency and understanding models:
AWS AI Service Cards are designed for pre-built AI services provided by AWS, not for custom ML models developed by a team. They are not applicable for this use case.

</details>

---

## Question 117: AIF-C01-ET-Q117
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A software company builds tools for customers. The company wants to use AI to increase software development productivity.

Which solution will meet these requirements?

**Choices:**
- A) Use a binary classification model to generate code reviews.
- B) Install code recommendation software in the company's developer tools.
- C) Install a code forecasting tool to predict potential code issues.
- D) Use a natural language processing (NLP) tool to generate code.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `86%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (86%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
B. Install code recommendation software in the company's developer tools: Code recommendation tools can be helpful, but they are often focused on suggesting improvements or alternatives to existing code rather than generating new code from scratch. While useful, it may not provide the same level of productivity boost as an NLP-based code generation tool.
---
Selected Answer: B
As the company wants to increase software development productivity - B is the right one. i.e. Amazon Q Developer
---
Selected Answer: D
D. Use a natural language processing (NLP) tool to generate code is likely a more impactful solution for increasing productivity. Code recommendations are helpful, but direct code generation from natural language can automate larger portions of the coding process.

</details>

---

## Question 118: AIF-C01-ET-Q118
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A retail store wants to predict the demand for a specific product for the next few weeks by using the Amazon SageMaker DeepAR forecasting algorithm.

Which type of data will meet this requirement?

**Choices:**
- A) Text data
- B) Image data
- C) Time series data
- D) Binary data

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Explanation:
The DeepAR forecasting algorithm in Amazon SageMaker is specifically designed for time series forecasting tasks. Time series data consists of observations collected over time, often at regular intervals (e.g., daily, weekly, or monthly). This data is typically used to forecast future values based on historical trends and patterns.

In the context of predicting the demand for a product, time series data would include past sales figures, inventory levels, and other relevant metrics over a period of time. The DeepAR algorithm can analyze this historical data and generate forecasts for future demand.
---
Selected Answer: C
DeepAR and Time Series Data:

The Amazon SageMaker DeepAR forecasting algorithm is specifically designed to handle time series data for forecasting tasks.
Time series data consists of observations collected at regular intervals over time (e.g., daily sales of a product).
DeepAR uses historical patterns in this data to predict future values.
Why Time Series Data is Required:

To predict product demand, the model needs past sales data (e.g., daily, weekly, or monthly), which is inherently time series data.
---
Selected Answer: C
The correct answer is C. DeepAR is specifically designed for processing and forecasting time series data.

</details>

---

## Question 119: AIF-C01-ET-Q119
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A large retail bank wants to develop an ML system to help the risk management team decide on loan allocations for different demographics.

What must the bank do to develop an unbiased ML model?

**Choices:**
- A) Reduce the size of the training dataset.
- B) Ensure that the ML model predictions are consistent with historical results.
- C) Create a different ML model for each demographic group.
- D) Measure class imbalance on the training dataset. Adapt the training process accordingly.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Measure class imbalance on the training dataset. Adapt the training process accordingly.
---
Selected Answer: D
When developing an unbiased machine learning (ML) model, it's crucial to address issues like class imbalance in the training data. Class imbalance refers to the situation where certain classes (or demographic groups, in this case) are underrepresented compared to others. If class imbalance exists, the model might learn to favor the majority class and perform poorly on minority classes, leading to biased predictions.
---
Selected Answer: D
D. Measure class imbalance on the training dataset. Adapt the training process accordingly: This is the correct answer. Class imbalance occurs when one class (e.g., loan approval) is significantly more represented in the training data than another. This can lead to biased models that favor the majority class. Measuring and addressing class imbalance (e.g., through resampling or weighting techniques) is crucial for building fair models.

Why not B?
B. Ensure that the ML model predictions are consistent with historical results: If historical results reflect existing biases in lending practices, ensuring consistency with them will simply perpetuate those biases. This is the opposite of what is desired.

</details>

---

## Question 120: AIF-C01-ET-Q120
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
Which prompting technique can protect against prompt injection attacks?

**Choices:**
- A) Adversarial prompting
- B) Zero-shot prompting
- C) Least-to-most prompting
- D) Chain-of-thought prompting

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Adversarial prompting is a technique designed to prevent prompt injection attacks, which are attempts to manipulate a model's behavior by injecting harmful or misleading instructions within the input prompt. This technique involves using carefully crafted prompts that make it harder for the model to misinterpret or be misled by unwanted inputs.

Adversarial prompting can include various methods to detect, block, or neutralize harmful inputs. It might involve incorporating security mechanisms in the prompt itself, such as validating or sanitizing the input or applying certain constraints on the model's output to mitigate the risk of prompt injections.
---
Selected Answer: A
Adversarial Prompting:

This technique involves testing a model with deliberately crafted adversarial prompts to identify vulnerabilities to injection attacks.
By simulating potential attacks during development, adversarial prompting helps design robust prompts and refine the model's behavior to resist manipulation.
This approach allows developers to identify weaknesses in the model's response to malicious inputs and implement mitigations.
---
Selected Answer: A
The correct answer is A. Adversarial prompting helps models recognize and defend against malicious inputs.

</details>

---

## Question 121: AIF-C01-ET-Q121
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company has fine-tuned a large language model (LLM) to answer questions for a help desk. The company wants to determine if the fine-tuning has enhanced the model's accuracy.

Which metric should the company use for the evaluation?

**Choices:**
- A) Precision
- B) Time to first token
- C) F1 score
- D) Word error rate

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
The F1 score is a widely used metric for evaluating the accuracy of a model, especially in classification tasks where there is an imbalance between precision and recall. It is the harmonic mean of precision and recall, providing a balanced measure of the model’s ability to correctly identify relevant information while minimizing false positives and false negatives.

In the context of a help desk model, you want to measure both the precision (correctness of answers) and recall (how well the model retrieves the relevant information). The F1 score helps you achieve a balanced view of these two metrics, making it a good choice for evaluating model accuracy in a fine-tuned large language model (LLM) for answering questions.
---
Selected Answer: C
C: F1 score

Explanation:
The F1 score is a balanced metric that combines precision and recall to evaluate the accuracy of a model, particularly in scenarios like question-answering, where both correctness (precision) and completeness (recall) matter. The F1 score is particularly useful when there is an uneven distribution of classes or when the model's ability to retrieve relevant and accurate answers is being assessed.
---
Selected Answer: C
The correct answer is C. F1 score combines precision and recall, making it ideal for question-answering evaluation.

</details>

---

## Question 122: AIF-C01-ET-Q122
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company is using Retrieval Augmented Generation (RAG) with Amazon Bedrock and Stable Diffusion to generate product images based on text descriptions. The results are often random and lack specific details. The company wants to increase the specificity of the generated images.

Which solution meets these requirements?

**Choices:**
- A) Increase the number of generation steps.
- B) Use the MASK_IMAGE_BLACK mask source option.
- C) Increase the classifier-free guidance (CFG) scale.
- D) Increase the prompt strength.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `57%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (57%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: D
Explicação:
A força do prompt (prompt strength) se refere ao grau de influência que o texto fornecido tem sobre a imagem gerada.

Quando a força do prompt é baixa, o modelo (como o Stable Diffusion) pode gerar imagens mais abstratas ou genéricas.

Ao aumentar a força do prompt, você orienta o modelo a seguir mais fielmente os detalhes fornecidos no texto, gerando imagens mais específicas e controladas — o que é justamente o que a empresa deseja.
---
Selected Answer: D
In Retrieval Augmented Generation (RAG) with Stable Diffusion, the prompt strength determines how closely the generated image aligns with the given text description. By increasing prompt strength, the model places more emphasis on the input prompt, making the output more specific and detailed, which directly addresses the company's concern about random and lacking specific details in generated images.
---
Selected Answer: C
Classifier-Free Guidance (CFG) is a technique used in generative models, especially in image generation tasks, that helps guide the generation process toward more specific or desired outputs. By increasing the CFG scale, the model's generated image becomes more closely aligned with the given text prompt, improving the specificity and control over the details in the generated image.

A higher CFG scale ensures that the model generates images that are more faithful to the prompt by reducing randomness and making the generation more deterministic. This technique allows for more control over the image generation process, making it suitable for use cases like generating product images from text descriptions, where specific details are important.

</details>

---

## Question 123: AIF-C01-ET-Q123
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to implement a large language model (LLM) based chatbot to provide customer service agents with real-time contextual responses to customers' inquiries. The company will use the company's policies as the knowledge base.

Which solution will meet these requirements MOST cost-effectively?

**Choices:**
- A) Retrain the LLM on the company policy data.
- B) Fine-tune the LLM on the company policy data.
- C) Implement Retrieval Augmented Generation (RAG) for in-context responses.
- D) Use pre-training and data augmentation on the company policy data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Retrieval Augmented Generation (RAG) is a technique that combines the power of pre-trained large language models (LLMs) with a retrieval mechanism to fetch relevant documents or data (like the company’s policies) and incorporate them into the response generation process. This approach allows the model to produce accurate, context-aware responses without the need to retrain or fine-tune the model extensively on the entire policy dataset, making it a cost-effective and efficient solution.
---
Selected Answer: C
RAG provides most cost-effective solution
---
Selected Answer: C
The correct answer is C. RAG allows direct use of policy documents without expensive model training.

</details>

---

## Question 124: AIF-C01-ET-Q124
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to create a new solution by using AWS Glue. The company has minimal programming experience with AWS Glue.

Which AWS service can help the company use AWS Glue?

**Choices:**
- A) Amazon Q Developer
- B) AWS Config
- C) Amazon Personalize
- D) Amazon Comprehend

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Amazon Q Developer is a service that helps users build and deploy machine learning (ML) models, and it includes tools that can assist with AWS Glue-related tasks. It can guide users through processes like data integration, transformation, and automation without requiring deep programming experience. It can simplify the use of AWS Glue by helping manage data flows and model development.
---
Selected Answer: A
The correct answer is A. Amazon Q Developer helps users work with AWS services through natural language assistance.
---
Selected Answer: A
Amazon Q Developer (Option A) is the service that would most help a company with minimal programming experience in using AWS Glue. It simplifies the process of building and managing data workflows, making it easier to use Glue without needing deep programming expertise.

</details>

---

## Question 125: AIF-C01-ET-Q125
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A pharmaceutical company wants to analyze user reviews of new medications and provide a concise overview for each medication.

Which solution meets these requirements?

**Choices:**
- A) Create a time-series forecasting model to analyze the medication reviews by using Amazon Personalize.
- B) Create medication review summaries by using Amazon Bedrock large language models (LLMs).
- C) Create a classification model that categorizes medications into different groups by using Amazon SageMaker.
- D) Create medication review summaries by using Amazon Rekognition.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Best suited for summarizing large volumes of text, like user reviews.
---
Selected Answer: B
The correct answer is B. LLMs are specifically designed for text analysis and summarization tasks.
---
Selected Answer: B
Using Amazon Bedrock’s large language models (LLMs) is the ideal solution for generating concise summaries of user reviews of new medications.

</details>

---

## Question 126: AIF-C01-ET-Q126
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to build a lead prioritization application for its employees to contact potential customers. The application must give employees the ability to view and adjust the weights assigned to different variables in the model based on domain knowledge and expertise.

Which ML model type meets these requirements?

**Choices:**
- A) Logistic regression model
- B) Deep learning model built on principal components
- C) K-nearest neighbors (k-NN) model
- D) Neural network

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Provides interpretable weights that can be manually adjusted based on domain expertise.
---
Selected Answer: A
A: Logistic regression model

Explanation:
A logistic regression model is interpretable and allows direct adjustment of the weights assigned to different variables (features). This aligns with the requirement for employees to view and modify the weights based on their domain knowledge and expertise. Logistic regression provides a clear relationship between input features and output predictions, making it ideal for use cases that demand transparency and control.
---
Selected Answer: A
The correct answer is A. Logistic regression models allow for easy interpretation and adjustment of weights.

</details>

---

## Question 128: AIF-C01-ET-Q128
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which strategy will determine if a foundation model (FM) effectively meets business objectives?

**Choices:**
- A) Evaluate the model's performance on benchmark datasets.
- B) Analyze the model's architecture and hyperparameters.
- C) Assess the model's alignment with specific use cases.
- D) Measure the computational resources required for model deployment.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Directly addresses how well the model meets business needs and objectives.
---
Selected Answer: C
C: Assess the model's alignment with specific use cases.

Explanation:
To determine if a foundation model (FM) effectively meets business objectives, it is crucial to evaluate how well the model aligns with the specific use cases and objectives of the business. This involves testing the model's performance on real-world tasks and ensuring that it addresses the desired outcomes, such as accuracy, relevance, and user satisfaction, in the context of the business problem.

Why not the other options?
A: Evaluate the model's performance on benchmark datasets:
While benchmarking provides useful insights into the model's capabilities, it does not guarantee alignment with business-specific needs or objectives.
---
Selected Answer: C
The correct answer is C. Assessing use case alignment determines business objective achievement.

</details>

---

## Question 129: AIF-C01-ET-Q129
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company needs to train an ML model to classify images of different types of animals. The company has a large dataset of labeled images and will not label more data.

Which type of learning should the company use to train the model?

**Choices:**
- A) Supervised learning
- B) Unsupervised learning
- C) Reinforcement learning
- D) Active learning

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Best for training a model with a labeled dataset, like the company's labeled images.
---
Selected Answer: A
A: Supervised learning

Explanation:
Supervised learning is the appropriate method when a dataset of labeled examples is available, as it involves training a model using input-output pairs. In this case, the labeled images of animals (input) and their corresponding categories (output) make supervised learning the ideal approach. The model learns from these examples to classify new, unseen images into the correct categories.

Why not the other options?
B: Unsupervised learning:
Unsupervised learning does not use labeled data and is typically used for clustering or pattern discovery. It is not suitable for this classification task, which requires labeled data.
---
Selected Answer: A
A. Supervised learning

Explanation: Since the company has a large dataset of labeled images, supervised learning is the appropriate choice. In supervised learning, a model is trained on a labeled dataset, where the input data (images) is paired with corresponding labels (the types of animals). This approach allows the model to learn from the labeled data and make predictions on new, unseen data.

</details>

---

## Question 130: AIF-C01-ET-Q130
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
Which phase of the ML lifecycle determines compliance and regulatory requirements?

**Choices:**
- A) Feature engineering
- B) Model training
- C) Data collection
- D) Business goal identification

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `73%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (73%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Explainability helps with understanding the cause of a prediction, auditing, and meeting regulatory requirements. Explainability is part of Operational excellence pillar best practices which rolls up to the Business goal identification lifecycle phase of the Well-Architected machine learning design principles.
https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mloe-02.html
---
Selected Answer: D
The business goal identification phase is crucial for determining compliance and regulatory requirements because it establishes the scope of the model’s application, including legal constraints, privacy regulations (like GDPR or HIPAA), and ethical considerations. These requirements are often aligned with the business objectives at the start of the project to ensure the solution remains compliant.
---
Selected Answer: D
A clear problem definition keeps the entire ML team aligned on what success looks like. However, this step is far from straightforward. For example, setting appropriate risk thresholds for fraud detection involves balancing regulatory requirements (like GDPR, AML, and KYC) with business priorities and operational constraints.

</details>

---

## Question 131: AIF-C01-ET-Q131
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A food service company wants to develop an ML model to help decrease daily food waste and increase sales revenue. The company needs to continuously improve the model's accuracy.

Which solution meets these requirements?

**Choices:**
- A) Use Amazon SageMaker and iterate with newer data.
- B) Use Amazon Personalize and iterate with historical data.
- C) Use Amazon CloudWatch to analyze customer orders.
- D) Use Amazon Rekognition to optimize the model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Provides tools for building, training, and iterating on ML models using newer data to continuously improve accuracy.
---
Selected Answer: A
The correct answer is A. Using Amazon SageMaker allows for continuous iteration and improvement of the model's accuracy with newer data.
---
Selected Answer: A
A. Use Amazon SageMaker and iterate with newer data.

Explanation:

To meet the requirements of decreasing food waste and increasing sales revenue, the company needs a machine learning model that can continuously improve and adjust based on new data.

Amazon SageMaker is a fully managed service that allows companies to build, train, and deploy machine learning models at scale. By iterating with newer data, the model can be continuously updated to reflect changing patterns in customer behavior, demand, and food consumption, leading to more accurate predictions over time.

</details>

---

## Question 132: AIF-C01-ET-Q132
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company has developed an ML model to predict real estate sale prices. The company wants to deploy the model to make predictions without managing servers or infrastructure.

Which solution meets these requirements?

**Choices:**
- A) Deploy the model on an Amazon EC2 instance.
- B) Deploy the model on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster.
- C) Deploy the model by using Amazon CloudFront with an Amazon S3 integration.
- D) Deploy the model by using an Amazon SageMaker endpoint.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
Selected Answer: D
Fully managed service for deploying ML models, allowing predictions without managing infrastructure.
---
Selected Answer: D
The correct answer is D. Deploying the model using an Amazon SageMaker endpoint allows for serverless predictions.
---
Selected Answer: D
D. Deploy the model by using an Amazon SageMaker endpoint.

Explanation:

Amazon SageMaker is a fully managed service that enables you to quickly build, train, and deploy machine learning models at scale. Deploying a model using an Amazon SageMaker endpoint allows the company to make predictions without needing to manage servers or infrastructure. SageMaker automatically handles the provisioning of resources, scaling, and maintenance, making it an ideal solution for production-grade ML deployments.

</details>

---

## Question 133: AIF-C01-ET-Q133
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to use generative AI to increase developer productivity and software development. The company wants to use Amazon Q Developer.
What can Amazon Q Developer do to help the company meet these requirements?

**Choices:**
- A) Create software snippets, reference tracking, and open source license tracking.
- B) Run an application without provisioning or managing servers.
- C) Enable voice commands for coding and providing natural language search.
- D) Convert audio files to text documents by using ML models.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `67%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (67%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: U
Explicação:
O Amazon Q Developer é um assistente de IA generativa da AWS projetado para desenvolvedores. Ele pode:

Gerar trechos de código (snippets) com base em perguntas feitas em linguagem natural.

Fornecer explicações sobre o código, com rastreamento de referências a documentação.

Identificar e rastrear licenças de código aberto, ajudando a evitar problemas legais ao reutilizar trechos de código.

As demais opções estão incorretas:

B se refere ao AWS Lambda, que executa código sem provisionar servidores.

C mistura comandos de voz e busca em linguagem natural, algo mais associado ao Amazon Lex ou Alexa, não ao Q Developer.

D descreve serviços como Amazon Transcribe, que convertem áudio em texto.
---
Selected Answer: U
Explicação:
Quando uma VPC não pode ter acesso à internet, mas ainda precisa se comunicar com serviços da AWS como o Amazon Bedrock, a solução ideal é o AWS PrivateLink.

O PrivateLink permite o acesso privado e seguro a serviços da AWS (como Bedrock, S3, etc.) sem sair da rede da AWS e sem usar a internet pública.

Isso é essencial em ambientes regulados, como instituições financeiras, onde há requisitos rígidos de conformidade e segurança.
---
Selected Answer: U
xplicação: O Amazon Q Developer é um assistente de IA generativa da AWS focado em aumentar a produtividade de desenvolvedores. Ele ajuda em diversas tarefas ligadas ao esenvolvimento de software, incluindo: Geração de código (snippets) com base em prompts em linguagem natural . Rastreamento de referências de onde os trechos de código vêm (para confiabilidade e entendimento) Verificação de licenças de código aberto, ajudando a evitar violações de compliance . Explicação de código, testes, depuração e integração com IDEs como VS Code.

</details>

---

## Question 134: AIF-C01-ET-Q134
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to develop an AI application to help its employees check open customer claims, identify details for a specific claim, and access documents for a claim.

Which solution meets these requirements?

**Choices:**
- A) Use Agents for Amazon Bedrock with Amazon Fraud Detector to build the application.
- B) Use Agents for Amazon Bedrock with Amazon Bedrock knowledge bases to build the application.
- C) Use Amazon Personalize with Amazon Bedrock knowledge bases to build the application.
- D) Use Amazon SageMaker to build the application by training a new ML model.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Amazon Bedrock agents and knowledge bases are designed to help build AI-powered applications that can understand and access specific claim details and documents.
---
Selected Answer: B
B. Use Agents for Amazon Bedrock with Amazon Bedrock knowledge bases to build the application: This is the correct answer. Agents for Bedrock can connect to and interact with various data sources, including knowledge bases. Using a Bedrock knowledge base (which could be populated with claim data and documents) allows the agent to retrieve the necessary information to fulfill user requests related to claims.
---
Selected Answer: B
The correct answer is B. Using Agents for Amazon Bedrock with Amazon Bedrock knowledge bases allows employees to check open customer claims, identify details, and access related documents effectively.

</details>

---

## Question 135: AIF-C01-ET-Q135
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A manufacturing company uses AI to inspect products and find any damages or defects.

Which type of AI application is the company using?

**Choices:**
- A) Recommendation system
- B) Natural language processing (NLP)
- C) Computer vision
- D) Image processing

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
Selected Answer: C
Involves analyzing and interpreting visual information from the world, perfect for inspecting products and detecting defects.
---
Selected Answer: C
Computer vision is a type of AI application that enables machines to interpret and analyze visual data from the real world, such as images and videos. In this scenario, the company is using AI to inspect products for damages or defects, which involves analyzing visual inputs—making computer vision the appropriate answer.
---
Selected Answer: C
The correct answer is C. Computer vision is used for visual inspection tasks.

</details>

---

## Question 136: AIF-C01-ET-Q136
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to create an ML model to predict customer satisfaction. The company needs fully automated model tuning.

Which AWS service meets these requirements?

**Choices:**
- A) Amazon Personalize
- B) Amazon SageMaker
- C) Amazon Athena
- D) Amazon Comprehend

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
Offers automatic model tuning through SageMaker Autopilot and SageMaker Hyperparameter Optimization, providing fully automated model tuning.
---
Selected Answer: B
The correct answer is B. Amazon SageMaker provides fully automated model tuning capabilities through its hyperparameter optimization features.
---
Selected Answer: B
B. Amazon SageMaker

Explanation:

Amazon SageMaker is a fully managed service that provides tools to build, train, and deploy machine learning models. It includes SageMaker Autopilot, which automates the machine learning model development process, including model tuning. This feature helps users create and optimize models with minimal manual intervention, making it ideal for fully automated model tuning.

</details>

---

## Question 137: AIF-C01-ET-Q137
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which technique can a company use to lower bias and toxicity in generative AI applications during the post-processing ML lifecycle?

**Choices:**
- A) Human-in-the-loop
- B) Data augmentation
- C) Feature engineering
- D) Adversarial training

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Involves human oversight during the post-processing phase to review and mitigate biased or toxic outputs generated by AI models.
---
Selected Answer: A
The question specifies reducing bias and toxicity during post-processing of generated content.

A. Human-in-the-loop: This is the correct answer. Human review of generated outputs allows for filtering or modification of biased or toxic content after generation.

B. Data augmentation: This occurs during training, modifying the training data itself, not the generated outputs.

C. Feature engineering: Also a training phase activity, focusing on input features, not generated content.

D. Adversarial training: Used during training to improve robustness, not to filter post-generation content
---
Selected Answer: A
The correct answer is A. Human-in-the-loop review provides direct oversight for reducing bias and toxicity.

</details>

---

## Question 138: AIF-C01-ET-Q138
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A bank has fine-tuned a large language model (LLM) to expedite the loan approval process. During an external audit of the model, the company discovered that the model was approving loans at a faster pace for a specific demographic than for other demographics.

How should the bank fix this issue MOST cost-effectively?

**Choices:**
- A) Include more diverse training data. Fine-tune the model again by using the new data.
- B) Use Retrieval Augmented Generation (RAG) with the fine-tuned model.
- C) Use AWS Trusted Advisor checks to eliminate bias.
- D) Pre-train a new LLM with more diverse training data.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
The model's bias likely stems from unrepresentative training data. Adding more diverse data and fine-tuning the model is the most cost-effective solution to address bias.
---
Selected Answer: A
The correct answer is A. Fine-tuning with more diverse data is the most cost-effective bias mitigation approach.
---
Selected Answer: A
A. Include more diverse training data. Fine-tune the model again by using the new data.

Explanation:

The issue of bias in the loan approval model likely arises from the model being trained on data that does not sufficiently represent all demographics. To address this, the bank should augment the training dataset with more diverse data to ensure that the model can learn to make fair and equitable decisions across different demographics. After incorporating the more diverse training data, the bank can fine-tune the model again to adjust its behavior and reduce any biases identified during the audit.

</details>

---

## Question 140: AIF-C01-ET-Q140
**Domain 3:** Applications of Foundation Models  

**Question:**  
A company needs to log all requests made to its Amazon Bedrock API. The company must retain the logs securely for 5 years at the lowest possible cost.

Which combination of AWS service and storage class meets these requirements? (Choose two.)

**Choices:**
- A) AWS CloudTrail
- B) Amazon CloudWatch
- C) AWS Audit Manager
- D) Amazon S3 Intelligent-Tiering
- E) Amazon S3 Standard

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `AD`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: AD (100%). Contributor Answer: AD.

Community Rationale & Discussion:
Selected Answer: AD
A. AWS CloudTrail Essential for logging API requests to Amazon Bedrock and other AWS services.
D. Amazon S3 Intelligent-Tiering This storage class automatically moves data between two access tiers (frequent and infrequent) based on access patterns. This is ideal when you expect to access the logs occasionally but need to retain them securely and at a lower cost over time.
---
Selected Answer: AD
A: AWS CloudTrail
D: Amazon S3 Intelligent-Tiering

Explanation:
A: AWS CloudTrail:
AWS CloudTrail records all API calls made to AWS services, including Amazon Bedrock, and provides detailed logs of these interactions. It is the primary service for tracking and logging API requests.
D: Amazon S3 Intelligent-Tiering:
Amazon S3 Intelligent-Tiering is a cost-effective storage class designed to optimize costs for data with unknown or changing access patterns. It automatically moves data between frequent and infrequent access tiers based on usage, ensuring cost efficiency while meeting long-term retention requirements.
---
Selected Answer: AD
To log all requests to the Amazon Bedrock API and retain them securely for 5 years at the lowest possible cost, use AWS CloudTrail for comprehensive logging and Amazon S3 Intelligent-Tiering for cost-effective, long-term storage.

</details>

---

## Question 141: AIF-C01-ET-Q141
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
An ecommerce company wants to improve search engine recommendations by customizing the results for each user of the company’s ecommerce platform.

Which AWS service meets these requirements?

**Choices:**
- A) Amazon Personalize
- B) Amazon Kendra
- C) Amazon Rekognition
- D) Amazon Transcribe

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A fully managed service that allows companies to build personalized recommendation systems for individual users. It’s perfect for customizing search engine results based on user preferences and behaviors.
---
Selected Answer: A
Amazon Personalize re-ranks search results based on:
User's past behavior
Metadata about items
Metadata about users
---
Selected Answer: A
Amazon Personalize is a fully managed machine learning service that uses your data to generate item recommendations for your users. It can also generate user segments based on the users' affinity for certain items or item metadata.

https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html

</details>

---

## Question 142: AIF-C01-ET-Q142
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
A hospital is developing an AI system to assist doctors in diagnosing diseases based on patient records and medical images. To comply with regulations, the sensitive patient data must not leave the country the data is located in.

Which data governance strategy will ensure compliance and protect patient privacy?

**Choices:**
- A) Data residency
- B) Data quality
- C) Data discoverability
- D) Data enrichment

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Ensures that sensitive data remains within the geographic boundaries of a specific country or region, helping to comply with data sovereignty and privacy regulations (such as HIPAA or GDPR).
---
Selected Answer: A
Data residency (residencia de datos) es una estrategia de gobernanza de datos que:

✔ Asegura que los datos permanezcan en una ubicación geográfica específica, según las regulaciones del país.
✔ Cumple con normativas de privacidad y seguridad como GDPR en Europa o HIPAA en EE.UU.
✔ Restringe el almacenamiento y procesamiento de datos fuera del país, evitando transferencias no permitidas.

En este caso, un hospital que maneja datos sensibles de pacientes debe asegurarse de que la información médica no se almacene ni procese fuera del país, lo que hace que Data residency sea la mejor estrategia.
---
Selected Answer: A
Only A talking about the data how to store

</details>

---

## Question 143: AIF-C01-ET-Q143
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company needs to monitor the performance of its ML systems by using a highly scalable AWS service.

Which AWS service meets these requirements?

**Choices:**
- A) Amazon CloudWatch
- B) AWS CloudTrail
- C) AWS Trusted Advisor
- D) AWS Config

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
highly scalable monitoring service that tracks and provides performance metrics for AWS resources, including machine learning systems. It allows for real-time monitoring and alerting.
---
Selected Answer: A
CloudWatch provides scalable monitoring for ML systems

</details>

---

## Question 144: AIF-C01-ET-Q144
**Domain 3:** Applications of Foundation Models  

**Question:**  
A financial institution is using Amazon Bedrock to develop an AI application. The application is hosted in a VPC. To meet regulatory compliance standards, the VPC is not allowed access to any internet traffic.
Which AWS service or feature will meet these requirements?

**Choices:**
- A) AWS PrivateLink
- B) Amazon Macie
- C) Amazon CloudFront
- D) Internet gateway

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
Privatelink allows secure, private connectivity to aws services.
---
Selected Answer: A
Answer is A, but this is a question for Solutions Architect exam..
---
Selected Answer: A
The correct answer is:

A. AWS PrivateLink

Explanation:
Since the VPC does not have internet access, the financial institution must use a private connectivity option to access Amazon Bedrock, which is a managed AI service. AWS PrivateLink allows private communication between VPCs and AWS services without requiring internet access, making it the best option for regulatory compliance.

Amazon Macie (B): A data security service that helps identify sensitive data but does not provide private connectivity.
Amazon CloudFront (C): A CDN service that optimizes content delivery but still requires internet access.
Internet Gateway (D): This would provide internet access, which is explicitly not allowed per the requirements.
Thus, AWS PrivateLink is the right solution to enable secure, private access to Amazon Bedrock within the VPC.

</details>

---

## Question 145: AIF-C01-ET-Q145
**Domain 3:** Applications of Foundation Models  

**Question:**  
An AI practitioner is developing a prompt for an Amazon Titan model. The model is hosted on Amazon Bedrock. The AI practitioner is using the model to solve numerical reasoning challenges. The AI practitioner adds the following phrase to the end of the prompt: “Ask the model to show its work by explaining its reasoning step by step.”

Which prompt engineering technique is the AI practitioner using?

**Choices:**
- A) Chain-of-thought prompting
- B) Prompt injection
- C) Few-shot prompting
- D) Prompt templating

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Chain-of-thought prompting

step by step
---
Selected Answer: A
This technique encourages the model to reason through a problem step by step, which is exactly what the AI practitioner is doing by asking the model to "show its work by explaining its reasoning step by step."
---
Selected Answer: A
CoT prompting involves structuring prompts so that the LLM breaks down complex problems into a series of logical, intermediate steps, similar to how a human would when thinking through a problem.

</details>

---

## Question 146: AIF-C01-ET-Q146
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
Which AWS service makes foundation models (FMs) available to help users build and scale generative AI applications?

**Choices:**
- A) Amazon Q Developer
- B) Amazon Bedrock
- C) Amazon Kendra
- D) Amazon Comprehend

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (80%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
mazon Bedrock is a fully managed service that provides access to foundation models (FMs) from leading AI companies, allowing users to build and scale generative AI applications.
---
Selected Answer: B
The tagline of Amazon Bedrock says "The easiest way to build and scale generative AI applications with foundation models" https://aws.amazon.com/bedrock/?sec=aiapps&pos=2
---
Selected Answer: B
Amazon Bedrock is a fully managed service that provides access to a variety of high-performing foundation models from leading AI companies and Amazon itself. 
It offers a single API for accessing different foundation models, allowing for easy experimentation and integration into applications.

</details>

---

## Question 147: AIF-C01-ET-Q147
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company is building a mobile app for users who have a visual impairment. The app must be able to hear what users say and provide voice responses.

Which solution will meet these requirements?

**Choices:**
- A) Use a deep learning neural network to perform speech recognition.
- B) Build ML models to search for patterns in numeric data.
- C) Use generative AI summarization to generate human-like text.
- D) Build custom models for image classification and recognition.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `A`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: A (100%). Contributor Answer: A.

Community Rationale & Discussion:
Selected Answer: A
A. Use a deep learning neural network to perform speech recognition.

This type of solution is similar to voice assistants like Amazon Alexa or Apple's Siri, which use deep learning for:

Converting speech to text (speech recognition)
Processing the request
Converting response text back to speech (text-to-speech)
---
Selected Answer: A
Deep learning neural networks are commonly used for speech recognition tasks, converting spoken language into text, which can then be processed to provide appropriate voice responses.
---
Selected Answer: A
A. Other options don't meet the requirement of speech recognition and voice response

</details>

---

## Question 148: AIF-C01-ET-Q148
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to enhance response quality for a large language model (LLM) for complex problem-solving tasks. The tasks require detailed reasoning and a step-by-step explanation process.

Which prompt engineering technique meets these requirements?

**Choices:**
- A) Few-shot prompting
- B) Zero-shot prompting
- C) Directional stimulus prompting
- D) Chain-of-thought prompting

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Chain-of-thought prompting
---
Selected Answer: D
This technique encourages the model to explain its reasoning step by step, which is ideal for tasks that require detailed reasoning and complex problem-solving.
---
Selected Answer: D
Chain-of-thought (CoT) prompting is one of the oldest “chain of” methods for improving LLM performance – in particular in the context of queries or tasks that need complex, human-like reasoning to reach an answer.

</details>

---

## Question 149: AIF-C01-ET-Q149
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company wants to keep its foundation model (FM) relevant by using the most recent data. The company wants to implement a model training strategy that includes regular updates to the FM.

Which solution meets these requirements?

**Choices:**
- A) Batch learning
- B) Continuous pre-training
- C) Static training
- D) Latent training

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (100%). Contributor Answer: B.

Community Rationale & Discussion:
B. Continuous pre-training
---
Selected Answer: B
This strategy involves regularly updating the foundation model with new data, ensuring the model stays relevant and accurate over time. It allows for the continuous improvement of the model as new information becomes available.
---
Selected Answer: B
Answer: B. Continuous pre-training

To keep a foundation model (FM) updated with the most recent data on a regular basis, you need a training approach that continually integrates new information. Continuous pre-training fits this requirement because it periodically (or even continuously) retrains or fine-tunes the model with the latest data, ensuring relevance and improved performance.

Here's why the other options are less suitable:

A. Batch learning: Trains in large, discrete batches and may introduce significant delays between training cycles, potentially causing the model to become stale.
C. Static training: Trains the model once and does not update it with new data, leading to outdated predictions.
D. Latent training: Not a standard industry term or recognized strategy for regularly updating foundation models.

</details>

---

## Question 151: AIF-C01-ET-Q151
**Domain 5:** Security, Compliance, and Governance for AI Solutions  

**Question:**  
Which option is a characteristic of AI governance frameworks for building trust and deploying human-centered AI technologies?

**Choices:**
- A) Expanding initiatives across business units to create long-term business value
- B) Ensuring alignment with business standards, revenue goals, and stakeholder expectations
- C) Overcoming challenges to drive business transformation and growth
- D) Developing policies and guidelines for data, transparency, responsible AI, and compliance

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `D`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: D (100%). Contributor Answer: D.

Community Rationale & Discussion:
D. Developing policies and guidelines for data, transparency, responsible AI, and compliance Most Voted
---
Selected Answer: D
AI governance frameworks are designed to ensure that AI technologies are developed and deployed in a way that is ethical, transparent, and aligned with societal values. This involves creating policies and guidelines that address key areas such as data usage, transparency in AI decision-making, responsible AI practices, and compliance with legal and regulatory standards. These measures help build trust and ensure that AI technologies are human-centered and beneficial to society.
---
Selected Answer: D
All other options are primarily about business growth

</details>

---

## Question 152: AIF-C01-ET-Q152
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
An ecommerce company is using a generative AI chatbot to respond to customer inquiries. The company wants to measure the financial effect of the chatbot on the company’s operations.

Which metric should the company use?

**Choices:**
- A) Number of customer inquiries handled
- B) Cost of training AI models
- C) Cost for each customer conversation
- D) Average handled time (AHT)

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (80%). Contributor Answer: C.

Community Rationale & Discussion:
C is the correct answer as it most directly measures the financial impact of the chatbot on operations.
---
Selected Answer: C
This metric directly relates to the financial impact of the chatbot by quantifying the cost associated with handling each customer interaction. By comparing this cost to the previous cost of handling inquiries (e.g., through human agents), the company can assess the financial efficiency and effectiveness of the chatbot.
---
Selected Answer: C
If "The company wants to measure the financial effect of the chatbot", the metric should be in terms of cost

</details>

---

## Question 153: AIF-C01-ET-Q153
**Domain 1:** Fundamentals of AI and ML  

**Question:**  
A company wants to find groups for its customers based on the customers’ demographics and buying patterns.

Which algorithm should the company use to meet this requirement?

**Choices:**
- A) K-nearest neighbors (k-NN)
- B) K-means
- C) Decision tree
- D) Support vector machine

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `B`  
**Community Consensus:** `80%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: B (80%). Contributor Answer: B.

Community Rationale & Discussion:
Selected Answer: B
K-means is a clustering algorithm widely used for customer segmentation. It groups customers based on similarities in their demographics and buying patterns, creating distinct clusters that can be analyzed for targeted marketing strategies or personalized product offerings. This algorithm is efficient, interpretable, and works well with large datasets, making it suitable for e-commerce applications.
---
A. K-nearest neighbors (k-NN) - classification
B. K-means - clustering - groups, so B
---
Selected Answer: A
Let's break down why:

Why K-means is correct:

The company wants to find "groups" of customers → This indicates a clustering task
K-means is specifically designed for grouping/clustering similar data points
It works well with multiple features (demographics AND buying patterns)
K-means can automatically discover natural groupings in customer data
It's commonly used for customer segmentation in business applications

Why other options are incorrect:

A (K-nearest neighbors): This is for classification when you already have labeled data, not for discovering groups

</details>

---

## Question 154: AIF-C01-ET-Q154
**Domain 2:** Fundamentals of Generative AI  

**Question:**  
A company’s large language model (LLM) is experiencing hallucinations.

How can the company decrease hallucinations?

**Choices:**
- A) Set up Agents for Amazon Bedrock to supervise the model training.
- B) Use data pre-processing and remove any data that causes hallucinations.
- C) Decrease the temperature inference parameter for the model.
- D) Use a foundation model (FM) that is trained to not hallucinate.

<details>
<summary><b>View Verified Answer & Community Consensus</b></summary>

**Verified Answer:** `C`  
**Community Consensus:** `100%` agreement.  

**Explanation & Analysis:**  
Community Most Voted: C (100%). Contributor Answer: C.

Community Rationale & Discussion:
this is how you decrease the hallucinations

C. Decrease the temperature inference parameter for the model.
---
C. Decrease the temperature inference parameter for the model.
---
C is the correct answer. Here's why:

Decreasing the temperature parameter makes the model's outputs more deterministic and conservative, reducing the likelihood of hallucinations.

</details>

---
