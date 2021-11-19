import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.exposure.exposure import _bincount_histogram
from skimage import filters

img = cv2.imread("../Imagens/impressao_digital.jpg", 0)

plt.title("Original image")
plt.imshow(img)

plt.figure()
plt.hist(img.ravel(), 256, [0, 256])

thresh = filters.threshold_otsu(img)
binary = img > thresh

plt.figure()
print(thresh)
plt.title("Binary image")
plt.imshow(binary, "gray")

plt.figure()
plt.title("Iterative image")
thresh_li = filters.threshold_li(img)
binary_li = img > thresh_li
plt.imshow(binary_li, "gray")

plt.show()
