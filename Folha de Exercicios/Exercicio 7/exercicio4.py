import cv2
import matplotlib.pyplot as plt
import numpy as np

img_ex4 = cv2.imread("../Imagens/retina.jpg")
plt.imshow(img_ex4)

kernel = np.ones((5, 5), np.float32) / 27
img_filtered = cv2.filter2D(img_ex4, -1, kernel, 27)

plt.imshow(img_filtered)
plt.show()
