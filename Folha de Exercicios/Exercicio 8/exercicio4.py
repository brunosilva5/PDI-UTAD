import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/edificio.tif")

plt.title("Original image")
plt.imshow(img)

grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

plt.figure()
plt.title("Sobel X")
plt.imshow(grad_x)

plt.figure()
plt.title("Sobel Y")
plt.imshow(grad_y)

plt.figure()
plt.title("Sobel X + Y")
plt.imshow(grad_x + grad_y)

plt.show()
