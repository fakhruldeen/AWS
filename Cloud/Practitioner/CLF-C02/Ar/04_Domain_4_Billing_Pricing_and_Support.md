<div dir="rtl">

# 💰📞 Domain 4: Billing, Pricing, and Support (12% من الامتحان)

الـ Domain الرابع عليه **12%** من الامتحان، وأسئلته سهلة جداً ومباشرة ومضمونة 100% لو حفظت الفرق بين أدوات الفواتير وباقات الدعم (**AWS Support Plans**)!

---

## 1️⃣ فلسفة التسعير في AWS (AWS Pricing Philosophy)

فيه **3 قواعد ذهبية** للتسعير في AWS:
1. **Pay-as-you-go (ادفع على قد استهلاكك):** مفيش عقود إلزامية طويلة لو مش عايز، طفيت السيرفر = الفاتورة تقف.
2. **Save when you reserve (وفّر لما تحجز مقدماً):** لو التزمت بسنة أو 3 سنين (**Savings Plans** أو **Reserved Instances**) بتاخد خصم يوصل لـ **72%**.
3. **Pay less by using more (كل ما تستخدم أكتر، سعر الوحدة يقل):** خصومات الكميات (**Volume-based Discounts**) زي التخزين في `Amazon S3`.

### 💸 إيه أكتر 3 حاجات بتدفع عليهم فلوس في AWS؟ (The 3 Fundamental Cost Drivers)
1. **Compute:** وقت تشغيل السيرفرات (`EC2`, `Lambda`).
2. **Storage:** حجم البيانات المتخزنة (`S3`, `EBS`, `RDS`).
3. **Outbound Data Transfer (البيانات اللي بتخرج من AWS للإنترنت):**
   * **معلومة بتيجي في الامتحان كتير:** رفع البيانات لـ AWS (**Data Transfer IN**) **مجاني 100%!** إنما سحب البيانات من AWS للإنترنت (**Data Transfer OUT**) هو اللي عليه فلوس!

### 🎁 أنواع الـ `AWS Free Tier`:
1. **Always Free (مجاني للأبد):** زي 1 مليون طلب شهرياً على `AWS Lambda`، و 25 GB على `Amazon DynamoDB`.
2. **12 Months Free (مجاني لأول سنة من فتح الحساب):** زي 750 ساعة شهرياً من `Amazon EC2` (`t2.micro` / `t3.micro`) و 5 GB على `Amazon S3`.
3. **Short-term Trials (تجربة مؤقتة):** زي شهر أو شهرين مجاناً لخدمات معينة زي `Amazon SageMaker` أو `Amazon Redshift`.

---

## 2️⃣ أدوات الفواتير وإدارة التكاليف (Billing & Cost Management Tools)

الجدول ده **كنز في الامتحان** — كل أداة وليها كلمة مفتاحية واحدة بتكشفها فوراً:

| الأداة | بتعمل إيه بالبلدي والمصري؟ | الكلمة المفتاحية في الامتحان |
| :--- | :--- | :--- |
| **`AWS Pricing Calculator`** | **الآلة الحاسبة قبل ما تبدأ:** قبل ما تنقل لـ AWS، بتدخل عليها وتحسب "لو شغلت 5 سيرفرات EC2 وداتابيز RDS هيكلفوني كام في الشهر تقريباً؟". | **Estimate monthly cost BEFORE deploying** |
| **`AWS Budgets`** | **الإنذار المبكر للميزانية:** بتقولها "ابعتيلي إيميل أو SMS فوراً لو فاتورتي وصلت \$50 أو متوقع توصل \$50 قبل آخر الشهر!". (ممكن كمان تقفل موارد أوتوماتيك!). | **Set custom cost/usage alerts & thresholds** |
| **`AWS Cost Explorer`** | **الرسوم البيانية والتحليل:** بيوريك صرفت كام الشهر اللي فات، وآخر 12 شهر، **ويتوقعلك هتصرف كام في الـ 12 شهر الجايين (`Forecast`)**! | **Visualize historical costs & forecast future spend** |
| **`AWS Cost and Usage Report (CUR)`** | **كشف الحساب التفصيلي جداً:** أدق وأشمل ملف (CSV/Parquet) بيتحفظ في `S3` فيه تفاصيل كل سنت وكل ساعة استهلاك لكل خدمة. | **Most comprehensive / granular billing data** |
| **`Cost Allocation Tags`** | **الاستيكرات (Labels):** بتحط Tag على كل سيرفر زي `Department: Marketing` أو `Project: App1` عشان آخر الشهر تعرف كل قسم صرف كام بالظبط! | **Track / categorize costs by department or project** |
| **`AWS Compute Optimizer`** | **خبير تقليص الأحجام (`Rightsizing`):** بيستخدم الـ **Machine Learning** عشان يقولك "السيرفر ده كبير أوي على شغلك، صغّره عشان توفر فلوس!". | **ML-powered rightsizing recommendations** |
| **`Consolidated Billing`** (جوه `AWS Organizations`) | **الفاتورة المجمعة:** بتجمع كل حسابات الشركة في فاتورة واحدة، فتاخد خصومات حجم أعلى (**Volume Discounts**) وتشارك الـ **Reserved Instances** بين الحسابات. | **Single bill across multiple accounts + volume discounts** |

---

