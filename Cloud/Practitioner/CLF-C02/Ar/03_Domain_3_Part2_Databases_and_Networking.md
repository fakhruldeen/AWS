<div dir="rtl">

# 🗄️🌐 Domain 3 (الجزء التاني): Databases & Networking — قواعد البيانات والشبكات

في الجزء ده هنتعرف على إزاي AWS بتخزن البيانات المنظمة (**Databases**) وإزاي بتبني شبكتك وتوصل موقعك للعالم كله بأسرع وقت وأعلى أمان (**Networking & Content Delivery**).

---

## 1️⃣ قواعد البيانات (AWS Database Services)

الأول، إيه الفرق ببساطة بين **SQL (Relational)** و **NoSQL (Non-Relational)**؟
* **SQL (Relational):** بيانات متنظمة في **جداول وصفوف وأعمدة** زي الإكسيل بالظبط، وكل جدول مربوط بالتاني (زي جدول العملاء مربوط بجدول الطلبات).
* **NoSQL (Non-Relational):** بيانات مرنة من غير جداول ثابتة (ممكن تبقى **Key-Value** زي القاموس أو ملفات **JSON**)، وسريعة جداً جداً في التوسع!

### 🗂️ خريطة خدمات الـ Databases في AWS:

| الخدمة | النوع | الشرح بالعامية والمثال المصري |
| :--- | :---: | :--- |
| **`Amazon RDS`** (Relational Database Service) | **SQL (Managed)** | **داتابيز SQL جاهزة ومدارة من AWS:** بتدعم 6 محركات مشهورة (`MySQL`, `PostgreSQL`, `MariaDB`, `Oracle`, `SQL Server`, `Db2`). AWS بتعملك الـ **Backups** وتحديثات الـ **OS Patching** أوتوماتيك! |
| **`Amazon Aurora`** | **SQL (Cloud-Native)** | **الوحش بتاع AWS!** داتابيز SQL معمولة مخصوص للكلاود، متوافقة مع `MySQL` و `PostgreSQL`، **أسرع 5 مرات من MySQL و 3 مرات من PostgreSQL**، وبتخزن 6 نسخ من بياناتك عبر 3 **AZs** أوتوماتيك! |
| **`Amazon DynamoDB`** | **NoSQL (Key-Value)** | **صاروخ الـ NoSQL والـ Serverless!** بترد في **Single-digit milliseconds** مهما كان حجم البيانات، ومش بتدير فيها أي سيرفرات. (لو عايزها أسرع 10 مرات في القراءة بـ **Microseconds** بنحط قدامها **`DynamoDB Accelerator — DAX`**). |
| **`Amazon ElastiCache`** | **In-Memory Cache** | **ذاكرة سريعة جداً (`Redis` / `Memcached`)** بتتحط قدام الداتابيز عشان تشيل الضغط عنها وتحفظ نتايج البحث المتكررة (**Sub-millisecond latency**). |
| **`Amazon Redshift`** | **Data Warehouse (OLAP)** | **مخزن البيانات الضخمة للتحليلات والتقارير (Business Intelligence):** مش للتطبيق اليومي العادي، ده عشان تحلل تيرابايتس وبيتابايتس من بيانات المبيعات لآخر 10 سنين وتطلع تقارير للإدارة! |
| **`Amazon DocumentDB`** | **Document (NoSQL)** | نسخة مدارة من AWS متوافقة مع **`MongoDB`** لتخزين ملفات الـ JSON. |
| **`Amazon Neptune`** | **Graph Database** | **داتابيز العلاقات والشبكات:** ممتازة لشبكات التواصل الاجتماعي (مين صاحب مين؟)، وأنظمة التوصيات (**Recommendation Engines**)، وكشف الاحتيال (**Fraud Detection**). |
| **`Amazon MemoryDB`** | **In-Memory (Durable)** | زي Redis بس بيحفظ البيانات بشكل دائم (**Durable**) كداتابيز أساسية. |
| **`AWS DMS`** (Database Migration Service) | **Migration** | **عربية النقل للداتابيز:** بتنقل الداتابيز بتاعتك من شركتك (**On-Premises**) لـ AWS بأقل وقت توقف (**Near-zero downtime**)، وتقدر تحول حتى من Oracle لـ PostgreSQL! |

