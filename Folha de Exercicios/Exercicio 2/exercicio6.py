import cv2
import matplotlib.pyplot as plt

img_ex6 = cv2.imread("../Imagens/brain.jpg")

img_rotated = cv2.flip(img_ex6, 0)
# img_rotated = cv2.rotate(img_ex6, cv2.ROTATE_180)

plt.imshow(img_rotated)
plt.show()
