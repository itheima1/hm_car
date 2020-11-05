#encoding:utf-8
import cv2 as cv

src = cv.imread("../img/itheima_salt.jpg")

# 中值滤波
dst = cv.medianBlur(src, 5)


cv.imshow("src",src)
cv.imshow("dst",dst)
cv.waitKey()
