# Kişisel Yüz Tanıma Projesi – YOLOv8 ile Nesne Tespiti

Bu proje, kendi yüz fotoğraflarımı kullanarak YOLOv8 algoritmasıyla kişisel bir yüz tanıma modeli eğitmek amacıyla geliştirilmiştir. Veri seti, manuel olarak etiketlenmiş ve YOLOv8 formatında hazırlanmıştır.

## 🔍 Amaç

- Kendi yüzümü nesne tespiti modeliyle tanımak
- Veri artırma (augmentation) teknikleriyle sınırlı veriyle model başarımını yükseltmek
- YOLOv8 mimarisiyle eğitim ve test süreçlerini yürütmek

## 🗂️ Proje Yapısı

```
project/
├── veri_seti/
│   ├── images/               # Etiketlenmiş yüz görüntüleri
│   ├── labels/               # YOLOv8 formatında label dosyaları
│   ├── data.yaml             # YOLOv8 için konfigürasyon dosyası
│   ├── README.dataset.txt    # Veri seti hakkında detay
│   └── README.roboflow.txt   # Roboflow kullanımıyla ilgili açıklamalar
├── deneme.py                  # local de yüz tanıma ara yüzü
├── app2.py                # flask kullanılarak oluşturaln ara yüz
└── README.md                 # Bu dosya
```

## ⚙️ Kullanılan Teknolojiler

- Python 3.x
- YOLOv8 (Ultralytics)
- OpenCV, Albumentations (veri artırma için)
- Roboflow (etiketleme & veri yönetimi)

## 🚀 Modeli Eğitmek

Eğitim için aşağıdaki komutu kullanabilirsin:

```bash
yolo task=detect mode=train model=yolov8n.pt data=veri_seti/data.yaml epochs=50 imgsz=640
```

> `yolov8n.pt` yerine `yolov8s.pt` veya `yolov8m.pt` gibi farklı mimariler deneyebilirsin.

## 🧪 Modeli Test Etmek

```bash
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=veri_seti/data.yaml
```

## 📈 Başarı Metrikleri

(P          R      mAP50  mAP50-95)
0.941          1      0.995      0.718
## 👤 Geliştirici

- Ad: **[Müge Yılmaz]**
- GitHub: [https://github.com/muge-124]([https://github.com/kullaniciadiniz](https://github.com/muge-124/face_detection.git))
  
