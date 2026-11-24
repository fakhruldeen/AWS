#!/usr/bin/env python3
"""
AWS Certification Delivery Packaging & Build Engine
===================================================
Compiles and packages self-sufficient course materials across CLF-C02 and AIF-C01
into static, distribution-ready artifacts:
  - Printable Student Handbooks (PDF via Headless Chrome)
  - Mobile & E-Reader Editions (ePub via Calibre)
  - Marp Classroom Slide Presentations (Interactive HTML & PDF)

Author: Mohamed Fakhruldeen (Repository Trainer)
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Tuple

try:
    import markdown
except ImportError:
    print("Error: 'markdown' package is required. Install via pip or python virtual environment.")
    sys.exit(1)

WORK_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = WORK_DIR / "dist"

# Professional Book CSS Stylesheet for PDF & Print
HANDBOOK_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');

@page {
    size: A4;
    margin: 22mm 16mm 22mm 16mm;
    @bottom-right {
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
    @bottom-left {
        content: "AWS Certified Training • Mohamed Fakhruldeen";
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

.cover-page {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 40px 60px;
    box-sizing: border-box;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    page-break-after: always;
    break-after: page;
}

.cover-badge {
    display: inline-block;
    background: #ff9900;
    color: #0f172a;
    font-weight: 800;
    font-size: 11pt;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 6px 16px;
    border-radius: 4px;
    margin-bottom: 24px;
}

.cover-title {
    font-size: 32pt;
    font-weight: 800;
    line-height: 1.15;
    margin: 0 0 16px 0;
    color: #ffffff;
}

.cover-subtitle {
    font-size: 16pt;
    font-weight: 400;
    line-height: 1.4;
    color: #94a3b8;
    max-width: 600px;
    margin: 0 0 40px 0;
}

.cover-meta {
    margin-top: auto;
    border-top: 1px solid #334155;
    padding-top: 24px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    font-size: 10pt;
    color: #cbd5e1;
}

.cover-author {
    font-weight: 600;
    color: #f8fafc;
}

.page-break {
    page-break-before: always;
    break-before: page;
    margin-top: 30px;
}

h1 {
    font-size: 20pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-top: 36px;
    margin-bottom: 18px;
    page-break-after: avoid;
    break-after: avoid;
}

h2 {
    font-size: 15pt;
    font-weight: 700;
    color: #1e293b;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 6px;
    margin-top: 28px;
    margin-bottom: 14px;
    page-break-after: avoid;
    break-after: avoid;
}

h3 {
    font-size: 12pt;
    font-weight: 600;
    color: #334155;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
    break-after: avoid;
}

h4, h5, h6 {
    font-size: 10.5pt;
    font-weight: 600;
    color: #475569;
    margin-top: 16px;
    margin-bottom: 8px;
}

p, ul, ol {
    margin-top: 0;
    margin-bottom: 12px;
}

li {
    margin-bottom: 4px;
}

/* Callouts / Alerts */
.callout {
    padding: 12px 16px;
    margin: 16px 0;
    border-left: 4px solid #3b82f6;
    border-radius: 0 6px 6px 0;
    background-color: #f8fafc;
    page-break-inside: avoid;
    break-inside: avoid;
}

.callout-title {
    font-weight: 700;
    font-size: 9.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.callout-note { border-left-color: #0284c7; background-color: #f0f9ff; }
.callout-note .callout-title { color: #0369a1; }

.callout-tip { border-left-color: #10b981; background-color: #f0fdf4; }
.callout-tip .callout-title { color: #047857; }

.callout-important { border-left-color: #8b5cf6; background-color: #f5f3ff; }
.callout-important .callout-title { color: #6d28d9; }

.callout-warning { border-left-color: #f59e0b; background-color: #fffbeb; }
.callout-warning .callout-title { color: #b45309; }

.callout-caution { border-left-color: #ef4444; background-color: #fef2f2; }
.callout-caution .callout-title { color: #b91c1c; }

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
}

th {
    background-color: #1e293b;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 8px 10px;
    border: 1px solid #334155;
}

td {
    padding: 7px 10px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

/* Code Blocks */
pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 12px 14px;
    border-radius: 6px;
    overflow-x: auto;
    font-family: 'Fira Code', 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    margin: 14px 0;
    page-break-inside: avoid;
    break-inside: avoid;
}

code {
    font-family: 'Fira Code', 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 4px;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    border-radius: 0;
}

blockquote {
    border-left: 3px solid #cbd5e1;
    margin: 14px 0;
    padding-left: 14px;
    color: #475569;
    font-style: italic;
}

hr {
    border: 0;
    height: 1px;
    background: #e2e8f0;
    margin: 24px 0;
}
"""

