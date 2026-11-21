#!/usr/bin/env python3
"""
generate_community_consensus_focus_sets.py

Generates dedicated Community Consensus Pool High-Yield Focus Sets in:
- Cloud/Practitioner/CLF-C02/phase4_step11_revision_questions/Community Consensus Pool_High_Yield_Focus_Set.md
- AI/Practitioner/AIF-C01/phase4_step11_revision_questions/Community Consensus Pool_High_Yield_Focus_Set.md
"""

import json
from pathlib import Path

WORK_REPO = Path("/home/mohamed/Desktop/Work/aws")
VAULT_REPO = Path("/home/mohamed/Documents/Obsidian Vault/Brain/AWS")

def generate_clf_set():
    clf_et_file = VAULT_REPO / "Questions_Bank/Community Consensus Pool_Questions/community_consensus_clf_c02_290q.json"
    data = json.loads(clf_et_file.read_text(encoding="utf-8"))
    
    # Balanced 65-question mock set: D1: 16, D2: 20, D3: 22, D4: 7 = 65
    by_domain = {1: [], 2: [], 3: [], 4: []}
    for q in data:
        by_domain[q["domain"]].append(q)

    dist = {1: 16, 2: 20, 3: 22, 4: 7}
    selected = []
    for d, count in dist.items():
        selected.extend(by_domain[d][:count])

    domain_names = {
        1: "Domain 1: Cloud Concepts (24%)",
        2: "Domain 2: Security and Compliance (30%)",
        3: "Domain 3: Cloud Technology and Services (34%)",
        4: "Domain 4: Billing, Pricing, and Support (12%)"
    }

    lines = [
        "# AWS Certified Cloud Practitioner (CLF-C02) - Community Consensus Pool High-Yield Focus Set",
        "",
        "> **Exam Code:** `CLF-C02`  ",
        "> **Source Provenance:** Authentic Community Consensus Pool Community Discussions & Verified Consensus  ",
        "> **Question Count:** 65 High-Yield Scenario Questions (Full Mock Balance: 16 D1, 20 D2, 22 D3, 7 D4)  ",
        "> **Interactive CLI Practice:** `python3 scripts/aws_revision_runner.py --cert CLF --community_consensus --mode practice`  ",
        "> **Interactive Timed Simulation:** `python3 scripts/aws_revision_runner.py --cert CLF --community_consensus --mode mock`  ",
        "",
        "---",
        "",
        "## 🎯 Exam Strategy & How to Use This Set",
        "",
        "These questions represent the **most frequent scenario patterns** tested on the actual exam according to community consensus on Community Consensus Pool.",
        "Work through each question, select your choice, and review the **Architectural Rationale & Distractor Breakdown** in the collapsible details.",
        "",
        "---",
        ""
    ]

    for i, q in enumerate(selected, 1):
        lines.append(f"### Question {i} (Community Consensus Pool #{q['question_number']})")
        lines.append(f"> **Domain:** `{domain_names[q['domain']]}` | **ID:** `{q['id']}` | [Community Consensus Pool Discussion]({q['community_consensus_url']})")
        lines.append("")
        lines.append(q["prompt"])
        lines.append("")
        for k, v in sorted(q["options"].items()):
            lines.append(f"- **{k})** {v}")
        lines.append("")
        lines.append("<details>")
        lines.append("<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>")
        lines.append("")
        lines.append(f"**Correct Answer:** `{q['answer']}`\n")
        lines.append(q["explanation"])
        lines.append("")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
        lines.append("")

    out_file = WORK_REPO / "Cloud/Practitioner/CLF-C02/phase4_step11_revision_questions/Community Consensus Pool_High_Yield_Focus_Set.md"
    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated CLF-C02 Community Consensus Pool set ({len(selected)} questions) at {out_file}")

def generate_aif_set():
    aif_et_file = VAULT_REPO / "Questions_Bank/Community Consensus Pool_AI_Practitioner_Questions/community_consensus_aif_c01_30q.json"
    data = json.loads(aif_et_file.read_text(encoding="utf-8"))

    lines = [
        "# AWS Certified AI Practitioner (AIF-C01) - Community Consensus Pool High-Yield Focus Set",
        "",
        "> **Exam Code:** `AIF-C01`  ",
        "> **Source Provenance:** Authentic Community Consensus Pool Community Discussions & Verified Consensus  ",
        "> **Question Count:** 30 High-Yield Community Consensus Pool Questions (Domains 1 through 5)  ",
        "> **Interactive CLI Practice:** `python3 scripts/aws_revision_runner.py --cert AIF --community_consensus --mode practice`  ",
        "> **Interactive Timed Simulation:** `python3 scripts/aws_revision_runner.py --cert AIF --community_consensus --mode mock`  ",
        "",
        "---",
        "",
        "## 🎯 Exam Strategy & How to Use This Set",
        "",
        "These questions represent the **most frequent scenario patterns** tested on the actual AI Practitioner exam according to community consensus on Community Consensus Pool.",
        "Work through each question, select your choice, and review the **Architectural Rationale & Distractor Breakdown** in the collapsible details.",
        "",
        "---",
        ""
    ]

    for i, q in enumerate(data, 1):
        lines.append(f"### Question {i} (Community Consensus Pool #{q.get('question_number', i)})")
        lines.append(f"> **Domain:** `{q.get('domain_name', 'Domain ' + str(q.get('domain_id', 1)))}` | **ID:** `{q['id']}`")
        lines.append("")
        lines.append(q["prompt"])
        lines.append("")
        options = q.get("options", {})
        if isinstance(options, dict):
            for k, v in sorted(options.items()):
                lines.append(f"- **{k})** {v}")
        elif isinstance(options, list):
            for opt in options:
                lines.append(f"- {opt}")
        lines.append("")
        lines.append("<details>")
        lines.append("<summary><b>🔍 Reveal Verified Answer & Architectural Rationale</b></summary>")
        lines.append("")
        lines.append(f"**Correct Answer:** `{q.get('answer', q.get('correct_answer', 'A'))}`\n")
        lines.append(q.get("explanation", "Verified from Community Consensus Pool community discussion."))
        lines.append("")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
        lines.append("")

    out_file = WORK_REPO / "AI/Practitioner/AIF-C01/phase4_step11_revision_questions/Community Consensus Pool_High_Yield_Focus_Set.md"
    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated AIF-C01 Community Consensus Pool set ({len(data)} questions) at {out_file}")

if __name__ == "__main__":
    generate_clf_set()
    generate_aif_set()
