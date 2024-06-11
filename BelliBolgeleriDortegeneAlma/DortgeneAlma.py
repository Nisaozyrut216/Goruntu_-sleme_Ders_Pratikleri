import cv2
import numpy as np

resim = cv2.imread("hababam.png")

cv2.rectangle(resim,(50,300),(250,10),[0,100,255],6)

cv2.imshow("Hababam",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()