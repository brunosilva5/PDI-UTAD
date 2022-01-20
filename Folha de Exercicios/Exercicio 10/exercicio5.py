import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage.morphology import disk

img = cv2.imread("../Imagens/text_grad.bmp", 0)

plt.title("Original image")
plt.imshow(img, "gray")

plt.figure()
plt.hist(img.ravel(), 256, [0, 256])

thresh = filters.threshold_otsu(img)
binary = img > thresh

plt.figure()
plt.title("Binary image")
plt.imshow(binary, "gray")

# threshold_adaptive
block_size = 11
adaptive_thresh = filters.threshold_local(img, block_size, offset=7)
binary_adaptive = img > adaptive_thresh

plt.figure()
plt.title("Adapative Threshold image")
plt.imshow(binary_adaptive, "gray")

plt.show()
