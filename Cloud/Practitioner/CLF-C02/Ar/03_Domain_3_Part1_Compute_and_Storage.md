<div dir="rtl">

# 🖥️ Domain 3 (الجزء الأول): Compute & Storage — السيرفرات والتخزين

الـ Domain التالت (**Cloud Technology and Services**) هو أكبر جزء في الامتحان (**34%**). عشان يبقى خفيف وسهل في المذاكرة، قسمناه لـ 3 ملفات، وهنا هنبدأ بأهم حاجتين: **الـ Compute (السيرفرات)** و **الـ Storage (التخزين)**.

---

## 1️⃣ خدمات السيرفرات والحوسبة (Compute Services)

### 🖥️ 1. `Amazon EC2` (Elastic Compute Cloud)
دي أشهر خدمة في AWS كلها — عبارة عن **سيرفر افتراضي (Virtual Machine)** بتأجره على الكلاود وتختارله الويندوز أو اللينكس اللي يعجبك وحجم الـ CPU والـ RAM.

#### 🏷️ عائلات الـ EC2 (Instance Families — بتيجي كتير في الامتحان!):
* **General Purpose (`T`, `M`):** متوازن (CPU و RAM و Network معقولين) — ممتاز لمواقع الويب العادية.
* **Compute Optimized (`C`):** بروسيسور جبار — للألعاب، معالجة الفيديو، والحسابات التقيلة (`High-performance computing`).
* **Memory Optimized (`R`, `X`):** RAM ضخمة جداً — لقواعد البيانات الكبيرة في الذاكرة (`In-memory databases`) وتحليل البيانات الضخمة.
* **Storage Optimized (`I`, `D`):** هاردات فائقة السرعة — للتطبيقات اللي بتقرأ وتكتب بيانات ضخمة بسرعة عالية (`High IOPS`).
* **Accelerated Computing (`P`, `G`):** فيه كروت شاشة (**GPU**) — للذكاء الاصطناعي (**Machine Learning**) والجرافيك.

#### 💰 خطط تسعير الـ EC2 (EC2 Pricing Models — سؤال مؤكد 100% في الامتحان!):

| الخطة | الفكرة بالبلدي والمصري | امتى تختارها؟ |
| :--- | :--- | :--- |
| **On-Demand** | **ادفع بالثانية/الساعة من غير أي التزام** — أغلى سعر بس حرية كاملة تطفي وتشغل براحتك. | شغل قصير، متقطع، مش عارف هياخد وقت قد إيه (**Unpredictable / Short-term**). |
| **Savings Plans** | **عقد التزام لمدة سنة أو 3 سنين** إنك تصرف مبلغ معين في الساعة (مثلاً \$10/ساعة) وتاخد خصم يوصل لـ **72%**. مرن جداً (بيغطي EC2 و Fargate و Lambda). | شغل ثابت ومستمر ومحتاج مرونة في تغيير نوع السيرفر أو الـ Region. |
| **Reserved Instances (RI)** | زي Savings Plans (عقد سنة أو 3 سنين وخصم لحد **72%**) بس مرتبط بنوع سيرفر معين في Region معينة. | شغل ثابت ومستقر (**Steady-state / Predictable workloads**). |
| **Spot Instances** | **مزاد البواقي!** بتشتري السيرفرات الفاضية عند AWS بخصم خرافي يوصل لـ **90%**! بس خلي بالك: AWS ممكن تاخد السيرفر منك تاني بإنذار **دقيقتين بس** لو احتاجته! | شغل يقدر يقف ويكمل تاني (**Fault-tolerant / Stateless / Batch jobs**). **أوعى تستخدمه للداتابيز!** |
| **Dedicated Hosts** | بتأجر **سيرفر فيزيائي كامل (`Physical Server`) ليك لوحدك** محدش بيشاركك فيه. | لو عندك رخص برامج قديمة مربوطة بعدد الـ Sockets/Cores (**BYOL — Bring Your Own License**) أو قوانين امتثال صارمة. |

---

### ⚖️ 2. التوزيع والتوسع التلقائي (`ELB` & `Auto Scaling`)
* **`Elastic Load Balancing (ELB)`:** **ظابط المرور** اللي واقف قدام سيرفراتك بيوزع الزوار بالتساوي عليهم، ولو سيرفر وقع مش بيبعتله حد (**Health Checks**):
  * **`ALB` (Application Load Balancer):** ذكي جداً، شغال على Layer 7 (**HTTP/HTTPS**)، بيفهم الروابط (مثلاً `/images` تروح لسيرفر و `/videos` تروح لسيرفر تاني).
  * **`NLB` (Network Load Balancer):** صاروخ في السرعة! شغال على Layer 4 (**TCP/UDP**)، بيتحمل ملايين الطلبات في الثانية مع **Ultra-low latency** وبيديك **Static IP**.
