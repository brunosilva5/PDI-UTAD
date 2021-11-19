import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu

img = cv2.imread("../Imagens/celulas.jpg", 0)


plt.title("Original image")
plt.imshow(img)

plt.figure()
plt.hist(img.ravel(), 256, [0, 256])


# thresh = 125
# binary = (img > thresh).astype(np.int32)

img[img < 100] = 0
img[(img < 123) & (img >= 100)] = 0.5
img[img >= 123] = 1

plt.figure()
plt.imshow(img, "gray")

plt.show()
