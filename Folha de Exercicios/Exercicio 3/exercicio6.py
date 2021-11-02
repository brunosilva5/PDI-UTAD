import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../Imagens/hospital_61.jpg")
img2 = cv2.imread("../Imagens/masc.jpeg")
cv2.imshow("1", img1)
cv2.imshow("2", img2)

img = cv2.bitwise_and(img1, img2, mask=None)

plt.imshow(img)
plt.show()

cv2.waitKey(0)
