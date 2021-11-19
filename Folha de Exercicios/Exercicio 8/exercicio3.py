import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/edificio.tif")

plt.title("Original image")
plt.imshow(img)

kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)

kernel1 = np.array([[-2, 0, 2]])
kernel2 = (np.array([[-2, 0, 2]])).transpose()

plt.figure()
img_kernel1 = cv2.filter2D(img, -1, kernel1)
plt.title("Prewitt X")
plt.imshow(img_prewittx)

plt.figure()
img_kernel1 = cv2.filter2D(img, -1, kernel1)
plt.title("Prewitt Y")
plt.imshow(img_prewitty)

plt.figure()
img_kernel1 = cv2.filter2D(img, -1, kernel1)
plt.title("Prewitt X + Y")
plt.imshow(img_prewittx + img_prewitty)

plt.show()