CLF_MANIFEST = {
    "cert_code": "CLF-C02",
    "title": "AWS Certified Cloud Practitioner (CLF-C02)",
    "subtitle": "Complete Student Handbook & Master MCQ Decryption Playbook",
    "sources": [
        "Cloud/Practitioner/CLF-C02/00_START_HERE.md",
        # Prerequisites
        "Cloud/Practitioner/CLF-C02/02_Prerequisites/01_Operating_Systems_and_Virtualization.md",
        "Cloud/Practitioner/CLF-C02/02_Prerequisites/02_Networking_and_OSI_Model.md",
        "Cloud/Practitioner/CLF-C02/02_Prerequisites/03_Storage_Paradigms.md",
        "Cloud/Practitioner/CLF-C02/02_Prerequisites/04_Security_and_Cryptography.md",
        "Cloud/Practitioner/CLF-C02/02_Prerequisites/05_Cloud_Economics_and_FinOps.md",
        # Domain 1: Cloud Concepts
        "Cloud/Practitioner/CLF-C02/06_Explanations/01_Cloud_Concepts/Cloud_Adoption_Framework_CAF.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/01_Cloud_Concepts/Cloud_Economics_and_TCO.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/01_Cloud_Concepts/Disaster_Recovery_and_High_Availability.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/01_Cloud_Concepts/Global_Infrastructure.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/01_Cloud_Concepts/Shared_Responsibility_Model.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/01_Cloud_Concepts/Well_Architected_Framework.md",
        # Domain 2: Security & Compliance
        "Cloud/Practitioner/CLF-C02/06_Explanations/02_Security_and_Compliance/AWS_IAM_and_Identity.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/02_Security_and_Compliance/Encryption_and_Secrets_Management.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/02_Security_and_Compliance/Shield_and_WAF.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/02_Security_and_Compliance/Threat_Detection_and_Compliance.md",
        # Domain 3: Cloud Technology & Services
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Compute_Services.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Storage_Services.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Database_Services.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Networking_and_Content_Delivery.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Application_Integration_and_DevOps.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Management_and_Observability.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/03_Technology_and_Services/Analytics_AI_and_Migration.md",
        # Domain 4: Billing & Pricing
        "Cloud/Practitioner/CLF-C02/06_Explanations/04_Billing_and_Pricing/Pricing_Models_and_Billing_Tools.md",
        "Cloud/Practitioner/CLF-C02/06_Explanations/04_Billing_and_Pricing/Support_Plans_and_Marketplace.md",
        # Cheat Sheets & Distinctions
        "Cloud/Practitioner/CLF-C02/01_Syllabus/Exam_Distinction_CheatSheet.md",
        # Architecture Tutorials
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_00_AWS_Account_Creation_and_Security_Baseline.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_01_Multi_Tier_VPC_and_Bastion_Host.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_02_Highly_Available_AutoScaling_Web_Tier.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_03_Secure_Multi_AZ_RDS_with_Secrets_Manager.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_04_Serverless_Event_Driven_Pipeline.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_05_Automating_Infrastructure_with_CloudFormation.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_06_Enterprise_Governance_Organizations_and_SCPs.md",
        "Cloud/Practitioner/CLF-C02/08_Tutorials/Tutorial_07_Global_Content_Delivery_CloudFront_Route53_S3.md",
    ]
}

