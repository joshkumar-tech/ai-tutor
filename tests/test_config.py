"""
Tests for configuration and basic setup.
"""

import pytest
from pathlib import Path
import sys

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

import config


def test_project_root_exists():
    """Test that project root is correctly identified."""
    assert config.PROJECT_ROOT.exists()
    assert config.PROJECT_ROOT.is_dir()


def test_directory_creation():
    """Test that ensure_directories creates all required directories."""
    config.ensure_directories()

    assert config.DATA_DIR.exists()
    assert config.DOCUMENTS_DIR.exists()
    assert config.DATASETS_DIR.exists()
    assert config.CHECKPOINTS_DIR.exists()


def test_gitkeep_files():
    """Test that .gitkeep files are created in directories."""
    config.ensure_directories()

    assert (config.DATA_DIR / ".gitkeep").exists()
    assert (config.DOCUMENTS_DIR / ".gitkeep").exists()
    assert (config.DATASETS_DIR / ".gitkeep").exists()
    assert (config.CHECKPOINTS_DIR / ".gitkeep").exists()


def test_model_config_has_required_keys():
    """Test that model configuration contains all required parameters."""
    required_keys = [
        "vocab_size",
        "embedding_dim",
        "hidden_dim",
        "num_layers",
        "num_heads",
        "dropout",
        "max_seq_length",
    ]

    for key in required_keys:
        assert key in config.MODEL_CONFIG, f"Missing key: {key}"


def test_training_config_has_required_keys():
    """Test that training configuration contains all required parameters."""
    required_keys = [
        "batch_size",
        "learning_rate",
        "num_epochs",
    ]

    for key in required_keys:
        assert key in config.TRAINING_CONFIG, f"Missing key: {key}"


def test_app_config_has_required_keys():
    """Test that app configuration contains all required parameters."""
    required_keys = [
        "page_title",
        "page_icon",
        "layout",
        "initial_sidebar_state",
    ]

    for key in required_keys:
        assert key in config.APP_CONFIG, f"Missing key: {key}"


def test_database_path_in_data_dir():
    """Test that database path is inside data directory."""
    assert config.DATABASE_PATH.parent == config.DATA_DIR


def test_config_values_are_reasonable():
    """Test that configuration values are within reasonable ranges."""
    # Model config
    assert config.MODEL_CONFIG["vocab_size"] > 0
    assert config.MODEL_CONFIG["embedding_dim"] > 0
    assert config.MODEL_CONFIG["hidden_dim"] > 0
    assert config.MODEL_CONFIG["num_layers"] > 0
    assert 0 <= config.MODEL_CONFIG["dropout"] < 1

    # Training config
    assert config.TRAINING_CONFIG["batch_size"] > 0
    assert config.TRAINING_CONFIG["learning_rate"] > 0
    assert config.TRAINING_CONFIG["num_epochs"] > 0

    # PDF config
    assert config.PDF_CONFIG["chunk_size"] > 0
    assert config.PDF_CONFIG["max_results"] > 0


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
