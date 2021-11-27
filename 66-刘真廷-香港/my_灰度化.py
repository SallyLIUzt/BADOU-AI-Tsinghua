# 灰度化
import cv2 as cv
import numpy as np
img = cv.imread("lenna.png")
width, height, channels = img.shape
gray_img = np.zeros((width, height), dtype = img.dtype)
for i in range(width):
    for j in range(height):
        gray_img[i,j] = img[i, j][0]*0.11 + img[i, j][1]*0.59 + img[i,j][2]*0.3
print(gray_img)
cv.imshow("gray_img",gray_img)
print("完成灰度化")
cv.waitKey(0)

# 第二种方法
img_gray = rgb2gray(cv.imread("lenna.png"))
plt.subplot(221)
plt.imshow(img_gray, cmap = 'gray')
plt.show()
print("---image gray----")
print(img_gray)