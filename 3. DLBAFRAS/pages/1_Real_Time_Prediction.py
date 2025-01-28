import cv2
from Home import st
from Home import face_rec
import time

st.set_page_config(page_title="real time attendance", layout="centered")

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
        }
        .sub-header {
            font-size: 1.5rem;
            color: #34495e;
            text-align: center;
            margin-bottom: 2rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 1.1rem;
            border-radius: 8px;
            padding: 10px 20px;
            margin-top: 1rem;
            border: none;
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
st.markdown("<div class='main-header'>REAL TIME PREDICTION</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Efficient and Secure Attendance Management Using AI</div>", unsafe_allow_html=True)


# 1. Retrieve data from redis database
# database name : "sharda"

st.markdown("### Data Retrieved from Database", unsafe_allow_html=True)
with st.spinner("Retrieving data from database ...."):
    redis_face_db = face_rec.retrieve_data("sharda")
    st.dataframe(redis_face_db)

st.success("Data successfully retrieved from database...")


# 2. Real time prediction

# waitTime (sec)
waitTime = 30
setTime = time.time()
realtimepred = face_rec.RealTimePred()

def real_time_attendance():
    global setTime

    # Initialize OpenCV camera
    camera_index = 1
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        st.error(f"Camera at index {camera_index} is not accessible.")
        return

    # Streamlit placeholder to display frames
    frame_placeholder = st.empty()

    st.info("Press 'Stop' to end the video stream.")
    stop_button = st.button("Stop")

    while not stop_button:
        ret, frame = cap.read()
        if not ret:
            st.warning("Failed to capture video. Exiting...")
            break

        # Perform face prediction
        pred_frame = realtimepred.face_prediction(frame, redis_face_db, "facial_features", ['Name', 'Role'], thresh=0.5)

        # Save logs at regular intervals
        timenow = time.time()
        difftime = timenow - setTime
        if difftime >= waitTime:
            realtimepred.saveLogsInRedis()
            setTime = time.time()
            print("Data saved to Redis database")

        # Convert BGR to RGB and display the frame in Streamlit
        frame_rgb = cv2.cvtColor(pred_frame, cv2.COLOR_BGR2RGB)
        
        frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

    # Release the camera and clean up
    cap.release()
    cv2.destroyAllWindows()

# Run the real-time attendance system
if st.button("Start Real-Time Attendance"):
    real_time_attendance()
    
# Footer with branding
st.markdown(
    """
    <div class='footer'>
        Powered by DLBAFRAS | Transforming Attendance Systems with AI
    </div>
    """,
    unsafe_allow_html=True
)