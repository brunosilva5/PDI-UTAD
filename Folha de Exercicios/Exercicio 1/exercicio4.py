import cv2
from matplotlib.pyplot import draw
import numpy as np

img_tif_ex4 = cv2.imread("Imagens/Retina.tif")
cv2.imshow("Retina.tif", img_tif_ex4)
channel_initials = list("BGR")
for channel_index in range(3):
    channel = np.zeros(shape=img_tif_ex4.shape, dtype=np.uint8)
    channel[:, :, channel_index] = img_tif_ex4[:, :, channel_index]
    cv2.imshow(f"{channel_initials[channel_index]}-RGB", channel)
