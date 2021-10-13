import cv2
import matplotlib.pyplot as plt

# Exercicio 2.1
img_ex1 = cv2.imread("Imagens/rx_mao.jpg")
# plt.imshow(img_ex1)
# plt.show()

# Pto = (y, x)
pto = (180, 70)
(b, g, r) = img_ex1[pto]
print(f"Pixel no ponto {pto} = Red: {r} | Green: {g} | Blue: {b}")

img_ex1[pto] = cv2.IMREAD_GRAYSCALE

print(f"O ponto tem o seguinte RGB: {img_ex1[pto]}")
print(f"O ponto tem o seguinte NDC: {img_ex1[pto]}")