* **`Amazon EC2 Auto Scaling`:** لما الزوار يزيدوا، بيزود عدد سيرفرات الـ EC2 أوتوماتيك (**Scale Out**)، ولما يقلوا، بيطفي السيرفرات الزيادة أوتوماتيك (**Scale In**) عشان توفر فلوس!

---

### ⚡ 3. الـ Serverless والحاويات (Serverless & Containers)

* **`AWS Lambda` (Serverless Compute):**
  * **بدون سيرفرات نهائياً!** إنت بتكتب الكود بتاعك (Python, Node.js, Java...) وبترفعه بس.
  * الكود بيشتغل بس لما يحصل حدث (**Event-driven** — زي حد يرفع صورة على S3 أو يضغط زرار)، وبتدفع بالملي ثانية على قد وقت تشغيل الكود بس! لو محدش استخدمه بتدفع **صفر**! *(أقصى مدة تشغيل للمرة الواحدة: 15 دقيقة).*
* **`Amazon ECS` (Elastic Container Service):** خدمة من AWS لإدارة وتشغيل الـ **Docker Containers** بسهولة.
* **`Amazon EKS` (Elastic Kubernetes Service):** لو فريقك بيستخدم **Kubernetes** وعايز AWS تديرهولك.
* **`AWS Fargate`:** **Serverless للـ Containers!** بتشغل الـ Containers على ECS أو EKS من غير ما تدير ولا سيرفر EC2 واحد تحتهم!
* **`AWS Elastic Beanstalk` (PaaS):** ارفع الكود بتاع موقعك بس، و Elastic Beanstalk هيعملك الـ EC2 والـ Load Balancer والـ Auto Scaling أوتوماتيك من غير ما توجع دماغك بالبنية التحتية (الخدمة نفسها مجانية وبتدفع تمن الموارد بس).
* **`Amazon Lightsail`:** أسهل وأبسط خدمة للمبتدئين والشركات الصغيرة — موقع ووردبريس أو سيرفر بسيط بسعر شهري ثابت ومحدد (**Fixed monthly pricing**).

---

## 2️⃣ خدمات التخزين (Storage Services)

### 🪣 1. `Amazon S3` (Simple Storage Service)
**مخزن الملفات اللا نهائي على الإنترنت (`Object Storage`)!**
* بتحط ملفاتك (`Objects`) جوه جرادل اسمها **`Buckets`** (اسم الـ Bucket لازم يكون **فريد على مستوى العالم كله — Globally Unique**).
* أقصى حجم للملف الواحد: **5 TB**.
* **الاعتمادية (`Durability`):** **`99.999999999%` (11 Nines!)** — يعني مستحيل ملفك يضيع!
* تقدر تستضيف عليه موقع ثابت (**Static Website Hosting** — HTML/CSS/JS).

#### 📦 فئات تخزين S3 (`S3 Storage Classes` — مهم جداً في الامتحان!):

| الفئة (`Storage Class`) | التشبيه المصري | امتى تستخدمها؟ |
| :--- | :--- | :--- |
| **`S3 Standard`** | **مكتبك اللي إيدك فيه كل يوم** | بيانات بتفتحها كتير جداً (**Frequently accessed**) ومحتاجها فوراً. |
| **`S3 Intelligent-Tiering`** | **المساعد الذكي** | لما ما تكونش عارف البيانات دي هتتفتح كتير ولا قليل (**Unknown or changing access patterns**). بينقلها أوتوماتيك للأرخص! |
| **`S3 Standard-IA` (Infrequent Access)** | **الرف العالي في الدولاب** | بيانات مش بتفتحها كتير، بس لو احتجتها لازم تطلع في نفس اللحظة (**Immediate access**). |
| **`S3 One Zone-IA`** | زي اللي فوق بس متخزنة في **AZ واحدة بس** (أرخص 20%) | لبيانات نقدر نعملها تاني بسهولة (**Re-creatable data** زي صور مصغرة Thumbnails). |
| **`S3 Glacier Instant Retrieval`** | **مخزن الأرشيف السريع** | أرشيف بتفتحه مرة كل 3 شهور بس عايزه يفتح في أجزاء من الثانية (**Milliseconds**). |
| **`S3 Glacier Flexible Retrieval`** | **أرشيف في المخزن تحت** | أرشيف رخيص جداً، لما تطلبه بياخد من **دقايق لساعات** عشان يرجعلك. |
| **`S3 Glacier Deep Archive`** | **خزنة في قبو البنك!** | **أرخص تخزين في AWS كلها!** لأرشيف قانوني مش بتفتحه غير مرة كل كام سنة، وبياخد من **12 لـ 48 ساعة** عشان يرجعلك. |

