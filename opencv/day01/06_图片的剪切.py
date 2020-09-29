#encoding: utf-8
import cv2 as cv

img = cv.imread("../img/lena.jpg")

# 利用python的切片功能进行截取 img[起始行号：结束行号,起始列号：结束列号]
dst = img[180:250,180:310]

# 显示图像


cv.imshow("src",img)
for col in range(130):
    dst[35,col] = (0,0,255)
cv.imshow("dst",dst)
cv.imshow("src1",img);

cv.waitKey(0)
