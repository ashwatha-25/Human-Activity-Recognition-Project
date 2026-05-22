# ============================================
# evaluate_model.py
# ============================================

print("Evaluation File Started")

import pandas as pd
import joblib

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# --------------------------------------------
# Load Processed Test Dataset
# --------------------------------------------

print("Loading Processed Test Dataset...")

test_df = pd.read_csv(
    "../outputs/processed_test.csv"
)

print("Processed Test Dataset Loaded!")

# --------------------------------------------
# Show Dataset Columns
# --------------------------------------------

print("\nDataset Columns:")
print(test_df.columns)

# --------------------------------------------
# Target Column
# --------------------------------------------

target_column = "Activity"

# --------------------------------------------
# Split Features and Labels
# --------------------------------------------

X_test = test_df.drop(
    target_column,
    axis=1
)

y_test = test_df[target_column]

print("\nFeature and Label Split Completed!")

# --------------------------------------------
# Load Trained Model
# --------------------------------------------

print("\nLoading Trained Model...")

model = joblib.load(
    "../models/best_model.pkl"
)

print("Model Loaded Successfully!")

# --------------------------------------------
# Make Predictions
# --------------------------------------------

print("\nMaking Predictions...")

y_pred = model.predict(X_test)

print("Predictions Completed!")

# --------------------------------------------
# Calculate Accuracy
# --------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# --------------------------------------------
# Classification Report
# --------------------------------------------

report = classification_report(
    y_test,
    y_pred
)

print("\nClassification Report:\n")
print(report)

# --------------------------------------------
# Save Classification Report
# --------------------------------------------

with open(
    "../outputs/reports/classification_report.txt",
    "w"
) as file:

    file.write(report)

print("Classification Report Saved!")

# --------------------------------------------
# Confusion Matrix
# --------------------------------------------

print("\nGenerating Confusion Matrix...")

cm = confusion_matrix(
    y_test,
    y_pred
)

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

# --------------------------------------------
# Save Confusion Matrix Figure
# --------------------------------------------

plt.savefig(
    "../outputs/figures/confusion_matrix.png"
)

print("Confusion Matrix Saved!")

# Show Plot
plt.show()

print("\nEvaluation Completed Successfully!")