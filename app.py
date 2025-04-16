from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import cv2

app = Flask(__name__)

# Load YOLOv8 model
model = YOLO("yolov8.pt")

# Make sure temp folder exists
os.makedirs("temp", exist_ok=True)


@app.route('/')
def home():
    return "Marine Biodiversity Monitoring API is running."


@app.route('/analyze', methods=['POST'])
def analyze_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No video uploaded'}), 400

    file = request.files['file']
    filepath = os.path.join("temp", file.filename)
    file.save(filepath)

    cap = cv2.VideoCapture(filepath)
    detected_species = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        names = model.names
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0])
                detected_species.append(names[cls])

    cap.release()
    os.remove(filepath)

    return jsonify({"species_detected": list(set(detected_species))})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
