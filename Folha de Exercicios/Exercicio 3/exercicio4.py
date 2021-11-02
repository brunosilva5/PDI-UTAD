import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/xadrez.tif")

img_result = cv2.bitwise_not(img)

plt.imshow(img_result)
plt.show()
