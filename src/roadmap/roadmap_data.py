"""
Extended 20-Month AI/ML & Career Roadmap (80 weeks) starting November 1, 2026.
"""

ROADMAP_WEEKS = [
    # Month 1: Python & Programming Foundations (Nov 2026)
    (1, "Python Basics: Variables, Data Types, and Operators", "Month 1: Python Foundations"),
    (2, "Control Flow: Conditionals, Loops, and Functions", "Month 1: Python Foundations"),
    (3, "Data Structures: Lists, Dictionaries, Sets, and Tuples", "Month 1: Python Foundations"),
    (4, "Object-Oriented Programming & File Handling in Python", "Month 1: Python Foundations"),

    # Month 2: Mathematics for AI/ML (Dec 2026)
    (5, "Linear Algebra: Vectors, Matrices, and Matrix Multiplication", "Month 2: Math for AI"),
    (6, "Linear Algebra: Eigenvalues, Eigenvectors, and PCA", "Month 2: Math for AI"),
    (7, "Calculus: Derivatives, Partial Derivatives, and Chain Rule", "Month 2: Math for AI"),
    (8, "Probability & Statistics: Distributions, Mean, Variance, and Bayes' Theorem", "Month 2: Math for AI"),

    # Month 3: Data Analysis & Visualization (Jan 2027)
    (9, "NumPy: Array Operations and Vectorization", "Month 3: Data Analysis"),
    (10, "Pandas: Dataframes, Cleaning, and Manipulation", "Month 3: Data Analysis"),
    (11, "Data Visualization: Matplotlib and Seaborn", "Month 3: Data Analysis"),
    (12, "Exploratory Data Analysis (EDA) Workflow", "Month 3: Data Analysis"),

    # Month 4: Classical Machine Learning - Part 1 (Feb 2027)
    (13, "Introduction to Machine Learning & Scikit-Learn", "Month 4: Classical ML I"),
    (14, "Linear Regression & Gradient Descent Optimization", "Month 4: Classical ML I"),
    (15, "Logistic Regression & Classification Metrics", "Month 4: Classical ML I"),
    (16, "Regularization: Ridge, Lasso, and ElasticNet", "Month 4: Classical ML I"),

    # Month 5: Classical Machine Learning - Part 2 (Mar 2027)
    (17, "Decision Trees and Random Forests", "Month 5: Classical ML II"),
    (18, "Support Vector Machines (SVMs) & Kernel Tricks", "Month 5: Classical ML II"),
    (19, "Unsupervised Learning: K-Means and Hierarchical Clustering", "Month 5: Classical ML II"),
    (20, "Dimensionality Reduction: t-SNE and UMAP", "Month 5: Classical ML II"),

    # Month 6: Deep Learning Foundations (Apr 2027)
    (21, "Introduction to PyTorch & Tensors", "Month 6: Deep Learning"),
    (22, "Neural Network Architecture & Activation Functions", "Month 6: Deep Learning"),
    (23, "Backpropagation and Loss Functions", "Month 6: Deep Learning"),
    (24, "Training Neural Networks: Optimizers and Regularization", "Month 6: Deep Learning"),

    # Month 7: Computer Vision (May 2027)
    (25, "Convolutional Neural Networks (CNNs) Fundamentals", "Month 7: Computer Vision"),
    (26, "Image Classification with PyTorch", "Month 7: Computer Vision"),
    (27, "Object Detection & Segmentation Concepts", "Month 7: Computer Vision"),
    (28, "Transfer Learning with Pretrained Vision Models", "Month 7: Computer Vision"),

    # Month 8: Natural Language Processing (Jun 2027)
    (29, "Text Preprocessing, Tokenization, and Stemming", "Month 8: NLP Basics"),
    (30, "Word Embeddings: Word2Vec and GloVe", "Month 8: NLP Basics"),
    (31, "Recurrent Neural Networks (RNNs) & LSTMs", "Month 8: NLP Basics"),
    (32, "Sequence-to-Sequence Models & Attention", "Month 8: NLP Basics"),

    # Month 9: Transformers & Large Language Models (Jul 2027)
    (33, "The Transformer Architecture: Self-Attention Mechanism", "Month 9: Transformers"),
    (34, "BERT and Encoder-Only Models", "Month 9: Transformers"),
    (35, "GPT and Decoder-Only Autoregressive Models", "Month 9: Transformers"),
    (36, "Fine-Tuning Strategies & PEFT (LoRA, QLoRA)", "Month 9: Transformers"),

    # Month 10: Retrieval-Augmented Generation (RAG) & Vector DBs (Aug 2027)
    (37, "Vector Embeddings & Vector Databases (FAISS, Chroma)", "Month 10: RAG Systems"),
    (38, "Document Chunking, Indexing, and Retrieval Strategies", "Month 10: RAG Systems"),
    (39, "Building a Complete Local RAG Pipeline", "Month 10: RAG Systems"),
    (40, "Evaluating RAG Systems & Hallucination Detection", "Month 10: RAG Systems"),

    # Month 11: Reinforcement Learning & Advanced Topics (Sep 2027)
    (41, "Reinforcement Learning Basics: MDPs and Q-Learning", "Month 11: RL & Advanced"),
    (42, "Deep Q-Networks (DQN) & Policy Gradients", "Month 11: RL & Advanced"),
    (43, "Diffusion Models & Generative AI Principles", "Month 11: RL & Advanced"),
    (44, "Model Quantization, Pruning, and Deployment", "Month 11: RL & Advanced"),

    # Month 12: Capstone Project & Model Training (Oct 2027)
    (45, "Designing Your Custom Small Language Model", "Month 12: Capstone"),
    (46, "Curating and Formatting Weekly Training Datasets", "Month 12: Capstone"),
    (47, "Training, Checkpointing, and Hyperparameter Tuning", "Month 12: Capstone"),
    (48, "Evaluating Model Performance and Mitigating Forgetting", "Month 12: Capstone"),
    (49, "Building the Personal AI Tutor Integration", "Month 12: Capstone"),
    (50, "Testing, Debugging, and Fine-Tuning Your Custom Model", "Month 12: Capstone"),
    (51, "Final Project Documentation & Portfolio Presentation", "Month 12: Capstone"),
    (52, "Graduation & Continuous Learning Plan", "Month 12: Capstone"),

    # Month 13: Advanced MLOps & Production Engineering (Nov 2027)
    (53, "MLOps Fundamentals: Model Versioning & Tracking (MLflow)", "Month 13: Advanced MLOps"),
    (54, "Containerizing AI Models with Docker", "Month 13: Advanced MLOps"),
    (55, "Serving Models with FastAPI and REST APIs", "Month 13: Advanced MLOps"),
    (56, "CI/CD Pipelines for Machine Learning", "Month 13: Advanced MLOps"),

    # Month 14: LLM Fine-Tuning & Alignment (Dec 2027)
    (57, "Advanced PEFT Techniques: QLoRA & DPO", "Month 14: LLM Alignment"),
    (58, "Instruction Tuning on Custom Datasets", "Month 14: LLM Alignment"),
    (59, "Model Evaluation Benchmarks (MMLU, HumanEval)", "Month 14: LLM Alignment"),
    (60, "Model Safety, Alignment, and Red Teaming", "Month 14: LLM Alignment"),

    # Month 15: Agentic AI & Autonomous Systems (Jan 2028)
    (61, "Agent Architectures: ReAct and Tool Use", "Month 15: Agentic AI"),
    (62, "Multi-Agent Collaboration Frameworks", "Month 15: Agentic AI"),
    (63, "Memory Systems and State Management in Agents", "Month 15: Agentic AI"),
    (64, "Building Autonomous Coding and Research Agents", "Month 15: Agentic AI"),

    # Month 16: Multimodal AI (Vision & Audio) (Feb 2028)
    (65, "Vision-Language Models (VLMs) Architecture", "Month 16: Multimodal AI"),
    (66, "Audio Processing, Speech-to-Text, and Whisper", "Month 16: Multimodal AI"),
    (67, "Multimodal RAG and Document Understanding", "Month 16: Multimodal AI"),
    (68, "Building Multimodal AI Applications", "Month 16: Multimodal AI"),

    # Month 17: Enterprise AI & Scalability (Mar 2028)
    (69, "Distributed Training & Data Parallelism", "Month 17: Enterprise AI"),
    (70, "Model Serving Optimization (vLLM, TensorRT-LLM)", "Month 17: Enterprise AI"),
    (71, "Latency, Throughput, and Cost Optimization", "Month 17: Enterprise AI"),
    (72, "Edge AI and On-Device Model Quantization", "Month 17: Enterprise AI"),

    # Month 18: Specialized Domains (Healthcare, Finance, Robotics) (Apr 2028)
    (73, "AI in Healthcare: Medical Imaging and Diagnostics", "Month 18: Specialized AI"),
    (74, "AI in Finance: Algorithmic Trading and Fraud Detection", "Month 18: Specialized AI"),
    (75, "Robotics AI: Simulation, Reinforcement Learning, and Control", "Month 18: Specialized AI"),
    (76, "Ethics, Governance, and AI Regulatory Compliance", "Month 18: Specialized AI"),

    # Month 19: Advanced Capstone & Open Source Contribution (May 2028)
    (77, "Proposing and Architecting Your Major Open Source Capstone", "Month 19: Capstone & OSS"),
    (78, "Building and Publishing Open Source AI Packages", "Month 19: Capstone & OSS"),
    (79, "Community Building, Documentation, and Technical Writing", "Month 19: Capstone & OSS"),
    (80, "AI/ML Career Portfolio, Interview Prep, and Job Search Strategy", "Month 19: Career & Portfolio"),
]
