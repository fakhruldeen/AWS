<div dir="rtl">

# Domain 3 (الجزء الثاني): Databases & Networking — قواعد البيانات وهندسة الشبكات

يتناول هذا الجزء الثاني من المجال الثالث (`Cloud Technology and Services`) محورين أساسيين في أي معمارية سحابية: **قواعد البيانات المُدارة (`Managed Databases`)** بمختلف أنواعها، و **هندسة الشبكات وتوصيل المحتوى العالمي (`Networking & Content Delivery`)**.

---

## أولاً: قواعد البيانات في AWS (`AWS Database Services`)

تتبنى AWS مبدأ **قواعد البيانات المصممة لغرض محدد (`Purpose-Built Databases`)**، أي اختيار نوع قاعدة البيانات الأنسب لطبيعة البيانات بدلاً من حشر جميع التطبيقات في نوع واحد.

### 1. الفرق الأساسي بين `Relational (SQL)` و `Non-Relational (NoSQL)`
* **قواعد البيانات العلائقية (`Relational / SQL`):** تخزّن البيانات في جداول منظمة (صفوف وأعمدة) ذات هيكل مخطط صارم (`Fixed Schema`) وعلاقات واضحة بين الجداول، وتدعم معاملات دقيقة (`ACID Transactions`). مثالية للأنظمة المالية، والمخازن، وتطبيقات الـ ERP.
* **قواعد البيانات غير العلائقية (`Non-Relational / NoSQL`):** تخزّن البيانات بهياكل مرنة (`Flexible Schema`) مثل أزواج المفتاح والقيمة (`Key-Value`) أو مستندات `JSON` أو الرسوم البيانية (`Graphs`). مصممة للتوسع الأفقي الهائل (`Horizontal Scaling`) وزمن الاستجابة فائق الانخفاض.

### 2. خريطة خدمات قواعد البيانات المُدارة في AWS

