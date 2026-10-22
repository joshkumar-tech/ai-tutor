"""
PDF document processing and local search module using pypdf and SQLite.
"""

import os
from pathlib import Path
import sys
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
import config
from src.progress.db import get_connection

def import_pdf(file_path: str, title: str = None) -> int:
    """Import a PDF document, extract text page by page, and index into SQLite."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    # Copy to documents directory if not already there
    dest_path = config.DOCUMENTS_DIR / path.name
    if path.resolve() != dest_path.resolve():
        with open(path, "rb") as src, open(dest_path, "wb") as dst:
            dst.write(src.read())

    reader = PdfReader(str(dest_path))
    total_pages = len(reader.pages)
    doc_title = title or path.stem

    conn = get_connection()
    cursor = conn.cursor()

    # Insert document record
    cursor.execute("""
        INSERT INTO documents (filename, title, total_pages, imported_at)
        VALUES (?, ?, ?, datetime('now'))
    """, (path.name, doc_title, total_pages))
    doc_id = cursor.lastrowid

    # Extract and chunk text per page
    for page_num in range(total_pages):
        page = reader.pages[page_num]
        text = page.extract_text() or ""
        if text.strip():
            cursor.execute("""
                INSERT INTO document_chunks (document_id, page_number, chunk_text)
                VALUES (?, ?, ?)
            """, (doc_id, page_num + 1, text))

    conn.commit()
    conn.close()
    return doc_id

def search_documents(query: str = "", max_results: int = 5):
    """Search imported PDF chunks for matching keywords."""
    conn = get_connection()
    cursor = conn.cursor()

    query_str = f"%{query}%"
    cursor.execute("""
        SELECT D.filename, D.title, C.page_number, C.chunk_text
        FROM document_chunks C
        JOIN documents D ON C.document_id = D.id
        WHERE C.chunk_text LIKE ?
        LIMIT ?
    """, (query_str, max_results))

    results = []
    for row in cursor.fetchall():
        results.append({
            "filename": row["filename"],
            "title": row["title"],
            "page_number": row["page_number"],
            "snippet": row["chunk_text"][:300] + "..." if len(row["chunk_text"]) > 300 else row["chunk_text"]
        })

    conn.close()
    return results

def get_imported_documents():
    """List all imported PDF documents."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, filename, title, total_pages, imported_at FROM documents ORDER BY imported_at DESC")
    docs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return docs
