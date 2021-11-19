import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../Imagens/bolas.jpg", 0)

img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

plt.title("Original image")
plt.imshow(img)

circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    1,
    20,
    param1=100,
    param2=30,
    minRadius=1,
    maxRadius=30,
)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 2)


plt.figure()
plt.title("Hough Circles Transfom")
plt.imshow(cimg)
plt.show()