AIF_MANIFEST = {
    "cert_code": "AIF-C01",
    "title": "AWS Certified AI Practitioner (AIF-C01)",
    "subtitle": "Complete Student Handbook & Master MCQ Decryption Playbook",
    "sources": [
        "AI/Practitioner/AIF-C01/00_START_HERE.md",
        "AI/Practitioner/AIF-C01/02_Prerequisites/01_Machine_Learning_Fundamentals.md",
        "AI/Practitioner/AIF-C01/02_Prerequisites/02_Generative_AI_and_Transformers.md",
        "AI/Practitioner/AIF-C01/02_Prerequisites/03_Agentic_AI_Multi_Agent_Systems_and_Model_Context_Protocol_MCP.md",
        "AI/Practitioner/AIF-C01/06_Explanations/01_Domain_1_Fundamentals_of_AI_and_ML.md",
        "AI/Practitioner/AIF-C01/06_Explanations/02_Domain_2_Fundamentals_of_Generative_AI.md",
        "AI/Practitioner/AIF-C01/06_Explanations/03_Domain_3_Applications_of_Foundation_Models.md",
        "AI/Practitioner/AIF-C01/06_Explanations/04_Domain_4_Guidelines_for_Responsible_AI.md",
        "AI/Practitioner/AIF-C01/06_Explanations/05_Domain_5_Security_Compliance_and_Governance.md",
        "AI/Practitioner/AIF-C01/09_Notes_and_Cheatsheets/02_Prompt_Engineering_Guide.md",
        "AI/Practitioner/AIF-C01/09_Notes_and_Cheatsheets/03_Amazon_Bedrock_and_RAG.md",
        "AI/Practitioner/AIF-C01/09_Notes_and_Cheatsheets/06_AIF-C01_Exam_CheatSheet.md",
        "AI/Practitioner/AIF-C01/09_Notes_and_Cheatsheets/Exam_Decryption_Playbook_and_Mnemonics.md",
        "AI/Practitioner/AIF-C01/08_Tutorials/Tutorial_01_Enterprise_RAG_Knowledge_Base_Architecture.md",
        "AI/Practitioner/AIF-C01/08_Tutorials/Tutorial_02_Multi_Agent_Autonomous_System_with_Bedrock_AgentCore_and_MCP.md",
        "AI/Practitioner/AIF-C01/08_Tutorials/Tutorial_06_Serverless_Generative_AI_App_Bedrock_APIGateway_Lambda.md",
    ]
}

CLF_AR_MANIFEST = {
    "cert_code": "CLF-C02-Ar",
    "title": "AWS Certified Cloud Practitioner (CLF-C02) — Arabic Handbook",
    "cover_title": "الدليل العربي الشامل لشهادة AWS Certified Cloud Practitioner (CLF-C02)",
    "subtitle": "شرح تفصيلي ومنهجي لمفاهيم وخدمات الحوسبة السحابية مع الحفاظ على المصطلحات التقنية الإنجليزية",
    "rtl": True,
    "lang": "ar",
    "sources": [
        "Cloud/Practitioner/CLF-C02/Ar/README.md",
        "Cloud/Practitioner/CLF-C02/Ar/00_Prerequisites_Asasiyat_ElCloud.md",
        "Cloud/Practitioner/CLF-C02/Ar/01_Domain_1_Cloud_Concepts.md",
        "Cloud/Practitioner/CLF-C02/Ar/02_Domain_2_Security_and_Compliance.md",
        "Cloud/Practitioner/CLF-C02/Ar/03_Domain_3_Part1_Compute_and_Storage.md",
        "Cloud/Practitioner/CLF-C02/Ar/03_Domain_3_Part2_Databases_and_Networking.md",
        "Cloud/Practitioner/CLF-C02/Ar/03_Domain_3_Part3_Integration_Monitoring_Analytics_AI.md",
        "Cloud/Practitioner/CLF-C02/Ar/04_Domain_4_Billing_Pricing_and_Support.md",
        "Cloud/Practitioner/CLF-C02/Ar/05_Exam_Tricks_and_Comparison_CheatSheet.md",
    ]
}

