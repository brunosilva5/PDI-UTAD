import cv2
import numpy as np
from skimage import io

img = cv2.imread("../Imagens/face_noise.jpg")

dst_1 = cv2.blur(img, (3, 3))
dst_2 = cv2.blur(img, (5, 5))
dst_gaussiano = cv2.GaussianBlur(img, (5, 5), 1)
dst_gaussiano = cv2.medianBlur(img, 3)

io.imshow_collection([img, dst_1, dst_2, dst_gaussiano])
io.show()
