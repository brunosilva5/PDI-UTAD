import cv2
from skimage.filters import unsharp_mask
from skimage import io

img = cv2.imread("../Imagens/moon.tif", 0)
# Unsharp with skimage
# img_unsharped = unsharp_mask(img, radius=1, amount=1)
img_unsharped2 = unsharp_mask(img, radius=5, amount=2)

# subtract = cv2.subtract(img_unsharped2, img)
# subtract = img - img_unsharped2

# gaussian_3 = cv2.GaussianBlur(img, (0, 0), 2.0)
# unsharp_image = cv2.addWeighted(img_ex7, 1.5, gaussian_3, -0.5, 0, img_ex7)


# Calculate the Laplacian
lap = cv2.Laplacian(img, cv2.CV_64F)

# Calculate the sharpened image
a = 0.7
sharp_image = img - a * lap

images = [img, img_unsharped2, sharp_image]
io.imshow_collection(images)
io.show()
