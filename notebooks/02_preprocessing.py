import pandas as pd

print("Program Started")

# Load datasets
train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

print("Datasets Loaded Successfully!")

# Show first rows
print(train_df.head())

# Save test output
train_df.to_csv("outputs/sample_output.csv", index=False)

print("Output Saved Successfully!")