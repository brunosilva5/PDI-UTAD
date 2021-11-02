import cv2
from matplotlib.pyplot import draw
import numpy as np

# Exercício 1.1
img = cv2.imread("Imagens/rx_mao.jpg")
cv2.imshow("Rx_Mão", img)
cv2.imwrite("Rx_gravado.tif", img)

cv2.waitKey(0)
