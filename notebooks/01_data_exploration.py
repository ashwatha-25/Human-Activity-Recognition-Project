# ============================================
# 01_data_exploration.py
# Human Activity Recognition Project
# ============================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# Load Dataset
# --------------------------------------------

train_path = "../data/train.csv"
test_path = "../data/test.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# --------------------------------------------
# Basic Information
# --------------------------------------------

print("\n===== TRAIN DATASET INFO =====")
print(train_df.info())

print("\n===== TEST DATASET INFO =====")
print(test_df.info())

# --------------------------------------------
# Display First 5 Rows
# --------------------------------------------

print("\n===== FIRST 5 ROWS OF TRAIN DATA =====")
print(train_df.head())

print("\n===== FIRST 5 ROWS OF TEST DATA =====")
print(test_df.head())

# --------------------------------------------
# Dataset Shape
# --------------------------------------------

print("\n===== DATASET SHAPE =====")
print(f"Train Shape : {train_df.shape}")
print(f"Test Shape  : {test_df.shape}")

# --------------------------------------------
# Missing Values
# --------------------------------------------

print("\n===== MISSING VALUES =====")
print(train_df.isnull().sum())

# --------------------------------------------
# Statistical Summary
# --------------------------------------------

print("\n===== STATISTICAL SUMMARY =====")
print(train_df.describe())

# --------------------------------------------
# Class Distribution
# --------------------------------------------

# Replace 'Activity' with your target column name
target_column = "Activity"

print("\n===== CLASS DISTRIBUTION =====")
print(train_df[target_column].value_counts())

# --------------------------------------------
# Plot Class Distribution
# --------------------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    x=train_df[target_column],
    palette="viridis"
)

plt.title("Activity Distribution")
plt.xlabel("Activities")
plt.ylabel("Count")
plt.xticks(rotation=45)

# Save Figure
plt.savefig("../outputs/activity_distribution.png")

plt.show()

# --------------------------------------------
# Correlation Heatmap
# --------------------------------------------

# Select only numeric columns
numeric_df = train_df.select_dtypes(include=['float64', 'int64'])

# Reduce columns if dataset is very large
corr_matrix = numeric_df.corr()

plt.figure(figsize=(12, 10))

sns.heatmap(
    corr_matrix,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")

# Save Heatmap
plt.savefig("../outputs/correlation_heatmap.png")

plt.show()

# --------------------------------------------
# Output Message
# --------------------------------------------

print("\nData Exploration Completed Successfully!")
print("Graphs saved in outputs folder.")