import cv2

# Exercício 1.2
dim = (300, 500)


def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


img_mao = cv2.imread("Imagens/rx_mao.jpg")
img_torax = cv2.imread("Imagens/rx_torax.jpg")
img_bexiga = cv2.imread("Imagens/Rx_bexiga.jpg")
img_brain = cv2.imread("Imagens/brain.jpg")

cv2.imshow("Rx_Mão", img_mao)
cv2.imshow("Rx_Torax", img_torax)
cv2.imshow("Rx_Bexiga", img_bexiga)
cv2.imshow("Rx_Brain", img_brain)

im1_s = cv2.resize(img_mao, dim)
im2_s = cv2.resize(img_torax, dim)
im3_s = cv2.resize(img_bexiga, dim)
im4_s = cv2.resize(img_brain, dim)

im_tile = concat_tile([[im1_s, im2_s], [im3_s, im4_s]])

cv2.imshow("rx_mao, rx_torax, rx_bexiga, brain", im_tile)