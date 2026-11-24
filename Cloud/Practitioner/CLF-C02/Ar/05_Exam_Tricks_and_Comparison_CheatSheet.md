<div dir="rtl">

# 🔥 الزتونة النهائية: مقارنات X vs Y وخدع الامتحان (ليلة الامتحان)

الملف ده هو **ورقة الإنقاذ** بتاعتك قبل الامتحان بساعات! جمعنالك فيه كل الخدمات اللي شكلها شبه بعض وبتوقع الناس في الفخاخ، ومعاها استراتيجية حل أسئلة الـ **MCQ** في الامتحان الحقيقي عشان تضمن النجاح بسكور عالي بإذن الله!

---

## ⚔️ 1. جدول المقارنات الذهبية (X vs Y) بالعامية المصرية

### 🛡️ مقارنات الأمان والمراقبة (Security & Monitoring)

| المقارنة | الخدمة الأولى | الخدمة التانية / التالتة |
| :--- | :--- | :--- |
| **`Security Groups` vs `NACLs`** | **`Security Groups`:** على مستوى الـ **EC2 Instance**، فيها **`Allow` فقط**، و **`Stateful`**. | **`NACLs`:** على مستوى الـ **Subnet**، فيها **`Allow` و `Deny`** (لو عايز تعمل Block لـ IP)، و **`Stateless`**. |
| **`AWS Shield` vs `AWS WAF`** | **`AWS Shield`:** حماية ضد هجمات حجب الخدمة (**DDoS** — Layer 3/4). | **`AWS WAF`:** حماية تطبيقات الويب (Layer 7 HTTP) ضد **`SQL Injection`** و **`XSS`**. |
| **`GuardDuty` vs `Inspector` vs `Macie`** | **`GuardDuty`:** كشف تهديدات وسلوك مريب بالـ AI (زي تعدين Crypto أو دخول هاكر). | **`Inspector`:** فحص ثغرات البرامج (**Software Vulnerabilities**) على EC2/Containers.<br>**`Macie`:** اكتشاف بيانات شخصية (**PII**) متسابة جوه **`Amazon S3`**. |
| **`CloudWatch` vs `CloudTrail` vs `Config`** | **`CloudWatch`:** **الأداء (`Metrics & Logs`)** — الـ CPU سخن؟ ابعت Alarm! | **`CloudTrail`:** **مين عمل إيه؟ (`API Auditing`)** — مين مسح السيرفر؟<br>**`AWS Config`:** **تاريخ الإعدادات (`Configuration History & Compliance`)** — إعدادات الـ Bucket اتغيرت امتى؟ |
| **`Secrets Manager` vs `Parameter Store`** | **`Secrets Manager`:** لبسوردات الداتابيز وفيه **`Automatic Rotation`** (تغيير باسورد أوتوماتيك) — مدفوع. | **`Parameter Store`:** لإعدادات التطبيقات البسيطة ومجاني (النسخة Standard) بس مفيهوش Rotation جاهز. |
| **`AWS KMS` vs `AWS CloudHSM`** | **`AWS KMS`:** مفاتيح تشفير مدارة من AWS على هاردوير مشترك (**Multi-tenant**). | **`AWS CloudHSM`:** جهاز هاردوير تشفير مخصص ليك لوحدك (**Single-tenant / Dedicated**) للبنوك. |
| **`AWS Trusted Advisor` vs `AWS Inspector`** | **`Trusted Advisor`:** مستشار **للحساب كله** (تكلفة، أمان، أداء، حدود الخدمات). | **`Inspector`:** فاحص **ثغرات برمجية (`CVEs`)** جوه سيرفرات الـ EC2 و Lambda و Containers. |

---

### 🖥️ مقارنات السيرفرات والتخزين (Compute & Storage)

| المقارنة | الخدمة الأولى | الخدمة التانية / التالتة |
| :--- | :--- | :--- |
| **`Amazon EC2` vs `AWS Lambda`** | **`Amazon EC2`:** سيرفرات كاملة بتديرها إنت (IaaS) — شغالة طول الوقت. | **`AWS Lambda`:** **Serverless** — ارفع الكود بس، بيشتغل عند حدوث Event وبتدفع بالملي ثانية (أقصى وقت 15 دقيقة). |
| **`Amazon S3` vs `Amazon EBS` vs `Amazon EFS`** | **`Amazon S3`:** **Object Storage** — ملفات وصور وفيديوهات و Backups بمساحة لا نهائية (ما ينفعش تنزل عليه OS). | **`Amazon EBS`:** **Block Storage** — هارد لسيرفر EC2 واحد في AZ واحدة.<br>**`Amazon EFS`:** **File Storage** — فولدر مشترك لعدة سيرفرات Linux عبر أكتر من AZ. |
| **`EBS` vs `EC2 Instance Store`** | **`EBS`:** تخزين **دائم (`Persistent`)** — البيانات مش بتتمسح لو طفيت السيرفر. | **`Instance Store`:** تخزين **مؤقت (`Ephemeral`)** — سريع جداً بس البيانات **بتتمسح** لو طفيت السيرفر! |
| **`Savings Plans` vs `Reserved Instances`** | **`Savings Plans`:** التزام بمبلغ بالساعة (مرن جداً — بيغطي EC2 + Fargate + Lambda). | **`Reserved Instances (RI)`:** التزام بنوع سيرفر معين في Region معينة (أقل مرونة). |
| **`ECS / EKS` vs `AWS Fargate`** | **`ECS` / `EKS`:** أدوات إدارة الـ Containers (على سيرفرات EC2 إنت بتديرها أو على Fargate). | **`AWS Fargate`:** محرك **Serverless** بيشغل الـ Containers من غير ما تدير ولا سيرفر EC2! |

