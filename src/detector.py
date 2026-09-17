import cv2
import numpy as np


class ThreatDetector:
    def __init__(self):
        self.prev = None

    def process(self, frame):
        small = cv2.resize(frame, (640, 360))
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 0)

        threat = False
        confidence = 0.0
        box = None

        if self.prev is not None:
            diff = cv2.absdiff(self.prev, gray)
            _, mask = cv2.threshold(diff, 28, 255, cv2.THRESH_BINARY)
            mask = cv2.dilate(mask, None, iterations=2)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                c = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(c)
                x, y, w, h = cv2.boundingRect(c)
                long_thin = max(w, h) / max(1, min(w, h)) > 2.0
                large = area > 9000
                if large and long_thin:
                    threat = True
                    confidence = min(0.99, 0.70 + area / 120000)
                    box = (x, y, w, h)

        self.prev = gray

        if box:
            x, y, w, h = box
            sx, sy = frame.shape[1] / 640, frame.shape[0] / 360
            p1 = (int(x * sx), int(y * sy))
            p2 = (int((x + w) * sx), int((y + h) * sy))
            cv2.rectangle(frame, p1, p2, (0, 0, 255), 3)
            cv2.putText(
                frame,
                f"FLYSWATTER {confidence*100:.1f}%",
                (p1[0], max(30, p1[1]-12)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.85,
                (0, 0, 255),
                2,
            )

        return frame, {"threat": threat, "confidence": round(confidence, 3)}
