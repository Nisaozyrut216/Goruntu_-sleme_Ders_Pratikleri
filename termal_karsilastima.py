import cv2
import numpy as np

def simulate_sunscreen_test(frame):
    # Güneş kremi uygulanmış görüntüyü simüle etmek için kırmızı bir filtre uygula
    simulated_frame = frame.copy()
    simulated_frame[:, :, 2] += 50  # Kırmızı kanalı arttırarak kırmızı bir filtre uygula
    return simulated_frame

def capture_and_process():
    cap = cv2.VideoCapture(0)  # 0 varsayılan kamera

    if not cap.isOpened():
        print("Kamera başlatılamadı!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Güneş kremi uygulanmış bir görüntü simüle et
        simulated_frame = simulate_sunscreen_test(frame)

        # İki görüntüyü yanyana göster
        comparison_frame = np.hstack((frame, simulated_frame))
        cv2.imshow('Comparison', comparison_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_process()
