from pathlib import Path
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "weights" / "best.pt"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

hazard_model = YOLO(str(MODEL_PATH))


def run_detection(source, confidence=0.50):
    """Detect road hazards in an image path or OpenCV frame."""

    results = hazard_model.predict(
        source=source,
        conf=confidence,
        imgsz=416,
        verbose=False
    )

    result = results[0]
    detections = []

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        detections.append({
            "hazard_type": result.names[int(box.cls[0])],
            "confidence": float(box.conf[0]),
            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2)
        })

    return detections
