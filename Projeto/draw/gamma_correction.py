import numpy as np
import cv2

x = "./IMG_2192.JPG"  # location of the image
original = cv2.imread(x, 1)

lookUpTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookUpTable[0, i] = np.clip(pow(i / 255.0, 0.6) * 255.0, 0, 255)
res = cv2.LUT(original, lookUpTable)
# cv2.imshow("gammam image 1", res)
res = cv2.GaussianBlur(res, (3, 3), 1)
cv2.imwrite("2192.JPG", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
