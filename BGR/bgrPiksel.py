import cv2
import numpy as np

kurt = cv2.imread("kurt.jpg")

cv2.imshow("Kurt Resmi",kurt) 
print(kurt[(100,96)])

print("Resmin Boyutu:" +str(kurt.size))
print("Resmin Özellikleri :" +str(kurt.shape))
print("Resmin Veri Tip:" +str(kurt.dtype))




cv2.waitKey(0)
cv2.destroyAllWindows()

