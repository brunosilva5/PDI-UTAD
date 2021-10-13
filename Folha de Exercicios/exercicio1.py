import cv2
from matplotlib.pyplot import draw
import numpy as np

# Exercício 1.1
# img = cv2.imread("Imagens/rx_mao.jpg")
# cv2.imshow("Rx_Mão", img)
# cv2.imwrite("Rx_gravado.tif", img)


# Exercício 1.2
# dim = (300, 500)


# def concat_tile(im_list_2d):
#     return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


# img_mao = cv2.imread("Imagens/rx_mao.jpg")
# img_torax = cv2.imread("Imagens/rx_torax.jpg")
# img_bexiga = cv2.imread("Imagens/Rx_bexiga.jpg")
# img_brain = cv2.imread("Imagens/brain.jpg")

# cv2.imshow("Rx_Mão", img_mao)
# cv2.imshow("Rx_Torax", img_torax)
# cv2.imshow("Rx_Bexiga", img_bexiga)
# cv2.imshow("Rx_Brain", img_brain)

# im1_s = cv2.resize(img_mao, dim)
# im2_s = cv2.resize(img_torax, dim)
# im3_s = cv2.resize(img_bexiga, dim)
# im4_s = cv2.resize(img_brain, dim)

# im_tile = concat_tile([[im1_s, im2_s], [im3_s, im4_s]])

# cv2.imshow("rx_mao, rx_torax, rx_bexiga, brain", im_tile)


# Exercício 1.3
# import matplotlib.pyplot as plt

# img_tif = plt.imread(fname="Imagens/Retina.tif")
# height, width, channels = img_tif.shape
# number_of_pixels = height * width * channels
# print(f"Altura: {height} | Largura: {width} | Número de pixels: {number_of_pixels}")
# plt.imshow(img_tif)
# plt.show()


# Exercício 1.4
# img_tif_ex4 = cv2.imread("Imagens/Retina.tif")
# cv2.imshow("Retina.tif", img_tif_ex4)
# channel_initials = list("BGR")
# for channel_index in range(3):
#     channel = np.zeros(shape=img_tif_ex4.shape, dtype=np.uint8)
#     channel[:, :, channel_index] = img_tif_ex4[:, :, channel_index]
#     cv2.imshow(f"{channel_initials[channel_index]}-RGB", channel)


# Exercício 1.5
import matplotlib.pyplot as plt

img_ex5 = np.zeros([256, 256, 3], dtype=np.uint8)
img_ex5.fill(255)
cv2.imshow("Imagem branca", img_ex5)
print(f"Shape da imagem: {img_ex5.shape}")

cv2.rectangle(img_ex5, pt1=(90, 70), pt2=(190, 170), color=(0, 0, 0), thickness=1)
cv2.imshow("Imagem final", img_ex5)

# Visualizar com o matplotlib
plt.title("PLT Imagem final - Ex1.5")
plt.imshow(img_ex5)
plt.show()

# Gravar em formato bmp
cv2.imwrite("img_ex5.bmp", img_ex5)

cv2.waitKey(0)
