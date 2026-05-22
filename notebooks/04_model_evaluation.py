# ============================================
# 04_model_evaluation.py
# ============================================

print("Evaluation Program Started")

import pandas as pd
import joblib

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score
)

# --------------------------------------------
# Load Processed Test Data
# --------------------------------------------

test_df = pd.read_csv("../outputs/processed_test.csv")

print("Processed Test Data Loaded!")

# --------------------------------------------
# Target Column
# --------------------------------------------

target_column = "Activity"

# --------------------------------------------
# Split Features and Labels
# --------------------------------------------

X_test = test_df.drop(target_column, axis=1)
y_test = test_df[target_column]

print("Features and Labels Split!")

# --------------------------------------------
# Load Trained Model
# --------------------------------------------

model = joblib.load("../models/har_model.pkl")

print("Trained Model Loaded!")

# --------------------------------------------
# Predictions
# --------------------------------------------

y_pred = model.predict(X_test)

print("Predictions Completed!")

# --------------------------------------------
# Accuracy
# --------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# --------------------------------------------
# Classification Report
# --------------------------------------------

report = classification_report(y_test, y_pred)

print("\nClassification Report:\n")
print(report)

# Save Report
with open(
    "../outputs/reports/classification_report.txt",
    "w"
) as file:
    file.write(report)

print("Classification Report Saved!")

# --------------------------------------------
# Confusion Matrix
# --------------------------------------------

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Save Figure
plt.savefig(
    "../outputs/figures/confusion_matrix.png"
)

plt.show()

print("Confusion Matrix Saved!")

print("Model Evaluation Completed Successfully!")