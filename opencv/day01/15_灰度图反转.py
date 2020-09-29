#encoding: utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/itheima.jpg")
height,width = src.shape[0:2]
grayImg = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.imshow("gray1",grayImg)
# 100 ---> 255 - 100 = 155
for row in range(height):
    for col in range(width):
        value = grayImg[row,col]
        grayImg[row,col] = 255 - value;

cv.imshow("gray2",grayImg)
cv.imshow("src",src)
cv.waitKey()
