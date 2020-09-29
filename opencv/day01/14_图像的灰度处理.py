#encoding: utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/lena.jpg")
height,width = src.shape[0:2]

# 创建一个画布  0-255 + 0-255
dst = np.zeros((height,width,1),np.uint8)

for row in range(height):
    for col in range(width):
        b,g,r = src[row,col]
        # gray = (int(b) + int(g) + int(r))/3
        # 0.299∗color.r + 0.587∗color.g + 0.114∗color.b
        gray = int(b)*0.114 + int(g)*0.587 + int(r)*0.299
        # 将计算出来的灰度值填充到画布中
        dst[row,col] = gray

cv.imshow("dst",dst)
cv.waitKey()
