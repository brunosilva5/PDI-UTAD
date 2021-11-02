import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../Imagens/dif1.bmp")
img2 = cv2.imread("../Imagens/dif2.bmp")
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

img_dif = abs(img2 - img1)
img_and = cv2.bitwise_xor(img2, img1, mask=None)

plt.imshow(img_dif)
plt.show()

cv2.waitKey(0)
