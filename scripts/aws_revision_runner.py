#!/usr/bin/env python3
"""
AWS Certification Interactive Revision Engine & Mock Exam Simulator
=====================================================================
A zero-dependency terminal CLI for practicing, drilling, and taking timed
mock exams for AWS certifications (CLF-C02, AIF-C01) powered by deduplicated
multi-source verified question banks.

Usage:
  python3 scripts/aws_revision_runner.py --cert CLF --mode practice --count 10
  python3 scripts/aws_revision_runner.py --cert AIF --mode mock
  python3 scripts/aws_revision_runner.py --cert AIF --mode drill --domain 3
  python3 scripts/aws_revision_runner.py --mode weakness
  python3 scripts/aws_revision_runner.py --cert CLF --service S3 --consensus 2

Author: Mohamed Fakhruldeen (Repository Trainer)
"""

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ANSI Terminal Styling
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    @classmethod
    def disable(cls):
        cls.HEADER = ''
        cls.BLUE = ''
        cls.CYAN = ''
        cls.GREEN = ''
        cls.YELLOW = ''
        cls.RED = ''
        cls.BOLD = ''
        cls.DIM = ''
        cls.UNDERLINE = ''
        cls.RESET = ''

DEFAULT_VAULT_PATHS = [
    Path("/home/mohamed/Documents/Obsidian Vault/Brain/AWS"),
    Path.home() / "Documents/Obsidian Vault/Brain/AWS",
    Path(__file__).resolve().parent.parent.parent / "Documents/Obsidian Vault/Brain/AWS",
]

DOMAINS_MAP = {
    "CLF": {
        1: "Domain 1: Cloud Concepts (24%)",
        2: "Domain 2: Security and Compliance (30%)",
        3: "Domain 3: Cloud Technology and Services (34%)",
        4: "Domain 4: Billing, Pricing, and Support (12%)",
    },
    "AIF": {
        1: "Domain 1: Fundamentals of AI and ML (20%)",
        2: "Domain 2: Fundamentals of Generative AI (24%)",
        3: "Domain 3: Applications of Foundation Models (28%)",
        4: "Domain 4: Guidelines for Responsible AI (14%)",
        5: "Domain 5: Security, Compliance, and Governance (14%)",
    },
    "MLA": {
        1: "Domain 1: Data Preparation for Machine Learning (28%)",
        2: "Domain 2: ML Model Development (26%)",
        3: "Domain 3: Deployment and Orchestration of ML Workflows (22%)",
        4: "Domain 4: ML Solution Monitoring and Maintenance (24%)",
    },
    "SAA": {
        1: "Domain 1: Design Secure Architectures (30%)",
        2: "Domain 2: Design Resilient Architectures (26%)",
        3: "Domain 3: Design High-Performing Architectures (24%)",
        4: "Domain 4: Design Cost-Optimized Architectures (20%)",
    }
}

MOCK_DISTRIBUTION = {
    "CLF": {1: 16, 2: 20, 3: 21, 4: 8},  # Total = 65 questions
    "AIF": {1: 13, 2: 16, 3: 18, 4: 9, 5: 9},  # Total = 65 questions
    "MLA": {1: 18, 2: 17, 3: 14, 4: 16},  # Total = 65 questions
    "SAA": {1: 20, 2: 17, 3: 15, 4: 13},  # Total = 65 questions
}

MOCK_TIME_LIMIT_MINUTES = {
    "CLF": 90,
    "AIF": 85,
    "MLA": 130,
    "SAA": 130,
}

