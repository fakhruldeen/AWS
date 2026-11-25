<div dir="rtl">

# دليل المقارنات المعمارية ومنهجية حل أسئلة الاختبار (`X vs Y` & MCQ Strategy)

يجمع هذا المرجع الخلاصة التنفيذية لجميع المقارنات الدقيقة بين خدمات **AWS** المتشابهة التي تمثل المصدر الأول للالتباس في اختبار **`CLF-C02`**، متبوعاً بمنهجية منظمة لتحليل أسئلة الاختيار من متعدد (`Multiple Choice Questions`) واستبعاد الخيارات المضللة بدقة.

---

## أولاً: جدول المقارنات المعمارية الحاسمة (`X vs Y`)

### 1. مقارنات الأمن السيبراني والمراقبة (`Security & Observability`)

| المقارنة | الخدمة الأولى | الخدمة الثانية / الثالثة |
| :--- | :--- | :--- |
| **`Security Groups` vs `NACLs`** | **`Security Groups`:** تعمل على مستوى الخادم (**`EC2 Instance Level`**)، تدعم قواعد **`Allow` فقط**، وتتبع الحالة (**`Stateful`**). | **`NACLs`:** تعمل على مستوى الشبكة الفرعية (**`Subnet Level`**)، تدعم قواعد **`Allow` و `Deny`** (تُستخدم لحظر عنوان IP محدد)، ولا تتبع الحالة (**`Stateless`**). |
| **[`AWS Shield`](../AWS_SERVICES_GLOSSARY.md#aws-shield) vs [`AWS WAF`](../AWS_SERVICES_GLOSSARY.md#aws-waf)** | **[`AWS Shield`](../AWS_SERVICES_GLOSSARY.md#aws-shield):** حماية ضد هجمات حجب الخدمة الموزعة (**`DDoS`** — الطبقتين 3 و 4). | **[`AWS WAF`](../AWS_SERVICES_GLOSSARY.md#aws-waf):** جدار حماية لتطبيقات الويب (الطبقة السابعة `HTTP/HTTPS`) ضد **`SQL Injection`** و **`XSS`**. |
| **`GuardDuty` vs `Inspector` vs `Macie`** | **[`Amazon GuardDuty`](../AWS_SERVICES_GLOSSARY.md#amazon-guardduty):** كشف تهديدات ذكي مستمر بالتعلم الآلي لتحليل السجلات واكتشاف الأنشطة المشبوهة (مثل تعدين العملات أو مفاتيح مسروقة). | **[`Amazon Inspector`](../AWS_SERVICES_GLOSSARY.md#amazon-inspector):** فحص آلي **للثغرات البرمجية (`CVEs`)** في `EC2`, `ECR`, `Lambda`.<br>**[`Amazon Macie`](../AWS_SERVICES_GLOSSARY.md#amazon-macie):** اكتشاف وحماية **البيانات الشخصية الحساسة (`PII`)** داخل حاويات **[`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3)**. |
| **`CloudWatch` vs `CloudTrail` vs `Config`** | **[`Amazon CloudWatch`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudwatch):** مراقبة **الأداء والسجلات والإنذارات (`Metrics, Logs, Alarms`)** مثل ارتفاع `CPU`. | **[`AWS CloudTrail`](../AWS_SERVICES_GLOSSARY.md#aws-cloudtrail):** سجل تدقيق **من قام بأي إجراء (`API Auditing`)**.<br>**[`AWS Config`](../AWS_SERVICES_GLOSSARY.md#aws-config):** تتبع **تاريخ تغييرات الإعدادات (`Configuration History`)** وتقييم قواعد الامتثال. |
| **`Secrets Manager` vs `Parameter Store`** | **[`AWS Secrets Manager`](../AWS_SERVICES_GLOSSARY.md#aws-secrets-manager):** مخصص لبيانات الاعتماد الحساسة ويدعم **التدوير التلقائي (`Automatic Secret Rotation`)** — مدفوع. | **`SSM Parameter Store`:** مخزن لإعدادات التطبيقات البسيطة (مجاني في الطبقة القياسية) ولا يمتلك ميزة التدوير التلقائي الجاهزة. |
| **[`AWS KMS`](../AWS_SERVICES_GLOSSARY.md#aws-kms) vs [`AWS CloudHSM`](../AWS_SERVICES_GLOSSARY.md#aws-cloudhsm)** | **[`AWS KMS`](../AWS_SERVICES_GLOSSARY.md#aws-kms):** إدارة مفاتيح التشفير عبر عتاد أمني مُدار ومشترك (`Multi-tenant`). | **[`AWS CloudHSM`](../AWS_SERVICES_GLOSSARY.md#aws-cloudhsm):** جهاز عتادي مخصص ومفرد للعميل (`Single-tenant Dedicated Hardware`) لمتطلبات الامتثال الصارمة (`FIPS 140-2 Level 3`). |
| **`Trusted Advisor` vs `Inspector`** | **[`AWS Trusted Advisor`](../AWS_SERVICES_GLOSSARY.md#aws-trusted-advisor):** مستشار **للحساب بأكمله** يقدم توصيات في التكلفة والأمان والأداء والتسامح مع الأخطاء وحدود الخدمات. | **[`Amazon Inspector`](../AWS_SERVICES_GLOSSARY.md#amazon-inspector):** أداة فحص **للثغرات الأمنية البرمجية** داخل خوادم `EC2` والحاويات ودوال `Lambda`. |
| **`IAM Identity Center` vs [`Amazon Cognito`](../AWS_SERVICES_GLOSSARY.md#amazon-cognito)** | **`IAM Identity Center` (`AWS SSO`):** إدارة دخول **الموظفين (`Workforce`)** لعدة حسابات AWS وتطبيقات الأعمال (`SaaS`) بتسجيل دخول موحد. | **[`Amazon Cognito`](../AWS_SERVICES_GLOSSARY.md#amazon-cognito):** إدارة تسجيل ودخول **عملاء تطبيقات الويب والموبايل (`External Customers`)** بما يشمل Google و Apple و Facebook. |

---

### 2. مقارنات الحوسبة والتخزين (`Compute & Storage`)

| المقارنة | الخدمة الأولى | الخدمة الثانية / الثالثة |
| :--- | :--- | :--- |
| **[`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2) vs [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda)** | **[`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2):** خوادم افتراضية (`IaaS`) يدير العميل نظام تشغيلها وتعمل باستمرار حسب الحاجة. | **[`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda):** حوسبة **`Serverless`** مبنية على الأحداث؛ ترفع الكود فقط وتدفع مقابل زمن التنفيذ الفعلي بالملي ثانية (بحد أقصى 15 دقيقة). |
| **`S3` vs `EBS` vs `EFS`** | **[`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3):** **`Object Storage`** بسعة غير محدودة للملفات والنسخ الاحتياطية والمواقع الثابتة (لا يُثبّت عليه نظام تشغيل). | **[`Amazon EBS`](../AWS_SERVICES_GLOSSARY.md#amazon-ebs):** **`Block Storage`** لخادم `EC2` واحد داخل `AZ` واحدة.<br>**[`Amazon EFS`](../AWS_SERVICES_GLOSSARY.md#amazon-efs):** **`File Storage (NFS)`** مشترك بين عدة خوادم Linux عبر أكثر من `AZ`. |
| **`EBS` vs `Instance Store`** | **[`Amazon EBS`](../AWS_SERVICES_GLOSSARY.md#amazon-ebs):** تخزين **دائم (`Persistent`)**؛ تبقى البيانات محفوظة عند إيقاف الخادم (`Stop`). | **`EC2 Instance Store`:** تخزين **مؤقت (`Ephemeral`)** عالي الأداء؛ **تُفقد بياناته بالكامل** عند إيقاف الخادم أو إنهائه. |
| **`Savings Plans` vs `Reserved Instances`** | **`Savings Plans`:** التزام بإنفاق مبلغ ثابت في الساعة مع مرونة عالية جداً (تغطي `EC2`, `Fargate`, `Lambda`). | **`Reserved Instances (RI)`:** التزام بعائلة خادم ومواصفات محددة في منطقة محددة (أقل مرونة). |
| **`ECS / EKS` vs [`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate)** | **[`Amazon ECS`](../AWS_SERVICES_GLOSSARY.md#amazon-ecs) / `EKS`:** منصات تنسيق وإدارة الحاويات (تعمل على `EC2` أو `Fargate`). | **[`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate):** محرك **`Serverless`** لتشغيل الحاويات دون توفير أو إدارة خوادم `EC2` أسفلها. |

---

### 3. مقارنات قواعد البيانات والشبكات والتكامل والفوترة (`DB, Networking, Integration & Billing`)

| المقارنة | الخدمة الأولى | الخدمة الثانية / الثالثة |
| :--- | :--- | :--- |
| **`RDS Multi-AZ` vs `Read Replicas`** | **`Multi-AZ`:** مخصصة **للتوافر العالي والتعافي التلقائي (`High Availability / Failover`)** فقط؛ لا تُستخدم للقراءة. | **`Read Replicas`:** مخصصة **لتحسين الأداء وتوزيع ضغط القراءة والتقارير (`Read Scaling`)**. |
| **`RDS` vs `DynamoDB` vs `Redshift`** | **[`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds):** قواعد بيانات علائقية (`SQL`) للمعاملات اليومية (`OLTP`). | **[`Amazon DynamoDB`](../AWS_SERVICES_GLOSSARY.md#amazon-dynamodb):** قاعدة بيانات **`NoSQL Serverless`** فائقة السرعة.<br>**[`Amazon Redshift`](../AWS_SERVICES_GLOSSARY.md#amazon-redshift):** مستودع بيانات (`Data Warehouse`) للتحليلات (`OLAP`). |
| **`CloudFront` vs `Global Accelerator`** | **[`Amazon CloudFront`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudfront):** شبكة توصيل محتوى (**`CDN Caching`**) للملفات الثابتة والديناميكية عبر `HTTP/HTTPS`. | **[`AWS Global Accelerator`](../AWS_SERVICES_GLOSSARY.md#aws-global-accelerator):** تسريع حركة مرور **`TCP/UDP`** عبر شبكة AWS الخاصة مع توفير **عنواني `Static Anycast IP`**. |
| **`Site-to-Site VPN` vs `Direct Connect`** | **`Site-to-Site VPN`:** اتصال مشفر عبر **الإنترنت العام** (سريع الإعداد ومنخفض التكلفة). | **[`AWS Direct Connect`](../AWS_SERVICES_GLOSSARY.md#aws-direct-connect):** كابل ألياف ضوئية **مخصص وخاص** لا يمر عبر الإنترنت العام (أداء ثابت وزمن استجابة منخفض). |
| **[`Amazon SQS`](../AWS_SERVICES_GLOSSARY.md#amazon-sqs) vs [`Amazon SNS`](../AWS_SERVICES_GLOSSARY.md#amazon-sns)** | **[`Amazon SQS`](../AWS_SERVICES_GLOSSARY.md#amazon-sqs):** **طابور رسائل (`Message Queue — Pull`)** لفصل المكونات (`Decoupling`) ومنع فقدان الطلبات. | **[`Amazon SNS`](../AWS_SERVICES_GLOSSARY.md#amazon-sns):** **خدمة نشر واشتراك (`Pub/Sub — Push`)** لإرسال الإشعارات (`Email`, `SMS`) لعدة مشتركين في وقت واحد. |
| **`Gateway` vs `Interface VPC Endpoint`** | **`Gateway Endpoint`:** مجاني عبر `Route Table`، يدعم **`S3` و `DynamoDB` فقط**. | **`Interface Endpoint` (`PrivateLink`):** عبر `ENI` بـ `Private IP`، يدعم معظم خدمات AWS الأخرى. |
| **`Amplify` vs `Device Farm` vs `AppSync`** | **[`AWS Amplify`](../AWS_SERVICES_GLOSSARY.md#aws-amplify):** بناء واستضافة تطبيقات الويب والموبايل `Full-Stack`. | **[`AWS Device Farm`](../AWS_SERVICES_GLOSSARY.md#aws-device-farm):** اختبار التطبيقات على هواتف فعلية حقيقية.<br>**[`AWS AppSync`](../AWS_SERVICES_GLOSSARY.md#aws-appsync):** واجهات **`GraphQL APIs`** لحظية و `Offline Sync`. |
| **`AppStream 2.0` vs `WorkSpaces`** | **[`Amazon AppStream 2.0`](../AWS_SERVICES_GLOSSARY.md#amazon-appstream-20):** **بث تطبيقات سطح المكتب (`Application Streaming`)** عبر متصفح الويب فقط دون نظام تشغيل دائم للمستخدم. | **[`Amazon WorkSpaces`](../AWS_SERVICES_GLOSSARY.md#amazon-workspaces):** **سطح مكتب افتراضي كامل ودائم (`Persistent Virtual Desktop — DaaS`)** بنظام `Windows` أو `Linux` للموظفين عن بُعد. |
| **[`AWS Budgets`](../AWS_SERVICES_GLOSSARY.md#aws-budgets) vs [`AWS Cost Explorer`](../AWS_SERVICES_GLOSSARY.md#aws-cost-explorer)** | **[`AWS Budgets`](../AWS_SERVICES_GLOSSARY.md#aws-budgets):** وضع حدود مالية وإرسال **إنذارات تلقائية (`Alerts`)** عند تجاوز الميزانية. | **[`AWS Cost Explorer`](../AWS_SERVICES_GLOSSARY.md#aws-cost-explorer):** **الرسوم البيانية وتحليل الإنفاق التاريخي والتنبؤ المستقبلي (`Forecasting`)**. |
| **`Health: Service` vs `Account Health`** | **`Service Health`:** الحالة العامة لجميع خدمات AWS عالمياً (متاح للجميع). | **`Account Health`:** تنبيهات مخصصة لحسابك حول الأعطال أو الصيانات التي تؤثر على مواردك. |

---

## ثانياً: المنهجية القياسية لتحليل وحل أسئلة الاختبار (`MCQ Strategy`)

عند التعامل مع أسئلة السيناريوهات الطويلة في اختبار **`CLF-C02`**، اتبع الخطوات الأربع التالية لرفع دقة الإجابة وتقليل التشتت:

### 1. قراءة الجملة الأخيرة أولاً لتحديد القيد الحاكم (`Identify the Governing Constraint`)
تبدأ معظم أسئلة AWS بسيناريو عملي يليه سؤال محدد يحتوي على كلمة مفتاحية حاكمة تحدد الإجابة الصحيحة:
* **`Least operational overhead` / `Minimal administrative effort`:** استبعد فوراً الخيارات التي تتطلب إدارة خوادم `EC2` يدوياً، واتجه نحو الخدمات المُدارة بالكامل أو `Serverless` (مثل [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda), [`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate), [`Amazon DynamoDB`](../AWS_SERVICES_GLOSSARY.md#amazon-dynamodb), [`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds), [`Amazon Athena`](../AWS_SERVICES_GLOSSARY.md#amazon-athena)).
* **`Most cost-effective` / `Lowest cost`:** ركّز على خيارات التحسين المالي (`Spot Instances`, `Savings Plans`, `S3 Glacier Deep Archive`, `S3 Intelligent-Tiering`).
* **`Globally` / `Lowest latency`:** فكّر مباشرةً في [`Amazon CloudFront`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudfront), [`AWS Global Accelerator`](../AWS_SERVICES_GLOSSARY.md#aws-global-accelerator), [`Amazon Route 53`](../AWS_SERVICES_GLOSSARY.md#amazon-route-53), أو `DynamoDB Global Tables`.

### 2. تطبيق الاستبعاد المنهجي (`Systematic Elimination`)
في كل سؤال من أربعة خيارات، غالباً ما يكون هناك خياران لا علاقة لهما بالمجال الوظيفي للسؤال (مثلاً ذكر خدمة تحليل صوتي في سؤال عن أمن الشبكات). استبعدهما فوراً لحصر المقارنة بين خيارين متقاربين فقط، ثم طبّق الفروق الدقيقة من جدول `X vs Y` أعلاه.

### 3. الحذر من مصائد المسؤولية المشتركة (`Shared Responsibility Traps`)
تذكر دائماً أن **بيانات العميل، وإدارة الهويات `IAM`، وتحديث نظام التشغيل الضيف على `EC2`** هي مسؤولية **العميل**؛ بينما **الأمن المادي لمراكز البيانات، والعتاد، والشبكة الأساسية، وأنظمة تشغيل الخدمات المُدارة (`RDS`, `Lambda`)** هي مسؤولية **AWS**.

### 4. إدارة الوقت والاستفادة من التمديد المجاني (`ESL +30`)
* يمنحك الاختبار 90 دقيقة لـ 65 سؤالاً (نحو 83 ثانية لكل سؤال)، ويمكن لغير الناطقين بالإنجليزية كلغة أم طلب تمديد مجاني لمدة 30 دقيقة إضافية (`ESL +30`) من لوحة تحكم الشهادات قبل حجز الموعد ليصبح الوقت الإجمالي **120 دقيقة**.
* لا تتوقف طويلاً أمام سؤال غامض؛ اختر أفضل تقدير لديك وضع عليه علامة للمراجعة (`Flag for Review`) ثم عد إليه بعد إنهاء باقي الأسئلة.

---

## الخطوة العملية للتدريب على الأسئلة

بعد إتمام قراءة هذا الدليل، يُنصح بالتدرب المكثف على الأسئلة المجمّعة في مجلد [11_Practice_Exams](../11_Practice_Exams/)، أو تشغيل أداة المحاكاة التفاعلية في سطر الأوامر:

<div dir="ltr">

```bash
# تدريب تفاعلي على 20 سؤالاً مع عرض استراتيجيات الحل
python3 scripts/aws_revision_runner.py --cert CLF --mode practice -n 20 --tricks

# محاكاة اختبار كامل بوقت محدد (65 سؤالاً)
python3 scripts/aws_revision_runner.py --cert CLF --mode mock
```

</div>

---

> **الدرس السابق:** [Domain 4: Billing, Pricing & Support](./04_Domain_4_Billing_Pricing_and_Support.md) | [العودة إلى الفهرس الرئيسي](./README.md)

</div>
