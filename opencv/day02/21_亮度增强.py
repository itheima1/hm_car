#encoding:utf-8

import cv2 as cv
import matplotlib.pyplot as plt

src = cv.imread("../img/itheima.jpg")
height,width = src.shape[0:2]


offset=40
cv.imshow("src1",src)
for row in range(height):
    for col in range(width):
        b,g,r = src[row,col]

        # 增加亮度
        b = b + offset
        g = g + offset
        r = r + offset

        if b > 255: b = 255;
        if g > 255: g = 255;
        if r > 255: r = 255;

        src[row,col] = (b,g,r)

cv.imshow("src2",src)

# 计算图像直方图
hist = cv.calcHist([src],[0],None,[256],[0,255])
print hist
plt.plot(hist)
plt.show()
cv.waitKey()