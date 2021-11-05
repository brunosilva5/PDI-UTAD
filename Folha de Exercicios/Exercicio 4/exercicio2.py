import cv2
import matplotlib.pyplot as plt

from skimage import io

img1 = cv2.imread("../Imagens/vertebra.jpg", 0)

# poderá ser o pto 100, pois é o mais alto no histograma
most_freq = cv2.calcHist([img1], [0], None, [256], [0, 256])

plt.plot(most_freq)
plt.show()
