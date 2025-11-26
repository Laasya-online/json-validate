# json-validate (GitHub Action)

Validate a JSON file against a JSON Schema (draft 2020-12).

## Usage
```yaml
- name: Validate result.json
  uses: laasya-online/json-validate@v1
  with:
    json_path: artifacts/result.json
    schema_path: schema/result.schema.json
