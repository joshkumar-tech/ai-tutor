"""
Basic tests for the main application.
"""

import pytest
from pathlib import Path
import sys

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))


def test_app_module_imports():
    """Test that the main app module can be imported."""
    import app
    assert hasattr(app, "main")


def test_config_module_imports():
    """Test that config module can be imported."""
    import config
    assert hasattr(config, "PROJECT_ROOT")
    assert hasattr(config, "ensure_directories")


def test_app_has_page_functions():
    """Test that all page display functions exist."""
    import app

    page_functions = [
        "show_home_page",
        "show_roadmap_page",
        "show_pdf_page",
        "show_tutor_page",
        "show_datasets_page",
        "show_training_page",
        "show_progress_page",
        "show_settings_page",
    ]

    for func_name in page_functions:
        assert hasattr(app, func_name), f"Missing function: {func_name}"


def test_python_syntax_check():
    """Test that Python files have valid syntax."""
    import py_compile

    files_to_check = [
        PROJECT_ROOT / "app.py",
        PROJECT_ROOT / "config.py",
    ]

    for file_path in files_to_check:
        try:
            py_compile.compile(str(file_path), doraise=True)
        except py_compile.PyCompileError as e:
            pytest.fail(f"Syntax error in {file_path}: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
