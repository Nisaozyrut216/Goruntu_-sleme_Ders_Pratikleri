import cv2
import numpy as np

def simulate_thermal_image(frame):
    # Renkleri termal renk haritasına dönüştür
    thermal_image = cv2.applyColorMap(frame, cv2.COLORMAP_HOT)
    return thermal_image

def capture_and_process():
    cap = cv2.VideoCapture(0)  # 0 varsayılan kamera

    if not cap.isOpened():
        print("Kamera başlatılamadı!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Görüntüyü termal benzeri bir görünüme dönüştür
        thermal_like_image = simulate_thermal_image(frame)

        cv2.imshow('Thermal-like Image', thermal_like_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_process()