# =====================================================================
# EXAM DECRYPTION & MNEMONIC TRIGGERS DATABASE
# =====================================================================
TRIGGERS_DB = [
    # Messaging & Decoupling
    {
        "patterns": [r"decouple\w*", r"asynchronous\w*", r"queue\w*", r"buffer\w* spikes"],
        "target": "Amazon SQS",
        "mnemonic": "Reliability Pillar (PERCOS) — SQS buffers asynchronous load spikes so workers process at steady rates.",
        "trap": "Beware of scaling up EC2 instances vertically or using synchronous HTTP calls instead of decoupling with SQS."
    },
    {
        "patterns": [r"fan-out", r"push\w* notification\w*", r"multiple subscribers", r"publish/subscribe"],
        "target": "Amazon SNS",
        "mnemonic": "Pub/Sub Fan-Out — Publishing once to an SNS Topic fans out identical messages to multiple SQS queues or mobile/email endpoints.",
        "trap": "Multiple consumers on a single SQS queue compete for messages (only one consumes); SNS fan-out is needed for parallel delivery."
    },
    {
        "patterns": [r"event bus", r"saas partner", r"content-based filtering"],
        "target": "Amazon EventBridge",
        "mnemonic": "Serverless Event Routing — EventBridge routes events from AWS services, SaaS apps, and microservices based on JSON content.",
        "trap": "EventBridge evaluates JSON payload content; CloudWatch Events is legacy; SQS only buffers messages."
    },
    {
        "patterns": [r"state machine", r"saga pattern", r"compensating transaction", r"coordinate\w* workflow"],
        "target": "AWS Step Functions",
        "mnemonic": "Workflow Orchestration — Step Functions coordinates distributed microservices into visual serverless state machines with retries and rollbacks.",
        "trap": "SQS and SNS do not maintain multi-step workflow execution state or handle compensating rollbacks."
    },
    # Audit & Monitoring
    {
        "patterns": [r"audit\w*", r"who made what", r"api call history", r"management events"],
        "target": "AWS CloudTrail",
        "mnemonic": "Accountability & Auditing — CloudTrail records 'Who did what and when' across AWS management and data APIs.",
        "trap": "CloudWatch monitors metrics & logs; CloudTrail records API audit history; AWS Config evaluates configuration rules over time."
    },
    {
        "patterns": [r"monitor\w* cpu", r"cloudwatch alarm", r"operational metric", r"dashboard"],
        "target": "Amazon CloudWatch",
        "mnemonic": "Observability & Alarms — CloudWatch collects real-time metrics, logs, and triggers automated alarms.",
        "trap": "CloudWatch does not record API caller identity (CloudTrail does); it monitors performance metrics and health."
    },
    {
        "patterns": [r"configuration drift", r"compliance rule\w*", r"track resource changes"],
        "target": "AWS Config",
        "mnemonic": "Continuous Compliance — AWS Config records point-in-time configuration history and evaluates resources against compliance rules.",
        "trap": "CloudTrail logs the API event that caused the change; AWS Config evaluates whether the resulting resource state is compliant."
    },
    # Security & Protection
    {
        "patterns": [r"compliance report\w*", r"soc 1", r"soc 2", r"pci-dss agreement"],
        "target": "AWS Artifact",
        "mnemonic": "Compliance Portal — AWS Artifact is your on-demand self-service portal for official AWS compliance reports and agreements.",
        "trap": "AWS Artifact provides audit reports; AWS Certificate Manager manages SSL/TLS certificates."
    },
    {
        "patterns": [r"rotate\w* database credential\w*", r"rotate\w* secret", r"automatic rotation"],
        "target": "AWS Secrets Manager",
        "mnemonic": "Credential Lifecycle — Secrets Manager automatically rotates RDS database credentials using Lambda without application downtime.",
        "trap": "Systems Manager Parameter Store stores encrypted strings, but does NOT provide built-in automated database credential rotation like Secrets Manager."
    },
    {
        "patterns": [r"layer 7", r"sql injection", r"sqli", r"cross-site scripting", r"xss"],
        "target": "AWS WAF",
        "mnemonic": "Web Application Firewall — WAF operates at Layer 7 (HTTP/HTTPS) inspecting request bodies, query strings, and headers.",
        "trap": "Security Groups and Network ACLs operate at Layer 4 (IP/port) and cannot detect SQLi or XSS attacks."
    },
    {
        "patterns": [r"ddos", r"shield standard", r"shield advanced", r"response team"],
        "target": "AWS Shield",
        "mnemonic": "DDoS Mitigation — Shield Standard is free/automatic for Layer 3/4; Shield Advanced provides 24/7 SRT and DDoS cost protection.",
        "trap": "WAF blocks Layer 7 exploits; Shield mitigates Layer 3/4 volumetric DDoS attacks."
    },
    {
        "patterns": [r"worm", r"compliance mode", r"write once read many", r"object lock"],
        "target": "S3 Object Lock (Compliance Mode)",
        "mnemonic": "Immutable WORM — In Compliance Mode, NO user (not even root) can overwrite or delete objects during the retention period.",
        "trap": "Governance Mode allows users with bypass permissions to delete; Compliance Mode is strict and irreversible."
    },
    {
        "patterns": [r"session manager", r"port 22", r"bastion host"],
        "target": "AWS Systems Manager Session Manager",
        "mnemonic": "Secure Shell Access — Session Manager provides browser-based CLI access to private EC2 instances without opening port 22 or bastion hosts.",
        "trap": "Opening port 22 to 0.0.0.0/0 on a public bastion host is an immediate security anti-pattern."
    },
    # Storage Economics
    {
        "patterns": [r"unpredictable\w* access", r"changing access pattern", r"no retrieval fee"],
        "target": "Amazon S3 Intelligent-Tiering",
        "mnemonic": "S-I-G-G Temperature — Intelligent-Tiering automatically moves data between tiers with ZERO retrieval fees.",
        "trap": "Standard-IA charges per-GB retrieval fees; if access surges, retrieval fees make IA far more expensive than Intelligent-Tiering."
    },
    {
        "patterns": [r"lowest storage cost", r"lowest cost.*archive", r"12 to 48 hours", r"deep archive"],
        "target": "Amazon S3 Glacier Deep Archive",
        "mnemonic": "Frozen Archive — Glacier Deep Archive is the absolute lowest-cost storage in AWS ($0.00099/GB/month) with 12-48h retrieval.",
        "trap": "S3 Standard costs ~23x more than Glacier Deep Archive."
    },
    # FinOps & Compute
    {
        "patterns": [r"least operational overhead", r"minimal management", r"minimal operational overhead"],
        "target": "AWS Managed / Serverless Services",
        "mnemonic": "Stop Heavy Lifting — Favor managed/serverless (Aurora, Fargate, S3, Secrets Manager) over custom scripts and EC2 VMs.",
        "trap": "Custom shell scripts, EC2 cron daemons, and manual failovers violate least operational overhead."
    },
    {
        "patterns": [r"up to 90% discount", r"stateless batch", r"can be interrupted", r"spot instance"],
        "target": "Amazon EC2 Spot Instances",
        "mnemonic": "Spare Capacity Economics — Spot offers up to 90% savings for fault-tolerant, interruptible workloads.",
        "trap": "Do not use Spot for databases or stateful applications that cannot tolerate 2-minute interruption notices."
    },
    {
        "patterns": [r"technical account manager", r"tam", r"concierge", r"15 minutes"],
        "target": "AWS Enterprise Support",
        "mnemonic": "B-D-B-E Support Ladder — Enterprise Support is the ONLY tier providing a dedicated Technical Account Manager (TAM) and 15-minute response.",
        "trap": "Business Support provides 24/7 phone/chat, but does NOT include a designated TAM."
    },
    {
        "patterns": [r"consolidated billing", r"volume discount\w* across", r"linked account"],
        "target": "AWS Organizations Consolidated Billing",
        "mnemonic": "Combined Usage Economics — Consolidated Billing aggregates usage across all member accounts to reach higher volume discount tiers.",
        "trap": "Separate standalone AWS accounts pay individual tiered rates and cannot share volume pricing tiers."
    },
    # AI / Generative AI
    {
        "patterns": [r"hallucination\w*", r"ground\w* foundation", r"citations", r"proprietary internal data"],
        "target": "RAG (Amazon Bedrock Knowledge Bases)",
        "mnemonic": "Model Adaptation (P-R-F-C) — RAG retrieves vector context without altering base model weights and provides verifiable source citations.",
        "trap": "Fine-tuning modifies weights and does NOT provide source citations or eliminate hallucinations like RAG."
    },
    {
        "patterns": [r"multi-step task", r"execute api call", r"orchestrate\w* tool"],
        "target": "Amazon Bedrock Agents",
        "mnemonic": "Autonomous Action Execution — Bedrock Agents break user requests into multi-step actions and invoke AWS Lambda APIs.",
        "trap": "Knowledge Bases retrieve static document context; Bedrock Agents take active transactional actions."
    },
    {
        "patterns": [r"mask\w* pii", r"filter toxic", r"prompt injection", r"guardrail\w*"],
        "target": "Amazon Bedrock Guardrails",
        "mnemonic": "Responsible AI (F-A-T-E) — Bedrock Guardrails filters harmful topics, redacts PII, and halts jailbreak attempts at runtime.",
        "trap": "SageMaker Clarify audits bias and SHAP explainability; Bedrock Guardrails enforces runtime input/output safety."
    },
    {
        "patterns": [r"translation", r"bleu"],
        "target": "BLEU Metric",
        "mnemonic": "B-P Rule — BLEU = Precision-oriented evaluation for Machine Translation against human reference texts.",
        "trap": "ROUGE has an R (Recall-oriented) and is used for Summarization, NOT translation."
    },
    {
        "patterns": [r"summariz\w*", r"rouge"],
        "target": "ROUGE Metric",
        "mnemonic": "R-R Rule — ROUGE = Recall-oriented evaluation for Text Summarization (n-gram overlap).",
        "trap": "BLEU has a P (Precision) for Translation; ROUGE is for Summaries."
    },
    {
        "patterns": [r"perplexity"],
        "target": "Perplexity (PPL)",
        "mnemonic": "The Confusion Metric — The more perplexed the model is, the worse it is! Lower Perplexity = Higher Fluency.",
        "trap": "Eliminate any option claiming 'higher perplexity indicates a better model'."
    },
    {
        "patterns": [r"without modifying base", r"without retraining", r"peft", r"lora", r"low-rank"],
        "target": "PEFT / LoRA (Parameter-Efficient Fine-Tuning)",
        "mnemonic": "Lightweight Adaptation — PEFT/LoRA freezes original base weights and trains small adapter matrices with ~90% less GPU compute.",
        "trap": "Full fine-tuning updates all weights, incurring massive compute cost and risking catastrophic forgetting."
    },
    {
        "patterns": [r"shap\w*", r"feature attribution", r"detect\w* bias", r"explainability"],
        "target": "Amazon SageMaker Clarify",
        "mnemonic": "Transparency (F-A-T-E) — SageMaker Clarify computes SHAP values to explain feature importance and detects pre-/post-training bias.",
        "trap": "Model Cards documents metadata; Clarify calculates the quantitative mathematical SHAP and bias values."
    },
    {
        "patterns": [r"payload up to 1 gb", r"up to 1 hour", r"queued in sqs"],
        "target": "SageMaker Asynchronous Inference",
        "mnemonic": "R-S-A-B Inference Modes — Asynchronous inference buffers requests in SQS, handles payloads up to 1 GB, and runs up to 1 hour.",
        "trap": "Real-time inference maxes out at 6 MB payload and 60 seconds."
    },
    {
        "patterns": [r"scale\w* to zero", r"sporadic\w* traffic", r"unpredictable\w* inference"],
        "target": "SageMaker Serverless Inference",
        "mnemonic": "R-S-A-B Inference Modes — Serverless inference automatically scales compute down to zero when idle, charging strictly per second of usage.",
        "trap": "Real-time inference bills 24/7 per provisioned instance-hour even when completely idle."
    }
]

