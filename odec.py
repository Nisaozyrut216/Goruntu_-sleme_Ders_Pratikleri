import cv2

def iyilestirilmis_goruntu(image_path, method='CLAHE'):
    # Görüntüyü yükle
    resim = cv2.imread(image_path)
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
        lab_planes[0] = clahe.apply(lab_planes[0])
        lab_image = cv2.merge(lab_planes)
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
cv2.imwrite('iyilestirilmis_goruntu11.jpg', iyilestirilmis_goruntu)
cv2.imshow('Iyilestirilmis Goruntu', iyilestirilmis_goruntu)

cv2.waitKey(0)
cv2.destroyAllWindows()
