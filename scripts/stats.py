#!/usr/bin/env python3
"""
Generates detailed lexical and rhetorical statistics for el-mehasin-vel-ezdad.
"""
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def generate_stats():
    data_path = "data/dialectic_pairs.jsonl"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    pairs = []
    with open(data_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                pairs.append(json.loads(line))

    total_arabic_chars = 0
    total_turkish_chars = 0
    total_quotes = 0
    devices = {}

    for p in pairs:
        t_ar = p["thesis"]["top_quote"]["arabic"]
        t_tr = p["thesis"]["top_quote"]["turkish"]
        a_ar = p["antithesis"]["top_quote"]["arabic"]
        a_tr = p["antithesis"]["top_quote"]["turkish"]

        total_arabic_chars += len(t_ar) + len(a_ar)
        total_turkish_chars += len(t_tr) + len(a_tr)
        total_quotes += 2

        for q in p["thesis"].get("additional_quotes", []):
            total_arabic_chars += len(q.get("arabic", ""))
            total_turkish_chars += len(q.get("turkish", ""))
            total_quotes += 1

        for q in p["antithesis"].get("additional_quotes", []):
            total_arabic_chars += len(q.get("arabic", ""))
            total_turkish_chars += len(q.get("turkish", ""))
            total_quotes += 1

        for d in p.get("metadata", {}).get("rhetorical_devices", []):
            devices[d] = devices.get(d, 0) + 1

    print("========================================")
    print("  [*] DIALECTIC CORPUS DETAILED METRICS")
    print("========================================")
    print(f"Total Dialectic Entries      : {len(pairs)}")
    print(f"Total Opposing Poles         : {len(pairs) * 2}")
    print(f"Total Poetic & Prosaic Quotes: {total_quotes}")
    print(f"Total Arabic Text Volume     : {total_arabic_chars} characters")
    print(f"Total Turkish Text Volume    : {total_turkish_chars} characters")
    print("----------------------------------------")
    print("Rhetorical Figures Frequency:")
    for dev, c in sorted(devices.items(), key=lambda x: -x[1]):
        bar = "#" * c
        print(f"  {dev: <20} | {c:02d} {bar}")
    print("========================================")

if __name__ == "__main__":
    generate_stats()
