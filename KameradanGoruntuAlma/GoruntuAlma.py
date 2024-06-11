import cv2

kamera = cv2.VideoCapture(0)  # 0:bilgisayar kamerası, 1:dışarıdan bağlı kamera, 2:videodan görüntü

while True:
    ret, goruntu = kamera.read()

    cv2.imshow("Goruntu Alma", goruntu)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
