# ============================================
# predict.py
# ============================================

print("Prediction Program Started")

import joblib
import pandas as pd

# --------------------------------------------
# Load Model
# --------------------------------------------

model = joblib.load(
    "../models/best_model.pkl"
)

print("Model Loaded Successfully!")

# --------------------------------------------
# Load Processed Dataset
# --------------------------------------------

df = pd.read_csv(
    "../outputs/processed_test.csv"
)

print("Dataset Loaded Successfully!")

# --------------------------------------------
# Target Column
# --------------------------------------------

target_column = "Activity"

# --------------------------------------------
# Feature Data
# --------------------------------------------

X = df.drop(target_column, axis=1)

# --------------------------------------------
# Take One Sample Row
# --------------------------------------------

sample_data = X.iloc[[0]]

print("\nSample Data:")
print(sample_data)

# --------------------------------------------
# Predict
# --------------------------------------------

prediction = model.predict(sample_data)

# --------------------------------------------
# Display Result
# --------------------------------------------

print("\nPrediction Result:")

print(prediction[0])

print("\nPrediction Completed Successfully!")