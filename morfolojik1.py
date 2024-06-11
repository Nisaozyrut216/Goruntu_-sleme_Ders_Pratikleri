import cv2
import numpy as np

resim = cv2.imread("3.png")
kernel = np.ones((5,5),np.uint8)
dilation=cv2.dilate(resim,kernel,iterations=1) #Genişletme işlemi
erosion=cv2.erode(resim,kernel,iterations=3)  # İnceltme ve gürültü giderme işlemi
opening=cv2.morphologyEx(resim,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(resim,cv2.MORPH_CLOSE,kernel)
gradyan=cv2.morphologyEx(resim,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(resim,cv2.MORPH_TOPHAT,kernel)
blackHat=cv2.morphologyEx(resim,cv2.MORPH_BLACKHAT,kernel)




cv2.imshow("Orijinal Resim",resim) 
cv2.imshow("dilation",dilation) 
cv2.imshow("erosion",erosion) 
cv2.imshow("Opening",opening) 
cv2.imshow("Closing",closing) #önce dilation sonra erosion işlemleri
cv2.imshow("Gradyan",gradyan) #dilation-erosion
cv2.imshow("Tophat",tophat) #orijinal-opening
cv2.imshow("BlackHat",blackHat) #closing yapılan resim - orijinal resim

cv2.waitKey(0)
cv2.destroyAllWindows()

