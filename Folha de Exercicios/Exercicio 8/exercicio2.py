import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/xadrezado.jpg")

plt.title("Original image")
plt.imshow(img)


kernel1 = np.array([[-2, 0, 2]])
kernel2 = (np.array([[-2, 0, 2]])).transpose()

plt.figure()
img_kernel1 = cv2.filter2D(img, -1, kernel1)
plt.title("Image after kernel1 aplication")
plt.imshow(img_kernel1)

plt.figure()
img_kernel2 = cv2.filter2D(img, -1, kernel2)
plt.title("Image after kernel2 aplication")
plt.imshow(img_kernel2)

plt.show()
