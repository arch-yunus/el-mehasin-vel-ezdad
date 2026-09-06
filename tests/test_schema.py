import unittest
import json
import jsonschema

class TestSchemaValidation(unittest.TestCase):
    def test_all_pairs_against_schema(self):
        with open("schemas/dialectic_entry.schema.json", "r", encoding="utf-8") as f:
            schema = json.load(f)

        with open("data/dialectic_pairs.jsonl", "r", encoding="utf-8") as f:
            for idx, line in enumerate(f, 1):
                if line.strip():
                    item = json.loads(line)
                    try:
                        jsonschema.validate(instance=item, schema=schema)
                    except jsonschema.ValidationError as e:
                        self.fail(f"Validation failed on line {idx}: {e.message}")

if __name__ == "__main__":
    unittest.main()
