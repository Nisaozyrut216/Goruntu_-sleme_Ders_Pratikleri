import cv2
import numpy as np

resim1 = cv2.imread("hababam.png")
resim2=cv2.imread("uzay.png")

print(resim1[350,440])
print(resim2[344,220])

cv2.imshow("Hababam",resim1)
cv2.imshow("Uzay",resim2)

print(resim1[350,440]+resim2[344,220])


cv2.waitKey(0)
cv2.destroyAllWindows()