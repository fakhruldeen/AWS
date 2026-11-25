<div dir="rtl">

# Domain 3 (الجزء الأول): Compute & Storage — الحوسبة والخوادم وأنظمة التخزين

يمثل المجال الثالث (**Cloud Technology and Services**) النسبة الأكبر من اختبار `CLF-C02` بوزن **34%**. لتسهيل الفهم والاستيعاب العميق، قُسّم هذا المجال إلى ثلاثة أجزاء متكاملة. يتناول هذا الجزء الأول خدمات **الحوسبة (`Compute`)** وخدمات **التخزين (`Storage`)** بتفصيل شامل.

---

## أولاً: خدمات الحوسبة (`AWS Compute Services`)

### 1. خدمة الخوادم الافتراضية (`Amazon EC2` — Elastic Compute Cloud)
تُعد **[`Amazon EC2`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2)** خدمة الحوسبة الأساسية من نموذج **`IaaS`** في AWS، حيث توفر خوادم افتراضية (`Instances`) قابلة للتخصيص بالكامل من حيث نظام التشغيل (`Amazon Machine Image — AMI`)، وسعة المعالج (`vCPU`)، والذاكرة (`RAM`)، والتخزين، والشبكة.

#### أ. عائلات خوادم EC2 (`EC2 Instance Families`):
تم تصميم كل عائلة لتحسين الأداء والتكلفة لنوع محدد من أحمال العمل:
* **`General Purpose` (مثل `T3`, `M6i`):** توازن مدروس بين المعالج والذاكرة والشبكة؛ مثالية لخوادم الويب، مستودعات الكود، وبيئات التطوير والاختبار.
* **`Compute Optimized` (مثل `C6i`, `C7g`):** معالجات عالية الأداء؛ مخصصة لمعالجة البيانات المكثفة (`Batch Processing`)، خوادم الألعاب، والنمذجة العلمية (`HPC`).
* **`Memory Optimized` (مثل `R6i`, `X2`):** سعة ذاكرة عشوائية (`RAM`) ضخمة؛ مصممة لقواعد البيانات في الذاكرة (`In-memory Databases`)، وتحليل البيانات الضخمة في الوقت الفعلي.
* **`Storage Optimized` (مثل `I3`, `D3`):** أقراص `NVMe SSD` محلية فائقة السرعة لعمليات القراءة والكتابة المتتابعة والعشوائية العالية (`High IOPS`) مثل قواعد بيانات NoSQL الموزعة وأنظمة الملفات الكبيرة.
* **`Accelerated Computing` (مثل `P4`, `G5`, `Inf2`):** مزودة بمسرّعات عتادية مثل بطاقات الرسوميات (**`GPU`**) أو شرائح الذكاء الاصطناعي المخصصة (`AWS Trainium / Inferentia`) لتدريب وتشغيل نماذج التعلم الآلي ومعالجة الرسوميات ثلاثية الأبعاد.

#### ب. نماذج تسعير EC2 (`EC2 Purchasing Options` — محور أساسي في الاختبار):

