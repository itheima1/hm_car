#encoding:utf-8
import cv2 as cv
import numpy as np

src = cv.imread("../img/itheima.jpg")

# 将彩图转成灰度图
grayImg = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
height,width = src.shape[0:2]

# 创建一个空白的矩阵 ， 画布
dst = np.zeros_like(grayImg)

for row in range(height):
    for col in range(width - 1):
        # 计算相邻两个像素的差值 ， 水平方向
        gray0 = grayImg[row,col]
        gray1 = grayImg[row,col+1]

        # 计算相邻像素的梯度 uint8 0-255
        value = int(gray0) - int(gray1) + 120

        if value < 0:
            value = -value
        # 将计算出来的值填充一个新的画布中
        dst[row,col] = value



cv.imshow("src",src)
cv.imshow("dst",dst)
cv.imshow("gray",grayImg)
cv.waitKey()
