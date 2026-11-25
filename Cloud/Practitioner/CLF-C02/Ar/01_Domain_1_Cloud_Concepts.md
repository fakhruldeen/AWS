<div dir="rtl">

# Domain 1: Cloud Concepts — مفاهيم الحوسبة السحابية (24% من الاختبار)

يمثل المجال الأول **24%** من إجمالي درجات اختبار `CLF-C02`. يركز هذا المجال على فهم القيمة الاقتصادية والتشغيلية للحوسبة السحابية، وهيكل البنية التحتية العالمية لـ **AWS**، وأطر العمل القياسية التي تعتمدها المؤسسات لتصميم الأنظمة السحابية والانتقال إليها بكفاءة وأمان.

---

## أولاً: تعريف الحوسبة السحابية ونماذجها (Cloud Computing & Models)

### 1. ما هي الحوسبة السحابية (`Cloud Computing`)؟
هي التوفير الفوري عند الطلب (`On-demand delivery`) لموارد تقنية المعلومات — مثل القدرة الحاسوبية (`Compute`)، والتخزين (`Storage`)، وقواعد البيانات (`Databases`)، والشبكات (`Networking`)، وتقنيات الذكاء الاصطناعي — عبر شبكة الإنترنت، مع نظام تسعير يعتمد على الاستهلاك الفعلي (`Pay-as-you-go pricing`). بدلاً من شراء مراكز بيانات وخوادم مادية وامتلاكها وصيانتها، تستأجر المؤسسة ما تحتاجه فقط من مزود سحابي مثل **AWS**.

