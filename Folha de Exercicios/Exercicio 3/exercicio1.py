import cv2
import matplotlib.pyplot as plt

img_ex1 = cv2.imread("../Imagens/mamograma.tif")
print(f"Imagem original: {img_ex1}")

img50 = img_ex1 + 50
print(f"Imagem + 50: {img50}")

img150 = img_ex1 + 150
print(f"Imagem + 150: {img150}")

plt.imshow(img150)
plt.show()
