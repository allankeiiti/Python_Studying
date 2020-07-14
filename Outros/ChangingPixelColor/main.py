from PIL import Image
import numpy as np
import time
start_time = time.time()
print(start_time)

# Source: https://stackoverflow.com/questions/48279745/create-image-from-rgb-list-with-pillow-and-python-3

# Abrindo a foto
photo_dir = 'amazing-spider-man-andrew-garfield-image.jpg'
im = Image.open(photo_dir, mode='r')

# Recolhendo dimensões da foto
dimensions = im.size

# Gerando um array de n0 = Altura com n1 = Coluna arrays com 3 valores cada
image_np = np.asarray(im)

# A linha abaixo permite que o array seja modificado
image_np = image_np.copy()

red_rgb = [[255, 160, 122], [250, 128, 114], [233, 150, 122], [240, 128, 128], [205, 92, 92],
           [220, 20, 60], [178, 34, 34], [255, 0, 0], [139, 0, 0], [128, 0, 0],
           [255, 99, 71], [255, 69, 0], [219, 112, 147]]

black_rgb = [[46, 46, 46], [65, 65, 65], [63, 63, 63], [101, 101, 101], [65, 65, 65],
             [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
             [0, 0, 0], [0, 0, 0], [93, 93, 93]]

red_rgb = [[255, 160, 122, 255], [250, 128, 114, 255], [233, 150, 122, 255], [240, 128, 128, 255], [205, 92, 92, 255],
           [220, 20, 60, 255], [178, 34, 34, 255], [255, 0, 0, 255], [139, 0, 0, 255], [128, 0, 0, 255],
           [255, 99, 71, 255], [255, 69, 0, 255], [219, 112, 147, 255]]

black_rgb = [[46, 46, 46, 255], [65, 65, 65, 255], [63, 63, 63, 255], [101, 101, 101, 255], [65, 65, 65, 255],
             [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255],
             [0, 0, 0, 255], [0, 0, 0, 255], [93, 93, 93, 255]]



# image_np[0][0] = np.array([255, 255, 255], dtype='uint8')

index = 0
for red_color in red_rgb:
    for i in range(len(image_np)):
        for j in range(len(image_np[0])):
            # image_np[i][j] = np.delete(image_np[i][j], 3)
                if list(image_np[i][j]) == red_color or (image_np[i][j][0] > image_np[i][j][1] and
                                                         image_np[i][j][0] > image_np[i][j][2]):
                    image_np[i][j] = np.asarray(black_rgb[index], dtype='uint8')
index += 1

image_np = bytes(image_np)
img = Image.frombytes('RGBA', dimensions, image_np)
img.show()
img.save('teste.png')
print("--- %s seconds ---" % (time.time() - start_time))
