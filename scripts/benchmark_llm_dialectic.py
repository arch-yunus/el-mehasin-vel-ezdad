#!/usr/bin/env python3
"""
Benchmark framework to evaluate LLM ability to generate balanced classical Arabic
thesis and antithesis dialectic arguments according to al-Mahasin wa-al-Addad standards.
"""
import json
import os

def load_benchmark_prompts():
    data_path = "data/dialectic_pairs.jsonl"
    with open(data_path, "r", encoding="utf-8") as f:
        pairs = [json.loads(l) for l in f if l.strip()]

    prompts = []
    for p in pairs:
        prompts.append({
            "id": p["entry_id"],
            "topic": p["topic_slug"],
            "prompt_thesis": f"Savun: {p['thesis']['concept']}. Klasik belagat ve edebi delillerle tezi açıkla.",
            "prompt_antithesis": f"Savun: {p['antithesis']['concept']}. Karşıt tezi ve bağlamsal itirazı açıkla.",
            "reference_synthesis": p["dialectic_synthesis"]
        })
    print(f"Generated {len(prompts)} dialectic benchmark prompts.")
    return prompts

if __name__ == "__main__":
    load_benchmark_prompts()
