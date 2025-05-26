import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.add_vertical_space import add_vertical_space


# set page configuration
st.set_page_config(
    page_title="DLBAFRAS - Face Recognition Attendance System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f7f6;
            font-family: 'Arial', sans-serif;
        }
        .main-header {
            font-size: 3rem;
            text-align: center;
            font-weight: bold;
            margin-bottom: 1rem;
            padding: 5px 0;
            background-color: #4CAF50;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background: linear-gradient(45deg, #FF5733, #FFD700, #4CAF50, #2980b9, #9b59b6);
            -webkit-background-clip: text;
            color: transparent;
            animation: gradient-animation 5s ease infinite;
        }
        
        @keyframes gradient-animation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .sub-header {
            font-size: 1.8rem;
            color: #34495e;
            text-align: center;
            margin-bottom: 2rem;
            font-style: italic;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and Sub-header
st.markdown("<div class='main-header'>DEEP LEARNING BASED FACE RECOGNITION ATTENDANCE SYSTEM</div>", unsafe_allow_html=True)

st.markdown("<div class='sub-header'>Efficient and Secure Attendance Management using AI</div>", unsafe_allow_html=True)


with st.spinner("Loading model and connecting to database ...."):
    import face_rec
    
# Success messages with emojis for appeal
st.success("\U0001F916 Model loaded successfully!")
st.success("\U0001F4C2 Database successfully connected!")

# Add decorative elements
add_vertical_space(2)
rain(
    emoji="\U0001F44B",  # Waving hand emoji
    font_size=20,
    falling_speed=7,
    animation_length="infinite"
)

# Footer with branding
st.markdown(
    """
    <hr style='border: 1px solid #ddd;'>
    <div style='text-align: center; font-size: 0.9rem; color: #888;'>
        Powered by DLBAFRAS | Transforming Attendance Systems with AI
    </div>
    """,
    unsafe_allow_html=True
)