| نموذج التسعير | آلية العمل والخصم | حالة الاستخدام المثالية |
| :--- | :--- | :--- |
| **`On-Demand Instances`** | الدفع بالثانية أو الساعة دون أي التزام طويل الأجل أو دفعة مقدمة. | أحمال العمل قصيرة الأجل، أو غير المتوقعة (`Unpredictable`)، أو التي لا تحتمل الانقطاع ولا يمكن التنبؤ بمدتها. |
| **`Savings Plans`** | التزام بإنفاق مبلغ ثابت في الساعة (مثلاً `$10/hr`) لمدة **سنة أو 3 سنوات** مقابل خصم يصل إلى **72%**. يتميز بمرونة عالية جداً؛ إذ يغطي **`Compute Savings Plans`** كلاً من `EC2` و [`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate) و [`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda) عبر مختلف الـ Regions وعائلات الخوادم. | أحمال العمل المستمرة والمستقرة مع الحاجة إلى مرونة في تغيير حجم الخادم أو نظام التشغيل أو الانتقال إلى Serverless. |
| **`Reserved Instances (RI)`** | التزام بعائلة خادم محددة (أو قابلة للتحويل في `Convertible RI`) لمدة **سنة أو 3 سنوات** مقابل خصم يصل إلى **72%**. | التطبيقات ذات الاستهلاك الثابت والمتوقع بدقة (`Steady-state workloads`). |
| **`Spot Instances`** | الاستفادة من السعة الفائضة غير المستخدمة في مراكز بيانات AWS بخصم يصل إلى **90%** مقارنة بـ `On-Demand`. **القيد الحاسم:** يمكن لـ AWS استعادة الخادم بإشعار مدته **دقيقتان فقط (`2-minute interruption notice`)**. | المهام المرنة القابلة للتوقف والاستئناف (`Fault-tolerant`, `Stateless`, `Batch jobs`, `CI/CD runners`). **لا تصلح مطلقاً لقواعد البيانات أو الأنظمة الحرجة.** |
| **`Dedicated Hosts`** | استئجار خادم فيزيائي كامل مخصص لك وحدك مع إظهار تفاصيل المعالجات (`Sockets / Physical Cores`). | الالتزام برخص البرمجيات القائمة على العتاد الفيزيائي (**`BYOL` — Bring Your Own License**) أو المتطلبات التنظيمية التي تحظر مشاركة العتاد (`Multi-tenancy`). |
| **`Dedicated Instances`** | تشغيل خوادمك على عتاد مخصص لحسابك فقط، ولكن دون التحكم في مستوى الـ Sockets أو تخصيص نفس الجهاز الفعلي عند إعادة التشغيل. | متطلبات عزل العتاد دون الحاجة لإدارة رخص `BYOL` على مستوى المعالج. |

---

### 2. موازنة الأحمال والتوسع التلقائي (`ELB` & `Amazon EC2 Auto Scaling`)
* **`Elastic Load Balancing (ELB)`:** خدمة مُدارة توزع حركة المرور الواردة تلقائياً عبر عدة خوادم (`Targets`) في أكثر من `Availability Zone`، وتجري فحوصات دورية (`Health Checks`) لتوجيه الطلبات فقط إلى الخوادم السليمة:
  * **`Application Load Balancer (ALB)`:** يعمل على **الطبقة السابعة (`Layer 7 — HTTP/HTTPS`)**، ويدعم التوجيه الذكي بناءً على المسار (`/api`, `/images`) أو اسم النطاق، وهو الأنسب لتطبيقات الويب الحديثة والـ Microservices.
  * **`Network Load Balancer (NLB)`:** يعمل على **الطبقة الرابعة (`Layer 4 — TCP/UDP/TLS`)**، ويُستخدم للأداء الفائق جداً (ملايين الطلبات في الثانية مع `Ultra-low latency`) وعند الحاجة إلى عناوين `Static IP`.
  * **`Gateway Load Balancer (GWLB)`:** يُستخدم لنشر وإدارة أجهزة الشبكة الأمنية الافتراضية من أطراف ثالثة (مثل Firewalls وأنظمة IDS/IPS).
