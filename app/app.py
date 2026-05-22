import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------
# Load Model
# --------------------------------------------

model = joblib.load(
    "../models/best_model.pkl"
)

# --------------------------------------------
# Load Dataset
# --------------------------------------------

df = pd.read_csv(
    "../outputs/processed_test.csv"
)

# --------------------------------------------
# Title
# --------------------------------------------

st.title("Human Activity Recognition System")

st.write(
    "Predict Human Activity Using Dataset Samples"
)

# --------------------------------------------
# Select Sample Row
# --------------------------------------------

row_number = st.number_input(
    "Enter Row Number",
    min_value=0,
    max_value=len(df)-1,
    value=0
)

# --------------------------------------------
# Target Column
# --------------------------------------------

target_column = "Activity"

# --------------------------------------------
# Remove Target Column
# --------------------------------------------

X = df.drop(
    target_column,
    axis=1
)

# --------------------------------------------
# Get Selected Sample
# --------------------------------------------

sample = X.iloc[[row_number]]

# --------------------------------------------
# Calories Mapping
# --------------------------------------------

calorie_map = {

    "Walking": 250,
    "Walking Upstairs": 400,
    "Walking Downstairs": 300,
    "Sitting": 80,
    "Standing": 100,
    "Laying": 60
}

# --------------------------------------------
# Prediction Button
# --------------------------------------------

if st.button("Predict Activity"):

    # ----------------------------------------
    # Predict Activity
    # ----------------------------------------

    prediction = model.predict(sample)

    # ----------------------------------------
    # Activity Labels
    # ----------------------------------------

    activity_labels = {

        0: "Walking",
        1: "Walking Upstairs",
        2: "Walking Downstairs",
        3: "Sitting",
        4: "Standing",
        5: "Laying"
    }

    predicted_activity = activity_labels.get(
        prediction[0],
        prediction[0]
    )

    # ----------------------------------------
    # Show Prediction
    # ----------------------------------------

    st.success(
        f"Predicted Activity: {predicted_activity}"
    )

    # ----------------------------------------
    # Actual Activity
    # ----------------------------------------

    actual_activity = df.iloc[row_number][target_column]

    st.info(
        f"Actual Activity Label: {actual_activity}"
    )

    # ----------------------------------------
    # Fall Detection
    # ----------------------------------------

    try:

        acc_x = sample['tBodyAcc-mean()-X'].values[0]
        acc_y = sample['tBodyAcc-mean()-Y'].values[0]
        acc_z = sample['tBodyAcc-mean()-Z'].values[0]

        magnitude = (
            acc_x**2 +
            acc_y**2 +
            acc_z**2
        ) ** 0.5

        st.write(
            f"Acceleration Magnitude: {magnitude:.4f}"
        )

        # Threshold Check

        if magnitude > 0.2:

            st.error("⚠️ Fall Detected!")

        else:

            st.success("✅ No Fall Detected")

    except:

        st.warning(
            "Fall Detection Features Not Found"
        )

    # ----------------------------------------
    # Calorie Estimation
    # ----------------------------------------

    estimated_calories = calorie_map.get(
        predicted_activity,
        0
    )

    st.info(
        f"🔥 Estimated Calories Burned: {estimated_calories} kcal/hour"
    )

# --------------------------------------------
# Display Sample Features
# --------------------------------------------

st.subheader("Selected Sample Features")

st.dataframe(sample)
