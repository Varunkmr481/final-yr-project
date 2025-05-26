import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DLBAFRAS - Face Recognition Attendance System",
    page_icon=":face_with_monocle:",
    layout="wide",
)

# Custom CSS for additional styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-top: 20px;
        }
        .subtitle {
            font-size: 1.5em;
            color: #7f8c8d;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<div class='title'>DEEP LEARNING BASED FACE RECOGNITION</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Attendance System</div>", unsafe_allow_html=True)

# Horizontal divider
st.markdown("---")

# Content Section
st.write("Welcome to the **Deep Learning Based Face Recognition Attendance System** (DLBAFRAS).")
st.write("""
This system leverages cutting-edge **deep learning algorithms** to provide an accurate, efficient, and secure method 
for tracking attendance through facial recognition. Explore the features, and let technology simplify attendance management for you.
""")

# Add a placeholder for future components or interactivity
st.info("This is a placeholder for future components like uploading files, results, or interactive features.")

# Footer Section
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #95a5a6; font-size: 0.9em;'>
        © 2025 DLBAFRAS | Powered by Deep Learning
    </div>
""", unsafe_allow_html=True)
