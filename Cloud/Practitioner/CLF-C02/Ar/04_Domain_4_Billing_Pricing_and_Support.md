<div dir="rtl">

# Domain 4: Billing, Pricing, and Support — التسعير وإدارة التكاليف وباقات الدعم (12% من الاختبار)

يمثل المجال الرابع **12%** من إجمالي اختبار `CLF-C02`. ورغم أنه الأقل وزناً نسبياً، إلا أن أسئلته واضحة ومباشرة ويمكن تحصيل درجاتها بالكامل من خلال الإتقان الدقيق لفلسفة التسعير، وأدوات مراقبة وتحليل التكاليف، والفروق بين باقات الدعم الفني (`AWS Support Plans`).

---

## أولاً: فلسفة التسعير ومحركات التكلفة في AWS

### 1. المبادئ الثلاثة لتسعير AWS (`AWS Pricing Philosophy`)
1. **الدفع حسب الاستهلاك (`Pay-as-you-go`):** تدفع فقط مقابل الموارد التي تستخدمها فعلياً وللفترة التي تعمل فيها فقط، دون عقود إلزامية طويلة الأمد، مما يمنحك مرونة كاملة في التوسع أو الإيقاف.
2. **التوفير مقابل الالتزام (`Save when you reserve`):** عند الالتزام بالاستخدام لمدة **سنة أو 3 سنوات** عبر **`Savings Plans`** أو **`Reserved Instances`**، تحصل على خصومات كبيرة تصل إلى **72%** مقارنة بالتسعير عند الطلب (`On-Demand`).
3. **كلما زاد الاستخدام انخفضت تكلفة الوحدة (`Pay less by using more`):** تطبق AWS خصومات متدرجة بناءً على الحجم (**`Volume-based Discounts`**) في خدمات مثل `Amazon S3` ونقل البيانات؛ فكلما ارتفع استهلاكك الشهري قلّ سعر الجيجابايت الواحد.

### 2. محركات التكلفة الأساسية الثلاثة (`The 3 Fundamental Cost Drivers`)
في معظم البنى السحابية، تتكون فاتورتك الشهرية من ثلاثة عناصر رئيسية:
1. **الحوسبة (`Compute`):** ساعات أو ثواني تشغيل الخوادم (`Amazon EC2`) أو عدد طلبات وزمن تنفيذ الدوال (`AWS Lambda`).
2. **التخزين (`Storage`):** حجم البيانات المخزنة شهرياً (`GB/month`) وفئة التخزين المستخدمة (`Amazon S3`, `EBS`, `RDS`).
3. **نقل البيانات الصادر (`Outbound Data Transfer`):**
   * **قاعدة جوهرية في الاختبار:** إدخال البيانات من الإنترنت إلى سحابة AWS (**`Data Transfer IN`**) **مجاني تماماً ($0)** في معظم الخدمات، بينما تُحتسب الرسوم على **نقل البيانات الصادر (`Data Transfer OUT`)** من AWS إلى الإنترنت العام أو بين الـ `Regions` المختلفة.

### 3. الطبقة المجانية (`AWS Free Tier`)
تنقسم العروض المجانية في AWS إلى ثلاث فئات محددة:
* **`Always Free` (مجاني بشكل دائم):** خدمات تمنح حصة مجانية شهرية لا تنتهي بانتهاء العام الأول، مثل **1 مليون طلب شهرياً** على `AWS Lambda`، و **25 GB** تخزين على `Amazon DynamoDB`، و **1 مليون طلب** على `Amazon SQS`.
* **`12 Months Free` (مجاني لمدة 12 شهراً من فتح الحساب):** مثل **750 ساعة شهرياً** من `Amazon EC2` (`t2.micro` / `t3.micro`)، و **5 GB** على `Amazon S3 Standard`، و **750 ساعة** من `Amazon RDS` (`Single-AZ`).
* **`Short-Term Trials` (فترات تجريبية محدودة):** تجارب مجانية لمدة 30 أو 60 يوماً لخدمات متخصصة مثل `Amazon SageMaker` أو `Amazon Redshift` أو `Amazon GuardDuty`.

---

## ثانياً: أدوات إدارة التكاليف والتحليل المالي (`Billing & Cost Management Tools`)

يخلط الكثيرون بين أدوات الفوترة في AWS؛ يوضح الجدول التالي الوظيفة الدقيقة لكل أداة والفرق الجوهري بينها:

