import cv2
import numpy as np

resim1 = cv2.imread("uzay1.png")
resim2 = cv2.imread("tekno.jpeg")


cv2.imshow("Uzay",resim1)
cv2.imshow("Teknopark",resim2)

#print(resim2.size)
#print(resim1.size)

toplam = cv2.add(resim1,resim2) #kullanılacak resimlerin birleştirilmesi , iki resmin de ahnı boyutlarda olması çok önemli
agirlikliToplam = cv2.addWeighted(resim1,0.6,resim2,0.4,0) #kullanılacak resimlerin istenen oranlara göre birleştime işelmi

cv2.imshow("Toplannmis Resimler",toplam)
cv2.imshow("Agirlikli Toplannmis Resimler",agirlikliToplam)

cv2.waitKey(0)
cv2.destroyAllWindows()