| الخدمة | التصنيف | الشرح التفصيلي وحالة الاستخدام |
| :--- | :---: | :--- |
| **`Amazon RDS`** (Relational Database Service) | **SQL (`OLTP`)** | خدمة مُدارة بالكامل لتشغيل قواعد البيانات العلائقية القياسية. تدعم 6 محركات معروفة: **`MySQL`, `PostgreSQL`, `MariaDB`, `Oracle`, `Microsoft SQL Server`, و `IBM Db2`**. تتولى AWS أتمتة النسخ الاحتياطي، وتحديثات نظام التشغيل (`OS Patching`)، والتوافر العالي، مما يقلل العبء التشغيلي مقارنة بتشغيل قاعدة البيانات يدوياً على `EC2`. |
| **`Amazon Aurora`** | **SQL (Cloud-Native)** | قاعدة بيانات علائقية طورتها AWS خصيصاً للسحابة، متوافقة تماماً مع **`MySQL`** و **`PostgreSQL`**. توفر أداءً **أسرع حتى 5 مرات من MySQL وحتى 3 مرات من PostgreSQL** بتكلفة أقل بكثير من القواعد التجارية. تقوم تلقائياً بتخزين **6 نسخ** من بياناتك موزعة على **3 `AZs`** وتتوسع تخزينياً تلقائياً حتى **128 TB**. |
| **`Amazon DynamoDB`** | **NoSQL (Key-Value)** | قاعدة بيانات غير علائقية **مُدارة بالكامل و `Serverless`**. تضمن أداءً ثابتاً بزمن استجابة في حدود **أجزاء من الملي ثانية (`Single-digit millisecond latency`)** مهما بلغ حجم البيانات أو عدد الطلبات (ملايين الطلبات في الثانية). تدعم النسخ العالمي متعدد المناطق (**`DynamoDB Global Tables`**). |
| **`DynamoDB Accelerator (DAX)`** | **In-Memory Cache** | طبقة تخزين مؤقت في الذاكرة مُدارة بالكامل ومصممة خصيصاً لـ `DynamoDB`، تحسّن سرعة القراءة بمقدار **10 أضعاف** لتصل إلى **الميكروثانية (`Microseconds`)**. |
| **`Amazon ElastiCache`** | **In-Memory Cache** | خدمة مُدارة لتشغيل محركات التخزين المؤقت في الذاكرة **`Redis`** و **`Memcached`**. توضع أمام قواعد البيانات (`RDS` أو غيرها) لحفظ نتائج الاستعلامات المتكررة وتخفيف الضغط عن قاعدة البيانات الرئيسية (`Sub-millisecond latency`). |
| **`Amazon Redshift`** | **Data Warehouse (`OLAP`)** | مستودع بيانات سحابي مُدار مخصص **لتحليلات البيانات الضخمة وذكاء الأعمال (`Business Intelligence / Analytics`)** على نطاق البيتابايت (`Petabyte-scale`). يُستخدم للاستعلامات التحليلية المعقدة وإعداد التقارير التاريخية، وليس للمعاملات اليومية للتطبيق (`OLTP`). |
| **`Amazon DocumentDB`** | **NoSQL (Document)** | قاعدة بيانات مستندات مُدارة بالكامل ومتوافقة مع واجهات برمجة **`MongoDB`** لتخزين وفهرسة بيانات `JSON` بسرعة وقابلية توسع عالية. |
| **`Amazon Neptune`** | **Graph Database** | قاعدة بيانات رسوم بيانية مُدارة، مصممة خصيصاً للبيانات شديدة الترابط والعلاقات المعقدة مثل **الشبكات الاجتماعية (`Social Networks`)، ومحركات التوصية (`Recommendation Engines`)، وكشف الاحتيال المالي (`Fraud Detection`)**. |
| **`Amazon MemoryDB`** | **In-Memory (Durable)** | قاعدة بيانات في الذاكرة متوافقة مع `Redis` لكنها توفر **متانة دائمة (`Multi-AZ Durability`)** تتيح استخدامها كقاعدة بيانات أساسية (`Primary Database`) وليست مجرد ذاكرة مؤقتة. |
| **`AWS DMS`** (Database Migration Service) | **Migration** | خدمة لنقل قواعد البيانات من البيئة المحلية (`On-Premises`) إلى AWS **بأقل زمن توقف ممكن (`Near-zero downtime`)** مع بقاء قاعدة البيانات المصدر تعمل طوال فترة النقل. تدعم النقل المتجانس (مثل `MySQL -> MySQL`) وغير المتجانس (مثل `Oracle -> Aurora PostgreSQL` بالتعاون مع أداة `AWS SCT`). |

> [!IMPORTANT]
> **تمييز حاسم داخل `Amazon RDS` يتكرر في الاختبار:**
> * **`RDS Multi-AZ Deployment`:** ينشئ نسخة احتياطية متزامنة (`Synchronous Standby`) في **`Availability Zone`** أخرى. الهدف الوحيد هو **التوافر العالي والتعافي التلقائي (`High Availability & Automatic Failover`)** عند تعطل القاعدة الأساسية. **لا يمكن توجيه استعلامات القراءة إلى النسخة الاحتياطية.**
> * **`RDS Read Replicas`:** تنشئ نسخاً غير متزامنة (`Asynchronous`) مخصصة **للقراءة فقط**. الهدف هو **تحسين الأداء وتوزيع ضغط القراءة والتقارير (`Read Scaling / Performance`)** بعيداً عن قاعدة البيانات الرئيسية.

---

## ثانياً: هندسة الشبكات وتوصيل المحتوى (`Networking & Content Delivery`)

### 1. السحابة الخاصة الافتراضية (`Amazon VPC` — Virtual Private Cloud)
تُمكّنك خدمة **`Amazon VPC`** من إنشاء قسم شبكي خاص ومعزول منطقياً داخل سحابة AWS، تتحكم فيه بالكامل في نطاق عناوين الـ `IP`، والشبكات الفرعية (`Subnets`)، وجداول التوجيه (`Route Tables`)، وبوابات الاتصال.

