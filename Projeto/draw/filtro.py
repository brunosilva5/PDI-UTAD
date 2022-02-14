import cv2
import numpy as np


def adjust_gamma(image, gamma=1.0):

    invGamma = 1.0 / gamma
    table = np.array(
        [((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]
    ).astype("uint8")

    return cv2.LUT(image, table)


x = "./IMG_2197.JPG"  # location of the image
original = cv2.imread(x, 1)
cv2.imshow("original", original)

gamma = 2.5  # change the value here to get different result
adjusted = adjust_gamma(original, gamma=gamma)
cv2.imshow("gammam image 1", adjusted)
cv2.imwrite("2070gamma.JPG", adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