RTL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
body {
    direction: rtl;
    text-align: right;
    font-family: 'Cairo', 'Noto Sans Arabic', 'DejaVu Sans', 'Segoe UI', Tahoma, sans-serif;
    line-height: 1.75;
}
.cover-page {
    align-items: flex-start;
    text-align: right;
}
th, td {
    text-align: right;
}
.callout {
    border-left: none;
    border-right: 4px solid #3b82f6;
    border-radius: 6px 0 0 6px;
}
.callout-note { border-right-color: #0284c7; }
.callout-tip { border-right-color: #10b981; }
.callout-important { border-right-color: #8b5cf6; }
.callout-warning { border-right-color: #f59e0b; }
.callout-caution { border-right-color: #ef4444; }
blockquote {
    border-left: none;
    border-right: 3px solid #cbd5e1;
    padding-left: 0;
    padding-right: 14px;
}
code {
    direction: ltr;
    unicode-bidi: isolate;
    display: inline-block;
}
pre {
    direction: ltr;
    text-align: left;
}
"""

VENDOR_DIR = WORK_DIR / "scripts/vendor"

def clean_markdown_for_compilation(text: str, strip_rtl_wrapper: bool = False) -> str:
    """Pre-processes markdown to handle alerts, math, and custom layout tags."""
    if strip_rtl_wrapper:
        # Remove outer <div dir="rtl"> / </div> and <div dir="ltr"> wrappers so Markdown parses cleanly
        text = re.sub(r'^\s*<div\s+dir="rtl">\s*', '', text)
        text = re.sub(r'\s*</div>\s*$', '', text)
        text = re.sub(r'<div\s+dir="ltr">\s*', '', text)
        text = re.sub(r'\s*</div>', '', text)

    # 1. Convert ```mermaid ... ``` to <pre class="mermaid">...</pre>
    mermaid_pattern = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)
    def repl_mermaid(m):
        diagram = m.group(1).strip()
        return f"\n\n<pre class=\"mermaid\">\n{diagram}\n</pre>\n\n"
    text = mermaid_pattern.sub(repl_mermaid, text)

    # 2. Convert GitHub Alerts: > [!NOTE] etc.
    alert_types = ["NOTE", "TIP", "IMPORTANT", "WARNING", "CAUTION"]
    for atype in alert_types:
        pattern = re.compile(rf'>\s*\[!{atype}\](.*?)(?=(\n\n|\Z))', re.DOTALL | re.IGNORECASE)
        def replace_alert(m):
            body = m.group(1).replace('\n> ', '\n').strip()
            return f'<div class="callout callout-{atype.lower()}" markdown="1"><div class="callout-title">{atype}</div>\n\n{body}\n\n</div>'
        text = pattern.sub(replace_alert, text)

    # 3. Clean Obsidian wiki-links: [[TargetNote|Display Text]] -> Display Text, [[TargetNote]] -> TargetNote
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'**\1**', text)

    return text

def build_cover_html(title: str, subtitle: str, cert_code: str) -> str:
    """Generates a stylish cover page."""
    return f"""
    <div class="cover-page">
        <div class="cover-badge">{cert_code} • OFFICIAL TRAINING</div>
        <div class="cover-title">{title}</div>
        <div class="cover-subtitle">{subtitle}</div>
        <div class="cover-meta">
            <div>
                <div><strong>Author & Trainer:</strong> Mohamed Fakhruldeen</div>
                <div><strong>Delivery Format:</strong> Master Student Handbook & Architecture Blueprint</div>
            </div>
            <div style="text-align: right;">
                <div><strong>Edition:</strong> 2026 Production Standard</div>
                <div><strong>Repository:</strong> fakhruldeen/AWS</div>
            </div>
        </div>
    </div>
    """

def compile_handbook(manifest: Dict, format_choice: str):
    """Compiles a student handbook into HTML, PDF, and ePub."""
    cert_code = manifest["cert_code"]
    title = manifest["title"]
    cover_title = manifest.get("cover_title", title)
    subtitle = manifest["subtitle"]
    is_rtl = manifest.get("rtl", False)
    lang = manifest.get("lang", "en")
    dir_attr = "rtl" if is_rtl else "ltr"
    out_dir = DIST_DIR / cert_code / "handbook"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n=======================================================")
    print(f"  Compiling Master Handbook: {cert_code} ({dir_attr.upper()})")
    print(f"=======================================================")

    combined_html_parts = []
    combined_html_parts.append(build_cover_html(cover_title, subtitle, cert_code))

    md_compiler = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'toc',
        'admonition',
        'attr_list',
        'def_list',
        'md_in_html'
    ])

    for rel_path in manifest["sources"]:
        src_file = WORK_DIR / rel_path
        if not src_file.exists():
            print(f"  [WARN] Source file missing: {rel_path}")
            continue

        print(f"  -> Processing: {src_file.name}")
        content = src_file.read_text(encoding="utf-8")
        cleaned_content = clean_markdown_for_compilation(content, strip_rtl_wrapper=is_rtl)
        rendered_html = md_compiler.convert(cleaned_content)
        md_compiler.reset()

        combined_html_parts.append(f'<div class="page-break"></div>\n{rendered_html}')

    # Read vendor libraries for inlined offline rendering
    katex_css = VENDOR_DIR.joinpath("katex.min.css").read_text(encoding="utf-8") if VENDOR_DIR.joinpath("katex.min.css").exists() else ""
    katex_js = VENDOR_DIR.joinpath("katex.min.js").read_text(encoding="utf-8") if VENDOR_DIR.joinpath("katex.min.js").exists() else ""
    auto_render_js = VENDOR_DIR.joinpath("auto-render.min.js").read_text(encoding="utf-8") if VENDOR_DIR.joinpath("auto-render.min.js").exists() else ""
    mermaid_js = VENDOR_DIR.joinpath("mermaid.min.js").read_text(encoding="utf-8") if VENDOR_DIR.joinpath("mermaid.min.js").exists() else ""
    extra_rtl_css = RTL_CSS if is_rtl else ""

    master_html = f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        {katex_css}
        {HANDBOOK_CSS}
        {extra_rtl_css}
        .mermaid {{ display: flex; justify-content: center; margin: 25px 0; background: #ffffff; page-break-inside: avoid; break-inside: avoid; }}
        .mermaid svg {{ max-width: 100%; height: auto; }}
        .katex-display {{ margin: 16px 0; overflow-x: auto; page-break-inside: avoid; break-inside: avoid; }}
        .katex {{ font-size: 1.05em; text-rendering: auto; }}
    </style>
    <script>
        {katex_js}
    </script>
    <script>
        {auto_render_js}
    </script>
    <script>
        {mermaid_js}
    </script>
</head>
<body>
    {''.join(combined_html_parts)}

    <script>
    document.addEventListener("DOMContentLoaded", function() {{
        if (typeof renderMathInElement === 'function') {{
            renderMathInElement(document.body, {{
                delimiters: [
                    {{left: "$$", right: "$$", display: true}},
                    {{left: "$", right: "$", display: false}},
                    {{left: "\\\\(", right: "\\\\)", display: false}},
                    {{left: "\\\\[", right: "\\\\]", display: true}}
                ],
                ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
                throwOnError: false
            }});
        }}
        if (typeof mermaid === 'object') {{
            mermaid.initialize({{
                startOnLoad: true,
                theme: "neutral",
                flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: "basis" }}
            }});
        }}
    }});
    </script>
</body>
</html>
"""

    safe_name = re.sub(r'[^A-Za-z0-9_\-]+', '_', title).strip('_')
    html_file = out_dir / f"{safe_name}.html"
    raw_html_file = out_dir / f"{safe_name}_raw.html"
    pdf_file = out_dir / f"{safe_name}.pdf"
    epub_file = out_dir / f"{safe_name}.epub"

    raw_html_file.write_text(master_html, encoding="utf-8")

    # Pass 1: Pre-render DOM with Headless Chrome (evaluates KaTeX and Mermaid to vector SVGs/HTML)
    print(f"  -> Pre-rendering Mermaid diagrams and KaTeX formulas via Headless Chrome...")
    dump_cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--virtual-time-budget=15000",
        "--run-all-compositor-stages-before-draw",
        "--dump-dom",
        f"file://{raw_html_file.resolve()}"
    ]
    res_dump = subprocess.run(dump_cmd, capture_output=True, text=True)
    if res_dump.returncode == 0 and len(res_dump.stdout) > 1000:
        html_file.write_text(res_dump.stdout, encoding="utf-8")
        print(f"  ✔ Fully Pre-Rendered DOM: {html_file.name} ({len(res_dump.stdout)//1024} KB)")
    else:
        print(f"  [WARN] DOM pre-rendering warning: {res_dump.stderr[:300]}, using raw HTML")
        html_file.write_text(master_html, encoding="utf-8")

    # 1. Compile PDF via Headless Chrome
    if format_choice in ["pdf", "all"]:
        print(f"  -> Rendering Print-Ready PDF via Headless Chrome...")
        chrome_cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={pdf_file}",
            "--print-to-pdf-no-header",
            f"file://{html_file.resolve()}"
        ]
        res = subprocess.run(chrome_cmd, capture_output=True, text=True)
        if res.returncode == 0 and pdf_file.exists():
            pdf_size_mb = pdf_file.stat().st_size / (1024 * 1024)
            print(f"  \033[92m✔ SUCCESS\033[0m: Generated PDF -> {pdf_file.name} ({pdf_size_mb:.2f} MB)")
        else:
            print(f"  \033[91m✘ FAIL\033[0m: PDF conversion failed: {res.stderr}")

    # 2. Compile ePub via Calibre
    if format_choice in ["epub", "all"]:
        print(f"  -> Compiling Reflowable ePub via Calibre...")
        epub_clean_html = out_dir / "epub_clean.html"
        clean_html_content = re.sub(r'<script.*?</script>', '', html_file.read_text(encoding="utf-8"), flags=re.DOTALL)
        epub_clean_html.write_text(clean_html_content, encoding="utf-8")
        epub_cmd = [
            "ebook-convert",
            str(epub_clean_html),
            str(epub_file),
            "--title", cover_title,
            "--authors", "Mohamed Fakhruldeen",
            "--language", lang,
            "--chapter", "h1",
            "--insert-metadata"
        ]
        res = subprocess.run(epub_cmd, capture_output=True, text=True)
        if epub_clean_html.exists():
            epub_clean_html.unlink()
        if res.returncode == 0 and epub_file.exists():
            epub_size_kb = epub_file.stat().st_size / 1024
            print(f"  \033[92m✔ SUCCESS\033[0m: Generated ePub -> {epub_file.name} ({epub_size_kb:.1f} KB)")
        else:
            print(f"  \033[91m✘ FAIL\033[0m: ePub conversion failed: {res.stderr[:500]}")


def compile_slides(cert_code: str, format_choice: str):
    """Compiles Marp presentation slides to standalone HTML and PDF."""
    slide_dir = WORK_DIR / ("Cloud/Practitioner/CLF-C02/04_Slides" if cert_code == "CLF-C02" else "AI/Practitioner/AIF-C01/04_Slides")
    out_dir = DIST_DIR / cert_code / "slides"
    out_dir.mkdir(parents=True, exist_ok=True)

    slide_files = sorted([f for f in slide_dir.glob("*.md") if f.name != "README.md"])

    print(f"\n=======================================================")
    print(f"  Compiling Marp Presentation Decks: {cert_code} ({len(slide_files)} modules)")
    print(f"=======================================================")

    for slide in slide_files:
        stem = slide.stem
        html_out = out_dir / f"{stem}.html"
        pdf_out = out_dir / f"{stem}.pdf"

        # 1. HTML Presentation
        if format_choice in ["html", "all"]:
            cmd_html = [
                "npx", "--yes", "@marp-team/marp-cli",
                str(slide),
                "--html",
                "-o", str(html_out)
            ]
            res = subprocess.run(cmd_html, capture_output=True, text=True)
            if res.returncode == 0 and html_out.exists():
                print(f"  ✔ Slide HTML: {html_out.name}")
            else:
                print(f"  ✘ Slide HTML Failed: {res.stderr[:300]}")

        # 2. PDF Presentation
        if format_choice in ["pdf", "all"]:
            cmd_pdf = [
                "npx", "--yes", "@marp-team/marp-cli",
                str(slide),
                "--pdf",
                "--chrome-path", "/usr/bin/google-chrome",
                "--allow-local-files",
                "-o", str(pdf_out)
            ]
            res = subprocess.run(cmd_pdf, capture_output=True, text=True)
            if res.returncode == 0 and pdf_out.exists():
                print(f"  ✔ Slide PDF:  {pdf_out.name} ({pdf_out.stat().st_size // 1024} KB)")
            else:
                print(f"  ✘ Slide PDF Failed: {res.stderr[:300]}")


def generate_manifest():
    """Generates distribution manifest with SHA256 checksums."""
    manifest_file = DIST_DIR / "MANIFEST.txt"
    entries = []

    for path in sorted(DIST_DIR.rglob("*")):
        if path.is_file() and path.name != "MANIFEST.txt":
            hasher = hashlib.sha256()
            hasher.update(path.read_bytes())
            checksum = hasher.hexdigest()
            size_kb = path.stat().st_size / 1024
            rel_path = path.relative_to(DIST_DIR)
            entries.append(f"{checksum}  {size_kb:>8.1f} KB  {rel_path}")

    manifest_content = (
        "================================================================================\n"
        "AWS CERTIFICATION STATIC DELIVERY ARTIFACTS DISTRIBUTION MANIFEST\n"
        "Author: Mohamed Fakhruldeen | Repository: fakhruldeen/AWS\n"
        "================================================================================\n"
        "SHA256 CHECKSUM                                SIZE      FILE\n"
        "--------------------------------------------------------------------------------\n"
        + "\n".join(entries) + "\n"
        "================================================================================\n"
    )

    manifest_file.write_text(manifest_content, encoding="utf-8")
    print(f"\n✔ Distribution Manifest Generated: {manifest_file.relative_to(WORK_DIR)}")


def main():
    parser = argparse.ArgumentParser(description="AWS Delivery Artifacts Packaging Engine")
    parser.add_argument("--cert", choices=["CLF", "CLF-AR", "AIF", "ALL"], default="ALL", help="Target certification")
    parser.add_argument("--target", choices=["handbook", "slides", "all"], default="all", help="Target component")
    parser.add_argument("--format", choices=["pdf", "epub", "html", "all"], default="all", help="Target format")
    args = parser.parse_args()

    certs = []
    if args.cert in ["CLF", "ALL"]:
        certs.append(("CLF-C02", CLF_MANIFEST, True))
    if args.cert in ["CLF-AR", "ALL"]:
        certs.append(("CLF-C02-Ar", CLF_AR_MANIFEST, False))
    if args.cert in ["AIF", "ALL"]:
        certs.append(("AIF-C01", AIF_MANIFEST, True))

    for cert_code, manifest, has_slides in certs:
        if args.target in ["handbook", "all"]:
            compile_handbook(manifest, args.format)
        if has_slides and args.target in ["slides", "all"]:
            compile_slides(cert_code, args.format)

    generate_manifest()
    print("\n🎉 ALL STATIC DELIVERY ARTIFACTS COMPILED SUCCESSFULLY!\n")


if __name__ == "__main__":
    main()
