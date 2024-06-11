import cv2
import numpy as np

resim = cv2.imread("uzay.png")

kesit=resim[50:150,300:400]
resim[0:100,0:100]=kesit

resim[0:100,0:100]=(0,150,255)

#cv2.imshow("Uzaydan Kesit",kesit)
cv2.imshow("Uzay",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
