"""
AI Tutor - Flask Local Web Application
A beginner-friendly personal AI tutor for learning AI/ML across custom PDF-generated roadmaps.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import os
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))
import config
from src.progress.db import init_db, get_connection
from src.roadmap.roadmap_data import ROADMAP_WEEKS
from src.roadmap.pdf_generator import generate_roadmap_from_pdf
from src.pdf_handler.handler import import_pdf, search_documents, get_imported_documents
from src.dataset_manager.manager import import_dataset, get_imported_datasets
from src.tutor.assistant import ask_tutor, get_sample_quiz, save_quiz_score, get_chat_history, clear_chat_history
from src.model.trainer import simulate_training_run, get_training_runs, get_checkpoints

app = Flask(__name__)
app.secret_key = "ai-tutor-secret-key-local"

# Ensure directories and database are initialized
config.ensure_directories()
init_db()

@app.route("/")
def index():
    """Home dashboard."""
    docs = get_imported_documents()
    datasets = get_imported_datasets()
    runs = get_training_runs()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM roadmap_progress WHERE status='completed'")
    completed_weeks = cursor.fetchone()["count"]
    cursor.execute("SELECT COUNT(*) as count FROM roadmap_progress")
    total_custom_weeks = cursor.fetchone()["count"]
    conn.close()

    stats = {
        "total_weeks": total_custom_weeks if total_custom_weeks > 0 else len(ROADMAP_WEEKS),
        "completed_weeks": completed_weeks,
        "pdf_count": len(docs),
        "dataset_count": len(datasets),
        "training_runs": len(runs)
    }
    return render_template("index.html", stats=stats, docs=docs[:3], datasets=datasets[:3])

@app.route("/roadmap")
def roadmap():
    """Roadmap page (loads custom PDF-generated roadmap if available, else default)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT week_number, title, month_label, status, notes FROM roadmap_progress ORDER BY week_number ASC")
    db_weeks = [dict(row) for row in cursor.fetchall()]
    conn.close()

    if db_weeks:
        weeks_data = [{
            "week_number": w["week_number"],
            "title": w["title"],
            "month": w["month_label"] or "Custom Roadmap",
            "status": w["status"],
            "notes": w["notes"]
        } for w in db_weeks]
    else:
        weeks_data = [{
            "week_number": w,
            "title": t,
            "month": m,
            "status": "upcoming",
            "notes": ""
        } for w, t, m in ROADMAP_WEEKS]

    return render_template("roadmap.html", weeks=weeks_data)

