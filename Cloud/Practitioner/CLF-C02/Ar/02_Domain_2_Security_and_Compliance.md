<div dir="rtl">

# 🔒 Domain 2: Security and Compliance (30% من الامتحان)

الـ Domain ده عليه **30%** من درجات الامتحان — يعني تلت الامتحان تقريباً! بس الجميل فيه إنه واضح جداً، وكل خدمة في الأمان ليها وظيفة محددة ومعروفة، ولو فهمت التشبيه بتاعها هتضمن درجاته 100%.

---

## 1️⃣ نموذج المسؤولية المشتركة (AWS Shared Responsibility Model)

ده **أهم مفهوم في الامتحان كله**! تخيل إنك مأجّر شقة في كومباوند فخم جداً:
* **صاحب الكومباوند (`AWS`) مسؤول عن أمان الكومباوند نفسه — Security OF the Cloud:**
  * مباني الـ **Data Centers**، الأمن والحراسة والكاميرات، الكهرباء، الهاردوير، السيرفرات الحقيقية، شبكات الـ **Regions** و الـ **AZs**، والـ **Hypervisor**.
* **إنت كساكن (`Customer`) مسؤول عن أمان شقتك وحاجتك جواها — Security IN the Cloud:**
  * بياناتك (**Customer Data**) وتشفيرها.
  * تقفل باب شقتك وتدي المفاتيح لمين (**IAM Users, Roles, MFA**).
  * تحديثات الويندوز واللينكس جوه سيرفر الـ **`Amazon EC2`** بتاعك (**Guest OS Patching**).
  * قواعد الفايروول بتاعتك (**Security Groups & NACLs**).

> [!IMPORTANT]
> **فرق مهم جداً في الامتحان:**
> * لو بتستخدم **`Amazon EC2`** (خدمة **IaaS**): إنت المسؤول عن تحديث الـ **Operating System (OS Patching)** جوه السيرفر.
> * لو بتستخدم **`Amazon RDS`** أو **`AWS Lambda`** أو **`Amazon S3`** (خدمات **Managed / Serverless**): **AWS** هي اللي بتعمل الـ **OS Patching** وإنت مسؤول بس عن بياناتك وصلاحيات الوصول ليها!
> * **حاجات مشتركة (`Shared Controls`):** زي **Patch Management** (AWS تحدث الهاردوير وإنت تحدث الـ Guest OS)، و **Awareness & Training** (AWS تدرب موظفيها وإنت تدرب موظفينك).

---

## 2️⃣ إدارة الهوية والصلاحيات (`AWS IAM`)

الـ **IAM (Identity and Access Management)** هو **خدمة عالمية (`Global Service`) ومجانية** بتتحكم في: مين يدخل حساب AWS بتاعك ويعمل إيه؟

### مكونات الـ IAM:
1. **Root User (المالك الأصلي للحساب):**
   * أول إيميل وباسورد عملت بيهم الحساب. ليه صلاحيات مطلقة ومحدش يقدر يوقفه.
   * **القاعدة الذهبية في الامتحان:** **أوعى تستخدم الـ Root User في شغلك اليومي!** فعّل عليه **MFA** فوراً، ما تعملش ليه **Access Keys**، واقفل عليه في الدرج! استخدمه بس في حاجات نادرة زي قفل الحساب أو تغيير الـ Support Plan.
2. **IAM User:** حساب لشخص أو تطبيق (ليه Username/Password للـ Console أو Access Keys للـ CLI).
3. **IAM Group:** جروب بتحط فيه مجموعة **IAM Users** (مثلاً جروب `Developers` أو `Admins`) وتديهم صلاحية مرة واحدة بدل ما تدي لكل واحد لوحده. *(ملحوظة: الجروب بياخد Users بس، ما ينفعش تحط Group جوه Group).*
4. **IAM Policy:** ورقة مكتوبة بصيغة **JSON** بتحدد الصلاحيات (مثلاً: مسموحلك تقرأ من `Amazon S3` بس، وممنوع تمسح).
   * دايماً نطبق مبدأ **Principle of Least Privilege:** ادي كل واحد **أقل صلاحية ممكنة** تكفي شغله وبس!
5. **IAM Role (بطاقة الزائر / تصريح مؤقت):**
   * مش لشخص معين، دي صلاحية **مؤقتة** بنلبسها لخدمة AWS عشان تكلم خدمة تانية (مثلاً: نلبس **IAM Role** لسيرفر **`Amazon EC2`** عشان يقدر يقرأ ملفات من **`Amazon S3`** من غير ما نحط باسورد أو **Access Keys** جوه الكود!).
