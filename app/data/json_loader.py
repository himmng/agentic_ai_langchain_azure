import json
from pathlib import Path

def load_json(filepath: str):
    with open(Path(filepath), "r", encoding="utf-8") as f:
        return json.load(f)