#### المكونات الجوهرية داخل `Amazon VPC`:
* **`Public Subnet`:** شبكة فرعية يحتوي جدول التوجيه الخاص بها (`Route Table`) على مسار يشير إلى **`Internet Gateway (IGW)`**، مما يسمح للموارد داخلها بالاتصال المباشر مع الإنترنت العام (مثل خوادم الويب و `ALB`).
* **`Private Subnet`:** شبكة فرعية معزولة لا تملك مساراً مباشراً إلى الإنترنت العام، وتُوضَع فيها الموارد الحساسة مثل قواعد البيانات (`RDS`) والخوادم الخلفية.
* **`Internet Gateway (IGW)`:** مكون مُدار وعالي التوافر يُربط بالـ `VPC` لتمكين الاتصال ثنائي الاتجاه بين الموارد في الـ `Public Subnets` والإنترنت العام.
* **`NAT Gateway` (Network Address Translation Gateway):** يُوضَع داخل **`Public Subnet`** ويسمح للخوادم الموجودة في **`Private Subnet`** ببدء اتصال **صادر فقط (`Outbound only`)** نحو الإنترنت (مثلاً لتحميل تحديثات النظام الأمنية)، بينما **يمنع تماماً** أي جهة من الإنترنت العام من بدء اتصال وارد نحو تلك الخوادم الخاصة.
* **`VPC Peering`:** ربط شبكي خاص ومباشر بين شبكتي **`VPC`** (في نفس الحساب أو حسابات مختلفة أو مناطق مختلفة) لتبادل البيانات عبر شبكة AWS الخاصة دون المرور بالإنترنت العام. *(علاقة واحد-إلى-واحد، غير متعدية `Non-transitive`).*
* **`AWS Transit Gateway`:** محور توجيه مركزي (`Central Hub-and-Spoke`) يربط **مئات الـ `VPCs`** وشبكات الشركة المحلية (`On-Premises`) معاً عبر نقطة إدارة مركزية واحدة، مما يلغي تعقيد إدارة مئات روابط الـ `VPC Peering`.
* **`VPC Endpoints` (`AWS PrivateLink`):** تتيح للخوادم داخل الـ `Private Subnet` الوصول المباشر والخاص إلى خدمات AWS الأخرى (مثل `Amazon S3` و `Amazon DynamoDB` و `Amazon Bedrock`) **عبر شبكة AWS الداخلية فقط** دون الحاجة إلى `Internet Gateway` أو `NAT Gateway` ودون خروج البيانات إلى الإنترنت العام.

---

### 2. نظام أسماء النطاقات وتسريع المحتوى العالمي

#### أ. `Amazon Route 53` (خدمة DNS العالمية)
خدمة **`DNS`** سحابية عالية التوافر وقابلة للتوسع (سُمّيت `53` نسبةً إلى المنفذ القياسي لبروتوكول DNS). تؤدي ثلاث وظائف أساسية:
1. تسجيل أسماء النطاقات (`Domain Registration`).
2. توجيه طلبات المستخدمين إلى موارد AWS (مثل `ALB`, `CloudFront`, `S3`) باستخدام سياسات توجيه ذكية (`Routing Policies`) مثل: **`Latency-based`**, **`Geolocation`**, **`Failover`**, و **`Weighted`**.
3. فحص صحة الموارد (`Health Checks`) والتحويل التلقائي بعيداً عن الخوادم المعطلة.

#### ب. المقارنة الدقيقة: `Amazon CloudFront` مقابل `AWS Global Accelerator`