6. **MFA (Multi-Factor Authentication):** طبقة حماية إضافية (كود من تطبيق على موبايلك زي Google Authenticator أو جهاز هاردوير) غير الباسورد.
7. **`AWS IAM Identity Center` (زمان كان اسمه AWS SSO):** بيخلي موظفين الشركة يدخلوا على **كل حسابات AWS** وتطبيقات الشركة بـ **تسجيل دخول واحد بس (`Single Sign-On`)**.

---

## 3️⃣ إدارة الحسابات المتعددة (`AWS Organizations`)

لو عندك شركة كبيرة وعندك حساب AWS للتطوير (`Dev`) وحساب للتجربة (`Test`) وحساب للعملاء (`Prod`):
* **`AWS Organizations`:** خدمة مجانية بتجمعلك كل حساباتك تحت شجرة واحدة (مقسمة لمجموعات اسمها **Organizational Units — OUs**).
* **أهم ميزتين فيها:**
  1. **Consolidated Billing (الفاتورة المجمعة):** فاتورة واحدة لكل الحسابات، وبتاخد خصم حجم استهلاك أكبر (**Volume Discounts**) وتشارك الـ **Reserved Instances / Savings Plans** بين الحسابات.
  2. **Service Control Policies (`SCPs`):** "السقف الأعلى للصلاحيات" — قواعد بتحطها الإدارة العليا تمنع حسابات معينة تعمل حاجات معينة (مثلاً: ممنوع أي حد في حساب الـ `Dev` يفتح سيرفرات برة أوروبا، حتى لو كان Admin!).

---

## 4️⃣ التشفير وإدارة الأسرار (Encryption & Secrets)

| الخدمة | وظيفتها بالبلدي والمصري |
| :--- | :--- |
| **`AWS KMS` (Key Management Service)** | **خزنة مفاتيح التشفير المدارة من AWS:** بتعمل وتدير مفاتيح التشفير لبياناتك في S3 و EBS و RDS بضغطة زرار (مشتركة على هاردوير AWS — **Multi-tenant**). |
| **`AWS CloudHSM`** | زي KMS بس **جهاز هاردوير مخصص ليك لوحدك (`Single-tenant / Dedicated Hardware`)** عشان قوانين البنوك الصارمة (**FIPS 140-2 Level 3**). |
| **`AWS Certificate Manager (ACM)`** | بيطلعلك ويجددلك شهادات الـ **SSL/TLS Certificates** بتاعة الـ **HTTPS** لموقعك أوتوماتيك ومجاناً! |
| **`AWS Secrets Manager`** | خزنة للباسوردات بتاعة الداتابيز (**Database Credentials**) و الـ API Keys. **الميزة القاتلة في الامتحان:** بتغير الباسورد **أوتوماتيك كل فترة (`Automatic Secret Rotation`)**! |
| **`AWS Systems Manager Parameter Store`** | مخزن لإعدادات التطبيق (**Configuration Data**) والباسوردات البسيطة ومجاني للـ Standard، لكن مفيهوش **Automatic Rotation** جاهز زي Secrets Manager. |

---

## 5️⃣ حماية الشبكة والمواقع (Network & Edge Security)

### 🧱 Security Groups vs. Network ACLs (NACLs) — سؤال أكيد في الامتحان!

| المقارنة | `Security Groups` | `Network ACLs (NACLs)` |
| :--- | :--- | :--- |
| **مكانه فين؟** | على باب **السيرفر نفسه (`EC2 Instance Level`)** — زي قفل شقتك | على باب **الشارع كله (`Subnet Level`)** — زي بوابة الكومباوند |
| **نوع القواعد** | **`Allow` rules ONLY** (بتقول مين يدخل بس، والباقي ممنوع تلقائي) | **`Allow` AND `Deny` rules** (تقدر تعمل Block صريح لـ IP معين!) |
| **الحالة (`State`)** | **`Stateful`** (لو سمحت لحد يدخل، مسموحله يخرج تاني أوتوماتيك) | **`Stateless`** (لازم تكتب قاعدة للدخول `Inbound` وقاعدة للخروج `Outbound`) |

### 🛡️ حماية ضد الهجمات على الإنترنت:
* **`AWS Shield`:** الحماية ضد هجمات حجب الخدمة (**DDoS Attacks** — لما هاكر يبعتلك ملايين الطلبات الوهمية عشان يوقع موقعك):
  * **`Shield Standard`:** مجاني وشغال أوتوماتيك لكل عملاء AWS!
  * **`Shield Advanced`:** مدفوع (3000 دولار شهرياً)، بيديك حماية متقدمة، وفريق طوارئ 24/7 اسمه **SRT (Shield Response Team)**، و**تعويض مالي (`Cost Protection`)** لو الهجمة خلت فاتورة AWS تزيد!
