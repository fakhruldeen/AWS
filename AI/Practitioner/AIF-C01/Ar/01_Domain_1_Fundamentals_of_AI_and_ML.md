<div dir="rtl">

# 01 — المجال الأول: أساسيات الذكاء الاصطناعي وتعلم الآلة (`Domain 1 — 20%`)

> **الوزن النسبي في الاختبار:** `20%` (حوالي 10 أسئلة مُقيّمة في الاختبار الرسمي)  
> **المهام الرسمية:** `Task 1.1` (المصطلحات وأنماط التعلم) • `Task 1.2` (حالات الاستخدام وخدمات AWS المُدارة) • `Task 1.3` (دورة حياة ML و `MLOps` والمقاييس)

---

## 1. مشكلة الملاءمة: `Overfitting` مقابل `Underfitting`
- **Overfitting (التخصيص المفرط — High Variance):** النموذج «يحفظ» بيانات التدريب بما فيها الضوضاء، فيحقق دقة ممتازة أثناء التدريب (`99%`) ولكنه يفشل على البيانات الجديدة (`65%`).
  - **الحلول في الاختبار:** زيادة كمية وتنوع البيانات، استخدام `Regularization` أو `Dropout`، تبسيط النموذج، أو `Early Stopping`.
- **Underfitting (التخصيص الناقص — High Bias):** النموذج أبسط من اللازم ولا يستوعب الأنماط الحقيقية، فيكون أداؤه ضعيفاً على بيانات التدريب والاختبار معاً.
  - **الحلول في الاختبار:** إضافة ميزات (`Feature Engineering`)، استخدام نموذج أكثر تعقيداً، أو التدريب لفترة أطول.

---

## 2. متى لا نستخدم الذكاء الاصطناعي (`When NOT to use AI/ML`)؟
قاعدة ذهبية متكررة في أسئلة `AIF-C01`:
1. عندما يتطلب العمل **نتيجة حتمية دقيقة 100%** تحكمها قواعد ثابتة (مثل حساب الضرائب أو المعادلات المحاسبية) ← استخدم **Rule-Based Software** وليس `ML`.
2. عندما تكون البيانات غير كافية أو منخفضة الجودة.
3. عندما تتجاوز تكلفة بناء وتشغيل النموذج العائد التجاري المتوقع (`ROI`).

---

## 3. خريطة خدمات الذكاء الاصطناعي المُدارة من AWS (بدون خبرة ML)

| الخدمة | الوظيفة الأساسية | متى تختارها في الاختبار؟ |
| :--- | :--- | :--- |
| [`Amazon Rekognition`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-rekognition) | الرؤية الحاسوبية (`Computer Vision`) | كشف الأجسام والوجوه ومراقبة المحتوى غير اللائق في الصور والفيديو |
| [`Amazon Textract`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-textract) | قراءة المستندات الذكية (`Smart OCR`) | استخراج النصوص و**الجداول والنماذج (`Key-Value Pairs`)** من الفواتير وملفات `PDF` الممسوحة |
| [`Amazon Comprehend`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-comprehend) | معالجة اللغة الطبيعية (`NLP`) | تحليل المشاعر (`Sentiment`)، الكيانات (`Entities`)، اللغة، وإخفاء `PII` من النصوص |
| [`Amazon Transcribe`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-transcribe) | تحويل الصوت إلى نص (`Speech-to-Text`) | تفريغ مكالمات مراكز الاتصال وإنتاج الترجمة النصية (`Subtitles`) |
| [`Amazon Polly`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-polly) | تحويل النص إلى صوت (`Text-to-Speech`) | إنشاء قراءة صوتية طبيعية للكتب أو التطبيقات |
| [`Amazon Translate`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-translate) | الترجمة الآلية العصبية | ترجمة المواقع وتذاكر الدعم بين اللغات المختلفة |
| [`Amazon Lex`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-lex) | روبوتات المحادثة (`Chatbots`) | بناء مساعدات صوتية ونصية تفاعلية (نفس تقنية `Alexa`) |
| [`Amazon Personalize`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-personalize) | أنظمة التوصية (`Recommendations`) | توصيات منتجات ومحتوى فورية مخصصة للمستخدمين |

---

## 4. أنماط الاستدلال الأربعة في `Amazon SageMaker AI`

| نمط الاستدلال | زمن الاستجابة | حجم الحمولة (`Payload`) | أفضل حالة استخدام |
| :--- | :--- | :--- | :--- |
| **Real-Time Inference** | أجزاء من الثانية (`ms`) | حتى `25 MB` (مهلة `60s`) | تطبيقات فورية بحركة مرور ثابتة ومستمرة |
| **Serverless Inference** | فوري (مع احتمال `Cold Start`) | حتى `4 MB` | حركة مرور متقطعة وغير متوقعة؛ يتوسع للصفر لتوفير التكلفة |
| **Asynchronous Inference** | شبه فوري (عبر صف انتظار) | حتى `1 GB` (معالجة حتى ساعة) | ملفات كبيرة (فيديو/صور طبية) تتطلب معالجة طويلة |
| **Batch Transform** | غير فوري (`Offline`) | مجموعات بيانات ضخمة في `S3` | معالجة ملايين السجلات ليلياً دون نقطة نهاية دائمة |

---

## 5. دورة حياة تعلم الآلة ومقاييس التقييم (`MLOps & Metrics`)
- **أدوات دورة الحياة في AWS:** [`Amazon SageMaker AI`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-sagemaker-ai) (`Data Wrangler` لتنظيف البيانات، `Ground Truth` لوسم البيانات، `Canvas` للنمذجة بدون كود، `Pipelines` للأتمتة، `Model Monitor` لمراقبة الانحراف `Drift`) + [`Amazon Bedrock`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock) + [`Amazon Quick`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-quick) + [`Kiro`](../AWS_AI_SERVICES_GLOSSARY.md#kiro).
- **مقاييس التصنيف (`Classification`):**
  - **Precision:** تقليل الإنذارات الكاذبة (`False Positives`) — مهم في فلاتر البريد المزعج (`Spam`).
  - **Recall:** تقليل الحالات الفائتة (`False Negatives`) — حرج في تشخيص السرطان وكشف الاحتيال.
  - **F1 Score:** المتوسط التوافقي بين `Precision` و `Recall` — الأفضل للبيانات غير المتوازنة (`Imbalanced Datasets`).
- **مقاييس الانحدار (`Regression`):** `MAE`، `RMSE` (يعاقب الأخطاء الكبيرة بشدة)، و `R²`.
- **مقاييس الأعمال (`Business Metrics`):** `ROI`، تكلفة المستخدم الواحد (`Cost per user`)، تكاليف التطوير، ورضا العملاء.

**الخطوة التالية:** [02_Domain_2_Fundamentals_of_GenAI.md](./02_Domain_2_Fundamentals_of_GenAI.md)

</div>
