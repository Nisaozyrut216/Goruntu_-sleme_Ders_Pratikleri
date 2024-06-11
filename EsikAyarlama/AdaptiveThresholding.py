import cv2 

resim=cv2.imread("2.png",0)

#SİMPLE THREHOLDİNG : Basit eşikleme, bir görüntüyü belirli bir eşik değeriyle karşılaştırarak pikselleri ikili (siyah ve beyaz) bir görüntüye dönüştürür
ret,thresh1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY)

#ADAPTİVE THREHOLDİNG: Uyumlu eşikleme, görüntünün farklı bölgeleri için farklı eşik değerleri uygulayarak daha esnek bir eşikleme yöntemi sağlar.
#görüntü üzerinde bir kayan pencere (örneğin, 3x3, 5x5) belirlenir ve bu pencere içindeki her bir bölge için lokal bir eşik değeri hesaplanır.
thresh2=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                  cv2.THRESH_BINARY,11,2)
#mean : Bu yöntemde, her pikselin etrafındaki bir pencere belirlenir ve bu pencere içindeki piksellerin ortalaması hesaplanır.
thresh3=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY,15,16) 
#gauss : Bu yöntemde, her bir pikselin etrafındaki bir pencere belirlenir ve bu penceredeki piksellerin yoğunluklarına göre bir Gauss filtresi uygulanır.

#OTSU THRESHOLDİNG : değer seçme zorunluluğunu ortadan kaldırarak değeri kendi belirler. Daha temiz ve net bir görüntü elde etmemii sağlar

ret1,thresh4=cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow("Orijinal",resim) #closing yapılan resim - orijinal resim
cv2.imshow("simple thresholding",thresh1)
cv2.imshow("adaptive mean thresholding",thresh2)
cv2.imshow("adaptive gauss thresholding",thresh3) 
cv2.imshow("otsu thresholding",thresh4) 

cv2.waitKey(0)
cv2.destroyAllWindows()