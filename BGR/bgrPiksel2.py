import cv2
import numpy as np

resim = cv2.imread("joker.jpg")

resim[50,30]=[255,255,255]

for i in range(100):    #belirtilen değerden i 'ye kadar belirtilen piksel değerlerine uygun çizgi çeker
    resim[70,i]=[255,154,90]

cv2.imshow("Joker",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