> [!TIP]
> **`S3 Lifecycle Policies`:** قواعد أوتوماتيك بتقول لـ S3: "أي ملف يعدي عليه 30 يوم انقله لـ `Standard-IA`، وبعد 90 يوم انقله لـ `Glacier Deep Archive`، وبعد 7 سنين امسحه!". دي بتوفر فلوس بالهبل!

---

### 💾 2. باقي خدمات التخزين المهمة:

| الخدمة | النوع | المعنى بالبلدي والمصري |
| :--- | :---: | :--- |
| **`Amazon EBS` (Elastic Block Store)** | **Block Storage** | **هارد الشبكة بتاع سيرفر EC2.** بيفضل محتفظ ببياناتك حتى لو طفيت السيرفر. مربوط بـ **AZ واحدة** (وتقدر تاخد منه نسخة احتياطية **EBS Snapshot** بتتخزن في S3). |
| **`EC2 Instance Store`** | **Temporary Block** | **هارد مؤقت (`Ephemeral`)** لازق في السيرفر الحقيقي، سريع جداً زي الصاروخ، بس **لو طفيت السيرفر البيانات بتتمسح!** (ممتاز للـ Cache والملفات المؤقتة بس). |
| **`Amazon EFS` (Elastic File System)** | **File Storage (Linux)** | **فولدر مشترك (`NFS`)** لمئات سيرفرات الـ Linux **في أكتر من AZ في نفس الوقت**، وبيكبر ويصغر لوحده أوتوماتيك! |
| **`Amazon FSx`** | **File Storage (Windows/HPC)** | لو محتاج **Windows File Server (`SMB`)** أو نظام ملفات فائق السرعة (`FSx for Lustre`). |
| **`AWS Storage Gateway`** | **Hybrid Storage** | **الكوبري** اللي بيربط سيرفراتك اللي في الشركة (**On-Premises**) بمساحات التخزين في **AWS Cloud** (`S3`). |
| **`AWS Backup`** | **Centralized Backup** | مكان واحد مركزي تعمل منه **Backups** أوتوماتيك لكل خدمات AWS (EBS, RDS, DynamoDB, EFS). |

---

## 🎯 زتونة الامتحان للجزء الأول (Compute & Storage)

| لو شفت في السؤال... | الإجابة الصح فوراً! |
| :--- | :--- |
| **Up to 90% discount, fault-tolerant / interruptible batch workloads** | **`EC2 Spot Instances`** |
| **Steady-state workload, 1-year or 3-year commitment, up to 72% discount** | **`Savings Plans` or `Reserved Instances`** |
| **Run code without managing servers, pay only for compute time consumed** | **`AWS Lambda`** |
| **Run containers without managing underlying EC2 servers** | **`AWS Fargate`** |
| **Deploy web app quickly without managing infrastructure (PaaS)** | **`AWS Elastic Beanstalk`** |
| **Lowest-cost long-term archival storage (retrieval in 12–48 hours)** | **`S3 Glacier Deep Archive`** |
| **Unknown or unpredictable data access patterns in S3** | **`S3 Intelligent-Tiering`** |
| **Shared file system accessible by multiple Linux EC2 instances across AZs** | **`Amazon EFS`** |
| **Persistent block-level storage volume attached to a single EC2 instance** | **`Amazon EBS`** |
| **Connect on-premises storage to AWS Cloud storage (Hybrid)** | **`AWS Storage Gateway`** |

---

> ⬅️ **الدرس السابق:** [Domain 2: Security & Compliance](./02_Domain_2_Security_and_Compliance.md) | **الدرس التالي:** 👉 **[03_Domain_3_Part2_Databases_and_Networking.md](./03_Domain_3_Part2_Databases_and_Networking.md)** | [الفهرس](./README.md)

</div>
