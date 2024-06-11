import cv2
import numpy as np

resim = cv2.imread("ast.jpg")

#AYNALAMA
aynalamaResim=cv2.copyMakeBorder(resim,50,75,50,25,cv2.BORDER_REFLECT)  #değerler sırası ile (kullanılacak resim.üst,alt,sol,sağ,uygulanacak işlem)
#Uzatma
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
#Tekrarlama
tekrarResim=cv2.copyMakeBorder(resim,300,100,300,100,cv2.BORDER_WRAP)
#Sarılan
sarmaResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,
                              value=(0,250,150))
                                    
cv2.imshow("Tekrarlanan Marslı",tekrarResim)
cv2.imshow("Uzatilan Marslı",uzatilanResim)
cv2.imshow("Aynalanan Marslı",aynalamaResim)
cv2.imshow("Sarılan Marslı",sarmaResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
