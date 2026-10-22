"""
Automatic Roadmap Generator from uploaded PDF documents.
Analyzes extracted PDF text and extracts structured learning milestones/weeks.
"""

import sys
from pathlib import Path
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
from src.progress.db import get_connection

def generate_roadmap_from_pdf(pdf_path: str):
    """
    Read an uploaded PDF curriculum or syllabus, extract text,
    and generate a custom multi-week roadmap stored in SQLite.
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = PdfReader(str(path))
    extracted_lines = []

    for page in reader.pages:
        text = page.extract_text() or ""
        for line in text.split("\n"):
            line = line.strip()
            if len(line) > 5 and not line.isdigit():
                extracted_lines.append(line)

    # Filter/sample lines to create structured learning weeks (up to 20-30 weeks or more)
    milestones = []
    step = max(1, len(extracted_lines) // 24) # Aim for ~24 weeks of custom curriculum

    for i in range(0, min(len(extracted_lines), 24 * step), step):
        topic_text = extracted_lines[i][:80]
        milestones.append(topic_text)

    if not milestones:
        milestones = ["Introduction and Fundamentals", "Core Concepts & Analysis", "Advanced Implementation", "Capstone Project"]

    # Save to SQLite roadmap_progress table (replacing or augmenting)
    conn = get_connection()
    cursor = conn.cursor()

    # Clear old roadmap or add custom generated ones
    cursor.execute("DELETE FROM roadmap_progress")

    generated_weeks = []
    for idx, topic in enumerate(milestones, 1):
        month_label = f"Custom Month {(idx - 1) // 4 + 1}: From PDF ({path.name})"
        title = f"{topic}"
        cursor.execute("""
            INSERT INTO roadmap_progress (week_number, title, month_label, status, notes)
            VALUES (?, ?, ?, 'upcoming', ?)
        """, (idx, title, month_label, f"Auto-generated from uploaded PDF: {path.name}"))
        generated_weeks.append((idx, title, month_label))

    conn.commit()
    conn.close()

    return generated_weeks
