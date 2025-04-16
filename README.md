# 🐠 Marine Biodiversity Monitoring with YOLOv8

This project uses a YOLOv8 deep learning model and a Flask API to automatically detect marine species in underwater **images and videos**.

It is part of a larger system for marine biodiversity monitoring, where users can upload marine media and get instant AI-based analysis of fish and marine life.

---

## 📌 What This Project Does

- 🧠 Runs a YOLOv8 object detection model trained on marine species
- 🖼️ Accepts **images** or 🎥 **videos** via a POST API endpoint (`/analyze`)
- 🐟 Returns a list of detected species
- 🌐 Supports integration with a front-end HTML dashboard hosted on GitHub Pages

---

## 🛠 Technologies Used

- Python + Flask
- YOLOv8 (Ultralytics)
- OpenCV (`cv2`)
- PIL (for image processing)
- Render (to host the backend)
- GitHub Pages (for the frontend UI)

---

## 🚀 How to Use

1. **Clone this repository**
2. Place your trained YOLOv8 model file as `yolov8.pt` in the project root
3. Install the required libraries:
pip install -r requirements.txt

markdown
نسخ
تحرير
4. Run the backend server:
python app.py

yaml
نسخ
تحرير
5. Use a tool like Postman or your frontend to send a `POST` request to `/analyze` with a file (`image` or `video`)

---

## 🌍 Live API on Render

https://marine-backend-s8fq.onrender.com/analyze

yaml
نسخ
تحرير

Use this URL in your HTML dashboard or test script to send media files and receive predictions.

---

## 📂 File Structure

marine-backend/ ├── app.py # Flask server with YOLOv8 integration ├── yolov8.pt # Trained YOLOv8 model (placed here manually) ├── requirements.txt # Python dependencies └── temp/ # Folder for temporary video/image uploads

yaml
نسخ
تحرير

---

## 👩‍💻 Developed by

**Sara Eshaaq & Team**  
Project: *Utilization of Deep Learning for Marine Biodiversity Monitoring*  
Year: 202
