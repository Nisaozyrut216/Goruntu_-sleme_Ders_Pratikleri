import cv2
import numpy as np

resim = cv2.imread("joker.jpg")

ikiKatBuyukResim = cv2.pyrUp(resim) #pyrUp komutu resmi iki katına çıkarır
ikiKatKucukResim = cv2.pyrDown(resim) 

print("Orijinal Resim",resim.shape)
print("Buyuk Resim",ikiKatBuyukResim.shape)
print("Kucuk Resim",ikiKatKucukResim.shape)

cv2.imshow("Orijinal resim",resim)
cv2.imshow("İki Kat Resim resim",ikiKatBuyukResim)
cv2.imshow("İki Kat Resim resim",ikiKatKucukResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
