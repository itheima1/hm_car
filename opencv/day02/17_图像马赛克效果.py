#encoding:utf-8
import cv2 as cv
import numpy as np

src = cv.imread('../img/itheima.jpg')
height,width = src.shape[0:2]
# 将图像划分成若干个4*4的小方块，
# 每一个小方块里面的所有像素值修改为和第一个像素块的颜色一样

offset = 10;
for row in range(160,240):
    for col in range(380,670):
        # 将图像划分成若干个4*4的小方块，
        if row%offset == 0 and col%offset == 0:
            # 获取当前位置的颜色快
            color = src[row,col]
            # 每一个小方块里面的所有像素值修改为和第一个像素块的颜色一样
            for i in range(offset):
                for j in range(offset):
                    src[row+i,col+j] = color

cv.imshow("src",src)
cv.waitKey()
