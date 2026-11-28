<div dir="rtl">

# الدليل العربي الشامل لشهادة AWS Certified AI Practitioner (AIF-C01)

مرحباً بك في الدليل التعليمي العربي الشامل والمفصّل لمسار شهادة **AWS Certified AI Practitioner (`AIF-C01`)** وفق أحدث دليل رسمي للاختبار (**Exam Guide v1.2 — October 29, 2026**). تم إعداد هذا الدليل بلغة عربية واضحة ومهنية لتبسيط مفاهيم الذكاء الاصطناعي (**AI**) وتعلم الآلة (**ML**) والذكاء الاصطناعي التوليدي (**Generative AI**) والوكلاء الذكيين (**Agentic AI**)، مع الإبقاء على جميع أسماء خدمات **AWS** والمصطلحات التقنية باللغة الإنجليزية كما ترد في الاختبار الدولي.

> [!NOTE]
> **منهجية هذا الدليل:**
> * **الوضوح والعمق:** شرح منهجي لكل مفهوم وخدمة يشمل آلية العمل، حالات الاستخدام العملية، والفروق الدقيقة بين الخدمات المتشابهة (`X vs Y`).
> * **الدقة المصطلحية:** الإبقاء على أسماء الخدمات والمصطلحات الإنجليزية (مثل [`Amazon Bedrock`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock)، `RAG`، `Prompt Caching`، `AgentCore`، `MCP`، `Guardrails`) لربط الفهم النظري بصياغة أسئلة الاختبار الحقيقية.
> * **التوافق الكامل مع تحديث 2026 (`v1.2`):** يغطي أحدث الإضافات الرسمية مثل `Amazon Bedrock AgentCore`، `Strands Agents`، `Kiro`، `Amazon Quick`، `AWS Transform`، `Model Distillation`، و `Context Engineering`.

---

## بطاقة تعريفية باختبار AWS AIF-C01 (`v1.2`)

| العنصر | التفاصيل الرسمية |
| :--- | :--- |
| **رمز الاختبار** | `AIF-C01` (AWS Certified AI Practitioner) |
| **المستوى** | تأسيسي (`Foundational`) |
| **عدد الأسئلة** | 65 سؤالاً (50 سؤالاً مُقيّماً بالدرجات + 15 سؤالاً تجريبياً غير محسوب) |
| **المدة الزمنية** | 90 دقيقة (+30 دقيقة مجانية لغير الناطقين بالإنجليزية عبر `ESL +30` قبل الحجز) |
| **درجة النجاح** | 700 من أصل 1000 درجة (`Scaled Scoring`) |
| **أنماط الأسئلة (4 أنماط)** | `Multiple Choice` • `Multiple Response` • **`Ordering` (3–5 خطوات)** • **`Matching` (3–7 أزواج)** |

---

## هيكل الدليل وتوزيع مجالات الاختبار (Exam Domains)

| القسم | المجال والموضوع | الوزن النسبي | الرابط |
| :---: | :--- | :---: | :--- |
| **التمهيد** | **الأساسيات التقنية للذكاء الاصطناعي وتعلم الآلة (`Prerequisites`)** | تأسيس تقني | [00_Prerequisites_Asasiyat_AlAI_walML.md](./00_Prerequisites_Asasiyat_AlAI_walML.md) |
| **Domain 1** | **Fundamentals of AI and ML** (أساسيات الذكاء الاصطناعي وتعلم الآلة) | **20%** | [01_Domain_1_Fundamentals_of_AI_and_ML.md](./01_Domain_1_Fundamentals_of_AI_and_ML.md) |
| **Domain 2** | **Fundamentals of GenAI** (أساسيات الذكاء الاصطناعي التوليدي والوكلاء) | **24%** | [02_Domain_2_Fundamentals_of_GenAI.md](./02_Domain_2_Fundamentals_of_GenAI.md) |
| **Domain 3** | **Applications of Foundation Models** (تطبيقات النماذج التأسيسية و `RAG`) | **28%** | [03_Domain_3_Applications_of_Foundation_Models.md](./03_Domain_3_Applications_of_Foundation_Models.md) |
| **Domain 4** | **Guidelines for Responsible AI** (إرشادات الذكاء الاصطناعي المسؤول) | **14%** | [04_Domain_4_Responsible_AI.md](./04_Domain_4_Responsible_AI.md) |
| **Domain 5** | **Security, Compliance, and Governance** (الأمن والامتثال والحوكمة) | **14%** | [05_Domain_5_Security_Compliance_and_Governance.md](./05_Domain_5_Security_Compliance_and_Governance.md) |
| **المراجعة** | **دليل المقارنات الذهبية وحيل الاختبار (`X vs Y`)** | مراجعة شاملة | [06_Exam_Tricks_and_Comparison_CheatSheet.md](./06_Exam_Tricks_and_Comparison_CheatSheet.md) |

---

## خطة الدراسة الموصى بها (10 أيام)

1. **اليوم 1–2:** دراسة [التمهيد](./00_Prerequisites_Asasiyat_AlAI_walML.md) ثم [Domain 1](./01_Domain_1_Fundamentals_of_AI_and_ML.md) + حل أسئلة المجال الأول.
2. **اليوم 3–4:** التعمق في [Domain 2](./02_Domain_2_Fundamentals_of_GenAI.md) وفهم `Transformers`، `Tokens`، `MCP`، وخدمات `Bedrock` و `AgentCore`.
3. **اليوم 5–6:** التركيز المكثف على [Domain 3](./03_Domain_3_Applications_of_Foundation_Models.md) (أعلى وزن في الاختبار `28%`): `RAG`، `Prompt Engineering`، `Fine-Tuning`، `Distillation`، و `Evaluation Metrics`.
4. **اليوم 7:** دراسة [Domain 4 (Responsible AI)](./04_Domain_4_Responsible_AI.md) والتمييز الدقيق بين `Bedrock Guardrails` و `SageMaker Clarify` و `Model Cards`.
5. **اليوم 8:** دراسة [Domain 5 (Security & Governance)](./05_Domain_5_Security_Compliance_and_Governance.md) ومصفوفة `Generative AI Security Scoping Matrix`.
6. **اليوم 9–10:** مراجعة [دليل المقارنات](./06_Exam_Tricks_and_Comparison_CheatSheet.md) وحل تدريبات [`Ordering & Matching`](../11_Practice_Exams/AIF_C01_Ordering_and_Matching_Drills.md) و[`Top 300`](../11_Practice_Exams/AIF_C01_Top_300_Most_Frequent_Exam_Questions.md) والاختبار التجريبي الكامل [`Mock Exam #2`](../11_Practice_Exams/AIF_C01_Full_Length_Mock_Exam_2_v1.2.md).

**ابدأ القراءة من هنا:** [00_Prerequisites_Asasiyat_AlAI_walML.md](./00_Prerequisites_Asasiyat_AlAI_walML.md)

</div>
