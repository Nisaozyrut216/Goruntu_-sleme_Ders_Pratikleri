import cv2 
import numpy as np

resim1 = cv2.imread("indir.png")  
resim2 = cv2.imread("kus.jpg")  
#resim1 = cv2.imread("indir.png")

cv2.imshow("Deneme Resim",resim1)

print(resim1.size)
print(resim1.dtype)
print(resim1.shape)


#cv2.imwrite("Yeniresim.png",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

