from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("best.pt")

def decode_base64_image(base64_str):
    header, encoded = base64_str.split(',', 1)
    data = base64.b64decode(encoded)
    np_arr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

def encode_base64_image(img):
    _, buffer = cv2.imencode('.jpg', img)
    encoded = base64.b64encode(buffer).decode('utf-8')
    return 'data:image/jpeg;base64,' + encoded

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    img_data = data['image']
    img = decode_base64_image(img_data)

    results = model(img)[0]
    boxes = results.boxes.xyxy.cpu().numpy()
    scores = results.boxes.conf.cpu().numpy()
    classes = results.boxes.cls.cpu().numpy().astype(int)

    for box, score, cls in zip(boxes, scores, classes):
        if score < 0.5:
            continue
        x1, y1, x2, y2 = map(int, box)
        label = model.names[cls] if hasattr(model, 'names') else str(cls)
        color = (0, 255, 0)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, f"{label} {score:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    img_base64 = encode_base64_image(img)
    return jsonify({'image': img_base64})

if __name__ == '__main__':
    app.run(debug=True)
