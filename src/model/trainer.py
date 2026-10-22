"""
Model training and checkpoint management module for the custom educational AI model.
"""

import json
from pathlib import Path
import sys
import time

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
import config
from src.progress.db import get_connection

def simulate_training_run(run_name: str, epochs: int, dataset_week: int):
    """
    Simulate a training run (or run lightweight training) on the specified dataset week.
    Saves a model checkpoint file and logs metrics to SQLite.
    """
    config.ensure_directories()

    # Check if dataset exists for this week
    dataset_path = config.DATASETS_DIR / f"week_{dataset_week:02d}" / "dataset.jsonl"
    if not dataset_path.exists():
        raise FileNotFoundError(f"No dataset found for week {dataset_week} at {dataset_path}")

    # Simulate training epochs with decreasing loss
    loss = 2.5
    for epoch in range(1, epochs + 1):
        loss = max(0.1, loss * 0.85 - 0.05)
        time.sleep(0.1) # Simulate training step

    # Save checkpoint file
    checkpoint_filename = f"checkpoint_{run_name}_week{dataset_week:02d}.pt"
    checkpoint_path = config.CHECKPOINTS_DIR / checkpoint_filename

    checkpoint_data = {
        "run_name": run_name,
        "epochs": epochs,
        "dataset_week": dataset_week,
        "final_loss": round(loss, 4),
        "model_config": config.MODEL_CONFIG,
        "training_config": config.TRAINING_CONFIG,
    }

    with open(checkpoint_path, "w", encoding="utf-8") as f:
        json.dump(checkpoint_data, f, indent=2)

    # Log training run to database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO training_runs (run_name, epochs, final_loss, checkpoint_path, dataset_info, completed_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (run_name, epochs, round(loss, 4), str(checkpoint_path), f"Week {dataset_week} Dataset"))
    conn.commit()
    conn.close()

    return {
        "run_name": run_name,
        "epochs": epochs,
        "final_loss": round(loss, 4),
        "checkpoint_path": str(checkpoint_path)
    }

def get_training_runs():
    """Get all completed training runs from database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, run_name, epochs, final_loss, checkpoint_path, dataset_info, completed_at FROM training_runs ORDER BY completed_at DESC")
    runs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return runs

def get_checkpoints():
    """List all saved model checkpoints."""
    config.ensure_directories()
    checkpoints = []
    for cp_path in config.CHECKPOINTS_DIR.glob("*.pt"):
        try:
            with open(cp_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                checkpoints.append(data)
        except Exception:
            checkpoints.append({"run_name": cp_path.stem, "checkpoint_path": str(cp_path)})
    return checkpoints
