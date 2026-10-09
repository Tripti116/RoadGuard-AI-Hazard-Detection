\# RoadGuard AI — Hazard Detection



A computer vision module developed for \*\*RoadGuard AI\*\* to detect road hazards in images and videos using a trained YOLO model.



\## Overview



Road damage and roadside hazards can create unsafe driving conditions. This project uses object detection to identify potential hazards and return their locations within an image or video frame.



\## Hazards Detected



\- \*\*Potholes\*\* — damaged or sunken road surfaces

\- \*\*Cracks\*\* — visible cracks in road surfaces

\- \*\*Waterlogging\*\* — standing water on roads

\- \*\*Debris\*\* — garbage or other objects on the road



\## Features



\- Image-based road hazard detection

\- Video-frame inference

\- Bounding-box localization

\- Confidence scores for predictions

\- Python prediction function designed for Django backend integration



\## Technology Stack



\- Python

\- Ultralytics YOLO

\- OpenCV

\- Computer Vision



\## Project Structure



```text

RoadGuard-AI-Hazard-Detection/

├── backend\_handoff/

│   ├── road\_hazard\_predictor.py

│   ├── requirements.txt

│   └── weights/

│       └── best.pt

├── README.md

└── .gitignore

```



Other project files may be present locally. Datasets, generated videos, and training outputs should not be committed unnecessarily.



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR\_GITHUB\_USERNAME/RoadGuard-AI-Hazard-Detection.git

cd RoadGuard-AI-Hazard-Detection

```



Replace `YOUR\_GITHUB\_USERNAME` with your GitHub username.



\### 2. Install dependencies



```bash

python -m venv .venv

```



Activate the environment on Windows:



```bat

.venv\\Scripts\\activate

```



Install the packages:



```bash

pip install -r backend\_handoff/requirements.txt

```



\### 3. Model weights



The predictor expects the trained weights at:



```text

backend\_handoff/weights/best.pt

```



If the weights are distributed separately, place the provided `best.pt` file at this location before running predictions.



\## Usage



```python

from backend\_handoff.road\_hazard\_predictor import run\_detection



image\_path = r"path\\to\\road\_image.jpg"



detections = run\_detection(image\_path, confidence=0.50)



for detection in detections:

&#x20;   print(detection)

```



The function returns a list of detections. Each detection contains:



| Field | Description |

|---|---|

| `hazard\_type` | Predicted hazard class |

| `confidence` | Model confidence score |

| `x1`, `y1` | Top-left bounding-box coordinates |

| `x2`, `y2` | Bottom-right bounding-box coordinates |



Coordinates are expressed in pixels relative to the original input image or frame.



\## Model Evaluation



The initial training run achieved the following validation results:



\- Precision: 0.483

\- Recall: 0.550

\- mAP@50: 0.478

\- mAP@50–95: 0.202



These are initial prototype results, not a guarantee of performance on unseen roads. Predictions should be validated on representative images and videos.



\## Backend Integration



The prediction function is intended to be called by a Django backend. API endpoints, database persistence, GPS integration, and frontend mapping must be implemented and tested separately.



\## Limitations



\- Some hazards may be missed or incorrectly classified.

\- Repeated video-frame detections may refer to the same physical hazard.

\- Confidence thresholds affect the number of predictions.

\- Model performance depends on the quality and diversity of the training data.



\## Project Status



\*\*AI detection prototype — ready for integration testing.\*\*



\## Author



Developed as the road hazard detection component of the RoadGuard AI project.

