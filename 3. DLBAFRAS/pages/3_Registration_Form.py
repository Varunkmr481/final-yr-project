import streamlit as st
import cv2
from Home import face_rec
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av

st.set_page_config(page_title="registration form", layout="centered")
st.subheader("REGISTRATION FORM")

# init registration form
registration_form = face_rec.RegistrationForm()

# COLLECT PERSON NAME AND ROLE
person_name = st.text_input(label="Name :", placeholder="Enter first and last name separated by space")
role = st.selectbox(label="Select your role :", options=('Student', 'Teacher'))

# COLLECT FACIAL EMBEDDING OF THE PERSON
def video_callback_func(frame):
    img = frame.to_ndarray(format='bgr24')
    reg_img, embedding = registration_form(img)

    return av.VideoFrame.from_ndarray(reg_img, format='bgr24')

webrtc_streamer(key='registration', video_frame_callback=video_callback_func)

# SAVE THE DATA IN REDIS DATABASE

if st.button("Submit"):
    st.write(f'Person name = ',person_name)
    st.write(f'Your role = ', role)
