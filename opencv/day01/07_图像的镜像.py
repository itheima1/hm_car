#encoding: utf-8
import cv2 as cv
import numpy as np

# 创建两倍原图的大小的画布出来
img = cv.imread("../img/lena.jpg")
#  获取图像尺寸
print img.shape
height = img.shape[0]
width = img.shape[1]
print height,width

dst = np.zeros((height * 2, width, 3), np.uint8)



for row in range(height):
    for col in range(width):
        dst[row,col] = img[row,col]

        dst[height*2 - row - 1,col] = img[row,col]

    # cv.imshow("dst", dst)
    # cv.waitKey(50)

cv.imshow("img",img)
cv.imshow("dst",dst)

cv.waitKey(0)
