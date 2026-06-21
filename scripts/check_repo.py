from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "SECURITY.md",
    "requirements.txt",
    "docs/results-summary.md",
    "docs/reproduction-notes.md",
    "data/weather_sample_data.csv",
    "notebooks/mqtt_adversarial_ml_reproduction.ipynb",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"\ba\d{7}\b", re.IGNORECASE),
    re.compile(r"Submission\s+" + "ID", re.IGNORECASE),
    re.compile("Turn" + "itin", re.IGNORECASE),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"  - {path}")
        return 1

    notebook_path = ROOT / "notebooks" / "mqtt_adversarial_ml_reproduction.ipynb"
    notebook = json.loads(read_text(notebook_path))
    if not notebook.get("cells"):
        print("Notebook has no cells")
        return 1

    text_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".md", ".txt", ".py", ".ipynb", ".csv"}
        and ".git" not in path.parts
    ]
    for path in text_files:
        content = read_text(path)
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(content):
                print(f"Forbidden private/course marker found in {path.relative_to(ROOT)}")
                return 1

    readme = read_text(ROOT / "README.md")
    expected_phrases = [
        "anomaly-detection evaluation",
        "attribution",
        "defensive security research",
    ]
    for phrase in expected_phrases:
        if phrase.lower() not in readme.lower():
            print(f"README is missing expected phrase: {phrase}")
            return 1

    print("Repository hygiene check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
