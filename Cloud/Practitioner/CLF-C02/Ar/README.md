<div dir="rtl">

# الدليل العربي الشامل لشهادة AWS Certified Cloud Practitioner (CLF-C02)

مرحباً بك في الدليل التعليمي العربي الشامل والمفصّل لمسار شهادة **AWS Certified Cloud Practitioner (`CLF-C02`)**. تم إعداد هذا الدليل بلغة عربية واضحة، موزونة، ورصينة تهدف إلى تبسيط المفاهيم الهندسية والمعمارية للحوسبة السحابية (**Cloud Computing**) وشرح خدمات **Amazon Web Services (AWS)** بعمق وتفصيل، مع الإبقاء على جميع أسماء الخدمات والمصطلحات التقنية باللغة الإنجليزية كما ترد في الوثائق الرسمية والاختبار الدولي.

> [!NOTE]
> **منهجية هذا الدليل:**
> * **الوضوح والعمق:** شرح مفصّل لكل مفهوم وخدمة يشمل آلية العمل، المكونات الأساسية، حالات الاستخدام العملية، والفروق الدقيقة بين الخدمات المتشابهة.
> * **الدقة المصطلحية:** الإبقاء على المصطلحات التقنية وأسماء خدمات AWS باللغة الإنجليزية (مثل `Amazon EC2`, `IAM`, `High Availability`, `Shared Responsibility Model`) لربط الفهم النظري بصياغة أسئلة الاختبار الرسمية وبيئة العمل الفعلية.
> * **الاستعداد للاختبار:** يتضمن كل قسم خلاصة مركزة ومنهجية واضحة لتحليل أسئلة الاختيار من متعدد (`MCQ`) وتجنب الخيارات المضللة.

---

## بطاقة تعريفية باختبار AWS CLF-C02

| العنصر | التفاصيل الرسمية |
| :--- | :--- |
| **رمز الاختبار** | `CLF-C02` (AWS Certified Cloud Practitioner) |
| **المستوى** | تأسيسي (`Foundational`) |
| **عدد الأسئلة** | 65 سؤالاً (50 سؤالاً مُقيّماً بالدرجات + 15 سؤالاً تجريبياً غير محسوب في النتيجة) |
| **المدة الزمنية** | 90 دقيقة (يمكن لغير الناطقين بالإنجليزية طلب تمديد مجاني لمدة 30 دقيقة إضافية تحت بند `ESL +30` قبل حجز موعد الاختبار) |
| **درجة النجاح** | 700 من أصل 1000 درجة (نظام تقييم متدرج `Scaled Scoring`) |
| **أنماط الأسئلة** | اختيار إجابة واحدة صحيحة (`Multiple Choice`) أو اختيار إجابتين صحيحتين من بين خمسة خيارات (`Multiple Response`) |

---

## هيكل الدليل وتوزيع مجالات الاختبار (Exam Domains)

| القسم | المجال والموضوع | الوزن النسبي في الاختبار | الرابط |
| :---: | :--- | :---: | :--- |
| **التمهيد** | **الأساسيات التقنية للحوسبة السحابية (Prerequisites)** | تأسيس تقني شامل | [00_Prerequisites_Asasiyat_ElCloud.md](./00_Prerequisites_Asasiyat_ElCloud.md) |
| **Domain 1** | **Cloud Concepts** (مفاهيم الحوسبة السحابية والبنية التحتية العالمية) | **24%** | [01_Domain_1_Cloud_Concepts.md](./01_Domain_1_Cloud_Concepts.md) |
| **Domain 2** | **Security and Compliance** (الأمن السيبراني وإدارة الهوية والامتثال) | **30%** | [02_Domain_2_Security_and_Compliance.md](./02_Domain_2_Security_and_Compliance.md) |
| **Domain 3** | **Cloud Technology and Services** (التقنيات والخدمات السحابية) | **34%** | مقسّم إلى 3 أجزاء تفصيلية 👇 |
| ↳ **3.1** | ↳ **Compute & Storage** (الحوسبة والخوادم وأنظمة التخزين) | ضمن 34% | [03_Domain_3_Part1_Compute_and_Storage.md](./03_Domain_3_Part1_Compute_and_Storage.md) |
| ↳ **3.2** | ↳ **Databases & Networking** (قواعد البيانات وهندسة الشبكات) | ضمن 34% | [03_Domain_3_Part2_Databases_and_Networking.md](./03_Domain_3_Part2_Databases_and_Networking.md) |
| ↳ **3.3** | ↳ **Integration, Monitoring, Migration & AI/ML** | ضمن 34% | [03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md](./03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md) |
| **Domain 4** | **Billing, Pricing, and Support** (التسعير وإدارة التكاليف وباقات الدعم) | **12%** | [04_Domain_4_Billing_Pricing_and_Support.md](./04_Domain_4_Billing_Pricing_and_Support.md) |
| **المراجعة** | **دليل المقارنات المعمارية ومنهجية حل الأسئلة (X vs Y)** | مراجعة شاملة قبل الاختبار | [05_Exam_Tricks_and_Comparison_CheatSheet.md](./05_Exam_Tricks_and_Comparison_CheatSheet.md) |

---

## خطة الدراسة الموصى بها (خلال 7 إلى 10 أيام)

1. **اليوم الأول:** دراسة ملف [الأساسيات التقنية](./00_Prerequisites_Asasiyat_ElCloud.md) لبناء تصور واضح للخوادم والشبكات والتخزين والتشفير، ثم قراءة [Domain 1](./01_Domain_1_Cloud_Concepts.md).
2. **اليوم الثاني والثالث:** التعمق في [Domain 2 (الأمن والامتثال)](./02_Domain_2_Security_and_Compliance.md) نظراً لوزنه الكبير (30%) وأهمية استيعاب `Shared Responsibility Model` و `IAM`.
3. **اليوم الرابع:** دراسة [Domain 3 — الجزء الأول (Compute & Storage)](./03_Domain_3_Part1_Compute_and_Storage.md) مع التركيز على نماذج تسعير `Amazon EC2` وفئات تخزين `Amazon S3`.
4. **اليوم الخامس:** دراسة [Domain 3 — الجزء الثاني (Databases & Networking)](./03_Domain_3_Part2_Databases_and_Networking.md) لفهم الفروق بين قواعد البيانات العلائقية وغير العلائقية وبنية `Amazon VPC`.
5. **اليوم السادس:** دراسة [Domain 3 — الجزء الثالث (Integration, Monitoring, Migration & AI/ML)](./03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md).
6. **اليوم السابع:** دراسة [Domain 4 (الفوترة والدعم الفني)](./04_Domain_4_Billing_Pricing_and_Support.md) ومراجعة [دليل المقارنات المعمارية](./05_Exam_Tricks_and_Comparison_CheatSheet.md).
7. **الأيام الثامن إلى العاشر:** التطبيق العملي وحل الأسئلة التدريبية في مجلد [11_Practice_Exams](../11_Practice_Exams/) لتقييم الجاهزية قبل دخول الاختبار الرسمي.

---

**ابدأ القراءة من هنا:** [00_Prerequisites_Asasiyat_ElCloud.md](./00_Prerequisites_Asasiyat_ElCloud.md)

</div>
