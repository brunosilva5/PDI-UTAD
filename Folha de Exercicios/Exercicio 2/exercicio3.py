import cv2
import matplotlib.pyplot as plt

img_ex3 = cv2.imread("../Imagens/irina.jpg")
img_ex31 = cv2.imread("../Imagens/cristiano.jpg")
img_concat = cv2.hconcat([img_ex3, img_ex31])

img_concat = cv2.cvtColor(img_concat, cv2.COLOR_BGR2RGB)

plt.imshow(img_concat)
plt.show()
