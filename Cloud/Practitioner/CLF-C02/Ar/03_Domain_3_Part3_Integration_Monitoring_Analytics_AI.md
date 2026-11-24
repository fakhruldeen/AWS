<div dir="rtl">

# Domain 3 (الجزء الثالث): Integration, Monitoring, Migration, Analytics & AI/ML

يستكمل هذا الجزء الأخير من المجال الثالث (`Cloud Technology and Services`) المنظومة السحابية بتغطية أربعة محاور حيوية: **فك الارتباط وربط التطبيقات (`Application Integration`)**، و **المراقبة والحوكمة والأتمتة (`Monitoring, Management & DevOps`)**، و **استراتيجيات وأدوات الانتقال للسحابة (`Migration & Transfer`)**، و **خدمات تحليل البيانات والذكاء الاصطناعي (`Analytics & AI/ML`)**.

---

## أولاً: تكامل التطبيقات وفك الارتباط (`Application Integration & Decoupling`)

في الأنظمة الموزعة الحديثة، يؤدي الربط المباشر والوثيق بين المكونات (`Tightly Coupled Architecture`) إلى توقف النظام بأكمله عند تعطل مكون واحد أو ارتفاع الضغط عليه. لحل ذلك نعتمد على **فك الارتباط (`Loosely Coupled / Decoupled Architecture`)** باستخدام خدمات الرسائل والأحداث:

| الخدمة | النمط المعماري | الشرح التفصيلي وحالة الاستخدام |
| :--- | :---: | :--- |
| **`Amazon SQS`** (Simple Queue Service) | **Message Queue (`Pull`)** | خدمة طوابير رسائل مُدارة بالكامل و `Serverless`. يضع المرسِل (`Producer`) الرسائل في الطابور، ويقوم المستقبِل (`Consumer`) بسحبها ومعالجتها بالسرعة التي تناسبه دون فقدان أي طلب عند ارتفاع الضغط المفاجئ. يتوفر بنوعين: **`Standard Queue`** (إنتاجية غير محدودة تقريباً مع تسليم *At-least-once*) و **`FIFO Queue`** (تضمن الترتيب الدقيق *First-In-First-Out* والمعالجة مرة واحدة بالضبط *Exactly-once*). |
| **`Amazon SNS`** (Simple Notification Service) | **Pub/Sub (`Push`)** | خدمة نشر واشتراك مُدارة بالكامل. تُرسل الرسالة مرة واحدة إلى موضوع (`SNS Topic`)، فتتولى الخدمة دفعها فوراً بالتوازي (**Fan-out**) إلى آلاف المشتركين عبر البريد الإلكتروني (`Email`)، الرسائل النصية (`SMS`)، إشعارات الهواتف (`Mobile Push`)، أو خدمات AWS مثل `AWS Lambda` و `Amazon SQS`. |
| **`Amazon EventBridge`** | **Event Bus (`Serverless`)** | ناقل أحداث ذكي يربط بين خدمات AWS، وتطبيقاتك الخاصة، وتطبيقات `SaaS` الخارجية (مثل Zendesk و Shopify و Datadog) عبر قواعد تصفية وتوجيه دقيقة، كما يدعم جدولة المهام الدورية (`Scheduled Rules / Cron`). |
| **`AWS Step Functions`** | **Workflow Orchestration** | خدمة تنسيق مرئية تتيح بناء وتنفيذ سلاسل عمل متعددة الخطوات (`State Machines`) تربط بين عدة دوال `AWS Lambda` وخدمات AWS أخرى، مع إدارة تلقائية لإعادة المحاولة (`Retries`) ومعالجة الأخطاء والتفرعات المنطقية. |
| **`Amazon API Gateway`** | **Managed API Front Door** | خدمة `Serverless` لإنشاء ونشر وتأمين ومراقبة واجهات برمجة التطبيقات (`REST`, `HTTP`, `WebSocket APIs`) على أي نطاق، مع دعم تحديد معدل الطلبات (`Throttling`) والمصادقة (`IAM` / `Cognito`) والتخزين المؤقت. |

---

## ثانياً: المراقبة والحوكمة والإدارة والأتمتة (`Monitoring, Governance & DevOps`)

### 1. منظومة المراقبة الثلاثية (التمييز الدقيق بينها ضروري للاختبار)

1. **`Amazon CloudWatch` (الأداء والسجلات والإنذارات — "كيف يؤدي النظام؟"):**
   * يجمع ويراقب **مؤشرات الأداء (`Metrics`)** مثل استهلاك الـ `CPU` والقرص والشبكة، ويجمع سجلات التطبيقات (**`CloudWatch Logs`**)، ويتيح إنشاء **إنذارات تلقائية (`CloudWatch Alarms`)** (مثل تشغيل `Auto Scaling` أو إرسال إشعار `SNS` عند تجاوز استهلاك المعالج 80%).
