from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import os
import urllib.request
import cv2
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)

# 🔽 Model setup
MODEL_PATH = "yolov8.pt"
MODEL_URL = "https://drive.google.com/uc?export=download&id=1qcicVZrldCzKt4dbP7017IG83b5d-gPq"

# Download the model if it doesn’t exist yet
if not os.path.exists(MODEL_PATH):
    print("Downloading YOLOv8 model from Google Drive...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Model download completed.")

# Load the YOLO model
model = YOLO(MODEL_PATH)

# Temporary upload folder
UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "✅ Marine Biodiversity Analyzer API is running."

@app.route('/analyze', methods=['POST'])
def analyze_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    detected_species = []

    try:
        # Image handling
        if file.content_type.startswith("image"):
            img = Image.open(filename)
            results = model(img)
            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    detected_species.append(model.names[cls])

        # Video handling
        elif file.content_type.startswith("video"):
            cap = cv2.VideoCapture(filename)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                results = model(frame)
                for r in results:
                    for box in r.boxes:
                        cls = int(box.cls[0])
                        detected_species.append(model.names[cls])
            cap.release()

        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        unique_species = list(set(detected_species))

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(filename)

    return jsonify({"species_detected": unique_species})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

