import streamlit as st

# --------------------------------------------
# PAGE CONFIG
# --------------------------------------------

st.set_page_config(
    page_title="Human Activity Recognition (Target)",
    page_icon="🏃",
    layout="wide"
)


# --------------------------------------------
# CUSTOM CSS
# --------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fbc2eb 0%, #a18cd1 100%);
}

[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.20);
    backdrop-filter: blur(10px);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* CARD DESIGN */

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.20);
    text-align: center;
    min-height: 180px;
}


/* BUTTON DESIGN */

.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: none;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg, #6A11CB, #2575FC);
    color: white;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #2575FC, #6A11CB);
    color: white;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------
# HEADER
# --------------------------------------------

st.markdown("""
<div style="
background: linear-gradient(90deg, #6A11CB, #2575FC);
padding: 30px;
border-radius: 20px;
text-align: center;
box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
">

<h1 style="color:white; font-size:42px;">
PULSEWELL AI
</h1>

<h3 style="color:white;">
A SMARTPHONE SENSOR-DRIVEN WELLNESS MONITORING SYSTEM WITH ACTIVITY RECOGNITION, FALL DETECTION AND CALORIE ESTIMATION
</h3>

<p style="color:white; font-size:17px;">

</p>

</div>
""", unsafe_allow_html=True)

st.write("")


# --------------------------------------------
# KPI CARDS
# --------------------------------------------

st.markdown("##  System Highlights")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        " Activities",
        "6"
    )

with col2:

    st.metric(
        " ML Models",
        "3"
    )

with col3:

    st.metric(
        " Best Accuracy",
        "98%"
    )

st.write("")


# ---------------------------------------------
# ACTIVITIES
# --------------------------------------------

st.markdown("##  Activities Recognized")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(" WALKING")

with col2:
    st.info("⬆ WALKING UPSTAIRS")

with col3:
    st.info("⬇ WALKING DOWNSTAIRS")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(" SITTING")

with col2:
    st.info(" STANDING")

with col3:
    st.info(" LAYING")

st.write("")


# --------------------------------------------
# NAVIGATION SECTION
# --------------------------------------------

st.markdown("##  Explore the System")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

    <h2> Model Comparison</h2>

    <p>
    Compare Random Forest, SVM and KNN
    models based on their accuracy.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        " View Model Comparison",
        use_container_width=True
    ):

        st.switch_page(
            "pages/1_Model_Comparison.py"
        )


with col2:

    st.markdown("""
    <div class="card">

    <h2> Activity Prediction</h2>

    <p>
    Select a smartphone sensor sample
    and predict the human activity.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        " Start Activity Prediction",
        use_container_width=True
    ):

        st.switch_page(
            "pages/2_Prediction.py"
        )


# --------------------------------------------
# FOOTER
# --------------------------------------------

st.write("")

st.markdown("---")

st.markdown("""

<center>

###  PULSEWELL AI

</center>

""", unsafe_allow_html=True)
