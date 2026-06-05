Car Detection System (Streamlit + OpenCV)

A real-time Car Detection Web App built using Streamlit and OpenCV. This project allows users to upload a video and automatically detects cars using a Haar Cascade classifier.

Features =>
📂 Upload video files (.mp4, .avi, .mov)
🚗 Detect cars in each frame using OpenCV
📊 Real-time detection status display
🔢 Live count of cars in the frame
🎥 Video playback with bounding boxes
⏹️ Auto-stop after 5 seconds of detection
⚡ Fast and lightweight UI with Streamlit

Tech Stack =>
Python
Streamlit
OpenCV (cv2)
Haar Cascade Classifier

Project Structure =>
├── app.py
├── cars.xml
├── requirements.txt
└── README.md

How It Works =>
Upload a video from the sidebar
Frames are processed using OpenCV
Cars are detected using cars.xml Haar cascade
Bounding boxes are drawn around detected cars
Detection status and count are shown in real-time
