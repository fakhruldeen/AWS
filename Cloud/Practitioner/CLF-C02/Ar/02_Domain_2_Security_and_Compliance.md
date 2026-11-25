<div dir="rtl">

# Domain 2: Security and Compliance — الأمن السيبراني وإدارة الهوية والامتثال (30% من الاختبار)

يمثل هذا المجال **30%** من إجمالي اختبار `CLF-C02`، وهو ثاني أكبر مجالات الاختبار وزناً. يركز على تقسيم المسؤوليات الأمنية بين AWS والعميل، وإدارة الهويات والصلاحيات، وحماية الشبكات والتطبيقات، وتشفير البيانات، وأدوات كشف التهديدات والامتثال القانوني.

---

## أولاً: نموذج المسؤولية المشتركة (`AWS Shared Responsibility Model`)

يُعد هذا النموذج حجر الأساس في الأمن السحابي وأحد أكثر الموضوعات تكراراً في الاختبار. يقوم النموذج على تقسيم واضح للمسؤوليات بين طرفين:

### 1. مسؤولية AWS: أمن السحابة نفسها (`Security OF the Cloud`)
تتحمل AWS المسؤولية الكاملة عن حماية البنية التحتية التي تُشغّل جميع الخدمات السحابية، وتشمل:
* **الأمن المادي (`Physical Security`):** حراسة مراكز البيانات (`Data Centers`)، وأنظمة الدخول البيومترية، وكاميرات المراقبة، وإتلاف الأقراص التالفة.
* **العتاد والشبكة الأساسية (`Hardware & Global Infrastructure`):** الخوادم الفيزيائية، وأجهزة التخزين، والشبكة التي تربط الـ `Regions` والـ `Availability Zones` والـ `Edge Locations`.
* **طبقة المحاكاة الافتراضية (`Virtualization Layer / Hypervisor`):** تأمين وعزل الآلات الافتراضية عن بعضها وتحديث برمجيات المضيف (`Host OS`).

### 2. مسؤولية العميل: الأمن داخل السحابة (`Security IN the Cloud`)
تعتمد مسؤولية العميل على نوع الخدمة التي يختارها (البنية التحتية مقابل الخدمات المُدارة):
* **بيانات العميل (`Customer Data`):** تصنيف البيانات، وإدارة صلاحيات الوصول إليها، وتشفيرها (`Encryption at Rest` و `Encryption in Transit`)، وتحديد مكان تخزينها (`Region`).
* **إدارة الهوية والصلاحيات (`IAM`):** إنشاء المستخدمين والأدوار، وتفعيل **`MFA`**، وتطبيق مبدأ أقل الصلاحيات (`Least Privilege`).
* **إعدادات الشبكة وجدران الحماية:** تكوين **`Security Groups`** و **`Network ACLs`** وجداول التوجيه (`Route Tables`).
* **تحديثات نظام التشغيل (`Guest OS Patching`):**
  * في الخدمات من نوع **`IaaS`** مثل **[`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2)**: **العميل** هو المسؤول الكامل عن تحديث نظام التشغيل (`Linux / Windows`) والتطبيقات المثبتة داخله.
  * في الخدمات المُدارة (`Managed Services`) مثل **[`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds)** و **[`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3)** و **[`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda)**: **AWS** هي المسؤولة عن تحديث نظام التشغيل الأساسي وإدارة الخادم، بينما يظل العميل مسؤولاً عن إعدادات الخدمة وبياناته وصلاحيات الوصول.

### 3. الضوابط المشتركة (`Shared Controls`)
هي مسؤوليات تنطبق على الطرفين ولكن في طبقات مختلفة، ومن أبرزها:
* **`Patch Management`:** تقوم AWS بتحديث العتاد ونظام التشغيل المضيف (`Host OS`)، بينما يقوم العميل بتحديث نظام التشغيل الضيف (`Guest OS`) وتطبيقاته على `EC2`.
* **`Configuration Management`:** تدير AWS إعدادات أجهزتها التحتية، بينما يدير العميل إعدادات أنظمته وقواعد بياناته.
* **`Awareness & Training`:** تدرب AWS موظفيها على معايير الأمان، ويدرب العميل موظفيه على الاستخدام الآمن لحسابات AWS.

---

## ثانياً: إدارة الهوية والوصول (`AWS IAM` — Identity and Access Management)

