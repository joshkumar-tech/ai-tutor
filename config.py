"""
Configuration settings for AI Tutor application.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
DOCUMENTS_DIR = PROJECT_ROOT / "documents"
DATASETS_DIR = PROJECT_ROOT / "datasets"
CHECKPOINTS_DIR = PROJECT_ROOT / "checkpoints"

# Database
DATABASE_PATH = DATA_DIR / "progress.db"

# Model configuration
MODEL_CONFIG = {
    "vocab_size": 8000,  # Small vocabulary for educational purposes
    "embedding_dim": 256,
    "hidden_dim": 512,
    "num_layers": 4,
    "num_heads": 8,
    "dropout": 0.1,
    "max_seq_length": 512,
}

# Training configuration
TRAINING_CONFIG = {
    "batch_size": 8,
    "learning_rate": 0.0001,
    "num_epochs": 10,
    "gradient_accumulation_steps": 4,
    "warmup_steps": 100,
    "checkpoint_every": 500,
    "eval_every": 100,
}

# PDF processing
PDF_CONFIG = {
    "chunk_size": 500,  # Characters per chunk
    "chunk_overlap": 50,  # Overlap between chunks
    "max_results": 5,  # Number of search results to return
}

# Roadmap
ROADMAP_CONFIG = {
    "total_weeks": 52,  # 12 months = ~52 weeks
    "start_date": "2026-11-01",
}

# Application
APP_CONFIG = {
    "page_title": "AI Tutor",
    "page_icon": "🎓",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

def ensure_directories():
    """Create necessary directories if they don't exist."""
    directories = [DATA_DIR, DOCUMENTS_DIR, DATASETS_DIR, CHECKPOINTS_DIR]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

        # Create .gitkeep files to preserve empty directories
        gitkeep = directory / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

if __name__ == "__main__":
    # Test configuration
    print("AI Tutor Configuration")
    print("=" * 50)
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Data Directory: {DATA_DIR}")
    print(f"Documents Directory: {DOCUMENTS_DIR}")
    print(f"Datasets Directory: {DATASETS_DIR}")
    print(f"Checkpoints Directory: {CHECKPOINTS_DIR}")
    print(f"Database Path: {DATABASE_PATH}")
    print("\nEnsuring directories exist...")
    ensure_directories()
    print("[OK] All directories created successfully")
