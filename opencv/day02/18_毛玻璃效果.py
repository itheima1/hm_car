#encoding: utf-8
import cv2 as cv
import numpy as np
import random

src = cv.imread("../img/itheima.jpg")
height,width = src.shape[0:2]

offset = 10;
# 创建一个和原图同样大小的画布
dst = np.zeros_like(src)

# 处理每一个像素
for row in range(height):
    for col in range(width):
        # 计算当前位置，周围的一个随机数
        # index = random.randint(0,offset);
        # 随机的行号
        randomRow = row + random.randint(0,offset)
        # 随机的列号
        randomCol = col + random.randint(0,offset)

        if randomRow > height -1 :
            randomRow = height - 1;

        if randomCol > width - 1:
            randomCol = width - 1;
        # 获取随机的周围颜色值
        color = src[randomRow,randomCol]

        # 填充到画布中
        dst[row,col] = color;

cv.imshow("dst",dst)
cv.imshow("src",src)
cv.waitKey()