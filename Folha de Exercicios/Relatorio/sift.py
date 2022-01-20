import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("igreja3.jpg")
img2 = cv2.imread("igreja4.jpg")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1 = cv2.GaussianBlur(img1, (3, 3), 0)
img2 = cv2.GaussianBlur(img2, (3, 3), 0)

sift = cv2.SIFT_create()

# Feature Matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

keypoints_1, descriptor_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptor_2 = sift.detectAndCompute(img2, None)

matches = bf.match(descriptor_1, descriptor_2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(
    img1, keypoints_1, img2, keypoints_2, matches[:100], img2, flags=2
)


plt.imshow(img3)
# plt.savefig("sift_match.jpg")
plt.show()
