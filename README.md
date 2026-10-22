# AI Tutor - Personal Learning Assistant

A local, private AI tutor designed to help you master Artificial Intelligence and Machine Learning throughout your 12-month learning roadmap starting November 1, 2026.

## Features

- 📚 **Personal Learning Roadmap**: Track your 52-week AI/ML journey week by week.
- 📄 **PDF Library & Local Search**: Import PDF study materials and search passages instantly with source citations.
- 💬 **AI Teaching Assistant**: Get beginner-friendly explanations, code examples, analogies, and practice quizzes.
- 🗂️ **Dataset Manager**: Validate and import weekly training datasets in JSONL format.
- 🤖 **Model Training & Checkpoints**: Train your custom educational AI model, save checkpoints, and track loss.
- 📊 **Progress Tracking**: Monitor completed lessons, quiz scores, and learning history via local SQLite database.
- 🔒 **100% Local & Private**: All data stays on your computer. No external API calls or subscriptions required.

---

## Quick Start (Windows)

### 1. Set Up Virtual Environment & Dependencies

Open Command Prompt or Git Bash in the project folder (`C:\Users\kumj3\ai-tutor`):

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

Open your web browser and go to:
**`http://127.0.0.1:5000`**

---

## Running Automated Tests

```bash
venv\Scripts\pytest tests/ -v
```

---

## Project Structure

- `app.py`: Flask web application and UI routes
- `config.py`: Global project paths and configurations
- `src/roadmap/`: 52-week AI/ML curriculum
- `src/pdf_handler/`: PDF text extraction and indexing
- `src/tutor/`: Pedagogical Q&A and quizzes
- `src/dataset_manager/`: JSONL dataset validation
- `src/model/`: Educational model training & checkpoints
- `src/progress/`: SQLite database initialization
- `templates/`: Bootstrap 5 responsive UI views
- `datasets/week_01/`: Sample Week 1 dataset (`dataset.jsonl`)

---

## License
Personal learning project.
