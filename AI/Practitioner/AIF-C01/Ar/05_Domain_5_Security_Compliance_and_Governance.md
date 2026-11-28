<div dir="rtl">

# 05 — المجال الخامس: الأمن والامتثال والحوكمة لحلول الذكاء الاصطناعي (`Domain 5 — 14%`)

> **الوزن النسبي في الاختبار:** `14%`  
> **المهام الرسمية:** `Task 5.1` (تأمين أنظمة الذكاء الاصطناعي) • `Task 5.2` (الحوكمة واللوائح التنظيمية والامتثال)

---

## 1. نموذج المسؤولية المشتركة (`AWS Shared Responsibility Model`) للذكاء الاصطناعي
- **مسؤولية AWS (`Security OF the Cloud`):** أمن مراكز البيانات الفيزيائية، العتاد والـ `GPUs`، البنية التحتية لخدمة `Amazon Bedrock`، وعزل النماذج الأساسية — **قاعدة ذهبية: بياناتك وأوامرك (`Prompts & Completions`) في `Amazon Bedrock` لا تُستخدم أبداً لتدريب النماذج الأساسية ولا تُشارك مع مزودي النماذج**.
- **مسؤولية العميل (`Security IN the Cloud`):** سياسات [`AWS IAM`](../AWS_AI_SERVICES_GLOSSARY.md#aws-iam) بأقل صلاحية (`Least Privilege`)، التشفير عبر [`AWS KMS`](../AWS_AI_SERVICES_GLOSSARY.md#aws-kms)، العزل الشبكي عبر [`AWS PrivateLink`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-vpc)، إعداد `Bedrock Guardrails`، وتنظيف البيانات قبل التدريب أو `RAG`.

---

## 2. خدمات وميزات تأمين أنظمة الذكاء الاصطناعي والوكلاء (`v1.2`)
- **[`Amazon Bedrock AgentCore Identity`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock-agentcore):** إدارة هويات الوكلاء الذكيين وتفويض صلاحيات `OAuth/IAM` محدودة النطاق بالنيابة عن المستخدم.
- **`Policy in AgentCore`:** فرض سياسات حتمية (`Allow / Forbid`) تتحقق من صلاحية كل استدعاء لأداة (`Tool Invocation`) قبل تنفيذه فعلياً.
- **[`AWS PrivateLink`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-vpc):** ربط تطبيقات `VPC` بخدمتي `Bedrock` و `SageMaker` عبر `Interface VPC Endpoints` دون مرور البيانات عبر الإنترنت العام.
- **[`Amazon Macie`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-macie):** اكتشاف وتصنيف البيانات الحساسة (`PII`) في حاويات `Amazon S3` قبل إدخالها في خطوط التدريب أو `RAG`.
- **`Bedrock Model Invocation Logging`:** تسجيل جميع الأوامر والردود في `S3` أو `CloudWatch Logs` لأغراض التدقيق والمراقبة.
- **التأصيل وكشف الهلوسة (`Grounding & Hallucination Detection`):** الجمع بين `RAG Grounding` + فحص `Contextual Grounding` في `Guardrails` + التحقق من المخرجات (`Output Validation`) وتوثيق المصادر (`Source Citation` و `Data Lineage`).

---

## 3. مصفوفة نطاق أمن الذكاء الاصطناعي التوليدي (`Generative AI Security Scoping Matrix`)

| النطاق (`Scope`) | نوع الاستخدام | الضوابط الأمنية الرئيسية |
| :---: | :--- | :--- |
| **Scope 1** | تطبيقات المستهلكين العامة (مثل روبوتات الويب العامة) | سياسة الاستخدام المقبول (`Acceptable Use Policy`) والتوعية فقط |
| **Scope 2** | تطبيقات المؤسسات المُدارة (`Amazon Quick`, `Kiro`) | تسجيل الدخول الموحد (`SSO`)، صلاحيات `IAM`، وحوكمة الوصول للبيانات |
| **Scope 3** | بناء تطبيقات فوق نماذج جاهزة عبر API (`Amazon Bedrock` + `RAG`) | `Guardrails`، `PrivateLink`، `KMS`، `Invocation Logging`، وحماية `Prompt Injection` |
| **Scope 4** | ضبط النماذج (`Fine-Tuning` / `Continued Pre-Training`) ببيانات الشركة | فحص `Macie`، منع تسميم البيانات (`Data Poisoning`)، وتقييد الوصول للنموذج المخصص |
| **Scope 5** | تدريب نموذج تأسيسي من الصفر (`Pre-training from Scratch`) | أمن كامل للبنية التحتية، سلاسل التوريد، وعناقيد التدريب (`GPU/Trainium Clusters`) |

---

## 4. خدمات الحوكمة والامتثال التنظيمي في AWS (`Task 5.2`)
- **[`AWS Artifact`](../AWS_AI_SERVICES_GLOSSARY.md#aws-artifact):** تحميل تقارير الامتثال الرسمية (`SOC 2`, `ISO 27001`, `PCI DSS`) واتفاقيات `HIPAA BAA`.
- **[`AWS CloudTrail`](../AWS_AI_SERVICES_GLOSSARY.md#aws-cloudtrail):** سجل تدقيق كامل لجميع استدعاءات `API` الإدارية (من نفّذ ماذا ومتى).
- **[`AWS Config`](../AWS_AI_SERVICES_GLOSSARY.md#aws-config):** تتبع تاريخ إعدادات الموارد والتحقق المستمر من التزامها بقواعد الامتثال.
- **[`Amazon Inspector`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-inspector):** فحص آلي مستمر للثغرات الأمنية (`CVEs`) في `EC2` وحاويات `ECR` ودوال `Lambda`.
- **[`AWS Trusted Advisor`](../AWS_AI_SERVICES_GLOSSARY.md#aws-trusted-advisor):** فحوصات أفضل الممارسات للأمن، التكلفة، الأداء، وحدود الخدمة (`Service Quotas`).
- **إقامة البيانات (`Data Residency`):** اختيار `AWS Region` المناسبة يضمن بقاء بيانات التدريب والاستدلال داخل النطاق الجغرافي المطلوب قانونياً (مثل `GDPR`).

**الخطوة التالية:** [06_Exam_Tricks_and_Comparison_CheatSheet.md](./06_Exam_Tricks_and_Comparison_CheatSheet.md)

</div>
