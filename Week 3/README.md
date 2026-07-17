# 🧠 DecodeLabs | Project 3: Digital Matchmaker Engine

This repository contains **Project 3: AI Recommendation Logic**, developed as part of the DecodeLabs Industrial Training Program (Batch 2026). This project focuses on the "Personalization Phase" of AI, utilizing vector mapping and similarity algorithms to build a powerful recommendation system.

Unlike simple rule-based bots or standard classifiers, this engine mathematically calculates the alignment between user preferences and a custom knowledge base of tech items using **Cosine Similarity**.

---

## 🚀 Core Features

- **Feature Extraction & Vector Mapping:** Transforms raw qualitative item data into 1D numerical feature vectors (Performance, Portability, Gaming, Productivity).
- **Cosine Similarity Engine:** Employs Scikit-Learn's `cosine_similarity` to calculate the exact mathematical angle/alignment between the user's target profile and database items.
- **Interactive Gradio Frontend:** A state-of-the-art, soft-themed web UI with intuitive slider controls for real-time input.
- **Dynamic Visual Analytics:** - A sorted Horizontal Bar Chart showing the top 3 recommended items based on alignment scores.
  - A Grouped Bar Chart directly comparing the user's requested profile against the best match's actual features.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Environment:** Google Colab / Jupyter Notebook
- **Machine Learning Core:** Scikit-Learn (Cosine Similarity)
- **Frontend Framework:** Gradio Blocks API
- **Data Engineering:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn

---

## 📂 Notebook Architecture (`Week 3.ipynb`)

The project is modularized into 4 distinct execution cells for clean deployment:

1. **Dependency Installation:** Installs `gradio`, `pandas`, `numpy`, `scikit-learn`, `matplotlib`, and `seaborn`.
2. **Knowledge Base Initialization:** Constructs a Pandas DataFrame of tech items, mapping them onto a standardized 0.0 to 1.0 feature scale.
3. **Similarity Mathematics Engine:** Contains the core function that calculates vector cosine similarity across the feature matrix.
4. **Frontend & Visualization:** Generates the Gradio interface, binds the backend calculation logic, and renders real-time analytical plots.

---

## 💻 How to Run This Project

1. Upload the `Week 3.ipynb` notebook to [Google Colab](https://colab.research.google.com/).
2. Run **Cell 1** to install all required dependencies.
3. Run **Cells 2 and 3** to initialize the database and the mathematical engine.
4. Run **Cell 4** to launch the Gradio User Interface.
5. A local Gradio interface will appear in the cell output, along with a public `.gradio.live` link for full-screen browser access.

---

*Powered by DecodeLabs | Batch 2026 Industrial Training Kit*
