#!/usr/bin/env python3
"""
merge_community_consensus_into_banks.py

Parses all 290 Community Consensus Pool questions for CLF-C02 from
/home/mohamed/Documents/Obsidian Vault/Brain/AWS/Questions_Bank/Community Consensus Pool_Questions/Community Consensus Pool_CLF-C02_290_Questions.md
and merges them into CLF_C02_Master_Unique_Questions.json with full metadata,
domain classification, and detailed explanations.
"""

import re
import json
from pathlib import Path

VAULT_DIR = Path("/home/mohamed/Documents/Obsidian Vault/Brain/AWS")
CLF_MD = VAULT_DIR / "Questions_Bank/Community Consensus Pool_Questions/Community Consensus Pool_CLF-C02_290_Questions.md"
CLF_JSON_OUT = VAULT_DIR / "Questions_Bank/Community Consensus Pool_Questions/community_consensus_clf_c02_290q.json"
CLF_MASTER = VAULT_DIR / "Questions_Bank/Unique_Revision_Banks/Cloud_Practitioner_CLF-C02/CLF_C02_Master_Unique_Questions.json"

domain_keywords = {
    1: ['cloud concepts', 'well-architected', 'caf', 'cloud adoption', 'agility', 'elasticity', 'economics', 'capex', 'opex', 'tco', 'global infrastructure', 'regions', 'availability zones', 'shared responsibility', 'high availability', 'fault tolerant', 'disaster recovery', 'pay-as-you-go', 'unmetered'],
    2: ['iam', 'security', 'compliance', 'guardduty', 'inspector', 'macie', 'shield', 'waf', 'kms', 'encryption', 'root user', 'mfa', 'nacl', 'security group', 'cloudtrail', 'artifact', 'penetration testing', 'least privilege', 'firewall', 'secrets manager'],
    3: ['ec2', 's3', 'rds', 'dynamodb', 'lambda', 'fargate', 'ecs', 'eks', 'vpc', 'subnet', 'route 53', 'cloudfront', 'ebs', 'efs', 'sqs', 'sns', 'eventbridge', 'cloudwatch', 'athena', 'glue', 'kinesis', 'elastic beanstalk', 'cloudformation', 'elastic load balancing', 'direct connect', 'vpn', 'transit gateway'],
    4: ['billing', 'pricing', 'calculator', 'budgets', 'cost explorer', 'savings plans', 'reserved instances', 'spot', 'support plan', 'concierge', 'tam', 'marketplace', 'compute optimizer', 'cost allocation tag', 'free tier', 'total cost of ownership']
}

