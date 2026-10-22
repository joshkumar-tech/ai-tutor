"""
Database and progress tracking module using SQLite and SQLAlchemy.
Manages roadmap progress, quiz scores, dataset imports, training checkpoints, and chat history.
"""

import sqlite3
from pathlib import Path
import json
from datetime import datetime
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
import config

def get_connection():
    """Get SQLite database connection."""
    config.ensure_directories()
    conn = sqlite3.connect(str(config.DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables and handle column migrations."""
    conn = get_connection()
    cursor = conn.cursor()

    # Roadmap progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roadmap_progress (
            week_number INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            month_label TEXT,
            status TEXT DEFAULT 'upcoming',
            notes TEXT,
            completed_at TEXT
        )
    """)

    # Ensure month_label column exists if table was already created without it
    try:
        cursor.execute("ALTER TABLE roadmap_progress ADD COLUMN month_label TEXT")
    except sqlite3.OperationalError:
        pass # Column already exists

    # PDF documents index table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            title TEXT,
            total_pages INTEGER,
            imported_at TEXT
        )
    """)

    # PDF text chunks for search
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS document_chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER,
            page_number INTEGER,
            chunk_text TEXT,
            FOREIGN KEY (document_id) REFERENCES documents(id)
        )
    """)

    # Datasets metadata table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_number INTEGER,
            topic TEXT,
            filename TEXT,
            valid_examples INTEGER,
            invalid_examples INTEGER,
            imported_at TEXT
        )
    """)

    # Training runs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS training_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_name TEXT,
            epochs INTEGER,
            final_loss REAL,
            checkpoint_path TEXT,
            dataset_info TEXT,
            completed_at TEXT
        )
    """)

    # Quiz scores table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_number INTEGER,
            score REAL,
            total_questions INTEGER,
            taken_at TEXT
        )
    """)

    # ChatGPT-like Chat History table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            sources TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("[OK] Database initialized successfully.")
