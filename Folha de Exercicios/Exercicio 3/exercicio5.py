import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../Imagens/And1.bmp")
img2 = cv2.imread("../Imagens/And2.bmp")
cv2.imshow("1", img1)
cv2.imshow("2", img2)

img_result = cv2.bitwise_or(img1, img2, mask=None)

plt.imshow(img_result)
plt.show()

cv2.waitKey(0)
