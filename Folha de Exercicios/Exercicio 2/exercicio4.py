import cv2
import matplotlib.pyplot as plt

img_ex4 = cv2.imread("../Imagens\Rx_bexiga.jpg")
# plt.imshow(img_ex4)

# img_crop = img_ex4[y_inicial:y_final, x_inicial:x_final]
img_crop = img_ex4[70:150, 72:162]

plt.imshow(img_crop)
plt.show()
