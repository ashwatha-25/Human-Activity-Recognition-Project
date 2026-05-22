# 🧠 Human Activity Recognition System Using Smartphones

A Machine Learning based Human Activity Recognition (HAR) system that detects human activities using smartphone sensor data such as accelerometer and gyroscope readings.

This project predicts:

- 🚶 Walking
- 🪑 Sitting
- 🧍 Standing
- 🛌 Laying
- ⬆ Walking Upstairs
- ⬇ Walking Downstairs
- ⚠ Fall Detection
- ✅ Fall Not Detected

The system also provides:

- 📊 Model Accuracy
- 🔥 Confusion Matrix Visualization
- 🖼 Activity Images
- 🔥 Estimated Calories Burned
- 📈 Interactive Streamlit Dashboard

---

# 📌 Project Features

✅ Human Activity Recognition  
✅ Fall Detection System  
✅ Machine Learning Classification  
✅ Confusion Matrix Heatmap  
✅ Accuracy Prediction  
✅ Real-Time Activity Visualization  
✅ Streamlit Web Application  
✅ Calories Burned Estimation  
✅ Smartphone Sensor Data Processing  

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Streamlit | Web Application |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Matplotlib | Visualization |
| Seaborn | Heatmap Visualization |
| Joblib | Model Saving |

---

# 📂 Project Structure

```text
HAR_Smartphone_Project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── models/
│   └── har_model.pkl
│
├── outputs/
│   ├── confusion_matrix.png
│   ├── accuracy_score.txt
│   └── predictions.csv
│
├── images/
│   ├── walking.png
│   ├── sitting.png
│   ├── standing.png
│   ├── laying.png
│   ├── fall_detected.png
│   └── no_fall.png
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── prediction.py
│
└── pages/
    ├── Home.py
    ├── Prediction.py
    └── Analysis.py
```

---

# 📊 Model Performance

| Metric | Value |
|---|---|
| Accuracy | 96% |
| Precision | 95% |
| Recall | 94% |
| F1 Score | 95% |

---

# 🔥 Confusion Matrix

The confusion matrix helps visualize the prediction performance of the machine learning model.

Features:
- Correct predictions on diagonal
- Misclassifications shown off-diagonal
- Heatmap visualization using Seaborn

---

# ⚠ Fall Detection Module

The system detects whether a person has fallen using smartphone motion sensor data.

### Output Classes

| Label | Meaning |
|---|---|
| 0 | Fall Not Detected |
| 1 | Fall Detected |

---

# 🔥 Calories Burned Estimation

The application estimates calories burned based on activity type.

| Activity | Estimated Calories |
|---|---|
| Walking | 120 kcal |
| Upstairs | 150 kcal |
| Downstairs | 130 kcal |
| Sitting | 50 kcal |
| Standing | 70 kcal |
| Laying | 40 kcal |

---

# 🖼 Activity Images

The Streamlit dashboard displays activity images dynamically based on predictions.

Examples:
- Walking Image
- Sitting Image
- Standing Image
- Fall Detection Alert Image

---

# 🚀 Run the Project

## 1️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📈 Machine Learning Workflow

```text
Data Collection
       ↓
Data Preprocessing
       ↓
Feature Scaling
       ↓
Model Training
       ↓
Prediction
       ↓
Accuracy Evaluation
       ↓
Confusion Matrix
       ↓
Streamlit Visualization
```

---

# 📷 Dashboard Preview

Features included in dashboard:

✅ Activity Prediction  
✅ Accuracy Display  
✅ Confusion Matrix Heatmap  
✅ Fall Detection Alert  
✅ Calories Burned Estimation  
✅ Interactive Charts  
✅ Activity Images  

---

# 📚 Dataset

Dataset used:
- UCI HAR Dataset
- Smartphone Accelerometer & Gyroscope Data

Activities are collected from multiple participants using wearable smartphone sensors.

---

# 🎯 Future Enhancements

- Deep Learning Models
- Real-Time Sensor Streaming
- Mobile App Integration
- Cloud Deployment
- Advanced Fall Detection
- Health Monitoring Dashboard

---

# 👨‍💻 Author

Ashwatha S

---

# ⭐ GitHub Repository

If you like this project, give it a ⭐ on GitHub.