@app.route("/roadmap/update/<int:week_num>", methods=["POST"])
def update_roadmap(week_num):
    """Update week status."""
    status = request.form.get("status", "upcoming")
    notes = request.form.get("notes", "")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE roadmap_progress
        SET status = ?, notes = ?, completed_at = CASE WHEN ? = 'completed' THEN datetime('now') ELSE completed_at END
        WHERE week_number = ?
    """, (status, notes, status, week_num))
    conn.commit()
    conn.close()

    flash(f"Updated Week {week_num} status to {status}.", "success")
    return redirect(url_for("roadmap"))

@app.route("/pdf", methods=["GET", "POST"])
def pdf_library():
    """PDF Library, search, and automatic roadmap generator."""
    if request.method == "POST":
        action = request.form.get("action", "import")
        if "pdf_file" in request.files:
            file = request.files["pdf_file"]
            title = request.form.get("title", "")
            if file and file.filename.endswith(".pdf"):
                temp_path = config.DOCUMENTS_DIR / file.filename
                file.save(str(temp_path))
                try:
                    doc_id = import_pdf(str(temp_path), title or file.filename)
                    if action == "generate_roadmap":
                        generated = generate_roadmap_from_pdf(str(temp_path))
                        flash(f"Successfully analyzed PDF and generated custom roadmap with {len(generated)} weeks!", "success")
                    else:
                        flash(f"Successfully imported and indexed {file.filename}!", "success")
                except Exception as e:
                    flash(f"Error processing PDF: {e}", "danger")
            else:
                flash("Please upload a valid PDF file.", "warning")
        return redirect(url_for("pdf_library"))

    query = request.args.get("q", "")
    search_results = search_documents(query) if query else []
    docs = get_imported_documents()
    return render_template("pdf.html", docs=docs, search_results=search_results, query=query)

@app.route("/tutor", methods=["GET", "POST"])
def tutor():
    """ChatGPT-style Tutor Q&A page."""
    week_num = 1

    if request.method == "POST":
        question = request.form.get("question", "")
        week_num = int(request.form.get("week_number", 1))
        if question:
            ask_tutor(question, week_num)
        return redirect(url_for("tutor"))

    history = get_chat_history()
    quiz = get_sample_quiz(week_num)
    return render_template("tutor.html", history=history, quiz=quiz, week_number=week_num)

@app.route("/tutor/clear", methods=["POST"])
def clear_chat():
    """Clear chat history."""
    clear_chat_history()
    flash("Chat history cleared.", "info")
    return redirect(url_for("tutor"))

@app.route("/tutor/quiz", methods=["POST"])
def submit_quiz():
    """Submit quiz answers."""
    week_num = int(request.form.get("week_number", 1))
    score = float(request.form.get("score", 0))
    total = int(request.form.get("total", 1))
    save_quiz_score(week_num, score, total)
    flash(f"Quiz submitted! Score: {score}/{total}", "success")
    return redirect(url_for("tutor"))

@app.route("/datasets", methods=["GET", "POST"])
def datasets():
    """Dataset management page."""
    if request.method == "POST":
        if "dataset_file" in request.files:
            file = request.files["dataset_file"]
            week_num = int(request.form.get("week_number", 1))
            topic = request.form.get("topic", "General ML")
            if file and file.filename.endswith(".jsonl"):
                temp_path = config.DATASETS_DIR / file.filename
                file.save(str(temp_path))
                try:
                    valid, invalid = import_dataset(str(temp_path), week_num, topic)
                    flash(f"Successfully imported dataset! Valid: {valid}, Invalid: {invalid}", "success")
                except Exception as e:
                    flash(f"Dataset import failed: {e}", "danger")
            else:
                flash("Please upload a valid JSONL file.", "warning")
        return redirect(url_for("datasets"))

    imported = get_imported_datasets()
    return render_template("datasets.html", datasets=imported)

@app.route("/training", methods=["GET", "POST"])
def training():
    """Model training page."""
    if request.method == "POST":
        run_name = request.form.get("run_name", "model_run_1")
        epochs = int(request.form.get("epochs", 5))
        week_num = int(request.form.get("dataset_week", 1))
        try:
            res = simulate_training_run(run_name, epochs, week_num)
            flash(f"Training completed successfully! Final loss: {res['final_loss']}", "success")
        except Exception as e:
            flash(f"Training failed: {e}", "danger")
        return redirect(url_for("training"))

    runs = get_training_runs()
    checkpoints = get_checkpoints()
    datasets = get_imported_datasets()
    return render_template("training.html", runs=runs, checkpoints=checkpoints, datasets=datasets)

@app.route("/progress")
def progress():
    """Progress tracking dashboard."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quiz_scores ORDER BY taken_at DESC")
    quizzes = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM roadmap_progress WHERE status='completed'")
    completed = [dict(row) for row in cursor.fetchall()]
    conn.close()

    runs = get_training_runs()
    datasets = get_imported_datasets()
    docs = get_imported_documents()

    return render_template("progress.html", quizzes=quizzes, completed=completed, runs=runs, datasets=datasets, docs=docs)

@app.route("/settings")
def settings():
    """Settings page."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM roadmap_progress")
    total_weeks = cursor.fetchone()["count"]
    conn.close()
    return render_template("settings.html", config=config, total_weeks=total_weeks if total_weeks > 0 else len(ROADMAP_WEEKS))

if __name__ == "__main__":
    print("=" * 60)
    print("🎓 Starting AI Tutor Flask Local Web Application...")
    print("Open your browser at: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5000, debug=True)
