import cv2
import matplotlib.pyplot as plt

img_ex5 = cv2.imread("../Imagens\Rx_mao.jpg")

print(f"Original Dimensions:, {img_ex5.shape}")

scale_percent = 200
width = int(img_ex5.shape[1] * scale_percent / 100)
height = int(img_ex5.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img_resized = cv2.resize(img_ex5, dim, interpolation=cv2.INTER_AREA)

print("Resized Dimensions : ", img_resized.shape)

plt.imshow(img_resized)
plt.show()