### 2. نماذج الخدمة السحابية (Cloud Service Models: `IaaS`, `PaaS`, `SaaS`)
تحدد هذه النماذج حجم المسؤولية التقنية التي تتحملها المؤسسة مقارنة بما تتولاه AWS:
* **البنية التحتية كخدمة (`IaaS` — Infrastructure as a Service):** توفر AWS الموارد الأساسية (خوادم افتراضية، شبكات، تخزين)، بينما يدير العميل أنظمة التشغيل والتطبيقات والبيانات. *مثال:* **[`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2)**, **[`Amazon VPC`](../AWS_SERVICES_GLOSSARY.md#amazon-vpc)**.
* **المنصة كخدمة (`PaaS` — Platform as a Service):** تتولى AWS إدارة البنية التحتية وأنظمة التشغيل وبيئة التشغيل، ويركّز العميل فقط على نشر وإدارة الكود البرمجي والبيانات. *مثال:* **[`AWS Elastic Beanstalk`](../AWS_SERVICES_GLOSSARY.md#aws-elastic-beanstalk)**, **[`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds)**.
* **البرمجيات كخدمة (`SaaS` — Software as a Service):** منتج برمجي كامل وجاهز للاستخدام النهائي تديره الشركة المزودة بالكامل. *مثال:* **`Amazon WorkMail`**, **[`Amazon QuickSight`](../AWS_SERVICES_GLOSSARY.md#amazon-quicksight)**, أو خدمات البريد السحابي وتطبيقات الـ CRM.

### 3. نماذج النشر السحابي (`Cloud Deployment Models`)
1. **السحابة الكاملة (`Cloud-Based / All-in on Cloud`):** جميع أجزاء التطبيق والبنية التحتية تعمل بالكامل على AWS دون أي خوادم محلية.
2. **المحلي (`On-Premises / Private Cloud`):** نشر الموارد داخل مركز البيانات الخاص بالمؤسسة باستخدام أدوات المحاكاة الافتراضية، مع تحمل المؤسسة كامل تكاليف العتاد والإدارة.
3. **الهجين (`Hybrid Cloud`):** ربط البنية التحتية المحلية (`On-Premises`) بالموارد السحابية على AWS للعمل كمنظومة واحدة متكاملة. يُستخدم هذا النموذج بكثرة عند وجود متطلبات تنظيمية تلزم بإبقاء بعض البيانات الحساسة داخل مقر المؤسسة، أو أثناء مراحل الانتقال التدريجي للسحابة.

---

## ثانياً: المزايا الست للحوسبة السحابية (The 6 Advantages of Cloud Computing)

تُعد هذه المزايا الست ركيزة أساسية تتكرر بصياغات متعددة في اختبار `CLF-C02`:

| الميزة (`Advantage`) | الشرح المفصّل والأثر العملي |
| :--- | :--- |
| **1. Trade fixed expense for variable expense** | تحويل النفقات الرأسمالية الثابتة (`CapEx`) التي تتطلب دفع مبالغ كبيرة مقدماً إلى نفقات تشغيلية متغيرة (`OpEx`) تُدفع فقط مقابل ما يتم استهلاكه فعلياً. |
| **2. Benefit from massive economies of scale** | بفضل تجميع استهلاك مئات الآلاف من العملاء حول العالم، تحقق AWS وفورات حجم هائلة (**Economies of Scale**) تنعكس على هيئة أسعار أقل بكثير مما تستطيع أي مؤسسة منفردة تحقيقه بمفردها. |
| **3. Stop guessing capacity** | التخلص من مشكلة التخمين الخاطئ للسعة؛ ففي النموذج التقليدي إما أن تشتري المؤسسة خوادم زائدة تظل خاملة لشهور (`Over-provisioning`)، أو خوادم أقل من الطلب فتتوقف الخدمة وقت الذروة (`Under-provisioning`). في السحابة تتوسع الموارد وتنكمش تلقائياً حسب الطلب الفعلي. |
| **4. Increase speed and agility** | زيادة سرعة الإنجاز والمرونة التنظيمية (`Agility`)؛ بدلاً من انتظار أسابيع لشراء وتجهيز خادم جديد، يمكن توفير الموارد في دقائق معدودة، مما يتيح للفرق الهندسية إجراء التجارب (`Experimentation`) بتكلفة منخفضة جداً وإلغاء الموارد فوراً إذا لم تنجح الفكرة. |
| **5. Stop spending money running and maintaining data centers** | توجيه الميزانية والجهد الهندسي نحو تطوير المنتجات وخدمة العملاء (ما يُعرف بـ **Differentiating work**) بدلاً من استنزافها في صيانة الأجهزة والتبريد والكهرباء (**Undifferentiated heavy lifting**). |
| **6. Go global in minutes** | القدرة على نشر التطبيقات في مناطق جغرافية متعددة حول العالم خلال دقائق، مما يقلل زمن الاستجابة (`Latency`) ويقدم تجربة استخدام سريعة للعملاء في أي قارة. |

---

## ثالثاً: البنية التحتية العالمية لـ AWS (AWS Global Infrastructure)

تعتمد AWS على بنية تحتية عالمية مصممة لتحقيق أعلى مستويات التوافر (`High Availability`) والاعتمادية (`Fault Tolerance`):

### 1. المناطق الجغرافية (`AWS Regions`)
الـ **`Region`** هي منطقة جغرافية محددة حول العالم (مثل `us-east-1` في شمال فرجينيا، و `eu-north-1` في ستوكهولم، و `me-central-1` في الإمارات). كل `Region` معزولة تماماً عن المناطق الأخرى لتحقيق أقصى درجات الاستقلالية والأمان، ولا يتم نسخ بياناتك خارج الـ `Region` التي اخترتها إلا بأمر صريح منك.

**العوامل الأربعة لاختيار الـ `Region` المناسبة (نقطة اختبار مهمة):**
1. **الامتثال القانوني وسيادة البيانات (`Compliance & Data Governance`):** قد تفرض القوانين المحلية بقاء بيانات المواطنين أو البنوك داخل حدود جغرافية محددة.
2. **القرب من المستخدمين (`Proximity / Latency`):** اختيار أقرب منطقة جغرافية للجمهور المستهدف لتقليل زمن الاستجابة.
3. **توافر الخدمات (`Available Services`):** بعض الخدمات الحديثة لا تتوفر في جميع الـ `Regions` في وقت واحد.
4. **التسعير (`Pricing`):** تختلف تكلفة الموارد بشكل طفيف من `Region` إلى أخرى تبعاً لتكاليف التشغيل والطاقة المحلية.

### 2. مناطق التوافر (`Availability Zones — AZs`)
* تتكون كل `Region` من عدة **`Availability Zones`** (ثلاث على الأقل، وقد تصل إلى ست في بعض المناطق، مثل `eu-north-1a`, `eu-north-1b`, `eu-north-1c`).
* تتألف كل `AZ` من مركز بيانات فعلي واحد أو أكثر (**Data Centers**)، ولها مصادر طاقة وتبريد وأنظمة أمن وشبكات مستقلة تماماً.
* تفصل بين الـ `AZs` داخل نفس الـ `Region` مسافة جغرافية مدروسة (عادةً عشرات الكيلومترات) بحيث لا تتأثر جميعها بكارثة طبيعية واحدة، وفي الوقت نفسه ترتبط ببعضها عبر كابلات ألياف ضوئية خاصة فائقة السرعة (`Ultra-low latency`) تتيح النسخ المتزامن للبيانات (`Synchronous Replication`).

### 3. نقاط الطرف (`Edge Locations`) وذاكرة التخزين الإقليمية (`Regional Edge Caches`)
* هي مئات المواقع الموزعة في المدن الكبرى حول العالم (أكثر بكثير من عدد الـ `Regions`).
* تُستخدم بشكل أساسي مع خدمة **[`Amazon CloudFront`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudfront)** (شبكة توصيل المحتوى `CDN`) لتخزين نسخ مؤقتة (`Caching`) من الملفات الثابتة والفيديوهات بالقرب من المستخدم النهائي، وكذلك مع **[`Amazon Route 53`](../AWS_SERVICES_GLOSSARY.md#amazon-route-53)** و **[`AWS WAF`](../AWS_SERVICES_GLOSSARY.md#aws-waf)** و **[`AWS Shield`](../AWS_SERVICES_GLOSSARY.md#aws-shield)**.

### 4. امتدادات البنية التحتية الهجينة والطرفية
* **[`AWS Local Zones`](../AWS_SERVICES_GLOSSARY.md#aws-local-zones):** تنقل خدمات الحوسبة والتخزين وقواعد البيانات إلى مدن كبرى لا تحتوي على `Region` كاملة، لتلبية التطبيقات التي تتطلب زمن استجابة بأجزاء من الملي ثانية (`Single-digit millisecond latency`) مثل البث المباشر والألعاب والتصميم الهندسي.
* **[`AWS Wavelength`](../AWS_SERVICES_GLOSSARY.md#aws-wavelength):** تدمج موارد AWS مباشرة داخل شبكات الجيل الخامس **`5G`** لشركات الاتصالات، مما يمنح تطبيقات الهواتف الذكية والسيارات ذاتية القيادة استجابة شبه فورية دون الخروج إلى الإنترنت العام.
* **[`AWS Outposts`](../AWS_SERVICES_GLOSSARY.md#aws-outposts):** خدمة مُدارة بالكامل تتيح لـ AWS شحن وتثبيت خزائن عتادية فعلية (`Physical Hardware Racks`) داخل مركز البيانات المحلي الخاص بالعميل (`On-Premises`)، بحيث تعمل بنفس واجهات برمجة التطبيقات (`APIs`) وأدوات الإدارة الموجودة في سحابة AWS.

---

## رابعاً: إطار العمل المعماري الجيد (`AWS Well-Architected Framework`)

يُعد **`AWS Well-Architected Framework`** الدليل الهندسي المرجعي الذي وضعته AWS لمساعدة المعماريين والمهندسين على تصميم وبناء وتشغيل أنظمة سحابية آمنة، عالية الأداء، مرنة، واقتصادية. وهو يجيب عن سؤال: **"كيف نصمّم التطبيق والبنية التحتية على السحابة بشكل صحيح؟"**

### 1. المبادئ التصميمية العامة الستة (`6 General Design Principles`)
قبل الدخول في الأعمدة الستة، يضع الإطار ستة مبادئ عامة تنطبق على جميع الأنظمة السحابية:
1. **`Stop guessing your capacity needs`:** التوقف عن تخمين السعة المطلوبة لسنوات قادمة والاعتماد على التوسع التلقائي (`Auto Scaling`).
2. **`Test systems at production scale`:** إنشاء نسخة اختبار مطابقة تماماً لبيئة الإنتاج، إجراء اختبارات الضغط، ثم حذفها خلال ساعات بدفع تكلفة ساعات الاختبار فقط.
3. **`Automate to make architectural experimentation easier`:** أتمتة البنية التحتية ككود (`Infrastructure as Code`) لتسهيل التجربة والتراجع الآمن دون عمل يدوي متكرر.
4. **`Allow for evolutionary architectures`:** تصميم أنظمة قابلة للتطور المستمر مع ظهور خدمات سحابية أحدث وأرخص دون قيود تقنية جامدة.
5. **`Drive architectures using data`:** اتخاذ القرارات المعمارية بناءً على بيانات وقياسات حقيقية (`CloudWatch Metrics`, `Logs`) لا على التخمين.
6. **`Improve through game days`:** محاكاة الأعطال والهجمات الدورية (`Game Days`) لاختبار جاهزية الفريق وخطط الاستعادة قبل وقوع أزمة حقيقية.

---

### 2. الشرح التفصيلي للأعمدة الستة (`The 6 Pillars`)

#### العمود الأول: `Operational Excellence` (التميز التشغيلي)
* **الهدف الأساسي:** تشغيل ومراقبة الأنظمة لتقديم قيمة مستمرة للأعمال، والتحسين الدائم للعمليات والإجراءات التشغيلية.
* **المبادئ التصميمية الأساسية (`Design Principles` — مهمة جداً في الاختبار):**
  * **`Perform operations as code`:** تعريف البنية التحتية وإجراءات التشغيل بالكامل ككود ([`AWS CloudFormation`](../AWS_SERVICES_GLOSSARY.md#aws-cloudformation), [`AWS CDK`](../AWS_SERVICES_GLOSSARY.md#aws-cdk)) لتقليل الأخطاء البشرية.
  * **`Make frequent, small, reversible changes`:** تنفيذ تحديثات صغيرة ومتكررة يسهل التراجع عنها فوراً إذا ظهر خلل.
  * **`Refine operations procedures frequently`:** مراجعة وتحديث أدلة التشغيل (`Runbooks`) باستمرار مع تطور النظام.
  * **`Anticipate failure`:** إجراء تدريبات استباقية (`Pre-mortems`) لاكتشاف نقاط الضعف قبل إطلاق النظام.
  * **`Learn from all operational failures`:** تحليل السبب الجذري (`Root Cause Analysis`) لكل عطل وتحويل الدروس المستفادة إلى تحسينات مؤتمتة.
* **أبرز خدمات AWS المرتبطة:** [`AWS CloudFormation`](../AWS_SERVICES_GLOSSARY.md#aws-cloudformation), [`AWS Systems Manager`](../AWS_SERVICES_GLOSSARY.md#aws-systems-manager), [`Amazon CloudWatch`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudwatch), [`AWS Config`](../AWS_SERVICES_GLOSSARY.md#aws-config).

#### العمود الثاني: `Security` (الأمان)
* **الهدف الأساسي:** حماية البيانات والأنظمة والأصول السحابية من خلال تقييم المخاطر وتطبيق الضوابط الأمنية في كل طبقة.
* **المبادئ التصميمية الأساسية:**
  * **`Implement a strong identity foundation`:** تطبيق مبدأ أقل الصلاحيات (`Least Privilege`)، المركزية في الهويات (`IAM Identity Center`)، وتفعيل `MFA`.
  * **`Enable traceability`:** تسجيل ومراقبة جميع الأنشطة والتغييرات في الوقت الفعلي ([`AWS CloudTrail`](../AWS_SERVICES_GLOSSARY.md#aws-cloudtrail), `CloudWatch`).
  * **`Apply security at all layers (Defense in Depth)`:** عدم الاعتماد على خط دفاع واحد؛ بل تأمين الحافة (`WAF`/`Shield`) والشبكة (`NACLs`/`Security Groups`) والنظام والبيانات معاً.
  * **`Automate security best practices`:** معالجة الإعدادات الخاطئة تلقائياً عبر [`AWS Config`](../AWS_SERVICES_GLOSSARY.md#aws-config) و `Lambda`.
  * **`Protect data in transit and at rest`:** فرض التشفير أثناء النقل (`TLS/HTTPS`) وأثناء السكون ([`AWS KMS`](../AWS_SERVICES_GLOSSARY.md#aws-kms)).
  * **`Keep people away from data`:** تقليل وصول البشر المباشر للبيانات الحساسة واستخدام خطوط معالجة مؤتمتة.
  * **`Prepare for security events`:** إعداد خطط استجابة جاهزة ومحاكاة الحوادث الأمنية.
* **أبرز خدمات AWS المرتبطة:** [`AWS IAM`](../AWS_SERVICES_GLOSSARY.md#aws-iam), [`AWS KMS`](../AWS_SERVICES_GLOSSARY.md#aws-kms), [`AWS Secrets Manager`](../AWS_SERVICES_GLOSSARY.md#aws-secrets-manager), [`AWS Shield`](../AWS_SERVICES_GLOSSARY.md#aws-shield), [`AWS WAF`](../AWS_SERVICES_GLOSSARY.md#aws-waf), [`Amazon GuardDuty`](../AWS_SERVICES_GLOSSARY.md#amazon-guardduty), [`AWS Security Hub`](../AWS_SERVICES_GLOSSARY.md#aws-security-hub), [`AWS CloudTrail`](../AWS_SERVICES_GLOSSARY.md#aws-cloudtrail).

#### العمود الثالث: `Reliability` (الاعتمادية)
* **الهدف الأساسي:** ضمان قدرة النظام على أداء وظيفته المطلوبة بدقة واستمرارية، والتعافي السريع والتلقائي من أي عطل.
* **المبادئ التصميمية الأساسية:**
  * **`Automatically recover from failure`:** مراقبة مؤشرات الأداء وتفعيل الاستبدال والتعافي التلقائي (`Auto Scaling`, `RDS Multi-AZ`, `Route 53 Failover`).
  * **`Test recovery procedures`:** اختبار النسخ الاحتياطية وعمليات التحويل الطارئ بانتظام (مثل [`AWS Fault Injection Service`](../AWS_SERVICES_GLOSSARY.md#aws-fault-injection-service)).
  * **`Scale horizontally to increase aggregate workload availability`:** استبدال خادم واحد ضخم بعدة خوادم صغيرة موزعة عبر أكثر من `AZ` لمنع نقطة الفشل الواحدة (`Single Point of Failure`).
  * **`Stop guessing capacity`:** ضبط السعة تلقائياً لمواجهة الزيادات المفاجئة دون انهيار الخدمة.
  * **`Manage change in automation`:** تطبيق التعديلات عبر خطوط أتمتة (`CI/CD`) لا عبر تعديلات يدوية عرضة للخطأ.
* **أبرز خدمات AWS المرتبطة:** [`Amazon EC2 Auto Scaling`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2-auto-scaling), `Elastic Load Balancing (ELB)`, [`Amazon Route 53`](../AWS_SERVICES_GLOSSARY.md#amazon-route-53), [`AWS Backup`](../AWS_SERVICES_GLOSSARY.md#aws-backup), [`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3).

#### العمود الرابع: `Performance Efficiency` (كفاءة الأداء)
* **الهدف الأساسي:** استخدام موارد الحوسبة بكفاءة مثلى لتلبية متطلبات النظام والحفاظ على هذه الكفاءة مع تغيّر حجم الطلب وتطور التقنيات.
* **المبادئ التصميمية الأساسية:**
  * **`Democratize advanced technologies`:** الاعتماد على خدمات AWS المُدارة لتقنيات معقدة (مثل [`Amazon SageMaker`](../AWS_SERVICES_GLOSSARY.md#amazon-sagemaker) و [`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds)) بدلاً من إدارتها يدوياً.
  * **`Go global in minutes`:** نشر التطبيق في عدة `Regions` واستخدام `Edge Locations` لتقليل زمن الاستجابة (`Latency`) عالمياً.
  * **`Use serverless architectures`:** التخلص من عبء إدارة الخوادم باستخدام [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda) و [`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate) و `DynamoDB`.
  * **`Experiment more often`:** تجربة أنواع مختلفة من الخوادم والتخزين بسرعة بفضل السحابة.
  * **`Consider mechanical sympathy`:** اختيار المورد الأنسب لطبيعة العمل (مثلاً خوادم `Memory-Optimized` للذاكرة المؤقتة، و `Compute-Optimized` للحسابات المكثفة).
* **أبرز خدمات AWS المرتبطة:** [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda), [`Amazon CloudFront`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudfront), [`Amazon ElastiCache`](../AWS_SERVICES_GLOSSARY.md#amazon-elasticache), [`AWS Compute Optimizer`](../AWS_SERVICES_GLOSSARY.md#aws-compute-optimizer).

#### العمود الخامس: `Cost Optimization` (تحسين التكلفة)
* **الهدف الأساسي:** تشغيل الأنظمة بأقل تكلفة ممكنة تحقق القيمة المرجوة للأعمال دون إهدار مالي.
* **المبادئ التصميمية الأساسية:**
  * **`Implement Cloud Financial Management (FinOps)`:** بناء ثقافة وإدارة مالية واعية لتكاليف السحابة.
  * **`Adopt a consumption model`:** الدفع فقط مقابل الموارد المستهلكة فعلياً وإيقاف بيئات التطوير خارج أوقات العمل.
  * **`Measure overall efficiency`:** قياس العائد التجاري مقارنة بتكلفة تشغيل البنية التحتية.
  * **`Stop spending money on undifferentiated heavy lifting`:** الاعتماد على خدمات AWS المُدارة بدلاً من الإنفاق على صيانة الخوادم ومراكز البيانات.
  * **`Analyze and attribute expenditure`:** استخدام `Cost Allocation Tags` لتحديد إنفاق كل مشروع أو قسم بدقة.
* **أبرز خدمات AWS المرتبطة:** [`AWS Cost Explorer`](../AWS_SERVICES_GLOSSARY.md#aws-cost-explorer), [`AWS Budgets`](../AWS_SERVICES_GLOSSARY.md#aws-budgets), `Savings Plans`, `EC2 Spot Instances`, [`AWS Trusted Advisor`](../AWS_SERVICES_GLOSSARY.md#aws-trusted-advisor).

#### العمود السادس: `Sustainability` (الاستدامة البيئية)
* **الهدف الأساسي:** تقليل الأثر البيئي واستهلاك الطاقة والانبعاثات الكربونية الناتجة عن تشغيل الأنظمة السحابية.
* **المبادئ التصميمية الأساسية:**
  * **`Understand your impact`:** قياس البصمة الكربونية لأحمال عملك باستخدام **[`AWS Customer Carbon Footprint Tool`](../AWS_SERVICES_GLOSSARY.md#aws-customer-carbon-footprint-tool)**.
  * **`Establish sustainability goals`:** وضع أهداف طويلة المدى لخفض استهلاك الطاقة لكل وحدة عمل.
  * **`Maximize utilization`:** رفع نسبة استغلال الخوادم وحذف الموارد الخاملة (`Idle Resources`) لتجنب استهلاك كهرباء دون فائدة.
  * **`Adopt new, more efficient hardware and software offerings`:** الانتقال إلى معالجات **`AWS Graviton`** التي تستهلك طاقة أقل بنسبة تصل إلى 60% لنفس الأداء.
  * **`Use managed services`:** الخدمات المُدارة المشتركة (`S3`, `Lambda`) تعظّم كفاءة استخدام العتاد الفيزيائي.
  * **`Reduce the downstream impact`:** ضغط البيانات وتقليل حجم النقل لتقليل استهلاك الطاقة على أجهزة المستخدمين.

---

### 3. أداة المراجعة المجانية (`AWS Well-Architected Tool`)
توفر AWS أداة مجانية داخل لوحة التحكم تُسمى **[`AWS Well-Architected Tool`](../AWS_SERVICES_GLOSSARY.md#aws-well-architected-tool)** تتيح للمؤسسات مراجعة أنظمتها عبر الإجابة عن أسئلة منظمة للأعمدة الستة، ثم تُصدر تلقائياً تقريراً يحدد **المخاطر العالية والمتوسطة (`High/Medium-Risk Issues`)** وخطة تحسين عملية. كما تدعم **عدسات متخصصة (`Well-Architected Lenses`)** مثل `Serverless Lens`, `SaaS Lens`, و `Generative AI Lens`.

### 4. جدول التمييز بين الأعمدة المتشابهة في أسئلة الاختبار
كثيراً ما تتشابه الكلمات بين عمودين؛ استخدم هذه القاعدة الحاسمة للتفريق:

| الفكرة المتشابهة | إذا ركّز السؤال على... | فالعمود الصحيح هو... |
| :--- | :--- | :--- |
| **الأتمتة (`Automation`)** | كتابة الإجراءات والبنية التحتية ككود (`Runbooks / IaC`) وتحديثات صغيرة قابلة للتراجع | **`Operational Excellence`** |
| **الأتمتة (`Automation`)** | التعافي التلقائي من الأعطال وتجنب التوقف عبر خطوط `CI/CD` | **`Reliability`** |
| **الأتمتة (`Automation`)** | إصلاح الثغرات والإعدادات الأمنية الخاطئة تلقائياً | **`Security`** |
| **السعة والتوسع (`Scaling`)** | التوسع الأفقي للنجاة من الأعطال ومنع نفاد الموارد | **`Reliability`** |
| **السعة والتوسع (`Scaling`)** | تقليص الأحجام وإيقاف الموارد غير المستغلة لتخفيض الفاتورة الشهرية | **`Cost Optimization`** |
| **السعة والتوسع (`Scaling`)** | تعظيم استغلال العتاد وإلغاء الخوادم الخاملة لتقليل استهلاك الطاقة والكربون | **`Sustainability`** |

---

## خامساً: إطار تبني السحابة (`AWS Cloud Adoption Framework — AWS CAF 3.0`)

بينما يجيب `Well-Architected Framework` عن سؤال **"كيف نصمّم التطبيق تقنياً؟"**، يجيب **`AWS CAF`** عن سؤال **"كيف تنجح المؤسسة ككل (إدارةً وبشراً وعملياتٍ وتقنيةً) في التحول إلى السحابة بأقل مخاطر؟"**

### 1. نتائج الأعمال الأربع المستهدفة (`4 Foundational Business Outcomes`)
يربط `AWS CAF` التحول السحابي بأربع نتائج ملموسة تسأل عنها اختبارات `CLF-C02`:
1. **`Reduced business risk`:** تقليل المخاطر الأمنية والتنظيمية ومخاطر توقف الأعمال.
2. **`Improved ESG performance`:** تحسين الأداء البيئي والاجتماعي والحوكمة (خفض الانبعاثات الكربونية).
3. **`Increased revenue`:** زيادة الإيرادات عبر إطلاق منتجات رقمية جديدة والوصول لأسواق عالمية أسرع.
4. **`Increased operational efficiency`:** رفع الكفاءة التشغيلية وخفض التكاليف وتسريع إنتاجية الفرق.

### 2. مجالات التحول الأربعة (`4 Transformation Domains`)
* **`Technology`:** ترحيل وتحديث البنية التحتية والتطبيقات ومنصات البيانات.
* **`Process`:** رقمنة وأتمتة وتحسين إجراءات العمل اليومية باستخدام الذكاء الاصطناعي والتحليلات.
* **`Organization`:** إعادة هيكلة فرق العمل ونماذج التشغيل (بما في ذلك إنشاء **مركز تميز سحابي `Cloud Center of Excellence — CCoE`** يجمع ممثلي الأعمال والأمان والبنية التحتية لكسر العزلة بين الأقسام).
* **`Product`:** ابتكار نماذج عمل ومنتجات رقمية جديدة وتجربة عملاء متطورة.

### 3. المنظورات الستة في `AWS CAF` بالتفصيل (`6 Perspectives`)

| الفئة | المنظور (`Perspective`) | أصحاب المصلحة (`Stakeholders`) | الهدف الدقيق والقدرات الأساسية (`Core Capabilities`) |
| :---: | :--- | :--- | :--- |
| **Business** | **1. `Business`** | `CEO`, `CFO`, `COO`, مديرو الأعمال | ضمان توافق الاستثمار السحابي مع استراتيجية الشركة، قياس العائد (`ROI`)، إدارة المنتجات، الابتكار التجاري، وتحقيق القيمة (`Strategy & Value Realization`). |
| **Business** | **2. `People`** | `CHRO`, الموارد البشرية، التدريب | الجسر بين التقنية والبشر: **تطوير المهارات والتدريب والشهادات**، تطور الثقافة التنظيمية (`Culture Evolution`)، إدارة التغيير، واستقطاب الكفاءات. |
| **Business** | **3. `Governance`** | `CIO`, `CTO`, مديرو البرامج، `FinOps` | توجيه برامج التحول السحابي، إدارة المحفظة والمخاطر، **الإدارة المالية للسحابة (`Cloud Financial Management / FinOps`)**، وإدارة المنافع والتراخيص. |
| **Technical** | **4. `Platform`** | `CTO`, معماريو السحابة، مهندسو البيانات | تصميم وبناء البيئة السحابية الأساسية القابلة للتوسع (**`Landing Zones`**)، **هندسة البيانات (`Data Architecture`)**، تحديث التطبيقات، وخطوط `CI/CD`. |
| **Technical** | **5. `Security`** | `CISO`, مهندسو الأمن، التدقيق | ضمان السرية والسلامة والتوافر: إدارة الهويات (`IAM`)، حماية البيانات والتشفير، كشف التهديدات، إدارة الثغرات، الاستجابة للحوادث، والامتثال القانوني. |
| **Technical** | **6. `Operations`** | `COO`, مهندسو الاعتمادية (`SRE`), `ITSM` | ضمان تشغيل الخدمات يومياً وفق اتفاقيات مستوى الخدمة (`SLAs`): **المراقبة (`Observability`)**، إدارة الحوادث والتغييرات، والتعافي واستمرارية الأعمال. |

### 4. مراحل رحلة التحول السحابي الأربع (`4 Cloud Transformation Journey Phases`)
*(من أكثر نقاط `CAF` تكراراً في اختبار `CLF-C02`):*
1. **`Envision` (التصور والرؤية):** توضيح كيف تسرّع السحابة تحقيق أهداف الأعمال، وتحديد الفرص ذات الأثر الأعلى، وتوحيد رؤية الإدارة العليا.
2. **`Align` (المواءمة):** تحديد فجوات الجاهزية والقدرات عبر المنظورات الستة (`6 Perspectives`)، معالجة مخاوف أصحاب المصلحة، وبناء خطة عمل متوافقة.
3. **`Launch` (الإطلاق التجريبي):** تنفيذ مشاريع تجريبية (`Pilot Initiatives`) في بيئة الإنتاج لإثبات القيمة العملية بسرعة وتصحيح المسار قبل التوسع الشامل.
4. **`Scale` (التوسع المؤسسي):** تعميم النماذج الناجحة على نطاق المؤسسة بالكامل بأتمتة كاملة لتحقيق القيمة الاستراتيجية القصوى.

---

## سادساً: استراتيجيات الانتقال إلى السحابة (`The 7 Rs`) ومراحل الترحيل

عندما تقرر مؤسسة نقل عشرات أو مئات التطبيقات المحلية (`On-Premises`) إلى AWS، لا تنقلها جميعاً بنفس الطريقة؛ بل تصنف كل تطبيق وفق **استراتيجيات الانتقال السبع (`The 7 Rs of Cloud Migration`)**:

| الاستراتيجية | الوصف الدقيق | مثال عملي واقعي | السرعة | الجهد الهندسي | الفائدة السحابية طويلة المدى | الأداة الأساسية في AWS |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **1. `Rehost`** *(Lift-and-Shift)* | نقل الخوادم والتطبيقات كما هي **دون أي تعديل في الكود**. | عقد إيجار مركز البيانات ينتهي خلال شهر ونريد الإخلاء فوراً إلى `EC2`. | **الأسرع** | منخفض جداً | متوسطة | `AWS Application Migration Service (MGN)` |
| **2. `Replatform`** *(Lift, Tinker & Shift)* | نقل التطبيق مع **تعديل بسيط للاستفادة من خدمة مُدارة** دون إعادة كتابة الكود الأساسي. | نقل قاعدة `MySQL` مدارة يدوياً إلى **[`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds)** أو نقل التطبيق إلى `Elastic Beanstalk`. | سريعة | منخفض | متوسطة إلى عالية | [`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds), [`AWS DMS`](../AWS_SERVICES_GLOSSARY.md#aws-dms), `Elastic Beanstalk` |
| **3. `Repurchase`** *(Drop and Shop)* | الاستغناء عن النظام القديم وشراء منتج سحابي جاهز (**`SaaS`**). | إيقاف نظام `CRM` أو بريد محلي قديم والانتقال إلى Salesforce أو منتج من [`AWS Marketplace`](../AWS_SERVICES_GLOSSARY.md#aws-marketplace). | متوسطة | منخفض إلى متوسط | عالية | [`AWS Marketplace`](../AWS_SERVICES_GLOSSARY.md#aws-marketplace) |
| **4. `Refactor / Rearchitect`** | **إعادة تصميم وكتابة التطبيق بالكامل** بمعمارية سحابية أصلية (`Cloud-Native`). | تفكيك تطبيق متكامل قديم (`Monolith`) إلى `Microservices` باستخدام [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda) و `DynamoDB`. | **الأبطأ** | **الأعلى** | **الأعلى على الإطلاق** | [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda), `ECS/EKS`, `API Gateway`, `DynamoDB` |
| **5. `Relocate`** *(Hypervisor-Level Lift)* | نقل الآلات الافتراضية على مستوى الـ `Hypervisor` دون تغيير الكود أو عناوين `IP`. | نقل بيئة `VMware` المحلية مباشرة إلى **`VMware Cloud on AWS`**. | سريعة جداً | منخفض جداً | متوسطة | `VMware Cloud on AWS` |
| **6. `Retain`** *(Revisit)* | **الإبقاء على التطبيق محلياً** في الوقت الحالي لعدم جاهزيته أو لقيود تنظيمية. | نظام صناعي مرتبط بجهاز مادي خاص أو تم تحديثه حديثاً جداً. | — | صفر | — | [`AWS Outposts`](../AWS_SERVICES_GLOSSARY.md#aws-outposts), `Storage Gateway` |
| **7. `Retire`** *(Decommission)* | **إيقاف وحذف** التطبيقات القديمة غير المستخدمة (تمثل عادةً 10%–20% من تطبيقات الشركات). | نظام تقارير قديم لم يسجل أحد الدخول إليه منذ عامين. | فورية | منخفض جداً | **توفير مالي فوري** | [`AWS Application Discovery Service`](../AWS_SERVICES_GLOSSARY.md#aws-application-discovery-service) |

### مراحل الترحيل المؤسسي الثلاث (`3 Migration Phases — AWS MAP`):
1. **`Assess` (التقييم):** قياس جاهزية المؤسسة، واكتشاف الخوادم المحلية وتبعياتها ([`AWS Application Discovery Service`](../AWS_SERVICES_GLOSSARY.md#aws-application-discovery-service))، وبناء دراسة الجدوى والتكلفة الكلية ([`AWS Migration Evaluator`](../AWS_SERVICES_GLOSSARY.md#aws-migration-evaluator)).
2. **`Mobilize` (التجهيز والتعبئة):** سد فجوات المهارات، وبناء بيئة متعددة الحسابات آمنة (`Landing Zone` عبر [`AWS Control Tower`](../AWS_SERVICES_GLOSSARY.md#aws-control-tower))، وتنفيذ أول موجة تجريبية.
3. **`Migrate and Modernize` (الترحيل والتحديث):** تنفيذ الترحيل على نطاق واسع (`AWS MGN`, [`AWS DMS`](../AWS_SERVICES_GLOSSARY.md#aws-dms), `DataSync`, `Snow Family`) مع المتابعة المركزية عبر [`AWS Migration Hub`](../AWS_SERVICES_GLOSSARY.md#aws-migration-hub)، ثم التحديث التدريجي نحو الخدمات المُدارة و `Serverless`.

---

## سابعاً: مفاهيم التوسع والاستمرارية والتعافي من الكوارث

### 1. الفرق الدقيق بين `Scalability` و `Elasticity`
* **قابلية التوسع (`Scalability`):** قدرة النظام على استيعاب زيادة في حجم العمل عبر إضافة موارد، وتتم بطريقتين:
  * **التوسع العمودي (`Vertical Scaling / Scale Up`):** ترقية مواصفات نفس الخادم (زيادة الـ `CPU` والـ `RAM`). له حد أقصى ويتطلب غالباً إعادة تشغيل مؤقتة.
  * **التوسع الأفقي (`Horizontal Scaling / Scale Out`):** إضافة خوادم إضافية متطابقة للعمل معاً بالتوازي خلف موزع أحمال (`Load Balancer`). وهو النمط المفضل في الحوسبة السحابية.
* **المرونة التلقائية (`Elasticity`):** قدرة النظام على التوسع التلقائي (`Scale Out`) عند ارتفاع الطلب، **والانكماش التلقائي (`Scale In`)** عند انخفاض الطلب لتجنب دفع تكاليف موارد غير مستغلة.

### 2. التوافر العالي (`High Availability`) مقابل التسامح مع الأخطاء (`Fault Tolerance`)
* **`High Availability (HA)`:** تصميم النظام ليعمل بأقل زمن توقف ممكن (مثلاً توزيع الخوادم على `2 AZs` بحيث إذا تعطل أحدها يتحول العمل للآخر خلال ثوانٍ).
* **`Fault Tolerance (FT)`:** تصميم النظام بحيث يستمر في العمل دون أي انقطاع ملحوظ إطلاقاً (**Zero Downtime**) حتى عند تعطل مكون أساسي بالكامل (أعلى تكلفة وتعقيداً من `HA`).

### 3. التعافي من الكوارث (`Disaster Recovery — DR`)
يُقاس نجاح أي خطة تعافٍ من الكوارث بمؤشرين أساسيين:
* **`RTO` (Recovery Time Objective):** الحد الأقصى المسموح به للوقت منذ وقوع الكارثة وحتى عودة النظام للعمل.
* **`RPO` (Recovery Point Objective):** الحد الأقصى المسموح به لفقدان البيانات مقاساً بالزمن (الفترة الفاصلة بين آخر نسخة احتياطية ولحظة وقوع الكارثة).

**استراتيجيات التعافي الأربع (مرتبة من الأقل تكلفة إلى الأسرع استعادة):**
1. **`Backup and Restore`:** استعادة البيانات وإعادة بناء الموارد من النسخ الاحتياطية عند وقوع الكارثة (أقل تكلفة، أعلى `RTO` و `RPO`).
2. **`Pilot Light`:** إبقاء قاعدة البيانات الأساسية فقط تعمل بوضع مزامنة مستمرة، مع إيقاف خوادم التطبيق وتشغيلها فقط عند الطوارئ.
3. **`Warm Standby`:** تشغيل نسخة مصغّرة وكاملة من النظام بشكل مستمر في منطقة أخرى، وتوسيعها بسرعة عند حدوث عطل كبير.
4. **`Multi-Site Active-Active`:** تشغيل النظام بكامل طاقته في منطقتين جغرافيتين بالتوازي طوال الوقت (أقرب إلى الصفر في `RTO/RPO`، والأعلى تكلفة).

---

## منهجية التعامل مع أسئلة Domain 1 في الاختبار

| مؤشر أو عبارة في نص السؤال | المفهوم أو الخدمة المطابقة بدقة |
| :--- | :--- |
| **"Experiment quickly / deploy resources in minutes / reduce time to market"** | **`Agility`** |
| **"Automatically scale out during peak traffic and scale in during off-peak hours"** | **`Elasticity`** |
| **"Lower pay-as-you-go prices due to aggregate usage of hundreds of thousands of customers"** | **`Economies of Scale`** |
| **"Physically isolated data centers with independent power and cooling within a Region"** | **`Availability Zones (AZs)`** |
| **"Cache static content close to global users to reduce latency"** | **`Edge Locations` ([`Amazon CloudFront`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudfront))** |
| **"Run AWS managed infrastructure and services on-premises using AWS hardware"** | **[`AWS Outposts`](../AWS_SERVICES_GLOSSARY.md#aws-outposts)** |
| **"Embed AWS compute inside 5G telecommunication networks"** | **[`AWS Wavelength`](../AWS_SERVICES_GLOSSARY.md#aws-wavelength)** |
| **"Update workforce skills and organizational culture during cloud migration"** | **`People Perspective` (`AWS CAF`)** |
| **"Design cloud architecture, Landing Zones, and Data Architecture"** | **`Platform Perspective` (`AWS CAF`)** |
| **"Cloud Financial Management (FinOps), portfolio & risk oversight"** | **`Governance Perspective` (`AWS CAF`)** |
| **"4 phases of AWS CAF transformation journey"** | **`Envision → Align → Launch → Scale`** |
| **"Perform operations as code / frequent small reversible changes"** | **`Operational Excellence Pillar`** |
| **"Automatically recover from failure / horizontal scaling / test recovery"** | **`Reliability Pillar`** |
| **"Democratize advanced technologies / mechanical sympathy / serverless"** | **`Performance Efficiency Pillar`** |
| **"Minimize energy consumption and carbon footprint (`AWS Graviton`)"** | **`Sustainability Pillar`** |
| **"Free tool to review workloads against the 6 pillars and find high-risk issues"** | **[`AWS Well-Architected Tool`](../AWS_SERVICES_GLOSSARY.md#aws-well-architected-tool)** |
| **"Lift-and-shift with zero code changes (`AWS MGN`)"** | **`Rehost`** |
| **"Move self-managed DB to [`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds) without rewriting app code"** | **`Replatform`** |
| **"Rewrite monolith into cloud-native serverless microservices"** | **`Refactor / Rearchitect`** |
| **"Replace legacy in-house software with a commercial SaaS product"** | **`Repurchase`** |

---

> **الدرس السابق:** [الأساسيات التقنية](./00_Prerequisites_Asasiyat_ElCloud.md) | **الدرس التالي:** 👉 [02_Domain_2_Security_and_Compliance.md](./02_Domain_2_Security_and_Compliance.md) | [الفهرس الرئيسي](./README.md)

</div>
