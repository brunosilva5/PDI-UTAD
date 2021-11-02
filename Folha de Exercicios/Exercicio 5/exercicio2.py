import cv2
import matplotlib.pyplot as plt
from skimage import exposure

# https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
# https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
# https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html

img1 = cv2.imread("../Imagens/babesia_1.jpg")
img2 = cv2.imread("../Imagens/babesia_2.jpg")


cv2.imshow("Imagem 1", img1)
cv2.imshow("Imagem 2", img2)
plt.show()
cv2.waitKey(0)
