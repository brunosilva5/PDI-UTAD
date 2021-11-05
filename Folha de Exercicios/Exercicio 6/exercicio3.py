import cv2
import matplotlib.pyplot as plt
from skimage import exposure

img = cv2.imread("../Imagens/rx_torax.jpg", 0)

plt.imshow(img, "gray")

# img_adjust = exposure.adjust_log(img, 1)
img_adjust_gamma = 1.8
img_adjust = exposure.adjust_gamma(img, img_adjust_gamma)

plt.figure()
plt.title(f"Adjust Gamma: gamma: {img_adjust_gamma}")
plt.imshow(img_adjust, "gray")

plt.show()
