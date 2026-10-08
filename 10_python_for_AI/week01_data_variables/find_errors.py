"""Find all code cells in 01-data_variables.ipynb that have error outputs."""

import json

NB_PATH = r"e:\PYTHON_MASTERY_PORTFOLIO\10_python_for_AI\week_01_data_variables\01-data_variables.ipynb"

with open(NB_PATH, "r", encoding="utf-8") as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
print("=" * 70)

for idx, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "code":
        continue
    src = "".join(cell.get("source", []))
    if not src.strip():
        continue
    for out in cell.get("outputs", []):
        if out.get("output_type") == "error":
            src_short = src.replace("\n", " | ")[:100]
            print(f"CELL #{idx}  --  {out.get('ename')}: {out.get('evalue', '')[:60]}")
            print(f"  source: {src_short}")
            print("-" * 70)
            break

