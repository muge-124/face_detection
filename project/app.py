import streamlit as st
import cv2
import time

st.title("Yüz Algılama - Stabil Canlı Video")

# Kamera kontrolü için session_state
if 'camera_active' not in st.session_state:
    st.session_state.camera_active = False
if 'cap' not in st.session_state:
    st.session_state.cap = None

# Butonlar
start = st.button("Başlat")
stop = st.button("Durdur")

if start:
    st.session_state.camera_active = True
if stop:
    st.session_state.camera_active = False

if st.session_state.camera_active:
    if st.session_state.cap is None:
        st.session_state.cap = cv2.VideoCapture(0)

    ret, frame = st.session_state.cap.read()
    if not ret:
        st.error("Kameradan görüntü alınamıyor.")
        st.session_state.cap.release()
        st.session_state.cap = None
        st.session_state.camera_active = False
    else:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame_rgb)

    # FPS kontrolü için yavaşlatma
    time.sleep(0.1)

else:
    if st.session_state.cap:
        st.session_state.cap.release()
        st.session_state.cap = None
