import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../Imagens/pulmao.jpg")

plt.title("Original image")
plt.imshow(img)
############### Laplacian of Gaussian ################
# Remove noise by blurring with a Gaussian filter
src = cv2.GaussianBlur(img, (3, 3), 0)
# Apply Laplace function
ddepth = cv2.CV_16S
kernel_size = 3
dst = cv2.Laplacian(src, ddepth, ksize=kernel_size)
# converting back to uint8
abs_dst = cv2.convertScaleAbs(dst)

plt.figure()
plt.title("Final Image")
plt.imshow(abs_dst)
######################################################

############### Laplacian of Gaussian ################
# (LoG) kernel
log_kernel = np.array(
    [
        [0, 0, 1, 0, 0],
        [0, 1, 2, 1, 0],
        [1, 2, -16, 2, 1],
        [0, 1, 2, 1, 0],
        [0, 0, 1, 0, 0],
    ]
)

plt.figure()
# https://notebook.community/darshanbagul/ComputerVision/EdgeDetection-ZeroCrossings/EdgeDetectionByZeroCrossings
log_image = cv2.filter2D(img, -1, log_kernel)
plt.title("LoG Image, imagem como o kernel LoG")
plt.imshow(log_image)
######################################################

############### Laplacian of Gaussian ################
plt.figure()
LoG = cv2.Laplacian(img, cv2.CV_16S)
plt.title("LoG Image, imagem como o cv2.Laplacian")
plt.imshow(LoG)

plt.show()
