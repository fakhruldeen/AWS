#!/usr/bin/env bash
# ==============================================================================
# ExamTopics Downloader & Ingestion Automated Runbook
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK_REPO="$(cd "${SCRIPT_DIR}/.." && pwd)"
VAULT_BASE="${AWS_BRAIN_PATH:-/home/mohamed/Documents/Obsidian Vault/Brain/AWS}"
RAW_CACHE_DIR="${WORK_REPO}/downloads/examtopics-data/Amazon"

usage() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --exam <CLF-C02|AIF-C01|SAA-C03|MLA-C01>  Target AWS exam code (default: CLF-C02)"
    echo "  --mode <cache|live>                      'cache' uses pre-scraped data, 'live' uses Docker scraper (default: cache)"
    echo "  --token <GITHUB_PAT>                     Optional GitHub PAT for live scraper"
    echo "  --help                                   Show this help message"
    exit 1
}

EXAM="CLF-C02"
MODE="cache"
GH_TOKEN=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --exam)
            EXAM="$2"
            shift 2
            ;;
        --mode)
            MODE="$2"
            shift 2
            ;;
        --token)
            GH_TOKEN="$2"
            shift 2
            ;;
        --help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

echo "=============================================================================="
echo "🎯 ExamTopics Downloader & Ingestion Engine"
echo "• Target Certification: ${EXAM}"
echo "• Execution Mode:      ${MODE}"
echo "• Work Repository:     ${WORK_REPO}"
echo "• Obsidian Vault:      ${VAULT_BASE}"
echo "=============================================================================="

case "${EXAM}" in
    CLF-C02)
        WORK_JSON="${WORK_REPO}/Cloud/Practitioner/CLF-C02/phase4_step11_revision_questions/CLF_C02_ExamTopics_Community_Pool_718Q.json"
        WORK_MD="${WORK_REPO}/Cloud/Practitioner/CLF-C02/phase4_step11_revision_questions/CLF_C02_ExamTopics_Community_Pool_718Q.md"
        VAULT_JSON="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/CLF_C02_ExamTopics_Community_Pool_718Q.json"
        VAULT_MD="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/CLF_C02_ExamTopics_Community_Pool_718Q.md"
        ;;
    AIF-C01)
        WORK_JSON="${WORK_REPO}/AI/Practitioner/AIF-C01/phase4_step11_revision_questions/AIF_C01_ExamTopics_Community_Pool_154Q.json"
        WORK_MD="${WORK_REPO}/AI/Practitioner/AIF-C01/phase4_step11_revision_questions/AIF_C01_ExamTopics_Community_Pool_154Q.md"
        VAULT_JSON="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/AIF_C01_ExamTopics_Community_Pool_154Q.json"
        VAULT_MD="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/AIF_C01_ExamTopics_Community_Pool_154Q.md"
        ;;
    SAA-C03)
        WORK_JSON="${WORK_REPO}/Cloud/Associate/SAA-C03/revision_questions/SAA_C03_ExamTopics_Community_Pool_1019Q.json"
        WORK_MD="${WORK_REPO}/Cloud/Associate/SAA-C03/revision_questions/SAA_C03_ExamTopics_Community_Pool_1019Q.md"
        VAULT_JSON="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/SAA_C03_ExamTopics_Community_Pool_1019Q.json"
        VAULT_MD="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/SAA_C03_ExamTopics_Community_Pool_1019Q.md"
        ;;
    MLA-C01)
        WORK_JSON="${WORK_REPO}/AI/Associate/MLA-C01/revision_questions/MLA_C01_ExamTopics_Community_Pool_106Q.json"
        WORK_MD="${WORK_REPO}/AI/Associate/MLA-C01/revision_questions/MLA_C01_ExamTopics_Community_Pool_106Q.md"
        VAULT_JSON="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/MLA_C01_ExamTopics_Community_Pool_106Q.json"
        VAULT_MD="${VAULT_BASE}/Questions_Bank/ExamTopics_Questions/MLA_C01_ExamTopics_Community_Pool_106Q.md"
        ;;
    *)
        echo "Error: Unsupported exam ${EXAM}."
        exit 1
        ;;
esac

if [[ "${MODE}" == "live" ]]; then
    OUTPUT_RAW="${WORK_REPO}/downloads/raw/${EXAM,,}-live.json"
    mkdir -p "$(dirname "${OUTPUT_RAW}")"
    echo "🐳 Invoking Docker container for live download..."
    DOCKER_ARGS=(
        run --rm
        -v "${WORK_REPO}/downloads/raw:/data"
        ghcr.io/thatonecodes/examtopics-downloader:latest
        -p amazon -s "${EXAM,,}" -type json -c -save-links -o "/data/${EXAM,,}-live.json"
    )
    if [[ -n "${GH_TOKEN}" ]]; then
        DOCKER_ARGS+=(-t "${GH_TOKEN}")
    fi
    docker "${DOCKER_ARGS[@]}"
    
    echo "🔄 Ingesting and sanitizing live download output..."
    python3 "${SCRIPT_DIR}/ingest_examtopics_downloader.py" \
        --raw "${OUTPUT_RAW}.json" \
        --exam "${EXAM}" \
        --work-json "${WORK_JSON}" \
        --work-md "${WORK_MD}" \
        --vault-json "${VAULT_JSON}" \
        --vault-md "${VAULT_MD}"
else
    if [[ ! -d "${RAW_CACHE_DIR}" ]]; then
        echo "📥 Initializing local dataset cache from GitHub..."
        mkdir -p "${WORK_REPO}/downloads"
        git clone --depth 1 https://github.com/thatonecodes/examtopics-data.git "${WORK_REPO}/downloads/examtopics-data"
    fi
    
    echo "⚙️ Processing and standardizing cached dataset..."
    python3 "${SCRIPT_DIR}/ingest_examtopics_downloader.py" \
        --chunks-dir "${RAW_CACHE_DIR}" \
        --exam "${EXAM}" \
        --work-json "${WORK_JSON}" \
        --work-md "${WORK_MD}" \
        --vault-json "${VAULT_JSON}" \
        --vault-md "${VAULT_MD}"
fi

echo "✅ Successfully synced ${EXAM} question pool to Work repo & Obsidian Vault!"
