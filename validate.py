import sys, json, argparse, pathlib
from jsonschema import Draft202012Validator

def main():
    ap = argparse.ArgumentParser(description="Validate JSON against a JSON Schema.")
    ap.add_argument("json_path")
    ap.add_argument("schema_path")
    args = ap.parse_args()

    jp = pathlib.Path(args.json_path)
    sp = pathlib.Path(args.schema_path)
    if not jp.exists():
        print(f"❌ JSON file not found: {jp}", file=sys.stderr)
        sys.exit(1)
    if not sp.exists():
        print(f"❌ Schema file not found: {sp}", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(jp.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"❌ Failed to read/parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        schema = json.loads(sp.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"❌ Failed to read/parse Schema: {e}", file=sys.stderr)
        sys.exit(1)

    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        print("❌ Validation failed:")
        for e in errors:
            loc = ".".join(map(str, e.path)) or "(root)"
            print(f"- {loc}: {e.message}")
        sys.exit(1)

    print("✅ JSON validates against schema.")

if __name__ == "__main__":
    main()
