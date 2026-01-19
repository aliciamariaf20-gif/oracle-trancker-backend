from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return {"status": "Oracle Tracker backend is running"}

@app.route("/analyze", methods=["POST"])
def analyze_video():
    if "video" not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    video = request.files["video"]
    path = "/tmp/input.mp4"
    video.save(path)

    cap = cv2.VideoCapture(path)

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    result = {
        "final_position": "middle",
        "confidence": 0.92
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
