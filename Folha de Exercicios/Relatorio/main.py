import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/lena.jpg", 0)

low_sigma = cv2.GaussianBlur(img, (3, 3), 0)
high_sigma = cv2.GaussianBlur(img, (5, 5), 0)

# Calculate the DoG by subtracting
dog = low_sigma - high_sigma

plt.imshow(dog, "gray")
plt.show()

cv2.imwrite("lena_DoG.jpg", dog)

cv2.waitKey(0)