| الأداة | الوظيفة الدقيقة والتفاصيل التشغيلية | الاستخدام الأمثل في الاختبار |
| :--- | :--- | :--- |
| **`AWS Pricing Calculator`** | أداة ويب مجانية تتيح نمذجة وتقدير التكلفة الشهرية والسنوية لمعماريتك المقترحة **قبل بناء أي موارد فعلية**، مع إمكانية مقارنة خيارات التسعير (`On-Demand` مقابل `Savings Plans`). | تقدير التكلفة المبدئية **قبل النشر (`Before deploying`)**. |
| **`AWS Budgets`** | أداة لوضع حدود مالية أو حدود استخدام مخصصة، وإرسال **تنبيهات تلقائية (`Alerts`)** عبر البريد الإلكتروني أو `SNS` عندما يتجاوز الصرف الفعلي أو المتوقع (`Forecasted`) الحد المرسوم. تدعم أيضاً إجراءات تلقائية (`Budget Actions`) لتقييد الموارد. | تلقي **إشعارات وتنبيهات** عند تجاوز الميزانية المحددة. |
| **`AWS Cost Explorer`** | واجهة تفاعلية لتحليل وتصوير أنماط الإنفاق التاريخية (حتى **13 شهراً سابقاً**)، و**التنبؤ بالإنفاق المستقبلي حتى 12 شهراً قادماً (`Forecasting`)**، مع تقديم توصيات لشراء `Savings Plans` و `Reserved Instances`. | **الرسوم البيانية والتحليل التاريخي والتنبؤ المستقبلي** بالتكاليف. |
| **`AWS Cost and Usage Report (CUR)`** | أكثر ملفات الفوترة **تفصيلاً وشمولية (`Most comprehensive & granular`)**؛ يُصدر تلقائياً في `Amazon S3` بصيغة `CSV` أو `Parquet` متضمناً تفاصيل الاستهلاك بالساعة لكل مورد وخدمة ووسم (`Tag`)، ويمكن تحليله باستخدام `Amazon Athena` و `QuickSight`. | الحصول على **أدق بيانات فوترة تفصيلية** للتحليل المالي العميق. |
| **`Cost Allocation Tags`** | وسوم تعريفية (`Key-Value pairs` مثل `Department: Finance` أو `Environment: Prod`) تُضاف إلى موارد AWS لتوزيع الفاتورة وتحديد إنفاق كل قسم أو مشروع أو عميل بدقة. | **تتبع وتصنيف التكاليف** حسب المشروع أو القسم أو البيئة. |
| **`AWS Compute Optimizer`** | أداة تعتمد على **التعلم الآلي (`Machine Learning`)** لتحليل بيانات استهلاك الموارد (`EC2`, `EBS`, `Lambda`, `ECS`) وتقديم توصيات دقيقة لضبط الأحجام (**`Rightsizing`**) وتجنب الدفع مقابل سعة غير مستغلة. | توصيات **`Rightsizing`** المدعومة بالذكاء الاصطناعي. |
| **`AWS Cost Anomaly Detection`** | تستخدم التعلم الآلي لمراقبة أنماط الإنفاق واكتشاف أي **ارتفاع مفاجئ وغير طبيعي في الفاتورة (`Unusual Spend Spikes`)** وتنبيهك فوراً مع تحليل السبب الجذري. | كشف **الارتفاعات المفاجئة غير المتوقعة** في الفاتورة. |
| **`Consolidated Billing`** (ضمن `AWS Organizations`) | توحيد فواتير جميع الحسابات التابعة للمؤسسة في فاتورة واحدة، مع **تجميع الاستهلاك (`Combined Usage`)** للاستفادة من شرائح خصم الكميات الأعلى، ومشاركة خصومات `RI` و `Savings Plans` بين الحسابات. | إصدار **فاتورة موحدة** لعدة حسابات وتعظيم خصومات الكميات. |

---

## ثالثاً: باقات الدعم الفني (`AWS Support Plans`)

تقدم AWS خمس باقات دعم فني تتدرج من المجانية إلى باقات المؤسسات الكبرى. يُعد التمييز بين زمن الاستجابة (`SLA`) ومستوى الوصول إلى **`AWS Trusted Advisor`** و **`TAM`** من أهم نقاط الاختبار:

| الباقة (`Support Plan`) | التكلفة التقديرية | الدعم التقني وأسرع زمن استجابة (`Response SLA`) | المزايا الحصرية ونقاط الاختبار الجوهرية |
| :--- | :---: | :--- | :--- |
| **`Basic Support`** | **مجاني (`$0`)** | دعم لحساب الفوترة والخدمات العامة فقط (**لا يوجد دعم تقني هندسي**). | وصول إلى الوثائق والمنتديات + `AWS Health Dashboard` + **الفحوصات السبعة الأساسية فقط (`7 Core Checks`)** في `Trusted Advisor`. |
| **`Developer Support`** | تبدأ من **`$29/شهر`** | دعم تقني عبر **البريد الإلكتروني فقط** خلال ساعات العمل: أقل من **24 ساعة** للإرشاد العام، وأقل من **12 ساعة** عند تعطل النظام (`System Impaired`). | مخصص لبيئات التطوير والاختبار؛ يتيح لشخص واحد فقط فتح تذاكر دعم تقني. |
| **`Business Support`** | تبدأ من **`$100/شهر`** | **دعم تقني 24/7** عبر الهاتف والدردشة والبريد الإلكتروني: أقل من **1 ساعة** عند تعطل بيئة الإنتاج (**`Production System Down`**). | **أقل باقة تكلفةً تفتح جميع فحوصات `AWS Trusted Advisor` الكاملة (`Full Set`)** + الوصول إلى `AWS Support API` + دعم برمجيات الطرف الثالث (`Third-party software`). |
| **`Enterprise On-Ramp`** | تبدأ من **`$5,500/شهر`** | دعم تقني 24/7: أقل من **30 دقيقة** عند تعطل نظام حيوي للأعمال (**`Business-Critical System Down`**). | وصول إلى **مجموعة مشتركة من مهندسي `TAM` (`Pool of TAMs`)** + فريق `Concierge Support` للفواتير + مراجعة سنوية واحدة للـ `Well-Architected` + فعالية `IEM` واحدة سنوياً. |
| **`Enterprise Support`** | تبدأ من **`$15,000/شهر`** | **أسرع استجابة في AWS: أقل من 15 دقيقة** عند تعطل نظام حيوي للأعمال (**`Business-Critical System Down`**). | **مهندس حسابات تقني مخصص لك وحدك (`Designated Technical Account Manager — TAM`)** + فريق **`AWS Support Concierge`** (لإدارة الفواتير والحسابات) + دعم **`Infrastructure Event Management (IEM)`** مجاناً لإطلاق المنتجات الكبرى والمواسم. |

