import matplotlib.pyplot as plt

img_tif = plt.imread(fname="Imagens/Retina.tif")
height, width, channels = img_tif.shape
number_of_pixels = height * width * channels
print(f"Altura: {height} | Largura: {width} | Número de pixels: {number_of_pixels}")
plt.imshow(img_tif)
plt.show()
