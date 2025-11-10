import csv
from pathlib import Path
from typing import List, Dict

def export_csv(rows: List[Dict], out_path: str = "reports/results.csv"):
    Path("reports").mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    keys = list(rows[0].keys())
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    return out_path
