from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import os
import cv2
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)

# Load YOLOv8 model (your trained model)
model = YOLO("yolov8.pt")

# Ensure a folder exists for temporary files
UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Marine Biodiversity Analyzer API is running."

@app.route('/analyze', methods=['POST'])
def analyze_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    detected_species = []

    try:
        # 🔍 If it's an image
        if file.content_type.startswith("image"):
            img = Image.open(filename)
            results = model(img)
        # 🎥 If it's a video
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

        # If it's an image, results is a list with one result
        if file.content_type.startswith("image"):
            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    detected_species.append(model.names[cls])

        # Remove duplicates
        unique_species = list(set(detected_species))

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(filename)  # Cleanup

    return jsonify({"species_detected": unique_species})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
