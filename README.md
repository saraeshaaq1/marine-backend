# 🐠 Marine Biodiversity Monitoring with YOLOv8

This project uses a YOLOv8 deep learning model and a Flask API to automatically detect marine species in underwater videos.

It is part of a larger system for marine biodiversity monitoring, where users can upload underwater footage and get instant AI-based analysis of fish and marine life.

---

## 📌 What This Project Does

- 🧠 Runs a YOLOv8 object detection model trained on marine species
- 🎥 Accepts video uploads via a POST API endpoint (`/analyze`)
- 🐟 Returns a list of detected species from the video
- 🔁 Works with a front-end dashboard to upload videos and view results

---

## 🛠 Technologies Used

- Python + Flask
- YOLOv8 (Ultralytics)
- OpenCV (for reading video frames)
- Render (to host the backend API)
- HTML (frontend dashboard – coming soon!)

---

## 🚀 How to Use

1. Clone this repository
2. Place your `yolov8.pt` model in the project root
3. Install the dependencies:
4. Run the server:
5. Use `/analyze` endpoint to upload a video and receive predictions

---

## 🌍 Live API on Render

Once deployed, the API will be live at:
https://marine-backend-s8fq.onrender.com

Use this URL in your HTML dashboard to send video files.

---

## 📂 File Structure

## 👩‍💻 Developed by

**Sara Eshaaq & Team**  
Project: *Utilization of Deep Learning for Marine Biodiversity Monitoring*  
Year: 2025

