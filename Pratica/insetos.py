# Ler imagem
# ver histograma, verificar os estao os insetos e fazer crop
# aplicar algoritmo para contar
# ver regianprops
import cv2
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
from skimage import measure

img = cv2.imread("./insetos.jpg", 0)

plt.imshow(img, "gray")

# img_crop = img[y_inicial:y_final, x_inicial:x_final]

img_crop = img[1615:2869, 2448:4222]

plt.figure()
plt.imshow(img_crop, "gray")

blurred = gaussian(img_crop, sigma=0.4)
binary = blurred > threshold_otsu(blurred)

plt.figure()
plt.imshow(binary)

plt.show()
