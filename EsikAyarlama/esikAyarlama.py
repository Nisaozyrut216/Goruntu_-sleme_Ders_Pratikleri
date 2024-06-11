import cv2 
import numpy as np

resim=cv2.imread("finger.png",0)
ret,thresh1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(resim,127,255,cv2.THRESH_BINARY_INV)  #İşlev: Binary thresholding işleminin tersidir. Eşik değerinin altındaki pikseller beyaz, üstündekiler siyah olur.
#Kullanım: Genellikle nesneleri arka plana karşı ayırmak veya vurgulamak için kullanılır.
ret,thresh3=cv2.threshold(resim,127,255,cv2.THRESH_TRUNC) #İşlev: Eşik değerinin üstünde olan piksellerin değerlerini eşik değerine ayarlar, altında olanları ise olduğu gibi bırakır.
#Kullanım: Görüntüyü belirli bir eşik değeri üzerinde kırpma veya sınırlama işlemlerinde kullanılır
ret,thresh4=cv2.threshold(resim,127,255,cv2.THRESH_TOZERO) #İşlev: Eşik değerinin altındaki pikselleri sıfıra ayarlar, üstündekileri ise olduğu gibi bırakır.
#Kullanım: Görüntü işlemede gürültüyü azaltmak veya belirli nesneleri vurgulamak için kullanılır.
ret,thresh5=cv2.threshold(resim,127,255,cv2.THRESH_TOZERO_INV) #İşlev: Eşik değerinin altında olan pikselleri sıfıra ayarlar, üstündekileri ise olduğu gibi bırakır.
#Kullanım: Genellikle belirli bir bölgedeki pikselleri vurgulamak veya arka planı filtrelemek için kullanılır.



cv2.imshow("Orijinal",resim) 
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)
cv2.imshow("thresh4",thresh4)
cv2.imshow("thresh5",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
