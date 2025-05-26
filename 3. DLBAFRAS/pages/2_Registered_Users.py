import cv2
import streamlit as st
from Home import face_rec
import time

st.set_page_config(page_title="registered users", layout="centered")

# Custom CSS for styling the page
st.markdown(
    """
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #2c3e50;
            font-weight: bold;
            text-align: center;
            margin-bottom: 1rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background: linear-gradient(45deg, #FF5733, #FFD700, #4CAF50, #2980b9, #9b59b6);
            -webkit-background-clip: text;
            color: transparent;
            animation: gradient-animation 5s ease infinite;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #34495e;
            text-align: center;
            margin-bottom: 2rem;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSpinner>div {
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
        }
        .stTextInput>label {
            font-weight: bold;
            font-size: 1rem;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #888;
            margin-top: 2rem;
            border-top: 1px solid #ddd;
            padding-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and Sub-header
st.markdown("<div class='main-header'>REGISTERED USERS</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Efficient and Secure Attendance Management Using AI</div>", unsafe_allow_html=True)


# 1. Retrieve data from redis database
# database name : "sharda"

st.markdown("### Data of registered users", unsafe_allow_html=True)
with st.spinner("Retrieving data from database ...."):
    redis_face_db = face_rec.retrieve_data("sharda")
    st.dataframe(redis_face_db)

st.success("Data successfully retrieved from database...")

# Footer with branding
st.markdown(
    """
    <div class='footer'>
        Powered by <strong>DLBAFRAS</strong> | Transforming Attendance Systems with AI
    </div>
    """,
    unsafe_allow_html=True
)