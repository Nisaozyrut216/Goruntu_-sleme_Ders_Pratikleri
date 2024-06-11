import cv2
import numpy as np

resim = cv2.imread("dib1.jpg")
resim2 = cv2.imread("dib1.jpg",0)
ret,thresh1=cv2.threshold(resim,50,150,cv2.THRESH_BINARY)
thresh2=cv2.adaptiveThreshold(resim2,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                  cv2.THRESH_BINARY,9,2)
kernel = np.ones((5,5),np.uint8)
gradyan=cv2.morphologyEx(resim,cv2.MORPH_GRADIENT,kernel)


cv2.imshow("esikli resim",thresh1)
cv2.imshow("esikli resim 2",thresh2)
cv2.imshow("Gradyan",gradyan) 



def iyilestirilmis_goruntu(resim, method='CLAHE'):
    # Görüntüyü yükle
    resim = cv2.imread("dib1.jpg")
    cv2.imshow('Orijinal Goruntu', resim)
 

    if method == 'Histogram Eşitleme':
        # Histogram eşitleme
        gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        iyilestirilmis_goruntu = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
    elif method == 'CLAHE':
        # CLAHE uygula
        lab_image = cv2.cvtColor(resim, cv2.COLOR_BGR2LAB)
        lab_planes = cv2.split(lab_image)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        lab_planes_list = list(lab_planes)
        lab_planes_list[0] = clahe.apply(lab_planes_list[0])
        lab_image = cv2.merge(lab_planes_list)
        iyilestirilmis_goruntu = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)
    elif method == 'Gaussian Bulanıklığı':
        # Gaussian bulanıklığı uygula
        iyilestirilmis_goruntu = cv2.GaussianBlur(resim, (5, 5), 0)
    else:
        print("Geçersiz yöntem.")
        return None
    
    return iyilestirilmis_goruntu

# Görüntüyü iyileştir
iyilestirilmis_goruntu = iyilestirilmis_goruntu('dib1.jpg', method='CLAHE')

# İyileştirilmiş görüntüyü göster
cv2.imwrite('iyilestirilmis_goruntu.jpg', iyilestirilmis_goruntu)
cv2.imshow('Iyilestirilmis Goruntu', iyilestirilmis_goruntu)



cv2.waitKey(0)
cv2.destroyAllWindows()
