import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../Imagens/soma_1.jpg")
img2 = cv2.imread("../Imagens/soma_2.jpg")
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

print(f"Imagem 1 shape: {img1.shape}")
print(f"Imagem 2 shape: {img2.shape}")

# Resize img1
img1 = cv2.resize(img1, (375, 281))
print(f"Imagem 1 shape: {img1.shape}")

img = cv2.add(img1, img2)

plt.imshow(img)
plt.show()