def find_tricks(text: str) -> List[Dict[str, Any]]:
    matches = []
    seen_targets = set()
    for item in TRIGGERS_DB:
        for p in item["patterns"]:
            if re.search(r'\b' + p + r'\b', text, re.IGNORECASE):
                if item["target"] not in seen_targets:
                    seen_targets.add(item["target"])
                    matches.append(item)
                break
    return matches

def locate_bank(cert: str, custom_path: Optional[str] = None, release_2026: bool = False, community: bool = False) -> Path:
    if custom_path:
        p = Path(custom_path)
        if p.is_file():
            return p
        raise FileNotFoundError(f"Custom question bank not found: {custom_path}")

    work_repo = Path(__file__).resolve().parent.parent
    local_clf_release = work_repo / "Cloud/Practitioner/CLF-C02/phase4_step11_revision_questions/CLF_C02_November_2026_Release_393Q.json"
    local_clf_comm = work_repo / "Cloud/Practitioner/CLF-C02/phase4_step11_revision_questions/CLF_C02_Community_Practice_Pool_718Q.json"
    local_aif_comm = work_repo / "AI/Practitioner/AIF-C01/phase4_step11_revision_questions/AIF_C01_Community_Practice_Pool_233Q.json"
    if not local_aif_comm.is_file():
        local_aif_comm = work_repo / "AI/Practitioner/AIF-C01/phase4_step11_revision_questions/AIF_C01_Community_Practice_Pool_154Q.json"
    local_saa_comm = work_repo / "Cloud/Associate/SAA-C03/phase4_step11_revision_questions/SAA_C03_Community_Practice_Pool_1019Q.json"
    local_mla_comm = work_repo / "AI/Associate/MLA-C01/phase4_step11_revision_questions/MLA_C01_Community_Practice_Pool_106Q.json"

    if community:
        if cert == "CLF" and local_clf_comm.is_file():
            return local_clf_comm
        if cert == "AIF" and local_aif_comm.is_file():
            return local_aif_comm
        if cert == "SAA" and local_saa_comm.is_file():
            return local_saa_comm
        if cert == "MLA" and local_mla_comm.is_file():
            return local_mla_comm

    if release_2026 and cert == "CLF":
        if local_clf_release.is_file():
            return local_clf_release

    env_vault = os.environ.get("AWS_BRAIN_PATH")
    search_paths = [Path(env_vault)] if env_vault else []
    search_paths.extend(DEFAULT_VAULT_PATHS)

    # Check Vault Community Practice Questions directory if requested
    if community:
        for base in search_paths:
            if cert == "CLF":
                v_target = base / "Questions_Bank/Community_Practice_Questions/CLF_C02_Community_Pool_718Q.json"
                if v_target.is_file():
                    return v_target
            elif cert == "AIF":
                v_target = base / "Questions_Bank/Community_Practice_Questions/AIF_C01_Community_Pool_233Q.json"
                if not v_target.is_file():
                    v_target = base / "Questions_Bank/Community_Practice_Questions/AIF_C01_Community_Pool_154Q.json"
                if v_target.is_file():
                    return v_target
            elif cert == "SAA":
                v_target = base / "Questions_Bank/Community_Practice_Questions/SAA_C03_Community_Pool_1019Q.json"
                if v_target.is_file():
                    return v_target
            elif cert == "MLA":
                v_target = base / "Questions_Bank/Community_Practice_Questions/MLA_C01_Community_Pool_106Q.json"
                if v_target.is_file():
                    return v_target

    subfolder_map = {
        "CLF": ("Cloud_Practitioner_CLF-C02", "CLF_C02_Master_Unique_Questions.json"),
        "AIF": ("AI_Practitioner_AIF-C01", "AIF_C01_Master_Unique_Questions.json"),
        "MLA": ("Machine_Learning_Associate_MLA-C01", "MLA_C01_Master_Unique_Questions.json"),
        "SAA": ("Solutions_Architect_Associate_SAA-C03", "SAA_C03_Master_Unique_Questions.json"),
    }
    subfolder, filename = subfolder_map.get(cert, (f"{cert}_Track", f"{cert}_Master_Unique_Questions.json"))

    for base in search_paths:
        target = base / "Questions_Bank" / "Unique_Revision_Banks" / subfolder / filename
        if target.is_file():
            return target

    # Local fallback for self-sufficiency
    if cert == "CLF" and local_clf_release.is_file():
        return local_clf_release

    raise FileNotFoundError(
        f"Could not locate master question bank for {cert}. "
        f"Looked for: {subfolder}/{filename} across {search_paths}. "
        "Use --bank-path to specify exact location."
    )

