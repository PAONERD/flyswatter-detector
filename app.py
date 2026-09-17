from flask import Flask, render_template, Response, jsonify
from src.detector import ThreatDetector
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)
detector = ThreatDetector()
last_state = {"threat": False, "confidence": 0.0}


def frames():
    global last_state
    while True:
        ok, frame = camera.read()
        if not ok:
            break
        frame, last_state = detector.process(frame)
        ok, encoded = cv2.imencode('.jpg', frame)
        if not ok:
            continue
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + encoded.tobytes() + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/state')
def state():
    return jsonify(last_state)


if __name__ == '__main__':
    app.run(debug=False, threaded=True)
