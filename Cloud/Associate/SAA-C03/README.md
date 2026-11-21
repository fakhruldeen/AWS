# AWS Certified Solutions Architect - Associate (SAA-C03) Training Suite

> **Exam Code:** `SAA-C03`  
> **Level:** Associate (Cloud Architecture)  
> **Passing Score:** `720 / 1000` (Scaled scoring)  
> **Questions:** 65 scenario-based questions, 130 minutes.

---

## 📂 Pedagogical Phase Architecture (12 Steps)

```
Cloud/Associate/SAA-C03/
├── phase0_step01_syllabus/             # Official blueprint, domain weighting, study schedules
├── phase0_step02_prerequisites/          # Core networking, compute, storage, security foundations
├── phase1_step03_lectures/               # Instructor delivery lesson plans and classroom talking points
├── phase1_step04_slides/                 # Marp slide decks for classroom delivery
├── phase1_step05_diagrams/               # Standalone production Mermaid architecture blueprints
├── phase1_step06_explanations/           # In-depth architectural mechanics & trade-off breakdowns
├── phase2_step07_labs/                   # Guided architectural hands-on labs with CLI runbooks
├── phase2_step08_tutorials/              # Production multi-service architectural build tutorials
├── phase3_step09_notes/                  # High-yield architectural trade-off cheat sheets
├── phase4_step10_knowledge_checks/       # Rapid diagnostic retention quizzes per domain
├── phase4_step11_revision_questions/     # Curated scenario questions + 1,019Q Community Practice Pool
└── phase5_step12_sources/                # Academic references, whitepapers, documentation indexes
```

---

## 🎯 Exam Domains & Weightings

```mermaid
pie title SAA-C03 Domain Weighting
    "Domain 1: Design Secure Architectures" : 30
    "Domain 2: Design Resilient Architectures" : 26
    "Domain 3: Design High-Performing Architectures" : 24
    "Domain 4: Design Cost-Optimized Architectures" : 20
```

1. **[Domain 1: Design Secure Architectures (30%)](phase0_step01_syllabus/SAA-C03_Official_Blueprint.md#domain-1-design-secure-architectures-30):** Secure access to AWS resources, secure workload/applications, data security (KMS, Secrets Manager).
2. **[Domain 2: Design Resilient Architectures (26%)](phase0_step01_syllabus/SAA-C03_Official_Blueprint.md#domain-2-design-resilient-architectures-26):** Scalable, loosely coupled architectures (SQS, EventBridge), high-availability / fault-tolerant multi-AZ architectures (ALB, Auto Scaling, Aurora).
3. **[Domain 3: Design High-Performing Architectures (24%)](phase0_step01_syllabus/SAA-C03_Official_Blueprint.md#domain-3-design-high-performing-architectures-24):** High-performing compute, storage (EFS, FSx, EBS io2), databases (DynamoDB DAX, ElastiCache), and networks (CloudFront, Global Accelerator).
4. **[Domain 4: Design Cost-Optimized Architectures (20%)](phase0_step01_syllabus/SAA-C03_Official_Blueprint.md#domain-4-design-cost-optimized-architectures-20):** Cost-effective storage (S3 tiers), compute (Savings Plans, Spot, Serverless), and database licensing.

---

## 🛠️ Interactive Tools

- **CLI Revision Engine:** Run interactive drills, practice pools, and simulated exams:
  ```bash
  # Practice by domain
  python3 scripts/aws_revision_runner.py --cert SAA --mode practice --domain 1

  # Practice authentic Community Practice Pool (1,019 questions)
  python3 scripts/aws_revision_runner.py --cert SAA --community --mode practice -n 20 --tricks

  # Timed 65-question mock exam
  python3 scripts/aws_revision_runner.py --cert SAA --mode mock
  ```
- **Integrity Validation:** Run test suite across repositories:
  ```bash
  python3 tests/verify_ecosystem_integrity.py
  ```
