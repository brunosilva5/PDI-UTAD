import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu

img = cv2.imread("../Imagens/bolas.jpg", 0)


plt.title("Original image")
plt.imshow(img)

plt.figure()
plt.hist(img.ravel(), 256, [0, 256])

thresh = 125
binary = (img > thresh).astype(np.int32)
print(thresh)
plt.figure()
plt.imshow(binary, "gray")

plt.show()
