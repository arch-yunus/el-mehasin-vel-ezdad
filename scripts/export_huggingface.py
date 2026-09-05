#!/usr/bin/env python3
"""
Exporter script to format the dialectic corpus for Hugging Face datasets.
Exports structured pairs into tabular/JSON format ready for push_to_hub or HF datasets loader.
"""
import os
import json

def export_dataset(input_jsonl="data/dialectic_pairs.jsonl", output_json="data/hf_dataset_export.json"):
    print("Exporting dialectic pairs to Hugging Face dataset format...")
    if not os.path.exists(input_jsonl):
        print(f"Error: {input_jsonl} not found.")
        return False
    
    rows = []
    with open(input_jsonl, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line.strip())
                flattened = {
                    "id": item["entry_id"],
                    "topic": item["topic_slug"],
                    "arabic_title": item["classical_arabic_title"],
                    "thesis_concept": item["thesis"]["concept"],
                    "thesis_premise": item["thesis"]["core_premise"],
                    "thesis_quote_ar": item["thesis"]["top_quote"]["arabic"],
                    "thesis_quote_tr": item["thesis"]["top_quote"]["turkish"],
                    "antithesis_concept": item["antithesis"]["concept"],
                    "antithesis_premise": item["antithesis"]["core_premise"],
                    "antithesis_quote_ar": item["antithesis"]["top_quote"]["arabic"],
                    "antithesis_quote_tr": item["antithesis"]["top_quote"]["turkish"],
                    "synthesis": item["dialectic_synthesis"],
                    "rhetorical_devices": ", ".join(item["metadata"].get("rhetorical_devices", []))
                }
                rows.append(flattened)
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully exported {len(rows)} records to {output_json}")
    return True

if __name__ == "__main__":
    export_dataset()
