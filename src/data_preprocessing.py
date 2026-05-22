# ============================================
# data_preprocessing.py
# ============================================

import pandas as pd

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)

print("File Loaded Successfully")

# --------------------------------------------
# Load Dataset
# --------------------------------------------

def load_data(train_path, test_path):

    print("Loading datasets...")

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    print("Datasets Loaded!")

    return train_df, test_df

# --------------------------------------------
# Preprocess Dataset
# --------------------------------------------

def preprocess_data(train_df, test_df, target_column):

    print("Preprocessing Started...")

    # Handle Missing Values
    train_df = train_df.fillna(
        train_df.mean(numeric_only=True)
    )

    test_df = test_df.fillna(
        test_df.mean(numeric_only=True)
    )

    # Label Encoding
    encoder = LabelEncoder()

    train_df[target_column] = encoder.fit_transform(
        train_df[target_column]
    )

    test_df[target_column] = encoder.transform(
        test_df[target_column]
    )

    # Split Features and Labels
    X_train = train_df.drop(target_column, axis=1)
    y_train = train_df[target_column]

    X_test = test_df.drop(target_column, axis=1)
    y_test = test_df[target_column]

    # Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Preprocessing Completed!")

    return X_train, X_test, y_train, y_test

# ============================================
# MAIN PROGRAM
# ============================================

print("Main Program Started")

train_df, test_df = load_data(
    "../data/train.csv",
    "../data/test.csv"
)

X_train, X_test, y_train, y_test = preprocess_data(
    train_df,
    test_df,
    "Activity"
)

print("Program Finished Successfully!")