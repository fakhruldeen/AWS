<div dir="rtl">

# 🔗📊🤖 Domain 3 (الجزء التالت): Integration, Monitoring, Migration & AI/ML

ده الجزء الأخير في Domain 3، وبيجمعلك كل الخدمات اللي بتخلي السيستم بتاعك مترابط (`Decoupled`)، ومتراقب كويس، وبتنقل بياناتك للكلاود، وبتضيف ذكاء اصطناعي وتحليلات بيانات. ركّز على **الوظيفة في سطر واحد** لكل خدمة!

---

## 1️⃣ ربط التطبيقات وفصلها (Application Integration & Decoupling)

تخيل مطعم شغال كويس: بدل ما الكاشير يقف يستنى الشيف يخلص الساندوتش عشان ياخد طلب الزبون اللي بعده (**Tightly Coupled**)، الكاشير بيحط ورقة الطلب في طابور الطلبات وياخد الزبون اللي بعده على طول (**Loosely Coupled / Decoupled**)!

| الخدمة | التشبيه المصري | الوظيفة الأساسية في AWS |
| :--- | :--- | :--- |
| **`Amazon SQS`** (Simple Queue Service) | **طابور طلبات الكاشير (`Message Queue`)** | بيفصل بين أجزاء التطبيق (**Decoupling**). خدمة ترمي رسايل في الطابور وخدمة تانية تسحبها (**Pull**) وتشتغل عليها براحتها من غير ما حاجة تضيع! فيه نوعين: **Standard** (أسرع بس الترتيب مش مضمون 100%) و **FIFO** (اللي يدخل الأول يخرج الأول بالترتيب بالظبط — *First-In-First-Out*). |
| **`Amazon SNS`** (Simple Notification Service) | **ميكروفون الجامع / جروب الإعلانات (`Pub/Sub`)** | بتبعت رسالة واحدة لـ **Topic**، و SNS بيزقها (**Push**) فوراً لآلاف المشتركين في نفس الوقت (إيميل، SMS، إشعار موبايل، أو حتى لـ Lambda و SQS). |
| **`Amazon EventBridge`** | **موزع الأحداث الذكي (`Event Bus`)** | بيستقبل الأحداث من خدمات AWS أو تطبيقات خارجية (SaaS زي Zendesk و Shopify) ويوجهها بقواعد ذكية لخدمات تانية (وكمان بيشغل مهام بجدول زمني زي الـ Cron Job). |
| **`AWS Step Functions`** | **المايسترو (`Workflow Orchestration`)** | بترسم عليه خطوات متسلسلة (**Visual Workflow**) تربط بيها عدة دوال **AWS Lambda** وخدمات AWS ورا بعض مع معالجة الأخطاء أوتوماتيك. |
| **`Amazon API Gateway`** | **موظف الاستقبال الرئيسي (`Front Door for APIs`)** | بيعملك ويديرلك الـ **REST / HTTP / WebSocket APIs** بشكل Serverless ويحميها (بـ Throttling و Authentication) ويوصلها بـ **AWS Lambda**. |

---

## 2️⃣ المراقبة والإدارة والأتمتة (Monitoring, Governance & DevOps)

### 👀 الـ 3 الكبار في المراقبة (لازم تفرق بينهم كويس أوي!):
1. **`Amazon CloudWatch` (مؤشرات الأداء والـ Logs — "السيستم عامل إيه؟"):**
   * بيراقب **الأداء (`Performance Metrics`)** زي استهلاك الـ **CPU** والـ **Memory** وبيجمع الـ **Application Logs** وبيبعتلك إنذار (**CloudWatch Alarms**) لو السيرفر سخن أو استهلاكه عدى 80%!
2. **`AWS CloudTrail` (كاميرا المراقبة — "مين عمل إيه وامتى؟"):**
   * بيسجل كل حركة و **API Call** بتحصل في حسابك (مين مسح الـ S3 Bucket الساعة 3 الفجر؟). أساسي للـ **Auditing & Governance**.
3. **`AWS Config` (سجل التغييرات والامتثال — "إعدادات السيرفر كانت إيه واتغيرت لإيه؟"):**
   * بيراقب **إعدادات مواردك (`Resource Configurations`)** عبر الزمن، ويتأكد إنها مطابقة لقواعد الشركة (**Compliance Rules** — مثلاً: هل كل S3 Buckets مشفرة ولا لأ؟).

### 🛠️ خدمات الإدارة والـ DevOps المهمة:
* **`AWS Trusted Advisor` (المستشار الشخصي بتاعك):** بيفحص حسابك كله ويديك نصايح ذكية في **5 مجالات**:
  1. **Cost Optimization** (بيقولك فيه سيرفرات فاضية بتدفع فيها فلوس عالفاضي!).
  2. **Performance**
  3. **Security** (بيقولك الـ Root User مش عليه MFA!).
  4. **Fault Tolerance**
  5. **Service Quotas**
