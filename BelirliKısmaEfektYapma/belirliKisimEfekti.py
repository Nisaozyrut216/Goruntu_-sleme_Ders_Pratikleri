import cv2
import numpy as np

saban = cv2.imread("saban.jpg")

#saban[:,:,2]=0
#saban[:,:,1]=34

saban[50:100,120:230,2]=255  #girilen matris konumuna istenen bgr değerlerinin rengini efekt yapmadır
saban[50:100,120:230,0]=150


cv2.imshow("Şaban",saban)
cv2.waitKey(0)
cv2.destroyAllWindows()

