# flyswatter-detector

> Built for Henry-01 — 166,700 neurons, one priority: don't get swatted.

A tiny webcam threat detector made for the **Henry-01 fruit-fly vibe-coding experiment**.

The demo watches a live camera feed, looks for a fast moving long/thin object, draws a `FLYSWATTER` bounding box and switches the interface to `THREAT DETECTED`.

```text
camera
  ↓
motion + shape heuristics
  ↓
threat score
  ↓
SWATTER WATCH
  ↓
escape_response()
```

## Run it

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` and allow camera access.

## Project

```text
flyswatter-detector/
├── app.py
├── src/
│   ├── detector.py
│   └── threat.py
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
├── requirements.txt
└── README.md
```

## How detection works

This prototype intentionally stays small. It compares consecutive webcam frames, finds the largest moving contour, and treats a sufficiently large elongated object as a possible flyswatter-like threat.

It is **not a trained flyswatter classifier**. For production use, replace the heuristic in `src/detector.py` with a trained object-detection model.

## Henry-01

The repository is the software prop / working prototype used in the Henry-01 animation. The fruit-fly connectome does not literally type Python token-by-token; the experiment visualizes neural activity being mapped into higher-level computer actions.

**166,700 neurons. One problem. Don't get swatted.**
