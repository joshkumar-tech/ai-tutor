"""
Dataset management and validation module for JSONL weekly training data.
"""

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
import config
from src.progress.db import get_connection

def validate_dataset(file_path: str):
    """
    Validate a JSONL dataset file.
    Checks that each line is valid JSON and contains required fields (role, content).
    Returns (valid_count, invalid_count, errors_list).
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    valid_count = 0
    invalid_count = 0
    errors = []

    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                if not isinstance(record, dict):
                    invalid_count += 1
                    errors.append(f"Line {line_num}: Not a JSON object")
                    continue

                if "role" not in record or "content" not in record:
                    invalid_count += 1
                    errors.append(f"Line {line_num}: Missing 'role' or 'content' field")
                    continue

                valid_count += 1
            except json.JSONDecodeError as e:
                invalid_count += 1
                errors.append(f"Line {line_num}: Invalid JSON ({e})")

    return valid_count, invalid_count, errors

def import_dataset(file_path: str, week_number: int, topic: str):
    """Validate and import a dataset into the project datasets directory and DB."""
    valid_count, invalid_count, errors = validate_dataset(file_path)
    if valid_count == 0:
        raise ValueError(f"Dataset validation failed: 0 valid examples found. Errors: {errors[:5]}")

    # Ensure week directory exists
    week_dir = config.DATASETS_DIR / f"week_{week_number:02d}"
    week_dir.mkdir(parents=True, exist_ok=True)

    src_path = Path(file_path)
    dest_path = week_dir / "dataset.jsonl"

    with open(src_path, "r", encoding="utf-8") as src, open(dest_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())

    # Record in database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets (week_number, topic, filename, valid_examples, invalid_examples, imported_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (week_number, topic, src_path.name, valid_count, invalid_count))
    conn.commit()
    conn.close()

    return valid_count, invalid_count

def get_imported_datasets():
    """Get all imported datasets from DB."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, week_number, topic, filename, valid_examples, invalid_examples, imported_at FROM datasets ORDER BY week_number ASC")
    datasets = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return datasets
