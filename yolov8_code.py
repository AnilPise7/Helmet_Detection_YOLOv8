import cv2
from ultralytics import YOLO

# Load your custom YOLOv8 model (Replace with the path to your trained model)
model = YOLO(r"D:\YOOv8_Helmet\models\hemletYoloV8_100epochs.pt")  # Ensure the file is in the same directory

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Perform inference
    results = model(frame)

    # Extract detections
    detections = results[0].boxes.data.cpu().numpy()  # Convert tensor to NumPy array

    # Assign class labels
    labels = [model.names[int(class_id)] for _, _, _, _, _, class_id in detections]

    # Draw bounding boxes and labels
    for (x1, y1, x2, y2, conf, class_id) in detections:
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])  # Convert coordinates to integers
        label = f"{model.names[int(class_id)]}: {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display output
    cv2.imshow("Helmet Detection - YOLOv8", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
