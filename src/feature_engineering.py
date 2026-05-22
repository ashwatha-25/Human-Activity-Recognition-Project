# ============================================
# feature_engineering.py
# ============================================

print("Feature Engineering File Started")

import pandas as pd

# --------------------------------------------
# Feature Engineering Function
# --------------------------------------------

def create_features(df):

    print("Creating Features...")

    # Example Feature
    if 'acc_x' in df.columns and 'acc_y' in df.columns:

        df['acc_magnitude'] = (
            df['acc_x']**2 +
            df['acc_y']**2
        ) ** 0.5

        print("acc_magnitude Feature Created!")

    else:

        print("acc_x and acc_y columns not found")

    return df

# ============================================
# MAIN PROGRAM
# ============================================

print("Loading Dataset...")

# Load Dataset
df = pd.read_csv("../data/train.csv")

print("Dataset Loaded Successfully!")

# Apply Feature Engineering
df = create_features(df)

print("Feature Engineering Completed!")

# Show First 5 Rows
print(df.head())

print("Program Finished Successfully!")