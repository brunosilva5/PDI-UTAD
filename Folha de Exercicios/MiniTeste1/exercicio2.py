import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../Images/detect_1.jpg")
img2 = cv2.imread("../Images/detect_2.jpg")
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

img_and = cv2.bitwise_xor(img2, img1, mask=None)
img = cv2.medianBlur(img_and, 3)

plt.imshow(img)
plt.title("Anterações entre os 2 exames")
plt.show()

cv2.waitKey(0)
