import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters

img = cv2.imread("../Imagens/TP_pcouto.bmp", 0)

plt.title("Original image")
plt.imshow(img, "gray")

plt.figure()
plt.title("Histograma da imagem original")
plt.hist(img.ravel(), 256, [0, 256])
# filtrar ruído sp
# segmentar imagem - apresentar rato (mask)
# segmentar - apresentar pto (mask)
# apos a segmentação, aplicar umm bloco por baixo e em cima

# Para remover da melhor forma ruído sal e pimenta
# Aplicamos o Median filters
kernel = np.ones((5, 5), np.float32) / 25
### Median filter
median_sp = cv2.medianBlur(img, 5)

plt.figure()
plt.title("Imagem filtrada pela mediana")
plt.imshow(median_sp, "gray")

# criar os rect para a imagem
img_rect = cv2.rectangle(median_sp, (0, 0), (479, 50), (0, 0, 0), -1)
img_rect = cv2.rectangle(img_rect, (0, 362), (479, 418), (0, 0, 0), -1)

thresh = filters.threshold_multiotsu(img_rect)
regions = np.digitize(img_rect, bins=thresh)

plt.figure()
print(thresh)
plt.title("Mask Mouse image")
plt.imshow(regions, "gray")


# Falta extrair os pontos do rato
plt.show()
