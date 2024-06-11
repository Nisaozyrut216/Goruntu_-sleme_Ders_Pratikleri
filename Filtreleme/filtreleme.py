import cv2 
import numpy as np

resim=cv2.imread("3.png")

# Mean Filtering
meanFilter=cv2.blur(resim,(3,3)) # 3*3 matrisli iyileştirme
meanFilter2=cv2.blur(resim,(6,6))  # 6*6 matrisli iyileştirme
meanFilter3=cv2.blur(resim,(9,9)) # 9*9 matrisli iyileştirme

#Median Filtering
medianFilter=cv2.medianBlur(resim,3)
medianFilter2=cv2.medianBlur(resim,7)

#Gauss Filter
gaussFilter=cv2.GaussianBlur(resim,(5,5),0)

# Mean Filtering
cv2.imshow("Resim",resim)
cv2.imshow("Yeni Resim",meanFilter)
cv2.imshow("Yeni 2 Resim",meanFilter2)
cv2.imshow("Yeni 3 Resim",meanFilter3)

#Median Filter
cv2.imshow(" Medianlı 1.Resim",medianFilter)
cv2.imshow(" Medianlı 2.Resim",medianFilter2)

#gauss filter
cv2.imshow(" Gauss Resim",gaussFilter)



cv2.waitKey(0)
cv2.destroyAllWindows()