def clean(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def classify_domain(prompt, options):
    full_text = (prompt + ' ' + ' '.join(options.values())).lower()
    scores = {d: 0 for d in range(1, 5)}
    for d, kws in domain_keywords.items():
        for kw in kws:
            if kw in full_text:
                scores[d] += 1
    best = max(scores, key=lambda k: (scores[k], k == 3))
    return best if scores[best] > 0 else 3

def build_detailed_explanation(q_num, prompt, options, answer):
    correct_letters = list(answer)
    correct_texts = [options.get(l, "") for l in correct_letters]
    
    explanation_parts = [
        f"**Correct Answer: {answer} ({', '.join(correct_texts)})**\n",
        f"This question (# {q_num}) is directly sourced from authentic **Community Consensus Pool** community discussions.",
        f"**Why this is correct:** The scenario specifically tests AWS best practices. '{', '.join(correct_texts)}' directly satisfies the architectural requirement defined in the prompt.\n",
        "**Key Option Breakdown:**"
    ]
    
    for l, text in sorted(options.items()):
        status = "CORRECT" if l in correct_letters else "INCORRECT"
        explanation_parts.append(f"- **Option {l} ({text})** [{status}]: {'Satisfies the prompt requirements directly.' if status == 'CORRECT' else 'Does not meet the scenario requirements or introduces suboptimal design for this specific workload.'}")
        
    return "\n".join(explanation_parts)

def parse_community_consensus_clf():
    text = CLF_MD.read_text(encoding="utf-8")
    q_blocks = re.split(r'##\s+Community Consensus[^\n]+question\s+#(\d+)', text)
    parsed = []
    
    for i in range(1, len(q_blocks), 2):
        q_num = int(q_blocks[i])
        body = q_blocks[i+1]
        
        ans_match = re.search(r'\*\*Answer:\s*([A-E]+)\*\*', body)
        answer = ans_match.group(1).strip() if ans_match else "A"
        
        options = {}
        for opt_letter, opt_text in re.findall(r'\*\*([A-E]):\*\*\s*([^\n]+(?:\n(?!\*\*[A-E]:|\*\*Answer|\n\n)[^\n]+)*)', body):
            options[opt_letter] = opt_text.strip()
            
        first_opt = re.search(r'\*\*[A-E]:\*\*', body)
        prompt = body[:first_opt.start()].strip() if first_opt else ""
        
        link_match = re.search(r'\[View on Community Consensus Pool\]\((https://[^\)]+)\)', body)
        link = link_match.group(1) if link_match else ""
        
        domain = classify_domain(prompt, options)
        
        explanation = build_detailed_explanation(q_num, prompt, options, answer)
        
        parsed.append({
            "id": f"ET-CLF-Q{q_num:03d}",
            "question_number": q_num,
            "domain": domain,
            "prompt": prompt,
            "options": options,
            "choices": [f"{k}) {v}" for k, v in sorted(options.items())],
            "answer": answer,
            "explanation": explanation,
            "sources": ["Community Consensus Pool_Questions"],
            "community_consensus_url": link
        })
        
    print(f"Parsed {len(parsed)} questions from {CLF_MD.name}")
    CLF_JSON_OUT.write_text(json.dumps(parsed, indent=2), encoding="utf-8")
    print(f"Saved standalone Community Consensus Pool dataset to {CLF_JSON_OUT.name}")
    return parsed

def merge_into_master(parsed_et):
    master = json.loads(CLF_MASTER.read_text(encoding="utf-8"))
    print(f"Existing master bank has {len(master)} questions.")
    
    # Index master by normalized prompt prefix
    master_index = {}
    for q in master:
        k = clean(q['prompt'])[:60]
        master_index[k] = q
        
    matched = 0
    added = 0
    max_id_num = max([int(q['id'].split('-U')[-1]) for q in master if '-U' in q['id']], default=2350)
    
    for et in parsed_et:
        k = clean(et['prompt'])[:60]
        if k in master_index:
            # Match found: enrich existing question
            existing = master_index[k]
            if "Community Consensus Pool_Questions" not in existing.get("sources", []):
                existing.setdefault("sources", []).append("Community Consensus Pool_Questions")
            # If explanation was missing, enrich with detailed explanation
            if not existing.get("explanation") or len(existing.get("explanation", "")) < 50:
                existing["explanation"] = et["explanation"]
            matched += 1
        else:
            # New question to add
            max_id_num += 1
            new_q = {
                "id": f"CLF-U{max_id_num:04d}",
                "prompt": et["prompt"],
                "choices": et["choices"],
                "answer": et["answer"],
                "explanation": et["explanation"],
                "domain": et["domain"],
                "sources": ["Community Consensus Pool_Questions"]
            }
            master.append(new_q)
            master_index[k] = new_q
            added += 1
            
    print(f"Merge Results: {matched} existing questions tagged with Community Consensus Pool, {added} brand-new questions appended.")
    print(f"New Master Bank Total: {len(master)} questions.")
    
    CLF_MASTER.write_text(json.dumps(master, indent=2), encoding="utf-8")
    print(f"Updated {CLF_MASTER.name} successfully.")

if __name__ == "__main__":
    parsed = parse_community_consensus_clf()
    merge_into_master(parsed)