* **`AWS WAF` (Web Application Firewall):** بيحمي موقعك (Layer 7 HTTP/HTTPS) من هجمات الويب المشهورة زي **`SQL Injection`** و **`Cross-Site Scripting (XSS)`** وتقدر تحطه على `CloudFront` أو `ALB` أو `API Gateway`.
* **`AWS Firewall Manager`:** لو عندك عشرات الحسابات في `AWS Organizations` وعايز تتحكم في قواعد الـ `WAF` و `Shield` و `Security Groups` من مكان واحد مركزي.

---

## 6️⃣ كشف التهديدات والمراجعة والامتثال (Threat Detection & Compliance)

الـ 5 خدمات دول بيتلخبط فيهم ناس كتير، بس بالمثال المصري ده مش هتنساهم أبداً:

| الخدمة | التشبيه المصري | الكلمة المفتاحية في الامتحان |
| :--- | :--- | :--- |
| **`Amazon GuardDuty`** | **ضابط المخابرات الذكي:** بيراقب Logs حسابك بالذكاء الاصطناعي ويلقط أي سلوك مريب (هاكر بيعدّن Bitcoin على سيرفرك أو دخول من دولة غريبة). | **Intelligent Threat Detection** (ML/AI) |
| **`Amazon Inspector`** | **مفتش الصحة والسلامة:** بيفحص سيرفرات الـ `EC2` و الـ `Lambda` و الـ `ECR Containers` عشان يلاقي **ثغرات أمنية في البرامج (`Software Vulnerabilities / CVEs`)** أو بورتات مفتوحة بالغلط. | **Automated Vulnerability Assessment / Scanning** |
| **`Amazon Macie`** | **كلب البوليس اللي بيشم البيانات السرية:** بيدوّر جوه ملفات **`Amazon S3`** عشان يكتشف أي بيانات شخصية حساسة (**PII** — أرقام بطاقات، كروت ائتمان) متسابة مكشوفة! | **Discover & Protect Sensitive Data (`PII`) in `S3`** |
| **`AWS Security Hub`** | **غرفة العمليات المركزية:** بتجمعلك كل التنبيهات من GuardDuty و Inspector و Macie في شاشة واحدة (**Single Pane of Glass**). | **Centralized Security Dashboard / Aggregator** |
| **`Amazon Detective`** | **المحقق كونان:** بعد ما يحصل اختراق، بتستخدمه عشان تحقق وتعرف السبب الجذري (**Root Cause Analysis**). | **Root Cause Investigation** |
| **`AWS Artifact`** | **مكتبة الشهادات الرسمية:** بوابة مجانية بتنزل منها شهادات الامتثال بتاعة AWS (زي **ISO 27001, SOC 2, PCI-DSS**) والـ **BAA** عشان توريها للمراجعين القانونيين. | **Download Compliance Reports & Agreements** |
| **`AWS Audit Manager`** | بيساعدك تجمع الأدلة أوتوماتيك من حسابك عشان تجهز نفسك للمراجعة (**Audit Preparation**). | **Continuous Auditing & Evidence Collection** |
| **`AWS CloudTrail`** | **كاميرا المراقبة (مين عمل إيه وامتى؟):** بتسجل كل حركة أو API Call بتحصل في حساب AWS بتاعك! | **Audit API Activity / Governance / Who did what?** |

---

## 🎯 زتونة الامتحان لـ Domain 2 (كلمة بكلمة!)

| لو شفت في السؤال... | الإجابة الصح 100% |
| :--- | :--- |
| **Who is responsible for patching the Guest OS on EC2?** | **The Customer (العميل)** |
| **Who is responsible for physical security of Data Centers?** | **AWS** |
| **Grant EC2 instance access to S3 without hardcoded credentials?** | **Attach an `IAM Role` to the EC2 instance** |
| **Block a specific malicious IP address at the Subnet level?** | **`Network ACL (NACL)`** (لأن الـ Security Group مفيهاش Deny!) |
| **Protect against SQL Injection or XSS?** | **`AWS WAF`** |
| **Protect against DDoS attacks?** | **`AWS Shield`** |
| **Detect PII (credit cards, SSN) in Amazon S3 buckets?** | **`Amazon Macie`** |
| **Scan EC2 instances or containers for software vulnerabilities?** | **`Amazon Inspector`** |
| **Detect unusual / malicious API activity or crypto mining?** | **`Amazon GuardDuty`** |
| **Download AWS SOC 2 or ISO compliance reports?** | **`AWS Artifact`** |
| **Automatically rotate database passwords?** | **`AWS Secrets Manager`** |
| **Restrict maximum permissions across multiple AWS accounts?** | **`AWS Organizations` with `SCPs`** |

---

> ⬅️ **الدرس السابق:** [Domain 1: Cloud Concepts](./01_Domain_1_Cloud_Concepts.md) | **الدرس التالي:** 👉 **[03_Domain_3_Part1_Compute_and_Storage.md](./03_Domain_3_Part1_Compute_and_Storage.md)** | [الفهرس](./README.md)

</div>
