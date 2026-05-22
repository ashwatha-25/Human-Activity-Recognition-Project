# ============================================
# 03_model_training.py
# Compare Random Forest, SVM, and KNN
# ============================================

print("Program Started")

import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error
)

# --------------------------------------------
# Load Processed Data
# --------------------------------------------

train_df = pd.read_csv("../outputs/processed_train.csv")
test_df = pd.read_csv("../outputs/processed_test.csv")

print("Processed Data Loaded Successfully!")

# --------------------------------------------
# Check Columns
# --------------------------------------------

print("Columns in Dataset:")
print(train_df.columns)

# --------------------------------------------
# Target Column
# --------------------------------------------

target_column = "Activity"

# --------------------------------------------
# Split Features and Labels
# --------------------------------------------

X_train = train_df.drop(target_column, axis=1)
y_train = train_df[target_column]

X_test = test_df.drop(target_column, axis=1)
y_test = test_df[target_column]

print("Feature and Label Split Completed!")

# --------------------------------------------
# Create Models
# --------------------------------------------

models = {

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "SVM": SVC(
        kernel='rbf'
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    )
}

# --------------------------------------------
# Store Results
# --------------------------------------------

results = []

best_accuracy = 0
best_model = None
best_model_name = ""

# --------------------------------------------
# Train and Evaluate Each Model
# --------------------------------------------

for model_name, model in models.items():

    print("\n===================================")
    print(f"Training {model_name}")
    print("===================================")

    # Train model
    model.fit(X_train, y_train)

    print(f"{model_name} Training Completed!")

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Precision
    precision = precision_score(
        y_test,
        y_pred,
        average='weighted'
    )

    # Recall
    recall = recall_score(
        y_test,
        y_pred,
        average='weighted'
    )

    # F1 Score
    f1 = f1_score(
        y_test,
        y_pred,
        average='weighted'
    )

    # Mean Absolute Error
    mae = mean_absolute_error(y_test, y_pred)

    # Print Results
    print(f"Accuracy  : {accuracy * 100:.2f}%")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    print(f"MAE       : {mae:.4f}")

    # Save results
    results.append([
        model_name,
        accuracy,
        precision,
        recall,
        f1,
        mae
    ])

    # Save best model
    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_model = model
        best_model_name = model_name

# --------------------------------------------
# Save Best Model
# --------------------------------------------

joblib.dump(
    best_model,
    "../models/best_model.pkl"
)

print("\n===================================")
print(f"Best Model: {best_model_name}")
print(f"Best Accuracy: {best_accuracy * 100:.2f}%")
print("Best Model Saved Successfully!")
print("===================================")

# --------------------------------------------
# Save Results to Text File
# --------------------------------------------

with open("../outputs/reports/model_results.txt", "w") as file:

    file.write("MODEL COMPARISON RESULTS\n")
    file.write("=============================\n\n")

    for result in results:

        file.write(f"Model      : {result[0]}\n")
        file.write(f"Accuracy   : {result[1] * 100:.2f}%\n")
        file.write(f"Precision  : {result[2]:.4f}\n")
        file.write(f"Recall     : {result[3]:.4f}\n")
        file.write(f"F1 Score   : {result[4]:.4f}\n")
        file.write(f"MAE        : {result[5]:.4f}\n")
        file.write("\n-------------------------\n\n")

print("Results Saved Successfully!")

print("Program Finished Successfully!")