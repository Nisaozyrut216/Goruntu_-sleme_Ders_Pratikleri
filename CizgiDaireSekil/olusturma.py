import cv2 
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8")
cv2.line(resim,(00,00),(100,100),(200,120,145),3)  #çizgi çekme(resim,başlama yeri,bitiş yeri,BGR değeri,çizgi kalınlığı)
cv2.circle(resim,(150,150),25,(120,24,166),2)  #daire çizme(resim,daire merkezi,yarıçap uzunluğu,BGR değeri,çizgi kalınlığı)
cv2.putText(resim,"Nisa Ozyurt",(75,250),cv2.FONT_HERSHEY_COMPLEX,1,(34,136,35),5)  #yazı yazma (resim, başlama yeri,yazı fontu,yazı boyutu,BGR Rengi,yazı kalınlığı)
cv2.imshow("Deneme Resim",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()

