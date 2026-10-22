# AI Tutor - Personal Learning Assistant

A local AI tutor to help you learn Artificial Intelligence and Machine Learning throughout your 12-month learning roadmap.

## Features

- 📚 **Personal Learning Roadmap**: Track your 12-month AI/ML journey week by week
- 📄 **PDF Tutor**: Import and search through your learning materials
- 🧠 **Teaching Assistant**: Get explanations, examples, quizzes, and exercises
- 🗂️ **Dataset Management**: Manually prepare and import training datasets
- 🤖 **Custom Model Training**: Build and train your own small language model
- 📊 **Progress Tracking**: Monitor lessons completed, quiz scores, and learning history
- 🔒 **Local & Private**: All data stays on your computer

## System Requirements

- **OS**: Windows 10/11
- **Python**: 3.10 or higher
- **RAM**: 16 GB recommended
- **Storage**: 5-10 GB for datasets and model checkpoints
- **GPU**: Not required (CPU-compatible training)

## Quick Start

### 1. Install Dependencies

```bash
cd ai-tutor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser at `http://localhost:8501`

### 3. First-Time Setup

1. **Configure your learning roadmap** in the Settings tab
2. **Import your first PDF materials** in the PDF Library
3. **Start learning** from Week 1!

## Project Structure

```
ai-tutor/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── datasets/             # Training datasets by week
│   ├── week_01/
│   ├── week_02/
│   └── ...
├── documents/            # Imported PDF files
├── checkpoints/          # Saved model checkpoints
├── data/                 # SQLite database and progress tracking
├── src/                  # Source code modules
│   ├── roadmap/          # Learning roadmap management
│   ├── pdf_handler/      # PDF import and search
│   ├── tutor/            # Question answering and exercises
│   ├── model/            # Model training and inference
│   └── progress/         # Progress tracking
└── tests/                # Automated tests
```

## Usage Guide

### Learning Roadmap

Navigate to the **Roadmap** page to:
- View your 12-month learning plan organized by months and weeks
- Mark lessons as completed
- Track your current progress
- Revisit earlier lessons

### PDF Library

In the **PDF Library** page:
- Import PDF files containing your learning materials
- Search across all imported documents
- View document sources and page numbers

### Ask Questions

Use the **Tutor** page to:
- Ask questions about topics you're learning
- Get explanations and examples
- Request quizzes and practice exercises
- Check your answers

### Dataset Management

In the **Datasets** page:
- Import weekly training datasets (JSONL format)
- Validate dataset format and contents
- Preview datasets before training
- Track which datasets have been imported

### Model Training

In the **Training** page:
- Start training on new weekly datasets
- Monitor training progress and metrics
- Save model checkpoints
- Resume training from saved checkpoints
- Evaluate model on old and new topics

## Dataset Format

Training datasets should be in JSONL format (one JSON object per line):

```jsonl
{"role": "user", "content": "What is supervised learning?", "week": 1, "topic": "ML Basics"}
{"role": "assistant", "content": "Supervised learning is...", "week": 1, "topic": "ML Basics"}
{"role": "user", "content": "Explain gradient descent", "week": 2, "topic": "Optimization"}
{"role": "assistant", "content": "Gradient descent is...", "week": 2, "topic": "Optimization"}
```

Save dataset files as `datasets/week_XX/dataset.jsonl`

## Troubleshooting

### Application won't start
```bash
# Check Python version
python --version  # Should be 3.10 or higher

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Try running with verbose output
streamlit run app.py --logger.level=debug
```

### Import errors
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Verify all packages installed
pip list
```

### Training fails or is too slow
- Reduce model size in config.py
- Reduce batch size
- Use smaller datasets for testing
- Close other memory-intensive applications

### PDF import not working
- Ensure PDF is not password-protected
- Try converting scanned PDFs with OCR first
- Check file permissions

### Out of memory during training
- Reduce batch_size in training settings
- Use gradient accumulation
- Train on smaller dataset samples
- Close other applications

## Known Limitations

- Model training is educational; expect basic performance compared to large commercial models
- CPU training is slower than GPU training
- Scanned PDFs require external OCR processing
- Initial model needs multiple weeks of training to be useful

## Recovery Instructions

### Reset progress tracking
Delete `data/progress.db` and restart the app. Your datasets and checkpoints will remain.

### Start fresh with training
Delete the `checkpoints/` folder. Your datasets will remain intact.

### Recover from corrupted dataset
Remove the problematic dataset file and re-import from your backup.

### Factory reset
Delete `data/`, `checkpoints/`, and `documents/` folders. The application will reinitialize.

## Development

### Running Tests
```bash
pytest tests/ -v
```

### Code Structure Check
```bash
python -m compileall .
```

## Support

This is a personal learning project. Refer to:
- PROJECT_STATUS.md for current development status
- Source code comments for implementation details
- Python/ML documentation for technical concepts

## License

Personal use project - not licensed for distribution.

---
**Created**: October 22, 2026
**Target Launch**: November 1, 2026
