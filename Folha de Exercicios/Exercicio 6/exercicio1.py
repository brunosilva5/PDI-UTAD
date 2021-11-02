import cv2

img = cv2.imread("../Imagens/mamograma.tif")

img_neg = cv2.bitwise_not(img)

cv2.imshow("Original", img)
cv2.imshow("Negativo", img_neg)

cv2.waitKey(0)
