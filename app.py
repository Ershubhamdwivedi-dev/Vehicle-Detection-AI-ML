import streamlit as st
import cv2
import tempfile
import time

# Page Config
st.set_page_config(page_title="🚗 Car Detection App", layout="wide")

# Title
st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>🚗 Car Detection System</h1>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
st.sidebar.header("⚙️ Settings")
uploaded_file = st.sidebar.file_uploader("📂 Upload Video", type=["mp4", "avi", "mov"])

# Load Haar Cascade
car_cascade = cv2.CascadeClassifier('cars.xml')

if car_cascade.empty():
    st.error("❌ Error loading cars.xml file")
    st.stop()

# Layout
col1, col2 = st.columns([3,1])

with col1:
    st.subheader("📺 Video Output")
    stframe = st.empty()

with col2:
    st.subheader("📊 Detection Info")
    status_box = st.empty()
    count_box = st.empty()

if uploaded_file is not None:
    # Save video
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)

    if not cap.isOpened():
        st.error("❌ Error opening video")
        st.stop()

    car_detected = False
    detection_time = 0
    total_cars = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.success("✅ Video Finished")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 3)

        total_cars = len(cars)

        # Detection Logic
        if total_cars > 0:
            if not car_detected:
                car_detected = True
                detection_time = time.time()

            status_box.success("🚗 Car Detected!")
        else:
            status_box.info("🔍 No Car Detected")

        # Stop after 5 sec
        if car_detected and (time.time() - detection_time > 5):
            status_box.warning("⏹️ Stopped after detection")
            break

        # Show count
        count_box.metric("🚘 Cars in Frame", total_cars)

        # Draw boxes
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

        # Convert color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display video
        stframe.image(frame, channels="RGB", use_container_width=True)

    cap.release()

else:
    st.info("⬅️ Please upload a video from sidebar")