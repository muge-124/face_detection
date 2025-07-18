from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.pt")  # Alternatif olarak yolov8s.pt vb.
    model.train(
        data=r"C:/Users/mge30/OneDrive/Masaüstü/face_detection/project/veri_seti/data.yaml",
        epochs=100,
        imgsz=640,
        batch=4,
        patience=10,
        name="face-detection"
    )

if __name__ == "__main__":
    train_model()