def load_questions(bank_file: Path) -> List[Dict[str, Any]]:
    with open(bank_file, "r", encoding="utf-8") as f:
        return json.load(f)

def clean_choice(raw_choice: str, expected_idx: int) -> str:
    # Remove leading option labels like "A)", "A. ", ") ", "1) "
    cleaned = raw_choice.strip()
    cleaned = re.sub(r'^[A-Ea-e\d][\)\.\:\-]\s*', '', cleaned)
    cleaned = re.sub(r'^\)\s*', '', cleaned)
    return cleaned.strip()

def normalize_answer(ans: Any) -> Set[str]:
    if isinstance(ans, list):
        return {str(x).strip().upper() for x in ans if str(x).strip()}
    if isinstance(ans, str):
        # Handle "A, C" or "A,C" or "AC" or "A and C"
        tokens = re.findall(r'[A-Ea-e]', ans)
        return {t.upper() for t in tokens}
    return set()

def load_history(history_file: Path) -> Dict[str, Any]:
    if not history_file.exists():
        return {"sessions": [], "weak_ids": {}}
    try:
        with open(history_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"sessions": [], "weak_ids": {}}

def save_history(history_file: Path, history: Dict[str, Any]):
    history_file.parent.mkdir(parents=True, exist_ok=True)
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def format_domain_name(cert: str, domain_val: Any) -> str:
    try:
        d_int = int(domain_val)
        return DOMAINS_MAP.get(cert, {}).get(d_int, f"Domain {d_int}")
    except (ValueError, TypeError):
        return str(domain_val)

def filter_questions(
    questions: List[Dict[str, Any]],
    domain: Optional[int] = None,
    service_query: Optional[str] = None,
    min_consensus: Optional[int] = None,
    weak_ids: Optional[Set[str]] = None,
    community_only: bool = False,
) -> List[Dict[str, Any]]:
    filtered = questions

    if community_only:
        filtered = [
            q for q in filtered
            if any("community" in s.lower() for s in q.get("sources", []))
        ]

    if weak_ids is not None:
        filtered = [q for q in filtered if q.get("id") in weak_ids]

    if domain is not None:
        filtered = [q for q in filtered if q.get("domain") == domain]

    if min_consensus is not None:
        filtered = [q for q in filtered if len(q.get("sources", [])) >= min_consensus]

    if service_query:
        query_pattern = re.compile(re.escape(service_query), re.IGNORECASE)
        filtered = [
            q for q in filtered
            if query_pattern.search(q.get("prompt", ""))
            or any(query_pattern.search(c) for c in q.get("choices", []))
            or query_pattern.search(q.get("explanation", ""))
        ]

    return filtered

