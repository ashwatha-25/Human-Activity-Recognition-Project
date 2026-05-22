import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix

# --------------------------------------------
# PAGE CONFIG MUST BE FIRST
# --------------------------------------------

st.set_page_config(
    page_title="HAR System",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #fbc2eb 0%,
            #a18cd1 100%
        );
    }

    section[data-testid="stSidebar"] {
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(10px);
    }

    h1, h2, h3 {
        color: white;
    }

    .stButton>button {
        background-color: white;
        color: #7B2CBF;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 10px 20px;
    }

    .stButton>button:hover {
        background-color: #f3e8ff;
        color: #5A189A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

st.title("Prediction Dashboard")

# --------------------------------------------
# Target Column
# --------------------------------------------

target_column = "Activity"

# --------------------------------------------
# Features and Labels
# --------------------------------------------

X = df.drop(target_column, axis=1)
y = df[target_column]

# --------------------------------------------
# Row Selection
# --------------------------------------------

row_number = st.number_input(
    "Enter Row Number",
    min_value=0,
    max_value=len(df)-1,
    value=0
)

# --------------------------------------------
# Get Selected Sample
# --------------------------------------------

sample = X.iloc[[row_number]]

# --------------------------------------------
# Display Selected Sample
# --------------------------------------------

st.subheader("Selected Sample Features")

st.dataframe(sample)

# --------------------------------------------
# Predict Button
# --------------------------------------------

if st.button("Predict Activity"):

    # ----------------------------------------
    # Prediction
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
        5: "Laying",
        6: "Fall"
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

    actual_activity_name = activity_labels.get(
        actual_activity,
        actual_activity
    )

    st.info(
        f"Actual Activity: {actual_activity_name}"
    )

    # ----------------------------------------
    # Fall Detection
    # ----------------------------------------

    try:

        # Accelerometer Features
        acc_x = sample['tBodyAcc-mean()-X'].values[0]
        acc_y = sample['tBodyAcc-mean()-Y'].values[0]
        acc_z = sample['tBodyAcc-mean()-Z'].values[0]

        # Magnitude Calculation
        magnitude = (
            acc_x**2 +
            acc_y**2 +
            acc_z**2
        ) ** 0.5

        # Display Magnitude
        st.write(
            f"Acceleration Magnitude: {magnitude:.4f}"
        )

        # Better Threshold
        if magnitude > 0.2:

            st.error("⚠️ Fall Detected!")

        else:

            st.success("✅ No Fall Detected")

    except:

        st.warning(
            "Accelerometer Features Not Found"
        )

    # ----------------------------------------
    # Calorie Estimation
    # ----------------------------------------

    calorie_map = {

        "Walking": 250,
        "Walking Upstairs": 400,
        "Walking Downstairs": 300,
        "Sitting": 80,
        "Standing": 100,
        "Laying": 60,
        "Fall": 0
    }

    calories = calorie_map.get(
        predicted_activity,
        0
    )

    st.warning(
        f"🔥 Estimated Calories Burned: {calories} kcal/hour"
    )

    # ----------------------------------------
    # Confusion Matrix Heatmap
    # ----------------------------------------

    st.subheader("Confusion Matrix Heatmap")

    # Predictions on Full Dataset
    y_pred = model.predict(X)

    # Confusion Matrix
    cm = confusion_matrix(y, y_pred)

    # Plot Heatmap
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=ax
    )

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")

    # Display Heatmap
    st.pyplot(fig)