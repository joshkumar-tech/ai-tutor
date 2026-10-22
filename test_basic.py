"""
Simple test to verify Python environment and imports work.
Run this before installing heavy dependencies.
"""

import sys
import sqlite3
from pathlib import Path

def test_python_version():
    """Check Python version."""
    print(f"Python version: {sys.version}")
    assert sys.version_info >= (3, 10), "Python 3.10+ required"
    print("[OK] Python version OK")

def test_sqlite():
    """Check SQLite is available."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version()")
    version = cursor.fetchone()[0]
    print(f"SQLite version: {version}")
    conn.close()
    print("[OK] SQLite OK")

def test_pathlib():
    """Check pathlib works."""
    p = Path(".")
    assert p.exists()
    print(f"Current directory: {p.absolute()}")
    print("[OK] Pathlib OK")

def test_project_structure():
    """Check project files exist."""
    expected_files = [
        "config.py",
        "app.py",
        "README.md",
        "requirements.txt",
    ]

    missing = []
    for file in expected_files:
        if not Path(file).exists():
            missing.append(file)

    if missing:
        print(f"[WARN] Missing files: {missing}")
    else:
        print("[OK] All core files present")

    return len(missing) == 0

def main():
    """Run all basic tests."""
    print("=" * 50)
    print("Basic Environment Test")
    print("=" * 50)

    try:
        test_python_version()
        test_sqlite()
        test_pathlib()
        test_project_structure()

        print("=" * 50)
        print("[SUCCESS] All basic tests passed!")
        print("=" * 50)
        return 0
    except Exception as e:
        print("=" * 50)
        print(f"[ERROR] Test failed: {e}")
        print("=" * 50)
        return 1

if __name__ == "__main__":
    sys.exit(main())