---

### 🗄️🌐 مقارنات الداتابيز والشبكات والرسائل (DB, Networking & Messaging)

| المقارنة | الخدمة الأولى | الخدمة التانية |
| :--- | :--- | :--- |
| **`RDS Multi-AZ` vs `RDS Read Replicas`** | **`Multi-AZ`:** للـ **High Availability / Failover** (نسخة طوارئ مش بنقرأ منها). | **`Read Replicas`:** للـ **Performance / Read Scaling** (تخفيف ضغط القراءة). |
| **`Amazon RDS` vs `Amazon DynamoDB` vs `Redshift`** | **`RDS`:** داتابيز **SQL** للتطبيقات اليومية (OLTP). | **`DynamoDB`:** داتابيز **NoSQL Serverless** فائقة السرعة.<br>**`Redshift`:** **Data Warehouse** للتحليلات والتقارير (OLAP). |
| **`CloudFront` vs `Global Accelerator`** | **`CloudFront`:** **CDN Caching** للصور والفيديوهات والمواقع (HTTP/HTTPS). | **`Global Accelerator`:** تسريع شبكة **TCP/UDP** بـ **Static IPs** للألعاب والـ VoIP. |
| **`Site-to-Site VPN` vs `Direct Connect`** | **`VPN`:** مشفر على **الإنترنت العام** (سريع التركيب ورخيص). | **`Direct Connect`:** كابل ألياف ضوئية **خاص ومباشر** مبيمرش على الإنترنت العام (سرعة ثابتة وتكلفة أعلى). |
| **`Amazon SQS` vs `Amazon SNS`** | **`SQS`:** **Queue (طابور)** — فصل الخدمات (**Decoupling**)، المستلم بيسحب (**Pull**) الرسالة. | **`SNS`:** **Pub/Sub (إذاعة)** — إرسال إشعارات (**Push**) لآلاف المشتركين (SMS, Email) في نفس اللحظة. |
| **`AWS Budgets` vs `AWS Cost Explorer`** | **`AWS Budgets`:** **إنذارات (`Alerts`)** لما الصرف يعدي حد معين. | **`AWS Cost Explorer`:** **رسوم بيانية وتحليل (`Charts & Forecast`)** للصرف القديم والمستقبلي. |

---

## 🧠 2. استراتيجية حل أسئلة الـ MCQ في الامتحان الحقيقي (4 خطوات مضمونة)

لما يظهرلك سؤال طويل في امتحان **CLF-C02**، ما تتخضش! امشي على الـ 4 خطوات دول:

1. **اقرأ آخر سطر في السؤال الأول!**
   * غالباً القصة اللي فوق كلها ديكور، والسؤال الحقيقي في آخر جملة: *"Which AWS service meets these requirements **with the LEAST operational overhead**?"* أو *"MOST cost-effectively?"*.
2. **اصطاد الكلمات المفتاحية (`Keywords`):**
   * شفت كلمة **`Least operational overhead`** أو **`No server management`**؟ $\leftarrow$ استبعد فوراً أي إجابة فيها `EC2` واختار خدمة **Serverless** (`Lambda`, `Fargate`, `DynamoDB`, `S3`, `Athena`)!
   * شفت كلمة **`Lowest cost`** أو **`Most cost-effective`**؟ $\leftarrow$ فكر في `Spot Instances`, `Savings Plans`, `S3 Glacier Deep Archive`, `S3 Intelligent-Tiering`.
   * شفت كلمة **`Global / Low latency / Static content`**؟ $\leftarrow$ فوراً **`Amazon CloudFront`**!
   * شفت كلمة **`Audit / Who did what`**؟ $\leftarrow$ فوراً **`AWS CloudTrail`**!
3. **استبعد الإجابات الغلط الأول (`Elimination`):**
   * في كل سؤال من 4 اختيارات، هتلاقي اختيارين ملهمش علاقة بالموضوع أصلاً (مثلاً سؤال عن الأمان وحاططلك `Amazon Polly` بتاعة الصوت!). شطب عليهم فوراً وهيفضلك اختيارين بس تقارن بينهم بهدوء.
4. **احذر فخ "الاختيار الصعب زيادة عن اللزوم":**
   * في امتحان **Cloud Practitioner**، AWS دايماً بتفضل **الخدمة الجاهزة المدارة (`Managed Service`)** عن إنك تبني حاجة بنفسك على `EC2`!

---

> 🏆 **عاش يا بطل! إنت دلوقتي خلصت شرح الكورس كله بالعامية المصرية!**
>
> **الخطوة الأخيرة عشان تقفّل الامتحان:** ادخل دلوقتي حل أسئلة تدريبية من مجلد [11_Practice_Exams](../11_Practice_Exams/) أو شغّل محاكي الامتحان على جهازك:
>
> <div dir="ltr">
>
> ```bash
> python3 scripts/aws_revision_runner.py --cert CLF --mode practice -n 20 --tricks
> ```
>
> </div>
>
> **بالتوفيق في الامتحان وإن شاء الله ترجع مبسوط بشهادة `AWS Certified Cloud Practitioner`! 🎓🚀**
>
> ⬅️ [الرجوع للفهرس الرئيسي للدليل المصري](./README.md)

</div>
