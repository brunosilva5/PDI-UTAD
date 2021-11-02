import cv2
import numpy as np
from skimage import io

img = cv2.imread("../Imagens/face.jpg")

# Image with first filter
kernel = np.ones((3, 3), np.float32) / 9
dst = cv2.filter2D(img, -1, kernel)

# Image with second filter
kernel2 = np.ones((7, 7), np.float32) / 49
dst2 = cv2.filter2D(img, -1, kernel2)

dst_gaussiano = cv2.GaussianBlur(img, (5, 5), 1)

io.imshow_collection([img, dst, dst2, dst_gaussiano])
io.show()
