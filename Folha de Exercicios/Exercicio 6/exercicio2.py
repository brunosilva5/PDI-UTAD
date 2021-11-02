import cv2
import matplotlib.pyplot as plt
from skimage import exposure

img = cv2.imread("../Imagens/polen.tif", 0)

plt.imshow(img, "gray")

# Value 'gain = 2.5'
img_adjust = exposure.adjust_log(img, 2.5)

plt.figure()
plt.title("Imagem Ajustada com skimage")
plt.imshow(img_adjust, "gray")

plt.figure()
plt.hist(img_adjust.ravel(), 256, [0, 256])

plt.show()