* **`AWS Systems Manager (SSM)`:** أداة سحرية بتدير بيها مئات السيرفرات (سواء على AWS أو On-Premises) من مكان واحد: تعملهم تحديثات (**Patch Manager**)، وتدخل على السيرفر بآمان من غير ما تفتح بورت SSH (**Session Manager**)!
* **`AWS Health Dashboard`:** بيوريك الحالة الصحية لخدمات AWS، وهل فيه عطل عالمي أو صيانة مجدولة هتأثر على حسابك إنت شخصياً (**Personal Health Dashboard**).
* **`AWS CloudFormation` (Infrastructure as Code — IaC):** بدل ما تقعد تضغط كليكات في الـ Console عشان تبني VPC وسيرفرات، بتكتب وصف البنية التحتية في ملف **YAML** أو **JSON**، و CloudFormation بيبنيها أو يمسحها كلها بضغطة زرار!
* **`AWS CDK` (Cloud Development Kit):** زي CloudFormation بس بتكتب البنية التحتية بلغات برمجة حقيقية بتحبها (زي **Python**, **TypeScript**, **Java**, **C#**)!
* **أدوات الـ CI/CD (توصيل الكود أوتوماتيك):**
  * `AWS CodeBuild` (بيبني ويختبر الكود)
  * `AWS CodeDeploy` (بينزل الكود الجديد على السيرفرات)
  * `AWS CodePipeline` (خط الإنتاج الكامل اللي بيشغل كل الخطوات أوتوماتيك من أول ما المبرمج يرفع الكود).

---

## 3️⃣ نقل البيانات والانتقال للكلاود (Migration & Transfer)

لو عندك شركة فيها **تيرابايتس أو بيتابايتس** من البيانات وعايز تنقلها لـ AWS، الإنترنت العادي هياخد سنين! AWS عملتلك حلول عبقرية:

* **`AWS Snow Family` (الشنط والصناديق الفعلية — Physical Data Transfer & Edge Computing):**
  * **`AWS Snowcone`:** أصغر واحد (حجم علبة مناديل) — بيشيل لحد **8–14 TB**.
  * **`AWS Snowball Edge`:** حجم شنطة سفر — بيشيل لحد **80–210 TB** وفيه CPU يقدر يعالج بيانات في الأماكن اللي مفيهاش إنترنت (زي السفن أو الصحراء).
  * *(ملحوظة: زمان كان فيه **`AWS Snowmobile`** عبارة عن تريلا/شاحنة بتنقل 100 Petabytes).*
* **`AWS DataSync`:** بينقل كميات ضخمة من الملفات **أونلاين** بسرعة عالية بين سيرفرات شركتك و AWS (`S3`, `EFS`, `FSx`).
* **`AWS Application Migration Service (MGN)`:** أسرع طريقة لنقل سيرفراتك الفعلية (**Lift-and-Shift / Rehost**) زي ما هي لـ AWS بأقل توقف.
* **`AWS Migration Hub`:** شاشة مركزية بتابع منها تقدم كل مشاريع النقل بتاعت شركتك.

### 🚀 الـ 7 استراتيجيات للانتقال للكلاود (The 7 Rs of Cloud Migration):
1. **Rehost (Lift-and-Shift):** انقل السيرفر زي ما هو من غير أي تعديل في الكود (أسرع طريقة).
2. **Replatform (Lift-and-Reshape):** انقل زي ما هو مع تعديل بسيط عشان تستفيد من الكلاود (مثلاً بدل ما تدير MySQL بنفسك تحطها على `Amazon RDS`).
3. **Refactor / Re-architect:** أعد كتابة التطبيق من جديد عشان يستفيد من الكلاود بالكامل (مثلاً تحوله لـ **Serverless / Microservices**).
4. **Repurchase (Drop and Shop):** تسيب برنامجك القديم وتشتري بداله منتج جاهز **SaaS** (مثلاً تسيب CRM قديم وتشترك في Salesforce).
5. **Relocate:** تنقل سيرفرات **VMware** للكلاود (`VMware Cloud on AWS`) من غير تعديل.
6. **Retain:** تسيب التطبيق عندك في الشركة زي ما هو دلوقتي ومش هتنقله.
7. **Retire:** تقفل وتمسح التطبيقات القديمة اللي محدش بيستخدمها أصلاً!

---

## 4️⃣ خدمات تحليل البيانات والذكاء الاصطناعي (Analytics & AI/ML)

في امتحان `CLF-C02` مش مطلوب منك تفاصيل عميقة هنا — بس لازم تعرف **اسم الخدمة = بتعمل إيه في 3 كلمات**:

### 📊 خدمات تحليل البيانات (Analytics):
* **`Amazon Athena`:** تكتب أوامر **SQL** عشان تحلل ملفات متخزنة جوه **`Amazon S3`** مباشرة (**Serverless** ومن غير ما تعمل داتابيز!).
* **`AWS Glue`:** خدمة **Serverless ETL** (بتنضف وتحول وتجهز البيانات للتحليل).
* **`Amazon EMR`:** لتشغيل بيانات ضخمة (**Big Data**) بأدوات مفتوحة المصدر زي **Apache Spark** و **Hadoop**.
* **`Amazon Kinesis`:** بتستقبل وتحلل **البيانات الحية المتدفقة في الوقت الفعلي (`Real-time Streaming Data`)** زي بيانات حساسات السيارات والأسهم.
* **`Amazon QuickSight`:** أداة **Business Intelligence (BI)** بتعملك رسوم بيانية و **Dashboards** تفاعلية جميلة للإدارة.
* **`Amazon OpenSearch Service`:** محرك بحث وتحليل Logs سريع جداً.

### 🤖 خدمات الذكاء الاصطناعي (AI & Machine Learning):
| الخدمة | بتعمل إيه في كلمتين؟ |
| :--- | :--- |
| **`Amazon Bedrock`** | **الذكاء الاصطناعي التوليدي (`Generative AI`)** — بتديك وصول لـ **Foundation Models (LLMs)** زي Claude و Amazon Nova بـ API جاهز ومن غير سيرفرات. |
| **`Amazon SageMaker`** | منصة متكاملة للمطورين وعلماء البيانات عشان **يبنوا ويدربوا وينشروا (`Build, Train, Deploy`)** نماذج **Machine Learning** خاصة بيهم. |
| **`Amazon Rekognition`** | **تحليل الصور والفيديوهات** (التعرف على الوجوه، الأشياء، والمحتوى غير اللائق). |
| **`Amazon Textract`** | **قراءة النصوص والجداول من المستندات والصور والـ PDF** (OCR ذكي للفواتير والعقود). |
| **`Amazon Comprehend`** | **فهم اللغة الطبيعية (`NLP`)** — يحلل تعليقات العملاء ويعرف هل هما مبسوطين ولا زعلانين (**Sentiment Analysis**). |
| **`Amazon Polly`** | يحوّل **النص إلى صوت بشري واقعي (`Text-to-Speech`)**. |
| **`Amazon Transcribe`** | يحوّل **الصوت إلى نص مكتوب (`Speech-to-Text`)** (مثلاً تفريغ مكالمات الكول سنتر). |
| **`Amazon Translate`** | **ترجمة اللغات** أوتوماتيك وبجودة عالية. |
| **`Amazon Lex`** | بناء **Chatbots** ومساعدين صوتيين (نفس المحرك اللي بيشغّل **Alexa**!). |
| **`Amazon Kendra`** | **محرك بحث ذكي جوه مستندات الشركة** بالذكاء الاصطناعي. |
| **`Amazon Personalize`** | محرك **توصيات المنتجات** (زي "الناس اللي اشترت ده اشترت كمان..." على موقع Amazon.com!). |

---

## 🎯 زتونة الامتحان للجزء التالت

| لو شفت في السؤال... | الإجابة الصح فوراً! |
| :--- | :--- |
| **Decouple microservices using a message queue** | **`Amazon SQS`** |
| **Send push notifications (SMS, Email) to multiple subscribers (Pub/Sub)** | **`Amazon SNS`** |
| **Monitor CPU utilization, application logs, and set alarms** | **`Amazon CloudWatch`** |
| **Audit who made an API call or deleted a resource** | **`AWS CloudTrail`** |
| **Track resource configuration history and evaluate compliance rules** | **`AWS Config`** |
| **Get best-practice recommendations for Cost, Security, Fault Tolerance** | **`AWS Trusted Advisor`** |
| **Provision AWS infrastructure using JSON/YAML templates (IaC)** | **`AWS CloudFormation`** |
| **Query data directly in Amazon S3 using standard SQL (Serverless)** | **`Amazon Athena`** |
| **Process real-time streaming data** | **`Amazon Kinesis`** |
| **Convert speech to text / transcribe customer service calls** | **`Amazon Transcribe`** |
| **Convert text to lifelike speech** | **`Amazon Polly`** |
| **Extract text and tables from scanned PDF forms** | **`Amazon Textract`** |
| **Analyze customer sentiment from product reviews (NLP)** | **`Amazon Comprehend`** |
| **Build conversational chatbots (same tech as Alexa)** | **`Amazon Lex`** |
| **Build Generative AI apps using Foundation Models (LLMs)** | **`Amazon Bedrock`** |

---

> ⬅️ **الدرس السابق:** [Domain 3 — الجزء التاني: Databases & Networking](./03_Domain_3_Part2_Databases_and_Networking.md) | **الدرس التالي:** 👉 **[04_Domain_4_Billing_Pricing_and_Support.md](./04_Domain_4_Billing_Pricing_and_Support.md)** | [الفهرس](./README.md)

</div>