### لوحة الحالة الصحية لـ AWS (`AWS Health Dashboard: Service Health vs. Account Health`)
توفر AWS مجاناً (حتى في باقة `Basic Support`) لوحة متابعة صحية تنقسم إلى عرضين مهمين في الاختبار:
* **`Service Health` (العرض العام العالمي — `Global / Public`):** متاح للجميع دون تسجيل دخول؛ يعرض الحالة التشغيلية العامة لجميع خدمات AWS في كل الـ `Regions` حول العالم (هل هناك عطل عام في `us-east-1`؟).
* **`Account Health` (العرض الشخصي المخصص — `Personal / Account-Specific`):** يتطلب تسجيل الدخول لحسابك؛ يعرض فقط الأعطال النشطة، أو الصيانات المجدولة (`Scheduled Maintenance`)، أو الإشعارات الأمنية التي **تؤثر مباشرة على مواردك الفعلية** (مثل خادم `EC2` أو قاعدة بيانات `RDS` في حسابك)، ويمكن ربطها بـ `Amazon EventBridge` لأتمتة التنبيهات.

---

## رابعاً: السوق الرقمي وشبكة الشركاء (`AWS Marketplace` & `APN`)

* **`AWS Marketplace`:** كتالوج رقمي مُدار يضم آلاف البرمجيات والخدمات الجاهزة من شركات تقنية عالمية (مثل جدران حماية Palo Alto و Cisco، وأنظمة قواعد بيانات، وحلول ذكاء اصطناعي). يتيح لك البحث عنها وشراءها ونشرها مباشرةً في حسابك مع **دمج تكلفتها تلقائياً داخل فاتورة AWS الموحدة**.
* **`AWS Partner Network (APN)`:** شبكة عالمية من الشركاء المعتمدين تنقسم إلى شركاء خدمات استشارية وتنفيذية (`Services / Consulting Partners`) وشركاء برمجيات (`Technology / Software Partners`) لمساعدة المؤسسات في التخطيط والانتقال وبناء الحلول على AWS.
* **`AWS Professional Services`:** فريق استشاري عالمي تابع مباشرة لشركة AWS يعمل جنباً إلى جنب مع فرق المؤسسات الكبرى وشركاء `APN` لتسريع مشاريع التحول السحابي المعقدة.

---

## منهجية التعامل مع أسئلة Domain 4 في الاختبار

| مؤشر أو عبارة في نص السؤال | الإجابة الدقيقة |
| :--- | :--- |
| **Estimate the monthly cost of a planned AWS architecture before deployment** | **`AWS Pricing Calculator`** |
| **Set a spending limit and send an email/SNS alert when exceeded** | **`AWS Budgets`** |
| **Visualize historical spending trends and forecast costs for the next 12 months** | **`AWS Cost Explorer`** |
| **Obtain the most detailed, hourly, granular billing dataset stored in S3** | **`AWS Cost and Usage Report (CUR)`** |
| **Categorize and track AWS spend by department, project, or environment** | **`Cost Allocation Tags`** |
| **Lowest-cost support plan with 24/7 technical support and Full Trusted Advisor checks** | **`AWS Business Support`** |
| **Support plan providing a Designated TAM and 15-minute response SLA** | **`AWS Enterprise Support`** |
| **Support plan providing 30-minute SLA and access to a Pool of TAMs** | **`AWS Enterprise On-Ramp`** |
| **Billing and account specialists (Concierge Support Team)** | **`AWS Enterprise Support` / `Enterprise On-Ramp`** |
| **Purchase and deploy third-party pre-configured software on your AWS bill** | **`AWS Marketplace`** |
| **Cost of uploading data INTO AWS from the internet (`Data Transfer IN`)** | **مجاني (`$0` / Free)** |

---

> **الدرس السابق:** [Domain 3 — الجزء الثالث](./03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md) | **الدرس التالي (المرجع النهائي قبل الاختبار):** 👉 [05_Exam_Tricks_and_Comparison_CheatSheet.md](./05_Exam_Tricks_and_Comparison_CheatSheet.md) | [الفهرس الرئيسي](./README.md)

</div>
