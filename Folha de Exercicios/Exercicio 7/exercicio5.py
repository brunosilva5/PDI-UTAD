import cv2
import matplotlib.pyplot as plt

img_ex7 = cv2.imread("../Imagens/moon.tif")

plt.title("Imagem original")
plt.imshow(img_ex7)

gaussian_3 = cv2.GaussianBlur(img_ex7, (0, 0), 2.0)
unsharp_image = cv2.addWeighted(img_ex7, 1.5, gaussian_3, -0.5, 0)

plt.figure()
plt.title("Imagem Unsharped")
plt.imshow(unsharp_image)

plt.show()
