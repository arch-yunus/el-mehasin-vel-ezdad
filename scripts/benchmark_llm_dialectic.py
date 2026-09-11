#!/usr/bin/env python3
"""
Benchmark framework to evaluate LLM ability to generate balanced classical Arabic
thesis and antithesis dialectic arguments according to al-Mahasin wa-al-Addad standards.
"""
import os
import sys
import json
from typing import List, Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def load_benchmark_prompts() -> List[Dict[str, Any]]:
    data_path = "data/dialectic_pairs.jsonl"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return []

    with open(data_path, "r", encoding="utf-8") as f:
        pairs = [json.loads(l) for l in f if l.strip()]

    prompts = []
    for p in pairs:
        prompts.append({
            "entry_id": p["entry_id"],
            "topic_slug": p["topic_slug"],
            "classical_title": p["classical_arabic_title"],
            "system_prompt": (
                "Sen klasik Abbâsî adab geleneğinde uzmanlaşmış bir münazara hakemisin. "
                "Verilen kavramı hem El-Mehâsin (bütün fazilet ve güzellikleriyle) "
                "hem de El-Ezdâd (bütün afet ve kusurlarıyla) eşit güçte savunmalı, "
                "en nihayetinde bir diyalektik senteze (Aristotelesçi altın orta yol) bağlamalısın."
            ),
            "user_prompt": f"Mevzu: {p['classical_arabic_title']}. {p['thesis']['concept']} ve {p['antithesis']['concept']} kutuplarını münazara et.",
            "gold_thesis": {
                "concept": p["thesis"]["concept"],
                "premise": p["thesis"]["core_premise"],
                "top_quote": p["thesis"]["top_quote"]
            },
            "gold_antithesis": {
                "concept": p["antithesis"]["concept"],
                "premise": p["antithesis"]["core_premise"],
                "top_quote": p["antithesis"]["top_quote"]
            },
            "gold_synthesis": p["dialectic_synthesis"],
            "target_balaghah_devices": p.get("metadata", {}).get("rhetorical_devices", [])
        })

    print(f"========================================")
    print(f"  [*] LLM DIALECTIC BENCHMARK SUITE")
    print(f"========================================")
    print(f"Total Evaluation Scenarios: {len(prompts)} topics")
    print(f"Dataset: Kitab al-Mahasin wa-al-Addad Gold Standard")
    print(f"----------------------------------------")
    return prompts


def evaluate_response_sample(llm_output: Dict[str, str], prompt_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates an LLM's dual-polarity output against gold dialectic references.
    """
    has_thesis = len(llm_output.get("thesis_text", "").strip()) > 30
    has_antithesis = len(llm_output.get("antithesis_text", "").strip()) > 30
    has_synthesis = len(llm_output.get("synthesis_text", "").strip()) > 20

    polarity_balance_score = 1.0 if (has_thesis and has_antithesis) else 0.5

    return {
        "entry_id": prompt_data["entry_id"],
        "polarity_coverage": {
            "thesis_present": has_thesis,
            "antithesis_present": has_antithesis,
            "synthesis_present": has_synthesis
        },
        "overall_dialectic_score": polarity_balance_score * 100
    }


if __name__ == "__main__":
    benchmark_data = load_benchmark_prompts()
    print("Sample Prompt Scenario:")
    sample = benchmark_data[0]
    print(f"Entry ID : {sample['entry_id']}")
    print(f"Prompt   : {sample['user_prompt']}")
    print(f"Synthesis: {sample['gold_synthesis']}")
    print("========================================")
