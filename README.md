# NEU Steel Surface Defect Detection

AI-based steel surface defect detection using YOLO and Streamlit.

## Defect Classes

- Scratches
- Rolled-in Scale
- Pitted Surface
- Patches
- Inclusion
- Crazing

## Technologies

- Python 3.11
- Ultralytics YOLO
- PyTorch
- Streamlit
- OpenCV
- Pillow
- NEU-DET Dataset

## Features

- Steel surface defect detection
- Bounding boxes
- Confidence scores
- Defect severity and risk
- Image-based detection
- Real-time webcam detection
- Streamlit web interface

## Validation Results

| Metric | Result |
|---|---:|
| Precision | 75.34% |
| Recall | 63.60% |
| mAP50 | 72.40% |
| mAP50-95 | 40.95% |

## Run the Application

Activate the virtual environment:

    venv\Scripts\activate

Run Streamlit:

    streamlit run scripts/app.py

## Project Purpose

This project demonstrates AI-based automated optical inspection (AOI) for detecting surface defects in steel.
