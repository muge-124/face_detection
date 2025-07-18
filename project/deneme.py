from ultralytics import YOLO
import cv2

# Modeli yükle
model = YOLO("best.pt")

# Kamera aç (0: varsayılan webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Model ile tahmin yap
    results = model.predict(source=frame, save=False, conf=0.5)

    # Tahmin sonuçlarını çizdir
    annotated_frame = results[0].plot()

    # Ekrana göster
    cv2.imshow("YOLOv8 Face Detection", annotated_frame)

    # 'q' ile çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