2. **`AWS CloudTrail` (التدقيق الأمني وسجل الأنشطة — "من فعل ماذا ومتى؟"):**
   * يسجل تاريخ جميع استدعاءات الـ **`API`** والإجراءات المنفذة في حسابك (سواء عبر Management Console أو CLI أو SDK). يُعد المرجع الأساسي للتدقيق الأمني (`Governance & Compliance Auditing`) والتحقيق في الحوادث التشغيلية.
3. **`AWS Config` (تاريخ الإعدادات والامتثال — "كيف تغيرت إعدادات المورد عبر الزمن؟"):**
   * يتتبع التغييرات التي تطرأ على **إعدادات وتكوينات موارد AWS (`Resource Configurations`)** عبر الزمن، ويقيّم تلقائياً مدى مطابقتها للقواعد الأمنية المعتمدة في المؤسسة (`Compliance Rules` — مثلاً التحقق من أن جميع أقراص `EBS` مشفرة وأن حاويات `S3` غير مفتوحة للعامة).

### 2. خدمات الإدارة والتوجيه والتحسين التشغيلي
* **`AWS Trusted Advisor`:** مستشار آلي يفحص بيئة حسابك وفق أفضل الممارسات العالمية لـ AWS ويقدم توصيات عملية في **خمس فئات رئيسية**:
  1. **`Cost Optimization`** (كشف الخوادم الخاملة أو غير المستغلة وعناوين Elastic IP غير المرتبطة).
  2. **`Performance`** (تحسين كفاءة الموارد).
  3. **`Security`** (التنبيه عند غياب `MFA` على `Root User` أو وجود منافذ مفتوحة للعامة).
  4. **`Fault Tolerance`** (التحقق من توزيع الموارد وتفعيل النسخ الاحتياطي).
  5. **`Service Quotas`** (التنبيه عند الاقتراب من الحدود القصوى للاستخدام).
* **`AWS Systems Manager (SSM)`:** مركز إدارة موحد لأسطول الخوادم (على AWS أو في البيئة المحلية `On-Premises`). يضم أدوات بالغة الأهمية مثل **`Patch Manager`** (أتمتة تحديثات أنظمة التشغيل)، و **`Session Manager`** (الدخول الآمن إلى خوادم `EC2` عبر المتصفح أو CLI **دون الحاجة لفتح منفذ `SSH 22`** أو استخدام `Bastion Host`)، و **`Parameter Store`**.
* **`AWS Health Dashboard`:** يعرض الحالة التشغيلية العالمية لخدمات AWS، بالإضافة إلى تنبيهات مخصصة لحسابك (`Account Health`) حول الصيانات المجدولة أو الأعطال التي قد تؤثر على مواردك تحديداً.

