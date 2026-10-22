"""
Teaching assistant module providing beginner-friendly explanations, quizzes, and RAG-based answers with ChatGPT-like chat history.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
from src.pdf_handler.handler import search_documents
from src.progress.db import get_connection

def save_chat_message(role: str, content: str, sources: str = None):
    """Save a chat message to SQLite database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO chat_messages (role, content, sources, created_at)
        VALUES (?, ?, ?, datetime('now'))
    """, (role, content, sources))
    conn.commit()
    conn.close()

def get_chat_history():
    """Retrieve all chat messages."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role, content, sources, created_at FROM chat_messages ORDER BY id ASC")
    messages = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return messages

def clear_chat_history():
    """Clear chat history."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_messages")
    conn.commit()
    conn.close()

def ask_tutor(question: str, week_number: int = None):
    """
    Answer a user question using imported PDF documents (RAG)
    and pedagogical AI tutor knowledge, saving the interaction to chat history.
    """
    search_results = search_documents(query=question, max_results=3)

    response_parts = []

    if search_results:
        response_parts.append("### 📄 Relevant Notes from Your PDF Library:\n")
        for res in search_results:
            response_parts.append(f"> **{res['title']}** (Page {res['page_number']})\n> {res['snippet']}\n")
        response_parts.append("\n--- \n")

    response_parts.append(f"### 🎓 AI Tutor Explanation:\n")
    response_parts.append(f"Here is a clear, step-by-step breakdown of your question: *\"{question}\"*\n")

    q_lower = question.lower()
    if "python" in q_lower or "variable" in q_lower:
        response_parts.append("""
1. **Core Concept**: In programming, we store information in **variables**. Think of a variable as a labeled box where you put a value.
2. **Analogy**: Imagine a shoebox with a label that says `age`. Inside the box, you place the number `25`.
3. **Example Code**:
```python
age = 25
name = "Alice"
print(name, "is", age, "years old.")
```
4. **Why it matters**: Variables let your program remember and manipulate data as it runs!
""")
    elif "machine learning" in q_lower or "ml" in q_lower or "supervised" in q_lower:
        response_parts.append("""
1. **Core Concept**: Machine Learning is teaching computers to learn from data rather than writing explicit rules for every single task.
2. **Supervised Learning**: You give the computer questions AND the correct answers (labels), and it learns the mapping between them.
3. **Analogy**: Teaching a child to recognize cats by showing them hundreds of flashcards labeled "cat" or "not cat".
""")
    elif "career" in q_lower or "roadmap" in q_lower or "month" in q_lower:
        response_parts.append("""
1. **Career Roadmap Guidance**: Expanding your learning plan up to 20+ months is a fantastic strategy for career transition into AI/ML Engineering.
2. **Advanced Months (Months 13-20)**: Focus on LLM Fine-Tuning, MLOps, Model Deployment (FastAPI, Docker, Kubernetes), Cloud AI services, and building an end-to-end Portfolio Capstone Project.
3. **Action Item**: You can customize or add custom career months in the **Roadmap** section at any time!
""")
    else:
        response_parts.append(f"""
1. **Overview**: When studying this topic in Week {week_number or 'current'}, focus on understanding core definitions first before writing code.
2. **Key Takeaway**: Break the problem down into smaller parts, test your assumptions with small code snippets, and review your notes if anything is unclear.
3. **Next Step**: Try writing a small practice exercise or quiz question to test your understanding!
""")

    answer = "".join(response_parts)
    sources_str = str(search_results) if search_results else None

    # Save to history
    save_chat_message("user", question)
    save_chat_message("assistant", answer, sources_str)

    return answer, search_results

def get_sample_quiz(week_number: int):
    """Return a sample quiz for the given week."""
    quizzes = {
        1: {
            "title": "Week 1: Python Basics Quiz",
            "questions": [
                {
                    "id": 1,
                    "question": "Which symbol is used for single-line comments in Python?",
                    "options": ["//", "#", "/*", "<!--"],
                    "correct": 1
                },
                {
                    "id": 2,
                    "question": "How do you create a variable with the numeric value 10?",
                    "options": ["variable x = 10", "x = 10", "int x = 10", "val x = 10"],
                    "correct": 1
                }
            ]
        }
    }
    return quizzes.get(week_number, {
        "title": f"Week {week_number} Practice Quiz",
        "questions": [
            {
                "id": 1,
                "question": f"What is the primary focus of Week {week_number}?",
                "options": ["Theoretical math only", "Practical understanding and coding", "Memorizing equations", "None of the above"],
                "correct": 1
            }
        ]
    })

def save_quiz_score(week_number: int, score: float, total: int):
    """Save quiz score to database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO quiz_scores (week_number, score, total_questions, taken_at)
        VALUES (?, ?, ?, datetime('now'))
    """, (week_number, score, total))
    conn.commit()
    conn.close()
