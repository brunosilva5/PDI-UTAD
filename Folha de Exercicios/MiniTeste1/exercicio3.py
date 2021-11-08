import cv2
import matplotlib.pyplot as plt
import numpy as np

from skimage import io

img1 = cv2.imread("../Images/img1.jpg", 0)
img2 = cv2.imread("../Images/img2.jpg", 0)
img3 = cv2.imread("../Images/img3.jpg", 0)
img4 = cv2.imread("../Images/img4.jpg", 0)
img5 = cv2.imread("../Images/img5.jpg", 0)

# img_crop = img[y_inicial:y_final, x_inicial:x_final]

images = [img1, img2, img3, img4, img5]
images_croped = []

for img in images:
    images_croped.append(img[260:560, 1:689])

io.imshow_collection(images_croped)

# 3 b)
result = np.median(images_croped, axis=0)
plt.figure()
plt.title("Media das imagens!")
plt.imshow(result)

# 3 c)
# img_final = cv2.bitwise_xor(result, images_croped[0], mask=None)
img_final = result - images_croped[0]
# img_final = cv2.medianBlur(img_final, 3)
print(f"{images_croped[0].shape}")
print(f"{result.shape}")

plt.figure()
plt.title("6!")
plt.imshow(img_final)
io.show()
