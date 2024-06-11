import cv2 
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()
    cv2.rectangle(goruntu,(100,100),(200,200),(234,156,123),7) #görüntü üzerinde dörtgen
    cv2.line(goruntu,(0,0),(50,50),(120,20,234),6) #görüntü üzerinde çizgi
    cv2.circle(goruntu,(120,120),30,(45,220,110),5)  #görüntü üzerinde daire
    cv2.putText(goruntu,"Nisa OZYURT",(0,60),cv2.FONT_HERSHEY_SIMPLEX,1,(21,0,213),3) #görüntü üzerinde yazı

    cv2.imshow("Goruntu Alma", goruntu)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()

