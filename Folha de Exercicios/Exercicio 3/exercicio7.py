import cv2
import numpy as np

from skimage import io

img1 = cv2.imread("../Imagens/dif1.bmp")
img2 = cv2.imread("../Imagens/dif2.bmp")

images = [cv2.addWeighted(img1, 1 - i, img2, i, 0) for i in np.arange(0, 1, 0.1)]

io.imshow_collection(images)

io.show()