def sample_mock_questions(
    cert: str,
    questions: List[Dict[str, Any]],
    community_only: bool = False
) -> List[Dict[str, Any]]:
    dist = MOCK_DISTRIBUTION.get(cert, {})
    pool_questions = questions

    if community_only:
        comm_pool = [q for q in questions if any("community" in s.lower() for s in q.get("sources", []))]
        if comm_pool:
            pool_questions = comm_pool

    by_domain: Dict[int, List[Dict[str, Any]]] = {}
    for q in pool_questions:
        d = q.get("domain", 1)
        by_domain.setdefault(d, []).append(q)

    mock_set = []
    target_count = 65 if not community_consensus_only or len(pool_questions) >= 65 else len(pool_questions)

    for d, count in dist.items():
        pool = by_domain.get(d, [])
        # Prioritize Community Consensus Pool questions within the domain pool
        pool.sort(key=lambda q: (1 if any("community_consensus" in s.lower() for s in q.get("sources", [])) else 0), reverse=True)
        take_count = min(count, len(pool))
        if take_count > 0:
            mock_set.extend(random.sample(pool[:max(take_count * 2, take_count)], take_count))

    # If count is less than target due to distribution shortages, top up
    if len(mock_set) < target_count:
        existing_ids = {q["id"] for q in mock_set}
        remaining = [q for q in pool_questions if q["id"] not in existing_ids]
        needed = target_count - len(mock_set)
        if len(remaining) >= needed:
            mock_set.extend(random.sample(remaining, needed))
        else:
            mock_set.extend(remaining)

    random.shuffle(mock_set)
    return mock_set[:target_count]

def display_question(
    q: Dict[str, Any],
    idx: int,
    total: int,
    cert: str,
    show_meta: bool = True,
    show_tricks: bool = False
) -> Tuple[List[str], Set[str]]:
    q_id = q.get("id", "Q")
    prompt = q.get("prompt", "")
    choices = q.get("choices", [])
    if not choices and "options" in q:
        choices = [f"{k}) {v}" for k, v in sorted(q["options"].items())]
    expected = normalize_answer(q.get("answer", ""))
    domain_str = format_domain_name(cert, q.get("domain"))
    sources = q.get("sources", [])
    consensus = len(sources)

    is_multi = len(expected) > 1

    print(f"\n{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}[Question {idx}/{total}]  ID: {q_id}  |  {domain_str}{Colors.RESET}")
    if show_meta:
        print(f"{Colors.DIM}Verified Sources ({consensus}): {', '.join(sources[:4])}{'...' if len(sources)>4 else ''}{Colors.RESET}")
    if any("2026" in str(s).lower() or "actual" in str(s).lower() or "q393" in str(s).lower() for s in sources):
        print(f"{Colors.YELLOW}{Colors.BOLD}🔥 NOVEMBER 2026 AUTHENTIC EXAM RELEASE — Candidate Practice Pool (393Q){Colors.RESET}")
    elif any("community" in str(s).lower() for s in sources):
        print(f"{Colors.GREEN}{Colors.BOLD}⭐ AUTHENTIC COMMUNITY PRACTICE QUESTION — Verified Candidate Discussion Consensus{Colors.RESET}")
    if show_tricks:
        print(f"{Colors.YELLOW}{Colors.BOLD}💡 TRICKS & MNEMONIC MODE ACTIVE — Key trigger words are highlighted in gold.{Colors.RESET}")
    print(f"{Colors.CYAN}{'-'*80}{Colors.RESET}\n")

    display_prompt = prompt
    if show_tricks:
        for item in TRIGGERS_DB:
            for p in item["patterns"]:
                display_prompt = re.sub(
                    r'(?i)\b(' + p + r')\b',
                    f"{Colors.YELLOW}{Colors.BOLD}\\1{Colors.RESET}{Colors.BOLD}",
                    display_prompt
                )

    print(f"{Colors.BOLD}{display_prompt}{Colors.RESET}\n")

    if is_multi:
        print(f"{Colors.YELLOW}{Colors.BOLD}⚡ MULTI-SELECT: Choose {len(expected)} options (e.g., A, C){Colors.RESET}\n")

    option_letters = ["A", "B", "C", "D", "E"]
    clean_choices = []
    for i, choice in enumerate(choices):
        letter = option_letters[i] if i < len(option_letters) else f"({i+1})"
        cleaned_text = clean_choice(choice, i)
        clean_choices.append(cleaned_text)
        print(f"  {Colors.BOLD}{Colors.CYAN}[{letter}]{Colors.RESET} {cleaned_text}")

    print("")
    return clean_choices, expected

def prompt_user_answer(expected_count: int) -> Optional[Set[str]]:
    while True:
        try:
            raw = input(f"{Colors.BOLD}Your Answer (or 'q' to quit, 's' to skip): {Colors.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting session...")
            return None

        if raw.lower() == 'q':
            return None
        if raw.lower() == 's':
            return set()

        letters = re.findall(r'[A-Ea-e]', raw)
        chosen = {l.upper() for l in letters}

        if not chosen:
            print(f"{Colors.RED}Invalid input. Please enter letter choices like 'A' or 'B, C'.{Colors.RESET}")
            continue

        if expected_count > 1 and len(chosen) != expected_count:
            print(f"{Colors.YELLOW}Warning: This question requires {expected_count} answers. You entered {len(chosen)}.{Colors.RESET}")
            confirm = input(f"Submit anyway? (y/N): ").strip().lower()
            if confirm != 'y':
                continue

        return chosen