> [!IMPORTANT]
> **فرق مهم جداً في الامتحان داخل `Amazon RDS`:**
> * **`Multi-AZ`:** نسخة احتياطية متزامنة في **AZ** تانية عشان **High Availability / Disaster Recovery** (لو الداتابيز الأساسية وقعت، التانية تشتغل مكانها أوتوماتيك — **Failover**). **ما تقدرش تقرأ منها!**
> * **`Read Replicas`:** نسخ للقراءة بس عشان **Performance / Read Scaling** (تخفف ضغط القراءة والتقارير عن الداتابيز الأساسية!).

---

## 2️⃣ الشبكات وتوصيل المحتوى (Networking & Content Delivery)

### 🏙️ 1. `Amazon VPC` (Virtual Private Cloud)
تخيل الـ **VPC** كأنها **مدينتك أو كومباوندك الخاص المعزول** جوه AWS. إنت اللي بترسم الشوارع وتتحكم مين يدخل ومين يخرج:

* **Public Subnet:** شارع ليه بوابة مباشرة على الإنترنت (**Internet Gateway — IGW**). بنحط فيه السيرفرات اللي الناس بتدخل عليها (زي الـ Web Servers و الـ Load Balancer).
* **Private Subnet:** شارع داخلي مقفول محدش من الإنترنت يقدر يدخله مباشرة. بنحط فيه الداتابيز (`RDS`) والبيانات السرية.
* **`Internet Gateway (IGW)`:** **البوابة الرئيسية** اللي بتوصل الـ VPC بالإنترنت العام.
* **`NAT Gateway`:** لو سيرفر في الـ **Private Subnet** محتاج ينزل تحديث (**Update**) من الإنترنت، بيخرج عن طريق الـ **NAT Gateway** (يعني يخرج للإنترنت يجيب حاجة ويرجع، **بس محدش من الإنترنت يقدر يبدأ اتصال معاه من برة!**).
* **`VPC Peering`:** وصلة خاصة بتربط **2 VPCs** ببعض عشان يكلموا بعض بشكل خاص من غير الإنترنت العام.
* **`AWS Transit Gateway`:** **ميدان التحرير / المركز الرئيسي (Hub-and-Spoke)!** لو عندك عشرات الـ VPCs وشبكة شركتك On-Premises وعايز تربطهم كلهم ببعض بطريقة منظمة بدل ما تعمل مئات الوصلات!
* **`VPC Endpoints` (`AWS PrivateLink`):** بتخلي سيرفراتك جوه الـ Private Subnet تكلم خدمات AWS (زي `S3` أو `DynamoDB`) **عن طريق شبكة AWS الداخلية الخاصة** من غير ما تخرج على الإنترنت العام خالص!

---

### 🌍 2. توصيل الموقع للعملاء في العالم كله (`Route 53`, `CloudFront`, `Global Accelerator`)

* **`Amazon Route 53` (DNS Service):**
  * خدمة الـ **DNS** العالمية بتاعة AWS (بالمناسبة: سموها 53 عشان بورت الـ DNS هو 53!).
  * بتسجل بيها أسماء الدومينات (زي `myshop.com`) وتوجه الزوار لسيرفراتك (وتقدر تعمل **Health Checks** وتوجيه ذكي زي **Latency-based routing** أو **Geolocation** أو **Failover**).

* **`Amazon CloudFront` vs. `AWS Global Accelerator` — مقارنة بتيجي كتير في الامتحان!**

