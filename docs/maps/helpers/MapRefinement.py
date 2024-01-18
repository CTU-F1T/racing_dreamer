import cv2
from PIL import Image
import numpy as np

im = cv2.imread("../maps/ral_experiment_2.pgm", 0)

ret = (im > 200) * 255

background = np.zeros((2000, 2000), int)

w_diff = background.shape[0] - im.shape[0]
h_diff = background.shape[1] - im.shape[1]
background[w_diff // 2: w_diff // 2 + ret.shape[0], h_diff // 2: h_diff // 2 + ret.shape[1]] = ret

Image.fromarray(np.uint8(background)).save('../maps/ral_experiment_2_bin.pgm')

# a = np.ones((5, 5))
# b = np.zeros((10, 10))
# b[2:7, 2:7] = a
# print(b)
