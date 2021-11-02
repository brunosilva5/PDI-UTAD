import cv2
import matplotlib.pyplot as plt

img_ex1 = cv2.imread("../Imagens/rx_mao.jpg", 0)
print(img_ex1.shape)
for l in range(10, 30):
    for c in range(10, 30):
        pto = (c, l)
        img_ex1[pto] = 100

plt.imshow(img_ex1, "bone")
plt.show()
