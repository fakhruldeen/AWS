#!/usr/bin/env python3
"""
apply_practitioner_numbering.py

Renames the study folders inside Cloud/Practitioner/CLF-C02 and AI/Practitioner/AIF-C01
to follow the pedagogical chronological naming scheme:
  phase0_step01_syllabus
  phase0_step02_prerequisites
  phase1_step03_lectures
  phase1_step04_slides
  phase1_step05_diagrams
  phase1_step06_explanations
  phase2_step07_labs
  phase2_step08_tutorials
  phase3_step09_notes
  phase4_step10_knowledge_checks
  phase4_step11_revision_questions
  phase5_step12_sources

Also updates all relative links and text references across the repository and Obsidian vault.
"""

import os
import subprocess
from pathlib import Path

WORK_REPO = Path("/home/mohamed/Desktop/Work/aws")
VAULT_REPO = Path("/home/mohamed/Documents/Obsidian Vault/Brain/AWS")

FOLDER_MAPPING = [
    ("syllabus", "phase0_step01_syllabus"),
    ("prerequisites", "phase0_step02_prerequisites"),
    ("lectures", "phase1_step03_lectures"),
    ("slides", "phase1_step04_slides"),
    ("diagrams", "phase1_step05_diagrams"),
    ("explanations", "phase1_step06_explanations"),
    ("labs", "phase2_step07_labs"),
    ("tutorials", "phase2_step08_tutorials"),
    ("notes", "phase3_step09_notes"),
    ("knowledge_checks", "phase4_step10_knowledge_checks"),
    ("revision_questions", "phase4_step11_revision_questions"),
    ("sources", "phase5_step12_sources"),
]

PRACTITIONER_DIRS = [
    WORK_REPO / "Cloud/Practitioner/CLF-C02",
    WORK_REPO / "AI/Practitioner/AIF-C01",
]

def rename_directories():
    for pdir in PRACTITIONER_DIRS:
        print(f"\nProcessing directory: {pdir}")
        for old_name, new_name in FOLDER_MAPPING:
            src = pdir / old_name
            dst = pdir / new_name
            if not src.exists():
                print(f"  [SKIP] {old_name} does not exist in {pdir.name}")
                continue
            
            # Check if tracked by git
            tracked = subprocess.run(
                ["git", "ls-files", str(src)],
                cwd=WORK_REPO,
                capture_output=True,
                text=True
            ).stdout.strip()
            
            if tracked:
                print(f"  [GIT MV] {old_name} -> {new_name}")
                subprocess.run(["git", "mv", str(src), str(dst)], cwd=WORK_REPO, check=True)
            else:
                print(f"  [MV (untracked)] {old_name} -> {new_name}")
                subprocess.run(["mv", str(src), str(dst)], check=True)

def update_references():
    print("\nUpdating references across Work Repo and Obsidian Vault...")
    
    # Replacement pairs for exact paths
    replacements = []
    for cert in ["CLF-C02", "AIF-C01"]:
        for old_name, new_name in FOLDER_MAPPING:
            replacements.append((f"{cert}/{old_name}/", f"{cert}/{new_name}/"))
            replacements.append((f"{cert}/{old_name})", f"{cert}/{new_name})"))
            replacements.append((f"{cert}/{old_name}`", f"{cert}/{new_name}`"))
            replacements.append((f"../{old_name}/", f"../{new_name}/"))
            replacements.append((f"./{old_name}/", f"./{new_name}/"))
            replacements.append((f"({old_name}/", f"({new_name}/"))

    # Also update relative links within practitioner directories
    # e.g. (../phase2_step07_labs/ -> (../phase2_step07_labs/

    # Scan work repo files
    files_to_update = []
    for p in WORK_REPO.rglob("*"):
        if p.is_file() and not any(x in str(p) for x in [".git", "node_modules", "graphify-out", ".epub", ".pdf"]):
            files_to_update.append(p)
            
    for p in VAULT_REPO.rglob("*"):
        if p.is_file() and not any(x in str(p) for x in [".git", "node_modules", "graphify-out", ".epub", ".pdf"]):
            files_to_update.append(p)

    updated_count = 0
    for f in files_to_update:
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
            new_content = content
            
            # Context-specific replacements if file is inside a practitioner folder
            is_practitioner_file = False
            for pdir in PRACTITIONER_DIRS:
                if str(pdir) in str(f):
                    is_practitioner_file = True
                    break
                    
            if is_practitioner_file:
                for old_name, new_name in FOLDER_MAPPING:
                    # Replace (../old_name/ or (old_name/ or [old_name/
                    new_content = new_content.replace(f"(../{old_name}/", f"(../{new_name}/")
                    new_content = new_content.replace(f"({old_name}/", f"({new_name}/")
                    new_content = new_content.replace(f"`{old_name}/`", f"`{new_name}/`")
                    new_content = new_content.replace(f"/{old_name}/", f"/{new_name}/")
            
            # Universal replacements for explicit cert paths
            for old_pat, new_pat in replacements:
                new_content = new_content.replace(old_pat, new_pat)
                
            if new_content != content:
                f.write_text(new_content, encoding="utf-8")
                updated_count += 1
                print(f"  Updated: {f.name}")
        except Exception as e:
            print(f"  Error reading {f}: {e}")

    print(f"\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    rename_directories()
    update_references()
    print("\nDirectory numbering and reference updates completed successfully.")
