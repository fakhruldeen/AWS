<div dir="rtl">

# 06 — دليل المقارنات الذهبية وحيل الاختبار (`X vs Y` — `AIF-C01 v1.2`)

> **الهدف:** جدول مراجعة سريعة ليلة الاختبار لفك شفرة الكلمات المفتاحية (`Keywords`) في أسئلة `Multiple Choice` و `Ordering` و `Matching` خلال ثوانٍ.

---

## 1. جدول المقارنات الذهبية (`X vs Y`)

| المقارنة | الخيار الأول (`X`) | الخيار الثاني (`Y`) | الكلمة المفتاحية الفاصلة في السؤال |
| :--- | :--- | :--- | :--- |
| **`RAG` vs `Fine-Tuning`** | `RAG`: يضيف **حقائق مؤسسية متغيرة** مع توثيق المصادر دون إعادة تدريب | `Fine-Tuning`: يغيّر **الأسلوب والنبرة والتنسيق** عبر أمثلة مُصنّفة | "up-to-date docs + citations" ← **`RAG`** \| "specific tone/style" ← **`Fine-Tuning`** |
| **`Fine-Tuning` vs `Continued Pre-Training`** | `Instruction Fine-Tuning`: بيانات **مُصنّفة (`Labeled`)** | `Continued Pre-Training`: نصوص قطاعية **غير مُصنّفة (`Unlabeled`)** ضخمة | "labeled prompt-completion" ← **`Fine-Tuning`** \| "massive unlabeled domain corpus" ← **`Continued Pre-Training`** |
| **`Model Distillation` vs `Prompt Caching`** | `Distillation`: نموذج طالب صغير/سريع/رخيص يحاكي نموذجاً كبيراً | `Prompt Caching`: تخزين مؤقت لبادئة نصية ثابتة متكررة | "smaller faster cheaper student model" ← **`Distillation`** \| "repeated static prefix" ← **`Prompt Caching`** |
| **`Bedrock` vs `SageMaker JumpStart`** | `Bedrock`: Serverless API بدون إدارة خوادم | `JumpStart`: تحكم كامل بالبنية التحتية والـ `GPUs` للنماذج مفتوحة المصدر | "serverless / no infra" ← **`Bedrock`** \| "dedicated infra / full control" ← **`JumpStart`** |
| **`Bedrock Guardrails` vs `SageMaker Clarify`** | `Guardrails`: تصفية فورية **أثناء التشغيل** (`PII`, `Denied Topics`, `Grounding`) | `Clarify`: قياس **التحيز** (`Bias`) وتفسير **`SHAP`** للبيانات والنماذج | "block topics / redact PII at runtime" ← **`Guardrails`** \| "bias / disparate impact / SHAP" ← **`Clarify`** |
| **`ROUGE` vs `BLEU` vs `BERTScore` vs `LLM-as-a-Judge`** | `ROUGE` = **تلخيص** \| `BLEU` = **ترجمة** | `BERTScore` = **تشابه دلالي** \| `LLM-as-a-Judge` = **تقييم مفتوح واسع النطاق** | Summarization ← **`ROUGE`** \| Translation ← **`BLEU`** \| Paraphrase semantics ← **`BERTScore`** |
| **`Precision` vs `Recall` vs `F1`** | `Precision`: تقليل `False Positives` (بريد مزعج) | `Recall`: تقليل `False Negatives` (سرطان/احتيال) \| `F1`: بيانات غير متوازنة | "cannot miss positive cases" ← **`Recall`** \| "imbalanced classes" ← **`F1`** |
| **`Textract` vs `Rekognition` vs `Comprehend`** | `Textract`: جداول ونماذج `PDF` \| `Rekognition`: صور وفيديو | `Comprehend`: مشاعر وكيانات `NLP` من النص | "forms & tables" ← **`Textract`** \| "objects/faces" ← **`Rekognition`** \| "sentiment/entities" ← **`Comprehend`** |
| **`Strands Agents` vs `Bedrock AgentCore` vs `Kiro`** | `Strands`: SDK لبناء الوكلاء \| `AgentCore`: تشغيل وتأمين الوكلاء بالإنتاج | `Kiro`: بيئة تطوير وكيلة `IDE` موجهة بالمواصفات | "open-source SDK" ← **`Strands`** \| "Identity/Policy/Runtime" ← **`AgentCore`** \| "spec-driven IDE" ← **`Kiro`** |
| **`CloudTrail` vs `Config` vs `Artifact` vs `Macie`** | `CloudTrail`: سجل `API` \| `Config`: امتثال الإعدادات | `Artifact`: تقارير `SOC/ISO` \| `Macie`: كشف `PII` في `S3` | "who called API" ← **`CloudTrail`** \| "discover PII in S3" ← **`Macie`** \| "download SOC/HIPAA" ← **`Artifact`** |

---

## 2. نصائح ذهبية للتعامل مع أنماط الأسئلة الأربعة
1. **أسئلة `Multiple Response` (`Choose TWO`):** استبعد فوراً الخيارات الخارجة عن نطاق الخدمة أو المبالغ فيها، وتأكد أن الخيارين معاً يغطيان شقّي السؤال.
2. **أسئلة `Ordering` (الترتيب):** حدد دائماً **الخطوة الأولى** (تحديد المشكلة / جمع البيانات / تقطيع المستندات / فحص الإدخال) و**الخطوة الأخيرة** (النشر والمراقبة / التوثيق / تسليم الإجابة) — هذا يحسم الترتيب بدقة 100%.
3. **أسئلة `Matching` (المطابقة):** اربط الأزواج التي تعرفها بيقين كامل أولاً لتقليص الخيارات المتبقية.
4. **إدارة الوقت:** 90 دقيقة لـ 65 سؤالاً (~1.38 دقيقة لكل سؤال) — لا تتردد في طلب **`ESL +30`** قبل حجز الاختبار لتحصل على **120 دقيقة** كاملة!

**الخطوة التالية للتطبيق العملي:**
- تدريبات الترتيب والمطابقة: [`AIF_C01_Ordering_and_Matching_Drills.md`](../11_Practice_Exams/AIF_C01_Ordering_and_Matching_Drills.md)
- أهم 300 سؤال متكرر: [`AIF_C01_Top_300_Most_Frequent_Exam_Questions.md`](../11_Practice_Exams/AIF_C01_Top_300_Most_Frequent_Exam_Questions.md)
- الاختبار التجريبي الكامل (`v1.2`): [`AIF_C01_Full_Length_Mock_Exam_2_v1.2.md`](../11_Practice_Exams/AIF_C01_Full_Length_Mock_Exam_2_v1.2.md)

</div>
