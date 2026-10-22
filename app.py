"""
AI Tutor - Main Streamlit Application
A personal AI tutor for learning AI/ML throughout a 12-month roadmap.
"""

import streamlit as st
from pathlib import Path
import sys

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

import config

# Initialize directories
config.ensure_directories()

def main():
    """Main application entry point."""

    # Page configuration
    st.set_page_config(
        page_title=config.APP_CONFIG["page_title"],
        page_icon=config.APP_CONFIG["page_icon"],
        layout=config.APP_CONFIG["layout"],
        initial_sidebar_state=config.APP_CONFIG["initial_sidebar_state"],
    )

    # Title
    st.title("🎓 AI Tutor - Personal Learning Assistant")
    st.markdown("---")

    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        page = st.radio(
            "Go to",
            [
                "🏠 Home",
                "📚 Roadmap",
                "📄 PDF Library",
                "💬 Tutor",
                "🗂️ Datasets",
                "🤖 Training",
                "📊 Progress",
                "⚙️ Settings",
            ],
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.caption("Version 0.1.0 (Foundation)")
        st.caption("October 22, 2026")

    # Route to appropriate page
    if page == "🏠 Home":
        show_home_page()
    elif page == "📚 Roadmap":
        show_roadmap_page()
    elif page == "📄 PDF Library":
        show_pdf_page()
    elif page == "💬 Tutor":
        show_tutor_page()
    elif page == "🗂️ Datasets":
        show_datasets_page()
    elif page == "🤖 Training":
        show_training_page()
    elif page == "📊 Progress":
        show_progress_page()
    elif page == "⚙️ Settings":
        show_settings_page()

def show_home_page():
    """Display the home page."""
    st.header("Welcome to Your AI Learning Journey!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📅 Your Learning Plan")
        st.info("""
        **Start Date**: November 1, 2026
        **Duration**: 12 months (52 weeks)
        **Current Status**: Ready to begin!
        """)

        st.subheader("🎯 Quick Start")
        st.markdown("""
        1. **📚 Set up your Roadmap** - Define your weekly learning goals
        2. **📄 Import PDFs** - Add your learning materials
        3. **💬 Start Learning** - Ask questions and get exercises
        4. **🗂️ Prepare Datasets** - Create training data for your model
        5. **🤖 Train Your Model** - Build your personal AI assistant
        """)

    with col2:
        st.subheader("📊 System Status")

        # Check directory status
        dirs_ok = all([
            config.DATA_DIR.exists(),
            config.DOCUMENTS_DIR.exists(),
            config.DATASETS_DIR.exists(),
            config.CHECKPOINTS_DIR.exists(),
        ])

        if dirs_ok:
            st.success("✓ All directories initialized")
        else:
            st.error("✗ Some directories missing - reinitializing...")
            config.ensure_directories()
            st.rerun()

        # Check database
        if config.DATABASE_PATH.exists():
            st.success("✓ Database initialized")
        else:
            st.warning("⚠ Database not yet created - will initialize on first use")

        # Dataset count
        dataset_weeks = list(config.DATASETS_DIR.glob("week_*/"))
        st.info(f"📦 Datasets imported: {len(dataset_weeks)} weeks")

        # Document count
        pdf_count = len(list(config.DOCUMENTS_DIR.glob("*.pdf")))
        st.info(f"📄 PDFs imported: {pdf_count}")

        # Checkpoint count
        checkpoint_count = len(list(config.CHECKPOINTS_DIR.glob("checkpoint_*.pt")))
        st.info(f"💾 Model checkpoints: {checkpoint_count}")

    st.markdown("---")
    st.subheader("🚀 Getting Started")
    st.markdown("""
    This AI Tutor will help you learn AI and Machine Learning step by step.

    **What makes this special:**
    - ✅ Runs completely on your computer
    - ✅ Your data stays private and local
    - ✅ Build and train your own AI model
    - ✅ Tracks your learning progress
    - ✅ Adapts to your learning pace

    **Use the sidebar** to navigate between different sections.
    Start with the **Roadmap** to plan your learning journey!
    """)

def show_roadmap_page():
    """Display the learning roadmap page."""
    st.header("📚 Learning Roadmap")
    st.markdown("Define and track your 12-month AI/ML learning journey.")
    st.info("🚧 **Coming Soon**: Full roadmap management will be implemented in the next phase.")

    # Placeholder for roadmap functionality
    st.subheader("Planned Features")
    st.markdown("""
    - View your complete 52-week learning plan
    - Mark lessons as completed
    - Track current week and progress
    - Revisit earlier lessons
    - Update curriculum as needed
    """)

def show_pdf_page():
    """Display the PDF library page."""
    st.header("📄 PDF Library")
    st.markdown("Import and search through your learning materials.")
    st.info("🚧 **Coming Soon**: PDF import and search will be implemented in the next phase.")

    # Placeholder
    st.subheader("Planned Features")
    st.markdown("""
    - Import PDF documents
    - Extract and index text
    - Search across all documents
    - View source document and page numbers
    - Handle OCR for scanned PDFs
    """)

def show_tutor_page():
    """Display the tutor/Q&A page."""
    st.header("💬 Ask Your AI Tutor")
    st.markdown("Get explanations, examples, and practice exercises.")
    st.info("🚧 **Coming Soon**: Interactive tutoring will be implemented in the next phase.")

    # Placeholder
    st.subheader("Planned Features")
    st.markdown("""
    - Ask questions about any topic
    - Get step-by-step explanations
    - Request practice problems and quizzes
    - Check your answers
    - Get hints before full solutions
    """)

def show_datasets_page():
    """Display the dataset management page."""
    st.header("🗂️ Dataset Management")
    st.markdown("Import and validate training datasets for your AI model.")
    st.info("🚧 **Coming Soon**: Dataset import and validation will be implemented in the next phase.")

    # Show expected format
    st.subheader("Dataset Format (JSONL)")
    st.code('''{"role": "user", "content": "What is supervised learning?", "week": 1, "topic": "ML Basics"}
{"role": "assistant", "content": "Supervised learning is a type of machine learning...", "week": 1, "topic": "ML Basics"}''', language="json")

def show_training_page():
    """Display the model training page."""
    st.header("🤖 Model Training")
    st.markdown("Train your personal AI model on your learning datasets.")
    st.info("🚧 **Coming Soon**: Model training will be implemented in the next phase.")

    # Show current config
    st.subheader("Current Model Configuration")
    st.json(config.MODEL_CONFIG)

def show_progress_page():
    """Display the progress tracking page."""
    st.header("📊 Learning Progress")
    st.markdown("Track your completed lessons, quiz scores, and learning history.")
    st.info("🚧 **Coming Soon**: Progress tracking will be implemented in the next phase.")

def show_settings_page():
    """Display the settings page."""
    st.header("⚙️ Settings")
    st.markdown("Configure your AI Tutor application.")

    st.subheader("📁 Directory Paths")
    st.text(f"Data: {config.DATA_DIR}")
    st.text(f"Documents: {config.DOCUMENTS_DIR}")
    st.text(f"Datasets: {config.DATASETS_DIR}")
    st.text(f"Checkpoints: {config.CHECKPOINTS_DIR}")

    st.subheader("🗄️ Database")
    st.text(f"Location: {config.DATABASE_PATH}")

    st.subheader("📅 Roadmap Configuration")
    st.text(f"Start Date: {config.ROADMAP_CONFIG['start_date']}")
    st.text(f"Total Weeks: {config.ROADMAP_CONFIG['total_weeks']}")

    st.markdown("---")
    st.caption("More settings will be added as features are implemented.")

if __name__ == "__main__":
    main()