تُعد **[`AWS IAM`](../AWS_SERVICES_GLOSSARY.md#aws-iam)** خدمة **عالمية (`Global Service`) ومجانية** تتيح التحكم الدقيق في من يُسمح له بالوصول إلى موارد AWS وما هي الإجراءات المصرح له بتنفيذها.

### المكونات الأساسية لـ `AWS IAM`:

1. **حساب الجذر (`AWS Account Root User`):**
   * هو الحساب الأولي الذي يُنشأ باستخدام البريد الإلكتروني وكلمة المرور عند فتح حساب AWS لأول مرة، ويمتلك صلاحيات غير محدودة لا يمكن تقييدها بسياسات IAM.
   * **أفضل الممارسات الإلزامية في الاختبار:**
     * تفعيل المصادقة متعددة العوامل (**`MFA`**) على حساب الجذر فوراً.
     * **عدم استخدام `Root User` للمهام اليومية مطلقاً**، بل إنشاء مستخدم إداري أو استخدام `IAM Identity Center`.
     * **عدم إنشاء `Access Keys`** لحساب الجذر (وحذفها فوراً إن وُجدت).
     * يقتصر استخدامه على مهام إدارية نادرة للغاية مثل إغلاق الحساب، أو تغيير باقة الدعم الفني (`Support Plan`)، أو تعديل بيانات مالك الحساب.

2. **مستخدمو IAM (`IAM Users`):**
   * هويات مخصصة للأفراد أو التطبيقات داخل حساب AWS. يُمنح كل مستخدم بيانات دخول مستقلة (`Console Password` أو `Access Keys` للـ CLI/SDK).

3. **مجموعات IAM (`IAM Groups`):**
   * حاوية تنظيمية تضم مجموعة من الـ **`IAM Users`** (مثل `Developers`, `Finance`, `Admins`) لربط السياسات الأمنية بالمجموعة دفعة واحدة بدلاً من تكرارها لكل مستخدم.
   * *ملاحظة هامة:* لا يمكن للمجموعة أن تحتوي على مجموعة أخرى (`Groups cannot be nested`)، ولا يمكنها احتواء `IAM Roles`.

4. **سياسات IAM (`IAM Policies`):**
   * مستندات مكتوبة بصيغة **`JSON`** تحدد الصلاحيات بدقة (`Effect: Allow / Deny`، و `Action`، و `Resource`).
   * **مبدأ التقييم الافتراضي (`Implicit Deny`):** أي مستخدم جديد يبدأ بصلاحيات **صفرية** تماماً، وأي قاعدة منع صريحة (**`Explicit Deny`**) تتغلب دائماً على أي قاعدة سماح (`Allow`).
   * يجب دائماً الالتزام بمبدأ أقل الصلاحيات (**`Principle of Least Privilege`**): منح المستخدم الحد الأدنى فقط من الصلاحيات اللازمة لأداء عمله.

5. **أدوار IAM (`IAM Roles`):**
   * هويات لا ترتبط بكلمة مرور دائمة أو مفاتيح ثابتة، بل تمنح **بيانات اعتماد مؤقتة (`Temporary Security Credentials`)** عبر خدمة **`AWS STS` (Security Token Service)**.
   * **الحالة القياسية في الاختبار:** لتمكين خادم **[`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2)** أو دالة **[`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda)** من قراءة ملفات في **[`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3)** بأمان، نربط **`IAM Role`** بالخادم بدلاً من كتابة `Access Keys` ثابتة داخل الكود.

6. **المصادقة متعددة العوامل (`MFA` — Multi-Factor Authentication):**
   * تضيف طبقة تحقق ثانية (شيء تمتلكه مثل تطبيق مصادقة على الهاتف أو مفتاح أمان فيزيائي `Hardware MFA`) بجانب كلمة المرور (شيء تعرفه).

7. **مركز الهوية ([`AWS IAM Identity Center`](../AWS_SERVICES_GLOSSARY.md#aws-iam-identity-center) — سابقاً `AWS SSO`):**
   * الخدمة الموصى بها للمؤسسات لإدارة وصول الموظفين إلى **عدة حسابات AWS** وتطبيقات الأعمال السحابية عبر **تسجيل دخول موحد (`Single Sign-On`)**، مع إمكانية الربط بمزودي الهوية الخارجيين مثل `Microsoft Active Directory` و `Okta`.

8. **محلل صلاحيات الوصول ([`AWS IAM Access Analyzer`](../AWS_SERVICES_GLOSSARY.md#aws-iam-access-analyzer)):**
   * أداة تحليل أمني متقدمة تساعد على تطبيق مبدأ **`Least Privilege`** من خلال ثلاث وظائف أساسية في الاختبار:
     * **اكتشاف الموارد المشتركة خارجياً (`External Access Analysis`):** تحديد أي موارد في حسابك (مثل `S3 Buckets`, `KMS Keys`, `IAM Roles`, `SQS Queues`) تمت مشاركتها مع جهات خارجية أو حسابات أخرى بشكل غير مقصود.
     * **اكتشاف الصلاحيات غير المستخدمة (`Unused Access Analysis`):** تحديد الأدوار أو المفاتيح أو الصلاحيات الممنوحة للمستخدمين والتي لم تُستخدم فعلياً لفترات طويلة لإلغائها.
     * **توليد والتحقق من السياسات (`Policy Generation & Validation`):** إنشاء سياسات `IAM` دقيقة بناءً على النشاط الفعلي المسجل في `CloudTrail`.

9. **إدارة هويات مستخدمي التطبيقات ([`Amazon Cognito`](../AWS_SERVICES_GLOSSARY.md#amazon-cognito)):**
   * خدمة مُدارة بالكامل لتوفير التسجيل وتسجيل الدخول (`Sign-up / Sign-in`) لمستخدمي **تطبيقات الويب والهواتف الذكية** (بما في ذلك تسجيل الدخول عبر حسابات التواصل الاجتماعي مثل Google و Apple و Facebook).

---

## ثالثاً: حوكمة الحسابات المتعددة (`AWS Organizations`, `Control Tower` & `RAM`)

تعتمد المؤسسات الاحترافية على فصل بيئات العمل في حسابات AWS مستقلة (حساب للتطوير `Dev`، وحساب للاختبار `Staging`، وحساب للإنتاج `Prod`) لتقليل نطاق الضرر (`Blast Radius`) وعزل الفواتير.

* **[`AWS Organizations`](../AWS_SERVICES_GLOSSARY.md#aws-organizations):** خدمة مجانية تتيح إدارة جميع حسابات المؤسسة مركزياً ضمن هيكل شجري من الوحدات التنظيمية (**`Organizational Units — OUs`**).
* **المزايا الجوهرية:**
  1. **الفوترة الموحدة (`Consolidated Billing`):** إصدار فاتورة واحدة لجميع الحسابات، وتجميع الاستهلاك للحصول على خصومات الكميات (**`Volume Discounts`**)، ومشاركة خصومات `Reserved Instances` و `Savings Plans` بين الحسابات.
  2. **سياسات التحكم في الخدمات (`Service Control Policies — SCPs`):** قواعد حوكمة مركزية تحدد **الحد الأقصى المسموح به من الصلاحيات (`Guardrails`)** للحسابات أو الوحدات التنظيمية. *ملاحظة هامة:* الـ `SCP` لا تمنح صلاحيات بحد ذاتها، لكنها تضع سقفاً لا يستطيع حتى مدير الحساب (`Administrator`) تجاوزه (مثل حظر إطلاق موارد خارج `eu-north-1`).
* **[`AWS Control Tower`](../AWS_SERVICES_GLOSSARY.md#aws-control-tower):** أسهل وأسرع طريقة لإعداد وإدارة بيئة متعددة الحسابات آمنة ومتوافقة مع أفضل الممارسات (**`Landing Zone`**)؛ تعمل فوق [`AWS Organizations`](../AWS_SERVICES_GLOSSARY.md#aws-organizations) وتطبق ضوابط وقائية وكشفية جاهزة (**`Guardrails`**).
* **`AWS Resource Access Manager (RAM)`:** تتيح مشاركة موارد AWS (مثل `VPC Subnets` و `Transit Gateway`) بأمان بين عدة حسابات داخل المؤسسة دون الحاجة لتكرار إنشائها.

---

## رابعاً: التشفير وإدارة الشهادات والأسرار (Encryption & Secrets Management)

| الخدمة | آلية العمل وحالة الاستخدام الدقيقة |
| :--- | :--- |
| **[`AWS KMS`](../AWS_SERVICES_GLOSSARY.md#aws-kms) (Key Management Service)** | خدمة مُدارة لإنشاء وإدارة مفاتيح التشفير المستخدمة في تشفير البيانات عبر خدمات AWS (`S3`, `EBS`, `RDS`, `DynamoDB`). تعمل على عتاد أمني مشترك (`Multi-tenant HSM`) وتتكامل تلقائياً مع [`AWS CloudTrail`](../AWS_SERVICES_GLOSSARY.md#aws-cloudtrail) لتسجيل كل عملية استخدام للمفتاح. |
| **[`AWS CloudHSM`](../AWS_SERVICES_GLOSSARY.md#aws-cloudhsm)** | جهاز عتادي مخصص ومفرد للعميل (**`Single-tenant Dedicated Hardware`**) يوفر تحكماً حصرياً بالمفاتيح ويلبي متطلبات الامتثال الصارمة للقطاع المصرفي والحكومي (`FIPS 140-2 Level 3`). لا تمتلك AWS صلاحية الوصول إلى المفاتيح داخله. |
| **`AWS Certificate Manager (ACM)`** | خدمة تتولى إصدار ونشر وتجديد شهادات **`SSL/TLS Certificates`** تلقائياً ومجاناً للشهادات العامة المرتبطة بخدمات AWS مثل `CloudFront` و `ALB` و `API Gateway` لتأمين حركة مرور `HTTPS`. |
| **[`AWS Secrets Manager`](../AWS_SERVICES_GLOSSARY.md#aws-secrets-manager)** | خزنة مُدارة لتخزين بيانات الاعتماد الحساسة مثل كلمات مرور قواعد البيانات (`RDS`) ومفاتيح الـ `API`. **الميزة الفارقة:** تدعم التدوير التلقائي لكلمات المرور (**`Automatic Secret Rotation`**) بشكل دوري دون تدخل بشري. |
| **`AWS Systems Manager Parameter Store`** | مخزن هرمي للإعدادات النصية (`Configuration Parameters`) والبيانات السرية البسيطة (بالتكامل مع KMS). يتميز بتكلفة منخفضة جداً (الطبقة القياسية مجانية)، لكنه لا يوفر ميزة التدوير التلقائي الجاهزة الموجودة في `Secrets Manager`. |

---

## خامساً: أمن الشبكات وحماية التطبيقات (Network & Edge Protection)

### 1. المقارنة الجوهرية: `Security Groups` مقابل `Network ACLs (NACLs)`

| وجه المقارنة | `Security Groups` | `Network ACLs (NACLs)` |
| :--- | :--- | :--- |
| **نطاق التطبيق** | على مستوى واجهة الشبكة للخادم (**`EC2 Instance / ENI Level`**) | على مستوى الشبكة الفرعية بالكامل (**`Subnet Level`**) |
| **أنواع القواعد** | تدعم قواعد السماح فقط (**`Allow rules ONLY`**) — كل ما لم يُسمح به مرفوض ضمنياً | تدعم قواعد السماح والمنع الصريح (**`Allow AND Deny rules`**) — تُستخدم لحظر عناوين IP خبيثة محددة |
| **تتبع الحالة (`State`)** | **`Stateful`:** حركة المرور المسموح بدخولها يُسمح بردّها بالخروج تلقائياً دون قاعدة إضافية | **`Stateless`:** يجب تعريف قواعد صريحة لحركة الدخول (`Inbound`) وأخرى منفصلة لحركة الخروج (`Outbound`) |
| **ترتيب التقييم** | يتم تقييم **جميع القواعد** معاً قبل اتخاذ القرار | يتم تقييم القواعد **بالتسلسل الرقمي** من الأصغر إلى الأكبر، ويُطبق أول تطابق |

### 2. الحماية من الهجمات الإلكترونية
* **[`AWS Shield`](../AWS_SERVICES_GLOSSARY.md#aws-shield) (الحماية من هجمات حجب الخدمة `DDoS` — الطبقتين 3 و 4):**
  * **`AWS Shield Standard`:** مفعّل تلقائياً **ومجاناً** لجميع عملاء AWS للحماية من هجمات `DDoS` الشائعة.
  * **`AWS Shield Advanced`:** خدمة مدفوعة للمؤسسات توفر حماية متقدمة ومخصصة، ووصولاً على مدار الساعة لفريق الاستجابة المتخصص (**`AWS Shield Response Team — SRT`**)، وحماية مالية ضد ارتفاع الفاتورة الناتج عن هجمات `DDoS` (**`DDoS Cost Protection`**).
* **[`AWS WAF`](../AWS_SERVICES_GLOSSARY.md#aws-waf) (Web Application Firewall — الطبقة السابعة `Layer 7`):**
  * يحمي تطبيقات الويب من الهجمات الشائعة على بروتوكول `HTTP/HTTPS` مثل حقن قواعد البيانات (**`SQL Injection`**) والبرمجة النصية العابرة للمواقع (**`Cross-Site Scripting — XSS`**)، ويمكن ربطه بـ [`Amazon CloudFront`](../AWS_SERVICES_GLOSSARY.md#amazon-cloudfront) و `ALB` و [`Amazon API Gateway`](../AWS_SERVICES_GLOSSARY.md#amazon-api-gateway).
* **[`AWS Network Firewall`](../AWS_SERVICES_GLOSSARY.md#aws-network-firewall):** جدار حماية شبكي مُدار على مستوى الـ **`VPC`** بالكامل، يوفر فحصاً عميقاً للحزم (`Stateful Inspection`) وتصفية لنطاقات الـ `DNS` ومنع التسلل (`IDS/IPS`).
* **[`AWS Firewall Manager`](../AWS_SERVICES_GLOSSARY.md#aws-firewall-manager):** أداة إدارة مركزية لتطبيق وتوحيد قواعد `WAF` و `Shield Advanced` و `Security Groups` و `Network Firewall` عبر جميع الحسابات داخل [`AWS Organizations`](../AWS_SERVICES_GLOSSARY.md#aws-organizations).

---

## سادساً: كشف التهديدات، التدقيق، والامتثال (Threat Detection & Compliance)

| الخدمة | الوظيفة الدقيقة والغرض الأمني |
| :--- | :--- |
| **[`Amazon GuardDuty`](../AWS_SERVICES_GLOSSARY.md#amazon-guardduty)** | **كشف التهديدات الذكي (`Intelligent Threat Detection`):** يحلل باستمرار سجلات `CloudTrail` و `VPC Flow Logs` و `DNS Logs` باستخدام التعلم الآلي (`Machine Learning`) لاكتشاف الأنشطة المشبوهة مثل تعدين العملات الرقمية (`Crypto-mining`)، أو استخدام مفاتيح مسروقة، أو التواصل مع خوادم خبيثة. |
| **[`Amazon Inspector`](../AWS_SERVICES_GLOSSARY.md#amazon-inspector)** | **فحص الثغرات البرمجية الآلي (`Automated Vulnerability Management`):** يفحص بشكل مستمر خوادم [`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2) وصور الحاويات في [`Amazon ECR`](../AWS_SERVICES_GLOSSARY.md#amazon-ecr) ودوال [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda) لاكتشاف الثغرات الأمنية المعروفة (**`CVEs`**) والتعرض الشبكي غير المقصود. |
| **[`Amazon Macie`](../AWS_SERVICES_GLOSSARY.md#amazon-macie)** | **اكتشاف وحماية البيانات الحساسة في `S3`:** يستخدم التعلم الآلي ومطابقة الأنماط لمسح حاويات **[`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3)** واكتشاف البيانات الشخصية الحساسة (**`PII`** — مثل أرقام بطاقات الائتمان والهويات) وتنبيه الفريق في حال وجود حاويات مكشوفة للعامة. |
| **[`AWS Security Hub`](../AWS_SERVICES_GLOSSARY.md#aws-security-hub)** | **لوحة التحكم الأمنية المركزية (`CSPM`):** يجمع ويوحد وينظم التنبيهات الأمنية من `GuardDuty` و `Inspector` و `Macie` و `Firewall Manager` في شاشة واحدة، ويقيّم امتثال الحساب لأطر الأمان القياسية مثل `CIS` و `PCI-DSS`. |
| **[`Amazon Detective`](../AWS_SERVICES_GLOSSARY.md#amazon-detective)** | **التحقيق الجنائي وتحليل السبب الجذري (`Root Cause Analysis`):** يبني رسماً بيانياً للعلاقات الأمنية لمساعدة فرق الأمان على تتبع مصدر الهجوم وفهم نطاقه بعد اكتشاف التهديد. |
| **[`AWS Artifact`](../AWS_SERVICES_GLOSSARY.md#aws-artifact)** | **بوابة تقارير الامتثال والاتفاقيات:** خدمة مجانية تتيح تنزيل شهادات الامتثال المستقلة لـ AWS (مثل **`ISO 27001`**, **`SOC 2`**, **`PCI-DSS`**) وإدارة الاتفاقيات القانونية مثل اتفاقية **`BAA`** الخاصة بمعيار `HIPAA`. |
| **[`AWS Audit Manager`](../AWS_SERVICES_GLOSSARY.md#aws-audit-manager)** | **أتمتة جمع أدلة التدقيق:** يساعد المؤسسات على جمع الأدلة التشغيلية تلقائياً وبشكل مستمر لتقييم جاهزيتها للمراجعات التنظيمية وتقليل الجهد اليدوي أثناء التدقيق. |
| **[`AWS CloudTrail`](../AWS_SERVICES_GLOSSARY.md#aws-cloudtrail)** | **سجل التدقيق الشامل للأنشطة (`API Auditing`):** يسجل كل استدعاء برمجي (`API Call`) وإجراء يتم عبر Console أو CLI أو SDK (من قام بالإجراء، متى، ومن أي عنوان IP)، وهو الأداة الأساسية للتحقيق والحوكمة. |

---

## منهجية التعامل مع أسئلة Domain 2 في الاختبار

| مؤشر أو عبارة في نص السؤال | الإجابة الدقيقة |
| :--- | :--- |
| **Patching the Guest Operating System on an [`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2) instance** | **مسؤولية العميل (`Customer`)** |
| **Patching the underlying OS of [`Amazon RDS`](../AWS_SERVICES_GLOSSARY.md#amazon-rds) or physical security of data centers** | **مسؤولية `AWS`** |
| **Allow an EC2 application to access S3 securely without storing credentials** | **ربط `IAM Role` بـ `EC2 Instance`** |
| **Explicitly block/deny a malicious IP address at the Subnet boundary** | **`Network ACL (NACL)`** (لأن `Security Groups` لا تدعم `Deny`) |
| **Protect web applications from SQL Injection and Cross-Site Scripting (XSS)** | **[`AWS WAF`](../AWS_SERVICES_GLOSSARY.md#aws-waf)** |
| **Protect against DDoS attacks with 24/7 SRT access and cost protection** | **`AWS Shield Advanced`** |
| **Discover Sensitive Data / PII stored inside [`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3) buckets** | **[`Amazon Macie`](../AWS_SERVICES_GLOSSARY.md#amazon-macie)** |
| **Continuously scan EC2 instances, ECR containers, and Lambda for CVEs** | **[`Amazon Inspector`](../AWS_SERVICES_GLOSSARY.md#amazon-inspector)** |
| **Intelligent threat detection using ML on CloudTrail, VPC Flow, and DNS logs** | **[`Amazon GuardDuty`](../AWS_SERVICES_GLOSSARY.md#amazon-guardduty)** |
| **Download AWS SOC 2, ISO, or PCI-DSS compliance reports** | **[`AWS Artifact`](../AWS_SERVICES_GLOSSARY.md#aws-artifact)** |
| **Store and automatically rotate database credentials** | **[`AWS Secrets Manager`](../AWS_SERVICES_GLOSSARY.md#aws-secrets-manager)** |
| **Set maximum permission boundaries across multiple accounts in an organization** | **[`AWS Organizations`](../AWS_SERVICES_GLOSSARY.md#aws-organizations) مع `Service Control Policies (SCPs)`** |
| **Identify AWS resources shared with external entities or detect unused IAM access** | **[`AWS IAM Access Analyzer`](../AWS_SERVICES_GLOSSARY.md#aws-iam-access-analyzer)** |
| **Centralized Single Sign-On (SSO) for workforce access across multiple AWS accounts & SaaS apps** | **[`AWS IAM Identity Center`](../AWS_SERVICES_GLOSSARY.md#aws-iam-identity-center) (`AWS SSO`)** |
| **Add user sign-up, sign-in, and social login (Google/Apple/Facebook) to web/mobile apps** | **[`Amazon Cognito`](../AWS_SERVICES_GLOSSARY.md#amazon-cognito)** |

---

> **الدرس السابق:** [Domain 1: Cloud Concepts](./01_Domain_1_Cloud_Concepts.md) | **الدرس التالي:** 👉 [03_Domain_3_Part1_Compute_and_Storage.md](./03_Domain_3_Part1_Compute_and_Storage.md) | [الفهرس الرئيسي](./README.md)

</div>
