import cv2
import matplotlib.pyplot as plt
from skimage import exposure

img = cv2.imread("../Images/carro.jpg", 0)

# Histograma original
plt.figure()
plt.title("Hist original")
plt.hist(img.ravel(), 256, [0, 256])

# Apresentar img original
plt.figure()
plt.title("Figura original")
plt.imshow(img, "gray")
print(f"Shape da img original: {img.shape}")

# Value 'gain = 1.9'
img_adjust = exposure.adjust_log(img, 1.9)
# Apresentar imagem alterada
plt.figure()
plt.title("Imagem Ajustada com skimage")
plt.imshow(img_adjust, "gray")

plt.figure()
plt.hist(img_adjust.ravel(), 256, [0, 256])
plt.title("Histograma da Imagem Ajustada com skimage")

# Criar mascara
# for l in range(0, 95):
#     for c in range(10, 30):
#         pto = (c, l)
#         img_ex1[pto] = 100

plt.show()
