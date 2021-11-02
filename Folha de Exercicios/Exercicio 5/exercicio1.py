import cv2
import matplotlib.pyplot as plt

# https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
# https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
# https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html

img = cv2.imread("../Imagens/polen.tif", 0)
# Plot do histograma nao normalizado
plt.hist(img.ravel(), 256, [0, 256])

# Apresentar o histograma normalizado da figura polen
hist_normalized = cv2.equalizeHist(img)
# hist_normalized = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot do histograma normalizado
plt.hist(hist_normalized.ravel(), 256, [0, 256])

cv2.imshow("original", img)
cv2.imshow("normalized", hist_normalized)
plt.show()

cv2.waitKey(0)
