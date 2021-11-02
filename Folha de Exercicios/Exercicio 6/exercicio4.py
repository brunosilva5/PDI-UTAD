import cv2
import matplotlib.pyplot as plt
from skimage import exposure
import numpy as np
import time

k = 3

img = cv2.imread("../Imagens/fce_clara.bmp", 0)

plt.imshow(img, "gray")

start1 = time.time()
table = np.array([pow(img, k) for img in range(0, 256)], dtype="uint8")

img_transformation = cv2.LUT(img, table)
end1 = time.time()

lut = {}

start2 = time.time()
new_img = img.copy()
i = 0

for y in range(new_img.shape[0]):
    for x in range(new_img.shape[1]):
        pixel_value = img[y, x]
        if pixel_value not in lut:

            lut[pixel_value] = pow(pixel_value, k)
            i += 1
        new_img[y, x] = lut[pixel_value]

end2 = time.time()


print(end1 - start1)
print(end2 - start2)

print("Called pow ", i, " times")
from skimage import io

io.imshow_collection([img_transformation, new_img.astype("int32")])
io.show()

print((new_img == img_transformation).all())