def render_feedback(
    is_correct: bool,
    expected: Set[str],
    explanation: str,
    prompt: str = "",
    show_tricks: bool = False
):
    if is_correct:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✅ CORRECT! Excellent job.{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ INCORRECT.{Colors.RESET}")
        print(f"{Colors.BOLD}Verified Correct Answer: {Colors.GREEN}{', '.join(sorted(expected))}{Colors.RESET}")

    if show_tricks:
        tricks = find_tricks(prompt + " " + explanation)
        if tricks:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}💡 EXAM DECRYPTION & MNEMONIC ANCHORS ({len(tricks)} detected):{Colors.RESET}")
            for t in tricks[:2]:
                print(f"  {Colors.BOLD}{Colors.CYAN}🔑 Target Match:{Colors.RESET} {Colors.BOLD}{t['target']}{Colors.RESET}")
                print(f"  {Colors.BOLD}{Colors.YELLOW}🧠 Mnemonic Cue:{Colors.RESET} {t['mnemonic']}")
                print(f"  {Colors.BOLD}{Colors.RED}🚫 Distractor Trap:{Colors.RESET} {t['trap']}")

    if explanation:
        print(f"\n{Colors.CYAN}{Colors.BOLD}📖 Architectural Rationale & Distractor Breakdown:{Colors.RESET}")
        print(f"{Colors.DIM}{explanation}{Colors.RESET}\n")

