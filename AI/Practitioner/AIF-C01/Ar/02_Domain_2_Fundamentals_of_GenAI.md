<div dir="rtl">

# 02 — المجال الثاني: أساسيات الذكاء الاصطناعي التوليدي (`Domain 2 — 24%`)

> **الوزن النسبي في الاختبار:** `24%` (ثاني أعلى مجال في الاختبار)  
> **المهام الرسمية:** `Task 2.1` (المفاهيم الأساسية و `Context Engineering` و `Agentic AI / MCP`) • `Task 2.2` (القدرات والقيود) • `Task 2.3` (البنية التحتية وخدمات `AWS GenAI`)

---

## 1. اللبنات الأساسية للذكاء الاصطناعي التوليدي
- **Tokens (الرموز):** وحدات نصية فرعية (الرمز الواحد ≈ ¾ كلمة إنجليزية). يُقاس بها **حجم نافذة السياق (`Context Window`)** وتكلفة الاستخدام (`Token-based pricing`).
- **Chunking (التقطيع):** تقسيم المستندات الكبيرة إلى فقرات متداخلة مناسبة للفهرسة والاسترجاع في `RAG`.
- **Embeddings & Vectors (التضمينات والمتجهات):** تحويل النصوص أو الصور إلى متجهات رقمية كثيفة تعبّر عن **المعنى الدلالي**، بحيث تقترب المفاهيم المتشابهة هندسياً في فضاء المتجهات.
- **Transformer Architecture & Self-Attention:** المعمارية التي أحدثت ثورة الـ `LLMs` بفضل آلية الانتباه الذاتي (`Self-Attention`) التي تفهم العلاقة بين جميع كلمات الجملة بالتوازي.
- **Diffusion Models:** نماذج توليد الصور والفيديو عبر إزالة الضوضاء تدريجياً من ضوضاء عشوائية (مثل `Amazon Nova Canvas`).

---

## 2. هندسة السياق (`Context Engineering`) والوكلاء الأذكياء (`Agentic AI & MCP`) — تحديث `v1.2`
- **Context Engineering:** لا تقتصر على كتابة نص السؤال (`Prompt`)، بل تشمل **التصميم والإدارة الديناميكية لكل ما يدخل في نافذة سياق النموذج**: تعليمات النظام + نتائج استرجاع `RAG` + الذاكرة قصيرة وطويلة المدى + تعريفات ومخرجات الأدوات ضمن ميزانية الرموز.
- **Model Context Protocol (`MCP`):** بروتوكول قياسي مفتوح يربط الوكلاء الذكيين (`AI Agents`) والنماذج التأسيسية بالأدوات الخارجية وقواعد البيانات وواجهات `APIs` بشكل موحد دون كتابة تكامل مخصص لكل أداة.
- **أنماط الوكلاء المتعددين (`Multi-Agent Patterns`):** تنسيق وكلاء متخصصين عبر مشرف (`Supervisor`)، تسليم متسلسل (`Handoffs`)، إدارة الذاكرة (`Memory Management`)، وتنفيذ مهام متعددة الخطوات.

---

## 3. المزايا والقيود ومقاييس القيمة التجارية
- **المزايا:** مرونة عالية عبر المهام، التفاعل الحواري الطبيعي، سرعة توليد المحتوى والكود والملخصات.
- **القيود والتحديات:**
  - **Hallucinations (الهلوسة):** توليد معلومات خاطئة بصياغة واثقة جداً.
  - **Nondeterminism (عدم الحتمية):** إعطاء إجابات مختلفة قليلاً لنفس السؤال.
  - **Interpretability (ضعف القابلية للتفسير):** طبيعة «الصندوق الأسود» للنماذج العميقة.
- **مقاييس القيمة التجارية:** `ROI`، كفاءة العمليات، معدل التحويل (`Conversion Rate`)، متوسط العائد لكل مستخدم (`ARPU`)، وقيمة العميل الدائمة (`CLV`).

---

## 4. منظومة AWS لبناء تطبيقات الذكاء الاصطناعي التوليدي (`v1.2`)

| الخدمة / الأداة | الدور الأساسي في `AWS` |
| :--- | :--- |
| [`Amazon Bedrock`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock) | خدمة Serverless موحدة للوصول عبر API إلى النماذج التأسيسية (`Nova`, `Claude`, `Llama`, `Mistral`) دون إدارة خوادم |
| [`Amazon Nova`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-nova) | عائلة نماذج AWS التأسيسية: `Nova Micro` (نص فائق السرعة)، `Nova Lite/Pro` (متعدد الوسائط)، `Nova Canvas` (صور)، `Nova Reel` (فيديو) |
| [`Amazon Bedrock AgentCore`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-bedrock-agentcore) | منصة Serverless متكاملة لتشغيل وتأمين ومراقبة الوكلاء في الإنتاج (`Runtime`, `Memory`, `Gateway/MCP`, `Identity`, `Policy`) |
| [`Strands Agents`](../AWS_AI_SERVICES_GLOSSARY.md#strands-agents) | مكتبة `Python SDK` مفتوحة المصدر من AWS لبناء وكلاء ذكيين بقيادة النموذج ودعم أصيل لـ `MCP` |
| [`Kiro`](../AWS_AI_SERVICES_GLOSSARY.md#kiro) | بيئة تطوير وكيلة (`Agentic AI IDE`) من AWS تعتمد على **التطوير الموجه بالمواصفات (`Spec-Driven Development`)** |
| [`Amazon Quick`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-quick) | مساحة عمل موحدة للذكاء التجاري (`BI`) والتحليل باللغة الطبيعية وأتمتة سير العمل المؤسسي |
| [`AWS Transform`](../AWS_AI_SERVICES_GLOSSARY.md#aws-transform) | خدمة ذكاء اصطناعي وكيلة لأتمتة تحديث وترحيل الأنظمة القديمة (`.NET`, `Java`, `VMware`, `Mainframe`) |
| [`Amazon SageMaker JumpStart`](../AWS_AI_SERVICES_GLOSSARY.md#amazon-sagemaker-jumpstart) | نشر وضبط النماذج مفتوحة المصدر على بنية `SageMaker` مخصصة عند الحاجة للتحكم الكامل بالخوادم |

### نماذج تسعير `Amazon Bedrock`
- **On-Demand:** الدفع لكل 1,000 رمز مدخل/مخرج — الأنسب للأحمال غير المتوقعة أو التجريبية.
- **Batch Inference:** خصم كبير لمعالجة ملفات ضخمة بشكل غير متزامن (`Offline`).
- **Provisioned Throughput:** حجز سعة ثابتة (`Model Units`) بالساعة — **إلزامي للنماذج المضبوطة خصيصاً (`Custom Fine-Tuned Models`)** وللأحمال الإنتاجية عالية الكثافة.

**الخطوة التالية:** [03_Domain_3_Applications_of_Foundation_Models.md](./03_Domain_3_Applications_of_Foundation_Models.md)

</div>
