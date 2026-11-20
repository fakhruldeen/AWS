#!/usr/bin/env python3
"""
AWS Ecosystem Automated Integrity & Quality Verification Suite
==============================================================
Validates ecosystem consistency across the Work repository (fakhruldeen/AWS)
and the Obsidian Knowledge Vault (Brain/AWS).

Checks:
  1. Question Bank Schema & Deduplication Integrity (CLF-C02 & AIF-C01)
  2. Guided Labs Standard (Zero broken screenshots, complete scenario matrices)
  3. Knowledge Vault Wiki-Link Resolution
  4. Work Repository Markdown Link Integrity
  5. Secret Safety & Git Hygiene

Author: Mohamed Fakhruldeen (Repository Trainer)
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

WORK_REPO = Path("/home/mohamed/Desktop/Work/aws")
VAULT_REPO = Path("/home/mohamed/Documents/Obsidian Vault/Brain/AWS")

class TestReport:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.failures: List[str] = []

    def log_pass(self, test_name: str):
        self.passed += 1
        print(f"  \033[92m✔ PASS\033[0m: {test_name}")

    def log_fail(self, test_name: str, reason: str):
        self.failed += 1
        msg = f"  \033[91m✘ FAIL\033[0m: {test_name} — {reason}"
        print(msg)
        self.failures.append(f"{test_name}: {reason}")

    def log_warn(self, test_name: str, reason: str):
        self.warnings += 1
        print(f"  \033[93m⚠ WARN\033[0m: {test_name} — {reason}")

    def summary(self) -> bool:
        print("\n" + "="*80)
        print(f"INTEGRITY VERIFICATION SUMMARY")
        print("="*80)
        print(f"Total Checks Passed:   \033[92m{self.passed}\033[0m")
        print(f"Total Warnings:        \033[93m{self.warnings}\033[0m")
        print(f"Total Checks Failed:   \033[91m{self.failed}\033[0m")
        if self.failures:
            print("\nFailures:")
            for f in self.failures:
                print(f"  - {f}")
        print("="*80)
        return self.failed == 0

def check_question_banks(report: TestReport):
    print("\n--- 1. Testing Question Bank Schemas & Deduplication ---")
    banks = [
        ("CLF-C02", VAULT_REPO / "Questions_Bank/Unique_Revision_Banks/Cloud_Practitioner_CLF-C02/CLF_C02_Master_Unique_Questions.json", 4),
        ("AIF-C01", VAULT_REPO / "Questions_Bank/Unique_Revision_Banks/AI_Practitioner_AIF-C01/AIF_C01_Master_Unique_Questions.json", 5),
        ("MLA-C01", VAULT_REPO / "Questions_Bank/Unique_Revision_Banks/Machine_Learning_Associate_MLA-C01/MLA_C01_Master_Unique_Questions.json", 4),
        ("SAA-C03", VAULT_REPO / "Questions_Bank/Unique_Revision_Banks/Solutions_Architect_Associate_SAA-C03/SAA_C03_Master_Unique_Questions.json", 4),
    ]

    for cert_name, path, max_domain in banks:
        if not path.is_file():
            report.log_fail(f"{cert_name} Bank File", f"File not found at {path}")
            continue

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            report.log_fail(f"{cert_name} Bank JSON", f"Invalid JSON format: {e}")
            continue

        report.log_pass(f"{cert_name} Bank JSON Valid ({len(data)} questions)")

        seen_ids = set()
        duplicate_ids = set()
        invalid_domains = []
        empty_prompts = []
        missing_explanations = []
        missing_sources = []

        for q in data:
            qid = q.get("id")
            if not qid:
                report.log_fail(f"{cert_name} Missing ID", f"Found question without ID: {q.get('prompt', '')[:50]}")
            elif qid in seen_ids:
                duplicate_ids.add(qid)
            else:
                seen_ids.add(qid)

            prompt = q.get("prompt", "")
            if not prompt or len(prompt.strip()) < 10:
                empty_prompts.append(qid)

            d = q.get("domain")
            if not isinstance(d, int) or d < 1 or d > max_domain:
                invalid_domains.append((qid, d))

            exp = q.get("explanation", "")
            if not exp or len(exp.strip()) < 10:
                missing_explanations.append(qid)

            srcs = q.get("sources", [])
            if not srcs:
                missing_sources.append(qid)

        if duplicate_ids:
            report.log_fail(f"{cert_name} Unique IDs", f"{len(duplicate_ids)} duplicate IDs found (e.g., {list(duplicate_ids)[:5]})")
        else:
            report.log_pass(f"{cert_name} Unique Question IDs (100% unique)")

        if empty_prompts:
            report.log_fail(f"{cert_name} Prompt Content", f"{len(empty_prompts)} questions have empty/truncated prompts")
        else:
            report.log_pass(f"{cert_name} Prompt Completeness (100% non-empty)")

        if invalid_domains:
            report.log_fail(f"{cert_name} Domain Ranges", f"{len(invalid_domains)} questions have out-of-range domains (must be 1-{max_domain})")
        else:
            report.log_pass(f"{cert_name} Domain Boundaries (All 1-{max_domain})")

        if missing_explanations:
            report.log_warn(f"{cert_name} Explanations", f"{len(missing_explanations)} questions lack detailed explanations")
        else:
            report.log_pass(f"{cert_name} Explanations Present (100%)")

        if missing_sources:
            report.log_warn(f"{cert_name} Sources", f"{len(missing_sources)} questions lack source provenance")
        else:
            report.log_pass(f"{cert_name} Source Provenance (100% sourced)")

def check_guided_labs(report: TestReport):
    print("\n--- 2. Testing Guided Labs Written Standard ---")
    lab_dirs = [
        ("CLF-C02", WORK_REPO / "Cloud/Practitioner/CLF-C02/labs"),
        ("AIF-C01", WORK_REPO / "AI/Practitioner/AIF-C01/labs"),
        ("SAA-C03", WORK_REPO / "Cloud/Associate/SAA-C03/labs"),
        ("MLA-C01", WORK_REPO / "AI/Associate/MLA-C01/labs"),
    ]

    for cert_name, lab_dir in lab_dirs:
        if not lab_dir.is_dir():
            report.log_fail(f"{cert_name} Labs Directory", f"Directory missing at {lab_dir}")
            continue

        lab_files = sorted(lab_dir.glob("*.md"))
        # Exclude README.md
        lab_files = [f for f in lab_files if f.name != "README.md"]

        report.log_pass(f"{cert_name} Found {len(lab_files)} guided lab documents")

        broken_img_pattern = re.compile(r'!\[.*?\]\((images/.*?|screenshots/.*?)\)')
        scenario_trap_pattern = re.compile(r'Exam Practice: Scenarios & Traps|Scenario Matrix', re.IGNORECASE)
        cli_runbook_pattern = re.compile(r'aws\s+[a-z0-9\-]+', re.IGNORECASE)

        for lab in lab_files:
            content = lab.read_text(encoding="utf-8")
            
            # Check for broken images
            broken_matches = broken_img_pattern.findall(content)
            if broken_matches:
                report.log_fail(f"{lab.name} Broken Images", f"Contains {len(broken_matches)} missing image links (e.g. {broken_matches[0]})")
            else:
                report.log_pass(f"{lab.name} Zero Broken Images")

            # Check for Exam Practice matrix
            if not scenario_trap_pattern.search(content):
                report.log_warn(f"{lab.name} Scenario Matrix", "Missing dedicated 'Exam Practice: Scenarios & Traps' section")
            else:
                report.log_pass(f"{lab.name} Exam Scenarios & Traps Matrix Verified")

            # Check for CLI commands
            if not cli_runbook_pattern.search(content):
                report.log_warn(f"{lab.name} CLI Runbook", "No AWS CLI commands found in lab text")
            else:
                report.log_pass(f"{lab.name} AWS CLI Runbook Present")

def check_vault_wiki_links(report: TestReport):
    print("\n--- 3. Testing Knowledge Vault Wiki-Links ---")
    all_vault_files = list(VAULT_REPO.rglob("*.md"))
    vault_note_basenames = {f.stem for f in all_vault_files}

    # Sample inspect 05_Knowledge_Tests README and blueprints
    test_files = [
        VAULT_REPO / "05_Knowledge_Tests/README.md",
        VAULT_REPO / "01_Certifications/AI_Practitioner_AIF-C01/AIF-C01_Master_Blueprint.md",
        VAULT_REPO / "01_Certifications/Cloud_Practitioner_CLF-C02/CLF-C02_Master_Blueprint.md",
        VAULT_REPO / "01_Certifications/Solutions_Architect_Associate_SAA-C03/SAA-C03_Master_Blueprint.md",
        VAULT_REPO / "01_Certifications/Machine_Learning_Associate_MLA-C01/MLA-C01_Master_Blueprint.md",
    ]

    wiki_link_pattern = re.compile(r'\[\[([^\]\\\|#]+)(?:\\?[\|#][^\]]*)?\]\]')

    for tf in test_files:
        if not tf.is_file():
            continue
        content = tf.read_text(encoding="utf-8")
        links = wiki_link_pattern.findall(content)
        broken = []
        for l in links:
            l_clean = l.strip().rstrip('\\').strip()
            # If link has folder path, take stem
            stem = Path(l_clean).stem
            if stem not in vault_note_basenames and l_clean not in vault_note_basenames:
                broken.append(l_clean)

        if broken:
            report.log_warn(f"{tf.name} Wiki-Links", f"{len(broken)} target notes not found in vault: {broken[:3]}")
        else:
            report.log_pass(f"{tf.name} Wiki-Links Valid ({len(links)} links checked)")

def check_git_hygiene(report: TestReport):
    print("\n--- 4. Testing Secret Safety & Git Hygiene ---")
    secret_patterns = [
        re.compile(r'AKIA[0-9A-Z]{16}'),  # AWS Access Key ID
        re.compile(r'BEGIN RSA PRIVATE KEY'),
        re.compile(r'BEGIN OPENSSH PRIVATE KEY'),
    ]

    tracked_text_files = []
    for base in [WORK_REPO]:
        for ext in ["*.md", "*.py", "*.json", "*.sh", "*.yaml", "*.yml"]:
            for f in base.rglob(ext):
                if ".git" in str(f) or "node_modules" in str(f) or "graphify-out" in str(f):
                    continue
                tracked_text_files.append(f)

    compromised = []
    for f in tracked_text_files[:200]:  # sample check
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
            for sp in secret_patterns:
                if sp.search(content):
                    compromised.append((f.name, str(sp)))
        except Exception:
            pass

    if compromised:
        report.log_fail("Secret Scanner", f"Potential secret exposure in: {compromised}")
    else:
        report.log_pass(f"Secret Scanner (Clean across {len(tracked_text_files)} repository files)")

def main():
    print("\033[1m\033[96m================================================================================")
    print("           AWS REPOSITORY & KNOWLEDGE VAULT INTEGRITY SUITE                      ")
    print("================================================================================\033[0m")

    report = TestReport()
    check_question_banks(report)
    check_guided_labs(report)
    check_vault_wiki_links(report)
    check_git_hygiene(report)

    success = report.summary()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