| المقارنة | `Amazon CloudFront` (CDN) | `AWS Global Accelerator` |
| :--- | :--- | :--- |
| **الفكرة بالبلدي** | **فروع تخزين مؤقت (`Caching`) في كل العالم** (في الـ **Edge Locations**) بتحفظ نسخة من صور وفيديوهات موقعك قريبة من المستخدم. | **طريق سريع خاص (`AWS Global Network`)** بياخد حركة البيانات بتاعتك من أقرب Edge Location ويوصلها لسيرفرك بأسرع طريق من غير زحمة الإنترنت العام! |
| **نوع البيانات** | ممتاز للمحتوى الثابت والديناميكي (**HTTP/HTTPS — صور، فيديوهات، مواقع**). | ممتاز للـ **Non-HTTP (TCP/UDP)** زي الألعاب الأونلاين، مكالمات الـ VoIP، وتطبيقات الـ IoT، وبيديك **2 Static Anycast IP Addresses**. |

---

### 🔌 3. ربط شركتك على الأرض بـ AWS (Hybrid Connectivity)

لو عندك فرع شركة حقيقي (**On-Premises Data Center**) وعايز توصله بالـ VPC بتاعتك على AWS، عندك حلّين:

| المقارنة | `AWS Site-to-Site VPN` | `AWS Direct Connect (DX)` |
| :--- | :--- | :--- |
| **التشبيه المصري** | **عربية مصفحة ماشية على الطريق الدائري العام (الإنترنت العام):** مشفرة وآمنة، بس ممكن تقابل زحمة الإنترنت. | **خط مترو خاص ومباشر من باب شركتك لباب AWS!** كابل ألياف ضوئية خاص مبيمرش على الإنترنت العام نهائياً. |
| **وقت التركيب** | **سريع جداً (في دقايق/ساعات)** ورخيص. | بياخد **أسابيع أو شهور** وتكلفته أعلى. |
| **السرعة والاستقرار** | بتعتمد على سرعة الإنترنت العام عندك. | سرعة رهيبة ومستقرة جداً (**Consistent Low Latency / High Bandwidth**). |

---

## 🎯 زتونة الامتحان للجزء التاني (Databases & Networking)

| لو شفت في السؤال... | الإجابة الصح فوراً! |
| :--- | :--- |
| **Managed relational database (MySQL, PostgreSQL, Oracle, SQL Server)** | **`Amazon RDS`** |
| **High Availability / Automatic Failover for RDS** | **`RDS Multi-AZ`** |
| **Offload read-heavy queries / reporting traffic from RDS** | **`RDS Read Replicas`** |
| **Serverless NoSQL key-value database with single-digit millisecond latency** | **`Amazon DynamoDB`** |
| **In-memory caching (Redis / Memcached) to speed up database reads** | **`Amazon ElastiCache`** |
| **Petabyte-scale Data Warehouse for Business Intelligence (OLAP)** | **`Amazon Redshift`** |
| **Graph database for social networks / fraud detection / recommendations** | **`Amazon Neptune`** |
| **Allow instances in a Private Subnet to access the internet for updates (outbound only)** | **`NAT Gateway`** |
| **Dedicated private physical fiber connection from On-Premises to AWS (no public internet)** | **`AWS Direct Connect`** |
| **Quick encrypted connection from On-Premises to AWS over the public internet** | **`AWS Site-to-Site VPN`** |
| **Connect hundreds of VPCs and on-premises networks via a central hub** | **`AWS Transit Gateway`** |
| **CDN to cache static content at Edge Locations globally** | **`Amazon CloudFront`** |
| **Connect privately from VPC to S3/DynamoDB without going over the internet** | **`VPC Endpoints` (`AWS PrivateLink`)** |

---

> ⬅️ **الدرس السابق:** [Domain 3 — الجزء الأول: Compute & Storage](./03_Domain_3_Part1_Compute_and_Storage.md) | **الدرس التالي:** 👉 **[03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md](./03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md)** | [الفهرس](./README.md)

</div>
