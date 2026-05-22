import streamlit as st

# --------------------------------------------
# PAGE CONFIG
# --------------------------------------------

st.set_page_config(
    page_title="HAR System",
    layout="wide"
)

# ----------------------------------------------
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

    h1 {
        text-align: center;
        color: white;
        font-size: 65px;
        margin-top: 40px;
        font-weight: bold;
    }

    .stButton>button {
        background-color: white;
        color: #7B2CBF;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        padding: 10px 25px;
        font-size: 18px;
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

st.markdown(
    """
    <h1>
        Human Activity Recognition System
    </h1>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------
# IMAGE
# --------------------------------------------

st.image(
    "images/har_image.png",
    use_container_width=True
)

# --------------------------------------------
# NEXT BUTTON
# --------------------------------------------

col1, col2, col3 = st.columns([8, 1, 1])

with col3:

    if st.button("Next ➜"):

        st.switch_page(
            "pages/1_Model_Comparison.py")
        