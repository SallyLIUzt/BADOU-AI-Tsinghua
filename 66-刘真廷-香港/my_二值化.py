import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from skimage.color import rgb2gray
img_gray = rgb2gray(cv.imread("lenna.png"))
img_binary = np.where(img_gray >= 0.5,1, 0)

plt.subplot(111)
plt.imshow(img_binary, cmap='gray')
plt.show()

