# kepler-Exoplanet-predictor
ml project for detecting exoplanets using NASA kepler telescope data with XGBoost,SMOTE,and Streamlite deployment

🚀 Kepler Exoplanet Predictor

🌌 Project Overview

This project uses Machine Learning to detect whether a signal captured by NASA’s Kepler Space Telescope represents a real exoplanet or a false alarm.

The system analyzes stellar transit characteristics and predicts planetary confirmation using trained classification models.

---

✨ Features

- Data preprocessing and cleaning
- Handling missing values
- SMOTE imbalance correction
- Multiple ML model training
- Streamlit deployment
- Interactive prediction dashboard
- Hugging Face deployment

---

🧠 Machine Learning Models Used

- Random Forest Classifier
- knn Classifier
- logistic regression

---

📊 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score

XGBoost achieved the best overall performance.

---

⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Imbalanced-learn
- Hugging Face Spaces

---

🔬 Workflow

1. Load Kepler cumulative dataset
2. Clean and preprocess data
3. Remove unnecessary ID columns
4. Handle missing values
5. Apply SMOTE for class balancing
6. Train multiple ML models
7. Evaluate performance
8. Deploy using Streamlit + Hugging Face

---

🖥️ Application Preview

Dashboard UI

(Add dashboard screenshot here)

Jupyter Training Notebook

(Add notebook screenshot here)

Live Deployment

(Add deployment screenshot here)

---

🚀 Run Locally

Install dependencies:

pip install -r requirements.txt

Run Streamlit app:
https://huggingface.co/spaces/Monafr/kepler-exoplanet-detector
streamlit run app.py

---

📌 Future Improvements

- Add deep learning models
- Real-time NASA API integration
- Better feature engineering
- Probability confidence visualization

---

👨‍💻 Author

Developed as part of an AI/ML Exoplanet Hunting project.
