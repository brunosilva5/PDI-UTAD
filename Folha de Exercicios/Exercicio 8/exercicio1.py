import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread("../Imagens/edificio.tif")

kernel = np.array([[-1, 0, 1]])

image = np.array(
    [
        [0, 0, 0.2, 0.5, 0.8, 1, 1],
        [0, 0, 0.2, 0.5, 0.8, 1, 1],
        [0, 0, 0.2, 0.5, 0.8, 1, 1],
        [0, 0, 0.2, 0.5, 0.8, 1, 1],
    ]
)

img = cv2.filter2D(image, -1, kernel)
plt.title("Original image")
plt.imshow(image)

plt.figure()
plt.title("Image after kernel aplication")
plt.imshow(img)
plt.show()