## 3️⃣ باقات الدعم الفني (`AWS Support Plans`) — سؤال أكيد في الامتحان!

AWS عندها 5 باقات دعم فني، ركّز على الفروقات الذهبية دي:

| الباقة | السعر التقريبي | مين يقدر يكلم الدعم؟ وأسرع وقت رد (`SLA`) | المميزات الحصرية في الامتحان |
| :--- | :--- | :--- | :--- |
| **`Basic Support`** | **مجاني ($0)** | خدمة عملاء للفواتير والحساب بس (مفيش دعم تقني للمهندسين!) | `AWS Health Dashboard` + الـ **7 Core Checks** بس في `Trusted Advisor`. |
| **`Developer Support`** | تبدأ من **\$29/شهر** | دعم تقني عبر **الإيميل فقط** في ساعات العمل (`12–24 ساعة`). | شخص واحد بس يفتح تذاكر دعم؛ ممتاز للتجربة والـ Development. |
| **`Business Support`** | تبدأ من **\$100/شهر** | **دعم تقني 24/7** (تليفون + شات + إيميل). رد في أقل من **1 ساعة** لو السيستم الإنتاجي واقع (**Production System Down**). | **أول باقة بتفتحلك كل فحوصات `AWS Trusted Advisor` الكاملة (`Full Set`)** + دعم لبرامج الطرف التالت! |
| **`Enterprise On-Ramp`** | تبدأ من **\$5,500/شهر** | رد في أقل من **30 دقيقة** لو السيستم الحساس واقع (**Business-Critical System Down**). | بيديك وصول لـ **فريق من الـ TAMs** (مش واحد مخصص ليك لوحدك) + `Concierge Support`. |
| **`Enterprise Support`** | تبدأ من **\$15,000/شهر** | **أسرع رد في AWS: أقل من 15 دقيقة** لو السيستم الحساس واقع (**Business-Critical System Down**)! | **مهندس مخصص ليك لوحدك: `Designated Technical Account Manager (TAM)`** + `AWS Support Concierge` (للفواتير) + `Infrastructure Event Management (IEM)` مجاناً! |

> [!TIP]
> **الزتونة السريعة لباقات الدعم (احفظ الـ 4 كلمات دول بس!):**
> * **`Basic`** = مجاني، 7 فحوصات Trusted Advisor بس، مفيش دعم تقني.
> * **`Business`** = أرخص باقة فيها **24/7 Support** + **Full `Trusted Advisor` checks** + رد **1 ساعة** للـ Production Down.
> * **`Enterprise On-Ramp`** = رد **30 دقيقة** + فريق TAM مشترك.
> * **`Enterprise`** = رد **15 دقيقة** + **`Designated TAM`** مخصص ليك + **`Concierge Support`**!

---

## 4️⃣ السوق والشركاء (`AWS Marketplace` & `APN`)

* **`AWS Marketplace`:** **متجر التطبيقات بتاع AWS** (زي App Store أو Google Play بس للشركات!). تقدر تشتري منه برامج جاهزة من شركات تانية (زي Firewalls من Cisco أو Palo Alto، أو WordPress، أو أدوات AI) وتنزلها على حسابك وتتحاسب عليها في **نفس فاتورة AWS**!
* **`AWS Partner Network (APN)`:** شبكة عالمية من الشركات الاستشارية (`Consulting Partners`) والتقنية (`Technology Partners`) المعتمدة من AWS اللي تقدر تستعين بيها تساعدك تبني وتنقل شغلك على الكلاود.
* **`AWS Professional Services`:** فريق مهندسين وخبراء من شركة AWS نفسها بيساعدوا الشركات الكبيرة جداً في التخطيط والانتقال للكلاود.

---

## 🎯 زتونة الامتحان لـ Domain 4

| لو شفت في السؤال... | الإجابة الصح فوراً! |
| :--- | :--- |
| **Estimate cost of an architecture BEFORE building it** | **`AWS Pricing Calculator`** |
| **Receive an alert when monthly spend exceeds a set threshold** | **`AWS Budgets`** |
| **Analyze past spending trends and forecast future costs** | **`AWS Cost Explorer`** |
| **Most detailed, granular billing report stored in S3** | **`AWS Cost and Usage Report (CUR)`** |
| **Track costs per department or project** | **`Cost Allocation Tags`** |
| **Lowest-cost support plan with 24/7 technical support & full Trusted Advisor** | **`AWS Business Support`** |
| **Support plan that provides a dedicated Technical Account Manager (TAM) & 15-min SLA** | **`AWS Enterprise Support`** |
| **Concierge team for billing & account inquiries** | **`AWS Enterprise Support` (أو Enterprise On-Ramp)** |
| **Buy third-party software pre-configured for AWS on your AWS bill** | **`AWS Marketplace`** |
| **Is Data Transfer IN (uploading to AWS) free or paid?** | **FREE (مجاني!) — إنت بتدفع على الـ Data Transfer OUT بس!** |

---

> ⬅️ **الدرس السابق:** [Domain 3 — الجزء التالت](./03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md) | **الدرس التالي (الأهم لليلة الامتحان!):** 👉 **[05_Exam_Tricks_and_Comparison_CheatSheet.md](./05_Exam_Tricks_and_Comparison_CheatSheet.md)** | [الفهرس](./README.md)

</div>
