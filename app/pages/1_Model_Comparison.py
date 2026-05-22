import streamlit as st
import matplotlib.pyplot as plt

# --------------------------------------------
# PAGE CONFIG (ONLY ONCE)
# --------------------------------------------

st.set_page_config(
    page_title="Model Comparison",
    layout="wide"
)

# --------------------------------------------
# BACKGROUND STYLE
# --------------------------------------------

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
        text-align: center;
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
# TITLE
# --------------------------------------------

st.title("Model Accuracy Comparison")

# --------------------------------------------
# MODEL ACCURACY DATA
# --------------------------------------------

models = [
    "Random Forest",
    "SVM",
    "KNN"
]

accuracies = [
    96,
    98,
    94
]

# --------------------------------------------
# CREATE BAR CHART
# --------------------------------------------

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(models, accuracies)

ax.set_xlabel("Models")
ax.set_ylabel("Accuracy (%)")
ax.set_title("Machine Learning Model Comparison")

# --------------------------------------------
# DISPLAY CHART
# --------------------------------------------

st.pyplot(fig)

# --------------------------------------------
# NEXT BUTTON
# --------------------------------------------

col1, col2 = st.columns([9, 1])

with col2:

    if st.button("Next ➜"):

        st.switch_page(
            "pages/2_Prediction.py"
        )