import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/results/neu_yolo_safe/weights/best.pt")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam.")
        break

    results = model.predict(
        frame,
        imgsz=512,
        conf=0.25,
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("NEU Steel Defect Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()