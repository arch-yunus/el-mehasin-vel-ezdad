#!/usr/bin/env python3
"""
Data validator for el-mehasin-vel-ezdad dialectic corpus.
Validates schemas, JSONL records, and corpus integrity.
"""
import os
import sys
import json

# Ensure utf-8 stdout on all platforms
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def validate_repository():
    print("========================================")
    print("[*] Running Dialectic Corpus Validator...")
    print("========================================")
    
    schema_path = "schemas/dialectic_entry.schema.json"
    data_path = "data/dialectic_pairs.jsonl"
    taxonomy_path = "data/taxonomy_ontology.json"
    
    errors = []
    
    # 1. Check Schema existence
    if not os.path.exists(schema_path):
        errors.append(f"Missing schema file: {schema_path}")
    else:
        with open(schema_path, "r", encoding="utf-8") as f:
            try:
                schema = json.load(f)
                print(f"[+] Schema loaded successfully: {schema_path}")
            except Exception as e:
                errors.append(f"Failed to parse schema JSON: {e}")
                schema = None

    # 2. Check and validate dialectic_pairs.jsonl
    if not os.path.exists(data_path):
        errors.append(f"Missing data file: {data_path}")
    else:
        try:
            import jsonschema
            has_jsonschema = True
        except ImportError:
            has_jsonschema = False
            print("[!] jsonschema module not installed; performing manual structural validation.")
        
        pair_count = 0
        with open(data_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                pair_count += 1
                try:
                    record = json.loads(line)
                except Exception as e:
                    errors.append(f"Line {idx} in {data_path} is invalid JSON: {e}")
                    continue
                
                # Check required fields
                required_fields = ["entry_id", "topic_slug", "classical_arabic_title", "thesis", "antithesis", "dialectic_synthesis", "metadata"]
                for rf in required_fields:
                    if rf not in record:
                        errors.append(f"Line {idx} ({record.get('entry_id', 'unknown')}): missing required field '{rf}'")
                
                if has_jsonschema and schema:
                    try:
                        jsonschema.validate(instance=record, schema=schema)
                    except jsonschema.ValidationError as ve:
                        errors.append(f"Line {idx} validation error: {ve.message}")
        
        print(f"[+] Verified {pair_count} dialectic pair records in {data_path}")

    # 3. Check taxonomy ontology
    if not os.path.exists(taxonomy_path):
        errors.append(f"Missing taxonomy ontology: {taxonomy_path}")
    else:
        with open(taxonomy_path, "r", encoding="utf-8") as f:
            try:
                ont = json.load(f)
                cat_count = len(ont.get("categories", []))
                print(f"[+] Taxonomy ontology verified ({cat_count} categories)")
            except Exception as e:
                errors.append(f"Invalid taxonomy JSON: {e}")

    # 4. Check corpus files
    corpus_dirs = ["corpus/arabic_raw", "corpus/turkish_annotated", "corpus/english_reference"]
    for cd in corpus_dirs:
        if not os.path.exists(cd):
            errors.append(f"Corpus directory missing: {cd}")
        else:
            files = [f for f in os.listdir(cd) if os.path.isfile(os.path.join(cd, f))]
            print(f"[+] Directory {cd} contains {len(files)} files")

    print("----------------------------------------")
    if errors:
        print(f"[-] Validation FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("[SUCCESS] ALL VALIDATION CHECKS PASSED SUCCESSFULLY!")
        sys.exit(0)

if __name__ == "__main__":
    validate_repository()
