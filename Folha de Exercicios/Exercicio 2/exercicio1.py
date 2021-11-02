import cv2
import matplotlib.pyplot as plt

img_ex1 = cv2.imread("../Imagens/rx_mao.jpg")

# Pto = (y, x)
pto = (180, 70)
print(img_ex1[pto])
img_ex1[pto] = 20
print(img_ex1[pto])

plt.imshow(img_ex1)
plt.show()