### 3. البنية التحتية ككود (`IaC`) وأدوات التكامل والنشر المستمر (`CI/CD`)
* **`AWS CloudFormation`:** يتيح تعريف ونشر وتحديث وحذف البنية التحتية الكاملة على AWS باستخدام قوالب نصية تصريحية بصيغة **`YAML`** أو **`JSON`**، مما يضمن قابلية التكرار (`Repeatability`) وتقليل الأخطاء البشرية.
* **`AWS CDK` (Cloud Development Kit):** يتيح للمطورين كتابة تعريف البنية التحتية باستخدام لغات برمجة مألوفة (مثل **TypeScript**, **Python**, **Java**, **C#**, **Go**)، ثم يقوم تلقائياً بترجمتها وتوليد قوالب `CloudFormation`.
* **منظومة `AWS Code*` للـ `CI/CD`:**
  * **`AWS CodeBuild`:** خدمة مُدارة لتجميع الكود وتشغيل الاختبارات الآلية وإنتاج حزم برمجية جاهزة للنشر.
  * **`AWS CodeDeploy`:** أتمتة نشر تحديثات التطبيقات على `EC2` أو `ECS` أو `Lambda` أو الخوادم المحلية بأقل توقف ممكن.
  * **`AWS CodePipeline`:** أتمتة خط الإنتاج الكامل (`Continuous Delivery Pipeline`) لربط مراحل البناء والاختبار والنشر تلقائياً عند كل تعديل في الكود.

---

## ثالثاً: نقل البيانات والانتقال إلى السحابة (`Migration & Transfer`)

### 1. أدوات نقل البيانات الضخمة والهجينة
* **`AWS Snow Family` (النقل المادي للبيانات والحوسبة الطرفية `Edge Computing`):** أجهزة مادية مؤمَّنة ومشفرة تشحنها AWS إليك عند الحاجة لنقل كميات ضخمة من البيانات (`Terabytes / Petabytes`) لا يمكن نقلها عملياً عبر الإنترنت العادي، أو لتشغيل المعالجة في بيئات منقطعة عن الإنترنت:
  * **`AWS Snowcone`:** أصغر جهاز محمول (حتى **8–14 TB**).
  * **`AWS Snowball Edge`:** جهاز بحجم حقيبة متينة (حتى **80–210 TB**) متوفر بنسخ محسّنة للتخزين (`Storage Optimized`) أو للحوسبة (`Compute Optimized`).
  * *(ملاحظة تاريخية في بعض الأسئلة: **`AWS Snowmobile`** كان شاحنة حاوية لنقل حتى 100 Petabytes).*
* **`AWS DataSync`:** خدمة نقل بيانات **عبر الشبكة (`Online`)** سريعة وآمنة ومؤتمتة لنقل كميات كبيرة من الملفات بين مراكز البيانات المحلية وخدمات تخزين AWS (`S3`, `EFS`, `FSx`).
* **`AWS Application Migration Service (MGN)`:** الخدمة الموصى بها لنقل الخوادم الفيزيائية والافتراضية كما هي (**`Lift-and-Shift / Rehost`**) إلى AWS بأقل زمن توقف.
* **`AWS Migration Hub`:** لوحة متابعة مركزية لتتبع حالة وتقدم جميع مشاريع الترحيل عبر أدوات AWS والشركاء من مكان واحد.

### 2. استراتيجيات الانتقال السبع (`The 7 Rs of Cloud Migration`)
1. **`Rehost` (Lift-and-Shift):** نقل التطبيقات والخوادم كما هي دون تعديل الكود البرمجي (الأسرع تنفيذاً).
2. **`Replatform` (Lift-and-Reshape):** نقل التطبيق مع إجراء تحسينات سحابية محدودة دون تغيير معماريته الجوهرية (مثل الانتقال من قاعدة بيانات مُدارة يدوياً إلى `Amazon RDS`).
3. **`Refactor / Re-architect`:** إعادة تصميم وبناء التطبيق بالكامل للاستفادة القصوى من مزايا السحابة (مثل التحول إلى `Serverless` و `Microservices`).
4. **`Repurchase` (Drop and Shop):** الاستغناء عن النظام التقليدي وشراء منتج بديل جاهز من نوع `SaaS` (مثل الانتقال إلى نظام CRM سحابي).
5. **`Relocate`:** نقل بنية تحتية كاملة تعمل على `VMware` إلى `VMware Cloud on AWS` دون الحاجة لشراء عتاد أو تعديل التطبيقات.
6. **`Retain`:** الإبقاء على بعض التطبيقات مؤقتاً في البيئة المحلية لاعتبارات تنظيمية أو تقنية.
7. **`Retire`:** إيقاف وإزالة التطبيقات القديمة التي لم تعد تحقق قيمة فعلية للأعمال لتوفير التكاليف.

---

## رابعاً: خدمات تحليل البيانات والذكاء الاصطناعي (`Analytics & AI/ML`)

### 1. خدمات تحليل البيانات (`AWS Analytics Services`)
* **`Amazon Athena`:** خدمة استعلام تفاعلية **`Serverless`** تتيح تحليل البيانات المخزنة مباشرةً داخل **`Amazon S3`** باستخدام لغة **`SQL`** القياسية (تدفع فقط مقابل حجم البيانات التي يتم مسحها في كل استعلام).
* **`AWS Glue`:** خدمة **`Serverless ETL`** (Extract, Transform, Load) لاكتشاف البيانات وتنظيفها وتحويل صيغها وتجهيزها للتحليل، مع فهرس مركزي (`Glue Data Catalog`).
* **`Amazon EMR` (Elastic MapReduce):** منصة مُدارة لمعالجة البيانات الضخمة (`Big Data`) باستخدام أطر مفتوحة المصدر مثل **`Apache Spark`** و **`Apache Hadoop`**.
* **`Amazon Kinesis`:** عائلة خدمات مُدارة لاستقبال ومعالجة وتحليل **البيانات المتدفقة في الوقت الفعلي (`Real-time Streaming Data`)** مثل سجلات النقر، وبيانات البورصة، ومستشعرات `IoT`.
* **`Amazon QuickSight`:** خدمة ذكاء أعمال (`Business Intelligence — BI`) سحابية و `Serverless` لإنشاء لوحات بيانات ورسوم بيانية تفاعلية (`Dashboards`) للإدارة وصناع القرار.
* **`Amazon OpenSearch Service`:** خدمة مُدارة للبحث النصي السريع وتحليل سجلات التشغيل (`Log Analytics`) في الوقت الفعلي.

### 2. خدمات الذكاء الاصطناعي وتعلم الآلة (`AWS AI & ML Services`)

| الخدمة | التخصص الدقيق وحالة الاستخدام |
| :--- | :--- |
| **`Amazon Bedrock`** | خدمة مُدارة و `Serverless` لبناء تطبيقات **الذكاء الاصطناعي التوليدي (`Generative AI`)** عبر واجهة برمجية موحدة تتيح الوصول إلى نماذج الأساس الرائدة (**`Foundation Models — FMs`**) مثل Claude و Amazon Nova مع ميزات `RAG` و `Guardrails`. |
| **`Amazon SageMaker`** | منصة متكاملة ومُدارة بالكامل تُمكّن علماء البيانات والمطورين من **بناء وتدريب ونشر (`Build, Train, and Deploy`)** نماذج التعلم الآلي المخصصة على نطاق واسع. |
| **`Amazon Rekognition`** | تحليل **الصور ومقاطع الفيديو** باستخدام الرؤية الحاسوبية (`Computer Vision`) للتعرف على الأشياء، الوجوه، النصوص داخل الصور، واكتشاف المحتوى غير اللائق. |
| **`Amazon Textract`** | استخراج النصوص المكتوبة والجداول والنماذج تلقائياً من المستندات الممسوحة ضوئياً وملفات الـ `PDF` (`Intelligent OCR`). |
| **`Amazon Comprehend`** | معالجة اللغات الطبيعية (**`NLP`**) لاكتشاف المشاعر (**`Sentiment Analysis`**)، واستخراج الكيانات الرئيسية، وتحديد لغة النصوص في مراجعات العملاء والمستندات. |
| **`Amazon Polly`** | تحويل **النص المكتوب إلى كلام صوتي واقعي (`Text-to-Speech`)** بلغات ولهجات متعددة. |
| **`Amazon Transcribe`** | تحويل **الصوت والكلام المسجل أو المباشر إلى نص مكتوب (`Speech-to-Text`)** (مثل تفريغ مكالمات مراكز خدمة العملاء). |
| **`Amazon Translate`** | خدمة ترجمة آلية عصبية سريعة ودقيقة بين اللغات المختلفة. |
| **`Amazon Lex`** | بناء واجهات محادثة ذكية (**`Conversational Chatbots`**) نصية وصوتية (تعتمد على نفس تقنية `Amazon Alexa`). |
| **`Amazon Kendra`** | محرك بحث مؤسسي ذكي مدعوم بتعلم الآلة للبحث بلغة طبيعية داخل مستندات ومستودعات المعرفة الداخلية للشركة. |
| **`Amazon Personalize`** | بناء أنظمة **توصية مخصصة في الوقت الفعلي (`Real-time Recommendations`)** للمنتجات والمحتوى (بنفس التقنية المستخدمة في متجر Amazon.com). |

---

## منهجية التعامل مع أسئلة هذا الجزء في الاختبار

| مؤشر أو عبارة في نص السؤال | الإجابة الدقيقة |
| :--- | :--- |
| **Decouple application components using a fully managed message queue** | **`Amazon SQS`** |
| **Send push notifications (Email, SMS) to multiple subscribers simultaneously (Pub/Sub)** | **`Amazon SNS`** |
| **Monitor EC2 CPU utilization, collect logs, and trigger alarms** | **`Amazon CloudWatch`** |
| **Audit user activity and API calls across an AWS account** | **`AWS CloudTrail`** |
| **Record resource configuration history and evaluate compliance rules** | **`AWS Config`** |
| **Inspect account for cost, security, fault tolerance, and service quota best practices** | **`AWS Trusted Advisor`** |
| **Provision and manage AWS infrastructure reproducibly using YAML/JSON templates** | **`AWS CloudFormation`** |
| **Query structured/unstructured files directly in S3 using SQL without servers** | **`Amazon Athena`** |
| **Ingest and analyze real-time streaming data** | **`Amazon Kinesis`** |
| **Extract text, forms, and tables from scanned PDF documents** | **`Amazon Textract`** |
| **Convert speech/audio recordings into text transcripts** | **`Amazon Transcribe`** |
| **Convert written text into lifelike speech** | **`Amazon Polly`** |
| **Analyze customer sentiment from product reviews (NLP)** | **`Amazon Comprehend`** |
| **Build Generative AI applications using Foundation Models via a serverless API** | **`Amazon Bedrock`** |

---

> **الدرس السابق:** [Domain 3 — الجزء الثاني: Databases & Networking](./03_Domain_3_Part2_Databases_and_Networking.md) | **الدرس التالي:** 👉 [04_Domain_4_Billing_Pricing_and_Support.md](./04_Domain_4_Billing_Pricing_and_Support.md) | [الفهرس الرئيسي](./README.md)

</div>
