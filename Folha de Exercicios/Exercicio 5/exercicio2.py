import cv2
import matplotlib.pyplot as plt
from skimage import exposure

# https://www.pyimagesearch.com/2021/02/08/histogram-matching-with-opencv-scikit-image-and-python/

img1 = cv2.imread("../Imagens/babesia_1.jpg")
img2 = cv2.imread("../Imagens/babesia_2.jpg")

cv2.imshow("Imagem 1", img1)
cv2.imshow("Imagem 2", img2)

multi = True if img1.shape[-1] > 1 else False
matched = exposure.match_histograms(img1, img2, multichannel=multi)

cv2.imshow("Imagem 1 Alterada", matched)
plt.show()
cv2.waitKey(0)
