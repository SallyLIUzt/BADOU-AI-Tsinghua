# nearest interpolation
import numpy as np
import cv2 as cv
def function(img):
    height, width, channels = img.shape
    img_nip = np.zeros((1000,1000,channels), dtype=img.dtype) #建立三通道1000*1000的0值array
    for i in range(1000):
        for j in range(1000):
            x = int(i*height/1000) #取样原图行坐标
            y = int(j*width/1000) #取样原图列坐标
            img_nip[i,j] = img[x,y] #完成量化
    return img_nip

img = cv.imread("lenna.png")
zoom = function(img)
print(zoom)
print(zoom.shape)
cv.imshow("nip", zoom)
cv.imshow("orginal", img)
cv.waitKey(0)