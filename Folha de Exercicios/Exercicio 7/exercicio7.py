import cv2
import numpy as np
from numpy.lib.function_base import median
from numpy.lib.type_check import imag
from skimage.util import random_noise
from skimage import io
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/edificio.tif")

img_noise_gauss = random_noise(img, mode="gaussian")
img_noise_gauss = np.array(255 * img_noise_gauss, dtype="uint8")

img_noise_sp = random_noise(img, mode="s&p", amount=0.15)
img_noise_sp = np.array(255 * img_noise_sp, dtype="uint8")

# Average filters
### Average filter with a kernel of 5x5
kernel = np.ones((5, 5), np.float32) / 25
average_gauss = cv2.filter2D(img_noise_gauss, -1, kernel)
### Median filter
median_gauss = cv2.medianBlur(img_noise_gauss, 5)

# Average filters
### Average filter with a kernel of 5x5
kernel = np.ones((5, 5), np.float32) / 25
average_sp = cv2.filter2D(img_noise_sp, -1, kernel)
### Median filter
median_sp = cv2.medianBlur(img_noise_sp, 5)

images = [
    img,
    img_noise_gauss,
    img_noise_sp,
    average_gauss,
    median_gauss,
    average_sp,
    median_sp,
]
io.imshow_collection(images)

plt.show()

# Conclusão, nota-se claramente que a mediana teve muito melhor efeito na imagem
# onde foi aplicada S&P, para o gauss, a media tem bons resultados também
