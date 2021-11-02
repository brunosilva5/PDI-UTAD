import cv2
import matplotlib.pyplot as plt

from skimage import io

img1 = cv2.imread("../Imagens/fce_clara.bmp", 0)

# Para normalizar aplicamos a função: cv2.equalizeHist
# Apresentar o histograma da figura fce_clara
img_hist = cv2.calcHist([img1], [0], None, [256], [0, 256])

# Intesidade média e Desvio padrão
std = cv2.meanStdDev(img1)
print(f"Intesidade média e desvio padrão: {std}")

plt.plot(img_hist)
plt.show()