* **[`Amazon EC2 Auto Scaling`](../AWS_SERVICES_GLOSSARY.md#amazon-ec2-auto-scaling):** يراقب حالة التطبيق ويقوم تلقائياً بإضافة خوادم جديدة (`Scale Out`) عند ارتفاع الحمل (مثل ارتفاع استهلاك `CPU` فوق 70%) وإزالة الخوادم الزائدة (`Scale In`) عند انخفاض الحمل، مما يحقق التوافر العالي (`High Availability`) والمرونة (`Elasticity`) وخفض التكلفة في آنٍ واحد.

---

### 3. الحوسبة بدون خوادم والحاويات والمنصات المُدارة
* **[`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda) (Serverless Compute):**
  * يتيح تنفيذ الكود البرمجي (Python, Node.js, Java, Go, .NET, وغيرها) دون إنشاء أو إدارة أي خوادم.
  * يعمل بنمط **مبني على الأحداث (`Event-driven`)** (مثل رفع ملف إلى `S3`، أو طلب عبر `API Gateway`، أو رسالة في `SQS`).
  * **نموذج التكلفة:** تدفع فقط مقابل عدد الطلبات ومدة التنفيذ الفعلية بالملي ثانية؛ وعند عدم وجود طلبات تكون التكلفة **صفراً**. *(الحد الأقصى لمدة تنفيذ الاستدعاء الواحد هو 15 دقيقة).*
* **[`Amazon ECS`](../AWS_SERVICES_GLOSSARY.md#amazon-ecs) (Elastic Container Service):** خدمة مُدارة بالكامل من AWS لتنسيق وتشغيل حاويات **Docker** بأداء عالٍ وتكامل عميق مع خدمات AWS.
* **[`Amazon EKS`](../AWS_SERVICES_GLOSSARY.md#amazon-eks) (Elastic Kubernetes Service):** خدمة مُدارة لتشغيل مجموعات **Kubernetes** القياسية دون عبء إدارة طبقة التحكم (`Control Plane`).
* **[`Amazon ECR`](../AWS_SERVICES_GLOSSARY.md#amazon-ecr) (Elastic Container Registry):** مستودع مُدار وآمن لتخزين وإدارة ونشر صور حاويات Docker.
* **[`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate):** محرك حوسبة **Serverless للحاويات** يعمل مع كل من `ECS` و `EKS`، حيث يتيح تشغيل الحاويات مباشرة دون الحاجة لتوفير أو إدارة خوادم `EC2` أسفلها.
* **[`AWS Elastic Beanstalk`](../AWS_SERVICES_GLOSSARY.md#aws-elastic-beanstalk) (`PaaS`):** خدمة تتيح للمطورين رفع الكود البرمجي للتطبيق فقط، فتتولى AWS تلقائياً إنشاء وإدارة البنية التحتية الكاملة (`EC2`, `ELB`, `Auto Scaling`, `Health Monitoring`) مع احتفاظ المطور بالقدرة على الوصول إلى الموارد التحتية إذا رغب. الخدمة نفسها مجانية ويدفع العميل تكلفة الموارد المُنشأة فقط.
* **[`Amazon Lightsail`](../AWS_SERVICES_GLOSSARY.md#amazon-lightsail):** منصة مبسطة ومثالية للمشاريع الصغيرة والمواقع التعريفية (مثل WordPress)، تقدم حزماً متكاملة (خادم + تخزين + شبكة) بـ **سعر شهري ثابت ومتوقع (`Predictable Monthly Pricing`)**.

---

## ثانياً: خدمات التخزين (`AWS Storage Services`)

### 1. خدمة التخزين الكائني (`Amazon S3` — Simple Storage Service)
تُعد **[`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3)** خدمة تخزين كائني (`Object Storage`) عالمية النطاق، مصممة لتحقيق متانة فائقة تصل إلى **`99.999999999%` (11 Nines of Durability)** عبر نسخ البيانات تلقائياً على عدة مرافق داخل نفس الـ `Region`.
* **المفاهيم الأساسية:** تُخزَّن الملفات (`Objects` بحد أقصى **5 TB** للملف الواحد) داخل حاويات تُسمى **`Buckets`**. يجب أن يكون اسم الـ `Bucket` **فريداً عالمياً (`Globally Unique`)** على مستوى جميع حسابات AWS.
* **مزايا هامة:** تدعم **`S3 Versioning`** (الاحتفاظ بنسخ سابقة من الملفات للحماية من الحذف أو التعديل العرضي)، و **`S3 Lifecycle Policies`** (أتمتة نقل الملفات بين فئات التخزين أو حذفها بعد مدة زمنية)، و **`Static Website Hosting`** (استضافة مواقع HTML/CSS/JS مباشرة بدون خوادم).

#### فئات التخزين في `Amazon S3` (`S3 Storage Classes`):

| فئة التخزين (`Storage Class`) | التوافر والانتشار | زمن الاسترجاع (`Retrieval`) | حالة الاستخدام المثالية |
| :--- | :---: | :---: | :--- |
| **`S3 Standard`** | `>= 3 AZs` | فوري (`Milliseconds`) | البيانات النشطة التي يتم الوصول إليها بشكل متكرر (`Frequently accessed data`). |
| **`S3 Intelligent-Tiering`** | `>= 3 AZs` | فوري / أرشيف اختياري | البيانات ذات **أنماط الوصول غير المعروفة أو المتغيرة (`Unknown or changing access patterns`)**؛ تنقل الكائنات تلقائياً إلى الفئة الأرخص دون رسوم استرجاع. |
| **`S3 Standard-IA`** (Infrequent Access) | `>= 3 AZs` | فوري (`Milliseconds`) | بيانات نادرة الوصول لكنها تتطلب استرجاعاً فورياً عند الحاجة (مثل النسخ الاحتياطية الحديثة). |
| **`S3 One Zone-IA`** | **`1 AZ` فقط** | فوري (`Milliseconds`) | أرخص بنحو 20% من `Standard-IA`؛ مناسبة للبيانات الثانوية القابلة لإعادة الإنشاء (`Re-creatable data` مثل الصور المصغرة). |
| **`S3 Glacier Instant Retrieval`** | `>= 3 AZs` | فوري (`Milliseconds`) | أرشيف طويل الأمد يُطلب مرة كل ربع سنة ولكنه يحتاج استرجاعاً فورياً (مثل الصور الطبية أو الأرشيف الإخباري). |
| **`S3 Glacier Flexible Retrieval`** | `>= 3 AZs` | من دقائق إلى ساعات (1 دقيقة – 12 ساعة) | الأرشيف السنوي والنسخ الاحتياطية التي لا تتطلب وصولاً لحظياً. |
| **`S3 Glacier Deep Archive`** | `>= 3 AZs` | من **12 إلى 48 ساعة** | **أقل فئة تخزين تكلفةً في AWS**؛ مصممة لحفظ السجلات القانونية والمالية لـ 7–10 سنوات دون الحاجة للوصول إليها إلا نادراً. |

---

### 2. خدمات التخزين الكتلي والملفي والهجين

| الخدمة | النوع | الشرح التفصيلي وحالة الاستخدام |
| :--- | :---: | :--- |
| **[`Amazon EBS`](../AWS_SERVICES_GLOSSARY.md#amazon-ebs)** (Elastic Block Store) | **Block Storage** | قرص تخزين شبكي دائم (`Persistent`) يُربط بخادم `EC2` واحد داخل نفس الـ **`Availability Zone`**. يحتفظ بالبيانات حتى بعد إيقاف تشغيل الخادم (`Stop`). يمكن أخذ نسخ احتياطية تدريجية منه تُسمى **`EBS Snapshots`** وتُخزَّن تلقائياً في [`Amazon S3`](../AWS_SERVICES_GLOSSARY.md#amazon-s3) لسهولة النقل بين الـ `AZs` أو الـ `Regions`. |
| **`EC2 Instance Store`** | **Temporary Block** | قرص عتادي مدمج مادياً في الخادم الفيزيائي، يتميز بأداء `IOPS` فائق جداً، لكنه **مؤقت (`Ephemeral`)** — أي تُفقد بياناته بالكامل عند إيقاف الخادم (`Stop`) أو إنهائه (`Terminate`). يُستخدم للذاكرة المؤقتة (`Cache` / `Buffer`) فقط. |
| **[`Amazon EFS`](../AWS_SERVICES_GLOSSARY.md#amazon-efs)** (Elastic File System) | **Managed File (`NFS`)** | نظام ملفات سحابي مُدار لخوادم **Linux**، يتميز بأنه قابل للمشاركة المتزامنة من مئات خوادم `EC2` عبر **عدة `AZs` في نفس الوقت**، ويتوسع وينكمش تلقائياً حسب حجم الملفات المخزنة (تدفع مقابل المساحة المستخدمة فعلياً فقط). |
| **[`Amazon FSx`](../AWS_SERVICES_GLOSSARY.md#amazon-fsx)** | **Managed File** | يوفر أنظمة ملفات قياسية مُدارة بالكامل مثل **`FSx for Windows File Server`** (يدعم بروتوكول **`SMB`** وتكامل Active Directory)، و **`FSx for Lustre`** للحوسبة عالية الأداء (`HPC`) والتعلم الآلي. |
| **[`AWS Storage Gateway`](../AWS_SERVICES_GLOSSARY.md#aws-storage-gateway)** | **Hybrid Storage** | خدمة هجينة تربط بيئة العمل المحلية (`On-Premises`) بسحابة تخزين AWS (مثل `S3` و `EBS` و `Glacier`) لتمكين النسخ الاحتياطي السحابي والوصول منخفض التأخير إلى الملفات السحابية من داخل مقر الشركة. |
| **[`AWS Backup`](../AWS_SERVICES_GLOSSARY.md#aws-backup)** | **Backup Management** | خدمة مركزية مُدارة بالكامل لأتمتة وإدارة ومراقبة سياسات النسخ الاحتياطي عبر معظم خدمات AWS (`EBS`, `RDS`, `DynamoDB`, `EFS`, `S3`) من لوحة تحكم واحدة. |

---

## منهجية التعامل مع أسئلة Compute & Storage في الاختبار

| مؤشر أو عبارة في نص السؤال | الإجابة الدقيقة |
| :--- | :--- |
| **Up to 90% cost savings for stateless, fault-tolerant, interruptible workloads** | **`EC2 Spot Instances`** |
| **Flexible 1-year or 3-year commitment covering EC2, Fargate, and Lambda** | **`Compute Savings Plans`** |
| **Dedicated physical server required for BYOL (per-socket / per-core licensing)** | **`EC2 Dedicated Hosts`** |
| **Execute event-driven code with zero server management (up to 15 min)** | **[`AWS Lambda`](../AWS_SERVICES_GLOSSARY.md#aws-lambda)** |
| **Run Docker containers without provisioning or managing underlying EC2 servers** | **[`AWS Fargate`](../AWS_SERVICES_GLOSSARY.md#aws-fargate)** |
| **Deploy a web application quickly by uploading code while AWS manages infrastructure** | **[`AWS Elastic Beanstalk`](../AWS_SERVICES_GLOSSARY.md#aws-elastic-beanstalk)** |
| **Lowest-cost long-term archival storage with 12–48 hour retrieval time** | **`S3 Glacier Deep Archive`** |
| **Optimize S3 storage costs automatically for unknown or changing access patterns** | **`S3 Intelligent-Tiering`** |
| **Shared POSIX/NFS file storage mounted simultaneously by Linux EC2 instances across AZs** | **[`Amazon EFS`](../AWS_SERVICES_GLOSSARY.md#amazon-efs)** |
| **Shared SMB file storage for Windows servers with Active Directory integration** | **`Amazon FSx for Windows File Server`** |
| **Persistent block volume attached to a single EC2 instance (retained after Stop)** | **[`Amazon EBS`](../AWS_SERVICES_GLOSSARY.md#amazon-ebs)** |

---

> **الدرس السابق:** [Domain 2: Security & Compliance](./02_Domain_2_Security_and_Compliance.md) | **الدرس التالي:** 👉 [03_Domain_3_Part2_Databases_and_Networking.md](./03_Domain_3_Part2_Databases_and_Networking.md) | [الفهرس الرئيسي](./README.md)

</div>
