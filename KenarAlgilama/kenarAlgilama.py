import cv2 
import numpy as np

resim=cv2.imread("groot.png")
gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gri,(3,3),0)

canny=cv2.Canny(blur,150,225)  # Gauss bulanıklaştırma sonrasında oluşturulan görüntü üzerinde 
#Canny kenar algılama algoritmasını uygular. Bu algoritma, keskin kenarları belirlemek için yaygın olarak kullanılır

def autoCanny(blur,sigma=0.33):
    median=np.median(blur)
    en_dusuk=int(max(0,(1.0-sigma)*median))
    en_yuksek=int(min(255,(1.0+sigma)*median))
    canny1=cv2.Canny(blur,en_dusuk,en_yuksek)
    return canny1

genis=cv2.Canny(blur,100,150)
dar=cv2.Canny(blur,200,230)
auto=autoCanny(blur)

cv2.imshow("orijinal resim",resim)
cv2.imshow("gri ve blur",np.hstack([gri,blur]))
cv2.imshow("dar ve genisler",np.hstack([genis,dar]))
cv2.imshow("manuel ve otomatik canny",np.hstack([canny,auto]))

cv2.waitKey(0)
cv2.destroyAllWindows()
