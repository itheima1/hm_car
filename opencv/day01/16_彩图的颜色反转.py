#encoding: utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/itheima.jpg")
height,width = src.shape[0:2]

# 创建画布
dst = np.zeros_like(src);

for row in range(height):
    for col in range(width):
        b,g,r = src[row,col];

        dst[row,col] = (255-b,255-g,255-r);


cv.imshow("src",src)
cv.imshow("dst",dst)
cv.waitKey()