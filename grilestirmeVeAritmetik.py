import cv2
import numpy as np

resim = cv2.imread("hababam.png")
griResim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)


cv2.imshow("Orijinal",resim)
cv2.imshow("Gri Hali",griResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
