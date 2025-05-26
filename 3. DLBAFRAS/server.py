from flask import Flask, Response
import cv2
import threading
import time
from Home import face_rec  # Import your face recognition module

app = Flask(__name__)

# Global Variables
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
frame = None
lock = threading.Lock()

# Load Face Recognition Model
redis_face_db = face_rec.retrieve_data("sharda")
realtimepred = face_rec.RealTimePred()

# Set Log Saving Time
waitTime = 30
setTime = time.time()

# Function to Capture Frames in a Separate Thread
def capture_frames():
    global frame, setTime
    while True:
        success, img = camera.read()
        if not success:
            continue
        
        # Perform Face Recognition
        pred_frame = realtimepred.face_prediction(img, redis_face_db, "facial_features", ['Name', 'Role'], thresh=0.5)

        # Save logs every 30 seconds
        timenow = time.time()
        if timenow - setTime >= waitTime:
            realtimepred.saveLogsInRedis()
            setTime = time.time()

        # Store latest frame
        with lock:
            frame = pred_frame

# Start a Background Thread for Capturing Frames
thread = threading.Thread(target=capture_frames, daemon=True)
thread.start()

# Function to Stream Frames
def generate_frames():
    global frame
    while True:
        with lock:
            if frame is None:
                continue
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