def run_practice_or_drill(
    cert: str,
    questions: List[Dict[str, Any]],
    mode: str,
    history_file: Path,
    show_tricks: bool = False
):
    total = len(questions)
    if total == 0:
        print(f"{Colors.YELLOW}No questions matched your filter criteria.{Colors.RESET}")
        return

    history = load_history(history_file)
    weak_ids = history.setdefault("weak_ids", {})

    print(f"\n{Colors.GREEN}{Colors.BOLD}🚀 Launching {cert} {mode.upper()} Mode with {total} question(s){Colors.RESET}")
    print(f"{Colors.DIM}Type 'q' anytime to end early and save progress.{Colors.RESET}")

    correct_count = 0
    attempted_count = 0
    results_summary = []

    for idx, q in enumerate(questions, 1):
        clean_choices, expected = display_question(q, idx, total, cert, show_meta=True, show_tricks=show_tricks)
        user_ans = prompt_user_answer(len(expected))

        if user_ans is None:
            print(f"\n{Colors.YELLOW}Session aborted early by user.{Colors.RESET}")
            break

        if not user_ans:  # Skipped
            print(f"{Colors.YELLOW}Skipped question {q.get('id')}.{Colors.RESET}")
            continue

        attempted_count += 1
        is_correct = (user_ans == expected)
        if is_correct:
            correct_count += 1
            if q.get("id") in weak_ids:
                weak_ids[q["id"]]["consecutive_correct"] = weak_ids[q["id"]].get("consecutive_correct", 0) + 1
                if weak_ids[q["id"]]["consecutive_correct"] >= 2:
                    del weak_ids[q["id"]]  # Mastered!
        else:
            weak_entry = weak_ids.setdefault(q.get("id"), {"cert": cert, "domain": q.get("domain"), "consecutive_correct": 0, "failures": 0})
            weak_entry["failures"] += 1
            weak_entry["consecutive_correct"] = 0
            weak_entry["prompt_preview"] = q.get("prompt", "")[:120]

        results_summary.append({
            "id": q.get("id"),
            "domain": q.get("domain"),
            "correct": is_correct
        })

        if mode == "practice":
            render_feedback(is_correct, expected, q.get("explanation", ""), prompt=q.get("prompt", ""), show_tricks=show_tricks)
            try:
                input(f"{Colors.DIM}Press [Enter] to continue to the next question...{Colors.RESET}")
            except (EOFError, KeyboardInterrupt):
                break

    save_history(history_file, history)

    # Session Summary Report
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}SESSION COMPLETE: SUMMARY REPORT{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    pct = (correct_count / attempted_count * 100) if attempted_count > 0 else 0
    print(f"Total Attempted: {attempted_count}/{total}")
    print(f"Correct Answers: {correct_count}")
    print(f"Accuracy Rate:   {Colors.BOLD}{Colors.GREEN if pct>=70 else Colors.RED}{pct:.1f}%{Colors.RESET}")

    # Domain Breakdown
    domains_attempted: Dict[int, List[bool]] = {}
    for r in results_summary:
        d = r["domain"]
        domains_attempted.setdefault(d, []).append(r["correct"])

    if domains_attempted:
        print(f"\n{Colors.BOLD}Domain Performance Breakdown:{Colors.RESET}")
        for d_key, bools in sorted(domains_attempted.items()):
            d_name = format_domain_name(cert, d_key)
            d_pct = (sum(bools) / len(bools)) * 100
            status_color = Colors.GREEN if d_pct >= 70 else (Colors.YELLOW if d_pct >= 50 else Colors.RED)
            print(f"  • {d_name:<45} {status_color}{sum(bools)}/{len(bools)} ({d_pct:.1f}%){Colors.RESET}")

    print(f"\n{Colors.DIM}Results recorded in: {history_file}{Colors.RESET}\n")

def run_mock_exam(
    cert: str,
    questions: List[Dict[str, Any]],
    history_file: Path,
    community_only: bool = False,
    show_tricks: bool = False
):
    mock_set = sample_mock_questions(cert, questions, community_only=community_only)
    total = len(mock_set)
    time_limit_mins = MOCK_TIME_LIMIT_MINUTES.get(cert, 90)

    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.RESET}")
    et_tag = f" [{Colors.GREEN}COMMUNITY PRACTICE FOCUS POOL{Colors.RESET}{Colors.HEADER}{Colors.BOLD}]" if community_only else ""
    print(f"{Colors.HEADER}{Colors.BOLD}🎓 OFFICIAL AWS TIMED MOCK EXAM SIMULATION: {cert}-C0{2 if cert=='CLF' else 1}{et_tag}{Colors.RESET}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.RESET}")
    print(f"• Total Questions:   {Colors.BOLD}{total}{Colors.RESET}")
    print(f"• Allocated Time:    {Colors.BOLD}{time_limit_mins} minutes{Colors.RESET}")
    print(f"• Passing Threshold: {Colors.BOLD}700 / 1000 (Scaled Scoring ~70% raw){Colors.RESET}")
    if community_only:
        print(f"• Question Provenance: {Colors.GREEN}{Colors.BOLD}Authentic Community Practice Pool (Discussion Consensus){Colors.RESET}")
    print(f"• Domain Balance:    Weighted exactly per official AWS Exam Blueprint")
    print(f"{Colors.DIM}Controls: Enter letters (A, B), 's' to skip, 'q' to finish and grade early.{Colors.RESET}\n")

    input(f"{Colors.BOLD}{Colors.GREEN}Ready? Press [Enter] to begin the exam clock...{Colors.RESET}")

    start_time = time.time()
    time_limit_secs = time_limit_mins * 60

    user_answers: Dict[int, Set[str]] = {}
    history = load_history(history_file)
    weak_ids = history.setdefault("weak_ids", {})

    for idx, q in enumerate(mock_set, 1):
        elapsed = time.time() - start_time
        remaining = max(0, time_limit_secs - elapsed)
        rem_mins = int(remaining // 60)
        rem_secs = int(remaining % 60)

        if remaining <= 0:
            print(f"\n{Colors.RED}{Colors.BOLD}⏰ TIME IS UP! The exam time limit has expired.{Colors.RESET}\n")
            break

        print(f"\n{Colors.DIM}[Time Remaining: {rem_mins:02d}:{rem_secs:02d}]{Colors.RESET}")
        clean_choices, expected = display_question(q, idx, total, cert, show_meta=False, show_tricks=show_tricks)
        ans = prompt_user_answer(len(expected))

        if ans is None:
            confirm = input(f"{Colors.YELLOW}Are you sure you want to end and submit the exam early? (y/N): {Colors.RESET}").strip().lower()
            if confirm == 'y':
                break
            else:
                continue

        user_answers[idx] = ans

    total_time_taken = time.time() - start_time
    mins_taken = int(total_time_taken // 60)
    secs_taken = int(total_time_taken % 60)

    # Grading
    score_tally = 0
    domain_scores: Dict[int, List[bool]] = {}
    missed_questions = []

    for idx, q in enumerate(mock_set, 1):
        expected = normalize_answer(q.get("answer", ""))
        user_ans = user_answers.get(idx, set())
        is_correct = (user_ans == expected and len(expected) > 0)
        d = q.get("domain", 1)
        domain_scores.setdefault(d, []).append(is_correct)

        if is_correct:
            score_tally += 1
            if q.get("id") in weak_ids:
                weak_ids[q["id"]]["consecutive_correct"] = weak_ids[q["id"]].get("consecutive_correct", 0) + 1
                if weak_ids[q["id"]]["consecutive_correct"] >= 2:
                    del weak_ids[q["id"]]
        else:
            missed_questions.append({
                "index": idx,
                "id": q.get("id"),
                "prompt": q.get("prompt"),
                "expected": expected,
                "user_ans": user_ans,
                "explanation": q.get("explanation"),
                "domain": d
            })
            weak_entry = weak_ids.setdefault(q.get("id"), {"cert": cert, "domain": d, "consecutive_correct": 0, "failures": 0})
            weak_entry["failures"] += 1
            weak_entry["consecutive_correct"] = 0
            weak_entry["prompt_preview"] = q.get("prompt", "")[:120]

    # Scaled AWS Score: 100 to 1000 scale
    # Raw formula: Scaled = 100 + (score_tally / total) * 900
    scaled_score = int(100 + (score_tally / total) * 900) if total > 0 else 100
    passed = scaled_score >= 700

    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.HEADER}                    OFFICIAL EXAM SCORE REPORT                    {Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*80}{Colors.RESET}")
    print(f"Certification: {Colors.BOLD}AWS Certified {('Cloud' if cert=='CLF' else 'AI')} Practitioner ({cert}-C0{2 if cert=='CLF' else 1}){Colors.RESET}")
    print(f"Time Elapsed:  {mins_taken}m {secs_taken}s / {time_limit_mins}m")
    print(f"Raw Score:     {score_tally} / {total} ({(score_tally/total*100):.1f}%)")
    print(f"Scaled Score:  {Colors.BOLD}{scaled_score} / 1000{Colors.RESET}")
    print(f"Pass/Fail:     {Colors.BOLD}{Colors.GREEN if passed else Colors.RED}{'PASS 🎉' if passed else 'DID NOT PASS ❌'}{Colors.RESET}")
    print(f"Passing Score: 700 / 1000\n")

    print(f"{Colors.BOLD}Domain Diagnostics:{Colors.RESET}")
    for d_key, bools in sorted(domain_scores.items()):
        d_name = format_domain_name(cert, d_key)
        d_pct = (sum(bools) / len(bools)) * 100
        status = "MEETS COMPETENCY" if d_pct >= 70 else "NEEDS IMPROVEMENT"
        color = Colors.GREEN if d_pct >= 70 else Colors.RED
        print(f"  • {d_name:<48} {color}{d_pct:.1f}% ({status}){Colors.RESET}")

    # Record Session in History
    history["sessions"].append({
        "cert": cert,
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "scaled_score": scaled_score,
        "raw_score": f"{score_tally}/{total}",
        "passed": passed,
        "time_mins": mins_taken
    })
    save_history(history_file, history)

    # Missed Questions Review
    if missed_questions:
        print(f"\n{Colors.BOLD}{Colors.YELLOW}Would you like to review the {len(missed_questions)} missed question(s) with full architectural rationales? (Y/n): {Colors.RESET}", end="")
        try:
            rev_choice = input().strip().lower()
        except (EOFError, KeyboardInterrupt):
            rev_choice = 'n'

        if rev_choice != 'n':
            for m in missed_questions:
                print(f"\n{Colors.RED}{'='*80}{Colors.RESET}")
                print(f"{Colors.BOLD}Question {m['index']} ({m['id']}) — {format_domain_name(cert, m['domain'])}{Colors.RESET}")
                print(f"{m['prompt']}\n")
                print(f"Your Answer:     {Colors.RED}{', '.join(sorted(m['user_ans'])) if m['user_ans'] else 'None (Skipped)'}{Colors.RESET}")
                print(f"Correct Answer:  {Colors.GREEN}{', '.join(sorted(m['expected']))}{Colors.RESET}\n")
                print(f"{Colors.CYAN}{Colors.BOLD}Explanation:{Colors.RESET}")
                print(f"{Colors.DIM}{m['explanation']}{Colors.RESET}")
                input(f"\n{Colors.DIM}Press [Enter] for next missed question...{Colors.RESET}")

    print(f"\n{Colors.GREEN}Mock exam completed. Keep studying and mastering the domain objectives!{Colors.RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        description="AWS Certification Interactive Revision Engine & Mock Exam Simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Practice 10 Bedrock / AI questions on AIF-C01
  python3 scripts/aws_revision_runner.py --cert AIF --mode practice --domain 3 --count 10

  # Run full timed 65-question mock exam for CLF-C02
  python3 scripts/aws_revision_runner.py --cert CLF --mode mock

  # Drill questions with at least 3 source confirmations
  python3 scripts/aws_revision_runner.py --cert CLF --consensus 3 --count 20

  # Retake all previously missed questions
  python3 scripts/aws_revision_runner.py --mode weakness
        """
    )

    parser.add_argument("--cert", choices=["CLF", "AIF", "MLA", "SAA"], default="CLF", help="Certification track (CLF, AIF, MLA, or SAA)")
    parser.add_argument("--mode", choices=["practice", "drill", "mock", "weakness"], default="practice", help="Operating mode")
    parser.add_argument("--domain", type=int, choices=[1, 2, 3, 4, 5], default=None, help="Filter by domain number")
    parser.add_argument("--service", "--tag", dest="service", default=None, help="Filter by AWS service or keyword (e.g., S3, Bedrock, VPC)")
    parser.add_argument("--consensus", type=int, default=None, help="Minimum source consensus count (e.g., 2, 3)")
    parser.add_argument("--count", "-n", type=int, default=None, help="Number of questions to test (default: 10 for practice/drill, 65 for mock)")
    parser.add_argument("--tricks", action="store_true", help="Enable Exam Decryption & Mnemonic Mode (highlights trigger keywords and reveals memory pegs)")
    parser.add_argument("--community", "--community-pool", "--practice-pool", dest="community", action="store_true", help="Filter and focus exclusively on authentic community discussion & consensus practice questions")
    parser.add_argument("--release-2026", "--nov-2026", dest="release_2026", action="store_true", help="Filter and focus exclusively on authentic November 2026 393-question exam practice suite")
    parser.add_argument("--bank-path", default=None, help="Custom path to question bank JSON file")
    parser.add_argument("--history-file", default=str(Path.home() / ".aws_revision_history.json"), help="Path to weakness tracking history file")
    parser.add_argument("--no-color", action="store_true", help="Disable colored terminal output")

    args = parser.parse_args()

    if args.no_color:
        Colors.disable()

    history_path = Path(args.history_file)

    if args.mode == "weakness":
        history = load_history(history_path)
        weak_dict = history.get("weak_ids", {})
        if not weak_dict:
            print(f"{Colors.GREEN}🎉 No weaknesses recorded! You have zero pending incorrect questions.{Colors.RESET}")
            return

        weak_cert_ids = [qid for qid, data in weak_dict.items() if data.get("cert") == args.cert or args.cert is None]
        if not weak_cert_ids:
            print(f"{Colors.GREEN}No recorded weaknesses for {args.cert}! Try practicing other domains.{Colors.RESET}")
            return

        bank_file = locate_bank(args.cert, args.bank_path, release_2026=args.release_2026, community=args.community)
        all_q = load_questions(bank_file)
        filtered = filter_questions(all_q, weak_ids=set(weak_cert_ids), community_only=args.community)
        print(f"\n{Colors.YELLOW}{Colors.BOLD}🔍 Found {len(filtered)} previously missed question(s) in weakness history.{Colors.RESET}")
        run_practice_or_drill(args.cert, filtered, "practice", history_path, show_tricks=args.tricks)
        return

    # Locate and load bank
    bank_file = locate_bank(args.cert, args.bank_path, release_2026=args.release_2026, community=args.community)
    all_questions = load_questions(bank_file)

    if args.mode == "mock":
        run_mock_exam(args.cert, all_questions, history_path, community_only=args.community, show_tricks=args.tricks)
        return

    # Filter questions for practice or drill
    filtered = filter_questions(
        all_questions,
        domain=args.domain,
        service_query=args.service,
        min_consensus=args.consensus,
        community_only=args.community
    )

    if not filtered:
        print(f"{Colors.RED}No questions match your filter criteria.{Colors.RESET}")
        return

    random.shuffle(filtered)
    count = args.count if args.count is not None else 10
    selected = filtered[:count]

    run_practice_or_drill(args.cert, selected, args.mode, history_path, show_tricks=args.tricks)

if __name__ == "__main__":
    main()
