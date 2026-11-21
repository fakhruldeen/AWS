# 🎯 AWS Certified AI Practitioner (AIF-C01) Revision Questions & Mock Exam Suite

> **Module:** Domain-Mapped Revision Questions & Full-Length Practice Exams  
> **Course:** AWS Certified AI Practitioner (`AIF-C01`)  
> **Exam Version Alignment:** Official v1.2 (October 2026)  
> **Total Question Bank:** Curated practice sets + 154-question Community Practice Pool + Full 65-Question Timed Mock Exam.  
> **Master Knowledge Brain Link:** For the complete offline repository of **1,814 unique deduplicated practice questions** across all 5 domains (with redundancy eliminated from across industry practice pools), see the Knowledge Vault at `Brain/AWS/Questions_Bank/Unique_Revision_Banks/AI_Practitioner_AIF-C01/`.

---

## 🗺️ Master Revision Suite Index

| Component File | Domain Alignment | Question Count | Question Formats Included |
|:--- |:--- |:---:|:--- |
| **[AIF_C01_Community_Practice_Pool_154Q.md](./AIF_C01_Community_Practice_Pool_154Q.md)** | **🌐 Community Practice Pool** | **154** | **Authentic community practice suite with consensus discussions and answer rationales** |
| **[Community_High_Yield_Focus_Set.md](./Community_High_Yield_Focus_Set.md)** | **⭐ Community High Yield Focus** | **30** | **High-frequency community questions with verified discussion consensus** |
| **[Domain 1 Revision](./Domain_1_AI_ML_Fundamentals_Revision.md)** | **Domain 1:** Fundamentals of AI & ML | 15 | Multiple Choice, Multiple Response |
| **[Domain 2 Revision](./Domain_2_Generative_AI_Fundamentals_Revision.md)** | **Domain 2:** Fundamentals of Generative AI | 15 | Multiple Choice, Multiple Response |
| **[Domain 3 Revision](./Domain_3_Applications_of_Foundation_Models_Revision.md)** | **Domain 3:** Applications of Foundation Models | 15 | Multiple Choice, Multiple Response |
| **[Domain 4 Revision](./Domain_4_Responsible_AI_Guidelines_Revision.md)** | **Domain 4:** Guidelines for Responsible AI | 15 | Multiple Choice, Multiple Response |
| **[Domain 5 Revision](./Domain_5_Security_Compliance_Governance_Revision.md)** | **Domain 5:** Security, Compliance & Governance | 15 | Multiple Choice, Multiple Response |
| **[AIF-C01 Full Mock Exam](./AIF_C01_Full_Length_Mock_Exam.md)** | **Full Exam Blueprint (Domains 1 to 5)** | **65** | **Multiple Choice, Multiple Response, Ordering, Matching** |

---

## 💻 Interactive Terminal Revision Engine

Run the interactive CLI revision runner with the `--community` flag to drill specifically on authentic community questions:

```bash
# 1. Practice 10 Community Practice Pool AI Practitioner questions with trick decryption
python3 scripts/aws_revision_runner.py --cert AIF --community --mode practice -n 10 --tricks

# 2. Drill by specific domain (e.g., Domain 3: Applications of FMs / RAG)
python3 scripts/aws_revision_runner.py --cert AIF --community --domain 3

# 3. Take a timed mock exam using the community pool
python3 scripts/aws_revision_runner.py --cert AIF --community --mode mock
```

---

## 🏆 Full-Length Mock Exam Simulation Parameters
* **Time Limit:** 90 Minutes.
* **Scored vs Unscored:** 50 Scored Questions + 15 Unscored Experimental Questions = 65 Total.
* **Passing Score:** 700 / 1000 Scaled Score (Target $\ge 46/65$ correct answers).
* **Question Formats Included:**
  1. Multiple Choice (1 correct out of 4)
  2. Multiple Response (2 correct out of 5)
  3. **Ordering** (rearranging 3-5 procedural steps in chronological order)
  4. **Matching** (pairing 3-7 concepts and services)
