import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype="uint8") #nupy kütüphanesine ait bu değişken içi sıfır ile dolu olan belirttiğimiz şekilde matrisler oluşturur


print(resim)


cv2.waitKey(0)
cv2.destroyAllWindows()
