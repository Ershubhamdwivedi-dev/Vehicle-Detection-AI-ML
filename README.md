# 🚗 Car Detection System

Car Detection System is a real-time web application built using Python, Streamlit, and OpenCV that allows users to upload a video and automatically detect cars in each frame. The system uses a Haar Cascade Classifier to identify vehicles and display detection results interactively.

---

## 🚀 Features

- 📂 Upload video files (.mp4, .avi, .mov)
- 🚗 Detect cars in each frame using OpenCV
- 📊 Real-time detection status display
- 🔢 Live count of cars in each frame
- 🎥 Video playback with bounding boxes
- ⏹️ Auto-stop detection after 5 seconds
- ⚡ Fast and lightweight Streamlit UI

---

## 🧠 How It Works

- The user uploads a video from the sidebar  
- The video is processed frame-by-frame using OpenCV  
- A Haar Cascade classifier (`cars.xml`) is applied to detect cars  
- Bounding boxes are drawn around detected vehicles  
- The system displays:
  - Number of cars detected  
  - Detection status in real-time  
- The detection automatically stops after a fixed duration  

---

## 🛠️ Tech Stack

- 🐍 Python  
- 🌐 Streamlit  
- 🎥 OpenCV (cv2)  
- 📦 Haar Cascade Classifier  

---

## 📂 Project Structure

```
project/
│
├── app.py
├── cars.xml
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---


## 🌐 Applications

- 🚦 Traffic monitoring systems  
- 🅿️ Smart parking solutions  
- 🚗 Vehicle counting systems  
- 🛣️ Road surveillance  
- 🤖 Computer vision learning projects  

---

## 📌 Note

This project uses a Haar Cascade classifier, which is fast and lightweight but may not be as accurate as modern deep learning models like YOLO. It is ideal for learning and basic real-time detection tasks.

---

## 🔮 Future Improvements

- 🤖 Upgrade to YOLO-based detection  
- 🎥 Real-time webcam support  
- 📊 Vehicle tracking and analytics  
- 🌈 Enhanced UI/UX  
- ☁️ Cloud deployment  

---

## 🙌 Author

**Shubham Dwivedi**

---

## ⭐ Support

If you like this project, please ⭐ star the repository!
