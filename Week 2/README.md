# 🌸 DecodeLabs | Project 2: Data Classification Using AI

This repository contains **Project 2: Data Classification Using AI**, developed as part of the DecodeLabs Industrial Training Program (Batch 2026). This project transitions from the deterministic rule-based logic of Project 1 into the domain of **Supervised Machine Learning** and interactive frontend deployment.

Using the classic Iris tabular dataset, this pipeline trains a **K-Nearest Neighbors (KNN) Classifier** using an **80/20 train-test split**, evaluates it with key performance metrics, and deploys a state-of-the-art interactive **Gradio Frontend UI** with **4 real-time data visualization plots**.

---

## 🚀 Features

- **End-to-End ML Pipeline:** Seamless transition from Data Ingestion to Scaling, Model Training, Evaluation, and Deployment.
- **Strict 80/20 Train-Test Split:** Splitted training and testing datasets according to strict project guidelines for proper model validation.
- **Feature Standardization:** Implemented `StandardScaler` to normalize features for optimal algorithm performance.
- **Evaluation & Performance Metrics:** Automatically outputs Model Accuracy and a complete Confusion Matrix to track True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN).
- **Interactive Gradio Blocks UI:** A beautifully formatted, soft-themed frontend with slider inputs.
- **Real-Time 2x2 Grid Visualization:** On every slider adjustment and prediction, the UI dynamically updates a 2x2 grid containing 4 separate scatter plots (Sepal & Petal features) with a **Large Red Star (⭐)** highlighting your current real-time input.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Platform:** Google Colab
- **Machine Learning Library:** Scikit-Learn
- **Frontend / UI Framework:** Gradio
- **Data Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn

---

## 📂 Project Architecture (Notebook Structure)

The Jupyter Notebook (`Untitled12.ipynb`) is modularly organized into 4 distinct executable cells for clear execution:

### Cell 1: Installation & Dependencies
Installs Gradio, Scikit-Learn, and plotting libraries quietly on the Google Colab environment.

### Cell 2: Data Loading & Preprocessing
- Loads the tabular Iris dataset.
- Performs an **80% Training and 20% Testing split**.
- Applies standard scaling on the feature sets.

### Cell 3: Model Training & Evaluation
- Trains the **K-Nearest Neighbors (KNN)** Classifier (with $k=3$).
- Generates the Confusion Matrix and accuracy percentage.

### Cell 4: Advanced Gradio Frontend with 2x2 Real-Time Plots
Launches the web application with sliders for input and outputs the prediction alongside 4 real-time Matplotlib/Seaborn subplots.

---

## 💻 How to Run This Project on Google Colab

1. **Create a New Notebook** on [Google Colab](https://colab.research.google.com/).
2. Copy and run the code block by block from the provided notebook cells.
3. Once you execute **Cell 4**, Gradio will generate a local notebook interface as well as a public **`.gradio.live` link**.
4. Click the public link to access your interactive AI frontend full-screen in any web browser!

---

## 📊 Live UI Visualization Preview

Adjust the sliders for:
- **Sepal Length (cm)**
- **Sepal Width (cm)**
- **Petal Length (cm)**
- **Petal Width (cm)**

Click **"Predict & Generate Plots 🚀"** to see:
1. **AI Output Layer:** The predicted class (e.g., SETOSA, VERSICOLOR, or VIRGINICA).
2. **Real-Time Plots:** A 2x2 grid displaying exactly where your input parameters sit (represented by a red ⭐) among the historical data points.

---

*Powered by DecodeLabs | Batch 2026 Industrial Training Kit*
