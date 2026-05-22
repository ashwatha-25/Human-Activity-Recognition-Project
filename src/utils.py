# ============================================
# utils.py
# ============================================

print("Utils File Loaded Successfully")

import os
import joblib
import pandas as pd

# --------------------------------------------
# Create Folder
# --------------------------------------------

def create_folder(folder_path):

    if not os.path.exists(folder_path):

        os.makedirs(folder_path)

        print(f"Folder Created: {folder_path}")

    else:

        print(f"Folder Already Exists: {folder_path}")

# --------------------------------------------
# Save CSV File
# --------------------------------------------

def save_csv(df, file_path):

    df.to_csv(file_path, index=False)

    print(f"CSV File Saved: {file_path}")

# --------------------------------------------
# Load CSV File
# --------------------------------------------

def load_csv(file_path):

    df = pd.read_csv(file_path)

    print(f"CSV File Loaded: {file_path}")

    return df

# --------------------------------------------
# Save Model
# --------------------------------------------

def save_model(model, file_path):

    joblib.dump(model, file_path)

    print(f"Model Saved: {file_path}")

# --------------------------------------------
# Load Model
# --------------------------------------------

def load_model(file_path):

    model = joblib.load(file_path)

    print(f"Model Loaded: {file_path}")

    return model

# --------------------------------------------
# Save Text Report
# --------------------------------------------

def save_report(text, file_path):

    with open(file_path, "w") as file:

        file.write(text)

    print(f"Report Saved: {file_path}")

# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":

    print("Utils File Running Successfully!")

    # Example Folder Creation
    create_folder("../outputs/test_folder")

    print("Utils Program Finished!")