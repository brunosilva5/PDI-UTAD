import cv2
from matplotlib.pyplot import draw
import numpy as np

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