| وجه المقارنة | `Amazon CloudFront` (`CDN`) | `AWS Global Accelerator` |
| :--- | :--- | :--- |
| **آلية العمل** | **تخزين مؤقت (`Caching`)** لنسخ المحتوى في مئات الـ **`Edge Locations`** القريبة من المستخدمين حول العالم. | توجيه حركة المرور عبر **الشبكة العالمية الخاصة لـ AWS (`AWS Global Network`)** بدءاً من أقرب `Edge Location` لتجنب ازدحام الإنترنت العام وتقليل زمن الاستجابة. |
| **البروتوكولات المدعومة** | مثالي للمحتوى الثابت والديناميكي عبر **`HTTP / HTTPS`** (صور، فيديوهات، ملفات ويب، APIs). | مثالي للتطبيقات التي تعتمد على **`TCP / UDP` (Non-HTTP)** مثل الألعاب الجماعية، المكالمات الصوتية (`VoIP`)، وإنترنت الأشياء (`IoT`). |
| **عناوين الـ IP** | عناوين IP ديناميكية تتغير تلقائياً. | يمنحك **عنواني `Static Anycast IP`** ثابتين عالمياً لا يتغيران حتى عند التحويل الفوري بين الـ Regions (`Instant Failover`). |

---

### 3. الاتصال الهجين بين مركز البيانات المحلي و AWS (`Hybrid Connectivity`)

| وجه المقارنة | `AWS Site-to-Site VPN` | `AWS Direct Connect (DX)` |
| :--- | :--- | :--- |
| **مسار الاتصال** | نفق مشفر (`IPsec VPN`) يمر عبر **شبكة الإنترنت العام**. | **خط ألياف ضوئية مادي مخصص ومباشر** يربط مركز بياناتك بـ AWS دون المرور بالإنترنت العام نهائياً. |
| **زمن الإعداد والتكلفة** | سريع الإعداد (دقائق إلى ساعات) ومنخفض التكلفة. | يستغرق **أسابيع إلى شهور** للتجهيز المادي وتكلفته أعلى. |
| **استقرار الأداء** | يعتمد على جودة واستقرار الإنترنت العام. | نطاق ترددي عالٍ (`High Bandwidth`) وزمن استجابة مستقر ومنخفض جداً (**`Consistent Network Performance`**). |
| **التشفير** | مشفر افتراضياً عبر `IPsec`. | غير مشفر تلقائياً افتراضياً؛ يمكن إضافة `VPN` فوقه أو استخدام `MACsec` إذا لزم التشفير. |

---

## منهجية التعامل مع أسئلة Databases & Networking في الاختبار

| مؤشر أو عبارة في نص السؤال | الإجابة الدقيقة |
| :--- | :--- |
| **Managed relational database supporting MySQL, PostgreSQL, Oracle, SQL Server** | **`Amazon RDS`** |
| **Cloud-native relational DB compatible with MySQL/PostgreSQL, up to 5x faster** | **`Amazon Aurora`** |
| **High Availability & automatic failover for an RDS database** | **`RDS Multi-AZ`** |
| **Offload heavy read/reporting traffic from an RDS database** | **`RDS Read Replicas`** |
| **Serverless NoSQL key-value database with single-digit millisecond latency** | **`Amazon DynamoDB`** |
| **Managed in-memory caching (Redis / Memcached) for sub-millisecond reads** | **`Amazon ElastiCache`** |
| **Petabyte-scale Data Warehouse for OLAP / Business Intelligence analytics** | **`Amazon Redshift`** |
| **Graph database for social networks, recommendations, and fraud detection** | **`Amazon Neptune`** |
| **Enable outbound internet access for instances in a Private Subnet (no inbound)** | **`NAT Gateway`** |
| **Private connection from VPC to S3/DynamoDB without traversing the public internet** | **`VPC Endpoints` (`AWS PrivateLink`)** |
| **Connect hundreds of VPCs and on-premises networks via a central hub** | **`AWS Transit Gateway`** |
| **Dedicated private fiber network connection from On-Premises to AWS** | **`AWS Direct Connect`** |
| **Quick encrypted hybrid connection over the public internet** | **`AWS Site-to-Site VPN`** |

---

> **الدرس السابق:** [Domain 3 — الجزء الأول: Compute & Storage](./03_Domain_3_Part1_Compute_and_Storage.md) | **الدرس التالي:** 👉 [03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md](./03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md) | [الفهرس الرئيسي](./README.md)

</div>
